#!/usr/bin/env python3
"""Batch 2: targeted arXiv queries (classics + gaps)."""
import time, urllib.request, urllib.parse, xml.etree.ElementTree as ET, os

OUT = "/tmp/arxiv_hunt/xml2"
os.makedirs(OUT, exist_ok=True)
NS = {"a": "http://www.w3.org/2005/Atom", "ar": "http://arxiv.org/schemas/atom"}
UA = "Mozilla/5.0 (X11; Linux x86_64) riemann-paper-finder/1.0"

QUERIES = {
    "mss-interlacing": 'au:Marcus AND au:Spielman AND au:Srivastava',
    "kadison-singer-ramanujan": 'all:"Kadison-Singer" AND all:Ramanujan',
    "graph-zeta-random-matrix": 'all:"graph zeta" AND all:"random matrix"',
    "ihara-rmt": 'all:Ihara AND all:"random matrix"',
    "selberg-zeros-phrase": 'all:"zeros of the Selberg zeta"',
    "selberg-statistics": 'all:"Selberg zeta" AND all:statistics',
    "selberg-eigenvalue-conj": 'all:"Selberg eigenvalue conjecture"',
    "aurich-steiner": 'au:Aurich AND au:Steiner',
    "bufetov-rigidity": 'au:Bufetov AND all:rigidity',
    "ghosh-peres": 'au:Ghosh AND au:Peres',
    "holroyd-soo": 'au:Holroyd AND au:Soo',
    "soshnikov-determinantal": 'au:Soshnikov AND all:determinantal',
    "zeta-local-statistics": 'all:"Riemann zeta" AND all:"local statistics"',
    "hiary-odlyzko": 'au:Hiary AND au:Odlyzko',
    "zeta-gue-numerical": 'all:"Riemann zeta" AND all:"GUE" AND all:numerical',
    "ramanujan-ti": 'ti:"Ramanujan graph"',
    "zeta-functions-of-graphs": 'all:"zeta functions of graphs"',
    "hyperbolic-eigenvalue-stat": 'all:"compact hyperbolic surface" AND all:eigenvalue AND all:statistics',
}

def fetch(query, name, max_results=20):
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(
        {"search_query": query, "start": 0, "max_results": max_results})
    fn = os.path.join(OUT, name + ".xml")
    if os.path.exists(fn) and os.path.getsize(fn) > 1000:
        print(f"[cached] {name}"); return fn
    for attempt in range(6):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            open(fn, "wb").write(data)
            print(f"[ok] {name} ({len(data)}B)")
            return fn
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(20 * (attempt + 1))
            else:
                print(f"[HTTP {e.code}] {name}"); time.sleep(6)
        except Exception as e:
            print(f"[ERR] {name}: {e}"); time.sleep(8)
    return None

def parse(fn):
    tree = ET.parse(fn); root = tree.getroot()
    out = []
    for e in root.findall("a:entry", NS):
        eid = e.find("a:id", NS).text.strip().split("/abs/")[-1]
        title = " ".join(e.find("a:title", NS).text.split())
        summ = " ".join(e.find("a:summary", NS).text.split())
        authors = [a.find("a:name", NS).text for a in e.findall("a:author", NS)]
        pub = e.find("a:published", NS).text[:10]
        cat = e.find("ar:primary_category", NS)
        prim = cat.get("term") if cat is not None else ""
        out.append((eid, title, authors, pub, prim, summ))
    return out

for i, (name, q) in enumerate(QUERIES.items()):
    fn = fetch(q, name)
    if fn:
        print(f"  -- {name} ({len(parse(fn))} results) --")
    time.sleep(3)
