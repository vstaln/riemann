#!/usr/bin/env python3
"""Honest Jensen disc-mass probe: does curvature-subtracted disc mass of |zeta|
separate true on-line zeros from planted off-line zeros?

Spec: research/notes/jensen-honest-build-2026-08-25.md
Run: uv run --with mpmath python3 tools/jensen_honest_probe.py

The disc log-average is computed via Jensen's formula in closed form
  S(t) = log|zeta(c)| + sum_{|rho-c|<r} log(r/|rho-c|)
which is EXACT (no quadrature instability from log|zeta| near zeros) and uses
mpmath for the function value at the center. Direct boundary quadrature is run
as a validation block and must agree within tolerance.
"""
import random
import sys
import time

import mpmath as mp

mp.mp.dps = 15

ZEROS_FILE = "tools/data/zeros_verified_32k.txt"
N_IMPLANTS = 12          # t0 = gamma_n, n=1..12 (all nearby zeros, no cherry-pick)
N_PERM = 1000
SEED = 20260825
CONFIGS = [(0.6, 0.2), (0.6, 0.3), (0.75, 0.2), (0.75, 0.3)]


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


def planted_set(beta, t_p):
    """FE-closed planted zero multiset at height t_p: {beta+-it_p, (1-beta)+-it_p}
    for beta != 1/2 (4 points); {1/2+-it_p} for beta = 1/2 (2 points, no dupes)."""
    pts = [mp.mpc(beta) + 1j * mp.mpc(t_p), mp.mpc(beta) - 1j * mp.mpc(t_p)]
    if beta != mp.mpf("0.5"):
        pts += [mp.mpc(1) - mp.mpc(beta) + 1j * mp.mpc(t_p),
                mp.mpc(1) - mp.mpc(beta) - 1j * mp.mpc(t_p)]
    return pts


def corr_factor(s, t0, beta, t_p=None):
    """FE-exact finite ratio R(s) = prod_P (1-s/p) / prod_M (1-s/m)
    with P = planted_set(beta, t_p), M = {1/2+-it0}. Identity swap (beta=1/2,
    t_p=t0) gives P=M and R=1 exactly. No e^{s/rho} factors -- those break
    xi(s)=xi(1-s) (they contribute e^{s*Delta}, Delta = sum 1/rho_p - sum
    1/rho_m = 0.004975 != 0, a ~16% FE violation). The plain finite ratio
    satisfies R(1-s)=R(s) exactly since both sets are FE-closed and
    #P == #M (mod 2). zeta_planted = zeta_true*R is then exactly
    xi-symmetric with the desired zero multiset."""
    if t_p is None:
        t_p = t0
    s = mp.mpc(s)
    t0 = mp.mpc(t0)
    planted = planted_set(beta, t_p)
    moved = [mp.mpf("0.5") + 1j * t0, mp.mpf("0.5") - 1j * t0]
    num = mp.mpc(1)
    for p in planted:
        num *= 1 - s / p
    den = mp.mpc(1)
    for m in moved:
        den *= 1 - s / m
    return num / den


def zeta_model(s, t0, beta, t_p=None):
    if t_p is None:
        t_p = t0
    if beta is None or (beta == mp.mpf("0.5") and t_p == t0):
        return mp.zeta(s)
    return mp.zeta(s) * corr_factor(s, t0, beta, t_p)


def model_zero_points(t0, beta, t_p, gammas):
    """Zeros of the model relevant to discs with Im >= 0 (conjugate partners at
    Im = -t_p are included in corr_factor for FE exactness but are never within
    reach of a disc here)."""
    if beta is None or (beta == mp.mpf("0.5") and t_p == t0):
        return [(mp.mpf("0.5"), g) for g in gammas]
    pts = [(mp.mpf("0.5"), g) for g in gammas if abs(g - t0) > mp.mpf("1e-12")]
    for p in planted_set(beta, t_p):
        if p.imag >= 0:
            pts.append((p.real, p.imag))
    return pts


def S(c_re, t, r, t0, beta, gammas, t_p=None):
    """Jensen boundary log-average in closed form (exact, no quadrature)."""
    if t_p is None:
        t_p = t0
    c = mp.mpc(c_re) + 1j * mp.mpc(t)
    ssum = mp.log(abs(zeta_model(c, t0, beta, t_p)))
    for re, im in model_zero_points(t0, beta, t_p, gammas):
        d = abs(mp.mpc(re) + 1j * mp.mpc(im) - c)
        if d <= r:
            ssum += mp.log(r / d)
    return ssum


def features(c_re, t0, r, beta, gammas, t_p=None):
    """(S, kappa, Q) at implant location t0. h = r (pre-specified)."""
    if t_p is None:
        t_p = t0
    h = r
    vals = [S(c_re, t0 + dt, r, t0, beta, gammas, t_p) for dt in (-h, mp.mpf(0), h)]
    kappa = vals[2] - 2 * vals[1] + vals[0]
    return float(vals[1]), float(kappa), float(vals[1] - kappa)


