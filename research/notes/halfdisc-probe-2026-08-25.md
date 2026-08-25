# Half-disc Jensen-mass asymmetry probe — does A = M_right − M_left separate zero displacement TYPE?
Date: 2026-08-25 | Agent: builder | Status: COMPLETE (INCONCLUSIVE, ratio 1.41)

## Question (banked open question, from jensen-honest-build-2026-08-25.md)
The full-disc curvature-subtracted probe separates *perturbed zero sets* from the true
set, but the LINE control (zero moved to (1/2, t0+0.3), still on the line) separated
just as strongly — the machinery detected *any displacement*, not *off-line status*.
Open question: can a statistic distinguish OFF-LINE from ON-LINE zero displacement?
The proposed mechanism: zeros ON the line (Re ρ = 1/2) are fixed points of the mirror
map s↔1−s, so they should contribute EQUALLY to mirror half-discs cut by Re(s)=1/2;
off-line zeros (β=0.9, FE-mirror 0.1) are not mirror-symmetric and should contribute
UNEQUALLY. This build tests the half-disc Jensen-mass asymmetry
A(t0) = M_right − M_left, which the full-disc probe could not even define.

## The honest statistic (tools/jensen_halfdisc_probe.py, mpmath dps=15)
Disc D(c,r), center c = (1/2 ± small, t0), r = 0.3, cut at Re(s) = 1/2.
Half-disc Jensen mass (adapted), per half h in {right, left}:
- B_h = mean of log|ζ_planted| over the boundary arc with Re(s) in h
  (genuine function evaluation — the ONLY term that sees zeros OUTSIDE the disc,
  e.g. the β=0.9 plant at r=0.3; each half normalized by its own arc length).
- Z_h = Σ_{|ρ−c|<r, Re(ρ) in h} log(r/|ρ−c|)  (Jensen zero term restricted per
  half; on-line zeros with Re(ρ)=1/2 lie exactly ON the cut and are excluded from
  BOTH halves — this is the "fixed-point" rule).
- M_h = B_h + Z_h,  A(t0) = M_right − M_left = (B_right − B_left) + (Z_right − Z_left).
Both components reported separately; verdict uses A.
Model: the exact FE-symmetric planted construction of jensen_honest_probe.py
(finite Hadamard ratio R(s), no e^{s/ρ} factors; R(1−s)=R(s) exactly).

