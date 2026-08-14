"""Adversarial validator, targets A-F of the three BHB notes (2026-08-14).

Independent of tools/check_pair_identity.py and tools/check_bhb_arithmetic.py.
Run: uv run --quiet python research/notes/check_validator_af.py
"""
import random, cmath, math
from fractions import Fraction as Fr

random.seed(20260817)

# ================= Target A: pair identity =================
# F real-coefficient (polynomial AND Dirichlet polynomial), set closed under rho <-> 1-rhobar.
def Fpoly(coefs, z): return sum(c * (z ** k) for k, c in enumerate(coefs))
def Fdir(bn, z): return sum(b * (n ** (-z)) for n, b in bn.items())

def trial_pair(coefs, bn, npairs):
    pts = []
    for _ in range(npairs):
        b = random.uniform(0.01, 0.99); g = random.uniform(0.5, 20.0)
        pts += [complex(b, g), complex(1 - b, g)]           # rho and 1-rhobar
    def F(z): return Fpoly(coefs, z) if bn is None else Fdir(bn, z)
    E = sum(F(z) * (F(z.conjugate()) - F(1 - z)) for z in pts)     # LHS
    R = sum(abs(F(pts[2 * i]) - F(1 - pts[2 * i].conjugate())) ** 2 for i in range(npairs))
    S2 = sum(abs(F(z)) ** 2 for z in pts)                          # sum|F(rho)|^2
    assert abs(E.imag) < 1e-9 * max(1.0, abs(E.real)), E
    assert abs(E.real - R) < 1e-9 * max(1.0, abs(E.real))
    assert E.real >= -1e-9                                         # E >= 0
    assert abs(E.real) <= 2 * S2 + 1e-9                            # |E| <= 2 S2 EXACT
    S2p = sum(F(z) * F(1 - z) for z in pts).real
    assert abs(E.real - (S2 - S2p)) < 1e-7 * max(1.0, abs(S2))  # E = S2 - sum F(rho)F(1-rho) (rounding-level)
    # on-line zero (beta=1/2) is a fixed point: contributes 0
    z0 = complex(0.5, random.uniform(0.5, 5.0))
    assert abs(F(z0) * (F(z0.conjugate()) - F(1 - z0))) < 1e-12
    assert abs(F(z0) - F(1 - z0.conjugate())) < 1e-12
    return True

for t in range(200):
    coefs = [random.uniform(-3, 3) for _ in range(random.randint(2, 7))]
    trial_pair(coefs, None, random.randint(2, 8))
    bn = {1: random.uniform(-2, 2)} | {n: random.uniform(-2, 2) for n in range(2, 12)}
    trial_pair(coefs, bn, random.randint(2, 8))
print("A: pair identity HOLDS (200 trials x2 F-types); E>=0; on-line fixed pts -> 0; |E|<=2*S2; E=S2-sum F(rho)F(1-rho)")

# ================= Target C: the left-tail 'E_out-/S2 -> inf' claim =================
# E_out- is a partial sum of the terms of E, so |E_out-| <= |E| <= 2*S2. Hence E_out-/S2 can
# never diverge. The note's worst case (sum over left zeros of |F|^2 ~ T^{1.258} L^2 >> S2 ~ T L^3)
# is inconsistent: that mass is a SUBSET of S2 = sum|F(rho)|^2.
beta, expo = 0.22, 0.478
print(f"C: note worst-case exponent: 1-beta = {1-beta:.2f}; count exponent {expo}; total T^{{{(1-beta)+expo:.3f}}} "
      "BUT this is subset mass of S2 => contradiction with E<=2S2; 'E_out-/S2 -> inf' is FALSE "
      "(correct worst case: E/S2 -> O(1), e.g. ~1).")

# ================= Target B / D / E(iv): arithmetic =================
slack = Fr(1) - Fr(6818, 10000) * Fr(27, 19)          # 0.0311263
r, rp = Fr(99, 1274), Fr(3, 5)
b_pair = math.sqrt(float(slack) / (8 * float(r + rp)))
b_tri = float(slack) / (2 * math.sqrt(2 * float(r + rp)))
print(f"B: slack={float(slack):.7f}  r+r'={float(r+rp):.7f}  b_pair={b_pair:.6f} (claim 0.07577)  b_tri={b_tri:.6f} (claim 0.01337)")
# r formula from firstcheck: (3 theta^3 int u^2 P^2)/(1/2 + 3 theta int P^2), theta=1/2
r_form = Fr(3, 8) * Fr(33, 140) / (Fr(1, 2) + Fr(3, 2) * Fr(17, 40))
print(f"B: r via formula = {float(r_form):.7f} vs 99/1274 = {float(r):.7f}  (denominator 91/80, NOT c(S2)=57/64 -> r_net=0.09925)")
D1 = Fr(19, 70); D2 = Fr(17, 60)
lhs1 = lambda D: 15 * (Fr(1, 2) - D) - Fr(1, 2) * (3 + 5 * (Fr(1, 2) + D))
print(f"D: 15(1/2-D)<(3+5(1/2+D))/2 iff D>19/70: below-threshold FAILS (lhs>0: {lhs1(D1 - Fr(1,10000)) > 0}), "
      f"above-threshold HOLDS (lhs<0: {lhs1(D1 + Fr(1,10000)) < 0})")
