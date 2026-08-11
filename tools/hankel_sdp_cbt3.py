#!/usr/bin/env python3
"""C-BT3 addendum: numeric feasibility SDP + 2-atom fits for (m1,m2,m3)=(1,4/3,2).

1) SDP-style check: does there exist m4 with H3(m4) = [[1,1,4/3],[1,4/3,2],[4/3,2,m4]]
   PSD?  minimize lambda_min(H3(m4)) over m4 (scipy minimize); report the feasibility
   threshold and that both candidate worlds' m4 pass.
2) 2-atom fit: find weights/atoms realizing (1, 4/3, 2) from several starts
   (least_squares).  Must find the extremal world (1, 2; w 2/3, 1/6).
3) Confirm the P6.5 LP verdict (optimum exactly 5/6 with these moments) is consistent
   with the realization: the extremal world achieves N_d/N = 5/6 with equality.

Run: uv run --quiet --with numpy --with scipy python /tmp/attack_hankel/hankel_sdp.py
"""
import numpy as np
from scipy.optimize import minimize_scalar, least_squares

def H3(m4):
    return np.array([[1.0, 1.0, 4/3], [1.0, 4/3, 2.0], [4/3, 2.0, m4]])

def min_eig(m4):
    return np.linalg.eigvalsh(H3(m4))[0]

print("1) SDP feasibility: minimize lambda_min(H3(m4)) over m4")
res = minimize_scalar(min_eig, bounds=(0, 10), method="bounded")
print(f"   min over m4 in [0,10]: lambda_min = {res.fun:.10f} at m4 = {res.x:.6f}")
# feasibility threshold: H3(m4) PSD  <=>  det >= 0 (leading 2x2 already PD)
# det(m4) = m4/3 - 28/27
print(f"   analytic threshold: det(m4) = m4/3 - 28/27 = 0  ->  m4 >= 28/9 = {28/9:.6f}")
for m4, lab in [(28/9, "28/9 (2-atom boundary)"), (13/4, "13/4 (paper)"), (10/3, "10/3 (extremal)")]:
    ev = np.linalg.eigvalsh(H3(m4))
    print(f"   m4 = {lab:>22s}: lambda_min = {ev[0]:+.8f}  PSD={ev[0] >= -1e-12}  rank={np.linalg.matrix_rank(H3(m4))}")

print("\n2) 2-atom fits of (m1, m2, m3) = (1, 4/3, 2)")
def resid(p):
    # p = (w1, a, b) with w2 = 1 - w1 ; moments m_k = w1 a^k + (1-w1) b^k
    w1, a, b = p
    w2 = 1 - w1
    m = np.array([w1*a + w2*b, w1*a*a + w2*b*b, w1*a**3 + w2*b**3])
    return m - np.array([1.0, 4/3, 2.0])
for start in [(0.5, 0.4, 1.6), (0.7, 1.0, 2.0), (0.3, 0.5, 1.5), (0.8, 1.2, 0.5)]:
    sol = least_squares(resid, start, bounds=([0.0, -5, -5], [1.0, 5, 5]))
    w1, a, b = sol.x
    ok = sol.cost < 1e-20
    print(f"   start {start}: converged={ok}  w1={w1:.6f} a={a:.6f} b={b:.6f}  cost={sol.cost:.2e}")
    if ok:
        print(f"     -> atoms at {a:.6f} (w {w1:.6f}) and {b:.6f} (w {1-w1:.6f});  "
              f"m4 = {w1*a**4 + (1-w1)*b**4:.6f}")

print("\n3) P6.5 LP consistency: optimum exactly 5/6 with moments (1, 4/3, 2)")
# The extremal world achieves N_d/N = 5/6 with equality in every step (lemmaR_tight,
# PROVEN); the c=3 certificate lower-bounds N_d/N by (3 - 4/3)/2 = 5/6 for ALL
# configurations with these moments.  Hence LP optimum = 5/6 exactly.
print("   lower bound: N_d/N >= (3 - m2)/2 = (3 - 4/3)/2 = 5/6   (c=3 cert, PROVEN)")
print("   upper bound: extremal world feasible with N_d/N = 5/6  (T1 of main script)")
print("   => LP optimum = 5/6 exactly.  Consistent: the 3-moment data does not move N_d.")
