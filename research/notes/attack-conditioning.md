# Attack: conditioning of the certificate functional — is the cosine a flat or sharp optimum?

**Agent:** EXECUTIONER (vector E5.4, idea-generator-earth.md + the conditioning idea)
**Date:** 2026 (Round 3+)
**Question:** the 0.6725 certificate's window is cos(√2u), the global minimizer of
Q(v) = [∫v² + ∬|s−s′|v(s)v(s′)]/(∫v)² over L²([−1/2,1/2]) (attack-kernel.md §1–§2, PROVEN). Is the
constant ROBUST (flat near the optimum — small window perturbations change the constant negligibly)
or LOAD-BEARING (sharp — the constant depends sensitively on being exactly at the cosine)?
**Verdict:** **ROBUST** — a 1% window perturbation (pointwise or L²) changes the certificate
constant by ~0.01–0.02% (quadratic in the perturbation, coefficient ≈ 1.2–1.5 relative), and the
second variation is nearly isotropic (condition number κ ≈ 1.05–1.25). One quantified caveat: the
C∞-compact-support boundary ramp (the cosine does not vanish at ±1/2) costs δ ≈ 0.45·w, linear in
ramp width — consistent with the attack-kernel note's "cost O(1/L)" only if the ramp's window-
coordinate width is O(1/L).
**Labels:** PROVEN (analytic) / CHECKED NUMERICALLY (script + command cited) / CONJECTURED /
INCONCLUSIVE (validator) — per hooks/agents.md.

**Code (final versions live in `tools/`):**
- `tools/attack_conditioning.py` — main second-variation / conditioning / perturbation-table run.
  Command: `uv run --quiet --with numpy python3 tools/attack_conditioning.py 2000` (also run at N=1000
  for convergence; all headline numbers agree to ≤ 1e-7).
- `tools/attack_conditioning_support.py` — supporting facts: ⟨1,T1⟩ = 1/3, conditional negative
  definiteness of |s−s′| on zero-mean functions, sin(πu) curvature −2/π², ramp linearity.
  Command: `uv run --quiet --with numpy python3 tools/attack_conditioning_support.py`.
- Machine note: the box was heavily loaded (load avg ~81, ~2GB free) during this run, so N=2000 was
  used instead of the validator's N=4000; the validator's analytic anchors
  (λmin = 1 − 2/π², λmax = 1 + 2/k², k = 2.399357) reproduce at N=2000 to ≤ 4e-7, and N=1000→2000
  convergence is shown (see §3).

---

## 1. Setup and the exact second variation (PROVEN, analytic)

M = I + T with (Tv)(u) = ∫_{−1/2}^{1/2}|u−v|v(v)dv,  Q(v) = ⟨v,Mv⟩/⟨v,1⟩².
v₀(u) = cos(√2u),  c = Q(v₀) = 1/2 + (1/√2)cot(1/√2) = 1.327499296320588
(discrete Q(v₀) at N=2000: 1.3274992199, diff 7.6e-8),  certificate constant 2 − c = 0.6725007036794116.

Two facts used (PROVEN in attack-kernel.md §2; spectrum CORRECTED by validation-001 target 2):
- Stationarity: Mv₀ = c·D₀·1, D₀ = ⟨v₀,1⟩ = √2 sin(1/√2) = 0.9187253699 (checked: max|Mv₀ − cD₀·1|
  = 2.7e-8 on the N=1000 grid).
- M ≻ 0 with λmin(M) = 1 − 2/π² = 0.79735763 (the validator's correction: the odd eigenfunctions
  sin((2m+1)πu), most negative −2/π² at sin(πu), were omitted from attack-kernel §2) and
  λmax(M) = 1 + 2/k² = 1.34740827, k = 2.399357 (even mode).

**The key identity (PROVEN):** on the affine hyperplane {⟨v,1⟩ = 1} the quotient is *exactly* a
quadratic form, Q(v) = ⟨v,Mv⟩. Hence for any perturbation w with ⟨w,1⟩ = 0, setting
v = (v₀ + εw)/D₀ (which has ⟨v,1⟩ = 1):

> **Q(v) = c + ε²·⟨w,Mw⟩/D₀²  EXACTLY** — no O(ε³) terms.

