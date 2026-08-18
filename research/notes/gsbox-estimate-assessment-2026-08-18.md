# GS/BGSTB box-strength quantification + feasibility assessment (2026-08-18)

**Agent:** research (deliverable-first). **Task:** box-strength quantification + feasibility of the
"Goldston–Suriajaya double-sum/box estimate, supplied by Guth–Maynard zero-density" lever (campaign
lever-miner #2). **Scope:** literature reconstruction + tradeoff arithmetic ONLY — no proof attempt.
**Grounding:** campaign notes `gs-general-estimate-2026-08-14.md`, `gs-pcurve-boxwidth-2026-08-14.md`,
`gm-box-certifiability-2026-08-14.md`, `k1-moving-boundary-decision-2026-08-17.md`,
`paper-wu-bgstb25.md` (VERIFIED-FROM-PAPER on all four primary sources), `wave10-2026-summer-...md`,
`CAMPAIGN-STATE.md`. Primary sources read in this campaign: BGSTB24, BGSTB25, GS25, GS26 (full texts in
`research/papers/`). All arithmetic below re-verified by awk this session (Rust-only directive honored).

**Corrected prior-state note:** the task brief says this lever is "UNTESTED in this campaign". It is not —
the campaign tested its binding sub-input on 2026-08-14/17 (`gs-pcurve-boxwidth`, `k1-moving-boundary`
Type-1 NO) and its literature on 2026-08-14 (`gs-general-estimate`, `gm-box-certifiability`) and wave-10
(2026-08-18). This note consolidates, quantifies the tradeoff curves, and corrects two prior-note errors.

---

## VERDICT (up front)

1. **The box lever is CLOSED for the campaign target p₀ = 0.6818 — at every box width, even granting the
   box hypothesis itself at RH scale.** The box-width→proportion curve (BGSTB25 Thm 1–2) saturates at
   the Montgomery–Taylor constant **0.67250070** as the box half-width b → 0, and decreases with b
   (b=1: 0.617483786; b=2: 0.47485; method fails for b ≥ 4.2). No width reaches 0.6818, which requires
   C ≤ 1.318171 in the GS 2−C bridge vs the best box-certifiable C = 1.327499 (gap ΔC ≈ 0.00933).
   **[PROVEN (conditional on the box hypothesis; arithmetic CHECKED NUMERICALLY this session)]**
2. **The box lever also cannot beat the campaign's OWN unconditional record 0.673563 simple-on-line.**
   The best *conditional* box theorem (b = 0.001, Montgomery–Taylor kernel) certifies 0.6725 simple AND
   0.6725 on-line. The joint simple-and-on-line bound from the box is ≤ 0.6725 in every reading:
   0.345 via BGSTB25's 3−2C_b bound, possibly up to 2−C_b = 0.6725 via GS25 Thm 3(i)'s stronger
   multiplicity argument (INCONCLUSIVE which — see §5b — but both ≤ 2/3-level, below the record); the
   b→0 limit gives 2/3 simple / 2/3 on-line. All < 0.673563. **[PROVEN (conditional; campaign record
   CHECKED NUMERICALLY in CAMPAIGN-STATE)]**
3. **The binding input — the k<1 moving-boundary count N(1/2+b/L,T) = o(T log T) at fixed b ≈ 0.0758 —
   is not reachable by any known theorem, Guth–Maynard included.** Any zero-density theorem
   N(σ_b,T) ≪ T^{A(1−σ_b)}log^k T has ratio to N(T) ≥ e^{−2b}·L^{k−1}·T^ε: certifies o(T log T) ONLY if
   ε = 0 AND k = 0 (log-free, ε-free density hypothesis at the moving boundary). Every known theorem
   carries ε > 0 and k ≥ 1 (Ingham k=5, Montgomery k=13). **[PROVEN — elementary floor, k1 note §2,
   re-derived here; Type-1 NO on this sub-question stands, HIGH confidence]**
4. **Guth–Maynard cannot certify the box: (i) fixed-σ (Shape-1) scale-blindness — PROVEN-grade model
   argument; (ii) polylog slack k ≥ 1 — every ZDE fails the k < 1 requirement; (iii) the GM method
   loses a fixed log power near the line (Littlewood–Jensen obstacle) and its corollary kills the tail
   only at fixed distance from the line.** GM's exact range/threshold: INCONCLUSIVE (not read directly
   this session; campaign read the expository survey arXiv:2607.04632 only). **[Verdict PROVEN given
   Shape-1; GM parameters INCONCLUSIVE]**