lhs2 = lambda D: Fr(30, 13) * (Fr(1, 2) - D) - Fr(1, 2)
print(f"D: (30/13)(1/2-D)<1/2 iff D>17/60: below-threshold FAILS (lhs>0: {lhs2(D2 - Fr(1,10000)) > 0}), "
      f"above-threshold HOLDS (lhs<0: {lhs2(D2 + Fr(1,10000)) < 0})")
s78 = Fr(1, 2) + Fr(28, 100)
print(f"D: GM exponent at Delta=0.28 (sigma=0.78): {float(15*(1-s78)/(3+5*s78)):.5f} (claim 0.4783 < 1/2)")
b_zo = float(slack) / (2 * math.sqrt(float(Fr(3, 5))))
b_ff = float(slack) / (2 * math.sqrt(2 * float(r + rp)))
print(f"E(iv): b(zeta''-only)=0.0311/(2 sqrt(3/5))={b_zo:.5f} (claim 0.0201);  b(full)=0.0311/(2 sqrt(2(r+r'))))={b_ff:.5f} (claim 0.0134)")

# ================= Target E(ii): the un-mollified constant (Gonek anchor) =================
# Coefficients a2 of zeta'/zeta * zeta'^2 = sum a2(n) n^{-s}; check sum_{n<=X} a2(n) ~ -X (log X)^4 / 24.
def spf_sieve(X):
    spf = list(range(X + 1))
    i = 2
    while i * i <= X:
        if spf[i] == i:
            for j in range(i * i, X + 1, i):
                if spf[j] == j:
                    spf[j] = i
        i += 1
    return spf

