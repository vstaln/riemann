# GM-bandwidth joint — does BDH (mean-square) + Goldston–Montgomery yield a POINTWISE-in-α bandwidth-(1+δ) gain?

**Agent:** BUILDER (literature-reduction check, no compute).
**Task:** Execute Candidate B's one uncertain joint (ihara-reverse-transfer-2026-08-14.md §3): does the
Goldston–Montgomery equivalence (in its proven mean-square form) transfer a pointwise-in-α extension of the
pair-correlation form factor F(α) beyond α=1, using Barban–Davenport–Halberstam as the prime-side datum?
**Date:** 2026-08-14. **Status:** reduction complete; joint resolves to **δ = 0** (see §5–§6).

---

## 0. Verdict up front (3 lines)

1. **Joint does NOT close.** GM87 is a *variance-to-variance* (L²-to-L²) equivalence whose zero-side object is a
   **weighted integral** ∫F(α)·sinc²(παUρ)dα — not F(α) pointwise; and each side of the equivalence is itself
   equivalent to Montgomery's pair-correlation conjecture (CCCM). It supplies **no unconditional datum at all**.
2. **BDH is the wrong object and the wrong range.** It is an L²-over-moduli datum valid only for log-power moduli
   Q ≤ x/log^A x (saving x²/log^A x). The band (1, 1+δ] pointwise requires prime/AP data at fixed-power scale
   (modulus ~ x^{1−δ}); BDH's log-power range certifies only **δ = A·log log x/log x → 0**.
3. **Verdict: ABANDONED for fixed δ > 0** (the unconditional prime-side route gives δ = 0, honestly). The fixed-δ
   version needs Hardy–Littlewood/Elliott–Halberstam-strength input — **CONJECTURED**, and already the subject of
   `beyond1-conditional-program.md`. No new lever.

---

## 1. The precise lemma (Candidate B, formalized)

Let the certificate test function ψ have Fourier support in [−1−δ, 1+δ], δ > 0, and let the beyond-1 contribution
of the form factor be the linear functional

```
L(ψ; F) := ∫_{1}^{1+δ} (F(α) − 1) · |ψ̂(α)|² dα .
```

The two-moment certificate ceiling is a variational problem **pointwise in α**: the clean ceiling (M2 model,
`beyond1-conditional-program.md` §1) is

```
v*(1+δ) = p₁(1+δ) + |E(1)| ,  p₁(1+δ) = 1 − (1−p₀)/(1+δ)² ,
```

and it is attained iff L(ψ; F) = 0 for the extremal ψ, i.e. iff **F(α) = 1 pointwise on [1, 1+δ]** (value datum).

**Lemma (B), the two readings.**

- **(B-pointwise)** F(α) = 1 on [1, 1+δ] pointwise ⟹ v* = p₁(1+δ) + |E(1)| > 0.6818. — *input* CONJECTURED
  (Montgomery PCC / Hardy–Littlewood); mechanism PROVEN (lpdual, pricing).
- **(B-mean-square, the joint)** If only an L² datum ‖F − 1‖_{L²(1,1+δ)} ≤ η is available, then by Cauchy–Schwarz
  |L(ψ; F)| ≤ η · ‖|ψ̂|²‖_{L²(1,1+δ)}, and the certified value is
  **v* ≥ p₁(1+δ) + |E(1)| − η·‖|ψ̂|²‖₂/∫ψ²** (normalized). A strict gain over 0.6818 requires
  **η < δ·(1−p₀)·(∫ψ²/‖|ψ̂|²‖₂)·(1 + o(1))** — i.e. η must vanish *on the fixed window (1, 1+δ)*, not merely on a
  growing band.

**The joint to settle:** does BDH supply η = η(δ) with η(δ) → 0 for some fixed δ > 0? **Answer: no (§5–§6).**

---

## 2. Goldston–Montgomery 1987 — precise statement (mean-square in which variable)

Source: held note `attack-gm-variance.md` §3, quoting Goldston's notes `research/papers/goldston-2004-paircorr-notes.pdf`
§9 (GM87 Theorem 7) and (9.3). **On RH**, the following two **variance** asymptotics are equivalent (each ⟺ the other):

- **Zero side (mean-square in the height t):** the number variance
  ∫₀ᵀ (Δ_U S(t))² dt ~ (T/π²)·log(2 + UL), equivalently (Parseval identity (7.10))
  **V(U) = (diag) + (U²ρ²/T)·∫₋∞^∞ sinc²(πα·Uρ)·F(α) dα − (Uρ)²** — a *weighted low-pass integral* of F, weight
  sinc²(παUρ) of width 1/(Uρ), ρ = (1/2π)log(T/2π).
- **Prime side (mean-square in the shift x):** ∫₁ˣ (ψ(x+h) − ψ(x) − h)² dx ~ h·X·log(X/h) for 1 ≤ h ≤ X^{1−ε}
  ((9.3)); equivalently I(x,δ) := ∫₁ˣ(ψ((1+δ)x) − ψ(x) − δx)² dx ~ (1/2)δX²log(1/δ) for X^{−B₂} ≤ δ ≤ X^{−B₁}
  (Theorem 7, with the height-range dictionary T ∈ [X^{B₁}log⁻³x, X^{B₂}log³x]).

