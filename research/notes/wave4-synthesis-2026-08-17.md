# Wave-4 Synthesis — sinc-m3 certificate REFUTED; barrier zoo now real (2026-08-17)

**Coordinator verdict after 4-agent wave + own line-by-line checks.**

## 1. sinc-kernel m₃ certificate LP: REFUTED as a ceiling-breaker

Two hostile blind referees (disjoint joints), one independent re-derivation, coordinator
counterexample check — all agree the claimed κ* = 0.7488 > 0.6818 does NOT hold up.

**Referee-A (d273aacb, tools/referee_a_probe/):** model does not survive.
- **(Decisive) Floor / E[T] ≥ 0 is unproven and FALSE per-config.** The certificate's floor
  max(D+P₃, m₂²) is only a valid S₃ lower bound if E[T] ≥ 0. Counterexample (3×3 PSD,
  G=[[1,a,a],[a,1,a],[a,a,1]], a=−0.2, ev (0.6,1.2,1.2), all marks 1): m₃=1.224 ≥ m₂²=1.1664
  (theorem HOLDS) yet T = m₃−D−P₂ = −0.016 < 0. **Coordinator verified by hand** (tr G²=3.24,
  tr G³=3.672, P₂=0.24, D=1, T=−0.016). Under the ONLY proven floor (S₃ ≥ m₂²):
  **min-p₁ = 0.4224 (mass) / 0.5939 (count), both below the wall 0.6818.** The 0.7488 is an
  artifact of an unproven inequality.
- **Convention mix.** Model p₁ is a MASS fraction (P(m=1)=2p₁/(1+p₁)); the wall p₀=0.6818287
  is the 256-law's COUNT simple-point fraction. Same-quantity (count) recompute gives
  min-p₁ = 0.8564, not 0.7488.
- **Calibration knife-edge.** m₂(1)=2.22 anchor: ±5% flips the verdict in both conventions
  (mass 2.11→0.608, 2.22→0.749, 2.33→0.870; count 2.11→0.756, 2.22→0.856). Real-zeros SE ~7%.
- **Control EXHIBITED:** the 256-law (mass p₁=0.5173 < 0.7488) has PROVEN floor m₂²=5.2488
  ∈ [4.56,5.44] → admissible under proven inputs; excluded only under the unproven E[T]≥0.
- Passes: row-0 formula (1/N convention), P₃ algebra (both branches, p₁=1 value 3.66
  reproduced), pair rows as class axiom (α>1 conjectural caveat).

**Referee-B (81636ce4, tools/referee_b_probe/):** interpretation + LP reconciliation.
- σ-blindness PROVEN by inspection (no Re ρ enters; pair rows an input constant; read hard-
  coded 5±0.44).
- "0.7488 = simple fraction" is a **dimensionally-loose label**: at p₁=0.7488 the law's own
  P(m=1)=2p₁/(1+p₁)=**0.8564**; the honest statement is "P(m=1) ≥ 0.8564 under H1–H4 with
  calibration anchor m₂(1)=2.22".
- κ* knife-edge on the unproven anchor (2.00→0.466, 2.22→0.749, 2.33→0.870): "exceeds 0.6818"
  is an artifact of the anchor within a narrow window.
- **Scan AUTHORITATIVE; minilp `Infeasible` is a linearization artifact**: probe proves the
  linearized tangent system is infeasible for EVERY p₁∈[0,1] while the true problem is
  feasible at p₁* — the LP block certifies nothing (this resolves the re-derivation agent's
  flagged follow-up).
- Floor monotone through the crossing (d=−2.724 at p₁=0.7488), non-monotone only in the m₂²
  tail p₁∈[0.955,1.0]; bisection min-p₁ correct.
- **Record mapping: raises NO published on-line record** (41.7% PRZZ20 and 0.6725 stand);
  would need an on-line proportion + multiplicity theorem.
- **Control (world B): VACUOUS** — "reads(B)==reads(A)" trivial (read hard-coded); flat rows
  never verified for B. **The on-line interpretation does NOT survive the firewall.**
