# Attack: QI inequality sweep vs Lemma 3.2/3.4 (P10.1 / P10.3)

**Agent:** EXECUTIONER — Round 1 (analogy + constraint + logic angles)
**Vector:** P10.1 (negativity/purity tradeoffs vs Lemma 3.2/3.4) and P10.3 (Schmidt-number dual) from
`research/notes/idea-generator-physics.md` Pool 10; TOP-10 item #2.
**Question:** Does the quantum-information literature contain a strictly stronger inequality than the
paper's rank–trace step (positive-index / purity-type bound) for the (1,1)-plane block structure of the
67.25% certificate?
**Status:** SWEEP COMPLETE. **Bottom line: NO — no QI inequality I could state precisely beats Lemma 3.2's
rank–trace bound on the certificate's data budget.** The single strongest candidate (Cauchy–Schwarz on the
positive part of the off-line block) is provably ≥ the certificate's bound term-by-term, but its gain
`(tr Q₊ − 2b)²/b` vanishes exactly at the sharp configurations, so it never moves the constant 0.67250.
All numeric claims below are **CHECKED NUMERICALLY** (f64, numpy; reproduce with
`uv run --with numpy python tools/qi_sweep.py`).

---

## 0. Numbering note (honesty label — the task brief conflates two lemmas)

- In the formal paper `research/papers/claude-riemann-paper.txt`, the **rank–trace inequality is Lemma 3.2**
  (c=2 form: `r ≥ 2trP + 4trQ − 4b − ‖P+Q‖²_F`), and **Lemma 3.4 is Weyl's inequality** (`n^θ₊(A+E) ≤ n₊(A)`
  for `θ ≥ ‖E‖`).
- In the informal note's numbering (as quoted by `research/notes/attack-finitet.md` §4.5), the same
  rank–trace step is called "Lemma 3.4 with B = 0".
- This note follows the formal paper's numbering: **Lemma 3.2 = rank–trace; Lemma 3.4 = Weyl.** When the
  brief says "Lemma 3.4's rank–trace", read Lemma 3.2.

---

## 1. The certificate structure, exactly as used (recap, condensed)

Window variational problem (`research/notes/attack-kernel.md` §1, PROVEN): the two-moment bound
`rank ≥ 2tr − ‖·‖²_F` fed with the prime-side moments `tr = (1+o(1))N`, `‖·‖²_F = (c + o(1))N`,
`c = 1/2 + (1/√2)cot(1/√2) = 1.3274992963…` (the cosine window is the global minimizer of the Rayleigh
quotient `Q(v) = [∫v² + ∬|s−s′|vv]/(∫v)²`; `I+T ≻ 0` with min eigenvalue ≈ 0.93 makes the cosine the
unique global minimizer) gives the constant `2 − c = 3/2 − (1/√2)cot(1/√2) = 0.6725007037…`.

Matrix structure (`claude-riemann-paper.txt` Prop 4.1, 4.4, PROVEN in Lean):
- `bA = P₁ + Q′`, `P₁ ⪰ 0` rank `≤ s₁`, `tr P₁ ≤ s₁` (simple on-line zeros, eigenvalues ≈ 1 in the (4.4)
  normalization), `n₊(Q′) ≤ s₂ + p` (multiple on-line zeros + off-line pairs).
- Each off-line pair contributes a **hyperbolic (1,1)-block**: in evaluation coordinates the 2×2 form
  `(x,y) ↦ 2m_ρ Re(xȳ)`, matrix `[[0, m_ρ],[m_ρ, 0]]`; in physical view `Q_ρ = m_ρ(v_ρ v_ρᵀ + v̄_ρ v̄_ρᵀ)`
  with `v_{ρ*} = conj(v_ρ)` (Schwarz reflection; **CHECKED NUMERICALLY** to 0 in attack-finitet §4.7).
- Lemma 3.2 (c=2) + `trP₁ ≤ s₁` gives Prop 4.4(i): `3s₁ + 4s₂ + 4p ≥ 4trA − ‖A‖²_F`. Together with
  `N ≥ s₁ + 2s₂ + 2p` and the prime side `4trA − ‖A‖²_F ≤ (4−c+o(1))N`, the LP minimum gives
  `s₁ ≥ (2−c)N = 0.67250·N` (paper §1.5, lines 288–291; re-derived in §3 below).
