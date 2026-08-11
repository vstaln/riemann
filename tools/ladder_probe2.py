#!/usr/bin/env python3
"""Q3 ladder probe — part 2: ladder n=3,7,9,11,13,15 under three span models."""
import numpy as np
from scipy.optimize import minimize
import json
rng = np.random.default_rng(11)
SQ2 = np.sqrt(2.0); PI = np.pi

def K(x):
    x = np.asarray(x, float); a = (SQ2-2*PI*x)/2.0; b = (SQ2+2*PI*x)/2.0
    return np.sinc(a/PI) + np.sinc(b/PI)
K0 = float(K(0.0))
def k(x): return K(x)/K0

def pair_sq(gaps, weights=None):
    gaps = np.asarray(gaps, float); Ns, m = gaps.shape; n = m+1
    P = np.concatenate([np.zeros((Ns,1)), np.cumsum(gaps, axis=1)], axis=1)
    tot = np.zeros(Ns)
    for s in range(1, n):
        d = P[:, s:] - P[:, :-s]
        tot += (1.0 if weights is None else weights[s-1]) * (k(d)**2).sum(1)
    return tot

def simp(Ns, m, S, al=1.0):
    u = -np.log(rng.random((Ns,m))+1e-300) if al==1.0 else rng.gamma(al,1.0,(Ns,m))
    return S*u/u.sum(1,keepdims=True)

def mix(Ns, m, S):
    t = Ns//3
    return np.concatenate([simp(t,m,S,0.2), simp(t,m,S,1.0), simp(Ns-2*t,m,S,3.0)])

def refine(obj, starts, m, H, niter=260):
    bnds = [(0.0, H)]*m
    cons = {'type':'ineq','fun': lambda g: H-np.sum(g)}
    best = (1e300, None)
    for g0 in starts:
        r = minimize(obj, g0, method='SLSQP', bounds=bnds, constraints=cons,
                     options={'ftol':1e-14,'maxiter':niter})
        if r.fun < best[0]: best = (r.fun, r.x.copy())
    return best

def minP(n, H, Ns, nref=60):
    m = n-1
    obj = lambda g: float(pair_sq(np.array(g).reshape(1,-1))[0])
    U = mix(Ns, m, H)
    v = pair_sq(U); i = np.argsort(v)[:nref]
    bv, bx = refine(obj, U[i], m, H)
    vs = float(v[i[0]])
    if vs < bv: bv, bx = vs, U[i[0]]
    return bv, bx

H0 = 3.0/2 - (1.0/SQ2)/np.tan(1.0/SQ2)
def const(eps, a, b): return (H0 - a*eps)/(1 - b*eps)
A3, B3 = 1.0/4, 1.0/2
A7, B7 = 2680.0/5111.0, 263.0/269.0

def Smodel(n, name):
    if name == 'I': return 4.0                       # constant span (3-pt rule)
    if name == 'II': return (5.0*n + 1.0)/4.0        # linear fit (3,4),(7,9)
    if name == 'III': return 2.0*(n-1)               # max-gap theorem (each<=2)

res = {}
print("=== LADDER: unweighted pair-squares min eps_n under span models ===")
print(f"{'n':>3} {'model':>5} {'S':>6} {'eps_min':>12} {'span*':>8} {'maxgap':>7}")
for n in (3, 7, 9, 11, 13, 15):
    Ns = {3: 1500000, 7: 1000000, 9: 700000, 11: 450000, 13: 300000, 15: 200000}[n]
    for mod in ('I', 'II', 'III'):
        S = Smodel(n, mod)
        e, g = minP(n, S, Ns)
        res[f"n{n}_{mod}"] = {"eps": e, "S": S,
                              "argmin": [float(x) for x in g],
                              "span": float(g.sum()), "maxgap": float(g.max())}
        print(f"{n:3d} {mod:>5} {S:6.2f} {e:12.4e} {g.sum():8.3f} {g.max():7.3f}")

print("\n=== PLUG-IN CONSTANTS (CONJECTURED coefficients) ===")
print(f"H0 = {H0:.12f}")
for n in (3, 7, 9, 11, 13, 15):
    for mod in ('I', 'II', 'III'):
        e = res[f"n{n}_{mod}"]["eps"]
        c3 = const(e, A3, B3)     # n=3 coefficient set
        c7 = const(e, A7, B7)     # n=7 coefficient set
        # linear extrapolation of (a,b) through anchors
        aL = A3 + (A7-A3)/4.0*(n-3); bL = B3 + (B7-B3)/4.0*(n-3)
        cL = const(e, aL, bL)
        print(f"n={n:2d} {mod}: eps={e:.4e}  set3={c3*100:.6f}%  set7={c7*100:.6f}%  lin={cL*100:.6f}%")

print("\n=== anchors sanity ===")
print("3pt documented: 67.2519767%   computed:", const(221e-6, A3, B3)*100, "%")
print("7pt documented: 67.3008528%   computed:", const(19/5000, A7, B7)*100, "%")

with open("/data/data/com.termux/files/home/riemann/scratch/ladder_res.json", "w") as f:
    json.dump(res, f, indent=1)
print("\nsaved scratch/ladder_res.json")
