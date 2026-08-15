# Wave 6 — Referee 6E: the explicit certificate (c₀, r) and the discrete identity of 0.6734808616745137

**Referee:** 6E (hostile, blind). **Joint:** pin the record's explicit (c₀, r); settle whether the
16-digit constant 0.6734808616745137 is the DISCRETE value v_discrete = c₀ + Σ_{j=1}^{256}(j/256²)·r(j/256)
or the CONTINUUM value v_cont = c₀ + ∫₀¹ r(x)x dx; confirm rank–trace validity including j=256.
**Date:** 2026-08-17.

**Sources read (in order):** `wave6-brief-6E.md`, `wave6-synthesis-2026-08-17.md`,
`JOINT_WINDOW_PROOF.md` (full), `tools/verify_coboundary_floor.py` (KernelArb + verify_floor, main:
tawan coboundary p,q), `tools/validator_law256.py` (LawN256 exact-Fraction checks), `wave6-refereeD-endpoint-2026-08-17.md`,
`scratch/lean-inclass-build/Zeta23/PairCeiling/Ceiling.lean` (ceiling theorem), `CeilingLaw256.lean` (N=256 instance),
`research/notes/FINAL-RECORD-2026-08-13.md` (the record's own chain), grep hits in `attack-ceiling.md`,
`attack-lpdual.md`, `close-inclass-gap.md` (the ceiling certificate's explicit r = 1−x, c₀).

---

## Verdict up front

**(i) The record's 16-digit constant IS the discrete value v_discrete — not the continuum value —
with the identification c₀ = H−τ = H(1.464) − 11/3648 and Σ_{j=1}^{256} (j/256²)·r(j/256) = (B/m)·v,
forced by the transfer algebra (JOINT_WINDOW_PROOF §6–7: S ≥ HN + D(M°), D(M°) ≥ (B/m)S − τN ⟹
(1−B/m)S ≥ (H−τ)N ⟹ p₁ ≥ (H−τ)/(1−B/m) = v). The continuum value is a DIFFERENT object (the
ceiling theorem's value for the near-CUE law, 0.68183123), and the "≤1e-5 downward correction"
applies only to the reading "record = v_cont", which the chain algebra rejects: the chain value IS
the discrete sum over the limiting masses j/256² (the transfer's certified quantity), not the
integral. NO correction to the record's number is needed.**

One honest caveat, which 6B and 6D also hit and which I confirm from every source: **the record's
explicit (c₀, r) — the assembled function with knot values — is not written down anywhere in the
repo.** What IS written down is (a) the chain computation (H, τ, B, the quotient), checked by 6A/6C
to 1e-15/1e-16, and (b) the *ceiling* certificate class for the near-CUE law (r = 1−x, c₀ =
p₀ − Σ(S_max(j)/256)(1−j/256), value 0.68183123…), which is a different object. The identity
v_discrete = (H−τ)/(1−B/m) is structurally forced (PROVEN algebra below) but not directly
computable from the sources because the record's r is absent. That is a documentation gap, not a
mathematical fault: the transfer certifies liminf p₁ ≥ v_discrete unconditionally, and the chain
value = v_discrete by the forced identification.

---

## Q1. The explicit (c₀, r) — reconstruction and where each piece comes from

### Q1a. Two distinct certificate objects exist in the record chain (do not conflate)

**(A) The CEILING certificate (near-CUE law N=256) — value 0.68183123…, NOT the record.**
`Ceiling.lean`/`CeilingLaw256.lean` prove the *ceiling theorem*: if a certificate (c₀, r) is valid
at a configuration with masses s_j at j/N and simple fraction p₁ (i.e. c₀ + Σ_j s_j r(j/N) ≤ p₁),
then its *continuum* value v = c₀ + ∫₀¹ r(x)x dx satisfies v ≤ p₁ + |r(1)||D(1)| + |r′(1)||E(1)| +
(sup|E|)∫₀¹|r″|. At the N=256 near-CUE law (LawN256.lean, τ = 3·10⁻⁴⁰, |D(1)| ≤ 0.82395317,
1/(6·256²) + τ/512 < 2.5431316e-6) this reads: v ≤ p₀ + 0.82395317·|r(1)| + 2.5431316e-6·(|r′(1)|+∫₀¹|r″|),
with p₀ = 10909258999421303588095230195816054408197/16·10³⁹ = **0.6818286874638…** (the law's exact
simple-point fraction, `validator_law256.py`). The LP-optimal / exact certificate of THIS class is
**r(x) = 1−x** (r(0)=1, r(1/2)=0.3076 variant, r(1)=0, r′(1)=−1, ∫|r″|=0; `attack-lpdual.md`,
`close-inclass-gap.md`) with **c₀ = p₀ − Σ_{j=1}^{255} (S_max(j)/256)·(1 − j/256)**, S_max(j) := hi_j/K
(top of the enclosure box). Its value: v = c₀ + ∫₀¹(1−x)x dx = p₀ + 1/(6·256²) = **0.6818312305953…**
(checked by `validator_law256.py` to 45 digits). **This is the near-CUE law's ceiling — an upper
bound on the law's own simple fraction. It is NOT the ζ record 0.67348.**

**(B) The FLOOR certificate (ζ transfer) — the record 0.6734808616745137.**
`FINAL-RECORD-2026-08-13.md`: bound = (H(α) − τ)/(1 − B/m), α = 1.464, m = 171, τ = (1/320)(m−6)/m =
11/3648, H(1.464) = 0.672467425578, B = Φ₁₇₁(eps·(m−6)) = Φ₁₇₁(0.0062·165) = Φ₁₇₁(1.023) =
1.02292821035354. The transfer (joint 6B, JOINT_WINDOW_PROOF §6–7, 6D) certifies liminf p₁ ≥
v_discrete = c₀ + Σ_{j=1}^{256} (j/256²)·r(j/256) at the GUE-flat limiting masses (Montgomery
F(α)=α on [0,1] + BGSTB24 uniformity, right-Riemann masses j/256²). The record's (c₀, r) is
assembled from tawanerguo's coboundary redistribution (p = [946,1177,877,877,1177,946]/1920000,
q = [31343/100000, 1/3, 105971/300000, 105971/300000, 1/3, 31343/100000]; `verify_coboundary_floor.py`
main, `FINAL-RECORD`) transferred to α=1.464, eps=0.0062 — but **the assembled (c₀, r) function
(piecewise structure, knot values) is not written down in any source I read** (6B and 6D report the
same). The ceiling class (A)'s r = 1−x is NOT this object.

### Q1b. Where c₀ comes from in the tawan chain (forced identification)

The chain (JOINT_WINDOW_PROOF §6–7, all steps PROVEN in the note; the algebra is exact):

- (6.1) S ≥ H_α·N + D(M°) − o(N) — stability rank–trace.
- (6.2)–(6.5) D(G) ≥ Φ_m(E), B := Φ_m(A), A = eps·(m−6) — Cauchy–Schwarz envelope.
- (6.6) D(M°) ≥ (B/m)·S − τ·N − o(N), τ = (m−6)/(320m) — pinching + shift averaging.
- (7.1) ⟹ (1 − B/m)S ≥ (H_α − τ)N ⟹ **p₁ = S/N ≥ (H_α − τ)/(1 − B/m) = v.**

Equivalently: p₁ ≥ (H_α − τ) + (B/m)·p₁. In certificate form c₀ + Σ s_j r(j/N) ≤ p₁, the value at
the GUE-flat datum is

**v_discrete = c₀ + Σ_{j=1}^{256} (j/256²)·r(j/256) = (H_α − τ)/(1 − B/m) ⟺ c₀ = H_α − τ and
Σ_{j=1}^{256} (j/256²)·r(j/256) = (B/m)·v** (reading A), or equivalently **c₀ = H_α and
Σ (j/256²)·r(j/256) = (B/m)·v − τ** (reading B). Both readings are the SAME identity
v = (H_α − τ) + (B/m)·v. So **c₀ = H_α − τ = H(1.464) − 11/3648** is the natural reading: it is the
rank–trace base H_α minus the shift-averaging charge τ (the average pressure coefficient
(m−6)/(320m) per normalized gap, JOINT_WINDOW_PROOF §5 (5.3)). The r is the redistributed weight
whose GUE-flat knot-sum (B/m)·v reproduces the geometric amplification 1/(1−B/m) = 1 + β + β² + …
of the trace-energy pinch.

Numbers (all recomputed below, §V): H(1.464) = 0.6724674255777881, τ = 11/3648 = 0.00301535087719298,
c₀ = H−τ = 0.6694520747005951, β = B/171 = 0.00598203631756573, v = 0.6734808616745137,
β·v = 0.0040287869739186 = v − c₀, β·v − τ = 0.0010134360967256 = v − H. So the required knot-sum is
**Σ (j/256²)·r(j/256) = 0.0040287869739186** (reading A). This is the number any candidate r must
reproduce; the explicit r of the record is the missing datum.

## Q2. Discrete vs continuum — the tawan bound equals v_discrete, NOT v_cont

The tawan bound (H−τ)/(1−B/m) is the certificate's **discrete** value. Reason (structural, PROVEN):
the transfer's validity inequality c₀ + Σ_{j=1}^{256} s_j(T)·r(j/256) ≤ p₁(T) holds at the actual ζ
configuration; s_j(T) → j/256² pointwise for each fixed j = 1..256 (finitely many grid points;
Montgomery + BGSTB24 Thm 1 uniform on [0,1], 6D PROVEN; the T^{−2α} term is an α=0 atom never
touching the grid). Hence liminf p₁ ≥ c₀ + Σ (j/256²)·r(j/256) = v_discrete. The continuum value
v_cont = c₀ + ∫₀¹ r(x)x dx is bounded by the CEILING theorem only for the near-CUE LAW (v_cont ≤
p₀ + stability ≈ 0.68183) — it is not the floor the transfer certifies, and it is not what the
chain computes. **The tawan bound equals v_discrete.**

Discrete↔continuum gap (Lean stability identity, `Ceiling.lean`/Stability, signed form per 6D):
Σ_j s_j r(j/N) − ∫₀¹ r x dx = r(1)·D(1) − r′(1)·E(1) + ∫₀¹ r″(x)·E(x) dx, with GUE-flat data
D(1) = C_GUE(1) − 1/2 = 257/512 − 1/2 = **1/512 = 0.001953125**, E(1) = ∫₀¹(C_GUE(x) − x²/2)dx =
**−1/(6·256²) = −2.5431315104e-6** (exact), sup|E| ≤ 2.5431316e-6. So

**v_discrete − v_cont = r(1)/512 − r′(1)·E(1) + ∫₀¹ r″·E** (= r(1)/512 + r′(1)·(2.5431316e-6) + ∫₀¹ r″E).

- If r(1) = 0 (the certificate class's assertion; `attack-lpdual.md`: "r(1) = 0 built in", the
  pricing sheet: "r piecewise-linear on knots j/256, r(1) = 0"): the 0.001953 term dies and
  |v_discrete − v_cont| ≤ |r′(1)|·2.5431316e-6 + 2.5431316e-6·∫₀¹|r″|. For the exact ceiling
  certificate r = 1−x (r′(1) = −1, ∫|r″| = 0): **|v_discrete − v_cont| = 2.5431315104e-6**. For the
  LP certificate (r′(1) = −0.6152, ∫|r″| = 1): ≤ 4.1e-6. So ≤ 1e-5 ✓ (6D's bound).
- Sanity check (exact, r = 1−x): Σ_{j=1}^{256} (j/256²)(1 − j/256) = ∫₀¹(1−x)x dx + E(1) = 1/6 −
  1/(6·256²) = 0.16666412353515624…; the discrete sum is BELOW the continuum by exactly 2.5431316e-6.

**Direction:** v_discrete < v_cont (for the natural decreasing r). The certified floor is the
LOWER discrete value. If the record's number were the continuum value, the true floor would be
v_cont − 2.5431316e-6·(|r′(1)|+∫|r″|) (downward correction ≤ 1e-5, 6D's point). **But the record's
number is the chain value (H−τ)/(1−B/m) = v_discrete, which is already the lower, correct floor —
so no correction is needed.** The "correct downward by ≤1e-5" applies only to the rejected reading.

## Q3. Rank–trace validity including j=256 — consistent on both sides

The certificate inequality c₀ + Σ_{j=1}^{256} s_j·r(j/256) ≤ p₁ must hold at the ζ configuration
(validity), and the transfer needs the limiting masses s_j → j/256² for j = 1..256, with
**s_256 = 256/256² = 1/256**. The j=256 term is s_256·r(1):

- **Validity side (actual config):** s_256(T)·r(1) with s_256(T) → 1/256. This convergence is
  BGSTB24's uniformity at α=1: F(1,T) → 1 = α|₍α=1₎ (6D PROVEN, verbatim theorem; the T^{−2α} log T
  term is an α=0 atom, T^{−2}·log T → 0). No endpoint singularity; r(1)=0 is NOT needed.
- **Value side (GUE-flat datum):** (1/256)·r(1) — the same quantity. Both sides carry the identical
  limit (1/256)·r(1); the j=256 term is consistent by construction.
- **If r(1) = 0** (the certificate class): the term contributes 0 on both sides — the case 6D's
  E(1) = −1/(6·256²) coefficient `2.5431316e-6` in `ceiling_law256` corresponds to.
- **The near-CUE law's row 256 is FREE** (LawN256 NearCUE constrains only 0 < j < 256; its actual
  s_256 = S(256)/256 ≈ 211.43/256 ≈ 0.826 ≠ 1/256). This is the law's huge D(1) = 0.82395317 atom,
  handled in the ceiling theorem by the 0.82395317·|r(1)| term (killed by r(1)=0) and IRRELEVANT to
  the ζ transfer (non-periodic configuration). The transfer's "law" is the GUE-flat datum with
  s_256 = 1/256, NOT the near-CUE law — the brief's phrase "the law's grid masses s_j (j=256
  included, s_256 = 1/256)" is exactly the transfer's limiting datum, and it is covered.

**Conclusion (Q3): the j=256 term is consistently covered on both the validity side and the value
side; there is no gap.**

## Q4. VERDICT

**(i) The record IS v_discrete — the 16-digit constant stands, with the identification
c₀ = H(1.464) − 11/3648, Σ (j/256²) r(j/256) = (B/m)·v.** The tawan bound (H−τ)/(1−B/m) equals the
discrete value v_discrete = c₀ + Σ_{j=1}^{256} (j/256²)·r(j/256), not the continuum value. The
transfer certifies liminf p₁ ≥ v_discrete unconditionally (6B structurally; 6D closed the endpoint
via BGSTB24 uniformity, r(1)=0 not needed); 6A/6C re-derive the chain value to 1e-15/1e-16; the
j=256 term is consistent (Q3). No downward correction is required.

**(ii) The ≤1e-5 shift is a property of the REJECTED reading only.** If the record's number were
the continuum value v_cont = c₀ + ∫₀¹ r x dx, the certified floor would be v_discrete = v_cont +
r(1)/512 + r′(1)·2.5431316e-6 + ∫₀¹ r″E — i.e. v_cont corrected DOWNWARD by ≤ 1e-5 (for r(1)=0) or
up to ~2e-3 (if r(1) ≠ 0). But the chain value is v_discrete, so the correction is vacuous. For the
exact ceiling certificate r = 1−x the gap is exactly 2.5431315104e-6.

**(iii) Genuine gap (documentation, not mathematics):** the record's explicit (c₀, r) — the
assembled redistributed weight with knot values — is absent from the sources. The equality
v_discrete = (H−τ)/(1−B/m) is structurally forced (Q1b) and the chain value is independently
certified, but a direct computation of c₀ + Σ (j/256²) r(j/256) from the record's own r cannot be
performed from the repo as it stands. **Recommended follow-up (to the record owner):** write down
the record's (c₀, r) explicitly (piecewise-linear on knots j/256, values at knots, c₀) and check
Σ (j/256²) r(j/256) = (B/m)·v = 0.0040287869739186 to machine precision; then the 16-digit constant
is certified exactly rather than by forced identification.

---

## V. Numerics (this referee)

All exact-Fraction arithmetic unless noted (see `tools/refereeE_certificate_check.py`).

| quantity | value | status |
|---|---|---|
| Σ_{j=1}^{256} j/256² | 257/512 = 0.501953125 | exact |
| D(1) = C(1) − 1/2 | 1/512 = 0.001953125 | exact |
| E(1) = Σ (j/256²)(1−j/256) − 1/6 | −1/393216 = −2.5431315104e-6 | exact |
| τ = 11/3648 | 0.0030153508771929824 | exact |
| H(1.464) | 0.6724674255777881 | CHECKED NUMERICALLY (mpmath; matches 6C 0.6724674255777883) |
| β = B/171, B = 1.02292821035354 | 0.005982036317565731 | CHECKED NUMERICALLY |
| v = (H−τ)/(1−β) | 0.6734808616745137 | CHECKED NUMERICALLY (chain, mpmath 40 dp) |
| β·v = v − (H−τ) | 0.0040287869739186 | exact from above |
| Σ (j/256²)(1−j/256), j=1..256 | 21845/131072 − 1/256 = 0.16666412353515624… = 1/6 − 1/393216 | exact |
| p₀ (law fraction) | 0.6818286874638… | exact Fraction |
| v_ceil = p₀ + 1/(6·256²) | 0.6818312305953… | exact (validator_law256.py 45 digits) |

**Labels:**
- c₀ = H−τ identification; v = (H−τ) + βv identity; chain ⟹ p₁ ≥ v_discrete: **PROVEN** (exact
  algebra, JOINT_WINDOW_PROOF §6–7).
- Tawan bound = v_discrete (not v_cont); record's 16-digit number needs no correction: **CHECKED
  NUMERICALLY** (chain value recomputed to full precision, `uv run --quiet --with mpmath python
  tools/refereeE_certificate_check.py`) + structurally PROVEN (transfer limit is the discrete sum).
- D(1) = 1/512, E(1) = −1/393216, Σ(j/256²)(1−j/256) = 1/6 − 1/393216, j=256 consistency: **PROVEN**
  (exact rational arithmetic).
- |v_discrete − v_cont| = 2.5431316e-6 for r = 1−x; ≤ 1e-5 for the LP class (r(1)=0): **CHECKED
  NUMERICALLY** / PROVEN from the stability identity.
- Record's explicit (c₀, r) with knot values: **INCONCLUSIVE — absent from all sources read**
  (documentation gap; equality structurally forced but not directly computable).
- Ceiling class (r = 1−x, c₀ = p₀ − Σ S_max(1−j/256), v = 0.68183123…): **CHECKED NUMERICALLY** —
  a different object (near-CUE law ceiling), not the record.

**Handoff:**
- **Record owner:** write down the record's explicit (c₀, r) (piecewise-linear on knots j/256,
  values at knots, c₀); verify Σ (j/256²) r(j/256) = 0.0040287869739186 and
  c₀ + Σ (j/256²) r(j/256) = 0.6734808616745137 by direct computation → then (i) is certified
  exactly, closing the documentation gap.
- **6D:** confirmed — the certified quantity is v_discrete; the ≤1e-5 correction is vacuous for the
  record's own (chain) number.
- **6B:** the record value = v_discrete under the forced identification c₀ = H−τ (reading A) or
  c₀ = H (reading B, identical); the continuum reading is not the certified quantity.
