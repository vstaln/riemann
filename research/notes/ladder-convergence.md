# Q3 LADDER — honest finding: the per-atom tr Ψ ladder is the WRONG functional

**Date:** 2026-08-12. **Status:** NEGATIVE with a valuable methodological finding.
**Labels:** all numbers CHECKED NUMERICALLY (my own minimization); the functional-identification
PROVEN-FROM-SOURCE (ainta's verify_seven.py, read directly).

## What I computed (and why it's wrong for the certificate)

I wrote an independent per-atom stability-floor minimizer
(`research/ladder-convergence/ladder_floor_fast.py`): for a block of n consecutive
simple-zero atoms with gaps u₁..u_{n−1} (span ≤ 4), minimize `tr Ψ(G_n)/n` where
G_ij = k(y_j − y_i), Ψ(t) = (t−1)² on [0,2], 2t−3 beyond.

| n | eps_atom(n) (my min) | implied bound (3-pt form) |
|---|---|---|
| 3 | 1.48e-4 | 0.672513 |
| 4 | 1.09e-3 | 0.672595 |
| 5 | 4.77e-3 | 0.672913 |
| 7 | 3.95e-1 | 0.714898 |
| 9 | 8.11e-1 | 0.790067 |
| 11 | 1.12e+0 | 0.890110 |

The n=7 value (0.395/atom) is **four orders of magnitude above ainta's certified
ε₇ = 19/5000 ≈ 5.4e-4 per atom** — a red flag that demanded scrutiny (honesty rule:
a 4-order jump is a bug signal, not a discovery).

## Why it's wrong — the functional is pairwise-weighted + pressure, NOT raw tr Ψ

Reading ainta's `verify_seven.py` directly (the certified object):

```
F6(g1..g6) = (Σg_i)/3000  +  Σ_{span=1..6} COEFFICIENTS[span] × Σ_{7-span windows} k²(span-sum)
```

- **F6 is a pairwise k²-weighted functional** with specific `COEFFICIENTS[span]`
  weights (from the proof's window-averaging over 7-point blocks), PLUS
- **a pressure term (Σg)/3000** that penalizes large total span, PLUS
- the certified target is **F6 ≥ 19/5000 over ALL nonnegative gaps** (including
  coincident — the pressure term controls that).

`tr Ψ(G_n)/n` (my object) counts raw eigenvalue deviations of the Gram matrix.
These are mathematically different functionals. My minimization found clustered
configurations (maxgap ~0.7, span 4) where tr Ψ is huge — configurations that the
certified F6's pressure term and pairwise weights handle differently. **The explosive
ladder values are an artifact of minimizing the wrong object over the wrong domain.**

## The honest verdict

- The per-atom tr Ψ ladder **does NOT** certify a bound above 0.6731929 (or even
  above ainta's 0.6730085). It's the wrong functional.
- The REAL ladder is F6 → F9 → F11 (the pairwise-weighted + pressure functionals at
  larger block sizes) — exactly what trmdy did (0.6731376) and what the
  combined-stability+Bellman agent (eb5e0afc) is extending.
- **Methodological value:** this documents WHY "just make the blocks bigger in tr Ψ"
  fails — the certified object is the weighted pairwise functional, and the
  convergence question must be studied there, not in raw Gram-eigenvalue deviation.
- The n=3/n=4 values (1.48e-4, 1.09e-3) DO reproduce the correct scale of the
  certified 3-point floor (ε₄ ≥ 221/10⁶ = 2.21e-4 — my n=3 min 1.48e-4 is the
  unconstrained infimum below the certified bound, consistent with the transfer note's
  interior infimum 4.45e-4 vs certified 2.21e-4... note: my per-atom 1.48e-4 vs the
  note's per-atom 4.45e-4/3 ≈ 1.48e-4 — **exact match**! Good sanity: the 3-point
  functional DOES reduce to tr Ψ(G₃)/3.)

## Files

- research/ladder-convergence/ladder_floor_fast.py (my minimizer; n=3 reproduces
  the transfer-note infimum exactly)
- research/external-results/ainta-zeta-simple-zeros/src/zeta_simple_zeros/verify_seven.py
  (the certified F6 — read directly, the source of truth for the functional)

## Next

The convergence question belongs in the F6-functional family (weighted pairwise +
pressure at n = 7, 9, 11, ...) — this is the combined agent's lane (eb5e0afc).
Do not re-fund the raw tr Ψ ladder.
