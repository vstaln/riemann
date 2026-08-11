#!/usr/bin/env python3
"""Scale-up with diagnostics, using common.py."""
import numpy as np
from scipy.optimize import linprog
import sys; sys.path.insert(0, '/home/vstaln/riemann/tools/regen_law')
from common import gen_family_vec, spectra, dedupe

def run(N, n_configs, F_bound, seed, tau=0.0, max_d_frac=0.25):
    X, M, s_c = gen_family_vec(N, n_configs, seed, max_d_frac)
    F = spectra(X, M, N)
    Fm, sc = dedupe(F, s_c)
    m = len(Fm)
    A_ub, b_ub = [], []
    for jj in range(N-1):
        A_ub.append(Fm[:, jj]); b_ub.append((jj+1) + tau)
        A_ub.append(-Fm[:, jj]); b_ub.append(-(jj+1) + tau)
    if F_bound is not None:
        A_ub.append(Fm[:, N-1]); b_ub.append(F_bound)
    A_eq = np.ones((1, m)); b_eq = np.array([1.0])
    res = linprog(sc, A_ub=np.array(A_ub), b_ub=np.array(b_ub), A_eq=A_eq, b_eq=b_eq,
                  bounds=[(0,None)]*m, method='highs')
    return res, Fm, sc

d1 = 0.82395317
for N, nc, seed in [(64, 2500, 1), (128, 2500, 2), (256, 2500, 3)]:
    F_bound = N*N*(d1+0.5) - N*(N-1)//2
    res0, Fm0, sc0 = run(N, nc, None, seed)
    print(f"N={N}: {len(Fm0)} configs. Feasible (no D1 bound): {res0.success}")
    res, Fm, sc = run(N, nc, F_bound, seed)
    print(f"  with D(1) bound: feasible = {res.success}, msg = {res.message}")
    if res.success:
        p1 = res.fun / N
        fbar = res.x @ Fm
        D1 = fbar.sum()/N**2 - 0.5
        print(f"  min p1 = {p1:.8f}   D(1) at optimum = {D1:.8f} (bound {d1})   fbar(N)={fbar[N-1]:.4f}")
        print(f"  max row residual = {np.max(np.abs(fbar[:N-1] - np.arange(1,N))):.2e}")
    # Chebyshev distance of the target to the convex hull
    m = len(Fm0)
    c = np.zeros(m+1); c[-1] = 1
    A_ub = []; b_ub = []
    for jj in range(N-1):
        row = np.zeros(m+1); row[:m] = Fm0[:, jj]; row[-1] = -1; A_ub.append(row); b_ub.append(jj+1)
        row = np.zeros(m+1); row[:m] = -Fm0[:, jj]; row[-1] = -1; A_ub.append(row); b_ub.append(-(jj+1))
    A_eq = np.concatenate([np.ones((1,m)), np.zeros((1,1))], axis=1); b_eq = [1.0]
    resC = linprog(c, A_ub=np.array(A_ub), b_ub=np.array(b_ub), A_eq=A_eq, b_eq=b_eq,
                   bounds=[(0,None)]*(m+1), method='highs')
    print(f"  Chebyshev distance target->conv hull: {resC.fun:.6e} (success={resC.success})")
    resP = linprog(sc0, A_eq=np.ones((1,m)), b_eq=[1.0], bounds=[(0,None)]*m, method='highs')
    print(f"  unconstrained min p1 (no rows): {resP.fun/N:.6f}")
