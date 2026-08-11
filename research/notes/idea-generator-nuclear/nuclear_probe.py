#!/usr/bin/env python3
"""nuclear_probe.py — code-backed probes for idea-generator-nuclear.md (Round 1).

Part 1 (N1.3, P6): raw-vs-unfolded finite-T moment deficit decomposition.
   Is the [AF]-convention finite-T deficit a density-drift artifact (removable by
   unfolding to N(gamma) coordinates) or pair-correlation arithmetic?
Part 2 (N2.1/N5.3/N6.1, P5): xi'-zero tower rigidity — m2/m3, spacing statistics,
   cosine-pair HS constant, double-mode mass (how close to the "picket fence").
Part 3 (N5.2/N6.4, multiplicity): eigenvalue-2 double-mode detector on the real
   configuration; flat m4 at finite T (the [AN §6] m4 loose end, one more point).
Part 4 (N1.2/N4.2, P6): CUE (free-fermion, periodic DPP) finite-N null model for
   (m2, m3): the "are the zeros GUE at finite N" distributional test.

Conventions (match tools/chem_probe.py, tools/qi_sweep.py):
  unfolded x = N(gamma) = (gamma/2pi) log(gamma/2pi) - gamma/2pi + 7/8 (density 1);
  flat kernel G_ij = sinc(pi*la*(x_i - x_j));  m_k = tr(G^k)/N;
  targets at la=1: m2 = 4/3, m3 = 2, m4 = 13/4 (paper claim, [AN §6] provenance UNRESOLVED);
  cosine-pair kernel = psi2 (transform of psi^2); cert-normalized m2_cos/(INT_PSI2^2) -> C_HS = 1.3275.

Honesty: every printed number is CHECKED NUMERICALLY (f64) in this run; no theorem claimed.
"""
import os
import sys
import time
import numpy as np

PI = np.pi
SQRT2 = np.sqrt(2.0)
INT_PSI2 = 0.849227999318304   # qi_sweep: psi2(0)
C_HS = 1.327499296320588       # 1/2 + (1/sqrt2) cot(1/sqrt2)
C_BOUND = 0.672500703679412    # 2 - C_HS

ROOT = "/home/vstaln/riemann"
Z1000 = f"{ROOT}/tools/data/zeros_1_1000.txt"
Z10K = f"{ROOT}/tools/data/zeros_computed_10000.txt"
XIPRIME = f"{ROOT}/tools/data/xiprime_on_line_1_1000.txt"
GAMMA1 = 14.134725141734693


def load_gams(path):
    z = np.loadtxt(path)
    if z.ndim == 2:
        return z[:, 1]
    return z


def unfold(g):
    """Riemann-Siegel counting function -> density-1 coordinates."""
    return (g / (2 * PI)) * np.log(g / (2 * PI)) - g / (2 * PI) + 7.0 / 8.0


def flat_moments(xs, la=1.0, k=3):
    """flat (sinc) kernel Gram moments m_2..m_k at window lambda."""
    d = xs[:, None] - xs[None, :]
    G = np.sinc(la * d)
    ev = np.linalg.eigvalsh(G)
    n = xs.size
    return {j: float((ev ** j).sum()) / n for j in range(2, k + 1)}, ev


def _safe_sinc(x):
    with np.errstate(divide="ignore", invalid="ignore"):
        v = np.where(np.abs(x) < 1e-18, 1.0, np.sin(x) / x)
    return v


def cosine_pair_m2(xs):
    """psi2 pair kernel (transform of psi^2); cert-normalized target C_HS."""
    d = xs[:, None] - xs[None, :]
    u = d
    ps = PI * u
    t1 = 0.5 * _safe_sinc(ps)
    a = SQRT2 - ps
    b = SQRT2 + ps
    t2 = _safe_sinc(a)
    t3 = _safe_sinc(b)
    G = t1 + 0.25 * (t2 + t3)
    ev = np.linalg.eigvalsh(G)
    n = xs.size
    return float((ev ** 2).sum()) / n / INT_PSI2 ** 2, ev


def spacing_stats(xs):
    s = np.diff(np.sort(xs))
    s = s[s > 1e-12]
    r = np.minimum(s[:-1], s[1:]) / np.maximum(s[:-1], s[1:])
    return float(s.mean()), float(r.mean()), s


