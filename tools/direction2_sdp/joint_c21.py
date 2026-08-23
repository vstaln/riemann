#!/usr/bin/env python3
"""Faithful F_B model + joint max-min (v2).

Fixes vs v1:
  * q_i = lambda * q_raw_i   (verifier main(): q_coeff = [lam*c])
  * w-term DROPOUT: verifier tables w only up to cutoff_cells ~= target/pressure*grid;
    terms with index >= length contribute 0. We model cutoff X_cut explicitly.
True objective for the probe: maximize min_g F_B^mod over (lambda, alpha, r-dist, q-dist).
Any eps* > 0.00703 => record candidate => Arb certification (in-repo verifier).
"""
import numpy as np
from scipy.optimize import minimize, differential_evolution

X_CUT = 21.09  # verifier cutoff_units = target*3000 = 0.00703*3000 (table covers x<=21.09)

def K(x, a):
    u1 = (a - 2*np.pi*x)/2; u2 = (a + 2*np.pi*x)/2
    return 0.5*(np.sinc(u1/np.pi) + np.sinc(u2/np.pi))

def make_w(a):
    k0 = K(np.array([0.0]), a)[0]
    def w(x):
        x = np.atleast_1d(np.asarray(x, dtype=float))
        out = np.where((x > 0) & (x <= X_CUT), (K(np.clip(x, 1e-12, None), a)/k0)**2, 0.0)
        return out if out.size > 1 else float(out[0])
    return w

PAIRS = [(i,j,2.0/(7-(j-i))) for i in range(6) for j in range(i+1,6)]

PAIRS21 = [(i,j,2.0/(7-(j-i))) for i in range(7) for j in range(i+1,7)]  # CANONICAL per CONVENTIONS.md

def F_B(g, p, q, w):
    # C21 canonical objective (tools/CONVENTIONS.md): 21 pairs incl. distances from y_0=0
    g = np.asarray(g, float)
    s = float(np.dot(p, g))
    s += float(np.dot(q, w(g)))
    y = np.concatenate([[0.0], np.cumsum(g)])
    for i,j,a_ij in PAIRS21:
        d = y[j]-y[i]
        if 0 < d <= X_CUT:
            s += a_ij * float(w(d))
    return s

_CUR = {}
def _obj(g):
    return F_B(g, *_CUR["args"])

def min_FB(p, q, a, seed=0, de_iter=180):
    w = make_w(a)
    _CUR["args"] = (p, q, w)
    r = differential_evolution(_obj, [(0.0, 25.0)]*6, seed=seed, maxiter=de_iter,
                               popsize=20, tol=1e-11, polish=True)
    # multi-start polish
    best, bg = r.fun, r.x
    for g0 in [r.x, np.full(6, 0.767), np.full(6, 1.77), np.full(6, 4.8), np.full(6, 11.3)]:
        r2 = minimize(lambda g: -F_B(g, p, q, w), g0, method="Nelder-Mead",
                      options={"maxiter": 8000, "xatol":1e-12, "fatol":1e-16})
        if -r2.fun < best: best, bg = -r2.fun, r2.x
    return best, bg

def unpack(theta):
    lam, a_, b_, c_, u, v, ww, alpha = theta
    s = 2*(a_+b_+c_)
    ra = np.array([a_,b_,c_,c_,b_,a_])/s
    p = ra * lam/320.0
    qq = np.array([u,v,ww,ww,v,u]); qq = qq/qq.sum()*2.0*lam
    return p, qq, alpha, lam

def eps_of(theta, seed=0):
    lam, a_, b_, c_, u, v, ww, alpha = theta
    if not (0.3 <= alpha <= 3.0 and 0.3 <= lam <= 3.0): return -1e9, None
    if min(a_,b_,c_) < 1e-4 or min(u,v,ww) < 1e-4: return -1e9, None
    p, q, a, lam = unpack(theta)
    e, _ = min_FB(p, q, a, seed=seed)
    return e, (p, q, a, lam)

def bound_from(e, a, lam, mmax=400):
    def H(aa):
        I0 = 2*np.sin(aa/2)/aa; I2 = 0.5 + np.sin(aa)/(2*aa)
        J  = -2*I2/aa**2 + (np.sin(aa/2)/aa + 2*np.cos(aa/2)/aa**2)*I0
        return 2 - 1/(I0**2/(I2+J))
    best = (-1e9, None)
    for m in range(40, mmax+1):
        A = e*(m-6); cap = m/(m-1)
        phi = A if A <= cap else 2*np.sqrt((m-1)*A/m) - 1 + A/m
        tau = (lam/320)*(m-6)/m
        bnd = (H(a) - tau)/(1 - phi/m)
        if bnd > best[0]: best = (bnd, m)
    return best

if __name__ == "__main__":
    import sys, json, time
    lam0, alpha0 = 1.15, 1.464
    raw = np.array([946,1177,877,877,1177,946], float)
    p0 = raw*lam0/1920000.0
    q0 = lam0*np.array([0.31343, 1/3, 105971/300000, 105971/300000, 1/3, 0.31343])
    t=time.time()
    e0, g0 = min_FB(p0, q0, alpha0, seed=1)
    print(f"RECORD POINT (faithful): min F_B = {e0:.7f} (certified 0.00703) g={np.round(g0,3)} [{time.time()-t:.0f}s]")
    b0, m0 = bound_from(e0, alpha0, lam0)
    print(f"  bound(m={m0}) = {b0:.10f}  (certified chain gives 0.6735633 from rigorous eps)")
    # joint optimization from record neighborhood
    theta0 = np.array([1.15, 1.0, 1.24255, 0.92766, 0.31343, 1/3, 0.353237, 1.464])
    # raw ratios: 946/1177/877 -> normalize a+b+c=0.5: a=946/6000*? use raw/sum*0.5*2... set a,b,c prop to raw
    theta0[1], theta0[2], theta0[3] = 946/6000, 1177/6000, 877/6000  # sums to 0.5 -> 2(a+b+c)=1 ok
    best_theta = theta0.copy(); best_e, _ = eps_of(theta0, seed=2)
    print(f"start theta eps={best_e:.7f}")
    rng = np.random.default_rng(7)
    scales = np.array([0.05, 0.02, 0.02, 0.02, 0.01, 0.01, 0.01, 0.02])
    T0 = time.time()
    for it in range(60):
        cand = best_theta * (1 + rng.normal(0, 1, 8)*scales)
        e, pack = eps_of(cand, seed=it)
        if e > best_e:
            best_e, best_theta = e, cand
            p,q,a,lam = pack
            b, m = bound_from(e, a, lam)
            print(f"[it {it}] eps={e:.7f} bound(m={m})={b:.10f} lam={lam:.4f} alpha={a:.4f} [{time.time()-T0:.0f}s]", flush=True)
    p,q,a,lam = unpack(best_theta)
    b, m = bound_from(best_e, a, lam)
    print(json.dumps({"eps": best_e, "bound": b, "m": m, "alpha": a, "lam": lam,
                      "p": list(p), "q": list(q)}, indent=1))
    print("RECORD: eps=0.00703 bound=0.6735633479946228")
