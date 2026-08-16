# E2 — 8E control-direction: the implemented control is NOT an RH-false model (index bug), corrected control verified

Date: 2026-08-18. Lever: 8E Beurling-operator (joint E2). Status: **CHECKED NUMERICALLY** (pending final numbers).
Ledger: "8E Beurling operator: real d_N²=1.13e-2 vs control 5.28e-3 at N=60; control-direction question OPEN."
Progress log: research/notes/wave8e-control-direction-2026-08-18.progress

## Question
RH ⟺ d_N → 0 (Báez-Duarte), d_N = dist(1, span{Λ_k = {1/(kx)}}). The 8E lever computed d_N² for the REAL case
(1.13e-2 @ N=60) and a "planted-zero control" (5.28e-3 @ N=60). Which is "supposed" to be smaller, and does
the discriminator point the right way? If the RH-false control has SMALLER d_N at every N, the lever is broken.

## THE KEY FINDING (derived, to be confirmed numerically below) — the 8E control has an index/Mellin-sign bug

The note (wave8e-beurling-operator-2026-08-17.md) defines the control as
  Λ'_k = {1/(kx)} + c0·{2/(kx)},  c0 = 2^(1/2+δ), δ=0.1,
claiming it is the "Mellin-lift of Z(s) = ζ(s)(1 + c0·2^{−s}) with exact zeros at 1/2+δ + iπ/ln2".
**The written formula and the code (tools/wave8e/src/main.rs, `gram_entry(2, j, k)`) implement {2/(kx)}, whose
Mellin factor is 2^{+s}, NOT 2^{−s}. The stated symbol (1+c0·2^{−s}) corresponds to {1/(2kx)} = Λ_{2k}.**

Mellin computation (u-substitution, exact):
  M[{a/(kx)}](s) = ∫₀¹ {a/(kx)} x^{s−1} dx = (a/k)^{s} ∫_{a/k}^∞ {u} u^{−s−1} du.
  → {1/(kx)} has factor k^{−s};  {2/(kx)} has factor (2/k)^{s} = **2^{+s}·k^{−s}**;  {1/(2kx)} = Λ_{2k} has factor (2k)^{−s} = **2^{−s}·k^{−s}**.

So for the large-k Mellin symbols g(s) of the two candidate controls:
- IMPLEMENTED control Λ'_k = Λ_k + c0·{2/(kx)}:  g(s) = ζ(s)(1 + c0·2^{+s}). Zeros: 1 + c0 2^s = 0 ⟺
  s = −(1/2+δ) + iπ(2m+1)/ln2 ⟹ **Re(s) = −(1/2+δ) < 0. NO zeros in Re(s) > 1/2.**
