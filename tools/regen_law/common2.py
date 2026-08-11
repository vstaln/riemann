#!/usr/bin/env python3
"""Correct family generator: configs with EXACTLY N marks, marks in {1,2}.
s simples + d doubles, s + 2d = N, s + d distinct positions. s_c = N - 2d."""
import numpy as np

def gen_valid_family(N, n_configs=1500, seed=42, max_d_frac=0.25):
    rng = np.random.default_rng(seed)
    fracs = (0.0, 0.5, 0.25, 0.75, 1/3, 2/3, 0.125, 0.375, 0.625, 0.875)
    xs_list, ms_list, s_list = [], [], []
    made = 0
    tries = 0
    while made < n_configs and tries < n_configs*20:
        tries += 1
        d = int(rng.integers(0, int(N*max_d_frac) + 1))
        s = N - 2*d
        npos = s + d
        if npos > N*2: continue
        # choose npos distinct base positions (0..N-1) and assign fractional parts
        base = rng.choice(N, size=npos, replace=False)
        u = rng.choice(fracs, size=npos)
        xs = (base + u) % N
        marks = np.concatenate([np.ones(s), 2*np.ones(d)])
        assert marks.sum() == N
        xs_list.append(xs); ms_list.append(marks); s_list.append(float(s))
        made += 1
    return np.array(xs_list, dtype=object), np.array(ms_list, dtype=object), np.array(s_list)

def spectra_valid(X, M, N):
    """F (m, N): f_c(j) = |sum_k m_k e^{2 pi i j x_k / N}|^2, j=1..N. Configs have varying #points."""
    j = np.arange(1, N+1)
    m = len(X)
    F = np.zeros((m, N))
    for c in range(m):
        xs = X[c]; ms = M[c]
        z = np.zeros(N, dtype=complex)
        for x, mk in zip(xs, ms):
            z += mk*np.exp(2j*np.pi*j*x/N)
        F[c] = np.abs(z)**2
    return F
