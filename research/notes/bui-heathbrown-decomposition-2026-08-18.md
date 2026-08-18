# Bui–Heath-Brown 19/27: decomposition + partial-unconditionalization assessment (synthesis)

**Agent:** general-purpose (read-only). **Date:** 2026-08-18.
**Scope:** decompose arXiv:1302.5018 ("On simple zeros of the Riemann zeta-function", Bui–Heath-Brown 2013)
into RH-essential vs control-suppliable estimates; assess partial unconditionalization; answer the
θ ≤ 6/11 sub-question; compare difficulty vs the GS-2026 diagonal (C<2) input.
**Method:** synthesis of the campaign's verified 08-14 decomposition trail
(`bhb-rh-role-2026-08-14.md`, `bhb-m6-synthesis-2026-08-14.md`, and the M1/M2/M3/M5 closures they cite),
plus `multiplicity-theorem-route.md`, `paper-finder-001.md`, `wave9-9B-short-mollifier-classification-2026-08-18.md`,
`wave-21-frontier.md`. Nothing here re-derives what those notes proved; it synthesizes and extends to the
task's specific questions. All numeric claims inherit the 08-14 verification status where noted.

---

## 0. Verdict (up front)

1. **The 19/27 shape has exactly ONE RH-essential estimate, and it is NOT a ζ′/ζ mean-value estimate.**
   Verbatim from the fetched paper text (quoted in bhb-rh-role): *"Assuming RH we have S₂ = Σ_{0<γ≤T}|B′(ρ)|².
   Note that this is the only place we need RH."* The RH-load is the qualitative identification
   1−ρ = ρ̄ for every zero (all zeros on the line). The mollified-moment evaluations (Lemma 1, residue
   theorem + functional equation + convexity), the main terms, the GLH-removal (Heath-Brown generalized
   Vaughan identity + hybrid large sieve), and the constant optimization are **already unconditional in
   the paper**. [PROVEN — verified against fetched text on 08-14.] This corrects the task framing: the
   RH-dependence does not live in RH-conditional on-line ζ′/ζ mean values; it lives in the denominator
   identification.
2. **There IS an unconditionalizable subset — the machinery — but it yields PRZZ's 0.407, not 19/27.**
   The whole S₁/S₂ + Cauchy framework runs unconditionally at a strictly smaller constant: that is
   exactly PRZZ (arXiv:1802.10521), κ* > 0.407, the unconditional record. [PROVEN — literature, per
   BGSTB remark quoted in bhb-m6 addendum.]
3. **Partial unconditionalization gives κ* ≥ (19/27)(1 − E/S₂); clearing p₀ = 0.6818 needs E/S₂ < 3.11%.**
   [PROVEN arithmetic: 1 − 0.6818·27/19 = 0.03113, from bhb-rh-role §3.] E = Σ_{0<γ≤T} F(ρ)[F(ρ̄) − F(1−ρ)],
   F = Bζ′ (the off-line reflection correction). No known input certifies E/S₂ < 3.11%: the box route needs
   a moving-boundary count N(1/2+b/L, T) = o(T log T) at width b ≈ 0.0758 (r′-dependent) — no known theorem
   certifies ANY fixed b at o(T log T) (Shape-1 families blind PROVEN; Ingham k=5 gives only b ~ 3 log log T);
   the box-free density route is REFUTED (right tail killed by GM only for fixed Δ > 19/70 ≈ 0.2714, 1.2–3.6×
   wider than needed; left tail uncontrollable by any density input). [PROVEN closures — M3/M5/M6.]
4. **So: no clean partial unconditionalization of the 19/27 shape clears p₀ today, and the wall premise
   (no unconditional simple-fraction theorem > p₀) survives this decomposition.** But the decomposition
   sharpens WHY and names the single input that would break the wall: any bound on E with E/S₂ < 0.0311.
   The 19/27 shape is a *template*: it converts ANY future box/density input directly into
   κ* ≥ 19/27·(1 − E/S₂) with zero additional RH cost. [PROVEN structure; existence of such input INCONCLUSIVE.]
5. **The θ ≤ 6/11 sub-question is a category error for this lever.** BHB already runs its mollifier at
   θ < 1/2 (optimization at θ → 1/2−), i.e. strictly shorter than 6/11 = 0.545. 6/11 is the Feng-type
   mollifier length of the **Levinson/on-line** machinery (PRZZ pushed the Feng θ from 17/33 to 6/11 via
   Kloosterman/zero-density decomposition) — a different mechanism (see §3). Shortening BHB's θ below 1/2
   degrades the constant below 19/27 and does not touch the single RH-use. [PROVEN structure; exact
   θ-dependence of the constants INCONCLUSIVE — needs Lemma 1 at general θ.]

