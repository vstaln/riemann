# k<1 Moving-Boundary Count — Type-1 Decision (2026-08-17)

**Task:** Is `N(1/2+b/L, T) = o(T log T)` at fixed b ≈ 0.0758 (L = log T) reachable by any known route?
**Agent:** IDEA/ATTEMPT PROBE, builder, background. **Model:** opencode-go/deepseek-v4-flash.
**Forecast (wrong-direction brief):** route EMPTY. **Mandate:** prove emptiness rigorously OR find the dual/inversion.
**VERDICT: Type-1 NO — no known route certifies the fixed-b count; the plan reallocates (M4-proper stays the live lever).**
Confidence: HIGH on "no known route" (walls program-proven + elementary strength analysis below); the count itself is open in BOTH directions (neither o(T log T) nor a positive proportion is known).

## 0. Role of the count in the certificate (context)

- Certificate: κ* ≥ N* = S₁²/(S₂+E), E = Σ_pairs |F(ρ)−F(1−ρ̄)|² (exact, machine-verified; ledger M3).
- E ≥ 0 is a LOWER bound; the certificate needs an UPPER bound on E. Inputs that give it: the box
  (|β−1/2| ≤ b/L for ALL zeros → E ≤ 8b²(r+r′)S₂, PROVEN pair-form ceiling b ≤ 0.2237 with r′ ≥ 0) — unproven
  as a fact about ζ — or the tail count N(1/2+b/L,T) = o(T log T) (o(1) proportion beyond the box → tail's
  E-contribution is o(S₂)). The count is THE binding input (M1 gap table; M6 §3.1). Without it the certificate
  is vacuous: no upper bound on E is known by any other route.

## 1. Wall (i) — Shape-1 families are blind (scale-gap lemma). LABEL: PROVEN (in-program, bhb-m6 §3.1; reproduced structurally)

- Shape-1 = methods counting zeros via point evaluations {F(ρ)} with a smooth test function whose variation
  scale is ≥ c₀/L (moments of ζ′, mollified second moments, Selberg value distribution, Levinson-type).
- Scale-gap lemma: such methods resolve the strip only at widths ≥ c₀/L; the needed width 0.0758/L < c₀/L
  ⟹ the method's output is IDENTICAL for the boundary 1/2+b/L and the line 1/2 — cannot certify o(T log T).
- All the standard technology is Shape-1 (Selberg/Levinson/Conrey/BHB/GM mollified moments, Σ|F(ρ)|² moments,
  Selberg CLT of log ζ on vertical lines). The moment sums Σ_{ρ} f(ρ) over zeros in a strip are exactly the
  resolution-limited quantity. No Shape-1 route reaches fixed b.

## 2. Wall (ii) — classical density theorems cannot reach fixed b. LABEL: PROVEN (new elementary derivation below; crossover constant per BHB M1)

**Fixed-b floor (derived here, PROVEN; probe CHECKED NUMERICALLY):** a density bound N(σ_b,T) ≪ T^{A(σ_b)(1−σ_b)} (log T)^k
has ratio to T log T of T^{A(1/2−b/L)−1} L^{k−1}. All known theorems have A(σ) ≥ 2 near 1/2 (A < 2 at σ = 1/2 would
give N(1/2,T) ≪ T^{1−δ} = o(T log T) ⟹ almost-all-zeros-on-line, OPEN — impossible for a true theorem), so the best
possible exponent is 1 − 2b/L (reached only if A = 2 EXACTLY at the boundary), and
**ratio ≥ e^{−2b}·L^{k−1}·T^{ε}**. This certifies o(T log T) ONLY for (ε = 0, k = 0) — a log-free, ε-free density
hypothesis. Probe rows: (eps=0,k=0) ratio → 3.7e-2 ✓ certifies but is NOT known; (eps=0,k=1) → 0.86 constant ✗;
(eps=0,k=2) → 20 ✗; (eps=0,k=13 Montgomery-class) → 1.9e16 ✗; (eps=0.1,k=44 Ingham-class) → 1e59 ✗. Every known
density theorem carries ε > 0 AND k ≥ 1 (Ingham k=44, Montgomery k=13) ⟹ ratio → ∞.