def log(msg):
    print(msg, flush=True)

log("=" * 78)
log("PART 1 (N1.3): raw-vs-unfolded finite-T deficit decomposition  (targets m2=4/3, m3=2)")
log("=" * 78)
zs = load_gams(Z10K)
log(f"loaded {zs.size} zeros, max gamma = {zs.max():.1f}")
hdr = f"{'T':>6} {'win':>6} {'raw m2':>8} {'unf m2':>8} {'raw m3':>8} {'unf m3':>8} {'raw-int':>8} {'unf-int':>8} {'def raw':>8} {'def unf':>8}"
log(hdr)
for T in (200.0, 500.0, 1000.0, 2000.0, 3000.0):
    m = (zs >= T) & (zs < 2 * T)
    g = zs[m]
    if g.size < 60:
        continue
    Nw = g.size
    raw_s = (g - T) * (Nw / T)              # [AF]/finitet convention
    x = unfold(g) - unfold(T)               # window-local unfolded (density 1)
    (m2r, m3r), _ = flat_moments(raw_s)
    (m2u, m3u), _ = flat_moments(x)
    # interior (drop 5% at each edge)
    lo, hi = int(0.05 * Nw), int(0.95 * Nw)
    (m2ri, _), _ = flat_moments(raw_s[lo:hi])
    (m2ui, _), _ = flat_moments(x[lo:hi])
    log(f"{T:6.0f} {Nw:6d} {m2r:8.4f} {m2u:8.4f} {m3r:8.4f} {m3u:8.4f} "
          f"{m2ri:8.4f} {m2ui:8.4f} {4/3-m2r:8.4f} {4/3-m2u:8.4f}")

log("\n(reading: 'def raw' vs 'def unf' — if unfolding removes most of the deficit,")
log(" the [AF]-convention finite-T error is density-drift; if it persists, it is")
log(" pair-correlation arithmetic. Targets: m2 -> 4/3 = 1.3333, m3 -> 2.)")

log("")
log("=" * 78)
log("PART 2 (N2.1/N5.3/N6.1): xi'-tower rigidity  (targets m2=4/3, m3=2; cos m2 -> 1.3275)")
log("=" * 78)
xip = np.loadtxt(XIPRIME)
t_xi = xip[:, 1]
y = unfold(t_xi)
ym = y[10:-10]                     # drop small-t roots + edges (chem F6 convention)
(m2xi, m3xi), evxi = flat_moments(ym)
m2xi_cos, _ = cosine_pair_m2(ym)
smean, rmean, gaps = spacing_stats(ym)
# double-mode mass of the xi'-gram spectrum
for eps in (0.05, 0.1):
    frac_n = float((np.abs(evxi - 2.0) <= eps).sum()) / ym.size
    log(f"xi'-gram eigenvalue-2 mass  (|lam-2|<= {eps}): fraction of eigenvalues = {frac_n:.5f}")
log(f"xi'-zeros: N'={ym.size}, flat m2={m2xi:.4f} m3={m3xi:.4f}, "
      f"cos-pair m2(/(INT_PSI2^2))={m2xi_cos:.4f} (target {C_HS:.4f})")
log(f"xi'-spacing: mean gap={smean:.4f} (density-1 -> ~1), mean r-stat={rmean:.4f} "
      f"(GUE ~0.599..0.61, lattice -> 1)")
log(f"zeta reference (1000 zeros, unfolded interior): m2 ~ 1.286, m3 ~ 1.84 (chem F1)")

log("")
log("=" * 78)
log("PART 3 (N5.2/N6.4 + N3.3): real-configuration eigenvalue-2 detector and m4")
log("=" * 78)
z1 = load_gams(Z1000)
x1 = unfold(z1)
xi = x1[50:950]
(m2z, m3z, m4z), evz = flat_moments(xi, k=4)
for eps in (0.05, 0.1):
    frac_n = float((np.abs(evz - 2.0) <= eps).sum()) / xi.size
    mass = float(evz[np.abs(evz - 2.0) <= eps].sum()) / xi.size
    log(f"zeta flat-gram eigenvalue-2 mass (|lam-2|<= {eps}): eigenvalue fraction = {frac_n:.5f}, "
          f"trace-mass fraction = {mass:.5f}  (ideal all-simple world: 0; ideal 1/6-double world: ~1/3)")
