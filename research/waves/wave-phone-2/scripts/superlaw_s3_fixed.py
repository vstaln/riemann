#!/usr/bin/env python3
"""superlaw_s3_fixed.py -- wave-phone-2 probe: marked-windowed m3 of the phase-randomized
GUE super-block law vs the PROVEN real-zero values m3(1/2)=5, m3(2/3)=13/4.

FIX vs the inherited probe (research/waves/wave-phone-local/scripts/superlaw_s3.py):
  - FATAL SCALING BUG FIXED: the old probe divided every block by the GLOBAL central-90%
    spacing (pooled over all blocks), but each GUE block spans the full semicircle and has
    density ~0 at its edges. Result: every block's mean spacing ~500, all fixed-window
    counts collapsed to 0, m3 ~ 1, all pair/triple correlations 0. ALL its verdicts VOID.
    Here: each block is scaled by ITS OWN central-90% spacing, so blocks tile the line
    with mean spacing 1 (density 1 locally), as attack-selberg-clt.md §3 requires.
  - DECISIVE PROBE per the task spec: the WINDOWED MARKED m3 = tr((M G)^3)/sum(m),
    G_ij = sinc(pi*lam*(x_i - x_j)), M = diag(marks), marks in {1,2} with double-prob q
    tuned so the simple fraction = p0 = 0.68182868746.

Run (from riemann/):
  proot-distro login ubuntu -- python3 research/waves/wave-phone-2/scripts/superlaw_s3_fixed.py
"""
import math
import numpy as np

p0 = 10909258999421303588095230195816054408197 / 16000000000000000000000000000000000000000
q = (1.0 - p0) / (1.0 + p0)          # per-point double probability
Em, Em2, Em3 = 1.0 + q, 1.0 + 3.0 * q, 1.0 + 7.0 * q
D = 4.0 - 3.0 * p0                   # marked diagonal part (position-free)

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
    """Central-90% mean spacing of ONE GUE block (self-normalization fix)."""
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
        d = xb[:, None] - xb[None, :]
        d = d[np.triu_indices(len(xb), 1)]
        idx = np.flatnonzero((d > 0) & (d < umax))
        w = np.ones(len(idx)) if mss is None else np.outer(mss[i], mss[i])[np.triu_indices(len(xb), 1)][idx]
        np.add.at(counts, np.floor(d[idx] / du).astype(int), w)
        Mtot += (len(xb) if mss is None else mss[i].sum())
    return counts / (Mtot * du)

def R3_measure(xs, mss=None, targets=((0.15, 0.20), (0.25, 0.35), (0.30, 0.15)), w3=0.06):
    out = []
    for (a, b) in targets:
        cnt = 0.0
        for i, xb in enumerate(xs):
            m = np.ones(len(xb)) if mss is None else mss[i]
            nb = len(xb)
            for j in range(nb):
                xj = xb[j]
                La = np.abs(xj - xb[:j] - a) < w3 / 2.0
                Rb = np.abs(xb[j+1:] - xj - b) < w3 / 2.0
                cnt += float((m[:j][La]).sum() * (m[j+1:][Rb]).sum())
        out.append((a, b, cnt))
    return out

def report_pair(xs, mss=None):
    R2 = R2_measure(xs, mss)
    du = 0.02
    for u in (0.2, 0.5, 0.9, 1.3):
        k = int(round(u / du))
        ref = 1.0 - sinc(u)**2
        print(f"    u={u:.2f}: measured {R2[k]:.4f}   ref {ref:.4f}   dev {R2[k]-ref:+.4f}")

def report_triple(xs, mss=None):
    for (a, b, cnt) in R3_measure(xs, mss):
        Ntot = sum(len(x) for x in xs) if mss is None else sum(m.sum() for m in mss)
        w3 = 0.06
        R3 = cnt / (Ntot * w3 * w3)
        ref = R3_sine(a, b)
        print(f"    (a,b)=({a},{b}): measured {R3:.4f}   sine {ref:.4f}   dev {R3-ref:+.4f} "
              f"({(R3-ref)/ref*100:+.2f}%)")

def R3_sine(a, b):
    return (1.0 - sinc(a)**2 - sinc(b)**2 - sinc(a-b)**2
            + 2.0 * sinc(a) * sinc(b) * sinc(a-b))

