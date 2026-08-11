#!/usr/bin/env python3
"""Compute the xi''-analog density D1^(2) from the honest coefficient-shift model.

Model (derived above, exact sympy, CHECKED): for W_j = xi^(j+1)/xi^(j),
    W_j - L = Z + j (L'+Z')/L + O(1/L^2)
so the coefficient system for derivative j is
    C^(j)(N; L*) = -Lambda(N) + j * (Lambda log)(N) / L* + O(1/L*^2)
(the leading -Lambda term is j-independent; the (Lambda log) correction carries the factor j).

The FGL diagonal law (Lemma 7.1) gives the pair density as the diagonal of |sum alpha_k/L*^k|^2.
For j = 1 we must recover D1(r) = r - 4r^2 + sum_k D1coeff(k) r^{2k+3}.  For general j we model
    alpha_0^(j) = -Lambda,  alpha_k^(j) = j * (Lambda log) * Lambda^{*(k-1)}  (k >= 1),
i.e. only the (Lambda log) terms carry the factor j (consistent with the eps-expansion).

We then recompute the squarefree-layer contributions exactly as in Coeff/MainTerm (the diagonal
law proof):  for N = p prime, C(p) = -log p + j log^2 p / L*, giving
    |C(p)|^2 = log^2 p - 2 j Re(1/L*) log^3 p + j^2 |1/L*|^2 log^4 p
with Re(1/L*) = 2/l + O(l^-3), |1/L*|^2 = 4/l^2 + O(l^-4), and sum_{p<=e^y} (log p)^b/p = y^b/b + ...
The D1 density follows from matching the y-powers.  Run: uv run --quiet --with mpmath python /tmp/d1shift.py
"""
import mpmath as mp
mp.mp.dps = 60

def D1coeff(k):
    return mp.mpf(2) * mp.power(4, k+1) * mp.factorial(k) / mp.factorial(2*k+2)

def D1(r, K=80):
    return r - 4*r**2 + sum(D1coeff(k)*r**(2*k+3) for k in range(K+1))

# The paper's D1 (j=1) — verify its origin from the prime layer:
#   sfPart(p-layer) ~ l^2 (s^2/2 - 4s^3/3 + s^4), s = y/l  (LayerOne.lean header)
#   => density (the d/dy derivative) = l * (d/ds)(s^2/2 - 4s^3/3 + s^4) / l^2 ... 
# D1(s) should integrate to (d/ds)(s^2/2 - 4 s^3/3 + s^4) = s - 4s^2 + 4s^3.
# Let's check: is D1's leading part r - 4r^2 + 4r^3?  D1coeff(0)=4 gives +4r^3, D1coeff(1)=4/3 -> +4/3 r^5...
# So D1 = r - 4r^2 + 4r^3 + 4/3 r^5 + ...  The first three terms r - 4r^2 + 4r^3 integrate to
# 1/2 - 4/3 + 1 = 0.1667.  The D1 series has MORE terms (from the k-fold Mertens layers).

# For general j: the prime-layer gives (s^2/2 - 2j s^3/3 + j^2 s^4) since
#   sum_p log^2 p/p ~ y, sum log^3/p ~ y^2/2 ... wait: sum (log p)^b/p = y^b/b + O(...) with y = l*s
#   |C(p)|^2 = log^2p - 2j Re(1/L*) log^3p + j^2|1/L*|^2 log^4p
#   sum = y^2/2 - 2j(2/l) y^3/3 + j^2 (4/l^2) y^4/4 ... = l^2 s^2/2 - (8j/3) l^2 s^3 ... hmm check scaling
# Let's do it carefully: y = l s.  sum log^2 p/p ~ y^2/2 = l^2 s^2/2.  sum log^3 p/p ~ y^3/3 = l^3 s^3/3.
#   |C|^2 ~ log^2 p - 2j(2/l) log^3 p + j^2(4/l^2) log^4 p
#   sum ~ l^2 s^2/2 - 4j/l * l^3 s^3/3 + 4j^2/l^2 * l^4 s^4/4 = l^2 [s^2/2 - (4j/3) s^3 + j^2 s^4]
# The density is (1/l^2) d/dy (this) = d/ds (s^2/2 - 4j s^3/3 + j^2 s^4) = s - 4j s^2 + 4j^2 s^3.
# For j=1: s - 4s^2 + 4s^3 (matches D1's leading 3 terms!).
# For j=2: s - 8s^2 + 16s^3.
# So the PRIME-LAYER density changes with j!  The full D1 has additional k-fold Mertens layers
# (the sum over k of D1coeff(k) r^{2k+3}), which also carry j-factors from alpha_k ~ j.

print("=== prime-layer density: s - 4j s^2 + 4 j^2 s^3 (derived) ===")
for j in [1,2,3]:
    print(f"  j={j}: D1^(j)_prime(s) = s - {4*j}s^2 + {4*j*j}s^3")
print()
print("=== Compare with D1 (j=1): leading 3 terms ===")
print("  D1(s) = s - 4s^2 + 4s^3 + 4/3 s^5 + ...")
print("  [CHECKED: D1coeff(0)=4 -> +4s^3; the s^2 coeff -4 = -4*1; s coeff 1]")
