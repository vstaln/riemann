#!/usr/bin/env python3
"""Final small-N table with VALID configs (sum marks = N): pointwise rows and cumulative-only.
Plus N=256 cumulative. Output for the report."""
import numpy as np
from scipy.optimize import linprog
import sys
sys.path.insert(0, '/home/vstaln/riemann/tools/regen_law')
from common2 import gen_valid_family, spectra_valid

def run(N, nc, seed, mode, tau=3e-40):
    X, M, s_c = gen_valid_family(N, nc, seed=seed)
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
    if res.success:
        return res.fun/N, int((res.x>1e-9).sum())
    return None, None

p0 = 10909258999421303588095230195816054408197 / 16000000000000000000000000000000000000000
print(f"recorded p0(256) = {p0:.16f}")
print("POINTWISE rows (|sum w f(j) - j| <= 3e-40, j=1..N-1) + |D(1)| <= 0.82395317, VALID configs:")
for N, nc in [(8, 8000), (16, 8000), (32, 5000), (64, 4000)]:
    p, ns = run(N, nc, seed=700+N, mode='pointwise')
    print(f"  N={N:3d}: min p1 = {p:.8f} (support {ns} configs)  [upper bound over random family]")
print("CUMULATIVE-only (|D(1)|<=d1, |E(1)|<=1/(6N^2)+tau/(2N)), VALID configs:")
for N, nc in [(8, 8000), (16, 8000), (32, 5000), (64, 4000), (128, 3000), (256, 2500)]:
    p, ns = run(N, nc, seed=800+N, mode='cumulative')
    print(f"  N={N:3d}: min p1 = {p:.8f} (support {ns} configs)" if p else f"  N={N:3d}: infeasible")
print()
print("Grid-config lower bound (exact rows + |D(1)|<=d1): p1 >= 3/2 - d1 =", 3/2-0.82395317)
print("Theorem B / D constants: 2/3 (flat-top), 0.6725007036794116 (Montgomery-Taylor)")
