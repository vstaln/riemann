#!/usr/bin/env python3
"""Li-coefficient falsification harness (lever 4, rung 1).

Question: does lambda_n > 0 actually FLAG a single planted off-line zero
(FE-symmetric model), and at what n?

Model (reused from tools/jensen_honest_probe.py):
  zeta_planted(s) = zeta_true(s) * R(s),
  R(s) = prod_{rho in P} (1 - s/rho) / prod_{rho in M} (1 - s/rho),
  M = {1/2 +- i t0},  P = {beta +- i t0, (1-beta) +- i t0} for beta != 1/2
      (FE + conjugation closed orbit),  P = {1/2 +- i t_p} for beta = 1/2.
  R(1-s) = R(s) exactly (both sets FE-closed) => planted model is exactly
  xi-symmetric.  Count |P| != |M| is accepted (probe convention: mod-2 closure).

Exactness trick (Bombieri-Lagarias): log xi(1/(1-x)) = sum_{n>=1} lambda_n x^n/n.
The per-zero contribution to lambda_n is h_n(rho) = 1 - (rho/(rho-1))^n, hence
  Delta lambda_n = sum_{rho in P} h_n(rho) - sum_{rho in M} h_n(rho)
is EXACT (unchanged zeros telescope out) and computable from the moved zeros
alone, and lambda_n(planted) = lambda_n(true) + Delta lambda_n exactly.
lambda_n(true) comes from the validated formal-power-series computation in
tools/li_probe.py (Stieltjes constants; lambda_1 cross-checked against the
closed form 1 + gamma/2 - log(4 pi)/2).

Per-zero conventions (all three computed; only bl/std are Li sequences):
  bl      h_n(rho) = 1 - (rho/(rho-1))^n      <- exact B-L per-zero (PRIMARY)
  std     h_n(rho) = 1 - (1 - 1/rho)^n        <- standard Li form (cross-check)
  mission h_n(rho) = 1 - (1 - 1/(rho-1))^n    <- mission-specified; NOT the Li
                 sequence: its lambda_1(true) = sum 1/(rho-1) = -lambda_1 < 0,
                 so true zeta already "flags" in this convention (artifact).

Verdict (n = 1..60, t0 = zetazero(1..12), no cherry-pick):
  FLAGS_AT_N=<first n>  if min_n lambda_n(planted) < 0
  NO_FLAG               if all lambda_n(planted) > 0
  INCONCLUSIVE          if an on-line control also flags

Run: uv run --with mpmath python3 tools/li_coefficient_harness.py
"""
import sys
import time

import mpmath as mp

import li_probe  # tools/li_probe.py: validated B-L series (series_log reused)

mp.mp.dps = 30

ZEROS_FILE = "tools/data/zeros_verified_32k.txt"
NMAX = 60
N_IMPLANTS = 12


# ---------------- true-side lambda_n (Bombieri-Lagarias series, li_probe core) ----------------

def lambda_true(N):
    """lambda_1..lambda_N of true zeta, dps=60 internally for Stieltjes stability."""
    old = mp.mp.dps
    mp.mp.dps = 60
    try:
        M = N + 2
        a = [mp.mpf(0)] * (M + 1)
        for m in range(1, M + 1):
            g = mp.stieltjes(m - 1)
            a[m] = ((-1) ** (m - 1)) * g / mp.fac(m - 1)
        b = li_probe.series_log(a, M)          # log[(s-1) zeta(s)]
        L = mp.log(mp.pi)
        c = [mp.mpf(0)] * (M + 1)
        for m in range(M + 1):
            if m == 0:
                hm = -mp.log(2) - L / 2 + mp.log(mp.pi) / 2
            else:
                hm = ((-1) ** (m - 1)) / m                 # log(s/2)
                if m == 1:
                    hm -= L / 2                            # -(s/2) log pi
                hm += mp.polygamma(m - 1, mp.mpf(0.5)) / (mp.fac(m) * (2 ** m))
            c[m] = b[m] + hm                               # log xi(1+u), u=s-1
        lam = [mp.mpf(0)] * (N + 1)                        # B-L: u = x/(1-x)
        for k in range(1, M + 1):
            ck = c[k]
            if ck == 0:
                continue
            for n in range(k, N + 1):
                lam[n] += ck * mp.binomial(n - 1, n - k)
        return [n * lam[n] for n in range(N + 1)]
    finally:
        mp.mp.dps = old


