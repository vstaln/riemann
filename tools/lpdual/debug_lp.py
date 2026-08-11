#!/usr/bin/env python3
import json, numpy as np
from scipy.optimize import linprog
d = json.load(open('law_data.json'))
s = np.array(d['s_mid']); p0 = d['p0']; N=256; h=1/N
E1 = d['E1']

def integral_coeffs(N):
    h = 1/N; I = np.zeros(N+1); I[0] = h*h/6
    for j in range(1, N): I[j] = j*h*h
    I[N] = (N-1)/2*h*h + h*h/3
    return I
I = integral_coeffs(N)

def build(M, B):
    n = N+2; c = np.zeros(n); c[0]=1; c[1:]=I
    rows = list(range(0, M))
    A_ub, b_ub = [], []
    if M>0:
        a = np.zeros(n); a[0]=1
        for i in rows: a[1+i+1] = s[i]
        A_ub.append(a); b_ub.append(p0)
    A_eq = np.zeros((1,n)); A_eq[0,-1]=1; b_eq=[0.0]
    bounds = [(None,None)] + [(-1,1)]*(N+1)
    bounds[1+N-1] = (-B/256, B/256)
    return linprog(-c, A_ub=np.array(A_ub), b_ub=np.array(b_ub), A_eq=A_eq, b_eq=b_eq,
                   bounds=bounds, method='highs')

res = build(255, 8.0)
r = res.x[1:]; c0 = res.x[0]
intr = (I*r).sum()
rowsum = (s[:255]@r[1:256])
print("c0 =", c0)
print("r_255 =", r[255], " r_256 =", r[256], "  r'(1) =", 256*(r[256]-r[255]))
print("int =", intr, " rowsum =", rowsum, " gain = int-rowsum =", intr-rowsum)
print("validity lhs = c0+rowsum =", c0+rowsum, " p0 =", p0)

# identity: sum_{j=1..256} s_j r_j - int = r(1) D(1) - g(1) E(1) + int h E
D1 = s.sum()-0.5
print("identity lhs (sum-int) =", rowsum - intr)
print("identity rhs (r1 D1 - g1 E1 + int hE) =", r[256]*D1 - (256*(r[256]-r[255]))*E1 + 0.0)
print("E1 =", E1)
# so gain = g(1)E(1) =", (256*(r[256]-r[255]))*E1)

# where are the box-active and free variables?
free = [j for j in range(257) if abs(abs(r[j])-1) > 1e-8]
print("free r_j:", free)
for j in free:
    print(f"  r_{j} = {r[j]:.6f}  (x={j/256:.4f})")

# residual: sum of |r_j| weight
print("r[0] =", r[0])
