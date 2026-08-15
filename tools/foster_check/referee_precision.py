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

# (1) m_0-only perturbation at 1e-5 (zeros-route's m_0 error)
mhp = list(mh0); mhp[0] *= (1 + mpf('1.25e-5'))
ap = cf(mhp, M)
print("m_0 perturbed by 1.25e-5 (zeros-route m_0 error): first a_k moving >10%%:",
      min((i for i in range(1,41) if abs(ap[i]-a0[i]) > 0.1*abs(a0[i])), default=None))
for i in range(20, 36):
    print("   a_%d: base %.5f  with m0-err %.5f" % (i, float(a0[i]), float(ap[i])))

# (2) which route certifies what: full-profile perturbation mimicking each route
random.seed(7)
def profile_test(eps_hi, eps_m0, label):
    worst = {}
    for trial in range(5):
        u = [mpf(random.uniform(-1,1)) for _ in range(M+1)]
        mhp = [mh0[n]*(1+eps_hi*u[n]) for n in range(1,M+1)]
        mhp = [mh0[0]*(1+eps_m0*u[0])] + mhp
        ap = cf(mhp, M)
        for i in range(1,41):
            if abs(ap[i]-a0[i]) > 0.1*abs(a0[i]) + mpf('1e-300'):
                worst[i] = max(worst.get(i, mpf(0)), abs(ap[i]-a0[i])/max(abs(a0[i]),mpf('1e-300')))
    first = min(worst) if worst else None
    print("%s: first a_k moving >10%%: %s" % (label, first))

profile_test(mpf('1e-32'), mpf('1.25e-5'), "zeros-route profile (m_n~1e-32 n>=1, m_0~1.25e-5):")
profile_test(mpf('5e-16'), mpf('5e-16'), "b_txt-route profile (all ~5e-16):")

# (3) sign-certifiable range: find max n where sign is stable across ALL profiles
signs_ok = []
for i in range(1, 41):
    ok = all(ap[i] > 0 for ap in [a0])
    signs_ok.append((i, ok))
print("a_1..a_40 all > 0 in base (b_txt) run:", all(a0[i] > 0 for i in range(1,41)))
print("first negative in base run:", min((i for i in range(1,41) if not a0[i] > 0), default=None))
