#!/usr/bin/env python3
"""Half-disc Jensen-mass asymmetry probe.

Question: does A(t0) = M_right - M_left of the half-disc Jensen mass
(disc D(c,r), c = (1/2 +/- small, t0), r = 0.3, cut by the vertical line
Re(s) = 1/2) separate the TYPE of planted zero displacement -- off-line
(beta = 0.9, FE-forced mirror 0.1) from on-line (t0 -> t0+0.3, t0 -> t0+0.5)?

Hypothesis mechanism: on-line zeros (Re rho = 1/2) are fixed points of the
mirror map s <-> 1-s; they sit exactly on the cut, so they contribute equally
to the mirror half-discs: 0 to the restricted zero sums (excluded from BOTH
halves, the "fixed point" rule) and a symmetric trough to the half-arc
integrals. An off-line zero at beta=0.9 sits well inside the right half and
depresses the right half-arc only (its FE mirror at 0.1 sits on the left but
at a different distance). Hence |A| should be large for off-line, ~0 for
on-line, and the no-implant baseline should look like the on-line group.

Model: the exact FE-symmetric planted construction of jensen_honest_probe.py
(finite Hadamard ratio R(s), NO e^{s/rho} factors -- they break xi(s)=xi(1-s);
R(1-s)=R(s) exactly since both zero sets are FE-closed with #P == #M mod 2).

Half-disc Jensen mass (adapted), per half h in {right, left}:
  M_h = B_h + Z_h
  B_h = mean of log|zeta_planted| over the boundary arc with Re(s) in h
        (genuine function evaluation via mpmath, dps=15; the ONLY term that
        can see zeros OUTSIDE the disc, e.g. beta=0.9 with r=0.3)
  Z_h = sum_{|rho-c|<r, Re(rho) in h} log(r/|rho-c|)   (Jensen zero term
        restricted per half; on-line zeros Re(rho)=1/2 lie exactly on the
        cut and are excluded from both halves)
  A(t0) = M_right - M_left = (B_right - B_left) + (Z_right - Z_left)
Both components are reported separately; the verdict uses A.

Controls: (a) 6 off-line implants beta=0.9 at t0 = gamma_1..gamma_6;
(b) 6 on-line implants at each of t0+0.3 and t0+0.5 (beta=0.5, exact same
FE machinery); (c) permutation p-values, 1000 draws, conservative
(1+count)/(1+N); (d) no-implant baseline at the same t0s.

Verdict: TYPE_SEPARATES iff p(off vs on-pooled) < 0.05 AND
mean|A_off| >= 3 * mean|A_on| AND p(base vs on-pooled) >= 0.05.
INCONCLUSIVE if off-line separates from on-line but the baseline does not
look on-line-like. NO_TYPE_SEPARATION otherwise. Raw distributions always
printed; no other thresholds imposed.

Run: uv run --with mpmath python3 tools/jensen_halfdisc_probe.py
"""
import random
import sys
import time

import mpmath as mp

mp.mp.dps = 15

ZEROS_FILE = "tools/data/zeros_verified_32k.txt"
N_IMPLANTS = 6            # t0 = gamma_n, n = 1..6 (all nearby, no cherry-pick)
N_PERM = 1000
SEED = 20260825
N_THETA = 800             # boundary samples per disc (full circle, midpoint rule)
CONFIGS = [(0.52, 0.3), (0.48, 0.3)]      # c_re = 1/2 +/- small, r = 0.3
DIAG_CONFIG = (0.6, 0.35)  # diagnostic only: disc reaches Re=0.95, so the
                           # restricted zero-sum term Z actually activates


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
    """FE-closed planted zero multiset at height t_p: {beta+-it_p,
    (1-beta)+-it_p} for beta != 1/2 (4 points); {1/2+-it_p} for beta = 1/2
    (2 points, no dupes)."""
    pts = [mp.mpc(beta) + 1j * mp.mpc(t_p), mp.mpc(beta) - 1j * mp.mpc(t_p)]
    if beta != mp.mpf("0.5"):
        pts += [mp.mpc(1) - mp.mpc(beta) + 1j * mp.mpc(t_p),
                mp.mpc(1) - mp.mpc(beta) - 1j * mp.mpc(t_p)]
    return pts


