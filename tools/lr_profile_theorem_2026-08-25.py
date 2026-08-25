"""lr-profile type-separation theorem — closed-form verification.

Convention: L_R(s) = (log R)'' = -Sum_{p in P} 1/(s-p)^2 + Sum_{m in M} 1/(s-m)^2
for zeta_planted = zeta_true * R (zeros added at P, removed at M). This is the
convention of turan-probe-2026-08-25.md and zigzag-proof-attempt-2026-08-25.md
(verified to 1.3e-51; matches FALSE=-2.77653 at sigma=0.3). The mission text's
stated sign (Sum_P - Sum_M) is the negative; all sign-STRUCTURE and
type-separation claims are convention-invariant.

Exact pair contribution (both conjugate points, real part) at s=sigma+i t0,
pair {a+i*tau, a-i*tau}:  (x^2-y1^2)/(x^2+y1^2)^2 + (x^2-y2^2)/(x^2+y2^2)^2
with x=sigma-a, y1=t0-tau, y2=t0+tau.

OFF (beta=0.9):  P={0.9,0.1}+-i*t0, M={0.5}+-i*t0   -> L_OFF = -2 pairs at 0.9,0.1 +1 pair at 0.5
LINE (delta=0.3): P={0.5}+-i(t0+delta), M={0.5}+-i*t0 -> L_LINE = -pair(0.5,t0+delta) + pair(0.5,t0)

Run: uv run --with mpmath,sympy python3 tools/lr_profile_theorem_2026-08-25.py
"""
import sympy as sp
import mpmath as mp

# ---------------- exact rational core ----------------
s, a, c, d = sp.symbols('s a c d', positive=True)

# --- OFF: B(s) = 1/(s-1/2)^2 - 1/(s-b)^2 - 1/(s-(1-b))^2, b=1/2+c, in s = 1/2 + a
# B = 1/a^2 - 1/(a-c)^2 - 1/(a+c)^2   ; numerator (as function of a, c):
num_off = sp.factor((a**2 - c**2)**2 - 2*a**2*(a**2 + c**2))  # over a^2 (a^2-c^2)^2
print('OFF numerator (a^2-c^2)^2 - 2a^2(a^2+c^2) =', sp.factor(num_off))
# numerator = -a^4 - 4 c^2 a^2 + c^4 ; sign determined by w=a^2 vs root  c^2(sqrt(5)-2)
r = sp.sqrt(sp.sqrt(5) - 2)
w = sp.symbols('w', positive=True)
num_w = -w**2 - 4*c**2*w + c**4
roots = sp.solve(num_w, w)
print('roots in w=a^2:', [sp.nsimplify(sp.simplify(x/c**2)) for x in roots],
      '  -> positive root = c^2*(sqrt(5)-2) =', sp.simplify(roots[0]/c**2))
assert sp.simplify(roots[0] - c**2*r**2) == 0, 'crossing a^2 = c^2(sqrt5-2)'

# sign of numerator polynomial: verify num_w > 0  <=>  w < c^2 r^2  (symbolic, m arbitrary)
m = sp.symbols('m', positive=True)      # w = m*c^2, m in (0, 1)
num_m = num_w.subs(w, m*c**2)/c**4      # = -m^2 - 4m + 1
print('num in m = -m^2 - 4m + 1 ;  zero at m =', sp.solve(num_m, m), ' (=-2+sqrt5), compare r^2 =', sp.simplify(r**2))
assert sp.simplify(sp.nsimplify(-2 + sp.sqrt(5)) - r**2) == 0
print('PROVEN: B_OFF(1/2+a) sign = sign(-w^2 - 4c^2 w + c^4),  zero at |a| = c*sqrt(sqrt5-2)')

# monotonicity of B on (1-b, crossing): a in (-c, -c*r);  B'(s) = -2/a^3 + 2/(a+c)^3 + 2/(a-c)^3
# lower bound: 2/|a|^3 - 2/|a-c|^3  (2/(a+c)^3 >= 0), |a|<=c, |a-c|>= (1+r)c
mono = sp.simplify(2/c**3 - 2/((1+r)*c)**3)
print('B\' lower bound (2/c^3)(1 - 1/(1+r)^3) =', sp.nsimplify(sp.simplify(mono*c**3)), '> 0')
assert sp.simplify(mono*c**3) > 0
print('PROVEN: B strictly increasing on (1-b, 1/2 - c*r), symmetric on (1/2+c*r, b)')

# exact boundary values at beta=9/10 (c=2/5), sigma=0.3055 and 0.3058
c5 = sp.Rational(2, 5)
Bsig = lambda st: sp.nsimplify(1/sp.Rational(2*st-1, 2)**2 - 1/sp.Rational(st, 1)**2
                               if False else
                               (1/(st-sp.Rational(1,2))**2 - 1/(st-sp.Rational(1,10))**2 - 1/(st-sp.Rational(9,10))**2))
