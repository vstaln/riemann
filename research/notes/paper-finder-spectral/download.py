#!/usr/bin/env python3
"""Download arXiv PDFs for the verified spectral-lane papers."""
import os, subprocess, sys, time

# (arxiv_id_without_version, descriptive_filename)
MANIFEST = [
    # ---- Lane (a): Ihara zeta sandbox / graph zeta / Ramanujan ----
    ("1905.13485", "ihara-zeta-maclaurin-ramanujan"),          # Huang: Ihara zeta, Maclaurin coefficients, Ramanujan graphs
    ("1512.09065", "ihara-rmt-longrange-percolation"),         # Khorunzhiy: Ihara RMT long-range percolation
    ("1508.07839", "ihara-rmt-large-random-graphs"),           # Khorunzhiy: Ihara RMT large random graphs
    ("2101.03338", "ihara-zeros-erdos-renyi"),                 # Khorunzhiy: absence of poles, ER graphs
    ("1302.4644", "ihara-generalized-heat-kernel"),            # Chinta-Jorgenson-Karlsson
    ("2011.14162", "ihara-grover-walk"),                       # Komatsu-Konno-Sato
    ("1304.4132", "ramanujan-interlacing-I-bipartite"),        # MSS I
    ("1505.08010", "ramanujan-interlacing-IV-all-sizes"),      # MSS IV
    ("2412.20721", "ramanujan-survey-icm2024-srivastava"),     # Srivastava ICM survey
    ("1502.04482", "ramanujan-friedman-bordenave"),            # Bordenave: Friedman's 2nd eigenvalue thm
    ("1505.06700", "random-regular-bulk-spectrum"),            # BHKY: bulk eigenvalue statistics
    ("1609.09052", "random-regular-kesten-mckay"),             # BHY: local Kesten-McKay
    ("1501.06087", "nonbacktracking-spectrum-random-graphs"),  # Bordenave-Lelarge-Massoulie
    ("2304.01281", "regular-graph-eigenvalue-limit-points"),   # Alon-Wei
    ("2312.06507", "ramanujan-bigraphs"),                      # Evra-Feigon-Maurischat et al.
    ("1410.8010", "graph-spectral-zeta-vs-riemann"),           # Friedli-Karlsson
    # ---- Lane (b): Selberg zeta / trace formula / hyperbolic surfaces ----
    ("2204.08218", "selberg-zeta-zeros-symmetric-surfaces"),   # Pollicott-Vytnova
    ("1302.5928", "selberg-derivative-zeros"),                 # Jorgenson-Smajlovic
    ("math/0407288", "selberg-trace-formula-intro-marklof"),   # Marklof
    ("2306.13636", "selberg-trace-formula-supersymmetry"),     # Choi-Takhtajan
    ("1509.04323", "selberg-trace-formula-dirichlet-series"),  # Booker-Lee
    ("1809.10140", "selberg-euler-products-critical-strip"),   # Kaneko-Koyama
    ("1110.2150", "hyperbolic-eigenvalues-algorithm"),         # Strohmaier-Uski
    ("1911.10493", "selberg-trace-jt-gravity-rmt"),            # Garcia-Garcia-Zacarias
    ("2202.06379", "hyperbolic-goe-moduli-rudnick"),           # Rudnick GOE moduli
    ("2301.00685", "hyperbolic-clt-linear-statistics"),        # Rudnick-Wigman
    ("2310.18663", "hyperbolic-random-covers-rmt"),            # Maoz
    ("1305.4850", "hyperbolic-resonance-distribution"),        # Borthwick
    # ---- Lane (c): DPP / sine kernel / rigidity ----
    ("math/0002099", "dpp-survey-soshnikov"),                  # Soshnikov survey
    ("1804.01216", "sine-beta-rigidity"),                      # Chhaibi-Najnudel
    ("1703.02349", "sine-process-conditional-universality"),   # Kuijlaars-Mina-Diaz
    ("1912.13454", "sine-process-excess-one"),                 # Bufetov
    ("1506.07581", "dpp-rigidity-airy-bessel-gamma"),          # Bufetov
    ("1211.2381", "rigidity-tolerance-ghosh-peres"),           # Ghosh-Peres
    ("1007.3538", "insertion-deletion-tolerance"),             # Holroyd-Soo
    ("1907.03391", "bandlimited-mimicry-lattice"),             # Lagarias-Rodgers
    ("1410.1440", "cue-zeta-microscopic-landscape"),           # Chhaibi-Najnudel-Nikeghbali
    ("2202.04284", "stochastic-zeta-function"),                # Najnudel-Nikeghbali
    ("1510.03641", "mesoscopic-fluctuations-unitary"),         # Lambert
    ("1906.11079", "sine-process-large-gap"),                  # Charlier
    ("0803.1141", "zeta-sine-kernel-kosters"),                 # Kosters
    # ---- Lane (c): finite-T sine kernel / hot-hand / LS-estimator ----
    ("math/0602270", "zeta-spacing-finiteT-corrections"),      # Bogomolny-Bohigas-Leboeuf et al.
    ("2507.10193", "cue-spacings-finite-size-zeta"),           # Nishigaki
    ("1008.2173", "zeta-moments-numerical-hiary-odlyzko"),     # Hiary-Odlyzko
    ("2507.04150", "selberg-clt-weighted-linear-statistics"),  # Fazzari-Gerspach-Minelli
    ("1112.0346", "riemann-zero-statistics-perez-marco"),      # Perez Marco
    ("2403.06722", "sine-kernel-finite-temperature"),          # Xu
    ("2309.03803", "sine-kernel-deformed-determinants"),       # Claeys-Tarricone
    ("1203.1605", "gaudin-mehta-single-gap-tao"),              # Tao
    ("1703.06985", "poisson-gm-transition-banded"),            # Olver-Swan
]

OUTDIR = "/home/vstaln/riemann/research/papers"
UA = "Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0"

def download(aid, name):
    dest = os.path.join(OUTDIR, name + ".pdf")
    if os.path.exists(dest) and os.path.getsize(dest) > 100000:
        print(f"[skip] {name} (already present {os.path.getsize(dest)}B)")
        return "skip"
    url = f"https://arxiv.org/pdf/{aid}"
    cmd = ["curl", "-sL", "-A", UA, "-o", dest, "--max-time", "120", url]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(dest) and os.path.getsize(dest) > 100000:
        with open(dest, "rb") as f:
            head = f.read(5)
        if head == b"%PDF-":
            print(f"[ok] {aid} -> {name}.pdf ({os.path.getsize(dest)}B)")
            return "ok"
        else:
            print(f"[BAD] {aid} -> {name}.pdf: not a PDF ({os.path.getsize(dest)}B) head={head!r}")
            os.remove(dest)
            return "bad"
    else:
        print(f"[FAIL] {aid} -> {name}.pdf: {r.stderr[-200:] if r.stderr else 'no output'}")
        return "fail"

results = {}
for i, (aid, name) in enumerate(MANIFEST):
    results[name] = download(aid, name)
    time.sleep(2.0)

print("\n==== SUMMARY ====")
from collections import Counter
c = Counter(results.values())
print(dict(c))
for name, st in results.items():
    if st != "ok":
        print(f"  {st}: {name}")
