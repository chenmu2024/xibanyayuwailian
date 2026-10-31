#!/usr/bin/env python3
"""Read-only, free, bounded public-page backlink verifier. No API keys."""
import argparse
import ipaddress
import json
import socket
import sys
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit, urlunsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

MAX_BYTES = 2_000_000
LIMIT = 15


def validate_https_url(url, resolve=False):
    parts = urlsplit(url)
    host = (parts.hostname or "").lower().rstrip(".")
    if parts.scheme != "https" or not host or "." not in host or parts.username or parts.password:
        raise ValueError("Only public HTTPS URLs without credentials are allowed")
    if parts.port not in (None, 443):
        raise ValueError("Only HTTPS port 443 is allowed")
    if any(c in url for c in ("\n", "\r", "\t", "\\")):
        raise ValueError("Control characters or backslashes are not allowed")
    if host.endswith((".local", ".internal", ".localhost", ".test", ".invalid", ".example")):
        raise ValueError("Private/reserved hostnames are not allowed for live fetches")
    try:
        addr = ipaddress.ip_address(host.strip("[]"))
    except ValueError:
        addr = None
    if addr is not None and not addr.is_global:
        raise ValueError("Private or non-global IP addresses are not allowed")
    if resolve:
        addresses = socket.getaddrinfo(host, 443, type=socket.SOCK_STREAM)
        if not addresses or any(not ipaddress.ip_address(a[4][0]).is_global for a in addresses):
            raise ValueError("DNS resolves to a private or non-global address")
    return host.removeprefix("www.")


def normalized(url):
    parts = urlsplit(url)
    return urlunsplit((parts.scheme.lower(), (parts.hostname or "").lower(), parts.path.rstrip("/") or "/", parts.query, ""))


class PublicRedirects(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        validate_https_url(newurl, resolve=True)
        if getattr(req, "_redirect_count", 0) >= 5:
            raise ValueError("Too many redirects")
        nxt = super().redirect_request(req, fp, code, msg, headers, newurl)
        if nxt is not None:
            nxt._redirect_count = getattr(req, "_redirect_count", 0) + 1
        return nxt


class Anchors(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.anchors = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() != "a":
            return
        a = dict(attrs)
        if a.get("href"):
            self.anchors.append((a["href"], a.get("rel", "")))


def classify_rel(rel):
    tokens = set(rel.lower().split())
    restricted = sorted(tokens & {"nofollow", "ugc", "sponsored"})
    return "+".join(restricted) if restricted else "no_restriction_token_observed"


def inspect_html(html, source_url, target_url, match="domain"):
    target_host = validate_https_url(target_url)
    source_host = validate_https_url(source_url)
    if target_host == source_host:
        raise ValueError("Source must be a separate third-party domain")
    parser = Anchors()
    parser.feed(html)
    found = []
    for raw_href, raw_rel in parser.anchors:
        actual = urljoin(source_url, raw_href)
        parts = urlsplit(actual)
        if parts.scheme.lower() not in ("http", "https"):
            continue
        host = (parts.hostname or "").lower().removeprefix("www.")
        if host != target_host:
            continue
        if match == "exact" and normalized(actual) != normalized(target_url):
            continue
        found.append({
            "href": actual,
            "raw_href": raw_href,
            "rel": raw_rel if raw_rel else "(none)",
            "rel_result": classify_rel(raw_rel),
        })
        if len(found) >= LIMIT:
            break
    return {
        "status": "found" if found else "not_found_in_fetched_html",
        "source_url": source_url,
        "target_url": target_url,
        "match": match,
        "links": found,
        "scanned_anchor_tags": len(parser.anchors),
        "checked_utc": datetime.now(timezone.utc).isoformat(),
        "verification_method": "public_html_anchor_scan_not_google_index_check",
        "caveat": "No match is limited to the fetched HTML; JS-rendered links, other pages and search indexing are not checked. Rel without nofollow/ugc/sponsored is not a guarantee of ranking benefit.",
    }


def fetch_public_html(source_url, timeout):
    validate_https_url(source_url, resolve=True)
    opener = build_opener(PublicRedirects())
    req = Request(source_url, headers={"User-Agent": "BacklinkEvidenceChecker/1.0 (read-only)", "Accept": "text/html"})
    with opener.open(req, timeout=timeout) as res:
        final = res.geturl()
        validate_https_url(final, resolve=True)
        ctype = res.headers.get_content_type()
        if ctype not in ("text/html", "application/xhtml+xml"):
            raise ValueError("Remote page is not HTML")
        data = res.read(MAX_BYTES + 1)
        if len(data) > MAX_BYTES:
            raise ValueError("Page exceeds 2 MB read limit")
        charset = res.headers.get_content_charset() or "utf-8"
        return data.decode(charset, errors="replace"), final


def main(argv=None):
    parser = argparse.ArgumentParser(description="Check a third-party public HTML page for actual target href and rel. Read-only; no paid API.")
    parser.add_argument("--source", required=True, help="Public HTTPS listing/detail page")
    parser.add_argument("--target", required=True, help="Your own HTTPS site or tool URL")
    parser.add_argument("--match", choices=("domain", "exact"), default="domain")
    parser.add_argument("--output", help="Optional path for a JSON report (keep personal notes private)")
    parser.add_argument("--html-file", help="OFFLINE TEST ONLY: use local HTML instead of making a network request")
    parser.add_argument("--timeout", type=float, default=12.0)
    args = parser.parse_args(argv)
    try:
        validate_https_url(args.source)
        validate_https_url(args.target)
        if args.html_file:
            raw = Path(args.html_file).read_text(encoding="utf-8")
            final = args.source
            mode = "offline_fixture_not_live_evidence"
        else:
            raw, final = fetch_public_html(args.source, max(1.0, min(args.timeout, 30.0)))
            mode = "live_public_page_fetched"
        result = inspect_html(raw, final, args.target, args.match)
        result["requested_source_url"] = args.source
        result["mode"] = mode
        output = json.dumps(result, indent=2, ensure_ascii=False)
        if args.output:
            Path(args.output).write_text(output + "\n", encoding="utf-8")
        print(output)
        return 0 if result["status"] == "found" else 1
    except Exception as exc:
        print("Verification failed (no link claim): " + str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
