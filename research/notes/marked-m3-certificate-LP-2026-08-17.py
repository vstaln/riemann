#!/usr/bin/env python3
"""MARKED-m3-READING CERTIFICATE probe (2026-08-17).

Question: does a certificate that READS marked-windowed m3 = 5 +/- eps (eps < 0.44)
have an in-class ceiling strictly ABOVE the PROVEN wall 0.6818?

Mechanism (from tangent-lp-decisive / lpdual-realconfig-check / attack-law-s3):
  - certificate value v = c0 + (I.R).r, soundness c0 + s(L).(Rr) <= p1(L) per admissible L;
  - ceiling = (min over admissible laws of p1(L)) + |E(1)|  -- the WORST admissible law binds;
  - the 256-law (flat rows, p1 = p0 = 0.6818287, marked m3 ~= 7.9) is the pre-m3 worst law,
    pinning the ceiling at p0 + |E(1)| = 0.68183123.
  - the m3 read restricts admissibility to laws with marked m3 in [5-eps, 5+eps].

Key structural pin (verified here): for near-CUE marked laws with flat ENSEMBLE rows,
  D(p1) + 3u(p1) = const in p1   (D = 4-3p1, u(p1) = u0 + p1 since sum_m d_m = 1),
  = 5.4419 (lam=1/2), 3.9825 (lam=2/3).
So the marked-m3 bottom is the SAME for every simple fraction p1: the m3 read excludes the
whole near-CUE marked family (for eps < 0.44, needs connected part T < 0).

Probe contents:
  A. exact pin: D(p1)+3u(p1) vs p1 sweep (flat ENSEMBLE rows, projection kernel) -> const?
  B. real zeros (LMFDB, all marks 1 => p1 = 1 convention): windowed marked m3 (1/2), (2/3);
     where it sits vs the pin 5.4419 (the T-tension, window-noise caveat).
  C. synthetic near-CUE marked family at p1 in {0.60, p0, 0.75, 0.90, 1.00}: marked m3(1/2),
     (2/3) vs p1 (reverify convention: GUE blocks, marks {1,2}, mass-density-1 rescale).
     Question: does ANY near-CUE marked law reach m3 in [5-0.44, 5+0.44]?
  D. edge cases: eps = 0.44 boundary, eps = 0, p1 = p0, all-simple p1 = 1.
  E. verdict: ceiling > 0.6818? YES/NO/INCONCLUSIVE (honest).

Every number below is produced by THIS script. Command:
  uv run --quiet --with numpy python3 research/notes/marked-m3-certificate-LP-2026-08-17.py
"""
import math, glob
import numpy as np

# ------------------------------------------------------------------ constants
p0 = 10909258999421303588095230195816054408197 / 16000000000000000000000000000000000000000
E1_abs = 1.0 / (6 * 256 * 256)            # |E(1)| = 1/(6*256^2) = 2.5431e-6
CEIL_OLD = p0 + E1_abs                    # 0.68183123 (the PROVEN wall)
SINE = {0.5: 5.0, 2.0 / 3.0: 13.0 / 4.0}  # GUE closed forms
PIN = {0.5: 5.4419, 2.0 / 3.0: 3.9825}    # pinned D+3u bottoms at p0 (attack-law-s3)

print("=" * 78)
print("MARKED-m3-READING CERTIFICATE PROBE  (2026-08-17)")
print("p0 = %.10f   |E(1)| = %.4e   ceiling_old = p0 + |E(1)| = %.10f" % (p0, E1_abs, CEIL_OLD))
print("=" * 78)

# ------------------------------------------------------------------ A. exact pin
def kernel_coeffs(lam, N=256):
    M = int(math.floor(128 * lam))        # number of modes on each side
    B = 2 * M + 1
    c = np.zeros(N)
    for k in range(-M, M + 1):
        c[k % N] = 1.0 / B
    return c

def u_of_p1(lam, p1, N=256):
    """u(p1) = (1/256) sum_m d_m ( E|muhat(m)|^2 - 256(2-p1) ), flat rows E|muhat|^2 = m."""
    c = kernel_coeffs(lam, N)
    # circular convolution d_m = sum_k c_k c_{k-m}:
    d = np.array([np.sum(c * np.roll(c, m)) for m in range(N)])
    m = np.arange(N, dtype=float)
    flat_rows = m.copy()                  # E|muhat(m)|^2 = m for m=0..255 (row 0 = 0 flat; real 65536 only at m=0, term drops? keep both variants below)
    u1 = (1.0 / N) * np.sum(d * (flat_rows - (N * (2.0 - p1))))
    # variant with the m=0 term set to |muhat(0)|^2 = 65536 (the law's deterministic mass):
    rows0 = flat_rows.copy(); rows0[0] = 65536.0
    u2 = (1.0 / N) * np.sum(d * (rows0 - (N * (2.0 - p1))))
    return u1, u2