5. **The most promising route is not more zero-density and not a smaller box — it is the classification
   lemma (gm-box §8): does N(1/2+b/L,T) = o(T log T) follow from a log|ζ|-type statement (e.g. an
   S(T) = o(log T) or Selberg second-moment input)?** The count is a genuinely RH-scale statement —
   strictly stronger than the Lindelöf-hypothesis density corollary, strictly weaker than RH
   **[PROVEN derivations]** — so the correct-scale toolset is Selberg/argument-type, not density-type.
   Honest caveat: S(T) = o(log T) is itself OPEN (best known S(T) ≪ log T/log log T); this is a
   literature-classification target, not a funded probe.

---

## 1. The object, reconstructed (paper identities RESOLVED)

### 1a. The double-sum estimate ("RH-replacement") — GS25 Theorem 2
**Source: Goldston–Suriajaya, *Zeta Zeros on the Critical Line*, arXiv:2511.20059v2 (Feb 2026), Thm 2.**
[VERIFIED-FROM-PAPER via campaign note `paper-wu-bgstb25.md` §4; this campaign holds the full text.]

> **Theorem 2 (GS25).** If there is a constant C with 1 ≤ C < 2 such that, as T → ∞,
> Σ_{ρ,ρ′: 0<γ,γ′≤T, γ=γ′} 1 ≤ (C+o(1))·(T/2π)log T,
> then asymptotically at least the proportion **2−C** of the zeros are **simple**, and at least the
> proportion **2−C** are **on the critical line**; and if 1 ≤ C < 3/2, at least **3−2C** are simple AND
> on the critical line.

- The sum is over pairs of zeros sharing an ordinate (a *double sum over zeros*); without RH, γ = γ′ no
  longer forces ρ = ρ′ (symmetric pairs β+iγ, 1−β+iγ share ordinates). GS25's (5.1) decomposes the sum
  into diagonal (multiplicity → simple) + symmetric-diagonal (off-line zeros → on-line) + non-symmetric
  horizontal residual. **[PROVEN — decomposition unconditional; the (4.4) hypothesis is the unproven
  input]**
- Under RH, Montgomery (1973) proves the hypothesis with C = 4/3 (Fejér kernel), giving 2/3 simple
  **[PROVEN (conditional on RH)]**. The open input: any unconditional (or weaker-than-RH) C < 2.
- Campaign ledger do-not-repeat: "GS-2026 needs C<2 (no C<2 known); wave-10 gave NO C<2 input." ✓
  consistent with this. **[PROVEN (literature state as surveyed)]**

### 1b. The box form — BGSTB24 Theorem 2 and BGSTB25 Theorems 1–2
**Sources: (i) Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh, *An unconditional Montgomery theorem for
pair correlation of zeros of the Riemann zeta-function*, arXiv:2306.04799 (2023) — "BGSTB24"; (ii) same
authors, *Pair correlation of zeros of the Riemann zeta-function I: proportions of simple zeros and
critical zeros*, arXiv:2501.14545 (2025) — "BGSTB25".** [VERIFIED-FROM-PAPER via `paper-wu-bgstb25.md`]

- **BGSTB24 Thm 2 (the campaign's "0.617"):** if all zeros with T^{3/8} < γ ≤ T satisfy
  |β − 1/2| < 1/(2 log T), then ≥ 61.7% of them are simple. The constant:
  2 − 1.289389678/(2 × 0.4663199124) = **0.617483786…** **[PROVEN (conditional on the box); constant
  CHECKED NUMERICALLY this session: 0.6174837877]**. Same result under the strong zero-density
  hypothesis N(σ,T) = o(T^{2(1−σ)}) on [1/2 + 1/(2logT), 25/32 + η] (Thm 3); box ⟹ ZDH (BGSTB24 §6).
- **BGSTB25 Thm 1 (b → 0, box B_b = {|σ−1/2| < b/(2 log T), T < t ≤ 2T}):** N^s ≥ (2/3+o(1))N(B_b),
  N⁰ ≥ (2/3+o(1))N(B_b), N^s₀ ≥ (1/3+o(1))N(B_b). **Thm 2 (fixed b):** see §2 curve. [VERIFIED-FROM-PAPER]
- **GS26 narrow box: Goldston–Suriajaya, *Zeta Zeros in a Narrow Vertical Box*, arXiv:2603.28104
  (2026):** box with b = b(T) → 0 ⟹ ≥ 2/3 simple AND on the line. [VERIFIED (abstract); full proof
  unopened in campaign → INCONCLUSIVE on proof details]

### 1c. Identity resolution (task item 1)
- **BGSTB = Baluyot, Goldston, Suriajaya, Turnage-Butterbaugh** (resolved; was open in the lever brief).
- The task brief's guess "arXiv:1904.08722" is NOT the paper; the correct objects are GS25
  (arXiv:2511.20059) Theorem 2 (double sum) + BGSTB24/BGSTB25 (box). **[PROVEN — arXiv API + full texts]**
- "Fujii's theorem" connection: GS25's framework is the pair-correlation lineage (Montgomery 1973
  Fejér kernel); the "double sum over zeros" is the equal-ordinate sum, not a Fujii-type mean of ζ at
  shifted zeros. If the lever brief meant a Fujii-type object (Σ_γ ζ(1/2+i(γ+u))), that is a DIFFERENT
  object not required by the GS bridge. **[INCONCLUSIVE on the brief's intent; the GS25 Thm-2 reading is
  the one that produces 0.617/2/3, so it is the operative one]**

