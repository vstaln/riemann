#!/usr/bin/env python3
"""m3-price v3: N=64 pool LP, regen_law's VALID family (common2.gen_valid_family: sum marks = N,
marks in {1,2}), pointwise rows |Fbar(j)-j|<=tau, F(N) bound, sum w = 1, and the
marked-windowed m3(1/2) in [5-e,5+e] pin (linear in weights: m3(mix) = sum_c w_c m3_c).
Maximize simple fraction p1. Same pool -> rows-only max p1 = the N=64 p0-proxy (fair comparison).
Kernel: periodic projection |m|<=M=16, coeff 1/B (Dirichlet closed form), K(0)=1 (attack-law-s3 object).
"""
import numpy as np, json, time, sys
from scipy.optimize import linprog
sys.path.insert(0, '/root/riemann/tools/regen_law')
from common2 import gen_valid_family

N = 64; LAM = 0.5
M = int(round(LAM*N/2)); B = 2*M + 1
jrows = np.arange(1, N)
TAU = 3e-40
D1 = 0.82395317
FB = N*N*(D1 + 0.5) - N*(N-1)//2   # F(N) bound (family_law)

def kernel_mat(xs):
    P = len(xs)
    d = xs[:, None] - xs[None, :]
    th = np.pi * d / N
    K = np.where(np.abs(th) > 1e-12, np.sin(B*th)/(np.sin(th)), B)
    return K / B

def m3_of(xs, ms):
    P = len(xs)
    G = kernel_mat(xs)
    MG = np.diag(ms.astype(float)) @ G
    return np.trace(MG @ MG @ MG).real / N

def build_pool(n_configs, seed):
    X, Mm, s_arr = gen_valid_family(N, n_configs, seed=seed)
    pool = []
    for c in range(len(X)):
        xs = np.array(X[c], dtype=float); ms = np.array(Mm[c], dtype=float)
        if abs(ms.sum() - N) > 1e-9: continue
        F = np.abs(np.exp(2j*np.pi*jrows[:, None]*xs[None, :]/N) @ ms)**2
        pool.append((F, m3_of(xs, ms), float(np.sum(ms == 1))/N))
    return pool

def lp(pool, tau, eps=None):
    Fs = np.array([p[0] for p in pool]); m3s = np.array([p[1] for p in pool]); sc = np.array([p[2] for p in pool])
    nc = len(pool)
    A_ub = []; b_ub = []
    for k in range(N-1):
        A_ub.append(Fs[:, k]);       b_ub.append((k+1) + tau)
        A_ub.append(-Fs[:, k]);      b_ub.append(-(k+1) + tau)
    pass  # F has N-1=63 cols; row-N bound not in pool (family_law only for N cols)
    if eps is not None:
        A_ub.append(m3s);            b_ub.append(5+eps)
        A_ub.append(-m3s);           b_ub.append(-(5-eps))
    A_eq = np.ones((1, nc))
    res = linprog(-sc, A_ub=np.array(A_ub), b_ub=np.array(b_ub), A_eq=A_eq, b_eq=np.array([1.0]),
                  bounds=[(0, None)]*nc, method='highs')
    return (-res.fun if res.success else None), res.status

if __name__ == "__main__":
    t0 = time.time()
    out = {}
    for seed, ncfg in [(42, 4000), (1234, 4000)]:
        pool = build_pool(ncfg, seed)
        Fs = np.array([p[0] for p in pool]); m3s = np.array([p[1] for p in pool]); sc = np.array([p[2] for p in pool])
        print(f"seed {seed}: pool {len(pool)} in {time.time()-t0:.0f}s | p1 {sc.min():.3f}..{sc.max():.3f} | m3 {m3s.min():.3f}..{m3s.max():.3f}", flush=True)
        for tau in (TAU, 1e-2):
            p0p, st = lp(pool, tau)
            print(f"  tau={tau:.0e}: rows-only max p1 (N=64 proxy) = {p0p if p0p is None else round(p0p,6)} (status {st})", flush=True)
            for eps in (0.1, 0.44, 1.0, 2.98):
                p1m, st = lp(pool, tau, eps)
                print(f"    eps={eps}: p1(m3=5±{eps}) = {p1m if p1m is None else round(p1m,6)} (status {st})", flush=True)
            out.setdefault(str(seed), {})[f"rows{tau:.0e}"] = p0p
    json.dump(out, open('/tmp/m3price_out.json', 'w'), indent=1)
    print("saved", flush=True)
