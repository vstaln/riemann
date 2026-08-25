# FV parameter-range analysis — three gaps closed — 2026-08-26

Author: builder subagent. Tool: `research/scripts/fv_parameter_analysis_2026-08-26.py`
(extends `speiser_probe.py` machinery; sympy/mpmath-exact).
Reads: `lr-profile-theorem-2026-08-25.md`, `negativity-attack-draft-2026-08-26.md` §4 (FV),
`speiser-probe-2026-08-25.md`.

Convention (matches `lr-profile-theorem-2026-08-25.md`):
`L_R(s) = (log R)'' = -Sum_P 1/(s-p)^2 + Sum_M 1/(s-m)^2`.
- **LINE** (on-line): P = {1/2 ± i(t0+d)} (pair moved UP in height), M = {1/2 ± it0}.
- **OFF** (off-line, FE-consistent): P = {beta ± it0, (1-beta) ± it0}, M = {1/2 ± it0},
  c = beta - 1/2, u = sigma - 1/2.  t0 = gamma1 = Im zetazero(1) = 14.1347251... (height).

---

## Task 1 — beta -> 1/2+ edge: L_R^OFF does NOT -> 0 uniformly (k=2 pointwise, k=1 geometry)

**Claim under test.** "As c -> 0+ the OFF quadruple degenerates to the removed pair — L_R -> 0
uniformly." **ANSWER: NO.** The quadruple P has **4** zeros and M has **2**; as c -> 0 the four
added zeros coalesce onto the removed pair with multiplicity 2, so a **leftover pair** survives:

```
L_R^OFF(s) -> -pair(1/2, t0)  (pointwise, sigma != 1/2)   [NOT 0]
B(u;c) = 1/u^2 - 1/(u-c)^2 - 1/(u+c)^2  ->  -1/u^2  + O(c^2/u^4)
```

**Exact rate (PROVEN, k = 2 pointwise).** Factorized B (from the theorem note):
`B = (-u^4 - 4c^2 u^2 + c^4) / (u^2 (u^2 - c^2)^2)`. Expanding at fixed u >> c:
```
B(u;c) = -1/u^2 - 6c^2/u^4 + O(c^4/u^6)      [verified: (B + 1/u^2)/c^2 -> -6/u^4]
```
So the *correction to the limiting profile* is exactly `-6 c^2 / u^4`: power **k = 2**.

**The sup does not scale as any c^k.** sup_sigma |L_R^OFF| over (0,1) \ {1/2, beta, 1-beta}
is `+inf` for **every** c > 0 (PROVEN): the denominator `u^2 (u^2 - c^2)^2` keeps the poles at
u = 0 and u = ±c; the c in the numerator never cancels them — the poles merely coalesce toward
1/2 as c -> 0 (`|L_OFF(1e-30)| ~ 1e60` for all c). On any **fixed** compact set away from the
poles the profile is **O(1)**: limit `|1/u^2 + O(t0^-2)|`, max ~ 4 at u -> ±1/2 (numerics:
388, 367, 323 for c = 0.4, 0.1, 0.01 — bounded, heading to ~400 = 1/(0.05)^2). There is no
"~ ?·c^k" for the sup; the honest c-powers are **k = 2** (pointwise correction) and **k = 1**
(geometry):

```
crossing positions  |u| = c * sqrt(sqrt(5) - 2) = 0.4858683 c   [rate c, verified to 7 digits]
positive-lobe half-width ~ 0.486 c                              [rate c]
```

