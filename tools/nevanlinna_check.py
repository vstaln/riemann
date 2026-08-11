#!/usr/bin/env python3
"""P8.1 probe: the (m1, m2) = (1, 4/3) truncated moment problem.

Checks:
  1. the two principal representations P- (2-point, symmetric) and P+ (atom at 0)
     of the Stieltjes moment problem with moments (1, 1, 4/3);
  2. the unique integer-marks {1,2} solution (2/3, 1/6) -- the certificate's extremal world;
  3. the integrality identity m2 = 2 - p1 for marks in {1,2} with sum of marks = N;
  4. the near-CUE 256-law's second moment m2 = 2 - p0 (p0 = 0.6818286874638...);
  5. the gap 0.6725 -> 0.6818 as a second-moment gap [2 - 1.3275, 2 - 1.3182];
  6. the Nevanlinna parametrization w(z) = (P(z)phi + R(z))/(Q(z)phi + S(z)):
     phi = 0 -> P-, phi = inf -> P+, general phi -> moments (1,1,4/3), Im w < 0;
  7. the marks-in-{1,2,3} one-parameter family (2/3+3t, 1/6-3t, t), t in [0,1/18];
  8. feasibility on [0,1] (m2 <= m1 there) -- the (1,4/3) pair is infeasible on [0,1].
"""
from fractions import Fraction as F
import mpmath as mp

mp.mp.dps = 50

print("=" * 72)
print("0. data from the notes (labels: PROVEN / CHECKED NUMERICALLY)")
print("=" * 72)

# p0: law's simple-point fraction, exact rational from LawN256.lean
p0_num = 10909258999421303588095230195816054408197
p0_den = 16000000000000000000000000000000000000000
p0 = F(p0_num, p0_den)
print("p0 (law simple-point fraction) =", float(p0), " =", mp.nstr(mp.mpf(p0_num)/mp.mpf(p0_den), 20))

# 1/c1* = 1/2 + (1/sqrt2) cot(1/sqrt2)  (attack-kernel, PROVEN)
th = 1/mp.sqrt(2)
c1inv = mp.mpf(1)/2 + (1/mp.sqrt(2))*mp.cot(1/mp.sqrt(2))
print("1/c1* = 1/2 + (1/sqrt2)cot(1/sqrt2) =", mp.nstr(c1inv, 20))
print("2 - 1/c1* =", mp.nstr(2 - c1inv, 20), "  (attack-kernel: 0.6725007036794116)")

# law's second moment from integrality identity m2 = 2 - p1 (marks in {1,2}, sum = N)
m2_law = 2 - p0
print("m2(law) = 2 - p0 =", float(m2_law), " =", mp.nstr(mp.mpf(2) - mp.mpf(p0_num)/mp.mpf(p0_den), 20))
print("2 - m2(law) = p0 =", float(p0))
print("gap in m2 units: 1/c1* - m2(law) =", mp.nstr(c1inv - (2 - mp.mpf(p0_num)/mp.mpf(p0_den)), 20))

print()
print("=" * 72)
print("1. two principal representations of the (1,1,4/3) Stieltjes problem")
print("=" * 72)

s3 = mp.sqrt(3)
# P-: masses 1/2 at 1 - 1/sqrt3, 1 + 1/sqrt3
xa, xb = mp.mpf(1) - 1/s3, mp.mpf(1) + 1/s3
print("P- atoms: 1 - 1/sqrt3 =", mp.nstr(xa, 12), ", 1 + 1/sqrt3 =", mp.nstr(xb, 12), " masses 1/2, 1/2")
# exact moment check: m0 = 1/2+1/2 = 1; m1 = (xa+xb)/2 = 1; m2 = (xa^2+xb^2)/2 = 4/3
m0m, m1m, m2m = mp.mpf(1), (xa+xb)/2, (xa*xa + xb*xb)/2
print("  P- moments (m0,m1,m2) =", mp.nstr(m0m,15), mp.nstr(m1m,15), mp.nstr(m2m,15), " (expect 1, 1, 4/3)")