---

## 1. Estimate-by-estimate table (RH-only vs control-suppliable)

| # | Estimate / step in 1302.5018 | RH-only? | Unconditional replacement? | Status |
|---|---|---|---|---|
| A | Cauchy reduction: N* ≥ \|ΣB′(ρ)\|²/Σ\|B′(ρ)\|²; denominator identified as S₂ = ΣB′(ρ)B′(1−ρ), i.e. 1−ρ = ρ̄ for every zero | **YES — the ONLY RH use (verbatim)** | Box (BGSTB-style \|β−1/2\| ≤ b/L): E = O(Δ·Σ\|B′B″\|); pair identity E = Σ_pairs\|F(ρ)−F(1−ρ̄)\|² → quadratic form, E/S₂ ≤ 8b²(r+r′), b ≤ 0.2237 (r′=0). Density: Route D REFUTED. | **The single target: E/S₂ < 0.0311** |
| B | Lemma 1: asymptotics of S₁, S₂ (residue theorem + FE + convexity bound ζ ≪ t^{(1−σ)/2+ε}) | no | already unconditional | PROVEN |
| C | Main terms M_{ν,1}, q = 1 (residue of ζ′/ζ at s = 1) | no | — | PROVEN |
| D | M_{ν,2}, 1 < q ≤ Λ (Siegel's theorem on exceptional real zeros) | no, but ineffective | Siegel unconditional-ineffective | PROVEN |
| E | M_{ν,3}, Λ < q ≤ y: generalized Vaughan identity (Lemma 3) + hybrid large sieve | no | **GLH fully removed** (paper's headline; replaces CGG's GLH/6th-moment input) | PROVEN |
| F | Optimization P(x) = −θx² + (1+θ)x, θ → 1/2−; S₁ ∼ (19/24)TL²/2π, S₂ ∼ (57/64)TL³/2π | no | calculus | PROVEN (19/27 is the limit shape) |
| G | Corollary κ_d ≥ 0.84665 (Montgomery 2N* ≤ Σ(m−2)(m−3)/m + Cheer–Goldston Σm(ρ) ≤ 1.3275N) | no | — | PROVEN |

**Net: 1 RH-essential estimate (row A); 0 GLH-essential (removed); the entire arithmetic core is
control-suppliable. The only input demand of the whole lever is a bound on
E = Σ_{0<γ≤T}F(ρ)[F(ρ̄) − F(1−ρ)].**

---

## 2. Mechanism-level assessment

**(a) Known unconditional replacements for the single RH-input** (each PROVEN-closed as stated):

- **Box condition** (BGSTB-style |β − 1/2| ≤ b/log T): E/S₂ ≤ 8b²(r + r′) with r = 99/1274 ≈ 0.0777 PROVEN;
  r′ (the ζ″-moment ratio) is REFUTED-as-derived = 3/5 (Gonek's theorem Σ|ζ′(ρ)|² ∼ (T/2π)ℒ⁴/12,
  arXiv:1302.5032, breaks its anchor), unknown O(1)-scale, M4-proper pending. Pair-identity ceiling:
  b ≤ 0.2237 (r′ = 0); target b ≈ 0.0758 only if r′ = 3/5 (now refuted). The binding sub-input is the
  moving-boundary count N(1/2 + b/L, T) = o(T log T) — M1 bottleneck (k < 1): no known route (Shape-1
  blind PROVEN; Ingham k=5 → b ~ 3 log log T only, useless at constant level).
- **Zero-density (Guth–Maynard 2024, arXiv:2405.20552):** kills the right tail only for fixed
  Δ > 19/70 ≈ 0.2714 — a width 1.2–3.6× larger than the needed b ∈ [0.0758, 0.2237]; the left tail is
  uncontrollable by any density input (worst case T^{1.258}L² ≫ S₂ ∼ TL³, consistent with all known
  bounds). Route D (box-free density) is REFUTED on both sides.
- **Mean-value / second-moment technology: not needed as a replacement.** S₂'s evaluation is already
  unconditional (Lemma 1, residue machinery; short mollifier θ < 1/2, within Montgomery–Vaughan range).
  The missing object is the **off-line weighted discrete moment** Σ_{β≠1/2}|B′(ρ)|² (or |B′B″| variant);
  no unconditional bound on it exists in the literature read this session (absence-of-evidence —
  INCONCLUSIVE, not a proof of impossibility). Crucial: this is a SHORT-mollifier object, so it is NOT
  the wave9-9B trap — that trap (Bettin–Gonek/Farmer "θ = ∞ ⟹ RH") is the LONG-mollifier second moment,
  at-least-as-hard-as-RH. The BHB second moment itself is not the RH-hard object; the zero-completeness
  correction is.

**(b) What each partial input would give (proportion):**
- The answer is a clean function, not a single number: **κ* ≥ (19/27)(1 − ε) with ε = E/S₂**; the
  p₀-threshold is ε < 0.0311. [PROVEN arithmetic.]
- Published evidence that the substitution mechanism is real (at the pair-correlation level, NOT yet at
  the BHB discrete-moment level): BGSTB (arXiv:2306.04799): box b = 1/2 → **61.7%** [PROVEN]; 
  Goldston–Suriajaya (arXiv:2603.28104, 2026): box b → 0 → **≥ 2/3, on the critical line** [PROVEN].
  Transferring the box-substitution from pair-correlation to the BHB discrete-moment level is exactly
  the open step (BGSTB's strong-ZDH — a moving-boundary hypothesis, unconditional status open — is the
  input type that would certify it).

**(c) Harder / easier than the GS-2026 diagonal input (C < 2)?** [CONJECTURED comparison — no formal reduction]
- **Comparable, structurally.** GS-2026 needs an unconditional diagonal count Σ_{γ=γ′}1 ≤ (C+o(1))N with
  C < 2 (campaign records ≈ need C ≤ 1.3265); the diagonal is on-line-sensitive (Montgomery: diagonal =
  Σ m_ρ under RH). BHB-removal needs E/S₂ < 3.11% — a box/density-weighted off-line moment. Both are
  counting inputs at the current-technology boundary; both have PROVEN walls against classical tools
  (no C<2 despite the wave-10/GM sweep; BHB: Shape-1 blind + Ingham k=5). Operationally equivalent
  dead-ends until a new counting technology exists.
- **Asymmetry in BHB's favor (structural):** the BHB target is *cleaner* — one explicit weighted sum
  over off-line zeros, with an internal mechanically-checkable step (M4-proper pins r′, upgrading or
  refuting the exact box target) that costs no compute. GS-2026 has no analogous internal step.
- **Asymmetry in GS-2026's favor (payoff):** C < 2 buys BOTH simple ≥ 2−C AND on-line ≥ 2−C with a
  single input; the BHB template buys only the simple fraction, and its slack budget (3.11%) is tight.

---

## 3. Mollifier-length sub-question (θ ≤ 6/11) and published partial results

- **Origin of 6/11:** 6/11 = 0.5454… is the Feng-type mollifier length of the Levinson/on-line machinery.
  PRZZ (arXiv:1802.10521) pushed the admissible Feng θ from 17/33 to 6/11 via Kloosterman-sum/zero-density
  decomposition, yielding 41.72% on-line (simple-on-line ≈ 0.407, the unconditional record).
  [PROVEN — multiplicity-theorem-route.md, paper-finder-001.md.]
- **Interaction with BHB:** BHB uses θ < 1/2 (optimization at θ → 1/2−); 6/11 > 1/2. The 19/27 mechanism
  ALREADY runs at θ < 1/2 < 6/11 with its mollifier unconditionally handled; running at strictly shorter θ
  only shrinks the constant, and the single RH-use (row A) is θ-independent. The campaign-frontier phrasing
  "Guth–Maynard-supplied mollifier θ past 6/11" targets the Levinson/PRZZ line (multiplicity-theorem
  Theorem C: extend Feng θ beyond 6/11 to push simple-on-line past 0.4075), NOT the BHB line.
  [PROVEN structure; exact θ-dependent constant curve INCONCLUSIVE — needs Lemma 1 at general θ.]
- **Published partial results (state of the art, verified 08-14 in bhb-m6 addendum):**
  - UNCONDITIONAL: κ* > 0.407 (PRZZ 1802.10521, record); box b = 1/2 → 61.7% (BGSTB 2306.04799);
    box b → 0 → ≥ 2/3 on-line (Goldston–Suriajaya 2603.28104, 2026).
  - RH: ≥ 2/3 (Montgomery 1973); ≥ 67.2% (Montgomery–Taylor); ≥ 67.9% (Chirre–Gonçalves–de Laat 2020);
    **≥ 19/27 = 70.37% (BHB 2013, record)**.
  - RH + GLH: 19/27 with κ_d ≥ 0.84568 (CGG 1998); κ_d ≥ 0.84665 (BHB corollary).
  - **No 2020–2026 paper claims an unconditional κ* above 0.407** (per BGSTB remark, verified 08-14).
- **Correction to the task brief:** the brief's presupposition — that BHB's RH-dependence sits in
  "RH-conditional mean-value estimates for ζ′/ζ on the critical line" — does not match the paper. The
  moments are over the mollified derivative at reflected points (S₂ = ΣB′(ρ)B′(1−ρ)), their evaluation is
  unconditional, and the single RH-use is the reflection identification. [PROVEN — verbatim quote.]

---

## 4. The single most promising partial result

**The M3 pair identity E = Σ_pairs |F(ρ) − F(1−ρ̄)|² ≥ 0 (CHECKED NUMERICALLY, 20 trials) + M4-proper
(mechanical, closed-form ζ″-moment re-derivation pinning r′) + the moving-boundary count
N(1/2 + b/L, T) = o(T log T).** This is the campaign's own M6 ranking. Honest caveat: the binding
sub-input (the k < 1 count) has NO known route and is the Type-1 one-way-door decision point (Shape-1
blind PROVEN; Ingham k=5 gives only b ~ 3 log log T; GM-family is Shape-1; a Shape-2 k<1 theorem via
GM's method is CONJECTURED-impossible — zero-detection loses a fixed log power via Littlewood–Jensen).
But M4-proper is cheap and falsifiable: it pins r′, which upgrades or refutes the exact box target
(currently b ≈ 0.0758, resting on the REFUTED r′ = 3/5). Externally, BGSTB's 61.7% and GS-2026's 2/3 are
the PROVEN existence proof that box-substitution works at the pair-correlation level — the discrete-moment
transfer is the open question, and a BGSTB-strong-ZDH-type moving-boundary hypothesis is the exact input
type that would certify the box.

---

## 5. Honesty section

**What would falsify this verdict:**
1. **Re-fetch 1302.5018 and re-verify the single-RH-use reading** (row A verbatim quote; Lemma 1 error
   terms carry no hidden zero-location input; θ → 1/2− optimization). The 08-14 session verified the
   text; I did not re-read the PDF here. [INCONCLUSIVE from this session alone.]
2. **The exact PRZZ constant:** campaign-verified κ* > 0.407 (1802.10521, per BGSTB remark); the task
   brief quoted ~0.4075. Cosmetic difference, but the precise value should be read off PRZZ's own text,
   not the second-hand remark. [INCONCLUSIVE.]
3. **r′ is unknown (O(1)-scale);** the b ≈ 0.0758 target rests on the REFUTED r′ = 3/5. If M4-proper
   finds r′ small, the required box shrinks and the barrier rises toward the 0.2237 ceiling; if r′ is
   large, the target relaxes. All "what fraction each input gives" statements inherit this uncertainty.
   [INCONCLUSIVE.]
4. **Post-2024 literature beyond what the campaign fetched:** any paper claiming unconditional
   κ* > 0.407, a Shape-2 k<1 zero-density theorem, or a C < 2 diagonal count would change the verdict.
   Check `literature-sweep-simplezeros.md` / `lit-sweep-2026-08-18.md`; I did not re-run the sweep.
   [INCONCLUSIVE — absence-of-evidence within files read.]
5. **What I could not verify from memory alone:** (i) the exact θ-dependence of the S₁, S₂ constants
   (needs Lemma 1 at general θ); (ii) whether 6/11 appears anywhere in 1302.5018 — I found no trace, and
   it is a Levinson/Feng number, but "no trace in my reads" ≠ "absent from the paper"; (iii) the Gonek
   Σ|ζ′(ρ)|² ∼ (T/2π)ℒ⁴/12 anchor (arXiv:1302.5032) — campaign-verified 08-14, cited second-hand here;
   (iv) the GS-2026-vs-BHB difficulty comparison is CONJECTURED, not reduced.

**Label map:** all claims traceable to bhb-rh-role / bhb-m6 / bhb-lemmaN / bhb-route-gap-table /
bhb-zeta2-moment (08-14, fetched-text verified) = PROVEN; the θ ≤ 6/11 interaction, the GS-2026
comparison, and the "cleaner target" asymmetry = CONJECTURED; exact constants (PRZZ value, r′, Gonek
anchor re-read) = INCONCLUSIVE. No fabricated numbers, lemmas, or estimates.
