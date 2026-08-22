# CANONICAL CONVENTIONS — tools/ (pinned 2026-08-22)

**Rule: every tool/script/agent-note touching F_B, kernels, or zero data MUST follow these
definitions. Any deviation = bug, not variant. (Root cause of the 2026-08-21 false counterexample
was an unpinned pair-set convention — see research/notes/cert-bug-2026-08-21.md.)**

## 1. F_B block inequality objective (the ONLY certified object)

Points y_0..y_6 with y_0 = 0 and y_k = g_1 + ... + g_k (g_i ≥ 0, six gaps, units: mean zero-spacing).

    F_B(g) = Σ_{i=1..6} p_i g_i  +  Σ_{i=1..6} q_i w(g_i)
           + Σ_{0≤i<j≤6} a_ij w(y_j − y_i)          ← **21 pairs, INCLUDING i=0 (distances from y_0=0)**

- a_ij = 2/(7−(j−i)) for ALL 21 pairs (i from 0!). 15-pair variants ("S1") are FORBIDDEN —
  they evaluate a different function and proved nothing about the certified one.
- Parameterization: p_i = λ·raw_i/1_920_000 (Σraw=6000 ⇒ Σp=λ/320); q_i = λ·q_raw_i (q scales by λ).
- Kernel: w(x) = (K(x)/K(0))², K(x) = ½[sinc((α−2πx)/2) + sinc((α+2πx)/2)], sinc(u)=sin(u)/u.
- Verifier cutoff: w-terms tabled for x ≤ target·3000; beyond that terms DROP (sound: w ≥ 0).

## 2. Bound chain

    bound(m) = (H(α) − τ)/(1 − φ_m(A)/m),  A = eps(m−6),  τ = (λ/320)(m−6)/m
    H(α) = 2 − 1/c,  c = I0²/(I2+J),  I0 = 2sin(α/2)/α,  I2 = ½ + sin α/(2α),
    J = −2·I2/α² + (sin(α/2)/α + 2cos(α/2)/α²)·I0
    φ_m(A) = A if A ≤ m/(m−1) else 2√((m−1)A/m) − 1 + A/m.   Maximize over integer m.

## 3. Sound certification standard

- ONLY `tools/verify_coboundary_floor.py` post-commit c6a8f5e (Gershgorin convexity certificate)
  output `verified: true` counts as PROVEN. Node-limit / terminal-cell = INCONCLUSIVE, never PASS.
- The pre-c6a8f5e tangent_lower (LDL on entrywise lower bounds of w″) is INVALID — its outputs
  are void regardless of target.
- Float surrogates (scipy/mpmath) may PROPOSE candidates only; they never certify.

## 4. Zeros data

- File `tools/data/zeros_rust_100k.txt`: header lines start with non-digit (`# rust-zeros v3...`)
  — parsers MUST skip them. Columns: γ_j (ordinates of zeros on the critical line), J=100000,
  γ_max = 74980.922970.
- Li λ_n engine variable: z = 1 − 1/ρ (NOT 1−1/(ρ−1)); plant uses FE quadruplet
  {ρ_p, ρ̄_p, 1−ρ_p, 1−ρ̄_p}; control fire n=5155 (β₀=0.85).

## 5. ζ′ left-strip certification (Speiser lane)

- Domain: σ∈[0.001, 0.49] (NOT 0.5 — ζ′ HAS zeros on σ=1/2 by Rolle; winding on a contour
  touching σ=0.5 is ill-posed and false-PASSes).
- Engine: Euler–Maclaurin Hurwitz zeta (N=60, M=10) with per-point certified bounds;
  argument-continuation winding with max arg-gap < 2.8 rad; DH control circle
  (0.42+85.70i, r=0.15) must wind 1 before any ζ band is trusted.
- Frontier as of 2026-08-22: zero-free t∈[10,12000] contiguous (commit 9a837c7).

## 6. Labels

PROVEN / CHECKED NUMERICALLY / CONJECTURED / ABANDONED / INCONCLUSIVE — as hooks/agents.md.
Missing binary or node-limit ⇒ INCONCLUSIVE, never VERIFIED.

## ⚠️ ZEROS DATA QUARANTINE (2026-08-22)
`tools/data/zeros_rust_100k.txt` is **UNTRUSTED above γ≈20100** (row ~21000): the RS-g0 scanner
progressively dropped zeros — drift vs mpmath zetazero reaches 27 units by row 58000 (audit
/tmp/thresh.log). Clean below γ≈20100 (diffs <7e-5).
Replacement being generated: `tools/data/zeros_verified_32k.txt` (mpmath zetazero, dps=25).
Until it lands: any computation consuming zeros MUST restrict to γ≤20100 from the old file or
use zetazero directly. Results that consumed corrupted rows (λ_n n≳? scan, UHDC t>20000
exclusions) are flagged for re-run. Do not delete the old file (provenance).
