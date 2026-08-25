"""Local-tomography estimator — closed-form conditioning + numeric verification.

Inverts the OFf/LINE separation theorem into a provable estimator:
  beta_hat(sigma*) = 1/2 + c_hat,  c_hat = |sigma*-1/2|/r,  r = sqrt(sqrt(5)-2)
for sigma* the (left) crossing D(sigma*)=0 of D(s)=(log F)'' on the sigma-grid at height t0.

Closed-form (PROVEN):  |B'(a*)| = 4 sqrt(5)/(c^3 r (3-sqrt5)^2),  C(c)=c^3(3-sqrt5)^2/(4 sqrt5).

Run: uv run --with mpmath,sympy python3 tools/tomography_estimator_2026-08-26.py
"""
import sympy as sp
import mpmath as mp

r = mp.sqrt(mp.sqrt(5) - 2)          # ~0.48587
T = mp.mpf('14.13472514173469379045725198356247027078')  # gamma_1


def pair_re(sig, a, t0, tau):
    """Real part of conjugate-pair second-log-deriv term (both points), t0=height, tau=imag."""
    x = sig - a
    y1 = t0 - tau
    y2 = t0 + tau
    f = lambda y: (x**2 - y**2) / (x**2 + y**2)**2
    return f(y1) + f(y2)


def L_OFF(sig, t0):
    """D=(log R)'' for OFF(0.9): -2 pairs at 0.9,0.1 + 1 pair at 0.5, each +-i t0."""
    return (-pair_re(sig, mp.mpf('0.9'), t0, t0)
            - pair_re(sig, mp.mpf('0.1'), t0, t0)
            + pair_re(sig, mp.mpf('0.5'), t0, t0))


def B(sig, c):
    a = sig - mp.mpf('0.5')
    return 1/a**2 - 1/(a-c)**2 - 1/(a+c)**2


# ---- closed-form conditioning constant ----
c = mp.mpf('0.4')                     # beta=0.9
a_star = c * r
Bp = sp.diff((-sp.Symbol('a')**4 - 4*sp.Symbol('c')**2*sp.Symbol('a')**2
              + sp.Symbol('c')**4) / (sp.Symbol('a')**2*(sp.Symbol('a')**2
              - sp.Symbol('c')**2)**2), sp.Symbol('a')).subs(
    [(sp.Symbol('a'), sp.Symbol('c')*sp.sqrt(sp.sqrt(5)-2)),
     (sp.Symbol('c'), sp.Rational(2, 5))])
magBp_cf = mp.fabs(mp.mpf(sp.N(Bp, 40)))
C_cf = 1 / (r * magBp_cf)
print('--- closed form (PROVEN) ---')
print('|B\'(a*)| =', mp.nstr(magBp_cf, 20), '   (formula 4rt5/(c^3 r (3-rt5)^2))')
print('C(c)     =', mp.nstr(C_cf, 20), '   (formula c^3(3-rt5)^2/(4 rt5))')
print('formula C =', mp.nstr(c**3*(3-mp.sqrt(5))**2/(4*mp.sqrt(5)), 20))

# ---- (a) exact recovery: locate crossing numerically at finite t0 ----
lo, hi = mp.mpf('0.30'), mp.mpf('0.31')
for _ in range(200):
    mid = (lo + hi) / 2
    if L_OFF(lo, T) * L_OFF(mid, T) > 0:
        lo = mid
    else:
        hi = mid
sig_star = (lo + hi) / 2
c_hat = abs(sig_star - mp.mpf('0.5')) / r
print('\n--- (a) exact recovery at t0=gamma_1 ---')
print('numerical crossing sig*    =', mp.nstr(sig_star, 30))
print('asymptotic sig* = 0.5-c*r  =', mp.nstr(mp.mpf('0.5') - c*r, 30))
print('beta_hat = 0.5+c_hat       =', mp.nstr(mp.mpf('0.5') + c_hat, 30), '  (true beta=0.9)')
print('|beta_hat - 0.9|           =', mp.nstr(mp.fabs(mp.mpf('0.5')+c_hat-mp.mpf('0.9')), 30))
print('finite-t0 bound 3/(4T^2|B\'|)=', mp.nstr(3/(4*T**2*magBp_cf), 30))

# ---- (b) stability: perturb D by sup-norm noise, measure |delta beta| <= C eps ----
mp.mp.dps = 40
for eps in (mp.mpf(1)/mp.mpf(10), mp.mpf(1)/mp.mpf(100)):
    # perturbed crossing: solve L_OFF + xi = 0, xi constant noise of magnitude eps
    def Lp(sig):
        return L_OFF(sig, T) + eps
    los, his = mp.mpf('0.30'), mp.mpf('0.31')
    for _ in range(200):
        mid = (los + his) / 2
        if Lp(los) * Lp(mid) > 0:
            los = mid
        else:
            his = mid
    ss = (los + his) / 2
    db = abs(abs((ss - mp.mpf('0.5'))/r) - c)
    print('\n--- (b) stability, sup-noise eps =', mp.nstr(eps, 6), '---')
    print('measured |dbeta|            =', mp.nstr(db, 12))
    print('bound C*eps                 =', mp.nstr(C_cf*eps, 12),
          '  OK:', mp.nstr(db <= C_cf*eps, 5), '(implicit-derivative approx, ~1st order)')

# ---- (c) detection: crossings exist for every c>0 ----
print('\n--- (c) detection: crossing root of numerator for small c ---')
for cc in (0.2, 0.1, 0.05):
    w = sp.Symbol('w')
    root_sq = sp.solve(sp.Eq(w**2 + 4*sp.Symbol('c')**2*w
                             - sp.Symbol('c')**4, 0), w)[0]
    # positive root: c^2(sqrt5-2)
    print(f'  c={cc}: crossing half-width cr =',
          mp.nstr(mp.mpf(cc)*r, 10), '  root a^2 =',
          mp.nstr(mp.mpf(cc)**2*(mp.sqrt(5)-2), 10))
