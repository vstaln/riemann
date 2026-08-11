#!/usr/bin/env python3
"""Adjudication with CORRECT configs (sum marks = N)."""
import numpy as np
from scipy.optimize import linprog
import sys
sys.path.insert(0, '/home/vstaln/riemann/tools/regen_law')
from common2 import gen_valid_family, spectra_valid

def run(N, nc, seed, mode):
    X, M, s_c = gen_valid_family(N, nc, seed=seed)
    F = spectra_valid(X, M, N)
    m = len(F)
    A_ub, b_ub = [], []
    if mode == 'pointwise':
        for jj in range(N-1):
            A_ub.append(F[:, jj]); b_ub.append((jj+1)+3e-40)
            A_ub.append(-F[:, jj]); b_ub.append(-(jj+1)+3e-40)
        Fb = N*N*(0.82395317+0.5) - N*(N-1)//2
        A_ub.append(F[:, N-1]); b_ub.append(Fb)
    else:  # cumulative
        wts = np.array([(1 - (jj+1)/N) for jj in range(N)])
        Mv = 1/(6*N*N) + 3e-40/(2*N)
        row = F.sum(axis=1)/N**2
        A_ub.append(row); b_ub.append(0.82395317 + 0.5)
        A_ub.append(-row); b_ub.append(0.82395317 - 0.5)
        rowE = F @ wts / N**2
        A_ub.append(rowE); b_ub.append(Mv + 1/6)
        A_ub.append(-rowE); b_ub.append(Mv - 1/6)
    A_eq = np.ones((1, m)); b_eq = [1.0]
    res = linprog(s_c, A_ub=np.array(A_ub), b_ub=np.array(b_ub), A_eq=A_eq, b_eq=b_eq,
                  bounds=[(0,None)]*m, method='highs')
    return res, F, s_c

print("CORRECT family (sum marks = N). min p1 = weighted (N-2d)/N.")
print()
for mode in ('pointwise', 'cumulative'):
    print(f"=== {mode.upper()} parametrization ===")
    for N, nc in [(8, 3000), (16, 3000), (32, 3000), (64, 3000), (128, 2000)]:
        res, F, sc = run(N, nc, seed=500+N, mode=mode)
        if res.success:
            fbar = res.x @ F
            # VALIDATE support configs
            X, M, s_c = gen_valid_family(N, nc, seed=500+N)
            bad = 0
            for c in np.where(res.x > 1e-9)[0]:
                if abs(M[c].sum() - N) > 1e-9: bad += 1
            D1 = fbar.sum()/N**2 - 0.5
            E1 = (fbar @ np.array([1-(jj+1)/N for jj in range(N)]))/N**2 - 1/6
            maxrow = np.max(np.abs(fbar[:N-1] - np.arange(1,N))) if mode=='pointwise' else float('nan')
            print(f"  N={N:3d}: min p1 = {res.fun/N:.10f} | #support={int((res.x>1e-9).sum())} "
                  f"bad-mark-configs={bad} | D(1)={D1:.6f} E(1)={E1:.6f}"
                  + (f" | maxrow={maxrow:.1e}" if mode=='pointwise' else ""))
        else:
            print(f"  N={N:3d}: INFEASIBLE: {res.message}")