(The first-order term vanishes by stationarity: ⟨w,Mv₀⟩ = cD₀⟨w,1⟩ = 0.) So the second variation is
not a local approximation — the constant's response to normalization-preserving perturbations is
exactly quadratic at *every* amplitude ε. Verified numerically to ratio 1.00000000 at
ε = 10⁻³, 10⁻², 10⁻¹ for w = sin(πu) (tools/attack_conditioning.py).

**Hessian:** on the tangent space T = {⟨w,1⟩ = 0}, the Hessian of Q at the optimum is the quadratic
form H(w) = 2⟨w,Mw⟩/D₀². Its conditioning = the spread of ⟨w,Mw⟩/⟨w,w⟩ over w ∈ T (the constant
changes like δ = η²·(‖v₀‖₂²/D₀²)·(⟨ŵ,Mŵ⟩/⟨ŵ,ŵ⟩)·... for a relative-L² perturbation of size η,
see §3). The pure-scaling direction v₀ is exactly flat (Q(λv₀) = Q(v₀)), but it is *not* in T
(⟨v₀,1⟩ = D₀ ≠ 0); it is a symmetry, not a sensitivity.

---

## 2. The relevant spectrum (CHECKED NUMERICALLY — tools/attack_conditioning.py 2000)

Curvature ⟨w,Mw⟩/⟨w,w⟩ of the second variation over w ∈ T:

| subspace | λmin (flattest) | λmax (steepest) | κ = λmax/λmin |
|---|---|---|---|
| full T (any w, ∫w = 0) | 0.79735759 (= 1 − 2/π², direction sin(πu)) | 0.99999987 → 1 (supremum) | **1.2541** |
| T ∩ even (proof-constrained) | 0.94933937 | 0.99999987 → 1 | **1.0534** |

- λmin|_T = 1 − 2/π² because sin(πu) ∈ T (odd ⟂ 1) and it is the validator-corrected global minimum.
- λmax|_T → 1 exactly: |s−s′| is **conditionally negative definite**, ⟨w,Tw⟩ ≤ 0 for every zero-mean
  w (verified on 60 random zero-mean vectors, max = 0.0; ⟨1,T1⟩ = 1/3 > 0 is the single positive
  direction — tools/attack_conditioning_support.py). So on T, ⟨w,Mw⟩ = ⟨w,w⟩ + ⟨w,Tw⟩ ≤ ⟨w,w⟩, and
  the supremum 1 is approached by high-frequency modes (Tw → 0).
- Hessian eigenvalues on T (H = 2M/D₀², D₀² = 0.844056): 1.8893 … 2.3695.
- With the validator's correction (0.797 instead of the old 0.93): κ_full = 1.2541 (old value would
  have been 1.347/0.93 ≈ 1.45; even-older 1.347/0.797≈1.69 if λmax unconstrained). Either way the
  second variation is **very well conditioned**: no direction in T is more than ~25% steeper than the
  average, and none is flatter than ~0.80 — there is no hidden flat direction and no hypersensitive one.

**Absolute scale (the number that matters for the verdict):** ‖v₀‖₂²/D₀² = 0.849228/0.844056 =
1.0061, so for a relative-L² window perturbation of size η (‖εw‖₂ = η·‖v₀‖₂, η = 1% → 0.01):

> δ_rel = δ/0.6725 = η² · 1.496 · (curvature) ∈ η²·[1.19, 1.50].

Empirical confirmation (200 random directions, η = 0.01, i.e. **1% relative-L² perturbation**):
δ ∈ [1.0052e-4, 1.0061e-4], δ_rel ∈ [0.0149%, 0.0150%].

---

## 3. Perturbation table (CHECKED NUMERICALLY — tools/attack_conditioning.py 2000)

Pointwise perturbations: v = v₀ + 0.01·g, ‖g‖_∞ = 1 (a 1% sup-norm perturbation of a window whose
max is 1). δ = Q(perturbed) − c; the certificate constant becomes 0.6725007 − δ.

| window perturbation g | ⟨g,1⟩ | δ (1% pert.) | constant after | rel. change |
|---|---|---|---|---|
| sin(πu)  [odd] | 0 | 4.72e-5 | 0.672453 | **0.0070%** |
| cos(πu)  [odd] | +0.637 | 7.40e-6 | 0.672493 | **0.0011%** |
| cos(2πu) [even] | 0 | 5.62e-5 | 0.672444 | **0.0084%** |
| 4u²     [even] | +0.333 | 1.18e-5 | 0.672489 | **0.0018%** |
| frequency detune λ = √2·(1±0.01) | — | 2.54–2.61e-6 | 0.672498 | **0.0004%** |

