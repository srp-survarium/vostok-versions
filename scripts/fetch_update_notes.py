#!/usr/bin/env python3
"""Archive update pages and source metadata from the Survarium Fandom wiki.

Recurses through Category:Updates, then follows version-number links from the
category pages, update pages, and Version history. Missing/redlinked versions
are recorded explicitly. Wikitext is retained unchanged; no inferred binary
build IDs or normalized version aliases are added to the build catalog.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import datetime
import hashlib
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

API = "https://survarium.fandom.com/api.php"
WIKI = "https://survarium.fandom.com/wiki/"
VERSION_TITLE = re.compile(r"^\d+\.\d+[a-z0-9.]*(?:[ -].*)?$", re.I)
ROOT_CATEGORY = "Category:Updates"


def api_query(**params) -> dict:
    query = urllib.parse.urlencode({"action": "query", "format": "json", **params})
    request = urllib.request.Request(API + "?" + query, headers={
        "User-Agent": "SurvariumVersionsArchive/1.0 (source-preservation; MediaWiki API)",
    })
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                result = json.load(response)
            if "error" in result:
                raise RuntimeError(f"MediaWiki error: {result['error']}")
            return result
        except (urllib.error.URLError, TimeoutError):
            if attempt == 3:
                raise
            time.sleep(2 ** attempt)
    raise AssertionError("unreachable")


def category_members(title: str) -> list[dict]:
    members, continuation = [], {}
    while True:
        result = api_query(list="categorymembers", cmtitle=title, cmlimit=500, **continuation)
        members.extend(result["query"].get("categorymembers", []))
        continuation = result.get("continue")
        if not continuation:
            return members


def fetch_page(title: str) -> dict:
    continuation, record, links = {}, None, set()
    while True:
        result = api_query(prop="revisions|info|links", titles=title, inprop="url",
                           rvprop="ids|timestamp|user|content", rvslots="main",
                           pllimit=500, **continuation)
        page = next(iter(result["query"]["pages"].values()))
        if record is None:
            record = page
        links.update(link["title"] for link in page.get("links", []) if link["ns"] == 0)
        continuation = result.get("continue")
        if not continuation:
            record["version_links"] = sorted(title for title in links if VERSION_TITLE.fullmatch(title))
            return record


def source_date(wikitext: str) -> str | None:
    match = re.search(r"^\|\s*date\s*=\s*(.+)$", wikitext, re.M | re.I)
    return match.group(1).strip().rstrip("}").strip() if match else None


def title_path(title: str) -> str:
    return urllib.parse.quote(title.replace(" ", "_"), safe="") + ".wiki"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="new snapshot directory (must not exist)")
    args = parser.parse_args()
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    output = args.output or (Path(__file__).resolve().parents[1] / ".generated" /
                             "wiki" / started[:10])
    if output.exists():
        parser.error(f"snapshot already exists: {output}; choose a new --output")
    output.mkdir(parents=True)
    (output / "pages").mkdir()
    (output / "INCOMPLETE").write_text("Fetch is incomplete until manifest.json is written.\n")
    siteinfo = api_query(meta="siteinfo", siprop="general|rightsinfo")["query"]
    (output / "siteinfo.json").write_text(json.dumps(siteinfo, indent=2, ensure_ascii=False) + "\n")
    categories, pending = {}, {ROOT_CATEGORY}
    titles = {"Version history", "Template:Navbox versions", "Template:Infobox version"}
    while pending:
        title = pending.pop()
        members = category_members(title)
        categories[title] = members
        titles.add(title)
        for member in members:
            if member["ns"] == 14 and member["title"] not in categories:
                pending.add(member["title"])
            elif member["ns"] == 0:
                titles.add(member["title"])
    (output / "categories.json").write_text(json.dumps(categories, indent=2, ensure_ascii=False) + "\n")
    pages, fetched = {}, set()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        while titles - fetched:
            batch = sorted(titles - fetched)
            print(f"Fetching {len(batch)} pages ({len(pages)} already read)", flush=True)
            for page in pool.map(fetch_page, batch):
                title = page["title"]
                pages[title] = page
                titles.update(page["version_links"])
            fetched.update(batch)
            fetched.update(pages)
    records = []
    for title, page in sorted(pages.items()):
        record = {"title": title, "page_id": page.get("pageid"),
                  "url": page.get("fullurl", WIKI + urllib.parse.quote(title.replace(" ", "_"))),
                  "history_url": "https://survarium.fandom.com/index.php?" +
                                 urllib.parse.urlencode({"title": title, "action": "history"}),
                  "version_links": page["version_links"],
                  "categories": [cat for cat, members in categories.items()
                                 if any(member["title"] == title for member in members)]}
        if "missing" in page:
            record["status"] = "missing"
        else:
            revision = page["revisions"][0]
            content = revision["slots"]["main"]["*"]
            path = "pages/" + title_path(title)
            (output / path).write_text(content, encoding="utf-8")
            record.update(status="captured", revision_id=revision["revid"],
                          revision_timestamp=revision["timestamp"],
                          last_editor=revision.get("user"), path=path,
                          revision_url=record["url"] + "?oldid=" + str(revision["revid"]),
                          sha256=hashlib.sha256(content.encode()).hexdigest(),
                          source_date=source_date(content))
        records.append(record)
    updates = [r for r in records if VERSION_TITLE.fullmatch(r["title"])]
    rights = siteinfo.get("rightsinfo", {})
    manifest = {"source": WIKI + "Category:Updates", "api": API,
                "started_at": started,
                "completed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                "license_as_reported": rights,
                "attribution": "Survarium Wiki contributors; each record links to its page, revision, and contributor history.",
                "format": "Unmodified MediaWiki wikitext, encoded as UTF-8.",
                "coverage": "Recursive Updates categories plus version-number links from captured pages and Version history. Missing pages are retained as records.",
                "pages": records}
    (output / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
    md = ["# Survarium Wiki update notes", "",
          f"Captured {started[:10]} from [Category:Updates]({manifest['source']}) and its subcategories, "
          "with additional version links from the wiki's history/navigation.", "",
          f"Attribution: Survarium Wiki contributors. The source API reports "
          f"[{rights.get('text', 'license unspecified')}]({rights.get('url', manifest['source'])}). "
          "Source text retains those terms; it is not relicensed as project code. "
          "Per-page revision and contributor-history links are in `manifest.json`.", "",
          "These are wiki descriptions of updates, not proof that a corresponding binary is available. "
          "Source version names and release-date text are preserved without equating them to binary build IDs.", "",
          f"Captured update pages: **{sum(r['status'] == 'captured' for r in updates)}**. "
          f"Missing linked update pages: **{sum(r['status'] == 'missing' for r in updates)}**.", "",
          "| Wiki version | Release date as written | Source revision |",
          "| --- | --- | --- |"]
    for record in updates:
        if record["status"] == "missing":
            md.append(f"| {record['title']} | Missing page | [source]({record['url']}) |")
        else:
            date = (record.get("source_date") or "Not recorded").replace("|", "\\|")
            md.append(f"| [{record['title']}]({record['path']}) | {date} | "
                      f"[{record['revision_id']}]({record['revision_url']}) |")
    (output / "README.md").write_text("\n".join(md) + "\n")
    (output / "INCOMPLETE").unlink()
    print(f"Stored {len(records)} page records in {output}", flush=True)


if __name__ == "__main__":
    main()
