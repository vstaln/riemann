#!/usr/bin/env python3
"""
LP dual of the near-CUE 256-law certificate — C^1 certificate class.
Certificate: r(x) = a0 + int_0^x g, g piecewise-linear with knots at j/256, g continuous.
  => r in C^2, r'(1) = g_256, r'' = g' piecewise-constant, int_0^1 |r''| = sum_j |Delta g_j|.
  r(1) = 0 is built in (a0 = -int_0^1 g).
Variables: c0, g_0..g_256, t_0..t_255 (epigraph for |Delta g|).
Objective: max v = c0 + int_0^1 r(x) x dx.
Constraints: validity c0 + sum_{j=1..M} s_j r(j/256) <= p0  (M rows of the law)
            |g_256| <= B, sum t_j <= C, t_j >= +-(g_{j+1}-g_j)
            box |r| <= 1 at knots and cell 1/4,1/2,3/4 points (window-kernel realism; optional)
Ceiling theorem (Stability.lean, signed): v <= p0 + M0*(|r'(1)| + int|r''|), M0=2.5431316e-6.
"""
import json, numpy as np
from scipy.optimize import linprog

d = json.load(open('law_data.json'))
s = np.array(d['s_mid']); p0 = d['p0']; N = 256; h = 1/N
M0 = 2.5431315104166665e-6

# --- build matrices ---
# w = trapezoid weights for int_0^1 g ; a0 = - w.g ; r_j = a0 + (W g)_j
w = np.full(N+1, h); w[0] = h/2; w[N] = h/2
W = np.zeros((N+1, N+1))
for j in range(1, N+1):            # int_0^{x_j} g, x_j = j/N
    W[j,0] = h/2
    for k in range(1, j):
        W[j,k] = h
    W[j,j] = h/2                   # W[0,:] = 0
R = -np.outer(np.ones(N+1), w) + W          # r = R g ; r(1)=0 by construction
# integral coeffs I: int r x dx = sum_j I_j r_j
def integral_coeffs(N):
    h = 1/N; I = np.zeros(N+1); I[0] = h*h/6
    for j in range(1, N): I[j] = j*h*h
    I[N] = (N-1)/2*h*h + h*h/3
    return I
I = integral_coeffs(N)
iG = I @ R          # int = iG.g
sG = s @ R[1:N+1,:] # rowsum over j=1..255 (= full rows since r_256=0)  [size N]
assert abs((R@np.zeros(N+1)).sum()) < 1e-20

def build(M, B, C, box=True, p1=None, s_use=None, Nrows=None):
    """M = number of law rows used in validity (rows 1..M). s_use/Nrows for extended-grid probes."""
    if s_use is None: s_use = s; Nrows = N
    if p1 is None: p1 = p0
    nG = Nrows+1
    # variables: c0, g_0..g_{Nrows}, t_0..t_{Nrows-1}
    n = 1 + nG + Nrows
    c = np.zeros(n); c[0] = 1; c[1:1+N+1] = iG   # objective: c0 + int_0^1 r(x) x dx
    # iG for the extended grid: recompute R', I' on Nrows grid? For probe we use the 256 grid with s_use extended.
    # Keep 256-grid geometry; s_use over rows 1..256.
    if Nrows != N: raise ValueError("extended grids need their own geometry; use probe fn")
    A_ub, b_ub = [], []
    # validity on rows 1..M: c0 + sum_{j=1..M} s_j r_j <= p1 ;  r_j = (R g)_j
    sG_M = (s_use[:M] @ R[1:M+1,:]) if M > 0 else np.zeros(N+1)
    a = np.zeros(n); a[0] = 1; a[1:1+N+1] = sG_M
    A_ub.append(a); b_ub.append(p1)
    # slope |g_256| <= B
    a = np.zeros(n); a[1+256] = 1; A_ub.append(a); b_ub.append(B)
    a = np.zeros(n); a[1+256] = -1; A_ub.append(a); b_ub.append(B)
    # epigraph: t_j >= +(g_{j+1}-g_j), >= -(g_{j+1}-g_j); sum t <= C
    for j in range(N):
        a = np.zeros(n); a[1+j] = -1; a[1+j+1] = 1; a[1+N+1+j] = -1; A_ub.append(a); b_ub.append(0.0)   # g_{j+1}-g_j - t_j <= 0
        a = np.zeros(n); a[1+j] = 1; a[1+j+1] = -1; a[1+N+1+j] = -1; A_ub.append(a); b_ub.append(0.0)
    a = np.zeros(n); a[1+N+1:1+N+1+N] = 1; A_ub.append(a); b_ub.append(C)
    # box on r: knots + quarter points
    if box:
        for xq in [0.0, 0.25, 0.5, 0.75]:
            pts = []
            for j in range(N):
                t = xq  # point at (j+xq)/N on cell j
                # r at (j+t)/N = r_j + h*(g_j t + (g_{j+1}-g_j) t^2/2)
                # r_j = (R g)_j ; coefficient of g_k in r_j is R[j,k]
                row = np.zeros(1+N)
                row += R[j,:]                    # r_j part
                row[j]   += h*(t - t*t/2)        # g_j part
                row[j+1] += h*t*t/2              # g_{j+1} part
                if j == N-1 and xq == 0.0: continue  # endpoint already covered
                pts.append(row)
            # also x=1 point
            for row in pts:
                a = np.zeros(n); a[1:1+N+1] = row; A_ub.append(a); b_ub.append(1.0)
                a = np.zeros(n); a[1:1+N+1] = -row; A_ub.append(a); b_ub.append(1.0)
    A_ub = np.array(A_ub); b_ub = np.array(b_ub)
    res = linprog(-c, A_ub=A_ub, b_ub=b_ub, bounds=[(None,None)]*n, method='highs')
    return res

def val(res):
    if not res.success: return None
    c0 = res.x[0]; g = res.x[1:1+N+1]; t = res.x[1+N:]
    v = c0 + (iG@g)
    return v

print("== LP-A': C^1 class, full validity (M=255), no box. Ceiling predicts v* = p0 + M0*(B+C) ==")
print(f"p0 = {p0:.12f}")
for (B, C) in [(0,0),(0,1),(1,0),(1,1),(2,1),(1,2),(4,2)]:
    res = build(255, B, C, box=False)
    v = val(res)
    pred = p0 + M0*(B+C)
    print(f"  B={B} C={C}: v* = {v:.12f}   predicted {pred:.12f}   gap = {v-pred:+.2e}   ok={abs(v-pred)<1e-9}")