- Sharpness: `lemmaR_tight` / Prop 4.4(b): given only `(tr, ‖·‖²_F, block structure, trP₁ ≤ s₁)` the bound is
  sharp, attained by `P₁ + Q′ = diag(1,…,1, 2,…,2)` (s₁ ones, s₂+p twos) — **CHECKED NUMERICALLY** (TEST E):
  `‖A‖²_F = 4trA − 3s₁ − 4(s₂+p)` exactly there.

---

## 2. The formal analogy map (task 2)

### 2.1 Dictionary (exact, no hand-waving)

| QI object | Certificate object | Exact correspondence |
|---|---|---|
| bipartite state `ρ` on `C^d ⊗ C^d` | Hermitian matrix `A = bA` on `C^d` (grid coordinates) | both Hermitian, possibly indefinite |
| partial transpose `ρ^{T_B}` (Hermitian, tr 1, may be indefinite) | `A = P + Q` (Prop 4.1) | the Weil form IS the "PT-like" object |
| separable / PSD part of `ρ^{T_B}` | `P` (on-line part, `P ⪰ 0`) | `P = Σ_{on-line} m_ρ u_ρ u_ρᵀ`, real `u_ρ` |
| entangled part of `ρ^{T_B}` (negative eigenvalues) | `Q` (off-line hyperbolic blocks) | `Q = Σ_pairs m_ρ(v vᵀ + v̄ v̄ᵀ)`, each signature (1,1) |
| Bell pair `\|Φ⁺⟩ = (|00⟩+|11⟩)/√2` | one off-line pair block | PT of Bell pair has off-diagonal `[[0,m],[m,0]]` block — exactly the pair's 2×2 form; physical view eigenvalues `{+mα, −mβ}` |
| negativity `N(ρ) = Σ\|λ⁻(ρ^{T_B})\|` (magnitude) | per-pair product `αβ` (via `‖Q_i‖² = (trQ_i)² + 2αβ`) | see §2.2 identity (1) |
| negative-eigenvalue **count** of `ρ^{T_B}` | `n₊(Q)` (positive index of off-line part) | certificate uses the count `n₊(Q) ≤ p` (Lemma 3.1 pull-back), i.e. "the off-line part carries ≤ p entangled directions" |
| purity `p = tr(ρ²)` | second moment `‖A‖²_F` (the certificate's "purity" input) | both are the ℓ₂ moment; the certificate's other moment is `trA` |
| Schmidt rank `r_S` | rank of the on-line part `P` | certificate lower-bounds `rank(P)` from `(tr, ‖·‖²_F)` |
| PPT criterion: `ρ^{T_B} ⪰ 0 ⟺` separable (2×2, 2×3) | `n₋(Q) = 0` ⟺ no off-line pairs | "all zeros on the line" is the PPT/separable case |
| purity–negativity tradeoff (pure 2-qubit: `N² = (1−p)/2`) | per-hyperbolic-block identity `‖Q_i‖²_F = (trQ_i)² + 2αβ` | exact PT-analog, §2.2 |

### 2.2 The matrix inequalities, side by side

**Per off-line pair block** (physical view `Q_ρ = m(v vᵀ + v̄ v̄ᵀ)`, eigenvalues `{+mα, −mβ}`), **CHECKED
NUMERICALLY** to ≤ 1.8·10⁻¹⁵ (TEST B):

```
‖Q_ρ‖²_F = (tr Q_ρ)² + 2αβ          (1)   [exact; 2αβ = 2·|det Q_ρ|]
```

Normalizing `ρ_ρ = Q_ρ/tr(Q_ρ)` (tr ≠ 0), with "negativity" `N_ρ = β/tr(Q_ρ)`:

```
purity(ρ_ρ) = 1 + 2N_ρ + 2N_ρ²      (2)   [PT-analog; purity > 1 because ρ_ρ has a negative eigenvalue]
pure 2-qubit:  p = 1 − 2N²           (2′)  [state analog; purity < 1]
```

**The certificate's rank–trace step** (Lemma 3.2, c=2, applied to `P = P₁`, `Q = Q′`):

```
‖P + Q‖²_F ≥ 2trP − r + 4trQ − 4b            (L)   [r = s₁, b = s₂+p]
```

**The would-be QI winning inequality** (what the literature would need to supply on the certificate's data
budget `D = (trP₁, s₁, b, trA, ‖A‖²_F, trP₁ ≤ s₁, n₊(Q) ≤ b, hyperbolic-block structure)`):

```
∃ δ(D) > 0 uniform over all configurations with:
    ‖P + Q‖²_F ≥ 2trP − r + 4trQ − 4b + δ(D)      (L*)   ⟹  s₁ ≥ 0.67250·N + δ
```

**The one candidate that achieves a strictly larger RHS than (L) on the same data** — Cauchy–Schwarz on the
positive part of Q (`Q₊ ⪰ 0`, rank ≤ b, so `‖Q₊‖²_F = Σ_{j≤b} q_j² ≥ (Σq_j)²/b = (trQ₊)²/b`):

```
‖P + Q‖²_F ≥ 2trP − r + 4trQ − 4b + (trQ₊ − 2b)²/b      (L′)   [CS refinement]
```

Why (L′) is valid on D: `(trQ₊)²/b − (4trQ₊ − 4b) = (trQ₊ − 2b)²/b ≥ 0`, and `4trQ₊ ≥ 4trQ`; the P–Q₋
interaction is handled by the same von Neumann pairing as in Lemma 3.2's proof (the Q₊ term adds
separately). **CHECKED NUMERICALLY** on 400 random indefinite matrices (TEST G): `‖Q‖²_F ≥ (trQ₊)²/b` always
(asserted), and `(trQ₊)²/b − (4trQ − 4b) ≥ +0.307` in the worst of the 400 trials.

