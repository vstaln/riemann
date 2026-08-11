#!/usr/bin/env python3
"""Write per-paper abstract .txt companions (title/authors/date/abstract) into
research/papers/ from the cached arXiv API XML. All content is fetched data."""
import glob, os, xml.etree.ElementTree as ET

NS = {"a": "http://www.w3.org/2005/Atom", "ar": "http://arxiv.org/schemas/atom"}
OUTDIR = "/home/vstaln/riemann/research/papers"
XMLDIRS = [os.path.dirname(os.path.abspath(__file__)) + "/xml"]

MANIFEST = [
    ("1905.13485", "ihara-zeta-maclaurin-ramanujan"),
    ("1512.09065", "ihara-rmt-longrange-percolation"),
    ("1508.07839", "ihara-rmt-large-random-graphs"),
    ("2101.03338", "ihara-zeros-erdos-renyi"),
    ("1302.4644", "ihara-generalized-heat-kernel"),
    ("2011.14162", "ihara-grover-walk"),
    ("1304.4132", "ramanujan-interlacing-I-bipartite"),
    ("1505.08010", "ramanujan-interlacing-IV-all-sizes"),
    ("2412.20721", "ramanujan-survey-icm2024-srivastava"),
    ("1502.04482", "ramanujan-friedman-bordenave"),
    ("1505.06700", "random-regular-bulk-spectrum"),
    ("1609.09052", "random-regular-kesten-mckay"),
    ("1501.06087", "nonbacktracking-spectrum-random-graphs"),
    ("2304.01281", "regular-graph-eigenvalue-limit-points"),
    ("2312.06507", "ramanujan-bigraphs"),
    ("1410.8010", "graph-spectral-zeta-vs-riemann"),
    ("2204.08218", "selberg-zeta-zeros-symmetric-surfaces"),
    ("1302.5928", "selberg-derivative-zeros"),
    ("math/0407288", "selberg-trace-formula-intro-marklof"),
    ("2306.13636", "selberg-trace-formula-supersymmetry"),
    ("1509.04323", "selberg-trace-formula-dirichlet-series"),
    ("1809.10140", "selberg-euler-products-critical-strip"),
    ("1110.2150", "hyperbolic-eigenvalues-algorithm"),
    ("1911.10493", "selberg-trace-jt-gravity-rmt"),
    ("2202.06379", "hyperbolic-goe-moduli-rudnick"),
    ("2301.00685", "hyperbolic-clt-linear-statistics"),
    ("2310.18663", "hyperbolic-random-covers-rmt"),
    ("1305.4850", "hyperbolic-resonance-distribution"),
    ("math/0002099", "dpp-survey-soshnikov"),
    ("1804.01216", "sine-beta-rigidity"),
    ("1703.02349", "sine-process-conditional-universality"),
    ("1912.13454", "sine-process-excess-one"),
    ("1506.07581", "dpp-rigidity-airy-bessel-gamma"),
    ("1211.2381", "rigidity-tolerance-ghosh-peres"),
    ("1007.3538", "insertion-deletion-tolerance"),
    ("1907.03391", "bandlimited-mimicry-lattice"),
    ("1410.1440", "cue-zeta-microscopic-landscape"),
    ("2202.04284", "stochastic-zeta-function"),
    ("1510.03641", "mesoscopic-fluctuations-unitary"),
    ("1906.11079", "sine-process-large-gap"),
    ("0803.1141", "zeta-sine-kernel-kosters"),
    ("math/0602270", "zeta-spacing-finiteT-corrections"),
    ("2507.10193", "cue-spacings-finite-size-zeta"),
    ("1008.2173", "zeta-moments-numerical-hiary-odlyzko"),
    ("2507.04150", "selberg-clt-weighted-linear-statistics"),
    ("1112.0346", "riemann-zero-statistics-perez-marco"),
    ("2403.06722", "sine-kernel-finite-temperature"),
    ("2309.03803", "sine-kernel-deformed-determinants"),
    ("1203.1605", "gaudin-mehta-single-gap-tao"),
    ("1703.06985", "poisson-gm-transition-banded"),
]

def index():
    idx = {}
    for d in XMLDIRS:
        for fn in glob.glob(os.path.join(d, "*.xml")):
            try:
                tree = ET.parse(fn)
            except Exception:
                continue
            for e in tree.getroot().findall("a:entry", NS):
                eid = e.find("a:id", NS).text.strip()
                key = eid.split("/abs/")[-1].lower().split("v")[0]
                idx.setdefault(key, e)
    return idx

idx = index()
missing = []
for aid, name in MANIFEST:
    key = aid.lower().split("v")[0]
    e = idx.get(key)
    if e is None:
        missing.append(aid)
        continue
    eid = e.find("a:id", NS).text.strip()
    title = " ".join(e.find("a:title", NS).text.split())
    summ = " ".join(e.find("a:summary", NS).text.split())
    authors = [a.find("a:name", NS).text for a in e.findall("a:author", NS)]
    pub = e.find("a:published", NS).text[:10]
    cat = e.find("ar:primary_category", NS)
    prim = cat.get("term") if cat is not None else ""
    txt = (
        f"arXiv: {eid}\n"
        f"Title: {title}\n"
        f"Authors: {', '.join(authors)}\n"
        f"Published: {pub}\n"
        f"Primary category: {prim}\n\n"
        f"ABSTRACT (fetched from arXiv export API):\n{summ}\n"
    )
    dest = os.path.join(OUTDIR, name + ".txt")
    with open(dest, "w") as f:
        f.write(txt)

print(f"wrote {len(MANIFEST) - len(missing)} abstracts; missing {len(missing)}: {missing}")
