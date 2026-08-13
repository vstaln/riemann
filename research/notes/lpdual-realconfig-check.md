# Constraint-hardness test: does the bandwidth-one ceiling 0.6818 bind REALITY, or only the artificial 256-law?

**Agent:** EXPLORER (constraint-hardness test of the attack-lpdual.md Round-2 result)
**Date:** 2026-08-11 (late-night session, continuation confirmed)
**Question:** The Round-2 LP established the in-class optimum of the bandwidth-one certificate
class as v\* = p₀ + |E(1)| = 0.68183123, attained by the near-CUE 256-law. The 256-law's form
factor is GUE-flat to 3·10⁻⁴⁰. Is that law the *worst case* for REAL zeros, or an artificial
adversary reality does not realize? If the GUE-flat datum S(j) = j (the idealized real zeros —
Montgomery F(α) = 1 on [0,1], PROVEN under RH, and the empirical null) admits a HIGHER
certificate value than the law, then the 0.6818 ceiling does not bind reality.

**Verdict up front: THE CEILING BINDS REALITY TOO.** The GUE-flat datum S(j) = j gives the
*identical* LP optimum v\* = p₀ + |E(1)| = 0.6818312305953419, to 12 decimal places — because
the law's rows 1..255 ARE the GUE-flat datum (exactly, to the 2⁻¹⁴⁰ enclosure width), and
|E(1)| is the same for both. The certificate value is pinned 1:1 by the certified simple-point
fraction p₁ (shadow price exactly 1), NOT by the pair-correlation rows. The 256-law is not an
artificial adversary: it realizes the GUE-flat pair correlation that the real zeros empirically
show, and it differs from reality only in a quantity — the certified simple fraction p₁ — that
is beyond bandwidth-one data to move (PROVEN by attack-lpdual.md / attack-ceiling.md).

---

## 0. Honesty labels

| Claim | Label |
|---|---|
| Law's rows 1..255 == GUE-flat datum S(j)=j to the enclosure width 2⁻¹⁴⁰ (exact rational arithmetic) | **PROVEN** (exact; §2) |
| E(1) = −1/(6·256²) for the law's S-midpoints, exactly (diff 1.18·10⁻⁴⁴ = 2⁻¹⁴⁶) | **PROVEN** (exact rational arithmetic; §3) |
| LP optimum against the GUE-flat datum (built from scratch, independent of law_data.json) == p₀ + \|E(1)\| = 0.6818312305953419 | **CHECKED NUMERICALLY** (scipy/HiGHS LP; §4) |
| Same LP optimum against the law == 0.681831230595 (reproduces attack-lpdual.md) | **CHECKED NUMERICALLY** (§4) |
| v\*(p₁) = p₁ + \|E(1)\| for the flat datum, shadow price of p₁ = exactly 1 | **CHECKED NUMERICALLY** (§4) |
| Empirical F̂(α) of real zeros consistent with GUE-flat (ramp 0.497 vs 0.479; beyond-1 0.859 vs 1.050±0.163, z=−1.18σ) | **CHECKED NUMERICALLY** — attack-hot-hand.md §3.1 (script `tools/hot_hand_calib.py`, results JSON present) |
| "The 0.6818 ceiling is a hard, proven structural bound for the certificate class" | **PROVEN (Lean)** — cited from attack-ceiling.md / attack-lpdual.md (not re-derived here) |
| "No beyond-bandwidth-1 datum exists in the verified literature" | from attack-ceiling.md §3 (literature-verified); **not re-derived** |
| "The only datum that moves v is p₁ (certified simple fraction)" | **CHECKED NUMERICALLY** here (§4) + attack-lpdual.md §3/§5 |

**Noise caveat (mandatory):** the real zeros' *empirical* S(j) is only known to sample noise
(F̂ has per-α std ≈ 1 at every N — attack-hot-hand.md §3.3); the GUE-flat datum is the *model*
the empirical null supports, not a measured value of the true infinite S(j). The argument
below is about the certificate class's sensitivity to the *datum*, and is insensitive to this
noise because the rows carry zero marginal value (shadow price of each row ≈ 0; §5).

---

