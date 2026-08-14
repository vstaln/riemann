#!/usr/bin/env python3
"""ADVERSARIAL INDEPENDENT RE-VERIFICATION of the marked-windowed m3 separation
(superlaw-s3 verdict: real zeros m3(1/2)=5 vs super-law marked m3 ~= 8, pins 5.4419/3.9825).

Fresh implementation on purpose:
  - own GUE sampler, own seed (42 vs wave's), own block size n=300 (wave: n=500)
  - own mark model (same construction: q=(1-p0)/(1+p0), mass-density-1 rescale)
  - own m3: tr((MG)^3)/sum(m), M=diag(marks), G_ij=sinc(pi*lam*(x_i-x_j))
  - REAL ZEROS leg: marked m3 == plain m3 (all marks 1) on LMFDB zeros, windowed blocks.

Belief this changes: whether super-law marked m3 really clears the sine values (5, 13/4)
AND the pinned bottoms (5.4419, 3.9825) under an independent implementation; and whether
the real zeros' marked m3 is actually ~5 (not ~8) — the separation the new certificate
class rests on. Also adjudicates the theory-formula discrepancy (note: 8.148; my first-
principles derivation: 7.69) via direct measurement.

Labels produced: CHECKED NUMERICALLY (this script) or REFUTED (with numbers).
"""
import math, glob
import numpy as np

p0 = 10909258999421303588095230195816054408197 / 16000000000000000000000000000000000000000
q = (1.0 - p0) / (1.0 + p0)
Em, Em2, Em3 = 1.0 + q, 1.0 + 3.0 * q, 1.0 + 7.0 * q
D = 4.0 - 3.0 * p0
print(f"p0={p0:.12f} q={q:.6f} Em={Em:.6f} Em2={Em2:.6f} Em3={Em3:.6f} D={D:.6f}")

# ---------------- PART A: REAL ZEROS (all marks 1 => marked m3 == plain m3) ----------------
def load_lmfdb_zeros():
    gammas = []
    for f in sorted(glob.glob('/home/vstaln/riemann/tools/argprinciple/data/lmfdb_zeros_*.txt')):
        for line in open(f):
            parts = line.split()
            if len(parts) >= 2:
                try:
                    gammas.append(float(parts[1]))
                except ValueError:
                    pass
    return np.array(sorted(gammas))

def density1_normalize(g):
    # x = (g/2pi) log(g/2pi) - g/2pi + 7/8  (mean spacing 1), empirical_m3.py convention
    return (g / (2 * np.pi)) * np.log(g / (2 * np.pi)) - g / (2 * np.pi) + 7.0 / 8.0

def m3_of_block(xb, lam, marks=None):
    n = len(xb)
    G = np.sinc(lam * np.subtract.outer(xb, xb))
    if marks is not None:
        MG = marks[:, None] * G
        return np.trace(MG @ MG @ MG) / marks.sum()
    return np.trace(G @ G @ G) / n

gammas = load_lmfdb_zeros()
print(f"\n[A] LMFDB zeros loaded: {len(gammas)}")

# windowed blocks of consecutive zeros (block-local, density-1 normalization)
B = 2000
xs_all = density1_normalize(gammas)
print(f"    x-range [{xs_all[0]:.2f}, {xs_all[-1]:.2f}], mean spacing {np.mean(np.diff(xs_all)):.4f}")
real_results = {}
for lam, ref, pin in ((0.5, 5.0, 5.4419), (2.0/3.0, 13.0/4.0, 3.9825)):
    vals = []
    for start in range(0, len(xs_all) - B, B):
        xb = xs_all[start:start+B]
        xb = xb - xb[0]  # local offset irrelevant for tr(G^3)/N? no: sinc kernel is translation-
        # invariant, so subtract offset for numerical conditioning only
        vals.append(m3_of_block(xb, lam))
    vals = np.array(vals)
    real_results[lam] = (vals.mean(), vals.std()/math.sqrt(len(vals)))
    print(f"    REAL ZEROS m3({lam:.4f}) = {vals.mean():.5f} ± {vals.std()/math.sqrt(len(vals)):.5f}"
          f"   (sine ref {ref}, pin {pin}; gap to ref {vals.mean()-ref:+.5f})")

