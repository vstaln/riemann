# Attack: multiplicity-aware bounds (2/3 simple, 5/6 distinct, 0.67250/0.83625) — can the tightness structure of the rank–trace inequality improve them?

Round 1, EXECUTIONER (investigation + logic). Sources: `research/lean-zeta-23/README.md`,
`Zeta23/ZeroSide/RankTraceMult.lean`, `Zeta23/ZeroSide/TightMult.lean`, `Zeta23/ZeroSide/Mult.lean`,
`research/papers/anthropic-informal-note.txt` (Lemma 3.4), `claude-riemann-paper.txt` (Thms B, C, D;
Prop 4.4, 4.5), `claude-appendix.txt`. Labels: PROVEN = Lean-verified or direct derivation from those
sources; CHECKED NUMERICALLY = computed here.

## 0. Bottom line (read this first)

The gap **5/6 → 1 (distinct)** and **2/3 → 1 (simple)** is a **HARD WALL of the two-moment
rank–trace method**, NOT attributable to provable multiplicity structure. The method already prices
multiplicity integrality *optimally* — the bookkeeping constants are LP-optimal (CHECKED NUMERICALLY)
and the underlying inequality is provably tight (`lemmaR_tight`, PROVEN). Worse for us: the
empirically-true multiplicity distribution (everything simple) is **exactly the configuration on which
the certificate has zero slack** — it is *the* worst case, not a source of slack. Knowing the
multiplicity distribution improves the bound **only** in worlds with on-line zeros of multiplicity ≥ 3
or off-line zeros — the opposite of reality. The only levers past 5/6 are higher moments
(tr Â³, tr Â⁴) or a non-spectral argument excluding the extremal world.

## 1. Reconstruction of the multiplicity-aware argument (PROVEN)

**The master inequality (Lemma R, k-form**; `rank_trace_mult_k_le`, PROVEN in Lean). For P = Σ_j m_j
v_j v_j* (on-line atoms: integer multiplicities m_j ≥ 1, ‖v_j‖² ≤ 1), Q Hermitian with
n₊(Q) ≤ p (off-line pairs; one positive eigenvalue per (1,1)-block), c > 0:

    2c·tr(P+Q) − ‖P+Q‖²_F  ≤  Σ_j k_c(m_j) + c²·p,     k_c(m) := c² − ((c−m)₊)².

k_c is the "penalty" for an on-line atom of multiplicity m: k_c(m) = 2cm − m² for m ≤ c (cap at c²).
Integer values (PROVEN, `kc_two_*`, `kc_three_*`): k₂(1)=3, k₂(m≥2)=4; k₃(1)=5, k₃(2)=8, k₃(m≥3)=9.
It encodes the integrality levels m² ≥ 2m−1 (c=2) / (m−1)(m−2) ≥ 0 via the eigenvalue form
(paper, after Prop 4.4; appendix item (c)).

**Assembly** (`Mult.lean`, PROVEN). In the normalized units Â = A/(aL²) where an isolated on-line
zero contributes eigenvalue ≈ m_ρ, with tr Â = (1+o(1))N, ‖Â‖²_F = (C+o(1))N, C = 1/λ + λ/3:

- **c=2, simple (Thm B)**: 4·tr Â − ‖Â‖²_F − 2N ≤ s₁  ⇒  s₁ ≥ (2−C)N  →  **2/3** (flat), **0.67250** (opt. window, C = 1/c₁*).
- **c=3, distinct (Thm C)**: 6·tr Â − ‖Â‖²_F − 3N ≤ 2·#Z(I′) = 2N_d  ⇒  N_d ≥ ((3−C)/2)N  →  **5/6** (flat), **0.83625** (opt. window).

