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
EDITORIAL = ROOT / "data/editorial-prospects.csv"
EDITORIAL_CONTACTS = ROOT / "data/editorial-outreach-ledger.csv"
SHORTLIST = ROOT / "data/reusable-free-shortlist.csv"

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
    if len(catalog) < 154:
        fail(f"V19 baseline has 154 rows; catalog unexpectedly shrank to {len(catalog)}.")

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


    headers_e, editorial = read(EDITORIAL)
    required_e = ["编号", "媒体/域名", "官方联系入口", "执行状态", "是否可保证链接"]
    for key in required_e:
        if key not in headers_e:
            fail(f"Missing editorial prospect column: {key}")
    if len(editorial) < 4:
        fail("V18 baseline requires at least four editorial prospects.")
    editorial_ids = [r["编号"].strip() for r in editorial]
    if len(set(editorial_ids)) != len(editorial_ids):
        fail("Duplicate editorial prospect IDs.")
    if any("保证" not in (r["是否可保证链接"] or "") for r in editorial):
        fail("Editorial prospects must explicitly state that a backlink is not guaranteed.")

    headers_o, outreach = read(EDITORIAL_CONTACTS)
    required_o = ["目标网站", "目标媒体", "收件公开地址", "发送日期", "邮件主题", "接触状态"]
    for key in required_o:
        if key not in headers_o:
            fail(f"Missing editorial outreach ledger column: {key}")
    if len(outreach) < 2:
        fail("V18 baseline requires the two pre-existing sent outreach records.")
    contacts_seen = set()
    for r in outreach:
        target = registered_domain_hint(r["目标网站"])
        media = registered_domain_hint(r["目标媒体"])
        if not target or not media:
            fail("Editorial outreach requires valid target and publisher domains.")
        k = (target, media, r["邮件主题"].strip())
        if k in contacts_seen:
            fail(f"Duplicate editorial outreach record: {k}")
        contacts_seen.add(k)
        if not r["发送日期"].strip():
            fail(f"Outreach marked as sent lacks date: {k}")


    headers_s, shortlist = read(SHORTLIST)
    for key in ["排序", "渠道根域名", "平台名称", "免费提交已证实",
                "强制反向徽章", "真实Rel实测", "实时DR/AS实测",
                "最新官方依据", "状态与下一步", "提交状态"]:
        if key not in headers_s:
            fail(f"Missing reusable shortlist column: {key}")
    if len(shortlist) < 8:
        fail("V19 shortlist must preserve at least eight qualified research candidates.")
    shortlist_domains = [registered_domain_hint(r["渠道根域名"]) for r in shortlist]
    if not all(shortlist_domains):
        fail("Reusable shortlist has an empty domain.")
    if len(set(shortlist_domains)) != len(shortlist_domains):
        fail("Reusable shortlist must have unique platform domains.")
    if any(not r["最新官方依据"].strip() for r in shortlist):
        fail("All shortlisted channels need an evidence source.")

    priorities = Counter(r["优先级"].strip() for r in catalog)
    print(f"OK: {len(catalog)} catalog entries, {len(queue)} priority targets, {len(ledger)} directory ledger rows.")
    print(f"Editorial: {len(editorial)} prospects, {len(outreach)} historical outreach records.")
    print(f"Strict free-first shortlist: {len(shortlist)} distinct channels; actual Follow/DR not guaranteed.")
    print("Priority labels:", ", ".join(f"{k}={v}" for k, v in sorted(priorities.items())))
    print("Note: This verifies data integrity, NOT link quality, DR, rel or indexation.")

if __name__ == "__main__":
    main()
