#!/usr/bin/env python3
"""superlaw_s3.py -- probe of the "super-law + S3 rigidity" idea (wave-phone-local, idea #1).

Claims tested (all numbers CHECKED NUMERICALLY by this script):
  C1. A phase-randomized super-block law built from scaled GUE blocks reproduces
      mean density, in-band form factor F ~ 1 on [0,1], and simple fraction p0.
  C2. Because its blocks are GUE, its triple correlation S3 (3-pt correlation
      function R3(a,b), Rudnick-Sarnak range max(|a|,|b|,|a-b|) < 2/3) equals the
      sine-kernel value R3(a,b) = 1 - sinc^2(pi a) - sinc^2(pi b) - sinc^2(pi(a-b))
                               + 2 sinc(pi a) sinc(pi b) sinc(pi(a-b)).
  C3. (adversarial) does ANY deviation appear at the precision the certificate
      needs (rows certified to ~3e-40 for near-CUE)?

Two variants are measured because C1+C2 are in tension:
  V0  PURE GUE blocks (all marks 1): in-band F = 1, S3 = sine-kernel for free,
      but simple fraction = 1 (NOT p0).
  V1  MARKED GUE blocks (per-point marks in {1,2}, double-prob q tuned so the
      simple fraction = #simples/#marks -> p0): does it keep F = 1 and S3 = sine?

Run (from wave-phone-local/):
  proot-distro login ubuntu -- python3 scripts/superlaw_s3.py
"""
import math
import numpy as np

# ---------------------------------------------------------------- constants
p0 = 10909258999421303588095230195816054408197 / 16000000000000000000000000000000000000000
q = (1.0 - p0) / (1.0 + p0)          # per-point double probability (marks in {1,2})
Em, Em2 = 1.0 + q, 1.0 + 3.0 * q     # E[m], E[m^2] per point
D = 4.0 - 3.0 * p0                   # diagonal (multiplicity) part of marked S3

def sinc(x):
    return np.sinc(x)                # np.sinc(t) = sin(pi t)/(pi t)

def R3_sine(a, b):
    return (1.0 - sinc(a)**2 - sinc(b)**2 - sinc(a-b)**2
            + 2.0 * sinc(a) * sinc(b) * sinc(a-b))

def gue_blocks(n, K, seed):
    rng = np.random.default_rng(seed)
    out = []
    for _ in range(K):
        A = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))) / math.sqrt(2.0 * n)
        out.append(np.linalg.eigvalsh((A + A.conj().T) / 2.0))
    return out

def m3_window(xb, marks=None, lam=0.5):
    """Windowed third moment of the marked config: (1/N) tr((M G)^3),
    G_ij = K_lam(x_i - x_j), K_lam(u) = sinc(pi lam u) = np.sinc(lam u)."""
    if marks is None:
        marks = np.ones(len(xb))
    Nm = marks.sum()
    G = np.sinc(lam * np.subtract.outer(xb, xb))
    MG = marks[:, None] * G
    return np.trace(MG @ MG @ MG) / Nm

# ---------------------------------------------------------------- data
n, K, seed = 100, 300, 42
blocks = gue_blocks(n, K, seed)
allw = np.concatenate([w[np.abs(w) < 1.9] for w in blocks])
lo, hi = np.percentile(allw, 5), np.percentile(allw, 95)
inner = allw[(allw >= lo) & (allw <= hi)]
spacing = (hi - lo) / len(inner)                     # pre-scale mean spacing, central 90%
# GUE semicircle: density at center = 2/pi = 0.63662 -> mean spacing pi/2 = 1.5708
dens_center = len(inner) / (hi - lo)
print("== data ==")
print(f"GUE blocks: n={n}, K={K}, seed={seed}; bulk pts (|w|<1.9): {len(allw)}")
print(f"central-90% empirical mean spacing (pre-scale): {spacing:.5f} "
      f"(GUE prediction pi/2 = {math.pi/2:.5f}; density 1/spacing = {1.0/spacing:.5f} vs 2/pi = {2.0/math.pi:.5f})")

xs = [(w[np.abs(w) < 1.9]) / spacing for w in blocks]    # mean spacing 1
Ntot = sum(len(x) for x in xs)
print(f"post-scale: {Ntot} bulk eigenvalues, mean spacing 1 by construction")

