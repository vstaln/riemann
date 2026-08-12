#!/usr/bin/env python3
"""superlaw_s3b.py -- FIXED probe of "super-law + S3 rigidity" (task-superlaw-s3.md).

Fixes the scaling bug in scripts/superlaw_s3.py: that script divided each block's
eigenvalues by the GLOBAL central-90% spacing, but every GUE block spans the full
semicircle, so blocks ended up with mean spacing ~500 -> all pair/triple counts 0,
G ~ identity, m3 ~ 1. The prior "C1+C2 jointly FAIL" verdict was computed on broken
data and is void.

Correct construction: per-block UNFOLDING by the semicircle CDF
F(w) = (w sqrt(4-w^2) + 4 asin(w/2))/(4 pi), y = n * F(w) for bulk points. Then every
block has mean spacing 1 and local statistics = sine process (standard unfolding).

Checks (all CHECKED NUMERICALLY by this script):
  A1. mean density: central-block median nearest-neighbor spacing ~ 1
  A2. in-band form factor F(a) ~ 1 on [0.05, 0.95] (pure GUE super-law)
  A3. windowed third moments m3(lam) vs sine-kernel closed form
      m3 = 1 + 3(1/lam - 2 J2) + 1/lam^2 - (6/lam) J2 + 2(1 - lam/2)
      -> {5, 13/4, 2} at lam = {1/2, 2/3, 1}  (PROVEN, attack-twobandwidth SS2)
      This is the integrated triple correlation S3 -- the certificate-relevant
      object (pointwise R3(a,b) in the RS range is ~0.005 and MC-noise-swamped;
      the windowed m3 is the discriminating statistic).
  B1. MARKED super-law (marks in {1,2}, double-prob q tuned to simple fraction p0),
      unit-marked-density rescaled: windowed marked m3(1/2) vs 5 (real zeros' value)
      and the diagram decomposition m3 = D + pair + T (attack-law-s3.md SS2).
  B2. D pinned = 4 - 3p0 = 1.95451; near-CUE-row lower bound D + 3u = 5.4419
      (PROVEN for ANY marked config with p0 + near-CUE rows, attack-law-s3 SS3).
      T measured vs prediction T ~ E[m]^3 * A3 (A3 = sine-kernel connected part
      = +1/2 at lam=1/2, +1/12 at lam=2/3, 0 at lam=1).
  Caveat recorded: i.i.d. 1/2-marking of GUE breaks the marked near-CUE rows
  (F_marked ~ E[m]^2*F ~ 1.41, not 1) -- so the measured pair part is NOT the
  row-pinned [3u,6u]; the pin applies to the true p0-family law (256-law blocks).
"""
import math
import numpy as np

p0 = 10909258999421303588095230195816054408197 / 16000000000000000000000000000000000000000
q = (1.0 - p0) / (1.0 + p0)

def semicdf(w):
    # semicircle CDF on [-2,2] (density sqrt(4-x^2)/(2 pi)), normalized to [0,1]
    return (w * np.sqrt(4.0 - w**2) + 4.0 * np.arcsin(w / 2.0)) / (4.0 * math.pi)

def gue_blocks(n, K, seed):
    rng = np.random.default_rng(seed)
    out = []
    for _ in range(K):
        A = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))) / math.sqrt(2.0 * n)
        out.append(np.linalg.eigvalsh((A + A.conj().T) / 2.0))
    return out

def unfold(blocks):
    xs = []
    for w in blocks:
        m = np.abs(w) < 1.9
        wb = w[m]
        y = len(wb) * semicdf(wb)
        xs.append(np.sort(y))
    return xs

def m3_window(xb, marks=None, lam=0.5):
    """(1/Nm) tr((M G)^3), G_ij = sinc(pi lam (x_i - x_j)) = np.sinc(lam*(x_i-x_j))."""
    if marks is None:
        marks = np.ones(len(xb))
    Nm = marks.sum()
    G = np.sinc(lam * np.subtract.outer(xb, xb))
    MG = marks[:, None] * G
    return np.trace(MG @ MG @ MG) / Nm

def decompose(xb, marks, lam):
    """marked m3 = D + pair + T (diagram identity, attack-law-s3.md SS2)."""
    n = len(xb)
    Nm = marks.sum()
    G = np.sinc(lam * np.subtract.outer(xb, xb))
    D = (marks**3).sum() / Nm
    mm = np.outer(marks, marks)
    K2 = G**2
    diag = (2.0 * marks**3).sum() / Nm   # i=j terms in the ordered sum
    pair = (3.0 / 2.0) * ((mm * (marks[:, None] + marks[None, :]) * K2).sum() / Nm - diag)
    MG = marks[:, None] * G
    m3 = np.trace(MG @ MG @ MG) / Nm
    T = m3 - D - pair
    return m3, D, pair, T

