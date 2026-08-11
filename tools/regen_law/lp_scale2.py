#!/usr/bin/env python3
"""Scale-up v2 with diagnostics."""
import numpy as np
from scipy.optimize import linprog
import sys
sys.path.insert(0, '/home/vstaln/riemann/tools/regen_law')
from lp_scale import gen_family_vec, spectra

def run(N, n_configs, F_bound, seed, tau=0.0):
    X, M, s_c = gen_family_vec(N, n_configs, seed)
    F = spectra(X, M, N)
    uniq = {}
    for c in range(len(X)):
        uniq.setdefault(tuple(np.round(F[c], 8)), (F[c], s_c[c]))
    items = list(uniq.values())
    m = len(items)
    Fm = np.array([f for f, s in items]); sc = np.array([s for f, s in items])
    A_ub, b_ub = [], []
    for jj in range(N-1):
        A_ub.append(Fm[:, jj]); b_ub.append((jj+1) + tau)
        A_ub.append(-Fm[:, jj]); b_ub.append(-(jj+1) + tau)
    if F_bound is not None:
        A_ub.append(Fm[:, N-1]); b_ub.append(F_bound)
    A_eq = np.ones((1, m)); b_eq = np.array([1.0])
    res = linprog(sc, A_ub=np.array(A_ub), b_ub=np.array(b_ub), A_eq=A_eq, b_eq=b_eq,
                  bounds=[(0,None)]*m, method='highs')
    return res, m

d1 = 0.82395317
for N, nc, seed in [(64, 2000, 1)]:
    F_bound = N*N*(d1+0.5) - N*(N-1)//2
    # feasibility without D(1) bound
    res0, m = run(N, nc, None, seed)
    print(f"N={N}: {m} configs. Feasible (no D1 bound): {res0.success}")
    if res0.success:
        fbar = res0.x @ np.array([f for f,s in list({tuple(np.round(f,8)): (f,s) for f,s in zip(*[(F,) for F in [None]])}.values())][:0]) if False else None
    res, m = run(N, nc, F_bound, seed)
    print(f"  with D(1) bound: feasible = {res.success}, msg = {res.message}")
    if res.success:
        Fm = np.array([f for f,s in items]) if False else None
    # inspect: distance from target spectrum to convex hull
    import itertools
    X, M, s_c = gen_family_vec(N, nc, seed)
    F = spectra(X, M, N)
    uniq = {}
    for c in range(len(X)):
        uniq.setdefault(tuple(np.round(F[c], 8)), (F[c], s_c[c]))
    items = list(uniq.values())
    Fm = np.array([f for f,s in items])
    target = np.arange(1, N)
    # min over w of max |sum w F[:,:N-1] - target|  (Chebyshev fit)
    m = len(items)
    # variables w, t
    c = np.zeros(m+1); c[-1] = 1
    A_ub = []; b_ub = []
    for jj in range(N-1):
        row = np.zeros(m+1); row[:m] = Fm[:, jj]; row[-1] = -1; A_ub.append(row); b_ub.append(target[jj])
        row = np.zeros(m+1); row[:m] = -Fm[:, jj]; row[-1] = -1; A_ub.append(row); b_ub.append(-target[jj])
    A_eq = np.concatenate([np.ones((1,m)), np.zeros((1,1))], axis=1); b_eq = [1.0]
    resC = linprog(c, A_ub=np.array(A_ub), b_ub=np.array(b_ub), A_eq=A_eq, b_eq=b_eq, bounds=[(0,None)]*(m)+[(0,None)], method='highs')
    print(f"  Chebyshev distance from target spectrum to conv-hull: {resC.fun:.6e}  (success={resC.success})")
    # also: what is the best achievable p1 ignoring rows (pure p1 minimization subject to sum w=1)?
    resP = linprog(sc, A_eq=np.ones((1,m)), b_eq=[1.0], bounds=[(0,None)]*m, method='highs')
    print(f"  unconstrained min p1 (no rows): {resP.fun/N:.6f}")
