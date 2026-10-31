#!/usr/bin/env python3
"""Bounded, read-only raw-HTML check of V52 curated third-party examples.

This is NOT an acquired-backlink check for generadordelettering.org.
Only published pages and external destinations explicitly in the evidence CSV
are requested. No submissions, logins, crawling, paid APIs or site changes.
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MATRIX = ROOT / "data" / "v52-curated-published-anchor-metadata-20261031.csv"
DEFAULT_OUTPUT = ROOT / "v52-curated-live-raw-anchor-audit.csv"
FIELDS = {
    "source_id", "platform", "public_example_page", "observed_third_party_href",
    "historical_rel_not_current_proof",
}
EXPECTED_IDS = {"159", "164", "151", "123", "75", "148", "163", "165", "172"}


def read_matrix(path: Path) -> list[dict[str, str]]:
    """Convert nine curated V52 rows to the existing V49 verifier's schema."""
    with path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        if not reader.fieldnames or not FIELDS.issubset(reader.fieldnames):
            raise ValueError("V52 matrix is missing required evidence columns")
        rows = list(reader)
    if len(rows) != 9 or {r["source_id"].strip() for r in rows} != EXPECTED_IDS:
        raise ValueError("V52 expects nine unique known existing source IDs")
    converted = []
    for row in rows:
        source = (row["public_example_page"] or "").strip()
        target = (row["observed_third_party_href"] or "").strip()
        if not source or not target:
            raise ValueError("V52 rows must have independently observed source and destination")
        converted.append({
            "编号": row["source_id"].strip(),
            "P1平台": row["platform"].strip(),  # Legacy adapter; P2 rows stay P2.
            "已刊登公开页": source,
            "实际上可见站外href": target,
            "原HTML rel历史样本": (row["historical_rel_not_current_proof"] or "").strip(),
        })
    return converted


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description="Read-only audit of exactly nine curated third-party href/rel examples."
    )
    ap.add_argument("--matrix", type=Path, default=MATRIX)
    ap.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    ap.add_argument("--max-requests", type=int, default=9,
                    help="0=offline preview; 1..9 = maximum public pages fetched")
    ap.add_argument("--timeout", type=float, default=12.0)
    args = ap.parse_args(argv)
    if not 0 <= args.max_requests <= 9 or not 1 <= args.timeout <= 30:
        ap.error("max-requests must be 0..9 and timeout must be 1..30 seconds")
    try:
        from audit_p1_published_links import audit_rows, write_report

        rows = read_matrix(args.matrix)
        result = audit_rows(rows, timeout=args.timeout, max_requests=args.max_requests)
        # Existing bounded verifier: public HTTPS only, DNS validation, <=2 MB,
        # <=5 redirects, exact href including query; raw rel separate from history.
        write_report(args.output, result)
        counts = {status: sum(item["status"] == status for item in result)
                  for status in sorted({item["status"] for item in result})}
        print("V52 public examples only: NOT the user's own acquired backlinks.")
        for status, n in counts.items():
            print(f"  {status}: {n}")
        print(f"Report: {args.output}")
        print("Semantic href / robots / canonical != live raw rel or Google indexing.")
        return 0
    except Exception as exc:
        print(f"V52 audit failed; no new link claim: {type(exc).__name__}: {exc}",
              file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
