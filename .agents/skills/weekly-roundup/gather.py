#!/usr/bin/env python3
"""List candidate items for a Way Into AI weekly issue.

Usage: gather.py [--today YYYY-MM-DD] [--since YYYY-MM-DD] [--until YYYY-MM-DD]

Defaults: --today is the local date; --until is the day before --today;
--since is the day after the last *sent* issue's window_end in weekly/ (or
7 days before --until). Prints markdown sections; reads only, never writes.
Stdlib only: the frontmatter parser handles the flat YAML used in this repo
(scalars, quoted scalars, block and inline lists), not full YAML.
"""
import argparse
import datetime as dt
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
STALE_DAYS = 28


def unquote(v):
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        return v[1:-1]
    return v


def frontmatter(path):
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    m = re.match(r"---\n(.*?)\n---[ \t]*(\n|$)", text, re.S)
    fm, key = {}, None
    for line in (m.group(1).splitlines() if m else []):
        item = re.match(r"^\s+- (.*)$", line)
        if item and key:
            if not isinstance(fm.get(key), list):
                fm[key] = []
            fm[key].append(unquote(item.group(1)))
            continue
        kv = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if kv:
            key, val = kv.group(1), kv.group(2).strip()
            if val.startswith("[") and val.endswith("]"):
                fm[key] = [unquote(x) for x in val[1:-1].split(",") if x.strip()]
            elif val in (">", "|", ">-", "|-"):
                fm[key] = ""  # folded/literal block: value not needed here
            else:
                fm[key] = unquote(val)
    body = text[m.end():] if m else text
    h1 = re.search(r"^# (.+)$", body, re.M)
    fm.setdefault("title", h1.group(1) if h1 else path.stem)
    return fm, body


def as_list(v):
    return v if isinstance(v, list) else ([v] if v else [])


def item_date(path, fm):
    for k in ("date", "created"):
        v = str(fm.get(k, ""))
        if re.match(r"\d{4}-\d{2}-\d{2}", v):
            return dt.date.fromisoformat(v[:10])
    m = re.match(r"(\d{4}-\d{2}-\d{2})", path.name)
    return dt.date.fromisoformat(m.group(1)) if m else None


def sent_issues():
    """Sent issues in weekly/: (path, frontmatter)."""
    out = []
    for p in sorted((ROOT / "weekly").glob("*-w*.md")):
        fm, _ = frontmatter(p)
        if fm.get("status") == "sent":
            out.append((p, fm))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--today")
    ap.add_argument("--since")
    ap.add_argument("--until")
    a = ap.parse_args()
    today = dt.date.fromisoformat(a.today) if a.today else dt.date.today()
    until = dt.date.fromisoformat(a.until) if a.until else today - dt.timedelta(days=1)
    sent = sent_issues()
    if a.since:
        since = dt.date.fromisoformat(a.since)
    else:
        ends = [dt.date.fromisoformat(fm["window_end"]) for _, fm in sent if fm.get("window_end")]
        since = max(ends) + dt.timedelta(days=1) if ends else until - dt.timedelta(days=6)
    if since > until:
        sys.exit(f"error: empty window {since} .. {until}; pass --since/--until")

    already = {}  # repo path -> issue file that included it
    for p, fm in sent:
        for rel in as_list(fm.get("items")) + as_list(fm.get("try")):
            already[rel] = p.name
    past_tries = [(p.name, fm["try"]) for p, fm in sent if fm.get("try")]

    print(f"# Candidates {since} .. {until}\n")
    if not sent:
        print("_No sent issues in weekly/ yet: this is issue 1._\n")

    items, undated = [], []
    for d in ("posts", "ref"):
        for p in sorted((ROOT / d).glob("*.md")):
            if p.name == "index.md":
                continue
            fm, _ = frontmatter(p)
            rel = p.relative_to(ROOT).as_posix()
            date = item_date(p, fm)
            items.append((rel, fm, date))
            if date is None:
                undated.append(rel)

    def done(rel, fm):
        return bool(fm.get("newsletter_sent")) or rel in already

    def line(rel, fm, date):
        tags = fm.get("tags", [])
        tags = "[" + ", ".join(tags) + "]" if isinstance(tags, list) else tags
        flags = " ".join(f"{k}={fm[k]}" for k in ("newsletter", "featured") if fm.get(k))
        stale = " STALE" if date and (until - date).days > STALE_DAYS else ""
        return f"- `{rel}` ({date}) {fm['title']} {flags}{stale} {tags}".rstrip()

    print("## Flagged, not yet sent (any date; STALE = older than 4 weeks, ask reviewer)\n")
    for rel, fm, date in items:
        if fm.get("newsletter") in ("weekly", "standalone") and not done(rel, fm):
            print(line(rel, fm, date))

    print("\n## Log newsletter_candidates in window (not yet sent)\n")
    lookup = {rel: fm for rel, fm, _ in items}
    for p in sorted((ROOT / "logs").glob("????-??-??.md")):
        fm, _ = frontmatter(p)
        d = item_date(p, fm)
        if d and since <= d <= until:
            for c in as_list(fm.get("newsletter_candidates")):
                if not done(c, lookup.get(c, {})):
                    print(f"- `{c}` (from logs/{p.name})")

    print("\n## New posts and refs in window (not yet sent)\n")
    for rel, fm, date in items:
        if date and since <= date <= until and not done(rel, fm):
            print(line(rel, fm, date))

    print("\n## Logs in window\n")
    for p in sorted((ROOT / "logs").glob("????-??-??.md")):
        fm, body = frontmatter(p)
        d = item_date(p, fm)
        if d and since <= d <= until:
            heads = re.findall(r"^## (.+)$", body, re.M)
            print(f"- `logs/{p.name}`: " + "; ".join(heads))

    print("\n## Past 'One thing to try' picks (do not repeat)\n")
    for name, t in past_tries:
        print(f"- `{t}` ({name})")

    if undated:
        print(f"\n## Undated posts/refs ({len(undated)}; not windowed, check by hand if relevant)\n")
        print(", ".join(f"`{u}`" for u in undated))


if __name__ == "__main__":
    main()
