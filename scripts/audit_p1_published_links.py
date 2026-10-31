#!/usr/bin/env python3
"""Read-only raw-HTML audit of the 13 known P1 public sample pages.

This script inspects THIRD-PARTY example links, not the user's acquired backlinks.
No registration, posting, paid APIs, broad crawling or inferred link equity.
"""
import argparse
import csv
import sys
from datetime import datetime, timezone
from pathlib import Path

from verify_published_backlink import fetch_public_html, inspect_html, validate_https_url

REPO = Path(__file__).resolve().parent.parent
DEFAULT_MATRIX = REPO / "data" / "v47-current-p1-outbound-proof-matrix-20261031.csv"
DEFAULT_REPORT = REPO / "p1-public-example-live-audit.csv"
HEADERS = [
    "source_id", "platform", "public_example_page", "expected_third_party_href",
    "status", "final_page_url", "matched_href", "live_raw_rel",
    "live_rel_classification", "historical_rel_not_current_proof",
    "checked_utc", "method", "note",
]


def read_matrix(path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    required = {"编号", "P1平台", "已刊登公开页", "实际上可见站外href", "原HTML rel历史样本"}
    if not rows or len(rows) != 13 or any(not required.issubset(row) for row in rows):
        raise ValueError("Expected exactly 13 P1 sources with V47 evidence columns")
    ids = [row["编号"] for row in rows]
    if len(set(ids)) != 13:
        raise ValueError("Duplicate source IDs in public-sample matrix")
    return rows


def audit_rows(rows, fetcher=fetch_public_html, timeout=12.0, max_requests=13):
    """Inspect one explicitly recorded example URL per platform; never discover/crawl more."""
    output = []
    requested = 0
    for row in rows:
        source = row["已刊登公开页"].strip()
        target = row["实际上可见站外href"].strip()
        historical = row["原HTML rel历史样本"].strip()
        entry = {
            "source_id": row["编号"], "platform": row["P1平台"],
            "public_example_page": source,
            "expected_third_party_href": target,
            "status": "", "final_page_url": "",
            "matched_href": "", "live_raw_rel": "",
            "live_rel_classification": "",
            "historical_rel_not_current_proof": historical,
            "checked_utc": datetime.now(timezone.utc).isoformat(),
            "method": "read_only_raw_html_anchor_exact_match",
            "note": "",
        }
        if not source or not target:
            entry["status"] = "no_verifiable_public_sample"
            entry["note"] = "No sample URL/href; not evidence that the platform never links out."
        elif requested >= max_requests:
            entry["status"] = "not_scanned_limit"
            entry["note"] = "User-selected request cap; not an absence-of-link result."
        else:
            requested += 1
            try:
                validate_https_url(source)
                validate_https_url(target)
                html, final = fetcher(source, timeout)
                entry["final_page_url"] = final
                result = inspect_html(html, final, target, match="exact")
                if result["status"] == "found":
                    entry["status"] = "found_in_live_raw_html"
                    entry["matched_href"] = " | ".join(link["href"] for link in result["links"])
                    entry["live_raw_rel"] = " | ".join(link["rel"] for link in result["links"])
                    entry["live_rel_classification"] = " | ".join(
                        link["rel_result"] for link in result["links"]
                    )
                    entry["note"] = (
                        "Only other sites' published examples; no claim of a backlink "
                        "to generadordelettering.org, indexation or ranking benefit."
                    )
                else:
                    entry["status"] = "not_found_in_fetched_raw_html"
                    entry["note"] = (
                        "Not present in fetched static HTML; JavaScript rendering, alternate "
                        "pages, robots/indexation and later approval are not evaluated."
                    )
            except Exception as exc:
                entry["status"] = "fetch_or_validation_error"
                entry["note"] = (type(exc).__name__ + ": " + str(exc))[:300]
        output.append(entry)
    return output


def write_report(path, rows):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    # Avoid formula injection when viewing untrusted remote hrefs/notes in Excel.
    def safe_cell(value):
        value = str(value or "")
        if value.lstrip().startswith(("=", "+", "-", "@")):
            return "'" + value
        return value
    with path.open("w", encoding="utf-8-sig", newline="") as out:
        writer = csv.DictWriter(out, fieldnames=HEADERS)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: safe_cell(row.get(field, "")) for field in HEADERS})


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Check up to 13 published THIRD-PARTY examples for raw a[href] and rel. Free, read-only."
    )
    ap.add_argument("--matrix", type=Path, default=DEFAULT_MATRIX)
    ap.add_argument("--output", type=Path, default=DEFAULT_REPORT)
    ap.add_argument("--timeout", type=float, default=12)
    ap.add_argument("--max-requests", type=int, default=13,
                    help="0=preview only; at most 13 single-page fetches")
    args = ap.parse_args(argv)
    if not 0 <= args.max_requests <= 13 or not 1 <= args.timeout <= 30:
        ap.error("max-requests must be 0..13 and timeout must be 1..30 seconds")
    try:
        records = read_matrix(args.matrix)
        output = audit_rows(records, timeout=args.timeout, max_requests=args.max_requests)
        write_report(args.output, output)
        counts = {state: sum(row["status"] == state for row in output)
                  for state in sorted(set(row["status"] for row in output))}
        print("P1 THIRD-PARTY example audit (not acquired backlinks):")
        for state, n in counts.items():
            print(f"  {state}: {n}")
        print(f"CSV report: {args.output}")
        print("Historical rel is separate from current raw rel. No ranking/index guarantees.")
        return 0
    except Exception as exc:
        print("Audit failed; no link verification claim: " + str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