**Why (L′) does not move the constant.** The certificate must hold configuration-by-configuration. The
sharp configuration `P₁ + Q′ = diag(1,…,1, 2,…,2)` has `trQ₊ = 2b` exactly, so `(trQ₊−2b)²/b = 0` there
(TEST E), and the LP minimum `s₁ ≥ 0.67250N` is attained on (a) such configuration(s). Any `δ` built from D
vanishes on them. So the uniform bound is unchanged; (L′) is a **strictly stronger inequality whose gain is
concentrated in non-sharp configurations** — exactly the "monogamy, real but unexploitable without a
clustering input" story of W-P6 / P10.4.

---

## 3. The sweep (task 3): candidate QI inequalities, verdicts

For each: does it imply a strictly better bound than (L) on the (1,1)-block structure, on the certificate's
data budget D?

| # | QI inequality (precise statement) | Verdict | Why |
|---|---|---|---|
| 1 | **Cauchy–Schwarz purity–rank**: `rank(R) ≥ (trR)²/‖R‖²_F` for `R ⪰ 0` ("Schmidt rank ≥ 1/purity" for pure states). | **EQUAL in class** | `(trR)²/‖R‖²_F ≥ 2trR − ‖R‖²_F` always (equality iff eigenvalues ∈ {0,1}); the paper's c=2 bound is the sharp member of the same family for integer spectra {1,2} and is forced by the combined P/Q/cross structure. On the real P-side (TEST A): `(tr)²/‖·‖²` beats `2tr−‖·‖²` (95.37 vs 88.13 at T=200), but the difference `(s₁−trP₁)²/s₁` vanishes asymptotically (trP₁ → s₁). No uniform gain. |
| 2 | **Q₊-side CS**: `‖Q₊‖²_F ≥ (trQ₊)²/b` (uses only `n₊(Q) ≤ b`, i.e. D). | **STRICTLY BETTER as an inequality; ZERO uniform gain** | Gives (L′); `(trQ₊−2b)²/b ≥ 0`, = 0 exactly at sharp configs (trQ₊ = 2b). Measured per-pair: gap `(trQ_i−2)² = 0.09–0.11` for β=0.3 pairs (TEST B); total on a mixed A: Δ = 0.407 for p=4 (TEST D); on the sharp config: 0 (TEST E). |
| 3 | **Purity–negativity tradeoff** (pure 2-qubit `N² = (1−p)/2`; Hofmann–Takeuchi-type `N ≤ f(p)` for mixed states). | **EQUAL / already saturated** | The exact analog is identity (1)–(2): `‖Q_i‖²_F = (trQ_i)² + 2αβ`, i.e. the block's purity-excess is fixed by its negativity product. This is precisely what the c=2 per-block bound saturates (sharp at tr = 2). Mixed-state tradeoffs bound negativity FROM purity — the wrong direction for the certificate, which needs ‖·‖²_F from below given the count. |
| 4 | **Schmidt-number bounds** (Sanpera–Terhal–Bruss–Kiess; Eltschka–Siewert: purity region of Schmidt-number-≤s states). | **INAPPLICABLE** | (i) Negativity/Schmidt number live on a fixed bipartite tensor-product split `C^d ⊗ C^d`; the certificate's matrices act on a single grid Hilbert space with no such split. (ii) A state's Schmidt number is unbounded by purity alone (pure states have purity 1 and any Schmidt number), so the dual bound "max p given purity" needs per-state witnesses that are not in D. |
| 5 | **PPT / smallest-eigenvalue bounds** (Peres–Horodecki: separable ⟹ `ρ^{T_B} ⪰ 0`). | **INAPPLICABLE** | The off-line blocks are indefinite **by construction** (signature (1,1) — they are the "entangled" part). The criterion's contrapositive is what the certificate already uses (n₋(Q) counts). No new information on D. |
| 6 | **Subadditivity of n₊ / monogamy of entanglement** (CKW-type; `n₊(Q₁+Q₂) ≤ n₊(Q₁)+n₊(Q₂)`). | **Real effect, NO unconditional gain** | The certificate already uses subadditivity via Lemma 3.1's diagonal pull-back. Numerically (TEST C): joint `n₊(M₁+M₂) < 2` only at **exact coincidence** (Δs = 0); any positive separation keeps `n₊ = 2` even at overlap 0.997. The magnitude-level gain `(trQ−2b)²/b` persists (candidate 2) but requires a clustering/repulsion input (P1.4, KNOWN-OPEN). |
| 7 | **Entanglement entropy / max-entropy under moments** (P10.2 diagnostic). | **Diagnostic only** | Measures spectral slack, not a certificate inequality. |
| 8 | **Higher moments (one-sided Chebyshev–Markov–Stieltjes; paper's own Remark, line 2316)** — the "m ≥ 2" extension of Lemma 3.3's `n^θ₊ ≥ (tr−θd)²/tr(R²)`. | **Not QI; needs new arithmetic input** | A 4th-moment bound `d⁻¹tr(Ĝ/ℓ₁)⁴` would need a new prime-side evaluation of the pair sum's 4th moment — outside the matrix-inequality class this sweep tests. Worth flagging as the paper's own strongest "more data" route. |

---

## 4. Numeric evidence (task 3), all CHECKED NUMERICALLY (f64)

`tools/qi_sweep.py` reconstructs the finitet `W_T` (port of `tools/finitet/src/main.rs`; constants
reproduced to 15 digits: `int_psi² = 0.849227999318304`, `c = 1.327499296320588`,
`3/2−(1/√2)cot(1/√2) = 0.672500703679412`).

**TEST A — real on-line W_T (P-side).** Reproduces attack-finitet: `(2tr−‖·‖²)/N = 0.7165, 0.7112, 0.7091`
at T = 200, 400, 600, all above 0.6725; `(tr)²/‖·‖²` is larger (95.37 vs 88.13 at T=200), i.e. the CS
rank bound dominates the c=2 bound on real data, but the gap `(s₁−trP₁)²/s₁` is a finite-T artifact
(trW/N → 1).

**TEST B — per-pair hyperbolic blocks (actual Gabor v-vectors, β=0.3).** Each pair: eigenvalues
`{+1.8176, −0.1517}` etc., n₊ = n₋ = 1; identity (1) holds to ≤ 1.8·10⁻¹⁵; certificate Q-side
`4tr−4 = 2.66–2.78 < ‖·‖²_F = 3.33–3.53`; per-pair gap `(tr−2)² = 0.09–0.11`.

**TEST B2 — deep pairs (β = 0.05…1.2).** Pair trace `trQ_i ∈ [1.655, 2.829]`; at β=1.2 the block is
`{+8.13, −5.30}`, `‖·‖²_F = 94.3 ≫ 4tr−4 = 7.3` — both bounds extremely loose for deep pairs (the
certificate's bound is tight near the on-line crystal, loose off it; the loose regimes cannot be exploited
because the certificate must cover the worst case).

**TEST C — subadditivity of n₊.** Two pairs at separation Δs ∈ {0, 0.05, …, 6}: joint n₊ = 2 for every
Δs > 0 (overlap 0.997 at Δs=0.05), n₊ = 1 only at Δs = 0 (coincident). Confirms P10.4's prior: the
count-level subadditivity gain is confined to exact coincidence.

**TEST D — mixed A = P_on(s₁=50) + Q_off(p=4, β=0.3) at T=200.** `trP_on = 49.83` (≈ s₁, matching Lemma 2.2's
`trP₁ ≤ s₁`), `trQ = 6.68`, `trQ₊ = 6.72`, `trA = 56.51`, `‖P‖²_F = 61.65`, `‖Q‖²_F = 15.59`,
`2Re tr(PQ) = +15.75`, `‖A‖²_F = 92.99`; Lemma 3.2 (c=2) RHS = 60.39 (slack +32.61); SHARP-1 RHS = 60.79
(Δ = (6.72−8)²/4 = 0.41, slack +32.20). CS on the P-side alone: `(trP_on)²/s₁ = 49.6683` vs
`2trP_on − s₁ = 49.6678` (CS wins by `(s₁−trP_on)²/s₁ = 0.00055` — the same finite-T artifact as TEST A).
The certificate's inequality holds with large slack on the realistic mixed config (spread spectrum, not
crystal); the CS gain is a small fraction of the slack.

