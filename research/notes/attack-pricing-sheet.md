# Attack: E5.3 — the pricing sheet for hypothetical inputs (shadow prices of m₃, min-gap, beyond-1 F)

**Agent:** EXECUTIONER (resource-allocation + opportunity-cost + epistemology lens)
**Vector:** E5.3 of `idea-generator-earth.md` ("Adjoint sensitivity / observation impact: the pricing
sheet for hypothetical inputs"), building on the in-class LP-dual analysis of `attack-lpdual.md`
(v\* = p₁ + |E(1)|, shadow price of p₁ = exactly 1).
**Round:** 2 → recommendation for round 3.
**Compute:** `scratch/e53_pricing/pricing_sheet.py` (self-contained; canonical `tools/lpdual/` untouched —
that path belongs to the LP-dual agent). Command: `cd /home/vstaln/riemann && uv run --quiet --with numpy
--with scipy python scratch/e53_pricing/pricing_sheet.py` (output `scratch/e53_pricing/pricing_output.txt`).
Final copy of the script: `research/notes/attack-pricing-sheet.py` (alongside this note).
**Labels:** PROVEN / CHECKED NUMERICALLY / CONJECTURED / likely-DEAD as per the program's honesty
framework. Nothing here is asserted without a script behind it; every number below was produced by the
run above.

---

## 0. Verdict up front

**The ranked shopping list for round 3: only ONE hypothetical input has a positive price — the
beyond-1 form-factor RANGE (F ≡ 1 on [1, 1.03+]), priced at dv\*/dA = 0.6363/A³ per unit bandwidth (M2
model, reproduces the paper's Remark points 0.70@1.04, 0.80@1.26, 0.90@1.70 to ≤ 1.1%). The other two
candidate inputs — the third moment m₃ = 2 and any repulsion/min-gap bound — are priced NEGATIVE for
the simple-fraction certificate: each one *excludes the law* but *caps the certified constant below
0.6818* (m₃ ≥ 2 ⟹ p₁ ≤ 2/3; min-gap > 0 ⟹ p₁ = 0.50195, the Parseval floor). They cannot move the
constant up in this certificate class; hunting them for P1 is misdirected. The m₃ input is exactly
neutral for the distinct-count certificate (B = 5/6 at m₃ = 2) and its only mechanism price is −1/18
per unit (an *upper* bound m₃ < 2 would help; none is available — the computable values are m₃ = 5,
13/4 ≥ 2).**

**Epistemic status of the prices (the honest note, in advance):** the *prices are exact* — every
number is either an exact identity (m₃ = 4 − 3p₁; first-period Parseval; v\* = p₁ + |E(1)|) or a
deterministic LP/model evaluation (CHECKED NUMERICALLY, HiGHS). The *feasibility labels are the
judgment*: whether any of these inputs can actually be PROVEN about ζ is the conjectural part (beyond-1:
CONJECTURED per M29 — every proven bound fails by 3.6·10³–3.7·10⁴×; m₃: likely-DEAD per
attack-twobandwidth [TB] and paper §7.5(e); min-gap: CONJECTURED/KNOWN-OPEN per CD-V17, and priced
negative even if proven). Buying a negative-priced input is spending round-3 effort to *lower* the
certificate — the opportunity-cost error the pricing sheet exists to prevent.

---

## 1. The pricing LP (formulation, with hypothetical-constraint slots)

**The certificate class (from `attack-lpdual.md` §1, PROVEN structure in Lean).** A certificate
(c₀, r), r ∈ C¹[0,1] (piecewise-linear at knots j/256 in the LP), value v = c₀ + ∫₀¹ r(x)x dx, is valid
against a marked configuration (form-factor masses sⱼ at xⱼ = j/N, simple-point fraction p₁) iff
c₀ + Σⱼ sⱼ r(j/N) ≤ p₁. The rank–trace method certifies "proportion of simple zeros ≥ v". The N = 256
near-CUE law (rows |256·S(j) − j| ≤ 3·10⁻⁴⁰, p₀ = 0.6818286874638315) is the worst case; `ceiling_law256`
(PROVEN, Lean) gives the ceiling, and the LP attains it.

**The LP** (`build()` in the script — identical class to `tools/lpdual/lpdual_full.py`, generalized to
a parameter (rows, p₁)):
- variables: c₀, g₀..g₂₅₆ (r′ at knots), epigraph t for |Δg|;
- **validity at the pinned rows with simple fraction p₁:** c₀ + Σ_{j=1}^{255} sⱼ r(j/N) ≤ p₁ — this is
  the **p₁ slot**;
- slope budget |r′(1)| ≤ B, curvature budget ∫₀¹|r″| ≤ C, window-kernel box |r| ≤ 1 (B = C = 1, box on);
- objective: max v = c₀ + ∫₀¹ r(x)x dx (exact linear form).

**Hypothetical-constraint slots.** Each candidate input is added as a constraint on the admissible
configuration class, i.e. it changes the certified worst-case simple fraction p₁ and/or the pinned rows:

| slot | input | how it enters | what is computed |
|---|---|---|---|
| (a) | m₃ ≥ 2 | integrality identity m₃ = 4 − 3p₁ caps the class at p₁ ≤ 2/3 | v\*(p₁ = 2/3); distinct-bound price dB/dM₃ |
| (b) | min-gap X > 0 | no coincident marks ⟹ first-period Parseval forces p₁ = 0.501953125 | v\*(p₁ = 0.501953125) |
| (c) | F(1+ε) = 1+δ | beyond-1 rows are outside the certificate's support (r lives on [0,1]); the whole price flows through p₁(A), the config-side worst case | certificate-side insensitivity (LP); M2/M3 model prices of p₁(A) |

The shadow price of each constraint = how much v\* improves per unit of the input, via
dv\*/d(input) = (dv\*/dp₁)·(dp₁/d(input)) with **dv\*/dp₁ = 1 exactly** (the p₁ shadow price, PROVEN
`attack-lpdual` §3, re-verified in §2 below).

---

## 2. Baseline (re-verification, CHECKED NUMERICALLY)

`v\*(p₁) = p₁ + |E(1)|` with |E(1)| = 1/(6·256²) = 2.5431315104·10⁻⁶, at every tested p₁
(0.6818, 0.65, 2/3, 0.70, 0.80, 0.90, 1.00): identity residual ≤ 2.2·10⁻¹⁶. Anchor:
v\*(p₀) = **0.681831230595** (diff 0.00e+00 vs `attack-lpdual`'s 0.6818312306). The slope of v\* in p₁
is exactly 1 (shadow price of the certified simple fraction).

---

## 3. Input (a): third-moment constraint m₃ ≥ 2 ("the value that would exclude the law")

**Identity (PROVEN, exact algebra; CHECKED):** for the marked class (marks ∈ {1,2}, Σ marks = N),
m₂ = 2 − p₁ and **m₃ = 4 − 3p₁**. Hence:
- m₃(law) = 4 − 3p₀ = **1.95451393761 < 2** — so m₃ ≥ 2 *does* exclude the law (matches
  `attack-nevanlinna` §4's "would separate the law");
- but m₃ ≥ 2 ⟺ p₁ ≤ 2/3: every configuration in the class {m₃ ≥ 2} has simple fraction ≤ 2/3, so the
  certified worst-case p₁ is at most 2/3, and
  **v\*(m₃ ≥ 2) ≤ 2/3 + |E(1)| = 0.6666692098 < v\*(p₀) = 0.6818312306.**

**Price for the simple-fraction certificate: NEGATIVE.** dv\*/dm₃ = (dv\*/dp₁)(dp₁/dm₃) =
1·(−1/3) = **−1/3 per unit m₃** (from the exact identity, valid where the cap binds). The input that
"excludes the law" excludes the certificate's 0.6818 constant with it: the law is the *maximal*-p₁
member of the class, and the constraint that forbids it also forbids every p₁ > 2/3 configuration.

**Price for the distinct-count certificate (the P2 home of the third moment).** The moment-weight LP
(ψ(m) = a m + b m² + c m³ + d 1_{m=1} ≤ 1, maximize B = a M₁ + b M₂ + c M₃ + d s₁, s₁ ≥ 2/3):
- B(1, 4/3, 2) = **5/6 = 0.833333333 exactly** (PROVEN `attack-twobandwidth`; LP coefs
  (a,b,c,d) = (+0.8583, −0.1875, +0.0042, +0.3250));
- **the cubic-weight LP is UNBOUNDED at every M₃ ≠ 2** (HiGHS status 3; extends `attack-twobandwidth`
  §3.3 — the third-moment term has no finite price in the raw LP; it degenerates off the measure-zero
  flat point M₃ = 2);
- the only *proven* mechanism (the admissible-cubic template, `attack-twobandwidth` §3.2) prices M₃ at
  **dB/dM₃ = −1/18 per unit** (B = 43/54 + (2m₂ − m₃)/18): an *upper* bound m₃ < 2 − 18Δ would move the
  distinct bound up by Δ, but the computable values (m₃(1/2) = 5, m₃(2/3) = 13/4 — corrected per
  `attack-twobandwidth`) are all ≥ 2 and give B = 41/54 = 0.7593, 0.8071 < 5/6.

**Feasibility: likely-DEAD.** Paper §7.5(e): odd moments do not lower Λ₁(0) (on-line functional);
the distinct functional is open but the corrected m₃ values are all ≥ 2, so no usable upper bound
exists in the Rudnick–Sarnak range (TB §3.2/§4).

---

## 4. Input (b): repulsion / min-gap bound of strength X

**Toy model (exact, no LP needed):** a min-gap of strength X > 0 forbids coincident marks (two marks at
the same position — gap 0 < X). The near-CUE rows force, by the exact first-period Parseval identity,
Σₓ mₓ² = (N² + Σ_{j=1}^{255} j)/N = (65536 + 32640)/256 = **383.5** (any positions, PROVEN/CHECKED).
With no coincidences, Σₓ mₓ² = Σᵢ mᵢ² = N(2 − p₁), hence
**p₁ = 2 − 383.5/256 = 0.501953125 exactly** (= the Parseval floor 1/2 + 1/(2N), `attack-f1curve` §4).

**Certificate at the min-gap-forced p₁: v\* = 0.5019556681** (= p₁ + |E(1)|), DOWN from 0.6818312306 by
**0.179876**.

**Why the direction is negative (the non-obvious finding):** the law's p₁ = 0.6818 is *paid for by
coincident marks* — coincidence excess = Σₓmₓ² − Σᵢmᵢ² = 383.5 − 337.4519 = **46.0481** at p₁ = p₀
(positive, as required; `attack-f1curve` §3a). In general the rows force coincidence excess =
256·p₁ − 128.5, which is positive for every p₁ > 0.50195. So the certificate class that pins 0.6818 is
**structurally built on coincidences**: the repulsion input does not "exclude the crystal" (P1.4's hope)
— it excludes the *entire* p₁ > 0.502 part of the class, crushing the certified constant to the floor.
For stronger gaps (X ≥ 2 cells) the floor p₁ ≥ 0.50195 still bounds the class (f1curve LB); no gap can
raise the constant in the marked model.

**Price: a step of −0.1799 at X = 0⁺** (the marginal price per unit X is a Dirac: any positive gap
collapses the certificate to the floor). Feasibility of the input itself: CONJECTURED / KNOWN-OPEN
(CD-V17 — no proven unconditional min-gap bound for ζ zeros at the required scale), and — the point of
the pricing sheet — **negative even if proven**. Funding a repulsion proof for P1 is the canonical
opportunity-cost error: it can only lower the certificate.

---

## 5. Input (c): beyond-1 form-factor value F(1+ε) = 1+δ

**Certificate-side insensitivity (CHECKED NUMERICALLY).** The beyond-1 rows (j > 256) are outside the
certificate's support r ∈ [0,1]; perturbing row j\* = ⌈(1+ε)N⌉ to j\*(1+δ)/N² leaves v\* unchanged
(0.681831230595 at δ ∈ {−0.5, 0, 0.5, 1} for ε ∈ {0.02, 0.50}). The row *values* at j ≥ 1 never enter
v\* directly; the entire price flows through the certified worst-case simple fraction p₁(A)
(`attack-lpdual` §5: "the only datum that moves v is p₁"; `attack-f1curve` §1: "the curve IS p₁(A)").

**The price of the RANGE (M2 model, `attack-f1curve` §4):** p₁(A) = 1 − (1−p₀)/A² ⟹
**dv\*/dA = 2(1−p₀)/A³ = 0.6363/A³ per unit bandwidth** (0.6363 at A = 1, 0.5657 at A = 1.04,
0.3181 at A = 1.26, 0.1295 at A = 1.70). Bandwidths needed: **0.70 → A = 1.030; 0.80 → A = 1.261;
0.90 → A = 1.784** (vs the paper's Remark 1.04 / 1.26 / 1.70 — the mid point exact, endpoints within
0.08, p₁ errors +0.8% / −0.1% / −1.1%, all ≤ 1.1%; reproduces `attack-f1curve`).

**The price of a single VALUE δ at 1+ε (M3 free-mass model):** dp₁/dδ = (1−p₀)·j\*/98176 per unit δ
(second-period twisted-Parseval total N·Σₓmₓ² = 98176): **8.49·10⁻⁴ at ε = 0.02 (j\* = 262)**,
1.04·10⁻³ at ε = 0.25, 1.24·10⁻³ at ε = 0.50, 1.58·10⁻³ at ε = 0.90. Moving the constant by +0.01 via
a *single* point needs δ ≈ 11.8 (ε = 0.02); moving it to 0.70 needs δ ≈ 21.4 (= 0.0181713/8.490964·10⁻⁴,
derived from the printed values) — i.e. F(1.02) ≈ 22, which contradicts the pair-correlation
value F = 1 beyond 1. **Single-point values are priced, and the price says they are the wrong unit to
hunt: the RANGE [1, 1+ε] is what pays.**

**Feasibility wall (twisted-Parseval budget, `attack-f1curve` §3c):** pinned second-period mass
Σ_{j=N}^{M}j + δ·j\* ≤ 98176. δ = 0 gives the bandwidth-2 wall A_max = 511/256 = 1.9961; δ = 1 at
j\* = 262 costs one row (A_max 1.9922); δ = 20 costs 11 rows (A_max 1.9531). So δ > 0 eats bandwidth —
a large bump beyond 1 *shrinks* the reachable range (and contradicts F = 1), a small δ ≈ 0 (F ≡ 1
continued) is the realistic input, priced by the M2 range curve.

**Feasibility of the input: CONJECTURED (M29).** Every proven bound on the off-diagonal prime-pair sum
fails the certificate's tolerance by 3.6·10³–3.7·10⁴× (measured, T = 10⁴–10⁶); the only inputs that
clear it are *values* (Hardy–Littlewood / Montgomery pair-correlation F = 1 beyond 1, or HL*(k₀, λ)) —
all conjectural. The Remark roadmap (0.70/0.80/0.90 at 1.04/1.26/1.70) is PROVEN-as-stated in the paper
but its *content* is exactly this conjectural value territory.

---

## 6. The ranked table (all code-cited to `pricing_sheet.py`, run as in §header)

Baseline: v\* = p₀ + |E(1)| = **0.681831230595** (no new input).

| input | strength needed to move 0.6818 UP | v\* at that strength | shadow price per unit | feasibility |
|---|---|---|---|---|
| **(c) F(1+ε) = 1+δ, the RANGE [1,1+ε]** | A = 1.030 (M2) for 0.70 | 0.70000254 | **dv\*/dA = 0.6363/A³** (M2) | **CONJECTURED** [M29: HL/PCC values; proven bounds fail 3.6·10³–3.7·10⁴×] |
| (c) single value δ at α = 1+ε | δ ≈ 21.4 at ε = 0.02 (M3) for 0.70 | 0.70000254 | 8.5·10⁻⁴ per unit δ (M3) | CONJECTURED; δ > 0 contradicts F = 1 beyond 1 — wrong unit |
| (a) m₃ ≥ 2, simple-fraction cert | **NONE** — caps v\* at 2/3 (moves DOWN 0.0152) | 0.66666921 | **−1/3 per unit m₃** (exact identity) | **likely-DEAD** [TB; paper §7.5(e)] |
| (a) m₃, distinct-count cert | **NONE** — need an *upper* bound m₃ < 2; unavailable (values 5, 13/4 ≥ 2) | 0.83333333 (5/6, neutral at m₃ = 2); 0.75926 (m₃ = 5) | −1/18 per unit (admissible-cubic mechanism; raw LP unbounded off M₃ = 2) | **likely-DEAD** [TB] |
| (b) min-gap X > 0 | **NONE** — caps v\* at the Parseval floor (moves DOWN 0.1799) | 0.50195567 | **−0.1799 step at X = 0⁺** (exact Parseval) | CONJECTURED [CD-V17]; negative even if proven |

**Reading of the table.** Ranked by price-per-unit-of-constant-improvement: only (c)-range has a
positive price; everything else is zero, negative, or a wrong unit. The "most affordable" input per unit
of constant improvement is therefore (c)-range by default — but its *procurement* cost is the
millennium-grade Hardy–Littlewood problem (M29), so "affordable in price" does not mean "affordable in
effort": the table prices the *value* of the inputs, not the cost of proving them.

---

## 7. Round-3 recommendation (resource allocation + opportunity cost)

**Available resource (s4h-resource-allocation-analysis):** the round-3 hunting budget for new inputs to
the 0.6818 certificate — one scarce pool shared by P1 (beyond-1 / simple fraction), P2 (third moment /
distinct count), P3 (repulsion).

**Competing claims and their prices (this sheet):**
1. **Beyond-1 form-factor RANGE (P1): the only positive-priced claim.** dv\*/dA = 0.6363/A³ (M2);
   +0.0182 of constant for A = 1.03; roadmap 0.70/0.80/0.90 at 1.04/1.26/1.70 (paper Remark,
   PROVEN-as-stated; reproduced by M2 to ≤ 1.1%). Feasibility CONJECTURED (M29: value-territory only —
   HL / Montgomery pair-correlation / HL*(k₀,λ)).
2. **Third moment (P2): priced neutral-to-negative and likely-DEAD.** Simple-fraction cert: −1/3 per
   unit m₃ (caps at 2/3). Distinct cert: neutral (5/6) at m₃ = 2, −1/18 per unit for an upper bound
   that does not exist (corrected m₃ = 5, 13/4). TB: no window beats 5/6; §7.5(e): odd moments don't
   lower Λ₁(0). **Do not fund for the simple-fraction certificate.**
3. **Repulsion/min-gap (P3): priced NEGATIVE even if proven** — the near-CUE rows force the
   coincidences that pay for p₁ = 0.6818; a gap crushes the constant to the 0.502 floor. This retires
   P1.4's "repulsion would break the ceiling" hope at the toy level with an exact computation.
   **Do not fund for this certificate.**

**Allocation (ranked budget):** fund the beyond-1 range hunt (P1) — and, within it, the *range*
[1, 1.03+] (F ≡ 1 continuation), not single-point values (per the M3 price a single point is worth only
~8.5·10⁻⁴ of certified constant per unit δ, and δ > 0 is physically excluded by F = 1 beyond 1). Record
m₃ and min-gap as documented negatives with their prices; re-fund them only if a new *mechanism* (not a
new value) appears — e.g. the admissible-cubic transfer to λ < 1 (TB §3.3, OPEN) or a repulsion
statement that acts on a *different* functional than the simple-fraction certificate.

**Opportunity cost (s4h-economics-opportunity-cost):** the next-best use of the round-3 budget is the
beyond-1 hunt; every unit spent on m₃ or min-gap for the simple-fraction certificate is a unit *not*
spent there, with a negative marginal return on the certificate. Inaction is also a choice: not funding
the beyond-1 hunt costs the 0.70/0.80/0.90 roadmap, which is unreachable by any other input.

---

## 8. Honest labels and epistemic status (s4h-epistemology)

| Claim | Label |
|---|---|
| v\*(p₁) = p₁ + |E(1)|, shadow price of p₁ = 1; anchor 0.6818312306 | **CHECKED NUMERICALLY** (LP, HiGHS; reproduces `attack-lpdual` to 0.00e+00) |
| m₃ = 4 − 3p₁, m₂ = 2 − p₁ for the marked class; m₃(law) = 1.954514 < 2; m₃ ≥ 2 ⟹ p₁ ≤ 2/3 | **PROVEN** (exact algebra; CHECKED) |
| v\*(m₃ ≥ 2) ≤ 2/3 + |E(1)| = 0.66666921; price −1/3 per unit m₃ | **PROVEN** (from the identity + the v\* identity) |
| B(1, 4/3, 2) = 5/6 exactly; cubic-weight LP unbounded off M₃ = 2 | **CHECKED NUMERICALLY** (LP, HiGHS status 3); 5/6 PROVEN (`attack-twobandwidth`) |
| admissible-cubic price dB/dM₃ = −1/18; B(1,13/6,5) = 41/54, B(1,31/18,13/4) = 0.80710 | **PROVEN** (arithmetic, `attack-twobandwidth` §3.2) |
| Parseval: Σₓmₓ² = 383.5; coincidence excess at p₀ = 46.0481; no-coincidence ⟹ p₁ = 0.501953125 exactly | **PROVEN** (exact identities; CHECKED) |
| v\*(min-gap) = 0.50195567, step −0.1799 at X = 0⁺ | **PROVEN** (identity chain + v\* identity) |
| beyond-1 rows outside the certificate's support; row values irrelevant to v\* | **CHECKED NUMERICALLY** (LP, all δ) |
| M2 price dv\*/dA = 0.6363/A³; bandwidths 1.030/1.261/1.784 for 0.70/0.80/0.90; Remark reproduced to ≤ 1.1% | **CHECKED NUMERICALLY** (model evaluation; reproduces `attack-f1curve`) |
| M3 price dp₁/dδ = 8.5·10⁻⁴/unit at ε = 0.02; δ ≈ 21.4 for +0.0182 at a single point | **CHECKED NUMERICALLY** (model evaluation; the δ ≈ 21.4 value is the derived ratio of printed numbers) |
| twisted-Parseval wall: A_max = 1.9961 (δ = 0), shrinks with δ | **PROVEN-BY-ARGUMENT / CHECKED NUMERICALLY** (`attack-f1curve` §3c) |
| Feasibility: beyond-1 = CONJECTURED; m₃ = likely-DEAD; min-gap = CONJECTURED, negative if proven | **JUDGMENT** (labels from M29 / TB / CD-V17 — the conjectural part, kept separate from the exact prices) |
| Whether a no-coincidence (or m₃ ≥ 2) marked configuration satisfying all 255 near-CUE rows exists | **OPEN** (config-LP feasibility; the authors' certificate file is not public). The certificate *cap* (v\* ≤ 0.502 + |E(1)|, v\* ≤ 2/3 + |E(1)|) holds either way — if the class is empty, the cap is vacuous and the negative stands a fortiori |

**Weakest links (justification chain, made explicit):** (i) the M2/M3 curves of p₁(A) are models
(CONJECTURED — the exact p₁(A) needs the authors' configuration LP over 256-periodic marked
configurations, whose witness `cert_N256_blk_b128m.json` is not public; same blocker as
`attack-f1curve`); (ii) the law's positions are documented in `LawN256.lean` but the certificate file is
absent — the identities here use only the *documented* marks structure (∈ {1,2}, Σ = N) and p₀, so the
prices are robust to the missing file; (iii) the feasibility labels are judgments, not computations —
any future *proof* of a beyond-1 value, a third-moment bound, or a repulsion bound re-opens its row of
the table at the stated price.

---

## 9. Bottom line and persistence note

1. **The pricing sheet is computed and ranked.** Only the beyond-1 form-factor RANGE has a positive
   price (0.6363/A³ per unit bandwidth, M2; Remark roadmap reproduced to ≤ 1.1%). It is the round-3
   fund target.
2. **m₃ and min-gap are documented negatives at the pricing level** — each excludes the law and caps
   the certificate *below* 0.6818 (exact identities, PROVEN): m₃ ≥ 2 ⟹ p₁ ≤ 2/3; min-gap > 0 ⟹
   p₁ = 0.50195. The E5.3 "ranked budget" answers: a unit of third-moment data is worth −1/3 of the
   certified constant (or neutral-to-negative on the distinct bound); a unit of min-gap is worth
   −0.1799 (a step at zero); a unit of beyond-1 *bandwidth* is worth +0.6363/A³ (and a single beyond-1
   *value* only +8.5·10⁻⁴).
3. **Honest note, repeated:** the prices are exact (identities + LP/model evaluations, all
   code-cited); the feasibility labels are the judgment (CONJECTURED / likely-DEAD per M29, TB,
   CD-V17, paper §7.5(e)). The prices do not depend on which feasibility label is right; the round-3
   allocation does.
4. **Persistence:** this closes E5.3 as a deliverable with a ranked budget, not as a stop. The 0.6818
   ceiling stands; the search for the beyond-1 input (the only positive-priced one) continues to be
   the Hardy–Littlewood / Montgomery-pair-correlation wall (M29). Documented negatives with exact
   prices are results — the m₃ and min-gap lines of the table are now priced, so any future proof of
   such an input can be slotted in at its stated price without re-running the analysis.

*Sources: `attack-lpdual.md` (LP-dual, p₁ shadow price 1), `attack-nevanlinna.md` (m₃ identity,
m₃(law) = 1.9545), `attack-twobandwidth.md` (corrected m₃ values; 5/6 distinct wall; unbounded cubic
LP), `attack-f1curve.md` (M2/M3 curves, Parseval floor, bandwidth-2 wall, Remark reproduction),
`attack-m29.md` (beyond-1 feasibility), `idea-generator-earth.md` E5.3 (task), P1.4 in
`idea-generator-physics.md` (repulsion framing). Code: `scratch/e53_pricing/pricing_sheet.py`
(final copy `research/notes/attack-pricing-sheet.py`); output
`scratch/e53_pricing/pricing_output.txt`.*