Derivation of the c=3 bookkeeping (why the constants are 3 and 2): Σ_j k₃(m_j) + 9p ≤ 3N + 2N_d,
using N ≥ Σm_j + 2p, Σm_j ≥ a₁+2a₂+3a₃ (a_i = # on-line of multiplicity i), N_d = s+2p. CHECKED
NUMERICALLY: with C=4/3 both routes give (4−4/3−2) = 2/3 and (3−4/3)/2 = 5/6; with C_opt = 1/c₁* =
1.3274993 they give 2−C = 0.6725007 and (3−C)/2 = 0.8362504 — matching Theorem D exactly.
(Consistent with the README note: the paper derives 5/6 from Prop 4.4(iii) with c=2; the Lean repo
uses c=3. Both give the same constant — this is not a coincidence, see §2.)

## 2. Tightness: what would improve 5/6 → 5/6 + ε?

**lemmaR_tight** (PROVEN in Lean): for on-line atoms with integer m_j ≤ c on orthonormal vectors plus
b pair-blocks of eigenvalue c, equality holds in Lemma R. The inequality cannot be improved using only
(tr, ‖·‖²_F, integer multiplicities, n₊(Q)).

**LP-optimality of the bookkeeping** (CHECKED NUMERICALLY, grid + hand LP). The final constant is
max (2c−C−A)/B over universal constants (A,B) with k_c(m) ≤ A·m + B (all m ≥ 1, on-line) and
c² ≤ 2A + 2B (pairs):  c=2 → (A,B)=(1,2);  c=3 → (A,B)=(3,2);  both give exactly 5/6 at C=4/3 and
0.83625 at C_opt; c=4 gives only 0.668. So 5/6 is the sharp constant of the whole method, not an
artifact of one derivation.

**Sharpened bound as a function of the multiplicity distribution** (derived here; verified against the
extremal world, CHECKED NUMERICALLY). Let s_i = # distinct on-line zeros of multiplicity i,
s₃₊ = # m ≥ 3, p = # off-line pairs, N_off = off-line count (≥ 2p), N = N_on + N_off. Writing the
certificate with its slack explicitly:

    N_d/N ≥ (3−C)/2 + Δ/(2N),   Δ := 2·s₃₊ + 3·Σ_{m_j≥4}(m_j−3) + 3·(N_off − 2p) + p      (c=3 route)
    N_d/N ≥ (3−C)/2 + [s₃₊ + Σ_{m_j≥4}(m_j−3) + N_off]/(2N)                              (c=2 route)
    s₁/N  ≥ (2−C) + [Σ_{m_j≥2}(m_j−2) + (N_off − 2p)]/N                                  (simple, c=2)

Every improvement term is ≥ 0. The certificate is a **worst case over distributions**: only on-line
multiplicities ≥ 3, or off-line zeros, create slack. Simple and double on-line zeros are priced at
exactly their N-cost (k₂(2) = 4 = 2·2; k₃(3) = 9 = 3·3) — multiplicities 1 and 2 are *neutral*,
m ≥ 3 is *profitable*.

**Numerical check** (CHECKED NUMERICALLY): LMFDB zeros `tools/data/zeros_1_1000.txt` — 1000 zeros,
all ordinates distinct, strictly increasing. mpmath: ζ′(ρ) ≠ 0 for the first 120 (min |ζ′| = 0.793,
dps=18); simplicity of the first 10¹³ zeros is established in the literature (Gourdon–Demichel 2004;
no multiple zero known). Plugging this empirical distribution (s₁ = N, s₂ = s₃₊ = 0, p = 0,
N_off = 0) into the formulas: **Δ = 0, all improvement terms vanish** — the bounds stay 5/6 and 2/3.
CHECKED NUMERICALLY: the extremal world (2N/3 simples + N/6 doubles, e.g. N=6: diag(1,1,1,1,2)) has
tr/N = 1, ‖·‖²/N = 4/3 — the *same two trace moments as ζ itself* — and saturates Lemma R
(4tr−‖·‖² = 16 = Σk₂) with N_d = 5N/6. The method provably cannot separate that world from a world
with all 6 zeros simple (N_d = N): both give identical (tr, ‖·‖²). The all-simple world also has
Δ = 0 — reality sits on the wall.

## 3. Weakest link

The steps the brief worried about are all solid: the pairing ρ ↔ 1−ρ̄ (functional equation, equal
multiplicities) is PROVEN; N = N_on + N_off is an identity, and N ≥ s₁+2s₂+2s₃₊+2p follows; the
n₊(W_off) ≤ p claim (one positive eigenvalue per (1,1) block, Prop 4.1(ii)/Lemma 3.1) is PROVEN —
it is n₊ ≤ p, not p/2. Lemma R itself is PROVEN and tight.

The genuine weakest link is the **universal bookkeeping step** Σ_j k_c(m_j) + c²p ≤ A·N + B·N_d — the
only place the certificate converts "penalty mass" into the pair (N, N_d). It is an equality exactly
for worlds with all on-line multiplicities ≤ 2 (and, for the distinct bound, no off-line zeros) —
i.e. **in precisely the worlds closest to reality**. Concretely: the certificate cannot certify more
than 5/6 in the all-simple world because a spectrally identical world (2N/3 simples + N/6 doubles)
achieves N_d = 5N/6 with equality in every step. Where could 5/6 be *wrong* (improvable)? Only by
excluding the extremal world through information the two moments don't carry, or in worlds with
triple-and-higher on-line zeros / off-line zeros (where Δ > 0 gives a genuine, formulaic improvement —
the opposite of the empirical situation).

## 4. Bottom line

- **5/6 and 2/3 are hard walls of the two-moment rank–trace method, not a function of the multiplicity
  distribution.** The method prices integrality optimally (LP-optimal constants, CHECKED NUMERICALLY;
  `lemmaR_tight`, PROVEN), and the empirical all-simple distribution is the extremal case (Δ = 0),
  not a source of slack. Funding multiplicity-distribution data will not move the constants.
- The only documented levers past the wall: (a) **higher moments** — tr Â³ is admissible for λ < 1
  (Rudnick–Sarnak range); HL*(4,λ) for all λ < 1 would give 13/18 simple, all moments → 1 (paper,
  after Prop 4.5, PROVEN-conditional on the correlation input); (b) **excluding the extremal world
  structurally** — lemmaR_tight realizes it as a matrix, but whether the Weil compression of any
  Selberg-class L-function can realize "2N/3 simples + N/6 tight doubles" is open.
- **Single most promising next step:** attack the third moment tr Â³ unconditionally in the
  Rudnick–Sarnak range (the λ < 1 admissibility was confirmed; the missing input is the
  triple-correlation asymptotics), which bypasses the wall instead of chipping at it.

## Label summary

- PROVEN (Lean): Lemma R + k-form + leak-free form; lemmaR_tight (all c); integer k_c values;
  mult_two/mult_three block inequalities; Thms B, C, D (2/3, 5/6, 0.67250, 0.83625).
- PROVEN (derived here from the above): slack formulas Δ (distinct, c=2 and c=3) and the simple-slack
  formula; the claim that empirical slack is 0.
- CHECKED NUMERICALLY: constants (2−C), (3−C)/2 at C = 4/3 and C_opt = 1/c₁*; LP-optimal (A,B);
  extremal-world spectral identity; simplicity of first 120 zeros (mpmath) and distinctness of the
  first 1000; first-10¹³-simple is literature.
- CONJECTURED: that no Selberg-class object realizes the extremal world (unused; not needed for the
  negative result above).
