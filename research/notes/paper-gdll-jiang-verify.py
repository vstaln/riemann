#!/usr/bin/env python3
"""paper-gdll-jiang-verify.py
Cross-checks for research/notes/paper-gdll-jiang.md.

Verifies (all mpmath, high precision):
  1. Theorem D clean constant: 3/2 - (1/sqrt(2))*cot(1/sqrt(2)) = 0.672500703679...
  2. GdLL pair-kernel (n=2, m=1) constant: c_{2,1} = 1/K(0,0), K(0,0) =
     1/( (1/sqrt(2))*cot(1/sqrt(2)) - (2*1-1)/(2*1) ); check 1 - c_{2,1} equals
     the Theorem D constant (i.e. 0.6725 = 2 - (1 + c_{2,1})).
  3. GdLL Theorem 1 arithmetic: Z_n/N >= 1 - c_{n,m}/(n-1)! with
     c_{3,1}=0.077197284 (Table 1, deg 60), c_{3,2}=1.400506625 (Table 2, d=5),
     c_{4,1}=447/3500 (Section 6) -> 0.9614 / 0.2997 / 0.9787.
  4. GdLL N_3 bound (6): N_3/N <= 1 + 3*c_{2,1} + c_{3,1} = 2.0597.
  5. Under-RH pair-SDP N* bound cited in GdLL: c = 1.3208 [9,8] ->
     simple fraction >= 2 - 1.3208 = 0.6792 (conditional only).
  6. 0.9614 > 0.955 (CGG 95.5% simple-or-double, [12]) and 0.6792 > 0.6725.
  7. Jiang Theorem 1.3 barrier exponent: sigma >= 1 - 1/(n^2+1) (n=1: 1/2).

Command: uv run --quiet --with mpmath python paper-gdll-jiang-verify.py
Labels: PROVEN (exact algebra / direct arithmetic) — numbers quoted from the
papers are marked VERIFIED-FROM-PAPER in the note; this script only checks the
arithmetic derivations built on those quoted values.
"""
import mpmath as mp
mp.mp.dps = 60

sq2 = mp.sqrt(2)
clean = mp.mpf(3)/2 - (1/sq2) * mp.cot(1/sq2)
print("1. clean constant 3/2 - (1/sqrt2)cot(1/sqrt2)      =", mp.nstr(clean, 20))

# 2. GdLL n=2 kernel (Section 3, m=1): K(0,0) = 1/( (1/sqrt2) cot(1/sqrt2) - 1/2 )
K00_inv = (1/sq2) * mp.cot(1/sq2) - mp.mpf(1)/2   # this is 1/K(0,0) = c_{2,1}
c21 = K00_inv
print("2. c_{2,1} = 1/K(0,0)                            =", mp.nstr(c21, 20))
print("   1 - c_{2,1}                                   =", mp.nstr(1 - c21, 20))
print("   diff vs clean constant                        =", mp.nstr((1 - c21) - clean, 20))
assert abs((1 - c21) - clean) < mp.mpf("1e-50")
print("   => 0.6725 = 2 - (1 + c_{2,1}) = 1 - c_{2,1}  : MATCH (same constant)")

# 3. Theorem 1 arithmetic
c31 = mp.mpf("0.077197284")     # Table 1, degree 60 (VERIFIED-FROM-PAPER value)
c32 = mp.mpf("1.400506625")     # Table 2, d=5 (VERIFIED-FROM-PAPER value)
c41 = mp.mpf(447)/3500          # Section 6 (VERIFIED-FROM-PAPER value)
z31 = 1 - c31/mp.factorial(2)
z32 = 1 - c32/mp.factorial(2)
z41 = 1 - c41/mp.factorial(3)
print("3. (3,1): Z_3/N >= 1 - c31/2!  =", mp.nstr(z31, 10), " (paper: 0.9614)")
print("   (3,2): Z_3/N >= 1 - c32/2!  =", mp.nstr(z32, 10), " (paper: 0.2997)")
print("   (4,1): Z_4/N >= 1 - c41/3!  =", mp.nstr(z41, 10), " (paper: 0.9787)")

# 4. N_3 bound (6): N_3 = M_1 + 3 M_2 + M_3, limsup M_2/N <= c_{2,1}, M_3/N <= c_{3,1}
n3 = 1 + 3*c21 + c31
print("4. N_3/N <= 1 + 3*c21 + c31    =", mp.nstr(n3, 10), " (paper: 2.0597)")

# 5. Under-RH N* bound cited in GdLL (Section 1, [8,9,26,27]): c = 1.3208
c_star = mp.mpf("1.3208")
simple_rh = 2 - c_star
print("5. under-RH simple >= 2 - 1.3208 =", mp.nstr(simple_rh, 10), " (conditional only)")

# 6. comparisons
print("6. 0.9614 > 0.955 (CGG 95.5%):", z31 > mp.mpf("0.955"),
      "| 0.6792 > 0.6725:", simple_rh > clean)

# 7. Jiang barrier exponent
for n in [1, 2, 4]:
    print(f"7. Jiang Thm 1.3 sigma-barrier n={n}: sigma >= 1 - 1/(n^2+1) =",
          mp.nstr(1 - mp.mpf(1)/(n*n + 1), 10))