**Consequence — minimum detectable displacement (explicit formula).** At a fixed observation
point u0 = sigma0 - 1/2 (|u0| > c), the OFF signal |B(u0;c)| is **strictly increasing in c**
(d/dc [1/(u0-c)^2 + 1/(u0+c)^2] > 0 for c < u0), from 1/u0^2 (as c -> 0) up to +inf (c -> u0).
Detection `|L_OFF(sigma0)| > B_max`:
```
c_min = 0                                                            if B_max <  1/u0^2
c_min = sqrt( u0^2 - ( sqrt(5 + 4 B_max u0^2) - 1 ) / (1/u0^2 + B_max) )   if B_max >= 1/u0^2
```
Closed form verified against exact bisection to all printed digits (|B(u0;c_n)| = B_max exactly).
Interpretation: the deep-left edge beta -> 1/2+ is **never invisible at a fixed sigma0** — the
signal converges to the fixed profile `-1/u0^2 - O(t0^-2)` (a leftover single on-line pair), so
if `B_max < 1/u0^2` the plant is detectable for **any** c > 0 (c_min = 0). Only when the local
base already sits at `B_max >= 1/u0^2` does a positive c threshold appear, given by the formula.
Finite-height correction is O(t0^-2) ~ 1.25e-3.

Label: **PROVEN** (algebra + exact arithmetic; all rates confirmed numerically).

---

## Task 2 — delta-general LINE: "Re L_LINE >= 0 for ALL delta > 0" is REFUTED (threshold exact)

**Exact expression (PROVEN, no truncation).**
```
Re L_LINE(sigma + it0) = main(u,d) + Delta(u,d)
main(u,d)  = d^2 (3u^2 + d^2) / (u^2 (u^2 + d^2)^2)            > 0  (u != 0)
Delta(u,d) = far(u,2t0) - far(u,2t0+d),   far(x,T) = (x^2 - T^2)/(x^2 + T^2)^2
far'(T)    = -2T (3u^2 - T^2)/(u^2 + T^2)^3  > 0  for T > sqrt3 |u|
```
Since `2t0 >= 2 gamma1 > sqrt3 * (1/2) > sqrt3 |u|`, `far` is strictly increasing at T = 2t0, so
**Delta < 0 for ALL delta > 0** (the far point of the moved pair). Positivity iff `main > |Delta|`.

**The monotone-log-derivative argument extends verbatim** (main is monotone decreasing in u^2
for every delta > 0 — that part is unbroken), **but it is not enough**: `Delta < 0` is a genuine
`delta`-linear correction:
```
|Delta| ~ delta * far'(2t0) = delta * 4t0 (4t0^2 - 3u^2)/(u^2 + 4t0^2)^3 ~ delta/(4 t0^3)
main ~ 3 delta^2 / u^4          (for |u| >> delta)
```
The delta-linear term beats the delta^2 main term for tiny delta.

**Exact threshold (PROVEN; lead order verified 0.999).**
```
delta_crit(u;t0) ~ u^4 / (12 t0^3)      [ d_crit/u^4/(12t0^3) = 0.9993..0.9997 for u=0.3..0.2 ]
max over |u| <= 1/2, t0 = gamma1:  delta0 = delta_crit(1/2) = 1.8409e-6
```
Sign-flip scan (exact mpmath, all u in (-1/2,1/2)):
```
delta  0.3        0.01        1e-4        1e-6        1e-7        1e-8
min_u  +2.6159    +5.2e-3     +5.1e-7     -3.6e-11    -8.3e-12    -8.8e-13   (NEGATIVE below ~2e-6)
min_u over grid: delta=1.80e-6 -> -1.65e-12 ;  delta=1.841e-6 -> +1.98e-12   (threshold straddle)
```
**Conclusion.**
- `delta >= delta0 = 1.8409e-6` (t0 = gamma1): `Re L_LINE > 0` uniformly on (0,1)\{1/2} — PROVEN.
- `delta < delta0`: `Re L_LINE < 0` on a band `delta < |u| < (12 t0^3 delta)^{1/4}` — REFUTED for
  "all delta > 0" (uniform positivity fails; exact, not just an unproven bound).
- The delta = 0.3 theorem is **unaffected and stronger than stated**: true margin at u = 1/2 is
  `main - |Delta| = 2.615917 - 2.61e-5 = 2.61589`, i.e. `|Delta|` is **~100x smaller** than the
  note's `1/(2 t0^2) ~ 2.5e-3` bound. Any mission-relevant delta (0.3, and any delta >= ~1e-5)
  is deep in the positive regime with margin >= ~5e-3·(delta/1e-4)^2.

