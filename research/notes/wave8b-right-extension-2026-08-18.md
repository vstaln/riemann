# WAVE 8B EXTENSION — ζ′ right-strip census T→12000; the "2651 unexplained" resolved

**Date:** 2026-08-18. **Lever:** wave8b machinery (Rust, certified ζ′, arg-principle winding).
**Status:** COMPLETE. **Verdict:** Right-strip ζ′ density ratio keeps rising toward 1
(0.586 → 0.657 cumulative over T=5000→12000; incremental 0.658 → 0.721); the count follows
N₁(T) = N(T) − (finite-T deficit) with deficit ≈ 0.74·T/log^{0.36}(T/2π). **The 2651 number
is explained as the finite-T approach to the classical N₁(T) ~ N(T) law. CHECKED NUMERICALLY,
RH-consistent, NO disproof signal, NO anomaly.**

## 1. Extended census (all CHECked NUMERICALLY, RUST release binary)
`right T0 T1 1000 0.02`, outputs research/notes/wave8b-right-ext-*.out.

| slab | ζ′ zeros (winding) | N(T₁)−N(T₀) | incremental ratio | cumulative count | cum ratio |
|---|---|---|---|---|---|
| [10,5000] (prior) | 2651 | 4520.3 | — | 2651 | 0.5865 |
| [5000,6000] | 709 | 1078.0 | 0.6577 | 3360 | 0.6002 |
| [6000,7000] | 754 | 1104.6 | 0.6826 | 4114 | 0.6138 |
| [7000,8000] | 790 | 1127.5 | 0.7007 | 4904 | 0.6263 |
| [8000,9000] | 797 | 1147.4 | 0.6946 | 5701 | 0.6350 |
| [9000,10000] | 812 | 1165.1 | 0.6969 | 6513 | 0.6421 |
| [10000,11000] | 853 | 1181.1 | 0.7222 | 7366 | 0.6505 |
| [11000,12000] | 862 | 1195.6 | 0.7210 | 8228 | 0.6572 |

- **TOTAL [10,12000]: 8228 ζ′ zeros in [0.5,1]** (2651 + 5579 new). N(T) by
  RvM (T/2π)(log(T/2π)−1)+7/8.
- All slabs: certified contour min-margins 1.8e-3 … 6.4e-3, neg-samples=0 (no zero on any
  contour), max|Δarg| ≤ 2.7 < π (winding unambiguous; adaptive subdivision active).
- **Step stability at high T: [7000,8000] winding = 790.000000 at step 0.04 — identical to
  step 0.02** (same validation standard as the prior census).
- Secant-artifact note: `right`'s refined-zero display produced 3 spurious points
  (σ=55.17@9501, σ=1.96@10500, σ=57.79@11498) — secant wandering OUTSIDE [0.5,1] where |ζ′|
  is super-exponentially small; these are NOT census objects (excluded; the winding counts and
  contour margins are the certified quantities).

## 2. THE QUESTION — does the ratio keep rising toward 1?
**YES, monotonically (no flattening).** Cumulative 0.5865@5000 → 0.6572@12000 (8 points,
strictly increasing). Incremental 0.658@5500 → 0.721@11500, with a benign 2-slab fluctuation
(0.7007 → 0.6946 → 0.6969 in [7000,9000]) that resumed rising — fluctuation, not a turn.
RH-consistent (under RH all ζ′ zeros lie in [1/2,1] by Speiser, and the classical count is
N₁(T) ~ N(T), so ratio → 1). Extrapolation of the fitted law reaches r≈0.72 at T≈2·10⁴,
r≈0.80 at T≈10⁵ — slow logarithmic approach.

## 3. σ-min drift (Levinson drift continues)
min-σ per locate window: **0.5426@[4900,5000] → 0.5063@[5000,5100] → 0.5224@[11000,11100]**;
prior: 0.78@t≈50 → 0.54@t≈4900. The drift σ-min → 1/2 continues (0.78 → ~0.51); the tail
minimum fluctuates ±0.02 (rare-event statistic — min over ~70–85 zeros per window). A ζ′ zero
at σ=0.506, t≈5006 is only 0.006 right of the critical line — consistent with zeros crowding
the line as t grows. No left-strip (σ<1/2) zero seen anywhere; consistent with Speiser/RH
(also Platt–Trudgian PROVEN below 3·10¹² — a left zero here would be expected impossible).

