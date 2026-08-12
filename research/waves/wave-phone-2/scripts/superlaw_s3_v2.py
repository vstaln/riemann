#!/usr/bin/env python3
"""superlaw_s3_v2.py -- decisive probe v2: marked-windowed m3 of the GUE super-law vs
the PROVEN real-zero values m3(1/2)=5, m3(2/3)=13/4 and the pinned bottoms 5.4419/3.9825.

Improvements over v1 (superlaw_s3_fixed.py):
  - LARGER blocks (n=500, K=60): v1's n=100 blocks gave a ~20% finite-size deficit on
    the pure-GUE reference (m3(0.5)=4.02 vs 5). Here the same deficit is measured at the
    SAME block size (V0 pure GUE = matched reference) and reported as a bias; the marked
    value is reported raw AND bias-corrected. The honest verdict uses the corrected one.
  - R2 sign bug fixed (ascending eigenvalues: use xb[None,:]-xb[:,None] for i<j).
  - Mark tuning verified against the notes: q=(1-p0)/(1+p0) gives E[m]=2/(1+p0),
    D=E[m^3]/E[m]=4-3p0, p0 = s/256 (simple count per mass) exactly as in
    attack-law-s3.md / attack-nevanlinna.md.

Run (host):  proot-distro login ubuntu -- python3 /root/riemann/research/waves/wave-phone-2/scripts/superlaw_s3_v2.py
"""
import math
import numpy as np

p0 = 10909258999421303588095230195816054408197 / 16000000000000000000000000000000000000000
q = (1.0 - p0) / (1.0 + p0)          # per-point double probability (verified vs notes)
Em, Em2, Em3 = 1.0 + q, 1.0 + 3.0 * q, 1.0 + 7.0 * q
D = 4.0 - 3.0 * p0                   # marked diagonal part (position-free) = Em3/Em

def sinc(x):
    return np.sinc(x)

def m3_window(xb, marks, lam):
    """Windowed marked third moment: tr((M G)^3)/sum(m), G = sinc(pi*lam*(x_i-x_j))."""
    if marks is None:
        marks = np.ones(len(xb))
    Nm = marks.sum()
    G = np.sinc(lam * np.subtract.outer(xb, xb))
    MG = marks[:, None] * G
    return np.trace(MG @ MG @ MG) / Nm

def per_block_spacing(w):
    wi = w[np.abs(w) < 1.9]
    lo, hi = np.percentile(wi, 5), np.percentile(wi, 95)
    return (hi - lo) / len(wi)

def gue_blocks(n, K, seed):
    rng = np.random.default_rng(seed)
    out = []
    for _ in range(K):
        A = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))) / math.sqrt(2.0 * n)
        out.append(np.linalg.eigvalsh((A + A.conj().T) / 2.0))
    return out

def R2_measure(xs, mss=None, du=0.02, umax=1.6):
    counts = np.zeros(int(umax / du) + 1)
    Mtot = 0.0
    for i, xb in enumerate(xs):
        d = xb[None, :] - xb[:, None]          # FIXED sign: d[i,j]=x_j-x_i > 0 for i<j
        d = d[np.triu_indices(len(xb), 1)]
        idx = np.flatnonzero((d > 0) & (d < umax))
        w = np.ones(len(idx)) if mss is None else np.outer(mss[i], mss[i])[np.triu_indices(len(xb), 1)][idx]
        np.add.at(counts, np.floor(d[idx] / du).astype(int), w)
        Mtot += (len(xb) if mss is None else mss[i].sum())
    return counts / (Mtot * du)

def R3_sine(a, b):
    return (1.0 - sinc(a)**2 - sinc(b)**2 - sinc(a-b)**2
            + 2.0 * sinc(a) * sinc(b) * sinc(a-b))

