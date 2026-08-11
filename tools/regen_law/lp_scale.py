#!/usr/bin/env python3
"""Scale-up: min p1 over a rich family vs N. Vectorized."""
import numpy as np
from scipy.optimize import linprog

def gen_family_vec(N, n_configs=1500, seed=42):
    rng = np.random.default_rng(seed)
    jitters = (0.25, 0.5, 1/3, 0.125, 0.75, 0.2, 0.4, 1/6, 0.1, 0.6)
    xs_list, ms_list = [], []
    for t in range(n_configs):
        eps = jitters[t % len(jitters)]
        b = (rng.random(N) < rng.uniform(0.1, 0.9)).astype(float)
        xs = np.arange(N) + eps*b
        d = int(rng.integers(0, N//4 + 1))
        ms = np.ones(N, dtype=float)
        if d > 0:
            ms[rng.choice(N, size=d, replace=False)] = 2.0
        xs_list.append(xs); ms_list.append(ms)
    X = np.array(xs_list)   # (m, N)
    M = np.array(ms_list)   # (m, N)
    s_c = (M == 1).sum(axis=1).astype(float)
    return X, M, s_c

def spectra(X, M, N):
    """f_c(j) = |sum_k m exp(2 pi i j x / N)|^2, j=1..N. Vectorized over configs and j."""
    m = X.shape[0]
    j = np.arange(1, N+1)                    # (N,)
    # angle = 2 pi j x / N  ->  (m, N) per j... do matrix: exp(2pi i outer(j, x)/N)  (N, m, N) too big for N=256,m=1500
    # instead: compute per-config DFT via matmul in chunks
    F = np.zeros((m, N))
    # z_c(j) = sum_k m_ck e^{2pi i j x_ck/N} = (e^{2pi i j x_c/N} * m_c) summed over k
    # Build matrix E[j, k] = e^{2pi i j k/N} for the integer part, then phase-shift by eps*b
    k = np.arange(N)
    E = np.exp(2j*np.pi*np.outer(j, k)/N)    # (N, N)
    for c in range(m):
        phase = np.exp(2j*np.pi*np.outer(j, X[c] - np.arange(N))/N)  # (N,N) diagonal-ish: x - k = eps*b_k
        # z(j) = sum_k m_k e^{2pi i j x_k/N} = sum_k m_k E[j,k] e^{2pi i j (eps b_k)/N}
        sh = np.exp(2j*np.pi*np.outer(j, X[c]-np.arange(N))/N)   # (N, N) but only nonzero where...
        z = (E * sh) @ M[c]
        F[c] = np.abs(z)**2
    return F

def run(N, n_configs, F_bound, seed):
    X, M, s_c = gen_family_vec(N, n_configs, seed)
    F = spectra(X, M, N)
    # dedupe approx
    uniq = {}
    for c in range(len(X)):
        key = tuple(np.round(F[c], 8))
        uniq.setdefault(key, (F[c], s_c[c]))
    items = list(uniq.values())
    m = len(items)
    Fm = np.array([f for f, s in items])
    sc = np.array([s for f, s in items])
    # LP: min sum w s  s.t. |sum w F[:,j] - j| <= 0, sum w F[:,N] <= F_bound, sum w = 1
    A_ub, b_ub = [], []
    for jj in range(N-1):
        A_ub.append(Fm[:, jj]); b_ub.append((jj+1) + 0.0)
        A_ub.append(-Fm[:, jj]); b_ub.append(-(jj+1) + 0.0)
    A_ub.append(Fm[:, N-1]); b_ub.append(F_bound)
    A_eq = np.ones((1, m)); b_eq = np.array([1.0])
    res = linprog(sc, A_ub=np.array(A_ub), b_ub=np.array(b_ub), A_eq=A_eq, b_eq=b_eq,
                  bounds=[(0,None)]*m, method='highs')
    if not res.success:
        return None, None, m
    p1 = res.fun / N
    # D(1) at optimum
    fbar = res.x @ Fm
    D1 = fbar.sum()/N**2 - 0.5
    return p1, D1, m

for N, nc, seed in [(64, 1500, 1), (128, 1500, 2)]:
    d1 = 0.82395317
    F_bound = N*N*(d1+0.5) - N*(N-1)//2
    p1, D1, m = run(N, nc, F_bound, seed)
    print(f"N={N}: {m} configs -> min p1 = {p1:.8f}, D(1) at optimum = {D1:.8f} (bound {d1})")
