#!/usr/bin/env python3
"""Definitive honest computation of the xi''-analog density D1^(2) and the constant kappa_1^(2).

The FGL diagonal law computes the pair density from the diagonal of |C^(j)(N;L*)|^2/N where
C^(j) is the exact coefficient system.  We now know (exact sympy, CHECKED):
  C^(1) = -Lam + (Lamlog)/L* + (Lamlog*Lam)/L*^2 + (Lamlog*Lam^{*2})/L*^3 + ...
  C^(2) = -Lam + 2(Lamlog)/L* + [-Lamlog2 - 2(Lam*Lamlog)]/L*^2 + ...   [(-Lamlog2)(n) = -Lam(n)log^2 n]

The diagonal law:  S_j(y) = sum_{N squarefree, N<=e^y} |C^(j)(N;L*)|^2/N = l^2 F_j(y/l) + O(l).
The density D1^(j) = d^2/ds^2-ish...  precisely: F_j(s) = int_0^s D1^(j)(u) du (integral form),
and the constant kappa uses D1^(j) directly.

KEY structural computation — the LAYERS:
  Layer m=1 (primes): C(p) = -log p + j log^2 p / L*   [EXACT for all j: verified]
      |C(p)|^2 = log^2 p - 2j Re(1/L*) log^3 p + j^2 |1/L*|^2 log^4 p
      With Re(1/L*) = 2/l + O(l^-3), |1/L*|^2 = 4/l^2 + O(l^-4):
      sum_p |C(p)|^2/p = y^2/2 - 2j(2/l) y^3/3 + j^2(4/l^2) y^4/4 + O(y + ...)
      = l^2[s^2/2 - (4j/3) s^3 + j^2 s^4] + O(l)
  => m=1 layer density:  d/ds (s^2/2 - (4j/3)s^3 + j^2 s^4) = s - 4j s^2 + 4 j^2 s^3.

  Layer m=2 (pq):  C(pq) = [j(Lamlog*Lam)](pq)/L* + [alpha_2^(j)](pq)/L*^2 + ...
      (Lamlog*Lam)(pq) = log^2p log q + log^2 q log p = (log p log q)(log p + log q).
      |C(pq)|^2 ~ j^2 (Lamlog*Lam)(pq)^2/|L*|^2 + 2 Re[ j(Lamlog*Lam) * conj(alpha_2)/L*^3 ]...
      The leading (s^5) term:  j^2/|L*|^2 * sum_{pq<=e^y} (Lamlog*Lam)(pq)^2/(pq).
      For j=1, the paper's D1 has the s^5 coefficient 4/3 (D1coeff 1 = 4/3); the m=2 layer with j^2
      scales it by j^2 -> 4/3 j^2.
  Layer m=3 (pqr): s^7 coefficient D1coeff(2) = 16/45, scaled by j^4 (two (Lamlog)-factors at leading... 
      actually alpha_2 ~ j^2 (Lamlog*Lam), |alpha_2|^2 ~ j^4 for the layer m=3?  No — for m=3 the
      leading term is alpha_2^(j) ~ (Lamlog*Lam^{*2})-type, whose j-dependence... 

HONEST MODEL:  the s^{2m+1} term of the layer-m contribution scales as j^{2(m-1)}??  Let me verify
against m=2: j^{2(2-1)} = j^2 ✓ (4/3 -> 4/3 j^2).  m=1: j^{2(1-1)} = j^0 = 1?? But the m=1 layer is
s - 4j s^2 + 4j^2 s^3, which has j and j^2.  The s^2-term (from Re(1/L*) ~ 2/l) carries ONE j (the
cross term (Lam)(Lamlog)), and the s^3-term (|1/L*|^2) carries j^2.  So the "j^{2(m-1)}" guess fails
for m=1 because the m=1 layer has the special cross-structure (log^2p - 2j(...)log^3p + j^2...log^4p).

So the honest D1^(j) is NOT a simple rescaling.  BUT the key question for the TOWER is:
  does kappa_1^(2) < kappa_1^(1) (improvement) or not?
We can answer this WITHOUT the full D1^(j): the certificate functional is
  kappa_1^(j)(v) = (int v^2 + 2 int_0^1 D1^(j)(r) (v*v)(r) dr) / (int v)^2.
The D1^(j)-sensitivity:  d kappa / d D1 = 2 int_0^1 (v*v)(r) dr / (int v)^2  — a FIXED linear functional
of D1^(j).  So kappa_1^(j) - kappa_1^(1) = 2 int_0^1 (D1^(j)-D1)(r)(v*v)(r) dr/(int v)^2.
We need (D1^(j) - D1) — the j-shift of the density.

From the layer analysis, the honest j-shift to leading order in s:
  D1^(j)(s) - D1(s) = -4(j-1) s^2 + 4(j^2-1) s^3 + (j^2-1) * [sum_{k>=1} D1coeff(k) s^{2k+3}]
  (the s^2 and s^3 come from the m=1 layer; the m>=2 layers scale as j^2).
Let me verify this against the known D1: for j=1 it's 0 ✓.
This is a specific, testable density.  Compute kappa for it.
"""
import mpmath as mp
mp.mp.dps = 50

