# Validation of EnclOK — the one non-Lean numeric hypothesis in the 0.68185 bandwidth-one ceiling

**Agent:** VALIDATOR (adversarial) — Riemann program, Round 1
**Date:** 2026-08-11
**Tooling:** `tools/verify_enclok.py` (fresh implementation; two independent code paths: exact Python big-integer arithmetic mirroring Lean's `decide` over ℤ, and mpmath at 100 digits on the real-number side; cross-checked).
**Sources read:** `research/lean-zeta-23/Zeta23/PairCeiling/{Defs,Ceiling,Stability,Grid,NearCUE,Bridge,NumericCert,RowCert,LawN256,CeilingLaw256,Signed}.lean`, `README.md`, `AUDIT.md`, `comparator/PrintAxioms/PairCeiling.lean`, `papers/claude-riemann-paper.txt` (Remark 1.1), prior notes `research/notes/attack-ceiling.md`, prior session transcripts (two VALIDATOR runs died mid-task; their partial findings are folded in below where they survive scrutiny).

---

## Verdict (top line)

- **EnclOK as a statement about the TRUE N = 256 law's form factor: INCONCLUSIVE — NOT independently verifiable from available sources; NOT REFUTED.** The exact-rational law data (weights, positions, marks) exists only in the authors' certificate file `cert_N256_blk_b128m.json` (sha256 `cc3de9917db4d14d844630a4e97dda8387fd6e257e52b6967f430b8914584eb8`), which is not public. (Label: INCONCLUSIVE — the claim is neither confirmed nor refuted here.)
- **Everything downstream of EnclOK in the 0.68185 ceiling chain: PROVEN (Lean, standard axioms {propext, Classical.choice, Quot.sound})** and independently re-checked in this run (Label: CHECKED NUMERICALLY — this run).
- **Important correction to the record:** the previously recorded "CHECKED NUMERICALLY — 70-digit interval arithmetic from an exact-rational certificate" for EnclOK (in `attack-ceiling.md` and this task brief) is *inherited from the authors' README*, **not** an independent Riemann-program check. No Riemann-program agent had actually re-run the enclosure computation before this task. (Label: CONJECTURED-as-verified previously; now re-classified.)

---

## 1. The exact statement of EnclOK

**Formal definition** (`NumericCert.lean:71-75`):

```
EnclOK (K : ℕ) (S : ℕ → ℝ) : ℕ → List (ℤ × ℤ) → Prop
| _, [] => True
| j, e :: l => ((e.1 : ℝ) ≤ K * S (j + 1) ∧ (K : ℝ) * S (j + 1) ≤ e.2) ∧ EnclOK K S (j + 1) l
```

**Instance** (`LawN256.lean`): the theorem `ceiling_law256`, `ceiling_law256_signed`, `ceiling_law256_decimal`, `lawN256_rows`, `D1_nonneg_of_edgeNonneg` all carry the single displayed hypothesis

```
hS : EnclOK LawN256.K S 0 LawN256.encl
```

i.e., for K := 1393796574908163946345982392040522594123776 = 2^140 and the 256 integer pairs (lo_j, hi_j) recorded in `LawN256.encl`,

```
lo_j ≤ 2^140 · S(j) ≤ hi_j          for every j = 1, …, 256,
```

where S(j) is the **grid form factor of the N = 256 near-CUE law of marked configurations** (`LawN256.lean` header; paper Remark 1.1):

```
S(j) = (1/256) · Σ_c w_c · | Σ_i m_{c,i} · e^{2πi j x_{c,i}/256} |²,
```

with exact-rational weights w_c ≥ 0 summing to 1, rational positions x_{c,i} ∈ [0,256), marks m_{c,i} ∈ {1,2} and Σ_i m_{c,i} = 256 per configuration. (The weight/position/mark data is the certificate, not in the repo.)

**Equivalent form (derived from the data):** for j = 1..255 the recorded boxes are width-1: hi_j = lo_j + 1, with lo_j ∈ {j·2^132 − 1, j·2^132}, so

```
| S(j) − j/256 | ≤ 2^−140          for every j = 1, …, 255        (1)
```

and for j = 256: K·S(256) ∈ [294693210168748317632180492755635579620342098, …099], i.e. S(256) ≈ 211.4320091424858. (Label: PROVEN — this is elementary arithmetic on the recorded data, verified exactly in this run; 124 of the 255 rows sit strictly below j/256 (lo = j·2^132−1), 131 at/above (lo = j·2^132).)

---

## 2. Derivation: what the ceiling is, and where EnclOK enters

The whole chain is **PROVEN in Lean** (standard axioms only, `comparator/PrintAxioms/PairCeiling.lean`); I re-derive the shape here and re-verify every numeric constant independently.

**Step 1 — the stability identity (configuration-free, `Stability.lean: ceiling_stability`).** For grid weights s_j at j/N, N ≥ 1, and a certificate r ∈ C¹[0,1] with r′ = g differentiable off a countable set with integrable derivative h, two integrations by parts (cellwise FTC + Abel summation, then FTC off a countable set) give

```
| Σ_{j=1}^N s_j r(j/N) − ∫₀¹ r(x) x dx | ≤ |r(1)|·|D(1)| + |g(1)|·|E(1)| + M·∫₀¹|h|,   M = sup_{[0,1]}|E|,
```

where C(x) = Σ_{j/N ≤ x} s_j, D = C − x²/2, E = ∫₀ˣ D. (Label: PROVEN (Lean); re-derived here.)

**Step 2 — near-CUE laws (`NearCUE.lean: ceiling_nearCUE, abs_Efun_le_of_nearCUE`).** If |N·S(j) − j| ≤ τ for 0 < j < N (the closed-band row j = N free) then, on each cell [m/N,(m+1)/N] with Nx = m + θ,

```
N³·E(x) = (−m + 3mθ(1−θ) − θ³)/6 + (perturbation of size ≤ m(m+1)τ/2),   −(m+1) ≤ −m + 3mθ(1−θ) − θ³ ≤ 0,
```

so |E(x)| ≤ 1/(6N²) + τ/(2N) on [0,1]. Consequently, for a near-CUE law with |D(1)| ≤ d₁,

```
v := c₀ + ∫₀¹ r(x)x dx ≤ p + d₁·|r(1)| + (1/(6N²) + τ/(2N))·(|r′(1)| + ∫₀¹|r″|).      (2)
```

(Label: PROVEN (Lean).)

**Step 3 — the integer row certificate (`RowCert.lean: cert_of_checkRows`).** The checker `checkRows` (pure integer arithmetic: `|N·e.1 − (j+1)·K|·td ≤ tn·K` per row and an aggregate `|2·Σlo − K·N|·dd ≤ dn·2KN`) is sound: if `checkRows d = true` and `EnclOK d.K S 0 d.encl` then NearCUE S N (tn/td) ∧ |D(1)| ≤ dn/dd. (Label: PROVEN (Lean, `LawN256_check : checkRows LawN256 = true := by decide +kernel`); re-run exactly in this run.)

**Step 4 — the law instance (`CeilingLaw256.lean`).** N = 256, τ = 3·10⁻⁴⁰, d₁ = 82395317/10⁸ = 0.82395317:

```
v ≤ p + 0.82395317·|r(1)| + 2.5431316·10⁻⁶·(|r′(1)| + ∫₀¹|r″|),     (3)
```

because 1/(6·256²) + τ/512 = 2.5431315104…×10⁻⁶ < 2.5431316×10⁻⁶ (slack 8.96×10⁻¹⁴; verified exactly). (Label: PROVEN (Lean); constants CHECKED NUMERICALLY here.)

**Step 5 — signed form (`Signed.lean`).** The actual certificates have r(1) ≥ 0 and the law has D(1) ≥ 0 (kernel-checked `LawN256_edge : edgeNonneg LawN256 = true`; D(1) > 0 from the enclosure sums, see §3), so the edge term −r(1)·D(1) ≤ 0 is dropped:

```
v ≤ p + 2.5431316·10⁻⁶·(|r′(1)| + ∫₀¹|r″|).                        (4)
```

**Step 6 — the ceiling number.** p = p₀ = 10909258999421303588095230195816054408197/16000000000000000000000000000000000000000 = 0.6818286874638314742559518872385034005123125… (the law's exact simple-point fraction; decimal verified at 60 digits here), and the certificates used in Theorem B have r(1) = 0, so

```
v ≤ 0.6818287 + 2.5431316·10⁻⁶·(|r′(1)| + V(r′)).                  (5)
```

This is the 0.68185 ceiling (paper Remark 1.1). (Label: PROVEN (Lean) modulo EnclOK; p₀ decimal CHECKED NUMERICALLY here.)

**Where EnclOK enters:** the ONLY unproved premise is that the true law's S(j) lies in the 256 integer enclosures (Step 3's hypothesis). Steps 1–2 are configuration-free; Step 3's checker and Step 4–6's constants are all kernel-verified in Lean once the enclosures are granted.

---

## 3. Independent numeric rerun (CHECKED NUMERICALLY — this run, tools/verify_enclok.py)

Two independent code paths, written fresh from the Lean statements (no prior-agent code):

| Check | Result | Value |
|---|---|---|
| K = 2^140 | CHECKED NUMERICALLY | True |
| τ = 3·10⁻⁴⁰, d₁ = 82395317/10⁸ | CHECKED NUMERICALLY | True |
| 256 enclosures, width 1 (hi = lo+1) | CHECKED NUMERICALLY | True |
| \|K·S(j) − j·2^132\| ≤ 1 for j = 1..255 | CHECKED NUMERICALLY | True (124 below / 131 at-or-above j/256) |
| near-CUE rows: max \|256·S(j) − j\| over box = 2⁻¹³² = 1.83671…×10⁻⁴⁰ ≤ τ = 3×10⁻⁴⁰ | CHECKED NUMERICALLY | True, margin 1.633355 |
| `checkRows LawN256 == true` (full integer re-run) | CHECKED NUMERICALLY | True |
| `edgeNonneg LawN256 == true` | CHECKED NUMERICALLY | True |
| D(1) = T/256 − 1/2 ∈ [0.823953160712835167297365…, +2⁻¹⁴⁰] | CHECKED NUMERICALLY | \|D(1)\| ≤ 0.82395317 (slack 9.287×10⁻⁹); D(1) > 0 |
| p₀ decimal | CHECKED NUMERICALLY | 0.6818286874638314742559518872385034005123125 |
| e₁ = 1/(6·256²) + τ/512 ≤ 2.5431316e-6 | CHECKED NUMERICALLY | True (slack 8.958×10⁻¹⁴) |
| mpmath@100 cross-check (near-CUE rows, D(1), p₀, e₁) | CHECKED NUMERICALLY | agrees with the exact path |

Notes:
- The exact big-int path mirrors Lean's `decide` (same integer inequalities), so agreement with `LawN256_check = true` is a check that the recorded data is self-consistent, not a re-derivation of the law.
- The mpmath path uses floating-point semantics (different rounding than exact integers) and agrees at 100 digits — good triangulation that no transcription error crept into my reading of the data.
- Cross-check: D(1) ≈ 0.8239531607 nearly saturates the bound 0.82395317; with the near-CUE rows ≈ exact (S(j) ≈ j/256 for j ≤ 255), this forces S(256) = 256(D(1)+1/2) − Σ_{j<256}S(j) ≈ 338.932 − 127.5 = 211.432, matching the recorded S(256) ≈ 211.4320091424858. The data is internally coherent. (Label: CHECKED NUMERICALLY.)

---

## 4. Robustness probes (adversarial)

1. **Uniform ±1 flip on all 256 enclosures.** `checkRows` becomes False (rows whose endpoint deviation reaches 2 units give \|256·2\| = 512 > threshold tn·K/td = 418.138972472). The D(1)-aggregate checks survive the flip (slack 9.3×10⁻⁹ in D(1)-units ≫ 2⁻¹⁴⁰). Conclusion: the certificate tolerates enclosure errors only while \|S(j) − j/256\| ≤ 2⁻¹⁴⁰ (≤ 1 unit); a 2-unit error is rejected. **There is no slack against 2-unit enclosure errors.** (Label: CHECKED NUMERICALLY.)
2. **Largest tolerable single-endpoint deviation.** 256 (the threshold is 418.14, margin 1.633). Same conclusion as 1.
3. **Margin against τ.** The enclosures guarantee \|256·S(j) − j\| ≤ 2⁻¹³² ≈ 1.84×10⁻⁴⁰, strictly inside τ = 3×10⁻⁴⁰ (factor 1.633). So even if the true S(j) sat outside the box by up to ~0.63×2⁻¹³², the near-CUE hypothesis (and hence the whole ceiling) would survive; but EnclOK itself would be false.
4. **Precision headroom of the authors' claimed 70-digit computation.** 70 decimal digits ≈ 2⁻²³²·⁵; the enclosure width is 2⁻¹⁴⁰; headroom ≈ 93 bits. **Rounding at 70 digits cannot flip an enclosure if the formula and data were correct.** The residual risk is an implementation bug or wrong certificate data, not precision. (Label: argued — reliability assessment.)
5. **Sensitivity of the final ceiling number.** The signed bound (4) with r(1) = 0 uses only p₀ and e₁; the D(1) bound enters only the unsigned form (3). So the displayed 0.68185 constant is insensitive to the individual S(j) values — it needs only the near-CUE rows and p₀. The D(1) ≥ 0 sign needed for the signed form holds with slack ≈ 0.824. (Label: argued / CHECKED NUMERICALLY.)

Net: the enclosure→ceiling pipeline is tight (no slack against 2-unit enclosure errors) but every downstream constant survives these perturbations; the ceiling's displayed numbers are robust. The load-bearing, un-verified-by-us fact remains exactly one: **the true law's S(j) equals j/256 to within 2⁻¹⁴⁰ at all 255 open-band rows** (razor-thin: ~42 significant digits).

---

## 5. The one unverifiable link — and why it is genuinely unverifiable here

To verify EnclOK from scratch one must compute S(j) = (1/256)Σ_c w_c |Σ_i m_{c,i} e^{2πi j x_{c,i}/256}|² for j = 1..256 from the law's exact rational data. That data lives only in `cert_N256_blk_b128m.json` (sha256 cc3de991…, "available from the authors"). Exhaustive search (this run and the two prior VALIDATOR runs):

- **Lean repo** `github.com/anthropics/zeta-23-lean`: absent from all branches (main, rc2, xiprime-pairceiling), the full git history (342 paths ever), tags, and releases; the .gitignore does not mention it. (Label: CHECKED — git clone + history inspection.)
- **Local workspace**: not under /home/vstaln/riemann (papers, transcripts, tools, notes, tmp). (Label: CHECKED.)
- **Public web**: exact-filename and hash searches on Google, Bing, DuckDuckGo, GitHub code search, Zenodo, arXiv: no hits. (Label: CHECKED.)
- **Paper/transcripts**: the law is described in prose only (Remark 1.1); no weight/position/mark data. (Label: CHECKED.)

**Constraint-hardness classification (s4h):** the "certificate is not available" constraint is **REAL (hard)** — sourced to the authors' distribution decision, consequence: any from-scratch recomputation of S(j) is impossible with available inputs, precedent: none of three independent agent runs found it. The constraint is not a limit on the method (the check itself is trivial once the data exists) but on the *inputs*.

**Justification assessment (s4h-epistemology):** the ceiling theorem is foundationalist with a reliabilist floor (Lean kernel + `decide`); its only external premise, EnclOK, is currently justified **reliabilistically** (trust in the authors' recorded 70-digit interval-arithmetic check from an exact-rational certificate) and **coherently** (the enclosure data is consistent with every downstream constraint, including the nearly-saturated D(1) bound and the forced S(256)). No independent foundationalist verification is possible without the certificate. Weakest link: the mapping certificate-data → enclosures.

**Evidence FOR EnclOK:** (a) authors' recorded 70-digit check with documented sha256; (b) full internal consistency of the enclosure data with the near-CUE rows, the (nearly saturated) \|D(1)\| bound, D(1) ≥ 0, and S(256); (c) the razor-thin \|S(j) − j/256\| ≤ 2⁻¹⁴⁰ pattern is exactly what a tight near-CUE LP optimum looks like (a certificate deliberately tuned to sit on the CUE datum). **Evidence AGAINST:** none found.

---

## 6. Bottom line and recommendation

- **Verdict:** EnclOK: **INCONCLUSIVE (not independently verifiable here), NOT REFUTED.** Downstream chain: **PROVEN (Lean)** and **CHECKED NUMERICALLY (this run)**. The 0.68185 ceiling's non-Lean dependency is **not closed by this run** — it cannot be closed without the authors' certificate.
- **What would close it (cheap, decisive):** obtain `cert_N256_blk_b128m.json` (hash cc3de991…), then (i) recompute the sha256 (should match), (ii) recompute S(j) = (1/256)Σ_c w_c |Σ_i m_{c,i} e^{2πi j x_{c,i}/256}|² at ≥ 45 significant digits with directed-rounding interval arithmetic (mpmath at 100 digits is more than enough given 93 bits of headroom), (iii) verify lo_j ≤ 2¹⁴⁰·S(j) ≤ hi_j for all 256 j, and (iv) re-run `checkRows`. Estimated effort: minutes once the file is in hand. If it fails, the ceiling collapses (that is the one live way it could be wrong). Until then, the honest status of the 0.68185 ceiling stands as: **PROVEN (Lean) modulo a numerically-consistent, author-checked, not-publicly-reproducible enclosure claim** — and every downstream number is independently confirmed.
- **Correction for the round log:** the "EnclOK CHECKED NUMERICALLY by the prior agent" record was inherited from the authors' README, not independently performed; this run is the first fresh attempt and reaches INCONCLUSIVE with a precise, closed, low-cost route to completion.

---

### Honesty labels used
PROVEN — Lean-verified with standard axioms, or exact arithmetic re-derived here; CHECKED NUMERICALLY — this run (exact big-int and/or mpmath@100); INCONCLUSIVE — claim neither confirmed nor refuted with available inputs; CONJECTURED — asserted without verification; ABANDONED — not used here.
