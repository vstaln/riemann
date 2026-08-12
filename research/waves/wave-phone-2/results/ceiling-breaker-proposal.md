# Ceiling-Breaker Proposal — certificate-class changes that could exceed 0.6818

**Agent:** RESEARCHER (wave-phone-2) · **Date:** 2026-08-12
**Charter:** honesty labels (PROVEN / CHECKED NUMERICALLY / CONJECTURED / SPECULATIVE) throughout.
**Mission:** find a *certificate-class change* past the in-class ceiling 0.6818312306, not an in-class retune.

## 0. The ceiling restated (what a "class change" must do)

PROVEN (Lean `PairCeiling`, modulo EnclOK): a certificate of the rank-trace type reading
**only** {mean density, form factor F on [0,1], multiplicity integrality} is valid against the
256-law, whose simple-point fraction is p₀ = 0.68182868746…; hence its value ≤ p₀ + 1/(6·256²)
= 0.6818312306. This is a *feasible-set* statement: the ceiling law is a configuration consistent
with every bandwidth-1 input. Therefore exactly two escapes exist, and every candidate below is
an instance of one:

- **(E1) new proven input** — a statistic the 256-law does *not* match (beyond-1 form factor,
  third moment outside the Rudnick–Sarnak range, off-line/half-spacing mass);
- **(E2) narrower adversary class** — a proven structural property of ζ's zeros that excludes
  the 256-law (arithmetic admissibility, interlacing rigidity).

---

## 1. The distinct→on-line bridge (asked item 1)

**Precise statement.** The distinct lane certifies N_d = s₁ + s₂ + 2p ≥ (3−C)/2·N (C = ‖·‖²_F/N).
The on-line lane certifies s₁ ≥ (2−C)·N. They share the *same* constant C; the gap is pure
bookkeeping of off-line pairs p and double-on-line s₂. PROVEN (attack-multiplicity §2,
twobandwidth-transfer §5): the extremal world (2N/3 simples + N/6 doubles, p=0) has
N_d = 5N/6 and s₁ = 2N/3 — so **N_d ≥ 5/6 (or 0.8071) does NOT force s₁ > 2/3.** No published
theorem bridges distinct→on-line directly; Conrey–Ghosh–Gonek 1998 (19/27, RH) and Bui–Heath-Brown
(19/27, RH) are about *simplicity*, not on-lineness, and are RH-conditional.

**The repulsion/rigidity form that WOULD bridge.** The only way off-line zeros enter N_d is via p
(2 per pair {ρ, 1−ρ̄}). If a proven bound existed that off-line pairs occupy mass ≤ ε at
half-integer spacings (the Alternative-Hypothesis structure, Baluyot–Goldston–Suriajaya–
Turnage-Butterbaugh 2508.10857), then N_on ≥ N_d − 2p ≥ N_d − c·ε. CONJECTURED:
N_on ≥ 0.8071 − O(ε) via the λ=2/3 cubic distinct bound. **What must be proven:** an unconditional
(or RH-conditional) bound on half-integer-spacing pair mass. **Feasibility:** LOW-MEDIUM — AH is a
*conjectural* structural statement (paper-ah-2508.md: no proven constant, dead as an input today).
SPECULATIVE as an unconditional ceiling-breaker; real only as a conditional map.

**The interlacing bridge (STRONGER, in-repo).** PROVEN (Rolle): m_ξ'(γ) = m_ξ(γ) − 1 at each
on-line zero γ; one ξ′-zero per ζ-gap. PROVEN (Lean `XiPrime`): ξ′ has ≥ 0.85838 simple-on-line and
≥ 0.92919 distinct, *unconditionally*. Hence ξ′'s simple-vs-distinct gap and the gap-count identity
N(ξ′) − N(ζ) = Σ_{non-simple}(m_ξ−1) together constrain ζ's non-simplicity. CONJECTURED: a joint
(ζ, ξ′) certificate on the shared frame certifies s₁(ζ) > 0.6818. **Why it breaks the ceiling:**
the 256-law is a ζ-only adversary; a law with double on-line ζ-zeros forces a ξ′-zero structure
incompatible with ξ′'s proven 0.85838 — the adversary class shrinks (E2). **Feasibility:** MEDIUM
(two-form machinery + Lean ξ′ proofs exist; the joint form + interlacing count are new math).

## 2. Higher moments m→∞ (asked item 2)

