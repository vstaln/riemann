#!/usr/bin/env python3
"""LP: can the third moment move the distinct bound N_d beyond 5/6?

Formulation follows the paper Sec 7.5(g) template: find weight
  psi(m) = a*m + b*m^2 + c*m^3 + d*1_{m=1}   with  psi(m) <= 1 for all integer m>=1
maximizing the per-N bound
  B = a*M1 + b*M2 + c*M3 + d*(s1/N)
where (M1,M2,M3) are the normalized Gram-matrix moments at a window and s1/N >= 2/3
is the unconditional simple-count bound (Theorem B). Then N_d >= B*N, PROVIDED the
Schur-Horn / admissibility step for the cubic holds (we report B as the unconstrained
LP optimum = upper bound on any achievable bound; admissibility is discussed separately).

Moment inputs (CORRECTED, diagonal method):
  window lam=1:    M=(1, 4/3, 2)          [paper; verified]
  window lam=1/2:  M=(1, 13/6, 5)         [corrected; task's asserted m3=2 is wrong]
  window lam=2/3:  M=(1, 31/18, 13/4)     [corrected]
  joint (A: 1,4/3)+(B: m3=5): M=(1, 4/3, 5) [formal; Schur-Horn validity unknown]
Also runs the task's asserted input m3(1/2)=2 for the record.
"""
import numpy as np
from scipy.optimize import linprog

def solve(M1, M2, M3, S1, Mmax=40, label=""):
    # maximize a*M1 + b*M2 + c*M3 + d*S1  s.t. psi(m) <= 1
    # linprog minimizes; negate objective
    c_obj = -np.array([M1, M2, M3, S1])
    A = []
    bub = []
    for m in range(1, Mmax + 1):
        row = [m, m*m, m**3, 1.0 if m == 1 else 0.0]
        A.append(row); bub.append(1.0)
    res = linprog(c_obj, A_ub=np.array(A), b_ub=np.array(bub),
                  bounds=[(None, None)]*4, method="highs")
    if not res.success:
        print(f"{label}: LP FAILED: {res.message}")
        return None
    a, b, c, d = res.x
    B = a*M1 + b*M2 + c*M3 + d*S1
    # sanity: check psi(m) <= 1 over a wider range
    viol = max(((a*m + b*m*m + c*m**3 + (d if m == 1 else 0.0)) for m in range(1, 200)), key=lambda v: v)
    print(f"{label:>52s}: B={B:.6f}  (a={a:+.4f} b={b:+.4f} c={c:+.4f} d={d:+.4f})  max_psi(1..199)={viol:.6f}")
    return B

S1 = 2/3
print("Unconstrained cubic-weight LP optima (upper bounds on achievable N_d/N):")
print("5/6 = 0.833333  (target to beat)\n")
solve(1, 4/3,   2,    S1, label="lam=1   (1,4/3,2)     paper moments")
solve(1, 13/6,  5,    S1, label="lam=1/2 (1,13/6,5)    corrected")
solve(1, 13/6,  2,    S1, label="lam=1/2 (1,13/6,2)    task-asserted m3=2")
solve(1, 31/18, 13/4, S1, label="lam=2/3 (1,31/18,13/4) corrected")
solve(1, 4/3,   5,    S1, label="joint   (1,4/3,5)     A two-moments + B third (formal)")
