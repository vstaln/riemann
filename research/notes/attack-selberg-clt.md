# Attack: V13 — Selberg-CLT / distributional certificate (exclude the 256-law by fluctuations)

**Agent:** EXECUTIONER (epistemology + strategy + constraint-hardness lenses; s4h applied: s4h-strategy-terrain — pick the terrain, s4h-epistemology-limits — what kind of knowing the fluctuation content even is, s4h-probability — base rate of the "distributional certificate" idea class)
**Round:** 3 (V13 is the last Tier-2 vector, catalog row 24: "do not fund" — this note executes the kill-or-keep decision with a precise reason)
**Sources read:** hooks/agents.md; idea-generator-crossdomain.md §V13; attack-ceiling.md (§1 ceiling structure, §3 beyond-1 wall, §4 strategy); attack-lpdual.md (§5 missing-constraint analysis, shadow price of p₁ = 1); attack-gm-variance.md (the variance dictionary + orthogonality verdict); attack-vector-catalog.md (row 24, funding status); papers/claude-riemann-paper.txt; papers/goldston-2004-paircorr-notes.pdf §10 (Selberg Thm 8, held, extracted /tmp/goldston-notes.md per gm-variance).

**Verdict up front: DEAD-consistent-with-walls.** The proposed distributional certificate cannot exist, for a reason that is now sharper than the two prior walls put together:

1. **YES, an unconditional fluctuation statement distinguishes the real zeros from the periodic 256-law** — Selberg 1946 (unconditional): E[S(t)²] ~ (1/2π²)·log log t → ∞, so the real zeros' count-fluctuation functional is unbounded with scale √(log log t); the 256-law's is a bounded periodic function, forever. (PROVEN-as-reported, held source; empirically visible, CHECKED NUMERICALLY here, §5.)
2. **NO, it cannot enter any certificate inequality — two independent reasons, either sufficient:**
   - **Leg 1 (orthogonality, prior wall):** the certificate reads means; every inequality of the class (rank–trace, stability, ceiling; the paper's Prop 5.6 M = D + O₁ + O₂) is a deterministic inequality in the grid rows and the simple fraction. "Variance": **0 hits** in the paper. A fluctuation input would require a genuinely new inequality whose left-hand side is a fluctuation functional — no such inequality exists or is suggested by any held source. (PROVEN-as-absence.)
   - **Leg 2 (class robustness — the NEW analysis of this note):** even granting a *new* certificate class whose validity hypothesis includes any fluctuation input the real zeros provably satisfy (Selberg CLT shape, √(log log t) scale with any constant, Θ(T log log T) mean square), the class still contains configurations with simple fraction **exactly p₀ = 0.6818287** and spectral discrepancy **converging to the 256-law's razor** (|E(1)| → 2.543·10⁻⁶, M → 2.543·10⁻⁶). Construction: super-blocks of the 256-law with exponentially growing lengths and independent random phases (§4). The ceiling argument runs identically against these siblings: v ≤ p₀ + 2.543·10⁻⁶(|r′(1)| + ∫|r″|) + o(1), boxed to **p₀ + |E(1)| + o(1) = 0.68183123 + o(1)**. A fluctuation input moves nothing. (PROVEN-by-construction, elementary.)
3. **The deeper reason (the crux, stated once):** the certificate's value is a universal quantifier over a class defined by *low-order, finite-T inputs* (density, bandwidth-one rows, marks). The fluctuation content is a *different object* — an asymptotic, distributional statistic of the *specific* zero configuration (S(t) at T → ∞). Distinguishing statements about a specific configuration cannot enter a validity hypothesis that quantifies over all configurations — and any sub-class they define still contains the p₀-siblings. Not an inequality problem; an object-type mismatch plus a class-robustness failure.

**Bottom line:** do not fund V13. The in-class optimum 0.68183123 stands; the fluctuation flank is closed on both sides. The one durable output of this note beyond the verdict: the 256-law is *not an isolated extremal configuration* — it is one member of a family of p₀-simple-fraction, near-CUE-row configurations parameterized by an arbitrary sublinear fluctuation profile — so any future "rule out the extremal law" input must rule out the whole family, which is strictly harder than the already-unknown "rule out the 256-law".

---

## 1. The proposed certificate, stated precisely (then refuted)

**Statistic read (as V13 proposes).** The normalized count discrepancy over a window: N(t+U) − N(t) − mean, or its global version S(t) = N(t) − [(t/2π)log(t/2π) − t/2π + 7/8]. For the real zeros (Selberg 1946, unconditional, held via Goldston notes §10 Thm 8, k = 1):

  E[S(t)²] ~ (1/2π²)·log log t,   and   ∫₀ᵀ S(t)² dt = (T/2π²)·log log T·(1 + o(1)).

So the real zeros' S is unbounded in mean square with scale √(log log t), and S(t)/√((1/2π²)log log t) → N(0,1) (Selberg CLT, unconditional; the variance of log|ζ(1/2+it)| itself is (1/2)log log t — the (1/2π²) is for S(t) = (1/π) arg ζ, matching Goldston's moment formula). The 256-periodic law's S(t) is a bounded periodic function — O(1) forever.

