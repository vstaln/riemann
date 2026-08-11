#!/usr/bin/env python3
"""Family: lattice + d doubles at half-integer positions. f(j) = (5-4cos(pi j/256)) |B_A(j)|^2.
s_c = 256 - 2d, f(256) = 9 d^2. LP: min p1 s.t. rows + D(1)."""
import numpy as np
from scipy.optimize import linprog
import time

N = 256
j = np.arange(1, N+1)
factor = 5.0 - 4.0*np.cos(np.pi*j/N)     # (N,)

def subset_spectra(As, N):
    out = []
    for A in As:
        A = np.asarray(A)
        if len(A) == 0:
            out.append(np.zeros(N)); continue
        z = np.zeros(N, dtype=complex)
        for q in A:
            z += np.exp(2j*np.pi*j*q/N)
        out.append(np.abs(z)**2)
    return np.array(out)

def gen_family(per_d=400, max_d=60, seed=21):
    rng = np.random.default_rng(seed)
    As, ds = [], []
    for d in range(1, max_d+1):
        for t in range(per_d):
            As.append(rng.choice(256, size=d, replace=False))
            ds.append(d)
        for s in (1,2,4,8,16,32,64,128,3,5,7,9,17,33,65):
            q0 = rng.integers(0,256)
            As.append(np.array([(q0+s*m) % 256 for m in range(d)]))
            ds.append(d)
    return As, ds

As, ds = gen_family(per_d=250, max_d=60)
print(f"{len(As)} configs")
t0 = time.time()
B2 = subset_spectra(As, N)
print(f"spectra {time.time()-t0:.1f}s")
m = len(As)
F = np.zeros((m, N))
for c in range(m):
    F[c] = factor * B2[c]
s_c = np.array([256 - 2*d for d in ds], dtype=float)
# rows j=1..255, D(1) bound
Fb = N*N*(0.82395317+0.5) - N*(N-1)//2
A_ub, b_ub = [], []
for jj in range(N-1):
    A_ub.append(F[:, jj]); b_ub.append((jj+1)+3e-40)
    A_ub.append(-F[:, jj]); b_ub.append(-(jj+1)+3e-40)
A_ub.append(F[:, 255]); b_ub.append(Fb)
A_eq = np.ones((1, m)); b_eq = [1.0]
t0 = time.time()
res = linprog(s_c, A_ub=np.array(A_ub), b_ub=np.array(b_ub), A_eq=A_eq, b_eq=b_eq,
              bounds=[(0,None)]*m, method='highs')
print(f"LP {time.time()-t0:.1f}s success={res.success} msg={res.message}")
if res.success:
    fbar = res.x @ F
    print(f"min p1 = {res.fun/N:.12f}  (p0 = 0.6818286874638315)")
    print(f"D(1) = {fbar.sum()/N**2-0.5:.8f}  fbar(128) = {fbar[127]:.4f}  fbar(256) = {fbar[255]:.4f}")
    print(f"max row resid = {np.max(np.abs(fbar[:255]-np.arange(1,256))):.2e}")
    nz = np.argsort(-res.x)[:10]
    for c in nz:
        if res.x[c] > 1e-9:
            print(f"  w={res.x[c]:.6f} d={ds[c]} A={As[c][:8]}...")
else:
    # Chebyshev to see closeness
    cvar = np.zeros(m+1); cvar[-1] = 1
    A_ub2, b_ub2 = [], []
    for jj in range(N-1):
        row = np.zeros(m+1); row[:m] = F[:, jj]; row[-1] = -1; A_ub2.append(row); b_ub2.append(jj+1)
        row = np.zeros(m+1); row[:m] = -F[:, jj]; row[-1] = -1; A_ub2.append(row); b_ub2.append(-(jj+1))
    A_eq2 = np.concatenate([np.ones((1,m)), np.zeros((1,1))], axis=1); b_eq2=[1.0]
    resC = linprog(cvar, A_ub=np.array(A_ub2), b_ub=np.array(b_ub2), A_eq=A_eq2, b_eq=b_eq2, bounds=[(0,None)]*(m+1), method='highs')
    print(f"Chebyshev dist = {resC.fun:.4f}")
