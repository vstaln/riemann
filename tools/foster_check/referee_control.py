import mpmath as mp
from mpmath import mpf, mpc
mp.mp.dps = 300

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

# EXACT control: D_control(z) = D(z) * (1 - 2Re(1/w) z + z^2/|w|^2) / (1 + z/g2^2),
# w = s2^2, s2 = alpha + 21.1i.  Division by (1+z/g2^2) is EXACT (g2 is a real zero).
def control_bk(alpha, g2=mpf('21.022039638771555')):
    s2 = mpc(alpha, mpf('21.1'))
    w = s2**2
    c = 2*mp.re(1/w); d = 1/abs(w)**2
    # D(z) = sum b_k z^k ;  mult by (1 - c z + d z^2):  P_k = b_k - c b_{k-1} + d b_{k-2}
    P = [mpf(0)]*(NB+3)
    for k in range(NB+1):
        P[k] += b[k]
        if k >= 1: P[k] -= c*b[k-1]
        if k >= 2: P[k] += d*b[k-2]
    # divide by (1 + z/g2^2):  Q_k + Q_{k-1}/g2^2 = P_k  ->  Q_k = P_k - Q_{k-1}/g2^2
    Q = [mpf(0)]*(NB+3)
    for k in range(NB+3):
        Q[k] = P[k] - (Q[k-1]/g2**2 if k >= 1 else mpf(0))
    return Q[:NB+1]

for alpha in [mpf('0.35'), mpf('0.05'), mpf('0.5'), mpf('0.01')]:
    bc = control_bk(alpha)
    mhc = moments_from_b(bc, RHO, M)
    ac = cf(mhc, M)
    bad = [i for i in range(1,41) if not (ac[i] > 0)]
    print("EXACT CONTROL alpha=%.2f: first non-positive a_k = %s" % (float(alpha), bad[0] if bad else "NONE (all a_1..a_40 > 0)"))
    if bad:
        print("    a_%d = %.4e ; a_1..a_6 = %s" % (bad[0], float(ac[bad[0]]), [mp.nstr(ac[i],5) for i in range(1,7)]))