# P+: masses 1/4 at 0, 3/4 at 4/3
print("P+ atoms: 0 (mass 1/4), 4/3 (mass 3/4)")
m0m2, m1m2, m2m2 = mp.mpf(1), mp.mpf(3)/4*mp.mpf(4)/3, mp.mpf(3)/4*(mp.mpf(4)/3)**2
print("  P+ moments (m0,m1,m2) =", mp.nstr(m0m2,15), mp.nstr(m1m2,15), mp.nstr(m2m2,15), " (expect 1, 1, 4/3)")
print("  on allowed grid {1,2}?  P-: NO (0.42265, 1.57735);  P+: NO (0, 1.33333)")

print()
print("=" * 72)
print("2. integer-marks-constrained problem: unique solution on {1,2}")
print("=" * 72)

# p1 + 2 p2 = 1 ; p1 + 4 p2 = 4/3  =>  p2 = 1/6, p1 = 2/3
p1, p2 = F(2,3), F(1,6)
print("p1 =", p1, " p2 =", p2, " total mass =", p1+p2, " empty =", 1-(p1+p2))
mom = {0: p1+p2, 1: p1 + 2*p2, 2: p1 + 4*p2, 3: p1 + 8*p2, 4: p1 + 16*p2}
for k in (1,2,3,4):
    print("  m%d = %s" % (k, mom[k]), " (float:", float(mom[k]), ")")
print("  P8.1 claimed m4 = 13/4 = 3.25 ; extremal-world m4 = 10/3 = 3.3333  -> MISMATCH, provenance unresolved")

print()
print("=" * 72)
print("3. integrality identity m2 = 2 - p1 (marks in {1,2}, sum of marks = N)")
print("=" * 72)
# symbolic check for arbitrary s simple, d double with s + 2d = N:
# m2 = (s + 4d)/N = (2N - s)/N = 2 - p1,  p1 = s/N
print("symbolic: s + 2d = N  =>  m2 = (s+4d)/N = 2 - s/N = 2 - p1   [PROVEN, trivial algebra]")
print("law: p1 = p0 =", float(p0), " => m2 = 2 - p0 =", float(m2_law))
print("extremal world: p1 = 2/3 => m2 = 4/3  (both satisfy the identity)")
print("=> the integrality identity does NOT exclude the law (the law satisfies it)")

print()
print("=" * 72)
print("4. the near-CUE 256-law's mark distribution (expected, per grid position)")
print("=" * 72)
p1_law = p0
p2_law = (1 - p0)/2   # d/256
p0_law = (1 - p0)/2   # empty positions: 1 - p1 - p2
print("simple fraction of zeros:", float(p1_law))
print("double positions d/256:", float(p2_law), "  empty positions:", float(p0_law))
m3_law = p1_law + 8*p2_law
m4_law = p1_law + 16*p2_law
print("law moments: m2 =", float(m2_law), " m3 =", float(m3_law), " m4 =", float(m4_law))
print("extremal-world moments: m2 = 4/3, m3 = 2, m4 = 10/3")
print("a third-moment inequality m3 >= 2 would exclude the law (m3 = %.5f), but is NOT provable" % float(m3_law))
print("   [paper 7.5(e): tr G^3 available only in Rudnick-Sarnak range k*lambda < 2, i.e. lambda < 2/3; odd moments do not lower Lambda_1(0)]")

print()
print("=" * 72)
print("5. the gap 0.6725 -> 0.6818 as a second-moment gap")
print("=" * 72)
print("certificate value v = 2 - C, C = second moment of the windowed operator (attack-multiplicity, PROVEN)")
print("  flat window : C = 4/3       -> v =", mp.nstr(2 - mp.mpf(4)/3, 16))
print("  opt. window : C = 1/c1*     -> v =", mp.nstr(2 - c1inv, 16))
print("  law's m2    : C = 2 - p0    -> v <= ", mp.nstr(mp.mpf(2) - (2 - mp.mpf(p0_num)/mp.mpf(p0_den)), 16), "= p0 (ceiling)")
print("closing the gap needs C(zeta) <= 2 - p0 =", mp.nstr(2 - mp.mpf(p0_num)/mp.mpf(p0_den), 12),
      " but C_min(zeta) = 1/c1* =", mp.nstr(c1inv, 12), " (PROVEN window optimum) > that.")

print()
print("=" * 72)
print("6. Nevanlinna parametrization of the truncated problem (1,1,4/3)")
print("=" * 72)

def w_of(z, phi):
    # w(z) = ((3z-1) phi(z) + (z-1)) / ((3z^2-4z) phi(z) + (z^2 - 2z + 2/3))
    num = (3*z - 1)*phi + (z - 1)
    den = (3*z*z - 4*z)*phi + (z*z - 2*z + mp.mpf(2)/3)
    return num/den

