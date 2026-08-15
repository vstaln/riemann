# Referee A — hostile blind attack: sinc-m3 marked-law model mathematics

**Joint:** the marked-law model (moments, D, P₃, m₂, floor, calibration) behind
`tools/sinc_m3_cert` and the claimed κ* = min-p₁ + |E(1)| = 0.7488 > 0.6818.
**Author:** refereeA (hostile blind referee). **Date:** 2026-08-17.
**Probe:** `tools/referee_a_probe/` (Rust, musl, no deps; command below).
**VERDICT: the model does NOT survive. κ* = 0.7488 is not a valid in-class ceiling above
0.6818.** Three independent breaks: (B) the binding constraint runs on the UNPROVEN
E[T] ≥ 0; under the proven floor min-p₁ = 0.42 (mass) / 0.59 (count) < 0.6818; (A) the
0.7488-vs-0.6818 comparison mixes MASS (model p₁) with COUNT (the wall p₀); (F) the result
is a knife-edge on calibration (5% shift flips the verdict).

## Verdict table

| # | Joint item | Verdict | Evidence |
|---|---|---|---|
| 1 | Marked-law normalization P(m=1)=2p₁/(1+p₁) | **BREAK (category mix)** | model p₁ = MASS fraction (mass-simple/total-mass); wall p₀ = COUNT ("simple-point fraction", "proportion of simple on-line zeros", attack-ceiling §1; Lean `ceiling_law256`). Mass↔count: p↔p/(2−p). Count-normalized full-floor min-p₁ = **0.8564**, not 0.7488. Direct comparison 0.7488 vs 0.6818 mixes conventions |
| 2 | Row-0 formula E|μ̂(0)|² = E[m²]/N + (N−1)E[m]²/N | **PASS** | code uses 1/N-normalized DFT (kh[m]=s/N); row-0 = E|(1/N)Σm_i|² = em2/N + (N−1)em²/N, re-derived ✓ |
| 3 | Pair rows E|μ̂(k)|² = c·k | **PASS (class axiom), caveat** | flat rows define the admissible class; real-zeros F≡1 justification for all k≤254 (α>1) is CONJECTURED (attack-ceiling §3: nothing proven beyond |α|≤1) |
| 4 | P₃ (two-equal) algebra | **PASS** | re-derived e_mu2mu(0)=em3/N+(N−1)em2·em/N, e_mu2mu(k≥1)=em3/N+em2·c·k/em−em2²/(N·em) from E[f(q)ḡ(q)] with marked rows + mark independence — matches code exactly; independent p₁=1 check P₃(1)=3[N·kk0−1+N·c·C]=3.678 ≈ code 3.66 |
| 5 | Floor = max(D+P₃, m₂²) | **BREAK (decisive)** | needs E[T] ≥ 0 (S₃ ≥ D+P₃), UNPROVEN; FALSE per-config for PSD Gram: 3×3 G=[[1,a,a],[a,1,a],[a,a,1]], a=−0.2 (PSD ev 0.6,1.2,1.2, all marks 1): m₃=1.224 ≥ m₂²=1.1664 (theorem HOLDS) yet T=m₃−D−P₂=−0.016<0 ⇒ S₃ can dip BELOW D+P₃ (probe). Proven floor is only m₂²(p₁). Under m₂²-floor: **min-p₁ = 0.4224 (mass) / 0.5939 (count), both < 0.6818** (probe) |
| 6 | Calibration m₂(1)=2.22 ← real-zeros sinc m₂²=4.9256 | **FRAGILE** | 4.9256 CHECKED (marked-moment note). But min-p₁ is knife-edge: mass conv m₂(1)=2.00→κ=0.466, 2.11→0.608, 2.22→0.749, 2.33→0.870 (binary); count conv 2.00→0.636, 2.11→0.756, 2.22→0.856. Real-zeros SE ~7% ⇒ m₂(1)∈[2.15,2.29] straddles the flip in BOTH conventions |
| 7 | Binding = D+P₃ = 5.44 (read top), m₂² = 5.02 slack | **CONFIRMED** | scan at p₁=0.7488: D+P₃=5.4400, m₂²≈4.99. The m₃≥m₂² theorem does NO work; the claim's real content is "D+P₃(p₁) ≤ 5.44 ⇒ p₁ ≥ 0.7488", valid ONLY under unproven E[T] ≥ 0 |

## Control demand

- **256-law (p₀ = 0.6818287, count simple-point fraction; mass-fraction = p₀/(2−p₀) = 0.517253):**
  floor(full) = 6.0436 ∉ [4.56, 5.44] → excluded ONLY under unproven E[T] ≥ 0.
  floor(proven) = m₂² = 5.2488 ∈ [4.56, 5.44] → **NOT excluded by proven inputs** (probe).
- Under the proven floor, a law at mass-p₁ = 0.5173 (the 256-law itself) has floor 5.25 in the
  window ⇒ **admissible with p₁ = 0.5173 < 0.7488 — CONTROL EXHIBITED** (the certificate's
  exclusion of the p₀-region is not theorem-backed).