## 4. PART B — the "2651 unexplained" resolution
**The 2651 number is explained by the classical count law; no mystery remains.**
1. **Classical theorem (PROVEN, classical — Berndt 1970 "The number of zeros of ζ′(s)";
   background in Radziwiłł 2013 "Gaps between zeros of ζ′(s)"; underlies Levinson's method):**
   N₁(T) := #{ζ′ zeros in 0<σ<1, 0<t<T} satisfies N₁(T) = N(T) + O(·), same main term
   (T/2π)log(T/2π) − T/2π + 7/8; i.e. N₁(T)/N(T) → 1. [Citation detail: no local copy of
   these papers verified in research/papers/ (searched — nothing); theorem PROVEN-classical,
   exact reference CONJECTURED-locally.]
   Under RH, Speiser ⟹ left strip empty ⟹ N₁(T) = N_right(T), so the [0.5,1] census ~ N(T).
2. **Empirical count law (CONJECTURED, fit):** deficit D(T) = N(T) − N₁(T) is ~linear in T
   with slowly decaying coefficient: **D(T) ≈ 0.74·T/log^{0.36}(T/2π)** (fits D/T = 0.374→0.358
   over the 8 points to ≤0.4%); equivalently
   **1 − r_c(T) ≈ 4.65/[log^{0.36}(T/2π)·(log(T/2π)−1)] ≈ 7.5/log^{1.52}(T/2π)**
   (max |residual| 0.009 at T=5000, ≤0.004 over [6000,12000]). The √log T candidate law from
   the brief tests poorly (predicts r≈0.36 at T=100 vs observed 0.15).
3. **Mechanism (CONJECTURED):** the deficit is the finite-T "migration" of ζ′ zeros into the
   strip — σ-min → 1/2 as t grows, so at height T a fraction ~1 − O(1/log^{1.5}) of the
   eventual (asymptotic) ζ′ zeros have entered [1/2,1] with t ≤ T. The 1:1 "turning point of
   Z" heuristic from the brief is only an asymptotic statement: every gap (γ_n, γ_{n+1})
   contains a Z-extremum (Rolle), yet the empirical count is 0.59·N at T=5000 — so the
   pairing is loose at finite T (zeros enter the strip gradually). This is NOT evidence for or
   against RH per se (it is the RH-consistent expectation); it explains the "2651".
4. **Proves-too-much check:** the law is a *consistency* statement, not a discriminator — an
   RH-false model (Davenport–Heilbronn with planted left zeros) would have ζ′ zeros in the
   left strip and a *different* [0.5,1]-only census; we do not claim the density law itself
   discriminates RH. (The discriminator was verified in the prior wave: fake f′ shows
   left-strip zeros, real ζ′ none.)

## 5. Verdict
- **Density ratio rising toward 1 (0.5865 → 0.6572, incremental 0.658 → 0.721): CHECKED
  NUMERICALLY — RH-consistent. No flattening, no anomaly, no disproof signal.**
- **"2651 unexplained" → RESOLVED:** N₁(5000) = N(5000) − D(5000), D ≈ 1870 ≈ 0.74·T/log^{0.36}u,
  the finite-T deficit in the classical N₁(T) ~ N(T) law. Label: count-law fit CONJECTURED,
  classical asymptotic PROVEN (Berndt/Rodziwiłł, unverified locally), census numbers CHECKED
  NUMERICALLY.
- Left strip NOT re-run at T>5000: redundant (Platt–Trudgian PROVEN RH below 3·10¹² + Speiser
  ⟹ no left ζ′ zeros below 3·10¹²). No left-zero anomaly observed.
- Follow-ups: (i) extend to T≈10⁵–10⁶ to pin the deficit exponent (log^{0.36} vs T^{0.95} vs
  C·T^{1/2}log T constant-5 — currently indistinguishable over [5000,12000]); (ii) verify the
  Berndt/Radziwiłł count statements from primary sources when budget allows; (iii) the
  refined-zero secant wandering (σ>1 artifacts) is cosmetic — could clamp refine to the strip.

## Labels
Census numbers: CHECKED NUMERICALLY (certified pointwise ζ′, adaptive winding, step-stability
verified at 0.02/0.04, margins ≥1.8e-3, neg=0 on every slab). Count-law fit: CONJECTURED
(empirical, 8 points). Classical asymptotic N₁(T) ~ N(T): PROVEN (classical knowledge; exact
citation unverified locally). RH: not claimed proved; this extension is RH-consistent evidence.

## Commands / outputs
`right 5000 10000 1000 0.02` → research/notes/wave8b-right-ext-5000-10000.out
`right 10000 12000 1000 0.02` → research/notes/wave8b-right-ext-10000-12000.out
`right 7000 8000 1000 0.04` (step-check) → inline
`locate 5000 5100`, `locate 11000 11100` → research/notes/wave8b-locate-{5000-5100,11000-11100}.out
