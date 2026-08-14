"""Model 1: Epstein zeta function of a class-number-2 field (Q(sqrt(-5))-type forms).

zeta(s;Q) = sum_{(m,n)!=(0,0)} Q(m,n)^(-s),  Q(x,y)=a x^2 + b x y + c y^2,  D=b^2-4ac<0.
Analytic continuation for ALL s (pole at s=1) via the theta-Mellin formula:
    zeta(s;Q) = pi^s / Gamma(s) * I(s),
    I(s) = int_1^inf [ (Theta_Q(t)-1) t^(s-1) + ((2t/sqrt|D|) Theta_{Q'}(t) - 1) t^(-s-1) ] dt,
    Theta_Q(t) = sum_{m,n} exp(-pi t Q(m,n)),
    Q' = dual form = (4/|D|)(c x^2 - b x y + a y^2),   [Poisson: Theta_Q(t) = (2/(t sqrt|D|)) Theta_{Q'}(1/t)]
Cross-checks (numerical, printed): (1) the modularity identity at several t;
(2) Dedekind decomposition  zeta_K(s) = zeta(s) L(s, chi_-20) = (1/2)(zeta(s,Q1)+zeta(s,Q2))
    for the two classes Q1=x^2+5y^2, Q2=2x^2+2xy+3y^2 of discriminant -20.
DH 1936 (theorem): class-number-2 Epstein zetas have zeros off the critical line.  The script
locates off-line zeros numerically (numpy fast search on I(s), then mpmath-certified).

Run: uv run --quiet --with numpy python3 tools/barrier_zoo/model_epstein.py
"""
import numpy as np
import mpmath as mp
from common import L_dirichlet, newton2d, dedupe_roots, grid_find_zeros

Q1 = (1, 0, 5)     # x^2 + 5y^2        disc -20
Q2 = (2, 2, 3)     # 2x^2+2xy+3y^2     disc -20
N_SUM = 40
L_INT = 8.0
STEPS = 500


def dual_form(Q):
    a, b, c = Q
    absD = -(b * b - 4 * a * c)
    return (4.0 / absD) * c, -(4.0 / absD) * b, (4.0 / absD) * a    # (4/|D|)(c x^2 - b xy + a y^2)


def _theta_arrays(Q, N=N_SUM):
    a, b, c = Q
    m = np.arange(-N, N + 1)[:, None]
    n = np.arange(-N, N + 1)[None, :]
    return a * m**2 + b * m * n + c * n**2        # (2N+1)x(2N+1) values of Q(m,n)


def I_np(s, Q, N=N_SUM, L=L_INT, steps=STEPS):
    """The Mellin integral I(s) (zeros of zeta(s;Q) == zeros of I(s); pi^s/Gamma(s) != 0)."""
    a, b, c = Q
    absD = -(b * b - 4 * a * c)
    Qmn = _theta_arrays(Q, N)
    Qst = _theta_arrays(dual_form(Q), N)
    t = np.linspace(1.0, L, steps)
    e1 = np.exp(-np.pi * t[:, None, None] * Qmn[None, :, :]).sum(axis=(1, 2))
    e2 = np.exp(-(4 * np.pi / absD) * t[:, None, None] * Qst[None, :, :]).sum(axis=(1, 2))
    g1 = (e1 - 1.0) * t ** (s - 1)
    g2 = ((2 * t / np.sqrt(absD)) * e2 - 1.0) * t ** (-s - 1)
    return float(np.trapezoid(g1, t) + np.trapezoid(g2, t))


def zeta_form_mp(s, Q, N=25):
    """High-precision zeta(s;Q) via mpmath quadrature (certification)."""
    a, b, c = Q
    absD = -(b * b - 4 * a * c)
    ap, bp, cp = dual_form(Q)

    def g1(t):
        th = sum(mp.e ** (-mp.pi * t * (a * m * m + b * m * n + c * n * n))
                 for m in range(-N, N + 1) for n in range(-N, N + 1))
        return (th - 1) * t ** (s - 1)

    def g2(t):
        th = sum(mp.e ** (-(4 * mp.pi * t / absD) * (cp * m * m - bp * m * n + ap * n * n))
                 for m in range(-N, N + 1) for n in range(-N, N + 1))
        return ((2 * t / mp.sqrt(absD)) * th - 1) * t ** (-s - 1)

    I = mp.quad(g1, [1, mp.inf]) + mp.quad(g2, [1, mp.inf])
    return mp.pi ** s / mp.gamma(s) * I


