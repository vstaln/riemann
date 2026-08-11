#!/usr/bin/env python3
"""Jensen-polynomial RH-ometer for the Riemann xi function (C-RH2 probe).

Objects (GORTTW arXiv:1910.01227 conventions):
    psi(z) := sum_j gamma(j)/j! z^{2j} = xi(1/2 + z)     => gamma(j) = xi^{(2j)}(1/2) * j!/(2j)!
    J_{d,n}(X) := sum_{j=0}^d binom(d,j) gamma(n+j) X^j
Pólya: RH  <=>  J_{d,n} hyperbolic for all d, n >= 0.
RH_m (all zeros of xi^{(m)} on the line) <=> J_{d,n} hyperbolic for all d>=1, n>=m.
Degree-2 hyperbolicity of J_{2,n} <=> gamma(n+1)^2 >= gamma(n) gamma(n+2)  (log-concavity;
proven unconditionally for all n, CNV / Dimitrov-Lucas / Chasse / GORTTW Cor 1.3).
GORTTW uniformizer:  Delta(M) = sqrt( (1/2)(1 - gamma(M-2)gamma(M)/gamma(M-1)^2 ) ) ~ 1/sqrt(2M).

ALL xi^{(2j)}(1/2) are computed from the EXPLICIT FORMULA (log-derivative tower at s=1/2:
L' = 1/s + 1/(s-1) - (1/2)log pi + (1/2)psi(s/2) + zeta'/zeta, with zeta'/zeta = analytic
continuation of -sum_p log p p^{-s}; mpmath Euler-Maclaurin, NO zero data).  Cross-checks:
  - parity L'(1/2) = L'''(1/2) = ... = 0
  - zeta'/zeta(1/2) = (1/2)(gamma + 3 log 2 + log pi + pi/2)      [functional equation, closed form]
  - (zeta'/zeta)^{(2k)}(1/2) = (chi'/chi)^{(2k)}(1/2)/2           [chi = 2^s pi^{s-1} sin(pi s/2) Gamma(1-s)]
  - direct mp.diff of xi(z+1/2) at 0
  - moment dictionary:  e_j = gamma(j)/(gamma(0) j!)  vs  zero-power sums sum_gamma gamma^{-2k}
    computed from the verified on-line zeros (zeros_1_1000.txt) + analytic tail.

Run:  uv run --quiet --with mpmath python tools/jensen_ometer.py
"""
import math
import time
import mpmath as mp

mp.mp.dps = 60
PI = mp.pi

# ----------------------------------------------------------------------------
# 1. explicit-formula derivative tower at s = 1/2
# ----------------------------------------------------------------------------


def zeta_log_derivatives(s, K):
    """w[k] = (zeta'/zeta)^{(k)}(s), k = 0..K, from zeta^{(k)}(s) via w*z = z'."""
    zk = [mp.zeta(s, derivative=k) for k in range(K + 2)]
    w = [mp.mpf(0)] * (K + 1)
    z0 = zk[0]
    for k in range(K + 1):
        acc = zk[k + 1]
        for j in range(k):
            acc -= mp.binomial(k, j) * w[j] * zk[k - j]
        w[k] = acc / z0
    return zk, w


def xi_log_derivatives(s, K):
    """L[k] = d^k/ds^k log xi at s, k = 0..K (explicit formula).

    log xi(s) = log(1/2) + log s + log(s-1) - (s/2) log pi + log Gamma(s/2) + log zeta(s)
      d^k[log s + log(s-1)] = (-1)^{k-1} (k-1)! (s^{-k} + (s-1)^{-k})
      d^k[log Gamma(s/2)]   = psi^{(k-1)}(s/2) / 2^k
      d^k[log zeta(s)]      = (zeta'/zeta)^{(k-1)}(s)
    """
    _, w = zeta_log_derivatives(s, K)
    L = [mp.mpf(0)] * (K + 1)
    L[0] = mp.log(mp.mpf('0.5') * s * (s - 1) * mp.power(PI, -s / 2)
                   * mp.gamma(s / 2) * mp.zeta(s))
    for k in range(1, K + 1):
        d_inv = (-1) ** (k - 1) * mp.factorial(k - 1) * (s ** (-k) + (s - 1) ** (-k))
        d_cst = -mp.log(PI) / 2 if k == 1 else mp.mpf(0)
        d_psi = mp.polygamma(k - 1, s / 2) / (2 ** k)
        L[k] = d_inv + d_cst + d_psi + w[k - 1]
    return L


