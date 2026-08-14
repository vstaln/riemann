#!/usr/bin/env python3
"""Fast analytic checks for the Li structure audit (final, unbuffered)."""
import mpmath as mp, sys
mp.mp.dps = 60

def P(s):
    print(s, flush=True)

# ================= probe lambda_n =================
def lambda_n_probe(N, dps=60):
    mp.mp.dps = dps
    M = N + 2
    a = [mp.mpf(0)] * (M + 1)
    for m in range(1, M + 1):
        g = mp.stieltjes(m - 1)
        a[m] = ((-1) ** (m - 1)) * g / mp.fac(m - 1)
    b = [mp.mpf(0)] * (M + 1)
    for m in range(1, M + 1):
        s = mp.mpf(0)
        for k in range(1, m):
            s += k * b[k] * a[m - k]
        b[m] = a[m] - s / m
    L = mp.log(mp.pi)
    c = [mp.mpf(0)] * (M + 1)
    for m in range(M + 1):
        if m == 0:
            c[m] = -mp.log(2) - L / 2 + mp.log(mp.pi) / 2
        else:
            hm = ((-1) ** (m - 1)) / m
            if m == 1:
                hm -= L / 2
            hm += mp.polygamma(m - 1, mp.mpf(0.5)) / (mp.fac(m) * (2 ** m))
            c[m] = b[m] + hm
    lam = [mp.mpf(0)] * (N + 1)
    for n in range(1, N + 1):
        tot = mp.mpf(0)
        for k in range(1, n + 1):
            tot += c[k] * mp.binomial(n - 1, k - 1)
        lam[n] = n * tot
    return lam

lam = lambda_n_probe(40)
P("== A. probe lambda_1..lambda_12 ==")
for n in range(1, 13):
    P(f"  lambda_{n:<2d} = {mp.nstr(lam[n], 20)}")
cf = 1 + mp.euler / 2 - mp.log(4 * mp.pi) / 2
P("lambda_1 closed form: " + mp.nstr(cf, 20) + "  match=" + mp.nstr(abs(lam[1] - cf), 15))

# ================= theta identity =================
P("== B. theta_gamma = pi - 2 atan(2 gamma) = arg(1-1/rho) ==")
def theta_of(g):
    return mp.pi - 2 * mp.atan(2 * g)
for k in [1, 2, 10, 100]:
    z = mp.zetazero(k)
    g = mp.im(z)
    d = abs(theta_of(g) - mp.arg(1 - 1 / z))
    P(f"  gamma_{k}: diff = {mp.nstr(d, 18)}")
n, g = 7, mp.zetazero(6).imag
th = theta_of(g)
P("4 sin^2(n theta/2) == 2(1-cos n theta): " + mp.nstr(abs(4 * mp.sin(n * th / 2) ** 2 - 2 * (1 - mp.cos(n * th))), 25))
rho = mp.mpc(0.5, g)
xr = 1 - 1 / (2 * rho * (1 - rho))
P("x_rho = 1-1/(2 rho(1-rho)) == cos(theta_rho): diff = " + mp.nstr(abs(mp.re(xr) - mp.cos(th)), 25))
P("1 - T_n(x_rho) == 1 - cos(n theta): diff = " + mp.nstr(abs(1 - mp.chebyt(n, mp.re(xr)) - (1 - mp.cos(n * th))), 25))

# ================= Toeplitz structure =================
P("== C. Toeplitz: {2-2cos(n theta)} NOT positive type;  {cos(n theta_gamma)} PSD per-zero ==")
th = mp.mpf("1.0")
A11 = 2 - 2 * mp.cos(0)
A12 = 2 - 2 * mp.cos(1 * th)
P("det [[2-2cos0, 2-2cost],[2-2cost, 2-2cos0]] = " + mp.nstr(A11 * A11 - A12 * A12, 20))
aa = [mp.mpf(x) for x in (0.3, -0.7, 0.5, 1.1)]
g = mp.zetazero(50).imag
thg = theta_of(g)
Q = sum(aa[j] * aa[l] * mp.cos((j - l) * thg) for j in range(4) for l in range(4))
sq = abs(sum(aa[j] * mp.e ** (mp.j * j * thg) for j in range(4))) ** 2
P(f"per-zero QF (gamma_50): Q = {mp.nstr(Q, 12)}  |sum a_j e^ij theta|^2 = {mp.nstr(sq, 12)}")

# ================= B-L Weil form =================
P("== D. B-L: ghat_n(s) = 1-(1-1/s)^n ; factorization; Mellin check; full spectrum ==")
def ghat(s, n):
    return 1 - (1 - 1 / s) ** n
s = mp.mpc(1.7, 0.9)
P("identity (1-1/s)(1-1/(1-s)) = 1 : " + mp.nstr((1 - 1 / s) * (1 - 1 / (1 - s)) - 1, 25))
for n in [3, 7]:
    lhs = ghat(s, n) * ghat(1 - s, n)
    rhs = ghat(s, n) + ghat(1 - s, n)
    P(f"factorization (n={n}): |prod - sum| = {mp.nstr(abs(lhs - rhs), 25)}")

def g_n(x, n):
    tot = mp.mpf(0)
    for j in range(1, n + 1):
        tot += mp.binomial(n, j) * (mp.log(x) ** (j - 1)) / mp.fac(j - 1)
    return tot

def mellin_g(n, s):
    h = lambda u: g_n(mp.e ** (-u), n) * mp.e ** (-s * u)
    return mp.quad(h, [0, mp.inf])

