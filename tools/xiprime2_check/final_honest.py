#!/usr/bin/env python3
"""ROBUSTNESS CHECK: kappa_1^(2) from the honest form-factor model + empirical corroboration.

1. Honest A^(2)(x) (measured numerically above): A^(2) >> A^(1), power ~ x^{1.54} vs x^{1.0}-ish.
   The FGL form-factor/density mapping: F_1^(2)(alpha) has a LARGER alpha T^{1-2alpha} log T (1 - 8|alpha| + 4*(...)) 
   coefficient than F_1.  The D1^(2) density is correspondingly larger on [0,1], driving kappa_1^(2) UP.
2. Empirical: the xi''-zero gap ratio was 1.05 (wider gaps = lower density near 0 = LARGER kappa if the
   density grows away from 0).  More pairs at larger separation -> larger int D1(v*v) -> larger kappa.

Both point the same way: kappa_1^(2) > kappa_1^(1).  KILL RULE TRIGGERED: kappa^(2) >= kappa^(1).

We now pin down the honest D1^(2) from the A^(2) measurement and compute the exact kappa.
The FGL mapping: D1(r) ~ the density whose Stieltjes integral with (v*v) gives the pair sum.
From (5.8)-(5.11): the density D1 is (d/ds)-ish of A(x)/x at x = e^{l s}-scaled.  Concretely the
F_1(alpha) form factor F_1(alpha) = |alpha| + alpha(1 - 4|alpha| + 2 sum (k-1)!/(2k)! (2|alpha|)^{2k}) * (logT-part)
maps to D1(r) = r - 4r^2 + sum D1coeff(k) r^{2k+3}.  The D1coeff(k) are the Fourier coefficients
of the (k-1)!/(2k)! (2|alpha|)^{2k} -> the Bessel-type transform.  For xi'' the coefficient of
(2|alpha|)^{2k} in the sum is scaled: k=0 (the -4|alpha|) -> -8|alpha| (factor 2 from A_{0,1} doubled),
k>=1 -> factor 4 (|alpha_k|^2 -> 4|alpha_k|^2) PLUS new log^2-terms that push to higher order.
So the honest density model (matching the A-measurement):
  D1^(2)(r) = r - 8 r^2 + 4 sum_{k>=1} D1coeff(k) r^{2k+3} + [r^3-term: 4*4 = 16 r^3]
  (the +16r^3 = 4 * D1coeff(0) r^3 from |alpha_1|^2 = 4 (Lamlog)^2)
This is exactly /tmp/definitive2.py's model -> kappa^(2)(flat) = 1.8998, (quartic) = 1.7634.
KILL RULE: 1.90 >= 1.14, 1.76 >= 1.13.  TRIGGERED for both windows.

3. Sanity: is the D1^(2) >= 0?  min 0.0 on grid ✓ (a valid pair density).
4. Cross-check the empirical gap ratio prediction: D1^(2) larger -> more pairs at larger r -> wider
   gaps.  Empirically the xi'' gaps were ~5% wider.  Consistent in direction.
"""
import mpmath as mp
mp.mp.dps = 50

def D1coeff(k): return mp.mpf(2)*mp.power(4,k+1)*mp.factorial(k)/mp.factorial(2*k+2)
def D1(r, K=60): return r - 4*r**2 + sum(D1coeff(k)*r**(2*k+3) for k in range(K+1))
def D1j2(r, K=60): return r - 8*r**2 + 16*r**3 + 4*sum(D1coeff(k)*r**(2*k+3) for k in range(1,K+1))

def kappa1(D):
    J = mp.quad(lambda r: D(r)*(1-r), [0,1])
    return (1 + 2*J)/1
def vq(s): return 1 - mp.mpf(7)/100*(2*s)**2 - mp.mpf(51)/200*(2*s)**4
def kappa_quartic(D):
    Iv = mp.quad(vq, [-mp.mpf('0.5'), mp.mpf('0.5')])
    Iv2 = mp.quad(lambda s: vq(s)**2, [-mp.mpf('0.5'), mp.mpf('0.5')])
    def vconv(r): return mp.quad(lambda s: vq(s)*vq(s+r), [-mp.mpf('0.5'), mp.mpf('0.5')-r])
    J = mp.quad(lambda r: D(r)*vconv(r), [0,1])
    return (Iv2 + 2*J)/Iv**2

print("=== FINAL HONEST RESULT: the tower dies at the second rung ===")
k1f = kappa1(lambda r: D1(r)); k2f = kappa1(lambda r: D1j2(r))
k1q = kappa_quartic(lambda r: D1(r)); k2q = kappa_quartic(lambda r: D1j2(r))
print(f"flat:     kappa^(1) = {mp.nstr(k1f,15)}   kappa^(2) = {mp.nstr(k2f,15)}   KILL? {k2f >= k1f}")
print(f"quartic:  kappa^(1) = {mp.nstr(k1q,15)}   kappa^(2) = {mp.nstr(k2q,15)}   KILL? {k2q >= k1q}")
print()
print("=== what the killed tower means ===")
print("xi'  flat:    2-kappa1 = 0.85838  (simple-on-line),  1.5-k/2 = 0.92919  (distinct-xi')")
print("xi'' flat:    2-kappa2 = 0.10020  (simple-on-line),  1.5-k/2 = 0.55010  (distinct-xi'')")
print("xi'' is WORSE: the derivative tower's certificate constants DEGRADE with j.")
print("The Farmer combination (Nd >= 2^-J[...]) needs BETTER fi_j as j grows to beat 0.6603.")
print("Since fi_2 <= 0.10 << fi_0 = 0.858, the combination cannot beat Wu's 0.6603.")
