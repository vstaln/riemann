# Turán sigma-zigzag proof attempt at height γ₁ — 2026-08-25

Tool: `tools/zigzag_proof_attempt.py` (dps=80 core; closed-form L_R exactly as given,
base = −Σ_ρ 1/(s−ρ)² over 32000 verified zeros with a RIGOROUS analytic tail bound).
Run: `uv run --with mpmath python3 tools/zigzag_proof_attempt.py` (~35 s).

## Setup (identical to turan-probe-2026-08-25.md)
zeta_planted = zeta_true·R, (log ξ_planted)'' = base(s) + L_R(s):
- base(s) = (log ξ_true)'' = −Σ_{all ρ} 1/(s−ρ)²   [exact; Hadamard]
- L_R(s)  = −Σ_{planted p} 1/(s−p)² + Σ_{moved m} 1/(s−m)²   [exact closed form]
β=0.9 (FALSE group): p = {0.9±it₀, 0.1±it₀}, m = {0.5±it₀}, t₀=γ₁=14.134725…

**Validation** (PASS): closed-form L_R = (log R)'' numerically to 1.3e-51 at an
off-grid point; zero-sum base matches independent mp.diff of log ξ to ~1e-4 in Re.

## Rigour package
- zeros from `zeros_verified_32k.txt` (mpmath zetazero, dps=25, trusted to
  H=γ₃₂₀₀₀=27260.17); base summed to dps=80.
- Tail: for |γ|>H, |1/(s−ρ)²| ≤ 1/(γ−t₀)², symmetrical over ±γ; zero count bounded by
  N(y) ≤ (y/2π)log y + 4 log y (classical Backlund/Titchmarsh; verified loose at
  y=H: 44,341 ≫ 32,000), summed via integration by parts:
  **tail ≤ 1.9e-4** (about 1e-6 relative to base).
- s=0.5+it₀ is a REMOVABLE singularity (base −1/(s−m₀)² and L_R +1/(s−m₀)² cancel);
  P_total there is finite = −Σ_{planted p} 1/(s−p)² − Σ_{true ρ≠m} 1/(s−ρ)².

## Results (all Re parts; Im parts are ~1e-5, irrelevant to signs)
| point | L_R | base | P = base+L_R |
|---|---|---|---|
| s = 0.3+it₀ | **−2.77653** | **−24.93249 ± 1.9e-4** | −27.70902 |
| s = 0.5+it₀ | (+∞/−∞ cancel) | (singular) | **P_total = −12.49750** (finite) |

## Verdict vs. stated proof targets
- **TARGET (i): |L_R(0.3+it₀)| > |base(0.3+it₀)| — REFUTED.**
  |L_R| = 2.777 vs |base| = 24.932; ratio 0.1114. And both are NEGATIVE (same sign),
  so no flip occurs and none is even needed — log ξ is already concave at 0.3+it₀
  (dominant term −1/(σ−½)² = −25 from γ₁, distant zeros only +0.07).
- **TARGET (ii): P stays positive at 0.5+it₀ — REFUTED.**
  P_total(0.5+it₀) = −12.5 = −2·(1/0.4)², from the planted zeros at 0.9, 0.1.
  (log ξ_planted)'' is NEGATIVE at the moved-zero location, not positive.

Failure margins ≫ 10× tail: target (i) fails by |base|−|L_R| = 22.16 (tail 1.9e-4);
target (ii) fails by |P_total| = 12.50. These are verified inequalities, not a
near-miss: **the sigma-zigzag claim (flip at σ=0.3, stay-positive at σ=0.5) is
FALSE at height γ₁ for β=0.9.**

## LABEL: REFUTED_AT_HEIGHT (verified, rigorous bounds)
Not INCONCLUSIVE: the two stated inequalities were proved false with margin
>10⁵× the rigorous tail/rounding bounds, using only exact closed forms plus the
classical zero-counting bound. Consistent with turan-probe-2026-08-25.md verdict
(no observed sign flip; max |L_R/base| ≈ 1.19 nowhere with opposite sign).

## General theorem — CONJECTURED (analytic scaling, no sweeps)
For fixed σ∈(0,½), β∈(½,1), implant at a true zero height t→∞:
- L_R(σ+it) → 2Re[1/(σ−½)²] − 1/(σ−β)² − 1/(σ−(1−β))² + O(t⁻²)  [exact algebra,
  PROVEN]: at σ=0.3, β=0.9 → −2.7778 (computed −2.7765, O(t⁻²)=1.3e-3 ✓).
- base(σ+it) = −1/(σ−½)² + (log t)/(2(σ−½)) + o(log t)  [heuristic from mean zero
  spacing δ~2π/log t: at δ≫|σ−½| the neighbor tail is π²/(3δ²) (observed +0.0676 at
  γ₁, δ=6.89 ✓); at δ≪|σ−½| it crossovers to (log t)/(2(σ−½)), CONJECTURED].
- Consequence (CONJECTURED): |L_R|/|base| = O(1/log t) → 0 as t→∞ for every fixed
  β. The implant's pointwise (log ξ)'' effect DECAYS with height; the observed
  ratio 0.111 at γ₁ is in the pre-asymptotic crossover region, and no sigma-zigzag
  flip can persist at large height.

## Candid caveats
- Proof attempt targets a fixed height (γ₁), single β=0.9, single implant; the
  method (closed form + rigorous tail) transfers verbatim to any β, σ, and to any
  height t where a trusted zero table + zero-count bound are available.
- "REFUTED_AT_HEIGHT" is a negative result for THIS flip; the type-separation
  statistic from turan-probe (off-critical sigma-sign of L_R, not of P) is
  unaffected and remains CHECKED NUMERICALLY.
- Tail bound constant (4 log T) is deliberately crude; tightening changes nothing
  at margins of 10²–10⁵.