- Frequency curvature: d²Q/dλ² at λ = √2 ≈ 0.0257 (three-point formula); δ(λ=√2(1±0.01)) = 2.6e-6.
- Polynomial (Chebyshev) approximations of cos(√2u): degree 4 is already within 3.6e-6 relative L²
  (1.2e-5 pointwise) of the cosine → δ = 1.3e-11 (rel. 1.9e-9%); degree ≥ 6 → machine zero
  (δ = 0.0). So any sane rational/spline/polynomial approximation of the cosine is *free*.
- Direct check of the exact identity: for sin(πu), Q(v₀+εg) − c = ε²⟨g,Mg⟩/D₀² to ratio 1.00000000
  at every ε tested; for ⟨g,1⟩ ≠ 0 shapes (cos(πu), 4u²) the leading coefficient is
  (⟨g,Mg⟩ − c⟨g,1⟩²)/D₀² and higher-order terms appear at O(ε³) as expected (ratio 0.986 at ε=0.01),
  so the table uses the *direct* Q evaluation (exact) for those rows.

---

## 4. Verdict: ROBUST (with numbers), one caveat

**1% window perturbation → ~0.01–0.02% constant change.** The dependence is exactly quadratic (no
linear term), with relative coefficient 1.19–1.50 and spread (condition number) 1.05–1.25. This is
flatness in the genuine sense: not a "valley" (that would be a near-flat direction, κ ≫ 1) and not a
needle (κ ≈ 1 with O(1) coefficient). Concretely: 1% → ≤0.02%; 0.1% → ≤2e-4%; 10% → ~1–2%; a
qualitatively different but still admissible window (box: δ = 0.0058, constant drops to 2/3, −0.87%;
(1−4u²): δ = 0.130, −19%) is *not* covered — the flatness is local, quadratic, around the cosine.

**The one non-quadratic caveat — the boundary ramp (NEW finding, quantified).** The cosine does NOT
vanish at ±1/2 (cos(1/√2) = 0.7602 ≠ 0), so any C∞ compactly-supported window — exactly what the
paper's construction requires (attack-kernel §1 constraint (iv), "fixed-width end ramp at cost
O(1/L)") — must deviate from the cosine by O(0.76) pointwise inside a boundary layer of width w.
Measured cost (linear ramp v = cos(√2u)·(d/w) on |u| ∈ [1/2−w, 1/2]):

| ramp width w | δ | rel. constant change |
|---|---|---|
| 0.005 | 0.0023 | 0.34% |
| 0.010 | 0.0046 | 0.68% |
| 0.020 | 0.0093 | 1.39% |
| 0.050 | 0.0240 | 3.57% |
| 0.100 | 0.0504 | 7.50% |

δ ≈ 0.45·w (linear; smooth-step ramp slightly worse, ≈ 0.51·w; δ/w → 0.450 as w → 0 —
tools/attack_conditioning_support.py). This is linear, not quadratic, because the layer's L² mass is
O(√w) (pointwise-large but thin), and the quadratic law then gives O(w). Two readings, both honest:

- (a) If the paper's ramp width in the window coordinate is O(1/L) (a *fixed number of grid cells /
  zero spacings*, so u-width ~ 1/N), then δ ≈ 0.45·(1/N) = O(1/L) — quantitatively consistent with
  the note's "cost O(1/L)". My measurement then *resolves* that claim to the coefficient 0.45.
- (b) If an implementation used a *fixed u-width* ramp (e.g. w = 0.01), the constant would drop by
  0.68% (0.6725 → 0.6679) — real, not negligible.
The paper's exact ramp construction is in its technical supplement (not in the repo), so the
connection is **CONJECTURED** (same class of caveat as the ξ′-quartic mechanism and EnclOK); what is
**CHECKED NUMERICALLY** is the ramp cost itself.

---

## 5. Practical implication for implementations (task 4)

