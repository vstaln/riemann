"""Redo: pure EM truncation error with N = max(10, ceil(1.6t/2pi)), K=10 (matches zeta-rs)."""
import math
import mpmath as mp
mp.mp.dps = 45

pairs = []
for line in open('tools/data/zeros_1_1000.txt'):
    p = line.split()
    if len(p) >= 2:
        pairs.append((int(p[0]), p[1]))

def zeta_em(s, N, K):
    s = mp.mpc(s)
    N = int(N)
    total = mp.mpc(0)
    for n in range(1, N):
        total += mp.power(n, -s)
    total += mp.power(N, 1 - s) / (s - 1)
    total += mp.mpf(1) / 2 * mp.power(N, -s)
    for k in range(1, K + 1):
        b = mp.bernoulli(2 * k) / mp.factorial(2 * k)
        poch = mp.mpf(1)
        for j in range(2 * k - 1):
            poch *= (s + j)
        total += b * poch * mp.power(N, -s - 2 * k + 1)
    return total

def theta_mp(t):
    t = mp.mpf(t)
    return mp.im(mp.loggamma(mp.mpc(1, 2) / 4 + mp.mpc(0, t / 2))) - (t / 2) * mp.log(mp.pi)

def z_mp(t):
    zeta = mp.zeta(mp.mpc(mp.mpf(1) / 2, t))
    th = theta_mp(t)
    return mp.re(zeta) * mp.cos(th) - mp.im(zeta) * mp.sin(th)

def N_tool(t):
    return max(10, int(math.ceil(1.6 * float(t) / (2 * math.pi))))

# pure EM truncation error at every ordinate (K=10, N_tool)
rows = []
for (i, gstr) in pairs:
    t = mp.mpf(gstr)
    N = N_tool(t)
    zem = zeta_em(mp.mpc(mp.mpf(1) / 2, t), N, 10)
    th = theta_mp(t)
    z = mp.re(zem) * mp.cos(th) - mp.im(zem) * mp.sin(th)
    zt = z_mp(t)
    rows.append((abs(z - zt), i, float(t), N))

rows.sort(reverse=True)
print("pure EM truncation error |EM10 - true Z|, N=max(10,ceil(1.6t/2pi)), K=10:")
for err, i, t, N in rows[:8]:
    print("   i=%4d t=%9.3f N=%3d  err=%.3e" % (i, t, N, float(err)))
print("max over i<=500:", mp.nstr(rows[0][0], 6))
# how many exceed 1e-6, 5e-6?
for thr in (1e-6, 2e-6, 5e-6):
    print("  count with err > %.0e: %d" % (thr, sum(1 for r in rows if r[0] > thr)))
# K=14 comparison at the top few
print("K=10 vs K=14 at top error ordinates:")
for err, i, t, N in rows[:5]:
    z14 = zeta_em(mp.mpc(mp.mpf(1) / 2, mp.mpf(t)), N, 14)
    th = theta_mp(t)
    z14z = mp.re(z14) * mp.cos(th) - mp.im(z14) * mp.sin(th)
    zt = z_mp(t)
    print("   i=%4d t=%.3f: |EM10-true|=%.3e  |EM14-true|=%.3e" % (i, t, float(err), float(abs(z14z - zt))))
