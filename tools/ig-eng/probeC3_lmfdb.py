#!/usr/bin/env python3
"""Cross-check the u<1 deficit sign/magnitude on the independent LMFDB 1000-zero file."""
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
    return D[0]+D[1], D[0], D[1], n, L, lam

x = load("../data/zeros_1_1000.txt")
for tag, sl in [("LMFDB all 1000 (gamma<=1419)", slice(None)),
                ("LMFDB first 500", slice(0,500)),
                ("LMFDB last 500", slice(500,1000)),
                ("LMFDB 600..1000", slice(600,1000))]:
    d01, d0, d1, n, L, lam = deficit_u1(x[sl])
    print(f"{tag:32s} n={n:4d}  gamma~[{x[sl][0]:7.1f},{x[sl][-1]:7.1f}]  lam={lam:5.3f}  "
          f"def(u<1)={d01:+.4f}  (band0 {d0:+.4f}, band1 {d1:+.4f})")
print("\nband0 = u in [0,1), band1 = u in [1,2). Negative = pair sum below sine-kernel (extra repulsion).")
