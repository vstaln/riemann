# SOTA AUDIT — proportion of zeros of ζ(s) on the critical line (2026-08-12)

Survey of the published record for κ = liminf (number of zeros on Re(s)=1/2 up to height T)/(total zeros up to height T).
Labels per honesty charter: PROVEN / CHECKED NUMERICALLY / REPORTED-UNVERIFIED / CONJECTURED.

## 1. The published progression (unconditional "proportion ON the line")

| Year | Authors | Constant | Fraction | Method (mollifier length θ, moment used) |
|---|---|---|---|---|
| 1974 | Levinson | 1/3 (≈0.3333; refined ≈0.3474) | — | Levinson's method; short/trivial mollifier; needs the second moment (mean square) of ζ — PROVEN |
| 1989 | Conrey | 2/5 (≈0.4000; actual ≈0.4088) | 2/5 | Levinson + mollifier of length θ = 4/7 − ε with the "infinitesimal shift"/harmonic weight; needs the fourth moment of |ζ(1/2+it)| (Ingham 1926) — PROVEN |
| 2011 | Bui–Conrey–Young | 0.4105 | 41.05% | Two-term mollifier; needs the twisted fourth moment (Hughes–Young / BCY) — PROVEN |
| 2012 | Feng | 0.4128 | 41.28% | Refined mollifier optimization of BCY — PROVEN |
| 2020 | Pratt–Robles–Zaharescu–Zeindler | 5/12 ≈ 0.4167 (stated "more than five-twelfths"; numerical constant ≈0.4171) | 5/12 | Levinson–Conrey with longer/optimized two-term mollifier; essential input the sharp twisted second/fourth moments (Bettin–Chandee; Bettin–Bui–Li–Radziwiłł) — PROVEN |

**2020–2026.** The last peer-reviewed *unconditional* constant I can confirm is PRZZ 2020 (5/12 ≈ 0.4167). No peer-reviewed unconditional improvement beyond 5/12 is verified in my knowledge — REPORTED-UNVERIFIED (any 2020–2026 claim of κ > 0.4167 must be checked against arXiv/MathSciNet before use).

Conditional / formalized results in the program's external-results (Anthropic zeta-23-lean) — REPORTED-UNVERIFIED (Lean-formalized, journal status unclear), constants cross-checked digit-for-digit — CHECKED NUMERICALLY:
- Thm A: 2/3 on-line; Thm B: 2/3 simple-on-line; Thm C: 5/6 distinct.
- Thm D: 0.6725007036794… = 3/2 − cot(1/√2)/√2 (described as "Montgomery–Taylor window", c1* = 0.75329).
- xi′-interlacing: 0.85838 simple-on-line / 0.92919 distinct, STANDALONE.
- PairCeiling: every bandwidth-one (c0,r) certificate certifies ≤ 0.6818287 + 2.5431316e-6·(|r′(1)| + ∫|r″|) — machine-checked, matches our 0.6818286874638315 = p0 + 1/(6·256²).

## 2. Where does our 0.6733 sit relative to PUBLISHED literature?

- Published unconditional κ record: **5/12 ≈ 0.4167 (PRZZ 2020)**. Our 0.6732660791 is far above every published *unconditional* constant — but it is NOT the same statistic: it is a lower bound on a *stronger, certificate-defined* "simple-on-line" quantity inside a weighted Levinson integral, certified numerically.
- Honesty (per charter): our 0.6733 is **CHECKED NUMERICALLY** (Arb verifier, grid=4000, eps=0.008065 certified), **NOT PROVEN** — it carries numeric-certification caveats (grid-artifact probes show the eps floor ≈0.0080606 does not rise at grid 6000/8000). It is not a classical hand-proved theorem.
- It beats the formalized Thm D **0.6725** by +7.65e-4 (CHECKED NUMERICALLY cross-check), but sits **below the PROVEN in-class ceiling 0.6818312306**. Verdict: a new record *within the certificate class*, not a new published record in the κ sense.

## 3. The STRUCTURAL gap (obstacle to ~2/3 or ~68%)

- **Moment barrier (PROVEN):** Levinson–Conrey mollifier length θ is capped at 4/7 by the proven fourth moment (Ingham); exceeding it requires the sixth/higher moments, which are only CONJECTURED (Keating–Snaith 2000 / Conrey–Ghosh–Gonek moment conjecture). This is why unconditional κ moved only 0.4088 → 0.4167 in 30 years. Conrey's 2/5 is exactly the θ=4/7 optimum against the fourth moment — PROVEN.
- **Simple-zeros heuristic (CONJECTURED):** reaching κ→1 needs "all zeros simple + on line". Best conditional (RH) simple-zeros results: Conrey–Ghosh–Gonek 1998 (19/27 ≈ 0.7037), improved by Bui–Heath-Brown (2013) — PROVEN (conditional on RH).
- **Program's internal 2/3 → 68% ladder:** 2/3 is the formalized Thm A/B floor; ~68.18% is the PROVEN ceiling of the n=7 two-moment certificate class (PairCeiling 0.6818287). "~2/3 barrier" = the point where two-moment certificates saturate; breaking it requires a class change (three-moment/xi′-interlacing), not better eps.

## 4. Single most promising PUBLISHED technique to break 68%

**The dual/inertia (Sylvester) certificate with xi′-interlacing companions** (adapted from zeta-23-lean E2: N_on ≥ 2n₊ − N, no positivity hypothesis). It would require feeding the PROVEN xi′-interlacing constraints (m_{ξ′}(γ) = m_ξ(γ) − 1 on-line; 0.85838 simple-on-line) into the marked LP — if this renders the ceiling witness's ~31.8% double-mass infeasible, the 0.6818 ceiling cracks toward 0.70 (CONJECTURED; probe cost LOW). Runner-up: the distinct-count lane N_d ≥ 0.8071 (λ=2/3), gated only on the untested admissible-cubic Schur–Horn transfer to λ<1.

## Verdict: where the real frontier is

1. Unconditional published κ is frozen at 5/12 (0.4167) behind the fourth-moment barrier; that line is not where we race.
2. Our 0.6733 is a real in-class record (CHECKED NUMERICALLY), above the formalized 0.6725 but below the PROVEN 0.6818 ceiling.
3. The 2/3 → 68% wall is a certificate-class ceiling, not a number-theory wall; eps/weight/P-ascent are CLOSED.
4. The frontier is proving a NEW class: the inertia/dual certificate with xi′-interlacing (to 0.70), or the distinct-count N_d ≥ 0.8071 transfer.
5. Both are currently CONJECTURED and gated on one testable transfer/infeasibility — cheap to probe, high payoff.
