#!/usr/bin/env python3
"""Robustness check of the sign flip: 5 disjoint windows + the LMFDB 1000-zero file.
For each window, internal density-1 rescale, banded off-diagonal sinc^2 sum, deficit vs GUE.
Cross-check: sign and magnitude of the u<1 deficit vs the height of the window."""
import numpy as np
from scipy import integrate

def load(fn, col=1):
    g = []
    with open(fn) as f:
        for line in f:
            p = line.split()
            if len(p) >= col+1: g.append(float(p[col]))
    return np.sort(np.array(g))

def sinc2(u):
    s = np.sinc(u); return s*s

def deficit_u1(x, K=8):
    n = x.size; L = x[-1]-x[0]
    u = (x - x[0])/(L/(n-1))
    lam = n/L
    O = np.zeros(K+1)
    for i in range(n):
        d = np.abs(u-u[i])
        w = np.where(d > 0, sinc2(d), 0.0)
        k = np.clip(np.floor(d).astype(int), 0, K)
        np.add.at(O, k, w)
    E = np.zeros(K+1)
    for k in range(K):
        val,_ = integrate.quad(lambda t: sinc2(k+t)*(1.0-sinc2(k+t)), 0.0, 1.0, limit=200)
        E[k] = 2.0*lam*lam*L*val
    tail,_ = integrate.quad(lambda t: sinc2(16.0+t)*(1.0-sinc2(16.0+t)), 0.0, np.inf, limit=200)
    E[K] = 2.0*lam*lam*L*tail
    D = (O-E)/n
    # normalized flat-window second moment (approx m2 = 1 + O/n  in density-1 units)
    m2 = 1.0 + (O[0]+O[1])/n   # u<2 window contribution to m2 (dominant)
    return D[0]+D[1], m2, n, L, lam

def run(tag, x):
    du1, m2, n, L, lam = deficit_u1(x)
    print(f"{tag:28s} n={n:5d}  gamma~[{x[0]:7.1f},{x[-1]:7.1f}]  lam={lam:6.3f}  def(u<1)={du1:+.4f}  m2(u<2)={m2:.4f}  (4/3=1.3333)")

x10 = load("../data/zeros_computed_10000.txt")
print("=== 5 disjoint windows of the 10000-zero file (internal rescale each) ===")
for i in range(5):
    run(f"window {2000*i+1}..{2000*i+2000}", x10[2000*i:2000*i+2000])
x1k = load("../data/zeros_1_1000.txt")
print("\n=== LMFDB 1000-zero file (independent data source) ===")
run("LMFDB all 1000", x1k)
run("LMFDB first 500", x1k[:500])
run("LMFDB last 500", x1k[500:])
print("\nnote: m2(u<2) is a *partial* second moment (u<2 pairs only) — used here only for sign/magnitude")
print("cross-check between windows, not as the global m2.")
