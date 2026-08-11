# Regenerate the 256-law from its defining LP — closing EnclOK, and the small-N adjudication

**Agent:** EXECUTIONER (regenerate-256law subprogram; LP formulation + numerical solver + adversarial checks)
**Date:** 2026-08-11
**Task (highest-value):** independently regenerate the N = 256 near-CUE law of marked configurations
(the ONE non-Lean link, EnclOK, in the 0.68185 bandwidth-one ceiling) by re-solving its defining LP,
then recompute S(j) at ≥ 45 digits and compare against the 256 enclosures of `LawN256.lean`
(K = 2^140). A match → EnclOK CHECKED NUMERICALLY (independent regeneration); a mismatch → the ceiling's
only non-Lean link REFUTED; infeasibility at N = 256 → document the precise blocker.

**Verdict up front:**
- **EnclOK: STILL OPEN — NOT independently regenerated, NOT refuted.** The exact-CUE spectrum
  f̄(j) = j (j = 1..255) required by the enclosures is NOT achievable by any configuration family I was
  able to reconstruct from the public constraints (infeasible at N = 64..256 for every family tested;
  Chebyshev distances 6–1915). The blocker is precise and documented: **the candidate configuration
  family of the authors' exact-rational LP is private** (cert_N256_blk_b128m.json, sha256 cc3de991…)
  and is *not* recoverable from the mathematical constraints alone — no natural family (jittered
  lattices, antipodal-pairs+specials, lattice+doubles at fractional parts, random marked configs)
  spans the CUE ramp. This is itself a finding (MB2.4-relevant): the exact CUE spectrum is a
  delicate, structured object; the authors' family is a non-trivial construction.
- **FLAG ADJUDICATED (parallel-agent contradiction probe):** the reported small-N values
  (min p₁ = 0.500/0.506/0.652 at N = 8/16/32 from `lp_smallN.py`) were computed with a **buggy
  family generator that emitted INVALID configurations (Σ marks = N+d, not N)**. With corrected
  valid configurations, the pointwise-rows min p₁(N) = 0.705/0.753/0.844/0.915 at N = 8/16/32/64 —
  all **above** Theorem B's 0.6725. **No contradiction with the PROVEN 0.6725 theorem is exhibited
  by the corrected LP.** Under the looser cumulative-only data budget (the certificate's integrated
  D(1), E(1) quantities), min p₁(8) = 0.669–0.687 (family-dependent upper bound) dips below 0.6725 — a genuine nuance for the MB2.4 question
  ("is the class ceiling an N = 256 phenomenon?"), but NOT a refutation of any PROVEN theorem
  (Theorem B/D concern the actual zeros, which satisfy near-CUE only with error O(1/√log T) ≫ τ;
  the abstract N-periodic laws are different objects).

---

## 0. Honesty labels

