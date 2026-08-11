#!/usr/bin/env python3
"""Empirical moments of the flat-window Gram matrix from ACTUAL zeta zeros.

Builds G_ij = sinc(pi*la*(x_i - x_j)) on a locally-rescaled zero band (mean spacing 1),
computes normalized moments m1 = tr G / N, m2 = tr G^2 / N, m3 = tr G^3 / N at lambda=1
and lambda=1/2. Compares with closed forms:
  lam=1:  m2=4/3, m3=2      lam=1/2: m2=13/6, m3=5.
Convergence is imperfect at finite height (pair/triple correlation), so expect ~few-% accuracy.
"""
import numpy as np

def load_band(fn, lo, hi):
    g = []
    with open(fn) as f:
        for line in f:
            p = line.split()
            if len(p) >= 2:
                g.append(float(p[1]))
    g = np.array(g)
    m = (g >= lo) & (g <= hi)
    return g[m]

def moments(gammas, la):
    # local rescale: mean spacing 1
    n = gammas.size
    if n < 5:
        return np.nan, np.nan, np.nan
    sp = np.diff(np.sort(gammas)).mean()
    x = np.sort(gammas)/sp
    d = x[:, None] - x[None, :]
    G = np.sinc(la*d)
    m1 = np.trace(G)/n
    G2 = G @ G
    m2 = np.trace(G2)/n
    G3 = G2 @ G
    m3 = np.trace(G3)/n
    return m1, m2, m3

fn = "data/zeros_computed_10000.txt"
for (lo, hi, name) in ((9000, 9880, "high 9000-9880 (1080 zeros)"),
                       (5000, 7000, "mid 5000-7000"),
                       (2000, 4000, "low-mid 2000-4000")):
    g = load_band(fn, lo, hi)
    print(f"\nband {name}: n={g.size}")
    for la, (e2, e3) in ((1.0, (4/3, 2.0)), (0.5, (13/6, 5.0))):
        m1, m2, m3 = moments(g, la)
        print(f"  lambda={la}: m1={m1:.4f} m2={m2:.4f} (exp {e2:.4f}) m3={m3:.4f} (exp {e3:.4f})")
