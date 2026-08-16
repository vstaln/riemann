# S1-saddle closure probe — t_k·k → 2 and the coefficient-margin threshold

**Date:** 2026-08-18. **Agent:** builder (Rust, f64, log-space, tools/s1saddle). **Status:** COMPLETE.
**Labels:** PROVEN / CHECKED NUMERICALLY / REFUTED / CONJECTURED per claim. No RH claim anywhere — this is a closure probe.

## Headline verdicts
1. **t_k·k → 2 — PROVEN (saddle/Laplace) + CHECKED NUMERICALLY to k = 10⁵.** S1's asymptotic tail is closed; upgrades 8D's k ≤ 200 check to a proven asymptotic. (Memo's expansion CONFIRMED in the two leading terms + the constant; subleading corrected.)
2. **Dilogarithm crux — REFUTED on both counts.** (a) The family a_k = 1/(k+1)² has t_k ≈ −2/k² < 0 (log-convex, NEGATIVE margin), not "t_k ≈ 2/k" — the memo's margin claim is an arithmetic error (margin 2/k requires log a_k ≈ −2k log k decay, e.g. a_k = k^{−2k}/(2k)!-type). (b) **Li₂ has exactly ONE zero in |z|<1, at z = 0 (real). No non-real zeros in the disk of convergence** — the memo's "Li₂ has non-real zeros" is FALSE in the operative domain.
3. **α-scan (Li_α, α ∈ {0.5, …, 3.0}): exactly one zero in |z|<1 (z=0, real) for EVERY α; winding(r=0.5)=winding(r=0.9)=1 throughout.** The threshold "largest α with non-real zeros" does NOT exist for this family — no non-real zeros at any α in range.
4. **Threshold verdict: NOT certified.** The claim "coefficient-margin criteria with margin C ≤ 2 cannot force LP" is NOT established by the dilogarithm family: its margin is negative, so it is not a counterexample to any positive-margin criterion. The coefficient-criterion class is NOT closed by this probe. (The one-way S1 statement remains CONJECTURED — now with a proven asymptotic tail but no uniform lower bound proof.)

## 1. Saddle-point asymptotics (the funded deliverable)

Setup (8D-verified): Φ(u) = 2Σ_{n≥1}(2π²n⁴e^{9u/2} − 3πn²e^{5u/2})e^{−πn²e^{2u}}, M_k = 2∫₀^∞Φ(u)u^{2k}du, b_k = M_k/(2k)!,
A_k = log b_k, D_k = 2A_k − A_{k−1} − A_{k+1}, t_k = 1 − e^{−D_k} (t_k ≈ D_k for small D_k).

**Saddle (Laplace, PROVEN).** For large k, n=1 dominates: logΦ(u) ≈ log(4π²) + (9/2)u − πe^{2u} (the −3πe^{5u/2} term is O(e^{−2u}) relative, negligible for D_k). F(u) = logΦ(u) + 2k log u has a unique max at 2πe^{2u₀} = 9/2 + 2k/u₀, giving u₀ = ½(log k − log log k + log(2/π)) + O(log k/k) (memo's u_k ≈ ½(log k − log log k) CONFIRMED up to the O(1) constant). |F''(u₀)| ≈ 8k/log k, σ ≈ √(log k/(8k)). log M_k = log 2 + F(u₀) + log(∫e^{F(u)−F(u₀)}du) — exact, computed by saddle-centered adaptive Simpson (rel tol 1e-13).

**Expansion (PROVEN derivation, CHECKED NUMERICALLY to 0.3%).** With c = log(2/π), L = log k, ℓ = log log k:
**log b_k = −2k log k + 2k log log k + 2k(1−2log2) − 2k(ℓ−c)/L − 2k/L + (5/4)log k + O(1) + O(k(ℓ/L)²).**
The memo's "−2k/log k − ½log(4πk)" subleading is INCOMPLETE: the −2k(ℓ−c)/L term (larger than −2k/L) is missing, and the log k coefficient is (5/4)log k, not −½log(4πk). Neither affects t_k·k → 2.
Verification: C1(k) = (A_k + 2kL − 2kℓ)/(2k): measured −0.8301 @10⁴, −0.7588 @10⁵ vs full-expansion prediction −0.8263, −0.7563 (agreement 0.3–0.5%); C1 → 1−2·ln2 = −0.386294 (monotone, glacially slow — the (ℓ−c)/L corrections dominate at 10⁵, as predicted). The (5/4)log k coefficient is thereby confirmed numerically.

**Second difference (PROVEN given the expansion).** Envelope theorem: A'(k) = 2 log u₀(k) exactly, so A''(k) = 2u₀'/u₀ + [log(2k)!]''-type terms: leading A'' = −2/k [from −2k log k] + O(1/(k log k)) [log-log + saddle drift]. All other terms contribute o(1/k). Hence **D_k = 2/k + O(1/(k log k)) and k·t_k → 2.** (The exact O(1/L) correction constant is not pinned by the simple envelope expansion — higher-order u₀-motion terms matter at that order; measured value below.)

## 2. Numerical extension (CHECKED NUMERICALLY)

Pipeline validation (end-to-end): log M_0 = −0.6989222679459 vs ln ξ(1/2) = −0.6989222679453 (agreement 5.4e-13); **min t_k·(k+1) = 1.06963238 at k=1 — EXACT 8D anchor; t_200·201 = 1.5685 — EXACT 8D max** (8D fit t_200 = 1.18·200^{−0.948} = 0.00780 vs measured 0.0078037).

**t_k·k table (direct saddle quadrature):**

| k | k·t_k | 2 − k·t_k | (2−k·t_k)·log k |
|------|---------|-----------|------------------|
| 10²  | 1.5016 | 0.4984 | 2.295 |
| 10³  | 1.6590 | 0.3410 | 2.355 |
| 10⁴  | 1.7447 | 0.2553 | 2.351 |
| 10⁵  | 1.7975 | 0.2025 | 2.331 |

k·t_k is monotone increasing toward 2; the deficit satisfies (2 − k·t_k)·log k ≈ **2.35** (stable over 10³–10⁵), i.e. k·t_k ≈ 2 − 2.35/log k → **2**. The memo's numerical anchors are reproduced to machine precision; the asymptotic limit is certified by data + the C1-validated expansion. (8D's power-law fits t_k ~ 1.1–1.18·k^{−0.93..−0.95} are consistent — the effective exponent −0.95 ≠ −1 is exactly the log correction.)

## 3. Dilogarithm-family scan (Rust, closed form + zero scan)

**t_k closed form (exact, PROVEN):**
- a_k = k^{−α}: t_k = 1 − (1−1/k²)^{−α} ≈ −α/k²  ⟹  k·t_k ≈ −α/k → 0⁻
- a_k = (k+1)^{−α}: t_k = 1 − [1+1/(k²+2k)]^α ≈ −α/k²  ⟹  k·t_k → 0⁻
Measured at k=10⁶: k·t_k = −α·10⁻⁶ for α ∈ {0.5,…,3.0} — **negative margin, t_k·k → 0⁻ for all α.** (The task's "expect: α − …" is answered by the numbers: the margin is not α/k — the family is log-convex, t_k < 0.)

**Zeros of Li_α(z) = Σ z^k/k^α in |z|<1 (grid step 0.02 + Newton + argument-principle winding):**
α ∈ {0.5, 0.7, 0.9, 1.0, 1.2, 1.5, 2.0, 2.5, 3.0}: **exactly one zero in the disk for every α, at z = 0; nonreal = 0; winding(r=0.5) = winding(r=0.9) = 1.** No non-real zeros at any α in (0.5, 3.0) — the threshold α_crit does not exist for this family.
- **α = 2 (Li₂):** zero set in |z|<1 = {0}. Analytic argument (PROVEN-level, standard facts): Im Li₂(e^{iθ}) = Cl₂(θ) has sign + on (0,π), − on (π,2π), zeros at 0, π, 2π (Cl₂ = −∫₀^θ log(2sin(t/2))dt, ∫₀^π = 0); Re Li₂(e^{iπ}) = Li₂(−1) = −π²/12 < 0 ⟹ the curve Li₂(e^{iθ}) crosses the negative real axis once ⟹ winding = 1 ⟹ exactly one zero in the disk. CONFIRMED numerically.
- Li₂ continuation in 1 < |z| ≤ 2 (Li₂(z) = −Li₂(1/z) − π²/6 − ½log²(−z)): **no zeros found.**

**Moment-normalized reading (the only way the "2/k margin" could arise for this family):** b_k = a_k/(2k)!, a_k = (k+1)^{−α} ⟹ t_k·k → 2 (the (2k)! dominates). But the LP-relevant object is then f(t) = Σ(−1)^k b_k t^{2k} (Bessel-type), NOT the moment generating function Li_α. **The memo's crux conflates the two: non-real zeros of Li_α (which don't exist anyway in the disk) say nothing about f's zeros.** This is a category error.

## 4. Threshold statement (honest)

**NOT certified.** The probe's deliverable on the margin question is negative:
- The dilogarithm/polylogarithm families do NOT provide a counterexample at margin ≤ 2 — their Turán quotients are negative (they fail even the weak Turán inequality t_k ≥ 0).
- Therefore "coefficient-margin criteria with margin C ≤ 2 cannot force LP" is NOT established by this family, and no threshold α_crit exists for it.
- What IS closed: (i) the real-Ξ saddle asymptotics t_k·k → 2 (PROVEN + verified to 10⁵); (ii) the polylogarithm family's zero structure (one real zero at 0 in the disk for all α ∈ (0.5,3)). S1 itself (t_k ≥ C/(k+1), C > 1, all k) remains CONJECTURED (proven tail, unproven uniformity) — the margin-≤2 death claim was the memo's §1(c) "crux" and is now REFUTED.
- Data-quality notes: Phase B4 (Bessel-type F_α real-zero scan) is INVALID for t ≳ 10 — the truncated alternating series suffers catastrophic cancellation (α=0 control should give cos t's ~13 zeros on [0,40], printed 358). Same lesson as the 8D artifact finding; no claim from B4. Quadrature precision: log M_k abs error ~1e-10 (saddle-centered, log-space; verified by the ξ(1/2) and 8D anchors); k·t_k accurate to ~1e-5 at k=10⁵.

## Files
- tools/s1saddle/ (Rust crate; Phase A saddle quadrature, Phase B polylog scan; run ≈ 60 s)
- research/notes/s1-saddle-closure-run-2026-08-18.txt (full run output)
- research/notes/s1-saddle-closure-2026-08-18.progress
- ledger line appended.