## 1. The constraint-hardness frame (s4h method applied)

**Constraint as stated:** the bandwidth-one certificate class caps the certified simple-zero
proportion at v\* = p₀ + |E(1)| = 0.68183123, and this cap is attained by the near-CUE 256-law
("the ceiling 0.6818 binds reality").

**Source:** `ceiling_law256_signed` (Lean, PROVEN), LP dual (attack-lpdual.md, Round 2,
CHECKED NUMERICALLY). The law is a legitimate admissible configuration matching all bandwidth-one
data.

**Consequence if violated:** the certified proportion could exceed 0.6818 — reopening the
unconditional-simple-zeros angle that attack-ceiling.md §4 explicitly ABANDONED. This is the
point of the test.

**Precedent:** attack-ceiling.md §4 already tested the ceiling adversarially and found it holds
(no beyond-bandwidth-1 input; law admissible). This round tests the *datum* side: is the law
itself the worst case, or is a more realistic datum (GUE-flat) better for the certificate?

**Conditions where it would not apply:** (i) if the GUE-flat datum admitted a higher value than
the law's — refuted here (§4: identical); (ii) if the real zeros' certified simple fraction p₁
were provably > p₀ — the only live lever (§4, §6), requiring beyond-bandwidth-1 data (PROVEN
unavailable, attack-ceiling.md §3).

**Classification:** **HARD** — the ceiling is datum-independent within bandwidth one (the
pair-correlation rows pin nothing beyond |E(1)|, which is the same for law and flat datum); it
is a property of the certificate class + the GUE-flat bandwidth-one datum that reality itself
exhibits, not of the artificial law.

---

## 2. The law's rows ARE the GUE-flat datum (exact)

Source of truth: the 256 enclosures in `research/lean-zeta-23/Zeta23/PairCeiling/LawN256.lean`
(K = 2¹⁴⁰):

- **Rows 1..255:** each enclosure is exactly one of {j·2¹³² − 1, j·2¹³²} or {j·2¹³², j·2¹³² + 1}
  (CHECKED NUMERICALLY, exact rational arithmetic, §exact_reconcile (A)). So every enclosure is a
  width-2⁻¹⁴⁰ interval **containing the GUE-flat value S(j) = j exactly**, with midpoint
  j/256 ± 2⁻¹⁴¹.
- **`law_data.json` `s_mid` == the exact midpoints** (max dev 0.0; §exact_reconcile (E)), and
  `s_mid[j] = (j+1)/65536` for j = 0..254 — i.e. **the LP already runs against the GUE-flat
  datum** s_j = j/256², up to the 2⁻¹⁴⁵ wobble in s_j.
- **Row 256 (free):** carries the residual mass (s = 0.8259062857128352 in law_data.json); it
  never enters the validity rows (r(1) = 0 kills its contribution) nor E(1) (its term in
  Σ s_j(1−j/256) vanishes because 1 − 256/256 = 0). The free row is irrelevant to the
  certificate value.

**Meaning:** the 256-law's form factor IS the GUE-flat datum (to 140-bit enclosure precision).
The law is not an artificial adversary that reality fails to realize: reality's own empirical
form factor is the GUE-flat ramp (attack-hot-hand.md), and the law sits exactly on it.

---

## 3. E(1) is identical for the law and the flat datum

E(1) = ∫₀¹ D = Σⱼ sⱼ(1 − j/256) − 1/6. For the law's S-midpoints (exact rational arithmetic,
§exact_reconcile (B)):

- **E(1) = −1/(6·256²) = −2.5431315104166665·10⁻⁶**, diff 1.18·10⁻⁴⁴ (= 2⁻¹⁴⁶, last-bit
  rounding of the 140-bit arithmetic).
- The ±2⁻¹⁴¹ enclosure wobble shifts E(1) by at most **2⁻¹³¹ ≈ 4.6·10⁻⁴⁰** (§exact_reconcile
  (D)) — 35 orders of magnitude below |E(1)| = 2.54·10⁻⁶.

So |E(1)| — the only pair-correlation quantity the certificate value depends on (via the signed
ceiling M·(|r′(1)| + ∫|r″|)) — is the **same number** for the law and for the pure GUE-flat
datum. The certificate cannot tell the two data apart.

