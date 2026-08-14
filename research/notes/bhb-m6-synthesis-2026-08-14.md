# M6: Synthesis — BHB partial-unconditionalization after M2/M3/M4-validation

**Date:** 2026-08-14. **Scope:** milestone synthesis per `bhb-unconditionalization-plan-2026-08-14.md`
(plan §M6). All quantitative claims trace to `tools/check_bhb_arithmetic.py` and
`tools/check_pair_identity.py` (both pass) or to derivations in the cited notes.

## 1. Where the program stands (commit trail)

| milestone | deliverable | verdict | commit |
|---|---|---|---|
| M1 | gap table: bottleneck = moving-boundary count N(1/2+b/L,T) = o(T log T), k<1 | DONE | `87d513d` |
| M2 | FE ζ″-elimination | **REFUTED** (ζ″ invariant under FE rewrite; exact step: δ(ρ) = 2(β−1/2)ζ″(1/2−iγ)+O((β−1/2)³)) | `b62adc9` |
| M4-in-essence | ζ″-moment M = (3/5)L²S₂ claim | **BREAK FOUND**: r′ = 3/5 REFUTED as derived (anchor (T/2π)L³/3 contradicts Gonek's theorem Σ\|ζ′(ρ)\|² ~ (T/2π)ℒ⁴/12, arXiv:1302.5032 verbatim; ℒ⁴ traced to the order-5 pole in the q=1 piece of ℳ₂, CHECKED NUMERICALLY); M = O(ℒ²S₂) survives at order level only | `b62adc9` + validation note |
| M3 | density exponent gap | **GAP**: Route D collapses into Route A; GM kills right tail at Δ > 19/70; left tail uncontrollable; NEW pair identity E = Σ_pairs\|F(ρ)−F(1−ρ̄)\|² ≥ 0 → box b ≈ 0.0758 (pair form) vs 0.0134 (triangle) | `fd94729` |
| M5 | box attainment b ≈ 0.0758 | GATED: no known input certifies any fixed b at o(T log T) (Shape-1 blind PROVEN; Ingham k=5 → b ~ 3 log log T; GM Shape-1) | — |
| M6 | this note | — | — |

## 2. The exact structural picture (all PROVEN unless labeled)

Setup: F = Bζ′, E = Σ_{0<γ≤T} F(ρ)[F(ρ̄) − F(1−ρ)], S₂ = Σ|F(ρ)|², slack 0.031126.

1. **E = S₂ − Σ_ρ F(ρ)F(1−ρ)** — exact (M2 note; re-verified).
2. **E = Σ_pairs |F(ρ) − F(1−ρ̄)|² ≥ 0** — exact pair identity (M3 note; CHECKED NUMERICALLY,
   20 random trials, machine precision). On-line pairs are fixed points (β = 1/2), contribute 0.
   Unconditional: E ≥ 0, so the off-line correction only lowers the certificate
   N* ≤ S₁²/(S₂+E) ≤ S₁²/S₂.
3. **Box (quadratic) form:** if |β−1/2| ≤ b/L for all zeros, E/S₂ ≤ 8b²(r+r′) with
   r = 99/1274 ≈ 0.0777 (PROVEN) and r′ ≥ 0 ⟹ **b ≤ 0.2237 (PROVEN ζ″-free ceiling)**. The
   claimed r′ = 3/5 (b ≈ 0.0758) is REFUTED as derived (Gonek's theorem breaks its anchor);
   r′ unknown, O(1)-scale, awaits M4-proper. The triangle form (b ≈ 0.0134) is superseded —
   the pair identity removes a factor ~5.7 of box width.
4. **Route D (box-free density) is REFUTED:** (a) thin strip needs the k<1 moving-boundary count
   (M1 bottleneck CONFIRMED; sup-level version needs N(σ_b,T) ≪ T^{1/2−ε}/L — even stronger);
   (b) right tail killed by GM at fixed Δ > 19/70 ≈ 0.2714 (PROVEN, arXiv:2405.20552 verbatim);
   (c) left tail uncontrollable by any density input (worst case T^{1.258}L² ≫ S₂ ~ T L³,
   consistent with all known bounds) — the box must cover both sides.

## 3. Remaining gaps, ranked (the lever set)

1. **The k<1 moving-boundary count N(1/2+b/L,T) = o(T log T) at b ≈ 0.0758** — the binding
   input. No known route: Shape-1 families blind (PROVEN, scale-gap lemma); Ingham k=5 → b ~
   3 log log T; GM-family is Shape-1; a Shape-2 k<1 theorem via GM's method is CONJECTURED-
   impossible (gm-box §6 obstacle (ii): zero-detection loses a fixed log power via
   Littlewood–Jensen). This is the one-way-door Type-1 decision point of the plan.
2. **M4 proper: mechanical re-derivation of BHB Lemma 1 with ζ′ → ζ″** (diagonal + ℳ-analogue,₁,₂,₃
   + convexity). Closed-form, no compute; pins r′ (currently REFUTED-as-derived, unknown
   O(1)-scale). Until then b_pair ≤ 0.2237 (2.2× narrower than BGSTB's b = 1/2). Cheapest live lever.
3. **S(T)-type / pair-correlation input for Σ_pairs(β−1/2)²|F′(1/2+iγ)|²** — the pair identity
   exposes E as a sum of squares of pair-differences; any input bounding the box-width-weighted
   F′-moment on average would feed the quadratic form directly. No unconditional input known
   (INCONCLUSIVE, new-input program).
4. **BGSTB strong zero-density hypothesis (1.6)** — a moving-boundary hypothesis; its
   unconditional status is open; it is exactly the kind of input that would certify the box.

## 4. Honest bottom line

The BHB in-class certificate ceiling remains 0.6818 (PROVEN, structural wall: no known
unconditional input reaches the 3.11% slack). The M2/M3 rounds **closed two named routes** (FE
elimination; box-free density) and **opened one exact structure** (the pair identity) that
relaxes the box need 5.7× but does not remove it. The program's next lever is M4-proper
(mechanical, closed-form, cheap) followed by the Type-1 decision on the k<1 count; the
structural thread continues per the persistence directive.

## 5. Open items for the next round

- M4-proper re-derivation (upgrade/refute r′ = 3/5).
- Re-check the literature constants: un-mollified Σ|ζ′(ρ)|² ~ (T/2π)L³/3 (Gonek-type; arXiv API
  was down this session — re-fetch and cite).
- If validator subagents report breaks in the M2/M3/zeta2 notes: fix and re-validate.
