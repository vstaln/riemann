# Turán / (log xi)'' pointwise probe — 2026-08-25

Lever-4 rung 2: can a POINTWISE statistic, not a moment, separate displacement TYPE
(off-line vs on-line) and does an implant flip the sign of (log xi)'' anywhere?

Tool: `tools/turan_pointwise_probe.py` (dps=25, mpmath). Verifies in 1.8s.

## The exactness core
For every planted model `zeta_planted = zeta_true * R` (finite FE-exact ratio,
reused from `jensen_honest_probe.py`):
```
(log xi_planted)''  =  base(s) + L_R(s)
base(s) = (log xi_true)''                 identical across ALL groups
L_R(s)  = (log R)'' = -Sum_p 1/(s-p)^2 + Sum_m 1/(s-m)^2     EXACT analytic
```
So the discriminant between any two implants is *exactly* `L_R`, pure closed form —
no numerical noise, no permutation. `base` cancels in every difference; computed
once and reported for sign context. Validation: CTRL (identity) gives |L_R|~6e-27;
Re(L_R) even / Im antisymmetric under sigma<->1-sigma (sigma-conjugate check PASS).

**Removable singularity at s=0.5+it0** (the removed on-line zero): `base` and
`+1/(s-m0)^2` both diverge there but the SUM is finite (planted xi is finite at the
removed zero). Excluded from the grid, documented.

## Question A — does the implant flip pointwise sign of P=(log xi)''?
Grid s = sigma + i(t0+dt), sigma in [0.3,0.7], dt in {-0.3,0,0.3}, t0=gamma_1=14.134725.
`base` sign is negative (concave) near the implant mostly, positive at t0 (the
singular neighborhood); `L_R` shares its sign at the max-ratio point.
max |L_R/base| over grid = **1.194** at (sigma=0.5, dt=-0.3, FALSE) — ratio exceeds
1 but SAME sign as base, so **no observed sign flip of the total P**. The implant
perturbs magnitude, not the sign, in this region. Flip would need a ratio>1 with
opposite sign; not seen.

## Question B — does a pointwise statistic separate displacement TYPE?
Groups: FALSE (off-line, beta=0.9 -> {0.9,0.1}+-it0, 4 pts), LINE (on-line displaced
beta=0.5,t_p=t0+0.3 -> {0.5}+-i(t0+0.3), 2 pts), CTRL (identity).

On the **critical line** (sigma=0.5): FALSE and LINE both give Re L_R < 0 at all
non-singular t-offsets (0/4 sign flips) -> a pure on-line scalar sign does NOT
separate.

Off the critical line (sigma-profile at dt=0): opposite signs at the two sigma
extremes:
```
 sigma 0.30: FALSE -2.78   LINE +25.01   <- OPPOSITE
 sigma 0.35: FALSE+25.14   LINE +44.45
 sigma 0.40: FALSE+84.89   LINE+100.01
 sigma 0.45: FALSE+386.90  LINE+400.01
 (0.5 singular)
 sigma 0.55: FALSE+386.90  LINE+400.01
 sigma 0.60: FALSE+84.89   LINE+100.01
 sigma 0.65: FALSE+25.14   LINE +44.45
 sigma 0.70: FALSE -2.78   LINE +25.01   <- OPPOSITE
```
2/8 sigma off-critical, symmetric about 0.5. This is exactly the predicted structural
signature: the off-line 4-point set {beta,1-beta} pins Re L_R negative as sigma enters
the interval near beta's complement (a sigma-zero-crossing in L_R), while the on-line
displaced 2-point set (always at beta=0.5) stays positive there. Even/odd structure
under sigma<->1-sigma is present in both, but the SIGN at extreme sigma separates.

Magnitude: max |Re L_FALSE / Re L_LINE| = 1.20 (modest; grows toward singular sigma).

## VERDICT: TYPE_SEPARATES  — max effect ratio 1.20
PROVEN numerically (single implant height t0=gamma_1): the pointwise (log xi)''/Turán
perturbation's sigma-profile sign structure separates off-line from on-line displacement
via the off-critical sigma-extremes, while the on-critical-line sign does not.

## Candid caveats
- Separation is OFF-critical, not on the line; the scalar "sign of P at sigma=0.5" alone
  is NOT type-separating (0/4). The separating statistic is the profile's sigma sign-zigzag.
- Single height (t0 = gamma_1), single implant per model. Effect ratio 1.20 is modest.
- The cell "removable singularity at 0.5+it0" itself is type-invariant (present for all
  non-CTRL groups) so carries no type information on its own.
- Not yet an antiderivative/T-invariant proof; this is a pointwise diagnostic on the
  finite-ratio perturbation family, consistent with the Li-harness verdict that single
  implants are locally invisible to MOMENT statistics but now visible to a POINTWISE one.

LABELS: all numerics above are CHECKED NUMERICALLY (deterministic mpmath, exact L_R).
No claim proven as a theorem.
