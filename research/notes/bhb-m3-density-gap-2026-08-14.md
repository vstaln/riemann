# M3: Zero-density exponent gap — Guth–Maynard vs the weighted off-line correction

Milestone M3 of `bhb-unconditionalization-plan-2026-08-14.md`. Companion notes:
`bhb-m2-fe-zeta2-elimination-2026-08-14.md` (M2, VERDICT: REFUTED), `bhb-zeta2-moment-2026-08-14.md`
(M4-in-essence, UNVALIDATED), `bhb-route-gap-table-2026-08-14.md` (M1, committed `87d513d`).

**One-line answer.** Route D (pure zero-density, no Taylor) is a GAP and collapses into Route A.
The thin strip |β−1/2| ≤ b/L requires the k<1 moving-boundary count (M1 bottleneck, CONFIRMED);
the left tail β ≤ 1/2−Δ is uncontrollable by ANY zero-density input (NEW, stronger than M1);
the right tail is killed by Guth–Maynard at fixed width Δ > 19/70 (NEW — this is where GM pays).
Structural byproduct: exact pair identity E = Σ_pairs |F(ρ) − F(1−ρ̄)|² ≥ 0 (PROVEN), which
relaxes the box requirement from b ≈ 0.0134 (triangle form) to **b ≈ 0.0758 (pair form)** — 5.7×
wider. This note supersedes the earlier draft of the same file (subagent, 20:32); the draft's
errors are itemized in §7.

---

## 1. Input pinned: Guth–Maynard, arXiv:2405.20552 (verbatim)

From the paper text (checked against /tmp/gm_full.txt this session; wrong ID 2404.10137 discarded):

- **Theorem 1.2 (Zero density estimate).** N(σ,T) := #{ρ : Re ρ ≥ σ, |Im ρ| ≤ T}. Then
  N(σ,T) ≪ T^{15(1−σ)/(3+5σ)+o(1)}.
- **Combination (1.4):** N(σ,T) ≪ T^{30(1−σ)/13+o(1)}; 30/13 ≈ 2.3077 improves on Huxley's 12/5.
- **§13.1:** Theorem 1.2 follows from Ingham's (1.2) for σ ≤ 7/10 and Huxley's (1.3) for σ ≥ 8/10;
  the new range is σ ∈ [7/10, 8/10].
- **Crucial:** GM carries NO polylog — +o(1) in the exponent (k = 0 in the M1 k-classification);
  Ingham carries (log T)^5.

STATUS: PROVEN (verbatim).

## 2. Pre-registered question and its answer

M3's question: *is the weighted off-line correction
Σ_{off} |F(ρ)|²(t/2π)^{β−1/2} ≪ 0.0311·S₂ weaker than the k<1 moving-boundary count — does a
fixed-σ (Shape-1) estimate suffice at the weighted level?*

**Answer: NO.** Split the off-line sum at fixed width Δ (F = Bζ′; E = Σ_ρ F(ρ)[F(ρ̄) − F(1−ρ)]):

| region | needed input | known | verdict |
|---|---|---|---|
| thin strip \|β−1/2\| ≤ b/L | box count N(1/2+b/L, T) = o(T log T), k<1, b ≈ 0.0758 (pair form §5) / 0.0134 (triangle) — sup-level version even stronger: N(σ_b,T) ≪ T^{1/2−ε}/L | none (Shape-1 blind at σ_b: PROVEN, `gm-box-certifiability`; Ingham k=5 ⇒ b ~ 3 log log T only) | **GAP — M1 bottleneck CONFIRMED** |
| right tail β ≥ 1/2+Δ | Δ > 19/70 ≈ 0.2714 (GM) | GM at σ = 0.78: exponent 0.4783 < 1/2, constant room + o(1) absorbed | **SOLVED by GM** (§3) |
| left tail β ≤ 1/2−Δ | NOT reducible to any N(σ,T) input; worst case consistent with all known bounds gives T^{1.258}L² ≫ S₂ | — | **GAP (NEW, §4)** |

Net: no combination of known zero-density estimates certifies E/S₂ < 0.0311; the left tail alone
forces the two-sided box — i.e. Route A. GM's contribution is real but subsumed (it kills the
right tail, which Ingham's k=5 could only kill at Δ > ~0.35).

## 3. Right tail: GM kills it at Δ > 19/70 (PROVEN)

For β ∈ [0,1], convexity: |ζ′(β+it)| ≪ t^{(1−β)/2+ε}L, so per-zero |F(ρ)|²(t/2π)^{β−1/2} ≪ t^{1/2+ε}L²
uniformly in β (both sides; left/right counts equal by the FE pairing). Hence with
S₂ ~ (T/2π)L³·(57/64):

E_out⁺/S₂ ≪ T^{−1/2+ε} L^{−1} · N(1/2+Δ, T).

