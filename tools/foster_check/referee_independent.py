import mpmath as mp
from mpmath import mpf, mpc
mp.mp.dps = 220

# ---------- load b_k (repo tower) ----------
b = {}
for line in open('/home/vstaln/riemann/tools/foster_check/b.txt'):
    p = line.split(); b[int(p[0])] = mpf(p[1])
NB = max(b)
RHO = mpf('199.79')

def cf_from_mh(mh, M):
    """regular C-fraction of S(w)=sum mh_n w^n: a_i = 1/cur[0]; cur <- (1/cur - a_i)/w"""
    cur = list(mh[:M+1]); a = {}
    for i in range(1, M+1):
        if cur[0] == 0: break
        inv = [mpf(0)]*len(cur); inv[0] = 1/cur[0]
        for j in range(1, len(cur)):
            inv[j] = -sum(inv[t]*cur[j-t] for t in range(j))/cur[0]
        a[i] = inv[0]
        cur = inv[1:]
        if len(cur) == 0: break
    return a

def moments_from_b(b, RHO, M):
    """mh_n = (-1)^n m_n rho^{n+1} via series division N~/D~ (note's scaling)"""
    bt = [b[k]*RHO**k for k in range(NB+1)]
    mh = [mpf(0)]*(M+1)
    for i in range(M+1):
        num = (i+1)*bt[i+1]; s = num
        for j in range(i): s -= mh[j]*bt[i-j]
        mh[i] = s/bt[0]
    return mh

M = 40
mh = moments_from_b(b, RHO, M)
m = lambda n: mh[n]*(1 if n%2==0 else -1)/RHO**(n+1)
print("== REAL data, b_k tower ==")
print("m_0 =", mp.nstr(m(0),20), " expect 0.02310499311541837")
print("m_1 =", mp.nstr(m(1),12), " expect ~3.71726e-5")
print("m_2 =", mp.nstr(m(2),12), " expect ~1.44174e-7")
print("b1/b0 =", mp.nstr(b[1]/b[0], 20))

# independent route: moments from zero file
zs = [mpf(l.split()[1]) for l in open('/home/vstaln/riemann/tools/data/zeros_1_1000.txt')]
for n in range(9):
    s = sum(z**(-2*n-2) for z in zs)
    if n==0:
        T = zs[-1]
        s += (1/(2*mp.pi*T))*(mp.log(T/(2*mp.pi))+1)
    print("  m_%d vs zeros-file rel diff: %.2e" % (n, abs((m(n)-s)/s)))

a = cf_from_mh(mh, M)
print("a_1..a_12:", [mp.nstr(a[i],8) for i in range(1,13)])
print("a_13..a_18:", [mp.nstr(a[i],6) for i in range(13,19)])
print("a_19..a_30:", [mp.nstr(a[i],5) for i in range(19,31)])
print("a_31..a_40:", [mp.nstr(a[i],4) for i in range(31,41)])
print("ALL a_1..a_40 > 0 (200 digits):", all(a[i] > 0 for i in range(1,41)))

# ---------- f64 collapse point ----------
import struct
def f64(v): return struct.unpack('d', struct.pack('d', float(v)))[0]
import numpy as np
def cf_f64(mh):
    cur = [float(x) for x in mh[:41]]; a = {}
    for i in range(1,41):
        inv = [0.0]*len(cur); inv[0] = 1.0/cur[0]
        for j in range(1,len(cur)):
            inv[j] = -sum(inv[t]*cur[j-t] for t in range(j))/cur[0]
        a[i] = inv[0]; cur = inv[1:]
    return a
mh64 = [f64(x) for x in mh]
af = cf_f64(mh64)
first_bad = min((i for i in range(1,41) if not (af[i] > 0)), default=None)
print("f64: first non-positive a_k:", first_bad, "(a_%d=%.3e)" % (first_bad, af[first_bad]) if first_bad else "none")
print("f64 vs mpmath a_1..a_12 rel err:", max(abs((af[i]-float(a[i]))/float(a[i])) for i in range(1,13)))
print("f64 vs mpmath a_13..a_18 rel err:", max(abs((af[i]-float(a[i]))/float(a[i])) for i in range(13,19)))

# ---------- CONTROL: plant gamma_2 -> alpha +- 21.1 i (off-line zero pair, RH FALSE) ----------
zs_all = [mpf(l.split()[1]) for l in open('/home/vstaln/riemann/tools/data/zeros_1_1000.txt')]
def control_moments(alpha, gamma2_idx=1, keep_g2=False):
    """m_n = sum_{j != g2} g_j^{-2n-2} + 2(-1)^{n+1} Re[s^{-2n-2}], s = alpha + 21.1i"""
    s2 = mpc(alpha, mpf('21.1'))
    g2 = zs_all[gamma2_idx]
    mc = []
    for n in range(M+1):
        tot = sum(z**(-2*n-2) for z in zs_all)  # all real zeros
        if n == 0:
            T = zs_all[-1]
            tot += (1/(2*mp.pi*T))*(mp.log(T/(2*mp.pi))+1)
        if not keep_g2:
            tot -= g2**(-2*n-2)
        tot += 2*((-1)**(n+1))*mp.re(s2**(-2*n-2))
        mc.append(tot)
    return mc

for alpha in [mpf('0.35'), mpf('0.05'), mpf('0.5')]:
    mc = control_moments(alpha)
    mhc = [(-1)**n * mc[n] * RHO**(n+1) for n in range(M+1)]
    ac = cf_from_mh(mhc, M)
    bad = [i for i in range(1,41) if not (ac[i] > 0)]
    print("CONTROL alpha=%.2f (RH FALSE): first non-positive a_k = %s" % (float(alpha), bad[0] if bad else "NONE (a_1..a_40 all > 0)"))
    if bad: print("    a_%d = %.4e" % (bad[0], float(ac[bad[0]])))
    else: print("    a_1..a_12:", [mp.nstr(ac[i],5) for i in range(1,13)])
    # stronger plant
mc2 = control_moments(mpf('0.35'), keep_g2=True)
mhc2 = [(-1)**n * mc2[n] * RHO**(n+1) for n in range(M+1)]
ac2 = cf_from_mh(mhc2, M)
bad2 = [i for i in range(1,41) if not (ac2[i] > 0)]
print("CONTROL additive (keep g_2, add planted pair) alpha=0.35: first non-positive =", bad2[0] if bad2 else "NONE")

# finite real-atom truncation sanity (theorem: Stieltjes -> all positive before termination)
for K in [10, 40]:
    mk = [sum(z**(-2*n-2) for z in zs_all[:K]) for n in range(M+1)]
    mhk = [(-1)**n * mk[n] * RHO**(n+1) for n in range(M+1)]
    ak = cf_from_mh(mhk, M)
    print("REAL truncation K=%d: a_1..a_%d positive: %s (terminates at %d)" % (K, M, all(ak[i]>0 for i in range(1,41)), len(ak)))
