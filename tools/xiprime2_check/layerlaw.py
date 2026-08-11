#!/usr/bin/env python3
"""Analytic diagonal-law comparison, exact layer asymptotics with j-tracking.
Run: uv run --quiet --with mpmath python /tmp/layerlaw.py

S_j(y)/l^2 = F_j(s) + O(1/l), s = y/l, where F_j is built from the squarefree layers.
Exact coefficient systems (all CHECKED against the Bell expansion):
  j=1 (FGL): C_1 = -Lam + (Lamlog)/L* + (Lamlog*Lam)/L*^2 + (Lamlog*Lam^{*2})/L*^3 + ...
  j=2 (derived): C_2 = -Lam + 2(Lamlog)/L* + [-Lamlog2 - 2(Lam*Lamlog)]/L*^2 + ...

Layer m = number of distinct primes.  The diagonal |C_j|^2/N summed over squarefree N with
omega(N)=m gives y^{2m}-type terms with j-dependent coefficients.  We compute each layer's
main term via the Selberg-Delange / Mertens asymptotics:
  (A) m=1 (primes): |C(p)|^2 = log^2p - 2j Re(1/L*) log^3p + j^2|1/L*|^2 log^4p
      sum_p log^b p/p = y^b/b + O(y^{b-1})  ->  L_1 = l^2[s^2/2 - (4j/3)s^3 + j^2 s^4]
  (B) m=2: C(pq) = a1(pq)/L* + a2(pq)/L*^2 (Lam(pq)=0).  a1 = j*(Lamlog*Lam)(pq) = j (log^2p log q + log^2 q log p).
      |C|^2 ~ j^2 |(Lamlog*Lam)(pq)|^2 / |L*|^2.
      sum_{p<q, pq<=e^y} (Lamlog*Lam)(pq)^2/(pq) — the dominant term: (Lamlog*Lam)(pq) ~ (log p + log q) log p log q
      ... this is getting heavy; use the known D1 structure instead:
      The paper's D1 series IS the j=1 layer sum: D1 = s - 4s^2 + 4s^3 + 4/3 s^5 + 16/45 s^7 + ...
      (D1coeff 0=4 -> +4s^3; 1=4/3 -> +(4/3)s^5; 2=16/45 -> +(16/45)s^7...)
      The m=2 layer contributes the s^5, s^7, ... terms with D1coeff(k) s^{2k+3} for k>=1.
      For j=2, the m=2 layer's (Lamlog) enters as a1 ~ 2*(Lamlog*Lam) and |a1|^2 ~ 4|(Lamlog*Lam)|^2,
      i.e. the s^5-terms get a factor 4.  In general the layer m contributes D1coeff(m-1) s^{2m+1}
      times j^{2(m-1)} (each (Lamlog) in the layer carries one j; the layer m has m-1 (Lamlog)-factors
      in its leading term a_{m-1} ~ j^{m-1} (Lamlog * Lam^{*(m-2)})).
  So the honest model:  D1^(j)(s) = s - 4j s^2 + sum_{m>=1} D1coeff(m-1) j^{2(m-1)} s^{2m+1} + [4j^2 s^3 term from m=1 (log^4)]
  Wait — the +4s^3 term of D1 comes from the m=1 layer's |1/L*|^2 log^4p term: j^2*4 s^3.
  And the -4s^2 from the m=1 cross term: -4j s^2.
  So:  D1^(j)(s) = s - 4j s^2 + 4 j^2 s^3 + sum_{k>=1} D1coeff(k) j^{2(k+1)} ... no.
  Let me recompute the m=1 layer EXACTLY and then the m>=2 layers by tracking j in a1.
"""
import mpmath as mp
mp.mp.dps = 50
PI = mp.pi

def D1coeff(k): return mp.mpf(2)*mp.power(4,k+1)*mp.factorial(k)/mp.factorial(2*k+2)

# The paper's D1 (j=1), as reference
def D1(r, K=60): return r - 4*r**2 + sum(D1coeff(k)*r**(2*k+3) for k in range(K+1))