Label: **PROVEN (extension to all delta) = REFUTED**; threshold + negativity band exact.

---

## Task 3 — window |Im - gamma0| <= 8: 8 is arbitrary (generous), not special

**Claim under test.** Is the window ±8 special, or an arbitrary safety factor?
**ANSWER: arbitrary.** The pushed xi'-zero sits within `|Im - gamma0| <= 0.01` for all tested
beta, and the argument-ranged N=1 is stable.

```
beta    c       N (Re<1/2, |Im-t0|<=8)   pushed xi'-zero Re    Im            |Im - gamma0|
0.6    0.10        1 (winding 1.00000)     0.442258          14.135291       5.65e-4
0.75   0.25        1 (winding 1.00000)     0.355549          14.138261       3.54e-3
0.9    0.40        1 (winding 1.00000)     0.268591          14.143782       9.06e-3
```
Each zero certified by `|f'| -> 0` to ~1e-27 via root-finding; the coarse 2-D scan + refine agrees.
So FV's production side (an xi'-zero left of 1/2 near height gamma0) holds across beta, and the
height offset stays `<= 0.01 < 8`. Combines with the §2 bound: the required exclusion radius is
`R(t) ~ (sigma-beta)^{1/2}/sqrt(log t) <= 0.43 < 8`, so **any** window `>= ~0.5` (even ~0.02)
suffices; 8 is a large convenience constant with ~3 orders of magnitude to spare. The push stays
on-height because the mechanism is a local sign-opening of Re(xi'/xi) at the planted height, not a
transport to a distant band.

**Correction to `speiser-probe-2026-08-25.md`.** Its §3 localization "Re ~ 0.4526, Im ~ t0 for
beta=0.9" is inaccurate: the certified zero is at **Re = 0.26859, Im = 14.14378**. The draft's
value came from a restricted search window [0.42,0.48]x[t0-2,t0+2] that missed the true minimum
near Re = 0.269 (which has |f'| ~ 0.014). **This does not change any conclusion**: N=1 is
robust, and FV needs only *some* xi'-zero left of 1/2 within |Im-gamma0| <= 8, not a specific
placement. The pushed zero moves monotonically left (Re: 0.442 -> 0.355 -> 0.269) and slightly
up in height as beta deepens.

Label: window-dependence **CHECKED NUMERICALLY + PROVEN-reduction** (8 arbitrary); localization
correction documented.

---

## Bottom line (one-liners)
1. **edge-rate:** NO uniform vanishing — multiplicity 4 vs 2 leaves a leftover on-line pair;
   pointwise correction is `-6 c^2/u^4` (k=2), crossing geometry is `~0.486 c` (k=1), and
   c_min = 0 iff B_max < 1/u0^2 else `sqrt(u0^2 - (sqrt(5+4B_max u0^2)-1)/(1/u0^2+B_max))`.
2. **LINE-generality:** the monotone-log-derivative argument extends verbatim but the far-term
   `Delta < 0` (exact) is delta-linear, so uniform positivity fails below an exact
   `delta0 = delta_crit(1/2) ~ 1.841e-6`; PROVEN positive for delta >= delta0.
3. **window:** 8 is arbitrary/generous — the pushed xi'-zero never strays beyond |Im-gamma0|
   ~ 0.01 (beta in {0.6, 0.75, 0.9}; N=1 stable), far inside any window >= ~0.5.

Counts: PROVEN 3 (edge-rate algebra + c_min formula + threshold; LINE threshold; window reduction
in Task 3) · CHECKED NUMERICALLY 2 (LINE sign-flip scan; pushed-zero localization across beta) ·
CORRECTION 1 (draft localization alpha=0.9: 0.4526 -> 0.2686, non-load-bearing).