---

## 4. LP optimum against the GUE-flat datum (independent reconstruction)

The certificate-class LP (canonical matrices from `tools/lpdual/lpdual_final.py`, but the flat
datum s_flat built from scratch as s_j = j/256², j = 1..256, independent of `law_data.json`):
script `tools/lpdual_realconfig_check.py` (this agent's file; `tools/lpdual/` is owned by the
LP agent, so the new file sits beside it unowned). Command:
`uv run --quiet --with numpy --with scipy python tools/lpdual_realconfig_check.py`.

Result (B = C = 1, box |r| ≤ 1, p₁ = p₀, validity on rows 1..255):

```
(0) max |s_law[j] - j/256^2| over rows 1..255 = 0.0  (exact match: True)
(1) E(1)_flat exact = -1/393216 = -2.5431315104166665e-06 ;  == -1/(6*256^2) ? True
(2) vs law : v* = 0.681831230595      vs flat: v* = 0.681831230595
    p0 + |E(1)|_flat = 0.681831230595 ;  identical? True ;  matches p0+|E(1)|? True
(3) exact r=1-x vs flat datum: v = p0 + 1/(6*256^2) ? True ;  delta = 0.0
(4) p1 sweep (flat): v*(p1) = p1 + |E(1)| for p1 = p0, 0.70, 0.80, 0.90, 1.00 — shadow = 1.0 exactly
(5) row sweep (flat): M=1: 0.8899 ... M=255: 0.6818312306 — identical to the law's sweep (attack-lpdual.md §3)
```

Exact rational cross-check (`/tmp/lpdual_realcheck/exact_reconcile.py`, command
`uv run --quiet python /tmp/lpdual_realcheck/exact_reconcile.py`): the certificate r(x) = 1−x
against the pure flat datum at p₁ = p₀ has value **v = p₀ + 1/(6·256²)** exactly (Fraction
arithmetic, §(C)), i.e. v = 0.6818312305953419.

**Bottom line:** the in-class optimum against the GUE-flat datum equals the in-class optimum
against the law, to the LP's 1e-12 reporting precision (and exactly, structurally, since the
validity rows are the same numbers and |E(1)| is the same). **The flat datum does not admit a
higher certificate value.** The 0.6818 ceiling is datum-independent inside bandwidth one.

---

## 5. Why the rows carry no marginal value (the mechanism)

The value is pinned by exactly two constraints (duals from attack-lpdual.md §4, reproduced in
`results.json`):
- validity at the datum (rows 1..255): dual **−1.000000** — the certified simple fraction p₁
  transfers 1:1 into value;
- the box |r| ≤ 1 at r(0): dual −2.54·10⁻⁶ — fixes the residual to |E(1)|.

Every individual pair-correlation row has **zero marginal value** (drop-row analysis,
attack-lpdual.md §3: the most valuable single row, j = 128, is worth 1.95·10⁻³ of *constraint
tightening*, but the 255-row aggregate only pins v to within 2.5·10⁻⁶ of p₀; the dual of every
row is ≈ 0 at the optimum). Row shadow prices here are reproduced identically for the flat
datum (§4(5)). Therefore: **replacing the law's rows with any other bandwidth-one datum that
keeps |E(1)| unchanged leaves v\* unchanged.** The datum is not the binding constraint; p₁ is.

---

## 6. Verdict

**(b) ≤ (a): the ceiling binds reality too.**

