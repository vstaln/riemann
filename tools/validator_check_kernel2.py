"""Verify attack-kernel claims with numpy (f64) — smooth kernel, large N is fine."""
import numpy as np

N = 4000
h = 1.0 / N
us = (np.arange(N) + 0.5) * h - 0.5
U, V = np.meshgrid(us, us, indexing='ij')
K = np.abs(U - V) * h
ev = np.linalg.eigvalsh(K)
print("discrete eigenvalues of T (N=%d):" % N)
print("  largest 3:  ", ev[-3:])
print("  smallest 3: ", ev[:3])
print("  min eigenvalue of I+T: %.6f" % (1 + ev[0]))
print("  max eigenvalue of I+T: %.6f" % (1 + ev[-1]))

import math
lo, hi = 2.0, 2.6
for _ in range(60):
    m = (lo + hi) / 2
    if (m / 2) * math.tanh(m / 2) > 1:
        hi = m
    else:
        lo = m
kpos = (lo + hi) / 2
print("analytic: k_pos=%.4f lam_max=2/k^2=%.5f" % (kpos, 2 / kpos ** 2))
lo, hi = math.pi, 2 * math.pi
for _ in range(80):
    m = (lo + hi) / 2
    if math.tan(m / 2) < -2 / m:
        hi = m
    else:
        lo = m
kneg = (lo + hi) / 2
print("analytic: k_neg=%.4f lam_min=-2/k^2=%.5f -> I+T min eig ~ %.5f" % (kneg, -2 / kneg ** 2, 1 - 2 / kneg ** 2))

# --- 2) v0 + A constant on grid ---
def A(u):
    return np.abs(u - us).dot(np.cos(np.sqrt(2) * us)) * h
vals = np.cos(np.sqrt(2) * us) + np.array([A(u) for u in us])
mid = vals[N // 2]
print("max |cos(sqrt2 u)+A(u) - const| over grid: %.2e" % np.max(np.abs(vals - mid)))
print("cos(1/sqrt2) = %.10f (boundary value, nonzero)" % np.cos(1 / np.sqrt(2)))

# --- 3) free-grid global minimizer of Q, no evenness: solve (I+T)v = mu*1, normalize int v = 1
M = np.eye(N) + K
b = np.ones(N)
sol = np.linalg.solve(M, b)
s = sol.sum() * h
sol /= s
Qv = sol.dot(M.dot(sol)) * h * h  # <v, M v> with two h's? careful: M includes h already for off-diag
# <v,Mv> = sum_i v_i ( (M v)_i ) h ; M_ii = 1 (no h), M_ij = |u_i - v_j| h
Mv = M.dot(sol)
Qv = np.dot(sol, Mv) * h
c = np.cos(np.sqrt(2) * us)
sc = c.sum() * h
c = c / sc
Qc = np.dot(c, M.dot(c)) * h
print("free-grid Q* (no evenness): %.12f ; Q(cos/int): %.12f ; diff %.2e" % (Qv, Qc, abs(Qv - Qc)))
print("asymmetry max |v(u)-v(-u)|: %.2e" % np.max(np.abs(sol - sol[::-1])))
print("analytic Q = 1/2 + (1/sqrt2) cot(1/sqrt2) = %.12f" % (0.5 + 1 / np.sqrt(2) * 1 / np.tan(1 / np.sqrt(2))))
# check the stationarity residual: M v = mu * 1 ?
mu = (M.dot(sol)).mean()
print("stationarity residual max |(I+T)v - mu*1|: %.2e (mu=%.10f)" % (np.max(np.abs(M.dot(sol) - mu)), mu))
