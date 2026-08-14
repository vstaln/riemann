# Smooth-kernel certificate structure (P6): raised-cosine spectral window replaces the hard cutoff

Author: BUILDER (smooth-kernel). Date: 2026-08-14.
Scope: STRUCTURE of the pair-correlation certificate with the hard-cutoff kernel
replaced by a C^k band-limited kernel, finite-T error terms typed. No full verifier run.
Skills applied: s4h-design-simplicity (simplest smooth kernel that keeps the interval
machinery), s4h-constraint-hardness-testing (is "hard cutoff is essential" real?).
Labels per hooks/agents.md: PROVEN / CHECKED NUMERICALLY / CONJECTURED.

---

## 1. Where the hard cutoff actually lives (read from the verifier)

`tools/verify_coboundary_floor.py` class `KernelArb` (line 46) defines

    K(x) = Σ_j c_j · ½ [ sinc((w_j − 2πx)/2) + sinc((w_j + 2πx)/2) ]

with `sinc(z)=sin(z)/z`. Taking the Fourier transform in the `e^{−2πixξ}` convention
(the one forced by the `2πx` argument):

    K̂(ξ) = Σ_j c_j cos(w_j ξ) · 1_{|ξ| ≤ 1/2}           (PROVEN, 2-line computation)

Every member of the class is therefore **band-limited with spectrum supported in
[−1/2, 1/2]**, and the *shape* is a cosine polynomial on top of the spectral box
`1_{|ξ|≤1/2}`. The current frontier kernel `ktw = cosine_kernel(1.47)` (line 479) is
`c=[1], w=[1.47]`, i.e. `K̂(ξ) = cos(1.47 ξ)·1_{|ξ|≤1/2}`.

**The "hard cutoff" is the spectral box `1_{|ξ|≤1/2}`.** It is C^{−1} (a jump) at
ξ = ±1/2, which by classical Paley–Wiener forces the physical kernel to decay only
O(|x|^{−1}). This is the certificate-side dual of the physical-cutoff corner studied in
`attack-finitet.md` / `attack-finitet-cinf.md` (those smoothed the *physical* cutoff
φ_T; this note smooths the *spectral* box). Bandwidth-1 "as it actually enters" is
exactly `supp K̂ ⊆ [−1/2,1/2]`; the factor 2 vs the standard Montgomery
`supp f̂ ⊆ [−1,1]` is the 2π-convention bookkeeping, not mathematics (CONJECTURED-as-convention,
trivially re-scalable — the verifier's `w=(K/K0)²` pair kernel then has `supp ŵ ⊆ [−1,1]`
by convolution).

Constraint-hardness verdict: **"hard cutoff is essential" is ASSUMED, not hard.** The
verifier's own `trmdy_kernel` (line 126) is already a 7-term sinc combination, i.e. a
non-box spectrum — the box is a *choice*, not a necessity. The only real constraints
(Section 3) are: (i) closed-form Arb-evaluable K, K′, K″; (ii) `w=(K/K0)² ≥ 0` per cell;
(iii) `w″ ≥ 0` for the tangent prune. The box satisfies none of these uniquely.

## 2. The kernel: Fejér–Cesàro (raised-cosine) spectral family

**Choice (design-simplicity): the raised-cosine spectral window**

    K̂_m(ξ) = cos^m(πξ) · 1_{|ξ| ≤ 1/2},   m = 0, 1, 2, 4, …

For the modulated version that keeps the frontier's cosine shape, use
`K̂(ξ) = cos(αξ)·cos^m(πξ)·1_{|ξ|≤1/2}` with α = 1.47 (the frontier modulation).

**Why this and not a Gauss/bump C∞ window:** a C∞ bump (e.g. `exp(−1/(1/4−ξ²))`)
leaves the finite-sinc class — its physical kernel is not a finite combination of
sincs, so `KernelArb.kernel_derivatives` cannot evaluate it, and the interval machinery
breaks. `cos^m(πξ)` is a *finite cosine polynomial*, hence a finite sinc combination —
**it is a new instance of the existing `KernelArb`, zero new code**. That is the whole
design win. Raising m buys any finite decay rate; only super-algebraic (C∞) decay
requires leaving the class (flagged as the honest ceiling).

