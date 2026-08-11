#!/usr/bin/env python3
"""General family: N points, positions k + u (u from a small set of rationals), marks 1/2.
Special structure: 'pairs + specials' (antipodal pairs cancel odd-j) OR plain random.
Probe: feasibility of target fbar(j)=j and min p1, at N = 64/128/256."""
import numpy as np
from scipy.optimize import linprog
import sys, time
sys.path.insert(0, '/home/vstaln/riemann/tools/regen_law')

def spectra_fast(X, M, N):
    """X (m,N) positions, M (m,N) marks -> F (m,N): f_c(j)=|sum m e^{2pi i j x/N}|^2, j=1..N."""
    m = X.shape[0]
    j = np.arange(1, N+1)[:, None]          # (N,1)
    # z_c(j) = sum_k M[c,k] exp(2 pi i j X[c,k]/N)
    # vectorize over c by chunking
    F = np.zeros((m, N))
    for c in range(m):
        ang = 2*np.pi*j*X[c][None, :]/N      # (N, N)
        z = np.exp(1j*ang) @ M[c]
        F[c] = np.abs(z)**2
    return F

def gen_mixed(N, n_configs, seed, fracs=(0.0, 0.5, 0.25, 0.75, 1/3, 2/3), pair_frac=0.0):
    """Configs: pairs (antipodal, odd-j cancelling) + special doubles with mixed fractional parts."""
    rng = np.random.default_rng(seed)
    out = []
    for t in range(n_configs):
        # choose k doubles (0..N/3), frac pattern for specials
        k = int(rng.integers(0, N//3 + 1))
        if k == 0:
            xs = np.arange(N).astype(float)
            ms = np.ones(N)
            out.append((xs, ms)); continue
        # pairs: N-k-? ... total marks: pairs use 2*(N-2k)/2? Let's build directly:
        # We want sum marks = N: s simples + 2k doubles = N -> s = N - 2k
        n_simple = N - 2*k
        n_pair_pos = n_simple // 2          # antipodal pairs of simples
        rem = n_simple - 2*n_pair_pos       # leftover simple (0 or 1)
        # positions: pair positions (any), special positions (mixed frac)
        pos = []
        marks = []
        for _ in range(n_pair_pos):
            base = rng.uniform(0, N)
            pos += [base, base + N/2 if base + N/2 < N else base - N/2]
            marks += [1, 1]
        if rem:
            pos.append(rng.uniform(0, N)); marks.append(1)
        for _ in range(k):
            u = fracs[rng.integers(0, len(fracs))]
            q = rng.integers(0, N)
            pos.append(q + u); marks.append(2)
        xs = np.array(pos); ms = np.array(marks)
        assert abs(ms.sum() - N) < 1e-9, (ms.sum(), N)
        out.append((xs, ms))
    return out

def to_matrix(configs, N):
    m = len(configs)
    X = np.zeros((m, N)); M = np.zeros((m, N))
    for c, (xs, ms) in enumerate(configs):
        # pad: configs have <= N positions
        n = len(xs)
        X[c, :n] = xs; M[c, :n] = ms
    return X, M

def solve_lp(F, s_c, N, tau=0.0, Fb=None):
    m = len(F)
    A_ub, b_ub = [], []
    for jj in range(N-1):
        A_ub.append(F[:, jj]); b_ub.append((jj+1)+tau)
        A_ub.append(-F[:, jj]); b_ub.append(-(jj+1)+tau)
    if Fb is not None:
        A_ub.append(F[:, N-1]); b_ub.append(Fb)
    A_eq = np.ones((1, m)); b_eq = [1.0]
    res = linprog(s_c, A_ub=np.array(A_ub), b_ub=np.array(b_ub), A_eq=A_eq, b_eq=b_eq,
                  bounds=[(0,None)]*m, method='highs')
    return res

def cheb_dist(F, N):
    m = len(F)
    c = np.zeros(m+1); c[-1] = 1
    A_ub = []; b_ub = []
    for jj in range(N-1):
        row = np.zeros(m+1); row[:m] = F[:, jj]; row[-1] = -1; A_ub.append(row); b_ub.append(jj+1)
        row = np.zeros(m+1); row[:m] = -F[:, jj]; row[-1] = -1; A_ub.append(row); b_ub.append(-(jj+1))
    A_eq = np.concatenate([np.ones((1,m)), np.zeros((1,1))], axis=1); b_eq = [1.0]
    res = linprog(c, A_ub=np.array(A_ub), b_ub=np.array(b_ub), A_eq=A_eq, b_eq=b_eq,
                  bounds=[(0,None)]*(m+1), method='highs')
    return res.fun if res.success else None

for N, nc in [(64, 800), (128, 800)]:
    configs = gen_mixed(N, nc, seed=N)
    # drop configs with wrong total
    configs = [(xs, ms) for xs, ms in configs if abs(ms.sum() - N) < 1e-9]
    X, M = to_matrix(configs, N)
    s_c = (M == 1).sum(axis=1).astype(float)
    F = spectra_fast(X, M, N)
    d = cheb_dist(F, N)
    print(f"N={N}: {len(configs)} configs, cheb dist target->hull = {d:.4f}")
    if d is not None and d < 1e-4:
        res = solve_lp(F, s_c, N, tau=0.0, Fb=None)
        if res.success:
            print(f"   feasible; min p1 (no D1 bound) = {res.fun/N:.6f}")
        else:
            print(f"   infeasible: {res.message}")