**Key structural facts (all from the held sources):**

1. **Both sides are L².** The zero side is mean-square in the height t; the prime side is mean-square in the shift
   x. There is **no pointwise-in-α statement anywhere in GM87**.
2. **The zero-side L² object does not determine F pointwise.** V(U) is a weighted integral of F against a fixed
   low-pass window; F can be redefined on a null set — or concentrated arbitrarily on (1, 1+δ) with the integral
   unchanged — so no family of variance values recovers F(α) for any α. (PROVEN, elementary.)
3. **GM87 is an equivalence, not a datum.** CCCM (held: `attack-gm-variance.md` §3 row 7) states the *asymptotic of
   each* of the three equivalent integrals is **equivalent to Montgomery's pair-correlation conjecture**. So GM87
   transfers a conjecture, not a theorem: it gives no unconditional content on either side.

---

## 3. Barban–Davenport–Halberstam — precise statement and the log-saving

**BDH (classical; [inferred] standard form, not re-fetched this session — exact A-dependence marked):**
for Q ≤ x/(log x)^A,

```
Σ_{q ≤ Q} Σ_{a mod q, (a,q)=1} |ψ(x; q, a) − x/φ(q)|²  ≪_A  x²/(log x)^A ,
```

with ψ(x;q,a) = Σ_{n ≤ x, n ≡ a (q)} Λ(n). **Saving: x²/log^A x; modulus range: Q ≤ x/log^A x (log-power).**

Two facts that close the joint:

- **BDH is mean-square over the modulus q and residue a** — an L² datum in (q, a), *not* in the GM shift variable x,
  and *not* pointwise in the gap h. It is the average-twin-prime datum summed over the divisor-type weight
  Σ_{q ≤ Q, q | h} 1/φ(q), i.e. control of the pair correlation **on average over all h ≤ x** with a log saving —
  a *global* (all-α) mean-square, not a bound on the fixed window (1, 1+δ).
- **Log-power range cannot reach fixed-power short intervals.** The AP-modulus ↔ gap dictionary is q ~ x/h (with
  log corrections per GM87 Theorem 7). Modulus q ≤ x/log^A x reaches gaps h ≥ log^A x, i.e. bandwidth
  δ = log h/log x ≥ A·log log x/log x. **Fixed δ > 0 needs h ≍ x^δ, i.e. modulus q ~ x^{1−δ}** — far beyond the
  BDH range. (Dictionary [inferred] standard; exact exponents carry GM87's log-corrections, but the *qualitative*
  log-power-vs-fixed-power split is robust.)
- **(Completeness, Bombieri–Vinogradov.)** BV is *proven* with a fixed-power modulus Q ≤ x^{1/2}/log^B x, but it is
  the **wrong functional** (L¹-over-q / sup-over-a), while the GM prime side is an L²-over-x variance; the
  AP → pair-variance transfer is not lossless, so BV does not supply the prime variance either. The only AP datum
  with the matching L² structure is BDH, and it is log-power. (PROVEN-as-known; [inferred] transfer loss.)

---

## 4. The normalization trade with ∫ψ² (what the BDH saving buys, exactly)

Certificate normalization (ihara-reverse-transfer (*) and the paper Prop 5.6): the value is
cert(g) = 1 − (1/∫ψ²)²·∫ g(u)Ψ₂(u)² du, and the beyond-1 term enters O₁ with the form-factor integral normalized
by ∫ψ². Concretely:

- **Gain from bandwidth δ:** added mass of |ψ̂|² on [1, 1+δ] normalized by ∫ψ² — of order δ for admissible ψ, giving
  the M2 lift p₁(1+δ) − p₀ ≈ 2(1−p₀)δ + O(δ²).
- **Error from an L²-only datum:** ≤ η·‖|ψ̂|²‖_{L²(1,1+δ)}/∫ψ². To beat the in-class ceiling the error must be
  strictly below the gain, i.e. **η must vanish on the fixed window (1,1+δ)**.

BDH's saving x²/log^A x translates (through the GM mean-square dictionary) into an L² mass that is o(1) on the
**growing band** [0, R] with R → ∞. That is **compatible with F − 1 being O(1) on the fixed window (1, 1+δ)** —
L²-o(1) on a growing band does not localize to a fixed window (the mass can be concentrated exactly there). Hence
the normalization trade certifies **nothing fixed**: η(δ) is not o(1) for any fixed δ > 0, and no margin opens.
(PROVEN.)

---

## 5. The δ — honest value

