#!/usr/bin/env python3
"""Primal LP probe at small N: min p1 = sum w_c s_c / N  s.t.
   sum_c w_c f_c(j) = j  (j=1..N-1),  sum_c w_c f_c(N) <= F_N_bound,  sum w_c = 1, w_c >= 0.
Rich family: jittered lattices + marks. Question: is the target spectrum achievable, and what is min p1?
"""
import numpy as np
from scipy.optimize import linprog

def gen_family(N, n_jitter_sets=600, jitters=(0.25, 0.5, 1/3, 0.125, 0.75, 0.2, 0.4)):
    rng = np.random.default_rng(1234)
    configs = []  # (f_vec (len N), s_c)
    for trial in range(n_jitter_sets):
        eps = jitters[trial % len(jitters)]
        # binary jitter pattern: fraction p of points jittered by eps
        p_jit = rng.uniform(0.1, 0.9)
        b = rng.random(N) < p_jit
        xs = np.arange(N) + eps * b
        # marks: choose d doubles at random positions, d ~ U[0, N/4]
        d = int(rng.integers(0, N // 4 + 1))
        ms = np.ones(N, dtype=int)
        if d > 0:
            idx = rng.choice(N, size=d, replace=False)
            ms[idx] = 2
        # ensure sum marks = N: s + 2d = N
        # (adjust: we set d doubles and N-d-? simples; N = s + 2d with s = N - 2d)
        s_c = N - 2 * d
        if s_c < 0: continue
        # f(j) = |sum m e^{2pi i j x / N}|^2
        f = np.array([abs(sum(ms[k]*np.exp(2j*np.pi*j*xs[k]/N) for k in range(N)))**2 for j in range(1, N+1)])
        configs.append((f, s_c))
    # dedupe
    seen = set()
    out = []
    for f, s in configs:
        key = tuple(np.round(f, 9))
        if key not in seen:
            seen.add(key); out.append((f, s))
    return out

def solve_lp(configs, N, F_bound=None, tau=0.0, maximize=False):
    m = len(configs)
    if F_bound is None:
        F_bound = float('inf')
    # variables w[0..m-1]
    A_ub, b_ub = [], []
    # |sum w f(j) - j| <= tau  ->  sum w f(j) <= j+tau, -sum w f(j) <= -j+tau
    for j in range(1, N):
        row_p = np.zeros(m); row_n = np.zeros(m)
        for cidx, (f, s) in enumerate(configs):
            row_p[cidx] = f[j-1]; row_n[cidx] = -f[j-1]
        A_ub.append(row_p); b_ub.append(j + tau)
        A_ub.append(row_n); b_ub.append(-j + tau)
    # sum w f(N) <= F_bound
    if F_bound < float('inf'):
        row = np.array([f[N-1] for f, s in configs])
        A_ub.append(row); b_ub.append(F_bound)
    # sum w = 1
    A_eq = np.ones((1, m)); b_eq = [1.0]
    # objective: min sum w s_c (then p1 = /N)
    obj = np.array([s for f, s in configs])
    if maximize: obj = -obj
    res = linprog(obj, A_ub=np.array(A_ub), b_ub=np.array(b_ub), A_eq=A_eq, b_eq=b_eq,
                  bounds=[(0, None)]*m, method='highs')
    return res

for N in (8, 16, 32):
    configs = gen_family(N)
    m = len(configs)
    print(f"\n=== N = {N}: {m} configs ===")
    # what is the natural F(N) bound? from D(1)<=0.82395317 at N=256: sum_j f(j)/N^2 - 1/2 <= d1
    # => sum f(j) <= N^2(d1+1/2); with rows j = 1..N-1 pinned: f(N) <= N^2(d1+1/2) - sum_{j<N} j
    d1 = 0.82395317
    F_bound = N*N*(d1+0.5) - N*(N-1)//2
    # feasibility WITHOUT objective
    res0 = solve_lp(configs, N, F_bound=None)
    print(f"  feasibility (no D(1) bound): {res0.success}, residual max|sum w f(j) - j| = "
          f"{max(abs(configs[c][0][j-1] for c in range(m)) if False else 0 for j in [1]) if False else 0}"
          f"{np.max(np.abs(np.array([configs[c][0] for c in range(m)]).T @ res0.x - np.concatenate([np.arange(1,N), [0]]))[:N-1]) if res0.success else 'n/a'}")
    res = solve_lp(configs, N, F_bound=F_bound)
    if res.success:
        p1 = res.fun / N
        print(f"  min p1 = {p1:.8f}   (active rows: {sum(1 for c in range(m) if res.x[c] > 1e-9)} positive weights)")
        nz = np.argsort(-res.x)[:8]
        print(f"  top configs: {[(c, round(float(res.x[c]),4), configs[c][1]) for c in nz if res.x[c] > 1e-9]}")
    else:
        print(f"  LP INFEASIBLE: {res.message}")
    # also maximize p1
    res2 = solve_lp(configs, N, F_bound=F_bound, maximize=True)
    if res2.success:
        print(f"  max p1 = {-res2.fun / N:.8f}")
    else:
        print(f"  max-LP INFEASIBLE: {res2.message}")
