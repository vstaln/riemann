"""Verify the pair identity E = sum_pairs |F(rho) - F(1-rhobar)|^2 and the M3 constants.

E := sum_{rho} F(rho)[F(rhobar) - F(1-rho)]  (BHB off-line correction, F real-coeff)
Pairing: rho <-> 1-rhobar  (involution on the zero multiset; for zeta: FE symmetry)
Claim (PROVEN algebraically in note): E = sum_{pairs} |F(rho) - F(1-rhobar)|^2 >= 0.
"""
import random, cmath, math
from fractions import Fraction as Fr

random.seed(20260814)

def Fval(coefs, z):
    # real-coefficient polynomial: sum c_k z^k
    return sum(c * (z**k) for k, c in enumerate(coefs))

for trial in range(20):
    deg = random.randint(2, 6)
    coefs = [random.uniform(-2, 2) for _ in range(deg + 1)]
    npairs = random.randint(2, 6)
    pts = []           # closed under rho -> 1-rhobar (conjugation closure not required)
    for _ in range(npairs):
        b = random.uniform(0.05, 0.95)   # beta
        g = random.uniform(0.5, 10.0)    # gamma > 0
        z1 = complex(b, g)
        z2 = complex(1 - b, g)           # 1 - conj(z1)
        pts += [z1, z2]
    # LHS: E = sum F(rho)[F(rhobar) - F(1-rho)]
    E = 0j
    for z in pts:
        E += Fval(coefs, z) * (Fval(coefs, z.conjugate()) - Fval(coefs, 1 - z))
    # RHS: sum over pairs |F(rho) - F(1-rhobar)|^2
    R = 0.0
    for i in range(0, len(pts), 2):
        z = pts[i]
        R += abs(Fval(coefs, z) - Fval(coefs, 1 - z.conjugate()))**2
    assert abs(E.imag) < 1e-9 * max(1.0, abs(E.real)), (trial, E)          # E must be real
    assert abs(E.real - R) < 1e-9 * max(1.0, abs(E.real)), (trial, E.real, R)  # identity holds
    assert E.real >= -1e-9                          # E >= 0
print("pair identity E = sum_pairs |F(rho)-F(1-rhobar)|^2 : HOLDS on 20 random trials (real F, symmetric zero sets)")

# --- constants ---
r = Fr(99, 1274)                      # r = 99/1274
rp = Fr(3, 5)                         # r' = 3/5 (zeta''-moment ratio, claim from companion note)
rsum = r + rp
slack = Fr(1) - Fr(6818, 10000) * Fr(27, 19)   # 3.11% slack (matches check_bhb_arithmetic)
print("slack:", float(slack))

# triangle-form box (old): b_tri = slack/(2*sqrt(2*(r+r')))
b_tri = slack / (2 * math.sqrt(2 * float(rsum)))
# pair-form box (new): E/S2 <= 8 b^2 (r+r') -> b_pair = sqrt(slack/(8*(r+r')))
b_pair = math.sqrt(float(slack) / (8 * float(rsum)))
print(f"b_triangle = {float(b_tri):.6f}   b_pair = {float(b_pair):.6f}   ratio = {float(b_tri)/b_pair:.2f}")

# zeta''-only pair box (r' only, sanity): b = sqrt(slack/(8 r'))
b_rp = math.sqrt(float(slack) / (8 * float(rp)))
print(f"b_pair (zeta''-only) = {b_rp:.6f}")

# GM threshold: 15(1-sigma)/(3+5sigma) < 1/2 at sigma = 1/2+Delta
# 15(1/2-D) < (11/2+5D)/2  <=>  D > 19/70
D_thr = Fr(19, 70)
print("GM right-tail threshold Delta >", float(D_thr), "= 19/70")
for D in [0.27, 19/70, 0.28, 0.30]:
    s = 0.5 + D
    if 0.7 <= s <= 0.8:
        exp = 15*(1-s)/(3+5*s)
    else:
        exp = 30*(1-s)/13
    print(f"  Delta={D:.3f} sigma={s:.3f} GM exponent={exp:.4f} vs 1/2: {'OK' if exp < 0.5 else 'FAIL'}")

# uniform 30/13 threshold: c(1/2-D) < 1/2 <=> D > (c-1)/(2c), c=30/13
c = Fr(30, 13)
D_uniform = (c - 1) / (2 * c)
print("uniform (1.4) threshold Delta >", float(D_uniform), "= 17/60")
print("ALL CHECKS PASS")
