# Zigzag stability across heights — Turán / (log ξ)″ scan — 2026-08-25

Author: builder subagent. Verdicts this scan builds on (read, not redone):
`turan-probe-2026-08-25.md` (TYPE_SEPARATES: off-line vs on-line displacement via the
off-critical sigma sign-zigzag of Re L_R at γ₁) and `speiser-probe-2026-08-25.md`
(N separates only for FE-consistent implants — bare single factor is inert).
This note answers: does that hold across the first 20 heights? does the β-threshold
depend on height? (Task C: re-verify FE-consistency single vs quadruple at γ₁₀.)

Tool: `research/scripts/zigzag_stability_scan.py` (dps=25, mpmath), runtime 7.8 s.
All numerics below: **CHECKED NUMERICALLY** (deterministic mpmath; closed-form L_R;
only structural claims are PROVEN).

## The exactness core (unchanged from the Turán probe)

`P(s) = (log ξ_planted)″ = base(s) + L_R(s)`,
`base(s) = (log ξ_true)″` (mp.diff dps=25; FE structure: Re even / Im antisymmetric
under σ ↔ 1−σ, i.e. `base(0.7+it0) = conj(base(0.3+it0))` — verified to 1e-12),
`L_R(s) = (log R)″ = −Σ_p 1/(s−p)² + Σ_m 1/(s−m)²` — EXACT closed form (no integration).
Fe-consistent plant (β): p = {β,1−β}±i·t₀, m = {½}±i·t₀ (moves the on-line zero).
On-line shift +0.3: p = {½}±i·(t₀+0.3), m = {½}±i·t₀.

**Removable singularity at s = ½+i·t₀** (the moved on-line zero): base and
+1/(s−m₀)² diverge but P_planted is finite. Computed by the zero-sum decomposition:
`P(s₀) = (log ξ_reg)″(s₀) − Σ_p 1/(s₀−p)²`, with `(log ξ_reg)″(s₀) = −1/s₀² − 1/(s₀−1)²
+ ¼ψ′(s₀/2) + (log ζ_reg)″(s₀)` and the exact `(log ζ_reg)″(s₀) =
ζ‴/(3ζ′) − (ζ″/(2ζ′))² + 1/D², D = s₀−s̄₀` at each zero. Validated vs
`method='quad'` to <1e-21 at γ₁ and γ₂₀, and by analytic continuity
(avg of P at s₀±1e-4 agrees to the O(ε²)≈2–4e-6 Taylor remainder).

Definition used: **zigzag(profile) = sign(Re P at σ=0.50) ≠ sign(Re P at σ=0.30)**
(the two off-critical ends are equal by FE evenness, so a profile is either
(−,−,−)/(+,+,+) constant or (−,+,−)/(+,−,+) − a true zigzag).

## Task A — P-sign at σ∈{0.30,0.50,0.70}, t₀=γ₁..γ₂₀

| h | t₀ | off-line β=0.9: P-triple | P-zigzag | L_R-zigzag | on-line +0.3: P-triple | P-zigzag | L_R-zigzag | sep |
|---|---|---|---|---|---|---|---|---|
| 1..20 | 14.13..77.14 | `---` (all 20) | N (all) | Y (all) | `+++` (all 20) | N (all) | N (all) | **Y (all 20)** |

P real triples (sampled): γ₁ FALSE [−27.71, −12.43, −27.71], LINE [3.03, 11.18, 3.03];
γ₁₀ FALSE [−27.24, −11.95, −27.24], LINE [3.50, 11.66, 3.50];
γ₂₀ FALSE [−26.93, −11.62, −26.93], LINE [3.81, 12.00, 3.81].
Middle values: `(log ξ_reg)″(½+iγ_k)` grows +0.07, +0.30, +0.55, +0.89 across
γ₁, γ₅, γ₁₀, γ₂₀ (positive, comfortably > −11); ends move −27.7→−26.9 / +3.0→+3.8
as t₀ grows (base −24.93→−24.14; L_R terms at the ends are height-independent).
L_R zigzag: off-line Y / on-line N at all 20 (structural, see below).
Type separation (opposite P-sign at ≥1 sampled σ): **20/20 heights**;
at every height all three σ have opposite signs (FALSE − vs LINE +).

**Verdict A: the statistic is fully stable across γ₁..γ₂₀ — 20/20 heights separate.**
Also sharpened: the *P*-profile itself is constant-sign for BOTH types at every height
(never a zigzag: the base, ≈ −25 at the ends / ≈ +0.07..0.9 at the middle, dominates),
so the separating content is the **type-opposite sign of P, not a per-type zigzag**;
the sign-zigzag lives in L_R (closed form) where it is 100% structural.

## Task B — β-sweep {0.6,0.7,0.8,0.9} at γ₁, γ₅, γ₁₀: β-threshold vs height

Re P at σ=0.30 (= σ=0.70 by FE evenness) for the off-line β-plant (base at σ=0.30: γ₁ −24.93,
γ₅ −24.71, γ₁₀ −24.46):

