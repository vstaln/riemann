# Attack: the Nevanlinna reframe of P1 (0.6725 → 0.6818) — is the marks/integrality constraint the missing input?

**Agent:** EXECUTIONER (epistemology + constraint-hardness-testing + other-perspectives) — vector **P8.1**
**Date:** Round 1
**Sources:** `research/notes/idea-generator-physics.md` (P8.1, TOP-10 #3), `attack-kernel.md` §1–2,
`attack-ceiling.md` §1, `attack-multiplicity.md`, `research/lean-zeta-23/Zeta23/PairCeiling/{Defs,NearCUE,Bridge,CeilingLaw256,LawN256}.lean`,
`research/papers/claude-riemann-paper.txt` (§7.5(b),(e), Prop 4.4).
**Compute:** `tools/nevanlinna_check.py` (exact rationals + mpmath; `uv run --with mpmath python`).
Labels: **PROVEN** = Lean or direct derivation from the cited sources; **CHECKED NUMERICALLY** = computed here;
**REASONABLY BELIEVED** = consistent with the sources but not re-derivable from the repo alone;
**UNRESOLVED** = open question flagged honestly.

---

## 0. Verdict up front (honest)

**NEGATIVE — the Nevanlinna reframe does not yield the missing constraint.** The marks/integrality
constraint is real and *does* restrict the Nevanlinna parameter function: within the (m₁, m₂) = (1, 4/3)
moment class it collapses the whole Nevanlinna family to the single integer-grid measure
(2/3 simple + 1/6 double, 1/6 empty) — reproducing the **flat-window** constant 2/3. But it does **not**
exclude the 0.6818-realizing (near-CUE) measures, because the near-CUE law **is itself an integer-marked
measure** and satisfies the integrality identity `m₂ = 2 − p₁` with (p₁, m₂) = (0.68183, 1.31817).
The 0.6818 law lies **outside** the (1, 4/3) moment class entirely (its second moment is 1.3182 ≠ 4/3),
and it is not required to match ζ's second moment — it only matches the bandwidth-one inputs (mean density 1,
F ≡ 1 on [0,1], integer marks ≤ 2) that the certificate is obliged to read.

The reframe does deliver a precise **diagnosis** (see §5): the whole in-class window
[0.6725, 0.6818] = [2 − 1.3275, 2 − 1.3182] is a **second-moment gap**, and integrality is exactly what
*permits* the upper endpoint (p₁ > 2/3 requires m₂ < 4/3). Closing the gap needs a provable lower bound
m₂ ≥ 1.3275 on near-CUE integer-marked configurations — i.e. the beyond-bandwidth-1 arithmetic input that
`attack-ceiling.md` §4 already lists as FUND. The reframe cross-confirms the ceiling analysis from an
independent direction; it does not reopen it.

---

## 1. The moment problem (setup, and a phantom-constraint finding)

**The certificate's constraints (verified from `attack-multiplicity.md` §1, PROVEN).** In the normalized
units of the rank–trace argument, an isolated on-line zero contributes eigenvalue ≈ m_ρ, and
`tr Â = (1+o(1))N`, `‖Â‖²_F = (C+o(1))N` with C = 1/λ + λ/3; at λ = 1, C = 4/3. The extremal world
(2N/3 simple + N/6 doubles) has tr/N = 1 and ‖·‖²/N = 4/3 — "the same two trace moments as ζ itself".
So the certificate's moment inputs are

    m₁ := tr Â / N = 1 ,      m₂ := ‖Â‖²_F / N = 4/3 .

**Phantom constraint: "measure on [0,1]".** For any measure on [0,1], x² ≤ x pointwise, so m₂ ≤ m₁;
the pair (1, 4/3) has m₂ > m₁. Hence **(1, 4/3) is INFEASIBLE on [0,1]** — the problem lives on the
multiplicity space, marks ⊆ [1, 2] ⊂ [0, ∞) (Stieltjes problem). The task's "measure on [0,1]" is an
**Assumed** constraint, refuted by the trivial inequality; the real constraint set is the mark space.
(Constraint-hardness: Assumed → refuted; no consequence lost.)

