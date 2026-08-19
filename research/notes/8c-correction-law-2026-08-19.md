# 8C Báez–Duarte finite-N correction law — MEASURED (2026-08-19)

**Lever:** 8C Báez-Duarte sharp-rate structure, frontier lane #2(b) — the honest open
question: is the finite-N correction in δ(N) = d_N²·log N of order O(√log N), O(1/log N),
or O(1)?
**Status:** RUN. **Label:** CHECKED NUMERICALLY (consistency-level, no RH content).
**Tool:** `/tmp/correction_law.py` (values from certified wave8c MPFR ladder).

## Data (certified d_N, k=1..N basis; * = rough interpolant, excluded from fits)

| N | d_N | d_N·√log N | δ(N)=d_N²·log N |
|---|-----|-----------|-----------------|
| 10 | 0.151041 | 0.2292 | 0.0525 |
| 20 | 0.126823 | 0.2195 | 0.0482 |
| 30 | 0.119192 | 0.2198 | 0.0483 |
| 50 | 0.107937 | 0.2135 | 0.0456 |
| 100 | 0.100139 | 0.2149 | 0.0462 |
| 600 | 0.083710 | 0.2117 | 0.0448 |
| 2000 | 0.077821 | 0.2146 | 0.0460 |
| 5000 | 0.072526 | 0.2117 | 0.0448 |

## Fits (certified points only)

```
delta = c + b*(1/log N)     : c=0.0418 b=+0.0215  mse=9.9e-07
delta = c + b*(1/sqrt logN) : c=0.0372 b=+0.0205  mse=1.36e-06
delta = c + b*(loglogN/logN): c=0.0350 b=+0.0375  mse=3.25e-06
```

## Verdict
- δ(N) is **essentially flat**: certified points lie in 0.0448–0.0483 except the small
  N=10 bump (0.0525). d_N·√(log N) stays in the 0.211–0.230 band across 3 decades.
- The finite-N correction is a **gentle O(1/log N)-type bend**, not an O(√log N) and not
  a clean O(1/√log N) sub-diffusive law. The best residual fit (1/log N) gives asymptotic
  δ∞ ≈ 0.042, slightly below the large-N measured 0.045 — the drift is real but small and
  does not resolve cleanly between 1/log N and 1/√log N at these N. Consistent with (and
  numerically reinforcing) the wave-23 refutation of agy's L2 (C₀∈0.22-0.28, Δ flat
  0.048-0.052).
- **Sharp-rate implication:** d_N ≈ c/√(log N) with c ≈ √0.045 ≈ 0.212 — the flat-law
  constant, reproduced. No sub-diffusive tail detected. This is a consistency read on the
  Báez-Duarte sharp rate, NOT RH evidence and not a proof that d_N ≤ C/log N.

## RH-false control (stated, not run)
Planted-zero Beurling world must give a DIFFERENT correction law (e.g. δ_N → δ∞ ≠ 0, or
a divergent law) since d_N saturates there. The frontier demands this before any claim;
the real-world measurement above stands alone as CHECKED NUMERICALLY.
