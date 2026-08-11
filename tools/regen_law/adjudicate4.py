#!/usr/bin/env python3
"""N=8 focus: (1) grid-config lower bound p1 >= 3/2 - d1; (2) can off-grid configs break it?
(3) push the N=8 family hard."""
import numpy as np
from scipy.optimize import linprog
import sys
sys.path.insert(0, '/home/vstaln/riemann/tools/regen_law')

# (1) verify the grid identity at N=8
def grid_sumf(N, marks_at_positions):
    """sum_j f(j) for a grid config with marks m_k at k=0..N-1."""
    j = np.arange(1, N+1)
    z = np.zeros(N, dtype=complex)
    for k, m in enumerate(marks_at_positions):
        z += m*np.exp(2j*np.pi*j*k/N)
    return np.abs(z)**2

N = 8
d1 = 0.82395317
lb = 3/2 - d1
print(f"Grid-config lower bound: p1 >= 3/2 - d1 = {lb:.10f}  (N=8, exact rows + D(1)<=d1)")
# verify with one config: marks [2,2,2,1,1,0,0,0]? no: sum marks must be 8. s=2,d=3: [2,2,2,1,1,0,0,0]
marks = [2,2,2,1,1,0,0,0]
f = grid_sumf(N, marks)
print(f"  check: sum_j f(j) = {f.sum():.4f}, N(2N - s) = {8*(16-2)} = {8*(16-2)}")

# (2) off-grid: can a config have sum_j f(j) < N(2N - s)?
def offgrid_sumf(N, xs, ms):
    j = np.arange(1, N+1)
    z = np.zeros(N, dtype=complex)
    for x, m in zip(xs, ms):
        z += m*np.exp(2j*np.pi*j*x/N)
    return np.abs(z)**2

# try: 2 simples at 0 and 0.5, marks [1,1], s=2
xs = [0.0, 0.5]; ms = [1, 1]
print(f"  off-grid [0, 0.5] s=2: sum_j f = {offgrid_sumf(N, xs, ms).sum():.4f} vs N(2N-s) = {8*14}")
xs = [0.0, 0.25]; 
print(f"  off-grid [0, 0.25] s=2: sum_j f = {offgrid_sumf(N, xs, ms).sum():.4f} vs 112")
xs = [0.0, 0.75]
print(f"  off-grid [0, 0.75] s=2: sum_j f = {offgrid_sumf(N, xs, ms).sum():.4f} vs 112")
xs = [0.0, 1/3]
print(f"  off-grid [0, 1/3] s=2: sum_j f = {offgrid_sumf(N, xs, ms).sum():.4f} vs 112")

# (3) N=8 hard push: rich family incl. structured off-grid configs
def gen_rich(N, n, seed):
    rng = np.random.default_rng(seed)
    fracs = (0.0, 0.5, 0.25, 0.75, 1/3, 2/3, 0.125, 0.375, 0.625, 0.875, 1/6, 5/6)
    out_x, out_m, out_s = [], [], []
    for _ in range(n):
        d = int(rng.integers(0, N//2+1))       # up to N/2 doubles
        s = N - 2*d
        npos = s + d
        base = rng.choice(N, size=npos, replace=False)
        u = rng.choice(fracs, size=npos)
        xs = (base + u) % N
        ms = np.concatenate([np.ones(s), 2*np.ones(d)])
        out_x.append(xs); out_m.append(ms); out_s.append(float(s))
    return out_x, out_m, np.array(out_s)

def spectra_list(X, M, N):
    j = np.arange(1, N+1)
    m = len(X); F = np.zeros((m, N))
    for c in range(m):
        z = np.zeros(N, dtype=complex)
        for x, mk in zip(X[c], M[c]):
            z += mk*np.exp(2j*np.pi*j*x/N)
        F[c] = np.abs(z)**2
    return F

for seed in (1, 2, 3):
    X, M, sc = gen_rich(N, 8000, seed)
    F = spectra_list(X, M, N)
    m = len(F)
    A_ub, b_ub = [], []
    for jj in range(N-1):
        A_ub.append(F[:, jj]); b_ub.append((jj+1)+3e-40)
        A_ub.append(-F[:, jj]); b_ub.append(-(jj+1)+3e-40)
    Fb = N*N*(d1+0.5) - N*(N-1)//2
    A_ub.append(F[:, N-1]); b_ub.append(Fb)
    A_eq = np.ones((1,m)); b_eq=[1.0]
    res = linprog(sc, A_ub=np.array(A_ub), b_ub=np.array(b_ub), A_eq=A_eq, b_eq=b_eq, bounds=[(0,None)]*m, method='highs')
    if res.success:
        fbar = res.x @ F
        print(f"N=8 rich seed={seed}: min p1 = {res.fun/8:.10f}  (grid LB = {lb:.10f}, ThmB = 0.6725)")
        # verify identity: sum_j fbar
        print(f"    sum_j fbar(j) = {fbar.sum():.4f} vs 128-64*p1 = {128-64*res.fun/8:.4f}")
    else:
        print(f"N=8 seed={seed}: infeasible")
