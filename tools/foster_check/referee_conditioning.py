import mpmath as mp
from mpmath import mpf, mpc
import random
mp.mp.dps = 500

b = {}
for line in open('/home/vstaln/riemann/tools/foster_check/b.txt'):
    p = line.split(); b[int(p[0])] = mpf(p[1])
NB = max(b); RHO = mpf('199.79'); M = 40

def moments_from_b(b, RHO, M):
    bt = [b[k]*RHO**k for k in range(NB+1)]
    mh = [mpf(0)]*(M+1)
    for i in range(M+1):
        num = (i+1)*bt[i+1]; s = num
        for j in range(i): s -= mh[j]*bt[i-j]
        mh[i] = s/bt[0]
    return mh

def cf(mh, M):
    cur = list(mh[:M+1]); a = {}
    for i in range(1, M+1):
        if cur[0] == 0: break
        inv = [mpf(0)]*len(cur); inv[0] = 1/cur[0]
        for j in range(1, len(cur)):
            inv[j] = -sum(inv[t]*cur[j-t] for t in range(j))/cur[0]
        a[i] = inv[0]
        cur = inv[1:]
    return a

mh0 = moments_from_b(b, RHO, M)
a0 = cf(mh0, M)

# independent input: moments from zeros file (16-digit zeros, independent route)
zs = [mpf(l.split()[1]) for l in open('/home/vstaln/riemann/tools/data/zeros_1_1000.txt')]
def moments_from_zeros(zs, M, tail0=True):
    m = []
    for n in range(M+1):
        s = sum(z**(-2*n-2) for z in zs)
        if n == 0 and tail0:
            T = zs[-1]; s += (1/(2*mp.pi*T))*(mp.log(T/(2*mp.pi))+1)
        m.append(s)
    return [(-1)**n * m[n] * RHO**(n+1) for n in range(M+1)]

mhz = moments_from_zeros(zs, M)
az = cf(mhz, M)

print("== cross-check two INDEPENDENT inputs (b.txt 18-digit vs zeros-file 16-digit) ==")
print("n  a(b_txt)      a(zeros)      rel diff")
for i in range(1, 41):
    d = abs(a0[i]-az[i])/max(abs(a0[i]), mpf('1e-300'))
    flag = "  <-- DIVERGE" if d > mpf('0.1') else ""
    print("%2d %12.6f %12.6f %.1e%s" % (i, float(a0[i]), float(az[i]), float(d), flag))

print()
print("== perturbation: m_n -> m_n*(1+eps*u_n), find where a_k sign flips ==")
random.seed(12345)
for eps in [mpf('1e-16'), mpf('1e-32'), mpf('1e-64'), mpf('1e-128')]:
    worst = {}
    for trial in range(5):
        u = [mpf(random.uniform(-1,1)) for _ in range(M+1)]
        mhp = [mh0[n]*(1+eps*u[n]) for n in range(M+1)]
        ap = cf(mhp, M)
        for i in range(1,41):
            if abs(ap[i]-a0[i]) > 0.1*abs(a0[i]) + mpf('1e-300'):
                worst[i] = max(worst.get(i, mpf(0)), abs(ap[i]-a0[i])/max(abs(a0[i]),mpf('1e-300')))
    if worst:
        first = min(worst)
        print("eps=%.0e: first a_k moving >10%% at k=%d (rel change %.1e)" % (float(eps), first, float(worst[first])))
    else:
        print("eps=%.0e: no a_k moved >10%%" % float(eps))