def inband_F(xs, marks_list, alphas):
    F = np.zeros(len(alphas))
    tot = 0.0
    for xb, m in zip(xs, marks_list):
        tot += m.sum()
        for ai, a in enumerate(alphas):
            F[ai] += abs(np.sum(m * np.exp(2j * math.pi * a * xb)))**2
    return F / tot

n, K, seed = 150, 400, 42
blocks = gue_blocks(n, K, seed)
xs = unfold(blocks)
Ntot = sum(len(x) for x in xs)
print(f"GUE blocks n={n} K={K} seed={seed}; bulk pts total {Ntot} (per block {Ntot//K})")

# A1 mean density
spac = []
for xb in xs:
    xc = xb[(xb > 0.15 * len(xb)) & (xb < 0.85 * len(xb))]
    spac.append(np.median(np.diff(xc)))
print(f"\n[A1] central-block median nearest-neighbor spacing: {np.mean(spac):.4f} (target 1.0)  [mean density]")

# A2 in-band form factor, pure GUE
alphas = np.linspace(0.05, 0.95, 19)
F0 = inband_F(xs, [np.ones(len(x)) for x in xs], alphas)
print(f"[A2] in-band F(a), a in [0.05,0.95] (pure GUE): mean {F0.mean():.5f}  max|F-1| {np.max(np.abs(F0-1)):.5f}")

# A3 windowed m3 pure GUE vs sine-kernel
print("[A3] windowed m3 (PURE GUE super-law) vs sine-kernel closed form (PROVEN):")
for lam, ref in ((0.5, 5.0), (2.0/3.0, 13.0/4.0), (1.0, 2.0)):
    vals = np.array([m3_window(xb, None, lam) for xb in xs])
    se = vals.std() / math.sqrt(K)
    print(f"  lam={lam:.4f}: mean {vals.mean():.5f} +- {se:.5f}   ref {ref}   dev {vals.mean()-ref:+.5f} ({(vals.mean()-ref)/ref*100:+.2f}%)")

# B marked super-law
print(f"\n[B] MARKED GUE super-law (marks in {{1,2}}, double-prob q={q:.6f}, simple fraction -> p0={p0:.8f})")
rng = np.random.default_rng(7)
xsm, msm = [], []
p1s = []
for xb in xs:
    nb = len(xb)
    m = 1 + (rng.random(nb) < q).astype(int)
    M = m.sum()
    xsm.append(xb * (M / nb))   # unit MARKED density (length becomes M)
    msm.append(m)
    p1s.append((m == 1).sum() / M)
p1_mean = sum(p1s) / K
print(f"  simple fraction: mean {p1_mean:.8f} (target {p0:.8f}, |dev| {abs(p1_mean-p0):.2e})")
F1 = inband_F(xsm, msm, alphas)
print(f"  in-band F_marked: mean {F1.mean():.5f}  max|F-1| {np.max(np.abs(F1-1)):.5f}")
print(f"    (caveat: i.i.d. 1/2-marking breaks marked near-CUE rows: E[m]^2 = {(1.0+q)**2:.4f}, "
      f"F_marked mean ~ {F1.mean():.4f}; the true p0-family uses 256-law blocks with near-CUE rows)")

print("  marked windowed m3 + diagram decomposition (m3 = D + pair + T):")
Em = 1.0 + q
print(f"    prediction for i.i.d. marks: D = E[m^3]/E[m] = {4.0-3.0*p0:.5f}; T ~ E[m]^3 * A3(lam)")
for lam, ref5, A3 in ((0.5, 5.0, 0.5), (2.0/3.0, 13.0/4.0, 1.0/12.0)):
    rows = [decompose(xb, m, lam) for xb, m in zip(xsm, msm)]
    m3 = np.mean([r[0] for r in rows]); D = np.mean([r[1] for r in rows])
    pr = np.mean([r[2] for r in rows]); T = np.mean([r[3] for r in rows])
    ok = all(abs(r[0] - (r[1] + r[2] + r[3])) < 1e-8 for r in rows)
    print(f"  lam={lam:.4f}: m3 {m3:.5f} = D {D:.5f} + pair {pr:.5f} + T {T:.5f}   "
          f"ref(sine/real-zeros) {ref5}; D pinned = 4-3p0 = {4.0-3.0*p0:.5f} (match {abs(D-(4.0-3.0*p0))<1e-8}); "
          f"identity holds: {ok}")
    print(f"    T vs E[m]^3*A3 = {Em**3 * A3:.5f};  near-CUE-row pin D+3u = 5.4419 (lam=1/2, PROVEN for p0+near-CUE rows)")

# B2: what the pin + measured T imply for the super-law family
print("\n  verdict (B): marked-windowed m3 of the super-law vs the real zeros' 5:")
print(f"    real zeros (all-simple marks): m3(1/2) = 5 (PROVEN sine-kernel)")
print(f"    super-law (marked, p0): measured m3(1/2) = (above); row-pinned bottom D+3u = 5.4419 > 5")