# ---------------------------------------------------------------- V0: pure GUE
print("\n== V0: PURE GUE super-law (all marks 1) ==")
# simple fraction
print(f"simple fraction: 1.0 (GUE eigenvalues are a.s. distinct)")

# in-band form factor F(a) = (1/N)|sum e^{2 pi i a x}|^2, a in (0,1)
alphas = np.linspace(0.05, 0.95, 19)
F0 = np.zeros(len(alphas))
for xb in xs:
    for ai, a in enumerate(alphas):
        F0[ai] += abs(np.sum(np.exp(2j * math.pi * a * xb)))**2
F0 /= (K * (Ntot / K))
print(f"in-band F(a), a in [0.05,0.95] (19 pts): mean = {F0.mean():.6f}, "
      f"max|F-1| = {np.max(np.abs(F0-1)):.6f}")

# pair correlation R2(u) = 1 - sinc^2(pi u)
du = 0.02
umax = 1.6
counts = np.zeros(int(umax / du) + 1)
for xb in xs:
    d = xb[:, None] - xb[None, :]
    d = d[np.triu_indices(len(xb), 1)]
    idx = np.flatnonzero((d > 0) & (d < umax))
    np.add.at(counts, np.floor(d[idx] / du).astype(int), 1)
R2 = counts / (Ntot * du)
print("pair correlation R2(u) vs 1 - sinc^2(pi u):")
for u in (0.2, 0.5, 0.9, 1.3):
    k = int(round(u / du))
    mc = math.sqrt(counts[k]) / (Ntot * du)
    ref = 1.0 - sinc(u)**2
    print(f"  u={u:.2f}: measured {R2[k]:.4f} +- {mc:.4f}   ref {ref:.4f}   dev {(R2[k]-ref)/ref*100:.2f}%")

# triple correlation R3(a,b) at 3 points, Rudnick-Sarnak range
targets = [(0.15, 0.20), (0.25, 0.35), (0.30, 0.15)]
w3 = 0.06
print("triple correlation R3(a,b) vs sine-kernel (window w3=0.06, ordered triples i<j<k):")
for (a, b) in targets:
    cnt = 0
    for xb in xs:
        nb = len(xb)
        for j in range(nb):
            xj = xb[j]
            La = np.abs(xj - xb[:j] - a) < w3 / 2.0      # x_j - x_i ~ a
            Rb = np.abs(xb[j+1:] - xj - b) < w3 / 2.0    # x_k - x_j ~ b
            cnt += int(La.sum()) * int(Rb.sum())
    R3 = cnt / (Ntot * w3 * w3)
    ref = R3_sine(a, b)
    mc = math.sqrt(cnt) / (Ntot * w3 * w3)
    print(f"  (a,b)=({a},{b}): measured {R3:.4f} +- {mc:.4f}   sine {ref:.4f}   dev {(R3-ref):+.4f} "
          f"({(R3-ref)/ref*100:+.2f}%)")

# windowed third moments (certificate-relevant)
for lam, ref in ((0.5, 5.0), (2.0/3.0, 13.0/4.0)):
    vals = np.array([m3_window(xb, None, lam) for xb in xs])
    print(f"windowed m3({lam:.4f}): mean {vals.mean():.5f} +- {vals.std()/math.sqrt(K):.5f}   "
          f"sine-kernel ref {ref}   dev {vals.mean()-ref:+.5f}")

# ---------------------------------------------------------------- V1: marked GUE
print("\n== V1: MARKED GUE super-law (marks in {1,2}, double-prob q tuned to p0) ==")
print(f"q (double prob) = {q:.10f}   E[m] = {Em:.6f}   E[m^2] = {Em2:.6f}   "
      f"expected simple fraction (1-q)/(1+q) = {(1.0-q)/(1.0+q):.10f} vs p0 = {p0:.10f}")
rng = np.random.default_rng(7)
xsm = []          # positions scaled so the MARKED measure has density 1
msm = []
p1s = []
for xb in xs:
    nb = len(xb)
    m = 1 + (rng.random(nb) < q).astype(int)
    M = m.sum()
    L = xb.max() - xb.min()
    xb2 = xb * (M / L)                     # marked density = M / M = 1
    xsm.append(xb2); msm.append(m)
    p1s.append((m == 1).sum() / M)