---

## 2. The box-width → proportion tradeoff (task item 2)

### 2a. The exact curve (BGSTB25 (7.1)–(7.2)) [VERIFIED-FROM-PAPER; all values CHECKED NUMERICALLY]

With the Tsang-type kernel K_b, K̂_b(t) = j(2πt)/cosh(2πbt), and kernel j ∈ {j_F Fejér, j_M
Montgomery–Taylor}:

> **P_j(b) := 2 − C_b(j),   C_b(j) = [j(0) + 2∫₀¹ α j(α)/cosh(bα) dα] / [2∫₀¹ j(α)/cosh(bα) dα],**
> giving N^s, N⁰ ≥ P_j(b)·(T/2π)log T and Σ_{β≠1/2} m_ρ ≤ (C_b(j) − 1 + o(1))·(T/2π)log T;
> simple-and-on-line ≥ 3 − 2C_b(j) = 2P_j(b) − 1.

Monotone **decreasing in b** for each fixed j. Anchors (BGSTB25 Thm 2 Table 1; paper-wu note):

| b (half-width in units 1/(2logT)) | P(b) = 2 − C_b | notes |
|---|---|---|
| → 0, j_M | **0.67250070** | Montgomery–Taylor constant 2 − (½ + 2^{−½}cot 2^{−½}) — CHECKED NUMERICALLY this session: 0.6725007037 |
| → 0, j_F | 0.66666667 = 2/3 | Fejér (Montgomery RH limit) |
| 0.001 | 0.67250064 | (j_M) |
| 0.3185 | 0.66666908 | ≈ 2/3; GS25 Thm 4: b=0.3185 ⟹ ≥ 2/3 simple-and-on-line [INCONCLUSIVE — see §5b] |
| **1** | **0.617483786** | = BGSTB24's 61.7% — the b=1 point of the same curve |
| 2 | 0.47485 | method fails for b ≥ 4.2 (simple/on-line); b ≥ 2 for simple-and-on-line |

### 2b. What width reaches p₀ = 0.6818? — NONE (decisive)

p₀ = 0.68182868746 ⟺ C ≤ 2 − p₀ = **1.318171** in the 2−C bridge. The curve's infimum over b is
C = 1.327499 (b→0, j_M) — **above** 1.318171. Gap ΔC ≈ 0.00933 ≈ Δp. **[PROVEN — monotone curve +
arithmetic CHECKED NUMERICALLY]**

The relation in C-terms (task item 2b, "proportion as a function of near-line density exponent"): the
machinery's input is the *guarantee that all but o(N) zeros lie in the box* (equivalently the tail count
N(1/2+b/L,T) = o(T log T)). That guarantee is a **binary gate**, not a continuum: once certified, it
feeds C_b(j); and C_b(j) is bounded below by 1.3275 no matter how narrow the certified box. A *weaker*
guarantee (positive proportion in the box) feeds a strictly weaker bound. Hence:

> **No box width, and no positive-proportion box guarantee, pushes the GS/BGSTB proportion past
> 0.67250070; p₀ = 0.6818 is unreachable through this machinery even with the box hypothesis granted at
> RH scale (b → 0).** Reaching p₀ via 2−C requires the raw diagonal input C ≤ 1.318171 — a near-RH
> statement (C = 4/3 is RH; C = 1 is the "essential simplicity"/100% limit). **[PROVEN-conditional;
> arithmetic CHECKED NUMERICALLY]**