**Two normalizations (must be kept apart, PROVEN/CHECKED).** Counting *zeros* gives the probability
measure μ = (2/3)δ₁ + (1/3)δ₂ with moments (m₁, m₂, m₃) = (4/3, 2, 8/3). Counting *distinct points*
normalized by N gives the submeasure ν = (2/3)δ₁ + (1/6)δ₂ (total mass 5/6, 1/6 empty positions) with
ordinary moments

    ∫dν = 5/6 ,  ∫x dν = 1 ,  ∫x² dν = 4/3 ,  ∫x³ dν = 2 ,  ∫x⁴ dν = 10/3 .   (CHECKED NUMERICALLY)

The certificate's inputs (m₁, m₂) = (1, 4/3) match the submeasure normalization, and the extremal world
realizes them. **Note (UNRESOLVED):** `idea-generator-physics.md` P8.1 states the sequence
(1, 4/3, 2, **13/4**) as "GUE values"; the extremal-world submeasure gives m₄ = **10/3 ≠ 13/4** (CHECKED).
The sequence (1, 4/3, 2, 13/4) is a valid Stieltjes sequence (all Hankel determinants positive: H₁ = 1/3,
H₂ = 5/108, Stieltjes minors 2/9, 1/3 — CHECKED NUMERICALLY), so its provenance is some other
normalization/source, not the extremal world. Does not affect the two-moment analysis; flagged for the
planner.

---

## 2. The two principal representations (canonical measures) of (1, 4/3)

For the truncated Stieltjes problem (m₀, m₁, m₂) = (1, 1, 4/3), the two natural canonical measures
(2-point, total mass 1) are:

    P⁻ = ½·δ_{1 − 1/√3} + ½·δ_{1 + 1/√3}      atoms 0.42264973…, 1.57735027…   (masses ½, ½)
    P⁺ = ¼·δ₀ + ¾·δ_{4/3}                    atoms 0, 4/3                    (masses ¼, ¾)

Moments: both have (m₀, m₁, m₂) = (1, 1, 4/3) (exact algebra, CHECKED NUMERICALLY);
m₃(P⁻) = 2, m₃(P⁺) = 16/9 (CHECKED NUMERICALLY). **Neither has atoms on the allowed grid {1, 2}** —
the first concrete finding of this probe: the free problem's canonical measures are off-grid.

**Nevanlinna parametrization (verified, CHECKED NUMERICALLY).** All solutions of the truncated problem
are given by the Stieltjes-transform formula

    w(z) = ∫ dσ/(z−x) = ( (3z−1)·φ(z) + (z−1) ) / ( (3z²−4z)·φ(z) + (z² − 2z + 2/3) ),

φ ranging over Nevanlinna functions (φ ≡ ∞ allowed). Verified: φ ≡ 0 ↦ w = w(P⁻), φ ≡ ∞ ↦ w = w(P⁺);
for φ ∈ {1, −2, z, z/(z²+1), 10⁴⁰z} the Laurent coefficients give (m₀, m₁, m₂) = (1, 1, 4/3) to 10⁻²⁰
and Im w < 0 on the upper half-plane (positive measures) — every tested φ yields a measure with exactly
the two certificate moments.

**Honest caveat (epistemology):** for a 2-moment problem the solution set is large (all measures with
mean 1, variance 1/3) and has a continuum of 2-point extreme points (e.g. atoms {0.5918, 1.4082} with
masses (2/3, 1/3) also solve it). P⁻, P⁺ are the natural canonical pair (symmetric-interior; boundary-at-0)
in the Krein–Nudelman sense. **The verdict below does not depend on this convention.**

---

## 3. The marks/integrality constraint as a bound on the parameter function

**The law's structure (documented in `LawN256.lean`):** a finitely supported 256-periodic law of marked
configurations, exact rational weights w_c ≥ 0 summing to 1, positions x_{c,i} ∈ [0,256),
marks m_{c,i} ∈ {1,2} with Σ_i m_{c,i} = 256 (per configuration), simple-point fraction
p₀ = 10909258999421303588095230195816054408197/16000000000000000000000000000000000000000 = **0.6818286874638…**,
near-CUE rows |256·S(j) − j| ≤ 3·10⁻⁴⁰ (0 < j < 256), |D(1)| ≤ 0.82395317.

**Integrality identity (PROVEN, trivial algebra).** For any configuration with marks ∈ {1,2} and
Σ marks = N: writing s = # simple, d = # double, s + 2d = N, so

    p₁ = s/N ,   m₂ = (s + 4d)/N = (2N − s)/N = 2 − p₁ .

The pair (p₁, m₂) of any such configuration lies on the line m₂ = 2 − p₁. In the Nevanlinna parametrization
this is a 1-dimensional constraint on the *outputs* of the parameter function (the simple-fraction and
second-moment functionals are locked together), and at the level of the measure it restricts the atoms to
the integer grid.

