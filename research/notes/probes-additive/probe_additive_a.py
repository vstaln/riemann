#!/usr/bin/env python3
"""Probe A (idea-generator-additive): crystal moment sequence vs GUE, and min-N_d LP
under (m1,m2), (m1,m2,m3), (m1,m2,m3,m4) constraints.

Extremal crystal (attack-multiplicity.md): multiplicity multiset = {1 x 2N/3, 2 x N/6}
(2/3 simple + 1/6 double on-line zeros, orthogonal atoms), so moments m_k = (2/3)*1^k + (1/6)*2^k.
GUE/paper moment sequence: m_k(1) = 1, 4/3, 2, 13/4 (paper Sec 7.5(f); attack-multiplicity.md).

min N_d over multiplicity multisets {m_j >= 1 ints, sum m_j = N} with given moment constraints:
  min N_d = N - max sum (k-1) n_k   s.t.  sum k^r n_k = m_r * N, r = 1..R,  n_k >= 0.
(The crystal is the N_d-minimizer under (m1,m2) only: N_d = 5N/6, PROVEN by the
inequality sum m_j(m_j-1) >= 2 sum (m_j-1), equality iff m_j in {1,2}.)
"""
import numpy as np
from scipy.optimize import linprog

def crystal_moments(K=6):
    return [(2.0/3)*1**k + (1.0/6)*2**k for k in range(1, K+1)]

def gue_moments():
    return [1.0, 4.0/3, 2.0, 13.0/4]   # paper values at lambda = 1

def min_Nd(moments, K=24):
    """min N_d = N - max obj, obj = sum (k-1) n_k, over n_k >= 0 (k=1..K), N=1 scale."""
    R = len(moments)
    c = [-(k - 1.0) for k in range(1, K + 1)]      # maximize -> minimize negative
    A_eq = np.array([[k**r for k in range(1, K + 1)] for r in range(1, R + 1)], dtype=float)
    b_eq = np.array(moments, dtype=float)
    res = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=[(0, None)] * K, method="highs")
    if not res.success:
        raise RuntimeError(res.message)
    return 1.0 + res.fun   # N_d = N - max_obj = 1 - (-res.fun)

print("Crystal moments m_k = (2/3) + (1/6)*2^k, k=1..6:")
print("  ", ["%.6f" % m for m in crystal_moments()])
print("GUE/paper moments at lambda=1:", ["%.6f" % m for m in gue_moments()])
print()
print("min N_d (fraction of N) under constraint sets:")
sets = {
    "(m1,m2)             ": gue_moments()[:2],
    "(m1,m2,m3=2)        ": gue_moments()[:3],
    "(m1,m2,m3,m4=13/4)  ": gue_moments()[:4],
}
for name, mom in sets.items():
    v = min_Nd(mom)
    print(f"  {name}: N_d/N = {v:.10f}   (5/6 = {5/6:.10f}, delta vs 5/6 = {v - 5/6:+.6f})")

# sanity: crystal is feasible for (m1,m2) and (m1,m2,m3) with N_d = 5/6; NOT for m4=13/4
cryst = crystal_moments()
print()
print("Crystal's own moments: m3 =", cryst[2], " vs GUE 2 ;  m4 =", cryst[3],
      " vs GUE 13/4 =", gue_moments()[3])
print("Crystal satisfies (m1,m2,m3):", all(abs(cryst[i]-gue_moments()[i]) < 1e-12 for i in range(3)))
print("Crystal satisfies (m1,m2,m3,m4):", all(abs(cryst[i]-gue_moments()[i]) < 1e-12 for i in range(4)))