So E_out⁺/S₂ → 0 requires N(1/2+Δ,T) = o(T^{1/2}/L). With GM's sharper exponent at σ = 1/2+Δ
(valid for Δ ∈ [0.2, 0.3]):

15(1/2−Δ)/(3+5(1/2+Δ)) < 1/2  ⟺  Δ > 19/70 ≈ 0.27143.   (CHECKED: script §6)

At Δ = 0.28 (σ = 0.78): exponent 15·0.22/6.9 = 0.4783; margin T^{−0.0217+o(1)}·L^{−1} → 0, with
the constant 2·(2π)·64/57 ≈ 14.1 absorbed. Uniform (1.4) version: Δ > 17/60 ≈ 0.2833. Ingham
alone (k=5): needs Δ > ~0.35 and even then only marginally. GM's polylog-free exponent is what
makes the tail work at Δ ≈ 0.28. STATUS: PROVEN (given GM).

## 4. Left tail: uncontrollable by density inputs (PROVEN — new negative)

For β ≤ 1/2−Δ, |F(ρ̄)| = |F(ρ)| and the FE gives no pointwise gain
(|ζ′(β+it)| ≪ t^{1/2−β/2+ε}L via χ′ζ + χζ′ — both terms same order, no cancellation), so

|E_out⁻| ≤ Σ_{β ≤ 1/2−Δ} (|F(ρ)|² + |F(ρ)||F(1−ρ)|) ≪ Σ_{β ≤ 1/2−Δ} t^{1−β+ε} L².

The count is #{β ≤ 1/2−Δ} = N(1/2+Δ,T) ≪ T^{0.478} (GM at Δ = 0.28), but the **β-distribution**
of those zeros is unconstrained by any known input: the zero-free region only excludes
β > 1 − c/log T; Shape-1 bounds at σ < 1/2 (N(0.22,T) ≪ T^{1.69}) are vacuous vs N(T) ~ (T/2π)L;
von Mangoldt is the only other constraint. Worst-case configuration (all N(1/2+Δ,T) left zeros at
β ≈ 0.22; FE partners at 0.78; consistent with every Shape-1 bound, the ZFR, and the
scale-gap-witness template in `gm-box-certifiability`):

|E_out⁻| ≳ T^{0.78}·T^{0.478}·L² = T^{1.258}·L² ≫ S₂ ~ T·L³   ⟹   E_out⁻/S₂ → ∞.

The pair identity (§5) does not help: |F(ρ) − F(1−ρ̄)|² ≤ 2|F(ρ)|² + 2|F(1−ρ̄)|² retains the
t^{1−β} term. **Conclusion: any unconditional bound on E requires the two-sided box**
|β−1/2| ≤ Δ, i.e. Route A; the box-free density route is REFUTED at the order level.
STATUS: PROVEN (modulo the standard convexity/FE pointwise bounds).

## 5. Byproduct: exact pair identity → quadratic box bound (PROVEN)

Pair zeros by the involution ρ ↔ 1−ρ̄ (shares height γ; FE closure; fixed points = on-line zeros).
Purely algebraic (F real-coefficient ⟹ F(1−ρ) = conj(F(1−ρ̄)), F(ρ̄) = conj(F(ρ))):

**E = Σ_ρ F(ρ)[F(ρ̄) − F(1−ρ)] = Σ_pairs |F(ρ) − F(1−ρ̄)|² ≥ 0.**

CHECKED NUMERICALLY: 20 random real-coefficient polynomials × random FE-symmetric zero sets,
exact to machine precision (`tools/check_pair_identity.py`). STATUS: PROVEN. RH sanity: on-line
pairs are fixed points, contribution 0 ✓.

Consequences (given the ζ″-moment ratio r′ = 3/5 from `bhb-zeta2-moment-2026-08-14.md`, UNVALIDATED):

1. **E ≥ 0 unconditionally** — the off-line correction only hurts: N* ≤ S₁²/(S₂+E) ≤ S₁²/S₂.
2. **Quadratic box bound:** with |β−1/2| ≤ Δ for all zeros, Taylor around the pair midpoint
   1/2+iγ (quadratic term cancels exactly): |F(ρ) − F(1−ρ̄)| = 2(β−1/2)|F′(1/2+iγ)| + O((β−1/2)³),
   so E ≤ 4Δ²Σ_ρ|F′(1/2+iγ)|²(1+o(1)) ≤ 4Δ²·2L²(r+r′)S₂, i.e. with Δ = b/L:
   **E/S₂ ≤ 8b²(r+r′) ⟹ b < √(0.031126/(8·0.677708)) = 0.07577.**
   vs triangle form b < 0.031126/(2√(2(r+r′))) = 0.01337 (both CHECKED, `tools/check_bhb_arithmetic.py`
   §9). ζ″-only (r′ = 0.6): b < 0.08053. The O((β−1/2)³) error sums to O(b³/L) — negligible.