B3055 = sp.nsimplify(Bsig(sp.Rational(3055,10000)))
B3058 = sp.nsimplify(Bsig(sp.Rational(3058,10000)))
print('B_OFF(0.3055) =', sp.N(B3055, 12), '  B_OFF(0.3058) =', sp.N(B3058, 12))
err_bound = sp.Rational(3, 4)*1/sp.Rational(141347,10000)**2   # 3/(4 T^2), T > 14.1347
print('far-term error bound 3/(4T^2) with T>14.1347 =', sp.N(err_bound, 12))
assert B3055 < -err_bound and B3058 > err_bound

# --- LINE: main(u;d) = d^2 (3u^2+d^2)/(u^2 (u^2+d^2)^2),  u = sigma-1/2 in (-1/2,1/2)
u, delta = sp.symbols('u delta', positive=True)
main = sp.simplify(1/u**2 - (u**2 - delta**2)/(u**2 + delta**2)**2)
print('LINE main part =', sp.factor(main))
assert sp.simplify(main - delta**2*(3*u**2+delta**2)/(u**2*(u**2+delta**2)**2)) == 0
# decreasing in w=u^2: d/dw log main = -(d^4+3d^2 w+6w^2)/(w(d^2+w)(d^2+3w)) < 0 for ALL w>0,d>0
# (manifestly negative: every factor of numerator and denominator positive)
w2 = sp.symbols('w2', positive=True)
m2 = delta**2*(3*w2+delta**2)/(w2*(w2+delta**2)**2)
dm = sp.factor(sp.diff(sp.log(m2), w2))
print('d/dw log main =', dm)
assert sp.simplify(dm + (delta**4+3*delta**2*w2+6*w2**2)/(w2*(delta**2+w2)*(delta**2+3*w2))) == 0
# numerator of dm is -(d^4+3d^2 w+6w^2): every factor positive, so dm < 0 for all w>0,d>0
print('PROVEN (symbolic, all delta>0): main strictly decreasing in u^2 on (0,1/4], min at |u|=1/2:',
      sp.N(main.subs(u, sp.Rational(1,2)).subs(delta, sp.Rational(3,10)), 12),
      ';  LINE far bound 1/(2T^2) <=', sp.N(1/(2*sp.Rational(141347,10000)**2), 12))
minmain = sp.N(main.subs(u, sp.Rational(1,2)).subs(delta, sp.Rational(3,10)), 12)
linebound = sp.N(1/(2*sp.Rational(141347,10000)**2), 12)
print('LINE lower bound (all sigma in (0,1), all T>=14.1347) =', sp.N(minmain - linebound, 12))

# ---------------- numeric spot check at T = gamma_1, dps=40 ----------------
mp.mp.dps = 40
t0 = mp.mpf('14.13472514173469379045725198356247027078')
def pair_re(sig, a, tau):
    x1 = sig - a; y1 = t0 - tau; y2 = t0 + tau
    return (x1**2 - y1**2)/(x1**2 + y1**2)**2 + (x1**2 - y2**2)/(x1**2 + y2**2)**2
def L_OFF(sig):
    return -pair_re(sig, mp.mpf('0.9'), t0) - pair_re(sig, mp.mpf('0.1'), t0) + pair_re(sig, mp.mpf('0.5'), t0)
def L_LINE(sig):
    return -pair_re(sig, mp.mpf('0.5'), t0 + mp.mpf('0.3')) + pair_re(sig, mp.mpf('0.5'), t0)

def sign_scan():
    off_neg, off_pos, line_neg = [], [], []
    for i in range(1, 1000):
        sg = mp.mpf(i)/1000
        if sg in (mp.mpf('0.1'), mp.mpf('0.5'), mp.mpf('0.9')):  # poles of OFF
            continue
        lo, ll = L_OFF(sg), L_LINE(sg)
        if lo < 0: off_neg.append(i/1000)
        else: off_pos.append(i/1000)
        if ll < 0: line_neg.append(i/1000)
    print('OFF negative sigma-range (grid, excl 0.5): [%.4f, %.4f]' % (min(off_neg), max(off_neg)))
    print('OFF positive sigma-range (grid):            [%.4f, %.4f]' % (min(off_pos), max(off_pos)))
    print('LINE negative count on grid:', len(line_neg))
sign_scan()
print('spot: L_OFF(0.3000) =', mp.nstr(L_OFF(mp.mpf('0.3')), 15), ' L_LINE(0.3000) =', mp.nstr(L_LINE(mp.mpf('0.3')), 15))
print('spot: L_OFF(0.4500) =', mp.nstr(L_OFF(mp.mpf('0.45')), 15), ' L_LINE(0.4500) =', mp.nstr(L_LINE(mp.mpf('0.45')), 15))
print('spot: L_OFF(0.9500) =', mp.nstr(L_OFF(mp.mpf('0.95')), 15), ' L_LINE(0.0500) =', mp.nstr(L_LINE(mp.mpf('0.05')), 15))
print('ALL CHECKS PASS')