#!/usr/bin/env python3
"""Certificate arithmetic for the third-moment attack (attack-thirdmoment.md).
Corrected moment values (verified: tools/m3_adjudicate.py, tools/m4_adjudicate.py):
  m2(lam) = 1/lam + lam/3
  m3(lam) = 3 + 3/lam + 1/lam^2 - lam - 6*J2(lam)*(1+1/lam),  J2 = int0^inf sinc(pi la u)^2 sinc(pi u)^2 du
  m2(1)=4/3, m3(1)=2, m2(2/3)=31/18, m3(2/3)=13/4, m2(1/2)=13/6, m3(1/2)=5
Cubic-weight certificate (paper 7.5(g)): N_d >= (1/2 + (2m2-m3)/18)N + (4/9) N_s
with s1/N = 2/3 (Thm A), 0.6725007 (Thm D), 19/27 (RH, BHB13).
"""
from fractions import Fraction as F

def cert(m2, m3, s1):
    return F(1,2) + (2*m2 - m3)/18 + F(4,9)*s1

print("2m2-m3 values:")
for la, m2, m3 in [(F(1,2), F(13,6), 5), (F(2,3), F(31,18), F(13,4)), (F(3,4), None, None), (1, F(4,3), 2)]:
    if m2 is None:
        continue
    print(f"  lam={la}: 2m2-m3 = {2*m2-m3} = {float(2*m2-m3):.6f}")

print("\nCertificate N_d/N:")
for (la, m2, m3) in [(F(2,3), F(31,18), F(13,4)), (1, F(4,3), 2)]:
    for name, s1 in [("ThmA 2/3", F(2,3)), ("ThmD 0.6725", F(6725007,10000000)), ("RH 19/27", F(19,27))]:
        c = cert(m2, m3, s1)
        print(f"  lam={la}: {name:14s}: N_d/N >= {float(c):.6f}")
    print()

print("wall: 5/6 =", float(F(5,6)))
print("two-moment values: C(1)=4/3 -> simple 2-C =", float(2-F(4,3)), "; distinct (3-C)/2 =", float((3-F(4,3))/2))