**TEST E — sharp configurations.** `diag(1,…,1,2,…,2)` with (s₁,b) = (67,16) and (6725,1638): the
certificate bound is **exact** (`‖A‖²_F = 4trA − 3s₁ − 4b` to 1e-9) and Δ = 0. This is the sharpness
(`lemmaR_tight` / Prop 4.4(b)) that blocks every D-based improvement.

**TEST G — 400 random indefinite Q.** `‖Q‖²_F ≥ (trQ₊)²/b` always (asserted); min `(trQ₊)²/b − (4trQ−4b)`
over all trials = +0.307; `diag(2,…,2)` (b=5): equality, Δ = 0.

---

## 5. Bottom line (task 4, honest)

**Does the QI literature beat Lemma 3.2/3.4's rank–trace on the (1,1)-block structure? NO.**

1. Every QI inequality I could state precisely on the certificate's data budget D is either
   **EQUAL in class** (CS purity–rank; purity–negativity per-block identities (1)–(2), which the c=2 bound
   already saturates), **INAPPLICABLE** (Schmidt-number bounds — no bipartite split; PPT — blocks
   indefinite by construction), or **strictly stronger but with zero uniform gain** (the Q₊-side CS bound
   (L′), whose gain `(trQ₊−2b)²/b` vanishes exactly at the sharp configurations that attain the LP minimum
   `s₁ ≥ 0.67250N`).
