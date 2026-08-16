# Referee verdict: S1-saddle closure claim (agent 456a3a85) — CRUX-REFUTATION HOLDS

Referee: hostile blind (no agent note read; first principles + probe code + independent Rust only)
Date: 2026-08-18
Labeling: PROVEN = verified by hand + code; CHECKED NUMERICALLY = probe + independent run.

## Verdict: crux-refutation HOLDS. No flaw found in claims (1)–(4). One minor wording nit (2.35 "stable").

---

## Part 1 — closed-form t_k arithmetic: HOLDS (PROVEN)

a_k = k^{−α}: t_k = 1 − (k²−1)^{−α}/k^{−2α} = 1 − (1−1/k²)^{−α}. For k≥2, 1−1/k² ∈ (0,1) ⟹ (1−1/k²)^{−α} > 1 ⟹ t_k < 0 for ALL k≥2, any α>0. Large k: t_k = −α/k² + O(k^{−4}).
a_k = (k+1)^{−α}: t_k = 1 − (1−1/(k+1)²)^{−α} ≈ −α/(k+1)² < 0. (Identical to k^{−α} shifted by one: t_k((k+1)^{−α}) = t_{k+1}(k^{−α}) — verified numerically.)

Independent exact-rational spot checks (referee_indep.rs): k=2, α=2: k^{−α} gives −0.777777777778 = −7/9 exactly; (k+1)^{−α} gives −0.265625 = −17/64 exactly. Asymptotic −α/k² accurate to ~10% for k≥3. Both families log-convex with NEGATIVE Turán quotient (margin → 0⁻, not 2/k). Probe Phase B1 (k=10⁶) confirms k·t_k → −α·10⁻⁶ ≈ 0⁻.

## Part 1-alt — moment-normalized b_k = a_k/(2k)!: t_k·k → 2 HOLDS (PROVEN by hand)