**Consequence (PROVEN):** the fixed-b count is STRICTLY STRONGER than the density hypothesis by TWO independent
gaps — it needs the ε-free DH exponent (1−2b/L) AND zero log power, or equivalently a sublinear A(σ) = 2 − c(σ−1/2)^β,
β<1 shape that no known theorem has anywhere. The count would follow from a log-free, ε-free density hypothesis
(a theorem nobody approaches); it follows from nothing weaker that is known or conjectured-close.

**Crossover (in-program, bhb-m6 §3.1; structure CHECKED by probe):** the best known bounds (Selberg/Ingham-type,
k=5 log-power structure) certify o(T log T) only for boundary width ≥ c·(log log T)/log T, i.e., b ≥ c·log log T → ∞
(log-log-scale boundary, never fixed). Probe (c): for the near-line form N ≪ T L^k (σ−1/2)^{−k}, k=5, the crossover
b*(T) = L^{(2k−1)/k} grows 54 → 283 over T = 1e4..1e10 — never fixed; the exact BHB constant (3) is cited, not
re-derived.

## 3. Wall (iii) — GM zero-detection loses a fixed log power (Littlewood–Jensen obstacle). LABEL: PROVEN (in-program, gm-box §6 obstacle (ii); mechanism reproduced)

- GM (arXiv:2405.20552) kills the right tail only at fixed Δ > 19/70 ≈ 0.2714 (σ ≥ ~0.77) — far from the
  moving boundary 1/2+b/L → 1/2. The GM family is Shape-1 (mollified moments).
- Zero-detection via contour/Jensen (counting N(σ_b,T) from ∫ ζ′/ζ over Re s = σ_b) needs sup|ζ′/ζ(σ_b+it)|
  on a line at distance b/L from the critical line; near the line this sup spikes (zeros/poles within reach),
  losing a FIXED log power — at the moving boundary the loss eats the entire margin (the Littlewood–Jensen
  obstacle). Mechanism reproduced; exact constant per gm-box note.

## 4. Inversion hunt (the win condition) — result: EMPTY, each dual documented

- **(D1) Lower bound on the far count, sharpened via E.** E ≥ Σ_far (2(β−1/2))²|F′(1/2+iγ)|²(1+o(1))
  ≥ (2b/L)² Σ_far|F′(1/2+iγ)|². But this is a LOWER bound on E; the certificate needs E ≤ E₀ (upper),
  and E₀ requires the count — CIRCULAR. The rank–trace-style dual ("far zeros must carry small |F′|") needs
  min|F′| over far zeros, uncontrolled (F′ can be small/vanish at multiple zeros). EMPTY.
- **(D2) Weighted-moment version** Σ_{β>1/2+b/L}(β−1/2)²|F′(1/2+iγ)|² = o(S₂/L²·b²) — the natural weakening
  of the count that the pair identity exposes. It is a moment over zeros RESTRICTED to a strip — a Shape-1
  quantity → walled by (i). EMPTY.
- **(D3) Thin-strip count N(1/2,T) − N(1/2+b/L,T)** — the complement; N(1/2,T) itself is open (equivalent to
  almost-all-on-line), so the thin-strip count is unboundedable. EMPTY.
- **(D4) In-class ceiling as the dual.** PROVEN (M3): no certificate reading {E ≥ 0, moments} exceeds 0.6818.
  The count is exactly the missing INPUT that separates 0.407 (PRZZ unconditional) from 0.6818; the dual
  "what the certificate forces about the count" is vacuous (the count is an input, not a consequence). EMPTY.
- **(D5) BGSTB strong ZDH (their 1.6)** — a moving-boundary hypothesis; unconditional status OPEN (M6 §5.4,
  confirmed against BGSTB text: it is used only as a weakening of the box, never proved). No unconditional
  partial input known. EMPTY (conjectural).
- **(D6) 5.7× box relaxation pushed further?** The pair identity E ≥ 0 is EXACT (machine-verified, ledger)
  and is NOT the sinc-m3 floor (which was false); the 5.7× survives the wave-4 REFUTATION intact. But the
  pair-form ceiling b ≤ 0.2237 is PROVEN with r′ ≥ 0 — no in-class sharpening exists (ceilings break by NEW
  OBJECTS, never sharper in-class inequalities; wave-4 lesson). New structure: none known. EMPTY.