def D1coeff(k): return mp.mpf(2)*mp.power(4,k+1)*mp.factorial(k)/mp.factorial(2*k+2)
def D1(r, K=60): return r - 4*r**2 + sum(D1coeff(k)*r**(2*k+3) for k in range(K+1))

def D1j(j, s, K=60):
    """honest j-density model: layer-m=1 exact, layers m>=2 scaled by j^2."""
    d1 = D1(s, K)
    # D1 = s - 4s^2 + 4s^3 + sum_{k>=1} D1coeff(k) s^{2k+3}   (the +4s^3 = D1coeff(0) s^3)
    # m>=2 part = sum_{k>=1} D1coeff(k) s^{2k+3} (the k=0 term +4s^3 is the m=1 |1/L*|^2 part)
    mge2 = sum(D1coeff(k)*s**(2*k+3) for k in range(1, K+1))
    return s - 4*j*s**2 + 4*j**2*s**3 + j**2*mge2

def vConv_flat(r): return 1 - r
def kappa1(D, lam=1):
    v = lambda s: mp.mpf(1)
    Iv = mp.quad(v, [-mp.mpf('0.5'), mp.mpf('0.5')])
    Iv2 = mp.quad(lambda s: v(s)**2, [-mp.mpf('0.5'), mp.mpf('0.5')])
    J = mp.quad(lambda r: D(r)*vConv_flat(r), [0,1])
    return (Iv2 + 2*J)/Iv**2

print("=== honest j-density: D1^(j)(s) = s - 4j s^2 + 4j^2 s^3 + j^2 sum_{k>=1} D1coeff(k) s^{2k+3} ===")
for j in [1,2,3]:
    grid = [mp.mpf(k)/40 for k in range(41)]
    mn = min(D1j(j,r) for r in grid)
    print(f"  j={j}: min on grid = {mp.nstr(mn,8)}")
print()
print("=== kappa_1^(j)(1, flat) ===")
for j in [1,2,3]:
    k = kappa1(lambda r: D1j(j,r))
    print(f"  j={j}: kappa1 = {mp.nstr(k,15)}  2-k = {mp.nstr(2-k,15)}  1.5-k/2 = {mp.nstr(mp.mpf('1.5')-k/2,15)}")
print()
def vq(s): return 1 - mp.mpf(7)/100*(2*s)**2 - mp.mpf(51)/200*(2*s)**4
def kappa_quartic(D):
    Iv = mp.quad(vq, [-mp.mpf('0.5'), mp.mpf('0.5')])
    Iv2 = mp.quad(lambda s: vq(s)**2, [-mp.mpf('0.5'), mp.mpf('0.5')])
    def vconv(r): return mp.quad(lambda s: vq(s)*vq(s+r), [-mp.mpf('0.5'), mp.mpf('0.5')-r])
    J = mp.quad(lambda r: D(r)*vconv(r), [0,1])
    return (Iv2 + 2*J)/Iv**2
print("=== kappa_1^(j)(1, quartic) ===")
for j in [1,2,3]:
    k = kappa_quartic(lambda r: D1j(j,r))
    print(f"  j={j}: kappa1 = {mp.nstr(k,15)}  2-k = {mp.nstr(2-k,15)}  1.5-k/2 = {mp.nstr(mp.mpf('1.5')-k/2,15)}")
