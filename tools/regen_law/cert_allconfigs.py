#!/usr/bin/env python3
"""Certificate LP valid against ALL (sampled) marked configurations.
max v = c0 + int_0^1 r x dx,  r piecewise-linear knots j/256, r(1)=0, box |r|<=1,
s.t. c0 + sum_j (f_c(j)/256) r_j <= s_c/256 for every sampled config c.
v* = all-configs dual optimum = primal min p1 (strong duality). Compare with p0=0.6818."""
import numpy as np
from scipy.optimize import linprog

N = 256
p0 = 10909258999421303588095230195816054408197 / 16000000000000000000000000000000000000000

def integral_coeffs(N):
    I = np.zeros(N+1)          # knots j=0..N
    I[0] = 1.0/(6*N*N)
    for j in range(1, N): I[j] = j/(N*N)
    I[N] = (3*N-1)/(6*N*N)
    return I

def rand_configs(n, seed):
    rng = np.random.default_rng(seed)
    out = []
    for _ in range(n):
        # random positions (mixed fractional parts) + marks
        kd = int(rng.integers(0, N//2))
        n_s = N - 2*kd
        # positions: some integer, some half-integer/quarter
        pos = []
        u = rng.choice([0.0, 0.5, 0.25, 0.75, 1/3, 2/3], size=n_s+kd)
        for i in range(n_s):
            pos.append((rng.integers(0,N) + u[i]) % N)
        for i in range(kd):
            pos.append((rng.integers(0,N) + u[n_s+i]) % N)
        marks = [1]*n_s + [2]*kd
        s_c = n_s
        out.append((pos, marks, s_c))
    return out

def spectra_f(configs, N):
    j = np.arange(1, N+1)
    m = len(configs)
    F = np.zeros((m, N))
    for c, (pos, marks, s) in enumerate(configs):
        z = np.zeros(N, dtype=complex)
        for p, mk in zip(pos, marks):
            z += mk*np.exp(2j*np.pi*j*p/N)
        F[c] = np.abs(z)**2
    return F

def cert_lp(F, sc, N, box=True):
    m = len(F)
    I = integral_coeffs(N)
    nvar = 1 + (N+1)                    # c0, r_0..r_N
    c = np.zeros(nvar); c[0] = 1.0; c[1:] = I
    A_ub, b_ub = [], []
    for cidx in range(m):
        row = np.zeros(nvar); row[0] = 1.0
        for jj in range(1, N+1):
            row[1+jj] = F[cidx, jj-1]/N
        A_ub.append(row); b_ub.append(sc[cidx]/N)
    A_eq = np.zeros((1, nvar)); A_eq[0, 1+N] = 1.0; b_eq = [0.0]     # r(1)=0
    if box:
        bounds = [(None,None)] + [(-1.0,1.0)]*(N+1)
    else:
        bounds = [(None,None)]*(N+1)
    res = linprog(-c, A_ub=np.array(A_ub), b_ub=np.array(b_ub), A_eq=A_eq, b_eq=b_eq,
                  bounds=bounds, method='highs')
    return res, c

for n, seed in [(800, 1), (1500, 2), (2500, 3)]:
    configs = rand_configs(n, seed)
    F = spectra_f(configs, N)
    sc = np.array([c[2] for c in configs])
    res, c = cert_lp(F, sc, N)
    if res.success:
        v = res.x[0] + float(np.array(integral_coeffs(N)) @ res.x[1:])
        print(f"{n} sampled configs: v* = {v:.10f}  (p0 = {p0:.10f}, p0+|E1| = {p0+2.5431315104166665e-6:.10f})")
    else:
        print(f"{n} configs: infeasible: {res.message}")