| height | β=0.6 | β=0.7 | β=0.8 | β=0.9 | flip? |
|---|---|---|---|---|---|
| γ₁ | −111.0 | −∞ (pltd pole@0.3) | −103.9 | −27.71 | NONE |
| γ₅ | −110.8 | −∞ | −103.7 | −27.49 | NONE |
| γ₁₀ | −110.6 | −∞ | −103.5 | −27.24 | NONE |

(β=0.7 puts the planted mirror zero 0.3+i·t₀ exactly on the σ=0.30 sample: P → −∞,
a true log-singularity, sign −.)

**Verdict B: the minimal β that flips the P-sign off-critical does not exist in
[0.5, 1] — and this is height-INDEPENDENT.** Two structural reasons (PROVEN, pure
near-field position arithmetic at dt=0, closed form):
1. Re L_R at the extreme σ is negative for every β∈(½,1) once the mirror zero is in
   the strip: the near terms are `−1/(σ−β)² − 1/(σ−(1−β))² + 1/(σ−½)²`, which at
   σ=0.30 is ≤ 0 for β∈[0.5,1] except β > β_c where it is positive but bounded by
   +11.77 (max at β→1). β_c (the L_R sign threshold at the extreme) = **0.9116**.
2. Even then P = base + L_R never flips: **max L_R +11.77 < |base| ≈ 24.9** — the
   implant can perturb but never reverse the sign of the total at the off-critical
   extremes, for any β, at any height (base at the extremes ranges −24.93..−24.14,
   always below −24 > 11.77).
Height dependence enters only through the far conjugate members, order 1.25e-3 (γ₁)
→ 1.01e-4 (γ₁₀) — 4–5 orders below the 25-scale near terms, so the β-threshold
(0.912) shifts by <1e-3 across heights. **No height dependence beyond noise.**

## Task C — FE-consistency rule at γ₁₀ (single-factor vs quadruple)

| implant (all at γ₁₀, sampled off-critical) | Re P @ σ=0.30 | Re P @ σ=0.70 | FE-even? | zigzag at ends |
|---|---|---|---|---|
| single factor, pure plant R=(s−p₀), p₀=0.9+it₀ | −27.24 | −49.46 | NO (asym) | N |
| single factor, displacement R=(s−p₀)/((s−m₀)(s−m̄₀)) | −2.24 (+22.2 L) | −24.46 (L≈0) | NO (asym) | N |
| quadruple pure plant (off4: 0.9/0.1±it₀) | −52.24 | −52.24 | YES | N |
| quadruple FE displacement (Task-A plant) | −27.24 | −27.24 | YES | N |

**Verdict C: single-factor inert = YES.** A single factor's L_R = −1/(s−p₀)² has
Re < 0 on the whole real axis — it can never produce the sigma sign-zigzag (Re L_R
≤ 0 everywhere), at γ₁₀ or any height. The FE-consistent plant produces the zigzag
in L_R (ends −, middle +∞: the removal pole at ½ supplies the +, the mirror pair the −
at the extremes) — absent for the single factor. The FE violation is visible only as
**value asymmetry** (Re P(0.30) ≠ Re P(0.70); e.g. −27.24 vs −49.46), mirroring the
displacement variant's −2.24 vs −24.46; it never reaches sign reversal. Consistent
with the speiser probe's off1-N=0 / off4-N=1 dichotomy: the FE-closed plant is the
only structure that carries type information.

## Verdict summary

- **A: 20/20 heights separate** (FALSE − vs LINE + at every sampled σ; stable across
  γ₁..γ₂₀). P-profile is constant-sign for both types at every height; the
  sign-zigzag is a property of L_R (closed form; FALSE Y, LINE N, exact at all heights).
- **B: minimal β that flips P-sign off-critical: NONE in [0.5,1]** (max |L_R| +11.8
  < |base| ≈ 24.9 at the extremes); the L_R sign threshold β_c = 0.912 at the extremes
  is **height-independent** (pure near-field arithmetic; height terms ≤ 1.3e-3).
- **C: single-factor inert: YES** (no zigzag possible; FE-consistent plant required),
  re-confirmed at γ₁₀.

## Candid caveats
- "Separates" here = opposite P-sign between the two implant types at the same σ, at
  every height; the per-type P-zigzag is N for both types everywhere (the base
  dominates P; the zigzag lives in the L_R perturbation).
- Methodology correction to `tools/turan_pointwise_probe.py`: its LINE group passed
  t_p=0.3 verbatim (planted at ½±i·0.3) while the intended convention "shift +0.3"
  plants at ½±i·(t₀+0.3). The dt=0 sigma-profile (basis of that probe's verdict) is
  identical under both (both far), so its TYPE_SEPARATES verdict stands; this scan
  uses the intended convention.
- β=0.7 row in Task B carries a planted pole exactly at the sample (P → −∞); sign
  assignment − is exact, magnitudes are not meaningful there.
- Labels: all table entries CHECKED NUMERICALLY (dps=25); the structure claims
  ("L_R zigzag for FE-consistent plants only", "base dominates the extremes",
  "β-threshold height-independent") are PROVEN by the closed-form near-field
  arithmetic at dt=0. Nothing beyond the finite-ratio displacement family is claimed.