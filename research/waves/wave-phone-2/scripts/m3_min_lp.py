#!/usr/bin/env python3
"""m3-min-frontier LP: min p1 over {rows, marks, m3 in 5±eps, T in [Tmin,Tmax]}
using m3-price's N=64 pool (regen_law common2.gen_valid_family). Per-config
T = m3 - D - pair computed from the config (exact), pair = (3/(2N)) sum_{i!=j}
m_i m_j (m_i+m_j) K_ij^2. Realized T-range from the zeros (m3_min_frontier.py):
N=64 [0.272, 0.427], N=256 [0.333, 0.401]. eps-grid {0.1, 0.44, 1.0, 2.98}.
"""
import numpy as np, json, time, sys
from scipy.optimize import linprog
sys.path.insert(0, '/root/riemann/tools/regen_law')
from common2 import gen_valid_family

N = 64; LAM = 0.5
M = int(round(LAM*N/2)); B = 2*M + 1
jrows = np.arange(1, N)
TAU = 3e-40

def kernel_mat(xs):
    P = len(xs)
    d = xs[:, None] - xs[None, :]
    th = np.pi * d / N
    K = np.where(np.abs(th) > 1e-12, np.sin(B*th)/(np.sin(th)), B)
    return K / B

def build_pool(n_configs, seed):
    X, Mm, s_arr = gen_valid_family(N, n_configs, seed=seed)
    pool = []
    for c in range(len(X)):
        xs = np.array(X[c], dtype=float); ms = np.array(Mm[c], dtype=float)
        if abs(ms.sum() - N) > 1e-9: continue
        G = kernel_mat(xs)
        MG = np.diag(ms) @ G
        m3 = np.trace(MG @ MG @ MG).real / N
        K2 = G*G
        pair = (3.0/(2.0*N)) * np.sum((ms[:,None]*ms[None,:]*(ms[:,None]+ms[None,:])) * K2).real
        D = float(np.sum(ms**3))/N
        T = m3 - D - pair
        F = np.abs(np.exp(2j*np.pi*jrows[:, None]*xs[None, :]/N) @ ms)**2
        pool.append((F, m3, float(np.sum(ms == 1))/N, T, D, pair))
    return pool

def lp(pool, tau, eps=None, Tlo=None, Thi=None):
    Fs = np.array([p[0] for p in pool]); m3s = np.array([p[1] for p in pool])
    sc = np.array([p[2] for p in pool]); Ts = np.array([p[3] for p in pool])
    nc = len(pool)
    A_ub = []; b_ub = []
    for k in range(N-1):
        A_ub.append(Fs[:, k]);  b_ub.append((k+1) + tau)
        A_ub.append(-Fs[:, k]); b_ub.append(-(k+1) + tau)
    if eps is not None:
        A_ub.append(m3s);  b_ub.append(5+eps)
        A_ub.append(-m3s); b_ub.append(-(5-eps))
    if Tlo is not None:
        A_ub.append(-Ts);  b_ub.append(-Tlo)
        A_ub.append(Ts);   b_ub.append(Thi)
    A_eq = np.ones((1, nc))
    res = linprog(sc, A_ub=np.array(A_ub), b_ub=np.array(b_ub), A_eq=A_eq, b_eq=np.array([1.0]),
                  bounds=[(0, None)]*nc, method='highs')
    return (res.fun, res.status)

if __name__ == "__main__":
    t0 = time.time()
    allres = {}
    for seed, ncfg in [(42, 4000), (1234, 4000)]:
        pool = build_pool(ncfg, seed)
        Fs = np.array([p[0] for p in pool]); m3s = np.array([p[1] for p in pool])
        sc = np.array([p[2] for p in pool]); Ts = np.array([p[3] for p in pool])
        print(f"seed {seed}: pool {len(pool)} in {time.time()-t0:.0f}s | p1 {sc.min():.3f}..{sc.max():.3f} | "
              f"m3 {m3s.min():.3f}..{m3s.max():.3f} | T {Ts.min():.3f}..{Ts.max():.3f}", flush=True)
        # class stats: how many configs satisfy m3 in 5±eps AND T in zeros range
        for Tlo, Thi, tname in [(0.272, 0.427, 'z64'), (0.333, 0.401, 'z256')]:
            for eps in (0.1, 0.44, 1.0, 2.98):
                inclass = (m3s >= 5-eps) & (m3s <= 5+eps) & (Ts >= Tlo) & (Ts <= Thi)
                if inclass.sum() == 0:
                    print(f"  T∈[{Tlo},{Thi}] eps={eps}: EMPTY pool class", flush=True)
                    continue
                v, st = lp(pool, TAU, eps, Tlo, Thi)
                # binding config = the argmin-ish (report min-p1 config in class)
                w = np.zeros(len(pool)); w[inclass] = 1.0/inclass.sum()
                print(f"  T∈[{Tlo},{Thi}] eps={eps}: {inclass.sum()} configs, min-p1 {v:.6f} (st {st}) | "
                      f"p1 in-class {sc[inclass].min():.3f}..{sc[inclass].max():.3f} | "
                      f"T in-class {Ts[inclass].min():.3f}..{Ts[inclass].max():.3f}", flush=True)
    print(f"elapsed {time.time()-t0:.0f}s")
