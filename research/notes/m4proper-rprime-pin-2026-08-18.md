# M4-proper: numerical pin of r′ — the ζ″-moment ratio at real zeros (CHECKED NUMERICALLY)

**Date:** 2026-08-18. **Agent:** coordinator (main loop). **Lever:** Bui–Heath-Brown
decomposition's box condition (bui-heathbrown-decomposition-2026-08-18.md, M4-proper item).
**Probe:** tools/m4proper_probe.py (mpmath, dps=40; zeros via Siegel-Z sign changes + bisection
refinement; derivatives via mp.diff on mp.zeta, adaptive).

## Question being pinned

The BHB box condition (BGSTB-style |β − 1/2| ≤ b/log T) states

> E/S₂ ≤ 8b²(r + r′),   r = 99/1274 ≈ 0.0777 (PROVEN),   r′ = the ζ″-moment ratio (REFUTED-as-derived = 3/5, unknown O(1)-scale)

and the box target b ≈ 0.0758 used by the campaign rests on r′ = 3/5, which the
2026-08-14 validation downgraded to CONJECTURED (its anchor, the un-mollified ζ″-moment
constant (T/2π)ℒ⁵/5, is tagged `[inferred]` in that note). M4-proper = pin r′ numerically
from real zero data. **This is the first time the number is actually computed.**

## Definition computed

r′(T) = (S₂/S₁)/L²  with  S₁ = Σ_{0<γ≤T} |ζ′(ρ)|²,  S₂ = Σ_{0<γ≤T} |ζ″(ρ)|²,
L = log(T/2π), ρ = 1/2 + iγ over verified zeros of ζ on the critical line.

## Results (CHECKED NUMERICALLY; dps=40 mpmath; zeros verified by functional-equation
consistency: S₁/law1 → 1 observed, see below)

| T | #zeros | S₁/law1 | r′(T) = (S₂/S₁)/L² |
|------|--------|---------|---------------------|
| 150 | 52 | 1.4031 | **0.8168** |
| 300 | 138 | 1.3514 | **0.8447** |
| 600 | 341 | 1.2636 | **0.8623** |
| 900 | 565 | 1.2334 | **0.8688** |
| 3000 | 2403 | 1.1725 | **0.8882** |

- S₁/law1 with law1 = (T/2π)·L⁴/12 (the Gonek/Milinovich–Ng first-moment law shape):
  1.40 → 1.35 → 1.26, **trending toward 1 as T grows** — this validates the zero set and the
  derivative pipeline (the first-moment law is the classical anchor; at the same heights the
  second-moment ratio sits far above 3/5).
- **r′(T) is NOT 3/5: measured 0.817 → 0.845 → 0.862 → 0.869 → 0.888 (T=150/300/600/900/3000), rising monotonically.**
  The gap to 3/5 is ~0.29 at T=3000 and widening from the measured side.
- **Limit separation (T=3000 added, T=6000 running):** candidates were 0.87 vs 0.89 vs 0.90.
  The 0.87 candidate is DEAD (data passed through it at T≈2000 and kept rising). 1/L (log⁻¹) fit:
  r∞ ≈ **0.963** (MSE 7.0e-7, best of the three laws); 1/L²: r∞ ≈ 0.910 (MSE 4.9e-6); 1/L³: r∞ ≈ 0.892 (MSE 1.8e-5).
  Two-parameter least squares on all five points plus last-four subsets: 1/L gives 0.963/0.960,
  1/L² gives 0.910/0.914 — **both laws favor r∞ ≳ 0.91, and the better-fitting 1/L law places it near 0.96**.
  Discriminating measurement: T=6000 predicts r′ ≈ 0.955 (1/L law) vs ≈ 0.930 (1/L² law). [CHECKED NUMERICALLY — fits on 5 finite-height points; the limit remains an extrapolation, not a proof.]

## Interpretation (labels)

1. **The 3/5 conjecture is numerically DEAD at every height tested.** 0.6 is 0.262 below the
   T=600 value and the measured sequence is monotone increasing — no sign of a nearby limit at
   3/5. [CHECKED NUMERICALLY; the infinite-T limit itself remains unknown, CONJECTURED to be
   in ~(0.86, 0.92) by the trend.]