## Controls (pre-specified)
(a) 6 OFF-line implants β=0.9 at t0 = γ_1..γ_6 (FE mirror 0.1 forced);
(b) 6 ON-line implants at each of t0+0.3 and t0+0.5 (β=0.5, same exact machinery);
(c) permutation p-values, 1000 draws, conservative (1+#≥)/(1+1000);
(d) no-implant baseline at the same t0s.
Verdict: TYPE_SEPARATES iff p(off vs on-pooled) < 0.05 AND mean|A_off| ≥ 3·mean|A_on|
AND p(base vs on) ≥ 0.05. INCONCLUSIVE if off-line separates but ">>" or the baseline
condition fails. Configs: c_re ∈ {0.52, 0.48} × r=0.3 (the ±small mirror pair), plus
one diagnostic c_re=0.6, r=0.35 that reaches Re=0.95 so the Z term activates.

## Construction — all honesty checks PASS
```
planted zero at 0.9+it0 present:        |zeta_planted| = 0.00e+00
on-line zero at 0.5+it0 removed:        limit 0.0179
xi(s)=xi(1-s) for planted model:        |diff| = 2.19e-19   (FE exact)
beta=0.5 identity control == true zeta: |diff| = 0.00e+00
quadrature vs Jensen closed form:       |diff| <= 2.2e-16   (2 discs, true zeta)
```
### Fixed-point rule (Z term) is numerically EXACT as the hypothesis predicts
```
off-line (beta=0.9):  Z_right = +0.154151 (zero at 0.9 inside, dist 0.3<0.35)
                      Z_left  =  0.000000 (mirror 0.1 outside the disc)
on-line moved (0.5,t0+0.3):  Z_right = 0, Z_left = 0  (zero on the cut, excluded)
baseline:                    Z_right = 0, Z_left = 0  (all zeros on the cut)
```
CHECKED NUMERICALLY: the discrete mechanism the hypothesis names is real — an on-line
zero contributes to NEITHER half-disc, an off-line zero to one half. The failure of
the overall verdict is NOT in the Z term.

## Main result (primary config c_re=0.52, r=0.3) — raw means of A
```
BASE   mean(A_B)=-0.182  mean(A_Z)=0.000  mean(A)=-0.182   raw: -0.070 -0.145 -0.178 -0.215 -0.230 -0.255
OFF    mean(A_B)=-0.314  mean(A_Z)=0.000  mean(A)=-0.314   raw: -0.201 -0.276 -0.309 -0.346 -0.361 -0.387
ON+0.3 mean(A_B)=-0.196  mean(A_Z)=0.000  mean(A)=-0.196   raw: -0.083 -0.158 -0.191 -0.228 -0.243 -0.269
ON+0.5 mean(A_B)=-0.250  mean(A_Z)=0.000  mean(A)=-0.250   raw: -0.137 -0.213 -0.246 -0.283 -0.298 -0.323
p(off vs on)=0.029  p(base vs on)=0.268  ratio mean|A_off|/mean|A_on| = 1.41
```
- The Z term is entirely inert at r=0.3 (A_Z = 0 for every group — the disc cannot
  reach the β=0.9/0.1 plants), so A = A_B here. The boundary integral carries everything.
- Off-line separates from on-line statistically (p=0.029) but with ratio only 1.41,
  an order of magnitude short of the required ">>". There is no type separation.
- ON+0.5 (−0.250) drifts toward OFF (−0.314), away from baseline (−0.182): a larger
  ON-line displacement (0.5 > 0.3) produces |A| comparable to the off-line plant. The
  statistic tracks displacement MAGNITUDE, consistent with the prior full-disc finding,
  not on/off-line status.

## Mirror config c_re=0.48, r=0.3 (the "1/2 − small" twin)
```
BASE   mean(A)=-0.354   raw: -0.240 -0.316 -0.349 -0.387 -0.402 -0.427
OFF    mean(A)=-0.223   raw: -0.109 -0.185 -0.218 -0.256 -0.271 -0.296
ON+0.3 mean(A)=-0.341   raw: -0.227 -0.303 -0.336 -0.374 -0.389 -0.414
ON+0.5 mean(A)=-0.286   raw: -0.172 -0.249 -0.282 -0.320 -0.335 -0.360
p(off vs on)=0.019  p(base vs on)=0.288  ratio = 0.71
```
At c_re=0.48 the off-line group is *less* extreme than baseline and *closer to
on-line* in magnitude (ratio 0.71 — off-line |A| is SMALLER than on-line). The sign
of the off-line effect relative to baseline reverses between the two mirror configs.
There is no stable off-line signature.

## Diagnostic c_re=0.6, r=0.35 (disc reaches the off-line zeros; Z term active)
```
BASE   mean(A_B)=+0.067  A_Z=0.000  mean(A)=+0.067   raw: +0.195 +0.109 +0.071 +0.030 +0.013 -0.017
OFF    mean(A_B)=-0.304  A_Z=+0.154 mean(A)=-0.150   raw: -0.021 -0.108 -0.145 -0.186 -0.203 -0.233
ON+0.3 mean(A_B)=-0.005  A_Z=0.000  mean(A)=-0.005   raw: +0.123 +0.037 -0.001 -0.041 -0.059 -0.089
ON+0.5 mean(A_B)=-0.212  A_Z=0.000  mean(A)=-0.212   raw: -0.083 -0.170 -0.207 -0.248 -0.265 -0.295
p(off vs on)=0.4995  p(base vs on)=0.0090  ratio = 1.38
```
Even with the Z term contributing its full −0-/+0.154 off-line signal (exactly as the
rule predicts), OFF does NOT separate from the pooled on-line group (p=0.50): the
boundary integral B is the dominant, noisy term and swamps the clean but small Z
signal. Baseline separates from on-line (p=0.009) here — a spurious asymmetry.

## VERDICT: INCONCLUSIVE  (primary config ratio = 1.41; no config meets ">> + baseline≈on-line")
stdout: `INCONCLUSIVE` — effect size ratio off/on = 1.41.
Config (0.52,0.3) INCONCLUSIVE ratio 1.41 · (0.48,0.3) INCONCLUSIVE ratio 0.71 ·
(0.6,0.35) NO_TYPE_SEPARATION ratio 1.38.

## Honest interpretation (what this does and does not show)
- CHECKED NUMERICALLY (exact): the fixed-point rule in the Z term is precisely as the
  hypothesis states — on-line zeros (Re=1/2) are excluded from both half-discs, off-line
  zeros enter exactly one half. This part of the mechanism is real.
- BUT the half-disc asymmetry A does NOT separate displacement type: (i) the Z term is
  structurally subdominant — inert at r=0.3 and, even when activated (diag), only ±0.154
  against B-noise of comparable magnitude; (ii) the dominant term B (half-arc boundary
  integral of log|ζ|) has a NONZERO, geometry-dependent baseline because a disc centered
  at c_re = 1/2±small is not itself symmetric about the cut, and the two half-arcs sample
  different parts of the ζ background; (iii) the on-line control is not clean — a 0.5
  shift (larger than disc reach) produces |A| comparable to the off-line plant, and the
  off-line effect flips sign relative to baseline between the two mirror configs.
- Therefore: no evidence that a half-disc asymmetry certifies off-line status. The probe
  adds a second, independent confirmation that these Jensen-type local-function statistics
  respond to zero displacement *of any kind* (position and magnitude), not to the on/off-line
  STATUS of the displaced zero. This is consistent with, and extends, the g30/jensen-honest
  conclusion: it rules out the mirror-asymmetry route as a type-discriminator.
- No threshold was imposed beyond the pre-registered ratio ≥ 3 (">>") and the standard
  p<0.05; raw distributions are printed in full. Multiple configs: primary (0.52) fails
  the ratio test; (0.48) fails it in the opposite direction; diag fails p entirely.

## Honesty labels
- PROVEN (algebra): R(1−s)=R(s) for the finite planted ratio; on-line zeros are excluded
  from both half-sum Z (the fixed-point rule is exact, not approximate).
- CHECKED NUMERICALLY: all values above; FE exactness 2.19e-19; zero structure; restricted
  zero-sum values agree with theory to 1e-12; quadrature vs Jensen closed form 2.2e-16.
- INCONCLUSIVE / NO CLAIM about RH: the half-disc asymmetry does not separate displacement
  type as required; this is a negative result for the mirror-asymmetry route.
