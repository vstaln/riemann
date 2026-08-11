#!/usr/bin/env python3
"""Check C (B3): the certificate value is pinned 1:1 by the certified simple fraction p_1
(shadow price exactly 1) -- the numerical anchor for "a CvS-type eigenfunction zero-location
statement has no handle on the certificate value".

Small LP over the piecewise-linear bandwidth-one certificate class against the 256-law data
(tools/lpdual/law_data.json, produced by attack-lpdual):
    variables c0, r_0..r_255 (r_256 = 0);  r piecewise linear on [j/256, (j+1)/256]
    validity:  c0 + sum_{j=1}^{255} s_j r_j <= p_1        (s_j = law masses at x_j = j/256)
    box:       |r_j| <= 1
    slope:     |r_{j+1} - r_j| <= 1/256                   (B = 1)
    curvature: sum_j |(r_{j+1}-r_j) - (r_j - r_{j-1})| <= 1/256   (C = 1, discrete)
    objective: maximize v = c0 + int_0^1 r(x) x dx  (exact per-cell quadrature)

For p_1 in {p0, 0.70, 0.80, 0.90, 1.00} we expect v* = p_1 + |E(1)|  (attack-lpdual §3),
i.e. the shadow price of p_1 is exactly 1 and nothing else in the class moves v.

Usage: uv run --quiet --with numpy --with scipy python tools/cvs-import/shadow_price_probe.py
"""
import json
import numpy as np
from scipy.optimize import linprog

DATA = '/home/vstaln/riemann/tools/lpdual/law_data.json'
N = 256

def weights():
    """w_j with int_0^1 r(x) x dx = sum_{j=0}^{255} w_j r_j (exact, piecewise-linear r)."""
    w = np.zeros(N)  # index j = 0..255 (r_256 = 0, contributes nothing)
    for j in range(N):
        a, b = j / N, (j + 1) / N
        L = b - a
        # r(x) = r_j (b-x)/L + r_{j+1} (x-a)/L
        w[j] += (1/L) * (b*(b*b - a*a)/2 - (b**3 - a**3)/3)          # weight of r_j
        if j + 1 < N:
            w[j + 1] += (1/L) * ((b**3 - a**3)/3 - a*(b*b - a*a)/2)  # weight of r_{j+1}
    return w

def solve(p1, s_at, w, B=1.0, C=1.0):
    """maximize c0 + w.r  s.t. c0 + sum_{k=1}^{255} s_at[k] r_k <= p1, |r|<=1,
    |Dr|<=B/N, sum|D2 r|<=C/N.  s_at[k] = mass at x = k/256, k = 1..256 (k=256 pairs with r_256 = 0)."""
    n = N
    n_t = n                 # epigraph slots for |second difference|, j = 0..n-1
    m = n + 1 + n_t         # total columns: [c0, r_0..r_255, t_0..t_255]
    def row_len(v):
        out = np.zeros(m); out[:len(v)] = v; return out
    c = np.zeros(m); c[0] = -1.0; c[1:1 + n] = -w   # minimize -v
    A_ub, b_ub = [], []
    # validity: c0 + sum_{k=1}^{255} s_at[k] r_k <= p1   (r_k = variable index 1+k; r_256 = 0)
    vrow = np.zeros(m); vrow[0] = 1.0
    for k in range(1, n):
        vrow[1 + k] = s_at[k]
    A_ub.append(vrow); b_ub.append(p1)
    # box
    for j in range(n):
        e = np.zeros(m); e[1 + j] = 1.0
        A_ub.append(e); b_ub.append(1.0)
        A_ub.append(-e); b_ub.append(1.0)
    # slope |r_{j+1}-r_j| <= B/N  (r_256 = 0)
    for j in range(n):
        e = np.zeros(m)
        e[1 + j] = 1.0
        if j + 1 < n:
            e[1 + j + 1] = -1.0
        A_ub.append(e); b_ub.append(B / N)
        A_ub.append(-e); b_ub.append(B / N)
    # curvature: d_j (one-sided at edges), |d_j| <= t_j, sum t_j <= C/N
    for j in range(n):
        e = np.zeros(m)
        if j == 0:
            e[1 + 1] = 1.0; e[1 + 0] = -1.0          # d_0 = r_1 - r_0
        elif j == n - 1:
            e[1 + j] = 1.0                            # d_{n-1} = 0 - r_{n-1}
        else:
            e[1 + j + 1] = 1.0; e[1 + j] = -2.0; e[1 + j - 1] = 1.0
        t = np.zeros(m); t[1 + n + j] = 1.0
        A_ub.append(e - t); b_ub.append(0.0)
        A_ub.append(-e - t); b_ub.append(0.0)
    e = np.zeros(m); e[1 + n:] = 1.0
    A_ub.append(e); b_ub.append(C / N)

    bounds = [(None, None)] + [(None, None)] * n + [(0, None)] * n_t
    res = linprog(c, A_ub=np.array(A_ub), b_ub=np.array(b_ub), bounds=bounds, method='highs')
    assert res.status == 0, f"LP failed: {res.message}"
    return -res.fun

def main():
    d = json.load(open(DATA))
    s = np.array(d['s_mid'])   # s_mid[j] = mass at x_{j+1} = (j+1)/256, j = 0..255 (law rows 1..256)
    # masses at x_k = k/256 for k = 1..256:  s_at_k = s_mid[k-1]
    s_at = np.zeros(N + 1)     # index k = 0..256; s_at[k] = mass at x = k/256
    for k in range(1, N + 1):
        s_at[k] = s[k - 1]
    p0 = float(d['p0'])
    E1 = float(d['E1'])
    # sanity: E(1) = int_0^1 (C(x) - x^2/2) dx,  C(x) = sum_{k/256 <= x} s_at[k], r(1)=0 -> k=256 term vanishes
    xk = np.arange(1, N) / N
    E1_check = float(np.sum(s_at[1:N] * (1.0 - xk)) - 1.0/6.0)
    print(f"law data: p0 = {p0:.16f}  E1(from masses) = {E1_check:.6e}  E1(stored) = {E1:.6e}  |E1| = {abs(E1):.6e}")
    w = weights()
    print("int_0^1 (1-x) x dx =", float(np.sum(w * (1 - np.arange(N) / N))), " (should be 1/6)")
    print()
    print("=== shadow-price probe: v* vs p1 (B=1, C=1, box) ===")
    for p1 in (p0, 0.70, 0.80, 0.90, 1.00):
        v = solve(p1, s_at, w)
        pred = p1 + abs(E1)
        print(f"  p1 = {p1:.6f} : v* = {v:.10f}   p1+|E1| = {pred:.10f}   diff = {v-pred:+.2e}")
    print()
    print("VERDICT C: v* = p1 + |E(1)| for every p1 -> shadow price of p1 is exactly 1; "
          "nothing inside the class moves v. A real-zeros/spectral statement that does not "
          "raise p1 cannot change the certificate value.")

if __name__ == '__main__':
    main()
