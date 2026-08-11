#!/usr/bin/env python3
"""Sine-process Gram-matrix moments m2,m3,m4 at a given lambda (flat window), MC.
Usage: python sine_sim.py <lambda> <nsamp>
"""
import numpy as np, sys, time

la = float(sys.argv[1]) if len(sys.argv) > 1 else 1.0
NSAMP = int(sys.argv[2]) if len(sys.argv) > 2 else 300
L = 60.0
M = 1200
rng = np.random.default_rng(11)

xs = np.linspace(-L/2, L/2, M, endpoint=False)
dx = L/M
S = np.sinc((xs[:, None] - xs[None, :]))
K = S * dx
evals, evecs = np.linalg.eigh(K)
mask = evals > 1e-10
evals = evals[mask]; evecs = evecs[:, mask]
Psi = evecs * np.sqrt(dx)
r_max = Psi.shape[1]

def sample_config():
    inc = rng.random(r_max) < evals
    if not inc.any():
        return np.zeros(0)
    PsiJ = Psi[:, inc]
    r = PsiJ.shape[1]
    Pmm = np.einsum('ij,ij->i', PsiJ, PsiJ)
    chosen = []
    while len(chosen) < r:
        if chosen:
            X = np.array(chosen); PX = PsiJ[X, :]; A = PX @ PX.T
            PmX = PsiJ @ PX.T
            sol = np.linalg.solve(A, PmX.T)
            corr = np.einsum('mk,mk->m', PmX, sol.T)
            diag = np.clip(Pmm - corr, 0, None)
        else:
            diag = Pmm
        tot = diag.sum()
        if tot < 1e-9:
            break
        m = rng.choice(M, p=diag / tot)
        chosen.append(m)
    return xs[np.array(chosen)]

def moments(pts, la):
    n = pts.size
    if n < 4:
        return (0.0, 0.0, 0.0)
    d = pts[:, None] - pts[None, :]
    G = np.sinc(la * d)
    G2 = G @ G; G3 = G2 @ G; G4 = G3 @ G
    return (np.trace(G2)/n, np.trace(G3)/n, np.trace(G4)/n)

m2s, m3s, m4s = [], [], []
t0 = time.time()
for s in range(NSAMP):
    pts = sample_config()
    if pts.size >= 4:
        a, b, c = moments(pts, la)
        m2s.append(a); m3s.append(b); m4s.append(c)
    if (s+1) % 50 == 0:
        print(f"  {s+1}/{NSAMP} done ({time.time()-t0:.0f}s)", flush=True)

m2s = np.array(m2s); m3s = np.array(m3s); m4s = np.array(m4s)
se = lambda a: a.std() / np.sqrt(a.size)
print(f"lambda={la}:  m2 = {m2s.mean():.5f} +- {se(m2s):.5f}   m3 = {m3s.mean():.5f} +- {se(m3s):.5f}   m4 = {m4s.mean():.5f} +- {se(m4s):.5f}")
