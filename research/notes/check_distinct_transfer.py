#!/usr/bin/env python3
"""
Q2 (distinct-zeros 5/6 -> 5/6+delta) verification: does the Gram-stability term
tr Psi(M) transfer to the DISTINCT-count functional?

The paper's chain (claude-riemann-paper.txt §1.4, lines 287-296) shows Theorem C's
5/6 is NOT a separate functional: it is the affine image (1+H)/2 of the simple-zeros
constant H, via the counting identity  s2+p <= (N-s1)/2  applied to the SAME
inequality (L): 3*s1 + 4*s2 + 4*p >= 4*tr - ||.||_F^2.

So the entire transfer question collapses to: does the corrected simple-zeros bound
(H=0.6730690, CERTIFIED) move the DISTINCT constant?  (1+H)/2 = 0.8365345.
An eps-floor refinement that certifies H -> H' certifies 5/6 -> (1+H')/2.

Here we CHECK NUMERICALLY the two hypotheses the transfer rests on, on the ONLY
data we have (kernel k of the alpha=1.49 certificate / cos(sqrt2) window):
  H1: the three-consecutive-gap positivity eps (tr Psi >= N*eps) holds for the
      DISTINCT-atom Gram (unit diagonal, all gaps present) with the same eps as the
      simple-atom Gram.  (same-kernel-eps argument)
  H2: multiplicity-scaled atoms (Theorem A/C multiple-on-line zeros) can only
      INCREASE tr Psi (so eps survives).
And computes the honest constant: (1+0.6730690)/2 = 0.8365345 (PROVEN affine).

Labels: [PROVEN] / [CHECKED NUMERICALLY] / [CONJECTURED] / [ABANDONED].
Run: uv run --with numpy --with scipy --with mpmath python /tmp/q2_distinct_56/check_distinct_transfer.py
"""
import numpy as np
from mpmath import mp, mpf, sin, cos, sqrt, pi, cot, polyroots

mp.dps = 40
SQ2 = np.sqrt(2.0)
A = SQ2 / 2.0
K0 = float(np.sin(A)/(SQ2) + np.sin(A)/(SQ2))  # K(0): sin(pi/4)*(1/sqrt2+1/sqrt2)=1
def K_np(x):
    x = np.asarray(x, dtype=float)
    d1 = SQ2 + 2.0*np.pi*x; d2 = SQ2 - 2.0*np.pi*x
    t1 = np.where(np.abs(d1)<1e-9, 0.5, np.sin(A+np.pi*x)/d1)
    t2 = np.where(np.abs(d2)<1e-9, 0.5, np.sin(A-np.pi*x)/d2)
    return t1+t2
def k_np(x):
    # normalize so k(0)=1
    return K_np(x)/float(K_np(np.array([0.0]))[0])

def psi_np(t):
    t = np.asarray(t, dtype=float)
    return np.where(t<=2.0, (t-1.0)**2, 2.0*t-3.0)

# ---------- H1: distinct-atom Gram, 3 consecutive gaps ----------
def trPsi3(u, v):
    kuv, ku, kv = k_np(u+v), k_np(u), k_np(v)
    G = np.array([[1.,ku,kuv],[ku,1.,kv],[kuv,kv,1.]])
    return float(np.sum(psi_np(np.linalg.eigvalsh(G))))

N = 400
u = np.linspace(1e-5, 4.0, N); v = np.linspace(1e-5, 4.0, N)
best=(1e30,None)
for ui in range(N):
    for vi in range(N):
        if u[ui]+v[vi] > 4.0+1e-9: continue
        val = trPsi3(u[ui],v[vi])
        if val < best[0]: best=(val,(u[ui],v[vi]))
print("H1 distinct-atom 3-pt min trPsi = %.10e  at u=%.5f v=%.5f  (claimed 221/1e6=2.21e-4)" % (best[0],best[1][0],best[1][1]))

# mpmath refinement
def trPsi3_mp(u,v):
    ku,kv,kuv = K_mp(u)/K0_mp, K_mp(v)/K0_mp, K_mp(u+v)/K0_mp
    S = ku*ku+kv*kv+kuv*kuv; P = 2*ku*kv*kuv
    roots = polyroots([-1,0,S,-P])
    lam = [1-r for r in roots]
    return sum((t-1)**2 if t<=2 else 2*t-3 for t in lam)