| Claim | Label |
|---|---|
| LP formulation (below) — variables, constraints, objective, p₀ | **DERIVED** from `attack-ceiling.md` §1 + `Stability.lean`/`NearCUE.lean`/`RowCert.lean`/`CeilingLaw256.lean` (PROVEN Lean structure); p₀ is the recorded value in `LawN256.lean`'s header, **not** independently re-derived |
| The bug: `tools/regen_law/common.py::gen_family_vec` and `lp_smallN.py` produced configs with Σ marks = N+d | **PROVEN** — code inspection + runtime `sum marks` prints (e.g. support config "s_c=8, sum marks=10" at N=8) |
| Small-N min p₁ with VALID configs, pointwise rows (N=8/16/32/64): 0.705/0.753/0.844/0.915 | **CHECKED NUMERICALLY** — scipy `linprog` (HiGHS), double precision, residual < 3e-14 on rows; upper bounds over the random family |
| Small-N min p₁ with valid configs, cumulative-only budget: 0.669–0.687 (N=8, family-dependent), 0.732/0.782/0.835/0.883/0.914 (N=16..256) | **CHECKED NUMERICALLY** — same solver; 2-config supports; E(1) saturated at ±M(N); upper bounds |
| The N = 256 pointwise LP is infeasible for every tested family (Chebyshev dist 6.3–1915) | **CHECKED NUMERICALLY** — six families, `linprog` + Chebyshev-fit LPs |
| Grid-config lower bound p₁ ≥ 3/2 − d₁ = 0.67604683 (exact rows + \|D(1)\| ≤ d₁, integer positions) | **PROVEN-BY-ARGUMENT** (exact identity Σⱼf̄(j) = N(2N − Np₁) for grid configs; verified numerically) — and it FAILS for off-grid configs (Re G(Δ) < 0 for Δ ∈ (0.45, 1)) |
| E(1) = −1/(6N²) exactly for exact-CUE rows (N=256 law: E(1) = −1/393216) | **PROVEN-BY-ARGUMENT** (closed form Σⱼ(j/N)(1−j/N)); CHECKED NUMERICALLY; matches `close-inclass-gap.md` |
| "The flagged small-N values contradict Theorem B" | **REFUTED** — artifact of invalid configs; no valid law with p₁ < 0.6725 found at N ≥ 8 under pointwise rows |
| "Theorem B/D are contradicted by abstract near-CUE laws" | **REFUTED-BY-CATEGORY** — Theorem B/D are PROVEN for the actual zero configuration (exact prime-side two-moment); abstract N-periodic laws with O(1/N²) two-moment deviations are not the actual zeros (which carry O(1/√log T) error) |

---

## 1. The LP, reconstructed from the certificate-validity constraint

**Objects (from `Defs.lean`, `NumericCert.lean`, `NearCUE.lean`, `RowCert.lean`, `CeilingLaw256.lean`; all PROVEN Lean):**
- A 256-periodic marked configuration: finitely many positions x_{c,i} ∈ [0,256), marks m_{c,i} ∈ {1,2},
  Σ_i m_{c,i} = 256; simple count s_c = #{i : m_{c,i} = 1}, simple-point fraction p₁,c = s_c/256.
- Form factor at frequency j: f_c(j) = |Σ_i m_{c,i} e^{2πi j x_{c,i}/256}|²; the law's S(j) = Σ_c w_c f_c(j)/256.
- Grid masses s_j = S(j)/256 at x_j = j/256; cumulative C(x) = Σ_{j/256 ≤ x} s_j; discrepancy
  D(x) = C(x) − x²/2 against the GUE datum; integrated discrepancy E(x) = ∫₀ˣ D.
- A certificate (c₀, r), r ∈ C¹[0,1], value v = c₀ + ∫₀¹ r(x)x dx, is **valid against a configuration**
  iff c₀ + Σ_{j=1}^{256} s_j r(j/256) ≤ p₁,c (`Ceiling.lean`; the `hvalid` hypothesis of `ceiling_law256`).
- `ceiling_stability` (Stability.lean, PROVEN): for any such certificate,
  v ≤ p₁ + |r(1)|·|D(1)| + |r′(1)|·|E(1)| + (sup|E|)·∫₀¹|r″|.
- `NearCUE.lean` (PROVEN): if |256·S(j) − j| ≤ τ = 3·10⁻⁴⁰ for 0 < j < 256 then
  |E(x)| ≤ M := 1/(6·256²) + τ/(2·256) on [0,1].

**The primal LP (reconstructed; the "optimal law of an exact-rational linear programme over
256-periodic marked configurations"):**
```
minimize   p₁ = Σ_c w_c s_c / 256
subject to |Σ_c w_c f_c(j) − j| ≤ τ,   j = 1, …, 255          (near-CUE rows, τ = 3·10⁻⁴⁰)
           |D(1)| ≤ d₁,  D(1) = Σ_j S(j)/256 − 1/2,  d₁ = 82395317/10⁸
           Σ_c w_c = 1,  w_c ≥ 0   (over a finite family of 256-periodic marked configurations)
```
Optimum (recorded in `LawN256.lean`): **p₀ = 10909258999421303588095230195816054408197/16000000000000000000000000000000000000000
= 0.6818286874638314742559518872385034005123125** (CHECKED NUMERICALLY at 60 digits in `validation-enclok.md`).

Direction of the objective — the ceiling mechanism (attack-ceiling.md §1) requires the law to be the
**adversarial worst case** (fewest simple points consistent with the data): "no certificate can certify
more than 0.6818 because there exists a configuration consistent with every bandwidth-one input that has
only 0.6818 simple zeros." Hence **min p₁ = p₀**. (The theorem itself only needs the law to EXIST with
p₁ = p₀ and the near-CUE data; the min/max direction of the generating LP is the authors' construction
choice and does not affect `ceiling_law256`.)

