#!/usr/bin/env python3
"""Q3 ladder probe — part 1: kernel + 3-pt reproduction + 7-pt domain scan."""
import numpy as np
from scipy.optimize import minimize
rng = np.random.default_rng(7)
SQ2 = np.sqrt(2.0); PI = np.pi

def K(x):
    x = np.asarray(x, float); a = (SQ2 - 2*PI*x)/2.0; b = (SQ2 + 2*PI*x)/2.0
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

def refine(obj, starts, m, H):
    bnds = [(0.0, H)]*m
    cons = {'type':'ineq', 'fun': lambda g: H - np.sum(g)}
    best = (1e300, None)
    for g0 in starts:
        r = minimize(obj, g0, method='SLSQP', bounds=bnds, constraints=cons,
                     options={'ftol':1e-14,'maxiter':240})
        if r.fun < best[0]: best = (r.fun, r.x.copy())
    return best

def minP(n, H, w=None, Ns=800_000, nref=60):
    m = n-1; obj = lambda g: float(pair_sq(np.array(g).reshape(1,-1), w)[0])
    U = mix(Ns, m, H)
    v = pair_sq(U, w); i = np.argsort(v)[:nref]
    bv, bx = refine(obj, U[i], m, H)
    return (min(float(v[i[0]]), bv), bx)

print("=== PART 1: 3-point, S2=k(u)^2+k(v)^2+k(u+v)^2, u+v<=4 ===")
N = 1500; u1 = np.linspace(0, 4, N)
U, V = np.meshgrid(u1, u1); W = U+V; mk = W <= 4
U, V, W = U[mk], V[mk], W[mk]
S2 = k(U)**2 + k(V)**2 + k(W)**2
i = int(np.argmin(S2))
S2w = k(U)**2 + k(V)**2 + 2*k(W)**2
iw = int(np.argmin(S2w))
obj3 = lambda g: float(k(g[0])**2 + k(g[1])**2 + k(g[0]+g[1])**2)
bv, bx = refine(obj3, [(U[i],V[i]), (2.03,1.03), (2.0,1.057), (2.0121,1.0531)], 2, 4.0)
print(f"grid unweighted min = {S2[i]:.8e} at u={U[i]:.5f}, v={V[i]:.5f}")
print(f"grid weighted(c=(1,2)) min = {S2w[iw]:.8e} at ({U[iw]:.5f},{V[iw]:.5f})")
print(f"SLSQP min S2 = {bv:.8e} at u={bx[0]:.8f}, v={bx[1]:.8f}, w={bx[0]+bx[1]:.8f}")
print(f"vs certified 221/10^6: ratio {bv/2.21e-4:.5f}")

print("\n=== PART 2: 7-point scan (target 19/5000=3.8e-3) ===")
cs7 = np.array([2.0/(7-s) for s in range(1,7)])
for H in (4.0, 6.0, 8.0, 9.0, 10.0, 11.0, 12.0):
    m = 6
    U = mix(500_000, m, H)
    vu = pair_sq(U); vw = pair_sq(U, cs7)
    bu, bw = float(vu.min()), float(vw.min())
    obju = lambda g: float(pair_sq(np.array(g).reshape(1,-1))[0])
    r = refine(obju, U[np.argsort(vu)[:40]], m, H)
    bu = min(bu, r[0])
    print(f"sum<= {H:5.1f}: unweighted {bu:.6e}   weighted {bw:.6e}")
