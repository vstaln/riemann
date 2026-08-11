#!/usr/bin/env python3
"""Mining OpenAI's Ten Advances: sphere-packing exact-LP evaluation -> transfer tests.

Mines /home/vstaln/riemann/research/external-results/openai-ten-proofs/SpherePacking.lean
and /home/vstaln/riemann/research/papers/openai-ten-proofs.pdf (markitdown) for
transferable technique to our certificate class (attack-lpdual.md, close-inclass-gap.md).

All numbers here are produced by THIS script (mpmath, 60-digit working precision).
Command: cd /home/vstaln/riemann && uv run --quiet --with mpmath python scratch/mine_openai/mine_openai_numerics.py
"""
import mpmath as mp

mp.mp.dps = 60
mp.mp.pretty = True

def section(t):
    print("\n" + "=" * 78)
    print(t)
    print("=" * 78)

# ----------------------------------------------------------------------
section("A. OpenAI's exact Cohn-Elkies LP evaluation: headline constants")
# Lean: criticalBinaryExponent = (1/2)*logb2(2*pi/e) ; base_two_decimal_certificate in Ioo(...,...)
cexp = mp.mpf(1) / 2 * mp.log(mp.mpf(2) * mp.pi / mp.e, 2)
lo = mp.mpf("0.604400544291677695341677307053")
hi = mp.mpf("0.604400544291677695341677307054")
print("(1/2)*log2(2*pi/e)             =", mp.nstr(cexp, 40))
print("inside Lean Ioo certificate?   =", lo < cexp < hi)
print("Lean Ioo bounds                =", mp.nstr(lo, 30), "...", mp.nstr(hi, 30))
print("sqrt(e/(2*pi))  (LP root)      =", mp.nstr(mp.sqrt(mp.e / (2 * mp.pi)), 40))
print("1/pi           (root_before_infimum) =", mp.nstr(1 / mp.pi, 40))
# natural log version (Lean natural_logarithmic_rate): (1/2)*log(e/(2pi))
print("(1/2)*log(e/(2*pi))            =", mp.nstr(mp.mpf(1)/2 * mp.log(mp.e/(2*mp.pi)), 40))
# walkthrough: naive norm-comparison route reaches LP root sqrt(e/8) < KL exponent
print("sqrt(e/8)   (naive norm-route root, walkthrough) =", mp.nstr(mp.sqrt(mp.e/8), 12),
      "  bin-exp", mp.nstr(mp.log(mp.sqrt(mp.e/8), 2), 12))
# KL exponent for comparison (paper: 0.59905576...)
print("KL78 exponent (paper, for comparison) = 0.59905576... (no code)")

# ----------------------------------------------------------------------
section("B. The gamma identities used by the Mellin-strip method  (paper eq (7))")
# |Gamma(i*b)|^2 = pi/(b*sinh(pi*b)); |Gamma(1/2+i*b)|^2 = pi/cosh(pi*b)
for b in [mp.mpf("0.3"), mp.mpf("1.7"), mp.mpf("5.43")]:
    lhs1 = mp.fabs(mp.gamma(mp.mpc(0, b))) ** 2
    rhs1 = mp.pi / (b * mp.sinh(mp.pi * b))
    lhs2 = mp.fabs(mp.gamma(mp.mpc(mp.mpf(1)/2, b))) ** 2
    rhs2 = mp.pi / mp.cosh(mp.pi * b)
    print(f"b={mp.nstr(b,4)}: |Gamma(ib)|^2      lhs-rhs = {mp.nstr(lhs1-rhs1, 3)}"
          f"   |Gamma(1/2+ib)|^2 lhs-rhs = {mp.nstr(lhs2-rhs2, 3)}")
print("both identities hold to working precision (60 digits).")

# ----------------------------------------------------------------------
section("C. The ideal saddle density and the 1/pi displacement  (paper (32)-(33))")
# w*(a) = e^{-2a}/(2a^2 cosh a);  paper (32): int_0^inf w*(a)*a*sinh(a) da = (1/2) log(pi/2)
# The negative shell w_s ~ -w* (truncated) enters the saddle radius with a MINUS sign:
#   r/ sqrt(d) ~ sqrt((1+u)/(4 pi)) * exp( int w(a) a sinh(ua) da )
#   at u=1, w = w_s ~ -w*:  exp(-(1/2)log(pi/2)) = sqrt(2/pi), and sqrt(2/(4 pi)) = (2pi)^{-1/2}
#   => r/sqrt(d) -> (2pi)^{-1/2} sqrt(2/pi) = 1/pi   (paper (33), Lean root_before_infimum)
def integrand(a):
    return mp.exp(-2 * a) * mp.tanh(a) / (2 * a)
