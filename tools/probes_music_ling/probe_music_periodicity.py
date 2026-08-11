#!/usr/bin/env python3
"""Probe M2.5/M3.1/M3.3 (music-ling catalog): periodicity / meter / oddity battery on real zeros.

Questions:
  (a) [M2.5] Does the real zero sequence carry ANY periodicity ("virtual fundamental")? The
      256-periodic extremal law has a delta-like autocorrelation peak at period 256 (rescaled
      units); GUE/Poisson has none. Report ACF at periods 16..512 and the max.
  (b) [M3.1] Subgrid ("meter") ratios 1/2, 1/3, 2/3 of the best period: any hierarchical
      structure?
  (c) [M3.3] Rhythmic oddity: fraction of shifts for which the occupied-grid sequence is
      invariant (period-halving rotations). Crystal (period 256): invariant under 128,64,...
      shifts. Aperiodic data: ~0.

Method: density-1 rescaled ordinates; occupancy grid with bin 0.5; ACF of the occupancy
sequence; oddity via rotational invariance of the binarized gap sequence.
Data: tools/data/zeros_computed_10000.txt.
Expected: flat ACF, no oddity -> reality is "aperiodic / GUE-like" (diagnostic).
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

def main():
    x = load(DATA)
    n = x.size
    L = x[-1] - x[0]
    sp = L / (n - 1)
    u = (x - x[0]) / sp  # density ~1

    binw = 0.5
    nb = int(np.ceil(L / binw))
    b = np.zeros(nb, dtype=np.float64)
    idx = np.clip((u / binw).astype(int), 0, nb - 1)
    np.add.at(b, idx, 1.0)
    mu = b.mean()
    print(f"n={n}  L={L:.1f}  bins={nb}  mean occ={mu:.4f}")

    # ACF via FFT (circular); use enough zero padding to avoid wrap artifacts is optional -
    # for a diagnostic, report circular ACF at lags << nb (wrap negligible).
    bm = b - mu
    acf = np.fft.irfft(np.abs(np.fft.rfft(bm)) ** 2, n=nb)
    denom = np.sum(bm * bm)
    acf = acf / denom if denom > 0 else np.zeros(nb)

    print("\n== periodicity scan: ACF at rescaled periods p (bin=%.2f) ==" % binw)
    for p in [16, 32, 64, 128, 256, 512]:
        lag = int(round(p / binw))
        if lag < nb:
            print(f"p={p:4d}  ACF={acf[lag]:+.4f}")
    lag256 = int(round(256 / binw))
    print(f"\nACF at crystal period 256: {acf[lag256]:+.4f}")
    imax = int(np.argmax(np.abs(acf[1:])) + 1)
    print(f"max |ACF| over lags 1..{nb-1}: {np.abs(acf[imax]):.4f} at lag {imax} (p={imax*binw:.1f})")
    print("noise floor ~ +/- %.4f (1/sqrt(#bins))" % (1.0 / np.sqrt(nb)))

    # subgrid ratios at the best period
    if imax > 1:
        for r in [1/2, 1/3, 2/3]:
            lag = max(int(round(imax * r)), 1)
            print(f"subgrid {r:.3f} of best period: ACF(lag {lag}, p={lag*binw:.1f}) = {acf[lag]:+.4f}")

    # oddity: binarize gaps (<1 vs >=1) and count shifts that leave the sequence invariant
    gaps = np.diff(u)
    seq = (gaps < 1.0).astype(np.uint8)
    m = seq.size
    # rotational self-match for shifts s; use cyclic comparison on a sample of shifts
    def selfmatch(s):
        return np.mean(seq[s:] == seq[:m - s])
    shifts = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    print("\n== M3.3 oddity: self-match under shift s (1 = fully periodic) ==")
    for s in shifts:
        print(f"s={s:4d}  selfmatch={selfmatch(s):.5f}")
    print("crystal (period 256, all marks on grid): selfmatch = 1 at s in {128,64,...}")
    print("aperiodic data: selfmatch ~ 0.5 (random) for all s")

    # period-halving check at the crystal period
    s128 = selfmatch(128) if m > 128 else float('nan')
    print(f"\nperiod-halving rotation (s=128) selfmatch: {s128:.5f}")

if __name__ == "__main__":
    main()