2. The rank–trace inequality is **not improvable within the class of inequalities reading only
   `(tr, ‖·‖²_F, block structure, trP₁ ≤ s₁)`** — this is exactly `lemmaR_tight` / Prop 4.4(b), now
   confirmed from the QI direction: the strongest candidate (CS) provably dominates (L) term-by-term yet
   cannot move the constant.
3. The **measured** finite-T slack (`bound/N = 0.709–0.717 > 0.6725`, positive, decaying ~1/log T;
   attack-finitet §5) is configuration slack, not an inequality improvement — it is an artifact of the
   zeros' actual pair correlation, not of a stronger matrix bound.

**What WOULD move the constant** (ranked by how much new input they need):
- **A repulsion/clustering input** forcing `trQ₊ ≠ 2b` (equivalently: forcing off-line pairs to be
  non-sharp) unlocks exactly `Δ = (trQ₊−2b)²/b` from (L′). This is P1.4 / W-P6 — **KNOWN-OPEN**; no such
  input exists in the certificate's current proven inputs.
- **Per-pair / cross-pair inner-product data** (the Gabor structure `|⟨v_ρ, v_ρ′⟩| = |Ψ(s_ρ−s_ρ′)|`,
  P10.4) can quantify `trQ₊` and the subadditivity gap configuration-by-configuration, but any use must
  be conditional — the certificate must hold for all configurations.