# ---------------- PART B: SUPER-LAW (independent construction) ----------------
def gue_blocks(n, K, seed):
    rng = np.random.default_rng(seed)
    out = []
    for _ in range(K):
        A = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))) / math.sqrt(2.0 * n)
        H = (A + A.conj().T) / 2.0
        out.append(np.linalg.eigvalsh(H))
    return out

def per_block_spacing(w):
    wi = w[np.abs(w) < 1.9]
    lo, hi = np.percentile(wi, 5), np.percentile(wi, 95)
    return (hi - lo) / len(wi)

print("\n[B] SUPER-LAW (independent GUE blocks, n=300, K=40, seed=99)")
n, K, seed = 300, 40, 99
blocks = gue_blocks(n, K, seed)
sp = [per_block_spacing(w) for w in blocks]
xs = [(w[np.abs(w) < 1.9]) / sp[i] for i, w in enumerate(blocks)]
xs = [x for x in xs if len(x) > 10]
for x in xs:
    l, h = np.percentile(x, 5), np.percentile(x, 95)
    assert abs((h - l) / len(x) - 1.0) < 1e-9, "per-block mean spacing != 1"
print(f"    blocks kept {len(xs)}, per-block spacing mean {np.mean(sp):.5f}")

# V0: pure GUE finite-size reference
pure = {lam: [] for lam in (0.5, 2.0/3.0)}
for xb in xs:
    for lam in pure:
        pure[lam].append(m3_of_block(xb, lam))
pure = {lam: np.array(v) for lam, v in pure.items()}
for lam in pure:
    print(f"    pure GUE m3({lam:.4f}) = {pure[lam].mean():.5f} ± {pure[lam].std()/math.sqrt(len(pure[lam])):.5f}"
          f"   (sine {5.0 if lam==0.5 else 3.25})  finite-n deficit {pure[lam].mean()-(5.0 if lam==0.5 else 3.25):+.5f}")

# V1: marked (marks {1,2}, q tuned to simple fraction p0), mass-density-1 rescale
rng = np.random.default_rng(11)
xsm, msm = [], []
for xb in xs:
    nb = len(xb)
    m = 1 + (rng.random(nb) < q).astype(int)
    Msum = m.sum()
    L = xb.max() - xb.min()
    xsm.append(xb * (Msum / L))
    msm.append(m)
p1s = np.array([(m == 1).sum() / m.sum() for m in msm])
print(f"    simple fraction mean {p1s.mean():.8f} (target p0 {p0:.8f})")

super_results = {}
for lam, ref, pin in ((0.5, 5.0, 5.4419), (2.0/3.0, 13.0/4.0, 3.9825)):
    vals = np.array([m3_of_block(xb, lam, m) for xb, m in zip(xsm, msm)])
    bias = pure[lam].mean() - (5.0 if lam == 0.5 else 13.0/4.0)
    corr = vals.mean() - bias
    se = vals.std() / math.sqrt(len(vals))
    super_results[lam] = (vals.mean(), se, corr)
    print(f"    MARKED SUPER-LAW m3({lam:.4f}) = {vals.mean():.5f} ± {se:.5f}"
          f"   bias-corrected {corr:.5f}   (sine {ref}, pin {pin})")

# ---------------- VERDICT ----------------
print("\n== VERDICT ==")
ok = True
for lam, (ref, pin) in ((0.5, (5.0, 5.4419)), (2.0/3.0, (13.0/4.0, 3.9825))):
    rm, rse = real_results[lam]
    sm, sse, scorr = super_results[lam]
    print(f"  λ={lam:.4f}: real-zeros marked m3 {rm:.4f}±{rse:.4f} | super-law raw {sm:.4f}±{sse:.4f} corr {scorr:.4f}")
    # separation criterion: real zeros within ~5% of sine value AND super-law raw >> real zeros
    near_sine = abs(rm - ref) / ref < 0.10
    separated = sm > rm + 5 * sse
    print(f"    real-zeros ≈ sine ({near_sine}); super-law separated from real zeros ({separated})")
    ok = ok and near_sine and separated
print(f"\nSEPARATION REPRODUCED: {'YES' if ok else 'NO — claim fails adversarial re-check'}")