def corr_factor(s, t0, beta, t_p=None):
    """FE-exact finite ratio R(s) = prod_P (1-s/p) / prod_M (1-s/m), P =
    planted_set(beta, t_p), M = {1/2+-it0}. Identity swap (beta=1/2, t_p=t0)
    gives P=M and R=1 exactly. No e^{s/rho} factors (they break FE, see
    jensen_honest_probe.py). zeta_planted = zeta_true*R is exactly
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
    """Zeros of the model relevant to discs with Im >= 0 (conjugate partners
    at Im = -t_p are included in corr_factor for FE exactness but are never
    within reach of a disc here)."""
    if beta is None or (beta == mp.mpf("0.5") and t_p == t0):
        return [(mp.mpf("0.5"), g) for g in gammas]
    pts = [(mp.mpf("0.5"), g) for g in gammas if abs(g - t0) > mp.mpf("1e-12")]
    for p in planted_set(beta, t_p):
        if p.imag >= 0:
            pts.append((p.real, p.imag))
    return pts


# ---------------- half-disc machinery ----------------

def half_arc_averages(c_re, t, r, t0, beta, gammas, t_p=None, n=N_THETA):
    """(B_right, B_left): mean of log|zeta_model| over the boundary arc with
    Re(s) >= 1/2 (right) resp. Re(s) < 1/2 (left). Each half normalized by its
    own arc length. Genuine function evaluation -- this term sees zeros
    outside the disc (off-line beta=0.9 with r=0.3)."""
    if t_p is None:
        t_p = t0
    c = mp.mpc(c_re) + 1j * mp.mpc(t)
    rs = []
    ls = []
    for j in range(n):
        th = 2 * mp.pi * (j + 0.5) / n
        s = c + r * mp.e ** (1j * th)
        v = float(mp.log(abs(zeta_model(s, t0, beta, t_p))))
        if s.real >= 0.5:
            rs.append(v)
        else:
            ls.append(v)
    return sum(rs) / len(rs), sum(ls) / len(ls)


def half_zero_sums(c_re, t, r, t0, beta, gammas, t_p=None):
    """(Z_right, Z_left): Jensen zero term restricted per half,
    sum_{|rho-c|<r, Re(rho) in half} log(r/|rho-c|). Zeros with Re(rho)=1/2
    exactly (on-line) lie ON the cut and contribute to NEITHER half -- this
    is the fixed-point rule."""
    if t_p is None:
        t_p = t0
    c = mp.mpc(c_re) + 1j * mp.mpc(t)
    zr = mp.mpf(0)
    zl = mp.mpf(0)
    for re, im in model_zero_points(t0, beta, t_p, gammas):
        d = abs(mp.mpc(re) + 1j * mp.mpc(im) - c)
        if d <= r:
            if re > 0.5:
                zr += mp.log(r / d)
            elif re < 0.5:
                zl += mp.log(r / d)
    return float(zr), float(zl)


def A(c_re, t0, r, beta, gammas, t_p=None):
    """(A_B, A_Z, A): half-disc asymmetry at height t0. A = M_right - M_left
    = (B_right-B_left) + (Z_right-Z_left); the shared log|zeta(c)| term of the
    adapted Jensen mass cancels in the difference."""
    if t_p is None:
        t_p = t0
    br, bl = half_arc_averages(c_re, t0, r, t0, beta, gammas, t_p)
    zr, zl = half_zero_sums(c_re, t0, r, t0, beta, gammas, t_p)
    ab = br - bl
    az = zr - zl
    return ab, az, ab + az


# ---------------- statistics ----------------

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


def verdict(A_off, A_on, A_base, rng):
    p_off_on, _ = permutation_p(A_off, A_on, rng)
    p_base_on, _ = permutation_p(A_base, A_on, rng)
    m_off = abs(sum(A_off) / len(A_off))
    m_on = abs(sum(A_on) / len(A_on))
    ratio = m_off / max(m_on, 1e-12)
    if p_off_on < 0.05 and ratio >= 3.0 and p_base_on >= 0.05:
        return "TYPE_SEPARATES", p_off_on, p_base_on, ratio
    if p_off_on < 0.05:
        return "INCONCLUSIVE", p_off_on, p_base_on, ratio
    return "NO_TYPE_SEPARATION", p_off_on, p_base_on, ratio


# ---------------- validation ----------------

def quadrature_boundary(c_re, t, r, f, n=N_THETA):
    tot = mp.mpf(0)
    for j in range(n):
        th = 2 * mp.pi * (j + 0.5) / n
        s = mp.mpc(c_re) + 1j * mp.mpc(t) + r * mp.e ** (1j * th)
        tot += mp.log(abs(f(s)))
    return tot / n


def S_full(c_re, t, r, gammas):
    """Full-disc Jensen closed form for TRUE zeta (validation reference)."""
    c = mp.mpc(c_re) + 1j * mp.mpc(t)
    ssum = mp.log(abs(mp.zeta(c)))
    for re, im in [(mp.mpf("0.5"), g) for g in gammas]:
        d = abs(mp.mpc(re) + 1j * mp.mpc(im) - c)
        if d <= r:
            ssum += mp.log(r / d)
    return ssum


def validate(gammas):
    ok = True
    t0 = gammas[0]
    print("-- model verification --")
    v = abs(zeta_model(mp.mpc(0.9) + 1j * t0, t0, mp.mpf("0.9")))
    ok &= v < 1e-8
    print(f"  planted zero at 0.9+it0 present: |zeta_planted| = {v:.2e} (want <1e-8)")
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
    ok &= 1e-4 < abs(lim) < 10
    print(f"  on-line zero at 0.5+it0 removed: |zeta_planted(limit)| = {abs(lim):.4f} (want 1e-4..10)")

    def xi(z):
        return mp.mpf("0.5") * z * (z - 1) * mp.pi ** (-z / 2) * mp.gamma(z / 2) * zeta_model(z, t0, mp.mpf("0.9"))
    s = mp.mpc(0.62) + 1j * (t0 + 1.7)
    fe = abs(xi(s) - xi(1 - s))
    ok &= fe < 1e-9
    print(f"  xi functional equation for planted model: |diff| = {fe:.2e} (want <1e-9)")
    s = mp.mpc(0.7) + 1j * (t0 + 1.1)
    d = abs(zeta_model(s, t0, mp.mpf("0.5")) - mp.zeta(s))
    ok &= d < 1e-12
    print(f"  beta=0.5 identity control == true zeta: |diff| = {d:.2e} (want <1e-12)")

    print("-- quadrature vs Jensen closed form (true zeta) --")
    for c_re, t, r in [(0.52, 15.0, 0.3), (0.48, 21.5, 0.3)]:
        cf = float(S_full(c_re, t, r, gammas))
        qd = float(quadrature_boundary(c_re, t, r, mp.zeta))
        ok &= abs(cf - qd) < 5e-2
        print(f"  c=({c_re},{t}) r={r}: closed={cf:+.4f} quadrature={qd:+.4f} |diff|={abs(cf-qd):.2e}")

    print("-- restricted zero-sum term (fixed-point rule) --")
    # disc (0.6, 0.35) reaches the planted zero at 0.9 (dist 0.3 < 0.35):
    zr, zl = half_zero_sums(0.6, t0, 0.35, t0, mp.mpf("0.9"), gammas)
    want = float(mp.log(mp.mpf("0.35") / mp.mpf("0.3")))
    ok &= abs(zr - want) < 1e-12 and abs(zl) < 1e-12
    print(f"  off-line: Z_right={zr:.6f} (want log(0.35/0.3)={want:.6f})  Z_left={zl:.6f} (want 0)")
    # on-line moved zero at (0.5, t0+0.3): dist 0.316 < 0.35, Re=0.5 -> on the
    # cut -> excluded from BOTH halves -> Z = 0
    zr, zl = half_zero_sums(0.6, t0, 0.35, t0, mp.mpf("0.5"), gammas, t0 + mp.mpf("0.3"))
    ok &= abs(zr) < 1e-12 and abs(zl) < 1e-12
    print(f"  on-line moved: Z_right={zr:.6f}  Z_left={zl:.6f}  (both 0: zero on the cut)")
    # baseline: all zeros Re=0.5 -> on the cut -> Z = 0
    zr, zl = half_zero_sums(0.6, t0, 0.35, t0, None, gammas)
    ok &= abs(zr) < 1e-12 and abs(zl) < 1e-12
    print(f"  baseline:     Z_right={zr:.6f}  Z_left={zl:.6f}  (both 0: zeros on the cut)")
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
    groups = (("BASE", None, None),
              ("OFF", mp.mpf("0.9"), None),
              ("ON+0.3", mp.mpf("0.5"), mp.mpf("0.3")),
              ("ON+0.5", mp.mpf("0.5"), mp.mpf("0.5")))
    results = {}
    for c_re, r in CONFIGS + [DIAG_CONFIG]:
        diag = (c_re, r) == DIAG_CONFIG
        tag = "  [DIAGNOSTIC: disc reaches Re=0.95, Z term active]" if diag else ""
        print(f"== config c_re={c_re}, r={r}{tag} ==")
        data = {}
        for label, beta, t_off in groups:
            As = [A(c_re, t0, r, beta, gammas, t0 + t_off if t_off is not None else None)
                  for t0 in gammas]
            data[label] = As
            AB = [a[0] for a in As]
            AZ = [a[1] for a in As]
            AA = [a[2] for a in As]
            print(f"  {label:<6} mean(A_B)={sum(AB)/len(AB):+.4f}  "
                  f"mean(A_Z)={sum(AZ)/len(AZ):+.4f}  mean(A)={sum(AA)/len(AA):+.4f}")
            print(f"          raw A: " + " ".join(f"{a:+.3f}" for a in AA))
        A_off = [a[2] for a in data["OFF"]]
        A_on = [a[2] for a in data["ON+0.3"]] + [a[2] for a in data["ON+0.5"]]
        A_base = [a[2] for a in data["BASE"]]
        v, p_off_on, p_base_on, ratio = verdict(A_off, A_on, A_base, rng)
        results[(c_re, r)] = (v, p_off_on, p_base_on, ratio)
        print(f"  p(off vs on)={p_off_on:.4f}  p(base vs on)={p_base_on:.4f}  "
              f"ratio mean|A_off|/mean|A_on|={ratio:.2f}")
        print(f"  VERDICT: {v}\n")

    prim = results[CONFIGS[0]]
    print(f"OVERALL (primary config c_re={CONFIGS[0][0]}, r={CONFIGS[0][1]}): {prim[0]}")
    print(f"  effect size ratio off/on: {prim[3]:.2f}")
    for c, (v, p_off_on, p_base_on, ratio) in results.items():
        print(f"  config {c}: {v}  ratio={ratio:.2f}  p_off_on={p_off_on:.4f}  "
              f"p_base_on={p_base_on:.4f}")
    print(f"elapsed {time.time() - t_start:.1f}s")


if __name__ == "__main__":
    main()
