"""Independent high-precision check of |Z(gamma_i)| at LMFDB ordinates.

Question: is max |Z(gamma_i)| ~ 4.67e-6 (f64 Euler-Maclaurin, K=10, N=ceil(1.6t/2pi))
plausible truncation error, or a bug (e.g. LMFDB ordinates not actually zeros,
or the EM implementation has an error)?

Plan:
  A) true |Z(gamma)| at the LMFDB ordinates (mpmath, dps=45)  -- should be ~0
  B) EM(K=10, N=ceil(1.6t/2pi)) computed in mpmath at dps=45 at the same t
     -> isolates PURE EM TRUNCATION error (no f64 rounding)
  C) analytic estimate of the first neglected Bernoulli term magnitude
  D) f64 result for comparison (from the Rust tool's bracket output: 4.67e-6)
"""
import math
import mpmath as mp

mp.mp.dps = 45

# ---- LMFDB ordinates as exact strings (34 digits) ----
pairs = []
for line in open('tools/data/zeros_1_1000.txt'):
    p = line.split()
    if len(p) >= 2:
        pairs.append((int(p[0]), p[1]))

def zeta_em(s, N, K):
    """Euler-Maclaurin zeta at s=1/2+it with mpmath. Returns complex."""
    s = mp.mpc(s)
    N = int(N)
    total = mp.mpc(0)
    for n in range(1, N):
        total += mp.power(n, -s)
    total += mp.power(N, 1 - s) / (s - 1)
    total += mp.mpf(1) / 2 * mp.power(N, -s)
    # Bernoulli terms B_{2k}/(2k)! * (s)_{2k-1} * N^{-s-2k+1}
    for k in range(1, K + 1):
        b = mp.bernoulli(2 * k) / mp.factorial(2 * k)
        poch = mp.mpf(1)
        for j in range(2 * k - 1):
            poch *= (s + j)
        total += b * poch * mp.power(N, -s - 2 * k + 1)
    return total

def theta_mp(t):
    t = mp.mpf(t)
    # theta(t) = Im log Gamma(1/4 + it/2) - (t/2) log pi
    return mp.im(mp.loggamma(mp.mpc(1, 2) / 4 + mp.mpc(0, t / 2))) - (t / 2) * mp.log(mp.pi)

def z_mp(t):
    s = mp.mpc(mp.mpf(1) / 2, t)
    zeta = mp.zeta(s)
    th = theta_mp(t)
    # Z = Re(e^{i theta} zeta) = Re(zeta)*cos(theta) - Im(zeta)*sin(theta)
    return mp.re(zeta) * mp.cos(th) - mp.im(zeta) * mp.sin(th)

# --- A) true |Z| at ordinates ---
max_true = mp.mpf(0)
max_true_i = 0
worst_ten = []
for (i, gstr) in pairs:
    t = mp.mpf(gstr)
    z = z_mp(t)
    a = abs(z)
    if a > max_true:
        max_true = a
        max_true_i = i
    worst_ten.append((a, i))
worst_ten.sort(reverse=True)
print("A) true |Z(gamma_i)| (mpmath 45 dps): max over i=1..1000 =", mp.nstr(max_true, 8), "at i =", max_true_i)
print("   top-5 |Z|:", [(i, mp.nstr(a, 5)) for a, i in worst_ten[:5]])

# --- B) pure EM truncation error at the same ordinates ---
max_trunc = mp.mpf(0)
max_trunc_i = 0
for (i, gstr) in pairs:
    t = mp.mpf(gstr)
    N = int(math.ceil(1.6 * float(t) / (2 * math.pi)))
    zeta_em_val = zeta_em(mp.mpc(mp.mpf(1) / 2, t), N, 10)
    th = theta_mp(t)
    zem = mp.re(zeta_em_val) * mp.cos(th) - mp.im(zeta_em_val) * mp.sin(th)
    # true Z:
    ztrue = z_mp(t)
    a = abs(zem - ztrue)
    if a > max_trunc:
        max_trunc = a
        max_trunc_i = i
print("B) |EM(K=10,N=ceil(1.6t/2pi)) - true Z| max over i=1..1000 =", mp.nstr(max_trunc, 6), "at i =", max_trunc_i)

# --- C) analytic size of first neglected term (k=11) at the max-truncation t ---
tmax = float(pairs[max_trunc_i - 1][1])
Nmax = int(math.ceil(1.6 * tmax / (2 * math.pi)))
t = mp.mpf(tmax)
N = Nmax
s = mp.mpc(mp.mpf(1) / 2, t)
neg_terms = []
for k in range(1, 15):
    b = abs(mp.bernoulli(2 * k) / mp.factorial(2 * k))
    poch = mp.mpf(1)
    for j in range(2 * k - 1):
        poch *= abs(s + j)
    term = b * poch * abs(mp.power(N, -s - 2 * k + 1))
    neg_terms.append((k, term))
print("C) at t=%.1f (i=%d, N=%d): |Bernoulli term k|:" % (tmax, max_trunc_i, Nmax))
for k, term in neg_terms:
    print("   k=%2d: %.3e" % (k, float(term)))
# also at i=500 (t ~ 811)
t500 = float(pairs[499][1])
N500 = int(math.ceil(1.6 * t500 / (2 * math.pi)))
print("   (for comparison: i=500 t=%.1f N=%d)" % (t500, N500))

# --- D) sanity: EM(K=10) vs EM(K=14) at a few ordinates to bound remainder ---
print("D) EM(K=10) vs EM(K=14) at ordinates (should bound the truncation):")
for (i, gstr) in [pairs[99], pairs[299], pairs[499], pairs[999]]:
    t = mp.mpf(gstr)
    N = int(math.ceil(1.6 * float(t) / (2 * math.pi)))
    z10 = zeta_em(mp.mpc(mp.mpf(1) / 2, t), N, 10)
    z14 = zeta_em(mp.mpc(mp.mpf(1) / 2, t), N, 14)
    print("   i=%4d: |zeta_EM10 - zeta_EM14| = %.3e   (true zeta err ~ 1e-45)" % (i, float(abs(z10 - z14))))
