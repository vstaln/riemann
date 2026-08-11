# GM/Selberg-variance flank on the beyond-α=1 wall (B10) — bookkeeping + certificate-side verdict

**Agent:** EXECUTIONER. **Round:** 2 (crystallography/astronomy idea generator, vector B10). **Date:** 2026-08-11.
**Question:** M29 (PROVEN negative) killed the *mean* off-diagonal prime-pair sums at X = T^{1+ε}. B10 proposes a
*second functional* of the beyond-1 form factor — the zero-counting **variance** over windows (windowed integral of
F), which "Goldston–Montgomery / Selberg variance theorems control **unconditionally** where the mean (HL) is not
proven", with the mapping *window U at height T ↔ form-factor scale α = U/T*, "beyond-1 data = long windows U > T".
**Task:** (1) read M29 + held bibliography for GM/Selberg variance statements and extract their EXACT proven ranges;
(2) bookkeeping: the windowed counting variance in form-factor language, the exact α ↔ U dictionary; (3)
certificate-side: can any certificate variant USE a proven beyond-1 variance integral? (4) numerics on real zeros;
(5) write this note with honesty labels.

**Verdict (up front): DEAD as a route to reopen M29 — a documented confirmation of the wall from the variance side.
The variance flank fails on all three legs:**
1. **The dictionary is inverted.** For the zero-counting variance, the probe window in form-factor space is
   `sinc²(πα·Uρ)` (Parseval identity, Goldston notes (7.10)); window U probes F at **α ≲ 1/(Uρ)**, ρ = local density
   = (1/2π)log(T/2π). **Beyond-1 (α > 1) ⟺ SHORT windows U < 1/ρ** (≈ one mean spacing, U* = 0.929 at our T), NOT
   long windows. B10's `α = U/T` is off by a factor ~(T logT/U²) and in the wrong direction: **long windows U > T
   probe α ≈ 0 (deep in-band, the Selberg regime)** — and are empirically inoperative (U = αT exceeds the zero list
   at α ≥ 0.5). The variance theorems' *sharp* content (Selberg global; Fujii U ≤ 1; GM/CCCM β ≤ 1) is **confined to
   α ≲ 1**; at the true beyond-1 windows they are vacuous.
2. **No UNCONDITIONAL variance statement reaches beyond-1 with content.** The unconditional results: Selberg 1946
   (global moments, α ≈ 0), Fujii via GLSS25 Prop 2 (U ≤ 1, sharp at UL ≳ 1 = in-band, error-dominated/vacuous at
   UL ≪ 1 = beyond-1), Gallagher–Mueller via CCCM (1.2) (β ≤ 1, the trivial/diagonal regime). The β > 1 asymptotic
   (CCCM) is **equivalent to Montgomery's pair-correlation conjecture** — CONJECTURED; under RH there are only
   order-of-magnitude bounds (0.8376β vs 1.4283β — not the value F = 1). So the "variance proven where mean is not"
   premise is FALSE — the variance is conjectural in **exactly** the same regime as the mean.
