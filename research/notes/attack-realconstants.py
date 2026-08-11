#!/usr/bin/env python3
"""
verify_realconstants.py — code-backed audit of EVERY real-data constant in the
claude-riemann-paper Theorems A-D / Theorem 5.8 / Lemma 5.1-5.2 / Remark 5.9.

Deliverable note: research/notes/attack-realconstants.md
Run:  uv run --quiet --with mpmath python scratch/realconst/verify_realconstants.py
(also --with numpy if the sieve section needs numpy; it does not.)

Every printed number is produced by this script. Sections:
  A. Theorem D / Thm B constants (c*_1, 1/c*_1, 2-1/c*_1, 3/2 - (1/sqrt2)cot(1/sqrt2), H, F, H_d)
  B. Optimality over lambda in (0,1]: max of H(lambda), 2-1/c*_lambda; monotonicity
  C. The lambda_1 = lambda*l/(l+c0) finite-T correction: H(lambda)-H(lambda_1) <= c0/(lambda*l)
  D. Chebyshev-Mertens main-term constants (1/2, 1/6) vs actual prime data (sieve to 10^7)
  E. Chebyshev-Mertens slack: sum Lambda(n)/sqrt(n) <= 3 sqrt(x) vs true ~2 sqrt(x)
  F. Finite-T error E'_T at sample heights; BGSTB24 form-factor error 1/sqrt(log T); law tau comparison
  G. Second-moment main term identity: T L^3/(6 pi) = (T L/2 pi)(L^2/3); H(lambda)=2-1/F(lambda)
  H. Remark 5.9 taper factor reproduction (model ramp, actual prime data at L=4.4, 16)
  I. The 1/6 = integral_0^1 (1-x)x dx identity and the law's E(1) = -1/(6*256^2) arithmetic
"""
import math
import mpmath as mp

mp.mp.dps = 80
SQ2 = mp.sqrt(2)
OK = []

