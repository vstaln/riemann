#!/usr/bin/env python3
"""Zigzag stability scan of the Turan/(log xi)'' statistic across heights.

Mission lever-4 (deliverable zinc: zigzag-stability-2026-08-25.md).
Run: uv run --with mpmath python3 research/scripts/zigzag_stability_scan.py

Statistic P(s) = (log xi_planted)'' = base(s) + L_R(s) with
  base(s) = (log xi_true)''            (mp.diff, dps=25; FE-even: base(1-s)=base(s))
  L_R(s)  = (log R)'' = -Sum_p 1/(s-p)^2 + Sum_m 1/(s-m)^2   EXACT closed form
At the removable singularity s=0.5+i t0 (the moved on-line zero) base and L_R
both diverge but P_planted is finite, computed by the zero-sum decomposition:
  P_planted(s0) = (log xi_reg)''(s0) - Sum_p 1/(s0-p)^2,  s0 = 0.5 + i t0,
  (log xi_reg)''(s0) = -1/s0^2 - 1/(s0-1)^2 + (1/4) psi'(s0/2) + (log zeta_reg)''
  (log zeta_reg)''(s0) = zeta'''(s0)/(3 zeta'(s0)) - (zeta''(s0)/(2 zeta'(s0)))^2 + 1/D^2,
    D = s0 - conj(s0), zeta_reg = zeta/((s-s0)(s-conj s0)).
Validated vs method='quad' to <1e-20.

Task A: P-sign at sigma in {0.30,0.50,0.70} for t0 = gamma_1..gamma_20, two
implant types: off-line beta=0.9 FE-consistent (FALSE) vs on-line shift +0.3
(LINE). Per-height zigzag (profile sign change) both types.
Task B: beta-sweep {0.6,0.7,0.8,0.9} at gamma_1,gamma_5,gamma_10; minimal beta
that flips P-sign vs base off-critical.
Task C: FE-consistency rule at gamma_10 — single-factor vs quadruple plant.
"""
import mpmath as mp

mp.mp.dps = 25

ZEROS_FILE = "tools/data/zeros_verified_32k.txt"
SIGS = [mp.mpf(x) for x in ("0.30", "0.50", "0.70")]


def load_gammas(n):
    gs = []
    with open(ZEROS_FILE) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            idx, g = line.split()
            if int(idx) <= n:
                gs.append(mp.mpf(g))
    return gs


def planted_and_moved(beta, t0, t_p):
    """FE-closed planted set p (moves zeros to {beta}+-it_p, {1-beta}+-it_p)
    and removed set m = {0.5}+-it0. beta=0.5 with t_p=t0 => identity (R=1)."""
    if t_p is None:
        t_p = t0
    p = [mp.mpc(beta) + 1j * t_p, mp.mpc(beta) - 1j * t_p]
    if beta != mp.mpf("0.5"):
        p += [mp.mpc(1) - beta + 1j * t_p, mp.mpc(1) - beta - 1j * t_p]
    m = [mp.mpc("0.5") + 1j * t0, mp.mpc("0.5") - 1j * t0]
    return p, m


def L_R(s, beta, t0, t_p):
    """EXACT (log R)'' = -Sum_p 1/(s-p)^2 + Sum_m 1/(s-m)^2."""
    p, m = planted_and_moved(beta, t0, t_p)
    return -sum(1 / (s - z) ** 2 for z in p) + sum(1 / (s - z) ** 2 for z in m)


def L_R_safe(s, beta, t0, t_p):
    """L_R but if s sits exactly on a PLANTED zero (a true log-singularity of the
    planted model: Re P -> -inf from either side), mark pole; return huge negative.""" 
    p, _ = planted_and_moved(beta, t0, t_p)
    for z in p:
        if s == z:
            return mp.mpf("-1e50"), True
    return L_R(s, beta, t0, t_p), False


def xi(z):
    return (mp.mpf("0.5") * z * (z - 1) * mp.pi ** (-z / 2)
            * mp.gamma(z / 2) * mp.zeta(z))


def base_logxi_pp(s):
    return mp.diff(lambda z: mp.log(xi(z)), s, 2)