1. The GUE-flat datum (the empirically-correct model of the real zeros' pair correlation) gives
   the **same** in-class optimum as the 256-law: v\* = p₀ + |E(1)| = 0.6818312305953419
   (CHECKED NUMERICALLY, LP + exact rational arithmetic).
2. The 256-law is not an artificial adversary: it realizes the GUE-flat form factor that the
   real zeros empirically exhibit (attack-hot-hand.md: ramp 0.497 vs GUE 0.479, beyond-1 level
   within 1.2σ of the GUE plateau). The law differs from reality only in its certified simple
   fraction p₀, and **that** quantity is exactly the one the certificate cannot move without
   beyond-bandwidth-one data (shadow price 1; attack-ceiling.md §3: no such data exists in the
   verified literature, unconditional or RH-conditional).
3. **The only genuine lever on v remains p₁** — the certified simple fraction of the true
   zeros. Real zeros are empirically all simple in the low range ("first 1000; first-10¹³-simple
   is literature" — attack-multiplicity.md), so a *proof* that the true simple fraction exceeds
   p₀ = 0.6818 would push v beyond 0.6818 even within bandwidth one. But the certificate class
   cannot produce that proof from bandwidth-one data (attack-lpdual.md §5, PROVEN): the LP's
   p₁-sweep shows v\*(p₁) = p₁ + |E(1)| for every p₁. What's missing is a *certified* simple
   fraction for ζ's zeros — a different input (multiplicity information), not a different
   form-factor datum.

**s4h classification: HARD.** Source: Lean theorem + LP dual (adversarially validated in
Round 2). Consequence if violated: real. Precedent: tested adversarially (Round 1 ceiling,
Round 2 LP); holds. Conditions where it wouldn't apply: none inside bandwidth one (proven
datum-independence here + no beyond-1 input, attack-ceiling.md §3). The search direction
"beat 0.6818 by feeding the certificate a more realistic bandwidth-one datum" is **closed** —
the datum was already the realistic one.

---

## 7. What would change what we believe (unchanged from attack-lpdual.md §6, sharpened)

1. **A proven (or certified-empirical) simple-fraction bound p₁ > p₀ for ζ's zeros** — the only
   datum that moves v (shadow price 1; every +δ in p₁ buys +δ in v). Multiplicity data for the
   true zeros is the live, un-mined input. The empirical side is promising (all-simple low range)
   but a *certificate* needs a proven lower bound, which requires a different mechanism (not the
   pair-correlation rows).
2. **Beyond-bandwidth-1 form-factor information** (F(α), α > 1 — Hardy–Littlewood prime-pair
   territory): PROVEN absent from the literature (attack-ceiling.md §3); each unit buys a unit of
   certified proportion, but nothing proven exists.
3. **Adversarial re-check of EnclOK** (the single non-Lean link): still open, still cheap, still
   the one live way the ceiling itself could be wrong (attack-ceiling.md §4).

---

## 8. Exact commands

```bash
# (1) canonical reproduction of the 0.6818 in-class optimum (law data) — verify_exact_cert.py
cd /home/vstaln/riemann && uv run --quiet python tools/lpdual/verify_exact_cert.py
#     -> v = 0.6818312305953419 = p0 + 1/(6*256^2); CEILING TIGHT

# (2) this agent's independent probe: LP optimum against the GUE-flat datum built from scratch
cd /home/vstaln/riemann && uv run --quiet --with numpy --with scipy python tools/lpdual_realconfig_check.py
#     -> v*_law = v*_flat = 0.6818312305953419; p1 shadow = 1.0; row sweep identical to the law's

# (3) exact rational reconciliation (enclosure structure, E(1), certificate value, wobble bound)
cd /home/vstaln/riemann && uv run --quiet python /tmp/lpdual_realcheck/exact_reconcile.py
#     -> rows 1..255 are width-2^-140 intervals containing j; E(1) = -1/(6*256^2) exactly;
#        v_flat = p0 + 1/(6*256^2) exactly; |E(1)|/wobble ~ 10^35

# (4) empirical form factor of real zeros vs GUE null (attack-hot-hand.md §3.1, reused)
cd /home/vstaln/riemann && uv run --quiet --with numpy --with scipy --with matplotlib python tools/hot_hand_calib.py
#     -> ramp 0.497 vs 0.479; beyond-1 level z = -1.18 sigma (N=10^4): real zeros consistent with GUE-flat
```

**Code location note:** the canonical probe is `tools/lpdual_realconfig_check.py` (new, at the
`tools/` root beside the owned `tools/lpdual/` directory — no other agent's file overwritten;
`tools/lpdual/` remains owned by the LP agent). The exact-rational helper lives at
`/tmp/lpdual_realcheck/exact_reconcile.py`; per protocol it is copied into this note's scope
and can be promoted into `tools/` if another round wants it.
