# Arguin–Creighton (arXiv:2603.01711) — Mining for Certificate Inputs (P2 fourth-moment / P3 form-factor)

**Agent:** adventurer (literature recon). **Date:** 2026-08-14. **Scope:** LITERATURE ONLY — no compute, no zero-counting, no statistics over zero data (charter binding).
**Paper:** L.-P. Arguin & N. Creighton, "Lower bounds for the large deviations and moments of the Riemann zeta function on the critical line," arXiv:2603.01711v1 [math.NT], 2 Mar 2026. Fresh (2026), not previously mined in any note. PDF read in full this session via `pdftotext`.

---

## 1. What the paper proves (objects, scale, on/off line)

The paper is about the **value distribution of log|ζ(1/2+it)|** — Selberg's Central Limit Theorem at the large-deviation (variance) scale — **not** about zeros, spacings, or multiplicities.

**Objects and scale** [verified, direct text]:
- **Large deviations on the line:** measure of the level set {t ∈ [0,T] : log|ζ(1/2+it)| > V}, at scale V ~ α·log log T, α > 0. **ON the critical line** (this is the paper's advertised advance over [AB24], which only got the off-line version at σ₀ = 1/2 + δ(α)/log T).
- **Fractional moments on the line:** ∫₀^T |ζ(1/2+it)|^{2α} dt (lower bounds).
- **q-aspect (Dirichlet L):** large deviations of central values L(1/2,χ), W ~ α·log log q, and fractional moments Σ_χ |L(1/2,χ)|^{2α}.
- **Internal machinery moments:** twisted **second** and **fourth** mollified moments E[|ζM|²], E[|ζM|⁴] twisted by an "α-separable" Dirichlet polynomial Q (Proposition 3.5).

## 2. Main theorems, decomposed (hypothesis → conclusion → unconditional?)

Applying s4h-investigation claim-decomposition to each:

**Theorem 1.1** (main, on-line large-deviation lower bound).
- *Hypothesis:* α > 0; V ~ α log log T; T sufficiently large; t uniform on [0,T]; **no unproven input** (uses Paley–Zygmund + twisted 2nd/4th moments).
- *Conclusion:* meas{t∈[0,T] : log|ζ(1/2+it)| > V} ≥ K_α · (T/√(log log T)) · e^{−V²/log log T}, with K_α ≫ (Cα² log α)^{−α²} as α→∞, C absolute.
- *Status:* **PROVEN, UNCONDITIONAL.** [verified]
- *Significance stated in-paper:* removes the RH dependency in Soundararajan [Sou09, Cor. B]; restores the Gaussian-decay constant; K_α is "approximately a square worse" than the Keating–Snaith conjectured a_α g_α. [verified]

**Corollary 1.2** (fractional moments).
- *Hypothesis:* α > 0, T large.
- *Conclusion:* ∫₀^T |ζ(1/2+it)|^{2α} dt ≫ K_α T (log T)^{α²}.
- *Status:* **PROVEN, UNCONDITIONAL — but explicitly "another proof" of the sharpest KNOWN bounds of Heap–Soundararajan [HS22] / Radziwiłł–Soundararajan [RS12], "with the same constant."** [verified] Not a new record; a new route to a known bound.

**Theorem 1.3 / Corollary 1.4** (q-aspect, Dirichlet L).
- *Hypothesis:* α > 0, q large prime, W ~ α log log q.
- *Conclusion:* (1.6) large-deviation lower bound for central L(1/2,χ); (1.8) Σ_{χ even primitive} |L(1/2,χ)|^{2α} ≫ K_α (log q)^{α²}.
- *Status:* **PROVEN, UNCONDITIONAL.** [verified]

**Proposition 3.5** (twisted mollified moments — the technical core).
- *Hypothesis:* Q "α-separable" (Def 3.4, real, length ≪ T^{1/1000}); M the complete mollifier (2.17), length ≪ T^{1/1000}, truncated at T* = T^{1/(R(α²+1))}.
- *Conclusion:* ∫|ζ(1/2+it)M Q²|² ≍ T(log T/log T_J)² b(1,1) ; ∫|ζ(1/2+it)M|⁴ Q² ≪ T(log T/log T_J)⁴ b(1,1).
- *Status:* **PROVEN, UNCONDITIONAL**; derived from Heath-Brown–Conrey [HBC85] twisted 2nd moment and Arguin–Bourgade–Radziwiłł [ABR20] 4th mollified moment. [verified] → **not new machinery.**

## 3. Unconditional vs conditional status (s4h-epistemology)

| Claim | Epistemic status | Basis |
|---|---|---|
| Thm 1.1, Cor 1.2, Thm 1.3, Cor 1.4, Prop 3.5 | **Known (PROVEN, unconditional)** | Direct statement in abstract + §1.1 + §3; no RH/GLH hypothesis anywhere in the paper. [verified] |
| "Fractional-moment lower bound is a new record" | **False** — paper says "another proof… same constant" as HS22/RS12 | [verified] |
| "This feeds the certificate's P2/P3 levers" | **False (see §4)** | Inference from direction mismatch + object mismatch. [inferred from lever definitions in structural-thread note §1] |

No status-inflation risk found: the paper is internally honest about being a lower-bound re-proof (it credits HS22/RS12 for the constant and calls its own result "another proof").

## 4. Transfer table

| Statement | Certificate lever it could feed | Unconditional? | Expected strength vs 0.6818 need |
|---|---|---|---|
| Cor 1.2 at α=2: ∫|ζ|⁴ ≫ K₂ T log⁴ T | P2 (fourth-moment) | Yes | **Nil** — the raw 4th moment is already known EXACTLY (Ingham 1926: (1/2π²)T log⁴ T + O(T log³ T), unconditional); a lower bound is strictly weaker, and the P2 lever needs upper/exact (or discrete-over-zeros) control, not a lower bound. |
| Thm 1.1 large-deviation lower bound | P2 or P3 | Yes | **Nil** — value distribution of log|ζ|, no zero spacing/multiplicity content. |
| Prop 3.5 twisted 2nd & 4th mollified moments | P2 (if lever needed an unconditional twisted-4th moment) | Yes | **Nil/near-nil** — re-derives HBC85/ABR20; mollifier length ≪ T^{1/1000} and truncation T^{1/(R(α²+1))} are far below the certificate's mollifier needs; the 4th-moment bound is an UPPER bound but for a specific short-mollified, truncated object, not the lever's object. |
| Thm 1.3 / Cor 1.4 (Dirichlet L) | neither | Yes | **Nil** — different family, still lower-bound direction. |
| (any pair-correlation / form-factor statement) | P3 (form-factor) | — | **Absent** — the paper contains no Montgomery F(α), no pair correlation, no zero-spacing content. [verified negative] |

## 5. Verdict

**NO NEW INPUT to P2 (fourth-moment/distinct-zeros) or P3 (form-factor).**

Reason, in one sentence: the paper's results are all **lower bounds on value-distribution quantities** (large deviations of log|ζ|, fractional moments), whereas the certificate's two levers require (P2) **upper/exact or discrete-over-zeros moment control** and (P3) **pair-correlation/form-factor statements** — neither of which appears.

Two independent reasons the verdict is robust:
1. **Direction mismatch** [inferred from lever definitions]: distinct-zeros needs to bound Σ_ρ(m_ρ−1) from ABOVE (fewer multiplicities → more distinct zeros), which needs upper bounds on moment-like sums; this paper only produces lower bounds. Its Paley–Zygmund method *inherently* yields lower bounds.
2. **No novelty in the only moment object that intersects P2**: the fourth moment ∫|ζ|⁴ (α=2 in Cor 1.2) is already exactly known unconditionally (Ingham); the paper's α=2 lower bound is strictly weaker than classical knowledge, and the paper itself labels the fractional-moment result "another proof … same constant" as HS22/RS12. [verified]

Epistemic caveat [inferred, flagged]: I have not read `structural-final-verdict.md` / `multiplicity-theorem-route.md` this session, so my description of exactly what P2/P3 consume rests on the charter ("distinct-zeros (P2, fourth-moment) … form-factor (P3)") and the structural-thread note §1 (p₁ = simple fraction over ALL zeros; pair-correlation bounds Σ_ρ(m_ρ−1)). If the P2 lever actually consumes a *twisted/mollified* fourth moment with a sharp ratio to the twisted second moment, Prop 3.5 is a (redundant, HBC85/ABR20-derived) reference — but it would still not be a NEW input.

## 6. One concrete next step

Record this paper as **mined → negative finding** (no P2/P3 input; direction and object both mismatch), and route future 2026-paper mining toward papers containing either (a) **unconditional UPPER bounds on weighted/twisted fourth moments or discrete moments evaluated over zeros** (P2), or (b) **unconditional pair-correlation / form-factor F(α) statements** (P3) — i.e., stay on the axis already mapped in `structural-thread-newinput-2026-08-14.md` Candidates 1–3. Do not reopen this paper for P2/P3.

*No computation was performed. Every [verified] label is backed by the PDF text read this session; [inferred] labels name the evidence they rest on.*