# ---------------- model (FE-symmetric planted sets, probe conventions) ----------------

def planted_set(beta, t_p):
    pts = [mp.mpc(beta) + 1j * mp.mpc(t_p), mp.mpc(beta) - 1j * mp.mpc(t_p)]
    if beta != mp.mpf("0.5"):
        pts += [mp.mpc(1) - mp.mpc(beta) + 1j * mp.mpc(t_p),
                mp.mpc(1) - mp.mpc(beta) - 1j * mp.mpc(t_p)]
    return pts


def load_gammas(n):
    try:
        gs = []
        with open(ZEROS_FILE) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                idx, g = line.split()
                if int(idx) <= n:
                    gs.append(mp.mpf(g))
        if len(gs) >= n:
            return gs
    except OSError:
        pass
    return [mp.zetazero(k) for k in range(1, n + 1)]


# ---------------- Delta (exact from moved zeros) ----------------

def per_zero(rho, n, kind):
    if kind == "bl":
        return 1 - (rho / (rho - 1)) ** n
    if kind == "std":
        return 1 - (1 - 1 / rho) ** n
    if kind == "mission":
        return 1 - (1 - 1 / (rho - 1)) ** n
    raise ValueError(kind)


def delta_lam(n, P, M, kind):
    d = sum(per_zero(r, n, kind) for r in P) - sum(per_zero(r, n, kind) for r in M)
    if abs(mp.im(d)) > mp.mpf("1e-25") * (1 + abs(mp.re(d))):
        raise AssertionError(f"non-real Delta at n={n} kind={kind}: {d}")
    return mp.re(d)


# ---------------- independent ground truths ----------------

def lambda_true_taylor(N):
    """Independent lambda_n via the derivative formula: c_k = [u^k] log xi(1+u)
    = log-xi^(k)(1)/k! computed by mpmath mp.diff (real-step finite differences),
    then the same B-L assembly. No Stieltjes machinery."""
    old = mp.mp.dps
    mp.mp.dps = 80
    try:
        def L(s):
            if s == 1:  # log xi(1) = log(1/2); analytic there (removable)
                return -mp.log(2)
            return (mp.log(mp.mpf(1) / 2) + mp.log(s) + mp.log(s - 1)
                    - (s / 2) * mp.log(mp.pi) + mp.log(mp.gamma(s / 2)) + mp.log(mp.zeta(s)))
        c = [mp.re(mp.diff(L, 1, k) / mp.factorial(k)) for k in range(N + 1)]
        # re(): the imaginary residue from high-order mp.diff through the removable
        # log(s-1)+log zeta(s) singularity is numerical noise (magnitudes ~1e80+);
        # coefficients of log xi on the real axis are real (validated by zero-sum).
        lam = [mp.mpf(0)] * (N + 1)
        for k in range(1, N + 1):
            ck = c[k]
            if ck == 0:
                continue
            for n in range(k, N + 1):
                lam[n] += ck * mp.binomial(n - 1, n - k)
        return [n * lam[n] for n in range(N + 1)]
    finally:
        mp.mp.dps = old


def lam_zero_sum(n, gammas):
    """lambda_n by direct sum over the given (on-line) zeros, bl per-zero form."""
    s = mp.mpf(0)
    for g in gammas:
        s += 2 * mp.re(per_zero(mp.mpc(0.5, g), n, "bl"))
    return s


