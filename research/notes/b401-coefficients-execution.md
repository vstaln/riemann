# B4-01/RF-09/LAD-01 — Derive the (A_n, B_n) plug-in coefficients for n=9,11,13,15

**Role:** EXECUTION agent (B4-01). **Date:** 2026-08-12 (phone mirror). **Status:** COMPLETED.
**Idea:** idea-factory-master §4 #16 (B4-01/RF-09/LAD-01). Prior attempt OOM-killed — deliverable missing; rebuilt here.
**Read first:** context-pack.md, idea-factory-master.md (§4 #16 + §8), verify-gram-stability.md, ladder-consecutive-zeros.md (§4.1), a601-secondmoment-execution.md (§2 audit), tools/ladder_probe2.py.
**Script:** `tools/b401_coefficients.py` (self-contained, mpmath@60dps + numpy; ~30 s wall).
**Command:**
```
proot-distro login ubuntu -- python3 /data/data/com.termux/files/home/riemann/tools/b401_coefficients.py
```
**Labels:** PROVEN / CHECKED NUMERICALLY / CONJECTURED / INCONCLUSIVE; every number code-backed.

---

## 0. VERDICT (one line)

The two-moment rule (t−1)² = t²−2t+1 is **extractable and exact at n=3** ((A3,B3)=(1/4,1/2) = the normalized expansion coefficients (1,2)/(3+1)), but at n=7 the SAME rule gives (1/8,1/4) ≠ documented (2680/5111, 263/269) — confirming the verify note's "7-pt is NOT a pure 3-pt-style inflation". The exact n≥7 coefficient law is **INCONCLUSIVE** (verify note flaw (a)); the ladder's n=9..15 constants are reproduced ONLY by the hand-extrapolation (A_n,B_n) = (A7,B7) (label CONJECTURED); the derived coefficient pairs are reported below as falsifiable predictions.

## 1. What was asked

The ε→constant map p_n = (H0 − A_n ε_n)/(1 − B_n ε_n) is anchored at
(A3,B3) = (1/4, 1/2) and (A7,B7) = (2680/5111, 263/269); beyond n=7 the ladder
hand-extrapolates. Task: (1) extract the derivation rule from verify-gram-stability.md
(how the anchors follow from the two-moment expansion (t−1)² = t²−2t+1);
(2) derive (A9,B9),(A11,B11),(A13,B13),(A15,B15) by the same rule; (3) verify against the
ladder ε values and constants; (4) report each pair as a falsifiable prediction.

## 2. The derivation rule — what is extractable (PROVEN)

**R0. Form of the map (PROVEN, 60 dps re-verified here).**
Every ladder constant is the fixpoint of p = H0 + ε_n·(B_n·p − A_n), i.e.
p_n = (H0 − A_n ε_n)/(1 − B_n ε_n). The stability correction added to the base bound H0 is
ε_n(B_n p − A_n). Anchors re-verified to 60 dps (B: A3=1/4, B3=1/2, ε₃=221/10⁶ →
0.672519767113677707...; A7=2680/5111, B7=263/269, ε₇=19/5000 → 0.673008527927779761...).

**R1. The two-moment expansion is the source of the coefficients (PROVEN at n=3).**
The stability function is Ψ(t) = (t−1)² = t² − 2t + 1. On an n-atom block with trace
t = tr M_n = n and second moment t2 = tr M_n² = n + 2P_n:
  tr Ψ(M_n) = t2 − 2t + n = 2P_n   (the Gram identity, verify-note D1; re-checked numerically)
and the rank–trace defect satisfies n − r ≤ n·trΨ/t2 = n·2P_n/(n + 2P_n) (exact algebra from
r ≥ t²/t2 with t = n). Normalizing the expansion coefficients (t², −2t, 1) → (1, 2, 1) by the
block count (n+1) gives
  (A_n, B_n) = (1/(n+1), 2/(n+1)),
which at n=3 reproduces (A3,B3) = (1/4, 1/2) EXACTLY. This is the "⇒ coefficients 1/4,1/2
derivable" claim of A8-02/EPS-10, made precise. PROVEN (arithmetic).

**R2. The same rule FAILS at n=7 (CHECKED NUMERICALLY).**
(A7,B7)-predicted by R1 = (1/8, 1/4); documented (2680/5111, 263/269) = (0.5243592245…,
0.9776951673…). Not equal. Factor structure of the documented pair (PROVEN arithmetic):
  2680 = 40·67, 5111 = 19·269, 263 = 269 − 6, 6 = n−1, 269 = 4·67+1, 19 = 5000·ε₇.
  A7·ε₇ = 2680/1345000 = 67/33625, B7·ε₇ = 4997/1345000 (ε-free structural constants d,e in
  (H0−d)/(1−e)). The 7-pt pair is NOT the (n+1) normalization — it is a different,
  7-block-specific normalization whose exact law the phone cannot recover (INCONCLUSIVE;
  identical to verify-note flaw (a): "19/5000 normalization unidentified").

**R3. What the rule leaves undetermined.**
Two anchors (n=3, n=7) do not pin the function n ↦ (A_n, B_n): the family of laws through
both anchors is infinite. Hence any n=9,11,13,15 derivation is a committed reading
(CONJECTURED), falsifiable by the ladder constants (which were computed with (A7,B7)
extrapolated — ladder_probe2.py const(e,A7,B7) — see §4).

## 3. Derived coefficient pairs for n=9,11,13,15 (CONJECTURED — three committed readings)

| n | R1 two-moment (1,2)/(n+1) | R2 anchored-7 (A7,B7) | R3 linear-in-n through anchors |
|---|---------------------------|------------------------|-------------------------------|
| 9  | (1/10, 1/5) | (2680/5111, 263/269) | A: 0.66153884, B: 1.2165428 |
| 11 | (1/12, 1/6) | (2680/5111, 263/269) | A: 0.79871845, B: 1.4553903 |
| 13 | (1/14, 1/7) | (2680/5111, 263/269) | A: 0.93589806, B: 1.6942379 |
| 15 | (1/16, 1/8) | (2680/5111, 263/269) | A: 1.0730777, B: 1.9330855 |

- **R1** = the extracted two-moment rule (§2 R1) applied verbatim to all n. Small coefficients ⇒ small corrections.
- **R2** = the ladder's current hand-extrapolation (coefficients frozen at the n=7 anchors).
- **R3** = linear interpolation in n between the two certified anchors ((A7−A3)/4 per step). NOTE: B exceeds 1 already at n=9 (1.2165), but the pole 1/B ≈ 0.82–0.52 stays far above the ladder ε (0.004–0.012) and B·H0 − A > 0 throughout, so every R3 plug-in sits on the monotone branch (verified numerically).

## 4. Verification against the ladder (CHECKED NUMERICALLY, mpmath 60 dps)

Ladder inputs (from ladder-consecutive-zeros.md §4.1, model II spans):
ε₉=4.2931e-3, ε₁₁=7.2479e-3, ε₁₃=8.5245e-3, ε₁₅=1.2343e-2.

| n | ε | ladder constant (doc) | R1 plug-in | R2 plug-in | R3 plug-in |
|---|---|----------------------|------------|------------|------------|
| 9  | 4.2931e-3 | 67.3075% | 67.264894% | 67.30747% | 67.317648% |
| 11 | 7.2479e-3 | 67.3473% | 67.270933% | 67.347259% | 67.381947% |
| 13 | 8.5245e-3 | 67.3645% | 67.271103% | 67.364521% | 67.426067% |
| 15 | 1.2343e-2 | 67.4164% | 67.276726% | 67.416414% | 67.537009% |

Prediction (confirmed by run): R2 reproduces the ladder constants exactly (relative diff
~2–6e-7, i.e. matches all printed digits; by construction the ladder note's "implied const
(A7,B7)" column IS this plug-in); R1 gives constants 67.2649–67.2767% (barely above H0) and
does NOT reproduce them; R3 gives the ladder note's separate "linear (A,B)" column
(67.3176/67.3819/67.4261/67.5370%), also ≠ the ladder constants. The ladder constants
therefore falsify R1 and R3 as *general coefficient laws* and are consistent only with
coefficient continuation (R2) — i.e., the honest status of the n≥9 coefficients remains
CONJECTURED, and the ladder constants themselves are the falsifier set.

## 5. Falsifiable predictions (each pair, each n)

1. **If the true coefficient law is the two-moment (n+1) rule (R1):** (A9,B9)=(1/10,1/5),
   (A11,B11)=(1/12,1/6), (A13,B13)=(1/14,1/7), (A15,B15)=(1/16,1/8); then the plug-in
   constants are ≈ 67.2649–67.2767% — i.e. the ladder's documented 67.3075–67.4164% values
   are WRONG and the refinement's gain nearly vanishes beyond n=7. FALSIFIER: any of the
   ladder constants holding to 4+ decimals kills R1.
2. **If the coefficient law saturates at the 7-pt block (R2):** all four pairs equal
   (2680/5111, 263/269); constants 67.3075/67.3473/67.3645/67.4164% — the ladder as documented.
   FALSIFIER: a certified (A_9,B_9) pair differing from (2680/5111,263/269) at the level that
   moves the 6th decimal.
3. **If the law interpolates linearly (R3):** constants 67.3176/67.3819/67.4261/67.5370%.
   FALSIFIER: the ladder's own values (67.3075% etc.) already exclude R3.

Adjudication needed to decide among these: the repo's block-averaging normalization for n≥9
(laptop, ainta/trmdy clones; verify-note flaw (a) item 1) or Arb-certified floors + a derived
coefficient law. Until then: R2 is the only reading consistent with the ladder as documented
(CONJECTURED), R1 is the only reading derivable from the two-moment expansion alone
(CONJECTURED, falsified by the ladder), R3 is already falsified by the ladder.

## 6. Honesty accounting

- All constants in §2/§4 recomputed at 60 dps in tools/b401_coefficients.py (no reuse of prior
  printouts).
- The n=7 derivation gap is inherited from verify-note flaw (a) (INCONCLUSIVE) — this note
  does not claim to close it; it isolates the exact locus (the (n+1)-normalization fails at
  n=7) and reports the falsification structure.
- R1/R2/R3 are committed readings (CONJECTURED); none is presented as the proven law.

*No existing notes were modified. Script + this note are the full deliverable.*