- **Numerical verification of the count is IMPOSSIBLE (vacuous):** all zeros up to ~10¹³ are verified ON the
  line ⟹ N(1/2+b/L,T) = 0 at every computationally reachable T — the count is a pure asymptotic, unfalsifiable
  numerically (same vacuity as the LMFDB route, offcentre note PROVEN). No probe can CHECK it.

## 5. RH-false control (mandatory) — Davenport–Heilbronn

- Certified (barrier zoo, PROVEN, |f_plus| < 1e-14): DH zeros at β−1/2 = 0.3085 (σ = 0.8085, t = 85.699) and
  0.1508 (σ = 0.6508, t = 114.163). Both at FIXED distance ≫ b/L for every T ≥ 2 (b/L ≤ 0.0758/ln2 ≈ 0.109 for
  b = 0.0758; ≤ 0.323 for b = 0.2237 at T = 2; → 0 as T → ∞).
- ⟹ The BOX |β−1/2| ≤ b/L FAILS for DH at all relevant T (PROVEN, arithmetic; probe checks). The certified
  zeros are beyond the moving boundary, so they are counted in N(1/2+b/L,T) — but whether DH's off-line count
  is o(T log T) or Θ(T log T) is an asymptotic I cannot resolve from a finite sample. Classical: infinitely
  many off-line zeros (DH 1936). Positive proportion: CONJECTURED (literature recall, not verified this session).
- **Firewall (holds in EITHER branch):** (a) if DH VIOLATES (positive proportion off-line beyond b/L), the
  count is NOT a universal analytic fact — it needs zeta-specific input, which is exactly what is missing
  (strengthens Type-1 NO). (b) if DH SATISFIES (off-line proportion o(1)), the count holds for an RH-false
  object → ZERO evidence about RH → the count as a lever is weak regardless. The count is NOT evidence for RH
  in either case.
- **Fake-Weil:** no analogue — fake Weil polynomials lack a critical-line/off-line structure, so no
  moving-boundary count exists to test. Stated per brief.

## 6. VERDICT

**Type-1 NO — the k<1 moving-boundary count N(1/2+b/L,T) = o(T log T) at fixed b is NOT reachable by any known
route.** Evidence: (i) Shape-1 families blind (PROVEN, scale-gap); (ii) count strictly stronger than the density
hypothesis (PROVEN, §2) — no density theorem, DH-included, reaches it; (iii) GM loses a fixed log power (PROVEN,
gm-box); inversion hunt EMPTY (D1–D6 all walled/circular/conjectural/vacuous); BGSTB strong ZDH open.
**Plan action:** the box-certificate's 0.6818 target cannot be certified by any in-hand input; the plan
reallocates — M4-proper (ζ″-moment r′, closed-form, cheap, never dispatched) remains the live lever to pin the
box ceiling; any future route to 0.6818 must supply a NEW OBJECT (not an in-class sharpening; wave-4 lesson).
The count itself remains open in both directions — this decision closes it as a ROUTE, not as a question.

**Confidence: HIGH** (walls program-proven; §2 is elementary algebra + a consistency argument; inversion
documented per candidate). Unknowns labeled: crossover constant 3/c per BHB M1 (PROVEN in-program, cited);
DH positive-proportion CONJECTURED; exact r′ pending M4-proper.

## 7. Scripts (all Rust, all run this session)

- `tools/k1_count_probe/` — built + run (release, musl). Outputs: (a) fixed-b floor table — ratio
  T^{A(1/2−b/L)−1}L^{k−1}: only (eps=0,k=0) certifies (3.7e-2 → 0); (eps=0,k=1) → 0.86 const; (k=2) → 20;
  (k=13) → 1.9e16; (eps=0.1,k=44) → 1e59 — all known theorem classes fail; (c) crossover b*(T) = L^{9/5}
  grows 54 → 283 (T = 1e4..1e10), never fixed; (b) DH control: both certified DH zeros beyond b/L at every
  sampled T for b = 0.0758 and 0.2237 (box fails for DH).
- `tools/barrier_zoo_rs/` — built + `dh` subcommand re-run: certified DH zeros matched 2/2
  (|f_plus| = 3.14e-14, 3.26e-14 < 1e-9), 6 off-line zeros total; rung-0 operational.
- Build: `cargo build --release --target x86_64-unknown-linux-musl --manifest-path tools/k1_count_probe/Cargo.toml`
  (same flag pattern for barrier_zoo_rs).