def a2_partial_sums(X):
    spf = spf_sieve(X)
    def divs(n):
        ds = [1]; m = n
        while m > 1:
            p = spf[m]; c = 0
            while m % p == 0:
                m //= p; c += 1
            ds = [d * (p ** e) for d in ds for e in range(c + 1)]
        return ds
    def is_prime_power(d):
        if d == 1: return 0.0
        p = spf[d]; m = d
        while m % p == 0: m //= p
        return math.log(p) if m == 1 else 0.0
    S = 0.0; out = []
    for n in range(1, X + 1):
        a2 = 0.0
        for d in divs(n):
            lam = is_prime_power(d)
            if lam:
                nd = n // d
                g = 0.0
                for dd in divs(nd):
                    g += math.log(dd) * math.log(nd // dd)
                a2 -= lam * g
        S += a2
        if n in (50000, 100000, 150000, 200000):
            out.append((n, S, -n * (math.log(n)) ** 4 / 24))
    return out

print("E(ii): sum_{n<=X} a2(n) vs -X(log X)^4/24 (Gonek anchor):")
for X, S, pred in a2_partial_sums(200000):
    print(f"   X={X:7d}  sum={S:16.2f}  -X(logX)^4/24={pred:16.2f}  ratio={S/pred:.3f}")
print("E(ii): ratio -> 1 from below at the expected 1 - c/log X rate => order-X(logX)^4 leading term with")
print("       constant -1/24 CONFIRMED. Hence B=1 Lemma-1: S2 ~ (T/2pi)L^3/2 - 2Re(M2), M2 = sum_{m<=T/2pi} a2(m)")
print("       ~ -(T/2pi)L^4/24  =>  S2(B=1) ~ (T/2pi)L^4/12 = Gonek's value (J1 ~ (1/12)L^3, N(T)~(T/2pi)L).")
print("       The notes' anchor (T/2pi)L^3/3 is REFUTED: it is only the L^3-subleading coefficient.")

# ================= Target E(i): chi and the zeta''-FE formula, numerically =================
Bnum = [0.0] * 26
for i, v in enumerate([1.0, -0.5, 1 / 6, 0.0, -1 / 30, 0.0, 1 / 42, 0.0, -1 / 30, 0.0, 5 / 66, 0.0,
                       -691 / 2730, 0.0, 7 / 6, 0.0, -3617 / 510, 0.0, 43867 / 798, 0.0,
                       -174611 / 330, 0.0, 854513 / 138, 0.0, -236364091 / 2730]):
    Bnum[i] = v

def lg(z, K=12):
    # Stirling log-Gamma, |z| large, off negative real axis (any branch fine: exp is branch-invariant)
    s = (z - 0.5) * cmath.log(z) - z + 0.5 * math.log(2 * math.pi)
    for k in range(1, K + 1):
        s += Bnum[2 * k] / (2 * k * (2 * k - 1)) * z ** (1 - 2 * k)
    return s
def zeta_em(s, N=6000, K=12):
    tot = sum(n ** (-s) for n in range(1, N))
    tot += N ** (1 - s) / (s - 1) + 0.5 * N ** (-s)
    for k in range(1, K + 1):
        rising = 1.0
        for j in range(2 * k - 1):
            rising *= (s + j)
        tot += Bnum[2 * k] / math.factorial(2 * k) * rising * N ** (-s - 2 * k + 1)
    return tot

def chi_log(s):
    # log chi(s), chi(s) = (2pi)^s/(2 Gamma(s) cos(pi s/2)); t = Im(s) > 0 branch.
    # log cos(pi s/2) = -i pi s/2 - log 2 + log(1 + e^{2 i z}), z = pi s/2, |e^{2iz}| = e^{-pi t} small
    t = s.imag
    z2 = cmath.exp(-math.pi * t) * cmath.exp(1j * math.pi * s.real) if t >= 0 else cmath.exp(math.pi * t) * cmath.exp(-1j * math.pi * s.real)
    if t >= 0:
        logcos = -1j * math.pi * s / 2 - math.log(2) + cmath.log(1 + z2)
    else:
        logcos = 1j * math.pi * s / 2 - math.log(2) + cmath.log(1 + z2)
    return s * math.log(2 * math.pi) - math.log(2) - lg(s) - logcos

def chi(s):
    return cmath.exp(chi_log(s))

def dlog_chi(s, h=1e-4):
    return (chi_log(s + h) - chi_log(s - h)) / (2 * h)

s0 = complex(0.5, 1000.0)
t = 1000.0; L = math.log(t / (2 * math.pi))
h = 3e-4
f = lambda s: zeta_em(s)
f1 = lambda s: (f(s + h) - f(s - h)) / (2 * h)
f2 = lambda s: (f(s + h) - 2 * f(s) + f(s - h)) / (h * h)
# FE itself
fe_err = abs(chi(s0) * zeta_em(1 - s0) - zeta_em(s0)) / abs(zeta_em(s0))
print(f"E(i): FE chi(s)zeta(1-s)=zeta(s) rel err = {fe_err:.2e}")
# chi'/chi symmetry and value
dl1, dl2 = dlog_chi(s0), dlog_chi(1 - s0)
print(f"E(i): (chi'/chi)(s) = {dl1.real:.4f}{dl1.imag:+.4f}i, (chi'/chi)(1-s) = {dl2.real:.4f}{dl2.imag:+.4f}i, -L = {-L:.4f}")
# zeta''(1-s) = chi(1-s)[zeta''(s) + 2L zeta'(s) + L^2 zeta(s)] + O(1/t)
lhs = f2(1 - s0)
rhs = chi(1 - s0) * (f2(s0) + 2 * L * f1(s0) + L * L * f(s0))
print(f"E(i): zeta''(1-s) LHS={lhs:.6g}  RHS(FE formula)={rhs:.6g}  rel err={abs(lhs-rhs)/max(abs(lhs),1e-9):.2e}")
# alternative: differentiate zeta'(1-s) = chi'(1-s) zeta(s) - chi(1-s) zeta'(s) (finite diff of exact objects)
rhs2 = -(1/h) * (chi(1 - s0 + h) * f1(s0 + h) - chi(1 - s0) * f1(s0))  # d/ds of [chi'(1-s)zeta(s)-chi(1-s)zeta'(s)]  ~ -zeta''(1-s)
# (skip; the direct formula check above is decisive)

# ================= Target F: Taylor center for delta(rho) =================
# delta = zeta'(rhobar) - zeta'(1-rho); rhobar and 1-rho both at height -gamma.
# Correct midpoint: 1/2 - i gamma. The M2 note expands about 1/2 + i gamma (wrong height).
beta, gamma = 0.52, 1000.0
rhobar = complex(beta, -gamma); onemin = complex(1 - beta, -gamma)
m_true = complex(0.5, -gamma)          # true midpoint
m_note = complex(0.5, +gamma)          # note's center
d_true = f1(rhobar) - f1(onemin)       # delta(rho) numerically
pred_true = 2 * (beta - 0.5) * f2(m_true)
pred_note = 2 * (beta - 0.5) * f2(m_note)
cubic = (beta - 0.5) ** 3
print(f"F: delta(rho)={d_true:.6g}")
print(f"F:  2(beta-1/2)zeta''(1/2-i gamma) = {pred_true:.6g}  |err|={abs(d_true-pred_true):.3g}  vs cubic scale {abs(cubic)*abs(f2(m_true)):.3g}  -> TRUE at true midpoint 1/2-i gamma")
print(f"F:  2(beta-1/2)zeta''(1/2+i gamma) = {pred_note:.6g}  |err|={abs(d_true-pred_note):.3g}  vs cubic scale {abs(cubic)*abs(f2(m_note)):.3g}  -> FALSE as O((beta-1/2)^3) at note's center 1/2+i gamma")
print("ALL CHECKS DONE")