### 2c. The strength ladder of the needed count (task item 2b continued)

The needed input, N(1/2+b/L,T) = o(T log T) at fixed b = 0.0758, sits in the following web
[derivations PROVEN; literature completeness caveated]:

- **RH ⟹ count = 0.** [PROVEN, trivial]
- **Lindelöf hypothesis does NOT reach it:** LH ⟹ density hypothesis N(σ,T) ≪ T^{2(1−σ)+ε} (ε > 0
  inherent); at σ_b this is T^{1−2b/L+ε} = T·e^{−2b}·T^ε, whose ratio to N(T) ~ (T/2π)L is
  2π·e^{−2b}·T^ε/L → ∞. [PROVEN — derivation; "LH doesn't imply it via any route" INCONCLUSIVE]
- **Any ZDE N(σ_b,T) ≪ T^{1−cb/L}log^kT** (equivalently exponent 1 − cb/L with c the slope, k the
  polylog power): ratio to N(T) ≥ 4π·e^{−cb}·log^{k−1}T (the P(b) curve in §4 of `gm-box`):
  certifies o(T log T) **iff k < 1** (k = 0 suffices for any fixed b); k = 1 gives positive proportion
  iff b > log(4π)/c (c=2: b > 1.266; c=4/3: b > 1.898 — CHECKED NUMERICALLY); k ≥ 2 is vacuous.
  **[PROVEN]**
- **The needed exponent at σ_b = 1/2 + b/L is 1 − c/L with polylog power k < 1** — the "k<1
  moving-boundary" of CAMPAIGN-STATE. Note b itself is NOT the obstacle: any fixed b > 0 works once
  k < 1 is available (b = 0.0758 is comfortably inside the certificate's usable range b ≤ 0.2237,
  pair-form ceiling [PROVEN, k1 note §0]).

### 2d. Direct answer to task item 2

(a) With box width 1/(2 log T) (b=1), the authors' arguments give **61.7% simple** (BGSTB24/BGSTB25).
(b) No box width pushes past p₀ = 0.6818: the curve maxes at 0.67250070 (b→0, Montgomery–Taylor);
even RH-conditional pair-correlation SDP (Chirre–Gonçalves–de Laat ≈ 0.679, per campaign p-curve note
— [INCONCLUSIVE, not independently re-verified]) is < 0.6818. The functional relation is
P(b) = 2 − C_b(j) (decreasing in b) and, via the near-line density exponent, P_out ≤ 4π·e^{−cb}·log^{k−1}T
(needs k < 1).

---

## 3. Guth–Maynard comparison (task item 3): does GM certify the box?

**No — and the reasons are now structural, not parametric.** [Verdict PROVEN given Shape-1; GM's exact
range INCONCLUSIVE]