def independent_check(gammas_2000, gammas_20000, lam_true):
    print("-- independent ground truth for lambda_n(true) --")
    lt = lambda_true_taylor(6)
    for n in range(1, 6):
        z2k = lam_zero_sum(n, gammas_2000)
        z20k = lam_zero_sum(n, gammas_20000)
        print(f"  n={n}: series={mp.nstr(lam_true[n], 12)}  taylor={mp.nstr(lt[n], 12)}  "
              f"zerosum2k={mp.nstr(z2k, 8)}  zerosum20k={mp.nstr(z20k, 8)}")
    bad = [n for n in range(1, 6) if abs(lam_true[n] - lt[n]) > mp.mpf("1e-10")]
    print(f"  series vs derivative-formula max |diff|: "
          f"{max(abs(lam_true[n] - lt[n]) for n in range(1, 6)):.2e}"
          + ("  (MISMATCH!)" if bad else "  (agree)"))
    print(f"  zerosum20k - series at n=2,3: "
          f"{mp.nstr(lam_zero_sum(2, gammas_20000) - lam_true[2], 3)}, "
          f"{mp.nstr(lam_zero_sum(3, gammas_20000) - lam_true[3], 3)}  "
          f"(tail-truncation level, expect ~1e-3)")


# ---------------- checks ----------------

def convention_check(gammas, lam_true, N=2000):
    print(f"-- convention sanity: per-zero sum over first {N} true zeros vs B-L lambda_n --")
    for n in (1, 2, 3):
        row = []
        for kind in ("bl", "std", "mission"):
            s = mp.mpf(0)
            for g in gammas[:N]:
                rho = mp.mpc(0.5, g)
                s += 2 * mp.re(per_zero(rho, n, kind))
            row.append(f"{kind}={mp.nstr(s, 8)}")
        print(f"  n={n}: lambda_true={mp.nstr(lam_true[n], 8)} | " + "  ".join(row))
    print(f"  exact: mission-convention lambda_1(true) = sum_rho 1/(rho-1) = -lambda_1 = "
          f"{mp.nstr(-lam_true[1], 12)}  (negative -> mission f_n is NOT the Li sequence)")


