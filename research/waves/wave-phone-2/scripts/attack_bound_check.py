#!/usr/bin/env python3
"""attack_bound_check.py -- adversarial re-derivation of tau, B, bound at m=133
from the discovery note formula. CHECKED NUMERICALLY (mpmath 120+ digits)."""
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
eps = mp.mpf(8060)/10**6
m = 133
psum = mp.mpf(1)/220
H, A, B, tau, bound = bound_from_eps(alpha, eps, m, psum)
target = mp.mpf("0.673262865534356014645368000853343519319712248")
print(f"H     = {mp.nstr(H, 50)}")
print(f"A     = {mp.nstr(A, 40)}  (eps*(m-6) = 8060/1e6 * 127)")
print(f"tau   = {mp.nstr(tau, 40)}  = psum*(m-6)/m = (1/220)(127/133)")
print(f"B     = {mp.nstr(B, 40)}  = Phi_m(eps*127)")
print(f"bound = {mp.nstr(bound, 50)}")
print(f"target= {mp.nstr(target, 50)}")
print(f"match = {mp.nstr(bound - target, 45)} (should be 0)")
print(f"HEADLINE MATCH: {bound == target}")
# cross-check tau as rational (1/220)(127/133)
t1 = mp.mpf(1)/220 * mp.mpf(127)/133
print(f"tau rational direct = {mp.nstr(t1, 40)}, diff={mp.nstr(t1-tau, 30)}")
# eps sweep at m=133: bound monotone in eps?
print("--- bound vs eps at m=133 (monotone check) ---")
for e in [0.00800, 0.00806, 0.008065, 0.00807, 0.00808, 0.00810, 0.00813, 0.00816]:
    _, _, _, _, b = bound_from_eps(alpha, mp.mpf(e), m, psum)
    print(f"eps={e}: bound={mp.nstr(b, 35)}")