**Why the D(1) row binds S(256):** with exact-CUE rows, D(1) = (Σ_{j<256} j/256 + S(256))/256 − 1/2
= S(256)/256 − 1/512, so |D(1)| ≤ d₁ forces S(256) ≤ 256(d₁ + 1/512) = 211.43201152; the recorded
S(256) ≈ 211.4320091424858 sits 2.4·10⁻⁶ below (slack 9.3·10⁻⁹ in D(1) units). Also E(1) =
−1/(6·256²) = −1/393216 exactly (closed form), saturating the near-CUE bound |E(1)| ≤ 1/(6·256²) + τ/512.

---

## 2. Solver method (all code saved under `tools/regen_law/`)

Environment: `uv run --with scipy --with mpmath python3 <script>` (HiGHS via `scipy.optimize.linprog`;
pip disabled; double precision; LP matrices built directly from the definitions, **not** from the
enclosures — the enclosures were only consulted for the final comparison, per the independence protocol).

Scripts (each cited by the command that ran it):
| Script | Purpose |
|---|---|
| `common.py`, `common2.py` | family generators (common.py has the BUG; common2.py is correct) |
| `lp_smallN.py`, `lp_scale.py`, `lp_scale3.py`, `lp_general.py` | small-N/scale-up pointwise LPs |
| `lp_pairs256.py`, `lp_pairs2.py`, `lp_doubles.py`, `lp_doubles_mixed.py`, `lp_defects_big.py` | N=256 pointwise LP on structured families |
| `search_defects.py`, `ramp_search.py`, `kernel_probe.py`, `gkernel.py` | structure probes (defect spectra, ramp fit, certificate kernel R(Δ), G(Δ)) |
| `cert_allconfigs.py`, `cert_allconfigs2.py` | certificate LP valid against all (sampled) configs |
| `adjudicate.py`, `adjudicate2.py`, `adjudicate3.py`, `adjudicate4.py`, `colgen8.py` | bug fix + small-N adjudication + column generation |
| `final_numbers.py` | the report's final table |

Representative exact commands (run in `/home/vstaln/riemann/tools/regen_law/`):
```
timeout 600  uv run --with scipy python3 lp_smallN.py      # (buggy family — superseded)
timeout 2400 uv run --with scipy python3 adjudicate2.py    # valid-config adjudication (pointwise + cumulative)
timeout 1800 uv run --with scipy python3 colgen8.py        # N=8 pool (19535 configs) + column generation
timeout 2400 uv run --with scipy python3 final_numbers.py  # final table
timeout 1800 uv run --with scipy python3 lp_doubles_mixed.py  # N=256 pointwise, mixed-frac doubles family
```

---

## 3. Small-N validation and the flag adjudication (mandated by the parallel agent)

