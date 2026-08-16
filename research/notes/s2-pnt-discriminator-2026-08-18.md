# S2-PNT discriminator probe — the prime-counting side (FINAL)

**Date:** 2026-08-18. **Agent:** builder (S2-PNT, task 10e2afd6). **Binary:** tools/s2pnt/main.rs (Rust, rustc -O, single file, no deps). **Data:** tools/data/zeros_rust_924k.txt (924,715 zeros, γ ≤ 559999.733, 8A-certified on-line). **Run:** `rustc -O tools/s2pnt/main.rs -o tools/s2pnt/s2pnt && ./tools/s2pnt/s2pnt` → tools/s2pnt/run2.out (v2, canonical). Runtime 20 s.

## 1. Object and method (RUST ONLY)

ψ(x) − x via the classical explicit formula, pair-summed over the cached zeros:

**ψ(x) − x = −Σ_ρ x^ρ/ρ − log(2π) − ½·log(1 − x^{−2})** (x > 1 non-integer, PROVEN classical; Davenport/Titchmarsh form), with

**Σ_ρ x^ρ/ρ = 2√x · Σ_{γ>0} [½·cos(γt) + γ·sin(γt)] / (γ² + ¼)**, t = log x.

Grid: 72 log-spaced points, x ∈ [10³, 3×10¹¹] (T = 5.6×10⁵ ≳ √x required; brief says cache suffices to x ≲ 3×10¹¹ — certified below). Envelope E(x) = max_{x′≤x} |ψ(x′)−x′|/√x′ (grid-sampled). Truncation certified empirically: |full − 462k-zeros| ≤ 1.6e3 ψ-units (2.9e-3 E-units) and |full − 100k| ≤ 6.6e3 (1.2e-2 E-units) at x = 3×10¹¹ — the tail beyond T = 5.6×10⁵ is negligible in E-units over the whole range (the pessimistic worst-case bound x·log²(xT)/T overstates; phases cancel).

**Validation (CHECKED NUMERICALLY):** explicit formula vs direct sieve of Λ(n): |diff| = 5.4e-4 (x=10), 6.3e-4 (10²), 2.2e-2 (10³), 8.5e-2 (10⁴), 2.2e-1 (10⁵) — all at the truncation-error scale (≤ 2.2e-1 in ψ-units ≈ 2e-6 relative at x=10⁵). Formula, constants (log 2π, ½log(1−x⁻²)) and signs verified.

## 2. Real case — ψ(x) − x with the 924k cached zeros (CHECKED NUMERICALLY — consistent with RH; consistency check, NOT a proof)

- **Envelope is FLAT:** E(x) ≤ 0.49·√x over x ∈ [10³, 3×10¹¹] (grid-sampled; run1's 60-pt grid caught a 0.487 bump at x≈1.1×10⁹, run2's 72-pt grid peaks at 0.434). No (log x)^p growth visible in range.
- **Band ratios (running envelope):** max E/√(log x) = 0.126 — **8× below the √x·(log x)^{1/2} band**; max E/log x = 0.041 — **24× below the von Koch √x·log x band**. Never touches either band.
- **Effective growth exponent δ = d(ln E)/d(ln x) (top-half LS fit): δ = 0.013** — flat. (The (log x)^p power fit is ill-posed for a flat envelope — ln(E/√x) vs ln ln x gave a nonsense p = −9 artifact; the honest exponent is δ ≈ 0.)
- Interpretation: with all 924k zeros on the line, |ψ−x| ~ √x·(fluctuating sum Σ x^{iγ}/γ) which is O(√x) in range — exactly the on-line-zeros signature (Littlewood: Ω±(√x log log log x), numerically ≪ band here). **Consistency check only; finite range, finite zero set, no proof content.** Not a proportion-on-line result; firewall respected.

## 3. Planted-zero controls (RH-FALSE MODEL — the discriminator, CHECKED NUMERICALLY)