**Inequality proposed (the V13 mechanism).** A certificate reading "the configuration is NOT the extremal law" would take the form: a new theorem

  simple-on-line(X) ≥ c₀ + Σⱼ sⱼ^X r(j/N) + G(F(X))   for all X with fluctuation statistic F(X) ∈ 𝒮,

where the actual zeros are in the class (F(real zeros) ∈ 𝒮, PROVEN by Selberg) and the 256-law is excluded (F(law) ∉ 𝒮). Then the certificate's value could exceed p₀ because validity is no longer required against the law.

**Why this exact object fails — the two legs.**

---

## 2. Leg 1 — orthogonality (the paper's class; PROVEN-as-absence)

The rank–trace / Weil-quadratic-form method bounds the simple on-line fraction from below by a specific *mean* quadratic form in the zeros: the off-diagonal prime-pair sums with 1/(y_n − y_m)·phase kernels (paper Prop 5.6: M = D + O₁ + O₂). The stability identity (Lean `abel_ibp_second`, PROVEN) is configuration-free and reads the *cumulative spectral measure* (D, E). The ceiling (`ceiling_law256_signed`, PROVEN Lean) is a bound on the certificate value v = c₀ + ∫₀¹ rx using the law's D, E, M. **The word "variance" occurs 0 times in the main paper** (checked: `grep -c variance claude-riemann-paper.txt` = 0). There is no inequality in the class whose left-hand side is a sliding-window second moment, an S(t) statistic, or any fluctuation functional (attack-gm-variance §4.1–4.3, PROVEN for the paper's class). A "distributional certificate" would require a *new inequality type* — a proven lower bound on the simple fraction in terms of fluctuation functionals. No held source contains one, and the rank–trace mechanism produces no such bound. (Label: absence documented PROVEN as to the text; the claim "no such inequality exists in mathematics" is beyond our sources — mark CONJECTURED-as-absent, i.e., not refuted but no mechanism found.)

---

## 3. Leg 2 — the class is robust to ANY fluctuation input (NEW analysis, PROVEN-by-construction)

Grant, hypothetically, a new certificate class whose validity hypothesis includes a fluctuation input: the theorem holds for configurations X with F(X) ∈ 𝒮, where 𝒮 is *any* statement the real zeros provably satisfy and the 256-law provably fails. Candidates (all PROVEN for the real zeros, unconditional):
- (a) "S is unbounded in mean square": ∫₀ᵀ S² dt = Θ(T log log T) (Selberg 1946).
- (b) "Selberg-CLT shape": S(t)/σ(t) → N(0,1) over t, σ(t) = c·√(log log t) for the specific constant c (Selberg 1946).
- (c) any monotone subfamily of these (e.g., only the lower-bound direction).

**Sibling construction X**(phase-randomized super-block law)**: partition [0,T] into super-blocks B_k of t-length L_k = 2^{2^k}·P(t_k) where P(t_k) = 256/ρ(t_k) is the 256-law's period at the local density ρ(t_k) ≈ (1/2π)log(t_k/2π), and B_k is a 256-periodic marked configuration (the 256-law scaled to density ρ(t_k)) with an *independent uniform random phase φ_k*. Properties (each elementary, one-line):

