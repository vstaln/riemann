# PCC II deep-read (GLSS26, arXiv:2507.06823) — and what PCC I (GLSS25) proves: mapping to the three walls

**Agent:** EXECUTIONER. **Round:** 3. **Date:** 2026-08-11.
**Files:** `research/papers/glss26-2507.06823-pccII-ah.pdf` (deep-read; text extraction `/tmp/glss26.md` via `uvx --from 'markitdown[pdf]' markitdown`), `research/papers/glss25-2503.15449-pccI.pdf` (read in full for the PCC I statements; extraction `/tmp/glss25.md`).
**Question:** what exactly do PCC I/II prove about pair correlation, in what ranges, under what hypotheses; is any of it unconditional; does either paper reopen the beyond-α=1 mean wall (M29), the beyond-1 variance wall (B10/GM-variance), or touch the GM variance / third moment.
**Expected outcome (per brief):** deep-read + mapping; likely a documented NO.
**Verdict (up front):** **NO wall reopens.** PCC II is **not** the "arithmetic/height aspects" paper the fetch memo guessed — it is *"Pair Correlation Conjecture for the zeros of the Riemann zeta-function II: The Alternative Hypothesis"*. It proves that the **Alternative-Hypothesis** pair-correlation conjectures (AH-Pairs + AH-Weak Density) would force asymptotically 100% of the zeros to be simple and on the critical line — the exact mirror of PCC I's "PCC ⟹ 100% simple and critical", both **without RH but with a conjecture as input**. The unconditional content in both papers is entirely **in-band** (fixed or slowly growing spacing-window statistics): Fujii's S-moment (the zero-count variance), the GM78 average-pair-correlation formula plus the Zero-Repulsion bound, and GM87 Lemma 9's close-pair-count bound. None of it constrains the form factor F(α) at |α| > 1 except through a growing-window Fejér *average* whose main term equals the F ≡ 1 value plus a variance log-correction — an average, not a value, and the classical GM87 average content. M29 (beyond-1 mean DEAD) and B10/GM-variance (beyond-1 variance DEAD) stand unchanged; the variance flank is confirmed, not strengthened.

---

## 0. What PCC II actually is (correcting the fetch memo)

- **VERIFIED-FROM-PAPER** (title page): glss26-2507.06823 is *"PAIR CORRELATION CONJECTURE FOR THE ZEROS OF THE RIEMANN ZETA-FUNCTION II: THE ALTERNATIVE HYPOTHESIS"*, Goldston, Lee, Schettler, Suriajaya (July 10, 2025). The task memo's guess "with arithmetic/height aspects?" is **wrong**: the paper concerns the Alternative Hypothesis (Landau–Siegel-type spacing structure), not heights and not arithmetic aspects. No height content anywhere in the paper (checked the full text).
- **VERIFIED-FROM-PAPER** (abstract, quoted): "In an earlier paper, we proved that Montgomery's Pair Correlation Conjecture (PCC) for zeros of the Riemann zeta-function can be used to prove without the assumption of the Riemann Hypothesis (RH) that asymptotically 100% of the zeros are both simple and on the critical line. This is based on a method of Gallagher and Mueller from 1978. We formulate an appropriate form of the Alternative Hypothesis (AH), which determines a different PCC, and, using the same method as above, prove that asymptotically, 100% of the zeros are both simple and on the critical line. As in our previous paper, we do not assume RH."

---

## 1. Main theorems — verbatim from the arXiv texts

Quotes below are taken from the markitdown text extractions; superscripts/√/table glyphs are normalized, mathematical content unchanged. The papers' L := (1/2π)log T and N(T) ~ TL.

### 1.1 PCC I (GLSS25): the conjecture-in, 100%-out route

- **PCC (GLSS25 (4.3)–(4.4), quoted).** With N(λ) := Σ_{0<(γ′−γ)L≤λ} 1: "For UL = λ > 0, then
  N(λ) = TL ∫₀^λ (1 − (sin πα/πα)²) dα + o(TL), as T → ∞, uniformly in each interval
  0 < λ₀ = U₀L ≤ λ = UL ≤ λ₁ = U₁L < ∞."
