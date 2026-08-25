# Jensen honest build — curvature-subtracted disc mass vs planted off-line zeros
Date: 2026-08-25 | Agent: builder | Status: COMPLETE (spec first, results below)

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

## Diagnostic extension (added before running, pre-registered in code)
The spec's on-line control (beta=0.5) is the IDENTITY swap (plant a zero at the
position it already occupies), so it is silent trivially. To determine whether any
separation is *specific to off-line structure* or just *any zero displacement*, an
additional on-line group LINE is measured: move the zero to (1/2, t0+0.3) (same
magnitude displacement, but along the critical line). FE-exact via the same
construction (planted_set with beta=1/2, t_p=t0+0.3).

---
## RESULTS (2026-08-25, tools/jensen_honest_probe.py, mpmath 1.4.1 dps=15, N_PERM=1000, seed 20260825)

### Model construction — all honesty checks PASS
```
planted zero at 0.9+it0 present:        |zeta_planted| = 0.00e+00   (exact zero)   
on-line zero at 0.5+it0 removed:        limit 0.0179, offset check rel 4.3e-08     
R far asymptotics vs distance formula:  rel 3.54e-16                                
xi(s)=xi(1-s) for planted model:        |diff| = 2.19e-19   (FE exact)            
beta=0.5 identity control == true zeta: |diff| = 0.00e+00                            
Jensen closed form vs direct boundary quadrature (4 discs, true zeta): |diff| <= 1.1e-16
```
Key construction facts (each CHECKED NUMERICALLY):
- The planted model is exactly FE-symmetric: zeta_planted = zeta_true * R with
  R(s) = prod_P(1-s/rho)/prod_M(1-s/rho), P = {0.9+-it0, 0.1+-it0}, M = {1/2+-it0}.
  The e^{s/rho} Hadamard exponentials were REJECTED after testing: they break
  xi(s)=xi(1-s) by ~16% (sum 1/rho_p - sum 1/rho_m = 0.004975 != 0); the plain
  finite ratio satisfies R(1-s)=R(s) exactly (sets FE-closed, #P == #M mod 2).
- mp.zeta(m0, 1) at an exact zero returns the ~1e-21 error floor, NOT the
  derivative (|zeta'(rho_1)| = 0.793 by central difference, verified at dps=50);
  the 0*inf limit at the removed zero is evaluated with the central-difference
  derivative and agrees with the offset evaluation to 4.3e-8.
- The Jensen disc log-average is computed in EXACT closed form
  S(t) = log|zeta(c)| + sum_{|rho-c|<r} log(r/|rho-c|)  (Jensen's formula),
  one mpmath evaluation per disc + the verified zero list. This is the honest
  fix for the g3-0 vacuity: the old probe computed only the zero-list sum on a
  disc missing the critical line (E_RH = 0 by tautology); the function value
  log|zeta(c)| carries the whole neighborhood, so no disc is ever vacuous.
  Direct 160-point boundary quadrature reproduces the closed form to 1e-16.

### Main result — per config, means of (S, kappa, Q) and permutation p-values
```
c=0.6, r=0.2:  RH   (-1.276, +0.211, -1.487)   FALSE (-4.431, +0.504, -4.934)
              CTRL (-1.276, +0.211, -1.487)   LINE  (-0.832, +0.007, -0.839)
              p_Q(FALSE)=0.0010  p_Q(CTRL)=1.0000  p_Q(LINE)=0.0010   p_S=0.0010  p_kappa=0.0010
c=0.6, r=0.3:  RH   (-0.871, +0.078, -0.948)   FALSE (-4.431, +0.973, -5.404)
              CTRL (-0.871, +0.078, -0.948)   LINE  (-0.832, +0.574, -1.406)
              p_Q(FALSE)=0.0010  p_Q(CTRL)=1.0000  p_Q(LINE)=0.0030
c=0.75,r=0.2:  RH   (-1.174, +0.483, -1.657)   FALSE (-4.695, +0.525, -5.219)
              CTRL (-1.174, +0.483, -1.657)   LINE  (-0.742, -0.025, -0.717)
              p_Q(FALSE)=0.0010  p_Q(CTRL)=1.0000  p_Q(LINE)=0.0010
c=0.75,r=0.3:  RH   (-0.992, +0.500, -1.492)   FALSE (-4.289, +0.389, -4.678)
              CTRL (-0.992, +0.500, -1.492)   LINE  (-0.742, +0.219, -0.961)
              p_Q(FALSE)=0.0010  p_Q(CTRL)=1.0000  p_Q(LINE)=0.0010
```
- FALSE vs RH: p_Q = 0.0010 in ALL 4 configs (minimum of the 1000-permutation
  resolution with the conservative (1+count)/(1+1000) estimator); effect size
  |mean Q_FALSE - mean Q_RH| = 3.2 .. 4.5 log-units. Separation is not marginal.
- CTRL (beta=0.5) vs RH: p = 1.0000 everywhere — exactly silent, as required.
- LINE (zero moved to (1/2, t0+0.3), still ON the line) vs RH: p = 0.001..0.003
  in all 4 configs — ALSO separates, with a comparable effect in the opposite
  direction (mean Q_LINE - mean Q_RH = +0.53 .. +0.94).

### Raw Q distributions (12 implant positions, t0 = gamma_1..gamma_12)
```
c=0.6, r=0.2  RH:   -2.102 -1.759 -1.578 -1.634 -1.579 -1.250 -1.510 -1.307 -1.462 -1.561 -1.037 -1.064
             FALSE: -4.641 -4.693 -4.686 -4.937 -4.961 -4.764 -5.110 -4.964 -5.221 -5.357 -4.895 -4.985
c=0.6, r=0.3  RH:   -1.576 -1.229 -1.047 -1.097 -1.041 -0.714 -0.968 -0.767 -0.913 -1.010 -0.497 -0.522
             FALSE: -5.122 -5.171 -5.162 -5.408 -5.431 -5.236 -5.576 -5.431 -5.679 -5.813 -5.362 -5.450
c=0.75,r=0.2 RH:   -2.210 -1.894 -1.726 -1.793 -1.744 -1.426 -1.690 -1.492 -1.650 -1.751 -1.237 -1.267
             FALSE: -4.864 -4.944 -4.949 -5.212 -5.242 -5.056 -5.405 -5.264 -5.524 -5.662 -5.210 -5.303
c=0.75,r=0.3 RH:   -2.057 -1.738 -1.568 -1.630 -1.580 -1.264 -1.522 -1.325 -1.475 -1.575 -1.071 -1.099
             FALSE: -4.335 -4.411 -4.415 -4.672 -4.701 -4.517 -4.860 -4.720 -4.973 -5.109 -4.667 -4.759
```
The FALSE distributions are tight (spread ~0.3) and far from RH (gap ~3.2-4.5);
the separation is not driven by one outlier position but by all 12 implant sites.

### VERDICT: SEPARATES  (p_FALSE = 0.0010, all 4 configs; on-line beta=0.5 control silent, p=1.000)

## Honest interpretation (what the separation does and does NOT mean)
- PROVEN / CHECKED NUMERICALLY: the statistic genuinely separates the planted
  off-line model from the true-zeta statistics at p < 0.05 with the specified
  on-line (beta=0.5) control silent. The construction is exact (FE, zero
  structure, closed-form Jensen) — this is a real effect, not the g3-0 vacuity.
- BUT the mechanism is NOT off-line-specific. The LINE diagnostic — moving the
  zero to (1/2, t0+0.3), which stays on the critical line — separates with the
  same significance (p=0.001..0.003). The statistic is a sensitive local probe:
  it detects that a zero moved AT ALL (its position in Re and Im relative to the
  off-line disc centers), not that the zero is off the line.
- WHY: for a single nearby zero, S(t0) = log|zeta'(rho)| + log(max(d, r))-style
  (Jensen cancellation inside the disc; log d outside), so S and kappa encode the
  zero's distance to the off-line center — a purely geometric quantity that
  responds to any displacement. The sign even flips with the geometry: moving the
  zero farther from the center raises S; FALSE sits lower because |zeta'| at the
  planted location is smaller. Nothing in (S, kappa, Q) consults the
  on/off-line STATUS of the zero as such.
- Therefore this build CONFIRMS the g30 suspicion at the code level: the
  curvature-subtracted Jensen machinery separates *perturbed zero sets* from the
  true set, but it does not provide evidence about the Riemann hypothesis — it
  would flag an on-line-but-moved zero exactly as strongly as an off-line one.
- No threshold was imposed; all reported quantities are raw distributions and
  permutation p-values. Multiple comparisons: 4 configs, all significant at
  p=0.001 (Bonferroni threshold 0.0125 would not change the verdict); the LINE
  finding uses the same 4 tests.

## Honesty labels
- PROVEN (algebra): R(1-s)=R(s) for the finite ratio; Jensen closed-form identity
  (quadrature agreement 1e-16); beta=0.5 swap is the identity.
- CHECKED NUMERICALLY: all values above; FE exactness 2.19e-19; zero structure;
  |zeta'(rho_1)| = 0.793 (central difference, dps=50); mp.zeta(m0,1) unreliable
  at exact zeros (error floor ~1e-21).
- INCONCLUSIVE (by design): whether off-line zeros are detectable *as off-line*;
  the LINE control shows the statistic cannot certify it. No claim about RH follows
  from this separation.