1. **Density 1:** each B_k is the 256-law at local density ρ(t_k); matches the smooth mean to O(1) per block. (PROVEN-by-construction.)
2. **Marks ≤ 2:** the law's marks are in {1,2}. (PROVEN-by-construction.)
3. **Simple fraction → p₀ = 0.6818287:** the simple fraction of a 256-law block is translation-invariant, so the whole configuration's simple fraction is p₀ (up to O(K/N) boundary effects, K = #super-blocks = o(N)). (PROVEN-by-construction.)
4. **Rows → the law's razor:** the pair correlation at distance j/256 spacings (j = 1..255) within a block equals the law's value (phase-invariant); cross-super-block pairs at distance ≤ 1 spacing occur only at the O(K) block boundaries — O(K) pairs vs N = Θ(T log T) total — negligible. Hence the grid rows and the cumulative discrepancy converge to the law's: D(1) → 0.82395316, E(1) → −2.5431315104·10⁻⁶, M = sup|E| → 2.5431315104·10⁻⁶. (PROVEN-by-construction + standard LLN for the phase averaging.)
5. **Fluctuation input satisfied, for every 𝒮 in (a)–(c):** with K(t) ≈ log log t super-blocks below t and i.i.d. bounded O(1) phase contributions, S(t) = Σ_{k<K(t)} ε_k, ε_k i.i.d. bounded. The classical CLT gives S(t)/√(Var·K(t)) → N(0,1); the variance constant is tunable by the phase distribution — match Selberg's c exactly. Mean square: ∫₀ᵀ S² dt ~ c²·T·log log T. (PROVEN-by-construction; classical CLT.)

**The ceiling runs identically against X\*.** Validity holds at X\* because the certificate's validity hypothesis is universal — it must hold for every configuration (attack-ceiling.md §1; attack-lpdual.md §1). The configuration-free stability identity then gives

  v = c₀ + ∫₀¹ rx ≤ p₁^{X\*} + |r(1)|·|D^{X\*}(1)| + |r′(1)|·|E^{X\*}(1)| + M^{X\*}·∫₀¹|r″|  →  p₀ + 2.543·10⁻⁶·(|r′(1)| + ∫₀¹|r″|) + o(1),