**Closed form (PROVEN, elementary).** Write `cos^m(θ) = 2^{−m} Σ_{k=0}^m C(m,k) cos((m−2k)θ)`.
Then

    K_m(x) = 2^{−m} Σ_{k=0}^m C(m,k) · ½ [ sinc(((m−2k)π − 2πx)/2) + sinc(((m−2k)π + 2πx)/2) ]

i.e. `KernelArb(coeffs = [2^{−m} C(m,k)]_{k=0}^m, omegas = [(m−2k)π]_{k=0}^m)`.
The modulated version has omegas `{±α ± (m−2k)π}` with coeffs `2^{−m} C(m,k)/2`.
Normalization `K0_m = ∫_{−1/2}^{1/2} cos^m(πξ)dξ`:
`K0_0 = 1`, `K0_1 = 2/π`, `K0_2 = 1/2`, `K0_4 = 3/8`, and generally
`K0_m = (2/π)·(√π/2)·Γ((m+1)/2)/Γ((m+2)/2)` (even m: `C(m,m/2)/2^m`).

Concrete instances:

| m | spectrum K̂ | regularity at ξ=±1/2 | physical decay K(x) | sinc terms |
|---|---|---|---|---|
| 0 | box `1` | C^{−1} (jump) | O(|x|^{−1}) | 1 (= hard cutoff) |
| 1 | `cos(πξ)` | C⁰ | O(|x|^{−2}) | 2 |
| 2 | `cos²(πξ)` = ½(1+cos 2πξ) | C¹ | O(|x|^{−3}) | 3 (Hann) |
| 4 | `cos⁴(πξ)` | C³ | O(|x|^{−5}) | 5 |

Decay column is classical Paley–Wiener: spectrum ∈ C^{m−1} with m-th derivative of bounded
variation ⟹ K = O(|x|^{−(m+1)}) (PROVEN). `cos^m` also has `K̂ ≥ 0` on the band, so K is
positive-definite (Bochner, PROVEN) — the pair-correlation admissibility is preserved.

**Recommended default: m = 2 (Hann, C¹ spectrum, O(|x|^{−3}) decay)** — the smallest
strictly-smoother-than-box member; m = 4 is the "more decay" knob. `w = (K/K0)²` is
normalized `w(0)=1` identically, matching the existing `k0` normalization.

## 3. Interval-bounding properties the verifier needs (read from signatures)

`box_lower(box)` (line 246) needs, per pair `(i,j)` with distance span `d = j−i`, the
range-minimum of `w = (K/K0)²` over cells `[left, right]` via `ranges.query` — a
precomputed `RangeMinimum` of `w_lower_on_cell` values (line 67). So it needs **w ≥ 0
(automatic, w is a square) and a computable rigorous per-cell lower bound** — no
monotonicity is actually assumed (RangeMinimum, not monotonicity, is the mechanism).

`tangent_lower(box, kernel, weights, pressure, grid, …)` (line 336) needs the Hessian of
F = Σ p_i g_i + Σ a_ij w(y_j−y_i) certified PSD, which uses `w_second_lower_on_cell`
(line 77): `w″ = 2((K′)² + K·K″)/K0²` over the same interval ranges (`second_ranges`).
So it needs **w″ ≥ 0 (convexity of w) over the pair-distance range**, evaluated in Arb
via `kernel_derivatives` (line 87) using `sinc_derivatives` (line 109).

**Correction (from the probe, Section 6): `w″ ≥ 0` is NOT required.** Line 368 of the
verifier clamps negative second derivatives: `scalar = _down(weights[(i,j)] * (s2 if s2 >= 0 else 0.0))`
— the tangent prune uses only the *positive part* of `w″`. Even the frontier hard-cutoff
kernel has `w″ < 0` on part of its range (probe: min −6.08 at x→0). So the real requirement
is weaker: the kernel stays inside `KernelArb`, and a kernel whose `w″` is more negative
over the pair range simply *loses tangent-prune power* (fewer `second_ranges` cells
contribute). **The smooth kernel keeps the machinery iff it stays inside `KernelArb`**
— which the raised-cosine family does by construction. This is the entire
interval-machinery compatibility statement; the convexity half of the task's brief is an
over-specification.

## 4. Finite-T error bookkeeping (typed)

Setup: zero window [T, 2T], normalized pair kernel w (supp ŵ ⊆ [−1,1]). The certificate
form is F = Σ p_i g_i + Σ a_ij w(y_j−y_i); its finite-T rigor rests on the explicit
formula for the pair sums. Typed terms:

**(a) Diagonal terms** — `Σ_i w(0) = N(T)` (w(0)=1). Riemann–von Mangoldt
(PROVEN, classical):

    N(T) = (T/2π) log(T/2π) − T/2π + 7/8 + S(T) + O(1/T),
    S(T) = (1/π) Im log ζ(1/2+iT) = O(log T)   [unconditional]

→ diagonal contributes a **log-type main term** `(T/2π)log(T/2πe)` and a **log-type error
`S(T) = O(log T)`** plus `O(1/T)`. Kernel-independent.

**(b) Pair main term** — `(T/2π) ∫ w(u)(1 − sinc²(πu)) du` (the O(T) pair correlation;
PROVEN structure, Montgomery 1973 / Goldston 1981). The kernel choice changes only the
integrand w — this is where the raised-cosine's `w(1) = 1/4` vs the box's `w(1) = 0`
enters (Section 6).

**(c) Prime strip (band-limited ⟹ short sum)** — the explicit-formula prime terms
`Σ_{m,n} Λ(m)Λ(n) ŵ(log(m/n))·(mn)^{−1/2}·…` are supported on `|log(m/n)| ≤ 1`, i.e.
`|m−n| = O(1)` (PROVEN — this is the standard consequence of `supp ŵ ⊆ [−1,1]`). Finite
range, O(1) coefficients, **no T growth**; kernel-independent beyond the ŵ values.

