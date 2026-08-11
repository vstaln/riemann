# Attack: Ho–Kalman / realization-theory rank test on the (1, 4/3, 2) moment Hankel (C-BT3)

Round, EXECUTIONER. Vector C-BT3 from `research/notes/idea-generator-control.md` (Pool 3):
the canonical rank test on the (1, 4/3, 2) moment Hankel as the cheapest concrete decider of
P2's linear-algebra feasibility. Question: **can any Hermitian matrix in the certificate's
block structure realize the moment sequence (m₁, m₂, m₃) = (1, 4/3, 2)?** If the Hankel is
rank-deficient or the moment problem infeasible in the required structure, the third-moment
route is structurally dead; if feasible, the arithmetic (the LP, P6.5) is the only question.

Sources read: `idea-generator-control.md` (C-BT3 + C-BT2), `attack-twobandwidth.md`
(corrected moments; LP with (1, 4/3, 2) gives optimum exactly 5/6), `attack-multiplicity.md`
(extremal world: 2N/3 simple + N/6 double, moments (N, 4N/3, 2N), N_d = 5N/6), the m3/m4
tooling in `tools/`. All numbers in this note were produced by the scripts and commands
listed in §8; nothing was hand-entered. Labels: PROVEN / CHECKED NUMERICALLY / CONJECTURED /
REFUTED per the program's honesty framework.

---

## 0. Bottom line (read this first)

**The third-moment route is ALIVE as a linear-algebra feasibility question and DEAD as a
separation mechanism. The 5/6 wall stands. This is a clean, code-backed confirmation of the
P6.5 negative from the realization-theory side.**

1. **(m₁, m₂, m₃) = (1, 4/3, 2) is FEASIBLE** (PROVEN, exact): the extremal world
   (Gram = diag(1,…,1,2,…,2), 2N/3 simples + N/6 doubles, p = 0 off-line pairs — the
   lemmaR_tight realization) satisfies tr/N = 1, tr²/N = 4/3, tr³/N = 2 with equality. The
   shifted 2×2 Hankel H = [[1, 4/3],[4/3, 2]] has det = 2/9 > 0, rank 2, is PSD. No rank
   deficiency, no infeasibility, no structural obstruction.
2. **The third moment carries ZERO separation power between the two worlds** (PROVEN,
   exact): the real sine-kernel world has m₃ = 2 (attack-twobandwidth, PROVEN) and the
   extremal world has m₃ = 2 (exact arithmetic). The 3-moment data is identical for both;
   every bound that holds for all realizations of (1, 4/3, 2) must hold for the extremal
   world, which pins N_d/N at 5/6 — consistent with the LP optimum being exactly 5/6
   (CHECKED NUMERICALLY, `tools/lp_twobandwidth.py`: B = 0.833333 at λ = 1).
3. **The rank separation is a FOURTH-moment phenomenon, not third** (PROVEN, exact):
   the extremal world has m₄ = 10/3 and, with its honest total mass m₀ = 5/6, its 3×3 Hankel
   has rank 2 (2 atoms, det = 0 exactly); the paper's m₄ = 13/4 forces the 3×3 Hankel
   (m₀ = 1) to rank 3 (≥ 3 atoms, det = 5/108). With the full mass-1 normalization, the
   unique 2-atom realization of (1, 1, 4/3, 2) is the symmetric measure {1 ± 1/√3} and it
   forces m₄ = 28/9 ≠ 13/4, 10/3.
4. **Empirical (first 1000 LMFDB zeros, flat window λ = 1)** (CHECKED NUMERICALLY): the
   real zeros' moments (m₁, m₂, m₃, m₄) = (1.000000, 1.321542, 1.940678, 3.065642) are
   feasible — the empirical Hankels are PSD (H₂ rank 2, H₃ rank 3) — with the known
   finite-height deficit pattern (m₂ −0.9%, m₃ −3.0%, m₄ −5.7% vs closed forms).
