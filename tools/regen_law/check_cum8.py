#!/usr/bin/env python3
"""Stability check: cumulative-only min p1 at N=8 across family sizes/seeds."""
import numpy as np
from scipy.optimize import linprog
import sys
sys.path.insert(0, '/home/vstaln/riemann/tools/regen_law')
from common2 import gen_valid_family, spectra_valid

N = 8
for nc, seed in [(4000, 1), (8000, 2), (12000, 3), (20000, 4)]:
    X, M, s_c = gen_valid_family(N, nc, seed=seed)
    F = spectra_valid(X, M, N)
    wts = np.array([(1-(jj+1)/N) for jj in range(N)])
    Mv = 1/(6*N*N)
    row = F.sum(axis=1)/N**2
    rowE = F @ wts / N**2
    A_ub = [row, -row, rowE, -rowE]; b_ub = [0.82395317+0.5, 0.82395317-0.5, Mv+1/6, Mv-1/6]
    A_eq = np.ones((1, len(F))); b_eq=[1.0]
    res = linprog(s_c, A_ub=np.array(A_ub), b_ub=np.array(b_ub), A_eq=A_eq, b_eq=b_eq, bounds=[(0,None)]*len(F), method='highs')
    if res.success:
        print(f"nc={nc} seed={seed}: cumulative min p1 (N=8) = {res.fun/8:.8f}, support={int((res.x>1e-9).sum())}")
    else:
        print(f"nc={nc} seed={seed}: infeasible")
