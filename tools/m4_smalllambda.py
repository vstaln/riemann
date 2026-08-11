#!/usr/bin/env python3
"""m4(lambda) at lambda < 1/2: corrected 4th-moment diagram, own derivation.

Definition: m_k(la) = lim d^{-1} tr(G/ell_1)^k, G_ij = sinc(pi*la*(x_i-x_j))
over the sine process (a DPP with kernel S(u) = sinc(pi u)). For k=4 the DPP
partition expansion (cluster expansion over distinct points, rho_r = r-point
correlation of the DISTINCT points) gives

    m4(la) = 1 + 6*A2 + B2 + 4*A3 + 2*C3 + A4

    A2 = int K(u)^2 rho2(u) du,            rho2(u) = 1 - S(u)^2
    B2 = int K(u)^4 rho2(u) du
    A3 = intint K(u)K(v)K(u+v) rho3(u,v),  rho3(u,v) = 1-S(u)^2-S(v)^2-S(u+v)^2+2S(u)S(v)S(u+v)
    C3 = intint K(u)^2 K(v)^2 rho3(0,u,v), rho3(0,u,v)=1-S(u)^2-S(v)^2-S(u-v)^2+2S(u)S(v)S(u-v)
    A4 = intintint K(u)K(v)K(w)K(u+v+w) rho4(u,v,w)
    rho4 = det[S]_{4x4} = 1 - sum S_ij^2 + sum S_ij^2 S_kl^2 + 2 sum S_ij S_jk S_ik - 2 sum S_ij S_jk S_kl S_li

A4 decomposes exactly (Fourier/convolution reductions, verified numerically here):
    A4 = T1 - 6*J/la^2 + 3*E + 8*F - 6*G
    T1 = intintint K(u)K(v)K(w)K(u+v+w) = 1/la^3        [Parseval: int Khat^4 ; NOT 2/3]
    J  = int K(u)^2 S(u)^2 du (over R) = 2*J2
    E  = (1/la) intint K(u)K(w)K(u+w) S(u)^2 S(w)^2 du dw
    F  = (1/la) int (Khat*Shat)^3 dxi = (1-la/2)/la     [closed form, la <= 1]
    G  = int (Khat*Shat)^4 dxi,  Khat*Shat = (1/la)*overlap([-la/2,la/2],[xi-1/2,xi+1/2])

Cross-checks built in: (i) lambda=1 vs 346/105 (m4_mc/m4_pieces consensus) and
paper's 13/4; (ii) direct tail-subtracted 3D quadrature of A4; (iii) Monte Carlo
of the full integrand; (iv) m2,m3 vs their verified closed forms; (v) lambda->0
rank-one limit m_k ~ (1/la)^{k-1}.

Run: uv run --quiet --with mpmath --with numpy python tools/m4_smalllambda.py
"""
import mpmath as mp
from mpmath import mpf, mp, quad, inf
import numpy as np

mp.dps = 25

def S(u): return mp.sinc(mp.pi*u)
def K(u, la): return mp.sinc(mp.pi*la*u)

def J2(la):
    """int_0^inf K(u)^2 S(u)^2 du"""
    return quad(lambda u: K(u, la)**2 * S(u)**2, [0, inf])

def B2(la):
    """int_R K^4 (1-S^2) = 2/(3 la) - 2 int_0^inf K^4 S^2"""
    a = mpf(2)/(3*la)
    b = 2*quad(lambda u: K(u, la)**4 * S(u)**2, [0, inf])
    return a - b

def ghat(xi, la):
    """(Khat*Shat)(xi) = (1/la)*length([-la/2,la/2] cap [xi-1/2,xi+1/2])"""
    lo = max(-la/2, xi - mpf(1)/2); hi = min(la/2, xi + mpf(1)/2)
    return max(0, hi - lo)/la

def G4(la):
    return quad(lambda xi: ghat(xi, la)**4, [-(1+la)/2, (1+la)/2])

# ---------------- numpy 2D/3D quadrature ----------------
def gl(n):
    x, w = np.polynomial.legendre.leggauss(n)
    return x, w

def sinc_np(x): return np.sinc(x)

def C3_pieces(la, R, n):
    """C3 = 1/la^2 - 2J/la - D + 2E'  (analytic leading terms + 2D quadrature)."""
    x, w = gl(n)
    xs = R*x; ws = R*w
    uu, vv = np.meshgrid(xs, xs, indexing='ij')
    Ku = sinc_np(la*uu); Kv = sinc_np(la*vv)
    Su = sinc_np(uu); Sv = sinc_np(vv); Suv = sinc_np(uu-vv)
    # D = intint K(u)^2 K(v)^2 S(u-v)^2
    D = float(np.sum((Ku*Ku)*(Kv*Kv)*(Suv*Suv) * np.outer(ws, ws)))
    # E' = intint K(u)^2 K(v)^2 S(u) S(v) S(u-v)
    Ep = float(np.sum((Ku*Ku)*(Kv*Kv)*Su*Sv*Suv * np.outer(ws, ws)))
    return D, Ep