def main():
    n, K, seed = 500, 60, 42
    blocks = gue_blocks(n, K, seed)
    sp = [per_block_spacing(w) for w in blocks]
    xs = [(w[np.abs(w) < 1.9]) / sp[i] for i, w in enumerate(blocks)]
    xs = [x for x in xs if len(x) > 10]
    Ntot = sum(len(x) for x in xs)
    print("== data ==")
    print(f"GUE blocks n={n}, K={K}, seed={seed}; per-block spacing mean {np.mean(sp):.5f} "
          f"± {np.std(sp):.5f}; blocks kept {len(xs)}; total points {Ntot}")
    for x in xs:
        l, h = np.percentile(x, 5), np.percentile(x, 95)
        assert abs((h - l) / len(x) - 1.0) < 1e-9, "per-block mean spacing != 1"
    assert np.mean(sp) > 1e-6 and np.std(sp) / np.mean(sp) < 0.2, "per-block spacing not in GUE regime"

    # ---- V0: pure GUE (all marks 1): matched reference; measures the finite-size bias
    print("\n== V0: pure GUE (marks 1) — matched finite-size reference ==")
    R2 = R2_measure(xs)
    du = 0.02
    for u in (0.2, 0.5, 0.9, 1.3):
        k = int(round(u / du))
        ref = 1.0 - sinc(u)**2
        print(f"  R2 u={u:.2f}: measured {R2[k]:.4f}   ref {ref:.4f}   dev {R2[k]-ref:+.4f}")
    m3v0 = {}
    for lam, ref in ((0.5, 5.0), (2.0/3.0, 13.0/4.0)):
        vals = np.array([m3_window(x, None, lam) for x in xs])
        bias = vals.mean() - ref
        m3v0[lam] = vals
        print(f"  m3({lam:.4f}): mean {vals.mean():.5f} ± {vals.std()/math.sqrt(len(vals)):.5f}"
              f"   sine ref {ref}   bias {bias:+.5f}")

    # ---- V1: marked GUE (marks {1,2}, q tuned so simple fraction = p0) — DECISIVE
    print("\n== V1: MARKED GUE super-law (q = (1-p0)/(1+p0), simple fraction = p0) ==")
    print(f"q = {q:.10f}; E[m]={Em:.6f}, E[m^2]={Em2:.6f}, E[m^3]={Em3:.6f}; "
          f"D=E[m^3]/E[m]={D:.6f} (attack-law-s3: D=4-3p0=1.9545)")
    rng = np.random.default_rng(7)
    xsm, msm = [], []
    for xb in xs:
        nb = len(xb)
        m = 1 + (rng.random(nb) < q).astype(int)
        Msum = m.sum()
        L = xb.max() - xb.min()
        xsm.append(xb * (Msum / L))      # marked measure density 1 (mass density 1)
        msm.append(m)
    p1s = np.array([(m == 1).sum() / m.sum() for m in msm])
    print(f"simple fraction (s/Σm): mean {p1s.mean():.8f} (target p0 = {p0:.8f}, |dev| {abs(p1s.mean()-p0):.2e})")
    Mtot = sum(m.sum() for m in msm)

    R2M = R2_measure(xsm, msm)
    for u in (0.2, 0.5, 0.9):
        k = int(round(u / du))
        ref = 1.0 - sinc(u)**2
        print(f"  marked R2 u={u:.2f}: measured {R2M[k]:.4f}   ref {ref:.4f}   dev {R2M[k]-ref:+.4f}")

    print("\n  WINDOWED MARKED m3 (the decisive probe):")
    results = {}
    for lam, ref in ((0.5, 5.0), (2.0/3.0, 13.0/4.0)):
        pin = 5.4419 if lam == 0.5 else 3.9825
        vals = np.array([m3_window(xb2, m, lam) for xb2, m in zip(xsm, msm)])
        bias = m3v0[lam].mean() - ref          # matched finite-size bias from V0
        corr = vals.mean() - bias              # bias-corrected marked m3
        se = vals.std() / math.sqrt(len(vals))
        results[lam] = (vals.mean(), se, corr, ref, pin)
        print(f"    lam={lam:.4f}: marked m3 = {vals.mean():.5f} ± {se:.5f}"
              f"   (bias-corrected {corr:.5f})")
        print(f"      sine ref {ref}; pinned bottom (D+3u) {pin}; "
              f"raw vs ref {vals.mean()-ref:+.5f}; corrected vs pin {corr-pin:+.5f}")

    print("\n== VERDICT ==")
    m12, se12, c12, ref12, pin12 = results[0.5]
    m23, se23, c23, ref23, pin23 = results[2.0/3.0]
    print(f"marked m3(1/2) raw {m12:.4f} ± {se12:.4f}, bias-corrected {c12:.4f} "
          f"(zeros PROVEN 5; pin 5.4419)")
    print(f"marked m3(2/3) raw {m23:.4f} ± {se23:.4f}, bias-corrected {c23:.4f} "
          f"(zeros PROVEN 13/4 = 3.25; pin 3.9825)")
    sep = c12 > pin12 + 3 * se12 and c23 > pin23 + 3 * se23
    print(f"SEPARATION (corrected marked m3 > pin + 3σ at both λ): {'YES' if sep else 'NO'}")

if __name__ == "__main__":
    main()
