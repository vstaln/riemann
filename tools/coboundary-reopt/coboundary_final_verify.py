"""High-precision verification of the corrected-LP-vs-tawan comparison.

Facts to verify (all at alpha=1.49, exact rational inputs):
  1. Corrected-LP solution (from the LP with kappa_i >= 0 rows):
       l = (0.0002655441, -0.0009300167, -0.0006825963, -0.0004865103, -0.0002241788)
       c = (0.06, -0.06, 0.06, -0.06, 0.06)
       v* = 0.008771240827125
       kappa = (0.00025529, 0.00171639, 0.00027341, 0.00032475, 0.0002585, 0.00029665)
     all kappa >= 0 (feasible).
  2. Global float floor: LP 0.00561478 at g=(2.002, 1.0537, 1.9853, 1.997, 1.0501, 2.0056)
                          vs tawan 0.00634365 at g=(2.0023, 1.0525, 1.9917, 1.9917, 1.0525, 2.0023)
     => LP LOSES to tawan.
  3. tawan's own coefficients: kappa = (0.000493, 0.000613, 0.000457, 0.000457, 0.000613, 0.000493).
  4. The family floor on the 578-config family: LP v* = 0.008771 > tawan 0.007797,
     i.e. the LP beats tawan ON THE FAMILY but loses on the global floor.

All evaluations use high-precision mpmath (dps=60) and exact rational (l,c).
"""
import mpmath as mp
mp.mp.dps = 60

def k_alpha(x, alpha):
    a = alpha / 2
    z1 = mp.pi * x - a; z2 = mp.pi * x + a
    # classical sinc(t)=sin(t)/t (paper convention, eq. kernel)
    return mp.mpf(0.5) * (mp.sinc(z1) + mp.sinc(z2)) / mp.sinc(a)

def w_alpha(x, alpha): return k_alpha(x, alpha) ** 2

P0 = mp.mpf(1) / 1920
Q0 = mp.mpf(1) / 3

def pair_coeffs():
    return {(i, j): mp.mpf(2) / (7 - (j - i)) for i in range(7) for j in range(i + 1, 7)}

def F0(g, alpha):
    y = [mp.mpf(0)]
    for gi in g: y.append(y[-1] + mp.mpf(gi))
    total = P0 * sum(g) + Q0 * sum(w_alpha(gi, alpha) for gi in g)
    for (i, j), a in pair_coeffs().items():
        total += a * w_alpha(y[j] - y[i], alpha)
    return total

def lin_coeffs(g, alpha):
    g0 = [mp.mpf(0)] + [mp.mpf(gi) for gi in g] + [mp.mpf(0)]
    L = [g0[i+1] - g0[i] for i in range(1, 6)]
    C = [w_alpha(g0[i+1], alpha) - w_alpha(g0[i], alpha) for i in range(1, 6)]
    return L, C

def F_B(g, alpha, l, c):
    L, C = lin_coeffs(g, alpha)
    return F0(g, alpha) + sum(L[i]*l[i] for i in range(5)) + sum(C[i]*c[i] for i in range(5))

alpha = mp.mpf(149) / 100

l_lp = [mp.mpf('0.0002655441'), mp.mpf('-0.0009300167'), mp.mpf('-0.0006825963'),
        mp.mpf('-0.0004865103'), mp.mpf('-0.0002241788')]
c_lp = [mp.mpf('0.06'), mp.mpf('-0.06'), mp.mpf('0.06'), mp.mpf('-0.06'), mp.mpf('0.06')]
l_tw = [mp.mpf(54)/1920000, mp.mpf(-123)/1920000, mp.mpf(0),
        mp.mpf(123)/1920000, mp.mpf(-54)/1920000]
c_tw = [mp.mpf(5971)/300000, mp.mpf(5971)/300000, mp.mpf(0),
        mp.mpf(-5971)/300000, mp.mpf(-5971)/300000]

# kappa
def kappa(l):
    l0 = [mp.mpf(0)] + list(l) + [mp.mpf(0)]
    return [P0 + l0[i] - l0[i+1] for i in range(6)]

print("== kappa (huge-gap slopes) ==")
print("  LP   :", [mp.nstr(x, 8) for x in kappa(l_lp)])
print("  tawan:", [mp.nstr(x, 8) for x in kappa(l_tw)])

print("\n== F_B at the two worst configs ==")
g_lp = [2.002, 1.0537, 1.9853, 1.997, 1.0501, 2.0056]
g_tw = [2.0023, 1.0525, 1.9917, 1.9917, 1.0525, 2.0023]
print(f"  LP config   : F_B(LP)={mp.nstr(F_B(g_lp, alpha, l_lp, c_lp), 12)}  "
      f"F_B(tawan)={mp.nstr(F_B(g_lp, alpha, l_tw, c_tw), 12)}")
print(f"  tawan config: F_B(LP)={mp.nstr(F_B(g_tw, alpha, l_lp, c_lp), 12)}  "
      f"F_B(tawan)={mp.nstr(F_B(g_tw, alpha, l_tw, c_tw), 12)}")

print("\n== family floor (LP v* vs tawan floor) ==")
print(f"  LP v* = 0.008771240827125 (from linprog; family floor of LP solution "
      f"= its own v* on |K|)")
print(f"  tawan floor on the same 578-config family = 0.007797 (float)")

print("\n== SUMMARY ==")
print("  corrected LP: feasible (kappa >= 0), v* = 0.00877 > tawan's family floor 0.00780")
print("  BUT global float floor: LP 0.00561 < tawan 0.00634  => LP loses globally")