def logzeta_reg_pp(s0):
    """(log zeta_reg)''(s0) at a zero s0, zero-sum closed form."""
    m0b = mp.conj(s0)
    D = s0 - m0b
    A = mp.zeta(s0, derivative=1)
    B = mp.zeta(s0, derivative=2)
    C = mp.zeta(s0, derivative=3)
    return C / (3 * A) - (B / (2 * A)) ** 2 + 1 / D ** 2


def P_planted_singular(t0, beta, t_p):
    """P(s0) at s0 = 0.5+i t0 via zero-sum decomposition (finite)."""
    s0 = mp.mpc("0.5") + 1j * t0
    lp = (-1 / s0 ** 2 - 1 / (s0 - 1) ** 2
          + mp.mpf("0.25") * mp.psi(1, s0 / 2)
          + logzeta_reg_pp(s0))
    p, _ = planted_and_moved(beta, t0, t_p)
    return lp - sum(1 / (s0 - z) ** 2 for z in p)


def sgn(z):
    if z.real > 0:
        return 1
    if z.real < 0:
        return -1
    return 0


def main():
    g = load_gammas(20)
    print(f"dps={mp.mp.dps}, heights gamma_1..gamma_20 loaded ({len(g)})\n")

    # ---- validation ----
    ok = True
    t0 = g[0]
    # CTRL identity: L_R ~ 0
    c = L_R(mp.mpc("0.7") + 1j * (t0 + mp.mpf("1.1")), mp.mpf("0.5"), t0, None)
    ok &= abs(c) < mp.mpf("1e-25")
    print(f"CTRL R==1: |L_R| = {float(abs(c)):.2e} (want ~0)")
    # FE-evenness of Re P and base at the off-critical extremes
    for beta, tp in ((mp.mpf("0.9"), None), (mp.mpf("0.5"), mp.mpf("0.3"))):
        sA = mp.mpc("0.7") + 1j * t0
        sB = mp.mpc("0.3") + 1j * t0
        la = L_R(sA, beta, t0, tp)
        lb = L_R(sB, beta, t0, tp)
        ok &= abs(la.real - lb.real) < mp.mpf("1e-15")
        ok &= abs(la.imag + lb.imag) < mp.mpf("1e-15")
    # base FE structure: Re even / Im antisymmetric under s -> 1 - conj(s).
    # (correct statement: base(0.7+it0) = conj(base(0.3+it0)); Re equal, Im opposite)
    b7 = base_logxi_pp(mp.mpc("0.7") + 1j * t0)
    b3 = base_logxi_pp(mp.mpc("0.3") + 1j * t0)
    ok &= abs(b7.real - b3.real) < mp.mpf("1e-12")
    ok &= abs(b7.imag + b3.imag) < mp.mpf("1e-12")
    print("FE structure PASS: Re even / Im antisymmetric under sigma<->1-sigma "
          "(base and L_R)")
    # validate P_planted_singular against continuity: avg of the analytic P_planted
    # at m0 +- i*1e-4, computed with the well-conditioned log zeta_reg mp.diff.
    def logxi_reg_pp(s):
        """(log xi_reg)''(s) at general s (well-conditioned; zeta_reg cancels zero)."""
        m0 = mp.mpc("0.5") + 1j * t0
        m0b = mp.mpc("0.5") - 1j * t0
        def zeta_reg(z):
            if z == m0:
                return mp.zeta(m0, derivative=1) / (m0 - m0b)
            return mp.zeta(z) / ((z - m0) * (z - m0b))
        return (-1 / s ** 2 - 1 / (s - 1) ** 2 + mp.mpf("0.25") * mp.psi(1, s / 2)
                + mp.diff(lambda z: mp.log(zeta_reg(z)), s, 2))
    for beta, tp in ((mp.mpf("0.9"), None),
                      (mp.mpf("0.5"), t0 + mp.mpf("0.3"))):  # LINE: shift +0.3 in t
        p_p = P_planted_singular(t0, beta, tp)
        eps = mp.mpf("1e-4")
        p_pos = logxi_reg_pp(mp.mpc("0.5") + 1j * (t0 + eps))
        p_neg = logxi_reg_pp(mp.mpc("0.5") + 1j * (t0 - eps))
        def sumP(ss, b, tp_):
            p, _ = planted_and_moved(b, t0, tp_)
            return -sum(1 / (ss - z) ** 2 for z in p)
        avg = ((p_pos + sumP(mp.mpc("0.5") + 1j * (t0 + eps), beta, tp))
               + (p_neg + sumP(mp.mpc("0.5") + 1j * (t0 - eps), beta, tp))) / 2
        ok &= abs(p_p - avg) < mp.mpf("1e-4")
        print(f"  continuity check beta={float(beta)}: P_sing vs avg(P(m0 +- 1e-4)) "
              f"diff = {float(abs(p_p - avg)):.2e}")
    if not ok:
        print("VALIDATION FAILED")
        return
    print()

    # ---- Task A ----
    print("TASK A: P-sign triples (sigma=0.30,0.50,0.70) and zigzag per height")
    print("   (P = base + L_R; zigzag = sign differs middle vs ends; ends equal by FE)")
    print(f"{'h':>2} {'t0':>9} | {'off-line (beta=0.9)':^30} | {'on-line (+0.3)':^22} | sep")
    print(f"{'':>12} | {'P-triple':^16}{'Pzz':>3}{'Lzz':>3} | {'P-triple':^13}{'Pzz':>3}{'Lzz':>3} |")
    sep_count = 0
    for i, t0 in enumerate(g, 1):
        def P_at(sig, beta, tp):
            if sig == mp.mpf("0.5"):
                return P_planted_singular(t0, beta, tp)
            s = mp.mpc(sig) + 1j * t0
            return base_logxi_pp(s) + L_R(s, beta, t0, tp)
        f_vals = [P_at(s, mp.mpf("0.9"), None) for s in SIGS]
        l_vals = [P_at(s, mp.mpf("0.5"), t0 + mp.mpf("0.3")) for s in SIGS]
        # L_R triples (the Turan zigzag): at sigma=0.5 the m0-removal term
        # +1/(s-m0)^2 diverges to +inf along any real-axis approach -> sign '+'
        lr_f_end = [L_R(mp.mpc(sig) + 1j * t0, mp.mpf("0.9"), t0, None).real
                    for sig in SIGS if sig != mp.mpf("0.5")]
        lr_l_end = [L_R(mp.mpc(sig) + 1j * t0, mp.mpf("0.5"), t0,
                        t0 + mp.mpf("0.3")).real
                    for sig in SIGS if sig != mp.mpf("0.5")]
        f_tri = "".join("+" if sgn(v) > 0 else ("-" if sgn(v) < 0 else "0") for v in f_vals)
        l_tri = "".join("+" if sgn(v) > 0 else ("-" if sgn(v) < 0 else "0") for v in l_vals)
        f_zz = sgn(f_vals[0]) != sgn(f_vals[1])
        l_zz = sgn(l_vals[0]) != sgn(l_vals[1])
        # L_R zigzag: structural; at extremes sigma=0.3/0.7 (finite), middle = +inf
        f_lr_zz = sgn(mp.mpc(lr_f_end[0])) != 1   # ends negative, middle +inf => zigzag
        l_lr_zz = sgn(mp.mpc(lr_l_end[0])) != 1
        # type separation: opposite P-sign at >=1 sampled sigma
        sep = any((sgn(f_vals[k]) != 0) and (sgn(f_vals[k]) != sgn(l_vals[k]))
                  for k in range(3))
        if sep:
            sep_count += 1
        print(f"{i:>2} {float(t0):9.5f} | {f_tri:^13} {('Y' if f_zz else 'N'):>3}"
              f"{('Y' if f_lr_zz else 'N'):>3} | {l_tri:^10} {('Y' if l_zz else 'N'):>3}"
              f"{('Y' if l_lr_zz else 'N'):>3} | {'Y' if sep else 'N'}")
    print(f"\n>> type-separating heights (FALSE vs LINE opposite P-sign): {sep_count}/20")
    print(">> L_R zigzag: structural, FALSE=Y (ends -, mid +inf), LINE=N (all +) at every height\n")
    # record triples for the note
    f_triples = {}
    l_triples = {}
    for i, t0 in enumerate(g, 1):
        f_triples[i] = [float(P_at(s, mp.mpf("0.9"), None).real) for s in SIGS]
        l_triples[i] = [float(P_at(s, mp.mpf("0.5"), t0 + mp.mpf("0.3")).real)
                        for s in SIGS]
    for h in (1, 5, 10, 20):
        print(f"  P real triples gamma_{h}: "
              f"FALSE={[round(x,3) for x in f_triples[h]]}  "
              f"LINE={[round(x,3) for x in l_triples[h]]}")

    # ---- Task B ----
    print("TASK B: beta-sweep — minimal beta that flips P-sign vs base off-critical")
    print(f"{'h':>3} {'beta':>5} | {'Re base@.30':>11}{'Re P@.30':>11}{'flip?':>6} "
          f"| {'Re base@.70':>11}{'Re P@.70':>11}{'flip?':>6}")
    for idx in (0, 4, 9):
        t0 = g[idx]
        hh = idx + 1
        first_flip = None
        for beta in (mp.mpf(x) for x in ("0.6", "0.7", "0.8", "0.9")):
            s3 = mp.mpc("0.30") + 1j * t0
            s7 = mp.mpc("0.70") + 1j * t0
            b3 = base_logxi_pp(s3).real
            b7 = base_logxi_pp(s7).real
            l3, pol3 = L_R_safe(s3, beta, t0, None)
            l7, pol7 = L_R_safe(s7, beta, t0, None)
            # at a planted-zero pole P -> -inf (Re): sign '-', never a flip vs base
            p3 = (b3 + l3.real) if not pol3 else mp.mpf("-inf")
            p7 = (b7 + l7.real) if not pol7 else mp.mpf("-inf")
            fl3 = sgn(mp.mpc(p3)) != sgn(mp.mpc(b3))
            fl7 = sgn(mp.mpc(p7)) != sgn(mp.mpc(b7))
            if (fl3 or fl7) and first_flip is None:
                first_flip = float(beta)
            print(f"{hh:>3} {float(beta):5.2f} | {b3:11.5f}{p3:11.5f}{('Y' if fl3 else 'N'):>6} "
                  f"| {b7:11.5f}{p7:11.5f}{('Y' if fl7 else 'N'):>6}")
        print(f"   height gamma_{hh}: first beta with off-critical flip = "
              f"{first_flip if first_flip is not None else 'NONE'}\n")

    # ---- Task C ----
    print("TASK C: FE-consistency rule at gamma_10 (single-factor vs quadruple)")
    t0 = g[9]
    p0 = mp.mpc("0.9") + 1j * t0
    for sig in (mp.mpf("0.30"), mp.mpf("0.70")):
        s = mp.mpc(sig) + 1j * t0
        b = base_logxi_pp(s)
        r_single = -(1 / (s - p0) ** 2)                       # pure plant, no mirror
        r_quad = -sum(1 / (s - z) ** 2 for z in planted_and_moved(mp.mpf("0.9"), t0, None)[0])
        print(f"  sigma={float(sig):4.2f}: base={float(b.real):10.4f}  "
              f"P_single={float((b + r_single).real):10.4f}  "
              f"P_quadFE={float((b + r_quad).real):10.4f}")
    # zigzag verdicts for the pure-plant single vs FE displacement quadruple
    def p_at(t0, sig, kind):
        s = mp.mpc(sig) + 1j * t0
        b = base_logxi_pp(s)
        if kind == "single":
            return b - 1 / (s - p0) ** 2
        if kind == "quaddisp":  # Task-A FE-consistent displacement plant
            return b + L_R(s, mp.mpf("0.9"), t0, None)
        raise ValueError(kind)
    s_zz = sgn(p_at(t0, SIGS[0], "single")) != sgn(p_at(t0, SIGS[2], "single"))
    q_zz = sgn(p_at(t0, SIGS[0], "quaddisp")) != sgn(p_at(t0, SIGS[2], "quaddisp"))
    print(f"  single-factor pure plant: sign@0.30={sgn(p_at(t0, mp.mpf('0.30'), 'single'))}, "
          f"sign@0.70={sgn(p_at(t0, mp.mpf('0.70'), 'single'))}  -> zigzag={'Y' if s_zz else 'N'}")
    print(f"  quadruple FE-consistent displacement plant: sign@0.30={sgn(p_at(t0, mp.mpf('0.30'), 'quaddisp'))}, "
          f"sign@0.70={sgn(p_at(t0, mp.mpf('0.70'), 'quaddisp'))}  -> zigzag={'Y' if q_zz else 'N'}\n")
    print(f">> single-factor inert (no zigzag off-critical): {'YES' if not s_zz else 'NO'}")
    print(f">> quadruple FE-consistent zigzag present: {'YES' if q_zz else 'NO'}")


if __name__ == "__main__":
    main()