**Within the (1, 4/3) class the integrality bound collapses the family (PROVEN, CHECKED).** With
marks ∈ {1,2} and m₂ = 4/3, the identity forces p₁ = 2/3, and the unique solution is the submeasure
ν = (2/3)δ₁ + (1/6)δ₂ (1/6 empty) — **exactly the certificate's extremal world**. If marks ∈ {1,2,3} are
allowed, a 1-parameter family appears: p₁ = 2/3 + 3t ∈ [2/3, 5/6] (t ∈ [0, 1/18]; endpoints
(2/3, 1/6, 0) and (5/6, 0, 1/18)); with marks unbounded, p₁ → 1 (mass at huge marks costs arbitrarily
little second moment). So the integrality constraint is **real and strong** — but its output inside the
(1, 4/3) class with marks ≤ 2 is exactly p₁ = 2/3, the flat-window constant. It does not reach 0.6818.

**The 0.6818 law satisfies the identity (CHECKED NUMERICALLY).** The law is itself an integer-marked
configuration (marks ∈ {1,2}, Σ marks = 256); its expected mark distribution per grid position is
simple 0.68183, double 0.15909, empty 0.15909, and

    m₂(law) = 2 − p₁(law) = 2 − 0.6818286874638 = 1.3181713125362 ≠ 4/3 ,
    m₃(law) = p₁ + 8·(1−p₁)/2 = 1.9545… ,  m₄(law) = 3.2272… .