def exp_tower(L, K):
    """F[k] = d^k/ds^k exp(L) at the point, from L[0..K] (Bell recurrence)."""
    F = [mp.mpf(0)] * (K + 1)
    F[0] = mp.exp(L[0])
    for k in range(1, K + 1):
        acc = mp.mpf(0)
        for j in range(1, k + 1):
            acc += mp.binomial(k - 1, j - 1) * L[j] * F[k - j]
        F[k] = acc
    return F


def xi_coeffs(nmax):
    """gamma(n) = xi^{(2n)}(1/2) * n!/(2n)!,  n = 0..nmax, via the explicit formula."""
    K = 2 * nmax
    s = mp.mpf('0.5')
    L = xi_log_derivatives(s, K)
    F = exp_tower(L, K)
    gam = []
    for n in range(nmax + 1):
        gam.append(F[2 * n] * mp.factorial(n) / mp.factorial(2 * n))
    return gam, L, F


def xi_direct(z):
    return mp.mpf('0.5') * (z + mp.mpf('0.5')) * (z - mp.mpf('0.5')) \
        * mp.power(PI, -(z + mp.mpf('0.5')) / 2) * mp.gamma((z + mp.mpf('0.5')) / 2) \
        * mp.zeta(z + mp.mpf('0.5'))


def chi_over_chi(s):
    """chi'/chi for chi(s) = 2^s pi^{s-1} sin(pi s/2) Gamma(1-s)."""
    return mp.log(2) + mp.log(PI) + (PI / 2) * mp.cot(PI * s / 2) - mp.psi(0, 1 - s)


# ----------------------------------------------------------------------------
# 2. discriminants / margins
# ----------------------------------------------------------------------------


def quad_disc(g0, g1, g2):
    """J_{2,n}: gamma(n) + 2 gamma(n+1) X + gamma(n+2) X^2.  Delta = 4(g1^2 - g0 g2)."""
    return 4 * (g1 ** 2 - g0 * g2)


def cubic_disc(A, B, C, D):
    """Discriminant of A x^3 + B x^2 + C x + D (real-rooted <=> >= 0)."""
    return B ** 2 * C ** 2 - 4 * A * C ** 3 - 4 * B ** 3 * D - 27 * A ** 2 * D ** 2 + 18 * A * B * C * D


