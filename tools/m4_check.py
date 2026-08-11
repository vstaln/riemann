#!/usr/bin/env python3
"""m4(1) via determinantal diagram expansion, vectorized. Check vs paper's 13/4.
rho4(u,v,w) = det[S(x_i-x_j)] with x1-x2=u,x2-x3=v,x3-x4=w:
  = 1 - sum_{i<j} S_ij^2 + (S12^2 S34^2 + S13^2 S24^2 + S14^2 S23^2)
    + 2*(S12 S23 S13 + S12 S24 S14 + S13 S34 S14 + S23 S34 S24)
    - 2*(S12 S23 S34 S14 + S12 S24 S34 S13 + S13 S23 S24 S14)
A4 = intintint K(u)K(v)K(w)K(u+v+w) rho4 dudvdw; '1'-term = 1 (la=1) analytic.
m4 = 1 + 6*A2 + D4 + A4, A2=1/3, D4=2/3 at la=1.
"""
import numpy as np

def gl(n):
    x, w = np.polynomial.legendre.leggauss(n)
    return x, w

def rho4_vec(uu, vv, ww):
    S12 = np.sinc(uu); S23 = np.sinc(vv); S34 = np.sinc(ww)
    S13 = np.sinc(uu+vv); S24 = np.sinc(vv+ww)
    S14 = np.sinc(uu+vv+ww)
    r = 1.0 - (S12**2 + S13**2 + S14**2 + S23**2 + S24**2 + S34**2)
    r = r + (S12**2*S34**2 + S13**2*S24**2 + S14**2*S23**2)
    r = r + 2.0*(S12*S23*S13 + S12*S24*S14 + S13*S34*S14 + S23*S34*S24)
    r = r - 2.0*(S12*S23*S34*S14 + S12*S24*S34*S13 + S13*S23*S24*S14)
    return r

def A4_fast(R, n=48):
    x, w = gl(n)
    xs = R*x; ws = R*w
    uu, vv, ww = np.meshgrid(xs, xs, xs, indexing='ij')
    K4 = np.sinc(uu)*np.sinc(vv)*np.sinc(ww)*np.sinc(uu+vv+ww)
    r4 = rho4_vec(uu, vv, ww)
    integ = K4*(r4 - 1.0)      # subtract the '1' (analytic = 1 at la=1)
    return float(np.sum(integ * np.einsum('i,j,k->ijk', ws, ws, ws)))

for R in (10, 20, 40):
    A4 = 1.0 + A4_fast(R)
    m4v = 1 + 6*(1/3.0) + 2/3.0 + A4
    print(f"R={R:3d}: A4 = {A4:+.6f}   m4(1) = {m4v:.6f}   (paper: 13/4 = 3.25)")

# also verify rho4 formula against np.linalg.det at a random point
rng = np.random.default_rng(0)
for _ in range(3):
    u, v, w = rng.uniform(-2, 2, 3)
    S12=np.sinc(u); S23=np.sinc(v); S34=np.sinc(w); S13=np.sinc(u+v); S24=np.sinc(v+w); S14=np.sinc(u+v+w)
    M = np.array([[1,S12,S13,S14],[S12,1,S23,S24],[S13,S23,1,S34],[S14,S24,S34,1]])
    det = np.linalg.det(M)
    my = rho4_vec(np.array([u]), np.array([v]), np.array([w]))[0]
    print(f"  rho4 check at u,v,w=({u:.3f},{v:.3f},{w:.3f}): linalg={det:.6f} formula={my:.6f}")
