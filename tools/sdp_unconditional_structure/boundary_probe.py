#!/usr/bin/env python3
"""Boundary probe: small LP for the unconditional Tsang strip-positive cone.

Reduced problem (research/notes/sdp-unconditional-structure-2026-08-14.md sec 6-8):

  Variables: j_k = j(alpha_k), alpha in {0, 1/4, 1/2, 3/4, 1}, j(0)=1 pinned.
  j is interpolated piecewise-linearly (hat basis phi_k), so j >= 0  <=>  all j_k >= 0.

  Objective (homogeneous ratio, BGSTB (7.2)):
      R(j) = [ j(0) + 2 int_0^1 a j(a) sech(a) da ] / [ 2 int_0^1 j(a) sech(a) da ]
      simple fraction >= 2 - R ;  Sigma_rho (m_rho-1)/N(T) <= R - 1.

  Constraints (strip positivity, the unconditional cone):
      Re K_j(x+iy) >= 0 for all x, |y| <= b0 = 1,
      Re K_j(x+iy) = (1/pi) int_0^1 j(a) sech(a) cosh(a y) cos(a x) da.

  All integrals are computed exactly for the piecewise-linear j via a fine alpha-grid
  (hat-function coefficients c_k = (1/pi) int phi_k(a) sech(a) cosh(ay) cos(ax) da).
  Solved as a Charnes-Cooper linear-fractional LP: min t + sum cobj_k y_k
  s.t. d0*t + sum d_k y_k = 1,  c0*t + sum c_k y_k >= 0,  y_k >= 0.

Runtime < 1 min (single HiGHS linprog, ~15k rows x 5 cols). numpy/scipy via uv.
"""
import numpy as np
from scipy.optimize import linprog

# ---------------- fine alpha-grid for exact-ish integrals ----------------
NA = 4001
ag = np.linspace(0.0, 1.0, NA)
agw = np.ones(NA) * (1.0 / (NA - 1))
agw[0] = agw[-1] = 0.5 / (NA - 1)          # trapezoid
sech = 1.0 / np.cosh(ag)

# ---------------- hat basis on the 5 nodes ----------------
alpha = np.array([0.0, 0.25, 0.5, 0.75, 1.0])
h = 0.25
K = 4                                      # free vars k=1..4 ; j_0 = 1
phi = np.zeros((5, NA))
for k in range(5):
    if k == 0:
        phi[k] = np.clip(1.0 - ag / h, 0.0, None)
    elif k == 4:
        phi[k] = np.clip((ag - alpha[3]) / h, 0.0, None)
    else:
        phi[k] = np.clip(1.0 - np.abs(ag - alpha[k]) / h, 0.0, None)

# denominator d_k = 2 int phi_k sech ; numerator weight cobj_k = 2 int a phi_k sech
d_full = 2.0 * (agw * sech) @ phi.T          # shape (5,)
cobj_full = 2.0 * (agw * ag * sech) @ phi.T  # shape (5,)
d0, d_free = d_full[0], d_full[1:]
cobj = cobj_full[1:]

# ---------------- strip sample grid ----------------
XMAX = 40.0
NX = 801
x_grid = np.linspace(0.0, XMAX, NX)
y_grid = np.array([0.0, 0.25, 0.5, 0.75, 1.0])

b0 = 1.0

rows = []
for y in y_grid:
    cosh_y = np.cosh(ag * y)
    for x in x_grid:
        ck = (1.0 / np.pi) * (agw * sech * cosh_y * np.cos(ag * x)) @ phi.T
        c0, cf = ck[0], ck[1:]
        rows.append(np.concatenate(([-c0], -cf)))
A_ub = np.array(rows)
b_ub = np.zeros(len(rows))

A_eq = np.concatenate(([d0], d_free))[None, :]
b_eq = np.array([1.0])

# Charnes-Cooper: numerator = (1 + C0)*t + sum_{k>=1} cobj_k y_k,  with y_0 = t*j_0 = t.
c = np.concatenate(([1.0 + cobj_full[0]], cobj))

bounds = [(0.0, None)] * (K + 1)

res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq,
              bounds=bounds, method="highs")

assert res.success, res.message
t = res.x[0]
y = res.x[1:]
j = y / t

R_min = res.fun
simple = 2.0 - R_min
mult_sum = R_min - 1.0

print("=== boundary probe: Tsang strip-positive cone, b0 =", b0, "===")
print("linprog status:", res.message)
print("nodes alpha           =", np.array2string(alpha, precision=4))
print("recovered j (j0..j4)  =", np.array2string(np.concatenate(([1.0], j)), precision=6))
print("Charnes-Cooper t      =", t)
print()
print("R_min   = ratio (j(0)+2A)/(2J)      = %.8f" % R_min)
print("simple fraction >= 2 - R_min        = %.8f" % simple)
print("Sigma(m_rho-1)/N(T) <= R_min - 1   = %.8f" % mult_sum)

# ---------------- Fejer reference (same hat basis) ----------------
j_F = np.array([1.0, 0.75, 0.5, 0.25, 0.0])       # (1-a)_+
den_F = d_full @ j_F
num_F = 1.0 + cobj_full @ j_F
R_F = num_F / den_F
print()
print("Fejer j=(1-a)+ reference: R = %.6f  simple = %.6f" % (R_F, 2.0 - R_F))

# ---------------- post-check: strip positivity on a finer/wider grid ----------------
fine_x = np.linspace(0.0, 120.0, 12001)
fine_y = np.linspace(0.0, b0, 9)
jfull = np.concatenate(([1.0], j))
jinterp = jfull @ phi          # (NA,)
cosx = np.cos(ag[:, None] * fine_x[None, :])   # (NA, NX)
min_re = np.inf
for yy in fine_y:
    ch = np.cosh(ag * yy)
    vgrid = (1.0 / np.pi) * ((agw * jinterp * sech * ch) @ cosx)
    min_re = min(min_re, float(vgrid.min()))
print("post-check min Re K_j on fine grid (y in [0,1], x in [0,120]) = %.6e" % min_re)

# ---------------- self-checks ----------------
assert R_min <= R_F + 1e-9, "LP must match or beat the Fejer feasible point"
assert min_re >= -1e-6, "recovered j must be strip-positive on the fine grid"
assert 0.5 < simple < 0.6818, "boundary must sit below the 0.6818 wall"
assert np.all(j >= -1e-12), "j must be nonnegative"
print("PASS")
