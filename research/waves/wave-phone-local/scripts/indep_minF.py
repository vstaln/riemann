#!/usr/bin/env python3
# INDEPENDENT minimization of the local 6-gap functional F6 for the record claim.
# Spec (ainta proof.md eq. 4.1, with the record's alpha=1.49 and per-gap pressure p=1/1320):
#   w(x) = k(x)^2,  k(x) = K(x)/K(0),  K(x) = sin((2 pi x - a)/2)/(2 pi x - a) + sin((2 pi x + a)/2)/(2 pi x + a)
#   F6(g_1..g_6) = p * sum(g_i) + sum_{s=1..6} (2/(7-s)) * sum_{i=1..7-s} w(g_i + ... + g_{i+s-1})
# Claim: min F6 >= 0.00806 over all g_i >= 0; 0.008065-0.00807 allegedly fail.
# Test my reconstruction: does min F6 come out near 0.00806?
import numpy as np
from scipy.optimize import differential_evolution, minimize

ALPHA = 1.49
P = 1.0/1320.0

def k(x):
    x = np.asarray(x, dtype=float)
    t1 = 2*np.pi*x - ALPHA
    t2 = 2*np.pi*x + ALPHA
    out = np.zeros_like(x)
    m1 = np.abs(t1) > 1e-12
    m2 = np.abs(t2) > 1e-12
    out[m1] += np.sin(t1[m1]/2)/t1[m1]
    out[m2] += np.sin(t2[m2]/2)/t2[m2]
    out[~m1] += 0.5
    out[~m2] += 0.5
    return out/k(0.0) if False else out/_k0()

_K0 = None
def _k0():
    global _K0
    if _K0 is None:
        a = ALPHA
        _K0 = 2*np.sin(a/2)/a
    return _K0

def w(x):
    kk = k(x)
    return kk*kk

def F6(g, p=P):
    g = np.asarray(g, dtype=float)
    total = p * np.sum(g)
    for s in range(1, 7):
        coeff = 2.0/(7.0-s)
        for i in range(0, 7-s):
            span = np.sum(g[i:i+s])
            total += coeff * w(span)
    return total

# ---- sanity: uniform gaps ----
print("=== F6 reconstruction sanity ===")
for gv in [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]:
    print(f"  F6(all gaps = {gv}) = {F6([gv]*6):.8f}")

# ---- global search ----
print("\n=== global min search (differential evolution) ===")
bounds = [(0.0, 6.0)]*6
res = differential_evolution(lambda g: F6(g), bounds, seed=7, tol=1e-10,
                             polish=True, workers=1, maxiter=3000, popsize=25)
print("  DE min =", res.fun, "at", np.round(res.x, 5))

# local refinement with more precision
def refine(g0):
    g = np.asarray(g0, float)
    best = (F6(g), g.copy())
    for _ in range(6):
        r = minimize(F6, best[1], method='Nelder-Mead',
                     options={'xatol':1e-12, 'fatol':1e-15, 'maxiter':20000})
        if r.fun < best[0]:
            best = (r.fun, r.x.copy())
    return best
bm = refine(res.x)
print("  refined min =", bm[0], "at", np.round(bm[1], 6))

# ---- also check a few candidate critical points by brute coarse grid ----
print("\n=== coarse grid scan (uniform-ish) ===")
best = 1e9; bg = None
for a in np.arange(0.0, 4.01, 0.25):
    for b in np.arange(0.0, 4.01, 0.25):
        # pattern a,b,b,b,b,a symmetric-ish and constant
        for pat in ([a]*6, [a,b]*3):
            f = F6(pat)
            if f < best:
                best = f; bg = pat
print(f"  coarse best = {best:.8f} at {np.round(bg,3)}")

print("\n  FINAL min F6 =", bm[0])
print(f"  vs claimed floor 0.00806: min {'ABOVE' if bm[0] > 0.00806 else 'BELOW'} 0.00806 by {abs(bm[0]-0.00806):.3e}")
print(f"  vs 0.008065 boundary claim: min {bm[0]:.10f}")