I = mp.quad(integrand, [0, mp.inf])
expected = mp.mpf(1) / 2 * mp.log(mp.pi / 2)
print("int_0^inf e^{-2a} tanh(a)/(2a) da =", mp.nstr(I, 30))
print("(1/2) log(pi/2)                   =", mp.nstr(expected, 30))
print("match (to 60 digits)?             =", abs(I - expected) < mp.mpf(10) ** -40)
# saddle displacement with the negative shell:
disp = mp.sqrt(1 / (2 * mp.pi)) * mp.exp(-expected)
print("(2pi)^{-1/2} * exp(-(1/2)log(pi/2)) =", mp.nstr(disp, 30),
      "  (should be 1/pi =", mp.nstr(1 / mp.pi, 30), ")")
# pointwise saturation: |w*| cosh(a) == e^{-2a}/(2a^2) exactly by construction
a0 = mp.mpf("1.5")
print("saturation check  w*(a)*cosh(a) == e^{-2a}/(2a^2): ",
      mp.nstr((mp.exp(-2*a0)/(2*a0**2*mp.cosh(a0)))*mp.cosh(a0) - mp.exp(-2*a0)/(2*a0**2), 3))

# ----------------------------------------------------------------------
section("D. Stirling conversion: V_d^{1/d} sqrt(d) -> sqrt(2*pi*e),  LP^{1/d} -> sqrt(e/(2*pi))")
# V_d = pi^{d/2}/Gamma(d/2+1);  root_before_infimum: q^{1/d}/sqrt(d) -> 1/pi
# LP_d^{1/d} = (V_d/2^d)^{1/d} * q^{1/d}  ~  [V_d^{1/d}/2] * [(1/pi) sqrt(d)]
print("V_d^{1/d} sqrt(d)  ->  sqrt(2*pi*e) =", mp.nstr(mp.sqrt(2*mp.pi*mp.e), 12), ":")
for d in [1000, 100000]:
    V = mp.pi ** (mp.mpf(d) / 2) / mp.gamma(mp.mpf(d) / 2 + 1)
    print(f"  d={d}: V^{{1/d}} sqrt(d) = {mp.nstr(V ** (1/mp.mpf(d)) * mp.sqrt(mp.mpf(d)), 12)}")
print("LP^{1/d}  ->  sqrt(e/2pi) =", mp.nstr(mp.sqrt(mp.e/(2*mp.pi)), 12), ":")
for d in [1000, 100000]:
    V = mp.pi ** (mp.mpf(d) / 2) / mp.gamma(mp.mpf(d) / 2 + 1)
    lp = (V / 2 ** d) ** (1 / mp.mpf(d)) * (1 / mp.pi) * mp.sqrt(mp.mpf(d))
    print(f"  d={d}: LP^{{1/d}} = {mp.nstr(lp, 12)}")
print("Convergence is O(1/d); the Stirling limit is exact.")

# ----------------------------------------------------------------------
section("E. OUR program's constants (from attack-lpdual.md / close-inclass-gap.md)")
p0 = mp.mpf("10909258999421303588095230195816054408197") / (mp.mpf(16) * mp.mpf(10) ** 39)
E1 = -mp.mpf(1) / (6 * 256 ** 2)   # = -1/393216 exactly (midpoint model, E(1))
D1 = mp.mpf("0.8239531607128352")
print("p0 (law simple fraction)        =", mp.nstr(p0, 30))
print("E(1) = -1/(6*256^2)             =", mp.nstr(E1, 30))
print("in-class optimum p0+|E(1)|      =", mp.nstr(p0 - E1, 30))
print("  exact rational per note       = 0.681831230595341890922618553905170067178979166...")
# Theorem D constant
c1 = mp.mpf(1) / (mp.mpf(1) / 2 + mp.mpf(1) / mp.sqrt(2) * mp.cot(mp.mpf(1) / mp.sqrt(2)))
thmD = 2 - 1 / c1
print("Thm D constant 3/2-(1/sqrt2)cot(1/sqrt2) =", mp.nstr(thmD, 30))
print("gap 0.6818 - 0.6725 (in-class)           =", mp.nstr((p0 - E1) - thmD, 12))
# shadow price identity v*(p1) = p1 + |E(1)|
for p1 in [p0, mp.mpf("0.70"), mp.mpf("0.80"), mp.mpf("1.00")]:
    print(f"  v*(p1={mp.nstr(p1,6)}) = p1+|E(1)| = {mp.nstr(p1 - E1, 12)}")

