#!/usr/bin/env python3
"""Probe C — 'Stefan front' check: does the short-range (u<1) finite-T deficit front move
with the height window T, or is it stationary? (P6 diagnostic; R6 showed the deficit
concentrates at u<1 in the GLOBAL rescale. Here we split the 10000-zero file into two
disjoint height windows, rescale each to density 1, and compare the banded deficit profile.)
Predictions: (i) stationary front (fixed u~0.4-1 band) => deficit is an O(1) short-range
arithmetic structure with a fixed cutoff — a 'Stefan front pinned at the material boundary';
(ii) front shrinking with T => the deficit is a true finite-T effect approaching GUE."""
import numpy as np
from scipy import integrate

def load(fn):
    g = []
    with open(fn) as f:
        for line in f:
            p = line.split()
            if len(p) >= 2: g.append(float(p[1]))
    return np.sort(np.array(g))

def sinc2(u):
    s = np.sinc(u); return s*s

def banded_profile(x, K=12):
    n = x.size; L = x[-1] - x[0]; lam = n/L
    u = (x - x[0]) / (L/(n-1))
    O = np.zeros(K+1)
    for i in range(n):
        d = np.abs(u - u[i])
        w = np.where(d > 0, sinc2(d), 0.0)
        k = np.clip(np.floor(d).astype(int), 0, K)
        np.add.at(O, k, w)
    E = np.zeros(K+1)
    for k in range(K):
        val, _ = integrate.quad(lambda t: sinc2(k+t)*(1.0-sinc2(k+t)), 0.0, 1.0)
        E[k] = 2.0*lam*lam*L*val
    tail, _ = integrate.quad(lambda t: sinc2(16.0+t)*(1.0-sinc2(16.0+t)), 0.0, np.inf)
    E[K] = 2.0*lam*lam*L*tail
    return O, E, n, L, lam

def report(tag, x):
    O, E, n, L, lam = banded_profile(x)
    D = (O - E)/n
    print(f"--- {tag}: n={n} L={L:.1f} lam={lam:.4f} ---")
    print("band:   ", "  ".join(f"{k:3d}" for k in range(7)))
    print("def/n:  ", "  ".join(f"{D[k]:+.4f}" for k in range(7)))
    cum_u1 = D[0] + D[1]
    rest = D[2:7].sum()
    print(f"deficit u<1: {cum_u1:+.4f}   u in [1,7): {rest:+.4f}")
    # 'front': largest u where |def| still > 30% of the u<1 magnitude
    mag = abs(cum_u1)
    front = 0
    for k in range(1, 7):
        if abs(D[k]) > 0.3*mag: front = k
    print(f"front (last band with |def|>0.3*|deficit u<1|): u in [{front},{front+1})")
    return D

x = load("../data/zeros_computed_10000.txt")
print(f"total n={x.size}, gamma range [{x[0]:.1f},{x[-1]:.1f}]")
D1 = report("window A: zeros 1..4000 (gamma<=~4300)", x[:4000])
D2 = report("window B: zeros 6000..10000 (gamma>=~5900)", x[6000:])
print("\nreading: if the front (u cutoff) is the same in both windows and the per-band profile")
print("is similar, the short-range deficit is a stationary arithmetic structure (fixed front);")
print("if the deficit magnitude shrinks with T with the same front, it is a genuine finite-T")
print("effect that decays in place (the 'aging' reading).")