- **Theorem 1 (GLSS25, quoted).** "Assuming the pair correlation conjecture PCC, then asymptotically 100% of the zeros of ζ(s) are simple and on the critical line." [The paper's headline: no RH anywhere in the proof.]
- **Proposition 1 (Gallagher–Mueller [GM78], GLSS25 (5.2)–(5.3), quoted).** For 0 < U ≤ 1:
  ∫₀^T (Δ_U N(t))² dt = T(UL)² + O(TU²L) + ∫₀^T (Δ_U S(t))² dt + O(L²), and the same integral equals Σ_{|γ′−γ|≤U} (U − |γ′−γ|) + O(L²). [Δ_U F(t) := F(t+U) − F(t).]
- **Proposition 2 (Fujii, GLSS25 (5.6), quoted; UNCONDITIONAL).** For 0 < U ≤ 1:
  ∫₀^T (Δ_U S(t))² dt = (T/π²) log(2+UL) + O(T √log(2+UL)). [The paper: "They both prove this unconditionally for the 2k-th moments. This result depends on an unconditional explicit formula of Selberg for S(t) [Sel46, Theorem 2]"; under RH the error improves to O(T) but "this does not improve any results we obtain".]
- **Unconditional average pair-correlation formula (GLSS25 (6.0)–(6.2), quoted in normalized form).** For λ → ∞ as T → ∞, 0 < λ² ≤ L (so U = λ/L ≤ 1):
  N^⊛(T) + (2/λ) ∫₀^λ N(α) dα = TL ( λ + log(2+λ)/(π²λ) + O(√log(2+λ)/λ) ),
  where N^⊛(T) := Σ_{γ=γ′} 1 counts ordered pairs with equal ordinates (the "horizontal multiplicity" sum).
- **Zero Repulsion (Gallagher–Mueller, GLSS25 (6.3), quoted; UNCONDITIONAL).** For 0 < λ ≤ √L:
  (2/λ) ∫₀^λ (N(α) − αTL) dα = −N^⊛(T) + TL·log(2+λ)/(π²λ) + O(TL·√log(2+λ)/λ) ≤ −TL + o(TL), if λ → ∞ as T → ∞. [The paper: "the negative upper bound in (6.3) is the minimum repulsion that can occur. As we will see, PCC gives this minimum repulsion."]
- **Horizontal Multiplicity Hypothesis (HMH, GLSS25 §7, quoted):** N^⊛(T) = Σ_γ H(γ) = (1+o(1))TL, H(γ) = number of zeros on the horizontal line t = γ (with multiplicity). H(γ) = 1 ⟺ the line carries exactly one simple, critical zero.
- **Theorem 2 (GLSS25, quoted).** "Assuming HMH is true, then asymptotically 100% of the zeros of ζ(s) are simple and on the critical line." [Proof: #{H(γ)=1} ≥ Σ(2−H(γ)) ≥ 2N(T) − (1+o(1))TL = (1+o(1))N(T).]

**The exact PCC ⟹ 100% route (GLSS25 §8, VERIFIED-FROM-PAPER):** PCC at λ₀ → 0 and λ → ∞ + the unconditional formula (6.2) + the Fejér-kernel evaluation 2∫₀^λ(1−α/λ)(sin πα/πα)²dα = 1 − logλ/(π²λ) + O(1/λ) [their (8.2)] ⟹ N^⊛(T)/TL → 1, i.e. HMH ⟹ (Theorem 2) 100% simple and critical. RH appears nowhere.

### 1.2 PCC II (GLSS26): the same machine for the Alternative Hypothesis

- **AH-Pairs (GLSS26 (1.9)–(AH0), quoted).** P(T,M) := {(γ,γ′): T/log²T < γ,γ′ ≤ T, |(γ−γ′)L| ≤ M}. "Then for every (γ,γ′) ∈ P(T,M) there is an integer k such that (γ−γ′)L = k/2 + O((|k|+1)R(T))" for a positive decreasing R(T) → 0. [Zeros sit at approximately half-integer multiples of the average spacing — the Landau–Siegel-spawned structure.]
- **Densities (1.10)–(1.11)** B_{k/2}(T) := {(γ,γ′) ∈ P(T,M): (γ−γ′)L ∈ (k/2−1/4, k/2+1/4]}, P_{k/2}(T) := |B_{k/2}(T)|/(TL), P_{k/2} = P_{−k/2}.
- **Unconditional bound (1.12)–(1.13), quoted; from GM87 Lemma 9.** For 0 ≤ h ≤ T: Σ_{ρ,ρ′, |(γ−γ′)L|≤h} 1 ≪ (1+h)TL; hence Σ_{|k|≤2M} P_{k/2}(T) ≪ M. ["the densities are unconditionally bounded for any fixed M, and the average of the densities are also bounded when M → ∞".]
- **RH-conditional density formulas (1.14)–(1.15) [BGSTB25a Theorem 1], quoted.** Assuming RH and AH-Pairs: 1+o(1) ≤ P₀(T) ≤ 3/2 − 2/π² + o(1) = 1.29735…+o(1), and for k ≠ 0: P_{k/2}(T) ∼ P₀(T) − 1/2 (k even), 3/2 − 2/(π²k²) − P₀(T) (k odd). [RH is used only here, through Montgomery's theorem for his F(α).]
- **Theorem 1 (GLSS26, quoted).** "Assuming AH-Pairs, we have that p₀ = 1 is equivalent to ESH." [ESH = N^⊛(T) = TL+o(TL) and N(T,λ₀) = o(TL) for λ₀ → 0 — the paper's AH-adapted "Essential Simplicity", (ES1)+(ES2); ESH ⟺ N^⊛(T) + 2N(T,λ₀) = TL + o(TL).]
- **Corollary 1 (GLSS26, quoted).** "Assuming AH-Pairs, if p₀ = 1, then asymptotically 100% of the zeros of ζ(s) are simple and on the critical line." [Via Theorem 1 + GLSS25 Theorem 2.]
- **AH-Weak Density (AH1)+(AH2), quoted.** For each positive integer j: P_{j−1/2}(T) + P_j(T) = 1 − 2/(π²(2j−1)²) + O(R_P(T)); and for any large even M: Σ_{j=1}^M P_{j−1/2}(T) = M/2 − 1/4 + O(1/M) + O(M R_P(T)), uniformly on 0 < m₁ ≤ M ≤ m₂ < ∞. [The paper: "the simplest model for the densities that is consistent with Theorem 2"; (AH1) "is obtained immediately from (1.15)".]
- **Theorem 2 (GLSS26, (1.18), quoted in extraction-normalized form).** Assuming AH-Pairs, for any sufficiently large even M: Σ_{j=1}^M 2(M−j)(P_{j−1/2}(T) + P_j(T) − (1 − 2/(π²(2j−1)²))) = (3/2 − P₀(T))M − Σ_{j=1}^M P_{j−1/2}(T) + O(√log M) + O(M²R(T) + M/L²).
- **Theorem 3 (GLSS26, (1.22)–(1.23)).** Assuming AH-Pairs + (AH1), the average forms 3/2 − P₀(T) = (1/M)Σ P_{j−1/2}(T) + O(√logM/M) + O(M(R(T)+R_P(T)) + 1/L²) and P₀(T) − 1/2 = (1/M)Σ P_j(T) + …; adding (AH2) gives P₀(T) = 1 + O(√logM/M) + O(M(R(T)+R_P(T)) + 1/L²), hence p₀ = 1 since M is arbitrary.
- **Theorem 4 (GLSS26, quoted).** "Assuming AH-Pairs and AH-Weak Density, we have p₀ = 1 and asymptotically 100% of the zeros of ζ(s) are simple and on the critical line."
- **Corollary 2 (GLSS26, quoted).** "Assuming AH-Pairs and (AH1), we have limsup_{T→∞} P₀(T) ≤ 3/2 and asymptotically at least 50% of the zeros of ζ(s) are simple and at least 50% are on the critical line." [Without (AH2).]
- **Proposition 2 (GM78/Fujii/Tsang, GLSS26 restatement, UNCONDITIONAL), quoted in normalized form.** For λ > 0 (fixed, so U = λ/L ≤ 1 eventually): ∫₀^T (N(t+λ/L) − N(t))² dt = λ²T + O(λ²T/L) + ∫₀^T (S(t+λ/L) − S(t))² dt + O(L²), with ∫₀^T (S(t+λ/L) − S(t))² dt = (T/π²)log(2+λ) + O(T√log(2+λ)); hence for the pair sum D(T,λ) := Σ_{|(γ−γ′)L|≤λ}(λ/L − |γ−γ′|): D(T,λ) − λ²T = (T/π²)log(2+λ) + O(T√log(2+λ)) + O(λ²T/L). [(3.1)–(3.2). This is GLSS25 Prop 1+2 restated in λ/L units.]

---

## 2. Exhaustive inventory of the UNCONDITIONAL content (both papers)

| # | Statement | Range | Where | Label |
|---|---|---|---|---|
| U1 | Fujii: ∫₀^T(Δ_U S(t))²dt = (T/π²)log(2+UL) + O(T√log(2+UL)) — the zero-count variance (via S) | 0 < U ≤ 1 (t-units; λ = UL ≤ L) | GLSS25 Prop 2 (5.6); GLSS26 Prop 2 | **PROVEN, UNCONDITIONAL** (Selberg explicit formula; no RH) |
| U2 | Average pair-correlation formula: N^⊛(T) + (2/λ)∫₀^λ N(α)dα = TL(λ + log(2+λ)/π²λ + O(√log(2+λ)/λ)) | λ → ∞, 0 < λ² ≤ L | GLSS25 (6.0)–(6.2) | **PROVEN, UNCONDITIONAL** (from U1 + GM78 Prop 1) |
| U3 | Zero Repulsion (GM): (2/λ)∫₀^λ(N(α) − αTL)dα ≤ −TL + o(TL) | λ → ∞, 0 < λ ≤ √L | GLSS25 (6.3) | **PROVEN, UNCONDITIONAL** |
| U4 | Close-pair count (GM87 Lemma 9): Σ_{|(γ−γ′)L|≤h} 1 ≪ (1+h)TL; Σ_{|k|≤2M}P_{k/2}(T) ≪ M | 0 ≤ h ≤ T | GLSS26 (1.12)–(1.13) | **PROVEN, UNCONDITIONAL** |
| U5 | Trivial estimates: Δ_U N(t) ≪ (1+U)L, Δ_U S(t) ≪ L | 0 ≤ t ≤ T, 0 ≤ U ≤ T | GLSS25 (9.1) | **PROVEN, UNCONDITIONAL** |
| U6 | Range-shifting estimate (2.1) (T/log²T < γ ≤ T vs 0 < γ ≤ T, error O(f(0)(1+h)T/L)) | 0 ≤ h ≤ M fixed | GLSS26 (2.1) | **PROVEN, UNCONDITIONAL** |

**Nothing unconditional about F(α) at |α| > 1 exists in either paper** — the form factor is never defined or used (the only mention of "his function F(α)" is in the RH-conditional remark around (1.15)). The one object that straddles α = 1 is U2/U3: the growing-window (Fejér/triangular) average of the pair correlation over spacing windows [0, λ] with λ → ∞. Interpreted via the standard duality (Σ_{|γ−γ′|L≤λ}(1 − |γ−γ′|L/λ) ↔ TL∫_{−λ}^{λ}(1−|α|/λ)F(α)dα), U2 says the λ-windowed average of F is 1 + log(2+λ)/(π²λ²) + o(1/λ) → 1. That is an **average** with weight vanishing at the boundary of the window; it constrains only the total mass of F and is compatible with any beyond-1 behavior that averages to the same. This is the classical GM87/Montgomery average-pair-correlation content, already implicit in the program's inputs; it supplies **no value** of F(α) for any α > 1 and no integral of F over any fixed window strictly beyond [−1,1].

*Normalization caution (VERIFIED-FROM-PAPER + program context):* Montgomery's F (≈ α on (0,1) unconditionally, B24 Thm 1) and the program's normalized form factor (≈ 1+|α| on [−1,1], giving ∫_{−1}^{1}(1−|α|)F = 4/3, per claude-riemann-paper Rem 5.10) are different normalizations; the GLSS papers work entirely in the pair-counting-function N(λ) language and never touch either F. This note reports only what the papers state, in their language.

---

## 3. Mapping to the three walls

### (a) Beyond-1 form factor (|α| > 1): does anything become unconditional?

**NO.** VERIFIED-FROM-PAPER: every statement in both papers whose conclusion concerns zeros is conditional on a conjecture (PCC in I; AH-Pairs (+AH-Weak Density) in II). The unconditional statements U1–U6 are in-band spacing-window statistics (fixed λ, or λ → ∞ with Fejér weight, or the (1+h)TL close-pair bound). U2/U3 are averages over windows straddling α = 1 but give no pointwise or fixed-window-beyond-1 information. The variance-side mechanism is identical to what the GM-variance note documented: unconditional theorems are sharp **in-band** (UL ≳ 1) and **vacuous beyond** (at UL ≪ 1, i.e. the α > 1 short-window regime, Fujii's error O(T√log 2) ≈ 0.83T dominates the main term (T/π²)log 2 ≈ 0.07T).

### (b) The exact PCC ⟹ 100% simple route, and what PCC II adds

Route (VERIFIED-FROM-PAPER, GLSS25 §8): PCC (conjecture) + U2 (unconditional, GM78/Fujii) + Fejér evaluation (8.2) ⟹ HMH (N^⊛(T) = (1+o(1))TL) ⟹ Theorem 2: 100% simple and critical. RH never appears. (See §1.1; the key step is that the λ-windowed pair correlation under PCC gives N^⊛(T)/TL → 1, and N^⊛(T) is the horizontal-multiplicity sum: N^⊛(T) = TL+o(TL) forces one zero per horizontal line a.e., hence simple + critical.)

What PCC II adds (VERIFIED-FROM-PAPER):
1. **The AH mirror (Theorem 4):** AH-Pairs + AH-Weak Density ⟹ p₀ = 1 ⟹ 100% simple and critical — i.e., if the Alternative-Hypothesis spacing structure holds, the same Gallagher–Mueller machine still forces 100%. This is a *conditional* statement about the zeros (both hypotheses are conjectures); it does not produce any unconditional statement.
2. **Theorem 1:** under AH-Pairs, p₀ = 1 ⟺ ESH (a clean equivalence pinning which AH datum controls essential simplicity).
3. **Corollary 2:** AH-Pairs + (AH1) only ⟹ limsup P₀ ≤ 3/2 and ≥ 50% simple, ≥ 50% critical (a partial, still AH-conditional, result).
4. **RH-conditional (1.15)** (from BGSTB25a): the full density formula p_{k/2} — the "arithmetic" of the AH spacing structure — used only as a model, and only under RH.
5. **No explicit error terms beyond Fujii's O(T√log(2+λ))**, and **no arithmetic/height aspects** (contrary to the memo guess).

### (c) GM variance / third moment

- **Variance:** the papers **use** the zero-side variance — Fujii's S-moment (U1) — as the engine of U2/U3 (the log(2+λ)/π²λ term in U2 IS the variance term). This is the identical statement already inventoried in `attack-gm-variance.md` (row 2: "Fujii via GLSS25 Prop 2, UNCONDITIONAL, sharp in-band, vacuous at UL ≪ 1"). The **Goldston–Montgomery PRIME variance** (the CCCM J(β,T) object; β > 1 ⟺ PCC) is **not** touched by either paper — no prime-side variance appears anywhere.
- **Third moment:** **not touched** by either paper (the third moment lives in `fg-2412.20099-third-moment-twisted-pcc.pdf`, held separately, not part of this read).

---

## 4. Verdict: does PCC II change M29 or B10/GM-variance? — NO, on both

| Wall | Prior verdict (labeled) | PCC II effect | Reason (all VERIFIED-FROM-PAPER + prior notes) |
|---|---|---|---|
| M29 — beyond-1 **mean** (|α|>1 form-factor values for the certificate's off-diagonal prime sums at X = T^{1+ε}) | DEAD (PROVEN negative, M29): only MV-Hilbert/sieve/VK bounds, all ≫ tolerance; the only inputs that clear it are HL / Montgomery PCC values — CONJECTURED | **No change** | PCC II contains no prime-side statement and no |α|>1 value statement. Its unconditional content (U1–U4) is zero-side, in-band, and already inventoried. The zero-to-prime bridge is the GM87/SPC correspondence (conjectural beyond trivial) — same orthogonality the GM-variance note documented. All beyond-1 statements remain conjectural. |
| B10/GM-variance — beyond-1 **variance** (β>1 variance ⟺ Montgomery's conjecture, CCCM) | DEAD (PROVEN, GM-variance note): dictionary inverted; no unconditional variance reaches α > 1 with content; variance orthogonal to the certificate | **No change** | PCC II's Fujii statement (U1) is the same in-band zero-side variance; at the beyond-1 windows (U < 1/ρ) it is vacuous (error dominates). PCC II states no beyond-1 variance, and its (3.2) is for fixed λ. The β > 1 variance asymptotic remains equivalent to PCC — CONJECTURED. |
| Third moment as unconditional input | DEAD (per literature map §(b)6: unconditionally higher moments add nothing) | **No change** | Neither paper touches the third moment. |

**Does PCC II reopen any wall? NO.** Reason, in one line: every conclusion-about-zeros statement in both papers is conditional on PCC (resp. AH-Pairs + AH-Weak Density); the unconditional statements are in-band second-moment/repulsion facts (Fujii, GM78, GM87 Lemma 9) that were already in the dossier and constrain the beyond-1 form factor only through averages that are consistent with every beyond-1 behavior. The papers strengthen the *route* "conjecture ⟹ 100%" (now available for both PCC and AH), but the conjecture is and remains the input; nothing is subtracted from the conjecture's status.

---

## 5. What its techniques offer the unconditional program

1. **Fujii's S-moment with explicit error (U1)** — a certified, unconditional, in-band variance input with a stated error O(T√log(2+UL)). Already in the dossier (GM-variance note, used in `var_probe2.py` as the GUE/Fujii comparison); this read confirms the statement and its range from the primary text.
2. **The Zero-Repulsion bound (U3)** — an unconditional upper bound on the Fejér-windowed integral of the pair correlation (equivalently the windowed form-factor integral over [−λ,λ]): (2/λ)∫₀^λ(N(α) − αTL)dα ≤ −TL + o(TL). This is a usable *in-band* constraint on the low-frequency mass of F; it does not reach α > 1 values.
3. **GM87 Lemma 9 (U4)** — the unconditional close-pair bound O((1+h)TL), verified against real zeros in the accompanying script (§6): a tight-ish, scripted in-band pair-counting bound.
4. **The horizontal-multiplicity framework (HMH/N^⊛, GLSS25 Thm 2)** — the clean structural statement "average pair correlation ⟹ 100% simple + critical without RH". For the unconditional program this is a template: any future *unconditional* control on N^⊛(T) (or on a windowed pair-correlation integral) converts directly into a proportion of simple-and-critical zeros by the (2−H(γ)) argument. The AH mirror (PCC II Thm 4) shows the machine is robust to the *form* of the conjecture — useful if a future attack targets the AH family (e.g. Landau–Siegel-adjacent L-function families, per paper-finder item #8 on bgst-2508.10857).
5. **The p₀ = 1 ⟺ ESH equivalence (PCC II Thm 1)** — reduces "100% under AH" to the single density p₀, a clean target for any future conditional analysis in the AH family.

**None of these touch the beyond-1 walls.** In-band, the program's certificate already works (0.6725; bandwidth-one ceiling 0.6818, literature map §3, PROVEN); the GLSS input U2/U3 is the same in-band second-moment content the certificate's λ=1 evaluation already uses (the (1/λ + λ/3) moment, literature map §5 item 5).

---

## 6. Numerics (all CHECKED NUMERICALLY — script + command)

**Script:** `research/notes/paper-pcc2/paper-pcc2-check.py`
**Command:** `cd /home/vstaln/riemann && timeout 300 uv run --with numpy --with scipy python research/notes/paper-pcc2/paper-pcc2-check.py`
**Data:** `tools/data/zeros_computed_10000.txt` (10⁴ zeros, γ ∈ [14.135, 9879.0], column 1 = ordinate).

| Check | Result | Reading |
|---|---|---|
| PCC II (1.14) constant 3/2 − 2/π² | 1.2973576327 | matches paper's "= 1.29735..." (VERIFIED-FROM-PAPER + numerics) |
| PCC II (1.17) at k=1: 1/2 − 2/π² | 0.2973576327 | matches |
| GLSS25 (8.2): I(λ) = 2∫₀^λ(1−α/λ)(sinπα/πα)²dα vs 1 − logλ/π²λ | λ·|diff| → 0.3460 as λ: 1→50 | confirms I(λ) = 1 − logλ/π²λ + O(1/λ) with constant ≈ 0.346 (VERIFIED-FROM-PAPER (8.2)) |
| PCC density g(α) = ∫₀^α(1−(sinπu/πu)²)du | g = α − 1/2 + o(1) (diff: 2.5e-2 → 1.0e-3) | confirms the PCC integrated density (Fejér repulsion value) |
| Cesàro (2/λ)∫₀^λ g = λ − 1 + o(1) | diff: 1.0e-1 → 4.4e-3 (λ: 5→200) | confirms "PCC achieves the minimum repulsion" (GLSS25 (6.3) remark), i.e. under PCC (2/λ)∫₀^λ(N(α)−αTL)dα → −TL |
| GM87 Lemma 9 / PCC II (1.12) on real zeros: count{(γ,γ′) : |(γ−γ′)·ρ| ≤ h} vs (1+h)TL | cnt/((1+h)TL) = 0.52–1.02 for h ∈ {0.25,…,5}; cnt/Poisson < 1 everywhere (0.46–0.59); cnt/PCC = 0.63–0.97 | (1.12)'s O((1+h)TL) bound holds with implied constant ≤ ~1.02 at these heights (measurement); the Fejér repulsion vs the uniform/Poisson count is present; at h ≥ 1 the count sits below the PCC prediction (finite-height effect, consistent with the Vf/GUE dip recorded in attack-gm-variance.md §5.4) |

All entries are sanity checks of statements quoted from the papers or consistency measurements on real zeros; none is a new theorem.

---

## 7. Honesty footer

- **VERIFIED-FROM-PAPER** (read in full, extractions /tmp/glss26.md, /tmp/glss25.md): every claim in §§0–3 about the papers' content — the title/topic of PCC II (AH, not heights); all quoted theorems, propositions, conjectures, formulas and ranges; the exhaustiveness of the unconditional inventory U1–U6; the absence of F(α)-beyond-1, prime-side, and third-moment content; the PCC ⟹ 100% route; the AH-Pairs/AH-Weak-Density conditional structure; the RH-conditional status of (1.14)–(1.15) (from BGSTB25a, cited); the Fujii error-term and vacuity structure at UL ≪ 1 (derived here from the quoted O(T√log(2+λ)) error vs (T/π²)log(2+λ) main term).
- **CHECKED NUMERICALLY** (this run; `research/notes/paper-pcc2/paper-pcc2-check.py`, command in §6): all §6 entries.
- **PROVEN / CHECKED as labeled in prior notes (quoted, not re-derived):** M29's negative (its script /tmp/prime-pairs, cited in attack-m29.md §2/§6); GM-variance's verdict (var_probe2.py, cited in attack-gm-variance.md §5); the bandwidth-one ceiling 0.6818 and the 0.70/0.80/0.90 ⟷ supports 1.04/1.26/1.70 roadmap (claude-riemann-paper Rem 1.1, PROVEN-as-stated, literature map §3); the (1/λ + λ/3) in-band moment and λ ≤ 1 essentiality (claude-riemann-paper §7.5(a), PROVEN, literature map §5).
- **CONJECTURED:** PCC itself; AH-Pairs; AH-Weak Density; any beyond-1 value of the form factor; the β > 1 variance asymptotic (equivalent to PCC, CCCM — cited from the GM-variance note); HL prime-pair input. Nothing in PCC I/II changes the conjectural status of any of these.
- **Conclusion label:** PCC II = **consistent-with, does-not-reopen** for both M29 (beyond-1 mean) and B10/GM-variance (beyond-1 variance). All beyond-1 statements remain conjectural from the pair-correlation side exactly as from the mean and variance sides.
- **Epistemic status (s4h-epistemology applied):** the question "does PCC II reopen any wall" is **settled** (NO) — it is not an open unknown but a documented read of the primary source; the reframed, answerable questions — "what exactly is unconditional in GLSS I/II" (U1–U6, in-band), "what is the exact PCC ⟹ 100% route" (§1.1), "does AH change the picture" (no: same conjecture-in/100%-out structure) — are answered above. **Strategy-intelligence applied:** the known/assumed split — *known*: the papers' statements (read); *assumed-and-now-corrected*: the memo's "arithmetic/height aspects" guess (wrong — AH paper); the operative strategic fact is unchanged: the only paths to a beyond-1 constant remain HL/PCC values (CONJECTURED) or the in-class 0.6725 → 0.6818 proven-inputs gap.
- **Sources:** glss26-2507.06823-pccII-ah.pdf (→ /tmp/glss26.md); glss25-2503.15449-pccI.pdf (→ /tmp/glss25.md); research/notes/attack-m29.md; research/notes/attack-gm-variance.md; research/notes/literature-map.md; research/notes/paper-finder-001.md; tools/data/zeros_computed_10000.txt.
- **Gap closed:** literature-map.md §5 listed GLSS25 as "cited-but-unread"; both GLSS papers are now read in full and this note is their program-side record.
