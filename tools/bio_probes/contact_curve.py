#!/usr/bin/env python3
"""B1.2 (biology note): contact-order shape prior on the F=1 support curve.

Data (paper Remark 1.1 / [CD-V5]): reaching certified simple fraction
0.70 / 0.80 / 0.90 by the two-moment route requires form-factor information on
supports A = 1.04 / 1.26 / 1.70  (F == 1 on [0, A]).

Folding prior: the curve v(A) should be monotone, concave (diminishing returns
per unit bandwidth), saturating at 1, and its value at A=1 should be consistent
with the known in-class constants (0.6725 two-moment cosine; 0.6818 class
optimum).

Run:  uv run --quiet python contact_curve.py
"""
import numpy as np

A = np.array([1.04, 1.26, 1.70], dtype=float)
v = np.array([0.70, 0.80, 0.90], dtype=float)

print("=== B1.2 contact-order / bandwidth curve ===")
print("data (A, v):", list(zip(A, v)))
slopes = np.diff(v) / np.diff(A)
print(f"incremental slopes: {slopes[0]:.4f}, {slopes[1]:.4f}  "
      f"-> decreasing? {slopes[0] > slopes[1]}  (concave prior: yes if decreasing)")
print(f"monotone increasing: {bool(np.all(np.diff(v) > 0))}")

# --- saturating model v = 1 - c * A^{-a}  (fit a, c by least squares) ---
# 1 - v = c * A^{-a}  ->  log(1-v) = log c - a log A
y = np.log(1 - v)
X = np.column_stack([np.ones(3), -np.log(A)])
coef, res, *_ = np.linalg.lstsq(X, y, rcond=None)
c, a = np.exp(coef[0]), coef[1]
vfit = 1 - c * A ** (-a)
print(f"\nsaturating fit v = 1 - {c:.4f}*A^(-{a:.4f}):")
print(f"  fit residuals: {np.max(np.abs(vfit - v)):.6f}")
print(f"  implied v(1)      = {1 - c:.4f}   (two-moment bandwidth-1: 0.6725/0.6818)")
print(f"  implied v(2)      = {1 - c * 2**(-a):.4f}")
print(f"  implied v(4)      = {1 - c * 4**(-a):.4f}")
print(f"  A needed for 0.99 = {(c / 0.01) ** (1 / a):.2f}")

# --- log model v = b*log(A) + c0 ---
X2 = np.column_stack([np.ones(3), np.log(A)])
coef2, *_ = np.linalg.lstsq(X2, v, rcond=None)
b, c0 = coef2[1], coef2[0]
vfit2 = b * np.log(A) + c0
print(f"\nlog fit v = {b:.4f}*log(A) + {c0:.4f}:  max res {np.max(np.abs(vfit2 - v)):.6f}")
print(f"  implied v(1) = {c0:.4f}  ;  v(4) = {b * np.log(4) + c0:.4f}")
print(f"  (log model is NOT saturating -> violates the prior at large A)")

# --- piecewise-linear back-extrapolation of the first two points ---
v1_extrap = v[0] - slopes[0] * (A[0] - 1.0)
print(f"\nlinear back-extrapolation of first segment to A=1: v(1) ~ {v1_extrap:.4f}")