def permutation_p(x, y, rng, nperm=N_PERM):
    obs = abs(sum(y) / len(y) - sum(x) / len(x))
    pooled = x + y
    count = 0
    for _ in range(nperm):
        rng.shuffle(pooled)
        a = pooled[: len(x)]
        b = pooled[len(x):]
        if abs(sum(b) / len(b) - sum(a) / len(a)) >= obs - 1e-15:
            count += 1
    return (1 + count) / (1 + nperm), obs


# ---------------- validation ----------------

def quadrature_boundary(c_re, t, r, f, n=160):
    tot = mp.mpf(0)
    for j in range(n):
        th = 2 * mp.pi * (j + 0.5) / n
        s = mp.mpc(c_re) + 1j * mp.mpc(t) + r * mp.e ** (1j * th)
        tot += mp.log(abs(f(s)))
    return tot / n


def validate(gammas):
    ok = True
    t0 = gammas[0]
    print("-- model verification --")
    v = abs(zeta_model(mp.mpc(0.9) + 1j * t0, t0, mp.mpf("0.9")))
    ok &= v < 1e-8
    print(f"  planted zero at 0.9+it0 present: |zeta_planted| = {v:.2e} (want <1e-8)")
    # moved zero removed: value at 0.5+it0 is a 0*inf limit. L'Hopital:
    # zeta_planted(m0) = -zeta'(m0)*m0 * prod_P(1-m0/p) / prod_{m!=m0}(1-m0/m)
    # mp.zeta(m0,1) is unreliable at an exact zero (returns the ~1e-21 error
    # floor); use a central difference for the derivative instead.
    m0 = mp.mpc("0.5") + 1j * t0
    b = mp.mpf("0.9")
    hh = mp.mpf("1e-8")
    d_zeta = (mp.zeta(m0 + hh) - mp.zeta(m0 - hh)) / (2 * hh)
    num = mp.mpc(1)
    for p in (b + 1j * t0, b - 1j * t0, (1 - b) + 1j * t0, (1 - b) - 1j * t0):
        num *= 1 - m0 / p
    den = mp.mpc(1)
    for m in (mp.mpc("0.5") - 1j * t0,):
        den *= 1 - m0 / m
    lim = -d_zeta * m0 * num / den
    v = abs(lim)
    ok &= 1e-4 < v < 10
    # cross-check: direct evaluation at a tiny offset must approach the limit
    eps = mp.mpf("1e-7")
    v2 = abs(zeta_model(m0 + eps, t0, mp.mpf("0.9")))
    ok &= abs(v2 - v) / v < 1e-3
    print(f"  on-line zero at 0.5+it0 removed: |zeta_planted(limit)| = {v:.4f}, "
          f"offset check {v2:.4f} (relative {abs(v2-v)/v:.1e})")
    # far-field: a different zero set is a genuinely different function, so
    # zeta_planted != zeta_true at finite points (that is the perturbation we
    # measure). The correct far check: |R(s)| = prod|rho_p-s|/|rho_p| *
    # prod|rho_m|/|rho_m-s| computed independently from distances.
    s = mp.mpc(0.7) + 1j * (t0 + 1000)
    R = corr_factor(s, t0, mp.mpf("0.9"))
    rho_p = [mp.mpc(0.9) + 1j * t0, mp.mpc(0.9) - 1j * t0,
             mp.mpc(0.1) + 1j * t0, mp.mpc(0.1) - 1j * t0]
    rho_m = [mp.mpc(0.5) + 1j * t0, mp.mpc(0.5) - 1j * t0]
    expect = mp.mpf(1)
    for p in rho_p:
        expect *= abs(p - s) / abs(p)
    for m in rho_m:
        expect *= abs(m) / abs(m - s)
    d = abs(abs(R) - expect) / expect
    ok &= d < 1e-6
    print(f"  R far asymptotics: |R|={abs(R):.6f} vs distance formula={expect:.6f} (rel {d:.2e})")

    def xi(z):
        return mp.mpf("0.5") * z * (z - 1) * mp.pi ** (-z / 2) * mp.gamma(z / 2) * zeta_model(z, t0, mp.mpf("0.9"))
    s = mp.mpc(0.62) + 1j * (t0 + 1.7)
    fe = abs(xi(s) - xi(1 - s))
    ok &= fe < 1e-9
    print(f"  xi functional equation for planted model: |diff| = {fe:.2e} (want <1e-9)")
    s = mp.mpc(0.7) + 1j * (t0 + 1.1)
    d = abs(zeta_model(s, t0, mp.mpf("0.5")) - mp.zeta(s))
    ok &= d < 1e-12
    print(f"  beta=0.5 control == true zeta: |diff| = {d:.2e} (want <1e-12)")

    print("-- closed-form Jensen vs direct boundary quadrature (true zeta) --")
    cases = [(0.6, 15.0, 0.25), (0.75, 18.5, 0.2), (0.6, 21.5, 0.3), (0.75, 30.0, 0.25)]
    for c_re, t, r in cases:
        cf = float(S(c_re, t, r, mp.mpf(0), None, gammas))
        qd = float(quadrature_boundary(c_re, t, r, mp.zeta))
        ag = abs(cf - qd)
        ok &= ag < 5e-2
        print(f"  c=({c_re},{t}) r={r}: closed={cf:+.4f} quadrature={qd:+.4f} |diff|={ag:.2e}")
    return ok


