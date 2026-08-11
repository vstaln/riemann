#!/usr/bin/env python3
"""Multi-window certificate, SCALE-FREE analysis (pair-density form).

Certificate value per zero (interior reading, Prop 4.4(ii) analog):
    cert = 4 - 2 - R  =  2 - R,   R = ||bA||_F^2 / tr bA.

For a single window with evaluation profile u (|s|<=1/2), pair profile v = u^2,
sampling kernel c(r) = b(v)(r) := int v(x) e^{-2 pi i r x} dx,  a = int v:
    R = 1 + (1/a^2) * I(c),   I(c) := int c(r)^2 (1 - sinc(pi r)^2) dr.

Joint system of m windows (all sharing the grid, read jointly):
    R_joint = 1 + (1/(m^2 a^2)) * I(sum_alpha c_alpha),   I(g) := int g(r)^2 (1-sinc(pi r)^2) dr.

We test:  does R_joint < R_single for detuned / phase-shifted / orthogonal window sets?
(m = 1,2,4,8).  Verified normalization: flat window u=1 gives I(sinc^2) = 1/3, R = 4/3 (paper's (5.12) limit).

Conventions:
  - P (paper/Theorem D): evaluation profile u = sqrt(v), v = cos(w x)  (phi^2 has profile v).
  - Q (qi_sweep):         evaluation profile u = cos(w x) directly.
Both are legitimate windows (0<=phi<=1); they differ in the pair profile v.
"""
import numpy as np

PI = np.pi
SQRT2 = np.sqrt(2.0)

def sinc(t):
    out = np.ones_like(t, dtype=float)
    nz = np.abs(t) > 1e-9
    out[nz] = np.sin(t[nz]) / t[nz]
    return out

def bv_cos(w, r):
    """b(v)(r) for v(x)=cos(w x) on [-1/2,1/2]:  int cos(w x) e^{-2 pi i r x} dx.
    = (1/2)[ sinc((w-2pi r)/2) + sinc((w+2pi r)/2) ]   (sinc t = sin t / t)"""
    return 0.5 * (sinc((w - 2*PI*r)/2.0) + sinc((w + 2*PI*r)/2.0))

def bv_cos2(w, r):
    """b(v)(r) for v(x)=cos^2(w x) = (1+cos(2 w x))/2."""
    return 0.5 * bv_cos(0.0, r) + 0.5 * bv_cos(2.0*w, r)

def pair_integral(cfun, rgrid, wgt, a2=None):
    """I = int cfun(r)^2 * wgt(r) dr by trapezoid on rgrid.
    Split: I = int c^2 dr - int c^2 sinc(pi r)^2 dr = a2 - (fast-decaying part),
    where int c^2 dr = int v^2 = a2 by Parseval (c = b(v))."""
    c = cfun(rgrid)
    fast = np.trapezoid(c**2 * np.sinc(rgrid)**2, rgrid)
    if a2 is None:
        a2 = np.trapezoid(c**2, rgrid)
    return a2 - fast

def a2_profile(w, conv):
    """a2 = int v^2 where v = u^2 is the pair profile."""
    if conv == 'P':
        v = lambda x: np.cos(w*x)          # v = cos(w x)
    else:
        v = lambda x: np.cos(w*x)**2       # v = cos^2(w x)
    xs = np.linspace(-0.5, 0.5, 200001)
    return np.trapezoid(v(xs)**2, xs)

def R_single(w, conv, rgrid, wgt):
    """R = 1 + (1/a^2) I(c),  a = int v, v = u^2."""
    if conv == 'P':
        a = 2.0*np.sin(w/2.0)/w
        cfun = lambda r: bv_cos(w, r)
    else:
        a = 0.5*(1.0 + np.sin(w)/w)
        cfun = lambda r: bv_cos2(w, r)
    a2 = a2_profile(w, conv)
    I = pair_integral(cfun, rgrid, wgt, a2=a2)
    return 1.0 + I / a**2, a, I

def scaled_profiles(ws, conv, a_target):
    """Return c-functions c_alpha(r) = b(v_alpha)(r) with int v_alpha = a_target
    (scale each profile to a common mass), and the a2 = int v^2 matrix."""
    m = len(ws)
    cfuns, vA = [], []
    for w in ws:
        if conv == 'P':
            a_i = 2.0*np.sin(w/2.0)/w
            A = a_target / a_i
            cfun = lambda r, w=w, A=A: A * bv_cos(w, r)
            vfun = lambda x, w=w, A=A: A * np.cos(w*x)
        else:
            a_i = 0.5*(1.0 + np.sin(w)/w)
            A = a_target / a_i
            cfun = lambda r, w=w, A=A: A * bv_cos2(w, r)
            vfun = lambda x, w=w, A=A: A * np.cos(w*x)**2
        cfuns.append(cfun)
        vA.append(vfun)
    xs = np.linspace(-0.5, 0.5, 200001)
    a2ij = np.zeros((m, m))
    for i in range(m):
        for j in range(m):
            a2ij[i, j] = np.trapezoid(vA[i](xs) * vA[j](xs), xs)
    return cfuns, a2ij

