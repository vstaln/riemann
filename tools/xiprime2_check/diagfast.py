#!/usr/bin/env python3
"""Analytic diagonal-law comparison for j=1 vs j=2 (fast, uses the layer asymptotics).
Run: uv run --quiet --with mpmath python /tmp/diagfast.py

For the diagonal law S_j(y) = sum_{N<=e^y} |C^(j)(N;L*)|^2/N with L* = l/2 + i pi/4:

  Squarefree layers omega(N) = m (m >= 1):
  - m = 1 (primes):   C(p) = -log p + j log^2 p / L*
      |C|^2 = log^2p - 2j Re(1/L*) log^3p + j^2 |1/L*|^2 log^4p
      sum_p (log p)^b/p = y^b/b (main term), y = l s
      layer_1 = l^2 (s^2/2 - (4j/3) s^3 + j^2 s^4) + O(l)
  - m = 2:  C(pq) = [j (Lambda log)](pq)/L* + [(-Lambda)(p)(-Lambda)(q)-type / L*^2 terms]...
      The j-multiplicity enters each (Lambda log) term linearly; the L*^-2 terms are j^2-weighted.

The full D1 has the form D1(r) = r - 4r^2 + sum_k d_{k+1} r^{2k+3} with d_1=4, d_2=4/3, ...
which is exactly the m=1 layer (r - 4r^2 + 4r^3) plus the m>=2 layers (the 4/3 r^5, ...).

KEY STRUCTURAL FACT (verified exactly via Bell-polynomial expansion): C^(j) = C^(1) with
every (Lambda log)-type coefficient multiplied by j.  In the diagonal law:
  |C^(j)|^2 = |C^(1)|^2 with cross terms (Lambda)(Lambda log) -> j-weighted, (Lambda log)^2 -> j^2-weighted.

We now compute the resulting densities D1^(j) by the SAME layer decomposition, tracking j:
  prime layer:   s - 4j s^2 + 4 j^2 s^3        (m=1)
  m=2 layer:     involves [j(Lambda log)*...] terms -> (4/3) * j^2 s^5-type / 4 ... 
  general m:     each (Lambda log)^{m-1} carries j^{m-1}; the D1coeff(k) for the k-th layer
                 (the 2*4^{k+1} k!/(2k+2)! s^{2k+3} terms) carry j^k.

We TEST this model:  D1^(j)(r) := r - 4j r^2 + sum_{k>=0} D1coeff(k) * j^{k+1} r^{2k+3}
i.e. the coefficient of r^{2k+3} is multiplied by j^{k+1} (each (Lambda log) in the k-th layer
carries one factor j; there are k+1 of them in the layer that produces r^{2k+3}).
Then compute kappa_1^(j)(1,v) for flat/quartic and compare with j=1.
"""
import mpmath as mp
mp.mp.dps = 50
PI = mp.pi

def D1coeff(k): return mp.mpf(2)*mp.power(4,k+1)*mp.factorial(k)/mp.factorial(2*k+2)

def D1j(j, r, K=60):
    """model density for derivative j: r - 4j r^2 + sum_k D1coeff(k) j^{k+1} r^{2k+3}."""
    return r - 4*j*r**2 + sum(D1coeff(k)*j**(k+1)*r**(2*k+3) for k in range(K+1))

def vConv_flat(r): return 1 - r

def kappa1(v, D, lam=1):
    Iv = mp.quad(v, [-mp.mpf('0.5'), mp.mpf('0.5')])
    Iv2 = mp.quad(lambda s: v(s)**2, [-mp.mpf('0.5'), mp.mpf('0.5')])
    J = mp.quad(lambda r: D(r) * vConv_flat(r), [0, 1])
    return (Iv2 + 2*J)/Iv**2

print("=== D1^(j) model check: positivity and kappa ===")
for j in [1,2,3]:
    D = lambda r: D1j(j, r)
    # sample positivity on [0,1]
    grid = [mp.mpf(k)/40 for k in range(41)]
    mn = min(D(r) for r in grid)
    kf = kappa1(lambda s: mp.mpf(1), D)
    print(f"  j={j}: min D1^(j) on grid = {mp.nstr(mn,8)};  kappa1(1,flat) = {mp.nstr(kf,15)}  2-k = {mp.nstr(2-kf,15)}")
print()
print("=== quartic window ===")
def vq(s): return 1 - mp.mpf(7)/100*(2*s)**2 - mp.mpf(51)/200*(2*s)**4
def kappa_quartic(D):
    Iv = mp.quad(vq, [-mp.mpf('0.5'), mp.mpf('0.5')])
    Iv2 = mp.quad(lambda s: vq(s)**2, [-mp.mpf('0.5'), mp.mpf('0.5')])
    def vconv(r): return mp.quad(lambda s: vq(s)*vq(s+r), [-mp.mpf('0.5'), mp.mpf('0.5')-r])
    J = mp.quad(lambda r: D(r)*vconv(r), [0,1])
    return (Iv2 + 2*J)/Iv**2
for j in [1,2,3]:
    D = lambda r: D1j(j, r)
    kq = kappa_quartic(D)
    print(f"  j={j}: kappa1(1,quartic) = {mp.nstr(kq,15)}  2-k = {mp.nstr(2-kq,15)}  1.5-k/2 = {mp.nstr(mp.mpf('1.5')-kq/2,15)}")