### 3.1 The bug (invalid configurations in the earlier small-N numbers)
`tools/regen_law/common.py::gen_family_vec` built configs by starting from N positions each with mark 1
and **upgrading d of them to mark 2** — giving Σ marks = N − d + 2d = **N + d ≠ N**. These are NOT valid
256-periodic marked configurations (the form factor definition requires Σ m_i = 256). Runtime prints
confirmed it: e.g. a support config reported "s_c = 8, sum marks = 10" at N = 8. **The earlier reported
min p₁ = 0.500/0.506/0.652 at N = 8/16/32 (in `idea-generator-math-branches.md` probe 2, quoting this
agent's `lp_smallN.py`) were computed with these invalid configs and are void.**

### 3.2 Corrected results (valid configs, Σ marks = N; `common2.py`)
`uv run --with scipy python3 final_numbers.py` (and adjudicate2/3):

| N | min p₁ (POINTWISE rows, valid family; upper bound) | min p₁ (CUMULATIVE-only budget; upper bound) |
|---|---|---|
| 8 | 0.70527517 (8 support) | **0.669–0.687** (2 support; family-dependent — see note) |
| 16 | 0.75295863 (16 support) | 0.73212229 (2 support) |
| 32 | 0.84375629 (32 support) | 0.78158772 (2 support) |
| 64 | 0.91490350 (64 support) | 0.83494799 (2 support) |
| 128 | infeasible (family too poor) | 0.88335207 (2 support) |
| 256 | infeasible (family too poor) | 0.91410346 (2 support) |

- **Pointwise rows** = the Lean near-CUE rows |Σ w f_c(j) − j| ≤ 3e-40, j = 1..N−1, plus |D(1)| ≤ 0.82395317
  (F(N)-bound N²(d₁+1/2) − N(N−1)/2). All values **≥ 0.6725** — no valid small-N near-CUE law below
  Theorem B's constant was found. E(1) saturates at −1/(6N²) exactly in every feasible pointwise run
  (consistent with exact-CUE rows forcing E(1) = −1/(6N²)).
- **Cumulative-only budget** = the certificate's *integrated* data: |D(1)| ≤ d₁ and |E(1)| ≤ 1/(6N²) + τ/(2N),
  with NO pointwise rows (these are the quantities that actually enter the stability ceiling). Under this
  looser budget, N=8 admits a valid 2-config mixture with p₁ below Theorem B's 0.6725: stability check
  across family sizes/seeds gives 0.687/0.673/0.674/0.669 for nc = 4k/8k/12k/20k
  (`check_cum8.py`). These are upper bounds (family-dependent; the true infimum over all configs could be
  lower). This is the nuance for the MB2.4 question — see §3.4.

### 3.3 Adjudication: is Theorem B (0.6725, PROVEN) contradicted?
**No.** The apparent contradiction is resolved in two independent ways:
1. **The stated numbers were artifacts.** With valid configurations and the correct (pointwise) rows, every
   computed small-N min p₁ is ≥ 0.705 > 0.6725. Nothing below Theorem B's constant survives the correction.
2. **Category error.** Even the cumulative-only N=8 value (0.669–0.687) does not contradict Theorem B/D, because:
   (a) Theorem B/D are proven for the **actual zeta zero configuration**, via the exact prime-side
   two-moment ∫(λ−|α|)F(α,T)dα = λ + λ³/3 (BGSTB24 Thm 1; unconditional) plus rank–trace. The actual zeros
   satisfy the near-CUE pair correlation only with error O(1/√log T) — they do **not** satisfy the exact
   rows (τ = 3e-40) nor the exact cumulative bounds at any fixed N;
   (b) the abstract N-periodic laws are synthetic extremal objects; their two-moment deviates from the CUE
   value by O(1/N²) (e.g. E(1) = ±1/(6N²), which is 2.6·10⁻³ at N=8 — comparable to the 0.6725 − 0.669 gap,
   so the "adversarial validity" of the N=8 cumulative law against the exact-two-moment certificate is at
   best borderline and is NOT established);
   (c) the class-level ceiling (0.6818) is itself conditional on the existence of the N=256 law (Remark 1.1);
   whether the certificate class has *lower* worst-case configurations at small N is precisely the OPEN
   MB2.4 question — a research question, not a refutation of any PROVEN theorem.

### 3.4 What the small-N data says about MB2.4 ("is the ceiling an N=256 phenomenon?")
- Under the **pointwise rows** (what the Lean near-CUE theorem assumes), my valid-family upper bounds are
  0.705/0.753/0.844/0.915 for N = 8/16/32/64 — **increasing**, and all above 0.6725. The recorded p₀(256) =
  0.6818 is *below* these upper bounds, which (since the law exists) implies my random families overestimate
  the true min p₁ at every N (they miss the low-p₁ configs the authors' family contains). The true min p₁(N)
  is therefore ≤ 0.6818 at N=256 and my data is consistent with a true min p₁(N) ≈ 0.68 (flat) with the
  families degrading at large N. **I cannot conclude the ceiling is an N=256 phenomenon from this data** —
  that requires the authors' family or a lower bound valid for off-grid configs.
- Grid-config lower bound p₁ ≥ 3/2 − d₁ = 0.67604683 (exact rows + |D(1)| ≤ d₁): PROVEN-BY-ARGUMENT via the
  exact identity Σ_{j=1}^{N} f̄(j) = N(2N − Np₁) for integer-position configs (verified numerically). It
  applies only to grid configs: off-grid configs break it (Re G(Δ) < 0 for Δ ∈ (0.45, 1), so off-grid pairs
  can lower Σ_j f_c(j) below N·Σ m²). No general-N lower bound for off-grid configs is known to me.

---

## 4. The N = 256 regeneration attempt — and the precise blocker

**Attempted families (all N = 256, pointwise rows, `uv run --with scipy`):**
1. Random jittered lattices + marks (`lp_smallN.py`, `lp_scale3.py`): infeasible (target spectrum not in
   convex hull; Chebyshev distance to the ramp ≈ 6.31 at N=256).
2. Antipodal pairs (128-lattice) + special doubles at one fractional coset: infeasible — **structural**:
   a single coset forces f(1) = f(255) = 4|Σ_special e^{2πix/256}|² (conjugation), while the ramp needs
   f̄(1) = 1 ≪ f̄(255) = 255.
3. Antipodal pairs + special doubles at mixed fractional parts: infeasible (Chebyshev ≈ 12.7–24.6).
4. Lattice + d doubles at half-integer positions: infeasible — the factor (5−4cos(πj/256)) ∈ [1,9] bounds
   f̄(255)/f̄(1) ≤ 9 < 255 while the subset part keeps |B(1)|² = |B(255)|².
5. Lattice + d doubles at mixed fractional parts (u ∈ {0,1/2,1/4,3/4,1/3,2/3,…}): infeasible (Chebyshev ≈ 12.7).
6. Lattice + moved simples + doubles, mixed fractional parts (most general defect family): infeasible
   (Chebyshev ≈ 14.4).
7. `cert_allconfigs*.py`: certificate LP valid against all sampled configs without budget constraints is
   degenerate (c₀ blows up via r ≈ −1); with budgets + box the sampled random configs don't bind (the
   binding configs are near-CUE ones, which are rare in random sampling).
8. Column generation at N=8 (19535-config pool): min p₁ = 0.6966; no violator found in 4·10⁴ random configs
   (reduced-cost extraction uncertain, but the pool result is the reliable number).

**The blocker (precise):** the exact-CUE spectrum f̄(j) = j for j = 1..255 requires configurations whose
spectra span the linear ramp in the convex hull, with the *weighted average* hitting j to within 2⁻¹³².
Every natural family I constructed produces spectra of specific shapes (sin²-combs, (5−4cos)|B(j)|²,
subset spectra with |B(1)|² = |B(255)|² symmetries, j²-growth near j=0) whose convex hull does not contain
the ramp. The authors' family — the finite set of configurations in their exact-rational LP — is recorded
only in `cert_N256_blk_b128m.json` (sha256 cc3de991…, "available from the authors", not public; absent from
the Lean repo, workspace, papers, and public search per `validation-enclok.md`). **The constraint
"the family is the authors' finite set" is HARD** (sourced to their distribution decision; three prior
agent runs + this run could not recover it). The solver choice (HiGHS/scipy) is NOT the blocker — the LP is
well-formed and solved instantly when feasible at N ≤ 64; the infeasibility is intrinsic to the candidate
families. The exact-rational refinement step was never reached because the float relaxation is infeasible.

**Consistency checks that did succeed (independent of the family):**
- E(1) = −1/(6·256²) = −2.5431315104166665·10⁻⁶ exactly for exact-CUE rows (closed form); the recorded
  D(1) = 0.8239531607128352 forces S(256) = 211.4320091424858, matching the j=256 enclosure
  [294693210168748317632180492755635579620342098, +1] (CHECKED NUMERICALLY).
- p₀ decimal = 0.6818286874638314742559518872385034005123125 (re-verified at 60 digits).
- The near-CUE enclosure data is internally consistent (validation-enclok.md §3): checkRows == true,
  edgeNonneg == true, |D(1)| ≤ d₁ with slack 9.3·10⁻⁹, all re-verified by the exact big-int path.

---

## 5. Verdict

**EnclOK (the law's S(j) lies in the 256 integer enclosures of LawN256.lean): STILL OPEN.**
- **NOT independently regenerated:** the defining LP's configuration family is private and not recoverable
  from the public constraints; every reconstructed family is infeasible at N = 256 (the exact-CUE ramp is a
  structured, delicate object, not in the convex hull of any natural family I built).
- **NOT refuted:** nothing in this run contradicts the enclosures or p₀. The recorded data remains
  internally consistent (validator re-checked exactly), the E(1) saturation and the S(256)/D(1) link are
  reproduced, and the failure is at the family-reconstruction level, not a mismatch of any regenerated law
  (none exists at N=256).
- **Status of the 0.68185 ceiling:** PROVEN (Lean, standard axioms) modulo the single displayed hypothesis
  EnclOK — unchanged. The blocker to closing it is documented above; the cheapest decisive close remains
  obtaining the authors' certificate (validation-enclok.md §6).

**S(j) comparison table (as requested):** no regenerated N=256 law exists, so no full S(j) table can be
produced. What CAN be reported (sample rows, all CHECKED NUMERICALLY):
| quantity | regenerated (independent) | recorded (LawN256 / validation-enclok) |
|---|---|---|
| E(1) (from exact-CUE rows) | −1/(6·256²) = −2.5431315104166665e-6 (closed form) | −2.543131510407415e-6 (midpoint data; diff 9.3e-18) |
| S(256) (from D(1) = 0.8239531607128352 + exact rows) | 211.4320091424858 | enclosure [211.43200914248579…, +2^-140] ✓ |
| p₀ | 0.6818286874638314742559518872385034005123125 (60 digits) | same ✓ |
| rows | not regenerated (blocker) | |256·S(j) − j| ≤ 2⁻¹³² over the box (validator) |

**Adjudication of the parallel flag:** the small-N values that seemed to contradict Theorem B (0.6725)
were artifacts of a buggy family generator (invalid configs, Σ marks ≠ N); with valid configs every
pointwise small-N min p₁ is ≥ 0.705 > 0.6725, and no valid near-CUE law below 0.6725 was found. The
cumulative-only N=8 value (0.669–0.687) is a genuine MB2.4 nuance (abstract law vs actual zeros; O(1/N²)
two-moment deviation), not a refutation of anything PROVEN. **The ceiling stands.**

---

## 6. What would close EnclOK (in priority order)

1. Obtain `cert_N256_blk_b128m.json` (sha256 cc3de991…): recompute the hash, recompute S(j) at ≥ 45 digits
   with directed rounding (mpmath@100 has 93 bits of headroom over the 2⁻¹⁴⁰ width), verify the 256
   enclosures, re-run `checkRows`. Estimated effort: minutes once in hand (validation-enclok.md §6).
2. Reconstruct the authors' family from the LP-dual structure: the N=256 law's configs appear to have
   ~244 integer marks (balanced parity) + ~12 half-integer marks with f_c(256) = (2n₀−256)² ∈ {53824, 54756}
   mixing to 54126.59 — a precise signature that could seed a targeted family search
   (MB2.4/MB5.3-relevant; not completed here).
3. Prove a lower bound on min p₁ valid for off-grid configs (the grid bound 3/2 − d₁ fails off-grid;
   Re G(Δ) < 0 on (0.45, 1) opens the door — this is a genuine open question, not a known result).

**Honesty labels used:** PROVEN — Lean-verified or exact-arithmetic re-derived; CHECKED NUMERICALLY — this
run (scipy/HiGHS, double precision; exact big-int where noted); PROVEN-BY-ARGUMENT — exact identity with
numeric confirmation, not formalized; DERIVED — reconstruction from proven structure; REFUTED — with the
documented reason; OPEN — neither confirmed nor refuted.