Hence **the integrality bound does NOT exclude the 0.6818-realizing measures**: the law satisfies the
bound (it is integer-marked). The only constraint that excludes it from the (1, 4/3) class is m₂ = 4/3 —
ζ's trace datum, which the law is not required to match: the ceiling's admissibility is the bandwidth-one
form factor + density + integer marks, and m₂ is not among them (NearCUE constrains only rows 0 < j < N;
the law's D(1) bound is independent of its second moment).

---

## 4. Does the bound explain the gap 0.6725 → 0.6818? **NO — it is a second-moment gap.**

The certificate's certified value is v = 2 − C with C the second moment of ζ's windowed operator
(`attack-multiplicity` §1, PROVEN):

| configuration / operator | C = m₂ | certified bound s₁/N ≥ 2 − C |
|---|---|---|
| ζ, flat window | 4/3 = 1.33333 | 2/3 = 0.66667 |
| ζ, optimal window (cosine, C = 1/c₁* = 1/2 + (1/√2)cot(1/√2)) | **1.3274992963206** | **0.6725007036794** |
| near-CUE 256-law (LP optimum) | **1.3181713125362** | 0.6818286874638 = p₀ (saturates) |

(All CHECKED NUMERICALLY; window values from `attack-kernel.md` §2, PROVEN.)

- Prop 4.4(ii) (PROVEN) is the universal bound s₁ ≥ 4·tr − 2N − ‖·‖², i.e. s₁/N ≥ 2 − m₂ for m₁ = 1.
  Every marks ∈ {1,2} configuration saturates this bound **identically** (it is the same identity as §3:
  RHS = 2N − Σm² = N·p₁ = s₁), so "the law saturates it" is not special to the law. The ceiling-specific
  content, in moment language, is that the law *achieves the worst-case value* over the admissible class:
  it is the LP optimum of max p₁ (= min m₂) subject to near-CUE + marks ∈ {1,2} + Σ marks = N, with
  p₁ = 0.68183 — the certificate therefore has zero slack against it, exactly the ceiling theorem.
- The gap is 0.67250 = 2 − 1.32750 vs 0.68183 = 2 − 1.31817, i.e. Δm₂ = 0.00933 between ζ's
  window-optimal second moment and the law's. Integrality ties p₁ to m₂ (identity §3) but permits both
  endpoints: p₁ = 2/3 ⟺ m₂ = 4/3 and p₁ = 0.6818 ⟺ m₂ = 1.3182 are *both* integer-marked.
- Closing the gap would require ζ's effective m₂ ≤ 1.3182. This is **PROVEN impossible within the window
  class**: the cosine is the global minimizer of the Rayleigh quotient (Euler–Lagrange + I+T ≻ 0,
  `attack-kernel.md` §2; CCLM17 Cor. 14), and 1/c₁* = 1.3275 > 1.3182. The alternative — a third input the
  law violates — is not integrality (the law is integer-marked). A third-moment lower bound m₃ ≥ 2 *would*
  separate the law (m₃(law) = 1.9545 < 2 = m₃(extremal world), CHECKED NUMERICALLY), but m₃ ≥ 2 is not
  provable: the paper §7.5(e) — tr G̃³ is available only in the Rudnick–Sarnak range kλ < 2 (λ < 2/3), and
  "an odd moment does not lower Λ₁(0)". So the third moment cannot price the law either.

---

## 5. What the reframe *does* give (diagnostic value; not nothing)

1. **The gap is provably a second-moment gap.** The entire in-class window [0.6725, 0.6818] =
   [2 − 1.3275, 2 − 1.3182] is the interval between ζ's best achievable effective m₂ and the worst-case
   law's m₂. The "missing constraint" is now precise: a *provable lower bound m₂ ≥ 1.3275 on near-CUE
   integer-marked configurations*, i.e. a constraint the 256-law violates. No such constraint is known; it
   is exactly the beyond-bandwidth-1 arithmetic input `attack-ceiling.md` §4 classifies as FUND (Hard wall).
2. **The marks/integrality mechanism is ruled out** as an explanation of the gap: the witness law is
   integer-marked, so any "integrality closes the gap" program is dead on arrival. This is a real epistemic
   gain — the reframe converts a plausible-sounding candidate constraint into a documented negative.
3. **Cross-validation:** the moment picture reproduces, from an independent direction, the ceiling
   (v ≤ p₀), the tightness (law saturates Prop 4.4(ii)), and the wall (§7.5(e): no third-moment input).
   Three notes now agree on the same structural conclusion.

---

## 6. Honest labels and epistemic status

| Claim | Status |
|---|---|
| Certificate inputs (m₁, m₂) = (1, 4/3); extremal world realizes them | PROVEN (attack-multiplicity; Lean) |
| (1, 4/3) infeasible on [0,1] (m₂ ≤ m₁ there) | PROVEN (trivial algebra) |
| P⁻, P⁺ explicit (masses, moments (1,1,4/3); m₃ = 2, 16/9) | PROVEN (exact algebra) / CHECKED NUMERICALLY |
| Nevanlinna parametrization formula; φ = 0 ↦ P⁻, φ = ∞ ↦ P⁺; all tested φ → moments (1,1,4/3), Im w < 0 | CHECKED NUMERICALLY (to 10⁻²⁰) |
| Grid-constrained (1,4/3) has unique solution (2/3, 1/6, 1/6); moments (1, 4/3, 2, 10/3) | PROVEN / CHECKED NUMERICALLY |
| Integrality identity m₂ = 2 − p₁ for marks ∈ {1,2}, Σm = N | PROVEN (trivial algebra) |
| m₂(law) = 2 − p₀ = 1.3181713125362; law's mark mix (0.68183, 0.15909, 0.15909) | CHECKED NUMERICALLY from the documented marks structure (REASONABLY BELIEVED: uses p₀ = E[s]/N, the simple-*zero* fraction, per the certificate semantics; the certificate file is not in the repo) |
| Law satisfies integrality ⟹ bound does not exclude it; gap = Δm₂ = 0.0093 | PROVEN from the above |
| C_min(ζ) = 1/c₁* = 1.3275 > m₂(law); window optimum global | PROVEN (attack-kernel §2; CCLM17) |
| m₃ ≥ 2 would exclude the law (1.9545 < 2) but is unprovable (§7.5(e)) | CHECKED NUMERICALLY / PROVEN-unprovable-as-input |
| P8.1's m₄ = 13/4 ≠ extremal-world m₄ = 10/3 | CHECKED NUMERICALLY — UNRESOLVED provenance |

**Weakest link (epistemology: justification chain):** the one externally-verifiable link I could not
re-derive is the law's exact weights/positions (certificate `cert_N256_blk_b128m.json` is absent from the
repo; only its sha256 is recorded). My use of the law reduces to its *documented* marks structure
(∈ {1,2}, Σ = 256) and its simple-point fraction p₀ — both stated in `LawN256.lean` — so the identity
m₂ = 2 − p₀ and its consequences are robust to the missing file; the file would only change the law's
*positions*, which do not enter my argument. Flagged, not hidden.

---

## 7. Constraint hardness (s4h-constraint-hardness-testing, applied)