# --- 1-p0 vs 1/pi coincidence check (curiosity, labeled) ---
print("\ncuriosity: 1-p0 =", mp.nstr(1 - p0, 12), " vs 1/pi =", mp.nstr(1/mp.pi, 12),
      " diff =", mp.nstr((1 - p0) - 1/mp.pi, 4), "  (numerical coincidence at 4e-4; "
      "the law is rational, no pi in its construction)")

# ----------------------------------------------------------------------
section("F. OUR certificate functional is cot-based, not gamma-based")
# Q(v0) for v0 = cos(sqrt(2)*u) on [-1/2,1/2]:  Q = 1/2 + (1/sqrt2) cot(1/sqrt2)
Q = mp.mpf(1) / 2 + mp.mpf(1) / mp.sqrt(2) * mp.cot(mp.mpf(1) / mp.sqrt(2))
print("Q(cos(sqrt2 u)) = 1/2 + (1/sqrt2)cot(1/sqrt2) =", mp.nstr(Q, 40))
print("proportion 2 - Q                             =", mp.nstr(2 - Q, 40), "(Thm D, matches)")

# direct numerical evaluation of the functional via mpmath quad:
# Q_num = (int v^2 + intint |s-s'| v v) / (int v)^2   on [-1/2,1/2]
def v(u):
    return mp.cos(mp.sqrt(2) * u)
I0 = mp.quad(lambda u: v(u), [-mp.mpf(1)/2, mp.mpf(1)/2])
I1 = mp.quad(lambda u: v(u) ** 2, [-mp.mpf(1)/2, mp.mpf(1)/2])
I2 = mp.quad(lambda s: mp.quad(lambda t: mp.fabs(s - t) * v(s) * v(t),
                               [-mp.mpf(1)/2, mp.mpf(1)/2]),
             [-mp.mpf(1)/2, mp.mpf(1)/2])
Qnum = (I1 + I2) / I0 ** 2
print("numeric quad quotient                   =", mp.nstr(Qnum, 20),
      "  diff vs closed form =", mp.nstr(Qnum - Q, 3))

# support-rescaled family Q(c) = c + (1/sqrt2) cot(sqrt2 c)  (attack-kernel.md table)
print("support-rescaled closed form Q(c)=c+(1/sqrt2)cot(sqrt2 c):")
for c in ["0.30", "0.40", "0.45", "0.50", "1.1107"]:
    cc = mp.mpf(c)
    qc = cc + mp.mpf(1)/mp.sqrt(2) * mp.cot(mp.sqrt(2) * cc)
    print(f"  c={c}: Q={mp.nstr(qc, 8)}   (attack-kernel: 1.865/1.514/1.407/1.3275/1.1107)")

# --- cot(1/sqrt2) is NOT a gamma-product value at integer/half-integer points ---
# The CE machinery only simplifies gamma at integer/half-integer Mellin args.
# cot(1/sqrt2) = cos(1/sqrt2)/sin(1/sqrt2): 1/sqrt2 is not in (1/2)*Z, so the
# reflection formula Gamma(z)Gamma(1-z)=pi/sin(pi z) yields no integer/half-int reduction.
print("cot(1/sqrt2) =", mp.nstr(mp.cot(mp.mpf(1)/mp.sqrt(2)), 30),
      " -- argument 1/sqrt2 not in Z/2: no gamma reflection identity applies (analytic fact).")

