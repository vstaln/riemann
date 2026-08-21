# Lever Ranking — local Jensen discriminant → global attack (2026-08-21)

**Author:** architect (read-only analysis). **Status:** DECISION NOTE, no proofs inside.
**Inputs:** E(c,r) discriminant from 100k zeros (E_RH=0.182322 vs E_false=1.098612 at
c=0.75+14.1347i, r=0.30; gap 0.916291; vanishes for |T−t0|>0.28). Five one-shot levers A–E.

Scoring: (i) proof-completeness achievable this session, (ii) genuine RH-equivalence content,
(iii) adversarial robustness — does the RH-false control actually fire, or is it tautological?

## Ranking (best → worst)

| Rank | Lever | (i) session completeness | (ii) equivalence content | (iii) control fires? | Verdict |
|---|---|---|---|---|---|
| 1 | C. Weil explicit-formula bridge | MEDIUM | HIGH — Weil positivity W(φ)≥0 ∀φ∈C_c^∞ is a true equivalence (Weil 1952) | YES — planted off-line zero makes the compressed Hermitian form indefinite; same machinery as the repo-certified 67.25% work | PUSH NOW |
| 2 | E. Nyman–Beurling defect-rate floor | MEDIUM-HIGH (cheap least-squares) | HIGH in theorem form — d_N decay exponent is tied to sup Re(ρ) (Báez-Duarte/Burnol line of results) | MIXED — signal is large (planted predicts N^{-2(1−0.85)}=N^{-0.3} floor vs ~e^{-1} at N=5000, a factor ~5) but exponent certification from N≤5000 is not honest | SECOND |
| 3 | A. Global covering | LOW | LOW — E(c,r)=0 ⟺ no zero in disc is a trivial restatement of the zero statement; all content would live in a proven L(T), which is circular | CONDITIONAL — fires only if E is computed from ζ itself (argument principle), never from the zero corpus; corpus-E is tautological | DEMO ONLY |
| 4 | B. Real Li λ_n | MEDIUM (cheap) | HIGH in statement (λ_n≥0 ∀n ⟺ RH, Bombieri–Lagarias) but the computable window is vacuous | NO at feasible n — see hole below; control likely cannot fire | SHELVE |
| 5 | D. E-island chain | LOW | LOW — strictly dominated by A | inherits A's tautology risk plus chain bookkeeping | SHELVE |

## Hole analysis (one biggest hole each)

**C — Weil bridge.** Hole: positivity for ALL φ is RH itself; one φ family proves nothing.
The finite-family version is a numerics check whose value depends entirely on (a) a *derived*
prime-side error budget (O(log T / X^{1/4}) must be proven for the truncation actually used,
not asserted) and (b) family richness sufficient for the planted perturbation to force an
indefinite form. Unquantified "sufficiently rich" is where inflated claims would hide.
Mitigating fact: this is exactly the finite-compression + Sylvester inertia methodology of the
certified 0.673481/0.836740 proportion record — tools and hostile validators already exist.

**E — Nyman–Beurling.** Hole: d_N decay *rate* asymptotics need N→∞; N≤5000 sits in the
pre-asymptotic regime, so a fitted exponent is a curve fit, not a certificate. The planted
control signal is the largest of the five (factor ~5 at N=5000), which is attractive, but
"the fitted slope matches the planted prediction" is CHECKED NUMERICALLY evidence at best and
must never be written as "the exponent theorem is confirmed."

**A — Global covering.** Hole: L≤0.19 is *measured*, not proven, and cannot be proven
non-circularly: E is a sum of log singularities, so it is not Lipschitz near zeros, and
knowing where it is smooth presupposes knowing where the zeros are. Worse, the tautology
trap: E computed from the 100k-zero corpus says nothing about zeros outside the corpus.
The honest version of A is per-disc argument-principle zero counting (∮ζ′/ζ) — which is
rigorous zero-free certification, i.e., Platt–Trudgian-style technology: real, but a
re-derivation of known methods, not a new lever. The Lipschitz shortcut is vacuous.

**B — Li coefficients.** Hole: sensitivity. A single off-line zero contributes O(1) to λ_n
(contribution → 1 as n grows for Re ρ > 1/2), while λ_n itself grows like O(n log n) and the
truncation error from the finite zero corpus swamps an O(1) shift at n≤50. Additionally
λ_1=λ_2=1 identically and the first dozens of λ_n are positive *unconditionally* — the
computable window has zero discriminative power. The planted control likely cannot fire at
any feasible n. This is the weakest control in the set; do not spend compute here.

**D — E-island chain.** Hole: identical to A — each disc in the chain needs a per-disc
sup/zero-free certificate, which is the same argument-principle problem, so the chain adds
bookkeeping (overlap > L·Δt with an unproven L) on top of an unsolved core. The pigeonhole
barrier language is narrative, not mathematics. Strictly dominated by A; shelve.

## The ONE lever to push hardest now: C

**Why:** only lever that is simultaneously (a) a genuine equivalence in its full form,
(b) fireable as an RH-false control with the existing planted-zero methodology, and
(c) executable with tools the repo has already certified (finite Weil compression,
inertia signatures, RUST-ONLY compute discipline).

**Minimal honest deliverable this session:**

1. Fix a finite φ family (e.g. smooth compact support in one annulus around
   c=0.75+14.1347i, a handful of dilates/translates — say 5–20 members).
2. Derive (on paper, in the note) the prime-sum truncation error for the *actual* X used;
   label it PROVEN only if the bound is derived, otherwise CONJECTURED error model.
3. Run two computations: real-zero data → expect W(φ)≥0 on the family;
   planted β0=0.85 zero → expect some family member gives W(φ)<0.
4. **The control must fire before the real-side result is trusted** (hard rule 7).
5. Label the outcome: "CHECKED NUMERICALLY on an n-member family with error budget B;
   NOT a proof; full statement W(φ)≥0 ∀φ ⟺ RH is Weil's theorem, cited not re-proven."
   A proportion-style statement ("k of n family members positive") is ZERO RH evidence
   in either direction and must be described exactly that way.

**Fallback if C stalls:** E's cheap least-squares run (d_N for N up to ~5000, real vs
planted), delivered as raw numbers + fitted slopes, explicitly labeled pre-asymptotic.

## Explicit non-claims

- Nothing here proves RH or any part of it.
- E's 0.18-vs-1.10 gap is a property of the 100k corpus plus the planted model; it is not
  evidence about zeros outside the corpus.
- A and D are shelved not because zero-free certification is worthless (it is the gold
  standard) but because their Lipschitz framing adds nothing over argument-principle
  counting, which is known technology.