| Constraint as stated | Source | Consequence if violated | Precedent | Classification |
|---|---|---|---|---|
| "measure on [0,1]" with (1, 4/3) | task phrasing | none (pair is infeasible there; refuted by x² ≤ x) | n/a | **Assumed → refuted (phantom)** |
| marks ∈ {1,2}, Σ marks = N (integrality) | ceiling law, Lean `LawN256` | configurations become non-integral-multiplicity, outside the certificate's world | law and extremal world both satisfy it | **Hard (real, and already priced)** |
| "integrality closes 0.6725 → 0.6818" | P8.1 hypothesis | the witness law is integer-marked — no exclusion | refuted here | **Assumed → refuted** |
| m₂ ≥ 1.3275 over near-CUE configs (what would close the gap) | none — this is the missing input | would crush the ceiling | no proven instance; equivalent to beyond-bandwidth-1 arithmetic | **Assumed (no proof); Hard wall per attack-ceiling** |

---

## 8. Other perspectives (OPS — adversarial voices)

- **The VALIDATOR** ("your m₂(law) = 2 − p₀ assumes p₀ counts simple *zeros*"): answered in §6 — the
  certificate validity condition `c₀ + Σ s_j r(j/N) ≤ p` uses p = s₁/N (simple-zero fraction; attack-ceiling
  §1), so p₀ is the simple-zero fraction; the law's mark-mix and m₂ follow. The missing certificate file
  changes only positions, not marks; the argument is invariant to it.
- **The PLANNER** ("we wanted the missing constraint"): the reframe is negative but *rules out a mechanism*.
  It converts "maybe the marks/integrality bookkeeping is the missing input" (a live P1 question before
  this probe) into "no — the witness satisfies it; the gap is a second-moment gap". That is the correct
  epistemic move: kill the cheap hypothesis, keep the expensive one (beyond-bandwidth-1 arithmetic) funded.
- **The PAPER (§7.5(b),(e))**: in agreement — higher moments beyond the second add nothing to the
  n₊-bound (odd moments don't lower Λ₁(0)); Prop 4.4 uses only the first two; and the extremal world
  (2/3 + 1/6) "realises tr = N, ‖·‖² = 4/3 N" — the same object this probe computes as the unique
  integer-grid solution of (1, 4/3).

---

## 9. Bottom line

- **The missing constraint for the in-class gap is NOT a bound on the Nevanlinna parameter function of
  the (1, 4/3) moment problem.** Integrality restricts that function to the single grid measure
  (2/3 simple, 1/6 double) — the flat-window constant 2/3 — and the 0.6818-realizing near-CUE law lives
  **outside** the (1, 4/3) class, at m₂ = 1.3182 ≠ 4/3. Integrality is satisfied by the law; it cannot
  exclude it.
- **The gap 0.6725 → 0.6818 is a second-moment gap**: [2 − 1.3275, 2 − 1.3182]. The law is the exact
  worst case (LP-minimal m₂ = LP-maximal p₁ over near-CUE integer-marked configurations) and saturates
  Prop 4.4(ii); ζ's window-optimal effective m₂ = 1.3275 is provably above the law's 1.3182.
- **Verdict: NEGATIVE as a constraint-discovery reframe; POSITIVE as a diagnosis.** P8.1's two
  principal representations are computed (P⁻, P⁺, plus the integer-grid solution); the parameter-function
  bound from integrality is derived and checked; it does not exclude the 0.6818 measures; the gap is
  localized, quantified (Δm₂ = 0.0093), and identified with the beyond-bandwidth-1 input
  (`attack-ceiling.md` §4 FUND). The two-moment + integrality class cannot certify more than 0.6818, and
  ζ's own data cannot reach it; the window [0.6725, 0.6818] is provably unclosable inside this class.
- **Recommendation:** close P8.1 as a documented negative with a sharpened diagnostic; do not re-fund the
  marks/integrality route; the live levers remain the beyond-bandwidth-1 arithmetic input (conjectural),
  the third-moment input (provably unavailable in the Rudnick–Sarnak range), and the adversarial
  re-check of EnclOK (the ceiling's single non-Lean link, `attack-ceiling.md` §4). Two cheap loose ends:
  resolve the m₄ = 13/4 provenance, and re-derive the 256-law from the certificate file when available
  (positions only; does not affect this verdict).

---

*Persistence note: this is a documented negative result, not a stop. The search for the 0.6725 → 0.6818
gap's missing input continues to be exactly the beyond-bandwidth-1 problem; P8.1 is retired as a mechanism,
not as a question.*
