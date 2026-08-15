# WAVE 8B — Speiser's criterion: ζ′(s) ≠ 0 in 0 < Re(s) < 1/2 (DIRECT RH attack)

**Date:** 2026-08-17. **Lever:** Speiser 1934: RH ⟺ ζ′(s) ≠ 0 for 0 < Re(s) < 1/2.
**Status:** COMPLETE. **Verdict:** LEFT-HALF-STRIP CENSUS EMPTY to T=5000 (CHECKED
NUMERICALLY, two independent methods) — evidence consistent with RH; control verified.

## 1. Machinery (tools/wave8b/src/, RUST, f64, certified bounds)
- `em.rs`: certified Euler–Maclaurin for Hurwitz ζ(s,a) AND ζ′(s,a), a∈(0,1], a=1 ⟹ ζ, ζ′.
  - ζ′ terms: main sum Σ−ln(k+a)(k+a)^{-s}; pole term N^{1-s}(−(s−1)lnN−1)/(s−1)²;
    half term −(lnN/2)N^{-s}; corrections C′_k = C_k(Σ_{j=0}^{2k−2}1/(s+j) − lnN),
    C_k = B_{2k}/(2k)!·(s)_{2k−1}N^{−s−2k+1}; |B|/(2k)! table copied from
    tools/argprinciple/src/zeta.rs (inflated 1+1e-14).
  - Error bounds (argprinciple style): Kahan main-sum rounding + trig-angle rounding +
    (3k+20)ε correction rounding + explicit EM remainder |R_K| ≤ 2|B_{2K}|/(2K)!·∏|s+j|/N·N^{1−σ}/(σ+2K−1).
  - Derivative remainder via Cauchy estimate (radius δ=0.1):
    |R_K′(s)| ≤ (1/δ)·2|B_{2K}|/(2K)!·∏_{j=0}^{2K−1}(|s+j|+δ)/N·N^{1−(σ−δ)}/(σ−δ+2K−1).
  - **Validation (BUG FOUND & FIXED):** initial ζ′ pole term divided by |s−1|⁴ with a conj((s−1))
    numerator = num/(s−1)³, not num/(s−1)² — produced a spurious ζ′-zero in [0.02,0.5]×[9,14].
    After fix, analytic ζ′ matches central-difference of certified ζ to ~1e-9 at 6 test points
    (diff 2.5e-10..3.5e-9 vs certified err ~1e-13; the FD itself carries O(h²)·|ζ‴| error).
- `main.rs`: argument-principle winding of ζ′ (and f′) on rectangles, adaptive subdivision
  to |Δarg| ≤ π/2 per segment (depth ≤ 12), certified |F|−err margins on contours;
  complex-secant refinement; grid-min locator (independent count).
- **Commands (all numbers below from release binary `tools/wave8b/target/release/wave8b`):**
  `control`, `left 10 5000 100`, `right 10 5000 100 0.02` (+ rerun step 0.04),
  `online 10 5000 0.05`, `interl 10 5000 0.05`, `realscan`, `dbg`, `locate 10 110`,
  `locate 110 210`, `locate 4900 5000`. Outputs: research/notes/wave8b-*.out.

## 2. Theory corrections to the brief's forecast (the inversion)
Forecast said "ζ′ has known zeros ON σ=1/2 (Fekete-type interlacing)". CORRECTED:
- **ζ′(1/2+it) = e^{−iθ(t)}(−θ′(t)Z(t) − iZ′(t))** (ζ(1/2+it)=e^{−iθ}Z, θ′>0). Hence
  ζ′(1/2+it)=0 ⟺ Z(t)=Z′(t)=0, i.e. ζ′ vanishes on the line ONLY at multiple zeros of ζ.
  For simple zeros: **ζ′ has NO zeros on σ=1/2.** (Derived; confirmed numerically:
  min|ζ′|−err on σ=1/2 over [10,5000] = 4.80e-2 > 0 at t=4589.7 — `online`.)
- **Interlacing belongs to ξ′ (Rolle), not ζ′:** ξ(1/2+it)=P(t)Z(t) real ⟹ d/dt ξ = P·H,
  H(t)=Z·P′/P+Z′, has ≥1 zero per gap (γ_n, γ_{n+1}). Numerically: **4521 H-sign-changes
  (= ξ′ zeros on the line) on [10,5000] ≈ RvM N(5000) = 4520.3 + 1** (`interl`) — one per gap,
  matches xiprime.rs (verified exactly one per gap to γ₁₀₀₀). Counts per 100-t band grow
  34 → 106, tracking N(T).
- **ζ′ real-axis (t=0): ζ′(σ) < 0 for all σ ∈ (0,1)** (`realscan`: ζ′(0.05)=−1.03 … ζ′(0.5)=−3.92
  … → −∞ at the double pole s=1). No real zeros in the strip; consistent with Speiser.
  (The ζ′=NaN at exactly (0,0) is a 0·∞ artifact of the correction 1/(s+j) at s=j=0 — outside
  all census regions, which start at σ=0.001, t≥4.)
- So the corrected picture: ζ′ zeros live in 1/2<σ<1 only (no left-strip zeros iff RH, no
  on-line zeros, no real-axis zeros); ξ′ interlaces on the line.

