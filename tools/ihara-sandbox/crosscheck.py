"""Independent cross-check of the Ihara-sandbox Rust numbers: K4, Petersen, HS.
Uses hand-entered eigenvalues + the same kernel formulas, entirely separate code path.
"""
import numpy as np

SQRT2 = np.sqrt(2.0); FRAC = 1.0 / SQRT2; PI = np.pi

def psi(s):
    d1 = SQRT2 - 2.0*PI*s; d2 = SQRT2 + 2.0*PI*s
    t1 = np.sin(FRAC - PI*s)/d1; t2 = np.sin(FRAC + PI*s)/d2
    if abs(d1) < 1e-12: t1 = 0.5
    if abs(d2) < 1e-12: t2 = 0.5
    return t1 + t2

def psi2(s):
    ps = PI*s
    t1 = 0.5 if abs(ps) < 1e-12 else np.sin(ps)/(2.0*ps)
    a = SQRT2 - ps; b = SQRT2 + ps
    t2 = 1.0 if abs(a) < 1e-12 else np.sin(a)/a
    t3 = 1.0 if abs(b) < 1e-12 else np.sin(b)/b
    return t1 + 0.25*(t2 + t3)

INT2 = 0.5 + np.sin(SQRT2)/(2.0*SQRT2)

def measure(name, nontriv, d):
    q = d - 1.0
    theta = np.array([np.arccos(l/(2.0*np.sqrt(q))) for l in nontriv])
    n = len(theta)
    s = theta * n / PI
    V = np.array([[psi(si - k) for k in range(n)] for si in s])
    W = V.T @ V / INT2
    tr = np.trace(W); hs2 = (W**2).sum()
    off_an = sum(psi2(s[i]-s[j])**2/INT2**2 for i in range(n) for j in range(n) if i != j)
    print(f"{name}: N={n} tr/N={tr/n:.6f} HS2/N={hs2/n:.6f} HS2_an/N={(n+off_an)/n:.6f} bound/N={(2*tr-hs2)/n:+.6f}")

# K4: d=3, q=2, nontriv = {-1,-1,-1}
measure("K4", [-1.0,-1.0,-1.0], 3)
# K5: d=4, q=3, nontriv = {-1 x4}
measure("K5", [-1.0]*4, 4)
# Petersen: d=3, q=2, {1 x5, -2 x4}
measure("Petersen", [1.0]*5 + [-2.0]*4, 3)
# CubeQ3: d=3, q=2, {1 x3, -1 x3}
measure("CubeQ3", [1.0]*3 + [-1.0]*3, 3)
# Clebsch: d=5, q=4, {1 x10, -3 x5}
measure("Clebsch", [1.0]*10 + [-3.0]*5, 5)
# Icosa: d=5, q=4, {sqrt5 x3, -1 x5, -sqrt5 x3}
s5 = np.sqrt(5.0)
measure("Icosa", [s5]*3 + [-1.0]*5 + [-s5]*3, 5)
# Q4: d=4, q=3, {2 x4, 0 x6, -2 x4}
measure("Q4", [2.0]*4 + [0.0]*6 + [-2.0]*4, 4)
# HS: d=7, q=6, {2 x28, -3 x21}
measure("Hoffman-Singleton", [2.0]*28 + [-3.0]*21, 7)