5. **Correction to the C-BT3 idea text**: "the two worlds … give different third moments —
   their realization ranks differ" is REFUTED as stated. The two worlds give the **same**
   third moment (2); the rank difference appears at **m₄** (13/4 vs 10/3) and at the honest
   **m₀** (1 vs 5/6), both of which the certificate does not have.

---

## 1. Setup and conventions

m_k = tr(Â^k)/N, the normalized power sums of the certificate's Gram matrix Â (λ = 1 flat
window). Paper's sine-kernel sequence: (m₁, m₂, m₃, m₄) = (1, 4/3, 2, 13/4)
([AM] / attack-twobandwidth §0–1, PROVEN at λ = 1 for m₁..m₃; m₄ is the paper's value, see
§5 for its verification status). Extremal world: eigenvalues 1 (×2N/3) and 2 (×N/6), power
sums (m₁, m₂, m₃, m₄) = (1, 4/3, 2, 10/3) (exact; attack-multiplicity §2).

Two Hankel conventions are used and kept distinct:

- **Shifted Hankel** (Ho–Kalman/Markov-parameter convention, h_ij = m_{i+j−1}): H₂ =
  [[m₁, m₂],[m₂, m₃]]. Its rank is the **McMillan degree** = minimal number of atoms
  realizing the sequence.
