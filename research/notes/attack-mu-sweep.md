# Attack: Control-family inequality sweep vs Lemma 3.2 on the (1,1)-blocks (C-MU2)

**Agent:** EXECUTIONER — Round 1 (constraint-hardness + investigation angles)
**Vector:** C-MU2 from `research/notes/idea-generator-control.md` (control catalog, Pool 6), the
control-side twin of the QI sweep `research/notes/attack-qi-sweep.md` (P10.1/P10.3).
**Question:** Does any control-theory inequality — Glover's 2Σσ balanced-truncation bound, Perron's
rank-1 / max-row-sum bounds, the Ostrowski–Schneider inertia theorems, D-scaled μ bounds — imply a
strictly better lower bound on the certificate's target (the simple on-line fraction s₁, via rank
r = s₁) than Lemma 3.2's rank–trace `r ≥ 2trP + 4trQ − 4b − ‖P+Q‖²_F` on the certificate's data budget
D = (tr, ‖·‖²_F, rank, n₊)?
**Status:** SWEEP COMPLETE. **Bottom line: NO — no control-family bound beats Lemma 3.2 on the data
budget D; independent confirmation of the QI sweep's negative from the control direction.** Two
independent layers close it: (i) the certificate consumes the *exact* (trA, ‖A‖²_F) from the prime side,
so a lower bound on ‖A‖²_F is moot at the certificate level, and (ii) any D-only bound on the counts
(s₁, b) is capped by the sharp crystal diag(1^r, 2^b) (Lemma 3.2's equality case, PROVEN = lemmaR_tight
/ Prop 4.4(b)). Every candidate individually fails on a third, candidate-specific reason (needs data
outside D, or is strictly weaker at the sharp crystal — quantified below).
All numeric claims are **CHECKED NUMERICALLY** (f64, numpy; reproduce with
`uv run --with numpy python tools/control_mu_sweep.py`; full output in `tools/control_mu_sweep_out.txt`).

---

## 0. Numbering note (same as the QI sweep)

The formal paper `research/papers/claude-riemann-paper.txt` has **Lemma 3.2 = rank–trace inequality**
(c=2 form: `r ≥ 2trP + 4trQ − 4b − ‖P+Q‖²_F`, stated at paper lines 639–645; equality at
`P = Π₁, Q = 2Π₂`, `Π₁ ⊥ Π₂`, ranks r, b). This note uses the formal numbering. Lemma 3.1 is the
positive-index pull-back (`n₊(Q₁+Q₂) ≤ n₊(Q₁)+n₊(Q₂)`).

---

## 1. The certificate structure (recap, condensed — details in attack-qi-sweep.md §1)

Window variational problem ([AK] §1, PROVEN): `rank ≥ 2tr − ‖·‖²_F` fed with prime-side moments
`tr = (1+o(1))N`, `‖·‖²_F = (c+o(1))N`, `c = 1/2+(1/√2)cot(1/√2) = 1.3274992963…` gives the constant
`2−c = 3/2−(1/√2)cot(1/√2) = 0.6725007037…`.

Matrix structure (paper Prop 4.1/4.4, PROVEN in Lean): `bA = P₁ + Q′`, `P₁ ⪰ 0` rank ≤ s₁, `trP₁ ≤ s₁`,
`n₊(Q′) ≤ s₂+p =: b`; each off-line pair contributes a hyperbolic (1,1)-block. Lemma 3.2 (c=2) + `trP₁ ≤ s₁`
gives Prop 4.4(i): `3s₁ + 4b ≥ 4trA − ‖A‖²_F`; with the prime side and the LP, `s₁ ≥ 0.67250·N`.
Sharpness (`lemmaR_tight`, paper §7.5(b), PROVEN): given only (tr, ‖·‖²_F, block structure, trP₁ ≤ s₁),
the bound is sharp, attained at `P₁ + Q′ = diag(1,…,1, 2,…,2)` (s₁ ones, b twos).

