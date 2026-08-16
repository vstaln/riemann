# Log-profile boundary probe — margin-2 approach-rate: the deficit-2 class is NOT LP-consistent (LEVER CLOSED)

**Date:** 2026-08-18. **Agent:** builder. **Status:** COMPLETE.
**Labels:** PROVEN / CHECKED NUMERICALLY / CONJECTURED / INCONCLUSIVE per claim. No RH claim anywhere.

## HEADLINE VERDICT (up front)
**The deficit-2 log-profile class {t_k·k ≥ 2 − 2/ln k} is NOT LP-consistent — the one-way sufficient-condition
lever is CLOSED.** It is consistency data only, exactly parallel to S1 (constant margin C > 1 dead; decaying
deficit-2 profile dead). Two independent lines establish this:
1. **PROVEN (existing S1 certified data + coordinator convention check):** the S1 non-LP perturbed families
   b_k = k^{−2k}(1+eps·cos(ω·ln k)), (eps,ω) = (0.01,5), (0.05,3), (0.05,5) — certified genuine non-real zeros
   (|t|=6.480, |F|=1.6e-13 etc., S1 note) — satisfy t_k·k ≥ 2 − 2/ln k for ALL k ≤ 2·10⁵ (zero violations).
   They are members of the deficit-2 class and are NON-LP. ⟹ class not sufficient.
