#!/usr/bin/env python3
"""Offline fixture tests for V52 public-example audit. No network requests."""
import csv
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))
from audit_curated_v52 import EXPECTED_IDS, FIELDS, main, read_matrix

HEADERS = list(FIELDS)


class V52CuratedAuditTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.matrix = Path(self.tmp.name) / "matrix.csv"
        self.output = Path(self.tmp.name) / "output.csv"

    def rows(self):
        return [{
            "source_id": key,
            "platform": "Sample " + key,
            "public_example_page": f"https://directory.example.org/example/{key}",
            "observed_third_party_href": f"https://resource.example.org/{key}",
            "historical_rel_not_current_proof": "historical, not current",
        } for key in sorted(EXPECTED_IDS)]

    def write(self, rows, headers=HEADERS):
        with self.matrix.open("w", encoding="utf-8-sig", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(rows)

    def test_valid_nine_rows_are_adapted_for_existing_verifier(self):
        self.write(self.rows())
        got = read_matrix(self.matrix)
        self.assertEqual(len(got), 9)
        self.assertEqual({r["编号"] for r in got}, EXPECTED_IDS)
        self.assertTrue(all(r["原HTML rel历史样本"] == "historical, not current"
                            for r in got))

    def test_duplicate_source_rejected(self):
        rows = self.rows()
        rows[-1]["source_id"] = rows[0]["source_id"]
        self.write(rows)
        with self.assertRaisesRegex(ValueError, "nine unique"):
            read_matrix(self.matrix)

    def test_missing_href_rejected(self):
        rows = self.rows()
        rows[2]["observed_third_party_href"] = ""
        self.write(rows)
        with self.assertRaisesRegex(ValueError, "observed source and destination"):
            read_matrix(self.matrix)

    def test_missing_column_rejected(self):
        rows = self.rows()
        rows = [{k: v for k, v in row.items() if k != "public_example_page"}
                for row in rows]
        self.write(rows, headers=[h for h in HEADERS if h != "public_example_page"])
        with self.assertRaisesRegex(ValueError, "missing required"):
            read_matrix(self.matrix)

    def test_cli_zero_requests_is_explicitly_read_only(self):
        self.write(self.rows())
        stub = types.ModuleType("audit_p1_published_links")
        calls = []

        def fake_audit(rows, **kwargs):
            calls.append(("audit", len(rows), kwargs.get("max_requests")))
            return [{"status": "not_scanned_limit"}] * len(rows)

        def fake_write(path, rows):
            calls.append(("write", str(path), len(rows)))

        stub.audit_rows = fake_audit
        stub.write_report = fake_write
        with patch.dict(sys.modules, {"audit_p1_published_links": stub}):
            code = main(["--matrix", str(self.matrix), "--max-requests", "0",
                         "--output", str(self.output)])
        self.assertEqual(code, 0)
        self.assertEqual(calls, [("audit", 9, 0), ("write", str(self.output), 9)])

    def test_invalid_request_limit_rejected_before_any_fetch(self):
        with self.assertRaises(SystemExit) as cm:
            main(["--max-requests", "10"])
        self.assertEqual(cm.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
