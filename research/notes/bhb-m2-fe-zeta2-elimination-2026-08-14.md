# M2 — Functional-equation ζ″-elimination check: REFUTED (with the exact identity)

**Agent:** main loop (executioner in-session; subagent infrastructure failed twice — see §6).
**Date:** 2026-08-14.
**Scope:** [CF] closed-form algebra only, no compute. This is the M2 artifact of
`bhb-unconditionalization-plan-2026-08-14.md` (§3 M2; gate: success ⇒ Lemma N reduces to the box
question M5; refutation ⇒ box route needs Route C / M4).
**Sources:** bhb-unconditionalization-plan-2026-08-14.md (spec); bhb-lemmaN-firstcheck-2026-08-14.md;
bhb-route-gap-table-2026-08-14.md (M1); bhb-zeta2-moment-2026-08-14.md (companion note, claims
Route C resolved at r′ = 3/5 — separate, unvalidated).

---

## 0. One-line answer

**The functional equation does NOT eliminate ζ″.** At every zero ρ (no RH needed) the exact identity

**F(ρ̄) − F(1−ρ) = [B(1−ρ) − B(ρ̄)]·ζ′(ρ)/χ(ρ) + B(ρ̄)·δ(ρ),   δ(ρ) := ζ′(ρ̄) − ζ′(1−ρ)**

holds, and the "defect" δ(ρ) is the **ζ′-analogue of the original difference**: its leading term is
2(β−1/2)ζ″(1/2−iγ) — the same second derivative the Taylor route produces. ζ″ is not relabeled away;
it is moved from "Bζ″ with B′" to "B(ρ̄)ζ″ with weight χ(ρ)⁻¹". **Gate outcome: REFUTATION.** The box
route therefore needs Route C — the ζ″-moment theorem — which the companion note
`bhb-zeta2-moment-2026-08-14.md` claims to resolve at r′ = 3/5 (unvalidated; see §5). The one genuine
byproduct: the mollifier-deviation term is a **pure ζ′-moment term** with box-weight, and the FE pairing
gives the exact decomposition E = S₂ − Σ F(ρ)F(1−ρ), which is the cleanest form of the problem.

---

## 1. Setup (from the firstcheck note, [verified])

- F = Bζ′; ρ = β+iγ, β ∈ (1/2, 1]; ρ̄ = β−iγ; 1−ρ = (1−β)−iγ. E = Σ_{0<γ≤T} F(ρ)[F(ρ̄) − F(1−ρ)].
- B is a Dirichlet polynomial with real coefficients (mollifier): B(s) = Σ_{n≤y} b(n)n^{−s}, b(n) ∈ ℝ.
- BHB's only RH-use is 1−ρ = ρ̄ (⇒ E = 0). Removing RH = bounding E/S₂ < 0.0311 (PROVEN arithmetic).

## 2. The two exact identities [PROVEN]

**(i) Real-coefficient reflection.** ζ′ has real coefficients on ℝ (Dirichlet series Σ(log n)n^{−s}
with real coefficients, continued), so by Schwarz reflection

**ζ′(ρ̄) = conj(ζ′(ρ))** for every ρ. [PROVEN]

**(ii) Functional equation at a zero.** ζ(s) = χ(s)ζ(1−s). At s = ρ, ζ(ρ) = 0 ⇒ ζ(1−ρ) = 0 (χ has no
zeros). Differentiating:

ζ′(ρ) = χ′(ρ)ζ(1−ρ) − χ(ρ)ζ′(1−ρ) = −χ(ρ)ζ′(1−ρ),  hence  **ζ′(1−ρ) = −ζ′(ρ)/χ(ρ).** [PROVEN]

Note: this needs ζ(1−ρ) = 0 (one use of the FE at the paired point) but **no RH** — 1−ρ ≠ ρ̄ in general.

## 3. The exact FE rewriting of the difference [PROVEN]

F(ρ̄) − F(1−ρ) = B(ρ̄)ζ′(ρ̄) − B(1−ρ)ζ′(1−ρ)
  = B(ρ̄)·conj(ζ′(ρ)) + B(1−ρ)·ζ′(ρ)/χ(ρ)                      [(i)+(ii)]
  = B(ρ̄)[conj(ζ′(ρ)) + ζ′(ρ)/χ(ρ)] + [B(1−ρ) − B(ρ̄)]·ζ′(ρ)/χ(ρ)
  = **B(ρ̄)·δ(ρ) + [B(1−ρ) − B(ρ̄)]·ζ′(ρ)/χ(ρ)**,   δ(ρ) := conj(ζ′(ρ)) + ζ′(ρ)/χ(ρ).  [PROVEN]

