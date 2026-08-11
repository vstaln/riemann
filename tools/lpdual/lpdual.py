#!/usr/bin/env python3
"""
LP dual of the near-CUE 256-law certificate.
Certificate space: (c0, r), r piecewise-linear on [0,1], breakpoints j/256.
  value  v = c0 + int_0^1 r(x) x dx
  valid against law rows 1..M:  c0 + sum_{i=1..M} s_i r(i/256) <= p0
  edge: r(1)=0 (kills |r(1)|*|D(1)| term), slope |r'(1)| <= B, box |r|<=1.
Ceiling (Stability.lean): v <= p0 + 2.5431316e-6*(|r'(1)| + int|r''|), signed form.
"""
import json, numpy as np
from scipy.optimize import linprog

d = json.load(open('law_data.json'))
s = np.array(d['s_mid'])           # s_j, j=1..256 (index j-1)
p0 = d['p0']
N = 256
h = 1/N
E1 = d['E1']

# integral coefficients: int_0^1 r(x) x dx = sum_j I_j r_j,  r_j = r(j/256), j=0..256
def integral_coeffs(N):
    h = 1/N
    I = np.zeros(N+1)
    I[0] = h*h/6
    for j in range(1, N):
        I[j] = j*h*h
    I[N] = (N-1)/2*h*h + h*h/3
    return I

I = integral_coeffs(N)
# sanity: r==1 -> 0.5 ; r==x -> 1/3
assert abs(I.sum() - 0.5) < 1e-12
xj = np.arange(N+1)*h
assert abs((I*xj).sum() - 1/3) < 1e-9

def build_lp(M, B, rows_extra=None, s_override=None, p1=None, extra_rows_offset=0):
    """rows = 1..M of the N=256 law (index j-1). Variables: [c0, r_0..r_256]."""
    n = N+2
    c = np.zeros(n); c[0] = 1; c[1:] = I      # max c0 + I.r  -> minimize -(c0 + I.r)
    # validity: c0 + sum_{i in rows} s_i r_i <= p
    if p1 is None: p1 = p0
    rows = list(range(0, M))                  # indices j-1 for j=1..M
    s_use = s if s_override is None else s_override
    A_ub, b_ub = [], []
    if M > 0:
        a = np.zeros(n); a[0] = 1
        for i in rows: a[1+i+1] = s_use[i]    # r_{i+1} corresponds to grid index i+1 (r_0 is x=0)
        A_ub.append(a); b_ub.append(p1)
    if extra_rows_offset:
        a = np.zeros(n); a[0] = 1
        for (i, si) in rows_extra or []:
            a[1+i+1] = si
        A_ub.append(a); b_ub.append(p1)
    # r(1) = r_256 = 0
    A_eq = np.zeros((1, n)); A_eq[0, -1] = 1
    b_eq = [0.0]
    # slope: |r'(1)| = 256*|r_255| <= B
    bounds = [(None, None)] + [(-1, 1)]*(N+1)
    bounds[1+N-1] = (-B/256, B/256)          # r_255
    res = linprog(-c, A_ub=np.array(A_ub) if A_ub else None, b_ub=np.array(b_ub) if b_ub else None,
                  A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')
    return res

def report(res, tag):
    print(f"\n== {tag} ==")
    if not res.success:
        print("  LP FAILED:", res.message); return None
    c0 = res.x[0]; r = res.x[1:]
    v = c0 + (I*r).sum()
    gain = (I*r).sum() - (s[:M_used]@r[1:M_used+1]) if M_used>0 else float('nan')
    print(f"  v* = {v:.10f}   (c0* = {c0:.6f})")
    if M_used>0:
        rowsum = s[:M_used]@r[1:M_used+1]
        print(f"  validity slack = {p0 - (c0 + rowsum):.3e}  rowsum = {rowsum:.6f}  int = {(I*r).sum():.6f}")
    print(f"  slope r'(1) = {256*(r[-1]-r[-2]):.4f} (budget B)")
    print(f"  box-active r_j: j in {[j for j in range(257) if abs(abs(r[j])-1)<1e-8][:12]} ... count={sum(1 for j in range(257) if abs(abs(r[j])-1)<1e-8)}")
    if res.ineqlin is not None and res.ineqlin.marginals is not None:
        print(f"  validity dual = {res.ineqlin.marginals}")
    # marginals on bounds
    up = res.upper.marginals if res.upper is not None else None
    lo = res.lower.marginals if res.lower is not None else None
    return dict(v=v, c0=c0, r=r, res=res)

print("E(1) =", E1, " |E(1)| =", abs(E1))
print("near-CUE: 1/(6N^2)+tau/(2N) =", 1/(6*N*N))

# ---- LP-A: full validity (M=255 near-CUE rows), B sweep ----
print("\n############ LP-A: full near-CUE validity (rows 1..255), slope budget B ############")
M_used = 255
for B in [0.5, 1.0, 2.0, 4.0, 8.0]:
    res = build_lp(M_used, B)
    report(res, f"LP-A B={B}")

# ---- LP-B: interpolation over rows M ----
print("\n############ LP-B: row sweep M (validity on rows 1..M), B=1 ############")
B = 1.0
for M in [1, 2, 4, 8, 16, 32, 64, 128, 192, 255]:
    M_used = M
    res = build_lp(M, B)
    if res.success:
        v = res.x[0] + (I*res.x[1:]).sum()
        print(f"  M={M:4d}:  v* = {v:.10f}")
    else:
        print(f"  M={M:4d}:  FAILED {res.message}")
