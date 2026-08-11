#!/usr/bin/env python3
"""Verify the Stability.lean identity numerically against the extracted law data."""
import json, numpy as np
d = json.load(open('law_data.json'))
s = np.array(d['s_mid'])   # s_j j=1..256
p0 = d['p0']; N = 256; h = 1/N

# E(1) = int_0^1 C(x) dx - int_0^1 x^2/2 dx, C(x) = sum_{j/256<=x} s_j
xs = np.arange(1, N+1)/N   # j/256
E1 = sum(s[j]*(1 - xs[j]) for j in range(N)) - 1/6
print("E(1) =", E1)
print("nearCUE bound 1/(6N^2)+tau/(2N) =", 1/(6*N*N) + 3e-40/(2*N))

# D(1) = sum s_j - 1/2
D1 = s.sum() - 0.5
print("D(1) =", D1)

# core identity: for r in C^1 with r'=g, h=r'' integrable:
#   sum_j s_j r(j/N) - int_0^1 r x dx = r(1) D(1) - g(1) E(1) + int_0^1 h E
def test(r, g, h, name):
    rs = np.array([r(x) for x in xs])
    lhs = (s@rs) - integral_rx(r)
    rhs = r(1.0)*D1 - g(1.0)*E1 + int_hE(h)
    print(f"{name}:  lhs={lhs:.10e}  rhs={rhs:.10e}  diff={lhs-rhs:.2e}")

def integral_rx(r):
    # trapezoid on each cell, exact for polynomials up to degree 1 in x*r... use Simpson-ish fine grid
    xf = np.linspace(0,1,4097)
    return np.trapezoid(xf*r(xf), xf)

def int_hE(h):
    xf = np.linspace(0,1,4097)
    # E(x) = int_0^x C - x^3/6
    def C(t):
        return s[np.searchsorted(xs, t, side='right')-1] if t>=xs[0] else 0.0
    E = np.array([np.trapezoid([C(u) for u in np.linspace(0,x,64)], np.linspace(0,x,64)) - x**3/6 for x in xf])
    return np.trapezoid(h(xf)*E, xf)

test(lambda x: 1-x, lambda x: -1., lambda x: 0.*x, "r=1-x")
test(lambda x: np.cos(np.pi*x), lambda x: -np.pi*np.sin(np.pi*x), lambda x: -np.pi**2*np.cos(np.pi*x), "r=cos(pi x)")

# what does the signed gain look like for r with r(1)=0, slope r'(1)=B?
# r(x) = (1-x)*(1 + a*x)  -> r(1)=0, r'(1) = -1-a => choose a so r'(1)=B  => a = -B-1
for B in [1.0, 4.0]:
    a = -B-1
    r = lambda x: (1-x)*(1+a*x)
    g = lambda x: -1 + a*(1-2*x)  # derivative: d/dx[(1-x)(1+ax)] = -(1+ax)+(1-x)a = -1-ax+a-ax = a-1-2ax
    gain = integral_rx(r) - (s@np.array([r(x) for x in xs]))
    print(f"B={B}: r'(1)={g(1.0):.3f}  gain=int-rowsum = {gain:.6e}   ceiling says gain <= |r'(1)||E(1)|+M int|h| = {abs(g(1.0))*abs(E1)+1/(6*N*N)*abs(a*2*1)}")