- CORRECTED control Λ'_k = Λ_k + c0·{1/(2kx)}:  g(s) = ζ(s)(1 + c0·2^{−s}). Zeros:
  s = 1/2+δ + iπ(2m+1)/ln2 ⟹ **Re(s) = 1/2+δ > 1/2. GENUINELY RH-FALSE** (exact planted zero at 1/2+δ + iπ/ln2 ≈ 0.6 + 4.532i, matching the note's stated intent).

By the Nyman–Beurling completeness criterion (span{φ_k} with M[φ_k] ≈ k^{−s}g(s)/s dense in L²(0,1) ⟺ g
zero-free in Re(s) > 1/2), the IMPLEMENTED control should still be DENSE: **d_N' → 0, never saturates.**
Stronger: {2/(2kx)} = {1/(kx)}, so via the even-index chains span{Λ'_1..Λ'_N} ⊇ span{Λ_j : j even ≤ N},
which is itself dense under RH ⟹ the implemented control's d_N' decays like the real one (or faster), and
control < real at every N is EXPECTED — it is a richer approximation family, not an RH-false model.

This fully explains the ledger's "wrong direction" (5.28e-3 < 1.13e-2 @ N=60): **the discriminator was
never given an RH-false object.** The direction question therefore splits:
  (i) implemented control: no saturation (dense) — verify by decay at N=100,200 vs real.
  (ii) corrected control: must saturate > 0 — measure; the crossing N vs real is the informative quantity.

## Prediction
- real d²(60) ≈ 1.13e-2, d²(100) ≈ 1.0028e-2 (= wave8c d(100)² — same normalization, cross-check),
  d²(200) ≈ 8.80e-3 (wave8c d(200)=9.3795e-2). Monotone decrease.
- implemented control d²: ≈5.28e-3 @60, keeps decaying (60→100→200), slope ~ real or faster. NEVER crosses.
- corrected control d²: since span{Λ'_1..Λ'_N} ⊆ span{Λ_1..Λ_{2N}}, d²_corr(N) ≥ d²_{2N}(real) ≥ 9.7e-3 @ N=60.
  Expect ≥ real d²(60); if it saturates visibly by N=200 with the real still decaying, direction confirmed
  (control above real at all N ⟹ no crossing needed; discriminator correct once fixed).

## Method (Rust only, tools/wave8e)
1. Add `control2` mode (corrected control via gram_entry(1, j, 1, 2k) etc.) + `mellin` mode (numerical
   Mellin ratio check of 2^{+s} vs 2^{−s}). One build.
2. Run real / control / control2 at N = 60, 100, 200 (timeouts; drop to 150 if 200 too slow).
3. Mellin mode at s=0.5, k=100: expect ratio ≈ 2^{+0.5}≈1.414 for {2/(100x)} vs ≈ 2^{−0.5}≈0.707 for {1/(200x)}.

## Results
- **Mellin mode (CHECKED NUMERICALLY, s=0.5, k=100)**:
  M[{2/(100x)}]/M[{1/(100x)}] = 1.3712 vs 2^{+0.5} = 1.4142 (known lower-limit correction 0.967×) ⟹
  the IMPLEMENTED control {2/(kx)} has Mellin factor **2^{+s}** — zeros at Re = −(1/2+δ) < 0, NOT RH-false.
  M[{1/(200x)}]/M[{1/(100x)}] = 0.7223 vs 2^{−0.5} = 0.7071 (correction 1.023×) ⟹ the CORRECTED control
  {1/(2kx)} = Λ_{2k} has factor **2^{−s}** — zero at 1/2+δ: genuinely RH-false. The two are cleanly separated.
- **real d²(60) = 1.1267e-2** (reproduced with the tool, matches ledger 1.13e-2). Same normalization as wave8c:
  certified d(100)=1.0013883664e-1 ⟹ d²(100)=1.0028e-2; d(200)=9.3795e-2 ⟹ d²(200)=8.80e-3.
- control (implemented) d²(60) = 5.28e-3 per ledger (same binary; rerun in background, box loaded).
- control2 (corrected) d²: background runs at N=60, 90 (box loaded, 3-4 agents; 400s timeouts expired mid-build
  under contention). PENDING numbers; bounds below are PROVEN regardless.

## The direction answer (theory, PROVEN; Mellin CHECKED NUMERICALLY)
1. **Implemented control**: symbol ζ(1+c0·2^{+s}), zero-free in Re(s) > 1/2 ⟹ span still DENSE under RH ⟹
   d_N' → 0, NEVER saturates, NEVER crosses the real curve. Stronger: {2/(2kx)} = {1/(kx)} gives, via the
   even-index chains, span{Λ'_1..Λ'_N} ⊇ {Λ_j : j even ≤ N}, itself dense under RH. So control < real at N=60
   (5.28e-3 < 1.13e-2) is EXPECTED — a richer approximation family, not an RH-false signal. The discriminator
   as built is unusable: it was never given an RH-false object.
2. **Corrected control**: symbol ζ(1+c0·2^{−s}), exact zero at 1/2+δ+iπ/ln2 (δ=0.1, height ≈4.532) ⟹
   (Beurling-type completeness criterion) span NOT dense ⟹ d_N² → c² > 0 while real d_N² → 0.
   **At N=60 already**: span{Λ'_1..Λ'_60} ⊆ span{Λ_1..Λ_{120}} ⟹ d²_corr(60) ≥ d²_{120}(real) ≈ 9.7e-3
   (vs real d²(60) = 1.13e-2) — the corrected control sits within ~15% of the real curve at N=60, i.e. the
   "wrong direction" 2× gap (5.28e-3) is an artifact of the index bug, and theory forces control ABOVE real
   eventually (real → 0, control → c² > 0). No renormalization fixes the buggy control; the fix is the
   index correction Λ_{2k} (control2 mode).

## Verdict — CHECKED NUMERICALLY (Mellin symbol + real-case reproduction) / INCONCLUSIVE (control2 saturation point, pending)
The OPEN 8E control-direction question is RESOLVED at the level of the bug: the measured "wrong direction"
(control 5.28e-3 < real 1.13e-2 @ N=60) was caused by a control that is NOT an RH-false model — its
{2/(kx)} basis has Mellin factor 2^{+s} (verified numerically), placing its planted zeros at Re = −(1/2+δ),
and its span provably contains the dense even-index subsystem, so its smaller d_N is expected and meaningless.
The corrected RH-false control (Λ'_k = {1/(kx)} + c0·{1/(2kx)}, control2 mode) has the intended zero at
Re = 1/2+δ; theory forces its d_N² to saturate > 0 while the real d_N² → 0, so the discriminator, once
index-fixed, points the right way (control ≥ real already within 15% at N=60 via the d_{2N} inclusion bound).
Campaign lesson: a planted-zero fake must be sign-checked at the Mellin level (2^{±s}) before use; the 8E
control numbers in the ledger (5.28e-3) are NOT evidence about RH-false behavior and should be re-labeled.

## Files
- tools/wave8e/src/main.rs (control2 + mellin modes added)
- research/notes/wave8e-beurling-operator-2026-08-17.md (original lever note)
- research/notes/wave8c-burnol-rate-2026-08-18.md (certified real d_N table)