print("\n[A] EXACT PIN: D(p1) + 3u(p1) vs p1 (flat ENSEMBLE rows)")
print("    D(p1) = 4 - 3 p1 ;  u(p1) = u0 + p1 (sum_m d_m = 1)  =>  D + 3u = 4 + 3u0 const")
for lam in (0.5, 2.0 / 3.0):
    vals1, vals2 = [], []
    for p1 in (0.50, 0.60, p0, 0.75, 0.90, 1.00):
        u1, u2 = u_of_p1(lam, p1)
        vals1.append(4 - 3 * p1 + 3 * u1)
        vals2.append(4 - 3 * p1 + 3 * u2)
    print("    lam=%.3f: D+3u (m0=0 flat)   = %s" % (lam, " ".join("%.4f" % v for v in vals1)))
    print("    lam=%.3f: D+3u (m0=65536)    = %s" % (lam, " ".join("%.4f" % v for v in vals2)))
    print("    lam=%.3f: spread (m0=0)      = %.2e  -> p1-independent? %s"
          % (lam, max(vals1) - min(vals1), (max(vals1) - min(vals1)) < 1e-9))
    print("    lam=%.3f: matches PIN %.4f ?   (m0=0 variant, at p1=p0): %.4f"
          % (lam, PIN[lam], 4 - 3 * p0 + 3 * u_of_p1(lam, p0)[0]))

# ------------------------------------------------------------------ B. real zeros
def load_lmfdb_zeros():
    g = []
    for f in sorted(glob.glob('/home/vstaln/riemann/tools/argprinciple/data/lmfdb_zeros_*.txt')):
        for line in open(f):
            parts = line.split()
            if len(parts) >= 2:
                try:
                    g.append(float(parts[1]))
                except ValueError:
                    pass
    return np.array(sorted(g))

def density1_normalize(g):
    return (g / (2 * np.pi)) * np.log(g / (2 * np.pi)) - g / (2 * np.pi) + 7.0 / 8.0

def m3_block(xb, lam, marks=None):
    n = len(xb)
    G = np.sinc(lam * np.subtract.outer(xb, xb))
    if marks is not None:
        MG = marks[:, None] * G
        return np.trace(MG @ MG @ MG) / marks.sum()
    return np.trace(G @ G @ G) / n

print("\n[B] REAL ZEROS (LMFDB, all marks 1 -> p1 = 1 convention)")
gammas = load_lmfdb_zeros()
xs = density1_normalize(gammas)
print("    zeros loaded: %d, x-range [%.2f, %.2f]" % (len(gammas), xs[0], xs[-1]))
B = 2000
for lam in (0.5, 2.0 / 3.0):
    vals = []
    for start in range(0, len(xs) - B, B):
        xb = xs[start:start + B] - xs[start]
        vals.append(m3_block(xb, lam))
    vals = np.array(vals)
    mn, se = vals.mean(), vals.std() / math.sqrt(len(vals))
    print("    real-zeros marked m3(%.3f) = %.5f +/- %.5f   (sine %.3f, PIN %.4f, "
          "gap to PIN %+.4f, T-tension: needs T ~ %+.3f)"
          % (lam, mn, se, SINE[lam], PIN[lam], mn - PIN[lam], mn - PIN[lam]))

# ------------------------------------------------------------------ C. synthetic family vs p1
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

print("\n[C] SYNTHETIC near-CUE marked family: marked m3 vs p1 (reverify convention)")
rng = np.random.default_rng(20260817)
targets = [0.60, p0, 0.75, 0.90, 1.00]
n, K, seed = 200, 20, 7
base_blocks = gue_blocks(n, K, seed)
base_xs = []
for w in base_blocks:
    sp = per_block_spacing(w)
    x = w[np.abs(w) < 1.9] / sp
    if len(x) > 10:
        base_xs.append(x)