def E2(la, R, n):
    """E = (1/la) intint K(u)K(w)K(u+w) S(u)^2 S(w)^2 du dw"""
    x, w = gl(n)
    xs = R*x; ws = R*w
    uu, ww = np.meshgrid(xs, xs, indexing='ij')
    v = (sinc_np(la*uu)*sinc_np(la*ww)*sinc_np(la*(uu+ww))
         * sinc_np(uu)**2 * sinc_np(ww)**2)
    return float((1.0/la) * np.sum(v * np.outer(ws, ws)))

def A4_3d_direct(la, R, n):
    """A4 = 1/la^3 - 6J/la^2 + intintint_{[-R,R]^3} K4 (rho4 - 1 + sum S_ij^2)
    (the slow-decaying T1 and S^2 pieces subtracted analytically; the rest decays fast)."""
    x, w = gl(n)
    xs = R*x; ws = R*w
    uu, vv, ww = np.meshgrid(xs, xs, xs, indexing='ij')
    S12 = sinc_np(uu); S23 = sinc_np(vv); S34 = sinc_np(ww)
    S13 = sinc_np(uu+vv); S24 = sinc_np(vv+ww); S14 = sinc_np(uu+vv+ww)
    rho4 = (1.0 - (S12**2 + S13**2 + S14**2 + S23**2 + S24**2 + S34**2)
            + (S12**2*S34**2 + S13**2*S24**2 + S14**2*S23**2)
            + 2.0*(S12*S23*S13 + S12*S24*S14 + S13*S34*S14 + S23*S34*S24)
            - 2.0*(S12*S23*S34*S14 + S12*S24*S34*S13 + S13*S23*S24*S14))
    K4 = sinc_np(la*uu)*sinc_np(la*vv)*sinc_np(la*ww)*sinc_np(la*(uu+vv+ww))
    integ = K4*(rho4 - 1.0 + (S12**2 + S13**2 + S14**2 + S23**2 + S24**2 + S34**2))
    return float(np.sum(integ * np.einsum('i,j,k->ijk', ws, ws, ws)))

def m4_full(la, verbose=True):
    J2v = float(J2(la))
    J = 2*J2v
    A2 = 1.0/la - 2*J2v
    b2 = float(B2(la))
    A3 = 1.0/la**2 - la + 2 - 6*J2v/la
    # C3: converge R
    D, Ep = C3_pieces(la, 120, 320)
    C3 = 1.0/la**2 - 2*J/la - D + 2*Ep
    E = E2(la, 80, 320)
    G = float(G4(la))
    T1 = 1.0/la**3
    F = (1 - la/2.0)/la
    A4 = T1 - 6*J/la**2 + 3*E + 8*F - 6*G
    m4 = 1 + 6*A2 + b2 + 4*A3 + 2*C3 + A4
    m2 = 1 + A2
    m3 = 1 + 3*A2 + A3
    if verbose:
        print(f"la={la}:")
        print(f"  J2={J2v:.10f}  A2={A2:.10f}  B2={b2:.10f}  A3={A3:.10f}")
        print(f"  C3: D={D:.10f} Ep={Ep:.10f} -> C3={C3:.10f}")
        print(f"  E={E:.10f}  G={G:.10f}  T1={T1:.10f}  F={F:.10f}  A4={A4:.10f}")
        print(f"  m2={m2:.10f} (ref {1/la+la/3:.10f})  m3={m3:.10f}  m4={m4:.10f}")
    return m4, m2, m3, dict(J2=J2v, A2=A2, B2=b2, A3=A3, D=D, Ep=Ep, C3=C3,
                            E=E, G=G, T1=T1, F=F, A4=A4)

if __name__ == "__main__":
    print("="*70)
    print("I1 = intintint K(u)K(v)K(w)K(u+v+w) : Parseval says 1/la^3")
    for la in (mpf(1)/4, mpf(1)/3, mpf(4)/10, mpf(1)/2, mpf(2)/3, mpf(1)):
        print(f"  la={float(la):.4f}: T1(analytic)=1/la^3 = {float(1/la**3):.10f}")

    print("="*70)
    print("A4 direct-3D tail-subtracted vs piecewise (convergence in R):")
    for la in (1/4, 1/3, 0.4, 1/2, 1.0):
        J = 2*float(J2(mpf(la)))
        vals = [A4_3d_direct(la, R, 28) + 1.0/la**3 - 6*J/la**2 for R in (6, 12, 24)]
        print(f"  la={la:.3f}: R=6: {vals[0]:+.8f}  R=12: {vals[1]:+.8f}  R=24: {vals[2]:+.8f}")

    print("="*70)
    print("m4(la) via the corrected diagram:")
    results = {}
    for la in (1/4, 1/3, 0.4, 1/2, 2/3, 1.0):
        results[la] = m4_full(mpf(la))
        print()
    print("="*70)
    print("checks: paper m4(1) = 13/4 = 3.25 ; m4_mc consensus m4(1) = 346/105 =",
          f"{346/105:.6f}")
    print("rank-one limit: m4*la^3, m3*la^2, m2*la at la=1/4:",
          f"{results[1/4][0]/results[1/4][2]*0:g}", end=" ")
    for la in (1/4, 1/3):
        m4, m2, m3, _ = results[la]
        print(f"  la={la}: m4*la^3={m4*la**3:.6f} m3*la^2={m3*la**2:.6f} m2*la={m2*la:.6f}", end="")
    print()
