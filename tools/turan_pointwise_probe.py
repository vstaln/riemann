#!/usr/bin/env python3
"""Turán / (log xi)'' POINTWISE probe: does a finite implant (zero displacement)
show up as a pointwise statistic and separate displacement TYPE?

Spec: mission lever-4 rung 2 (turan-probe-2026-08-25.md)
Run: uv run --with mpmath python3 tools/turan_pointwise_probe.py

The statistic: P(s) = (log xi)'' = xi''/xi - (xi'/xi)^2  (log xi concave iff P<0).
For every planted model zeta_planted = zeta_true * R (R = finite FE-exact ratio,
reused from jensen_honest_probe.py):
    log xi_planted = log xi_true + log R
    => (log xi_planted)'' = base(s) + L_R(s)
with
    base(s) = (log xi_true)''      identical across ALL groups (independent of the implant)
    L_R(s)  = (log R)'' = -Sum_p 1/(s-p)^2 + Sum_m 1/(s-m)^2    EXACT analytic

The discriminating content between any two groups is *exactly* L_R(FALSE) vs
L_R(LINE) etc. -- no numerical noise, no permutation. base is computed once and
cancels in every difference; we also report |base| to show it dominates/shapes
the sign. A point where the implant "flips" the sign of P is where base and L_R
have opposite signs with |L_R| > |base|; since base is common, the flip is
controlled purely by L_R.
"""
import sys
import time

import mpmath as mp

mp.mp.dps = 25

ZEROS_FILE = "tools/data/zeros_verified_32k.txt"
SIGS = [mp.mpf(x) for x in ("0.30", "0.35", "0.40", "0.45", "0.50",
                            "0.55", "0.60", "0.65", "0.70")]
# t offsets to sample beside/at the former-zero location
T_OFFS = [mp.mpf(x) for x in ("-0.3", "0.0", "0.3")]

GROUPS = [  # label, beta, t_p
    ("FALSE", mp.mpf("0.9"), None),            # off-line: {0.9+-it0, 0.1+-it0}
    ("LINE",  mp.mpf("0.5"), mp.mpf("0.3")),   # on-line, displaced in t: {0.5+-i(t0+0.3)}
    ("CTRL",  mp.mpf("0.5"), None),            # identity swap -> R=1
]


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
    """Returns (planted_re_set, moved_re_set) of COMPLEX zero locations."""
    if t_p is None:
        t_p = t0
    p = [mp.mpc(beta) + 1j * t_p, mp.mpc(beta) - 1j * t_p]
    if beta != mp.mpf("0.5"):
        p += [mp.mpc(1) - beta + 1j * t_p, mp.mpc(1) - beta - 1j * t_p]
    m = [mp.mpc("0.5") + 1j * t0, mp.mpc("0.5") - 1j * t0]
    return p, m


def L_R(s, beta, t0, t_p):
    """EXACT (log R)'' = -Sum_p 1/(s-p)^2 + Sum_m 1/(s-m)^2. Pure analytic; no diff."""
    p, m = planted_and_moved(beta, t0, t_p)
    val = mp.mpc(0)
    for z in p:
        val -= 1 / (s - z) ** 2
    for z in m:
        val += 1 / (s - z) ** 2
    return val


def xi(z):
    return (mp.mpf("0.5") * z * (z - 1) * mp.pi ** (-z / 2)
            * mp.gamma(z / 2) * mp.zeta(z))


def base_logxi_pp(s):
    """(log xi_true)'' at s via mp.diff on log xi. Common to every group."""
    return mp.diff(lambda z: mp.log(xi(z)), s, 2)


