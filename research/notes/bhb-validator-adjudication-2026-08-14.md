# Adjudication of validator attacks A–F (2026-08-14, main loop)

**Adjudicator:** main loop. **Inputs:** validator subagent closing report +
`research/notes/bhb-adversarial-validator-af-2026-08-17.md` + `research/notes/check_validator_af.py`
(ran clean: ALL CHECKS DONE); this session's own earlier validation
(`bhb-zeta2-moment-validation-2026-08-14.md`). **Rule (AGENTS.md):** both sides re-derive in
code; the resolution is written into both notes.

## Verdicts

| Attack | Validator verdict | Adjudication | Status |
|---|---|---|---|
| A pair identity | NOT BROKEN | CONFIRMED (matches own 20-trial check; their 200-trial × 2 F-types + E = S₂ − ΣF(ρ)F(1−ρ) identity) | **ACCEPTED** |
| B box arithmetic | NOT BROKEN | CONFIRMED (b_pair 0.075770, b_tri 0.013368, ζ″-only 0.0805, ζ″-free 0.2237; factor 4; r = 99/1274 with diagonal denominator 91/80, r_net 0.09925 — cosmetic) | **ACCEPTED** |
| C left tail | BROKEN as stated | **REJECTED in substance — obstruction STANDS** (see below); two wording/number fixes ACCEPTED | **REJECTED (with fixes)** |
| D GM thresholds | NOT BROKEN | CONFIRMED (exact Fraction checks 19/70, 17/60, 0.47826 at Δ=0.28) | **ACCEPTED** |
| E ζ″-moment r′ = 3/5 | BROKEN (Gonek (T/2π)ℒ⁴/12) | CONFIRMED — identical to this session's independent break; plus accepted §2-mechanism correction (s=1 residue is L-independent / suppressed by B(1)=0 for the μ-mollifier; main terms come from the character-sum diagonal) | **ACCEPTED (both findings)** |
| F M2 δ-Taylor | FAIL as written (center 1/2+iγ) | CONFIRMED — genuine writeup defect; corrected to 1/2−iγ (true midpoint of ρ̄, 1−ρ); numeric: |err| = 0.0017 ≪ |δ| = 0.779 at true center vs 1.35 > |δ| at note's center | **ACCEPTED — FIXED in both notes** |

## The C adjudication (the one substantive disagreement)

**Validator's claim:** |E| ≤ 2·S₂ is exact and unconditional, because "the pairing bijection
ρ↦1−ρ̄ gives Σ|F(1−ρ)|² = Σ|F(ρ)|² = S₂"; hence the left-mass T^{1.258}L² ⊂ S₂ contradicts the
premise S₂ ~ T L³, and E/S₂ → O(1) is the true worst case.

**Why it fails:** the pairing gives Σ|F(1−ρ)|² = Σ|F(ρ)|² =: **M₂** — but M₂ ≠ S₂. In this
program S₂ := ΣF(ρ)F(1−ρ) (BHB Lemma 1's sum, ~ (T/2π)ℒ³·57/64 unconditionally). By definition
E = ΣF(ρ)[F(ρ̄) − F(1−ρ)] = M₂ − S₂, so **M₂ = S₂ + E**. The left-mass is a subset of M₂, which is
NOT constrained by Lemma 1. The correct trivial bound is |E| ≤ 2M₂ (C–S + involution), not |E| ≤ 2S₂.

**Counterexamples (code, `tools/check_left_tail_adjudication.py`):**
1. Single FE-consistent pair, exact arithmetic: F(ρ) = 100, F(1−ρ) = 1 (real coefficients;
   F(ρ̄) = conj F(ρ), F(1−ρ̄) = conj F(1−ρ)): E_pair = (100−1)² = 9801, S₂_pair = 2·100·1 = 200,
   E/S₂ = **49.005 > 2** — |E| ≤ 2S₂ is FALSE.
2. FE-consistent left-heavy model (the M3 worst case: N = T^{0.478} left zeros at β = 0.22,
   |F(ρ)|² ~ T^{0.78}L², |F(1−ρ)|² ~ T^{0.22}L²): E/S₂_lemma = 10.2, 14.2, 20.8 at
   T = 10⁴, 10⁵, 10⁶ — growing at the predicted rate T^{0.258}/L (constant 2π·64/57); while the
   left pairs' own contribution to S₂ is T^{0.978}L² ≪ S₂ (ratio 0.78, 0.56, 0.43 → 0) — so the
   configuration violates neither Lemma 1 nor any density input. **E/S₂ → ∞ is the correct worst
   case; the left-tail obstruction stands.**

**Accepted sub-findings:** (i) the "N(0.22,T) ≪ T^{1.69}" exponent was wrong — the correct
statement is N(0.22,T) = N(T) − N(0.78,T) + O(1) ~ (T/2π)L (FE complement; GM gives
N(0.78,T) ≪ T^{0.478}); the uniform GM value at σ = 0.22 would be T^{30·0.78/13} = T^{1.80} (the
GM-formula 15(1−σ)/(3+5σ) = 2.85 is out of GM's range [7/10, 8/10]) — fixed in the M3 note; (ii)
the M3 note now states explicitly that the worst-case mass contributes to Σ|F(ρ)|² = S₂ + E, not
to S₂.

## Fixes applied (this round)

- `bhb-m2-fe-zeta2-elimination-2026-08-14.md`: §4 and summary/table — δ-Taylor center corrected
  1/2+iγ → 1/2−iγ, false O((β−1/2)³) claim at the wrong center documented with the numeric
  refutation; conclusions unchanged (|ζ″(1/2−iγ)| = |ζ″(1/2+iγ)|).
- `bhb-lemmaN-firstcheck-2026-08-14.md`: §3 same correction (s₀ = 1/2−iγ; modulus statements
  unaffected).
- `bhb-m3-density-gap-2026-08-14.md`: left-tail section — wrong "T^{1.69}" removed; explicit
  M₂ = S₂ + E structure; |E| ≤ 2S₂ explicitly rejected with the counterexample + model (script
  cited).
- `bhb-zeta2-moment-2026-08-14.md`: addendum gains the §2-mechanism correction (s=1 residue is
  L-independent / B(1)=0 for the μ-mollifier; main terms from the character-sum diagonal).
- New script: `tools/check_left_tail_adjudication.py` (run:
  `uv run --quiet python tools/check_left_tail_adjudication.py`).

## Net effect on the milestone chain

Unchanged: pair identity, M2 FE-elimination REFUTED, Route D GAP (left-tail obstruction —
now with a cleaner proof and code), GM right tail, Gonek break (r′ = 3/5 REFUTED), box ceiling
b ≤ 0.2237, κ* records table. The validator's A, B, D, E, F findings and my independent pass are
now mutually confirming; the single substantive disagreement (C) is resolved in the notes' favor
with code.
