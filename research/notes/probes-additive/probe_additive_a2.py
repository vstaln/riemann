#!/usr/bin/env python3
"""Probe A2: what does the 4th moment do to min N_d?

- achievable range of m4 over integer-multiplicity multisets with (m1,m2,m3) = (1,4/3,2)
- min N_d under (m1,m2,m3) with m4 <= 13/4  (the GUE value as an upper bound)
- min N_d under (m1,m2,m3) with m4 <= M for a sweep of M (incl. crystal's 10/3)
"""
import numpy as np
from scipy.optimize import linprog

K = 60

def solve(c, A_ub=None, b_ub=None, A_eq=None, b_eq=None):
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq,
                  bounds=[(0, None)] * K, method="highs")
    if not res.success:
        raise RuntimeError(res.message)
    return res.fun, res.x

mom1 = np.array([1.0, 4.0/3, 2.0])
A_eq = np.array([[k**r for k in range(1, K+1)] for r in range(1, 4)], dtype=float)

# max m4 and min m4 subject to (m1,m2,m3)
f, _ = solve([-(k**4) for k in range(1, K+1)], A_eq=A_eq, b_eq=mom1)
g, _ = solve([k**4 for k in range(1, K+1)], A_eq=A_eq, b_eq=mom1)
print(f"m4 range over (m1,m2,m3)=(1,4/3,2), integer-support multisets (real LP, K={K}):")
print(f"  min m4 = {g:.6f}   max m4 = {-f:.6f}   (GUE 13/4 = 3.25; crystal 10/3 = {10/3:.6f})")

# min N_d under (m1,m2,m3) + m4 <= M, for several M
print("\nmin N_d under (m1,m2,m3) and m4 <= M:")
c_Nd = [(k - 1.0) for k in range(1, K+1)]   # minimize N_d = sum n_k ; N_d = 1 + sum(k-1)n_k... use sum n_k directly
# N_d = sum n_k ; with N=1: minimize sum n_k subject to moments
for M in (13.0/4, 3.30, 10.0/3, 3.5, 4.0, 6.0, None):
    A_ub = None; b_ub = None
    if M is not None:
        A_ub = np.array([[k**4 for k in range(1, K+1)]], dtype=float)
        b_ub = np.array([M])
    try:
        f, _ = solve([1.0]*K, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=mom1)
        print(f"  M = {M if M is not None else 'inf'}: min N_d/N = {f:.6f}  (5/6 = {5/6:.6f})")
    except RuntimeError as e:
        print(f"  M = {M}: infeasible ({e})")

# with m4 >= M (lower-bound constraint), for the "reality has m4 >= 13/4" direction
print("\nmin N_d under (m1,m2,m3) and m4 >= M:")
for M in (13.0/4, 10.0/3):
    A_ub = np.array([[-k**4 for k in range(1, K+1)]], dtype=float)
    b_ub = np.array([-M])
    try:
        f, _ = solve([1.0]*K, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=mom1)
        print(f"  M = {M}: min N_d/N = {f:.6f}  (5/6 = {5/6:.6f})")
    except RuntimeError as e:
        print(f"  M = {M}: infeasible ({e})")