def main():
    t_start = time.time()
    print(f"mpmath {mp.__version__}, dps={mp.mp.dps}")
    gammas = load_gammas(N_IMPLANTS)
    print(f"loaded {len(gammas)} true zeros (n=1..{N_IMPLANTS}): "
          f"{float(gammas[0]):.4f} .. {float(gammas[-1]):.4f}")
    if not validate(gammas):
        print("VALIDATION FAILED")
        sys.exit(1)
    print("validation: PASS\n")

    rng = random.Random(SEED)
    t0s = gammas
    rows = {}
    for c_re, r in CONFIGS:
        rows[(c_re, r)] = {}
        groups = (("RH", None, None), ("FALSE", mp.mpf("0.9"), None),
                  ("CTRL", mp.mpf("0.5"), None), ("LINE", mp.mpf("0.5"), mp.mpf("0.3")))
        for label, beta, t_off in groups:
            F = [features(c_re, t0, r, beta, gammas, t0 + t_off if t_off is not None else None)
                 for t0 in t0s]
            rows[(c_re, r)][label] = ([f[0] for f in F], [f[1] for f in F], [f[2] for f in F])
        m = lambda v: sum(v) / len(v)
        pQ_f = permutation_p(rows[(c_re, r)]["RH"][2], rows[(c_re, r)]["FALSE"][2], rng)[0]
        pQ_c = permutation_p(rows[(c_re, r)]["RH"][2], rows[(c_re, r)]["CTRL"][2], rng)[0]
        pQ_l = permutation_p(rows[(c_re, r)]["RH"][2], rows[(c_re, r)]["LINE"][2], rng)[0]
        pS_f = permutation_p(rows[(c_re, r)]["RH"][0], rows[(c_re, r)]["FALSE"][0], rng)[0]
        pK_f = permutation_p(rows[(c_re, r)]["RH"][1], rows[(c_re, r)]["FALSE"][1], rng)[0]
        rows[(c_re, r)]["p"] = (pQ_f, pQ_c, pQ_l, pS_f, pK_f)
        print(f"c={c_re},r={r}:")
        for label in ("RH", "FALSE", "CTRL", "LINE"):
            print(f"  {label:<5} mean(S,kappa,Q)=({m(rows[(c_re,r)][label][0]):+.4f},"
                  f"{m(rows[(c_re,r)][label][1]):+.4f},{m(rows[(c_re,r)][label][2]):+.4f})")
        print(f"  p_Q(FALSE)={pQ_f:.4f}  p_Q(CTRL)={pQ_c:.4f}  p_Q(LINE)={pQ_l:.4f}  "
              f"p_S={pS_f:.4f}  p_kappa={pK_f:.4f}")

    print("\n-- raw Q distributions per group (12 implant positions, in t0 order) --")
    for c_re, r in CONFIGS:
        for label in ("RH", "FALSE", "CTRL"):
            print(f"c={c_re},r={r} {label:<5}: " + " ".join(f"{q:+.3f}" for q in rows[(c_re, r)][label][2]))

    sig = [(c, rows[c]["p"][0]) for c in CONFIGS if rows[c]["p"][0] < 0.05]
    ctrl_ok = all(rows[c]["p"][1] >= 0.05 for c in CONFIGS)
    line_sep = any(rows[c]["p"][2] < 0.05 for c in CONFIGS)
    if sig and ctrl_ok:
        verdict = "SEPARATES"
    elif not sig:
        verdict = "NO_SEPARATION"
    else:
        verdict = "INCONCLUSIVE (control not silent)"
    print(f"\nVERDICT: {verdict}")
    for c, p in sig:
        print(f"  significant config {c}: p_Q={p:.4f}")
    print("  control p-values: " + ", ".join(f"{c}:{rows[c]['p'][1]:.3f}" for c in CONFIGS))
    print(f"  LINE (on-line displacement) separates: {line_sep}")
    print(f"elapsed {time.time() - t_start:.1f}s")


if __name__ == "__main__":
    main()
