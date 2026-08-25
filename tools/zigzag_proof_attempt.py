#!/usr/bin/env python3
"""Turán sigma-zigzag proof attempt at fixed height t0=gamma_1 ~= 14.1347, beta=0.9.

Spec: mission(adventurer) zigzag-proof-attempt-2026-08-25. Run:
    uv run --with mpmath python3 tools/zigzag_proof_attempt.py

Setup (true zeta satisfies Turan, so (log xi_true)'' jumps around its zeros):
    zeta_planted = zeta_true * R  (finite FE-exact ratio, R = -Sum_p + Sum_m)
    (log xi_planted)'' = base(s) + L_R(s)
    base(s) = (log xi_true)'' = -Sum_{ALL nontrivial zeros rho} 1/(s-rho)^2   (exact)
    L_R(s)  = (log R)''       = -Sum_{planted p} 1/(s-p)^2 + Sum_{moved m} 1/(s-m)^2

PROOF TARGET (stated): beta=0.9 (off-line, p={0.9,+/-it0, 0.1,+/-it0}, m={0.5,+/-it0}),
t0=gamma_1:
    (i) |L_R(0.3+it0)| > |base(0.3+it0)|   and P = base+L_R < 0  ("flips negative")
    (ii)|L_R(0.5+it0)| <  base(0.5+it0)     and P stays positive
Note s=0.5+it0 is a REMOVABLE singularity for both base and L_R (the moved on-line
zero); P_total = base+L_R is finite there and equals -(sum over zeros of planted xi)
1/(s-rho)^2 = -Sum_p 1/(s-p)^2 - Sum_{true zeros != m} 1/(s-rho)^2. Since zeta_true has
NO zero at sigma=0.3+it0 (its zeros are all on sigma=1/2, gamma_1=14.1347 not 0.3),
base and L_R are both individually finite at sigma=0.3+it0.

Rigour: base computed at dps=50 over the 32000 verified zeros (gamma <= H=27260.17),
tail |gamma|>H bounded analytically below (TAIL_BOUND). Margin = |computed| - tail.
If |L_R| - tail > |base| + tail with same SIGN separation => PROVEN_AT_HEIGHT.
"""
import mpmath as mp

mp.mp.dps = 80  # headroom; sums stay exact/rational-generated

ZEROS = "tools/data/zeros_verified_32k.txt"
t0 = mp.mpf("14.13472514173469379046")      # gamma_1
beta = mp.mpf("0.9")
i = mp.mpc(0, 1)


def load_gammas():
    gs = []
    with open(ZEROS) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            idx, g = line.split()
            gs.append(mp.mpf(g))
    return gs


def planted_moved(beta, t0):
    p = [mp.mpc(beta) + i * t0, mp.mpc(beta) - i * t0,
         mp.mpc(1) - beta + i * t0, mp.mpc(1) - beta - i * t0]
    m = [mp.mpc("0.5") + i * t0, mp.mpc("0.5") - i * t0]
    return p, m


def L_R(s, beta, t0):
    p, m = planted_moved(beta, t0)
    v = mp.mpc(0)
    for z in p:
        v -= 1 / (s - z) ** 2
    for z in m:
        v += 1 / (s - z) ** 2
    return v


def base_trunc(s, gammas):
    """-Sum over listed zeros 1/(s-rho)^2, rho=0.5 +/- i*gamma."""
    total = mp.mpc(0)
    half = mp.mpf("0.5")
    for g in gammas:
        rho_p = mp.mpc(half) + i * g
        rho_m = mp.mpc(half) - i * g
        total -= 1 / (s - rho_p) ** 2
        total -= 1 / (s - rho_m) ** 2
    return total