- **A 4th moment from the prime side** (paper's one-sided Chebyshev remark) is the only route inside the
  certificate's own method class, but it is an arithmetic input, not a matrix inequality, and is out of
  scope for this sweep.

**Honest verdict on the vector:** P10.1/P10.3 as stated (find a QI inequality beating the rank–trace on the
(1,1)-structure) is **closed with a documented negative** — the strongest QI-type bound (CS) provably
dominates but provably cannot improve the uniform constant; its gain is exactly the conditional quantity
that a repulsion input would unlock. The deliverable value is: (i) the exact side-by-side inequalities (L)
vs (L′), (ii) the quantified conditional gain `(trQ₊−2b)²/b` and its sharp-config behavior, (iii) the
numerical confirmation that the certificate's inequality holds with the predicted slack on real and mixed
synthetic data. The P10.4 subadditivity probe's negative (n₊ < 2 only at exact coincidence) is also now a
**CHECKED NUMERICALLY** result.

**Next steps that remain open (from this sweep's dead ends):** attack the 0.6725 → 0.68185 PairCeiling gap
with a *different certificate* (more of the configuration/multiplicity structure), or fund the 4th-moment
prime-side input. These are outside the QI inequality class and are flagged for the PLANNER.

---

## 6. Files

- Numerics: `tools/qi_sweep.py` (reproduces every number in §4; `uv run --with numpy python tools/qi_sweep.py`).
- Sources read: `research/papers/claude-riemann-paper.txt` (Lemmas 3.1–3.4, Props 4.1/4.4/4.5, §1.5, §7.5(b)),
  `research/notes/attack-kernel.md` (§1), `research/notes/attack-finitet.md` (§3–§4),
  `research/notes/idea-generator-physics.md` (Pool 10 preamble, P10.1, P10.3, P10.4, TOP-10 #2).

---

## ROUND-3 VALIDATOR CORRECTIONS (from validation-001.md, adversarial pass, all rerun-backed)

- VALIDATOR TARGET (a): the I+T spectrum numbers in this note are CORRECTED — the odd eigenfunctions sin((2m+1)πu) with eigenvalue −2/((2m+1)²π²) were omitted. Min eigenvalue is ≈ 0.797 (not ≈ 0.93); the even root is k ≈ 5.60 (not 5.43). The conclusion (I+T ≻ 0, cosine is the global minimizer) SURVIVES. See validation-001.md target 2.
- VALIDATOR TARGET (b): the "Δ decays to 0 at ~1/log T" reading is INCONCLUSIVE as stated — the note's own fits have nonzero asymptotes (0.014, 0.037, 0.028). Convergence of bound/N to 0.6725 is not demonstrated by the reported data. See validation-001.md target 3.
- VALIDATOR TARGET (c): this note does not mention that EnclOK is the one non-Lean numerical hypothesis in the 0.68185 ceiling; see validation-enclok.md (INCONCLUSIVE, not refuted). See validation-001.md target 5.
- VALIDATOR TARGET (d, verification-001 only): "noise floor" → "Euler–Maclaurin truncation error" (max 6.2e-6 over i≤1000, K=10; collapses at K=14). See validation-001.md target 1.
