#!/usr/bin/env python3
"""ADJUDICATION of the Theorem-B/0.6725 contradiction flag.
(A) Recompute small-N min p1 under POINTWISE near-CUE rows |sum w f(j) - j| <= tau (the Lean rows),
    verifying the solution (config validity, residuals, D(1), E(1)).
(B) Recompute under the CUMULATIVE-DISCREPANCY parametrization: no pointwise rows; instead
    |D(1)| <= d1 and |E(1)| <= M(N) = 1/(6N^2) + tau/(2N)  (the certificate's actual data budget).
(C) Report N = 8/16/32/64/256 and adjudicate vs Theorem B (0.6725, PROVEN for the actual zeros).
"""
import numpy as np
from scipy.optimize import linprog
import sys
sys.path.insert(0, '/home/vstaln/riemann/tools/regen_law')
from common import gen_family_vec, spectra, dedupe

def solve_pointwise(N, configs, tau=3e-40, Fb=None):
    F, sc = dedupe(spectra(configs[0], configs[1], N), configs[2])
    m = len(F)
    A_ub, b_ub = [], []
    for jj in range(N-1):
        A_ub.append(F[:, jj]); b_ub.append((jj+1)+tau)
        A_ub.append(-F[:, jj]); b_ub.append(-(jj+1)+tau)
    if Fb is not None:
        A_ub.append(F[:, N-1]); b_ub.append(Fb)
    A_eq = np.ones((1, m)); b_eq = [1.0]
    res = linprog(sc, A_ub=np.array(A_ub), b_ub=np.array(b_ub), A_eq=A_eq, b_eq=b_eq,
                  bounds=[(0,None)]*m, method='highs')
    return res, F, sc

def solve_cumulative(N, configs, d1=0.82395317, tau=3e-40):
    """Constraints: |D(1)| <= d1, |E(1)| <= M(N). D(1)=sum_j S(j)/N - 1/2 = sum f(j)/N^2 - 1/2.
    E(1) = sum_j s_j (1 - j/N) - 1/6 = sum_j (f(j)/N)(1-j/N)/N - 1/6 = sum f(j)(1-j/N)/N^2 - 1/6."""
    F, sc = dedupe(spectra(configs[0], configs[1], N), configs[2])
    m = len(F)
    M = 1/(6*N*N) + tau/(2*N)
    A_ub, b_ub = [], []
    # |D(1)|: |sum f(j)/N^2 - 1/2| <= d1
    row = F.sum(axis=1)/N**2; A_ub.append(row); b_ub.append(d1 + 0.5)
    A_ub.append(-row); b_ub.append(d1 - 0.5)
    # |E(1)|: |sum f(j)(1-j/N)/N^2 - 1/6| <= M
    wts = np.array([(1 - (jj+1)/N) for jj in range(N)])
    rowE = F @ wts / N**2
    A_ub.append(rowE); b_ub.append(M + 1/6)
    A_ub.append(-rowE); b_ub.append(M - 1/6)
    A_eq = np.ones((1, m)); b_eq = [1.0]
    res = linprog(sc, A_ub=np.array(A_ub), b_ub=np.array(b_ub), A_eq=A_eq, b_eq=b_eq,
                  bounds=[(0,None)]*m, method='highs')
    return res, F, sc

print("="*70)
print("(A) POINTWISE rows |sum w f(j) - j| <= 3e-40,  j = 1..N-1  (+ D(1) <= d1)")
print("="*70)
for N, nc in [(8, 2000), (16, 2000), (32, 2000)]:
    cfg = gen_family_vec(N, nc, seed=N)
    Fb = N*N*(0.82395317+0.5) - N*(N-1)//2
    res, F, sc = solve_pointwise(N, cfg, tau=3e-40, Fb=Fb)
    if res.success:
        fbar = res.x @ F
        # verify the mixture is a valid near-CUE law
        D1 = fbar.sum()/N**2 - 0.5
        E1 = (fbar @ np.array([1-(jj+1)/N for jj in range(N)]))/N**2 - 1/6
        maxrow = np.max(np.abs(fbar[:N-1] - np.arange(1, N)))
        nz = (res.x > 1e-9).sum()
        p1 = res.fun/N
        print(f"N={N}: min p1 = {p1:.10f}  | max row resid = {maxrow:.2e} | D(1)={D1:.6f} | "
              f"E(1)={E1:.6f} (M={1/(6*N*N):.6f}) | #positive-weight configs = {nz}")
        # check config validity: sum marks = N for the support configs
        X, M_, s_ = cfg
        for c in np.where(res.x > 1e-9)[0][:3]:
            print(f"   support: w={res.x[c]:.5f} s_c={int(s_[c])} sum marks={M_[c].sum():.0f}")
    else:
        print(f"N={N}: INFEASIBLE (family too poor): {res.message}")

print()
print("="*70)
print("(B) CUMULATIVE-DISCREPANCY data budget: |D(1)|<=0.82395317, |E(1)|<=1/(6N^2)+tau/(2N)")
print("    (no pointwise rows; the certificate's actual integrated data)")
print("="*70)
for N, nc in [(8, 2000), (16, 2000), (32, 2000), (64, 2000), (128, 2000)]:
    cfg = gen_family_vec(N, nc, seed=100+N)
    res, F, sc = solve_cumulative(N, cfg)
    if res.success:
        fbar = res.x @ F
        p1 = res.fun/N
        D1 = fbar.sum()/N**2 - 0.5
        E1 = (fbar @ np.array([1-(jj+1)/N for jj in range(N)]))/N**2 - 1/6
        print(f"N={N}: min p1 = {p1:.10f}  | D(1)={D1:.6f} E(1)={E1:.6f} (|E1|<=M={1/(6*N*N):.6f}) | rows NOT pinned")
    else:
        print(f"N={N}: INFEASIBLE: {res.message}")
