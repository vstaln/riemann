#!/usr/bin/env python3
"""arXiv literature hunt for the Riemann program paper-finder (spectral lanes).

Queries the arXiv export API, saves raw XML per query, prints a compact
parsed listing. 429-aware backoff, 3.5s polite delay between requests.
"""
import json, os, sys, time, urllib.parse, urllib.request, xml.etree.ElementTree as ET

OUTDIR = os.path.dirname(os.path.abspath(__file__)) + "/xml"
os.makedirs(OUTDIR, exist_ok=True)

NS = {"a": "http://www.w3.org/2005/Atom", "ar": "http://arxiv.org/schemas/atom"}

def fetch(query, label, max_results=25, sort="relevance"):
    params = {
        "search_query": query,
        "start": 0,
        "max_results": max_results,
        "sortBy": sort,
    }
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(params)
    fn = os.path.join(OUTDIR, label + ".xml")
    if os.path.exists(fn) and os.path.getsize(fn) > 1000:
        print(f"[cached] {label}: {fn}")
        return fn
    for attempt in range(6):
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) arXiv-paper-finder/1.0 (riemann program)"})
            with urllib.request.urlopen(req, timeout=30) as r:
                data = r.read()
            open(fn, "wb").write(data)
            print(f"[ok] {label}: {len(data)} bytes -> {fn}  (query: {query[:80]})")
            return fn
        except urllib.error.HTTPError as e:
            if e.code == 429:
                wait = 10 * (2 ** attempt)
                print(f"[429] {label}: backing off {wait}s")
                time.sleep(wait)
            else:
                print(f"[HTTP {e.code}] {label}: {e.reason}")
                time.sleep(5)
        except Exception as e:
            print(f"[err] {label}: {e}")
            time.sleep(5)
    return None

def parse(fn):
    tree = ET.parse(fn)
    root = tree.getroot()
    out = []
    for e in root.findall("a:entry", NS):
        eid = e.find("a:id", NS).text.strip()
        title = " ".join(e.find("a:title", NS).text.split())
        summ = " ".join(e.find("a:summary", NS).text.split())
        authors = [a.find("a:name", NS).text for a in e.findall("a:author", NS)]
        pub = e.find("a:published", NS).text[:10]
        cats = [c.get("term") for c in e.findall("a:category", NS)]
        out.append({"id": eid, "title": title, "summary": summ,
                    "authors": authors, "published": pub, "cats": cats})
    return out

QUERIES = [
    ("ihara-zeta", 'all:"Ihara zeta"', 30, "relevance"),
    ("ihara-zeta-fn", 'all:"Ihara zeta function"', 25, "relevance"),
    ("graph-zeta-moments", 'all:"graph zeta" AND all:moments', 20, "relevance"),
    ("ihara-zeros", 'all:"Ihara" AND all:"zeta zeros"', 20, "relevance"),
    ("ramanujan-graphs-2020", 'all:"Ramanujan graph" AND submittedDate:[202001010000 TO 202612312359]', 30, "submittedDate"),
    ("ramanujan-spectrum", 'all:"Ramanujan" AND all:spectrum', 20, "relevance"),
    ("selberg-zeta", 'all:"Selberg zeta"', 30, "relevance"),
    ("selberg-trace-formula", 'all:"Selberg trace formula"', 25, "relevance"),
    ("selberg-zeta-zeros", 'all:"Selberg zeta" AND all:zeros', 15, "relevance"),
    ("hyperbolic-zeta", 'all:"hyperbolic surface" AND all:zeta', 15, "relevance"),
    ("dpp-sine-kernel", 'all:"determinantal point process" AND all:"sine kernel"', 25, "relevance"),
    ("sine-kernel-rigidity", 'all:"sine kernel" AND all:rigidity', 20, "relevance"),
    ("sine-process-2018", 'all:"sine process" AND submittedDate:[201801010000 TO 202612312359]', 25, "submittedDate"),
    ("finite-rank-determinantal", 'all:"finite rank" AND all:determinantal', 20, "relevance"),
    ("sine-kernel-finite", 'all:"sine kernel" AND all:finite', 20, "relevance"),
    ("dyson-sine-kernel", 'all:"Dyson sine kernel"', 15, "relevance"),
    ("gaudin-mehta", 'all:"Gaudin" AND all:Mehta', 15, "relevance"),
    ("dpp-zeta-zeros", 'all:"determinantal" AND all:"Riemann zeta"', 15, "relevance"),
]

results = {}
for label, q, n, sort in QUERIES:
    fn = fetch(q, label, n, sort)
    if fn:
        results[label] = parse(fn)
    time.sleep(3.5)

with open(os.path.dirname(os.path.abspath(__file__)) + "/results.json", "w") as f:
    json.dump(results, f, indent=1)

for label, lst in results.items():
    print("\n" + "=" * 100)
    print(f"## {label}  ({len(lst)} results)")
    for p in lst:
        aid = p["id"].split("/abs/")[-1]
        au = ", ".join(p["authors"][:3]) + (" et al." if len(p["authors"]) > 3 else "")
        print(f"\n- {aid} | {p['published']} | {au}")
        print(f"  T: {p['title']}")
        print(f"  S: {p['summary'][:280]}")
