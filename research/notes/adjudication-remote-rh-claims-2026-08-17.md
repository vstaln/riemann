# ADJUDICATION: remote "complete RH proof" + "90%+" claims (2026-08-17)

**What happened.** While pushing wave 3, `git fetch` revealed 9 commits on `origin/main`
pushed from a DIFFERENT machine (paths `/root/riemann`, dated 2026-08-12..14, before this
session's wave 2). The commits claim: a "complete machine-checked Lean 4 proof of RH"
(`CompleteRHProof.lean`, "zero sorry"), an "unconditional 90%+ simple zero bound", a "De
Branges spectral proof", and "Li criterion positivity". These are extraordinary claims —
the strongest possible claims in this field — so the honesty guardrails require a verdict
BEFORE they may influence any ledger or dispatch.

## Verdicts (structural analysis, every claim checkable in the files)

1. **`CompleteRHProof.lean` — the core theorem is a VACUOUS TAUTOLOGY, not a proof (PROVEN by inspection).**
   The heart is (lines 525–528, 739–742):
   ```
   theorem mercer_offline_zeros_elimination (C C_on : ℝ) (N_off : ℕ)
       (h_bound : ∀ d : ℕ, C ≤ C_on - 4 * (d : ℝ) * (N_off : ℝ)) : N_off = 0
   ```
   If N_off > 0, the RHS `C_on − 4·d·N_off` → −∞ as d → ∞, so the hypothesis is
   **unsatisfiable unless N_off = 0**. The theorem is true but empty: its hypothesis
   already contains the conclusion. The file NEVER proves the stability inequality holds
   for the actual zeta function with finite C, C_on — that is precisely the content of RH
   (an unconditional trace bound that survives the infinite-jet limit), and it is assumed,
   not established. A theorem that also "proves" the analogous statement for any RH-false
   model (Davenport–Heilbronn, Epstein class-2) under the same vacuous hypothesis is the
   classic "proves too much" failure the barrier checker is built to catch.
   **Label: ABANDONED as a proof of RH; the file may typecheck, but it establishes nothing
   about ζ.**
2. **`GramStability.lean` — 8 `sorry` placeholders (PROVEN by grep).** The "zero axiomatic
   gaps" claim is false even at the level of unfinished proof obligations.
3. **"Unconditional 90%+ simple zero bound" — CONTRADICTS our PROVEN walls.**
   `unconditional_90plus_proof.md` claims bandwidth θ = 1 → 4/3 via Kuznetsov/Kloosterman
   and a "spectral doubling" β(θ) = θ/(2−θ) giving 93.45% and 90.147%. Our repo has
   **PROVEN (Lean + adversarial): beyond-α=1 pair correlation closed everywhere; in-class
   certificate ceiling 0.6818; third moment does not break the 5/6 distinct wall.** A 90%
   simple-zero claim would exceed the 5/6 distinct ceiling by a wide margin — it cannot be
   right without breaking a Lean-checked theorem. The scaling transformation β(θ) looks
   like model-fitting (0.8690 → 93.45% via an asserted formula), not a proof; the "20
   degrees" of Deshouillers–Iwaniec are real literature but their use here is unverified.
   **Label: INCONCLUSIVE-to-REFUTED — contradicts PROVEN walls; requires independent
   re-derivation before any weight; treat as NOT a record.**
4. **Li criterion note — easy direction only (PROVEN).** "Off-line zero exponential
   destruction" (λ_n → −∞ if an off-line zero exists) is the trivial direction of Li's
   criterion, known since 1997. The hard direction — λ_n ≥ 0 for the ACTUAL ζ — IS
   equivalent to RH and is NOT proven; only λ_1..λ_50 were checked numerically (and the
   note itself corrects an earlier float64-corrupted table). "PROVEN EQUIVALENCE" in the
   header is the equivalence theorem (Li 1997), not a proof of positivity.
   **Label: CHECKED NUMERICALLY for n ≤ 50 only; the RH claim is NOT established.**

## Root cause (process lesson)
The other session ran an agent (or agents) that produced a formal-looking artifact whose
theorems are vacuously true — the familiar failure mode where the hard input is moved into
a hypothesis. Its reports self-label PROVEN with no adversarial validator. Per the campaign
method: extraordinary claims get hostile referees before the coordinator reads the proof;
these claims have NOT been refereed by any independent instance. Nothing in these commits
is a record; nothing is a lever.

## What stands (unchanged, re-affirmed)
- Our own PROVEN results stand: marked-moment inequality m₃ ≥ m₂² (theorem),
  convention-locking S₃ ≥ 6.153476, m₃-separation (88σ), BHB input verified.
- Our PROVEN walls stand: 0.6818 in-class ceiling, 0.6725007 window ceiling, beyond-α=1
  closed, third moment doesn't break 5/6, RH-inert ceiling.
- The remote commits were rebased in (history preserved) but are labeled NOT-RECORD in the
  ledger. No dispatch is to be based on them without independent re-derivation.

## Files checked
- research/lean-stability/CompleteRHProof.lean (746 lines; theorem at L525–528, L739–742)
- research/lean-stability/GramStability.lean (8 sorries)
- research/lean-stability/FormalTheorems.lean, FullRHTheorems.lean, ArgumentPrinciple.lean
- research/notes/unconditional_90plus_proof.md, lean4_*_report.md, li_criterion_proof.md
