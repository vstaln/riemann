#!/usr/bin/env python3
"""Shared: family generation + spectra (vectorized)."""
import numpy as np

def gen_family_vec(N, n_configs=1500, seed=42, max_d_frac=0.25):
    rng = np.random.default_rng(seed)
    jitters = (0.25, 0.5, 1/3, 0.125, 0.75, 0.2, 0.4, 1/6, 0.1, 0.6, 0.3, 0.45)
    xs_list, ms_list = [], []
    for t in range(n_configs):
        eps = jitters[t % len(jitters)]
        b = (rng.random(N) < rng.uniform(0.1, 0.9)).astype(float)
        xs = np.arange(N) + eps*b
        d = int(rng.integers(0, int(N*max_d_frac) + 1))
        ms = np.ones(N, dtype=float)
        if d > 0:
            ms[rng.choice(N, size=d, replace=False)] = 2.0
        xs_list.append(xs); ms_list.append(ms)
    X = np.array(xs_list); M = np.array(ms_list)
    s_c = (M == 1).sum(axis=1).astype(float)
    return X, M, s_c

def spectra(X, M, N):
    m = X.shape[0]
    j = np.arange(1, N+1)
    k = np.arange(N)
    E = np.exp(2j*np.pi*np.outer(j, k)/N)   # (N,N)
    F = np.zeros((m, N))
    for c in range(m):
        dx = X[c] - k                        # eps*b_k, the off-grid part
        sh = np.exp(2j*np.pi*np.outer(j, dx)/N)
        z = (E * sh) @ M[c]
        F[c] = np.abs(z)**2
    return F

def dedupe(F, s_c, rtol=1e-8):
    uniq = {}
    for c in range(len(F)):
        uniq.setdefault(tuple(np.round(F[c], 8)), (F[c], s_c[c]))
    items = list(uniq.values())
    Fm = np.array([f for f, s in items]); sc = np.array([s for f, s in items])
    return Fm, sc
