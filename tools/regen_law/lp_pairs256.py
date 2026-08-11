#!/usr/bin/env python3
"""
Primal LP for the N=256 law, family = {128-k antipodal pairs at even grid + k half-integer special doubles}.
Open-band spectrum (j != 128):  f_c(j) = 4 |sum_{q in Q} zeta^{j q}|^2,  Q = integer parts of special points (size k).
f_c(128) = 4(128-k)^2 + 4(evens-odds in Q)^2 ;  f_c(256) = 16(64-k)^2 ;  s_c = 256 - 2k.
LP:  min p1 = sum w_c s_c / 256  s.t.  |sum w_c f_c(j) - j| <= tau (j=1..255),  sum w_c f_c(256) <= 54126.7,  sum w = 1.
Independent of the enclosures (family from the math; enclosures only for the final comparison).
"""
import numpy as np
from scipy.optimize import linprog
import json, sys, time

N = 256

def zeta_spectra(Q_list, N=256):
    """|sum_{q in Q} zeta^{j q}|^2 for j = 1..N, for each Q. Vectorized-ish."""
    j = np.arange(1, N+1)
    out = []
    for Q in Q_list:
        Q = np.asarray(Q)
        if len(Q) == 0:
            out.append(np.zeros(N)); continue
        # sum_q zeta^{j q} = sum_q exp(2 pi i j q / 256)  (q integer in 0..255)
        z = np.zeros(N, dtype=complex)
        for q in Q:
            z += np.exp(2j*np.pi*j*q/N)
        out.append(np.abs(z)**2)
    return np.array(out)

def gen_family(max_k=64, per_k=120, seed=7, include_structured=True):
    rng = np.random.default_rng(seed)
    configs = []  # (k, Q tuple, f128, f256)
    for k in range(0, max_k+1):
        if k == 0:
            configs.append((0, (), 4*128**2, 16*64**2))
            continue
        seen = set()
        added = 0
        tries = 0
        while added < per_k and tries < per_k*30:
            tries += 1
            Q = tuple(sorted(rng.choice(256, size=k, replace=False).tolist()))
            if Q in seen: continue
            seen.add(Q)
            ev = sum(1 for q in Q if q % 2 == 0); od = k - ev
            f128 = 4*(128-k)**2 + 4*(ev-od)**2
            f256 = 16*(64-k)**2
            configs.append((k, Q, f128, f256))
            added += 1
        # structured: arithmetic progression Q = {q0 + s*m mod 256}
        if include_structured:
            for s in (1, 2, 4, 8, 16, 32, 64, 128, 3, 5, 7, 9, 17, 33, 65, 129):
                if k > 0 and s*k < 512:
                    q0 = rng.integers(0, 256)
                    Q = tuple(sorted((q0 + s*m) % 256 for m in range(k)))
                    ev = sum(1 for q in Q if q % 2 == 0); od = k - ev
                    f128 = 4*(128-k)**2 + 4*(ev-od)**2
                    f256 = 16*(64-k)**2
                    configs.append((k, Q, f128, f256))
    return configs

def build_matrix(configs):
    ks = [c[0] for c in configs]
    Qs = [c[1] for c in configs]
    sp = zeta_spectra(Qs)          # (m, 256)
    m = len(configs)
    F = np.zeros((m, N))
    for cidx in range(m):
        F[cidx, :127] = 4*sp[cidx, :127]       # j=1..127
        F[cidx, 127] = configs[cidx][2]        # j=128
        F[cidx, 128:] = 4*sp[cidx, 128:]       # j=129..255
        F[cidx, 255] = configs[cidx][3]        # j=256 (overwrite)
    s_c = np.array([256 - 2*k for k in ks], dtype=float)
    return F, s_c, ks, Qs

def solve(F, s_c, tau=0.0, F256_bound=54126.7, verbose=True):
    m = len(F)
    A_ub, b_ub = [], []
    for jj in range(N-1):
        A_ub.append(F[:, jj]); b_ub.append((jj+1) + tau)
        A_ub.append(-F[:, jj]); b_ub.append(-(jj+1) + tau)
    A_ub.append(F[:, 255]); b_ub.append(F256_bound)
    A_eq = np.ones((1, m)); b_eq = np.array([1.0])
    t0 = time.time()
    res = linprog(s_c, A_ub=np.array(A_ub), b_ub=np.array(b_ub), A_eq=A_eq, b_eq=b_eq,
                  bounds=[(0,None)]*m, method='highs')
    if verbose:
        print(f"  LP solved in {time.time()-t0:.1f}s: success={res.success} msg={res.message}")
    if res.success:
        fbar = res.x @ F
        p1 = res.fun / N
        D1 = fbar.sum()/N**2 - 0.5
        print(f"  min p1 = {p1:.12f}   (target 0.6818286874638315)")
        print(f"  D(1) = {D1:.12f}  (bound 0.82395317)   fbar(256) = {fbar[255]:.4f} (bound {F256_bound})")
        print(f"  fbar(128) = {fbar[127]:.6f} (target 128)   max row resid = {np.max(np.abs(fbar[:255]-np.arange(1,256))):.2e}")
        return res, fbar
    return res, None

if __name__ == '__main__':
    tau = 3e-40
    F256_bound = 256*256*(0.82395317+0.5) - 256*255//2   # from |D(1)| <= d1 with rows pinned
    print(f"F256_bound = {F256_bound}")
    configs = gen_family(max_k=64, per_k=150)
    print(f"generated {len(configs)} configs")
    F, s_c, ks, Qs = build_matrix(configs)
    res, fbar = solve(F, s_c, tau=tau, F256_bound=F256_bound)