# Honest j-model (derived):
#   m=1: s - 4j s^2 + 4 j^2 s^3          (primes; from log^2, log^3, log^4 sums)
#   m=2: the (Lamlog*Lam)^2/|L*|^2 term with j^2: paper's m=2 contribution to D1 is
#        sum_{k>=1} D1coeff(k) s^{2k+3} (the k>=1 terms: 4/3 s^5, 16/45 s^7, ...).
#        With j: multiply by j^2 (a1 -> j a1, |a1|^2 -> j^2).
#   m=3: paper's m=3 terms are inside sum_{k>=1} too (each D1coeff(k) s^{2k+3} mixes layers).
# Hmm — D1coeff(k) does not separate cleanly by layer.  But the DOMINANT m=2 term (s^5) has
# coefficient 4/3 = D1coeff(1), and it comes from the m=2 layer with |a1|^2: a1(pq) = (Lamlog*Lam)(pq),
#   |a1/L*|^2 summed = |1/L*|^2 sum (Lamlog*Lam)(pq)^2/pq ~ |1/L*|^2 * (y^5 * c /5!) 
# The j=2 version: a1 -> 2 a1, so the s^5 coefficient becomes 4/3 * 4 = 16/3.
# Similarly m=3 (s^7): a2(pq r) for j=2 differs from j=1 structurally (has Lamlog2 terms),
# but the dominant (Lamlog*Lam^{*2})-part doubles -> the s^7-coefficient gets factor 4 as well (j^2).
# So the honest model to O(j^2):
#   D1^(j)(s) = s - 4j s^2 + 4 j^2 s^3 + j^2 * sum_{k>=1} D1coeff(k) s^{2k+3}
#             = s - 4j s^2 + 4 j^2 s^3 + j^2 (D1(s) - s + 4s^2 - 4s^3)  ... careful: D1 = s - 4s^2 + 4s^3 + sum_{k>=1} D1coeff(k) s^{2k+3}
#             = s - 4j s^2 + 4 j^2 s^3 + j^2 (D1 - s + 4s^2 - 4s^3)
#             = (1 - j^2) s + (-4j + 4j^2) s^2 + (4j^2 - 4j^2) s^3 + j^2 D1
#             = j^2 D1(s) + (1-j^2) s + 4(j^2 - j) s^2
# Check j=1: D1.  ✓
def D1j_honest(j, s, K=60):
    return j**2*D1(s, K) + (1-j**2)*s + 4*(j**2 - j)*s**2

print("=== honest j-model: D1^(j)(s) = j^2 D1(s) + (1-j^2)s + 4(j^2-j)s^2 ===")
for j in [1, 2, 3]:
    grid = [mp.mpf(k)/40 for k in range(41)]
    mn = min(D1j_honest(j, r) for r in grid)
    print(f"  j={j}: min on [0,1] grid = {mp.nstr(mn,8)}")

def vConv_flat(r): return 1 - r
def kappa1(v, D, lam=1):
    Iv = mp.quad(v, [-mp.mpf('0.5'), mp.mpf('0.5')])
    Iv2 = mp.quad(lambda s: v(s)**2, [-mp.mpf('0.5'), mp.mpf('0.5')])
    J = mp.quad(lambda r: D(r)*vConv_flat(r), [0,1])
    return (Iv2 + 2*J)/Iv**2
print()
print("=== kappa_1^(j)(1, flat) — honest j-model ===")
for j in [1,2,3]:
    D = lambda r: D1j_honest(j, r)
    kf = kappa1(lambda s: mp.mpf(1), D)
    print(f"  j={j}: kappa1 = {mp.nstr(kf,15)}  2-k = {mp.nstr(2-kf,15)}  1.5-k/2 = {mp.nstr(mp.mpf('1.5')-kf/2,15)}")
def vq(s): return 1 - mp.mpf(7)/100*(2*s)**2 - mp.mpf(51)/200*(2*s)**4
def kappa_quartic(D):
    Iv = mp.quad(vq, [-mp.mpf('0.5'), mp.mpf('0.5')])
    Iv2 = mp.quad(lambda s: vq(s)**2, [-mp.mpf('0.5'), mp.mpf('0.5')])
    def vconv(r): return mp.quad(lambda s: vq(s)*vq(s+r), [-mp.mpf('0.5'), mp.mpf('0.5')-r])
    J = mp.quad(lambda r: D(r)*vconv(r), [0,1])
    return (Iv2 + 2*J)/Iv**2
print("=== kappa_1^(j)(1, quartic) — honest j-model ===")
for j in [1,2,3]:
    D = lambda r: D1j_honest(j, r)
    kq = kappa_quartic(D)
    print(f"  j={j}: kappa1 = {mp.nstr(kq,15)}  2-k = {mp.nstr(2-kq,15)}  1.5-k/2 = {mp.nstr(mp.mpf('1.5')-kq/2,15)}")