def main():
    t0 = time.time()
    print("=" * 78)
    print("JENSEN-POLYNOMIAL RH-OMETER  (C-RH2)   -- explicit-formula, no zero data")
    print("=" * 78)

    nmax = 6
    gam, L, F = xi_coeffs(nmax)
    print(f"\n[dps {mp.mp.dps}] explicit-formula log-derivative tower at s = 1/2")
    print(f"  L(1/2)      = {mp.nstr(L[0], 30)}")
    print(f"  L'(1/2)     = {mp.nstr(L[1], 10)}   (parity: expect 0)")
    print(f"  L'''(1/2)   = {mp.nstr(L[3], 10)}   (parity: expect 0)")
    print(f"  L^(5)(1/2)  = {mp.nstr(L[5], 10)}   (parity: expect 0)")
    print(f"  L''(1/2)    = {mp.nstr(L[2], 30)}   (= xi''/xi(1/2) = 2*sum 1/gamma^2 under RH)")
    print(f"  L^(4)(1/2)  = {mp.nstr(L[4], 30)}")

    # closed-form cross-checks on zeta'/zeta at 1/2
    _, w = zeta_log_derivatives(mp.mpf('0.5'), 6)
    cf0 = mp.mpf('0.5') * (mp.euler + 3 * mp.log(2) + mp.log(PI) + PI / 2)
    print("\n[closed-form functional-equation checks]")
    print(f"  zeta'/zeta(1/2)        = {mp.nstr(w[0], 30)}")
    print(f"  closed form (1/2)(g+3l2+lpi+pi/2) = {mp.nstr(cf0, 30)}   diff = {mp.nstr(w[0] - cf0, 3)}")
    for k in (2, 4):
        chi_der = mp.diff(chi_over_chi, mp.mpf('0.5'), k)
        print(f"  (zeta'/zeta)^({k})(1/2)  = {mp.nstr(w[k], 30)}")
        print(f"    vs (chi'/chi)^({k})(1/2)/2 = {mp.nstr(chi_der / 2, 30)}   diff = {mp.nstr(w[k] - chi_der / 2, 3)}")

    # direct mp.diff cross-check of gamma(n)
    print("\n[gamma(n) = xi^{(2n)}(1/2) n!/(2n)!; tower vs direct mp.diff]")
    for n in range(4):
        direct = mp.diff(xi_direct, mp.mpf('0'), 2 * n) * mp.factorial(n) / mp.factorial(2 * n)
        print(f"  gamma({n}) tower = {mp.nstr(gam[n], 35)}")
        print(f"           direct = {mp.nstr(direct, 35)}   diff = {mp.nstr(gam[n] - direct, 3)}")

    print("\n[gamma coefficients]")
    for n in range(nmax + 1):
        print(f"  gamma({n}) = {mp.nstr(gam[n], 40)}")

    # ---- degree-2 Jensen discriminants and margins ----
    print("\n" + "=" * 78)
    print("DEGREE-2 JENSEN DISCRIMINANTS   J_{2,n}(X) = g(n) + 2 g(n+1) X + g(n+2) X^2")
    print("=" * 78)
    print("  Delta = 4(g(n+1)^2 - g(n)g(n+2));   hyperbolicity <=> Delta >= 0")
    print("  (proven unconditionally for ALL n: CNV/Dimitrov-Lucas d<=3, Chasse d<=2e17,"
          " GORTTW Cor 1.3 d<=9.36e20)")
    print(f"  {'n':>2} {'shift-window':>12} {'Delta':>28} {'r=g(n)g(n+2)/g(n+1)^2':>24} {'margin=1-r':>16}")
    for n in range(4):
        D = quad_disc(gam[n], gam[n + 1], gam[n + 2])
        r = gam[n] * gam[n + 2] / gam[n + 1] ** 2
        win = "xi" if n == 0 else (f"xi' (n>=1)" if n == 1 else f"xi'' (n>=2)" if n == 2 else "n>=3")
        print(f"  {n:>2} {win:>12} {mp.nstr(D, 26):>28} {mp.nstr(r, 22):>24} {mp.nstr(1 - r, 15):>16}")

    # margin asymptotic vs 1/n
    print("\n[degree-2 margin asymptotics: 1 - r_n vs 1/n (Hermite limit r_n ~ e^{-1/n})]")
    for n in range(1, nmax - 1):
        r = gam[n] * gam[n + 2] / gam[n + 1] ** 2
        print(f"  n={n}: margin = {mp.nstr(1 - r, 12)}   1/n = {1 / n}   ratio = {mp.nstr((1 - r) * n, 6)}")

    # GORTTW uniformizer Delta(M) ~ 1/sqrt(2M)
    print("\n[GORTTW uniformizer  Delta(M) = sqrt((1/2)(1 - g(M-2)g(M)/g(M-1)^2)) ~ 1/sqrt(2M)]")
    for M in range(2, nmax + 1):
        Delta = mp.sqrt(mp.mpf('0.5') * (1 - gam[M - 2] * gam[M] / gam[M - 1] ** 2))
        print(f"  M={M}: Delta = {mp.nstr(Delta, 12)}   1/sqrt(2M) = {mp.nstr(1 / mp.sqrt(2 * M), 12)}")

    # ---- degree-3 Jensen discriminants ----
    print("\n" + "=" * 78)
    print("DEGREE-3 JENSEN POLYNOMIALS   J_{3,n}(X) = g(n) + 3 g(n+1) X + 3 g(n+2) X^2 + g(n+3) X^3")
    print("=" * 78)
    for n in range(3):
        A, B, C, D = gam[n + 3], 3 * gam[n + 2], 3 * gam[n + 1], gam[n]
        D3 = cubic_disc(A, B, C, D)
        rts = mp.polyroots([A, B, C, D], maxsteps=200)
        rts = sorted([mp.re(r) for r in rts])
        gaps = [rts[i + 1] - rts[i] for i in range(2)]
        scale = max(abs(c) for c in (A, B, C, D))
        print(f"  n={n}:  Delta_3 = {mp.nstr(D3, 24)}")
        print(f"         roots  = {[mp.nstr(x, 12) for x in rts]}")
        print(f"         min gap/scale = {mp.nstr(min(gaps) / scale, 12)}  (Hermite limit H3(X/2)=X^3-6X: 0.5*scale)")
    # Hermite limit comparison for d=3
    print("  Hermite limit:  J_{3,n}((Delta X - 1)/...) -> X^3 - 6X, roots {0, +/-sqrt(6) ~ +/-2.449}")

    # ---- derivative-tower discriminants in the paper sense (shifts n >= m) ----
    print("\n" + "=" * 78)
    print("DERIVATIVE TOWER (GORTTW sense):  RH_m (xi^{(m)} zeros on line)")
    print("  <=>  J_{d,n} hyperbolic for all d>=1, n>=m   (paper eq. after Thm 1.2)")
    print("=" * 78)
    print("  already tabled above: n=1 -> xi' window (J_{2,1}, J_{3,1}), n=2 -> xi'' window (J_{2,2}, J_{3,2}).")
    print("  All positive margins (proven range).  RH_1 verified numerically to height 1419 in")
    print("  tools/xiprime_check (999 on-line xi'-zeros, one per gap);  xi'' tower in check_tower.py.")

    # ---- local (pointwise) discriminant probe: C-RH2's "grid at height" object ----
    print("\n" + "=" * 78)
    print("LOCAL POINTWISE PROBE (C-RH2 probe design: xi,xi',xi'' along the line)")
    print("  D(t) = 2 xi xi'' - xi'^2  = discriminant of the local quadratic at s = 1/2+it.")
    print("  NOT a Jensen discriminant: J_{d,n} lives in the (d, shift n) table of global")
    print("  coefficients, not at a height t.  Sign of D(t) tracks local convexity only.")
    print("=" * 78)
    mp.mp.dps = 25
    hs = [1000, 1200, 1500, 1800, 2200, 2700, 3300, 4000, 5000, 6000, 7500, 9000, 10000]
    neg = pos = 0
    def xi_loc(s):
        return mp.mpf('0.5') * s * (s - 1) * mp.power(PI, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)
    def A(s):
        return (1 / s + 1 / (s - 1) - mp.mpf('0.5') * mp.log(PI)
                + mp.mpf('0.5') * mp.psi(0, s / 2) + mp.zeta(s, derivative=1) / mp.zeta(s))
    def Ap(s):
        zp = mp.zeta(s, derivative=1)
        return (-1 / s ** 2 - 1 / (s - 1) ** 2 + mp.mpf('0.25') * mp.psi(1, s / 2)
                + mp.zeta(s, derivative=2) / mp.zeta(s) - (zp / mp.zeta(s)) ** 2)
    print("  {:>8} {:>26} {:>6}".format("t", "D(t) = 2 xi*xipp - xip^2", "sign"))
    stats = []
    for t in hs:
        s = mp.mpf('0.5') + 1j * mp.mpf(t)
        v = xi_loc(s)
        xip_v = v * A(s)
        xipp_v = v * (A(s) ** 2 + Ap(s))
        Dt = 2 * v * xipp_v - xip_v ** 2
        Dt = mp.re(Dt)
        sign = "+" if Dt > 0 else ("-" if Dt < 0 else "0")
        pos += Dt > 0
        neg += Dt < 0
        stats.append(Dt)
        print(f"  {t:>8} {mp.nstr(Dt, 18):>26} {sign:>6}")
    print(f"  D(t) > 0: {pos}/{len(hs)}   D(t) < 0: {neg}/{len(hs)}   "
          "(negative on concave 'hills' of g(t)=xi(1/2+it) -- carries no RH information)")
    mp.mp.dps = 60

    # ---- prime-side demonstrations ----
    print("\n" + "=" * 78)
    print("PRIME-SIDE COMPUTABILITY OF THE COEFFICIENTS (honest statement)")
    print("=" * 78)
    # (a) convergent prime sum at Re s = 2
    N = 10 ** 6
    sieve = bytearray(b'\x01') * (N + 1)
    sieve[0:2] = b'\x00\x00'
    for i in range(2, int(N ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = b'\x00' * (((N - i * i) // i) + 1)
    primes = [i for i in range(2, N + 1) if sieve[i]]
    zz2 = mp.mpf(0)
    for p in primes:
        pp = mp.mpf(p)
        zz2 -= mp.log(pp) / (pp ** 2 - 1)
    ref2 = mp.zeta(2, derivative=1) / mp.zeta(2)
    print(f"  zeta'/zeta(2) via prime sum sum_p log p/(p^2-1), p<=10^6 = {mp.nstr(zz2, 15)}")
    print(f"  mpmath zeta'/zeta(2)                                        = {mp.nstr(ref2, 15)}")

    # (b) NON-convergence of the C-RH2 'convergent' series  sum_p log p p^{-1/2} cos(t log p)
    t_ = 14.1347251417346937904572519835625
    print("\n  raw series S(x) = sum_{p<=x} log p * p^{-1/2} * cos(t log p),  t = gamma_1:")
    print("  (C-RH2 calls this 'convergent and computable' -- it is NOT convergent;"
          " |S| grows ~ sqrt(x))")
    for x in (10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7):
        S = mp.mpf(0)
        for p in primes:
            if p > x:
                break
            lp = mp.log(p)
            S += lp * mp.power(p, -mp.mpf('0.5')) * mp.cos(t_ * lp)
        print(f"    x = {x:>9}:  S = {mp.nstr(S, 10)}   (sqrt(x)/(t^2+1/4) = "
              f"{mp.nstr(mp.sqrt(x) / (t_ ** 2 + mp.mpf('0.25')), 5)})")
    print("  Conclusion: the unweighted prime series diverges; the coefficient values are the")
    print("  explicit-formula (functional-equation) analytic continuation, evaluated here via")
    print("  mpmath's Euler-Maclaurin zeta at s = 1/2 -- no zeros used anywhere.")

    # (c) convergent Dirichlet-side route to zeta(1/2): eta-series with Euler transform
    print("\n  zeta(1/2) from the convergent alternating eta-series (Euler transform):")
    s12 = mp.mpf('0.5')
    a = [mp.power(mp.mpf(i + 1), -s12) for i in range(80)]
    b = a[:]
    total = mp.mpf(0)
    for k in range(60):
        # forward-difference averaging (van Wijngaarden)
        for i in range(0, len(b) - 1 - k):
            b[i] = (b[i] + b[i + 1]) / 2
        total += b[0] / 2 ** (k + 1)
    eta = total
    zeta12 = eta / (1 - mp.power(2, 1 - s12))
    print(f"    eta(1/2) Euler-transformed = {mp.nstr(eta, 15)}")
    print(f"    zeta(1/2) = eta/(1-2^(1/2)) = {mp.nstr(zeta12, 15)}")
    print(f"    mpmath zeta(1/2)            = {mp.nstr(mp.zeta(s12), 15)}")

    # ---- moment dictionary vs verified zero data ----
    print("\n" + "=" * 78)
    print("MOMENT DICTIONARY CHECK:  e_j = gamma(j)/(gamma(0) j!) = e_j(1/gamma_k^2)")
    print("  vs zero power sums from the verified on-line zeros (zeros_1_1000.txt) + tail.")
    print("  (identity holds numerically because the first 1000 zeros are all on the line)")
    print("=" * 78)
    zs = []
    with open('/home/vstaln/riemann/tools/data/zeros_1_1000.txt') as f:
        for line in f:
            zs.append(mp.mpf(line.split()[1]))
    T = zs[-1]
    m1 = gam[1] / gam[0]
    m2 = m1 ** 2 - gam[2] / gam[0]           # e2 = (m1^2 - m2)/2 = gamma(2)/(2 gamma(0))
    e3 = gam[3] / (gam[0] * 6)
    m3 = (6 * e3 - m1 ** 3 + 3 * m1 * m2) / 2
    for k, (mref, name) in enumerate([(m1, 'm1'), (m2, 'm2'), (m3, 'm3')], start=1):
        part = sum(z ** (-2 * k) for z in zs)
        # tail: refined zero density N'(T) = (1/2pi) log(T/2pi):
        #   tail_k = (1/2pi) T^{1-2k} [ (log T - log 2pi)/(2k-1) + 1/(2k-1)^2 ]
        tail = (1 / (2 * PI)) * T ** (1 - 2 * k) * (
            (mp.log(T) - mp.log(2 * PI)) / (2 * k - 1) + 1 / (2 * k - 1) ** 2)
        print(f"  {name} from gamma: {mp.nstr(mref, 12)}   | partial(gamma<=gamma_1000) + tail: "
              f"{mp.nstr(part + tail, 12)}   | diff = {mp.nstr(mref - (part + tail), 4)}")

    print(f"\n[done in {time.time() - t0:.1f}s]")


if __name__ == '__main__':
    main()