def main():
    t_start = time.time()
    t0 = load_gammas(1)[0]
    print(f"mpmath {mp.__version__}, dps={mp.mp.dps}, t0=gamma_1={float(t0):.6f}\n")

    # ---- validation: identities ----
    ok = True
    ok &= abs(L_R(mp.mpc(0.7) + 1j * (t0 + 1.1), mp.mpf("0.5"), t0, None)) < mp.mpf("1e-20")
    print(f"CTRL R==1 (no implant): max|L_R| = {float(abs(L_R(mp.mpc(0.7)+1j*(t0+1.1), mp.mpf('0.5'), t0, None))):.2e} (want ~0)")
    # FE-trace: L_R real part is even about sigma=1/2 for FE-closed sets;
    # imag part should be antisymmetric (conjugate pairs)
    sA = mp.mpc("0.6") + 1j * (t0 + mp.mpf("0.2")); sB = mp.mpc("0.4") + 1j * (t0 + mp.mpf("0.2"))
    for lbl, b, tp in GROUPS:
        la, lb = L_R(sA, b, t0, tp), L_R(sB, b, t0, tp)
        # sA and sB are sigma-conjugates; real parts equal, imag parts opposite
        ok &= abs(la.real - lb.real) < mp.mpf("1e-15")
        ok &= abs(la.imag + lb.imag) < mp.mpf("1e-15")
    print("even/odd sigma-structure check (Re even, Im antisymmetric under sigma<->1-sigma): " +
          ("PASS" if ok else "FAIL"))
    if not ok:
        print("VALIDATION FAILED")
        sys.exit(1)

    # ---- grid scan ----
    # base is common: compute once per (sigma,t); cache.
    base_cache = {}
    print(f"\n{'sigma':>6} {'toff':>5} | " +
          " ".join(f"{lbl:>7}(Re,Im)" for lbl, _, _ in GROUPS) +
          " | base_sign")
    for sig in SIGS:
        for dt in T_OFFS:
            s = mp.mpc(sig) + 1j * (t0 + dt)
            # base: skip if too near a logarithmic singularity (true zero)
            if sig == mp.mpf("0.5") and dt == mp.mpf("0"):
                bstr = "SING(zero)"
                base_here = None
            else:
                base_here = base_logxi_pp(s)
                if abs(xi(s)) < mp.mpf("1e-8"):
                    bstr = "SING(lo|xi|)"
                    base_here = None
                else:
                    bstr = "+" if base_here.real < 0 else "-"
            base_cache[(sig, dt)] = base_here
            # The point s = 0.5+it0 is a removable singularity for every non-CTRL
            # group (base and +1/(s-m0)^2 both diverge, sum is finite); skip it.
            if sig == mp.mpf("0.5") and dt == mp.mpf("0"):
                print(f"{float(sig):6.2f} {float(dt):5.1f} | " +
                      " ".join(f"{'removable-sing':>16}" for _ in GROUPS) +
                      f" | {bstr}")
                continue
            cells = []
            for lbl, b, tp in GROUPS:
                L = L_R(s, b, t0, tp)
                cells.append(f"{float(L.real):+8.4f},{float(L.imag):+7.4f}")
            print(f"{float(sig):6.2f} {float(dt):5.1f} | " + " ".join(f"{c:>16}" for c in cells) +
                  f" | {bstr}")

    # ---- Question A: does any implant flip the pointwise sign of P=(log xi)''? ----
    print("\n== Question A: pointwise sign of P = base + L_R ==")
    # sign(P) differs between groups only through L_R. base is common; a flip at
    # point s needs |L_R| > |base| with opposite sign. Report the max ratio.
    max_ratio = (None, mp.mpf(0))
    for sig in SIGS:
        for dt in T_OFFS:
            s = mp.mpc(sig) + 1j * (t0 + dt)
            base_here = base_cache[(sig, dt)]
            if base_here is None:
                continue
            for lbl, b, tp in GROUPS:
                L = L_R(s, b, t0, tp)
                if base_here.real != 0:
                    r = abs(L.real / base_here.real)
                    if r > max_ratio[1]:
                        max_ratio = ((sig, dt, lbl), r)
    print(f"max |L_R/base| over grid = {float(max_ratio[1]):.3f} at "
          f"{max_ratio[0]}  (a flip needs ratio > 1)")

    # ---- Question B: does a pointwise statistic separate displacement TYPE? ----
    print("\n== Question B: pointwise statistic separating FALSE (off-line) vs LINE (on-line) ==")
    # On the critical line sigma=1/2: off-line planted pairs {beta,1-beta} at +-t0
    # contribute Re(L_R) with sign sensitive to (0.5-beta); on-line set contributes
    # only via b=(t-t_p) displacement. Use the sigma-even Re profile and detect a
    # stable sign separation between FALSE and LINE across the sigma-grid.
    # NOTE: exclude dt=0 (removable singularity at the removed on-line zero).
    B_OFFS = [mp.mpf(x) for x in ("-0.3", "-0.15", "0.15", "0.3")]
    sep = 0
    for dt in B_OFFS:
        s = mp.mpc("0.5") + 1j * (t0 + dt)
        LF = L_R(s, mp.mpf("0.9"), t0, None)
        LL = L_R(s, mp.mpf("0.5"), t0, mp.mpf("0.3"))
        LC = L_R(s, mp.mpf("0.5"), t0, None)
        print(f"  t=t0{float(dt):+.2f}: Re[L_FALSE]={float(LF.real):+9.5f}  "
              f"Re[L_LINE]={float(LL.real):+9.5f}  Re[L_CTRL]={float(LC.real):+9.5f}")
        if (LF.real > 0) != (LL.real > 0):
            sep += 1
    print(f"  opposite-sign Re(L_R) on critical line in {sep}/{len(B_OFFS)} offsets")

    # also: sign of Re(L_R) as function of sigma (even), FALSE vs LINE
    # skip sigma=0.5 at toff=0 (removable singularity)
    print("  Re[L_R] across sigma (expect even about 0.5), FALSE vs LINE:")
    offcrit = 0
    for sig in SIGS:
        s = mp.mpc(sig) + 1j * (t0)
        if sig == mp.mpf("0.5"):
            continue
        LF = L_R(s, mp.mpf("0.9"), t0, None)
        LL = L_R(s, mp.mpf("0.5"), t0, mp.mpf("0.3"))
        if (LF.real > 0) != (LL.real > 0):
            offcrit += 1
        print(f"    sigma={float(sig):5.2f}: FALSE={float(LF.real):+9.4f}  LINE={float(LL.real):+9.4f}")
    print(f"  opposite-sign Re(L_R) off critical line (toff=0) in {offcrit}/{len(SIGS)-1} sigmas")

    # verdict
    ratios = [abs(L_R(mp.mpc(sig) + 1j * (t0 + dt), mp.mpf("0.9"), t0, None).real) /
              abs(L_R(mp.mpc(sig) + 1j * (t0 + dt), mp.mpf("0.5"), t0, mp.mpf("0.3")).real)
              for sig in SIGS for dt in T_OFFS if dt != mp.mpf("0")]
    max_eff = max(ratios) if ratios else mp.mpf("nan")
    if sep >= 2 or offcrit >= 2:
        verdict = "TYPE_SEPARATES"
    elif sep == 1 or offcrit == 1:
        verdict = "INCONCLUSIVE"
    else:
        verdict = "NO_TYPE_SEPARATION"
    print(f"\nVERDICT: {verdict}")
    print(f"max effect ratio (|Re L_FALSE / Re L_LINE|) = {float(max_eff):.2f}")
    print(f"elapsed {time.time() - t_start:.1f}s")


if __name__ == "__main__":
    main()
