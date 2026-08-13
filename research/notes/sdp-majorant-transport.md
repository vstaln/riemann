# SDP-majorant transport into our certificate class — analysis

**Date:** 2026-08-14. **Status:** PROVEN facts (from the Anthropic paper + our records,
verified against the sources); transport verdict CONJECTURED (structural argument, no
computation). **s4h method applied:** s4h-constraint-hardness-testing (is the "different
regime" a real wall or an assumption?).

## The question

Chirre–Gonçalves–de Laat [CGdL20] obtained **0.6792 simple-on-line** (and 0.8825 simple /
0.9412 distinct for ξ′) under RH via semidefinite programming (SDP majorants exploiting
positivity of Montgomery's F outside [−1,1]). Our certified **unconditional** record is
0.673481 simple-on-line. Question: can the SDP-majorant input be transported into our
certificate class (Weil quadratic form + Sylvester inertia + rank–trace, coboundary
redistribution, band-width ≤ 1) to break 0.673481 unconditionally?

## (a) The "different regime" — verified facts

The Anthropic paper (§1.2, head.txt lines 129-131) says of CGdL20: "obtained 0.6792 via
semidefinite programming by exploiting the positivity of F outside [−1, 1]; the optimality
statement in Theorem D is scoped to the values of F on [−1, 1] only, so such majorants
operate in a different regime."

**What "different regime" means (PROVEN from the structure):**
- Montgomery's F(α) is the pair-correlation form factor. On |α| ≤ 1 it has the known shape
  F(α) = |α| (plus the δ-atom at 0); outside [−1,1] only the positivity F(α) ≥ 0 is known.
- CGdL20 use SDP to find the *best majorant* of F that is ≥ F everywhere AND has compact
  Fourier support ≤ 1 — the SDP exploits the positivity constraint outside [−1,1] to
  sharpen the majorant inside [−1,1].
- **Our certificate uses test functions with band-width ≤ 1** (the λ-parameter family;
  record at α=1.464 corresponds to band-limit ≤ 1 in Montgomery normalization). The
  explicit formula only sees the test function's Fourier transform on |α| ≤ 1 — the region
  where F is *known*, not the region where SDP positivity helps.
- Therefore: **the SDP majorant's advantage lives precisely in the part of F that our
  certificate cannot see.** This is the "different regime": CGdL20 gain from F's behavior
  on |α| > 1 (positivity-only, RH-conditional reading); our Weil-form machinery is
  restricted to |α| ≤ 1 (unconditional). This is a STRUCTURAL separation, not an
  implementation gap.

## (b) Can transport break the eps=0.00620 wall? — structural argument

Our ceiling analysis (research/notes/structural-final-verdict.md) pins the in-class ceiling
at **0.68183123 = p₀ + |E(1)|** where p₀ = 0.6818287 is the simple-point fraction bound
from the two-moment machinery and |E(1)| = 1/(6·256²) is the error term. The eps=0.00620
floor is PROVEN exact (eps-boundary-exact.md: 0.00621 is a real violation, true F_B =
0.0059188 at the terminal cell, 60-digit mpmath).

**Argument (CONJECTURED, structural):** an SDP-majorant input would need to enter as a new
constraint on the multiplicity split. But:
1. The eps floor is a property of the 6-gap coboundary inequality F_B ≥ eps with tawan's
   coefficients — an SDP majorant does not change the *inequality's* coefficients, only the
   *reading* of the zero side. In our class the zero side is read by Sylvester inertia +
   rank–trace (spectral), not by F's pointwise values. The SDP's gain (F's positivity
   outside [−1,1]) has no spectral analogue in the Weil compression.
2. The one place a majorant COULD enter is the H(α) constant itself: H(α) is computed from
   the test-function family. CGdL20's 0.6792 vs our H(1.464) = 0.6724674 — the gap 0.0068
   is exactly the "different regime" gain. If a better test family with band-width ≤ 1
   existed, H would already be higher — the LP threads (coboundary-reopt, symmetric re-opt)
   found tawan's coefficients LP-optimal in-class.
3. Conclusion: **transport is structurally blocked for the eps floor; the only transport
   channel is the H(α) constant, which requires a band-width ≤ 1 test function with
   provably higher H — and the SDP majorants do not provide that (they violate band-width
   ≤ 1 by design).**

## (c) Related: the ξ′ results do not transfer (verified)

The paper's §7.3 (full txt, lines 2600-2625) proves for **ξ′ zeros** (derivative of ξ):
flat window 0.85838 simple on-line, quartic window 0.86864, distinct 0.92919 — all
unconditional; CGdL20 Cor 7 gives 0.8825/0.9412 conditional. **These are for ξ′, NOT ζ.**
Our earlier note research/notes/xiprime-transfer.md established the ξ′ → ζ transfer is
VACUOUS (no pointwise zero transfer; ξ′ zeros interlace ζ zeros but G(γ₁) ≈ −0.0014 ≠ 0
while ζ(γ₁) ≈ 0). So the 0.86864/0.92919 do not lift to ζ. (This also explains why the
distinct-integrality agent's 0.8466 sighting was for a different function context.)

## (d) The RH-conditional distinct 0.85082 formula (verified)

The paper (txt lines 2780-2785) proves under RH: **N_d ≥ 1/2 + (2m₂ − m₃)/18 + (4/9)·(19/27)
= 0.85082**, using the weight "optimal within span{m, m², m³, 1_{m=1}} by linear programming"
with m₂, m₃ interval-certified. The m₃ (third moment) term is exactly why this needs RH —
our C4 note (c4-second-moment-denominator.md) PROVED higher moments add nothing
unconditionally on (1/2,1). So 0.85082 is unreachable unconditionally in the current
framework.

## Verdict

**SDP-majorant transport is blocked as a route past 0.673481 within the current certificate
class** (structural separation: band-width ≤ 1 vs F-outside-[−1,1] positivity; eps floor
proven exact; H LP-optimal in-class). The open directions that survive:
1. A genuinely new test-function family with band-width ≤ 1 and H > 0.6724674 (would move
   the H constant; tawan LP-optimality is only within the 578-config family, not all
   families).
2. A new unconditional moment (not m₃, which is dead) that enters the distinct bound
   directly.
3. The 0.6818 ceiling is the in-class bound; breaking it needs a structural input change.

## Sources

- [CGdL20] A. Chirre, F. Gonçalves, D. de Laat, Pair correlation estimates for the zeros
  of the zeta function via semidefinite programming, Adv. Math. 361 (2020) 106926;
  arXiv:1810.08843. (cited in paper, txt line 3607)
- Paper §1.2 head.txt lines 124-131 (0.6725/0.6727/19-27/0.6792 chain, "different regime")
- Paper §7.3 txt lines 2600-2625 (ξ′ results, flat/quartic windows, CGdL20 Cor 7)
- Paper txt lines 2780-2785 (N_d ≥ 0.85082 under RH, m³ weight LP-optimal)
- Our records: FINAL-RECORD-2026-08-13.md; eps boundary: eps-boundary-exact.md;
  ξ′ transfer: xiprime-transfer.md; ceiling: structural-final-verdict.md; C4: c4-second-moment-denominator.md

## Honesty note

This note makes NO new certified claim and raises NO record. It documents, from verified
sources, that the SDP-majorant route is structurally separated from our certificate class,
and identifies the surviving open directions. The transport verdict is a structural
argument (CONJECTURED), not a computation.