**finitet's effective window is EXACTLY the cosine.** `tools/finitet/src/main.rs` uses
ψ(u) = cos(√2u)·1_{|u|≤1/2} (the idealized model, hard cutoff — no ramp), so Q(window) = c to f64
precision; the window contributes **zero** to the measured Δ(T) = bound/N − 0.6725 ∈ [+0.037, +0.047].
The deficit is finite-height arithmetic, exactly as the validator decomposed it (validation-001 target
3): (i) the k-truncation of the Poisson sum (HS2 vs HS2_an at T=700: 1.2838 vs 1.2869), and (ii) the
genuine pair-correlation deficit of the zeros at heights 100–1400 (HS2_an/N = 1.287 still 3% below
c = 1.3275). Note the sign: any boundary ramp would push the constant *down* (0.6725 − δ_ramp), the
*opposite* direction from the measured Δ(T) > 0 — so no window effect of any kind explains the
positive overshoot.

**On the "~1/log T decay" claim — no overclaim.** The validator flagged the note's §5 reading
INCONCLUSIVE: all three fitted laws (1/logT, 1/T, 1/log²T) have nonzero asymptotes (0.0141, 0.0371,
0.0283); convergence of bound/N to 0.6725 is not demonstrated by the data. This task does not touch
that question; the label stays INCONCLUSIVE (validator), and my finding only says the deficit is not
window-related.

**Concrete safety statements for implementations:**
- f64 evaluation of the cosine: relative error ~1e-16 → δ ~ (1e-16)²·1.5 ~ 1e-32. Nil.
- Rational/spline/polynomial approximations within 1% of the cosine (L² or pointwise): constant
  changes ≤ ~0.02%; Chebyshev degree 4 already gives δ < 1e-10.
- The only real implementation hazard is the boundary: keep the compact-support ramp at the
  resolution scale (a few grid cells), never a fixed fraction of the window — or account for the
  δ ≈ 0.45·w it costs.

---

## 6. Epistemic status

| Claim | Status | Basis |
|---|---|---|
| Q is exactly quadratic on {⟨v,1⟩=1}; Q(v₀+εw) = c + ε²⟨w,Mw⟩/D₀² exactly for ∫w=0 | PROVEN | analytic (stationarity + hyperplane quadraticity); numerically exact to 1.00000000 |
| Hessian on T = 2M/D₀²; curvature range [0.797,1] full / [0.949,1] even; κ = 1.2541 / 1.0534 | PROVEN + CHECKED NUMERICALLY | validator-corrected spectrum (1−2/π²) + conditional negative definiteness; tools/attack_conditioning.py 2000 (N=1000 identical to ≤1e-7) |
| Perturbation table (1% → 0.001–0.008% pointwise, 0.015% L²-generic, 0.0004% detuning, <1e-10 polynomial) | CHECKED NUMERICALLY | tools/attack_conditioning.py 2000 |
| Boundary-ramp cost δ ≈ 0.45·w (linear) | CHECKED NUMERICALLY | tools/attack_conditioning.py 2000 + attack_conditioning_support.py |
| "cost O(1/L)" of the paper's ramp ⟺ ramp u-width O(1/L), coefficient 0.45 | CONJECTURED | technical supplement not in repo (same caveat class as ξ′-quartic/EnclOK) |
| finitet window = exact cosine; Δ(T) not window-caused | CHECKED NUMERICALLY (finitet source) + validator decomposition | tools/finitet/src/main.rs; validation-001 target 3 |
| Δ(T) decays like ~1/log T | INCONCLUSIVE (validator) | validation-001 target 3 (nonzero fitted asymptotes) |

**Bottom line:** the 0.6725 constant is **ROBUST** — quadratic-flat at the cosine with relative
curvature ~1.2–1.5 and condition number ~1.05–1.25, so "almost-optimal" windows (1%-accurate
rational/spline/finite-precision implementations) are safe by ~2 orders of magnitude. The only place
the constant is load-bearing is the boundary ramp, which is a *structural* requirement (C∞ compact
support) not a numerical accident, and its cost is exactly linear in ramp width (≈ 0.45·w) — keep
the ramp at the resolution scale and it is O(1/L), consistent with the attack-kernel note. This
closes the E5.4 cheap probe: the bottleneck for the 0.6725 certificate is arithmetic (finite-height
pair correlation and the Poisson truncation, per validation-001 target 3), **not** fragility of the
window choice.
tic (finite-height
pair correlation and the Poisson truncation, per validation-001 target 3), **not** fragility of the
window choice.