for n in [1, 4, 8]:
    for s in [mp.mpc(0.6, 1.3), mp.mpc(0.85, -2.2)]:
        mt = mellin_g(n, s)
        P(f"n={n} s={s}: Mellin-int={mp.nstr(mt, 10)}  closed={mp.nstr(ghat(s, n), 10)}  diff={mp.nstr(abs(mt - ghat(s, n)), 6)}")

P("composed h_n = g_n * x^-1 g_n(x^-1):  hhat(1/2+it) full support, decay ~ t^-2:")
n = 5
for t in [1, 5, 20, 100, 500]:
    hh = ghat(mp.mpc(0.5, t), n) * ghat(mp.mpc(0.5, -t), n)
    P(f"  t={t:<5d} |hhat(1/2+it)| = {mp.nstr(abs(hh), 10)}   t^-2 = {(1.0/t)**2:.2e}")

# ================= Weil pairing (the key check) =================
P("== E. Weil pairing:  lambda_n = (1/2) sum_rho ghat_n(rho) ghat_n(1-rho)  ==")
P("   computing first 1500 zeros (cache)...")
import json
try:
    with open("/tmp/zeros1500.json") as f:
        gam = json.load(f)
    gam = [mp.mpf(x) for x in gam]
    P("   loaded from cache")
except Exception:
    gam = []
    for k in range(1, 1501):
        gam.append(mp.im(mp.zetazero(k)))
        if k % 300 == 0:
            P(f"   ... {k} zeros")
    with open("/tmp/zeros1500.json", "w") as f:
        json.dump([str(x) for x in gam], f)

def weil_pairing(n, ng):
    tot = mp.mpf(0)
    for k in range(ng):
        rho = mp.mpc(0.5, gam[k])
        tot += ghat(rho, n) * ghat(1 - rho, n)
    return 2 * tot  # pairs {rho, 1-rho} both counted

def zerosum_lambda(n, ng):
    tot = mp.mpf(0)
    for k in range(ng):
        g = gam[k]
        th = theta_of(g)
        tot += 2 * (1 - mp.cos(n * th))
    return tot

P("partial sums vs probe (convergence in N):")
for n in [1, 2, 3, 5, 10]:
    line = f"  n={n:<3d} "
    for ng in [200, 500, 1000, 1500]:
        wp = weil_pairing(n, ng) / 2
        line += f"N={ng}:{mp.nstr(wp, 7)} "
    P(line + f"  probe={mp.nstr(lam[n], 7)}")
P("zero-sum lambda_n partial sums:")
for n in [1, 2, 3, 5, 10]:
    line = f"  n={n:<3d} "
    for ng in [200, 500, 1000, 1500]:
        line += f"N={ng}:{mp.nstr(zerosum_lambda(n, ng), 7)} "
    P(line + f"  probe={mp.nstr(lam[n], 7)}")

# tail-bound sanity: sum_{k>N} n^2/(2 gamma_k^2)
P("tail bound check: sum_{k>1500} n^2/(2 gamma^2)  (upper bound for the truncation error):")
gN = gam[-1]
for n in [1, 5, 10]:
    est = n ** 2 / (2 * gN) * mp.log(gN) / (2 * mp.pi)  # ~ (1/2pi) int (log t)/t^2 dt from gN
    P(f"  n={n}: est tail <= {mp.nstr(est, 6)}")

# ================= Suzuki norm (cheap version) =================
P("== F. Suzuki G_n: direct L2 integral shape check (N=200 zeros, dps=30) ==")
mp.mp.dps = 30
gam200 = [mp.mpf(x) for x in json.load(open("/tmp/zeros1500.json"))[:200]]

def xi(s):
    if abs(s) < mp.mpf("1e-30"):
        return mp.mpf("0.5")
    if abs(s - 1) < mp.mpf("1e-30"):
        return mp.mpf("0.5")
    return mp.mpf(0.5) * s * (s - 1) * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)

def xi_prime(s):
    h = mp.mpc("1e-5", "1e-5")
    return (xi(s + h) - xi(s - h)) / (2 * h)

def H_n(s, n, ng):
    tot = mp.mpc(0)
    for k in range(ng):
        rho = mp.mpc(0.5, gam200[k])
        tot += (1 - (1 - 1 / rho) ** n) / (s - rho)
    xs = xi(s)
    xp = xi_prime(s)
    return xs * tot / (xs + xp)

def G2_integral(n, R, ng):
    import math
    # composite Simpson on a grid finer than zero spacing near low t; skip near-poles
    N = 4000
    a, b = -R, R
    h = (b - a) / N
    tot = mp.mpf(0)
    for i in range(N + 1):
        t = a + i * h
        if i == 0 or i == N:
            w = mp.mpf(1) / 3
        elif i % 2 == 1:
            w = mp.mpf(4) / 3
        else:
            w = mp.mpf(2) / 3
        s = mp.mpc(0.5, -t)
        H = H_n(s, n, ng)
        tot += w * abs(H) ** 2
    return tot * h

for n in [1, 2]:
    for R in [30, 100]:
        I = G2_integral(n, R, 200)
        P(f"n={n}: (1/2pi) int_-{R}^{R} |G_n|^2 dt ~ {mp.nstr(I / (2 * mp.pi), 6)}   probe lambda_n = {mp.nstr(lam[n], 6)}")

# H_n zero-sum convergence in N
s0 = mp.mpc(1.4, 0.6)
for n in [1, 2]:
    h200 = H_n(s0, n, 200)
    h150 = H_n(s0, n, 150)
    P(f"H_n convergence at s={s0} (n={n}): |N=150 - N=200| = {mp.nstr(abs(h200 - h150), 8)}")

mp.mp.dps = 60
P("DONE.")