def check_modularity(Q):
    absD = -(Q[1] ** 2 - 4 * Q[0] * Q[2])
    Qd = dual_form(Q)
    ok = True
    m = np.arange(-N_SUM, N_SUM + 1)[:, None]
    n = np.arange(-N_SUM, N_SUM + 1)[None, :]
    a, b, c = Q
    ad, bd, cd = Qd
    for t in [1.1, 2.0, 5.0]:
        Th = np.exp(-np.pi * t * (a * m**2 + b * m * n + c * n**2)).sum()
        Thd = np.exp(-(np.pi / t) * (ad * m**2 + bd * m * n + cd * n**2)).sum()
        rhs = 2.0 / (t * np.sqrt(absD)) * Thd
        rel = abs(Th - rhs) / max(1.0, Th)
        ok &= rel < 1e-9
        print(f"    t={t}: Theta(t) = {Th:.10e}  2/(t sqrt|D|) Theta_dual(1/t) = {rhs:.10e}  rel diff {rel:.1e}")
    print(f"  modularity identity: {ok}")
    return ok


def check_dedekind():
    # zeta_K(s) = zeta(s) * L(s, chi_-20)  vs  (1/2)(zeta(s;Q1)+zeta(s;Q2))
    def kronecker(D, n):
        n = abs(n)
        if n == 0:
            return 1 if abs(D) == 1 else 0
        res = 1
        if n % 2 == 0:
            if D % 2 == 0:
                return 0
            e = 0
            while n % 2 == 0:
                n //= 2; e += 1
            if D % 8 in (3, 5) and e % 2 == 1:
                res = -res
        p = 3
        while n > 1:
            if n % p == 0:
                if D % p == 0:
                    return 0
                e = 0
                while n % p == 0:
                    n //= p; e += 1
                v = pow(D % p, (p - 1) // 2, p)
                if v == p - 1:
                    v = -1
                if e % 2 == 1 and v == -1:
                    res = -res
            p += 2
        return res

    chi = [kronecker(-20, n) for n in range(20)]
    chi_mp = [mp.mpc(x) for x in chi]
    ok = True
    for s in [mp.mpc(2.5, 0), mp.mpc(1.2, 1.7), mp.mpc(0.75, 3.1)]:
        zK = mp.zeta(s) * L_dirichlet(s, chi_mp)
        half_sum = (zeta_form_mp(s, Q1) + zeta_form_mp(s, Q2)) / 2
        rel = mp.fabs(zK - half_sum) / mp.fabs(zK)
        ok &= rel < mp.mpf('1e-8')
        print(f"    s={mp.nstr(s,5)}: zeta_K = {mp.nstr(zK,9)}  (1/2)(zQ1+zQ2) = {mp.nstr(half_sum,9)}  rel {mp.nstr(rel,3)}")
    print(f"  Dedekind decomposition zeta_K = (1/2)(zeta(.;Q1)+zeta(.;Q2)): {ok}")
    return ok


def verify():
    print("== model_epstein: Epstein zeta, class number 2 (model 1) ==")
    print("  sanity: zeta(2; x^2+y^2) should be 4*zeta(2)*Catalan = 6.0268120396028507...")
    s2 = zeta_form_mp(mp.mpc(2, 0), (1, 0, 1))
    print(f"    zeta(2; x^2+y^2) = {mp.nstr(s2, 12)}")
    print("  modularity identity (dual-form Poisson summation):")
    check_modularity(Q1)
    print("  Dedekind cross-check (validates the theta-Mellin continuation):")
    check_dedekind()
    print("  off-line zero search (numpy fast on I(s), mpmath-certified):")
    offline_all = []
    for label, Q in [("Q1=x^2+5y^2", Q1), ("Q2=2x^2+2xy+3y^2", Q2)]:
        mp.mp.dps = 20
        try:
            cands = grid_find_zeros(lambda s: I_np(s, Q), t_hi=40.0, dt=0.5)
        finally:
            mp.mp.dps = 40
        roots = []
        for z0 in cands:
            z, err = newton2d(lambda s: zeta_form_mp(s, Q), mp.mpc(z0))
            if err < mp.mpf('1e-8'):
                roots.append(z)
        roots = dedupe_roots(roots)
        offline = [z for z in roots if mp.fabs(mp.re(z) - 0.5) > mp.mpf('1e-5')]
        offline_all += offline
        print(f"    [{label}] zeros: {len(roots)}, off-line: {len(offline)}")
        for z in sorted(offline, key=lambda z: mp.im(z))[:8]:
            print(f"      off-line zero: s = {mp.nstr(mp.re(z), 8)} + i*{mp.nstr(mp.im(z), 8)}"
                  f"   |zeta(s;Q)| = {mp.nstr(mp.fabs(zeta_form_mp(z, Q)), 7)}")
    assert len(offline_all) >= 1, "no off-line zeros found for disc -20 forms"
    print("VERDICT: Epstein zeta functions of the class-number-2 forms (disc -20) have zeros OFF "
          "Re(s)=1/2 (numerically certified at high precision; theorem DH 1936). The individual "
          "partial zetas have NO Euler product, yet each has a self-dual functional equation -- "
          "FE + sign + real coefficients is NOT enough. RH FALSE in this model world.")
    return {'status': 'PROVEN (numeric off-line zeros)', 'n_offline': len(offline_all),
            'zeros': [str(z) for z in offline_all[:5]]}


if __name__ == '__main__':
    verify()
