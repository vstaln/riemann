# Lemma N first check: is Σ|B′B″| = O(S₂) from BHB residue machinery alone, and what box Δ clears 0.6818?

**Agent:** builder (atomic research deliverable). **Date:** 2026-08-14.
**Task:** First check of Lemma N (bhb-rh-role-2026-08-14.md §5) — closed-form only.
**Sources:** hooks/agents.md; bhb-rh-role-2026-08-14.md; s4h-investigation-claim-decomposition,
s4h-logic-check (read & applied); arXiv:1302.5018 full text via ar5iv (Lemma 1 and §2 "The setup"
extracted verbatim).

---

## 0. One-line answer

**NO — not unconditionally, and not even with the residue machinery alone, because the note's
notation is wrong.** BHB's moments are not Σ|B′(ρ)|² with B′ = derivative of the mollifier; they
are **Σ|Bζ′(ρ)|²** (mollified derivative of ζ). Correcting this, the Taylor reduction needs
**F′ = B′ζ′ + Bζ″**, and the **Bζ″ cross-term produces a new moment Σ|B(ρ)|²|ζ″(ρ)|² that
Lemma 1 does not evaluate**. The part that *is* pure residue bookkeeping gives
**Σ|B′ζ′|² ~ L²·S₂**, so the *optimistic* (ζ″-free) box is **Δ(T) = b/L with b ≈ 0.05**
(diagonal-only; M₂ corrections pending). The honest verdict: **INCONCLUSIVE**, with the blocker
named exactly.

---

## 1. NOTATION CORRECTION (PROVEN, from paper text)

arXiv:1302.5018 eq. (1) and Lemma 1 state, verbatim:

- N*(T) ≥ |Σ_{0<γ≤T} **Bζ′**(ρ)|² / Σ_{0<γ≤T} |**Bζ′**(ρ)|²,
- S₁ := Σ_{0<γ≤T} **Bζ′**(ρ),  S₂ := Σ_{0<γ≤T} **Bζ′**(ρ)·**Bζ′**(1−ρ).

The mollified object is **F(s) := B(s)·ζ′(s)**, *not* the derivative of the mollifier B. The
source note (bhb-rh-role-2026-08-14.md §1 and §5) writes this as "B′(ρ)", which collides with the
true derivative of B(s) = Σ_{k≤y} b(k)/k^s. **Lemma N as literally written (B′ = d/ds B) does not
match the paper's moments, so its premise "Σ|B′(ρ)|² = S₂" is false.** Everything below uses the
correct object F = Bζ′.

---

## 2. The mollifier and its derivatives (PROVEN, closed-form)

B(s) = Σ_{k≤y} b(k)/k^s, b(k) = μ(k)·P(log(y/k)/log y), y = T^ϑ, P(0)=0, P(1)=1 [paper eq. (2)].

- **B′(s) = −Σ_{k≤y} b(k)(log k)/k^s**
- **B″(s) = +Σ_{k≤y} b(k)(log k)²/k^s**

These are the (−log k) factors the task asked for; they are harmless weights (each −log k → a
factor −ϑuL under u = log k/log y). But they enter only through the **first** piece of F′:

**F′(s) = B′(s)ζ′(s) + B(s)ζ″(s).**

The second piece, Bζ″, has **no** Dirichlet-polynomial weight structure — it is a genuinely new
object (see §4).

---

## 3. Taylor form of E (PROVEN, closed-form)

ρ = β+iγ, ρ̄ = β−iγ, 1−ρ = (1−β)−iγ. Both ρ̄ and 1−ρ sit on opposite sides of s₀ = 1/2+iγ:

**ρ̄ − (1−ρ) = 2(β−1/2) ∈ ℝ.**

Taylor at s₀ (odd term survives, even term cancels exactly):

**F(ρ̄) − F(1−ρ) = 2(β−1/2)·F′(1/2+iγ) + O((β−1/2)³·sup|F‴|),  F′ = B′ζ′ + Bζ″.**

So under a box |β−1/2| ≤ Δ:

**E := Σ_{0<γ≤T} F(ρ)[F(ρ̄) − F(1−ρ)] = 2Σ(β−1/2)F(ρ)F′(1/2+iγ) + O(Δ³·…)**
**|E| ≪ Δ·Σ_{0<γ≤T}|F(ρ)||F′(1/2+iγ)| + O(Δ³).**

(Note the exact factor 2 — it must be kept in any explicit Δ.)

---

## 4. The Cauchy–Schwarz reduction — and where it breaks

Cauchy–Schwarz:

**Σ|F(ρ)||F′(ρ)| ≤ (Σ|F(ρ)|²)^{1/2}·(Σ|F′(ρ)|²)^{1/2} = S₂^{1/2}·(Σ|F′|²)^{1/2}**

using Σ|F(ρ)|² = S₂, which **is** BHB's single RH-use (1−ρ = ρ̄ ⇒ F(1−ρ) = conj F(ρ)).
[verified: paper text via bhb-rh-role note §2.]

Now Σ|F′|² = Σ|B′ζ′ + Bζ″|² ≤ 2Σ|B′ζ′|² + 2Σ|Bζ″|². **Split:**

**(a) Good part — Σ|B′ζ′|² = O(L²·S₂), PROVEN (transfer claim).**
B′(s) = Σ b(k)(−log k)/k^s is a Dirichlet polynomial of the same type as B, with coefficient
polynomial Q(u) := −ϑL·u·P(u) (still a polynomial in u, Q(0)=0). Applying Lemma 1 verbatim to the
mollifier B′ in place of B, the main term becomes (T/2π)L³·[1/2 + 3ϑ∫₀¹Q(u)²du] − 2Re(M₂^Q),
with Q² = ϑ²L²·u²P². The diagonal term scales as L² while the pole term stays O(L³·1); hence

**Σ|B′ζ′|² ~ (T/2π)L⁵·3ϑ³∫₀¹u²P(u)²du (dominant),  i.e. Σ|B′ζ′|² = L²·r·S₂** with
**r := 3ϑ³∫₀¹u²P² / (1/2 + 3ϑ∫₀¹P²)** (diagonal ratio; the M₂^Q term shifts the constant but not
the L-power). No new hypothesis beyond Lemma 1's own inputs — the (−log k)² weights are exactly
the "harmless extra L factors" the task anticipated. [Label: PROVEN, modulo reading M₂^Q off the
same Lemma 1 proof.]

**(b) Bad part — Σ|B(ρ)|²|ζ″(ρ)|² is NOT covered by Lemma 1. THE BLOCKER.**
Lemma 1 evaluates moments of ζ′ (mollified), i.e. integrals of B(s)ζ′(s)·B(1−s)ζ′(1−s)·(ζ′/ζ)(s)
around the symmetric rectangle. A ζ″ moment would require the integrand with ζ″(s)ζ″(1−s) — a
completely different residue structure (ζ″ has a double pole at s=1, and its horizontal-segment
convexity/error analysis is not in the paper). **Lemma 1 provides no bound for Σ|B(ρ)|²|ζ″(ρ)|²,**
and no such bound appears in arXiv:1302.5018. Unconditionally, a weighted discrete second moment
of ζ″ is an open-type problem (it is not implied by the ζ′-moment evaluations S₁, S₂; even its
heuristic order requires the rescaled-ζ′ conjecture at zeros). It is **not** "harmless log-weights":
it is a new function ζ″ appearing as a genuine factor, not a polynomial weight.

**Therefore Σ|B′B″| (in the only reading that matters, Σ|F||F′|) is NOT shown to be O(S₂) by the
residue machinery. It is O(L·S₂) *if and only if* the ζ″ piece is separately shown to be
O(L²·S₂) — an unproven input.**

---

## 5. Explicit Δ(T) (optimistic, ζ″-free) and comparisons

If the ζ″ term were bounded by the good part's order (Σ|F′|² ≪ L²·S₂, NOT established), then:

E/S₂ ≤ 2Δ·√r·L  ⇒  **Δ(T) < 0.0311/(2√r·L) = b/L,  b = 0.0311/(2√r).**

