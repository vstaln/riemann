#!/usr/bin/env python3
"""Batch 3: final targeted arXiv queries."""
import time, urllib.request, urllib.parse, xml.etree.ElementTree as ET, os

OUT = "/tmp/arxiv_hunt/xml3"
os.makedirs(OUT, exist_ok=True)
NS = {"a": "http://www.w3.org/2005/Atom", "ar": "http://arxiv.org/schemas/atom"}
UA = "Mozilla/5.0 (X11; Linux x86_64) riemann-paper-finder/1.0"

QUERIES = {
    "random-regular-spectrum": 'all:"random regular graph" AND all:spectrum',
    "bordenave-regular": 'au:Bordenave AND all:regular',
    "bauerschmidt-regular": 'au:Bauerschmidt AND all:regular',
    "selberg-value-dist": 'all:"Selberg zeta" AND all:"value distribution"',
    "selberg-gue": 'all:"Selberg zeta" AND all:GUE',
    "zeta-spacing-numerics": 'all:"spacing" AND all:"zeros of the Riemann zeta"',
    "quantum-chaos-hyperbolic": 'all:"quantum chaos" AND all:"hyperbolic surface"',
    "ghosal-rigidity": 'au:Ghosal AND all:rigidity',
    "ihara-zeta-spectrum": 'all:"Ihara zeta" AND all:spectrum',
    "sarnak-hyperbolic": 'au:Sarnak AND (all:spectrum OR all:eigenvalue) AND all:hyperbolic',
    "zeta-zeros-gue-2018": 'all:"Riemann zeta" AND all:zeros AND all:"random matrix" AND submittedDate:[201801010000 TO 202612312359]',
    "sine-kernel-finite2": 'ti:"sine kernel"',
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
        out.append((eid, title, authors, pub, summ))
    return out

for i, (name, q) in enumerate(QUERIES.items()):
    fn = fetch(q, name)
    if fn:
        print(f"  -- {name} ({len(parse(fn))} results) --")
    time.sleep(3)