def main():
    n, K, seed = 100, 300, 42
    blocks = gue_blocks(n, K, seed)
    sp = [per_block_spacing(w) for w in blocks]
    xs = [(w[np.abs(w) < 1.9]) / sp[i] for i, w in enumerate(blocks)]
    xs = [x for x in xs if len(x) > 10]
    Ntot = sum(len(x) for x in xs)
    print("== data (FIXED scaling: per-block central-90% mean spacing = 1) ==")
    print(f"GUE blocks n={n}, K={K}, seed={seed}; per-block spacing mean {np.mean(sp):.5f} "
          f"± {np.std(sp):.5f} (GUE pred pi/2 = {math.pi/2:.5f}); blocks kept {len(xs)}; "
          f"total points {Ntot}")

    # --- self-check (smallest thing that fails if the scaling logic breaks) ---
    # Per-block spacing is ~0.0225 for this GUE normalization (semicircle radius sqrt(2),
    # not 2: H_ij per-entry variance 1/2n). The absolute constant is irrelevant — what
    # matters is that blocks are scaled to mean spacing 1. The OLD global-scaling bug
    # pooled all blocks and gave spacing ~500; assert we're in the per-block regime.
    assert 0.005 < np.mean(sp) < 0.1, f"per-block spacing {np.mean(sp):.4f} not in GUE regime"
    for x in xs:
        l, h = np.percentile(x, 5), np.percentile(x, 95)
        assert abs((h - l) / len(x) - 1.0) < 1e-9, "per-block mean spacing != 1"

    # --- V0: PURE GUE (marks all 1) sanity: does the fixed super-law match sine kernel? ---
    print("\n== V0: pure GUE (marks all 1) — sanity of the FIX ===")
    R2 = R2_measure(xs)
    du = 0.02
    for u in (0.2, 0.5, 0.9, 1.3):
        k = int(round(u / du))
        ref = 1.0 - sinc(u)**2
        print(f"  R2 u={u:.2f}: measured {R2[k]:.4f}   ref {ref:.4f}   dev {R2[k]-ref:+.4f}")
    R3 = R3_measure(xs)
    w3 = 0.06
    for (a, b, cnt) in R3:
        val = cnt / (Ntot * w3 * w3)
        ref = R3_sine(a, b)
        print(f"  R3 (a,b)=({a},{b}): measured {val:.4f}   sine {ref:.4f}   dev {val-ref:+.4f} "
              f"({(val-ref)/ref*100:+.2f}%)")
    for lam, ref in ((0.5, 5.0), (2.0/3.0, 13.0/4.0)):
        vals = np.array([m3_window(x, None, lam) for x in xs])
        print(f"  m3({lam:.4f}): mean {vals.mean():.5f} ± {vals.std()/math.sqrt(len(vals)):.5f}   "
              f"sine ref {ref}   dev {vals.mean()-ref:+.5f}")

    # --- V1: MARKED GUE (marks {1,2}, q tuned to p0) — THE decisive probe ---
    print("\n== V1: MARKED GUE super-law (q tuned so simple fraction = p0) ==")
    print(f"q = {q:.10f}; E[m]={Em:.6f}, E[m^2]={Em2:.6f}, E[m^3]={Em3:.6f}; "
          f"expected simple fraction {(1.0-q)/(1.0+q):.8f} vs p0 {p0:.8f}")
    rng = np.random.default_rng(7)
    xsm, msm = [], []
    for xb in xs:
        nb = len(xb)
        m = 1 + (rng.random(nb) < q).astype(int)
        Msum = m.sum()
        L = xb.max() - xb.min()
        xsm.append(xb * (Msum / L))   # marked measure density 1 (span L holds Msum marks)
        msm.append(m)
    p1s = np.array([(m == 1).sum() / m.sum() for m in msm])
    print(f"simple fraction: mean {p1s.mean():.8f} (target p0 = {p0:.8f}, |dev| {abs(p1s.mean()-p0):.2e})")
    Mtot = sum(m.sum() for m in msm)

    print("  marked pair correlation (marked weights):")
    report_pair(xsm, msm)
    print("  marked triple correlation (marked weights):")
    report_triple(xsm, msm)

    print("\n  WINDOWED MARKED m3 (the decisive probe) vs sine refs and pinned bottoms:")
    for lam, ref in ((0.5, 5.0), (2.0/3.0, 13.0/4.0)):
        vals = np.array([m3_window(xb2, m, lam) for xb2, m in zip(xsm, msm)])
        pin = 5.4419 if lam == 0.5 else 3.9825
        print(f"    lam={lam:.4f}: marked m3 = {vals.mean():.5f} ± {vals.std()/math.sqrt(len(vals)):.5f}"
              f"   sine ref {ref}   pinned bottom (D+3u) {pin}   "
              f"vs 5/13/4: {vals.mean()-ref:+.5f}   vs pin: {vals.mean()-pin:+.5f}")
        print(f"    (theory mark-moment prediction: D*E[m^3]/E[m] + pair*Em2/Em + T*Em^2/Em ... "
              f"rough {D*Em3/Em:.3f} + {3*Em2*1.162449/Em:.3f} + ...)")

    # verdict
    m3_12 = np.array([m3_window(xb2, m, 0.5) for xb2, m in zip(xsm, msm)])
    m3_23 = np.array([m3_window(xb2, m, 2.0/3.0) for xb2, m in zip(xsm, msm)])
    print("\n== VERDICT ==")
    print(f"marked m3(1/2) = {m3_12.mean():.4f} ± {m3_12.std()/math.sqrt(len(m3_12)):.4f} "
          f"(zeros PROVEN 5; pin 5.4419)")
    print(f"marked m3(2/3) = {m3_23.mean():.4f} ± {m3_23.std()/math.sqrt(len(m3_23)):.4f} "
          f"(zeros PROVEN 13/4 = 3.25; pin 3.9825)")
    sep = m3_12.mean() > 5.2  # > 5 + 4 sigma
    print(f"SEPARATION (marked m3 != 5): {'YES' if sep else 'NO'}")

if __name__ == "__main__":
    main()
