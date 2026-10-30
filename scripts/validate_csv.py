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
AUDIT = ROOT / "data/v22-link-evidence-audit.csv"
ACTIONABLE = ROOT / "data/actionable-applications-v22.csv"
EDUCATION = ROOT / "data/education-resource-submissions.csv"
V23 = ROOT / "data/v23-design-submission-check.csv"
V24 = ROOT / "data/v24-curated-submission-audit.csv"
V25 = ROOT / "data/v25-spanish-resource-evidence.csv"

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
    if len(catalog) < 171:
        fail(f"V25 baseline has 171 rows; catalog unexpectedly shrank to {len(catalog)}.")

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
    if len(editorial) < 5:
        fail("V22 baseline requires at least five editorial prospects.")
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
    if len(shortlist) < 10:
        fail("V21 shortlist must preserve at least ten qualified research candidates.")
    shortlist_domains = [registered_domain_hint(r["渠道根域名"]) for r in shortlist]
    if not all(shortlist_domains):
        fail("Reusable shortlist has an empty domain.")
    if len(set(shortlist_domains)) != len(shortlist_domains):
        fail("Reusable shortlist must have unique platform domains.")
    if any(not r["最新官方依据"].strip() for r in shortlist):
        fail("All shortlisted channels need an evidence source.")
    master_names = chr(10).join(
        " ".join((r["平台/域名"], r["提交入口URL"], r["官方来源URL"])).lower()
        for r in catalog
    )
    for platform in shortlist_domains:
        if platform not in master_names:
            fail(f"Shortlisted platform not found in catalog by domain: {platform}")


    headers_ed, education = read(EDUCATION)
    for key in ["教育资源平台", "渠道根域名", "原始官网资料", "直接公开投稿入口",
                "目标资源URL", "关键版权或身份门槛", "当前状态", "核验日期"]:
        if key not in headers_ed:
            fail(f"Missing education submission column: {key}")
    if len(education) < 3:
        fail("V20 education resource research must preserve at least three entries.")
    e_domains = [registered_domain_hint(r["渠道根域名"]) for r in education]
    if any(not x for x in e_domains) or len(set(e_domains)) != len(e_domains):
        fail("Invalid or duplicate education resource platform domains.")
    if any(not r["关键版权或身份门槛"].strip() or not r["原始官网资料"].strip()
           for r in education):
        fail("Education resources require explicit copyright/identity conditions and source.")


    audit_fields, audit = read(AUDIT)
    for key in ["根域名", "官网提交/资格依据", "第三方rel抽样证据", "V22动作级别"]:
        if key not in audit_fields:
            fail(f"Missing V22 evidence audit column: {key}")
    if len(audit) != 10:
        fail(f"V22 must preserve ten reviewed shortlist sites; got {len(audit)}.")
    audited_domains = [registered_domain_hint(r["根域名"]) for r in audit]
    if len(set(audited_domains)) != 10:
        fail("Duplicate or missing audited platform domains.")
    if set(audited_domains) != set(shortlist_domains):
        fail("V22 audit domains and research shortlist must match.")

    act_fields, active = read(ACTIONABLE)
    for key in ["平台根域名", "当前入口", "当前阻断", "出站Follow实测", "当前申请状态"]:
        if key not in act_fields:
            fail(f"Missing V22 actionable applications column: {key}")
    if len(active) != 6:
        fail(f"V22 initial actionable list must contain six candidates, got {len(active)}.")
    act_domains = [registered_domain_hint(r["平台根域名"]) for r in active]
    if len(set(act_domains)) != 6 or not set(act_domains).issubset(set(audited_domains)):
        fail("Actionable domains must be unique and all come from audited shortlist.")
    if "toptool.io" in act_domains:
        fail("TopTool is paused for new submissions and cannot be called currently actionable.")
    if any(r["当前申请状态"].strip() != "未提交" for r in active):
        fail("Actionable list may not claim submissions without supported ledger evidence.")

    v23_fields, v23 = read(V23)
    for key in ["平台根域名", "官方投稿入口", "官方资格依据", "核验缺口", "真实提交状态"]:
        if key not in v23_fields:
            fail(f"Missing V23 evidence column: {key}")
    if len(v23) < 4:
        fail("V23 must preserve at least three new candidates and the preexisting Enlineados review.")
    v23_domains = [registered_domain_hint(r["平台根域名"]) for r in v23]
    if any(not d for d in v23_domains) or len(set(v23_domains)) != len(v23_domains):
        fail("V23 has an empty or duplicate platform domain.")
    if any(r["真实提交状态"].strip() != "未提交" for r in v23):
        fail("V23 research table cannot claim submitted; record actual actions in submission-ledger.")
    if any(not r["核验缺口"].strip() for r in v23):
        fail("Every V23 source must state evidence gaps.")
    if set(["fountn.design", "uxresources.info", "lds-library.vercel.app", "enlineados.com"]) - set(v23_domains):
        fail("V23 baseline source missing.")
    if not all(str(n) in ids for n in (161, 162, 163)):
        fail("V23 new numbered entries missing from master.")

    v24_fields, v24 = read(V24)
    for key in ["平台根域名", "官方来源", "免费与徽章限制", "阻断或未证实项", "新申请状态"]:
        if key not in v24_fields:
            fail(f"Missing V24 evidence column: {key}")
    if len(v24) != 4:
        fail(f"V24 audit must contain four source records; got {len(v24)}.")
    v24_domains = [registered_domain_hint(r["平台根域名"]) for r in v24]
    if len(set(v24_domains)) != 4 or any(not d for d in v24_domains):
        fail("V24 has duplicate or missing platform domains.")
    if set(v24_domains) != {"unikist.com", "markitnow.net", "dailylaunch.io", "softwarecomoservicio.com"}:
        fail("V24 baseline channels changed unexpectedly.")
    if any(r["新申请状态"].strip() != "未提交" for r in v24):
        fail("V24 research must not claim actual submissions.")
    if any(not r["官方来源"].strip() or not r["阻断或未证实项"].strip() for r in v24):
        fail("V24 channels must preserve source and limitations.")
    if not any("强制" in r["强制互链"] for r in v24 if r["平台根域名"] == "softwarecomoservicio.com"):
        fail("Software Como Servicio reciprocal badge prohibition must stay explicit.")
    if not any("徽章" in r["免费与徽章限制"] for r in v24 if r["平台根域名"] == "dailylaunch.io"):
        fail("DailyLaunch must disclose its badge-based dofollow restriction.")
    if numbers[163:167] != [164,165,166,167]:
        fail("V24 last four catalog IDs must be 164-167.")

    v25_fields, v25 = read(V25)
    for key in ["编号", "根域名", "官网证据", "强制互链", "状态级别", "本轮是否提交"]:
        if key not in v25_fields:
            fail(f"Missing V25 evidence column: {key}")
    if len(v25) != 4:
        fail(f"V25 must contain four new research records, got {len(v25)}.")
    v25_domains = [registered_domain_hint(r["根域名"]) for r in v25]
    if set(v25_domains) != {"herramientasyrecursos.com", "freedesignertools.com", "ghostbyte.dev", "founderomni.com"}:
        fail("V25 new domains changed or duplicated.")
    if any(r["本轮是否提交"].strip() != "未提交" for r in v25):
        fail("V25 research may not claim a submission without ledger evidence.")
    if any(not r["官网证据"].strip() or not r["状态级别"].strip() for r in v25):
        fail("V25 entries require actual official evidence and an actionable status.")
    if numbers[-4:] != [168, 169, 170, 171]:
        fail("V25 IDs must append 168 through 171 without rewriting historical rows.")
    aicatalog=[r for r in catalog if r["编号"] == "109"]
    if len(aicatalog)!=1 or aicatalog[0]["优先级"] != "排除" or "徽章" not in aicatalog[0]["关键限制/拒绝原因"]:
        fail("V25 badge-mandatory AI Webcatalog #109 must remain excluded with official warning.")
    if not any(r["编号"].strip() == "E006" and "bestproductivityresources.com" in r["媒体/域名"]
               for r in editorial):
        fail("V25 LinkedIn-only editorial lead E006 must be preserved, not treated as a directory.")

    priorities = Counter(r["优先级"].strip() for r in catalog)
    print(f"OK: {len(catalog)} catalog entries, {len(queue)} priority targets, {len(ledger)} directory ledger rows.")
    print(f"Editorial: {len(editorial)} prospects, {len(outreach)} historical outreach records.")
    print(f"Strict free-first shortlist: {len(shortlist)} distinct channels; actual Follow/DR not guaranteed.")
    print(f"Education resource platforms: {len(education)} conditional entries; rights/status must be verified.")
    print(f"V22: {len(audit)} audited directory candidates and {len(active)} currently actionable research targets.")
    print(f"V23: {len(v23)} extra evidence records; no real submissions claimed.")
    print(f"V24: {len(v24)} new research records, two current design-submission forms; no submissions claimed.")
    print(f"V25: {len(v25)} evidence records, #109 excluded, E006 editorial lead; no submissions claimed.")
    print("Priority labels:", ", ".join(f"{k}={v}" for k, v in sorted(priorities.items())))
    print("Note: This verifies data integrity, NOT link quality, DR, rel or indexation.")

if __name__ == "__main__":
    main()
