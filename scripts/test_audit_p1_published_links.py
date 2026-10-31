#!/usr/bin/env python3
"""Offline regression tests for the free 13-source raw-rel audit."""
import csv
import tempfile
import unittest
from pathlib import Path

from audit_p1_published_links import audit_rows, read_matrix, write_report


def row(id_, source, href, rel="未知/无法从清理后的HTML确认"):
    return {
        "编号": str(id_), "P1平台": "Example " + str(id_),
        "已刊登公开页": source,
        "实际上可见站外href": href,
        "原HTML rel历史样本": rel,
    }


class BatchAuditTests(unittest.TestCase):
    def test_no_sample_does_not_fetch_or_claim_no_links(self):
        calls = []
        def fake_fetch(source, timeout):
            calls.append(source)
            raise AssertionError("Must not fetch missing samples")
        result = audit_rows([row(2, "", "")], fetcher=fake_fetch)
        self.assertEqual(result[0]["status"], "no_verifiable_public_sample")
        self.assertEqual(calls, [])

    def test_raw_comma_rel_distinct_from_historical_rel(self):
        url = "https://directory.public.org/tool/fancy"
        href = "https://fancytools.org/?ref=directory"
        def fake_fetch(source, timeout):
            self.assertEqual(source, url)
            return ('<a href="' + href + '" rel="nofollow,ugc">Visit</a>', url)
        result = audit_rows([row(123, url, href, "noopener")], fetcher=fake_fetch)
        self.assertEqual(result[0]["status"], "found_in_live_raw_html")
        self.assertEqual(result[0]["live_raw_rel"], "nofollow,ugc")
        self.assertEqual(result[0]["live_rel_classification"], "nofollow+ugc")
        self.assertEqual(result[0]["historical_rel_not_current_proof"], "noopener")

    def test_query_string_and_hostname_must_match(self):
        url = "https://directory.public.org/tool/x"
        wanted = "https://fancytools.org/?ref=pepliohub"
        def fake_fetch(source, timeout):
            return ('<a href="https://fancytools.org/?ref=unrelated" rel="noopener">Wrong campaign</a>'
                    '<a href="https://fancytools.org.evil.net/?ref=pepliohub">Spoof</a>', url)
        result = audit_rows([row(149, url, wanted)], fetcher=fake_fetch)
        self.assertEqual(result[0]["status"], "not_found_in_fetched_raw_html")
        self.assertEqual(result[0]["live_raw_rel"], "")

    def test_fetch_error_is_never_recorded_as_missing(self):
        def fake_fetch(source, timeout):
            raise TimeoutError("Timed out")
        result = audit_rows([row(123, "https://directory.public.org/x",
                                 "https://fancytools.org/")], fetcher=fake_fetch)
        self.assertEqual(result[0]["status"], "fetch_or_validation_error")
        self.assertIn("TimeoutError", result[0]["note"])

    def test_limited_batch_labels_skipped_items(self):
        url1 = "https://directory.public.org/x"
        url2 = "https://directory.public.org/y"
        def fake_fetch(source, timeout):
            return ('<a href="https://fancytools.org/">OK</a>', source)
        x = audit_rows([row(1, url1, "https://fancytools.org/"),
                        row(2, url2, "https://fancytools.org/")],
                       fetcher=fake_fetch, max_requests=1)
        self.assertEqual([r["status"] for r in x],
                         ["found_in_live_raw_html", "not_scanned_limit"])

    def test_report_escapes_excel_formula_values(self):
        with tempfile.TemporaryDirectory() as td:
            output = Path(td) / "report.csv"
            record = audit_rows([row(2, "", "")])[0]
            record["platform"] = '=HYPERLINK("http://bad.test")'
            write_report(output, [record])
            with output.open(encoding="utf-8-sig", newline="") as f:
                saved = list(csv.DictReader(f))
            self.assertTrue(saved[0]["platform"].startswith("'=HYPERLINK"))

    def test_canonical_v47_has_thirteen_unique_sources(self):
        rows = read_matrix(Path(__file__).resolve().parent.parent / "data" /
                           "v47-current-p1-outbound-proof-matrix-20261031.csv")
        self.assertEqual(len(rows), 13)
        self.assertEqual(sum(bool(r["已刊登公开页"]) for r in rows), 11)


if __name__ == "__main__":
    unittest.main()
