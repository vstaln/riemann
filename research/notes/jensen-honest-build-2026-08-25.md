# Jensen honest build — curvature-subtracted disc mass vs planted off-line zeros
Date: 2026-08-25 | Agent: builder | Status: SPEC (results appended below)

## Root cause this addresses (from g30-hardened-2026-08-25.md)
The wave-90 g3-0 probe was vacuous: it never evaluated the function. It computed
E(c,r) = Σ log(r/|ρ−c|) from the zero LIST only, on a disc (c_re=0.75, r=0.2) that
misses the critical line, so E_RH=0 by tautology and the "gap" was the single-plant
log(r/d0) toy. No curvature term, no permutation test, thresholds from thin air.

## The honest statistic
For a disc D(c,r), c = c_re + i·t, the Jensen disc mass is the average of log|ζ|
over the disc (Jensen's formula ties the boundary average to log|ζ(c)| + Σ log(r/|ρ−c|);
the area average is the well-defined version when a zero sits exactly on the boundary,
which happens by construction for c_re=0.6, r=0.3, β=0.9). We evaluate the ACTUAL
function ζ(s) via mpmath (dps=15) — no zero-list short-circuit, no vacuous geometry.

- S(t) = mean of log|ζ(s)| over the disc area (grid: 5 radial rings × 20 angles).
- κ(t) = Turan-type curvature = second finite difference of S along the Im line,
  κ(t) = S(t+h) − 2S(t) + S(t−h), h = r (pre-specified, no tuning).
- Primary combined statistic: Q(t) = S(t) − κ(t) ("curvature-subtracted disc mass").
  Raw S and κ distributions are ALSO reported; no thresholds are imposed.

## Planted model (exact, FE-symmetric)
Moving the on-line zero 1/2±it0 to β±it0 must keep the functional equation. The exact
Hadamard ratio (ξ-form, exponential factors included) is
  ζ_planted(s) = ζ_true(s) · Π_{p∈P}(1−s/ρ_p)e^{s/ρ_p} / Π_{m∈M}(1−s/ρ_m)e^{s/ρ_m}
with P = {β±it0, (1−β)±it0}, M = {1/2±it0}. This is exact (ξ(s)=ξ(0)e^{bs}Π(1−s/ρ)e^{s/ρ})
and gives a genuine FE- and conjugation-symmetric zeta-like function. Verified in code:
ζ_planted has a zero at β+it0, no zero at 1/2+it0, matches ζ_true away from the swap, and
satisfies the ξ functional equation numerically. On-line control β=0.5 ⇒ P=M ⇒ correction
≡ 1 ⇒ the control distribution is identical to the RH distribution by construction.

## Design (pre-specified, no cherry-picking)
- True zeros: tools/data/zeros_verified_32k.txt (verified, dps=25 source).
- Implant positions: t0 = γ_n for n = 1..12 (all nearby zeros 14.13..56.45; using ALL
  satisfies "≥10 random implant positions" without cherry-picking).
- Discs: c_re ∈ {0.6, 0.75} × r ∈ {0.2, 0.3} (4 configs), h = r.
- Groups per config: RH (true zeta), FALSE (β=0.9 implant at each t0), CTRL (β=0.5).
- Test: permutation test on group labels (RH vs FALSE), two-sided
  statistic |mean_Q(FALSE) − mean_Q(RH)|, 200 permutations, conservative p = (1+#≥)/(1+200).
  Same test on S and κ reported for transparency. Control must stay silent (p ≥ 0.05).

## Verdict logic (from mission)
SEPARATES iff some config gives p_FALSE < 0.05 AND all on-line controls stay silent.
Otherwise NO_SEPARATION / INCONCLUSIVE, with honest labeling of what the statistic
does and does not measure.

---
## RESULTS (appended after run)
