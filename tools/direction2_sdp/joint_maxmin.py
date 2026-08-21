#!/usr/bin/env python3
"""Joint max-min optimization of the F_B coboundary block inequality.

Scalar problem (extracted from tools/dilation-cert + verify_coboundary_floor.py):
  F_B(g) = sum_i p_i g_i + sum_i q_i w(g_i) + sum_{i<j} a_ij w(y_j - y_i),  g >= 0 (6 gaps)
  w(x)   = (K(x)/K(0))^2,  K(x) = [sinc((a-2pi x)/2) + sinc((a+2pi x)/2)]/2,  a = alpha
  a_ij   = 2/(7-(j-i))
  Record parameterization: p_i = raw_i * lambda/1920000 (sum raw = 6000 => sum p = lambda/320),
  q symmetric summing to 2, y_j - y_i = sum of gaps i..j-1.

  bound(m) = (H(alpha) - tau) / (1 - phi_m(A)/m)
  H(a)     = 2 - 1/c,  c = I0^2/(I2+J)
  tau      = psum*(m-6)/m,  psum = lambda/320
  A        = eps*(m-6);  phi_m(A)=A if A<=m/(m-1) else 2 sqrt((m-1)A/m)-1+A/m

Joint max-min NEVER run (weights came from external 'tawanerguo' design, re-certified only).
If eps* > 0.00703 at improved bound -> record candidate -> Arb certification next.
"""
import numpy as np
from scipy.optimize import minimize, differential_evolution

def K(x, a):
    u1 = (a - 2*np.pi*x)/2; u2 = (a + 2*np.pi*x)/2
    def sinc(u): return np.sinc(u/np.pi)
    return 0.5*(sinc(u1) + sinc(u2))

def make_w(a):
    k0 = K(np.array([0.0]), a)[0]
    def w(x):
        x = np.asarray(x, dtype=float)
        k = K(x, a)
        return (k/k0)**2
    return w

# pair indices i<j over 6 gaps, weight 2/(7-(j-i))
PAIRS = [(i,j,2.0/(7-(j-i))) for i in range(6) for j in range(i+1,6)]

def F_B(g, p, q, w):
    s = float(np.dot(p, g) + np.dot(q, w(g)))
    y = np.concatenate([[0.0], np.cumsum(g)])  # y_0..y_6
    for i,j,a_ij in PAIRS:
        s += a_ij * float(w(y[j]-y[i]))
    return s

def min_FB(p, q, a, n_starts=40, seed=0):
    """min over g>=0 of F_B; multi-start L-BFGS + coarse grid seed."""
    w = make_w(a)
    rng = np.random.default_rng(seed)
    best = np.inf; bg = None
    # coarse random seeds in plausible box (record g scale: eps~0.007, p~0.001/gap-unit =>
    # g ~ O(1)); use box [0,3]
    starts = [np.full(6, 0.5), np.full(6, 1.0), np.full(6, 1.5)]
    starts += [rng.uniform(0, 3, 6) for _ in range(n_starts)]
    for g0 in starts:
        r = minimize(lambda g: -F_B(g, p, q, w), g0, method="Nelder-Mead",
                     options={"maxiter": 4000, "xatol":1e-10, "fatol":1e-14})
        if -r.fun < best:
            best = -r.fun; bg = r.x
    return best, bg

def unpack(theta):
    """theta = [lam, a, b, c, u, v, ww, alpha]:
       p redistribution r=(a,b,c,c,b,a), sum=2(a+b+c)=1;
       q symmetric (u,v,ww,ww,v,u), sum=2(u+v+ww)=2."""
    lam, a_, b_, c_, u, v, ww, alpha = theta
    s = 2*(a_+b_+c_)
    ra = np.array([a_,b_,c_,c_,b_,a_])/s
    p = ra * lam/320.0 * 1.0  # sum p = lam/320
    qq = np.array([u,v,ww,ww,v,u])
    qq = qq / qq.sum() * 2.0
    return p, qq, alpha, lam

def eps_of(theta, seed=0):
    p, q, a, lam = unpack(theta)
    if a <= 0.5 or a > 3.0 or lam <= 0.2 or lam > 3.0: return -1e9, None
    e, _ = min_FB(p, q, a, n_starts=24, seed=seed)
    return e, (p, q, a, lam)

def bound_from(e, a, lam, mmax=400):
    def H(aa):
        I0 = 2*np.sin(aa/2)/aa
        I2 = 0.5 + np.sin(aa)/(2*aa)
        J  = -2*I2/aa**2 + (np.sin(aa/2)/aa + 2*np.cos(aa/2)/aa**2)*I0
        c  = I0**2/(I2+J)
        return 2 - 1/c
    best = (-1e9, None)
    for m in range(40, mmax+1):
        A = e*(m-6)
        cap = m/(m-1)
        phi = A if A <= cap else 2*np.sqrt((m-1)*A/m) - 1 + A/m
        tau = (lam/320)*(m-6)/m
        bnd = (H(a) - tau)/(1 - phi/m)
        if bnd > best[0]: best = (bnd, m)
    return best

if __name__ == "__main__":
    # record point sanity
    lam0, alpha0 = 1.15, 1.464
    raw = np.array([946,1177,877,877,1177,946], float)
    p0 = raw*lam0/1920000.0
    q0 = np.array([0.31343, 1/3, 105971/300000, 105971/300000, 1/3, 0.31343])
    e0, g0 = min_FB(p0, q0, alpha0, n_starts=60, seed=1)
    print(f"RECORD POINT: eps_min F_B = {e0:.7f}  (certified 0.00703)  at g={np.round(g0,4)}")
    b0, m0 = bound_from(e0, alpha0, lam0)
    print(f"  bound(m={m0}) = {b0:.16f}  (record 0.6735633479946228)")
    # NOTE: certified eps uses rigorous lower bounds; our float min is an upper estimate of the true inf,
    # so b0 here is optimistic vs the certified chain unless e0 <= 0.00703.
