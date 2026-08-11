#!/usr/bin/env python3
"""Pairs+specials family with MIXED fractional parts for specials (break f(1)=f(255)).
Config: (128-k) antipodal pairs at even grid (u=0) + k special doubles at (q + u), u in {1/4, 3/4}.
Odd-j spectrum: f_c(j) = 4 |sum_{specials} e^{2pi i j (q+u)/256}|^2.
s_c = 256 - 2k. LP: min p1 s.t. rows + D(1)."""
import numpy as np
from scipy.optimize import linprog
import time

N = 256

def spectra_pairs(Qs, Us, k_list):
    """Qs: list of arrays (integer parts of specials), Us: list of arrays (frac parts).
    Returns F (m, N): f_c(j) for j=1..N using the pairs+specials formula (pairs at even grid)."""
    m = len(Qs)
    j = np.arange(1, N+1)
    F = np.zeros((m, N))
    for c in range(m):
        Q = Qs[c]; U = Us[c]; k = k_list[c]
        # special DFT: sum_a 2 e^{2 pi i j (q_a + u_a)/256}
        z = np.zeros(N, dtype=complex)
        for q, u in zip(Q, U):
            z += 2*np.exp(2j*np.pi*j*(q + u)/N)
        # odd j: pairs cancel -> f = |z|^2 ; even j: pairs contribute 2*(128-k) * e^{2 pi i j * (even)/256}... 
        # pairs at even grid positions p (128-k of them), antipodal at p+128.
        # even j: sum_pairs e^{2pi i j p/256} = sum_{p in P} e^{2 pi i j p/256} + e^{2 pi i j (p+128)/256}
        #   = sum_p e^{2 pi i j p/256} (1 + e^{pi i j}) ; j even -> 2 sum_p e^{2 pi i j p/256}.
        # Choose P = first (128-k) even positions {0,2,...,2(128-k)-2}: sum = (1-e^{2 pi i j (128-k)/128})/(1-e^{2 pi i j/128}) * ... 
        # For simplicity use P = every other even position... use the formula with a clean set:
        # P = {2r : r=0..128-k-1}  -> sum_p e^{2 pi i j p/256} = sum_r e^{2 pi i j r/128} = 0 unless 128 | j.
        # So for even j < 256 (j != 128): pairs contribute 0; for j=128: 2(128-k); for j=256: 2(128-k).
        f = np.abs(z)**2
        # j=128: |2(128-k) + z(128)|^2
        z128 = z[127]
        f[127] = abs(2*(128-k) + z128)**2
        # j=256: |2(128-k) + z(256)|^2
        f[255] = abs(2*(128-k) + z[255])**2
        F[c] = f
    return F

def gen_family(per_k=200, max_k=64, seed=11):
    rng = np.random.default_rng(seed)
    Qs, Us, ks = [], [], []
    fracs = (0.25, 0.75)
    for k in range(0, max_k+1):
        for t in range(per_k):
            q = rng.choice(256, size=k, replace=False)
            u = rng.choice(fracs, size=k)
            Qs.append(q); Us.append(u); ks.append(k)
        # structured: quarter-integer arithmetic progressions
        for s in (1,2,4,8,16,32,64,128,3,5,7,9,17):
            if k == 0: break
            q0 = rng.integers(0,256)
            q = np.array([(q0 + s*m) % 256 for m in range(k)])
            u = np.array([0.25]*k)
            Qs.append(q); Us.append(u); ks.append(k)
            u2 = np.array([0.25 if m % 2 == 0 else 0.75 for m in range(k)])
            Qs.append(q); Us.append(u2); ks.append(k)
    return Qs, Us, ks

def solve(F, s_c, tau=0.0, Fb=None, verbose=True):
    m = len(F)
    A_ub, b_ub = [], []
    for jj in range(N-1):
        A_ub.append(F[:, jj]); b_ub.append((jj+1)+tau)
        A_ub.append(-F[:, jj]); b_ub.append(-(jj+1)+tau)
    if Fb is not None:
        A_ub.append(F[:, 255]); b_ub.append(Fb)
    A_eq = np.ones((1, m)); b_eq = [1.0]
    t0=time.time()
    res = linprog(s_c, A_ub=np.array(A_ub), b_ub=np.array(b_ub), A_eq=A_eq, b_eq=b_eq,
                  bounds=[(0,None)]*m, method='highs')
    if verbose: print(f"  LP {time.time()-t0:.1f}s success={res.success} msg={res.message}")
    if res.success:
        fbar = res.x @ F
        print(f"  min p1 = {res.fun/N:.12f}  D(1)={fbar.sum()/N**2-0.5:.8f}  fbar(128)={fbar[127]:.4f} fbar(256)={fbar[255]:.4f}")
        return res, fbar
    return res, None

Qs, Us, ks = gen_family(per_k=150, max_k=64)
print(f"{len(Qs)} configs")
F = spectra_pairs(Qs, Us, ks)
s_c = np.array([256-2*k for k in ks], dtype=float)
Fb = N*N*(0.82395317+0.5) - N*(N-1)//2
res, fbar = solve(F, s_c, tau=3e-40, Fb=Fb)
if not res.success:
    # Chebyshev: which rows are hardest?
    m = len(F)
    c = np.zeros(m+1); c[-1] = 1
    A_ub = []; b_ub = []
    for jj in range(N-1):
        row = np.zeros(m+1); row[:m] = F[:, jj]; row[-1] = -1; A_ub.append(row); b_ub.append(jj+1)
        row = np.zeros(m+1); row[:m] = -F[:, jj]; row[-1] = -1; A_ub.append(row); b_ub.append(-(jj+1))
    A_eq = np.concatenate([np.ones((1,m)), np.zeros((1,1))], axis=1); b_eq = [1.0]
    resC = linprog(c, A_ub=np.array(A_ub), b_ub=np.array(b_ub), A_eq=A_eq, b_eq=b_eq, bounds=[(0,None)]*(m+1), method='highs')
    print(f"Chebyshev dist = {resC.fun:.4f}")
    # find rows with largest violation at best fit
    w = resC.x[:m]; t = resC.x[-1]
    fbar = w @ F
    viol = np.abs(fbar[:255] - np.arange(1,256))
    worst = np.argsort(-viol)[:12]
    print("worst rows:", [(int(j)+1, round(float(viol[j]),3)) for j in worst])
    print("fbar at worst rows:", np.round(fbar[worst], 3))