PROVEN (paper §7.5(e/f)): unconditional evaluation of tr Ĝᵏ exists only in the Rudnick–Sarnak
range kλ < 2; odd moments do not lower the n₊-bound on (1/2,1); λ ≤ 1/2 is killed by the
dimension cap (Prop 7.4). Under HL*(k₀, λ) — a Hardy–Littlewood additive-correlation conjecture —
the ladder gives 13/18 (k₀=4) and → 1 as k₀→∞. **Conclusion:** m→∞ approaches 1 only under
prime-pair input (E1, CONJECTURED); unconditionally it is a *genuine barrier* (RS wall), not a
limitable gain. Already priced; NOT a novel ceiling-breaker.

## 3. New certificate functionals (asked item 3)

- **ξ″/higher-derivative windows:** KILLED. CHECKED NUMERICALLY (attack-xiprime2-tower):
  κ₁⁽²⁾ = 4.57 (flat) ≫ κ₁⁽¹⁾ = 1.14, certificate vacuous; α₁⁽ʲ⁾ = j·(Λlog) inflates with j. Closed.
- **Gram-stability Ψ-functional (twisted/weighted kernels):** PROVEN (ceiling-gram-constraint) it
  cannot move the ceiling — a feasible-set restriction of a maximization; only the universal floor
  ε_univ ≈ 5e-4 shifts, matching external 0.6732. In-class; not a breaker.
- **Feng–Platzer two-parameter certificates:** SPECULATIVE, no verified source in-repo. The repo's
  "Feng (2012)" is the mollifier line (41.6%, Levinson-type), which shares the prime-pair wall
  (attack-mollifier §4-6). Not independently fundable here.
- **NEW: the marked-m₃ = 5 pinned class (E2, third moment at λ=1/2).** This IS a class change:
  add the two-sided pin m₃(1/2) = 5±ε. PROVEN (m3-price.md, identity level): the super-laws and
  the 256-law have m₃ ≈ 8.15 ∉ [5−ε, 5+ε] for ε < 3.15, so the ceiling law is **excluded**; the
  old −1/3-per-unit price is VOID (the pair term 3u(p₁) refunds the p₁-room). Result: the pin does
  NOT cap p₁ below p₀; p₁ = 0.70 is reachable iff the connected triple-correlation T lands in
  [−3.87−ε, −0.44+ε], inside the real zeros' realized range. **What must be proven:** a bound on T
  (unproven third-order frontier). **Feasibility:** HIGH for the LP (machinery exists, N=64 price ≈ 0
  already computed); the actual climb is CONJECTURED (conditional on T-achievability).

## 4. The rank-trace/integrality ladder toward 2/3 (asked item 4)

PROVEN (attack-multiplicity §1-2): the ladder is the LP-optimal bookkeeping k_c(m) ≤ A·m + B·N_d.
c=2 → (A,B)=(1,2) gives simple ≥ 2−C → 2/3; c=3 → (3,2) gives distinct 5/6; c=4 gives 0.668 simple.
The c=2 constants are LP-optimal and `lemmaR_tight` — **the ladder IS the 2/3 method, it does not
pass 2/3.** Higher c only helps the *distinct* functional, never the simple one (the rank side sees
no eigenvalues, twobandwidth-transfer §3). NOT a path past 0.6818; it is the in-class wall restated.

---

## Ranked list (2 most promising novel certificate-class changes)

1. **ξ′-interlacing companion certificate (E2):** joint (ζ, ξ′) inertia form fed by the PROVEN
   ξ′ bounds (0.85838 simple / 0.92919 distinct) + Rolle interlacing m_ξ'(γ)=m_ξ(γ)−1, excluding
   the 256-law. Uses only proven input; new math = the joint form + gap-count constraint.

2. **Marked-m₃=5 pinned class (E2):** two-sided third-moment pin at λ=1/2 excludes the ceiling
   law (m₃≈8) with no cap below p₀ (PROVEN at identity level); climb to 0.70 gated only on the
   unproven connected triple-correlation T.

## Honesty footer

PROVEN: ceiling theorem structure; distinct≠simple (N_d = s₁+s₂+2p, extremal world); interlacing
m_ξ'(γ)=m_ξ(γ)−1; ξ′ 0.85838/0.92919 (Lean); RS wall kλ<2; c=2 LP-optimality/lemmaR_tight; m₃=5
pin excludes 256-law and voids the −1/3 price. CHECKED NUMERICALLY: ξ″ kill (κ⁽²⁾=4.57); m₃=5 N=64
pool LP (price ≈ 0); Gram-stability surrogates. CONJECTURED: half-spacing→on-line bridge; joint
(ζ,ξ′) certificate exceeds 0.6818; m₃-class climb conditional on T. SPECULATIVE: Feng–Platzer
two-parameter certificates (no source in-repo).