- Under the proven floor the min-p₁ over the class is 0.4224 (mass), well below the wall.

## Probe numbers (tools/referee_a_probe, cargo build --release --target x86_64-unknown-linux-musl)

```
calibration c = 0.00003484 (both conventions; m2(1)=2.22, m2(1)^2=4.9284 ≈ real-zeros 4.9256)
scan p1=0.6818: D+P3(mass)=5.6184  m2^2=5.0386 | D+P3(count)=6.0437 m2^2=5.2488
min-p1 (eps=0.44):  full/mass 0.748807 k=0.748809 >0.6818
                    prov/mass 0.422384 k=0.422386 <=0.6818
                    full/count 0.856363 k=0.856366 >0.6818
                    prov/count 0.593909 k=0.593912 <=0.6818
256-law control: mass p1=0.517253: floor(full)=6.0436 not-in-window; floor(proven)=5.2488 IN-window
calib (count): m2(1)=2.00->k=0.636 | 2.11->0.756 | 2.22->0.856 | 2.33->0.930 | 2.44->EMPTY
3x3 PSD a=-0.2: m3=1.2240 >= m2^2=1.1664 (theorem HOLDS); T=m3-D-P2=-0.0160 < 0 (E[T]>=0 FALSE)
```
Note: floors are only approximately decreasing over [0,1] (max non-monotone step 1e-4, probe) —
the bisection min-p₁ is accurate to ~1e-3, immaterial to the verdict.

## Why each break is decisive
- **(B) floor / E[T] ≥ 0.** The code's floor takes max(D+P₃, m₂²); at the optimum the max is
  D+P₃ = 5.44 with m₂² = 4.99 slack (attack 7). D+P₃ is a valid S₃-lower-bound only if
  E[T] ≥ 0. The 3×3 PSD counterexample shows T < 0 occurs with the theorem m₃ ≥ m₂² intact,
  so E[T] ≥ 0 is not a consequence of PSD; no note states it as a theorem. Under the ONLY
  proven bound (S₃ ≥ E[m₂²] ≥ m₂²), min-p₁ drops to 0.42 (mass) — the read then forces
  κ ≈ 0.42, i.e. the m₃-read certificate has NO power above the wall. The claimed 0.7488 is
  an artifact of an unproven inequality.
- **(A) convention mix.** attack-ceiling defines the certificate's p₁ as the simple-POINT
  fraction (count) and the ceiling as "proportion of simple on-line zeros". The marked-m3
  program silently re-interprets p₀ as a mass fraction (synthetic family draws marks at
  P(m=2)=q=(1−p₀)/(1+p₀) and measures realized p₁ ≈ 0.68 = mass fraction). The sinc-m3 claim
  then prints a mass-fraction κ* = 0.7488 against the count-fraction wall 0.6818. Same-quantity
  recompute (count normalization, still granting E[T]≥0) gives min-p₁ = 0.8564 — the honest
  comparison number, not 0.7488.
- **(F) calibration.** min-p₁ sits on the steep part of the m₂(1)-calibration curve in both
  conventions; a ±5% calibration shift (well within the real-zeros measurement SE) moves κ*
  across the wall in both directions. Not a robust record even under the (broken) model.

## Honesty labels
- P₃ algebra, row-0, code-internal consistency: **CHECKED** (independent derivation + p₁=1 value).
- E[T] ≥ 0 false per-config (PSD Gram): **PROVEN** (3×3 counterexample, probe).
- Proven-floor min-p₁ 0.4224/0.5939; full-floor min-p₁ 0.7488/0.8564; 256-law floors;
  calibration sensitivity: **CHECKED NUMERICALLY** (probe, musl binary).
- Convention mix (mass vs count): **PROVEN** by definition reading (attack-ceiling §1/Lean).
- α>1 pair-row justification: **CONJECTURED** (literature; not needed for the break).
- Real-zeros m₂² = 4.9256: CHECKED in marked-moment-inequality-2026-08-17.md (not re-derived here).

## Conclusion
The sinc-m3 certificate's κ* = 0.7488 does not survive hostile review. (1) Its binding
constraint D+P₃ = 5.44 is only a lower bound on S₃ under the unproven E[T] ≥ 0, which is
false per-config for PSD Gram; the theorem-backed floor (m₂²) gives min-p₁ ≈ 0.42–0.59,
below the wall 0.6818, and the 256-law itself is admissible under proven inputs (control
exhibited). (2) The printed comparison mixes mass-fraction p₁ with the count-fraction wall.
(3) The result is a knife-edge on the calibration constant. The m₃ ≥ m₂² theorem (marked-
moment-inequality) is genuine but contributes nothing to this certificate (m₂² is slack at
the optimum). The claim "in-class ceiling above 0.6818 via the sinc-m3 marked-m₃ read" is
**REFUTED as stated**; what survives is the much weaker CHECKED fact that IF one grants
E[T] ≥ 0 and the mass convention, min-p₁ = 0.7488 — neither hypothesis is established.
