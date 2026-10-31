#!/usr/bin/env python3
"""Offline regression checks for V35 backlink verifier (no network requests)."""
import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path

from verify_published_backlink import classify_rel, inspect_html, main, validate_https_url

SOURCE = "https://directory.valid.org/listings/lettering"
TARGET = "https://generadordelettering.org/"
HTML = """<html><body>
<a href="https://generadordelettering.org/editor" rel="noopener noreferrer">Generador</a>
<a href="https://generadordelettering.org/" rel="nofollow ugc">Homepage</a>
<a href="https://generadordelettering.org.evil.com/rel" rel="follow">Spoof</a>
<a href="https://otherwebsite.org/?next=https://generadordelettering.org/" rel="follow">No backlink</a>
<a href="//generadordelettering.org/tools" rel="sponsored">Scheme relative</a>
</body></html>"""


class BacklinkVerifierTests(unittest.TestCase):
    def test_find_only_real_target_hostname(self):
        result = inspect_html(HTML, SOURCE, TARGET)
        self.assertEqual(result["status"], "found")
        self.assertEqual(len(result["links"]), 3)
        self.assertEqual(
            [i["rel_result"] for i in result["links"]],
            ["no_restriction_token_observed", "nofollow+ugc", "sponsored"],
        )
        self.assertEqual(result["scanned_anchor_tags"], 5)

    def test_exact_match(self):
        result = inspect_html(HTML, SOURCE, TARGET, match="exact")
        self.assertEqual(len(result["links"]), 1)
        self.assertEqual(result["links"][0]["href"], TARGET)

    def test_missing_is_limited_to_html(self):
        result = inspect_html('<script>const href="https://generadordelettering.org/"</script>', SOURCE, TARGET)
        self.assertEqual(result["status"], "not_found_in_fetched_html")
        self.assertIn("JS-rendered", result["caveat"])

    def test_html_parser_ignores_plain_text(self):
        result = inspect_html("<p>generadordelettering.org</p>", SOURCE, TARGET)
        self.assertEqual(result["links"], [])

    def test_malformed_anchor_does_not_hide_valid_link(self):
        html = '<a href="http://[">broken</a><a href="https://generadordelettering.org/">valid</a>'
        result = inspect_html(html, SOURCE, TARGET)
        self.assertEqual(result["status"], "found")
        self.assertEqual(len(result["links"]), 1)
        self.assertEqual(result["links"][0]["href"], TARGET)

    def test_inert_html_template_does_not_count_as_a_live_backlink(self):
        html = ('<template><a href="https://generadordelettering.org/">not active</a></template>'
                '<a href="https://generadordelettering.org/editor">live</a>')
        result = inspect_html(html, SOURCE, TARGET)
        self.assertEqual(len(result["links"]), 1)
        self.assertEqual(result["links"][0]["href"], "https://generadordelettering.org/editor")
        only_inert = inspect_html('<template><a href="https://generadordelettering.org/">not active</a></template>', SOURCE, TARGET)
        self.assertEqual(only_inert["status"], "not_found_in_fetched_html")

    def test_valueless_rel_does_not_crash(self):
        result = inspect_html('<a href="https://generadordelettering.org/" rel>valid</a>', SOURCE, TARGET)
        self.assertEqual(result["status"], "found")
        self.assertEqual(result["links"][0]["rel"], "(none)")
        self.assertEqual(result["links"][0]["rel_result"], "no_restriction_token_observed")

    def test_rel_classification(self):
        self.assertEqual(classify_rel("noopener NOFOLLOW sponsored"), "nofollow+sponsored")
        self.assertEqual(classify_rel("ugc,nofollow"), "nofollow+ugc")
        self.assertEqual(classify_rel("noopener,nofollow, sponsored"), "nofollow+sponsored")
        self.assertEqual(classify_rel("noopener\tnofollow,UGC"), "nofollow+ugc")
        self.assertEqual(classify_rel("noopener noreferrer"), "no_restriction_token_observed")
        self.assertEqual(classify_rel(""), "no_restriction_token_observed")

    def test_comma_delimited_rel_in_actual_anchor(self):
        html = '<a href="https://generadordelettering.org/" rel="nofollow,ugc">Direct link</a>'
        result = inspect_html(html, SOURCE, TARGET)
        self.assertEqual(result["status"], "found")
        self.assertEqual(result["links"][0]["rel"], "nofollow,ugc")
        self.assertEqual(result["links"][0]["rel_result"], "nofollow+ugc")

    def test_reject_non_public_urls_and_same_site(self):
        for url in ("http://directory.valid.org/", "https://localhost/", "https://127.0.0.1/",
                    "https://10.0.0.1/", "https://file.example/", "https://user:pass@directory.valid.org/"):
            with self.subTest(url=url), self.assertRaises(ValueError):
                validate_https_url(url)
        with self.assertRaises(ValueError):
            inspect_html(HTML, TARGET, TARGET)

    def test_offline_cli_never_claims_live_fetch(self):
        with tempfile.TemporaryDirectory() as tmp:
            html_path = Path(tmp) / "input.html"
            report_path = Path(tmp) / "result.json"
            html_path.write_text(HTML, encoding="utf-8")
            with contextlib.redirect_stdout(io.StringIO()):
                code = main(["--source", SOURCE, "--target", TARGET, "--html-file", str(html_path),
                             "--output", str(report_path)])
            self.assertEqual(code, 0)
            record = json.loads(report_path.read_text(encoding="utf-8"))
            self.assertEqual(record["mode"], "offline_fixture_not_live_evidence")
            self.assertEqual(record["status"], "found")

    def test_cli_exit_code_one_when_not_found(self):
        with tempfile.TemporaryDirectory() as tmp:
            html_path = Path(tmp) / "input.html"
            html_path.write_text("<html>no link</html>", encoding="utf-8")
            with contextlib.redirect_stdout(io.StringIO()):
                code = main(["--source", SOURCE, "--target", TARGET, "--html-file", str(html_path)])
            self.assertEqual(code, 1)


if __name__ == "__main__":
    unittest.main()
