"""Generate the exact constraint families used by the Python LPs (alpha-independent)
into data files the Rust tool reads, so the LP v* match is exact (same configs, incl.
numpy default_rng(12345) intermediate samples). Not part of the Rust tool itself."""
import numpy as np, os

OUT = os.path.join(os.path.dirname(__file__), "..", "data")
os.makedirs(OUT, exist_ok=True)

def crystal2(n):
    return np.array([[a, b, a, b, a, b] for a in np.linspace(0.8, 1.6, n)
                     for b in np.linspace(1.4, 2.6, n)], float)

def crystal3(n):
    return np.array([[a, b, c, a, b, c]
                     for a in np.linspace(0.85, 1.55, n)
                     for b in np.linspace(1.4, 2.5, n)
                     for c in np.linspace(0.85, 1.55, n)], float)

def huge_gap():
    out = []
    base = np.array([1.05, 1.98, 1.05, 1.98, 1.05, 1.98])
    for pos in range(6):
        for H in [8.0, 14.0, 21.0]:
            g = base.copy(); g[pos] = H
            out.append(g)
    return np.array(out, float)

def intermediate(n, seed=12345):
    """reopt-style mixed intermediate: n draws in [0.5,3] then n//2 in [0.9,1.6]."""
    rng = np.random.default_rng(seed)
    return np.vstack([rng.uniform(0.5, 3.0, (n, 6)), rng.uniform(0.9, 1.6, (n // 2, 6))])

def intermediate_sym(n, seed=12345):
    """symmetric-style: n draws in [0.5,3] only."""
    rng = np.random.default_rng(seed)
    return rng.uniform(0.5, 3.0, (n, 6))

# 578-family (symmetric LP): crystal2(14) + crystal3(4) + huge_gap + inter(300)
f578 = np.vstack([crystal2(14), crystal3(4), huge_gap(), intermediate_sym(300)])
np.savetxt(os.path.join(OUT, "family_578.txt"), f578, fmt="%.17g")
# 1089-family (full reopt LP): crystal2(14) + crystal3(5) + huge_gap + inter(500) [->750]
f1089 = np.vstack([crystal2(14), crystal3(5), huge_gap(), intermediate(500)])
np.savetxt(os.path.join(OUT, "family_1089.txt"), f1089, fmt="%.17g")
print("family_578.txt", f578.shape, "family_1089.txt", f1089.shape)
