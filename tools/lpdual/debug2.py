#!/usr/bin/env python3
import json, numpy as np
d = json.load(open('law_data.json'))
s = np.array(d['s_mid']); p0 = d['p0']; N = 256; h = 1/N

w = np.full(N+1, h); w[0] = h/2; w[N] = h/2
W = np.zeros((N+1, N+1))
for j in range(1, N+1):            # int_0^{x_j} g, x_j = j/N
    W[j,0] = h/2
    for k in range(1, j):
        W[j,k] = h
    W[j,j] = h/2                   # W[0,:] = 0
R = -np.outer(np.ones(N+1), w) + W
def integral_coeffs(N):
    h = 1/N; I = np.zeros(N+1); I[0] = h*h/6
    for j in range(1, N): I[j] = j*h*h
    I[N] = (N-1)/2*h*h + h*h/3
    return I
I = integral_coeffs(N)
iG = I @ R
sG = s @ R[1:N+1,:]

# g ≡ -1
g = -np.ones(N+1)
r = R @ g
print("r(0), r(0.5), r(1) for g=-1:", r[0], r[N//2], r[N], "  (expect 1, 0.5, 0)")
print("int =", iG@g, " (expect 1/6 =", 1/6, ")")
print("rowsum =", sG@g, " (expect sum s_j(1-j/256) =", sum(s[j]*(1-(j+1)/N) for j in range(255)), ")")
print("gain = int - rowsum =", iG@g - sG@g)

# direct check of I vector
r_exact = np.array([1 - j*h for j in range(N+1)])
print("int via I:", (I*r_exact).sum(), " via analytic:", 1/6)
print("I sum (r=1):", I.sum(), " expect 0.5")
print("I·x (r=x):", (I*np.arange(N+1)*h).sum(), " expect 1/3")

# feasibility of g=-1, c0 = p0 - rowsum: v = c0 + int
c0 = p0 - sG@g
print("c0 =", c0, " v =", c0 + iG@g, " p0 =", p0)

# slope |g_256|=1<=B, C=0: sum|Δg| = 0 ok
print("sum |Δg| =", np.abs(np.diff(g)).sum())