**Consistency checks (both hold exactly):**
- Under RH, ρ̄ = 1−ρ: δ(ρ) = ζ′(ρ̄) − ζ′(1−ρ) = 0, B(1−ρ) − B(ρ̄) = 0 ⇒ difference = 0 ⇒ E = 0. ✓
- δ(ρ) = ζ′(ρ̄) − ζ′(1−ρ): by (i) ζ′(ρ̄) = conj(ζ′(ρ)) and by (ii) −ζ′(ρ)/χ(ρ) = ζ′(1−ρ). ✓

## 4. Why ζ″ is NOT eliminated [PROVEN]

δ(ρ) = ζ′(ρ̄) − ζ′(1−ρ) is the difference of ζ′ at the conjugate and FE-paired points. Both points
ρ̄ = β−iγ and 1−ρ = (1−β)−iγ sit at height **−γ**; their midpoint is **1/2−iγ**. Taylor around the
true midpoint:

δ(ρ) = (ρ̄ − (1/2−iγ))ζ″(1/2−iγ) − ((1−ρ) − (1/2−iγ))ζ″(1/2−iγ) + O((β−1/2)³)
     = (β−1/2)ζ″(1/2−iγ) − (−(β−1/2))ζ″(1/2−iγ) + O((β−1/2)³)
     = **2(β−1/2)ζ″(1/2−iγ) + O((β−1/2)³)**   [PROVEN]

(Correction, validation addendum 2026-08-14: an earlier draft expanded about 1/2+iγ, claiming
O((β−1/2)³). At that wrong center the quadratic remainder is −4iγ(β−1/2)ζ‴(1/2+iγ) — it does NOT
cancel (the points are not symmetric about 1/2+iγ) and is numerically ENORMOUS (|err| ≈ 1.35 > |δ|
at β−1/2 = 0.02, t = 1000; verified by `research/notes/check_validator_af.py`). The corrected
statement above is numerically verified (|err| = 0.0017 ≪ |δ| = 0.779 at the same point). All
modulus conclusions survive the correction because |ζ″(1/2−iγ)| = |ζ″(1/2+iγ)|.)

The (β−1/2)-coefficient of δ is exactly ζ″, with the same 2(β−1/2) weight as the Taylor route's
F′(1/2+iγ). The FE rewrite moves ζ″ from the B′·ζ′ product derivative (F′ = B′ζ′ + Bζ″) into the
conjugate-pair defect δ — same order, same weight, same object. **The second derivative is an invariant
of the problem, not an artifact of the Taylor step.** [PROVEN]

Alternative phrasing: E = S₂ − Σ F(ρ)F(1−ρ) exactly (expand F(ρ)F(ρ̄) = |F(ρ)|² using (i) and
B(ρ̄) = conj(B(ρ))). Under RH the two sums coincide; their difference is nonzero only to the extent
that ζ′(1−ρ) ≠ conj(ζ′(ρ)) — and ζ′(1−ρ) − conj(ζ′(ρ)) = −δ(ρ) is first-order in (β−1/2) with
coefficient ζ″. Any bound of E must control this first-order defect; no FE manipulation removes it.

## 5. What the FE route DOES buy (and what it costs)

**Buys (genuine, kept):**
1. **Exact structure:** E = S₂ − Σ F(ρ)F(1−ρ) — the cleanest form: the off-line correction is the
   S₂-pairing minus the FE-pairing. [PROVEN]
2. **Mollifier-deviation term is ζ′-type:** [B(1−ρ) − B(ρ̄)]ζ′(ρ)/χ(ρ) has |ζ′(ρ)|² moments (S₂-type)
   modulated by the mollifier's two-point difference |B(1−ρ) − B(ρ̄)| ≤ (1−2β)·max|B′| ≪ (β−1/2)·L^O(1)
   and by |χ(ρ)|⁻¹ = (t/2π)^{β−1/2}(1+o(1)). This is a *box-weighted ζ′-moment*: it needs a box input
   (|β−1/2| ≤ b/L on average) but NOT any ζ″-moment. [PROVEN]
3. **χ-weight is the box in disguise:** |χ(ρ)|⁻¹ = (t/2π)^{β−1/2} — so the FE route's "price" for
   dropping B′ζ′ is that ζ′(ρ)²/χ(ρ) terms carry the β-deviation in the χ weight: same information as
   the box, in exponent form. [PROVEN]

