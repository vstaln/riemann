# Log-profile boundary probe — margin-2 approach-rate, LP consistency

**Date:** 2026-08-18. **Agent:** builder. **Status:** IN PROGRESS (partial note — deliverable seed).
**Labels:** PROVEN / CHECKED NUMERICALLY / CONJECTURED / INCONCLUSIVE per claim.

## Task (coordinator-corrected)
Family b_k(C,D) = k^{−C·k}·(ln(k+2))^{−D·k}, margin profile t_k·k ≈ C + D/ln k (PROVEN form:
f=ln b_k = −Ck ln k − Dk ln ln k ⟹ t_k = −f″ ≈ C/k + D/(k ln k)(1−1/ln k) ⟹ k·t_k ≈ C + D/ln k − D/ln²k).
**Deficit-2 profile t_k·k = 2 − 2/ln k ⟺ (C,D) = (2,−2)** — the target family is
b_k = k^{−2k}(ln(k+2))^{2k}. (Coordinator correction: the original brief's D=+2 was a sign error.)

Decisive questions:
(a) is (2,−2) [deficit-2 target] LP or non-LP?
(b) is the class {t_k·k ≥ 2 − 2/ln k} (C ≥ 2, or C=2 with D ≥ −2) LP-consistent on the scan?
(c) where is the non-LP boundary curve D*(C) — through (2,−2)? at D=0 (S1 line, known C*≈1.7–1.8)? elsewhere?

## Known anchors (from S1 probe note, cite)
- D=0, C∈[1.8,2.1]: LP-consistent. C=1.7 borderline-non-LP, C≤1.5 non-LP (genuine non-real zeros).
- k^{−2k} = (2,0): LP-consistent, margin 2 exactly.
- J₀(2t) b=1/(k!)²: margin 2−1/k, PROVEN LP (Bessel).
- S1 counterexample b_k = k^{−1.0696k} = (1.0696,0): NON-LP, margin 1.0696 — NOT in the deficit-2 class.
- S1 probe: LP-ness NOT determined by pointwise margin alone (perturbed margin-2 family, min margin 1.8786 > clean c=2's 1.875, was NON-LP).

## Method plan
- Reuse S1 probe machinery (tools/s1margin/probe.rs, probe2.rs, probe3.rs): section roots via
  Aberth–Ehrlich on R_N(w) (w=(t/S)²), genuine-vs-artifact via |t|-stability across N + Newton
  polish on the INFINITE series (immune to cancellation; control J₀ validates zero false-positives).
- One new bounded scan binary (Rust, std-only), grid (C,D): C∈[1.7,2.4], D∈[−3,3] coarse, then
  refine near boundary; decisive sub-question first: (2,−2) and C=2 line D∈[−3,0].
- Part B: Xi certified t_k·k (g02 oracle, k=10..250) vs the found boundary.

## Progress
- t=1..3: read s1-margin-probe note + g02 note + dirs. t=4: coordinator sign correction absorbed.
- NEXT: read probe.rs/probe2.rs/probe3.rs for exact t_k convention + root machinery; then write scan binary.