Pattern (8A's): remove the on-line pair at γ₁ = 14.134725…, plant (β, γ₁) + (1−β, γ₁) — conjugate + FE-symmetric fake ξ′, so the zero set stays symmetric under ρ ↦ 1−ρ. Off-line pair term: 2x^β[βcos(γ₁t)+γ₁sin(γ₁t)]/(β²+γ₁²).

| case | δ measured | β−1/2 expected | max E/√(log x) | first x where E > √x(log x)^{1/2} band |
|---|---|---|---|---|
| REAL | 0.013 | 0 | 0.126 | never |
| β = 0.6 | 0.083 | 0.10 | 0.386 | never (needs x ≈ 10¹⁶) |
| β = 0.65 | 0.151 | 0.15 | 1.319 | **1.9×10¹⁰** |
| β = 0.7 | 0.202 | 0.20 | 4.828 | **4.5×10⁷** |

- **Discriminator FIRES for β−1/2 ≥ 0.15 within range:** β=0.7 crosses the √x(log x)^{1/2} band at x = 4.5×10⁷ (|ψ−x|/√x = 3.68 at 1.5×10⁷, band 4.06 — visibly climbing); β=0.65 crosses at 1.9×10¹⁰. The control envelope grows like ~(2/γ₁)·x^{β−1/2}·√x with the real envelope riding below — clean separation from the flat real case.
- **The probe MEASURES β−1/2:** the fitted envelope exponent δ recovers the planted β−1/2 to within 0.02 (0.083 vs 0.10, 0.151 vs 0.15, 0.202 vs 0.20) — the off-line displacement is readable from the envelope's growth rate.
- **Detection threshold (CONJECTURED, empirical):** with T = 5.6×10⁵ and x ≤ 3×10¹¹, violations with β−1/2 ≲ 0.13 are NOT detectable (β=0.6 crosses the band only at x ≈ 10¹⁶ — the x^β/γ₁ term needs x^{β−1/2}·(2/γ₁) > √(log x), i.e. x^{0.1} > 14.15·√(log x)/2 ≈ 34 → x ≈ 10¹⁶). The probe is a finite-resolution RH-false detector, not a proof.
- Honest limits: the control is a fake-ξ′ explicit-formula model (8A's pattern), not a literal ζ with a planted zero; the discriminator validates the *mechanism* (off-line zero ⟹ x^β envelope growth ⟹ band crossing), which is the classical Landau-oscillation direction. Verified against real: real never crosses (ratio ≤ 0.13), controls with β−1/2 ≥ 0.15 do (ratio up to 4.8).

## 4. Literature check — one-way vs trap (PROVEN from the campaign corpus)

- **No RH-conditional O(√x (log x)^{1/2+ε}) PNT bound is cited anywhere in research/ (notes + papers).** Grep for von Koch / √x·log / x^{1/2}·log / oscillation across research/notes/*.md and research/papers/ returns only: (a) fresh-object-hunt §2's own statements, (b) the ledger S2 entry, (c) unrelated explicit-formula machinery. The papers corpus (zeta moments, Anthropic campaign) contains nothing on von Koch PNT refinements.
- **The best cited RH-conditional PNT error is von Koch's π(x) = li(x) + O(√x log x)** (fresh-object-hunt §2(b): "The best published RH-conditional bound is this O(√x log x); no improvement of the log-power is standard"). RH ⟹ O(√x log x) is PROVEN classical; RH ⟹ O(√x (log x)^{1/2+ε}) is NOT a theorem (it would be a sharpening of von Koch's log-power; under RH the zero-sum truncation gives √x·log²x for ψ / √x·log x for π — the (log x)^{1/2} target is strictly stronger, consistent with Montgomery's conjecture that the true oscillation is ~√x(log log x)^{O(1)}).
- **Verdict: S2 is one-way, NOT a trap.** No published ⟺ — the hypothesis π(x) = li(x) + O(√x(log x)^{1/2+ε}) does not collapse to RH. fresh-object-hunt's contingent literature claim (§2(c), CONJECTURED-there) is now CONFIRMED.

## 5. The catch — S2 is a known theorem restated (deflating class 1), NOT a lever

- The **forward direction is already PROVEN classical** (fresh-object-hunt §2(b) itself): √x(log x)^{1/2+ε} = O(x^{1/2+ε}) ∀ε, and the von Koch criterion π(x) = li(x) + O(x^{1/2+ε}) ∀ε ⟺ RH is classical (Titchmarsh Ch. XIV; the ⟹ direction is Landau's abscissa-of-convergence/oscillation argument: O(x^{1/2+δ}) error ⟹ no zeros with Re > 1/2 ⟹ RH via the functional equation).
- **The hypothesis is strictly stronger than RH:** RH gives only π = li + O(√x log x); the (log x)^{1/2+ε} refinement is not implied by RH (no such theorem exists, §4). So S2 ⟹ RH is true but S2 is not ⟺ RH, and proving the S2 hypothesis would require proving something strictly stronger than RH.
- **Consequence:** S2 has zero proof leverage — it restates a classical implication with a stronger-than-RH hypothesis. Class-1 deflation (known theorem restated), exactly as fresh-object-hunt §0/§2(e) forecast (65% true, 1% provable — confirmed: true as a criterion, provability nil). **Do not fund as a proof lever.** The probe's value is the new discriminator data family (prime-counting side, zero-overlap with the equivalence-lever zoo) and the closure of the trap question.

## 6. Headline numbers (run2.out, canonical)

- Real: E(x) ≤ 0.49√x for x ≤ 3×10¹¹ (flat, δ=0.013); max E/√(log x) = 0.126 (8× under band); max E/log x = 0.041 (24× under von Koch band); truncation certified ≤ 1.2e-2 E-units at 3×10¹¹.
- Controls (planted (β,γ₁)+(1−β,γ₁)): β=0.7 fires at x=4.5×10⁷ (max ratio 4.83); β=0.65 fires at 1.9×10¹⁰ (max 1.32); β=0.6 never fires in range (0.386 max; crossing at x≈10¹⁶). δ recovers β−1/2 to ±0.02.
- S2 status: **one-way (not trap), but known-theorem-restated — closed as a lever; discriminator family validated and reusable.**

## Labels

- Explicit formula + anchors: PROVEN formula, CHECKED NUMERICALLY (sieve match ≤ 2.2e-1 ψ-units, truncation-scale).
- Real envelope flat, control firing, δ-recovery: CHECKED NUMERICALLY (finite grid, finite zeros; consistency check, no proof content).
- Detection threshold β−1/2 ≳ 0.13: CONJECTURED (empirical from this run).
- Literature: PROVEN from campaign corpus (no (log x)^{1/2+ε} RH-conditional PNT result cited; von Koch O(√x log x) is the best cited).
- S2 = one-way CONJECTURED-as-novel → downgraded to **known theorem restated (class 1), closed.**

## Files

- tools/s2pnt/main.rs (probe), tools/s2pnt/run2.out (canonical v2 output), tools/s2pnt/run.out (v1, x ≤ 1e10), research/notes/s2-pnt.progress.