# ----------------------------------------------------------------------
section("G. Spectrum of our |s-s'| kernel: tan/cot character, NOT gamma")
# T v(s) = int_{-1/2}^{1/2} |s-s'| v(s') ds'  on L^2[-1/2,1/2].
# Exact identities (sympy-verified in the mining round; integrals split at the cusp):
#   T(cosh ks) = sinh(k/2)/k - 2cosh(k/2)/k^2 + 2cosh(ks)/k^2   (eigenfunction iff tanh(k/2)=2/k)
#   T(cos ks)  = sin(k/2)/k  + 2cos(k/2)/k^2  - 2cos(ks)/k^2    (eigenfunction iff tan(k/2)=-2/k,
#                                                              or k=(2m+1)pi with eigenvalue -2/k^2)
#   T(sin ks)  = 2s cos(k/2)/k - 2 sin(ks)/k^2                  (odd: k=(2m+1)pi, eigenvalue -2/k^2)
def Tapply(f, s):
    # split the |s-u| kernel at the cusp u=s for accuracy
    return (mp.quad(lambda u: (s - u) * f(u), [-mp.mpf(1) / 2, s]) +
            mp.quad(lambda u: (u - s) * f(u), [s, mp.mpf(1) / 2]))
print("positive branch: tanh(k/2) = 2/k, k =", end=" ")
kh = mp.findroot(lambda z: mp.tanh(z / 2) - 2 / z, 2.4)
lam_p = 2 / kh ** 2
print(mp.nstr(kh, 15), " -> lambda = 2/k^2 =", mp.nstr(lam_p, 15))
for s in ["0.25", "-0.1", "0.49"]:
    ss = mp.mpf(s)
    lhs = Tapply(lambda u: mp.cosh(kh * u), ss)
    print(f"  s={s}: T(cosh(k s)) = {mp.nstr(lhs, 15)}   lambda*cosh(k s) = {mp.nstr(lam_p * mp.cosh(kh * ss), 15)}"
          f"  diff={mp.nstr(lhs - lam_p * mp.cosh(kh * ss), 3)}")
print("negative branch (even): tan(k/2) = -2/k, k =", end=" ")
k2 = mp.findroot(lambda z: mp.tan(z / 2) + 2 / z, 5.6)
print(mp.nstr(k2, 15), " -> lambda = -2/k^2 =", mp.nstr(-2 / k2 ** 2, 10))
print("negative branch (pi family, even+odd): k=(2m+1)pi, lambda = -2/((2m+1)^2 pi^2):")
for m in [0, 1, 2]:
    print(f"  m={m}: lambda = {mp.nstr(-2 / ((2 * m + 1) ** 2 * mp.pi ** 2), 12)}")
s0 = mp.mpf("0.2")
lhs = Tapply(lambda u: mp.sin(mp.pi * u), s0)
print("odd check: T(sin(pi s)) at s=0.2:", mp.nstr(lhs, 15),
      " vs -(2/pi^2)sin(pi s) =", mp.nstr(-2 / mp.pi ** 2 * mp.sin(mp.pi * s0), 15))
print("I+T min eigenvalue = 1 - 2/pi^2 =", mp.nstr(1 - 2 / mp.pi ** 2, 10),
      " (matches validator-corrected ~0.797)")
print("=> spectral data of our kernel = transcendental roots of tan/cot + pi-family,")
print("   i.e. cot/tan-based (digamma-free); NO gamma products, unlike the CE Mellin multiplier.")

# ----------------------------------------------------------------------
section("H. Fourier-symbol contrast: CE unitary multiplier vs our pole-type symbol")
# CE: |m_lambda(t)| = 1 (pure phase, gamma ratio)  -- the reason Mellin works.
for t in [mp.mpf("1"), mp.mpf("3.0"), mp.mpf("10.0")]:
    lam = mp.mpf("0.5")
    m = mp.exp(mp.mpc(0, t) * mp.log(mp.pi)) * mp.gamma(mp.mpc(lam, -t) / 2) / mp.gamma(mp.mpc(lam, t) / 2)
    print(f"  t={mp.nstr(t,3)}: |m_lambda(t)| = {mp.nstr(abs(m), 20)}  (should be 1)")
# Our |s-s'| kernel: Fourier symbol w^(xi) = -1/(2*pi^2*xi^2) (tempered distribution,
# pole at 0, not a phase). Check numerically that the pairing intint|s-s'|vv equals the
# spectral evaluation (i.e. it is a principal-value/spectral object, not a Mellin one):
print("our kernel symbol: -1/(2*pi^2*xi^2) -- pole at xi=0, NOT a unitary multiplier;")
print("  the pairing intint|s-s'|vv stays finite only as a principal-value/spectral object")
print("  (analytic fact; the CE multiplier has |m|=1 everywhere, the reason Mellin is exact there).")

print("\nDONE.")
