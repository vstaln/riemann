#!/usr/bin/env python3
"""Verify A4 piece groupings by 3D quadrature over ALL of R^3, using the whole-line
substitution u = x/(1-x^2) (GL on x in (-1,1)) so tails are handled exactly.

Terms of rho4 = det[S]_4x4 with the 6 edge S's; each piece
   P = intintint K(u)K(v)K(w)K(u+v+w) * term dudvdw
computed on the full space. Symmetry orbits (dihedral group of the square):
  S^2: 4 adjacent (S12^2,S23^2,S34^2,S14^2) + 2 diagonal (S13^2,S24^2)
  S^2S^2: E1=S12^2S34^2 (=E3=S14^2S23^2 by reflection), E2=S13^2S24^2 (own orbit)
  triples: all 4 in one orbit
  quads: q1 (own orbit), q2=q3 (reflection pair)
Also directly assembles A4 and compares with the analytic reduced form
  A4 = 1/la^3 - 6J/la^2 + (2E1+E2) + 8t - 2(q1+2q2).
"""
import numpy as np

def gl(n):
    x, w = np.polynomial.legendre.leggauss(n)
    return x, w

def sinc(x): return np.sinc(x)

def transform(xs):
    """u = x/(1-x^2); returns u and |du/dx|."""
    return xs/(1-xs**2), (1+xs**2)/(1-xs**2)**2

def piece_int(la, n, termfn):
    x, w = gl(n)
    uu, jac = transform(x)
    wu = w*jac
    U, V, W = np.meshgrid(uu, uu, uu, indexing='ij')
    wvol = np.einsum('i,j,k->ijk', wu, wu, wu)
    S12 = sinc(U); S23 = sinc(V); S34 = sinc(W)
    S13 = sinc(U+V); S24 = sinc(V+W); S14 = sinc(U+V+W)
    K4 = sinc(la*U)*sinc(la*V)*sinc(la*W)*sinc(la*(U+V+W))
    return float(np.sum(K4*termfn(S12, S23, S34, S13, S24, S14)*wvol))

def run(la, n):
    print(f"la={la} n={n} (full-space GL):")
    p = {}
    p["S12^2"] = piece_int(la, n, lambda S12,S23,S34,S13,S24,S14: S12**2)
    p["S13^2"] = piece_int(la, n, lambda S12,S23,S34,S13,S24,S14: S13**2)
    p["S14^2"] = piece_int(la, n, lambda S12,S23,S34,S13,S24,S14: S14**2)
    p["S23^2"] = piece_int(la, n, lambda S12,S23,S34,S13,S24,S14: S23**2)
    p["S24^2"] = piece_int(la, n, lambda S12,S23,S34,S13,S24,S14: S24**2)
    p["S34^2"] = piece_int(la, n, lambda S12,S23,S34,S13,S24,S14: S34**2)
    print("  S^2:", " ".join(f"{k}={v:.8f}" for k, v in p.items()))
    E1 = piece_int(la, n, lambda S12,S23,S34,S13,S24,S14: S12**2*S34**2)
    E2 = piece_int(la, n, lambda S12,S23,S34,S13,S24,S14: S13**2*S24**2)
    E3 = piece_int(la, n, lambda S12,S23,S34,S13,S24,S14: S14**2*S23**2)
    print(f"  S2S2: E1={E1:.8f} E2={E2:.8f} E3={E3:.8f}")
    t1 = piece_int(la, n, lambda S12,S23,S34,S13,S24,S14: S12*S23*S13)
    t2 = piece_int(la, n, lambda S12,S23,S34,S13,S24,S14: S12*S24*S14)
    t3 = piece_int(la, n, lambda S12,S23,S34,S13,S24,S14: S13*S34*S14)
    t4 = piece_int(la, n, lambda S12,S23,S34,S13,S24,S14: S23*S34*S24)
    print(f"  triples: t1={t1:.8f} t2={t2:.8f} t3={t3:.8f} t4={t4:.8f}")
    q1 = piece_int(la, n, lambda S12,S23,S34,S13,S24,S14: S12*S23*S34*S14)
    q2 = piece_int(la, n, lambda S12,S23,S34,S13,S24,S14: S12*S24*S34*S13)
    q3 = piece_int(la, n, lambda S12,S23,S34,S13,S24,S14: S13*S23*S24*S14)
    print(f"  quads: q1={q1:.8f} q2={q2:.8f} q3={q3:.8f}")
    T1 = 1.0/la**3
    A4 = T1 - sum(p.values()) + (E1+E2+E3) + 2*(t1+t2+t3+t4) - 2*(q1+q2+q3)
    print(f"  A4 assembled = {A4:.8f}")
    return dict(E1=E1, E2=E2, E3=E3, t1=t1, t2=t2, t3=t3, t4=t4, q1=q1, q2=q2, q3=q3, A4=A4,
                s12=p["S12^2"], s13=p["S13^2"])

if __name__ == "__main__":
    for la in (1.0, 0.5, 1/3):
        res = {}
        for n in (28, 44, 64):
            res[n] = run(la, n)
            print()
        # convergence summary
        base = res[64]
        print(f"summary la={la}: E1={base['E1']:.8f} E2={base['E2']:.8f} "
              f"t={base['t1']:.8f} q1={base['q1']:.8f} q2={base['q2']:.8f} A4={base['A4']:.8f}")
        print()
