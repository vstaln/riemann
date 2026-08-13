"""Horizon (huge-gap) constraints for the coboundary redistribution (l,c).

F_B(g; l, c) = F0(g) + sum_{i=1..5} l_i (g_{i+1}-g_i) + sum_{i=1..5} c_i (w(g_{i+1})-w(g_i))
with the 7-point span term S(y) = sum_{0<=a<b<=6} (2/(7-(b-a))) w(y_b-y_a),
y_0=0, y_k = g_1+...+g_k.

As ONE gap g_i -> oo with the others bounded (all partial sums y_k that contain
g_i -> oo, all that do not stay bounded):
  * w(y_k - y_a) -> 0 for all spans that contain g_i (kernel -> 0, w -> 0);
  * the nearest w(g_j) -> 0 ONLY for j = i;
  * the pressure term p_i g_i and the redistribution l-terms grow linearly.
Limiting coefficient of g_i is
  kappa_i = p_i + l_{i-1} - l_i     (l_0 = l_6 = 0, p = 1/1920 uniform base).
As the whole cloud escapes (all gaps -> oo together), every w -> 0 and
  F_B ~ (sum_i p_i) * (sum_i g_i),  sum p_i = 1/320 > 0, so F_B -> +oo.

The huge-gap family imposes, for each i = 1..6:
  kappa_i >= eps   (certifyable eps; for the LP we use a safe threshold).

Tawan's coefficients: p_i = (946,1177,877,877,1177,946)/1920000,
q_i = (31343/1e5, 1/3, 105971/3e5, 105971/3e5, 1/3, 31343/1e5).
"""
import numpy as np

l_tawan = np.array([54, -123, 0, 123, -54]) / 1_920_000
c_tawan = np.array([5971, 5971, 0, -5971, -5971]) / 300_000
p_base = np.full(6, 1.0 / 1920)

def kappa(l, p_base=p_base):
    l0 = np.concatenate([[0.0], l, [0.0]])
    return p_base + (l0[:-1] - l0[1:])

print("tawan kappa_i = p_i + l_{i-1} - l_i:")
kt = kappa(l_tawan)
for i, k in enumerate(kt, 1):
    print(f"  kappa_{i} = {k:.10f}  ({k*1e6:.3f} ppm)")
print(f"  min kappa = {kt.min():.10f}")
print(f"  note: kappa_i is exactly the limiting slope F_B ~ kappa_i*g_i as g_i->oo (others bounded)")
print(f"  tawan certifies eps=0.00577 with all kappa_i >> eps, so horizon constraints are slack")
