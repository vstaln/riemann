# The family-averaged legality of the Gevrey taper for Rem 7.2(iii):
# For the family average over chi mod q, the prime side M[P_X,P_X] is EXACTLY diagonal
# (orthogonality), so the off-diagonal O_1 (which forced X <= T^{1-eps} per character)
# is ABSENT.  The remaining obstruction is the zero-side tail (Prop 4.2):
#   ||E|| <= X^{1/2} log(4T) D0^{-2} * [taper factor]
# where the taper factor is exp(-c' D0^{1/s}) for a Gevrey window (vs the paper's C^3
# taper which has NO such factor, giving ||E|| ~ q^{lambda/2} polylog -> oo in the q-aspect).
#
# With D0 = T^{1/2} = (log q)^{c/2} and X = q^lambda (family: X < q so lambda < 1),
# the Gevrey factor exp(-c' (log q)^{c/(2s)}) kills q^{lambda/2} iff c/(2s) * (some positive) > lambda/2 * log q
# i.e. (log q)^{c/(2s)-1} * c' > lambda/2 * log 2  --  needs c/(2s) >= 1.
# So s <= c/2 is the condition. With s = 1/2 (analytic window, maximal Gevrey class):
#   c >= 1 suffices.  T = (log q)^1, (log q)^2, (log q)^3 all work.
import math

def ell(q, T):
    # ell_{1,chi} = ln(qT/2pi) + 2ln2 - 1
    return math.log(q*T/(2*math.pi)) + 2*math.log(2) - 1

def lambda_f(q, T, eps=0.01):
    # family legal bandwidth: X = q^{1-eps}, so lambda = (1-eps) log q / ell
    return (1-eps)*math.log(q)/ell(q, T)

def tail_gevrey(q, T, D0, c=2.0, s=0.5):
    # ||E|| <= X^{1/2} log(4T) D0^{-2} * exp(-c D0^{1/s})   (Gevrey factor)
    X = math.exp(ell(q,T))  # lambda=1 upper bound; X = q^lambda <= q
    # For lambda<1 use X = q^lambda; conservative: X ~ q
    return math.sqrt(X) * math.log(4*T) / (D0*D0) * math.exp(-c * D0**(1/s))

def tail_c3(q, T, D0):
    # paper C^3: ||E|| <= X^{1/2} log(4T) D0^{-2} * (no exp factor; C1 r^-2 only)
    X = math.exp(ell(q,T))
    return math.sqrt(X) * math.log(4*T) / (D0*D0)

print("Family-average legality of the Gevrey taper, T=(log q)^c:")
print(f"{'q':>6} {'c':>2} {'T':>6} {'D0':>6} {'lambda_F':>8} {'tail C3':>10} {'tail Gevrey':>12} {'ok?':>4}")
for q in [101, 1009, 10007, 100003]:
    for c in [1,2,3]:
        T = math.log(q)**c
        D0 = math.sqrt(T)
        lf = lambda_f(q,T)
        t3 = tail_c3(q,T,D0)
        tg = tail_gevrey(q,T,D0)
        # relative to tr bG ~ N(T,2T) ~ T/(2pi) ell ~ (log q)^c/(2pi) * ell
        N = T*ell(q,T)/(2*math.pi)
        ok = tg < 0.01*N  # tail < 1% of trace
        print(f"{q:>6} {c:>2} {T:>6.1f} {D0:>6.2f} {lf:>8.4f} {t3/N:>10.2e} {tg/N:>12.2e} {('YES' if ok else 'no'):>4}")
