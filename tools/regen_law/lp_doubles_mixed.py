#!/usr/bin/env python3
"""Family: lattice + d doubles at (q_a + u_a), u_a mixed in {0,1/2,1/4,3/4,1/3,2/3}.
Z(j) = sum_a (2 e^{2 pi i j u_a/256} - 1) omega^{j q_a};  f(j) = |Z(j)|^2.
s_c = 256 - 2d. LP: min p1 s.t. rows j=1..255 exact + D(1) bound."""
import numpy as np
from scipy.optimize import linprog
import time

N = 256
j = np.arange(1, N+1)
US = (0.0, 0.5, 0.25, 0.75, 1/3, 2/3, 0.125, 0.375, 0.625, 0.875)

def config_spectrum(qs, us):
    z = np.zeros(N, dtype=complex)
    for q, u in zip(qs, us):
        z += (2*np.exp(2j*np.pi*j*u/N) - 1)*np.exp(2j*np.pi*j*q/N)
    return np.abs(z)**2

def gen_family(per_d=200, max_d=60, seed=31):
    rng = np.random.default_rng(seed)
    qs_list, us_list, ds = [], [], []
    for d in range(1, max_d+1):
        for t in range(per_d):
            qs = rng.choice(256, size=d, replace=False)
            us = rng.choice(US, size=d)
            qs_list.append(qs); us_list.append(us); ds.append(d)
        # structured: all u=1/2, u alternating, u in {0,1/2}
        for s in (1,2,4,8,16,32,64,128,3,5,7,9):
            q0 = rng.integers(0,256)
            qs = np.array([(q0+s*m) % 256 for m in range(d)])
            for us in (np.full(d, 0.5), np.array([0.5 if m%2==0 else 0.25 for m in range(d)]),
                       np.array([0.0 if m%2==0 else 0.5 for m in range(d)]),
                       np.array([0.25 if m%2==0 else 0.75 for m in range(d)])):
                qs_list.append(qs); us_list.append(us); ds.append(d)
    return qs_list, us_list, ds

qs_list, us_list, ds = gen_family(per_d=150, max_d=60)
print(f"{len(qs_list)} configs")
t0 = time.time()
F = np.array([config_spectrum(q,u) for q,u in zip(qs_list, us_list)])
print(f"spectra {time.time()-t0:.1f}s")
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
print(f"LP {time.time()-t0:.1f}s success={res.success} msg={res.message}")
if res.success:
    fbar = res.x @ F
    print(f"min p1 = {res.fun/N:.12f}  (p0 = 0.6818286874638315)")
    print(f"D(1)={fbar.sum()/N**2-0.5:.8f} fbar(128)={fbar[127]:.4f} fbar(256)={fbar[255]:.4f} resid={np.max(np.abs(fbar[:255]-np.arange(1,256))):.2e}")
    nz = np.argsort(-res.x)[:10]
    for c in nz:
        if res.x[c] > 1e-9:
            print(f"  w={res.x[c]:.6f} d={ds[c]} us={np.round(us_list[c][:6],4)}")
else:
    cvar = np.zeros(m+1); cvar[-1] = 1
    A_ub2, b_ub2 = [], []
    for jj in range(N-1):
        row = np.zeros(m+1); row[:m] = F[:, jj]; row[-1] = -1; A_ub2.append(row); b_ub2.append(jj+1)
        row = np.zeros(m+1); row[:m] = -F[:, jj]; row[-1] = -1; A_ub2.append(row); b_ub2.append(-(jj+1))
    A_eq2 = np.concatenate([np.ones((1,m)), np.zeros((1,1))], axis=1); b_eq2=[1.0]
    resC = linprog(cvar, A_ub=np.array(A_ub2), b_ub=np.array(b_ub2), A_eq=A_eq2, b_eq=b_eq2, bounds=[(0,None)]*(m+1), method='highs')
    print(f"Chebyshev dist = {resC.fun:.4f}")
    if resC.success:
        w = resC.x[:m]
        fbar = w @ F
        viol = np.abs(fbar[:255]-np.arange(1,256))
        worst = np.argsort(-viol)[:10]
        print("worst rows:", [(int(wi)+1, round(float(viol[wi]),2)) for wi in worst])