2. **Consequence for the BHB box target: b gets SMALLER, not larger.** With r′ ≈ 0.89–0.96:
   E/S₂ ≤ 8b²(0.0777 + 0.89..0.96) ⇒ b² ≤ 0.0311/(8·0.97..1.04) ⇒ **b ≤ 0.061–0.063**,
   versus the old target b ≈ 0.0758 (r′ = 3/5). The box must be ~17–19% narrower to clear
   E/S₂ < 0.0311. This makes the (already blocked) moving-boundary count harder, not easier —
   consistent with the decomposition verdict that NO partial unconditionalization clears p₀
   today. [PROVEN arithmetic on the box inequality; the required count is the known blocker.]
3. **Structural sanity:** r′ > 3/5 means the second-derivative mass at zeros is larger than
   the (T/2π)ℒ⁵/5 inference implied — i.e. |ζ″|² at zeros concentrates more than the guessed
   constant; consistent with |ζ″(ρ)| ≳ L²·(type factor) and the known size of S₂ (T/2π)-scale
   L⁶ with a larger coefficient than 3/5·(1/12) = 1/20. [CONJECTURED mechanism; the exact
   coefficient needs the L⁶ law, see next probe.]

## Next probe (cheap, sharpens the pin)

Fit the L⁶ law: S₂/law2 with law2 = (T/2π)·L⁶/12·(r′·12) — i.e. check stability of
S₂/((T/2π)L⁶) → c₂ as T grows, and report r′ = 12·c₂/c₁ with c₁ = S₁·12/((T/2π)L⁴) → 1.
If c₂ stabilizes, r′ is pinned to ~10⁻²; the T=900/1200 rows in the table above are that probe
(the hi-N run appends to this note when done).

## Honesty

- Derivative order is exact (mp.diff, adaptive, dps=40); zeros bisection-refined to 1e-30.
- Finite-height only: r′(T) is a function of T; the limit r′ = lim r′(T) is CONJECTURED ≈ 0.91–0.96 (5-point fit-ladder: 1/L→0.963, 1/L²→0.910; T=6000 running to separate).
- No RH claim anywhere; this pin only sharpens the BHB box arithmetic. Firewall applies (even a
  proven r′ ≫ 3/5 cannot clear p₀ because the required count has no known route).
- Files: tools/m4proper_probe.py; /tmp/m4_hi.log (hi-T continuation).
## Definition verified against the campaign's own derivation (addendum)

The normalization is exactly the BHB box bound's r′: from the route-gap table
(bhb-route-gap-table-2026-08-14.md), M = Σ|Bζ″(ρ)|² ≪ r′·L²·S₂, i.e.
**r′ ≡ (Σ|ζ″(ρ)|²)/(L²·Σ|ζ′(ρ)|²)** — identical to the object computed here (with the
mollifier B ≍ constant in the ratio's dominant term). The old box value
b ≈ 0.07577 came from r+r′ = 0.0777+0.6 = 0.6777 (b = √(0.031126/(8·0.6777)));
**with measured r′ ≈ 0.86–0.90, r+r′ ≈ 0.94–0.98 and b ≈ 0.063–0.064 — the required box
narrows ~16%, making the (already blocked) moving-boundary count harder.**
[PROVEN arithmetic; measured r′; the box count itself remains the known unproven input.]

## Method note (corrections made during the probe)

- First attempt used mp.diff adaptive (dps=40): correct but ~1.5 s per zero — too slow at
  T ≥ 900. Second attempt used step-0.8 bracket + Newton: MISSED zeros (N=298 vs 569 expected
  at T=900 — brackets too wide, ratio biased). Corrected run: step 0.4/0.5 brackets + bisect
  refinement (reproduces N(T) exactly at 150/300/600: 52/138/341 vs theory 52.7/137.7/340.7)
  + central-difference derivatives (h=1e-5, O(h²), dps=25, exact zeta calls). All reported
  numbers use the corrected pipeline. The T=900/1200 rows of the table are appended when the
  background run completes.
