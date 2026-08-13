"""Dump the true corrected-LP solution (l,c) at full precision, then scan it.
Solve once, print res.x, and run the global float floor with the TRUE l,c.
"""
import numpy as np
from scipy.optimize import linprog, minimize
import time

SQRT2 = np.sqrt(2.0)
def k_alpha(x, alpha):
    x = np.asarray(x, float); a = alpha/2.0
    z1 = np.pi*x - a; z2 = np.pi*x + a
    return 0.5*(np.sinc(z1/np.pi)+np.sinc(z2/np.pi))/np.sinc(a/np.pi)
def w_alpha(x, alpha): return k_alpha(x, alpha)**2
P0, Q0 = 1.0/1920, 1.0/3
def pair_coeffs():
    return {(i,j): 2.0/(7-(j-i)) for i in range(7) for j in range(i+1,7)}
def F0(g, alpha):
    g = np.asarray(g, float)
    y = np.concatenate([[0.0], np.cumsum(g)])
    total = P0*np.sum(g) + Q0*np.sum(w_alpha(g, alpha))
    for (i,j),a in pair_coeffs().items(): total += a*w_alpha(y[j]-y[i], alpha)
    return total
def lin_coeffs(g, alpha):
    g = np.asarray(g, float)
    g0 = np.concatenate([[0.0], g, [0.0]])
    return (np.asarray(g0[1:]-g0[:-1], float)[1:6],
            np.asarray(w_alpha(g0[1:], alpha)-w_alpha(g0[:-1], alpha), float)[1:6])
def F_B(g, alpha, l, c):
    L, C = lin_coeffs(g, alpha)
    return F0(g, alpha) + np.dot(L, l) + np.dot(C, c)

def solve_lp(alpha, cfgs, l_bound=0.0012, c_bound=0.06):
    A, b = [], []
    for g in cfgs:
        L, C = lin_coeffs(g, alpha)
        A.append(np.concatenate([-L, -C, [1.0]])); b.append(F0(g, alpha))
    for i in range(1, 7):
        row = np.zeros(11)
        if i >= 2: row[i-2] = -1.0
        if i <= 5: row[i-1] = +1.0
        A.append(row); b.append(P0)
    res = linprog(c=[0]*10+[-1.0], A_ub=np.array(A), b_ub=np.array(b),
                  bounds=[(-l_bound,l_bound)]*5 + [(-c_bound,c_bound)]*5 + [(None,None)],
                  method='highs')
    return res

def base_family(n2=14, n3=4, nint=300):
    cfgs = []
    for a in np.linspace(0.8, 1.6, n2):
        for b in np.linspace(1.4, 2.6, n2):
            cfgs.append(np.array([a,b,a,b,a,b]))
    for a in np.linspace(0.85, 1.55, n3):
        for b in np.linspace(1.4, 2.5, n3):
            for cc in np.linspace(0.85, 1.55, n3):
                cfgs.append(np.array([a,b,cc,a,b,cc]))
    rng = np.random.default_rng(12345)
    for _ in range(nint): cfgs.append(rng.uniform(0.5, 3.0, 6))
    base = np.array([1.05, 1.98, 1.05, 1.98, 1.05, 1.98])
    for pos in range(6):
        for H in [8.0, 14.0, 21.0]:
            g = base.copy(); g[pos] = H
            cfgs.append(g)
    return cfgs

def find_worst(alpha, l, c, verbose=True):
    f = lambda g: F_B(g, alpha, l, c)
    t0 = time.time()
    rng = np.random.default_rng(21)
    cands = []
    for a in np.linspace(0.5, 2.6, 45):
        for b in np.linspace(0.5, 2.8, 45):
            cands.append((f([a,b,a,b,a,b]), np.array([a,b,a,b,a,b])))
    for a in np.linspace(0.6, 2.2, 18):
        for b in np.linspace(0.8, 2.6, 18):
            for cc in np.linspace(0.6, 2.2, 18):
                cands.append((f([a,b,cc,a,b,cc]), np.array([a,b,cc,a,b,cc])))
    for _ in range(8000):
        g = rng.uniform(0.4, 3.5, 6); cands.append((f(g), g))
    cands.sort(key=lambda t: t[0])
    best = cands[0]
    def refine(g0, mi=2500):
        r = minimize(f, g0, method='Nelder-Mead',
                     options={'maxiter': mi, 'xatol': 1e-10, 'fatol': 1e-13})
        return r.fun, r.x
    for _, g0 in cands[:20]:
        r = refine(g0)
        if r[0] < best[0]: best = (r[0], r[1])
    for pos in range(6):
        for H in np.linspace(5, 21, 9):
            for variant in (np.array([1.05,1.98,1.05,1.98,1.05,1.98]), np.full(6,1.1)):
                g = variant.copy(); g[pos] = H
                r = refine(g, 1000)
                if r[0] < best[0]: best = (r[0], r[1])
    if verbose:
        print(f"  FINAL floor={best[0]:.8f} at g={np.round(best[1],4)} ({time.time()-t0:.0f}s)", flush=True)
    return best

if __name__ == "__main__":
    alpha = 1.49
    res = solve_lp(alpha, base_family())
    print(f"LP status={res.status} v*={res.x[10]:.15f}")
    l = res.x[:5]; c = res.x[5:10]
    print(f"TRUE l = {', '.join(f'{x:.10f}' for x in l)}")
    print(f"TRUE c = {', '.join(f'{x:.10f}' for x in c)}")
    # kappa from the true l
    l0 = np.concatenate([[0.0], l, [0.0]])
    kap = P0 + (l0[:-1] - l0[1:])
    print(f"kappa = {np.round(kap, 8)}  min = {kap.min():.8f}")
    # scan the TRUE solution
    l_tw = np.array([54,-123,0,123,-54])/1_920_000
    c_tw = np.array([5971,5971,0,-5971,-5971])/300_000
    fl, g = find_worst(alpha, l, c)
    flt, gt = find_worst(alpha, l_tw, c_tw, verbose=False)
    print(f"TRUE-LP global float floor = {fl:.8f} at {np.round(g,4)}")
    print(f"tawan global float floor   = {flt:.8f} at {np.round(gt,4)}")
    print(f"RESULT: LP {'BEATS' if fl > flt else 'LOSES TO'} tawan on global float floor")