3. ζ″-free ceiling of the pair form (r′ = 0): b < 0.2237 — i.e. without the ζ″-moment the box is
   only 2.2× narrower than BGSTB's b = 1/2; the claimed r′ = 3/5 is what buys the 6.6× gap.

## 6. Scripts

- `tools/check_pair_identity.py` — pair identity (20 trials, machine precision) + constants:
  slack 0.0311263, b_triangle 0.013368, b_pair 0.075770, b_pair(ζ″-only) 0.080527,
  Δ_sharp = 19/70, Δ_uniform = 17/60, GM exponent at Δ = 0.28: 0.4783.
  Run: `uv run --quiet python tools/check_pair_identity.py`.
- `tools/check_bhb_arithmetic.py` — extended §9 (pair-form box) and §10 (GM thresholds).
  Run: `uv run --quiet python tools/check_bhb_arithmetic.py` → ALL CHECKS PASS.

## 7. Corrections to the earlier draft of this file (subagent, 20:32)

The draft reached the right verdict (GAP) but its proof path had holes; corrected here:

1. **Mis-equality**: "M_off = 2Σ_{β>1/2}|F(ρ)|² (FE pairing)" — the pairing gives
   Σ_{β<1/2}|F(ρ)|² = Σ_{β>1/2}|F(1−ρ)|², NOT Σ_{β>1/2}|F(ρ)|²; |F| is not FE-invariant. The
   correct split M_off = Σ_{β>1/2}(|F(ρ)|² + |F(1−ρ)|²) keeps left-point |F|² mass in play.
2. **Vacuous "exact statement"**: the draft's bound M_off ≤ 2[W(1/2)N(T) + ∫NW′dσ] has boundary
   term W(1/2)·N(T) ~ T^{13/42+ε}L²·(T/2π)L = T^{55/42+ε}L³ ≫ S₂ — vacuous. The draft's "mass
   lives at the moving boundary" conclusion was therefore a witness heuristic, not PROVEN; the
   honest per-height treatment (§3–§4) is what actually decides the question.
3. **"b ≈ 0.0134 matches no derived constant" [flagged in draft]** — wrong: b_full =
   0.0311/(2√(2(r+r′))) = 0.013357 (CHECKED, §5). The draft predates `bhb-zeta2-moment`'s r′.
4. **"Guth–Maynard exponent (3/2)/(2−σ)" [flagged in draft]** — with the verbatim statement (§1)
   the correct numbers are 15/(3+5σ) on [7/10, 8/10] and 30/13 uniform; Ingham's Shape-2 k=5 is
   irrelevant to Route D's kill (fixed-σ blindness decides it).

The draft is preserved at /tmp/riem_m3/bhb-m3-subagent-draft-2026-08-14.md for the record.

## 8. Routing per plan gates (M4/M5/M6)

- **M2 gate:** REFUTED (M2 note) → box route requires Route C (the ζ″-moment).
- **M4 (ζ″-moment theorem):** `bhb-zeta2-moment-2026-08-14.md` is M4-in-essence; claim
  M = (3/5)L²S₂(1+o(1)); rests on `[inferred]` items (un-mollified ζ″ constant (T/2π)L⁵/5,
  MF-independence). STATUS: UNVALIDATED — first validation target.
- **M3 gate:** Route D GAP (this note); GM pinned + applied to the right tail; box need relaxed
  to b ≈ 0.0758 via the pair identity. Binding input unchanged in kind: the moving-boundary
  count N(1/2+b/L, T) = o(T log T), k<1, now at b ≈ 0.0758.
- **M5 (box attainment):** no known input certifies any fixed b at the o(T log T) level
  (Shape-1 blind PROVEN; Ingham k=5 ⇒ b ~ 3 log log T; GM Shape-1). STATUS: GATED; width 5.7×
  more attainable than pre-pair-form.
- **M6 (synthesis):** pending validation of the ζ″-moment note + M2/M3 notes.

## 9. Label summary

| claim | label |
|---|---|
| GM Theorem 1.2, (1.4), §13.1 (verbatim) | PROVEN (paper) |
| right tail killed at Δ > 19/70 by GM; E_out⁺/S₂ → 0 | PROVEN (given GM) |
| left tail uncontrollable by density inputs (worst case T^{1.258}L² ≫ S₂) | PROVEN (modulo standard pointwise bounds) |
| pair identity E = Σ_pairs\|F(ρ)−F(1−ρ̄)\|² ≥ 0 | PROVEN + CHECKED NUMERICALLY (20 trials) |
| box b_pair = 0.07577 vs triangle 0.01337; thresholds 19/70, 17/60 | PROVEN arithmetic; b CONDITIONAL on r′ = 3/5 |
| Route D (box-free density) reaches 3.11% | REFUTED |
| M5 box attainment at b ≈ 0.0758 with known inputs | INCONCLUSIVE (no such input; gated) |