With ϑ = 1/2, P(u) = −ϑu²+(1+ϑ)u (BHB's optimizer): ∫₀¹P² = 17/40, ∫₀¹u²P² = 33/140, giving

**r_diag = 3ϑ³∫u²P²/(1/2+3ϑ∫P²) = (99/1120)/(91/80) = 99/1274 ≈ 0.0777,**
**b ≈ 0.0311/(2·√(99/1274)) ≈ 0.0558** (≈ 1/17.9); using the net S₂ constant 57/64 in place of
91/80 gives **b ≈ 0.0494** (≈ 1/20.2). Order of magnitude: **b ≈ 0.05, i.e. Δ(T) ≈ 0.05/L**
(diagonal-only; the M₂^Q contribution will move the last digit, not the order).

**Comparisons:**
- BGSTB's box: |β−1/2| < 1/(2 log T), i.e. **b = 1/2**.
- This optimistic route: **b ≈ 0.05** — about 10× narrower than BGSTB.
- GS-style density (b→0): strictly narrower still; not what this route gives.

So even in the best case the box route demands a **~10× stronger-than-standard box** to reach the
3.1% slack — and that best case is not established because of the ζ″ blocker.

---

## 6. Labels

| Claim | Label |
|---|---|
| BHB's moments are Σ Bζ′(ρ), Σ Bζ′(ρ)Bζ′(1−ρ) (not B′) | PROVEN (verbatim, Lemma 1/eq. 1) |
| B′, B″ of the mollifier: (−log k)^ν weights | PROVEN (termwise differentiation) |
| ρ̄−(1−ρ) = 2(β−1/2); quadratic Taylor term cancels | PROVEN (exact algebra) |
| E ≪ Δ·Σ\|F\|\|F′\|, F′ = B′ζ′+Bζ″ | PROVEN (Taylor + box) |
| Σ\|B′ζ′\|² = L²·r·S₂ (residue method, no new hypothesis) | PROVEN (transfer; M₂^Q constant pending) |
| Σ\|Bζ″\|² = O(L²·S₂) (what Lemma N needs) | **INCONCLUSIVE (blocker: new ζ″-moment, not in Lemma 1)** |
| Δ(T) = b/L, b ≈ 0.05 | PROVEN (form) / rough (value), **conditional on the ζ″ blocker being resolved** |
| Box route clears 0.6818 with a standard b=1/2 box | INCONCLUSIVE (needs b≈0.05, i.e. 10× stronger, plus ζ″ input) |

---

## 7. Blockers / next step

**Blocker (exact):** Lemma N's Cauchy–Schwarz step needs Σ|F′(ρ)|² = Σ|B′ζ′ + Bζ″|², and the
cross/ζ″ term Σ|B(ρ)|²|ζ″(ρ)|² is a weighted discrete **second moment of ζ″**, which Lemma 1 (a
ζ′-moment theorem) does not provide and which is not in the literature read this session. The
"harmless (log k)(log m) weights" story is correct **only** for the B′ζ′ piece.

**Next step (named):** either (i) find/prove an unconditional bound Σ_{0<γ≤T}|B(ρ)|²|ζ″(ρ)|² ≪
L²·S₂ (this is the new input that would close Lemma N), or (ii) replace the Taylor-in-β route with
a decomposition that avoids ζ″ (e.g. the functional-equation identity ζ′(1−ρ) = −χ(1−ρ)ζ′(ρ),
valid at zeros, which trades ζ″ for the phase of ζ′ and the χ-factor — not obviously simpler), or
(iii) accept that the box route is blocked at this level and fund the zero-density route
(Guth–Maynard) instead, which bounds E = Σ_{off-line}|F(ρ)|² directly without Taylor expansion.

*Assumptions tagged:* `[verified]` S₂ = Σ|Bζ′(ρ)|² is BHB's only RH-use (paper text);
`[verified]` Lemma 1 evaluates only ζ′-type moments (paper Lemma 1 statement);
`[inferred]` no unconditional weighted ζ″-moment bound exists in the sources read (absence-of-
evidence; flagged as the blocker, not a proof of impossibility).
