#!/usr/bin/env python3
"""Certificate LP (proper: r(1)=0, |g(1)|<=B, int|r''|<=C, box |r|<=1, epigraph) with validity
against ALL sampled marked configurations. v* = dual optimum = primal min p1 (strong duality).
Compare with p0 = 0.6818."""
import numpy as np
from scipy.optimize import linprog

N = 256
p0 = 10909258999421303588095230195816054408197 / 16000000000000000000000000000000000000000
h = 1.0/N

def integral_coeffs(N):
    I = np.zeros(N+1)
    I[0] = 1.0/(6*N*N)
    for j in range(1, N): I[j] = j/(N*N)
    I[N] = (3*N-1)/(6*N*N)
    return I

def rand_configs(n, seed):
    rng = np.random.default_rng(seed)
    out = []
    for _ in range(n):
        kd = int(rng.integers(0, N//2))
        n_s = N - 2*kd
        pos, marks = [], []
        for i in range(n_s):
            pos.append((rng.integers(0,N) + rng.choice([0.0,0.5,0.25,0.75])) % N)
            marks.append(1)
        for i in range(kd):
            pos.append((rng.integers(0,N) + rng.choice([0.0,0.5,0.25,0.75])) % N)
            marks.append(2)
        out.append((pos, marks, n_s))
    return out

def lattice_defect_configs():
    out = []
    # lattice + t moved (offset eps) + u doubled
    for eps in (0.5, 0.25, 0.75, 1/3, 1/6):
        for t in range(0, 5):
            for u in range(0, 5):
                for _ in range(30):
                    moved = np.random.choice(N, size=t, replace=False).tolist() if t else []
                    doubled = np.random.choice([p for p in range(N) if p not in moved], size=u, replace=False).tolist() if u else []
                    pos, marks = [], []
                    for k in range(N):
                        if k in moved:
                            pos.append((k + eps) % N); marks.append(1)
                        elif k in doubled:
                            pos.append(k); marks.append(2)
                        else:
                            pos.append(k); marks.append(1)
                    out.append((pos, marks, N - 2*u))
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

def cert_lp(F, sc, N, B=1.0, C=1.0):
    """variables: c0, g_0..g_N (slopes), t_0..t_{N-1} (epigraph |g_{j+1}-g_j|). r_j = cumsum."""
    m = len(F)
    I = integral_coeffs(N)
    nvar = 1 + (N+1) + N
    c = np.zeros(nvar); c[0] = 1.0
    # r_j = r_0 + h*sum_{i<=j} g_i  ->  r_0 = -h*sum g_i  (r_N = r(1) = 0)
    # int r x dx = sum_j I_j r_j ; r_j in terms of g: r_j = sum_{i=1}^{j} h g_i  (r_0=0? no)
    # Use r_j = h * sum_{i=1}^{j} g_i with r_0 = 0; r_N = h sum_{i=1}^N g_i = 0 -> sum g = 0.
    # Then r_j = h sum_{i=1}^j g_i. integral coeffs: int r x dx = sum_j I_j r_j.
    # Build objective directly on g.
    c[0] = 1.0
    for j in range(1, N+1):
        coeff = h * sum(I[i] for i in range(1, j+1))
        c[1+j-1] = coeff
    # constraints
    A_ub, b_ub = [], []
    # validity: c0 + sum_j (f_c(j)/N) r_j <= s_c/N ; r_j = h sum_{i<=j} g_i
    for cidx in range(m):
        row = np.zeros(nvar); row[0] = 1.0
        for j in range(1, N+1):
            rcoef = h * sum(1.0 for _ in range(0))  # placeholder
            # r_j = h * sum_{i=1}^{j} g_i
            for i in range(1, j+1):
                row[1 + i - 1] += (F[cidx, j-1]/N) * h
        A_ub.append(row); b_ub.append(sc[cidx]/N)
    # sum g_i = 0 (r(1)=0)
    A_eq = np.zeros((1, nvar))
    for i in range(1, N+1): A_eq[0, 1+i-1] = 1.0
    b_eq = [0.0]
    # |g(1)| <= B : g_N
    row = np.zeros(nvar); row[1+N-1] = 1; A_ub.append(row); b_ub.append(B)
    row = np.zeros(nvar); row[1+N-1] = -1; A_ub.append(row); b_ub.append(B)
    # epigraph |g_{i+1}-g_i| <= t_i, sum t <= C
    for i in range(1, N):
        row = np.zeros(nvar); row[1+i-1] = 1; row[1+i] = -1; row[1+N+i-1] = -1; A_ub.append(row); b_ub.append(0.0)
        row = np.zeros(nvar); row[1+i-1] = -1; row[1+i] = 1; row[1+N+i-1] = -1; A_ub.append(row); b_ub.append(0.0)
    row = np.zeros(nvar); row[1+N:1+N+N] = 1; A_ub.append(row); b_ub.append(C)
    # box |r_j| <= 1
    for j in range(1, N+1):
        row = np.zeros(nvar)
        for i in range(1, j+1): row[1+i-1] += h
        A_ub.append(row); b_ub.append(1.0)
        row = np.zeros(nvar)
        for i in range(1, j+1): row[1+i-1] += -h
        A_ub.append(row); b_ub.append(1.0)
    bounds = [(None,None)]*nvar
    res = linprog(-c, A_ub=np.array(A_ub), b_ub=np.array(b_ub), A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')
    return res

for n, seed in [(600, 1), (1200, 2)]:
    configs = rand_configs(n, seed) + lattice_defect_configs()
    F = spectra_f(configs, N)
    sc = np.array([c[2] for c in configs])
    res = cert_lp(F, sc, N, B=1.0, C=1.0)
    if res.success:
        v = res.x[0] + sum(res.x[1:1+N][i] * (h*sum(integral_coeffs(N)[j] for j in range(1, i+2))) for i in range(N))
        # recompute v directly
        g = res.x[1:1+N]
        I = integral_coeffs(N)
        r = np.cumsum(g)*h
        v = res.x[0] + float(I[1:] @ r)
        print(f"{len(configs)} configs: v* = {v:.10f}   (p0 = {p0:.10f})")
    else:
        print(f"{len(configs)}: infeasible: {res.message}")