**Costs:**
4. **δ(ρ) needs ζ″-control:** bounding Σ|B(ρ̄)δ(ρ)|² requires the second moment of
   ζ′(ρ̄) − ζ′(1−ρ) — either via Taylor (⇒ Σ|Bζ″|², the Route C object, r′ = 3/5 claimed in the
   companion note, [INCONCLUSIVE until validated]) or via a new two-point ζ′-moment (no literature
   input found; [INCONCLUSIVE]). The phase of ζ′(ρ) is uncontrolled, so the two terms of the difference
   do NOT cancel in |·| — the naive bound |F(ρ̄)−F(1−ρ)| ≤ |ζ′(ρ)|(|B(ρ̄)| + |B(1−ρ)|/|χ(ρ)|) loses the
   cancellation entirely and gives E/S₂ ~ 1 + avg(t/2π)^{β−1/2}, useless (PROVEN: even β−1/2 ~ 1/L gives
   avg ~ e). [PROVEN]

## 6. Verdict and gate

**M2 verdict: REFUTED** — the FE cannot express E in terms of ζ′-moments controlled by BHB Lemma 1
without either (a) the ζ″-moment (Route C/M4 — companion note claims r′ = 3/5, transfer-level,
unvalidated) or (b) a box input of the same b ≈ 0.0134–0.05 scale (M1/M5), now visible both in the
mollifier-deviation term and in the χ-weight. ζ″ is invariant under the FE rewrite; the exact step is
§4: δ(ρ) = ζ′(ρ̄) − ζ′(1−ρ) = 2(β−1/2)ζ″(1/2−iγ) + O((β−1/2)³) (true midpoint of ρ̄, 1−ρ is 1/2−iγ; corrected 2026-08-14).

**Plan gate outcome (per plan §3 M2):** refutation ⇒ the box route needs Route C. Route C is exactly
what `bhb-zeta2-moment-2026-08-14.md` attempts (M = (3/5)L²S₂ by ζ′→ζ″ substitution into Lemma 1
machinery). **Therefore the next decision point is: validate the companion note** (adversarial
check of the ζ′→ζ″ transfer, the un-mollified constant (T/2π)L⁵/5, and MF-independence), and run
**M5** (box attainment at b ≈ 0.0134 — is any box b < 1 attainable at the BHB discrete-moment level?).

## 7. Labels

| Claim | Label |
|---|---|
| ζ′(ρ̄) = conj(ζ′(ρ)) (real coefficients) | PROVEN |
| ζ′(1−ρ) = −ζ′(ρ)/χ(ρ) at zeros (FE differentiated once) | PROVEN |
| F(ρ̄)−F(1−ρ) = B(ρ̄)δ(ρ) + [B(1−ρ)−B(ρ̄)]ζ′(ρ)/χ(ρ), δ(ρ) = ζ′(ρ̄)−ζ′(1−ρ) | PROVEN (exact identity) |
| E = S₂ − Σ F(ρ)F(1−ρ) | PROVEN |
| δ(ρ) = 2(β−1/2)ζ″(1/2−iγ) + O((β−1/2)³) | PROVEN (corrected center 1/2−iγ; earlier 1/2+iγ version had a false error term) |
| ζ″ invariant under FE rewrite (second derivative unavoidable) | PROVEN (from the two rows above) |
| Mollifer-deviation term is a box-weighted ζ′-moment (no ζ″) | PROVEN |
| |χ(ρ)|⁻¹ = (t/2π)^{β−1/2}(1+o(1)) | PROVEN (classical χ-asymptotic, Stirling) |
| Naive (phase-losing) bound is useless (E/S₂ ~ 1+e) | PROVEN |
| FE elimination SUCCEEDS | **REFUTED** |
| Companion note's r′ = 3/5 | INCONCLUSIVE (separate artifact, needs validation) |

*No computation performed — pure algebra; every step above is hand-checkable. The only external input
is the classical |χ| asymptotic (Stirling), stated with its form, not a number.*

## 8. Handoff

- **M2 done (REFUTED).** Next: (1) VALIDATOR breaks this note and the companion
  `bhb-zeta2-moment` note (adversarial, per charter); (2) M3 (density exponent gap) — the only
  remaining cheap probe before M4/M5 commitments; (3) M5 gated on M2-refutation + M3 outcome per plan
  §3 (M5: "fund only if M2 succeeds OR M4 succeeds" — with M2 refuted, M5 waits on the ζ″-moment note
  surviving validation, i.e. M4-success-in-essence; see M6 synthesis).
