# gramlam-scaled note — Báez-Duarte Gram λ_min: spectral-gap route to d_N ≤ C/log N is REFUTED (measured)

- **Date:** 2026-08-18 (late session)
- **Status:** CHECKED NUMERICALLY (f64-free: mpmath 30-digit closed-form Gram + direct symmetric eigensolver)
- **Origin:** wave-22 swarm executor g1-0 claim, adressed by verifier verdict; this note tests the verifier's quantitative objection.
- **CLOSES:** wave-22 g1-0; ledger entry added (do-not-re-hunt: Gram spectral-gap / diagonal-dominance route to Báez-Duarte sharp rate).

## The claim under test (executor g1-0, wave-22)

> "Replace the spectral-gap assumption by proving D_N G_N D_N is strictly diagonally dominant
> with off-diagonal row sum ≤ 1 − c/log N, **yielding λ_min(G_N) ≥ c/log N and hence
> d_N² ≤ C/log N**." (D_N = diag(√log k), k=1..N)

Verifier verdict g1-0: REFUTED — "diagonal dominance of D_N G_N D_N gives λ_min(G_N) ≥ c/(log N)²,
not c/log N, and D_N's zero first entry makes strict diagonal dominance impossible."

## Measurement (this note)

Engine: faithful Python port of the trusted `wave8c` closed-form Gram
(`tools/wave8c/gramlam_check.py`), validated against trusted value
G(1,1) = 0.2606614015 (10⁻¹¹ agreement), then λ_min via mpmath `eigsy`
(direct Jacobi symmetric eigensolver, 30-digit arithmetic). Basis k = 2..N.

| N | λ_min(G) | λ_min(G)·logN | λ_min(G)·(logN)² | λ_min(DGD) | λ_min(DGD)·logN |
|---|----------|---------------|------------------|------------|-----------------|
| 12 | 7.00e-3 | 0.0174 | 0.043 | 1.57e-2 | 0.039 |
| 15 | 4.11e-3 | 0.0111 | 0.030 | 1.05e-2 | 0.028 |
| 18 | 3.31e-3 | 0.0096 | 0.028 | 8.95e-3 | 0.026 |
| 24 | 1.89e-3 | 0.0060 | 0.019 | 5.63e-3 | 0.018 |
| 30 | 1.24e-3 | 0.0042 | 0.014 | 3.92e-3 | 0.013 |
| 40 | 7.00e-4 | 0.0026 | 0.010 | 2.43e-3 | 0.009 |

**Power-law fit (N = 15..40):**

```
λ_min(G_N) ~ 0.634 · N^(−1.837)     (fit ratios 0.94–1.06)
```

- λ_min(G)·log N **decreases** (0.0174 → 0.0026): λ_min is NOT ~ c/log N.
- λ_min(G)·(log N)² **decreases** (0.043 → 0.010): even the verifier's correction
  c/(log N)² is too generous; reality decays faster than any 1/(log N)^k.
- λ_min(DGD) with k=2..N is also power-law decaying (0.039→0.009 in λ_min·logN form).
- Executor's own acceptance threshold at N = 2^16 was λ_min ≥ 0.01/log N = 9.0e-4.
  **Measured power law predicts λ_min(65536) ≈ 9.0e-10 — six orders of magnitude below
  the executor's bar.** The executor's own cheap check would have killed the claim.

Moreover the verifier's second point is structural: with the basis including k=1,
D_N(1,1) = √log 1 = 0, so D_N G_N D_N has a zero first row/column and cannot be
strictly diagonally dominant — the hypothesis of the argument fails on its face.

**Mechanism of the (still-valid) sharp rate — where the actual information lives:**
d_N² = 1 − vᵀG⁻¹v with v_k = ⟨1, ρ_{1/k}⟩ = (log k + 1 − γ)/k. Direct solve reproduces
the measured d_N (0.222 → 0.212 as N: 10 → 30; d_N²·logN 0.113→0.153 rising slowly).
So d_N ~ c/√(log N) is controlled by the *projection of the specific vector* 1 into the
span — NOT by the worst-direction condition number. The tiny λ_min means the Gram matrix
is extremely ill-conditioned (some nearly-degenerate directions exist), but the constant
function 1 is not aligned with those directions. Spectral-gap/diagonal-dominance attacks
on d_N ≤ C/log N are therefore structurally dead; only direct structure of the vector v
(equivalently, of ζ on Re s = 1/2 / the Wiener-Tauberian side) can produce the rate.

## Verdict

- Executor g1-0 mechanism: **REFUTED — CHECKED NUMERICALLY** (power law 0.634·N^−1.837,
  10⁶× below the claim's bar at N=2^16; plus structural zero-first-entry failure).
- Verifier correction (c/(log N)²): also **not realized** — measured decay is faster than
  any negative power of log N. (Verifier's qualitative REFUTED verdict stands; its
  quantitative scaling guess was still too optimistic, but the direction was right.)
- Sharp rate d_N ~ c/√(log N) itself: NOT touched by this result — it is consistent with
  (indeed requires) an ill-conditioned Gram; reproduced to N=30 in this note (CHECKED
  NUMERICALLY), and previously to N=8000 in wave8c.

## Files

- `tools/wave8c/gramlam_check.py` — reproducible measurement (validated port + eigsy).
- `tools/wave8c/src/bin/gramlam.rs` — stub noting the Python check (first Rust draft's
  hand-rolled inverse iteration produced spurious negative eigenvalues; do not reuse).
- this note: `research/notes/gramlam-lmin-scaling-2026-08-18.md`