- **Moment Hankel** (Hamburger convention, h_ij = m_{i+j} with m₀ the total mass): H₃ =
  [[m₀, m₁, m₂],[m₁, m₂, m₃],[m₂, m₃, m₄]]. PSD of these matrices ⟺ the truncated Hamburger
  moment problem is solvable. **m₀ = (#eigenvalues)/N** is 1 for the all-simple real world
  and 5/6 for the compressed extremal world (the certificate does not know m₀ — it does not
  know N_d).

---

## 2. Hankel matrices: ranks, determinants, eigenvalues (theory)

All exact determinants (Fractions) and eigenvalues (`numpy.linalg.eigvalsh`); produced by
`tools/hankel_test_cbt3.py` Part 1.

| Matrix | entries | rank | det (exact) | eigenvalues (ascending) | PSD |
|---|---|---|---|---|---|
| H₂ (shifted) | [[1, 4/3],[4/3, 2]] | **2** | 2/9 | 0.07599938, 2.92400062 | yes |
| H₂ᵇ (m₀=1) | [[1, 1],[1, 4/3]] | 2 | 1/3 | 0.15287291, 2.18046042 | yes |
| H₃ paper | [[1, 1, 4/3],[1, 4/3, 2],[4/3, 2, 13/4]] | **3** | 5/108 | 0.02302297, 0.38883989, 5.17147047 | yes |
| H₃ extremal (m₀=1) | [[1, 1, 4/3],[1, 4/3, 2],[4/3, 2, 10/3]] | 3 | 2/27 | 0.03464280, 0.40941705, 5.22260682 | yes |
| H₃ extremal (honest m₀=5/6) | [[5/6, 1, 4/3],[1, 4/3, 2],[4/3, 2, 10/3]] | **2** | 0 | 0, 0.29909314, 5.20090686 | yes |
| H₃ all-simple (control) | [[1,1,1],[1,1,1],[1,1,1]] | 1 | 0 | 0, 0, 3 | yes |

Key facts, in order:

- **H₂ is PSD and rank 2**: det = 2/9 > 0, smallest eigenvalue 0.076. A rank-1 Hankel would
  require m₂² = m₁·m₃ (one atom): 16/9 ≠ 2. So the 3-moment data is **not rank-deficient**;
  its **McMillan degree is exactly 2**.
- **H₃(paper) is PD, rank 3**: det = 5/108 > 0 — needs ≥ 3 atoms.
- **The honest extremal-world H₃ is singular, rank 2**: det = 0 exactly (the column relation
  c₃ = −2·c₁ + 3·c₂ holds), consistent with a genuine 2-atom measure. This is the rank-2
  "realization" the C-BT3 idea looked for — it belongs to the extremal world, not to the
  real world.
- **The m₀ = 1 convention erases the distinction**: with m₀ forced to 1, the extremal
  world's sequence (1, 1, 4/3, 2, 10/3) is rank 3 too (det = 2/27) — because forcing the
  all-simple count bakes in an extra (zero) eigenvalue shell {0, 1, 2}. The rank-2 vs rank-3
  separation is only visible with the honest m₀ = N_d/N.

---

## 3. Feasibility verdict for the theoretical (1, 4/3, 2) sequence — PROVEN

**Question: does there exist a Hermitian matrix in the certificate's block structure
(Â = P + Q, P = Σ m_j v_j v_j* with integer m_j, orthonormal atoms ‖v_j‖² ≤ 1, Q with
n₊(Q) ≤ p) realizing (m₁, m₂, m₃) = (1, 4/3, 2)?**

**YES — PROVEN, and the extremal world is the witness** (exact arithmetic in
`tools/hankel_test_cbt3.py` §i): with N = 6, take P = diag(1, 1, 1, 1, 2), Q = 0,
p = 0. Then
s₁/N = 1, s₂/N = 4/3, s₃/N = 2, and N_d/N = 5/6, with equality in every step of the
c = 3 certificate (lemmaR_tight, PROVEN in Lean, attack-multiplicity §1–2). This is not
merely "some matrix": it is the tightness witness of the whole two-moment rank–trace method.

Two further numeric confirmations (all in `tools/hankel_sdp_cbt3.py` / `tools/hankel_free_cbt3.py`):

- **Truncated Hamburger extension**: the data (m₀, m₁, m₂, m₃) = (1, 1, 4/3, 2) is
  extendable to a moment sequence iff some m₄ makes H₃(m₄) ⪰ 0; det H₃(m₄) = m₄/3 − 28/27
  forces m₄ ≥ 28/9 ≈ 3.111. Both candidate worlds' m₄ (13/4 = 3.25 and 10/3 ≈ 3.333) pass
  (λ_min = +0.0230, +0.0346 > 0). The minimum of λ_min(H₃(m₄)) over m₄ is −1.566 at m₄ ≈ 0,
  so the constraint m₄ ≥ 28/9 is real but satisfied.
- **The 2-atom realization is a 1-parameter family with the extremal world on it**: with the
  total mass m₀ free (the certificate's honest situation — it does not know N_d), the system
  m₁ = w₁a + w₂b = 1, m₂ = w₁a² + w₂b² = 4/3, m₃ = w₁a³ + w₂b³ = 2 is 3 equations in 4
  unknowns and admits a continuum of 2-atom solutions (47/52 grid points converged in the
  sweep). Named members verified exactly: the extremal world (a, b; w₁, w₂) = (1, 2; 2/3,
  1/6), m₀ = 5/6, m₄ = 10/3, error 0; and the mass-1 symmetric measure {1 ± 1/√3}, w₁ = w₂ =
  1/2, m₀ = 1, m₄ = 28/9, error 2e-16. A control (single atom at 3, mass 1/3) fails m₃ as
  expected.

**Hence**: the moment sequence is realizable; the minimal (McMillan-degree-2) realization is
a whole family that contains the extremal world. Any certificate lower bound that is valid
for all realizations of the data must hold for the extremal world, i.e. cannot exceed
N_d/N = 5/6. This is the realization-theoretic restatement of the LP verdict.

---

## 4. Why the third moment cannot separate the worlds (the logic, PROVEN)

- Both candidate worlds share (m₁, m₂, m₃) = (1, 4/3, 2) (extremal world: exact arithmetic,
  §3; real sine-kernel world: m₃(1) = 2, attack-twobandwidth §2, PROVEN three ways).
- Therefore any functional of the first three moments takes the same value on both worlds;
  no third-moment datum can discriminate them. The separation shows up only at the **fourth
  moment** (13/4 vs 10/3) or at the **total mass m₀** (1 vs 5/6 = N_d/N) — both quantities
  the certificate does not possess.
- Concretely: with m₄ = 13/4 (and m₀ = 1), H₃ has rank 3, so the real-world spectral
  measure has ≥ 3 atoms; the extremal world has m₄ = 10/3, so it is excluded by the m₄ datum
  regardless of convention (zero eigenvalues don't change m₄). **The fourth moment — not the
  third — is the structural lever** (this is the realization-theoretic content of the
  paper's HL*(4, λ) → 13/18 roadmap, Prop 4.5, CONJECTURED-conditional on the correlation
  input).

---

## 5. Status of m₄ = 13/4 (honesty note)

- m₄ = 13/4 is the **paper's value** (claude-riemann-paper §7.5 / [AM]).
- The project's own 3D-diagram quadrature scripts **do not converge**: `tools/m4_check.py`
  gives 3.686 (R=10), 4.142 (R=20), 4.457 (R=40) — drifting, not settling; the corrected
  reduction in `tools/m4_adjudicate.py` gives 3.616 (R=40/80), 3.366 (R=160) at λ = 1 — still
  drifting. So 13/4 is **NOT numerically verified in this project** (attack-twobandwidth §6
  flagged the same gap).
- The empirical flat-window m₄ from the first 1000 zeros is 3.0656 (−5.7% vs 13/4), the
  same direction and scale as the m₂/m₃ finite-height deficits — weakly supportive but not a
  verification.
- **The core verdicts of this note do not depend on m₄ = 13/4.** T1–T2 (§0) use only
  (m₁, m₂, m₃). The extremal world's m₄ = 10/3 is PROVEN by exact arithmetic. The only
  conclusion conditional on m₄ = 13/4 is "the real-world spectral measure has ≥ 3 atoms"
  (rank 3), which is anyway already forced by the m₀ = 1 + McMillan-degree-2-with-no-mass-1
  2-atom solution (the unique mass-1 2-atom realization forces m₄ = 28/9 ≠ 13/4 — that part
  is PROVEN).

---

## 6. Empirical test on the first 1000 LMFDB zeros (flat window) — CHECKED NUMERICALLY

Script: `tools/hankel_test_cbt3.py` Part 2 (loads `tools/data/zeros_1_1000.txt` directly;
local-rescale convention of `tools/m3_zeros_check.py`: x = γ/sp, sp = mean spacing;
G_ij = sinc(π(xᵢ − xⱼ)) at λ = 1; m_k = tr(G^k)/N).

- γ₁ = 14.134725, γ₁₀₀₀ = 1419.422481, mean spacing sp = 1.406694.
- Empirical moments: m₁ = 1.000000, m₂ = 1.321542 (4/3 = 1.3333, −0.9%),
  m₃ = 1.940678 (2, −3.0%), m₄ = 3.065642 (13/4 = 3.25, −5.7%).
- Empirical Hankels: H₂ rank 2, det = 0.1942, eigenvalues (0.0676, 2.8731), **PSD**;
  H₃ (m₀ = 1) rank 3, det = 0.0408, eigenvalues (0.0226, 0.3606, 5.0039), **PSD**.

Verdict: the real zeros' moment sequence is feasible — both Hankels are positive
semidefinite, no rank deficiency, no numerical infeasibility. The deficits vs the closed
forms are the known finite-height pair/triple-correlation deficit (same pattern as the
paper's own §8 table and attack-twobandwidth §2.3). Nothing in the data suggests a
structural obstruction.

---

## 7. Consistency with the P6.5 LP verdict

`tools/lp_twobandwidth.py` (λ = 1, moments (1, 4/3, 2), s₁ ≥ 2/3): LP optimum
**B = 0.833333 = 5/6 exactly**. The other windows' unconstrained cubic LPs are unbounded
(HiGHS Status 10) — the documented reason is that without the Schur–Horn admissibility
constraint the cubic coefficient runs to −∞ (attack-twobandwidth §3.3). This is fully
consistent with the realization analysis: the extremal world realizes the moments with
N_d/N = 5/6 and equality in every step, so the LP cannot move below 5/6 (lower side, c = 3
certificate: N_d/N ≥ (3 − 4/3)/2 = 5/6) nor above it (upper side, extremal world feasible).
The 5/6 wall is the LP optimum because the moment data is feasible exactly at the wall.

---

## 8. Code and commands (every number above)

- `tools/hankel_test_cbt3.py` — theory Hankels (ranks/dets/eigenvalues/PSD), extremal-world
  power sums, mass-1 2-atom realization (m₄ = 28/9), det H₃(m₄) = m₄/3 − 28/27, McMillan
  degree, empirical moments + Hankels on the first 1000 zeros.
  Command: `uv run --quiet --with numpy --with mpmath --with scipy python tools/hankel_test_cbt3.py`
  Output: `/tmp/attack_hankel/out_test.txt` (reproduced verbatim in §2, §6).
- `tools/hankel_sdp_cbt3.py` — SDP-style λ_min(H₃(m₄)) minimization, m₄ threshold 28/9,
  mass-1 2-atom fits, LP consistency statement.
  Command: `uv run --quiet --with numpy --with scipy python tools/hankel_sdp_cbt3.py`
  Output: `/tmp/attack_hankel/out_sdp.txt`.
- `tools/hankel_free_cbt3.py` — free-mass 2-atom family sweep + named-member verification
  (extremal world error 0, symmetric measure error 2e-16, control fails).
  Command: `uv run --quiet --with numpy --with scipy python tools/hankel_free_cbt3.py`
  Output: `/tmp/attack_hankel/out_free.txt`.
- `tools/lp_twobandwidth.py` (existing) — LP optima; λ = 1: B = 5/6.
  Command: `uv run --quiet --with numpy --with scipy python tools/lp_twobandwidth.py`.
- `tools/m4_check.py`, `tools/m4_adjudicate.py` (existing) — m₄ quadrature status (§5),
  run for the record; both non-convergent.
- Scratch copies: `/tmp/attack_hankel/` (development); final versions installed in
  `tools/hankel_*_cbt3.py` (new files; no existing tool was edited).

---

## Label summary

- PROVEN (exact arithmetic, this note): (1, 4/3, 2) is realizable — extremal world realizes
  it with equality (N_d/N = 5/6); H₂ PSD rank 2 (det 2/9, McMillan degree 2); extremal-world
  m₄ = 10/3; honest-m₀ extremal H₃ rank 2 (det 0); paper m₄ = 13/4 ⟹ H₃ rank 3 (det 5/108);
  det H₃(m₄) = m₄/3 − 28/27 with threshold m₄ = 28/9; unique mass-1 2-atom realization is
  {1 ± 1/√3} forcing m₄ = 28/9; free-mass 2-atom family contains the extremal world; the two
  worlds share m₃ = 2, so the third moment carries no separation power.
- CHECKED NUMERICALLY (scripts + commands in §8): empirical moments (1.000000, 1.321542,
  1.940678, 3.065642) and PSD/rank of the empirical Hankels; λ_min(H₃(m₄)) minimization;
  family sweep (47/52 converged); LP optimum 5/6 at λ = 1; unboundedness of the other
  unconstrained cubic LPs.
- CONJECTURED / paper-value: m₄ = 13/4 (paper's value; the project's quadrature scripts fail
  to converge — NOT independently verified; the empirical 3.0656 is weakly supportive).
- REFUTED: C-BT3's claim that the two worlds "give different third moments — their
  realization ranks differ": the third moments are equal (2 = 2); the rank difference is at
  m₄ and at the honest m₀.
- VERDICT: third-moment route = feasible but non-separating; the 5/6 wall stands. The
  structural levers are m₄ (13/18 roadmap, conditional) and beyond-bandwidth-1 inputs (M29),
  exactly as attack-multiplicity §4 and attack-twobandwidth §5 recorded.
