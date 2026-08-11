#!/usr/bin/env python3
"""Verify each piece of the m4 diagram reduction by direct Monte Carlo at lambda=1.
Pieces (all *dudvdw, K=S=sinc(pi x), x1-x2=u,x2-x3=v,x3-x4=w, x1-x4=u+v+w):
  T1  = int K(u)K(v)K(w)K(u+v+w)                       = 1          (analytic)
  S2u = int ... S(u)^2                                 = J/lam^2, J=int S^2K^2=2/3 (at lam=1) -> 2/3
  E   = int ... S(u)^2 S(w)^2                          = 12/35 (closed via tri2^3) 
  F   = int ... S(u)S(v)S(u+v)                         = (1-lam/2)/lam = 1/2
  G4c = int ... S(u)S(v)S(w)S(u+v+w)                   = int tri(ξ)^4 = 2/5
  also S13^2 S24^2 and S14^2 S23^2 pieces -> compare to E
Monte Carlo on [-B,B]^3 with B=25, N samples, importance-weighted.
"""
import numpy as np
rng = np.random.default_rng(5)
B = 25.0
N = 2_000_000
u = rng.uniform(-B, B, N); v = rng.uniform(-B, B, N); w = rng.uniform(-B, B, N)
vol = (2*B)**3
def sinc(x): return np.sinc(x)
Su = sinc(u); Sv = sinc(v); Sw = sinc(w)
Suv = sinc(u+v); Svw = sinc(v+w); Suvw = sinc(u+v+w)
Kprod = sinc(u)*sinc(v)*sinc(w)*sinc(u+v+w)   # K(u)K(v)K(w)K(u+v+w) at lam=1

def mc(x): return vol*np.mean(x)
print("MC estimates (B=25, N=2e6):")
print("  T1   =", mc(Kprod), "  (analytic 1)")
print("  S12^2 =", mc(Kprod*Su**2), "  (analytic J/lam^2 = 2/3)")
print("  S13^2 =", mc(Kprod*Suv**2))
print("  S14^2 =", mc(Kprod*Suvw**2))
print("  E  S12^2 S34^2 =", mc(Kprod*Su**2*Sw**2), "  (closed 12/35 = 0.342857)")
print("  E' S13^2 S24^2 =", mc(Kprod*Suv**2*Svw**2))
print("  E''S14^2 S23^2 =", mc(Kprod*Suvw**2*Sv**2))
print("  F  S12 S23 S13 =", mc(Kprod*Su*Sv*Suv), "  (closed 1/2)")
print("  F' S13 S34 S14 =", mc(Kprod*Suv*Sw*Suvw))
print("  G  S12 S23 S34 S14 =", mc(Kprod*Su*Sv*Sw*Suvw), "  (closed 2/5)")
print("  G' S12 S24 S34 S13 =", mc(Kprod*Su*Svw*Sw*Suv))
print("  G''S13 S23 S24 S14 =", mc(Kprod*Suv*Sv*Svw*Suvw))
# sanity: full A4 = 1 - 6*(2/3) + 3E - 2*3*G + 2*4*F   (coeffs: -1 each S2, +1 each S2S2, -2 each 4cyc, +2 each tri)
E = 12/35; F = 1/2; G = 2/5
A4_an = 1 - 6*(2/3) + 3*E - 2*3*G + 2*4*F
m4_an = 1 + 6*(1/3) + 2/3 + A4_an
print("\nA4 analytic =", A4_an, " m4(1) =", m4_an, "  (paper 13/4 = 3.25)")
# MC full A4 integrand
rho4 = (1 - (Su**2+Suv**2+Suvw**2+Sv**2+Svw**2+Sw**2)
        + (Su**2*Sw**2 + Suv**2*Svw**2 + Suvw**2*Sv**2)
        + 2*(Su*Sv*Suv + Su*Svw*Suvw + Suv*Sw*Suvw + Sv*Sw*Svw)
        - 2*(Su*Sv*Sw*Suvw + Su*Svw*Sw*Suv + Suv*Sv*Svw*Suvw))
print("  MC full A4 =", mc(Kprod*(rho4-1)) + 1)