def K_mp(x): return sin(A+pi*x)/(SQ2+2*pi*x)+sin(A-pi*x)/(SQ2-2*pi*x)
K0_mp = K_mp(0)
ub,vb = best[1]
bm,ba = mpf(1e30),None
for du in [mpf('-2e-3'),mpf('-1e-3'),mpf(0),mpf('1e-3'),mpf('2e-3')]:
    for dv in [mpf('-2e-3'),mpf('-1e-3'),mpf(0),mpf('1e-3'),mpf('2e-3')]:
        uu,vv = mpf(ub)+du, mpf(vb)+dv
        if uu+vv > mpf(4): continue
        val = trPsi3_mp(uu,vv)
        if val < bm: bm,ba = val,(uu,vv)
print("H1 mpmath min trPsi = %s at u=%s v=%s" % (mp.nstr(bm,18), mp.nstr(ba[0],10), mp.nstr(ba[1],10)))

# ---------- H2: multiplicity-scaled atoms ----------
def trPsi3_m(u,v,m):
    m=np.asarray(m,dtype=float); sq=np.sqrt(m)
    G=np.array([[m[0],sq[0]*sq[1]*k_np(u),sq[0]*sq[2]*k_np(u+v)],
                [sq[0]*sq[1]*k_np(u),m[1],sq[1]*sq[2]*k_np(v)],
                [sq[0]*sq[2]*k_np(u+v),sq[1]*sq[2]*k_np(v),m[2]]])
    return float(np.sum(psi_np(np.linalg.eigvalsh(G))))
print("H2 multiplicity blocks at argmin (u=%.4f v=%.4f):" % (best[1][0],best[1][1]))
for mm in [(1,1,1),(2,1,1),(1,2,1),(1,1,2),(2,2,1),(1,2,2),(3,1,1),(2,2,2),(4,4,4)]:
    print("   m=%s trPsi=%.6e" % (mm, trPsi3_m(best[1][0],best[1][1],mm)))
rng=np.random.default_rng(42); viol=0
for _ in range(4000):
    uu=rng.uniform(1e-3,4.0); vv=rng.uniform(1e-3,4.0)
    if uu+vv>4.0: continue
    base=trPsi3(uu,vv); m=rng.integers(1,5,size=3)
    if trPsi3_m(uu,vv,m) < base-1e-9: viol+=1
print("H2 random 4000 configs: violations (trPsi_m < all-simple) = %d" % viol)

# ---------- Affine theorem: (1+H)/2 ----------
Hcert = mpf('0.6730690301666756')
print("\nPROVEN affine: distinct const = (1+H)/2;  at H=Hcert (0.6730690): (1+H)/2 = %s" % mp.nstr((1+Hcert)/2, 16))
print("paper's abstract 0.83625 = (1+0.6725)/2 = %s" % mp.nstr((1+mpf('0.67250070367941164573'))/2, 12))
print("base 5/6 = %s" % mp.nstr(mpf(5)/6, 12))

# the sharpness config: 2N/3 simples + N/6 doubles -> distinct = 5/6 N
# with stability, s1 >= H' N: distinct >= (1+H')/2 via s2+p <= (N-s1)/2.
print("\ndelta from Hcert: (1+0.6730690)/2 - 5/6 = %s" % mp.nstr((1+Hcert)/2 - mpf(5)/6, 12))

# what eps-floor would be needed to exceed the CONDITIONAL distinct record 0.83625?
# and what our certified eps gives (linear response from the 3-pt/7-pt formulas):
resp = mpf('0.086250')  # H0/2 - 1/4 (dc/deps)
for name,eps in [("3-pt 221/1e6", mpf(221)/mpf(1e6)), ("7-pt 19/5000", mpf(19)/mpf(5000)), ("certified 7759/1e6 (not comparable: different eps def) ", mpf(7759)/mpf(1e6))]:
    print("   %s: dc = %s  (hypothetical linear response)" % (name, mp.nstr(resp*eps, 10)))
print("\nDONE.")