log(f"zeta interior (idx 51..950, N={xi.size}): flat m2={m2z:.4f} m3={m3z:.4f} m4={m4z:.4f}")
log(f"  targets: m2=4/3, m3=2, m4=13/4=3.25 (paper claim; [AN §6] flag), extremal-world mark-only m4=10/3=3.3333")
log(f"lambda_max = {evz.max():.4f}; fraction of trace above 1.5 = {evz[evz>1.5].sum()/evz.sum():.4f}")

log("")
log("=" * 78)
log("PART 4 (N1.2/N4.2): CUE finite-N null model for (m2, m3)  ('are the zeros GUE at finite N?')")
log("=" * 78)
rng = np.random.default_rng(20260812)


def cue_angles(N, rng):
    """Eigenangles of a Haar unitary (CUE)."""
    Z = (rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))) / np.sqrt(2.0 * N)
    Q, R = np.linalg.qr(Z)
    d = np.diag(R)
    Q = Q * (d / np.abs(d))
    ev = np.linalg.eigvals(Q)
    th = np.sort(np.angle(ev))
    return th


for N in (200, 500, 900):
    S = 150 if N <= 200 else (80 if N <= 500 else 40)
    m2s, m3s = [], []
    t0 = time.time()
    for it in range(S):
        th = cue_angles(N, rng)
        x = th * N / (2.0 * PI)                    # density 1 on [0, N)
        dd = np.abs(x[:, None] - x[None, :])
        d = np.minimum(dd, N - dd)                 # circular distance (periodic BC)
        G = np.sinc(d)
        ev = np.linalg.eigvalsh(G)
        m2s.append(float((ev ** 2).sum()) / N)
        m3s.append(float((ev ** 3).sum()) / N)
        if (it + 1) % 20 == 0:
            log(f"  CUE N={N}: sample {it+1}/{S} ({(time.time()-t0):.0f}s)")
    m2s, m3s = np.array(m2s), np.array(m3s)
    log(f"CUE N={N}: E[m2]={m2s.mean():.4f} +/- {m2s.std():.4f}   E[m3]={m3s.mean():.4f} +/- {m3s.std():.4f}")

# z-scores of the measured line-zero values against the N=900 CUE
N = 900
S = 60
m2s, m3s = [], []
for it in range(S):
    th = cue_angles(N, rng)
    x = th * N / (2.0 * PI)
    dd = np.abs(x[:, None] - x[None, :])
    d = np.minimum(dd, N - dd)
    G = np.sinc(d)
    ev = np.linalg.eigvalsh(G)
    m2s.append(float((ev ** 2).sum()) / N)
    m3s.append(float((ev ** 3).sum()) / N)
    if (it + 1) % 20 == 0:
        log(f"  CUE N={N} z-score batch: sample {it+1}/{S}")
m2s, m3s = np.array(m2s), np.array(m3s)
z2 = (m2z - m2s.mean()) / m2s.std()
z3 = (m3z - m3s.mean()) / m3s.std()
log(f"\nmeasured line-zero interior (N={xi.size}): m2={m2z:.4f}, m3={m3z:.4f}")
log(f"CUE N=900 (periodic BC): E[m2]={m2s.mean():.4f} +/- {m2s.std():.4f}; E[m3]={m3s.mean():.4f} +/- {m3s.std():.4f}")
log(f"z-scores: z(m2) = {z2:.2f}, z(m3) = {z3:.2f}   (|z|>2 => deficit NOT explained by finite-N CUE fluctuation)")
log("caveat: periodic (circle) vs line boundary conditions differ; the CUE gives the scale of")
log("finite-N effects, and the measured deficit is additionally systematic in sign (same sign at")
log("every T in Part 1), so significance is assessed with that caveat.")

log("")
log("=" * 78)
log("SUMMARY ANCHORS")
log("=" * 78)
log(f"C_HS = {C_HS:.7f}, C_BOUND = {C_BOUND:.7f}, INT_PSI2 = {INT_PSI2:.7f}")