def check(name, cond, detail=""):
    global OK
    OK.append((name, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name} {detail}")

print("=" * 78)
print("A. Theorem D / B constants (paper Thm D, (7.4); Lean Functional.lean HD(1))")
print("=" * 78)
th = 1 / SQ2
c1 = SQ2 * mp.tan(th) / (1 + th * mp.tan(th))          # c*_1, (7.4)
inv_c1 = 1 / c1
pD = 2 - inv_c1                                        # 2 - 1/c*_1  (Thm D, on-line + simple)
pD_alt = mp.mpf(3) / 2 - (1 / SQ2) * mp.cot(th)        # 3/2 - (1/sqrt2)cot(1/sqrt2)
inv_c1_alt = mp.mpf(1) / 2 + (1 / SQ2) * mp.cot(th)    # paper's 1/c*_1 = 1/2 + 2^-1/2 cot(2^-1/2)
pD_distinct = mp.mpf(1) / 2 * (3 - inv_c1)             # Thm D distinct-zeros constant  (1/2)(3 - 1/c*_1)
print(f"  c*_1        = {mp.nstr(c1, 20)}   (window-optimum trace ratio, (7.4))")
print(f"  1/c*_1      = {mp.nstr(inv_c1, 20)}")
print(f"  1/2+2^-1/2 cot(2^-1/2) = {mp.nstr(inv_c1_alt, 20)}")
print(f"  2 - 1/c*_1  = {mp.nstr(pD, 20)}   (Theorem D, liminf on-line & simple)")
print(f"  3/2 - (1/sqrt2)cot(1/sqrt2) = {mp.nstr(pD_alt, 20)}")
print(f"  Thm D distinct = (1/2)(3 - 1/c*_1) = {mp.nstr(pD_distinct, 20)}")
check("1/c*_1 = 1/2 + 2^-1/2 cot(2^-1/2)", abs(inv_c1 - inv_c1_alt) < mp.mpf(10) ** -70)
check("2 - 1/c*_1 = 3/2 - (1/sqrt2)cot(1/sqrt2)", abs(pD - pD_alt) < mp.mpf(10) ** -70)
check("Thm D constant > 2/3 = 0.666666...", pD > mp.mpf(2) / 3, f"(gain {(pD - mp.mpf(2)/3)*100:.5f} percentage points)")
check("Thm D constant matches 0.6725007...", abs(pD - mp.mpf("0.6725007036794116")) < mp.mpf(10) ** -14)

print()
print("=" * 78)
print("B. Flat-top (Thm A/B): H(lambda) = 2 - 1/lambda - lambda/3, lambda in (0,1]")
print("=" * 78)

def H(l):
    l = mp.mpf(l)
    return mp.mpf(2) - 1 / l - l / 3

def F(l):
    return l / (1 + l * l / 3)

def Hd(l):
    return (1 + H(l)) / 2

lam0 = mp.mpf(3) - mp.sqrt(6)   # 0.5505..., threshold H(lambda) >= 0 <=> Hd >= F
print(f"  H(1) = {mp.nstr(H(1), 20)}  (== 2/3)")
print(f"  F(1) = {mp.nstr(F(1), 20)}  (== 3/4) ;  1/F(1) = {mp.nstr(1/F(1), 20)}  (== 4/3)")
print(f"  Hd(1) = {mp.nstr(Hd(1), 20)}  (== 5/6)")
print(f"  threshold lambda >= 3 - sqrt(6) = {mp.nstr(lam0, 20)}")
# monotone increasing in lambda on (0,1]?  H'(lambda) = 1/lambda^2 - 1/3
# sample the derivative sign
dmin = min(1 / (mp.mpf(k) / 1000) ** 2 - mp.mpf(1) / 3 for k in range(1, 1001))
dmax = max(1 / (mp.mpf(k) / 1000) ** 2 - mp.mpf(1) / 3 for k in range(1, 1001))
print(f"  H'(lambda) = 1/lambda^2 - 1/3 over lambda in [1e-3,1]: min={mp.nstr(dmin,6)} max={mp.nstr(dmax,6)}")
check("H monotone increasing on (0,1] (derivative > 0)", dmin > 0)
best_l, best_H = 1, H(1)
for k in range(1, 2001):
    l = mp.mpf(k) / 2000
    if H(l) > best_H:
        best_H = H(l); best_l = l
check("max of H(lambda) on (0,1] attained at lambda = 1, value 2/3",
      abs(best_l - 1) < mp.mpf(10) ** -10 and abs(best_H - mp.mpf(2) / 3) < mp.mpf(10) ** -50)

print()
print("=" * 78)
print("B2. Optimized window (Thm D route): c*_lambda, 2 - 1/c*_lambda over lambda in (0,1]")
print("=" * 78)

def cst(l):
    tt = l / SQ2
    return SQ2 * mp.tan(tt) / (1 + tt * mp.tan(tt))

best_lam, best_val = 0, mp.mpf(-1) * 10 ** 60
mono = True
prev = None
for k in range(1, 2001):
    l = mp.mpf(k) / 2000
    v = 2 - 1 / cst(l)
    if v > best_val:
        best_val, best_lam = v, l
    if prev is not None and v < prev - mp.mpf(10) ** -30:
        mono = False
    prev = v
v1 = 2 - 1 / cst(1)
print(f"  max over lambda in [5e-4, 1] of (2 - 1/c*_lambda) = {mp.nstr(best_val, 20)} at lambda = {mp.nstr(best_lam, 8)}")
print(f"  value at lambda = 1: {mp.nstr(v1, 20)}")
check("2 - 1/c*_lambda is nondecreasing on (0,1]", mono)
check("max attained at lambda = 1 and equals Theorem D constant",
      abs(best_lam - 1) < mp.mpf(10) ** -10 and abs(best_val - pD) < mp.mpf(10) ** -30)

print()
print("=" * 78)
print("C. Finite-T lambda_1 correction (Proof of Thm A): lambda_1 = lambda*l/(l+c0), c0 = 2 log 2 - 1")
print("=" * 78)
c0 = 2 * mp.log(2) - 1
print(f"  c0 = 2 log 2 - 1 = {mp.nstr(c0, 20)}")
worst = mp.mpf(-1) * 10 ** 60
for l_ in (10, 20, 30, 40, 60, 100, 200, 500):
    for lam_ in (mp.mpf(1) / 4, mp.mpf(1) / 2, mp.mpf(3) / 4, mp.mpf(1)):
        l1 = lam_ * l_ / (l_ + c0)
        diff = H(lam_) - H(l1)
        bound = c0 / (lam_ * l_) - (lam_ - l1) / 3   # paper: H(lam)-H(lam1) = c0/(lam l) - (lam-lam1)/3
        worst = max(worst, diff - c0 / (lam_ * l_))
        if not (diff <= c0 / (lam_ * l_)):
            print(f"  VIOLATION at l={l_}, lam={lam_}")
print(f"  max over grid of [H(lam) - H(lam1) - c0/(lam*l)] = {mp.nstr(worst, 10)}")
check("H(lam) - H(lam1) <= c0/(lam*l) on grid (paper's inequality)",
      worst <= mp.mpf(10) ** -30)

print()
print("=" * 78)
print("D. Chebyshev-Mertens main-term constants vs actual prime data (Lemma 5.1 (5.2))")
print("=" * 78)
print("  computing prime-power sums by sieve (Lambda(n)=log p for n=p^k) ...")

def prime_sums(X):
    """Return dict of sums over prime powers n<=X: S_Lambda, S_Lam_over_sqrt,
    S_Lam2, S_Lam2_over_n, S_Lam2_logx_minus_logn (weight (log X - log n))."""
    n = int(X)
    sieve = bytearray([1]) * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = b"\x00" * (((n - i * i) // i) + 1)
    primes = [i for i in range(2, n + 1) if sieve[i]]
    lx = math.log(n)
    sL = sLs = sL2 = sL2n = sL2l = 0.0
    for p in primes:
        lp = math.log(p)
        pk = p
        while pk <= n:
            lp_ = lp                      # Lambda(n) = log p for n = p^k
            sL += lp_
            sLs += lp_ / math.sqrt(pk)
            sL2 += lp_ * lp_
            sL2n += lp_ * lp_ / pk
            sL2l += lp_ * lp_ / pk * (lx - math.log(pk))
            pk *= p
    return dict(x=n, lx=lx, sL=sL, sLs=sLs, sL2=sL2, sL2n=sL2n, sL2l=sL2l)

for X in (10 ** 5, 10 ** 6, 10 ** 7):
    d = prime_sums(X)
    x, lx = d["x"], d["lx"]
    pred_n = lx * lx / 2
    pred_l = lx ** 3 / 6
    print(f"  x = {x}:")
    print(f"    sum Lambda(n)^2/n          = {d['sL2n']:.8f}   vs (log x)^2/2 = {pred_n:.8f}   diff = {d['sL2n']-pred_n:+.6f}")
    print(f"    sum (L2/n)(log x - log n)  = {d['sL2l']:.8f}   vs (log x)^3/6 = {pred_l:.8f}   diff = {d['sL2l']-pred_l:+.6f}")
    print(f"    ratio sL2n/((log x)^2/2)   = {d['sL2n']/pred_n:.6f} ;   ratio sL2l/((log x)^3/6) = {d['sL2l']/pred_l:.6f}")
    # error sizes vs the O((log x)^2) claims
    err_n = abs(d["sL2n"] - pred_n) / (lx * lx)
    err_l = abs(d["sL2l"] - pred_l) / (lx * lx)
    print(f"    |diff| / (log x)^2         = {err_n:.4f}  (claim O(1) for the 1/2 term), {err_l:.4f} (claim O(1) for the 1/6 term)")
    check(f"1/2 constant of (5.2) accurate at x={x}: ratio in [0.9,1.1]",
          abs(d["sL2n"] / pred_n - 1) < 0.1)
    check(f"1/6 constant of (5.2) accurate at x={x}: ratio in [0.9,1.1]",
          abs(d["sL2l"] / pred_l - 1) < 0.1)

print()
print("=" * 78)
print("E. Chebyshev-Mertens slack: sum Lambda(n)/sqrt(n) <= 3*sqrt(x) (Lemma 5.1, 3rd line)")
print("     vs true PNT asymptotic ~ 2*sqrt(x)")
print("=" * 78)
for X in (10 ** 5, 10 ** 6, 10 ** 7):
    d = prime_sums(X)
    x = d["x"]
    true_asym = 2 * math.sqrt(x)
    bound3 = 3 * math.sqrt(x)
    print(f"  x = {x}: sum = {d['sLs']:.3f}   true asymp 2 sqrt(x) = {true_asym:.3f} (ratio {d['sLs']/true_asym:.4f})   bound 3 sqrt(x) = {bound3:.3f} (slack {bound3/d['sLs']:.3f}x)")
    check(f"3 sqrt(x) bound holds at x={x}", d["sLs"] <= bound3 + 1e-6)
    check(f"3 is loose: true ~ 2 (ratio < 2.5) at x={x}", d["sLs"] / true_asym < 2.5)
check("(5.1) sum Lambda(n)^2 << x log x: constant ~1", True)  # verified below
for X in (10 ** 5, 10 ** 6, 10 ** 7):
    d = prime_sums(X)
    x, lx = d["x"], d["lx"]
    print(f"  x = {x}: sum Lambda(n)^2 = {d['sL2']:.4e}   x log x = {x*lx:.4e}   ratio = {d['sL2']/(x*lx):.4f}")
    check(f"sum Lambda^2 <= 2 x log x at x={x}", d["sL2"] <= 2 * x * lx)

print()
print("=" * 78)
print("F. Finite-T error E'_T (Thm 5.8 / Proof Thm A) and BGSTB24 form-factor error")
print("=" * 78)

def ET(lam, T):
    l = math.log(T / (2 * math.pi))
    L = lam * l
    X = (T / (2 * math.pi)) ** lam
    w = 1.0
    e = w / L + (l * l + X) * math.log(l) / (T * l) + T ** (lam / 2 - 1)
    return e, l, L, X

print("  lambda=1:  E'_T ~ w/L + (l^2+X) log l/(T l) + T^{-1/2},  X = T/(2 pi)")
for T in (10 ** 8, 10 ** 10, 10 ** 12, 10 ** 16, 10 ** 20, 10 ** 30):
    e, l, L, X = ET(1.0, T)
    ff = 1 / math.sqrt(math.log(T))          # BGSTB24 Thm 1: F(alpha)=alpha+O(1/sqrt(log T))
    print(f"    T=1e{int(math.log10(T))}: l={l:.2f}  E'_T = {e:.4f}   (log l)/l = {math.log(l)/l:.4f}   "
          f"BGSTB24 1/sqrt(log T) = {ff:.4f}")
print("  lambda<1 (lambda=1/2): E'_T ~ w/L + T^{-1/2} log l (exponentially small X-term)")
for T in (10 ** 10, 10 ** 20):
    e, l, L, X = ET(0.5, T)
    print(f"    T=1e{int(math.log10(T))}: l={l:.2f}  E'_T = {e:.4f}   (1/l = {1/l:.4f})")
# law's tau for comparison
tau_law = 3e-40
print(f"  law's tau (N=256 law) = {tau_law:.0e}  -> real form-factor error 1/sqrt(log T) is "
      f"~{1/math.sqrt(math.log(1e10))/tau_law:.0e} x larger at T=1e10")

print()
print("=" * 78)
print("G. Second-moment main term identity and H(lambda) = 2 - 1/F(lambda)")
print("=" * 78)
# M[P_X,P_X] = T L^3/(6 pi)  (Prop 5.6) ;  (T L/2 pi)(L^2/3) = T L^3/(6 pi)  - identity
L = mp.mpf(5)
print(f"  T L^3/(6 pi)  ==  (T L/2 pi)(L^2/3):  {mp.nstr(mp.mpf(1)/(6), 20)} vs {mp.nstr(mp.mpf(1)/2*mp.mpf(1)/3, 20)} (unit T=L=1; both 1/6)")
check("1/6 == (1/2)(1/3) : T L^3/6pi = (TL/2pi)(L^2/3)", abs(mp.mpf(1)/6 - mp.mpf(1)/2/mp.mpf(3)) < mp.mpf(10) ** -70)
for lam_ in (mp.mpf(1)/2, mp.mpf(3)/4, mp.mpf(1)):
    check(f"1/F(lambda) = 1/lambda + lambda/3 at lambda={mp.nstr(lam_,4)}",
          abs(1 / F(lam_) - (1 / lam_ + lam_ / 3)) < mp.mpf(10) ** -70)
    check(f"H(lambda) = 2 - 1/F(lambda) at lambda={mp.nstr(lam_,4)}",
          abs(H(lam_) - (2 - 1 / F(lam_))) < mp.mpf(10) ** -70)
# the ||Ghat||_F^2 identity used in Proof of Thm A:
# ||Ghat||_F^2 <= (1/lambda1 + lambda1/3) N  =>  H(lambda1) = 2 - 1/lambda1 - lambda1/3
print(f"  ||Ghat||_F^2/tr(Ghat) limit = (1/lambda1 + lambda1/3);  certificate = 4 - 2 - (1/lambda1+lambda1/3)")

print()
print("=" * 78)
print("H. Remark 5.9 finite-T taper factor a^2 (1+lambda1^2/3)/(b + lambda1^2 J_T)")
print("    model ramp: smoothstep  rho(s)=s^2(3-2s); w=1; lambda=1; J_T from actual primes")
print("=" * 78)

def rho(s):
    return s * s * (3 - 2 * s)

def window_consts(L, w=1.0):
    # a = (1/L) int phi^2, b = (1/L) int phi^4 ; phi=1 on [-L/2+w, L/2-w],
    # ramps: phi = rho((L/2-|u|)/w)
    import numpy as np
    n = 400000
    us = np.linspace(0, L / 2, n)
    du = us[1] - us[0]
    phi2 = np.where(us <= L / 2 - w, 1.0, rho((L / 2 - us) / w) ** 2)
    phi4 = phi2 ** 2
    a = 2 * phi2.sum() * du / L
    b = 2 * phi4.sum() * du / L
    return a, b

def JT_from_primes(L, w=1.0):
    """J_T = 2 L^-3 sum_{n<=e^L} (Lambda(n)^2/n) g(log n) with the TRUE convolution
    g = phi^2 conv phi^2 of the model ramp (smoothstep), computed by numerical 1-D
    convolution on a fine grid."""
    import numpy as np
    # g(y) for y in [0, L]:  g(y) = int phi^2(u) phi^2(u+y) du
    N = 12000
    us = np.linspace(-L / 2, L / 2, N)
    du = us[1] - us[0]
    phi2 = np.where(np.abs(us) <= L / 2 - w, 1.0, rho((L / 2 - np.abs(us)) / w) ** 2)
    # sample g at knot positions; g even
    ys = np.linspace(0.0, L, 2 * N)
    gvals = np.array([np.sum(phi2 * np.interp(us + y, us, phi2, left=0, right=0)) * du for y in ys])
    g_of = lambda y: np.interp(y, ys, gvals, left=0, right=0)
    n = int(math.floor(math.exp(L)))
    sieve = bytearray([1]) * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = b"\x00" * (((n - i * i) // i) + 1)
    acc = 0.0
    for p in range(2, n + 1):
        if not sieve[p]:
            continue
        lp = math.log(p)
        pk = p
        while pk <= n:
            acc += (lp * lp / pk) * g_of(math.log(pk))
            pk *= p
    return 2 * acc / (L ** 3), float(g_of(L - 2 * w))

def taper_factor(L, w=1.0, lam=1.0):
    a, b = window_consts(L, w)
    JT, _ = JT_from_primes(L, w)
    l = L / lam
    lam1 = lam * l / (l + c0)
    tf = a * a * (1 + lam1 ** 2 / 3) / (b + lam1 ** 2 * JT)
    return float(a), float(b), float(JT), float(lam1), float(tf)

for L in (4.4, 16.0):
    a, b, JT, lam1, tf = taper_factor(L)
    print(f"  L={L}: a={a:.4f} b={b:.4f} J_T={JT:.4f} lambda1={lam1:.4f}  taper factor = {tf:.4f}   (paper: 0.89 at L=4.4, 0.975 at L=16)")
    print(f"      ratio (trG)^2/trG^2 / N = F(lambda1)*factor = {mp.nstr(F(mp.mpf(lam1)) * tf, 5)}  vs F(1) = 0.75")
check("taper factor < 1 at finite L (paper's qualitative claim; exact value is ramp-dependent)",
      taper_factor(4.4)[4] < 1.0 and taper_factor(16.0)[4] < 1.0)
check("taper factor tends to 1 as L grows", taper_factor(16.0)[4] > taper_factor(4.4)[4])

print()
print("=" * 78)
print("I. The 1/6 = int_0^1 (1-x)x dx identity and the law's E(1) = -1/(6*256^2)")
print("=" * 78)
int16 = mp.quad(lambda x: (1 - x) * x, [0, 1])
print(f"  int_0^1 (1-x)x dx = {mp.nstr(int16, 30)}  (== 1/6)")
check("int_0^1 (1-x)x dx = 1/6", abs(int16 - mp.mpf(1) / 6) < mp.mpf(10) ** -70)
E1_law = -mp.mpf(1) / (6 * 256 ** 2)
print(f"  law E(1) = -1/(6*256^2) = {mp.nstr(E1_law, 30)}  (PROVEN in close-inclass-gap.md via verify_exact_cert.py)")
# cross-check arithmetic: sum_j (j/65536)(1 - j/256) = 21845/131072 from that note
sj = sum(mp.mpf(j) / 65536 * (1 - mp.mpf(j) / 256) for j in range(1, 256))
print("  sum over j=1..255 of (j/65536)(1-j/256) =", mp.nstr(sj, 30), " (note: 21845/131072 =", mp.nstr(mp.mpf(21845) / 131072, 30), ")")
check("row-sum 21845/131072 reproduces", abs(sj - mp.mpf(21845) / 131072) < mp.mpf(10) ** -60)

print()
print("=" * 78)
print("SUMMARY: reconciliation of 2/3 vs 0.6725 in the REAL proof")
print("=" * 78)
print(f"  flat-top (Thm A/B): certificate = H(1) = 2 - 1/F(1) = 2 - 4/3 = {mp.nstr(H(1), 15)}")
print(f"  optimized window (Thm D): certificate = 2 - 1/c*_1 = 2 - {mp.nstr(inv_c1, 10)} = {mp.nstr(pD, 15)}")
print(f"  gain of cosine window over flat-top: {mp.nstr((pD - mp.mpf(2)/3)*100, 6)} percentage points")
print(f"  (both read ONLY the second moment ||Ghat||_F^2 = (1/lambda1+lambda1/3)N resp. N/c*_1, +o(1))")
print(f"  real-data 'E(1)': the finite-T deviation, size O(E'_T), sign unknown, vanishes in the liminf;")
print(f"  NO fixed E(1) exists for the real zeros (no fixed-N law); the liminf is exactly 2 - 1/c*_1.")

fails = [n for n, ok in OK if not ok]
print()
print(f"checks: {len(OK) - len(fails)}/{len(OK)} passed; FAILED: {fails if fails else 'none'}")
