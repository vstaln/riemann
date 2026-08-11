#!/usr/bin/env python3
"""Supplementary LIT queries (targets 1-2 completeness) + author extraction."""
import os, re, time, urllib.parse, urllib.request, xml.etree.ElementTree as ET

BASE = "http://export.arxiv.org/api/query"
UA = "Mozilla/5.0 (research-literature-sweep; contact: riemann-program-phone) python-urllib"
SCRATCH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scratch", "lit-sweep")
NS = {"a": "http://www.w3.org/2005/Atom"}

EXTRA = [
    ("proportion-simple-zeros", 'all:"proportion of simple zeros"'),
    ("distinct-zeros", 'all:"distinct zeros" AND all:"Riemann zeta"'),
]

def fetch(search_query, retries=4):
    params = {"search_query": search_query, "start": 0, "max_results": 10,
              "sortBy": "submittedDate", "sortOrder": "descending"}
    url = BASE + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read().decode("utf-8", "replace")
        except Exception as e:
            last = e
            time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"failed: {last}")

def dump(name, q):
    fn = os.path.join(SCRATCH, f"{name}.xml")
    if not (os.path.exists(fn) and os.path.getsize(fn) > 0):
        xml = fetch(q)
        open(fn, "w").write(xml)
        time.sleep(2)
    else:
        xml = open(fn).read()
    print(f"### {name} :: {q}")
    root = ET.fromstring(xml)
    n = 0
    for e in root.findall("a:entry", NS):
        eid = e.find("a:id", NS).text.strip()
        t = re.sub(r"\s+", " ", e.find("a:title", NS).text).strip()
        d = e.find("a:published", NS).text[:10]
        s = re.sub(r"\s+", " ", e.find("a:summary", NS).text).strip()
        print(f"  [{d}] {eid} :: {t}")
        print(f"      {s[:230]}")
        n += 1
    print(f"  ({n} results)\n")

for name, q in EXTRA:
    try:
        dump(name, q)
    except Exception as ex:
        print(f"!! {name}: {ex}")

# Author extraction for the key papers found in the main sweep
print("===== AUTHORS of key papers =====")
KEY = {
    "2603.28104": "simple-zeros.xml",
    "2511.20059": "simple-zeros.xml",
    "2607.02828": "weil-quadratic-form.xml",
    "2606.09096": "weil-quadratic-form.xml",
    "2602.04022": "weil-quadratic-form.xml",
    "2508.10857": "baluyot.xml",
    "2508.11108": "critline-online.xml",
    "2509.18963": "critline-online.xml",
    "2511.06109": "critline-online.xml",
    "2310.10119": "simple-zeros.xml",
    "1902.05473": "two-thirds-of-zeros.xml",
    "1302.5018": "simple-zeros.xml",
    "1410.2433": "simple-zeros.xml",
    "2307.13498": "gap-distribution.xml",
}
for aid, fname in KEY.items():
    fn = os.path.join(SCRATCH, fname)
    try:
        root = ET.parse(fn).getroot()
        for e in root.findall("a:entry", NS):
            eid = e.find("a:id", NS).text.strip()
            if aid in eid:
                authors = ", ".join(a.text for a in e.findall("a:author", NS))
                title = re.sub(r"\s+", " ", e.find("a:title", NS).text).strip()
                print(f"{aid} [{e.find('a:published', NS).text[:10]}] :: {title}")
                print(f"    AUTHORS: {authors}")
    except Exception as ex:
        print(f"!! {aid}: {ex}")
