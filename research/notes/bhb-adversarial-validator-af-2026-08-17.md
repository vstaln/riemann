# Adversarial validation A–F of the three BHB notes (2026-08-14) — final pass

**Validator:** adversarial validator subagent. **Script:** `research/notes/check_validator_af.py`
(run: `uv run --quiet python research/notes/check_validator_af.py`; also reran `tools/check_pair_identity.py`
and `tools/check_bhb_arithmetic.py` — both PASS). **Date:** 2026-08-17.

## Per-target verdicts

**A (pair identity): NOT BROKEN.** Verified by hand (conjugation/real-coefficient algebra: pair
contribution = [F(ρ)−F(1−ρ̄)]·[F(ρ̄)−F(1−ρ)] = |F(ρ)−F(1−ρ̄)|² since F(ρ̄)−F(1−ρ) =
conj(F(ρ)−F(1−ρ̄))) and numerically: 200 trials × 2 F-types (polynomial and Dirichlet polynomial,
real coefficients), sets closed under ρ↔1−ρ̄. E ≥ 0; on-line zeros (fixed points) contribute 0;
also E = S₂ − ΣF(ρ)F(1−ρ) and |E| ≤ 2·S₂ exactly.

**B (box bound): NOT BROKEN (arithmetic).** b_pair = 0.075770 (claim 0.07577), b_tri = 0.013368
(claim 0.01337), b_pair(ζ″-only) = 0.080527, b_pair(r′=0) = 0.2237; factor 4 in E ≤ 4Δ²Σ|F′|² correct
(ρ, 1−ρ̄ symmetric about 1/2+iγ, quadratic Taylor term cancels exactly — M3 note uses the CORRECT
midpoint here). r = 99/1274 reproduces 3ϑ³∫u²P²/(1/2+3ϑ∫P²) = (99/1120)/(91/80) exactly (the
denominator is 91/80, not c(S₂)=57/64; the "r_net" variant is 0.09925 — cosmetic). Box VALUES inherit
the CONJECTURED/refuted status of r′ (see E).

**C (left tail): BROKEN as stated.** |E| ≤ 2·S₂ is exact and unconditional (C–S with the pairing
bijection ρ↦1−ρ̄: Σ|F(1−ρ)|² = Σ|F(ρ)|² = S₂), so "E_out⁻/S₂ → ∞" is impossible: the worst-case mass
T^{1.258}L² is a SUBSET of S₂ = Σ|F(ρ)|². The note's worst case is inconsistent with its own premise
S₂ ~ T L³; the correct worst case is E/S₂ → O(1) (up to ~1 via E = S₂ − ΣF(ρ)F(1−ρ) with the latter
fixed at (T/2π)ℒ³·57/64). The GAP conclusion (no density input certifies E/S₂ < 0.0311) SURVIVES in
weakened form; the demonstration numbers are broken. Minor: "N(0.22,T) ≪ T^{1.69}" matches neither GM
(2.85) nor uniform (1.80) exponents at σ=0.22.

**D (GM thresholds): NOT BROKEN.** Exact Fraction checks: 15(1/2−D) < (3+5(1/2+D))/2 ⟺ D > 19/70;
(30/13)(1/2−D) < 1/2 ⟺ D > 17/60; at Δ=0.28 (σ=0.78) GM exponent 0.47826 < 1/2.

**E (zeta2-moment note): PARTIALLY BROKEN — the r′ = 3/5 anchor is REFUTED.**
- (i) NOT BROKEN: FE χζ(1−s)=ζ(s) verified numerically (rel err 2·10⁻¹²); (χ′/χ)(s) =
  (χ′/χ)(1−s) = −L + O(1/t) ✓; ζ″(1−s) = χ(1−s)[ζ″+2Lζ′+L²ζ] + O(1/t) rel err 3.9·10⁻⁵ ✓ (both
  signs +2L, +L² confirmed; two independent hand derivations agree).
- (ii) **BROKEN: the un-mollified constant is (T/2π)ℒ⁴/12 (Gonek: J₁ ~ (1/12)ℒ³ with N ~ (T/2π)ℒ),
  NOT (T/2π)L³/3.** Independent numeric check: coefficients a₂ of ζ′/ζ·ζ′² give
  Σ_{n≤X} a₂(n) ~ −X(logX)⁴/24 (ratios 0.556, 0.576, 0.587, 0.595 at X = 5·10⁴…2·10⁵, converging from
  below; order-5 pole at s=1, B=1 ⟹ B(1)≠0). B=1 Lemma 1: S₂ = (T/2π)ℒ³/2 − 2Re(ℳ₂), ℳ₂ =
  Σ_{m≤T/2π}a₂(m) ~ −(T/2π)ℒ⁴/24 ⟹ S₂(B=1) ~ (T/2π)ℒ⁴/12. The note's "1/2 − 2·(1/12) = 1/3" is only
  the ℒ³-subleading coefficient. (The mollifier case is regular because B(1) = Σμ(k)P(·)/k → 0 kills
  the ℒ⁴ term — the B=1 limit is singular, so "B=1 limit of Lemma 1" is not a valid limit.)