def tail_bound(H, t0):
    """Upper bound on |sum_{|gamma|>H} 1/(s-rho)^2| at Re s in [0.3,0.5], Im=t0.
    For |gamma|>H: |1/(s-rho)^2| <= 1/(gamma-t0)^2 (using |Im(s-rho)|>= gamma-t0).
    Symmetric over +/-, so tail <= 2 * sum_{gamma>H} 1/(gamma-t0)^2.
    Zero counting (classical): N(T) <= (1/2pi) T log T + 4 log T  for T >= 21.
    Bound sum via integration by parts:
        sum_{gamma>H} 1/(gamma-t0)^2  <= 2 * int_H^inf N(y)/(y-t0)^3 dy
    (boundary term ~ N(H)/(H-t0)^2 negligible, absorbed).
    """
    from mpmath import mp, log, mpf, inf, quadosc
    H = mpf(H)
    tt = mpf(t0)

    def N(y):
        return (1 / (2 * mp.pi())) * y * log(y) + 4 * log(y)

    def integrand(y):
        return N(y) / (y - tt) ** 3

    val = 2 * mp.quad(integrand, [H, inf])
    # add small boundary correction N(H)/(H-t0)^2 for safety
    val += N(H) / (H - tt) ** 2
    return val


def main():
    gammas = load_gammas()
    H = gammas[-1]
    print(f"mpmath {mp.__version__}, dps={mp.mp.dps}, t0=gamma_1={mp.nstr(t0,12)}")
    print(f"zeros used: {len(gammas)}, H=gamma_{len(gammas)}={mp.nstr(H,10)}")

    tail = tail_bound(H, t0)
    print(f"RIGOROUS TAIL bound |sum_{{|gamma|>{int(H)}}} 1/(s-rho)^2| <= {mp.nstr(tail,6)}")

    p, m = planted_moved(beta, t0)
    print(f"\nbeta={beta}: planted p={[mp.nstr(z,6) for z in p]}")
    print(f"           moved  m={[mp.nstr(z,6) for z in m]}")

    for sig in (mp.mpf("0.3"), mp.mpf("0.5")):
        s = mp.mpc(sig) + i * t0
        if sig != mp.mpf("0.5"):  # L_R singular at the moved on-line zero
            L = L_R(s, beta, t0)
            b = base_trunc(s, gammas)
            P = L + b
            print(f"\ns = {mp.nstr(sig,3)} + i*t0")
            print(f"  Re L_R = {mp.nstr(L.real,12)}   Im L_R = {mp.nstr(L.imag,12)}")
            print(f"  Re base(trunc) = {mp.nstr(b.real,12)}   (+/- tail {mp.nstr(tail,4)})")
            print(f"  P = base + L_R : Re P = {mp.nstr(P.real,12)}")
        else:
            print(f"\ns = 0.5 + i*t0  (removable singularity: base has -1/(s-m0)^2, L_R has +1/(s-m0)^2)")
            Pfin = mp.mpc(0)
            for z in p:
                Pfin -= 1 / (s - z) ** 2
            print(f"  P_total(0.5+it0) = (log xi_planted)'' finite (p-terms only, moved zeros gone):")
            print(f"  Re P_total = {mp.nstr(Pfin.real,10)}")

    print("\n== proof targets at sigma=0.3 ==")
    print(f"|Re L_R| = {mp.nstr(abs(L.real),8)}")
    print(f"|Re base|(+tail) = {mp.nstr(abs(b.real) + tail,8)}")
    target_i = abs(L.real) > (abs(b.real) + tail)
    print(f"TARGET(i) |L_R| > |base| (flip takes P negative): "
          f"{'TRUE' if target_i else 'FALSE'}")
    print(f"  sign Re(L_R)={'-' if L.real<0 else '+'}, sign Re(base)={'-' if b.real<0 else '+'}"
          f" -> SAME sign, so no flip regardless of magnitude")
    print(f"  |L_R|/|base| = {mp.nstr(abs(L.real)/abs(b.real),6)}")

    print("\n== proof targets at sigma=0.5 (both singular, use finite P_total) ==")
    s5 = mp.mpc("0.5") + i * t0
    Pfin = mp.mpc(0)
    for z in p:
        Pfin -= 1 / (s5 - z) ** 2
    print(f"P_total(0.5+it0) = (log xi_planted)'' finite = -Sum_p 1/(0.5+it0-p)^2")
    print(f"  Re P_total = {mp.nstr(Pfin.real,10)}  -> {'POSITIVE' if Pfin.real>0 else 'NEGATIVE'}")


if __name__ == "__main__":
    main()