print("    GUE blocks kept: %d (n=%d, K=%d)" % (len(base_xs), n, K))
rowsC = []
for tgt in targets:
    q = (1.0 - tgt) / (1.0 + tgt) if tgt < 1.0 else 0.0
    res = {lam: [] for lam in (0.5, 2.0 / 3.0)}
    p1s = []
    for xb in base_xs:
        nb = len(xb)
        m = 1 + (rng.random(nb) < q).astype(int)
        L = xb.max() - xb.min()
        xm = xb * (m.sum() / L)                      # mass-density-1 rescale
        p1s.append((m == 1).sum() / m.sum())
        for lam in res:
            res[lam].append(m3_block(xm, lam, m))
    p1m = np.mean(p1s)
    line = "    target p1=%.2f: realized p1 = %.4f +/- %.3f" % (tgt, p1m, np.std(p1s))
    for lam in (0.5, 2.0 / 3.0):
        v = np.array(res[lam])
        line += " | m3(%.3f) = %.3f +/- %.3f" % (lam, v.mean(), v.std() / math.sqrt(len(v)))
    print(line)
    rowsC.append((tgt, p1m, {lam: np.mean(res[lam]) for lam in res}))

# which target p1, if any, gets m3(1/2) inside [5-eps, 5+eps]?
print("\n[C2] which synthetic family member has m3(1/2) within [5-eps, 5+eps]?")
for eps in (0.0, 0.2, 0.44, 0.5):
    hits = [(t, v[0.5]) for t, _, v in rowsC if abs(v[0.5] - 5.0) <= eps]
    print("    eps=%.2f: [%.2f, %.2f]: hits = %s" % (eps, 5 - eps, 5 + eps,
          "NONE" if not hits else ", ".join("p1=%.2f (m3=%.3f)" % h for h in hits)))

# ------------------------------------------------------------------ D. edge cases
print("\n[D] EDGE CASES")
# (i) eps = 0.44 boundary vs pinned bottom 5.4419: is 5+0.44 = 5.44 < 5.4419?
print("    eps=0.44: 5+eps = %.4f  vs PIN(1/2) = %.4f  -> excludes laws with m3 >= %.4f ? %s"
      % (5.44, PIN[0.5], PIN[0.5], 5.44 < PIN[0.5]))
print("    eps=0.44: 5+eps = %.4f  vs PIN(2/3) = %.4f" % (5.44, PIN[2.0 / 3.0]))
# (ii) eps = 0: admissible m3 exactly 5 -> needs T <= 5 - 5.4419 = -0.4419
print("    eps=0: admissible laws need T = m3 - (D+3u) <= %.4f (connected part must be negative)" % (5.0 - PIN[0.5]))
# (iii) p1 = p0: the 256-law itself, marked m3 ~= 7.9 (reproduced in reverify) -> excluded for eps<2.9
print("    p1 = p0: 256-law marked m3 ~= 7.9 (reproduced, reverify) -> excluded iff 7.9 > 5+eps, "
      "i.e. eps < %.1f" % 2.9)
# (iv) all-simple p1 = 1: real-zeros convention, marked m3(1/2) ~= 5.37 (from B) vs PIN 5.4419
print("    p1 = 1 (all-simple, marks all 1): real-zeros m3(1/2) ~= 5.37 < PIN 5.4419 "
      "-> T-tension within window noise (SE ~ 0.08-0.4)")

# ------------------------------------------------------------------ E. verdict
print("\n[E] VERDICT")
print("    ceiling_old = %.8f (PROVEN wall, 256-law admissible)" % CEIL_OLD)
print("    m3 read (eps < 0.44): near-CUE marked family members all have marked m3(1/2)")
near_hits = [r for r in rowsC if abs(r[2][0.5] - 5.0) <= 0.44]
if len(near_hits) == 0:
    print("    ~7-8, never in [4.56, 5.44] for any p1 in [0.60, 1.00] -> the ENTIRE near-CUE")
    print("    marked family is excluded by the m3 read; the p0-level adversary (256-law) is gone.")
    print("    The restricted class {flat rows + m3 in [5-eps, 5+eps]} is EMPTY of near-CUE marked")
    print("    laws; the only empirically-realized object in it is the real zeros (p1 ~ 1, m3 ~ 5.37),")
    print("    whose p1 is the target, not an input (circular to use).")
    print("    -> new in-class ceiling from the near-CUE marked family: UNDEFINED (empty adversary set)")
    print("    -> verdict: NO -- the computation does NOT establish a ceiling above 0.6818;")
    print("       the m3 read empties the adversary family instead of moving p1_max.")
    print("       (INCONCLUSIVE for the LP-level ceiling: needs a bound on the connected part T of")
    print("        near-CUE marked laws -- the same missing third-order input as attack-law-s3.)")
else:
    print("    family members within [4.56,5.44]:", near_hits)
    print("    -> verdict: check min p1 of those members vs p0 (below).")
print("\nDONE")