- DH's simple off-line zeros (certified σ=0.8085/0.6508, t=85.7/114.16) kill the RH-type
  hypothesis needed for any on-line reading.

**Re-derivation agent (7f447497, tools/rederivation_m3/):** m₃ ≥ m₂² PROVEN independently
via Parseval + Cauchy–Schwarz (m₃ − m₂² = N²M² Var(T1) ≥ 0, equality ⟺ uniform marks;
numeric slack −1.16e-10 at m_j≡2). Raw mark moments fail (−8+17p₁−9p₁²<0); mean-1 variable
holds in BOTH normalizations → the theorem binds the sinc branch legitimately (m₂ p₁-dependent,
closed form reproduces m₂(1)=2.22). Torus E[m₂]=2.480620 is NOT the theorem's m₂ under either
normalization → the torus-infeasibility declaration is outside the theorem's scope
(INCONCLUSIVE). Firewall stated: position-blind, says nothing about the line.

**Synthesis:** the m₃ ≥ m₂² theorem is genuine (two independent proofs now) but contributes
NOTHING to the ceiling question — it is slack at the certificate's optimum, and the claimed
κ*=0.7488 rests on the unproven/false E[T]≥0. Under proven inputs the m₃-read certificate
forces min-p₁ ≈ 0.42–0.59, below the wall. **The sinc-m3 lever is CLOSED as a ceiling-breaker.
No on-line record is affected. Firewall: proportion theorems remain zero evidence about RH.**
Ledger: label REFUTED (hostile referees + coordinator counterexample).

## 2. Barrier zoo: NOW REAL (rung-0 discipline tool operational)

Wave-4 builder (f0f32ad5) fixed all 8 root causes: Gamma off-by-half (t=z+6.5 not z+6),
C::exp angle in the real slot (e^{2πa/5} not e^{i2πa/5}), q^{+s} vs q^{-s} ×3, DH grid dt=0.5
can't resolve t=85.7/114.16, theta origin excluded, classifier regex parens. Acceptance
(real run, verified by coordinator):
- Γ(2)=1.0000000000, Γ(5)=24.0000000000; eps(psi)=0.850651+0.525731i (|ε|=1); FE +1/−1 both
  true; |f_plus|=3.1e-14/3.3e-14 at both certified DH zeros (need <1e-9); DH search finds 6
  off-line zeros, certified matched 2/2; Epstein modularity rel 1e-15–1e-13, Dedekind TRUE
  (rel ≤7e-10), direct-sum anchors 1e-7/1e-10; |Z(s0)|=2.3e-16 and 1.5e-16 (both planted
  zeros); classifier 10/10 (pre-fix was 7/10).
- Honest caveat: Epstein's own off-line zero search still finds 0 (grid resolution; a fine
  grid ~1000× too slow with the O(50k)-term theta integral; flagged as follow-up with a fast
  I(s) evaluator; the pre-existing VERDICT text overclaims there).
- **All briefs must now be disciplined through this zoo (rung-0), per the goal.**

## 3. Wave-5 prepared (briefs on disk) — M4-proper + k<1 Type-1 decision

- research/notes/wave5-briefs-2026-08-17.md: (A) M4-proper mechanical ζ″-moment re-derivation
  (pins r′; closed-form, cheap, never dispatched); (B) k<1 moving-boundary Type-1 decision
  (prove the route empty or find the inversion, per Anthropic E2 playbook).
- Dispatch plan: when the next wave launches, both go out in parallel with their RH-false
  controls (DH / fake-Weil for A; DH for B).

## 4. What did NOT get answered (open items)
- The exact definition of torus E[m₂]=2.480620 and why it was labeled p₁-independent
  (INCONCLUSIVE; lives in the now-forbidden-file lineage).
- Epstein off-line zero search resolution (grid-limited; follow-up needs a fast I(s)).
- A genuinely NEW object/input that beats the wall (the history lesson stands: ceilings break
  by NEW OBJECTS/INPUTS, never by sharper in-class inequalities — the sinc-m3 lever was
  another sharpening and it died, consistent with the lesson).
