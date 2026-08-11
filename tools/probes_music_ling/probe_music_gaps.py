#!/usr/bin/env python3
"""Probe M3.5/M6.1/M6.2/M6.3 (music-ling catalog): gap-distribution statistics battery.

Questions:
  (a) [M3.5] Gap entropy and KS distance of the empirical gap distribution vs
      Wigner-surmise (GUE proxy), exponential (Poisson), and a lattice (crystal proxy).
  (b) [M6.1] Zipf-style rank-size fit of the sorted gaps: is there a power law?
  (c) [M6.2] Surprisal: top-20 gaps under the Wigner model - local anomaly detector.
  (d) [M6.3] LZ76 compressibility of the binarized gap sequence vs shuffled control.

Data: tools/data/zeros_computed_10000.txt.
Expected: gaps close to Wigner/exp (not lattice); entropy ~1 nats; no LZ structure.
"""
import numpy as np

DATA = "data/zeros_computed_10000.txt"

def load(fn):
    g = []
    with open(fn) as f:
        for line in f:
            p = line.split()
            if len(p) >= 2:
                g.append(float(p[1]))
    return np.sort(np.array(g))

def wigner_pdf(s):
    return (np.pi / 2.0) * s * np.exp(-np.pi * s * s / 4.0)

def wigner_cdf(s):
    return 1.0 - np.exp(-np.pi * s * s / 4.0)

def lz76(seq):
    """LZ-type complexity (dictionary of substrings seen in the sequence; a valid
    LZ78-style complexity proxy). seq: bytes. Random binary string of length n gives
    c ~ n / log2(n)-ish; a constant/periodic string gives c ~ small."""
    n = len(seq)
    seen = set()
    c = 0
    i = 0
    while i < n:
        L = 0
        while i + L < n and seq[i:i + L + 1] in seen:
            L += 1
        ph = seq[i:i + L + 1]
        for k in range(1, len(ph) + 1):
            seen.add(seq[i:i + k])
        c += 1
        i += L + 1
    return c

def bin_entropy(vals, edges):
    """Shannon entropy (nats) of vals binned by edges - discrete entropy of the
    binned distribution (includes the ln(1/binwidth) discretization offset)."""
    h, _ = np.histogram(vals, bins=edges)
    p = h / h.sum()
    p = p[p > 0]
    return -np.sum(p * np.log(p))

def bin_entropy_pmf(pmf):
    p = pmf[pmf > 0]
    return -np.sum(p * np.log(p))

def main():
    x = load(DATA)
    n = x.size
    L = x[-1] - x[0]
    sp = L / (n - 1)
    u = (x - x[0]) / sp
    gaps = np.diff(u)
    m = gaps.size
    print(f"n={n}  gaps={m}  mean gap={gaps.mean():.4f}  std={gaps.std():.4f}")

    # ---- KS distances ----
    gs = np.sort(gaps)
    ecdf = np.arange(1, m + 1) / m
    ks_wig = np.max(np.abs(ecdf - wigner_cdf(gs)))
    ks_exp = np.max(np.abs(ecdf - (1.0 - np.exp(-gs))))
    print("\n== M3.5 KS distances ==")
    print(f"vs Wigner-surmise (GUE proxy):  {ks_wig:.4f}")
    print(f"vs exponential (Poisson):       {ks_exp:.4f}")
    print(f"fraction of gaps within 0.05 of 1 (lattice closeness): {np.mean(np.abs(gaps-1) < 0.05):.4f}")
    print(f"mean |gap-1| (lattice would be ~0): {np.mean(np.abs(gaps-1)):.4f}")

    # ---- entropy of binned gaps (same binning for all models) ----
    bins = np.arange(0, 8.0, 0.1)
    H_emp = bin_entropy(gaps, bins)
    # exponential(1) discretized to the same bins (analytic)
    p_exp = np.exp(-bins[:-1]) - np.exp(-bins[1:])
    H_exp = bin_entropy_pmf(p_exp)
    # Wigner-surmise discretized to the same bins (numeric)
    p_wig = np.diff(wigner_cdf(bins))
    H_wig = bin_entropy_pmf(p_wig)
    print("\n== M3.5 gap entropy (binned, bin=0.1, nats; same binning all models) ==")
    print(f"empirical: {H_emp:.4f}   Wigner-surmise: {H_wig:.4f}   exponential(1): {H_exp:.4f}   lattice: 0.0000")

    # ---- Zipf rank-size ----
    gd = np.sort(gaps)[::-1]
    rank = np.arange(1, m + 1)
    lg = np.log(gd)
    lr = np.log(rank)
    # fit log(rank) ~ a + b*log(gap)
    A = np.vstack([np.ones(m), lg]).T
    coef, res, *_ = np.linalg.lstsq(A, lr, rcond=None)
    pred = A @ coef
    ss_res = np.sum((lr - pred) ** 2)
    ss_tot = np.sum((lr - lr.mean()) ** 2)
    r2 = 1 - ss_res / ss_tot
    print("\n== M6.1 Zipf rank-size fit ==")
    print(f"slope (log rank vs log gap): {coef[1]:.4f}   R^2={r2:.4f}")
    print("(Zipf power law would give slope ~ -1 with high R^2; exponential gaps give a log-linear curve)")

    # ---- surprisal top-20 ----
    surpr = -np.log(np.maximum(wigner_pdf(gaps), 1e-300))
    order = np.argsort(surpr)[::-1][:20]
    print("\n== M6.2 surprisal top-20 (under Wigner model) ==")
    print("idx    gap      surprisal   zero index (1-based)   ordinate")
    for i in order:
        print(f"{i+1:5d}  {gaps[i]:7.4f}  {surpr[i]:9.3f}   {i+2:5d}              {x[i+1]:10.4f}")

    # ---- LZ76 ----
    seq = (gaps < 1.0).astype(np.uint8).tobytes()
    rng = np.random.default_rng(7)
    seq_sh = rng.permutation(np.frombuffer(seq, dtype=np.uint8)).tobytes()
    c_real = lz76(seq)
    c_shuf = lz76(seq_sh)
    print("\n== M6.3 LZ76 (binarized gap<1 sequence) ==")
    print(f"LZ76 real = {c_real}   shuffled control = {c_shuf}")
    print("(ratio ~ 1 -> no sequential compressible structure)")

if __name__ == "__main__":
    main()