**The two forms of Lemma 3.2 used below** (careful — they are different objects):
- **L-form** (the inequality as proved): `‖P+Q‖²_F ≥ 2trP − r + 4trQ − 4b`. Let `L := 2trP − r + 4trQ − 4b`.
- **r-form** (the certificate's use): `r ≥ 2trP + 4trQ − 4b − ‖P+Q‖²_F =: L_r`.

The certificate plugs the **exact** prime-side (trA, ‖A‖²_F) into the r-form via (C)
`3s₁+4b ≥ 4trA − ‖A‖²_F`; it never uses a *lower bound* on ‖A‖²_F (the true value is in D). This is the
first layer of the negative (§2.5).

---

## 2. The candidates, stated precisely, expressed in D, verdicts (the side-by-side table)

For each candidate: exact inequality → D-expression → implied bound on s₁/n₊ → verdict.
Data budget D = (trP, trA, ‖A‖²_F, rank P = r, n₊(Q) ≤ b, P ⪰ 0, hyperbolic (1,1)-block structure).
`trQ₊` below = trace of the positive part of Q (eigenvalues > 0) — *not* in strict D, noted where used.

| # | Inequality (precise statement) | Expressed in D | Verdict |
|---|---|---|---|
| 1 | **Glover 2Σσ (balanced truncation, Glover 1984 / Enns 1984, standard)**: for a stable transfer function G with Hankel singular values σ₁ ≥ σ₂ ≥ …, the k-th-order balanced truncation satisfies `‖G − G_k‖_∞ ≤ 2Σ_{i>k} σᵢ`. | Needs the Hankel singular values = eigenvalues of √(W_c W_o), a **pair** of Gramians. The certificate has one Hermitian form bA, no transfer function, no Gramian pair — σᵢ are not defined from D. Even the most generous grant (σᵢ := \|λᵢ(A)\|, the full spectrum) is data outside D, and the bound's direction is an UPPER bound on approximation error — not a lower bound on ‖A‖²_F. The family's natural certificate-side reading is the Eckart–Young top-r energy `Σ_{i≤r} λᵢ(A)²` (=: L_glo), which misses the Q-charge: at the sharp crystal `L_glo = r + 3b < L = r + 4b` (r ≥ b), strictly below by exactly **b** (T1: gains −1, −16, −1638 for b = 1, 16, 1638). On a realistic mixed config, L_glo ≈ ‖A‖²_F itself (T4: 92.9934 vs 92.9937) — i.e. it is just "the true F-norm minus a tail", and the certificate already has the true F-norm. | **INAPPLICABLE on D** (needs the spectrum / a transfer function); even granted the full spectrum, strictly **below L at the sharp crystal**. No gain. |
| 2 | **Perron–Frobenius family** (standard): (a) spectral radius vs max row sum `ρ(M) ≤ max_i Σ_j \|M_ij\|`; (b) "rank-1 / max ≥ average": for Q₊ ⪰ 0 with b positive eigenvalues, `λ_max(Q₊) ≥ trQ₊/b`, so `‖Q₊‖²_F ≥ λ_max² ≥ (trQ₊)²/b²`. | (a) reads **entrywise** data (the Gram matrix's row sums = the zero *separations* — zero-side data, outside D; exactly the C-BT1/C-PF caveat). (b) is D-only but **strictly weaker than the QI sweep's CS bound** `(trQ₊)²/b` (b ≥ 1 ⟹ (trQ₊)²/b² ≤ (trQ₊)²/b) **and strictly below Lemma 3.2's flat charge at the sharp crystal**: `(trQ₊)²/b² − (4trQ₊−4b)` at trQ₊ = 2b equals `4−4b < 0` for b ≥ 2. Numerically: T1 gains −60 (67,16), −6548 (6725,1638); T4 L_per = 52.32 < L = 60.39 (gain −8.07). | **INAPPLICABLE as a certificate input** (entrywise form reads zero-side data); the D-only form is **strictly weaker than Lemma 3.2 at the sharp crystal** for b ≥ 2. No gain. |
| 3 | **Ostrowski–Schneider inertia theorem** (1962, standard): if `AX + XA* = −Q`, `Q ⪰ 0`, X Hermitian nonsingular, (A,Q) controllable, then `inertia(X) = inertia(A)` (n₊(X) = n₊(A)). The brief's paraphrase "inertia of A = inertia of A+Q for suitable Q" is the transfer content; the usable finite fragment is the monotonicity `n₊(A+Q) ≥ n₊(A)` for Q ⪰ 0. | The equality form needs the **Lyapunov dynamics A whose spectrum is the zeros** — the Hilbert–Pólya operator, whose construction IS RH (C-LY1, KNOWN-OPEN). The certificate has bA (a Gramian-like form), not the HP operator; no X, no Lyapunov equation exists. The finite monotonicity is exactly the positive-index statement the certificate **already consumes** (Lemma 3.1 pull-back, PROVEN in Lean): `n₊(Q′) ≤ s₂+p = b`. Sanity-checked on 2000 random (A, Q ⪰ 0): 0 violations (T7). | **INAPPLICABLE** (needs the Hilbert–Pólya operator = RH itself); the finite content is already consumed as Lemma 3.1. No gain. |
| 4 | **D-scaled μ upper bound** (Doyle 1982, standard): for block-structured uncertainty, `μ_Δ(M) ≤ inf_D σ̄(DMD⁻¹)` over block-diagonal positive D. | Two sub-claims. **(a) F-norm (the certificate's datum) is D-scaling-INVARIANT** (PROVEN identity, checked in T6): for Hermitian A and diagonal D > 0, `‖DAD⁻¹‖²_F − ‖A‖²_F = Σ_{i<j} \|a_ij\|²[(dᵢ/dⱼ)²+(dⱼ/dᵢ)²−2] ≥ 0`, equality at D ∝ I ⟹ `inf_D ‖DAD⁻¹‖_F = ‖A‖_F` exactly (T6: ratio 1.00000000 on both random configs; 2000 random D never beat it). **(b) spectral norm**: DAD⁻¹ is similar to A, so its spectrum equals A's; `σ̄(X) ≥ ρ(X)` gives `σ̄(DAD⁻¹) ≥ σ̄(A)`, equality at D=I ⟹ `inf_D σ̄(DAD⁻¹) = σ̄(A)` exactly (T6: 2×2 min 3.618034 = σ̄(A); 400 random D on d=40 only raise it, max 3772). The nontrivial μ inequality `inf_D σ̄ < σ̄(M)` requires **non-normal M** (asymmetric singular values); the Weil form bA is Hermitian, so the D-scaling family is vacuous on it. The LP-level D-scaling *reading* (C-MU1: the certificate's row reweighting r(j/N) is a D-scaling; the 256-law is the worst-case real perturbation; |E(1)| = 2.54·10⁻⁶ is the margin) is a MARGIN statement that re-derives the [AL] closure — it confirms the ceiling, it does not touch ‖A‖²_F. | **VACUOUS on the certificate's Hermitian data** (both norms D-scaling-invariant, PROVEN + checked); as a μ statement it is an upper bound on a margin (confirms [AL]), not a lower bound on ‖A‖²_F. No gain. |

**The one candidate that is a strictly stronger *inequality* than (L) pointwise — and why it still cannot
move the constant (the certificate-level layer, §2.5):** the QI sweep's CS refinement
`(L′): ‖A‖²_F ≥ 2trP − r − 4trQ₋ + (trQ₊)²/b = L + (trQ₊−2b)²/b`. It is the *best* D+ε candidate in
either family (it dominates the Perron form by `(trQ₊)²/b − (trQ₊)²/b² ≥ 0`). Its gain vanishes exactly
at the sharp crystal (trQ₊ = 2b), and the certificate does not use L-form bounds at all (§2.5). The
control family adds nothing above it.

---

## 2.5 Why NO D-only bound can move the constant (PROVEN — the class-level argument)

Let `A* = diag(1^r, 2^b)` be the sharp crystal (Lemma 3.2's equality case; `lemmaR_tight`, PROVEN).
At A*: `L = 2trP − r + 4trQ − 4b = r + 4b = ‖A*‖²_F` exactly (T1: "Lemma-exact? True" for
(2,1),(67,16),(6725,1638)). Two layers:

1. **Certificate layer (the deeper one).** The certificate plugs the **exact** (trA, ‖A‖²_F) into the
   r-form via (C) `3s₁+4b ≥ 4trA − ‖A‖²_F`; ‖A‖²_F is in D, so a *lower bound* on it is never invoked.
   A candidate improves the s₁-bound only by producing a **new constraint on the counts (s₁, b)** from D.
   No such D-only constraint can be uniform: A* is a valid configuration with data
   `D* = (trP = r, ‖A*‖²_F = r+4b, rank P = r, n₊(Q) = b)`, and at A* equality holds in (C). Any
   D-only bound `s₁ ≥ g(D)` must satisfy `g(D*) ≤ s₁ = r = (4trA* − ‖A*‖²_F − 4b)/3`, so no strict uniform
   improvement exists. ∎
2. **Inequality layer (the QI sweep's argument, restated).** For L-form lower bounds on ‖A‖²_F: any
   D-only `f(D) ≤ ‖A*‖²_F = L(A*)` at the sharp crystal, so `f ≯ L` uniformly; and even a strictly-stronger
   pointwise f (the CS form (L′)) has its gain `(trQ₊−2b)²/b` = 0 at A*, which attains the LP minimum. ∎

Candidates that read data **outside D** (Glover's σᵢ, Perron's row sums, the D-scaling family's
non-Hermitian regime) fail the certificate-input test for the independent reason that the certificate
must hold for **all** configurations, and their inputs are configuration-specific quantities not
available from D at certificate time.

---

## 3. Numerics (task 3) — all CHECKED NUMERICALLY (f64, numpy)

`tools/control_mu_sweep.py` (new file; imports the W_T/Gabor machinery from `tools/qi_sweep.py`,
untouched). Command: `uv run --with numpy python tools/control_mu_sweep.py`. Full output:
`tools/control_mu_sweep_out.txt`. Constants reproduced: `int_psi2 = 0.849227999318304`,
`c_HS = 1.327499296320588`, `3/2−(1/√2)cot(1/√2) = 0.672500703679412`.

**T1 — sharp crystal (Lemma 3.2 equality case).** A = diag(1^r, 2^b): `L = ‖A‖²_F` exact at
(r,b) = (2,1),(67,16),(6725,1638) (‖A‖² = 6, 131, 13277; L = 6, 131, 13277). Gains over L:
CS (trQ₊−2b)²/b = 0 always; Perron `4−4b` = 0, −60, −6548; Glover-top `−b` (r ≥ b) = −1, −16, −1638.
No candidate exceeds L at the sharp crystal.

**T2 — real on-line W_T (P-side, Q = 0).** T=200/400/600, N=123/289/472:
`(2tr−‖·‖²)/N = 0.716530 / 0.711225 / 0.709068` (reproduces the QI sweep TEST A; no asymptotic-decay
claim is made here — see the validator note in attack-qi-sweep.md §6). The family cap: CS
`(tr)²/‖·‖² ≥ 2tr−‖·‖²` always (equality iff eigenvalues ∈ {0,1}); the win `(tr−h)²/h` = 7.2328 /
18.2792 / 30.6449 is the finite-T spectrum-spread artifact (tr/N → 1), not a uniform gain.

**T3 — synthetic hyperbolic pair blocks (actual Gabor v-vectors, β=0.3).** Per pair: eig {+1.81758,
−0.15169} etc., tr = 1.67–1.70, ‖Q‖²_F = 3.33–3.53; Lemma Q-side `4tr−4` = 2.66–2.78 < CS `(trQ₊)²` =
3.30–3.50; per-pair gap `(trQ₊−2)²` = 0.017–0.033. Single block (b=1): CS ≡ Perron. inf_D‖DQD⁻¹‖²_F =
‖Q‖²_F exactly (D-scaling invariant, T6).

**T4 — mixed certificate A = P_on(s₁=50) + Q_off(p=4) at T=200 (N=123).** trP = 49.8339, trQ = 6.6799,
trQ₊ = 6.7235, ‖A‖²_F = 92.9937, n₊(A) = 51. L = 60.3875 (slack +32.61); L′(CS) = 60.7948
(gain 0.4074 = (trQ₊−2b)²/b); L_per = 52.3188 (gain −8.07 — weaker than L); L_glo = 92.9934
(≈ ‖A‖²_F — the certificate already has the true value). Prop 4.4(i) holds: 4trA − ‖A‖²_F = 133.06 ≤
3s₁+4b = 166.0 (slack +32.94). These match the QI sweep's TEST D (60.39 / 60.79 / 0.41).

**T5 — gap distribution over 500 random (1,1)-block configs (d=40, r=12, b=4).** Pointwise gain over L:
CS: min +7.45, median +4936, max +29392 — beats L 500/500 (and `L′ ≥ L` asserted on all 500); Perron:
min −48.0, median +800, max +6307 — beats L 470/500; Glover-top: min +257, median +21409, max +79939 —
beats L 500/500 (trivially: it is ≈ ‖A‖²_F ≫ L on spread configs). **Interpretation (honest):** the
pointwise gains are configuration slack on non-sharp configs (spread spectra, trQ₊ ≠ 2b); the uniform
gain is 0 because the sharp crystal is in the class (T1) and the certificate must cover all configs.
This is exactly the QI sweep's "strictly stronger pointwise, zero uniform gain" picture.

**T6 — D-scaling on Hermitian data is vacuous.** F-norm: inf_D‖DAD⁻¹‖²_F = ‖A‖²_F exactly (ratio
1.00000000 on d=20 and d=40 random configs; PROVEN identity in the header); 2000 random D never beat
the minimizer (D ∝ I). Spectral: σ̄(DAD⁻¹) ≥ σ̄(A) with equality at D=I (PROVEN: similarity + σ̄ ≥ ρ);
2×2 check: min over t of σ̄([[3,t],[1/t,2]]) = 3.618034 = σ̄(A); on d=40, 400 random D give σ̄ up to 3772,
never below 120.53 = σ̄(A). The μ upper bound inf_D σ̄ is only nontrivial for non-normal M; bA is
Hermitian. The LP-level D-scaling *reading* (C-MU1: row reweighting r(j/N) = D-scaling; 256-law =
worst-case real perturbation; margin |E(1)| = 2.54e-6) re-derives the [AL] closure — a confirmation,
not a new inequality.

**T7 — Ostrowski–Schneider finite content.** The usable fragment is the monotonicity n₊(A+Q) ≥ n₊(A)
for Q ⪰ 0 (Lemma 3.1, already consumed by the certificate): 0 violations in 2000 random (A Hermitian,
Q ⪰ 0). The equality/inertia-transfer form needs the Hilbert–Pólya operator (C-LY1, KNOWN-OPEN).

---

## 4. Bottom line (task 4, honest)

**Does the control-theory inequality family beat Lemma 3.2's rank–trace on the (1,1)-block data budget
D = (tr, ‖·‖²_F, rank, n₊)? NO.**

1. **Independent confirmation of the QI sweep.** The QI sweep closed the question from the
   quantum-information direction; this sweep closes it from the control direction with a *different*
   candidate family and a *different* (stronger) class-level argument: the certificate consumes the
   exact (trA, ‖A‖²_F), so only a D-only constraint on the counts (s₁, b) could move the constant, and
   lemmaR_tight (PROVEN) rules that out at the sharp crystal diag(1^r, 2^b) — where Lemma 3.2 holds with
   equality (T1) and every candidate's gain is ≤ 0.
2. **Per-candidate verdicts (all negative, each for a different reason):**
   - **Glover 2Σσ**: no transfer function / no Hankel singular values exist for the certificate (data
     outside D); even granted the full spectrum, its natural top-r-energy bound misses the Q-charge and
     is strictly below L at the sharp crystal (gains −1, −16, −1638 = −b for r ≥ b, T1); on mixed
     configs it degenerates to the true ‖A‖²_F the certificate already has (T4).
   - **Perron**: entrywise/max-row-sum form reads zero-side data (outside D); the D-only
     λ_max ≥ trQ₊/b form is strictly weaker than both CS and Lemma 3.2's flat charge at the sharp
     crystal for b ≥ 2 (T1: −60, −6548; T4: −8.07).
   - **Ostrowski–Schneider**: the equality/inertia-transfer form needs the Hilbert–Pólya operator (RH
     itself, C-LY1); the finite monotonicity is already consumed as Lemma 3.1 (T7 sanity: 0/2000
     violations).
   - **D-scaled μ**: on Hermitian data both the F-norm and the spectral norm are D-scaling-**invariant**
     (PROVEN identities, T6) — the μ bound inf_D σ̄ is vacuous on bA; the LP-level D-scaling *reading*
     is a margin statement confirming [AL] (C-MU1), not a new certificate inequality.
3. **The strongest candidate in either sweep remains the QI-side CS bound (L′)** — strictly stronger
   pointwise, gain (trQ₊−2b)²/b, exactly 0 at the sharp configurations that attain the LP minimum. The
   control family contributes nothing above it.

**What WOULD move the constant** (unchanged from the QI sweep's dead ends, now confirmed from the
control direction): an input forcing `trQ₊ ≠ 2b` / non-sharp configurations (repulsion/clustering,
P1.4, KNOWN-OPEN — C-PF's explicit contraction |⟨v_ρ,v_ρ′⟩| ≤ Φ(0)(1−s²/α₁²) is the concrete pricing
form), or data genuinely outside D (a certified count p₁ via the argument principle, C-NY1; a fourth
moment, P2; the sign/Hadamard structure of Φ, C-LY3/C-PF). All of these are phase/structural/count
data, not (tr, ‖·‖², rank, n₊) inequalities — the certificate reads intensity-only, D-scaled,
two-moment data, and every escape is outside that class.

**Honest verdict on the vector:** C-MU2 is **closed with a documented negative** — the control family
confirms the QI sweep's NO at the class level, the sharp-crystal invariance of D-scaling and the
per-candidate weaknesses are now quantified (T1–T7), and the deliverable value is the independent,
side-by-side confirmation plus the two-layer class-level argument (§2.5). Flagged for the PLANNER: the
C-NY1 (argument-principle certified off-line counts) and C-LY3/C-PF (kernel real-rootedness →
repulsion pricing) vectors remain the live control-side frontier — they consume data outside D.

---

## 5. Files

- Numerics: `tools/control_mu_sweep.py` (new; imports the Gabor/W_T machinery from `tools/qi_sweep.py`,
  which was NOT modified); output `tools/control_mu_sweep_out.txt`.
  Reproduce: `uv run --with numpy python tools/control_mu_sweep.py`.
- Sources read: `research/notes/attack-qi-sweep.md` (D-budget formalism, (L) vs (L′), CS dominance,
  TEST A–G), `research/notes/idea-generator-control.md` (funnel, C-MU1/C-MU2/C-MU4, C-BT1, C-LY1, C-PF),
  `research/papers/claude-riemann-paper.txt` (Lemma 3.1–3.3, Prop 4.1/4.4, §1.5, §7.5(b), lines
  636–700, 272–276, 926–951, 2515–2520).

## Honesty labels recap

- PROVEN (paper/Lean): Lemma 3.2, its equality case, lemmaR_tight / Prop 4.4(b); the §2.5 class-level
  argument is a direct consequence (PROVEN by the sharp crystal being in the class).
- PROVEN (derived here, identity): F-norm D-scaling invariance `‖DAD⁻¹‖²_F − ‖A‖²_F = Σ_{i<j}|a_ij|²[(dᵢ/dⱼ)²+(dⱼ/dᵢ)²−2] ≥ 0`; spectral `inf_D σ̄(DAD⁻¹) = σ̄(A)` for Hermitian A (similarity + σ̄ ≥ ρ).
- CHECKED NUMERICALLY: every number in §3 (T1–T7), reproduce with the command in §5.
- CONJECTURED / KNOWN-OPEN (cited, not claimed here): Hilbert–Pólya operator (C-LY1), repulsion input
  (P1.4), C-NY1/C-LY3/C-PF routes.
- No claim of asymptotic decay of the T2 deficit is made (the QI sweep's ~1/log T reading was flagged
  INCONCLUSIBLE by the validators in attack-qi-sweep.md §6).