3. **The variance is orthogonal to the certificate.** The word "variance" appears **zero** times in the main paper
   (claude-riemann-paper.txt). Every certificate inequality (rank–trace, ‖Â‖²_F = C·M/L², Prop 5.6's D + O₁ + O₂)
   reads **means** — off-diagonal prime-pair sums with 1/(y_n−y_m)·phase kernels. A variance statement bounds a
   *fluctuation functional* (sliding-window second moment of the zero/prime count) — a different quadratic form in
   the zeros — and the GM87 transfer from variance to pair-correlation runs through the SPC (conjectural). Even a
   PROVEN beyond-1 variance would not bound the certificate's mean pair sums. B10's kill criterion is met: "the
   vector is a documented confirmation of the wall from the variance side — still worth writing down."

---

## 1. Sources and what they hold (all held, all read for this note)

- **research/notes/attack-m29.md** — the model negative (bound table); tolerance bookkeeping: in-class gap
  0.0093 = 0.6818 − 0.6725 (paper Rem 1.1) ⇒ budget |O₁| ≤ 0.0093·(1+ε)N·L²/4; M29's proven-bound survey.
- **research/papers/goldston-2004-paircorr-notes.pdf** (Goldston, math/0412313; text extracted to /tmp/goldston-notes.md
  via `uvx markitdown`) — §9 "Equivalence between SPC and Primes" contains **GM87 Theorem 7**; §10 "Selberg's theory
  of S(T)" contains **Selberg's Theorem 8** (1946, unconditional even moments); §7 the Parseval identity (7.9)/(7.10).
- **research/papers/cccm-2108.09258-three-integrals.pdf** (Carneiro–Chandee–Chirre–Milinovich; extracted to
  /tmp/cccm.md) — the "Selberg prime-variance integral" J(β,T) = ∫₁^{T^β}(ψ(x+x/T)−ψ(x)−x/T)²dx/x², with (1.2)
  Gallagher–Mueller unconditional, (1.3) Selberg RH-conditional, (1.4)/(1.10) RH-conditional order bounds
  (0.8376β/1.4283β, Goldston–Gonek 0.307/21.647), Theorem 14 (the J ↔ ∫F dictionary), and the intro's statement
  that the conjectured asymptotics of all three integrals are **equivalent to Montgomery's PCC**.
- **research/papers/glss25-2503.15449-pccI.pdf** (Goldston–Lee–Schettler–Suriajaya; extracted to /tmp/glss25.md) —
  §5 "The Second Moment for Zeros in Short Intervals": Prop 1 (GM78) and **Prop 2 (Fujii, UNCONDITIONAL)**:
  ∫₀ᵀ(Δ_U S(t))²dt = (T/π²)log(2+UL) + O(T√log(2+UL)) for 0 < U ≤ 1.
- **research/papers/baluyot-etal-2306.04799.txt** (B24) — unconditional Montgomery theorem, F(α) ≈ 1 for 0 ≤ α ≤ 1
  only (range ends at α = 1; M29 §4 row).
- **research/papers/claude-riemann-paper.txt** — Prop 5.6 (M = D + O₁ + O₂), §7.5(a) (beyond-1 = prime-pair /
  pair-correlation-conjecture territory), Rem 1.1 (0.70/0.80/0.90 ↔ supports 1.04/1.26/1.70). **"variance": 0 hits.**
- **research/notes/paper-finder-001.md** — item #80 confirms goldston-2004 fetched; the CCCM entry flags
  "equivalence of three integrals (∫F(α,T)dα, Selberg's prime-variance integral, second moment of ζ′/ζ); under RH,
  substantially improved bounds".

No held paper contains a variance statement reaching beyond-1 **unconditionally**; the strongest unconditional
short-window statement is Fujii's (GLSS25 Prop 2), whose sharp range is in-band (see §3).

---

## 2. Bookkeeping: the windowed counting variance in form-factor language (the <1h probe)

**Setup (zero side).** N(t) counts zeros with 0 < γ ≤ t; N(t+U) − N(t) = mean + S(t+U) − S(t) + O(1), mean =
(1/2π)∫_t^{t+U} log(s/2π) ds, S = (1/π)arg ζ(1/2+it). The sliding-window second moment (GLSS25 Prop 1 (5.2)–(5.3),
Goldston notes (7.10)):

  V(U) := (1/T)∫_T^{2T} (N(t+U) − N(t) − mean)² dt = (1/T)Σ_{γ,γ'} (U − |γ−γ′|)_+ − (Uρ)² + O(U/T, ...)

with ρ = (1/2π)log(T/2π). The pair kernel (U − |γ−γ′|)_+ is the *triangular* window in γ-space, i.e. in normalized
spacing δ = (γ−γ′)·ρ it is (1 − |δ|/D)_+·U with **D = Uρ** spacings. Its Fourier transform (form-factor variable α,
r̂(α) = D·sinc²(παD), per the Parseval identity (7.10) of the notes) shows:

  **V(U) = (diagonal) + (U²ρ²/T)·∫_{−∞}^{∞} sinc²(πα·Uρ)·F(α) dα − (Uρ)²  (+ small).**

**The dictionary (zero side, the operative one):** the variance's probe of the form factor is the low-pass window
**sinc²(πα·Uρ)** — width **1/(Uρ) = 2π/(U·log(T/2π))** in α. Hence:
- window U ↔ form-factor scales **α ≲ 1/(Uρ)**; the fraction of probe weight at |α| > 1 is
  **1 − (2/π)∫₀^{πUρ} sinc²(u)du**;
- **beyond-1 (α > 1) ⟺ U < 1/ρ** (windows shorter than ~one mean spacing);
- **long windows U > T ⟺ α ≲ 1/(Tρ) ≈ 0** — deep in-band (the Selberg regime).

**B10's dictionary (α = U/T, "beyond-1 = U > T") is inverted**: it applies to the *mean*-side pair windows of M29
(X/T = T^ε in the log-window of the prime-pair sums), not to the variance. Empirically it is inoperative: at
T_ref = 5450, the B10 windows are U = α·T_ref = 2725…10899, i.e. up to ~1.1× the entire zero range [14, 9879]
(§5); at U > T the count variance is dominated by the t-drift of the mean (V_raw = 30 at U = 80, n = 86 spacings —
drift, not fluctuation).

**Prime side (for completeness; CCCM Theorem 14, quoted):** under RH, for β > b > 0,
L⁻·limliminf ∫_{b+ε}^{β−ε} F(α,τ)dα + o(1) ≤ (T/log²T)·(J(β,T) − J(b,T)) ≤ L⁺·limlimsup ∫_{b−ε}^{β+ε} F(α,τ)dα + o(1),
with L⁻ = 0.9028…, L⁺ = 1.0736… — the prime-variance integral over the position range [T^b, T^β] is (RH-)tied to
∫F over frequencies [b, β]. Under this dictionary, "β > 1" (positions x > T, prime windows h = x/T > 1) is the
beyond-1 regime — and every statement there is conditional or conjectural (§3 rows 4–6). Both dictionaries agree on
the operative conclusion: **no unconditional variance statement supplies beyond-1 content.**

---

## 3. Proven variance statements — the range table (each labeled)

| # | Statement (verbatim-in-spirit, held source) | Window range | α-regime | Label |
|---|---|---|---|---|
| 1 | Selberg 1946: ∫₀ᵀ\|S(t)\|^{2k}dt = (2k)!/(k!(2π)^{2k})·T(loglogT)^k + O_k(T(loglogT)^{k−1/2}); proven on (T,T+H], T^a ≤ H ≤ T, a > 1/2 (Goldston notes §10, Theorem 8) | global / H ≥ T^{1/2+ε} | α ≈ 0 | **PROVEN, UNCONDITIONAL** |
| 2 | Fujii (via GLSS25 Prop 2): ∫₀ᵀ(Δ_U S(t))²dt = (T/π²)log(2+UL) + O(T√log(2+UL)), 0 < U ≤ 1 | U ≤ 1 (t-units) | sharp at UL ≳ 1 (α ≲ 1, incl. the α ≈ 1 boundary); **vacuous at UL ≪ 1 (α > 1: error O(√log2) ≈ 0.83 dominates the main term ≈ 0.07)** | **PROVEN, UNCONDITIONAL** (sharp content in-band) |
| 3 | Gallagher–Mueller (via CCCM (1.2)): J(β,T) ~ β²log²T/(2T) for 0 ≤ β ≤ 1 | x ≤ T, prime windows h = x/T ≤ 1 | β ≤ 1 = in-band / trivial-diagonal regime (the answer equals the diagonal; no pair-correlation content) | **PROVEN, UNCONDITIONAL** |
| 4 | GM87 Theorem 7 (Goldston notes §9): I(x,δ) := ∫₁ˣ(ψ((1+δ)x)−ψ(x)−δx)²dx ~ (1/2)δX²log(1/δ), X^{−B₂} ≤ δ ≤ X^{−B₁} ⟺ F(x,T) ~ (T/2π)logT on X^{B₁}log⁻³x ≤ T ≤ X^{B₂}log³x; (9.3): **on RH, SPC ⟺** ∫(ψ(x+h)−ψ(x)−h)²dx ~ hXlog(X/h), 1 ≤ h ≤ X^{1−ε} | h up to X^{1−ε} (prime) | all α — but the *asymptotic* is **equivalent to the Strong Pair Correlation Conjecture** | **RH-CONDITIONAL; the variance asymptotic itself = CONJECTURED** (equivalent to PCC) |
| 5 | Selberg (via CCCM (1.3)): J(β,T) = O(βlog²T/T), 1 < β ≤ 4 | β > 1 (beyond-1 in the CCCM dictionary) | α ∈ (1, 4] | **RH-CONDITIONAL** upper bound only |
| 6 | Goldston–Gonek + CCCM (1.4)/(1.10), Cor 4: under RH, 0.8376β(1+o(1))·log²T/T ≤ J(β,T) ≤ 1.4283β(1+o(1))·log²T/T (β > 1); GG: 0.307·log²T/T ≤ J(b+2,T)−J(b,T) ≤ 21.647·log²T/T | β > 1 | α ∈ (1, β] | **RH-CONDITIONAL, order-of-magnitude bounds only** (not the value F = 1) |
| 7 | "The conjectured asymptotic for any of these three integrals is equivalent to Montgomery's pair correlation conjecture" (CCCM intro; line (1.5) (III): J(β,T) ~ β·log²T/T·(L±-weighted)) | β > 1 | α > 1 | **CONJECTURED** (equivalent to PCC) |
| 8 | B24 (baluyot) unconditional Montgomery: F(α) ≈ 1 for 0 ≤ α ≤ 1 only; nothing for α > 1 (M29 §4) | — | 0 ≤ α ≤ 1 | **PROVEN-as-stated; range ends at α = 1** |

**Answer to the task's question "does ANY proven variance statement reach U > T / α > 1?":**
- U > T (B10's dictionary): trivially "reached" by Selberg/Fujii (long windows = α ≈ 0) — but that is **in-band**,
  exactly the data the certificate already has; it is not a beyond-1 statement.
- α > 1 (correct dictionary, short windows U < 1/ρ): **no UNCONDITIONAL statement with content.** Fujii's U ≤ 1
  theorem covers the α ≈ 1 boundary but is vacuous beyond (error term dominates); GM87's asymptotic is
  RH-conditional and equivalent to SPC (conjectured); the only beyond-1 statements (rows 5–6) are RH-conditional
  *order* bounds (log²T/T-scale), not values — they do not even provide the F(α) = 1 datum M29 showed would be
  required. The variance is conjectural **in exactly the same regime as the mean** — B10's "proven where mean is
  not" premise is FALSE.

---

## 4. Certificate-side bookkeeping: usable flank or orthogonal?

**Verdict: ORTHOGONAL — the variance cannot be a certificate input, even if proven.**
1. **The certificate reads means only.** The rank–trace inequality reads ‖Â‖²_F = C·M/L² with M = M[P_X, P_X] =
   D + O₁ + O₂ (paper Prop 5.6); O₁ is the *mean* off-diagonal prime-pair sum with kernel 1/(y_n − y_m) and phases;
   the tolerance is |O₁| ≤ 0.0093·(1+ε)N·L²/4 (M29 §1). The word "variance" occurs **0 times** in the main paper.
   There is no certificate inequality in the paper (or any variant we hold) whose left-hand side is a sliding-window
   second moment of the zero count.
2. **Variance ≠ the certificate's quadratic form.** The variance V(U) = Σ_{γ,γ′}(U−|γ−γ′|)_+/T − mean² is a
   *fluctuation* functional of the zero configuration; the certificate's M is a *mean* over prime pairs with a
   different (1/Δy·phase) kernel. The only bridge from the prime variance to the pair correlation is GM87's
   equivalence, which runs **through the SPC (conjectural)** — so even a proven variance could not be transported to
   the certificate's O₁ bound without a conjectural step.
3. **The variance-type certificate variants do not need beyond-1 input.** [P9.1] (idea-generator-physics.md §P9.1)
   is a *finite-T* diagnostic: it uses the variance of the certificate value Δ(T) over T-windows (whose covariance
   is the *in-band* F on [0,1] — "the pair correlation IS the covariance", P9.2) to target an **almost-everywhere
   0.6725 certificate** (the in-class value). It does not feed a beyond-1 integral into any inequality. The
   two-moment class's "variance analog" is not defined in any note; the two-moment MT certificate itself is a mean
   object. B10's assertion that "[P9.1]'s a.s.-certificate … would use a proven beyond-1-integral input" is **not
   supported by P9.1's own text** (its input is in-band; its target is in-class 0.6725).
4. **Even a hypothetical proven beyond-1 variance** would bound a *weighted low-pass* integral of F (weight
   sinc²(πα·Uρ): at U = one spacing only ≈ 10% of the weight is at α > 1; at U = 0.5 spacings ≈ 23%) — a
   fluctuation bound, not a constraint on the mean pair sums the rank–trace inequality needs.

So B10 is an *interesting-but-unusable* fact: the bookkeeping is real (the variance IS a second functional of the
beyond-1 form factor, with a computable, empirical dictionary), but it cannot feed any certificate, and no proven
statement supplies its beyond-1 content anyway.

---

## 5. Numerics (all CHECKED NUMERICALLY, script + command cited)

**Script:** research/notes/attack-gm-variance/var_probe2.py (final; probe v1 var_probe.py also kept).
**Command:** `cd /home/vstaln/riemann/research/notes/attack-gm-variance && timeout 300 uv run --with numpy python var_probe2.py`
**Data:** tools/data/zeros_computed_10000.txt (10k zeros, γ ∈ [14.135, 9879.037]). Sliding windows t ∈ [2000, γ_N−U−10],
M = 4000 starts; V_fluct = mean over t of (N(t+U) − N(t) − exact-mean)² with the exact mean
(1/2π)[(t+U)(log((t+U)/2π)−1) − t(log(t/2π)−1)]; ρ_avg = 1.0767 (so α = 1 boundary U* = 1/ρ = 0.929); GUE prediction
(1/π²)(log(2πn)+1+γ), n = Uρ; Fujii leading term (1/π²)log(2+n); beyond1_wgt = probe weight at |α| > 1.

**Corrected-dictionary windows U = 1/(αρ), α ∈ {0.5, 0.9, 1.1, 1.5, 2.0}:**

| α | U | n = Uρ | V_fluct | GUE | Vf/GUE | Fujii-lead | Poisson | beyond1_wgt |
|---|---|---|---|---|---|---|---|---|
| 0.50 | 1.857 | 2.000 | 0.3775 | 0.4163 | 0.907 | 0.1405 | 2.000 | 0.050 |
| 0.90 | 1.032 | 1.111 | 0.3285 | 0.3567 | 0.921 | 0.1150 | 1.111 | 0.096 |
| 1.10 | 0.844 | 0.909 | 0.3087 | 0.3364 | 0.918 | 0.1082 | 0.909 | 0.098 |
| 1.50 | 0.619 | 0.667 | 0.2956 | 0.3049 | 0.969 | 0.0994 | 0.667 | 0.133 |
| 2.00 | 0.464 | 0.500 | 0.2758 | 0.2758 | 1.000 | 0.0928 | 0.500 | 0.226 |

**Readings (all CHECKED NUMERICALLY, this run):**
1. At the corrected windows the empirical variance matches GUE-with-constant to 0.91–1.00 (Vf/GUE = 0.907–1.000);
   the empirical boundary value V_fluct(U*) = 0.315 at U* = 0.929 (GUE(1) = 0.346). This is the well-known empirical
   rigidity (sub-Poisson: Poisson V = n is 1.8–5.3× larger) — i.e., **empirically** the beyond-1 F ≈ 1 content shows up
   in the short-window variance exactly as PCC predicts — but this is a MEASUREMENT, not a theorem.
2. **Fujii's unconditional leading term (1/π²)log(2+n) sits 2–3× below the data at these heights** (0.093–0.141 vs
   V_fluct 0.276–0.378): at T ~ 5000 the constant term matters; Fujii is a leading-order statement (error
   O(√log(2+n)) per window). Honest: the unconditional theorem's sharp content (UL ≳ 1) is in-band; at the beyond-1
   windows it is vacuous (§3 row 2).
3. **The dictionary is verified empirically**: the variance is O(1)-and-GUE-like at short windows (n ≤ ~2, where the
   probe weight crosses α = 1), stays O(1)-sub-Poisson across all n up to 86, and its raw form becomes drift-dominated
   at large U (V_raw = 30 at U = 80 vs fluctuation 0.35). B10's windows U = α·T_ref = 2725–10899 exceed the data
   range (α ≥ 1.5) or span the whole range (α = 0.5–1.1) — inoperative; and at U > T the count variance is the
   global-drift/Selberg quantity (α ≈ 0), not a beyond-1 probe.
4. Side observation (measured, low-T): Vf/GUE dips to 0.44–0.57 at intermediate windows n = 8–86 — the empirical
   number variance on 10k zeros at heights 2000–9879 is *below* the GUE asymptotic there. Reported as a measurement
   (consistent with known small-T effects in Odlyzko-type data); not a theorem, not needed for the verdict.

---

## 6. Bottom line

**DEAD as a route to reopen M29's negative — documented confirmation of the wall from the variance side.** Exact
reasons:
1. **Dictionary inverted (PROVEN, algebra + numerics):** window U probes F at α ≲ 2π/(U·log(T/2π)); beyond-1 =
   short windows U < 1/ρ ≈ 0.93 at our heights. B10's α = U/T and "beyond-1 = U > T" are wrong; long windows probe
   α ≈ 0 (the Selberg regime), and U = αT exceeds the zero list already at α = 0.5.
2. **No unconditional variance statement reaches beyond-1 with content (PROVEN-as-reported, held sources):** Selberg
   1946 (global, α ≈ 0), Fujii U ≤ 1 (sharp in-band, vacuous beyond), GM78 β ≤ 1 (trivial/diagonal). The β > 1
   variance asymptotic is **equivalent to the pair-correlation conjecture** (CCCM) — CONJECTURED; under RH only
   order-of-magnitude bounds (0.8376β/1.4283β) exist. The "variance proven where the mean is not" premise is false.
3. **Orthogonal to the certificate (PROVEN, text of the paper + P9.1):** the certificate reads means (M = D + O₁ + O₂,
   off-diagonal prime-pair sums); "variance" appears 0 times in the paper; no certificate variant (including [P9.1]'s
   a.e.-certificate, whose variance input is in-band and whose target is the in-class 0.6725) uses a beyond-1 variance
   integral. Even a proven beyond-1 variance would bound fluctuations, not the mean pair sums the rank–trace
   inequality needs.

**Consequences (validated, not changed):** M29's negative stands (PROVEN). The bandwidth-one ceiling 0.6818 and the
roadmap 0.70/0.80/0.90 → supports 1.04/1.26/1.70 (paper Rem 1.1) stand; beyond-1 constants remain conjectural-input
territory from the variance side exactly as from the mean side. The one *new* recorded fact of value: the empirical
short-window variance curve (§5) is a clean, scripted GUE-consistent measurement of the beyond-1-weighted fluctuation
functional — a diagnostic for the program's empirical P3 dossier, and the two unconditional variance theorems (Selberg,
Fujii) are now inventoried with their exact ranges in our literature map. No escalation.

---

## 7. Honesty footer

- **PROVEN (algebra, this note):** the Parseval dictionary (window U ↔ probe sinc²(πα·Uρ), width 2π/(U·log(T/2π));
  beyond-1 ⟺ U < 1/ρ), from Goldston notes (7.10)/GLSS25 Prop 1 (5.3); the certificate-side orthogonality argument
  (paper reads means; "variance" 0 hits in claude-riemann-paper.txt; P9.1's input is in-band).
- **PROVEN-as-reported (held sources, quoted):** Selberg 1946 moments (Goldston notes §10 Thm 8); Fujii (GLSS25 Prop 2);
  GM78 β ≤ 1 (CCCM (1.2)); GM87 Theorem 7 / SPC equivalence (Goldston notes §9); CCCM (1.3),(1.4),(1.10), Theorem 3/4,
  Cor 15, Theorem 14, L± = 0.9028…/1.0736…; B24 range 0 ≤ α ≤ 1 (baluyot-etal txt; M29 §4).
- **CHECKED NUMERICALLY (this run; research/notes/attack-gm-variance/var_probe2.py, command in §5):** all entries of
  the §5 tables; the boundary U* = 0.929; the B10-window inoperativity (U = αT_ref = 2725–10899 vs zero range
  [14, 9879]); the Fujii-vs-data gap (2–3×); the Vf/GUE dip at n = 8–86 (measured, low-T).
- **CONJECTURED:** any beyond-1 variance value (equivalent to PCC per CCCM); the transfer of the measured short-window
  GUE-match to a theorem; the GUE number-variance formula as a statement about the zeros (proven for GUE matrices,
  conjectural for ζ).
- **DEAD:** B10 as a certificate-input flank (reasons §6). Not reopened by any held source.
- Sources: research/papers/claude-riemann-paper.txt (Prop 5.6, §7.5(a), Rem 1.1); goldston-2004-paircorr-notes.pdf
  (extracted /tmp/goldston-notes.md); cccm-2108.09258-three-integrals.pdf (extracted /tmp/cccm.md);
  glss25-2503.15449-pccI.pdf (extracted /tmp/glss25.md); baluyot-etal-2306.04799.txt; attack-m29.md;
  idea-generator-physics.md §P9.1/P9.2; idea-generator-crystallography.md §B10/TOP-10/strategic-reading.
- Epistemology note (s4h-epistemology-limits applied): the question "does any proven variance statement reach α > 1"
  is **settled** (no, unconditionally; conditional order-bounds only) — it is not an "unknown yet" but a documented
  inventory from held sources; the reframed, answerable question — "which windows does the variance probe, what is
  the empirical curve, and can the certificate use it" — is answered above (α ≲ 1/(Uρ); GUE-consistent data;
  no). Constraint-hardness note (s4h-constraint-hardness-testing applied): B10's two operative constraints —
  "variance theorems are proven where means are not" and "beyond-1 = long windows" — were **tested**; the first is
  an **assumed** constraint (variance asymptotics are PCC-equivalent), the second is **wrong** (inverted dictionary).
