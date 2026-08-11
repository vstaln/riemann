"""Quick exploratory check: why is diag2/N ~ 1.13 for real zeros but ~1.0 for lattice?
vvt[r][r] = sum_{k=0}^{N-1} Psi(s_r - k)^2 should be ~ int Psi^2 = 0.8492 by Poisson summation.
Measure the actual distribution of x_r = vvt[r][r]/int_psi2 over the zeros.
"""
import numpy as np

SQRT2 = np.sqrt(2.0)
FRAC_1_SQRT2 = 1.0 / SQRT2
PI = np.pi

def psi(s):
    # closed form of int_{-1/2}^{1/2} cos(sqrt2 u) e^{-2 pi i s u} du (real for real s)
    s = np.asarray(s, dtype=np.float64)
    d1 = SQRT2 - 2.0 * PI * s
    d2 = SQRT2 + 2.0 * PI * s
    t1 = np.sin(FRAC_1_SQRT2 - PI * s) / d1
    t2 = np.sin(FRAC_1_SQRT2 + PI * s) / d2
    # removable poles at 2 pi s = +-sqrt2 : limit = 1/2
    t1 = np.where(np.abs(d1) < 1e-12, 0.5, t1)
    t2 = np.where(np.abs(d2) < 1e-12, 0.5, t2)
    return t1 + t2

def psi2(s):
    s = np.asarray(s, dtype=np.float64)
    ps = PI * s
    t1 = np.where(np.abs(ps) < 1e-12, 0.5, np.sin(ps) / (2.0 * ps))
    a = SQRT2 - ps
    b = SQRT2 + ps
    t2 = np.where(np.abs(a) < 1e-12, 1.0, np.sin(a) / a)
    t3 = np.where(np.abs(b) < 1e-12, 1.0, np.sin(b) / b)
    return t1 + 0.25 * (t2 + t3)

INT_PSI2 = 0.5 + np.sin(SQRT2) / (2.0 * SQRT2)
print(f"int psi^2 (closed form) = {INT_PSI2:.15f}")

# sanity: full-Z sum vs closed form at a few s
for s in [0.37, 3.14, 7.7, 50.5, 120.3]:
    k = np.arange(-2000, 2001, dtype=np.float64)
    full = np.sum(psi(s - k) ** 2)
    print(f"  sum_{{-2000..2000}} psi({s}-k)^2 = {full:.9f}  (expect ~0.849228)")

# load zeros, window T=200
gams = []
for line in open("/home/vstaln/riemann/tools/data/zeros_1_1000.txt"):
    p = line.split()
    if len(p) >= 2:
        gams.append(float(p[1]))
gams = np.array(gams)
T = 200.0
gwin = gams[(gams >= T) & (gams < 2.0 * T)]
n = len(gwin)
s_rho = (gwin - T) * n / T
print(f"\nT={T} N={n}")

k = np.arange(n, dtype=np.float64)
x = np.array([np.sum(psi(s - k) ** 2) / INT_PSI2 for s in s_rho])
print(f"x_r = vvt[r][r]/int_psi2 : min={x.min():.6f} max={x.max():.6f} mean={x.mean():.6f} var={x.var():.6f}")
print(f"diag2/N = mean(x^2)      = {(x**2).mean():.6f}   (finitet reports ~1.113 for T=200)")

# where is the variance coming from? look at x_r vs s mod 1
mod1 = s_rho % 1.0
print("\nx_r vs s mod 1 (first 12):")
for i in range(12):
    print(f"  s={s_rho[i]:8.4f}  s mod 1={mod1[i]:.4f}  x={x[i]:.6f}")

# truncated full-Z sum error: compare finite-grid vs full
kfull = np.arange(-2000, 2001, dtype=np.float64)
for s in [s_rho[0], s_rho[5], s_rho[60], s_rho[120]]:
    full = np.sum(psi(s - kfull) ** 2)
    grid = np.sum(psi(s - np.arange(n, dtype=np.float64)) ** 2)
    print(f"  s={s:8.4f} fullZ={full:.6f} grid0..N-1={grid:.6f}  x={grid/INT_PSI2:.6f}")
