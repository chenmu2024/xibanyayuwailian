#!/usr/bin/env python3
"""Validate the Spanish backlink catalog without paid services or dependencies."""
from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / "data/backlinks-master.csv"
QUEUE = ROOT / "data/priority-queue.csv"
LEDGER = ROOT / "data/submission-ledger.csv"

def read(path: Path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        return reader.fieldnames or [], rows

def fail(msg: str) -> None:
    raise SystemExit(f"ERROR: {msg}")

def registered_domain_hint(url: str) -> str:
    """Safe display-only host extraction; NOT a public-suffix parser."""
    if not url or not url.strip():
        return ""
    u = urlparse(url if "://" in url else "https://" + url)
    return (u.hostname or "").lower().removeprefix("www.")

def main():
    headers, catalog = read(MASTER)
    needed = ["编号", "平台/域名", "优先级", "提交入口URL", "规则核验情况", "官方来源URL"]
    if any(key not in headers for key in needed):
        fail("Missing columns in backlinks-master.csv")
    if len(catalog) < 150:
        fail(f"V17 baseline has 150 rows; catalog unexpectedly shrank to {len(catalog)}.")

    ids = [r["编号"].strip() for r in catalog]
    dup_ids = [k for k, v in Counter(ids).items() if v > 1]
    if dup_ids:
        fail(f"Duplicate record IDs: {dup_ids}")
    if any(not n.isdigit() for n in ids):
        fail("All catalog IDs must be numeric.")
    numbers = [int(n) for n in ids]
    if numbers != list(range(1, len(numbers) + 1)):
        fail("Catalog IDs must be sequential and historical rows must stay in place.")

    bad_entries = [
        r["编号"] for r in catalog
        if not r["平台/域名"].strip() or not r["提交入口URL"].strip()
    ]
    if bad_entries:
        fail(f"Missing platform or submission URLs: {bad_entries}")

    headers_q, queue = read(QUEUE)
    for key in ["优先序", "目标平台", "直接提交网址", "执行状态"]:
        if key not in headers_q:
            fail(f"Missing priority queue column: {key}")
    if len(set(r["优先序"] for r in queue)) != len(queue):
        fail("Priority positions must not repeat.")

    headers_l, ledger = read(LEDGER)
    for key in ["目标网站域名", "外链平台根域名", "提交阶段（未提交/已提交/审核中/已拒绝/已上线）", "公开条目URL"]:
        if key not in headers_l:
            fail(f"Missing submission ledger column: {key}")
    seen = set()
    for r in ledger:
        key = (registered_domain_hint(r["目标网站域名"]), registered_domain_hint(r["外链平台根域名"]))
        if key in seen:
            fail(f"Duplicate submission target/platform pair: {key}")
        seen.add(key)
        stage = r["提交阶段（未提交/已提交/审核中/已拒绝/已上线）"].strip()
        if stage == "已上线" and not r["公开条目URL"].strip():
            fail(f"Approved link has no public URL: {key}")

    priorities = Counter(r["优先级"].strip() for r in catalog)
    print(f"OK: {len(catalog)} catalog entries, {len(queue)} priority targets, {len(ledger)} ledger records.")
    print("Priority labels:", ", ".join(f"{k}={v}" for k, v in sorted(priorities.items())))
    print("Note: This verifies data integrity, NOT link quality, DR, rel or indexation.")

if __name__ == "__main__":
    main()