2. **CHECKED NUMERICALLY (this probe, independent, smooth family):** the smooth-family member at the deficit-2
   target (C,D) = (2,−2), i.e. b_k = k^{−2k}·(ln(k+2))^{2k}, has margin profile k·t_k = 2 − 2/ln k + 2/ln²k + …
   strictly ABOVE the deficit-2 curve (min pointwise gap over k=10..400: **+0.0517** — it IS a class member) yet
   is NON-LP with genuine non-real zeros at |t| = 4.472, 6.844, 8.995, 11.019 (full-series Newton polish
   |F| ≤ 2e-10 for the first two; pipeline validated by exact reproduction of S1's c=1.7 result: |t|=17.632@3.674°
   vs S1 note's 17.632@3.7°, |F|=5.7e-7 vs 5.6e-7).

**Xi is NOT in the class either**: certified g02 profile k·t_k = 1.427 (k=50), 1.502 (100), 1.538 (150), 1.561
(200), 1.577 (250) — min gap vs 2 − 2/ln k is **−0.0642 (at k≈92)**, i.e. Xi's margin sits BELOW the deficit-2
curve (D(k) = (2−k·t_k)·ln k = 2.24–2.33 > 2, → 2 from above). So Xi's profile is not covered by the (dead) class.
**No margin-profile sufficient condition for Xi is opened by this probe.**

---

## Part A — the (C,D) scan (CHECKED NUMERICALLY)

**Family.** b_k(C,D) = k^{−C·k}·(ln(k+2))^{−D·k}, margin profile k·t_k ≈ C + D/ln k − D/ln²k (PROVEN saddle form:
f = −Ck ln k − Dk ln ln k ⟹ t_k ≈ C/k + D/(k ln k)(1 − 1/ln k)). Deficit-2 target ⟺ (C,D) = (2,−2)
(coordinator-corrected sign; verified: k·t_k@100 = 1.66, @300 = 1.705 — matches coordinator's 1.66@100→1.75@800).

**Convention (verified from tools/s1margin/probe.rs source, not guessed).** t_k = 1 − exp(−d), d = 2·lb[k] −
lb[k−1] − lb[k+1] (= −Δ² log b_k); margin reported as t_k·(k+1) (Newton requires ≥ 1); the class curve is
t_k·k vs 2 − 2/ln k. Reproduces S1's asymptotic t_k·(k+1) = c + c(1−c/2)/k for b_k = k^{−ck} exactly.

**Method (reused S1 machinery).** Aberth–Ehrlich sections on R_N(w), w = (t/S)², S = exp(−lb[N]/(2N)), N ∈
{80,120,160}; trust |t| ≤ 0.7S; candidate non-real t-roots (non-real w or real-negative w) verified by Newton
polish on the INFINITE series (quadratic shrink ⟹ GENUINE; immune to section artifacts). ~92 grid points,
runs in ~5s total. tools/logprofile/ (Rust, std-only).

**Phase diagram (verdicts, "weak" = genuine zero at |F| ∈ [1e-7, 1e-4])**

| C \ D | −3 | −2.5 | −2 | −1.5 | −1 | −0.5 | 0 | +1 | +2 | +3 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1.7 | NL | – | NL | – | NL | – | NL(weak) | LP | LP | LP |
| 1.8 | NL | – | NL | – | NL | – | LP | LP | LP | LP |
| 1.85 | NL | NL | NL | NL | NL | NL(weak) | LP | – | – | – |
| 1.9 | NL | NL | NL | NL | NL | NL(weak) | LP | LP | LP | LP |
| 1.95 | NL | NL | NL | NL | NL | LP | LP | – | – | – |
| 2.0 | NL | NL | NL(4.47,6.84,9.00,11.02) | NL | NL(10.63,15.05) | LP | LP | LP | LP | LP |
| 2.05 | NL | NL | NL | NL | NL(weak 15.95) | LP | LP | – | – | – |
| 2.1 | NL | NL | NL | NL | NL(weak 21.99) | LP | LP | LP | LP | LP |
| 2.2 | NL | – | NL | – | LP | – | LP | LP | LP | LP |
| 2.4 | NL | – | NL(14.51,weak) | – | LP | – | LP | LP | LP | LP |

(NL = NON-LP with genuine non-real zeros; LP = LP-consistent; – = not tested.)

**Boundary curve D*(C) (CHECKED NUMERICALLY, documentation only).** The non-LP/LP boundary decreases with C:
D* ≈ 0 to +0.5 at C ≈ 1.7 (D=0 borderline-non-LP there, matching S1's c=1.7 borderline); D* ∈ (−0.5, 0) for
C ≈ 1.8–1.9; D* ∈ (−1, −0.5) for C ≈ 1.95–2.1; D* ∈ (−2, −1) for C ≈ 2.2–2.4. Rough line D* ≈ 3.7 − 2.2·C
(fuzzy, ±0.5; the weak-|F| borderline points make the exact locus INCONCLUSIVE to finer than ±0.5 in D).
**The boundary does NOT pass through (2,−2)** — (2,−2) is deep inside the non-LP region. Empirical
characterization: within this smooth family, non-LP sets in when the pointwise margin min t_k·(k+1) dips below
≈ 1.75–1.85 (LP neighbors have min ≥ 1.80–1.89; non-LP neighbors min ≤ 1.69–1.83) — consistent with S1's
phase transition at C ≈ 1.7–1.8. (With the S1 caveat: pointwise margin alone does not determine LP-ness in
general — the S1 perturbed margin-1.88 family is non-LP while clean margin-1.875 is LP-consistent.)

**The decisive point (2,−2).** Margin profile 2 − 2/ln k + 2/ln²k − … (saddle, PROVEN form), min t_k·(k+1) =
1.3668 (Newton satisfied ⟹ not trivially non-LP), min class gap +0.0517 (in class). Genuine non-real zeros:
|t| = 4.472@25.5° (|F|=3.6e-13), 6.844@−23.3° (|F|=2.0e-10), 8.995@22.2° (|F|=1.1e-7), 11.019@−21.5°
(|F|=2.9e-5); stable across N ∈ {80,120,160}. **The deficit-2 target family is NON-LP.**

## Part B — Xi position (CHECKED NUMERICALLY, certified g02 data)
Xi's certified profile is strictly BELOW the deficit-2 curve at all k = 10..250 (min gap −0.0642 at k=92);
D(k) ≈ 2.24–2.33 (converging to 2 from above, matching the PROVEN expansion). Xi approaches margin 2 at the
same leading rate 2/ln k but with a deficit D(k) > 2 (margin slightly below the curve), while the non-LP member
(2,−2) has deficit D(k) = 2 − 2/ln k < 2 (margin slightly above the curve). **Xi is not in the deficit-2 class.**
Conclusion: even before the class was shown non-LP, Xi's profile would not have been covered by it.

## Part C — Verdict
1. **Boundary location:** CHECKED NUMERICALLY, D*(C) ≈ 3.7 − 2.2C (fuzzy ±0.5), decreasing from ≈ 0 (C≈1.7)
   to ≈ −1.5 (C≈2.4); does NOT pass through (2,−2); (2,−2) is inside the non-LP region.
2. **Is {t_k·k ≥ 2 − 2/ln k} LP-consistent? NO.** Strongest non-LP class member tested: the certified S1
   perturbed families (PROVEN non-LP, in class for all k ≤ 2e5) and the smooth (2,−2) (CHECKED NUMERICALLY,
   in class pointwise for k ≥ 10, min gap +0.052). Smallest margin observed among LP members: min t_k·(k+1) =
   1.80 (C=1.8, D=0) / 1.7957 (C=1.95, D=−0.5) — i.e. LP-consistent members keep their pointwise margin above
   ≈ 1.8, while the class curve 2 − 2/ln k dips to 1.65 at k=300 — the class allows margins the LP region does
   not. **The class is not a sufficient condition.**
3. **Is Xi strictly inside an LP-consistent region? NO — Xi is outside the (dead) deficit-2 class** (below the
   curve). Nothing about Xi's LP status is decided by any margin-profile condition here.
4. **Honest bottom line: LEVER CLOSED.** The deficit-2 log-profile is consistency data only, PROVEN non-LP as a
   class (existing S1 data + convention check; independently corroborated in the smooth family by (2,−2)).
   A candidate one-way sufficient condition at the deficit-2 approach rate is refuted, exactly as S1's
   constant-margin C > 1 was. The search for a sufficient-condition lever must use the full coefficient
   structure (Jensen degrees), not a margin/approach-rate profile. **No RH claim, no Xi claim, no LP claim
   beyond the finite scanned family.**

## Files
- tools/logprofile/ (Rust, std-only; scan + Xi-profile binary; modes coarse/refine/point/xi)
- research/notes/logprofile-scan-coarse-2026-08-18.txt, logprofile-scan-refine-2026-08-18.txt,
  logprofile-point-2m2-2026-08-18.txt, logprofile-xi-2026-08-18.txt (full outputs)
- This note. Progress: logprofile-boundary-2026-08-18.progress. Ledger line appended.
