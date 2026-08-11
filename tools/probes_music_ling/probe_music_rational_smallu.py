#!/usr/bin/env python3
"""Follow-up to probe_music_rational.py: resolve the small-u pair correlation
(u < 0.5) where the sinc^2 weight concentrates and the fine scan did not print bins.

Findings recorded: g(u) below GUE for u < 0.45 (stronger repulsion), above GUE for
u in ~[0.45, 0.8); the u<1 integrated off-diagonal is consistent with this (ratio ~0.93
after the two-sided-integral factor 2, see probe_music_bands.py).
"""
import numpy as np

x = []
for line in open('data/zeros_computed_10000.txt'):
    p = line.split()
    if len(p) >= 2:
        x.append(float(p[1]))
x = np.sort(np.array(x))
n = x.size
L = x[-1] - x[0]
sp = L / (n - 1)
u = (x - x[0]) / sp
lam = n / (n - 1)

du = 0.02
U = 1.0
nb = int(np.ceil(U / du))
counts = np.zeros(nb)
for i in range(n):
    hi = np.searchsorted(u, u[i] + U, side='right')
    if hi > i + 1:
        d = u[i + 1:hi] - u[i]
        idx = (d / du).astype(int)
        np.add.at(counts, idx, 1.0)
g = np.zeros(nb)
for k in range(nb):
    umid = (k + 0.5) * du
    g[k] = counts[k] / (lam * lam * max((n - 1) - umid, 1e-9) * du)
s = np.sinc(np.arange(0.5, nb + 0.5) * du)
gue = 1 - s * s
print("u_center  g_meas   g_GUE    ratio(meas/GUE)")
for k in range(0, 45):
    um = (k + 0.5) * du
    print(f"{um:7.3f}  {g[k]:7.4f}  {gue[k]:7.4f}  {g[k]/gue[k]:6.3f}")