- (iii) **BROKEN as derived:** r′ = 3/5 = c(M)/c(S₂) = (1/5)/(1/3) rests on the refuted anchor; the
  factorization 57/64 = (1/3)(1+107/64) is algebra but "1/3 = un-mollified constant" is false, so
  MF-derivative-independence has no standing. M = (3/5)L²S₂: FAIL. Order-level M = O(ℒ²S₂) survives
  (both ℒ⁵-scale). Also the note's §2 mechanism ("the s=1 pole … exactly produces the T L⁵ main term")
  is wrong: the s=1-pole residue of the M-integrand is L-independent (all coefficients are constants
  γ₀, ζ^(k)(0)); the main term comes from the character-sum diagonal (same as S₂).
- (iv) NOT BROKEN (arithmetic): b = 0.0201, 0.0134 ✓ — but conditional on the refuted r′.

**F (M2 note): NOT BROKEN (corrected form) — one genuine writeup defect.**
- Exact identity F(ρ̄)−F(1−ρ) = B(ρ̄)δ(ρ) + [B(1−ρ)−B(ρ̄)]ζ′(ρ)/χ(ρ), δ(ρ) = ζ′(ρ̄)−ζ′(1−ρ), with
  ζ′(1−ρ) = −ζ′(ρ)/χ(ρ) (FE differentiated at a zero, unconditional): verified by hand. ✓
- δ(ρ) = 2(β−1/2)ζ″(1/2−iγ) + O((β−1/2)³): TRUE at the true midpoint 1/2−iγ (numeric: err 0.0017 vs
  |δ| 0.779 at β−1/2 = 0.02, t = 1000). **But the M2 note §4 (and firstcheck §3) expand about
  1/2+iγ — the WRONG height (ρ̄ and 1−ρ are at −γ) — and claim O((β−1/2)³); numerically the error
  there is |δ − 2(β−1/2)ζ″(1/2+iγ)| ≈ 1.35 > |δ| (the ζ‴-term −4iγ(β−1/2)ζ‴ does not cancel). The
  note's leading-coefficient conclusion survives only because |ζ″(1/2−iγ)| = |ζ″(1/2+iγ)| (real
  coefficients).** Corrected statement: 2(β−1/2)ζ″(1/2−iγ) + O((β−1/2)³).
- E = S₂ − ΣF(ρ)F(1−ρ): verified numerically. ✓

## Verdict table

| Note / claim | Verdict |
|---|---|
| M3: pair identity E = Σ_pairs \|F(ρ)−F(1−ρ̄)\|² ≥ 0; on-line zeros → 0 | **PASS** |
| M3: E ≥ 0 unconditionally (N* ≤ S₁²/S₂) | **PASS** |
| M3: box b_pair = 0.07577 / b_tri = 0.01337 / 0.0805 / 0.2237 arithmetic | **PASS** (values conditional on r′) |
| M3: b_pair = 0.0758 (pair form) | **NEEDS-WORK** — r′ = 3/5 refuted; only ζ″-free ceiling 0.2237 stands |
| M3: GM right tail killed at Δ > 19/70; exponent 0.4783 at Δ=0.28; uniform 17/60 | **PASS** |
| M3: left tail worst case T^{1.258}L² ≫ S₂, E_out⁻/S₂ → ∞ | **FAIL** (|E| ≤ 2S₂ exact; worst case O(1)) |
| M3: Route D GAP (left tail uncertifiable by density inputs) | **PASS** (weakened: E/S₂ can be O(1), not ∞) |
| M2: exact FE identities (i),(ii); E = S₂ − ΣF(ρ)F(1−ρ); ζ″-invariance conclusion | **PASS** |
| M2: δ(ρ) Taylor §4 (center 1/2+iγ, O((β−1/2)³)) | **FAIL** as written — wrong center, false error term; corrected (1/2−iγ) version true |
| zeta2: ζ″(1−s) FE formula | **PASS** |
| zeta2: un-mollified ζ′ constant (T/2π)L³/3 | **FAIL** — true value (T/2π)ℒ⁴/12 (Gonek; J₁ ~ (1/12)ℒ³) |
| zeta2: M = (3/5)L²S₂, r′ = 3/5 | **FAIL** — anchor refuted, ratio unknown (O(1)) |
| zeta2: M = O(ℒ²S₂) order-level | **PASS** (both ℒ⁵-scale; transfer plausible) |
| zeta2: box 0.0201 / 0.0134 | **NEEDS-WORK** — arithmetic fine, conditional on refuted r′ |
| zeta2: "s=1 pole produces the T L⁵ main term" (mechanism §2) | **FAIL** (mechanism) — residue is L-independent |

Net: 2 real breaks (left-tail "→ ∞"; r′ = 3/5 anchor via Gonek) + 1 writeup defect (M2 Taylor
center). All milestone conclusions that are r′-independent (pair identity, M2 refutation, Route D GAP,
GM right tail) survive.
