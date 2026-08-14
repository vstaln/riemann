"""Model 2: Davenport–Heilbronn function (linear combination of L-functions).

psi = the character mod 5 with psi(2) = i, psibar = its conjugate.  Build
    f(s) = L(s,psi) + c * L(s,psibar),   c = +-eps(psi),
    eps(psi) = tau(psi)/(i*sqrt(5))  (Gauss sum), chosen so the completed function
    Phi(s) = (5/pi)^((s+1)/2) Gamma((s+1)/2) f(s)  satisfies  Phi(s) = +-Phi(1-s)
    (sign +1 for c = +eps, sign -1 for c = -eps; both verified numerically below).
f has NO Euler product (a linear combination of two distinct L-functions) yet a zeta-type
functional equation -- the classic "proves too much" trap.  DH 1936 proved zeros off the
critical line for this family; the script locates them numerically and certifies them.

Run: uv run --quiet --with numpy python3 tools/barrier_zoo/model_dh.py
"""
import mpmath as mp
from common import (I, L_dirichlet, gauss_sum, newton2d, dedupe_roots,
                    grid_find_zeros, find_offline_zeros)

Q = 5
PI = mp.pi


def chars_mod5():
    """psi(2)=i, psibar(2)=-i; index 0..4 (chi(0)=0)."""
    psi = [mp.mpc(0, 0), mp.mpc(1, 0), mp.mpc(0, 1), mp.mpc(0, -1), mp.mpc(-1, 0)]
    psibar = [mp.mpc(0, 0), mp.mpc(1, 0), mp.mpc(0, -1), mp.mpc(0, 1), mp.mpc(-1, 0)]
    return psi, psibar


def build():
    psi, psibar = chars_mod5()
    tau_psi = gauss_sum(psi)
    eps_psi = tau_psi / (I * mp.sqrt(Q))          # FE epsilon for the odd char psi
    assert mp.fabs(mp.fabs(eps_psi) - 1) < mp.mpf('1e-30'), "|eps| must be 1"
    c_plus = eps_psi
    c_minus = -eps_psi

    def make(c):
        def f(s):
            return L_dirichlet(s, psi) + c * L_dirichlet(s, psibar)
        return f
    return dict(psi=psi, psibar=psibar, eps_psi=eps_psi,
                c_plus=c_plus, c_minus=c_minus,
                f_plus=make(c_plus), f_minus=make(c_minus))


def check_fe(b):
    gamma = lambda s: (mp.mpf(Q) / PI) ** ((s + 1) / 2) * mp.gamma((s + 1) / 2)
    ok_p, ok_m = True, True
    for t in [0.3, 1.7, 5.1, 12.7]:
        s = mp.mpf('0.4') + I * t
        gp = gamma(s) * b['f_plus'](s); gpc = gamma(1 - s) * b['f_plus'](1 - s)
        gm = gamma(s) * b['f_minus'](s); gmc = gamma(1 - s) * b['f_minus'](1 - s)
        rp, rm = gp / gpc, gm / gmc
        ok_p &= mp.fabs(rp - 1) < mp.mpf('1e-8')
        ok_m &= mp.fabs(rm + 1) < mp.mpf('1e-8')
        print(f"    t={t}:  Phi_+/Phi_+(1-s) = {mp.nstr(rp, 6)}   Phi_-/Phi_-(1-s) = {mp.nstr(rm, 6)}")
    print(f"    FE sign +1 (c=+eps): {ok_p} ;  FE sign -1 (c=-eps): {ok_m}")
    assert ok_p and ok_m, "FE constants are wrong"
    return ok_p, ok_m


def verify():
    print("== model_dh: Davenport–Heilbronn function (model 2) ==")
    b = build()
    print(f"  eps(psi) = {mp.nstr(b['eps_psi'], 10)}   (|eps| = {mp.nstr(mp.fabs(b['eps_psi']), 6)})")
    print("  FE check (must be +1 and -1 respectively):")
    check_fe(b)
    # NOTE: the first off-line zeros of the Titchmarsh kappa-combination sit at
    # t ~ 85.7 and t ~ 114.2 (certified at 50 dps in this session: Re(s) = 0.808517...,
    # 0.650830...).  A search truncated at t_hi=40 (as originally) finds ZERO off-line
    # zeros and must NOT be used to conclude anything.  Search high enough here.
    off_plus = find_offline_zeros(b['f_plus'], 'f_plus (FE sign +1)', t_hi=130.0)
    off_minus = find_offline_zeros(b['f_minus'], 'f_minus (FE sign -1)', t_hi=130.0)
    all_off = off_plus + off_minus
    assert len(all_off) >= 1, "no off-line zeros found: model construction suspect"
    print(f"VERDICT: {len(all_off)} off-line zeros located (|f|<1e-9 at high precision) for the "
          "Davenport–Heilbronn combination: zeta-type functional equation, NO Euler product, "
          "zeros OFF Re(s)=1/2. RH FALSE in this model world (numerically verified). Any argument "
          "that would prove all-zeros-on-the-line for THIS object proves too much.")
    return {'status': 'PROVEN (numeric off-line zeros)', 'n_offline': len(all_off),
            'zeros': [str(z) for z in all_off[:5]]}


if __name__ == '__main__':
    verify()