# phi = 0 -> P-, phi = inf -> P+
z = mp.mpf(3) + mp.mpf(2)*1j
print("phi=0  : w(z) =", mp.nstr(w_of(z, mp.mpf(0)), 15))
print("         1/(z-x) averaged vs P- :", mp.nstr(mp.mpf(1)/2/(z-xa) + mp.mpf(1)/2/(z-xb), 15))
print("phi->inf: w(z) =", mp.nstr((3*z-1)/(3*z*z-4*z), 15),
      " P+ :", mp.nstr(mp.mpf(1)/4/z + mp.mpf(3)/4/(z - mp.mpf(4)/3), 15))

# moments from asymptotics for various phi: w(z) ~ m0/z + m1/z^2 + m2/z^3
for name, phi_fun in [("phi = c (c=1)", lambda z: mp.mpf(1)),
                      ("phi = c (c=-2)", lambda z: mp.mpf(-2)),
                      ("phi = z", lambda z: z),
                      ("phi = 1/z", lambda z: 1/z),
                      ("phi = z/(z^2+1)", lambda z: z/(z*z+1))]:
    zz = mp.mpf(10) + mp.mpf(7)*1j   # large |z| for the asymptotic read
    wv = w_of(zz, phi_fun(zz))
    # read moments: m0 = z*w, m1 = z*(z*w - m0), ...
    m0 = zz*wv
    m1 = zz*(zz*wv - m0)
    m2 = zz*(zz*(zz*wv - m0) - m1)
    imw = mp.im(w_of(mp.mpf(2)+mp.mpf(1)*1j, phi_fun(mp.mpf(2)+mp.mpf(1)*1j)))
    print("%-18s m0=%s m1=%s m2=%s  Im w(2+i)=%s" % (
        name, mp.nstr(m0,6), mp.nstr(m1,6), mp.nstr(m2,6), mp.nstr(imw,6)))

print()
print("=" * 72)
print("7. marks in {1,2,3}: one-parameter family with fixed (1, 4/3)")
print("=" * 72)
# p1 = 2/3 + 3t, p2 = 1/6 - 3t, p3 = t, t in [0, 1/18]
for t_ in [F(0), F(1,36), F(1,18)]:
    p1t = F(2,3) + 3*t_
    p2t = F(1,6) - 3*t_
    p3t = t_
    m1 = p1t + 2*p2t + 3*p3t
    m2 = p1t + 4*p2t + 9*p3t
    print("t = %s : (p1,p2,p3) = (%s, %s, %s)  m1 = %s m2 = %s" % (
        t_, p1t, p2t, p3t, m1, m2))

print()
print("=" * 72)
print("8. feasibility on [0,1]")
print("=" * 72)
print("for ANY measure on [0,1]: x^2 <= x  =>  m2 <= m1.  (1, 4/3) has m2 > m1.")
print("=> the (1,4/3) moment pair is INFEASIBLE on [0,1]; the problem lives on the")
print("   multiplicity space [1,2] (marks) / [0, inf) (Stieltjes). 'on [0,1]' is a phantom constraint.")

print()
print("=" * 72)
print("9. P8.1 stated GUE sequence (1, 4/3, 2, 13/4): Stieltjes positivity")
print("=" * 72)
# Hankel determinants: H0 = m0 = 1; H1 = m0 m2 - m1^2; H2 = det[[m0,m1,m2],[m1,m2,m3],[m2,m3,m4]]
m0_, m1_, m2_, m3_, m4_ = 1, 1, F(4,3), 2, F(13,4)
H1 = m0_*m2_ - m1_**2
H2 = m0_*(m2_*m4_ - m3_**2) - m1_*(m1_*m4_ - m3_*m2_) + m2_*(m1_*m3_ - m2_**2)
sH1 = m1_*m3_ - m2_**2   # Stieltjes: det [[m1,m2],[m2,m3]]
sH2 = m2_*m4_ - m3_**2   # det [[m2,m3],[m3,m4]]
print("H1 =", H1, " H2 =", H2, " (Hamburger), Stieltjes dets:", sH1, sH2, "-> all positive: valid Stieltjes sequence")
print("but extremal-world submeasure gives m4 = 10/3, not 13/4: P8.1 m4 provenance UNRESOLVED.")