and with r(1) = 0 and the window-kernel box |r| ≤ 1 (the LP's boxed optimum): **v ≤ p₀ + |E(1)| + o(1) = 0.68183123 + o(1)** — the same boxed ceiling the law already imposes (attack-lpdual §3, CHECKED NUMERICALLY to 5·10⁻⁹). **A fluctuation input cannot move the constant, not by 10⁻³, not by o(1).** (PROVEN-by-construction.)

**Why the sibling cannot be excluded by any stronger proven input.** The proven fluctuation content for the real zeros is exhausted by (a)–(c) (Selberg moments/CLT; the beyond-1 variance content is PCC-equivalent, attack-gm-variance §3 rows 4–7). Each of (a)–(c) is satisfied by X\* with a tunable constant. Any *unproven* stronger input (e.g., a specific joint law of S across scales, the exact value distribution of the real zeros' S beyond the CLT) is CONJECTURED for the real zeros and cannot serve as a certificate hypothesis. So no proven input separates the class below p₀.

---

## 4. The sharp question, answered precisely

**Q:** Is there ANY known unconditional fluctuation statement that DISTINGUISHES the real zeros from the periodic 256-law (variance 0)?

**A (first half — YES):** Selberg 1946 (unconditional, held): E[S(t)²] ~ (1/2π²)log log t → ∞; the 256-law's S is bounded (periodic). Empirically visible at our heights (CHECKED NUMERICALLY, §5): the real zeros' S(t) over t ∈ [2000, 9000] ranges over ≈ 5 units (max |S| ≈ 2.43), RMS 1.15 — vs the exact-periodic value 0. The distinction is real and unconditional.

**A (second half — NO, it cannot enter any inequality of the certificate type):** three independent obstructions:
1. **Object-type mismatch:** the certificate is a finite, per-T, deterministic inequality; the distinguishing content is an *asymptotic, distributional* statistic of the *specific* configuration (bounded vs √(log log t) growth). At every fixed T both configurations' S is O(1) — the distinction is invisible at finite T, so no finite-T certificate inequality can read it. Its deterministic shadow (the mean square Θ(T log log T)) is a property of the specific zeros, and the certificate's validity hypothesis quantifies over a class.
2. **Class robustness (Leg 2):** any sub-class defined by a fluctuation input still contains X\* (p₀, razor rows, input satisfied) → ceiling v ≤ p₀ + |E(1)| + o(1) survives.
3. **In-band determination (the V13 kill criterion itself):** the *variance* (windowed second moment) is, at leading order, determined by F near 0 (Parseval dictionary: window U probes F at α ≲ 1/(Uρ); long windows = Selberg regime, in-band — attack-gm-variance §2). The 256-law matches in-band F ≡ 1 (its near-CUE property), so the leading variance CANNOT distinguish the law from the real zeros. The beyond-1 part (short windows) is PCC-equivalent — CONJECTURED. The distributional *shape* is the only remaining distinguisher, and it is the wrong object (obstruction 1) and matched by X\* (obstruction 2).

**Which step would need to change (the honest negative):** the certificate's validity hypothesis would have to become "valid against all configurations with F(X) ∈ 𝒮" and the rank–trace theorem would need a new term G(F(X)) provably ≥ 0 on the real zeros and > 0 against the law. Step 1 (the theorem with G) does not exist — there is no proven inequality connecting the simple on-line count to S(t)/variance/CLT (Leg 1). Step 2 (shrinking the class) fails — the class still contains X\* (Leg 2). And the input itself (Selberg CLT) is a limit statement, not a finite-T inequality (object-type mismatch). The fluctuation statistic is a *different object* — a statistic of the specific zero set at infinity — and no amount of it feeds a per-T universal certificate.

---

## 5. Numerics (CHECKED NUMERICALLY)

**Script:** research/notes/attack-selberg-clt/s_probe.py
**Command:** `cd /home/vstaln/riemann/research/notes/attack-selberg-clt && timeout 120 uv run --quiet --with numpy python s_probe.py`
**Data:** tools/data/zeros_computed_10000.txt (10k zeros, γ ∈ [14.135, 9879.037]).
**Statistic:** S(t) = N(t) − [(t/2π)log(t/2π) − t/2π + 7/8] (Titchmarsh 9.4 form).

| t | S(t) | √((1/2π²)log log t) |
|---|---|---|
| 2000 | +0.007 | 0.321 |
| 4000 | −0.382 | 0.327 |
| 6000 | −0.327 | 0.331 |
| 8000 | −2.432 | 0.334 |
| 9000 | −1.838 | 0.335 |

RMS of S(t) over t ∈ [2000, 9000] (1401-point grid): **1.150**; Selberg leading-order prediction: 0.330 (ratio 3.5).

**Readings (all CHECKED NUMERICALLY, this run):**
1. The fluctuation statistic is present and O(1)-scale with excursions up to |S| ≈ 2.4 — 3+ orders of magnitude above the exact-periodic value 0. The qualitative distinction (fluctuating vs bounded-periodic) is robust.
2. The *scale* is NOT the Selberg leading order at these heights: RMS 1.15 vs 0.33 (mean square ratio ≈ 11.8). This is the known slow convergence of the Selberg asymptotic at log log t ≈ 2 (the (1/2π²)log log t term is 0.11; the O(1) constant dominates). Honest: the empirical data is consistent with the *existence* of the fluctuation, not with a verified Selberg *constant* at low height. The argument in §3 does not depend on the constant.
3. The asymptotic-vs-finite-T point is visible directly: at any fixed height both configurations have O(1) S; only the growth to ∞ (asymptotic) separates them.

No further numerics are run: the §3 sibling construction is an asymptotic limit argument (K(T) ≈ 2 super-blocks at T = 10⁴ — a finite-T check of the CLT-shape is not meaningful at available heights), and its claims are elementary (PROVEN-by-construction).

---

## 6. Verdict and strategic record

**Verdict: DEAD-consistent-with-walls.** V13's mechanism fails on all three obstructions (§4). Consistent with — and strictly sharper than — the two prior walls: attack-gm-variance (the variance is orthogonal to the certificate class, PROVEN) and attack-lpdual (in-class optimum 0.68183123, shadow price of p₁ = 1, no missing constraint inside the class, PROVEN numerically to 5·10⁻⁹). This note adds the *class-robustness* leg: even a hypothetical new class reading fluctuations is capped at p₀ + |E(1)| + o(1) because the p₀-family (§3) realizes every proven fluctuation input.

**Durable output 1 — the p₀-family (the one new mathematical fact):** the 256-law is not an isolated extremal; there is a family of configurations {density 1, marks ≤ 2, near-CUE rows → razor, simple fraction exactly p₀ = 0.6818287} parameterized by an arbitrary sublinear fluctuation profile (bounded / √(log log t) / anything slower than √T, via block-length and phase distributions). Consequence for the record (attack-ceiling §4 / attack-lpdual §5): the already-unknown input "rule out the 256-law" is *insufficient even in principle* — any future multiplicity/shape input must rule out the whole family, and the family's freedom makes that equivalent to proving the real zeros' simple fraction exceeds p₀, which is circular. This hardens the ceiling.

**Durable output 2 — the epistemic classification (s4h-epistemology-limits):** the question "can a fluctuation statistic distinguish the zeros from the law?" has two halves with different epistemic status: (i) "does a distinguishing statement exist?" — SETTLED YES (Selberg 1946, PROVEN); (ii) "can it enter a certificate inequality?" — SETTLED NO (object-type mismatch + class robustness, PROVEN-by-construction). The reframed answerable question — "what does the fluctuation statistic of the real zeros actually do at our heights, and what is its beyond-1-weighted part?" — is answered empirically in §5 and in attack-gm-variance §5 (GUE-consistent short-window variance, measured). No escalation.

**Keep/kill decision: KILL (do not fund).** Catalog row 24's "do not fund" is confirmed with the precise reason now documented. Re-funding conditions (would reopen): a *proven* bound on F(α) for some α > 1 (beyond-bandwidth-1 pair correlation — CONJECTURED, attack-ceiling §3), or a proven inequality of a genuinely new type connecting the simple on-line count to a new functional. Neither exists in the held sources.

---

## 7. Honesty labels

| Claim | Label | Source |
|---|---|---|
| Selberg 1946 moments of S: E\|S\|^{2k} ~ (2k)!/(k!(2π)^{2k})·(log log T)^k, k = 1: E[S²] ~ (1/2π²)log log T → ∞ | **PROVEN-as-reported** (unconditional; held) | goldston-2004-paircorr-notes.pdf §10 Thm 8 (via gm-variance §3 row 1) |
| Selberg CLT: S(t)/√((1/2π²)log log t) → N(0,1) in distribution over t | **PROVEN-as-reported** (unconditional; standard, implied by the moments) | Selberg 1946 (as reported in held sources) |
| 256-law's S is bounded (periodic): "long-interval count variance O(1)" | **PROVEN** (a periodic configuration's count deviation is a bounded periodic function) | elementary; V13 text |
| "variance": 0 hits in the main paper; certificate inequalities read means | **PROVEN** (grep) + attack-gm-variance §4 | claude-riemann-paper.txt; gm-variance.md |
| Ceiling: v ≤ p₀ + 2.543·10⁻⁶(|r′(1)| + ∫\|r″\|); boxed v ≤ p₀ + \|E(1)\| = 0.68183123 | **PROVEN (Lean)** bound; **CHECKED NUMERICALLY** (LP to 5·10⁻⁹) | attack-ceiling.md; attack-lpdual.md §3 |
| Sibling family X\*: density 1, marks ≤ 2, p₁ → p₀, rows/D/E/M → the law's razor, any sublinear fluctuation profile incl. Selberg-CLT shape with tunable constant | **PROVEN-by-construction** (elementary; each property one line; classical CLT for i.i.d. bounded summands; finite-T numeric check not meaningful at 10⁴ zeros — K(T) ≈ 2 blocks) | this note §3 |
| v ≤ p₀ + \|E(1)\| + o(1) for any certificate class with any fluctuation input the real zeros provably satisfy | **PROVEN-by-construction** (consequence of the above + the configuration-free stability identity, itself PROVEN in Lean) | this note §3 |
| Empirical S(t) table + RMS 1.15 vs 0.33; the O(1)-scale fluctuation present, Selberg constant not yet attained at these heights | **CHECKED NUMERICALLY** | s_probe.py (command §5) |
| "The real zeros' simple fraction provably exceeds p₀" (would-be input) | **CONJECTURED** (this is the goal of the whole program; nothing proven) | — |
| Any beyond-1 variance value | **CONJECTURED** (PCC-equivalent) | CCCM intro, via gm-variance §3 row 7 |
| "No fluctuation-type inequality exists in mathematics" (beyond the held sources) | **CONJECTURED-as-absent** (documented absence; not refuted) | — |
| **Verdict: V13 DEAD-consistent-with-walls; do not fund** | **DECISION** | this note §6 |

Sources: idea-generator-crossdomain.md §V13; attack-ceiling.md; attack-lpdual.md; attack-gm-variance.md (+ its held bibliography: goldston-2004-paircorr-notes.pdf §10; cccm-2108.09258; glss25-2503.15449; baluyot-etal-2306.04799); attack-vector-catalog.md row 24; research/papers/claude-riemann-paper.txt; research/lean-zeta-23/Zeta23/PairCeiling/*.lean (via the attack notes). Script: research/notes/attack-selberg-clt/s_probe.py.
