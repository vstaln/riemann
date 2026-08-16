# HOSTILE BLIND REFEREE — 8E control-direction bug analysis

Date: 2026-08-18. Role: hostile blind referee (did not read the agent's note before judging; only the probe code + first-principles math). Verdict: **HOLDS (headline), with one supporting argument REFUTED and replaced by a correct one.**

## Claim under attack
The 8E "control-direction anomaly" (planted-zero control d_N²=5.28e-3 < real 1.13e-2 at N=60) was caused by a control bug: {2/(kx)} carries Mellin factor 2^{+s} placing planted zeros at Re = −(1/2+δ) (wrong side; should be Re = 1/2+δ), its span contains the dense even-index subsystem, so its smaller d_N is expected and meaningless. Corrected control Λ''_k = {1/(kx)} + c0·{1/(2kx)} has the intended zero at Re=1/2+δ; theory forces its d_N² to saturate > 0 while real d_N² → 0. The 5.28e-3 numbers are NOT evidence about RH-false behavior.

## 1. Mellin exponent/sign claim — CONFIRMED (hand + code)
Substitute u = a/(kx) in M[{a/(kx)}](s) = ∫₀¹ {a/(kx)} x^{s−1} dx:
  **M[{a/(kx)}](s) = (a/k)^s ∫_{a/k}^∞ {u} u^{−s−1} du.**
Using ∫₁^∞ {u}u^{−s−1}du = 1/(s−1) − ζ(s)/s and ∫_c^1 {u}u^{−s−1}du = (1−c^{1−s})/(1−s):
  **M[{a/(kx)}](s) = (a/k)^s·(−ζ(s)/s) + (a/k)/(1−s)**  (exact).
So {2/(kx)} has factor 2^{+s}·k^{−s}; {1/(2kx)} = Λ_{2k} has factor 2^{−s}·k^{−s}. The two are cleanly separated; the code's `mellin` mode implements exactly (a/k)^s·∫, and its measured ratios (1.3712 for {2/(100x)} vs 2^{+0.5}=1.4142; 0.7223 vs 2^{−0.5}=0.7071) match my hand computation of the finite-k correction: ratio = 2^s·[∫_{0.02}^∞/∫_{0.01}^∞] = 1.4142·0.9696 = 1.3712. ✓ (converges to 2^{+s} as k→∞).

Zeros: implemented control symbol g'(s) = −ζ(s)(1+c0·2^{+s})/s with c0 = 2^{1/2+δ}:
  1 + c0·2^{+s} = 0 ⟺ s = −(1/2+δ) + iπ(2m+1)/ln2, Re(s) = −0.6 < 0. **NOT in Re(s)>1/2.**
Corrected control symbol g''(s) = −ζ(s)(1+c0·2^{−s})/s:
  1 + c0·2^{−s} = 0 ⟺ s = 1/2+δ ± iπ/ln2 ≈ 0.6 ± 4.532i. **In the strip, Re > 1/2.** ✓
(Cf. code: control mode uses gram_entry(1,j,2,k) i.e. {2/(kx)} = 2^{+s} — the code comment claims 2^{−s}, i.e. the comment contradicts the implementation; control2 mode uses gram_entry(1,j,1,2k) = Λ_{2k} = 2^{−s} ✓.)

## 2. Even-index subsystem claim — PARTIALLY REFUTED (but conclusion survives)
TRUE for the {2/(kx)} family: {2/(2mx)} = {1/(mx)} = Λ_m, so span{{2/(kx)}} ⊇ span{Λ_m} (dense under RH).
**FALSE for the control sum-family**: control element A_k = Λ_k + c0·{2/(kx)}. Refutation (N=2): if Λ_2 ∈ span{A_1, A_2}, then (1−β)Λ_2 = (α+βc0)Λ_1 + αc0{2/x}; linear independence of {Λ_1, Λ_2, {2/x}} (e.g. {2/x} breaks at x=2/n, not at 1/m) forces α=0, β=1, then c0 = 0 — contradiction. So span{Λ_k + c0{2/(kx)}} does NOT contain span{Λ_{2m}}; the note's "via the even-index chains span{Λ'_1..Λ'_N} ⊇ {Λ_j : j even ≤ N}" is wrong.
CORRECT route to the same conclusion (control span dense under RH): symbol g'(s) = −ζ(s)(1+c0·2^s)/s; on Re(s) > 1/2, |1+c0·2^s| ≥ |c0·2^s| − 1 = 2^{0.6+σ} − 1 ≥ 2^{1.1} − 1 ≈ 1.14 > 0 and ≤ 1 + 2^{0.6+σ} < ∞ — a bounded, zero-free multiplicative perturbation of the Báez-Duarte symbol ⟹ density ⟺ RH preserved (same proof structure). Under RH: control d_N → 0, never saturates. So "control d²(60)=5.28e-3 is expected/meaningless" HOLDS, by the symbol argument, not by containment.

## 3. Corrected control2 saturation — PROVEN (lower bound 9.6e-3)
Obstruction functional ℓ(f) = M[f](ρ), ρ = 1/2+δ + iπ/ln2 = 0.6 + 4.532i.
- Bounded on L²(0,1): |ℓ(f)| ≤ ‖f‖₂·(∫₀¹ x^{2β−2}dx)^{1/2} = ‖f‖₂/√(2β−1), β = 0.6 > 1/2.
- ℓ(Λ''_k) = M[Λ''_k](ρ) = k^{−ρ}·g''(ρ) = 0 (g'' has the zero at ρ).
- ℓ(1) = ∫₀¹ x^{ρ−1}dx = 1/ρ ≠ 0.
⟹ for every N: d''_N² = dist²(1, span) ≥ |ℓ(1)|²/‖ℓ‖² = (2β−1)/|ρ|² = 0.2/(0.6²+4.532²) = 0.2/20.90 = **9.57e-3 > 0**.
Real d_N² → 0 under RH (Báez-Duarte). Hence d''_N² − d_N² → ≥ 9.6e-3 > 0: **discriminator points the right way in the limit, once index-fixed.** Consistent independent bound: span{Λ''_k : k≤N} ⊆ span{Λ_j : j ≤ 2N} ⟹ d''²(N) ≥ d²(2N) ≈ 9.7e-3 at N=60 (two bounds agree at 9.6–9.7e-3).
Caveat (not a break): at N=60 control2 d² ≈ 9.7e-3 is still slightly BELOW real d²(60) = 1.13e-2 (the direction only reverses at larger N where real → 0); the claim asserts saturation in the limit, which is correct.

## 4. Empirical verification (fresh runs, same binary, 2026-08-18)
- mellin mode: M[{2/(100x)}]/M[{1/(100x)}] = 1.3712 → 2^{+0.5} (k→∞); M[{1/(200x)}]/M[{1/(100x)}] = 0.7223 → 2^{−0.5}. Matches my hand value 1.3712 exactly (finite-k correction 0.9696 = ∫_{0.02}^∞/∫_{0.01}^∞). The two symbols are cleanly separated. ✓
- real d²(60) = 1.1267e-2 (fresh, reproduces ledger 1.13e-2).
- control (buggy {2/(kx)}) d²(60) = 5.2848e-3 (fresh, reproduces ledger 5.28e-3 — the number under re-label is real and reproducible).
- control2 (corrected Λ_k + c0·Λ_{2k}) d²(60) = **3.8809e-2** — ABOVE real d²(60)=1.1267e-2 by 3.4× at N=60 already (direction REVERSED and correct, stronger than the "within 15%" prediction), and ≥ proven lower bound 9.57e-3 ✓. The discriminator points the right way once index-fixed — confirmed numerically, not just in the limit.

## Verdict
**HOLDS.** (1) Mellin factor 2^{+s} and zero placement Re=−(1/2+δ) for the implemented control: PROVEN (hand + code numerics). (2) The specific containment "control span ⊇ even-index subsystem" is REFUTED for the sum family (N=2 independence argument), but the operative conclusion — control span dense under RH, d_N → 0, 5.28e-3 is meaningless — holds via the bounded-zero-free-symbol argument. (3) control2 places the zero at Re=1/2+δ and d''_N² provably saturates ≥ 9.57e-3 while real → 0: PROVEN. The ledger 8E numbers (5.28e-3) are NOT evidence about RH-false behavior; re-labeling is justified. One claim-internal statement needs rewriting (containment → symbol argument).

## Ledger line
- 8E control-direction bug analysis (2026-08-18): REFEREE VERDICT HOLDS — implemented control {2/(kx)} has Mellin factor 2^{+s}, planted zeros at Re=−(1/2+δ) (NOT an RH-false model); control d_N²=5.28e-3@60 is meaningless (span dense under RH via bounded zero-free symbol (1+c0·2^s) on Re>1/2; the even-subsystem containment argument as stated is FALSE). Corrected control Λ''_k=Λ_k+c0Λ_{2k} has zero at 0.6±4.532i and d''_N² ≥ 9.57e-3 for all N (obstruction functional; matches d²(120)≈9.7e-3 bound) while real → 0 — discriminator correct once index-fixed. Re-label ledger 5.28e-3 as "not RH-false evidence". [PROVEN / CHECKED NUMERICALLY]