| Reading of the transfer | Bandwidth δ certified by BDH | Label |
|---|---|---|
| Pointwise-in-α (what the certificate needs) | **δ = 0** (BDH has no pointwise-in-h content; it is a mean over moduli) | PROVEN |
| Mean-square (granting the full GM L² dictionary) | **δ = A·log log x/log x → 0** (log-power moduli ⟹ log-power gaps only) | PROVEN given the standard dictionary [inferred exponents] |
| Fixed δ > 0 (the 0.70/0.80/0.90 roadmap) | **not certified by any unconditional datum** — needs modulus q ~ x^{1−δ} (HL/EH-strength) | CONJECTURED input |

---

## 6. VERDICT

**ABANDONED for the unconditional claim** — "BDH ⟹ bandwidth-(1+δ) certificate ceiling > 0.6818 for some fixed
δ > 0" does not close, for two independent reasons:

1. **GM87 provides no unconditional datum** (equivalence of two L² asymptotics, each equivalent to the PCC), and its
   zero-side object is a weighted integral of F, from which pointwise F(α) — or even localized L² control of F−1 on
   (1, 1+δ) — cannot be recovered.
2. **BDH is the wrong range** (log-power moduli Q ≤ x/log^A x vs. the fixed-power q ~ x^{1−δ} needed for δ > 0) and
   its saving localizes to nothing on the fixed window.

The **conditional** fixed-δ statement (HL / Montgomery PCC / EH ⟹ p₁(1+δ) roadmap) is **CONJECTURED**, and is
already written with code-verified pricing in `beyond1-conditional-program.md` — this note does not duplicate it
(per the task's cross-check instruction).

The search is not stopped: Candidate B is re-priced from "unconditional anchor (BDH)" to "conditional value
territory (HL)", consistent with M29's proven negative and the structural-final-verdict's HARD constraint.

---

## 7. Labels

| Claim | Label |
|---|---|
| GM87 = RH-conditional equivalence of two L² variance asymptotics; zero side = ∫F·sinc²(παUρ) weighted integral | PROVEN-as-reported (held: goldston-2004 §9, `attack-gm-variance.md` §2–§3) |
| GM87 asymptotic on either side ⟺ Montgomery PCC | PROVEN-as-reported (CCCM, held: `attack-gm-variance.md` §3 row 7) |
| L²/mean-square control does not yield pointwise control (null-set / window-concentration argument) | PROVEN (elementary) |
| BDH statement + saving x²/log^A x, range Q ≤ x/log^A x | [inferred] standard classical theorem (named in `ihara-reverse-transfer` §2) |
| BDH is mean-square over (q, a); global all-h average, not fixed-window | PROVEN (from the statement's own structure) |
| Log-power moduli ⟹ δ = A·log log x/log x → 0; fixed δ needs q ~ x^{1−δ} | PROVEN given the standard AP↔gap dictionary [inferred exponents, robust qualitatively] |
| BV (fixed-power q ≤ x^{1/2−ε}) is the wrong functional for the GM prime variance | [inferred] known transfer loss; BV not re-derived |
| "BDH ⟹ bandwidth-(1+δ) ceiling > 0.6818, δ > 0 fixed" | **ABANDONED** |
| "HL/PCC ⟹ bandwidth-(1+δ) ceiling" | CONJECTURED (already in `beyond1-conditional-program.md`) |
| δ = 0 (pointwise reading); δ = A log log x/log x → 0 (mean-square reading) | PROVEN (this note, reduction) |

---

## 8. Next step

Record the closure: **the unconditional prime-side datum (BDH) is exhausted — it certifies δ = 0 and cannot move
0.6818.** The only fixed-δ route remains the conditional value territory (Montgomery PCC / Hardy–Littlewood /
Elliott–Halberstam), which `beyond1-conditional-program.md` already prices (0.6363/A³ per unit bandwidth). No new
builder lever; the structural-final-verdict HARD constraint (new unconditional p₁ > p₀ theorem) is **re-confirmed**
from the prime side. Optional follow-up for a literature agent: verify the exact A-dependence and the AP↔gap
dictionary exponent against a fetched copy of GM87/BDH (the qualitative δ = 0 verdict is independent of them).

---

## 9. Assumptions

- `[verified]` GM87 Theorem 7 / (9.3), the Parseval identity V(U) = …∫sinc²(παUρ)F(α)dα, the CCCM
  PCC-equivalence, and the in-band-only unconditional Montgomery datum — from `attack-gm-variance.md` (read this
  session), which extracts them from held papers `goldston-2004-paircorr-notes.pdf` and `cccm-2108.09258-three-integrals.pdf`.
- `[verified]` Certificate structure (M2 curve, v* = p₁ + |E(1)|, ∫ψ² normalization, pointwise-in-α variational
  problem) — from `structural-final-verdict.md` and `beyond1-conditional-program.md` (read this session).
- `[inferred]` BDH's exact statement/A-dependence and the AP-modulus ↔ gap dictionary exponent (q ~ x/h) are
  standard classical facts, cited from general knowledge, **not** re-fetched this session; the verdict's qualitative
  content (log-power vs fixed-power) does not depend on the exact exponent.
- No computation performed — the load-bearing step is a reduction (§4–§6), and per the compute discipline a numeric
  probe would not change any belief.
