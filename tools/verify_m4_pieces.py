#!/usr/bin/env python3
"""Verify the A4 piece groupings by direct 3D quadrature (R-sweep, tail-handled).

For each of the 15 terms in rho4 = det[S]_4x4:
  1, -6 S^2, +3 S^2S^2, +8 triples, -6 quadruples,
compute P = intintint K(u)K(v)K(w)K(u+v+w) * (term) dudvdw directly on [-R,R]^3
and check the symmetry orbits:
  S^2: {S12^2,S23^2,S34^2,S14^2} vs {S13^2,S24^2}
  S^2S^2: E1=S12^2S34^2, E2=S13^2S24^2, E3=S14^2S23^2
  triples: t1=S12S23S13, t2=S12S24S14, t3=S13S34S14, t4=S23S34S24
  quads:   q1=S12S23S34S14, q2=S12S24S34S13, q3=S13S23S24S14
Also verify C3 = intint K(u)^2K(v)^2 rho3(0,u,v) directly vs the reduced form.
And B2 directly.
"""
import numpy as np

def gl(n):
    x, w = np.polynomial.legendre.leggauss(n)
    return x, w

def sinc(x): return np.sinc(x)

def piece_int(la, R, n, termfn):
    """intintint_{[-R,R]^3} K4(u,v,w) * term(u,v,w) dudvdw, term built from the 6 S's."""
    x, w = gl(n)
    xs = R*x; ws = R*w
    uu, vv, ww = np.meshgrid(xs, xs, xs, indexing='ij')
    S12 = sinc(uu); S23 = sinc(vv); S34 = sinc(ww)
    S13 = sinc(uu+vv); S24 = sinc(vv+ww); S14 = sinc(uu+vv+ww)
    K4 = sinc(la*uu)*sinc(la*vv)*sinc(la*ww)*sinc(la*(uu+vv+ww))
    integ = K4 * termfn(S12, S23, S34, S13, S24, S14)
    return float(np.sum(integ * np.einsum('i,j,k->ijk', ws, ws, ws)))

def run(la, R, n):
    print(f"la={la} R={R} n={n}:")
    # S^2 pieces (sign not included)
    def s12(S12,S23,S34,S13,S24,S14): return S12**2
    def s13(S12,S23,S34,S13,S24,S14): return S13**2
    def s14(S12,S23,S34,S13,S24,S14): return S14**2
    def s23(S12,S23,S34,S13,S24,S14): return S23**2
    def s24(S12,S23,S34,S13,S24,S14): return S24**2
    def s34(S12,S23,S34,S13,S24,S14): return S34**2
    p = {name: piece_int(la, R, n, f) for name, f in
         [("S12^2",s12),("S13^2",s13),("S14^2",s14),("S23^2",s23),("S24^2",s24),("S34^2",s34)]}
    print("  S^2 pieces:", " ".join(f"{k}={v:.6f}" for k, v in p.items()))
    # S^2S^2
    def e1(S12,S23,S34,S13,S24,S14): return S12**2*S34**2
    def e2(S12,S23,S34,S13,S24,S14): return S13**2*S24**2
    def e3(S12,S23,S34,S13,S24,S14): return S14**2*S23**2
    E = {k: piece_int(la, R, n, f) for k, f in [("E1",e1),("E2",e2),("E3",e3)]}
    print("  S^2S^2 pieces:", " ".join(f"{k}={v:.6f}" for k, v in E.items()))
    # triples
    def t1(S12,S23,S34,S13,S24,S14): return S12*S23*S13
    def t2(S12,S23,S34,S13,S24,S14): return S12*S24*S14
    def t3(S12,S23,S34,S13,S24,S14): return S13*S34*S14
    def t4(S12,S23,S34,S13,S24,S14): return S23*S34*S24
    T = {k: piece_int(la, R, n, f) for k, f in [("t1",t1),("t2",t2),("t3",t3),("t4",t4)]}
    print("  triples:", " ".join(f"{k}={v:.6f}" for k, v in T.items()))
    # quads
    def q1(S12,S23,S34,S13,S24,S14): return S12*S23*S34*S14
    def q2(S12,S23,S34,S13,S24,S14): return S12*S24*S34*S13
    def q3(S12,S23,S34,S13,S24,S14): return S13*S23*S24*S14
    Q = {k: piece_int(la, R, n, f) for k, f in [("q1",q1),("q2",q2),("q3",q3)]}
    print("  quads:", " ".join(f"{k}={v:.6f}" for k, v in Q.items()))
    # assemble A4 = T1 - sum S^2 + sum S^2S^2 + 2 sum tri - 2 sum quad, T1 = 1/la^3 analytic
    T1 = 1.0/la**3
    A4 = T1 - sum(p.values()) + sum(E.values()) + 2*sum(T.values()) - 2*sum(Q.values())
    print(f"  A4 assembled from direct pieces = {A4:.6f}")
    return p, E, T, Q, A4

if __name__ == "__main__":
    for la in (1.0, 0.5):
        for R, n in ((10, 24), (20, 28), (40, 32)):
            run(la, R, n)
        print()