1. **Scale blindness (Shape-1).** GM (2024, "New large value estimates for Dirichlet polynomials") is a
   fixed-σ zero-density estimate: valid for σ ≥ σ₀ > 1/2 with exponent of the shape A(1−σ) + ε. A
   fixed-σ estimate is consistent with ALL zeros lying at β = 1/2 + σ₀/2 (a valid configuration
   satisfying the estimate trivially) while N(1/2+b/L,T) = N(T) — so it certifies NO shrinking box.
   **[PROVEN — model configuration argument, gm-box §3; independent of GM's exact (A, σ₀)]**
2. **Polylog slack.** The count needs ε = 0 AND k = 0 at the moving boundary. GM, like Ingham (k=5)
   and Montgomery's density hypothesis (k=13), carries ε > 0 and k ≥ 1; the ratio
   e^{−2b}·L^{k−1}·T^ε → ∞. **[PROVEN — §2c]**
3. **Near the line, every zero-detection method loses a fixed log power** (sup |ζ′/ζ| on a line at
   distance b/L from the line spikes; Littlewood–Jensen obstacle) — this eats the entire margin at the
   moving boundary. Campaign's in-program note: GM's corollary kills the right tail only at fixed
   Δ > 19/70 ≈ 0.2714 (σ ≳ 0.77) — far from 1/2 + 0.0758/L → 1/2. **[PROVEN (in-program, k1 §3);
   the 19/70 threshold itself INCONCLUSIVE — source chain is gm-box → k1, GM paper not read]**
4. **Wave-10 (2026-08-18) adjudication:** GM improves zero-density away from 1/2 and primes-in-short-
   intervals, but near-line exponent → 1 as σ → 1/2⁺ (same as Ingham's 3(1−σ)/(2−σ) → 1), so it
   supplies no input to the GS diagonal bound C < 2 and no near-line control. [VERIFIED-FROM-SURVEY
   arXiv:2607.04632, Turnage-Butterbaugh's expository account; GM paper itself INCONCLUSIVE]

**Exact GM data as known this session:** the campaign cites GM as arXiv:2405.20552 (k1 note) — the ID
was not independently confirmed here (the campaign's wave-10 read only the survey 2607.04632). Whether
GM's threshold is σ₀ ≈ 0.5169 or σ₀ = 25/32-type does not change the verdict (item 1 above is
parameter-independent). **[INCONCLUSIVE on the precise GM corollary; PROVEN that it cannot certify the
box regardless]**

**Is the box-lever the same wall as the GS-2026 diagonal? YES.** The GS bridge needs C < 2; the
off-line symmetric-diagonal term Σ_{β≠1/2}m_ρ is controlled exactly by near-line zero counts
(= 2N(σ_b,T) by functional-equation symmetry, gm-box §1 [PROVEN]); GM controls neither. Wave-10's
negative for the diagonal is the same near-line wall as the box's count input. **[PROVEN —
identification; the near-line wall itself is the open quantity]**

---

## 4. Single most promising route (task item 4)

Within THIS lever, nothing is fundable: the box is closed for p₀ (max 0.6725 < 0.6818), cannot beat the
campaign's own unconditional 0.673563 record, and the count input is Type-1 NO (HIGH confidence). The
lever's residual value is:

1. **The classification lemma (gm-box §8) — the only "correct-scale" move.** Establish whether
   N(1/2+b/L,T) = o(T log T) at fixed b is implied by — or equivalent to — a log|ζ|-type statement
   (S(T) = o(log T); Selberg second-moment/argument-type inputs). The count is RH-scale, so the
   correct toolset is Selberg/argument-type, NOT zero-density (which is scale-blind). Honest caveat:
   S(T) = o(log T) is itself OPEN (best unconditional S(T) ≪ log T/log log T), so this is a
   literature-classification target that would, at best, re-anchor the open problem — not a proof.
   **[CONJECTURED value; the classification itself is open/INCONCLUSIVE]**
2. **GS25 Thm 2 as the cleanest framing of what a new object would buy:** any input proving the
   diagonal count with C < 2 (or the multiplicity-sum form with C ≤ 1.318171 for p₀) converts
   directly into simple + on-line proportions. It does not change what needs proving (near-line
   control), but it is the sharpest statement of the prize. **[PROVEN — framework]**
3. Everything else on the record side is terminal in-class (ceiling 0.6818 Lean-proven; class
   saturated at 0.673563). The campaign's surviving openings stand unchanged: GJT-completion
   (RH-equivalent, hard) and genuinely new objects. **[PROVEN — CAMPAIGN-STATE]**

---

## 5. Honesty section

### 5a. Corrections to prior campaign notes (new this session)
1. **`gs-pcurve-boxwidth-2026-08-14.md` says P(b) is "flat on (0,1]". REFUTED by BGSTB25 Table 1**
   (VERIFIED-FROM-PAPER): P(b) = 2 − C_b(j) decreases in b (0.6725 @ b→0 → 0.61748 @ b=1 → 0.47485
   @ b=2). The p-curve note's constant is the **b = 1 specialization** of BGSTB25's (7.1) (its
   cosh(α) = 1/sech(α) matches the p-curve's sech kernel). Its conclusion (no b solves 0.6818) is
   CORRECT and is here strengthened: sup_b P = 0.67250070 < 0.6818. **[CORRECTION; conclusion
   unchanged]**
2. **`wave9-9A` / wave-9 note says "BGSTB25 Thm 2 at b=0.001 gives 67.25% simple-and-on-line".**
   Mislabeling: 67.25% is simple AND (separately) on-line; simple-and-on-line at b=0.001 is 34.5%
   (2·0.67250064 − 1 = 0.34500128, CHECKED NUMERICALLY). Wave-9's conclusion (record stands above
   conditional box theorems) survives — strengthened. **[CORRECTION; conclusion unchanged]**
3. The task brief's "0.617 from the box, 0.617 < p₀" framing is right, but the "what box width would
   push past p₀" question has a **negative answer independent of width** (§2b) — the campaign's own
   p-curve note already concluded this; this note grounds it in the full BGSTB25 curve.

### 5b. INCONCLUSIVE items (checked, not resolved)
- **Simple-and-on-line under the box: BGSTB25 (1.4)/(7.2) gives 1/3 (b→0) via 3−2C_b; GS25 Thm 3(i)/Thm 4
  claim ≥ 2−C_b = 2/3 under the multiplicity-sum hypothesis H2 = Σm + Σ_{β≠1/2}m ≤ C·N.** Re-derivation
  this session: H2 ⟹ simple-and-on-line ≥ 2−C **is correct** (the +2O_m term from off-line multiple
  zeros, missed by naive inclusion-exclusion), so GS25 (Feb 2026) plausibly improves BGSTB25's (Nov 2025)
  weaker 3−2C_b intersection bound — a later-paper improvement, likely not a transcription error. Either
  way the joint bound is ≤ 2/3 < 0.673563 and < p₀, so the verdict is unaffected. Needs the GS25 full
  text to adjudicate. **[INCONCLUSIVE]**
- GM's exact corollary range/threshold and arXiv ID. **[INCONCLUSIVE]**
- Whether the count is implied by any known hypothesis weaker than RH (LH: NO via density corollary —
  PROVEN; any other route: INCONCLUSIVE).
- Chirre–Gonçalves–de Laat 0.679 simple (RH-conditional, SDP) — cited via campaign p-curve note, not
  independently re-verified. **[INCONCLUSIVE]**
- GS26 (narrow box, 2603.28104) proof details. **[INCONCLUSIVE]**

### 5c. Labels summary
| Claim | Label |
|---|---|
| GS25 Thm 2: Σ_{γ=γ′}1 ≤ (C+o(1))N, 1≤C<2 ⟹ 2−C simple, 2−C on-line, 3−2C both (C<3/2) | PROVEN (conditional on the count; statement VERIFIED-FROM-PAPER) |
| RH ⟹ C = 4/3 ⟹ 2/3 simple (Montgomery 1973) | PROVEN (conditional on RH) |
| BGSTB24 Thm 2: box 1/(2logT) ⟹ 61.7% simple | PROVEN (conditional on box); constant 0.617483786 CHECKED NUMERICALLY (this session: 0.6174837877) |
| BGSTB25: P(b) = 2 − C_b(j), decreasing; sup = 0.67250070 (b→0, Montgomery–Taylor) | PROVEN (conditional on box; VERIFIED-FROM-PAPER; MT constant CHECKED NUMERICALLY) |
| No box width reaches p₀ = 0.6818 (needs C ≤ 1.318171; best C = 1.327499; ΔC ≈ 0.00933) | PROVEN (arithmetic CHECKED NUMERICALLY) |
| Box machinery's simple-and-on-line ≤ 0.345 (b=0.001) / 1/3 (b→0) per BGSTB25 (7.2); ≤ 2/3 in every reading (GS25 Thm 3(i) — INCONCLUSIVE) — below record 0.673563 | PROVEN (conditional; arithmetic CHECKED NUMERICALLY) |
| Count N(1/2+b/L,T) = o(T log T) at fixed b: needs ε=0, k=0 (log-free moving-boundary ZDE); no known theorem reaches it (Ingham k=5, Montgomery k=13, GM Shape-1) | PROVEN (elementary floor; Type-1 NO HIGH confidence, k1 note) |
| GM cannot certify the box (Shape-1 scale-blindness) | PROVEN (model argument, parameter-independent); GM exact range INCONCLUSIVE |
| LH does not imply the count via its density corollary | PROVEN (derivation) |
| Count open in both directions; numerically unfalsifiable (all zeros verified on line to 3·10¹², Platt–Trudgian, per GS25) | PROVEN (campaign literature chain); [underlying verification INCONCLUSIVE here] |
| "Flat P(b)" (gs-pcurve note) | REFUTED (BGSTB25 Table 1) — conclusion (no b₀) survives |
| "67.25% simple-and-on-line at b=0.001" (wave-9) | CORRECTED: 67.25% simple, 67.25% on-line separately; 34.5% jointly |
| Classification lemma (count vs S(T)=o(log T)) as the most promising route | CONJECTURED (value); S(T) = o(log T) itself OPEN |

*No proof attempt made; no computation beyond re-verification of published constants (awk, this
session). All labels per hooks/agents.md §2. Sources cited precisely: GS25 arXiv:2511.20059, GS26
arXiv:2603.28104, BGSTB24 arXiv:2306.04799, BGSTB25 arXiv:2501.14545, Guth–Maynard 2024 (ID
INCONCLUSIVE), Turnage-Butterbaugh survey arXiv:2607.04632, Montgomery 1973.*
