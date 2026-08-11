#!/usr/bin/env python3
"""Joint-certificate inputs: m_k(lambda) at lambda = 1/2 (window B), 2/3, 1 (window A).

Closed-form reduction (from m3_check.py / m3_pin.py, all 1D mpmath integrals):
  m2 = 1 + A2,  A2 = 1/la - 2*J2,   J2 = int_0^inf sinc(pi la u)^2 sinc(pi u)^2 du
  m3 = 1 + 3*A2 - 6*J3 + 2*C + 3/(4 la),
       J3 = int_0^inf sinc(pi la u)^3 sinc(pi u)^2 du,  C = int (Khat*Shat)^3 = 1 - la/2
  m4 = 1 + 6*A2 + D4 + A4 (D4 = int K^4; A4 = triple integral with det4) - computed by
       full diagram in m3_moment.py; here we give the k<=3 values that feed the LP.
"""
import mpmath as mp
from mpmath import sinc, mpf, quad, inf

mp.mp.dps = 30

def S(u): return mp.sinc(mp.pi * u)
def K(u, la): return mp.sinc(mp.pi * la * u)

def J2(la):
    return quad(lambda u: K(u, la)**2 * S(u)**2, [0, inf])

def J3(la):
    return quad(lambda u: K(u, la)**3 * S(u)**2, [0, inf])

def A2(la): return 1/la - 2*J2(la)

def Cint(la):
    # (Khat * Shat)(xi), Khat = (1/la)1_{|.|<=la/2}, Shat = 1_{|.|<=1/2}; C = int conv^3
    def conv(xi):
        lo = max(-la/2, xi - mpf(1)/2); hi = min(la/2, xi + mpf(1)/2)
        return max(mpf(0), hi - lo)/la
    return quad(lambda xi: conv(xi)**3, [-(1+la)/2, (1+la)/2])

def m2(la): return 1 + A2(la)
def m3(la): return 1 + 3*A2(la) - 6*J3(la) + 2*Cint(la) + mpf(3)/(4*la)

if __name__ == "__main__":
    print(f"{'lam':>8} {'m2':>14} {'A2':>12} {'m3':>14} {'2m2-m3':>14}")
    for s in ("0.5", "2/3", "1.0"):
        la = mp.mpf(s)
        m2v = m2(la); m3v = m3(la)
        print(f"{s:>8} {mp.nstr(m2v,12):>14} {mp.nstr(A2(la),12):>12} {mp.nstr(m3v,12):>14} {mp.nstr(2*m2v-m3v,12):>14}")
    # also rational check at lambda=1
    la = mpf(1)
    print("\nlambda=1 exact check: m2 = 4/3? ", mp.nstr(m2(la), 18), "  m3 = 125/64? ", mp.nstr(m3(la), 18))
