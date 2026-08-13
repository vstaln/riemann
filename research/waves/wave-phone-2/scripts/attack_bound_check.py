#!/usr/bin/env python3
"""attack_bound_check.py -- adversarial re-derivation of tau, B, bound at m=133
from the discovery note formula. CHECKED NUMERICALLY (mpmath 160+ digits).

HEADLINE: the certified record 0.6732660791400006829... at
(alpha, psum, P, m, eps) = (1.49, 1/220, 1/1320, 133, 8065/1e6 exact).
The script emits the headline itself: run and read 'bound'.
"""
import mpmath as mp
mp.mp.dps = 160

def H_cosine(alpha):
    I0 = 2*mp.sin(alpha/2)/alpha
    I2 = mp.mpf(1)/2 + mp.sin(alpha)/(2*alpha)
    constant = mp.sin(alpha/2)/alpha + 2*mp.cos(alpha/2)/alpha**2
    J = -2*I2/alpha**2 + constant*I0
    c = I0**2/(I2+J)
    return 2 - 1/c

def Phi(E, m):
    E, m = mp.mpf(E), mp.mpf(m)
    thr = m/(m-1)
    return E if E <= thr else 2*mp.sqrt((m-1)*E/m) - 1 + E/m

def bound_from_eps(alpha, eps, m, psum):
    H = H_cosine(alpha)
    A = eps*(m-6); B = Phi(A, m); tau = psum*(m-6)/m
    return H, A, B, tau, (H-tau)/(1-B/m)

alpha = mp.mpf(149)/100
eps = mp.mpf(8065)/10**6          # EXACT rational 8065/1e6 (the certified frontier)
m = 133
psum = mp.mpf(1)/220              # pair-weight sum (P = 1/1320 is the mollifier parameter)
H, A, B, tau, bound = bound_from_eps(alpha, eps, m, psum)
record = mp.mpf("0.67326607914000068290279687189167079692373428880136")
print(f"H     = {mp.nstr(H, 50)}")
print(f"A     = {mp.nstr(A, 40)}  (eps*(m-6) = (8065/1e6)*127)")
print(f"tau   = {mp.nstr(tau, 40)}  = psum*(m-6)/m = (1/220)(127/133)")
print(f"B     = {mp.nstr(B, 40)}  = Phi_m(eps*127)")
print(f"bound = {mp.nstr(bound, 50)}")
print(f"record= {mp.nstr(record, 50)}")
print(f"HEADLINE MATCH (bound==record): {bound == record}")
print(f"residual: {mp.nstr(bound - record, 45)}")
# cross-check tau as rational (1/220)(127/133)
t1 = mp.mpf(1)/220 * mp.mpf(127)/133
print(f"tau rational direct = {mp.nstr(t1, 40)}, diff={mp.nstr(t1-tau, 30)}")
# eps sweep at m=133: bound monotone in eps (frontier context)
print("--- bound vs eps at m=133 (monotone check) ---")
for e in [0.00800, 0.00806, 0.008065, 0.00807, 0.00808, 0.00810, 0.00813, 0.00816]:
    _, _, _, _, b = bound_from_eps(alpha, mp.mpf(e), m, psum)
    print(f"eps={e}: bound={mp.nstr(b, 35)}")
