#!/usr/bin/env python3
"""Extract the small-N optimal laws (cumulative + pointwise) and understand their structure.
Also try richer families to push min p1 down at N=8."""
import numpy as np
from scipy.optimize import linprog
import sys
sys.path.insert(0, '/home/vstaln/riemann/tools/regen_law')
from common2 import gen_valid_family, spectra_valid

def run(N, nc, seed, mode, max_d_frac=0.25, tau=3e-40):
    X, M, s_c = gen_valid_family(N, nc, seed=seed, max_d_frac=max_d_frac)
    F = spectra_valid(X, M, N)
    m = len(F)
    A_ub, b_ub = [], []
    if mode == 'pointwise':
        for jj in range(N-1):
            A_ub.append(F[:, jj]); b_ub.append((jj+1)+tau)
            A_ub.append(-F[:, jj]); b_ub.append(-(jj+1)+tau)
        Fb = N*N*(0.82395317+0.5) - N*(N-1)//2
        A_ub.append(F[:, N-1]); b_ub.append(Fb)
    else:
        wts = np.array([(1-(jj+1)/N) for jj in range(N)])
        Mv = 1/(6*N*N) + tau/(2*N)
        row = F.sum(axis=1)/N**2
        A_ub.append(row); b_ub.append(0.82395317+0.5)
        A_ub.append(-row); b_ub.append(0.82395317-0.5)
        rowE = F @ wts / N**2
        A_ub.append(rowE); b_ub.append(Mv+1/6)
        A_ub.append(-rowE); b_ub.append(Mv-1/6)
    A_eq = np.ones((1,m)); b_eq=[1.0]
    res = linprog(s_c, A_ub=np.array(A_ub), b_ub=np.array(b_ub), A_eq=A_eq, b_eq=b_eq,
                  bounds=[(0,None)]*m, method='highs')
    return res, X, M, s_c

print("N=8 detailed: extract support configs of the cumulative optimum")
res, X, M, sc = run(8, 5000, seed=508, mode='cumulative', max_d_frac=0.4)
if res.success:
    print(f"min p1 (cumulative, N=8) = {res.fun/8:.10f}")
    for c in np.where(res.x > 1e-9)[0]:
        xs = np.round(X[c], 4); ms = M[c]
        print(f"  w={res.x[c]:.6f} s_c={int(sc[c])} d={int((ms==2).sum())} marks={ms} positions={xs}")

print("\nN=8 richer family push (pointwise rows), max_d_frac sweep:")
for mdf in (0.25, 0.4, 0.49):
    res, X, M, sc = run(8, 6000, seed=508, mode='pointwise', max_d_frac=mdf)
    if res.success:
        fbar = res.x @ spectra_valid(X, M, 8)
        print(f"  max_d_frac={mdf}: min p1 = {res.fun/8:.10f}  E(1)={ (fbar@np.array([1-(jj+1)/8 for jj in range(8)]))/64 - 1/6 :.8f}")

print("\nN=16/32 richer (pointwise):")
for N, mdf in [(16, 0.4), (32, 0.4), (16, 0.49), (32, 0.49)]:
    res, X, M, sc = run(N, 6000, seed=500+N, mode='pointwise', max_d_frac=mdf)
    if res.success:
        fbar = res.x @ spectra_valid(X, M, N)
        E1 = (fbar@np.array([1-(jj+1)/N for jj in range(N)]))/N**2 - 1/6
        print(f"  N={N} max_d_frac={mdf}: min p1 = {res.fun/N:.10f}  E(1)={E1:.8f} (M={1/(6*N*N):.8f})")
    else:
        print(f"  N={N} max_d_frac={mdf}: infeasible")