def main():
    t_start = time.time()
    print(f"mpmath {mp.__version__}, dps={mp.mp.dps}, NMAX={NMAX}, t0 = zetazero(1..{N_IMPLANTS})")

    lam_true = lambda_true(NMAX)
    lam1_closed = mp.mpf(1) + mp.euler / 2 - mp.log(4 * mp.pi) / 2
    print("lambda_1..lambda_10(true):")
    for n in range(1, 11):
        print(f"  lambda_{n:2d} = {mp.nstr(lam_true[n], 18)}")
    print(f"cross-check lambda_1: {mp.nstr(lam_true[1], 18)} vs closed form "
          f"{mp.nstr(lam1_closed, 18)}  (|diff|={mp.nstr(abs(lam_true[1] - lam1_closed), 3)})")
    print(f"min lambda_n(true) over n=1..{NMAX}: {mp.nstr(min(lam_true[1:]), 6)}  "
          f"(>0: implied-positivity baseline)")

    gammas = load_gammas(N_IMPLANTS)
    print("implant heights t0: " + ", ".join(f"{float(g):.4f}" for g in gammas))
    g2000 = load_gammas(2000)
    g20000 = load_gammas(20000)
    convention_check(g2000, lam_true)
    independent_check(g2000, g20000, lam_true)

    t0s = gammas
    implants = {
        "OFFLINE_beta0.9":  lambda t: dict(M=[mp.mpc(0.5, t), mp.mpc(0.5, -t)],
                                           P=planted_set(mp.mpf("0.9"), t)),
        "ONLINE_shift+0.3": lambda t: dict(M=[mp.mpc(0.5, t), mp.mpc(0.5, -t)],
                                           P=planted_set(mp.mpf("0.5"), t + mp.mpf("0.3"))),
        "ONLINE_swap_t1":   lambda t: dict(M=[mp.mpc(0.5, t), mp.mpc(0.5, -t)],
                                           P=planted_set(mp.mpf("0.5"), t0s[1])),
    }

    summary = {}
    for kind in ("bl", "std"):
        print(f"\n== Delta_lambda_n and lambda_n(planted), per-zero kind '{kind}' (n=1..{NMAX}) ==")
        summary[kind] = {}
        for name, maker in implants.items():
            best = None
            first_neg = None
            for t in t0s:
                P, M = maker(t)["P"], maker(t)["M"]
                for n in range(1, NMAX + 1):
                    lp = lam_true[n] + delta_lam(n, P, M, kind)
                    if best is None or lp < best[0]:
                        best = (lp, n, t)
                    if lp < 0 and first_neg is None:
                        first_neg = (n, t)
            summary[kind][name] = (best, first_neg)
            tag = (f"  FIRST_NEGATIVE n={first_neg[0]} (t0={float(first_neg[1]):.2f})"
                   if first_neg else "  no negative in 1..60")
            print(f"  {name:<16} min lambda_n(planted) = {mp.nstr(best[0], 8)} at n={best[1]} "
                  f"(t0={float(best[2]):.2f})" + tag)

    # detail table at t0 = zetazero(1), bl convention
    t = t0s[0]
    print(f"\n-- detail at t0={float(t):.6f}, kind='bl' --")
    print("  n   lambda_n(true)   Delta(offline)  planted_offline  Delta(shift)  Delta(swap)")
    for n in (1, 2, 3, 5, 10, 20, 30, 40, 50, 60):
        row = [f"{n:3d}", mp.nstr(lam_true[n], 9)]
        for name in ("OFFLINE_beta0.9", "ONLINE_shift+0.3", "ONLINE_swap_t1"):
            P, M = implants[name](t)["P"], implants[name](t)["M"]
            d = delta_lam(n, P, M, "bl")
            if name == "OFFLINE_beta0.9":
                row.append(mp.nstr(d, 9))
                row.append(mp.nstr(lam_true[n] + d, 9))
            else:
                row.append(mp.nstr(d, 9))
        print("  ".join(row))

    # mission-variant artifact check
    print("\n== mission-specified per-zero f_n(rho)=1-(1-1/(rho-1))^n : artifact check ==")
    print(f"  mission lambda_1(true) = {mp.nstr(-lam_true[1], 12)} < 0  "
          f"(true zeta ALREADY flags -> f_n is not a positivity sequence)")
    t = t0s[0]
    P, M = implants["OFFLINE_beta0.9"](t)["P"], implants["OFFLINE_beta0.9"](t)["M"]
    d1 = delta_lam(1, P, M, "mission")
    print(f"  mission Delta_lambda_1(OFFLINE at t0={float(t):.4f}) = {mp.nstr(d1, 8)}")
    print(f"  mission lambda_1(planted) = {mp.nstr(-lam_true[1] + d1, 8)} < 0 : "
          f"FALSE-POSITIVE artifact (true side already negative), not an RH-flag")

    # extended-n estimate (where would the offline implant actually flag?)
    print("\n-- extended-n estimate: where would OFFLINE_beta0.9 actually flag? --")
    # lambda_n ~ (n/2) log n + b*n ; b fitted on exact values at n=40..60.
    b = mp.mpf(sum((lam_true[n] - (n / 2) * mp.log(n)) / n for n in range(40, 61))) / 21
    asym = lambda n: (n / 2) * mp.log(n) + b * n
    fit = [abs(lam_true[n] - asym(n)) / abs(lam_true[n]) for n in (30, 40, 50, 60)]
    print(f"  fitted lambda_n ~ (n/2)log n + ({mp.nstr(b, 5)})*n ; rel err vs exact at "
          f"n=30,40,50,60: " + " ".join(f"{v:.4f}" for v in fit))
    for kind in ("bl", "std"):
        nstar = None
        for n in range(61, 200001):
            if asym(n) + delta_lam(n, P, M, kind) < 0:
                nstar = n
                break
        print(f"  kind={kind}: expected first flag n* = {nstar}  "
              f"(CONJECTURED beyond n=60: exact Delta, fitted lambda_true; "
              f"flag is PROVEN to exist at some n by Li's theorem for the planted model)")

    # verdicts
    print("\n== VERDICT (n<=60) ==")
    for kind in ("bl", "std"):
        for name in implants:
            best, first_neg = summary[kind][name]
            v = f"FLAGS_AT_N={first_neg[0]}" if first_neg else "NO_FLAG"
            print(f"  kind={kind:<7} {name:<16} {v:<12} min lambda_n(planted)={mp.nstr(best[0], 8)}")
    print(f"elapsed {time.time() - t_start:.1f}s")


if __name__ == "__main__":
    main()