## 3. RH-false control (verified FIRST) — DISCRIMINATOR WORKS
Control: fake f(s) = ζ(s)·G(s) with G(s) = ∏_j ((s−ρj)²+γj²)((s−(1−ρj))²+γj²), ρ₁=0.3+15i,
ρ₂=0.25+28i (real symmetric quartic, G(1−s)=G(s), real on line ⟹ f has a functional equation
and Speiser-per-L structure; planted off-line zeros at ρ₁, ρ₂ — in the LEFT half-strip).
- Planted zeros verified: |f(0.3+15i)| = |f(0.25+28i)| = 0 exactly (G vanishes there).
- **f′ left-strip winding (windows [0.02,0.5]×[4,34]) = 2** (one in [14,19], one in [24,29];
  refined f′-zero at σ=0.4907, t=14.98 — inside the left strip). NON-EMPTY, as Speiser-per-L
  predicts from the planted off-line zeros.
- **Real ζ′ winding in the SAME windows = 0** everywhere (min certified margins 0.17–1.07).
- **DISCRIMINATOR: VERIFIED** — same machinery, same rectangles: fake f′ shows left-strip
  zeros, real ζ′ shows none. (The control would have caught a broken ζ′/winding pipeline: the
  pre-fix binary actually DID show a spurious winding=1 for real ζ′ on [9,14], caught by the
  finite-difference check and fixed — the bug is documented, not hidden.)

## 4. Real-ζ census (all CHECKED NUMERICALLY; binary+cmd above; outputs wave8b-*.out)
### (a) LEFT half-strip 0.001 < σ < 0.5, 10 ≤ t ≤ 5000 — **EMPTY** (the lever)
- ζ′ winding on [0.001,0.5]×[T,T+100], T=10..4900 (50 slabs): **TOTAL = 0.000000**,
  every slab winding 0; zero samples with |ζ′|−err < 0; global certified contour margin
  min 4.8e-2; interior-grid |ζ′|−err margins 1.6–2.8 (`left`). (t∈[4,10] also 0 per the
  control windows; t=0 axis negative per realscan.)
- Label: CHECKED NUMERICALLY (arg-tracking is adaptive-subdivision numerical, values certified
  pointwise). Not a proof. Consistent with RH via Speiser; also consistent with the PROVEN
  fact RH-below-3·10¹² (Platt–Trudgian) + Speiser ⟹ no left-strip ζ′ zeros below 3·10¹².

### (b) Elsewhere picture to T=5000
- **On σ=1/2: no ζ′ zeros** (min |ζ′|−err = 4.80e-2 > 0 over t-grid step 0.05; theory:
  zeros only at double zeros of ζ — all known simple).
- **Right half-strip [0.5,1]×[10,5000]: 2651 ζ′ zeros** (winding census `right`; identical at
  steps 0.02 and 0.04). Independently validated by grid-min+secant locator: exactly 5 in
  [10,110], 14 in [110,210], 73 in [4900,5000] — matching the per-slab windings 5, 14, 73.
  - Structure: sparse at low t (ratio ζ′-count/N(T) = 0.15 at t≈100 → 0.69 at t≈5000;
    total 2651/4520 = 0.586), first zeros at high σ: first five at
    (0.965,48.85), (0.849,60.14), (0.865,76.36), (0.864,88.18), (0.781,95.29); σ-min drifts
    down (0.78 at t≈50 → 0.54 at t≈4900) — the Levinson-type drift of ζ′ zeros toward
    σ=1/2 as t grows; σ spread at t≈5000 is 0.54–0.94.
- **ξ′ on the line: 4521 interlacing zeros** (one per gap, Rolle) ≈ N(5000)+1.

## 5. Verdict
- **Real ζ′ left-half-strip census EMPTY to T=5000 with certified pointwise bounds and
  winding 0 on every slab rectangle (two independent methods): evidence FOR RH.**
  Label: CHECKED NUMERICALLY — NOT a proof (finite computation; the winding's arg-unwrapping
  is numerical, though values are certified). No anomaly found → no escalation.
- **Control: VERIFIED** (fake with planted off-line zeros shows f′ left-strip zeros; real ζ′
  none) — the Speiser-per-L discriminator works on this machinery.
- Follow-ups (next budget): (i) verify the classical count theorem for ζ′ strip zeros
  (N_{ζ′}(T) vs N(T)) against the literature — the 2651 number is stable but unexplained by
  a simple formula at T=5000; (ii) extend the right-strip census to higher T to confirm the
  density ratio → 1; (iii) certify the winding rigorously (bound |ζ′/ζ″|-style arc control)
  for a PROVEN emptiness statement in a narrower band; (iv) the brief's (c) — the geometric
  reformulation (image of the critical line under ζ′ winding around the origin) is partially
  captured by the interlacing census; leave as future work.

## Labels
All statements PROVEN here: the arithmetic of the certified EM error bounds; ζ′(1/2+it)=0 ⟺
double zero (derivation); ξ′ interlacing (Rolle). All census numbers: CHECKED NUMERICALLY
(binary+cmd). RH itself: NOT claimed proved; the empty left-strip census is supporting evidence.
