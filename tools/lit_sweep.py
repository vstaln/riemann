#!/usr/bin/env python3
"""LIT sweep against the arXiv export API.

Runs each search query, saves the raw XML under scratch/lit-sweep/, and prints
a compact per-item digest (id, date, title) for relevance triage.

Usage: python3 tools/lit_sweep.py
"""
import os, re, sys, time, urllib.parse, urllib.request, xml.etree.ElementTree as ET

BASE = "http://export.arxiv.org/api/query"
UA = "Mozilla/5.0 (research-literature-sweep; contact: riemann-program-phone) python-urllib"
SCRATCH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scratch", "lit-sweep")
os.makedirs(SCRATCH, exist_ok=True)

NS = {"a": "http://www.w3.org/2005/Atom"}

# (name, search_query) pairs. URL-encoded automatically.
QUERIES = [
    ("simple-zeros",
     'all:"simple zeros" AND all:"Riemann zeta"'),
    ("critline-online",
     'all:"zeros on the critical line" AND cat:math.NT'),
    ("critline-proportion",
     'all:"critical line" AND all:"proportion"'),
    ("weil-quadratic-form",
     'all:"Weil quadratic form" AND all:"zeta"'),
    ("rank-trace-inequality",
     'all:"rank-trace inequality"'),
    ("vonneumann-trace",
     'all:"von Neumann trace inequality" AND all:"zeta"'),
    ("baluyot",
     'all:"Baluyot"'),
    ("gram-matrix",
     'all:"Gram matrix" AND all:"Riemann zeta"'),
    ("gap-distribution",
     'all:"gap distribution" AND all:"zeros"'),
    ("pct-6725",
     'all:"67.25"'),
    ("two-thirds-of-zeros",
     'all:"two thirds of the zeros"'),
]

def fetch(search_query, retries=4):
    params = {
        "search_query": search_query,
        "start": 0,
        "max_results": 20,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    url = BASE + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read().decode("utf-8", "replace")
        except Exception as e:  # network / HTTP errors
            last = e
            time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"failed after {retries} attempts: {last}")

def parse(xml):
    root = ET.fromstring(xml)
    out = []
    for entry in root.findall("a:entry", NS):
        eid = entry.find("a:id", NS).text.strip()
        title = re.sub(r"\s+", " ", entry.find("a:title", NS).text).strip()
        published = entry.find("a:published", NS).text.strip()
        summary = re.sub(r"\s+", " ", entry.find("a:summary", NS).text).strip()
        out.append((eid, published[:10], title, summary))
    return out

def main():
    total = 0
    for name, q in QUERIES:
        fn = os.path.join(SCRATCH, f"{name}.xml")
        if os.path.exists(fn) and os.path.getsize(fn) > 0:
            xml = open(fn).read()
            print(f"### {name} (cached) :: {q}", flush=True)
        else:
            print(f"### {name} :: {q}", flush=True)
            try:
                xml = fetch(q)
            except Exception as e:
                print(f"  !! ERROR: {e}", flush=True)
                continue
            with open(fn, "w") as f:
                f.write(xml)
            time.sleep(3)  # polite throttle between queries
        try:
            items = parse(xml)
        except Exception as e:
            print(f"  !! PARSE ERROR: {e}", flush=True)
            continue
        if not items:
            print("  (0 results)", flush=True)
            continue
        for eid, date, title, summary in items:
            total += 1
            aid = re.sub(r"^.*abs/", "", eid)
            print(f"  [{date}] {aid} :: {title[:110]}", flush=True)
            # keep summaries for grep-ability but compact
            print(f"      {summary[:200]}", flush=True)
        time.sleep(1)
    print(f"\nTOTAL items listed: {total}")
    print(f"Raw responses in {SCRATCH}")

if __name__ == "__main__":
    main()