**(d) 1/T-type errors** — (i) Gamma/archimedean terms: O(1/T) (PROVEN, classical);
(ii) truncation of the finite window vs the full explicit formula. **This is the term the
smoothing moves:** the box spectrum (C^{−1}) gives O(1/T) truncation; the raised-cosine
C^{m−1} spectrum gives O(1/T^{m+1}) — the dual of `attack-finitet-cinf.md`'s proven
numerical fact that smoothing kills the Poisson k-sum truncation (O(1/K) → 2.7e-9).
Label: kernel-decay O(|x|^{−(m+1)}) PROVEN; the explicit-formula truncation improvement
CONJECTURED (dual transfer from the finitet note's numeric result, not yet re-derived here).

**(e) log-type errors** — `S(T) = O(log T)` (diagonal count) and nothing else at this
order; the band-limited prime strip contributes no log-T. Kernel-independent.

Net: **the smooth kernel changes exactly two entries** — the pair integrand w in (b)
and the 1/T truncation exponent in (d). Everything else is kernel-independent. The log-type
errors are NOT improved by smoothing (they live in the diagonal count, not the kernel).

## 5. Trade-off table: hard cutoff vs smooth kernel

| quantity | hard cutoff (m=0, box) | Hann (m=2, C¹) | m=4 (C³) |
|---|---|---|---|
| spectrum K̂ | `1_{|ξ|≤1/2}` | `cos²(πξ)·1` | `cos⁴(πξ)·1` |
| physical decay K | O(|x|^{−1}) | O(|x|^{−3}) | O(|x|^{−5}) |
| w(1) (=pair kernel at unit spacing) | 0.0034 (α=1.47; 0 only at α=π/2) | **0.25** | ? (probe) |
| pair main integrand ∫w(1−sinc²) | minimal (cosine minimizer, PROVEN in attack-kernel.md) | **larger** — raises the pair constant Q | larger still |
| diagonal terms | N(T) (unchanged) | N(T) | N(T) |
| 1/T truncation error | O(1/T) | O(1/T³) | O(1/T⁵) |
| log-type error S(T) | O(log T) | O(log T) — **unchanged** | O(log T) |
| prime strip | O(1), |m−n|=O(1) | same | same |
| interval machinery | existing | **same class, 3 sinc terms** | same class, 5 terms |
| w″ sign over pair range | mixed (min −6.08) — not required; verifier clamps | mixed (min −2.45) | probe |

**The cost/benefit (the structural finding).** Smoothing *buys* a better 1/T truncation
(d) but *costs* a larger pair constant (b): `attack-kernel.md` PROVES the cosine/box
minimizes the window functional Q, so any spectral taper moves the pair main term up —
exactly the direction `attack-finitet-cinf.md` measured for physical smoothing (Q rises
1.333 → 1.415 → 2.20 → 3.86 as taper mass moves off the corners). The box's O(1/T) error
is a *lower-order* term; the pair constant is the *leading* term. Therefore at the heights
where the certificate currently operates, **the hard cutoff wins: it trades a sub-leading
error for a better leading constant.** The smooth kernel becomes worth it only in the
asymptotic regime T → ∞ where O(1/T^{m+1}) vs O(1/T) matters more than the constant shift
— i.e. it is a *rigor-tightening* swap for the eventual T→∞ limit, not a record-pusher
at finite T. (CONJECTURED as strategy; the pair-constant ordering is PROVEN in
attack-kernel.md, the finite-T numbers are CHECKED NUMERICALLY in the finitet notes.)

## 6. Reduced numeric probe at the terminal cell (4220,8007,8027,8027,7995,4220)/4000

**CHECKED NUMERICALLY** — float probe using the verifier's own closed forms
(`sinc_derivatives` lines 109–115), step 0.0005, range [0,11], runtime ~1s (below the 1-min
budget). Span lengths `j−i` for the terminal cell's 15 pairs are
{3787, 3807, 8007, 20, 8027, 11794, 7995, 4202, 7995, 2, 4220, 3795, 8015, 40, 7995} (in
units of 1/4000); all are ≤ 3 in x-units except the two long pairs {11794, 8027} ≈ {2.95, 2.01}.

| kernel | w(0) | w(1) | w(1.5) | w(2.0) | min w″ on [0,11] | w″ at 1.0 |
|---|---|---|---|---|---|---|
| hard cutoff α=1.47 (frontier) | 1.0000 | **0.0034** | 0.372 (w″ −0.63) | 0.0014 | **−6.08** (at x→0) | +2.13 |
| raised-cosine mod, m=2 | 1.0000 | **0.2712** | — | — | −2.45 (at x→0) | +1.13 |
| raised-cosine no-mod, m=2 | 1.0000 | **0.2500** | — | — | −2.58 (at x→0) | +1.23 |

**Belief it changes (stated before running):** whether the smooth kernel keeps the tangent
prune viable or collapses it. **Result — the belief is CHANGED:** the tangent prune was
never gated on `w″ ≥ 0`; the verifier clamps `w″` to its positive part (line 368). The
smooth kernel's `w″` is *less negative* than the hard cutoff's (−2.45 vs −6.08) but also
*less positive* at the unit-spacing point (+1.13 vs +2.13); both kernels are partially
convex/partially concave on the relevant range. The smooth kernel therefore **keeps the
tangent prune, with roughly the hard cutoff's convexity profile**, but the pair-weight
mass at span 1 jumps 0.003 → 0.27 (raised-cosine) — the 1/T-error tightening is paid for
by an 80× larger kernel mass at unit spacing. That pair-main-term cost is the dominant
effect, exactly as the trade-off table predicted (CHECKED NUMERICALLY for the weights;
the certificate-level effect is CONJECTURED, unverified).

Note the hard cutoff's w(1) = 0.0034 (not exactly 0): α = 1.47 is off the first zero of
`cos(αx)/x`, so the "hard-cutoff w(1)=0" in the trade-off table holds only at α = π/2 ≈ 1.5708;
the frontier α = 1.47 was chosen to put the *minimizer* elsewhere.

## 7. Labels + next step

- Kernel closed form, bandwidth, decay, positive-definiteness, K0 values: PROVEN.
- Explicit-formula error types (diagonal S(T), Gamma O(1/T), band-limited short prime
  strip): PROVEN (classical literature).
- "Smoothing improves the 1/T truncation to O(1/T^{m+1})": kernel-decay half PROVEN,
  explicit-formula half CONJECTURED (dual transfer from attack-finitet-cinf.md).
- "Hard cutoff wins at finite T, smooth kernel is a T→∞ tightening": CONJECTURED
  (strategy), pair-constant ordering PROVEN, finite-T numbers CHECKED NUMERICALLY.
- "Hard cutoff is essential": ASSUMED — refuted as a *necessity*; the box is one member
  of a family the verifier already generalizes over.

**Next step (one):** implement `raised_cosine_kernel(m, alpha=1.47)` as a 6-line
`KernelArb` constructor in a scratch copy of `verify_coboundary_floor.py` (do NOT edit the
canonical tool), run the existing tangent prune on the recorded terminal cell, and confirm
whether the `w″ ≥ 0` certification survives — this is the single decision point that
decides if the smooth kernel is a drop-in or needs a convexity fix.