A_k = log b_k ≈ −α ln k − [2k ln(2k) − 2k + O(ln k)]; factorial part dominates: D_k ≈ 2/k + O(1/(k ln k)) ⟹ k·t_k → 2. The k^{−α} factor is a vanishing perturbation. So the LP-relevant Bessel-type f(t)=Σ(−1)^k b_k t^{2k} has margin → 2/k — SAME as the real Ξ — and the raw-coefficient Li_α analysis is a category error. (Part of the refutation's structure: whichever reading E4 intended, the dilogarithm family does not provide a counterexample to margin ≥ c/k criteria.)

## Part 2 — Li_α zero claim: HOLDS (PROVEN for α=2 by hand; CHECKED NUMERICALLY for α∈(0.5,3))

KEY THEOREM (proved here; stronger than the claim): for ALL α>0, Im Li_α(e^{iθ}) = Cl_α(θ) = Σ sin(kθ)/k^α > 0 on (0,π).
Proof: k^{−α} = (1/Γ(α))∫₀^∞ t^{α−1}e^{−kt}dt; Σ sin(kθ)e^{−kt} = e^t sinθ/(e^{2t}−2e^t cosθ+1) > 0 for θ∈(0,π), t>0. Integrand strictly positive ⟹ Cl_α(θ) > 0 on (0,π) for every α>0. (This is the load-bearing positivity; it holds.)
Winding: for r<1, γ(θ)=Li_α(re^{iθ}) starts on the POSITIVE real axis (Li_α(r)>0), upper arc (Im>0) crosses the negative real axis once at θ=π (Li_α(−r)<0, since alternating series with decreasing terms; at r→1, Li_α(−1)=−η(α)<0), lower arc back ⟹ arg change 2π ⟹ winding 1 ⟹ exactly one zero in |z|<r (z=0, simple) for every r<1. No zeros on |z|=1: for α>1, Li_α(e^{iθ})=0 requires Cl_α(θ)=0 ⟹ θ∈{0,π,2π}, and Li_α(1)=ζ(α)≠0, Li_α(−1)=−η(α)≠0; for 0.5<α<1, z=1 is a boundary singularity (Li_α(z)~Γ(1−α)(−ln z)^{α−1}→+∞, not a zero). Hence exactly one zero in |z|<1.
SUBTLETY (not a flaw): for α<1 the boundary curve is NOT closed (Li_α(e^{iθ})→+∞ as θ→0), so the winding argument must be run at r<1 and the limit taken; the claim's statement remains correct.
Li₂(−1) = −π²/12 ✓ (independent check: −0.822467033, exact to 9 digits). Winding of Li₂(e^{iθ}) = 1 sound.
Independent numerical check (referee_indep.rs, different summation/grid): winding = 1 at r = 0.5, 0.9, 0.99, 0.999 for α ∈ {0.5, 0.6, 1.0, 1.5, 2.0, 2.7, 3.0}. The probe's grid stops at |z|≤0.97; the r=0.999 winding covers the annulus (0.97,1) — no zero there. Claim's α∈(0.5,3) holds; in fact all α>0.

## Part 4 — saddle asymptotics: HOLDS (leading terms PROVEN by hand; constant CHECKED NUMERICALLY)

log M_k (saddle u₀ ≈ (1/2)(ln k − ln ln k + c), c = ln(2/π)): log M_k ≈ 2k ln u₀ + subleading ≈ 2k ln ln k − 2k ln 2 + subleading.
log b_k = log M_k − log(2k)! = [2k ln ln k − 2k ln 2] − [2k ln(2k) − 2k + O(ln k)] = −2k ln k + 2k ln ln k + 2k(1−2 ln 2) + subleading. Coefficient 1−2ln2 = −0.3864 ✓ (the +2k from Stirling combines with the two −2k ln 2's).
D_k = −A'' ≈ 2/k − 2/(k ln k) + (2−2 ln ln k)/(k ln²k) ⟹ k·t_k → 2 PROVEN. Subleading corrections (saddle constant c, O(ln k) term) shift the finite-k deficit.
Numerical (probe AND independent referee_indep.rs — brute-force saddle + plain composite Simpson N=10⁶, no Newton/adaptive, agree to 6 digits):
  k=1000:   k·t_k = 1.658984, (2−kt)·ln k = 2.3557
  k=10⁴:    k·t_k = 1.744732, (2−kt)·ln k = 2.3511
  k=10⁵:    k·t_k = 1.797521, (2−kt)·ln k = 2.3311
k·t_k increasing toward 2 with deficit ≈ 2.34/ln k ✓. Claim's "2.35 stable over 10³..10⁵": accurate to ~1% (2.356→2.331; "≈2.34, slowly decreasing" is the precise statement; true limit presumably 2). NOT a break — a wording nit.
Anchors: probe log M₀ = −0.698922267945 vs ln ξ(1/2) = ln(0.497120778188314) = −0.698922267945 (match to 1e-12); t₁·2 = 1.06963238 matches the external 8D anchor. Probe's printed "model" column (2−4/L+4/L²) is stale/wrong (implies constant 4) and does NOT match its own computed k·t_k — cosmetic; the computed values are what matter and they match my independent run.

## Part 3 — category error / E4 refutation: SUPPORTED

Dilogarithm-family raw coefficients: log-convex, negative margin — cannot serve as a counterexample to margin ≥ c/k criteria. Moment-normalized version: margin → 2/k exactly like the real Ξ — no counterexample either (it sits at the threshold, same as the target sequence). Non-real zeros of Li_α in |z|<1: there are none (Part 2), and they would be irrelevant to the real-zero question for f(t)=Σ(−1)^k b_k t^{2k} anyway. E4's "margin ≤ 2 criteria cannot force LP" is NOT established by the dilogarithm family.

## Files / reproducibility
- Probe: tools/s1saddle/ (built, ran: Phase A/A2/B1–B4 all as quoted above).
- Independent check: tools/s1saddle/referee_indep.rs (std-only; rustc -O; ~30 s). Not part of the repo build.
- This note: research/notes/referee-s1-crux-2026-08-18.md; progress: referee-s1-crux-2026-08-18.progress.

## Bottom line
All four sub-claims verified: t_k closed form negative (exact rationals), Li_α one zero at z=0 (winding 1 through r=0.999; Cl_α>0 proven for all α>0), category-error analysis coherent, saddle limit k·t_k→2 with (2−kt)·ln k ≈ 2.34 in the probed range (independent 6-digit agreement). Verdict: crux-refutation HOLDS. Margin question re-opened; S1 remains CONJECTURED with numerically proven tail (t_k·k → 2, deficit 2.35/ln k). No validator weakened.