def R_joint(ws, conv, rgrid, a_target=None):
    """R_joint = 1 + (1/(m^2 a^2)) I(sum_alpha c_alpha), windows scaled to common a."""
    m = len(ws)
    if a_target is None:
        a_target = (2.0*np.sin(SQRT2/2.0)/SQRT2) if conv == 'P' else 0.5*(1.0+np.sin(SQRT2)/SQRT2)
    cfuns, a2ij = scaled_profiles(ws, conv, a_target)
    S = np.zeros_like(rgrid)
    for f in cfuns:
        S += f(rgrid)
    a2sum = a2ij.sum()
    fast = np.trapezoid(S**2 * np.sinc(rgrid)**2, rgrid)
    I = a2sum - fast
    return 1.0 + I/(m*m*a_target*a_target)

def main():
    # integration grid: r in [-Rmax, Rmax], weight (1 - sinc(pi r)^2)
    Rmax = 400.0
    N = 400001
    rgrid = np.linspace(-Rmax, Rmax, N)
    wgt = 1.0 - np.sinc(rgrid)**2   # np.sinc(x) = sin(pi x)/(pi x): sinc(pi r) = np.sinc(r)

    print("=== calibration: single window ===")
    for conv in ('P', 'Q'):
        for w in (SQRT2,):
            R, a, I = R_single(w, conv, rgrid, wgt)
            print(f"  conv={conv} w={w:.4f}: R={R:.9f}  (c*1=0.7532960 -> 1/c=1.3274993)  a={a:.6f}")
    # flat window check
    R, a, I = R_single(1e-6, 'Q', rgrid, wgt)
    print(f"  flat (Q, w->0): R={R:.9f}  (expect 4/3 = 1.3333...)")
    # paper-convention flat: v = 1 (u=1) -> a=1, c=sinc(pi r)
    I = np.trapezoid(np.sinc(rgrid)**2 * wgt, rgrid)
    print(f"  flat paper-style: I = {I:.9f} (expect 1/3), R = {1+I:.9f} (expect 4/3)")

    print("\n=== window scan (single window R as function of w), conv P and Q ===")
    for conv in ('P', 'Q'):
        print(f"  conv {conv}:")
        for w in (0.5, 1.0, SQRT2, 1.8, 2.0, 2.5, 3.0):
            R, a, I = R_single(w, conv, rgrid, wgt)
            print(f"    w={w:.2f}: R={R:.6f}  cert=2-R={2-R:.6f}")

    print("\n=== JOINT systems (windows scaled to common a) ===")
    for conv in ('P', 'Q'):
        print(f"conv {conv}:")
        for label, ws in [
            ("identical x2  w=1.4142",             [SQRT2, SQRT2]),
            ("identical x4",                       [SQRT2]*4),
            ("cosine+flat x2",                     [SQRT2, 1e-9]),
            ("detuned x2  {1.4142, 2.0}",          [SQRT2, 2.0]),
            ("detuned x2  {1.4142, 2.5}",          [SQRT2, 2.5]),
            ("detuned x2  {1.4142, 3.0}",          [SQRT2, 3.0]),
            ("detuned x2  {1.0, 2.0}",             [1.0, 2.0]),
            ("detuned x4  {1.0,1.4142,2.0,2.5}",   [1.0, SQRT2, 2.0, 2.5]),
            ("detuned x8  {0.5,1.0,1.3,1.4142,1.8,2.2,2.6,3.0}", [0.5,1.0,1.3,SQRT2,1.8,2.2,2.6,3.0]),
        ]:
            Rj = R_joint(ws, conv, rgrid)
            print(f"    {label}: R_joint={Rj:.9f}  cert=2-R={2-Rj:.6f}   [single MT: R=1.327499, cert=0.672501]")

    print("\n=== SUM-PROFILE IDENTITY (the reason for NO-GAIN) ===")
    print("R_joint(m windows) must equal R_single(V/m), V = sum v_alpha (all scaled to common a):")
    for conv in ('P', 'Q'):
        for label, ws in [
            ("detuned x2 {1.4142,2.0}", [SQRT2, 2.0]),
            ("detuned x4 {1.0,1.4142,2.0,2.5}", [1.0, SQRT2, 2.0, 2.5]),
        ]:
            Rj = R_joint(ws, conv, rgrid)
            # single window with pair profile V/m:
            m = len(ws)
            a_t = 2.0*np.sin(SQRT2/2.0)/SQRT2 if conv == 'P' else 0.5*(1.0+np.sin(SQRT2)/SQRT2)
            cfuns, a2ij = scaled_profiles(ws, conv, a_t)
            S = np.zeros_like(rgrid)
            for f in cfuns:
                S += f(rgrid)
            S /= m          # b(V/m) = (1/m) b(V)
            a2V = a2ij.sum() / (m*m)
            fast = np.trapezoid(S**2 * np.sinc(rgrid)**2, rgrid)
            I_V = a2V - fast
            Rs = 1.0 + I_V / a_t**2
            print(f"    conv={conv} {label}: R_joint={Rj:.9f}  R_single(V/m)={Rs:.9f}  |diff|={abs(Rj-Rs):.2e}")

if __name__ == '__main__':
    main()