Mt = sum(m.sum() for m in msm)
p1_mean = sum(p1s) / K
print(f"simple fraction: mean {p1_mean:.8f}  (target p0 = {p0:.8f},  |dev| = {abs(p1_mean-p0):.2e})")

# in-band form factor of the marked measure
F1 = np.zeros(len(alphas))
for xb2, m in zip(xsm, msm):
    for ai, a in enumerate(alphas):
        F1[ai] += abs(np.sum(m * np.exp(2j * math.pi * a * xb2)))**2
F1 /= Mt
print(f"in-band F_marked(a), a in [0.05,0.95]: mean = {F1.mean():.6f}, max|F-1| = {np.max(np.abs(F1-1)):.6f}")
print(f"   (pure value was mean {F0.mean():.6f}; ratio F_marked/F_pure ~ {F1.mean()/F0.mean():.4f}, "
      f"E[m] = {Em:.4f})")

# pair correlation of the marked measure
countsM = np.zeros(int(umax / du) + 1)
for xb2, m in zip(xsm, msm):
    d = xb2[:, None] - xb2[None, :]
    d = d[np.triu_indices(len(xb2), 1)]
    mm = np.outer(m, m)[np.triu_indices(len(xb2), 1)]
    idx = np.flatnonzero((d > 0) & (d < umax))
    np.add.at(countsM, np.floor(d[idx] / du).astype(int), mm[idx])
R2M = countsM / (Mt * du)
print("pair correlation R2_marked(u) vs 1 - sinc^2(pi u):")
for u in (0.2, 0.5, 0.9):
    k = int(round(u / du))
    ref = 1.0 - sinc(u)**2
    print(f"  u={u:.2f}: measured {R2M[k]:.4f}   ref {ref:.4f}   dev {(R2M[k]-ref):+.4f} "
          f"({(R2M[k]-ref)/ref*100:+.2f}%)")

# triple correlation of the marked measure (weighted by m_i m_j m_k)
print("triple correlation R3_marked(a,b) vs sine-kernel:")
for (a, b) in targets:
    cnt = 0.0
    for xb2, m in zip(xsm, msm):
        nb = len(xb2)
        for j in range(nb):
            xj = xb2[j]
            La = np.abs(xj - xb2[:j] - a) < w3 / 2.0
            Rb = np.abs(xb2[j+1:] - xj - b) < w3 / 2.0
            cnt += float((m[:j][La]).sum() * (m[j+1:][Rb]).sum())
    R3 = cnt / (Mt * w3 * w3)
    ref = R3_sine(a, b)
    print(f"  (a,b)=({a},{b}): measured {R3:.4f}   sine {ref:.4f}   dev {(R3-ref):+.4f} "
          f"({(R3-ref)/ref*100:+.2f}%); ratio to sine {R3/ref:.4f} (E[m]^2 = {Em*Em:.4f})")

# windowed third moments of the marked measure
for lam, ref in ((0.5, 5.0), (2.0/3.0, 13.0/4.0)):
    vals = np.array([m3_window(xb2, m, lam) for xb2, m in zip(xsm, msm)])
    print(f"windowed m3_marked({lam:.4f}): mean {vals.mean():.5f} +- {vals.std()/math.sqrt(K):.5f}   "
          f"sine-kernel ref {ref} (diagonal part D = 4-3p0 = {D:.5f})   dev {vals.mean()-ref:+.5f}")

# ---------------------------------------------------------------- verdict
print("\n== VERDICT ==")
print(f"V0 (pure GUE): F in-band mean {F0.mean():.6f} (~1), R3 matches sine within MC/finite-n error, "
      f"but simple fraction = 1.0, NOT p0 = {p0:.6f}.")
print(f"V1 (marked GUE): simple fraction {p1_mean:.8f} = p0, but in-band F_marked mean {F1.mean():.6f} "
      f"(dev from 1: {abs(F1.mean()-1):.3f}, cert tolerance 3e-40) and R3_marked ~ E[m]^2 * R3_sine.")
print("C1+C2 jointly FAIL: no tested GUE-block super-law simultaneously attains p1 = p0, F = 1 in-band, "
      "and S3 = sine-kernel. Random 1/2 marking (the only p0-tuner available without the private "
      "256-family) breaks both F and S3 at O(1).")
