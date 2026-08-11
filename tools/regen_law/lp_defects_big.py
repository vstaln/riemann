#!/usr/bin/env python3
"""Largest family attempt: lattice 0..255 + defects.
Defects: (a) d doubles at (q+u), u in {0,1/2}; (b) e moved simples at (q+u), u in {1/2,1/4,3/4,1/3,2/3}.
Z(j) = sum_doubles (2 e^{2pi i j u/256} - 1) w^{j q} + sum_moved (e^{2pi i j u/256} - 1) w^{j q}.
s_c = 256 - 2d. LP: min p1 s.t. rows + D(1)."""
import numpy as np
from scipy.optimize import linprog
import time

N = 256
j = np.arange(1, N+1)
US2 = (0.0, 0.5)
US1 = (0.5, 0.25, 0.75, 1/3, 2/3)

def cfg_spectrum(dqs, dus, eqs, eus):
    z = np.zeros(N, dtype=complex)
    for q, u in zip(dqs, dus):
        z += (2*np.exp(2j*np.pi*j*u/N) - 1)*np.exp(2j*np.pi*j*q/N)
    for q, u in zip(eqs, eus):
        z += (np.exp(2j*np.pi*j*u/N) - 1)*np.exp(2j*np.pi*j*q/N)
    return np.abs(z)**2

def gen(per=150, max_d=40, max_e=24, seed=41):
    rng = np.random.default_rng(seed)
    out = []
    for _ in range(per*20):
        d = int(rng.integers(0, max_d+1))
        e = int(rng.integers(0, max_e+1))
        tot = d + e
        qs = rng.choice(256, size=tot, replace=False)
        dus = rng.choice(US2, size=d) if d else np.array([])
        eus = rng.choice(US1, size=e) if e else np.array([])
        out.append((qs[:d], dus, qs[d:], eus))
    return out

configs = gen(per=150)
print(f"{len(configs)} configs")
t0 = time.time()
F = np.array([cfg_spectrum(*c) for c in configs])
print(f"spectra {time.time()-t0:.1f}s")
ds = np.array([len(c[0]) for c in configs])
s_c = np.array([256-2*d for d in ds], dtype=float)
Fb = N*N*(0.82395317+0.5) - N*(N-1)//2
m = len(F)
A_ub, b_ub = [], []
for jj in range(N-1):
    A_ub.append(F[:, jj]); b_ub.append((jj+1)+3e-40)
    A_ub.append(-F[:, jj]); b_ub.append(-(jj+1)+3e-40)
A_ub.append(F[:, 255]); b_ub.append(Fb)
A_eq = np.ones((1,m)); b_eq=[1.0]
t0=time.time()
res = linprog(s_c, A_ub=np.array(A_ub), b_ub=np.array(b_ub), A_eq=A_eq, b_eq=b_eq, bounds=[(0,None)]*m, method='highs')
print(f"LP {time.time()-t0:.1f}s success={res.success}")
if res.success:
    fbar = res.x @ F
    print(f"min p1 = {res.fun/N:.12f}  (p0 = 0.6818286874638315)")
    print(f"D(1)={fbar.sum()/N**2-0.5:.8f} fbar(128)={fbar[127]:.4f} fbar(256)={fbar[255]:.4f} resid={np.max(np.abs(fbar[:255]-np.arange(1,256))):.2e}")
    nz = np.argsort(-res.x)[:8]
    for c in nz:
        if res.x[c] > 1e-9:
            print(f"  w={res.x[c]:.6f} d={len(configs[c][0])} e={len(configs[c][2])}")
else:
    cvar = np.zeros(m+1); cvar[-1]=1
    A_ub2, b_ub2 = [], []
    for jj in range(N-1):
        row=np.zeros(m+1); row[:m]=F[:,jj]; row[-1]=-1; A_ub2.append(row); b_ub2.append(jj+1)
        row=np.zeros(m+1); row[:m]=-F[:,jj]; row[-1]=-1; A_ub2.append(row); b_ub2.append(-(jj+1))
    A_eq2 = np.concatenate([np.ones((1,m)), np.zeros((1,1))], axis=1); b_eq2=[1.0]
    resC = linprog(cvar, A_ub=np.array(A_ub2), b_ub=np.array(b_ub2), A_eq=A_eq2, b_eq=b_eq2, bounds=[(0,None)]*(m+1), method='highs')
    print(f"Chebyshev dist = {resC.fun:.4f}")
