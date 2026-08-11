# Attack: importing the Connes–van Suijlekom theorem into the rank–trace–inertia certificate

**Agent:** EXECUTIONER (analogy-domain-transfer + logic + epistemology-limits lens)
**Round:** 2. Mandatory code-backed-verification protocol applied (hooks/agents.md): every numeric claim
below was produced by a script in `tools/cvs-import/`, run in this session; commands are cited inline.

**Sources read at source this session:**
`research/papers/cvs-2511.23257-quadratic-forms-real-zeros.txt` (converted from the PDF this session with
`uvx --from 'markitdown[pdf]' markitdown`), `suzuki-2607.02828-truncated-weil-zero-sum.txt` (Groskin),
`suzuki-2606.09096-weil-quadratic-screw.txt` (Suzuki), `claude-riemann-paper.txt` (§§2–4, §7.5),
`research/notes/close-inclass-gap.md`, `research/notes/attack-lpdual.md`, `research/notes/attack-ceiling.md`,
`research/notes/attack-multiplicity.md`, `research/notes/attack-finitet.md`, `research/notes/paper-finder-001.md`.

---

## 0. Verdict up front

**The in-class question is now CLOSED** (close-inclass-gap.md): the exact rational certificate
`r(x) = 1 − x` attains the in-class optimum **v = p₀ + 1/(6·256²) − δ = 0.6818312305953419**, the Lean
ceiling `ceiling_law256_signed` is TIGHT, and the gap 0.6725 → 0.6818 is closed *in-class*, **not** for
the real zeros. The only datum that moves the REAL constant is a certified real simple fraction p₁ above
p₀, which requires beyond-bandwidth-1 arithmetic (CONJECTURED/unavailable) or a proven multiplicity/
structure bound excluding the 256-law shape.

Framed against that closure, the import question is: **does the CvS theorem (simple isolated lowest
eigenvalue + even eigenfunction ⇒ all Fourier zeros real) change the REAL-zero bound, or is it orthogonal
to the certificate class?**

**Answer: ORTHOGONAL. The import is DEAD for both G1 (past-0.6818) and G6 (an SDP/Weil certificate).**
Three independent fatal blockers, each sufficient alone, all code-anchored:

- **B1 — Object mismatch (code-backed, Check A):** the CvS operator is the *frequency-band* truncation of
  the Weil form (divided-difference matrices of form (11)); the paper's W_T is the *height* truncation
  (Gabor Gram matrices). The paper's W_T **fails** the divided-difference 3-cycle cocycle by O(1) with
  full-rank `(i−j)W_ij` (needs rank ≤ 2); genuine form-(11) matrices satisfy it to 10⁻¹⁶. The CvS
  theorem's proof mechanism (Carathéodory–Fejér / Toeplitz / `D′ = D − |Dξ⟩⟨η|`) does not apply to G.
- **B2 — Hypothesis gap:** the theorem needs the minimum eigenvalue **simple, isolated, even** — proven
  only for small cutoff (Suzuki Thm 1.4), numerically plausible at fixed (c,N), and inaccessible to the
  paper's inertia/rank tools (which bound positive index and rank, never spectral fine structure). CvS
  themselves: verifying the simple minimal eigenvalue is "the key difficulty".
- **B3 — Conclusion orthogonality (code-anchored, Check C):** the certificate value is pinned 1:1 by p₁
  (shadow price exactly 1: v* = p₁ + |E(1)| for every p₁, LP-verified). Real zeros of an eigenfunction's
  Fourier transform carry no information about p₁, about F(α) for α > 1, about multiplicities, or about
  excluding the 256-law. **Even a proof of RH does not move the 0.6818 ceiling** (the ceiling is over
  configurations matching all bandwidth-one data — exactly the data RH supplies; paper §7.5(f)).

**Honest residue (alive, but a different program):** CvS Thm 6.1 is a genuine, carefully-stated theorem —
the rigorous statement of the CCM spectral mechanism (real zeros of the ground-state Fourier transform
under spectral hypotheses). It belongs to the RH-*horizontal* Weil-positivity program (Hilbert–Pólya via
Weil), not to the proportion-*vertical* certificate program. The genuinely useful G6-adjacent certificate
mechanism in this literature is Groskin's tail-order/budget theorem, which is independent of CvS.

**Labels:** PROVEN = proved in a source read at source, or Lean; CHECKED NUMERICALLY = produced by the
scripts below (command cited); ARGUED = reasoning in this note; CONJECTURED = open in the sources.

---

## 1. The in-class closure (the frame, close-inclass-gap.md — read this first)

- The certificate class: pairs (c₀, r), r ∈ C¹[0,1], value v = c₀ + ∫₀¹ r(x)x dx, valid against a
  configuration with grid masses s_j and simple-point fraction p₁ iff c₀ + Σ_j s_j r(j/N) ≤ p₁.
- The 256-law (near-CUE): grid form factor |256·S(j) − j| ≤ 2⁻¹³² (midpoint model S(j) = j/256, so
  s_j = j/65536 at x_j = j/256), simple fraction p₀ = 0.6818286874638315, E(1) = −1/(6·256²) = −2.54·10⁻⁶
  exactly, D(1) = +0.8239531607128352.
- **Closed (PROVEN):** the certificate r = 1−x with c₀ = p₀ − Σ_j (S_max(j)/256)(1 − j/256) is valid
  against the whole enclosure class and attains v = p₀ + 1/(6·256²) − δ = **0.6818312305953419**; the
  Lean ceiling bounds every valid certificate (|r′(1)| ≤ 1, ∫|r″| = 0) by p₀ + 1/(6·256²) + τ/512 —
  ceiling TIGHT; boxed-class optimum = p₀ + |E(1)| exactly (LP, `tools/lpdual/`).
- **Not closed (CONJECTURED):** the real-zero constant is 0.6725 (Thm D, PROVEN); p₁ ≥ 0.6818 for the
  real zeros needs beyond-bandwidth-1 F(α) (Hardy–Littlewood prime pairs), a multiplicity bound, or a
  structural exclusion of the law's shape — all CONJECTURED/unavailable (attack-ceiling §3).
- **Consequence for the import question:** a candidate import only matters if it changes the REAL-zero
  constant. It must therefore either (a) raise the certified real p₁, or (b) enlarge the certificate
  class's reach. CvS does neither (B1–B3).

---

## 2. The CvS theorem, verbatim (from `cvs-2511.23257-quadratic-forms-real-zeros.txt`, converted from
the PDF this session)

### 2.1 Theorem 6.1 (the precise statement; the Introduction's Theorem 1.2 is the "slightly imprecise"
version — their own words, see Remark 4.3)

> **Theorem 6.1.** Let L > 0, and let D be a real distribution on the interval [0, L]. Let Q be the
> quadratic form defined on trigonometric polynomials by (6). Assume that Q defines a lower-bounded
> essentially self-adjoint operator and that the minimum of its spectrum is a simple, isolated eigenvalue
> λ, with even eigenfunction ξ. Then all the zeros of the entire function ξ̂(z), z ∈ C, the Fourier
> transform of ξ, lie on the real line.

The quadratic form (6), verbatim:
> ⟨f|g⟩_Q := D̃(f∗ ∗ g) = ∫₀^L ((f∗ ∗ g)(x) + (f∗ ∗ g)(−x))D(x)dx,

with D̃ the even symmetrization of D (equation (4): D̃(f) := D(f) + D(f̃), f̃(x) := f(−x)).

Footnote to Theorem 6.1, verbatim: "i.e. invariant under the symmetry x ↦ L − x of [0, L]" (the meaning
of *even*).

### 2.2 Theorem 1.2 (Introduction), verbatim (the "slightly imprecise" version they point to Thm 6.1 for)

> Let L > 0, D be a real distribution on the interval [0, L] and D̃ the associated even distribution on
> [−L, L]. Assume that the quadratic form with Schwartz kernel D̃(x − y) defines a lower-bounded
> self-adjoint operator A on L²([−L/2, L/2]), and that the minimum of its spectrum is a simple, isolated
> eigenvalue λ, with even eigenfunction ξ. Then all the zeros of the entire function ξ̂(z), z ∈ C,
> Fourier transform of ξ, lie on the real line.

### 2.3 The hypothesis list, verbatim/unpacked

H1. **L > 0.**
H2. **D is a real distribution on [0, L]** — not on [−L, L]: the form must be built by symmetrization (6).
    Essential (Remark 4.3, verbatim): "It is important to take as a starting point a distribution D on
    [0, L] and then define the associated quadratic form using (6), rather than starting from an even
    distribution on [−L, L]. For instance the derivative δ′₀ of the Dirac distribution at 0 ∈ [0, L]
    gives rise to a non-zero quadratic form while the associated even distribution obtained by
    symmetrisation is equal to 0."
H3. **Q is the quadratic form on trigonometric polynomials given by (6).** Its matrix in the orthonormal
    basis U_n(x) = L^(−1/2) exp(2πinx/L) has the divided-difference ("screw") structure (Prop 4.1,
    eq. (11)), verbatim:
    q_ii = a_i,   q_ij = (b_i − b_j)/(i − j)   (j ≠ i),   with a_{−i} = a_i, b_{−i} = −b_i.
H4. **Q defines a lower-bounded essentially self-adjoint operator** (the trig polynomials are a core —
    used throughout the proof of Thm 6.1).
H5. **The minimum of its spectrum is a simple, isolated eigenvalue λ.** "Isolated" = a spectral gap:
    spectrum ⊂ {λ} ∪ [λ + δ, ∞) for some δ > 0 (used via min–max in the proof).
H6. **Even eigenfunction ξ** (γξ = ξ, γ(e_j) = e_{−j}); Q commutes with γ because a_{−i} = a_i,
    b_{−i} = −b_i, so even/odd sectors decouple, and the theorem needs the *global* minimum in the even
    sector, simple there.

Conclusion C. All zeros of the entire function ξ̂(z) (Fourier transform of ξ, exponential type, zeros =
2πZ ∪ 2π·roots of P, P(s) = Σ_k ξ_k ∏_{j≠k}(j − s), Thm 5.6) lie on the real line.

### 2.4 The two caveats that matter (verbatim)

- **Simplicity is essential** (Remark 2.3): "in general, when the kernel of T is more than one-dimensional
  — in other words, when the extreme eigenvalue is not simple — … it is not true in general if the
  eigenvalue is not simple, that the theorem holds. The correct formulation … is that if you take the
  intersection of the zeros of the various eigenfunctions, then they are all on the unit circle."
- **The hypotheses are the hard part** (Introduction, verbatim): "The key difficulty in this context, then,
  becomes the verification that zero is indeed the (simple) minimal eigenvalue of T."

### 2.5 What the conclusion is NOT (do not overstate)

The conclusion concerns the **Fourier transform of the eigenfunction of the truncated quadratic form** — a
function different from ζ. It says nothing about ζ's zeros directly. The bridge to ζ is a *conjectural*
limit formula (Suzuki (1.2): c_a v̂_a(z) → ξ(1/2 + iz)), which is OPEN. See §3.3.

---

## 3. The two compressions of the Weil form (are CvS's operator and the paper's W_T the same object?)

**No.** Both are finite compressions of the same Weil Hermitian form W, along different axes, in different
bases, with different asymptotics and different roles.

### 3.1 The paper's W_T (claude-riemann-paper.txt §2)

Gabor system f_k(u) = φ(u)e^(−iτ_k u), τ_k = T + kh, h = 2π/L, L = λl (l = log(T/2π)), k = 0..d−1,
d = LT/2π; window φ even, 0 ≤ φ ≤ 1, supp φ ⊂ [−L/2, L/2]. Matrix (2.20):
G_{kl} = Σ_ρ m_ρ bφ(γ_ρ − τ_k) bφ(γ_ρ − τ_l) = ∫ bφ(τ−τ_k)bφ(τ−τ_l)ν_X(τ)dτ (real symmetric).
**Entries are a Gram-type sum of rank-one outer products u_ρ u_ρ^T, u_ρ = (bφ(γ_ρ − τ_k))_k — not
divided differences.** Role: zero-side reading G = A + E; off-line pair {ρ, 1−ρ̄} contributes a
signature-(1,1) block; n₊(eA) ≤ s₁+s₂+p, rank(eA) ≤ s₁+s₂+2p (Prop 4.1); rank–trace inequality
(Lemma 3.2) + prime-side trace asymptotics ⇒ counting inequalities (Prop 4.4, Thms A–C). **Vertical
(proportion) information at height T.** Generically NOT positive semidefinite (the method works without
positivity — that is its point).

### 3.2 The CvS/CCM operator (Groskin Lemma 2.1; CvS Prop 4.1)

Frequency band {−N, …, N} of trig polynomials on [0, L], L = log c (prime cutoff), size 2N+1.
Q_∞ = Q_prime + Q_pole + Q_arch,∞ with divided-difference source matrices (Q_ψ)_mn = (ψ(m) − ψ(n))/(m − n)
(m ≠ n), ψ′(m) (m = n) — the form (11) verbatim. **Groskin Thm 2.5:** every real even coefficient vector v
determines a band-limited Guinand–Weil test function g_v with ⟨v, Q_∞v⟩ = Σ^*_{ζ(1/2+iz)=0} ĝ_v(z) — every
value of the truncated form is an exact sum over the zeros. (The paper's G has the same "exact zero sum"
property entrywise — the *shared origin*, not a shared mechanism.) Role: the finite-rank window on **Weil
positivity**; ground state is the object of the CvS theorem and of the conjectural limit formula.
**Horizontal (spectral) content.**

Groskin's archimedean-cutoff budget (Cor 3.3): B_T = (2N+1)ρ log(T/2π)/(π²T); finite-T positivity
certifies cutoff-free positivity; a finite-T eigenvalue below −B_T certifies a cutoff-free negative;
(−B_T, 0) certifies nothing. At (c,N) = (100,200) the cutoff-free matrix is certified positive
(n⁻ = 0, Arb LDL^T at 9000 bits) — the negative eigenvalues that motivated that line were tail artifacts.

### 3.3 Suzuki's operator-theoretic refinement (2606.09096)

A_a = Friedrichs extension of B_a = D* G_a D (D = i d/dx, G_a the screw-kernel integral operator) on
L²(−a,a), a = log λ; spectrum discrete, lower-bounded; λ_a = lowest eigenvalue (exists). **Thm 1.4:** for
sufficiently small a > 0, λ_a is positive, **simple**, and the eigenfunction is **even** — the CvS
hypotheses are PROVEN in the small-a regime only. **Thm 1.5 (unconditional):** a different function
W(a,θ;z) (zeros = eigenvalues of a self-adjoint extension of D) has all real zeros, for every a, without
any spectral hypotheses. **Conjectures (OPEN):** the limit formulas (1.2) c_a v̂_a(z) → ξ(1/2+iz) and
(1.12) W(a,θ;z) → ξ/ξ′; the Hilbert–Pólya-via-Weil operator (Cor 1.6: if (1.12) holds uniformly on
compacts, RH follows); the spectral hypotheses for large a.

### 3.4 Terminology trap

"Finite T" means different things: the paper's T is the **height** parameter (interval [T, 2T) of
ordinates); CvS/CCM's T is the **archimedean integration cutoff** in the density
h_+(r) = Re ψ(1/4 + ir/2) − log π. Conflating them produces a false identity between W_T and Q_∞.

---

## 4. Mapping table (CvS/Groskin/Suzuki object ↔ paper object)

| CvS / Groskin / Suzuki object | Paper (C) object | Identification |
|---|---|---|
| Weil Hermitian form W; Q_W(v₁,v₂) = W(v₁∗ṽ₂) | W(f,g) = Σ_ρ m_ρ ĥ_f(γ_ρ)ĥ_g(γ_ρ) (2.2) | **SAME** (the Weil form; explicit formula gives the prime side) |
| CvS operator A of (6)/(11), freq. band {−N..N}, cutoff c = e^L | W_T = G, d×d Gabor compression at heights [T, 2T), d = LT/2π | **DIFFERENT** truncations (frequency vs height), different bases (U_n vs f_k), different matrix structure (divided-difference vs Gram) — Check A |
| ⟨v, Q_∞v⟩ = exact zero sum Σ ĝ_v(zeros) (Groskin Thm 2.5) | G_{kl} = Σ_ρ m_ρ bφ(γ_ρ−τ_k)bφ(γ_ρ−τ_l) (2.20) | **Shared origin** (exact zero sums); different test-function families |
| Ground state ξ of A; conclusion: zeros of ξ̂ real | (no analogue) — C never reads eigenvectors of G | **No counterpart**; C's quantities: tr bG, ‖bG‖²_F, n₊(eG), rank(eA) |
| Spectral hypotheses: λ_a simple, isolated, even (CvS Thm 6.1; Suzuki Thm 1.4 for small a) | No eigenvalue-level hypotheses; only inertia/rank (Props 4.1, 4.4) | **C's tools cannot certify CvS's hypotheses** (B2) |
| Weil positivity ⇔ RH (Weil; Suzuki §1.1) | "RH itself is out of reach of the mechanism" (C §7.5(f)) | Same regime boundary, opposite use |
| Conjectural limits (1.2)/(1.12) → ξ(1/2+iz) / ξ/ξ′ (OPEN) | (none) | **Open conjectures**; the only ζ-connection, horizontal |
| Certificate value v = c₀ + ∫₀¹ r(x)x dx ≤ p₁; ceiling 0.68183123 (close-inclass-gap, attack-lpdual) | the method's output | **CvS provides no input to any of these quantities** (B3, Check C) |

---

## 5. Code-backed checks (mandatory protocol; scripts in `tools/cvs-import/`)

### 5.1 Check A — B1: is the paper's W_T of the CvS divided-difference form (11)?
`tools/cvs-import/check_divided_difference.py`
Run: `uv run --quiet --with numpy python tools/cvs-import/check_divided_difference.py`

A matrix of form (11) satisfies the 3-cycle cocycle (i−j)q_ij + (j−k)q_jk + (k−i)q_ki = 0 for all
distinct i,j,k (equivalently M_ij = (i−j)q_ij has rank ≤ 2). Results (real zeta-zero data
`tools/data/zeros_1_1000.txt`, attack-finitet's verified model — the script reproduces their
tr W/N and ‖W‖²_HS/N tables to 6 decimals, e.g. T=100: 0.992343 / 1.265459):

| object | max 3-cycle residual | rank((i−j)q_ij) | verdict |
|---|---|---|---|
| W_T, T=100 (d=50) | 1.335e+00 (max|W|=1.585) | 50 (full) | **not form (11)** |
| W_T, T=200 (d=123) | 1.439e+00 (max|W|=1.758) | 122 (full) | **not form (11)** |
| single-zero rank-one building block | 1.70e-01 | 1 | **not form (11)** |
| genuine form-(11), N=8 | 4.44e-16 | 2 | form (11) ✓ |
| genuine form-(11), N=40 | 5.00e-16 | 2 | form (11) ✓ |

**Establishes B1 by code:** the paper's W_T (and even its single-zero building block) fails the
divided-difference cocycle by O(1) relative to the matrix scale, with full-rank `(i−j)W_ij`; genuine
form-(11) matrices satisfy the cocycle to machine precision with rank exactly 2. The CvS theorem's
mechanism does not apply to the paper's matrix.

### 5.2 Check B — the CvS mechanism and the essentiality of extremality/simplicity
`tools/cvs-import/check_cvs_mechanism.py`
Run: `uv run --quiet --with numpy python tools/cvs-import/check_cvs_mechanism.py`

(1) The paper's own N=1 toy M(c) = [[0,−1,−1],[−1,c,−1],[−1,−1,0]] (Appendix B.1), c ∈ {2, 0, −1, −3, −5},
for every eigenvector the roots of P(s) = Σ_k ξ_k ∏_{j≠k}(j−s):

- **Extremal (min/max) eigenvectors: P real-rooted for every c.** (e.g. c = −3: min → ±0.7598 real; the
  paper's formulas X(c), Y(c) reproduced.)
- **Non-extremal middle eigenvector: P has non-real roots exactly when c < 0** (c = −1: ±1.5538i;
  c = −3: ±0.7598i; c = −5: ±0.5384i), and its eigenvalue is strictly between the other two — the
  paper's Appendix B.1 statement, reproduced exactly. This is the numerical content of
  **Remark 2.3: extremality/simplicity is essential**.

(2) A guaranteed-PSD form-(11) instance built from a positive combination of the divided-difference
matrices of sin(2πωx) (Groskin Lemma 2.3 family; the single-frequency matrices Q_sin(2πωx) are PSD only
for ω in a narrow upper range — ω ≳ 0.78 at N=1, ω ≳ 0.88 at N=2): Q = Q_sin(0.8) + 1.004265·Q_sin(0.95),
N = 2, eigenvalues [0, 1.261, 5.589, 8.627, 11.619] —
PSD with **1-dim kernel**, ground state ξ = [0.6957, 0.1055, 0.0985, 0.1055, 0.6957] **even**, and
**P-roots ±1.2013, ±0.4007 — all real**. The CvS Thm 5.6 conclusion verified on a genuine instance.

(3) Nulls (recorded): naive random search for PSD form-(11) instances with prescribed 1-dim kernel
(3000 trials) and 2-dim kernel (200k trials) found none — the PSD region is thin; not a failure of the
theorem (which is PROVEN), only of naive sampling.

**Establishes:** I have read the theorem correctly (its mechanism and its essential caveat), verified on
instances and on the paper's own example.

### 5.3 Check C — B3: shadow price of p₁ is exactly 1 (nothing else moves the certificate value)
`tools/cvs-import/shadow_price_probe.py`
Run: `uv run --quiet --with numpy --with scipy python tools/cvs-import/shadow_price_probe.py`

Small LP over the piecewise-linear bandwidth-one class against the 256-law midpoint masses
(`tools/lpdual/law_data.json`; note the row convention: s_mid[j] is the mass at x = (j+1)/256, law rows
1..256 with S(j)/256 = j/65536 — two off-by-one bugs were found and fixed during this check, in line with
the hooks' insistence that the check itself be suspect first):

```
E1(from masses) = -2.543132e-06   (matches stored E1 = -1/393216 exactly)
  p1 = 0.681829 : v* = 0.6818312207   p1+|E1| = 0.6818312306   diff = -9.9e-09
  p1 = 0.700000 : v* = 0.7000025332   p1+|E1| = 0.7000025431   diff = -9.9e-09
  p1 = 0.800000 : v* = 0.8000025332   p1+|E1| = 0.8000025431   diff = -9.9e-09
  p1 = 0.900000 : v* = 0.9000025332   p1+|E1| = 0.9000025431   diff = -9.9e-09
  p1 = 1.000000 : v* = 1.0000025332   p1+|E1| = 1.0000025431   diff = -9.9e-09
```

**v* = p₁ + |E(1)| for every p₁ (to LP tolerance ~1e-8): the shadow price of p₁ is exactly 1, and nothing
else inside the class moves v.** A spectral/zero-location statement about an eigenfunction that does not
raise the certified p₁ cannot change the certificate value. This is the numeric anchor for B3 and for the
claim "even RH does not move the ceiling" (RH supplies only F(α) = 1 on [0,1], which the near-CUE law
already encodes: the midpoint masses are exactly S(j) = j/256).

---

## 6. Adversarial import check (step 3) — the strongest version first

**Strongest version:** "CvS Thm 6.1 + Suzuki Thm 1.4 (small a) + Groskin Thm 2.5 ⇒ the truncated Weil
form's ground state has a real-rooted Fourier transform at every scale; with the conjectural limit
formula (1.2), ξ(1/2 + iz) has real zeros ⇒ RH; and RH-consistent data is exactly the near-CUE input of
the 256-law, so the import must help." The chain dies at B3 (and B1/B2 before it): its successful end is
RH — a *horizontal* statement — and the ceiling is a *vertical* certificate-optimality statement over
configurations matching all bandwidth-one data, which is precisely the data RH supplies. RH does not give
simplicity density, and the ceiling is independent of RH (paper §7.5(f)).

### 6.1 B1 — Object mismatch (fatal, and first in order; Check A)

The CvS theorem's proof mechanism (Carathéodory–Fejér corollary, Toeplitz kernel vectors, D = diag(j),
Shannon sampling of a trig-polynomial eigenvector) requires the divided-difference structure (11). The
paper's G is a Gabor Gram matrix (sum of rank-one outer products), no divided-difference structure, no
natural D = diag(j), no frequency-symmetry x ↦ L − x (its symmetry is height-translation: Poisson
summation, Lemma 2.2). Check A: the cocycle fails by O(1). Even the nearest Toeplitz analogy (the
infinite-height-grid kernel K∞(τ,τ′) = LΦ(τ−τ′) is Toeplitz in k−l) does not rescue it: the associated
"polynomial" lives in the grid index, has no ζ-connection, and the CvS Toeplitz theorem requires PSD,
which G is generically not (off-line zeros give negative eigenvalues — the whole point of the inertia
argument).

### 6.2 B2 — Hypothesis gap (fatal, independent)

The theorem needs λ **simple, isolated, even**:
- at fixed (c, N): a finite-matrix statement, **not proven** (numerically plausible — Groskin Fig 2,
  even-sector eigenvalue flow; CvS Appendix A toy); CvS themselves call verifying it "the key
  difficulty";
- for the limit relevant to RH (a → ∞): Suzuki Thm 1.4 proves it only for **sufficiently small a**; for
  large a it is open, and it is the content of the Hilbert–Pólya-via-Weil conjecture (Suzuki Cor 1.6;
  Connes 2026). Assuming it is assuming the target;
- the paper's tools (inertia on (1,1) pair blocks; rank–trace inequality) bound the **positive index**
  and **rank** — counts of zeros, not spectral fine structure. There is no bridge from index/rank
  counting to eigenvalue simplicity, isolation gaps, or ground-state parity.

### 6.3 B3 — Conclusion orthogonality (fatal, independent, decisive for G1; Check C)

The 0.6818 ceiling is a certificate-optimality statement: v ≤ p₀ + |E(1)|, attained (PROVEN,
close-inclass-gap), with the value pinned 1:1 by p₁ (shadow price exactly 1, Check C). The CvS conclusion
— real zeros of the ground-state Fourier transform — is a zero-location statement about a different
function, on the horizontal axis. It does not and cannot:
- bound p₁ (a count of order N(T,2T) = (T/2π)(l + 2 log 2 − 1) + O(log T); a single eigenvalue/zero-set
  cannot carry a proportion);
- provide F(α) for α > 1 (the theorem never touches pair correlation);
- exclude the 256-law (the law is consistent with ALL bandwidth-one data, including every RH-consistent
  structure: its form factor is exactly CUE, S(j) = j/256, matching Montgomery's unconditional F(α) = 1
  on [0,1]; real zeros of an eigenfunction impose no constraint on the form-factor measure's
  simple-point fraction);
- give multiplicity bounds on ζ's zeros.

**The decisive point:** even a complete proof of RH — the strongest conceivable outcome of the
CvS/CCM/Suzuki route (via the open limit formula (1.2) + Hurwitz) — does **not** move the 0.6818 ceiling.
RH gives horizontal location, not simplicity density; proportions need pair-correlation input beyond the
diagonal (HL*(k₀,λ) / Hardy–Littlewood prime pairs), which is exactly the conjectural datum the ceiling
is measured against. The paper states the complementary direction itself: "RH itself is out of reach of
the mechanism" (§7.5(f)) — and, symmetrically, the mechanism's ceiling is independent of RH.

### 6.4 B4 — the ζ-connection is conjectural

The only bridge from "zeros of ξ̂_N are real" to "zeros of ζ are real" is the open limit formula (1.2)
(Suzuki) / (1.12); Suzuki's unconditional Thm 1.5 builds a different function W(a,θ;z) whose own limit is
a separate open conjecture. Each line has its own open limit; none produces vertical/proportion content.

### 6.5 B5 — evenness

The theorem needs the global minimum to be an even eigenfunction. Q commutes with γ, so even/odd sectors
decouple; whether the global lowest eigenvalue lies in the even sector and is simple there is an unproven
spectral fine-structure statement (numerically plausible — Groskin restricts to the even sector by
construction). Covered by B2.

### 6.6 Steelman verdict

The strongest surviving form of the import is: **CvS Thm 6.1 is the correct rigorous statement of the CCM
spectral mechanism, and it is a real theorem of the RH-horizontal Weil-positivity program.** True, and
recorded (§7). As an import into the proportion-certificate program it is **DEAD** — three independent
fatal blockers (B1 object, B2 hypothesis, B3 orthogonality), each sufficient alone, two of them
code-anchored (Checks A and C). The honest negative is the deliverable.

---

## 7. What survives (the honest positive residue)

1. **CvS is a genuine theorem — of a different program.** CvS Thm 6.1 is exactly the statement Suzuki
   describes as [CCM Thm 5.10], with the full proof (Carathéodory–Fejér corollary → continuous kernel →
   divided differences → Hurwitz) and the honest caveats (Remark 2.3 non-simplicity; Remark 4.3
   symmetrization trap; "key difficulty" = the simple minimal eigenvalue). PROVEN, read at source.
   Check B verifies its mechanism and the essentiality of extremality on the paper's own example.
2. **The actually-useful G6-adjacent certificate mechanism in this literature is Groskin's, not CvS's.**
   Groskin Cor 3.3 (tail budget B_T; finite-T positivity certifies cutoff-free positivity; eigenvalue
   below −B_T certifies a cutoff-free negative) is a genuine certification rule for Weil positivity —
   with the honest caveat that deep spectral scales (10⁻⁵⁹ at c=100) are unreachable by brute cutoff
   (T ≈ 8·10⁶²) and need the cutoff-free LDL^T route (certified n⁻ = 0 at (c,N) = (100,200), 9000 bits).
   This is the correct object to cite when the Riemann program next discusses "SDP/Weil-form certificate"
   (G6): **the CvS theorem is not it.** Note it certifies positivity of the Weil form (RH-horizontal
   type) and produces no proportion bound.
3. **A bounded, checkable, honest sub-task** (low priority, does not change what we believe about the
   certificate): at fixed (c,N), prove (Lean-able, or exact-arithmetic) that the even-sector ground state
   of the truncated Weil matrix is simple and even with a real-rooted Fourier transform — a test of the
   CvS mechanism, not an input to any proportion bound.

---

## 8. Where the import dies, exactly (step 4)

- **B1 (object mismatch):** the CvS theorem is a theorem about the frequency-band truncation Q_∞; the
  paper's W_T is the height-band Gabor truncation G. The theorem does not formally apply to G. Dies at
  §3–§4, Check A.
- **B2 (hypothesis gap):** the hypotheses (simple, isolated, even lowest eigenvalue) are unproven for the
  Weil form except at small a (Suzuki Thm 1.4), are "the key difficulty" (CvS), and are inaccessible to
  the paper's inertia/rank tools. Dies at §6.2.
- **B3 (orthogonality):** even granting every hypothesis and the conjectural limit formula, the conclusion
  carries zero information about the certificate value, which is pinned 1:1 by p₁ (shadow price exactly 1,
  Check C); even RH does not move the ceiling. Dies at §6.3 — decisive for G1, independent of B1/B2.

**Consequence:** the paper-finder's suggestion that the CvS theorem is "a candidate route toward an
SDP/Weil-form certificate (G6) and possibly PAST the 0.6818 ceiling (G1)" is **not supported**. The
ceiling is a certificate-optimality bound (closed in-class); the CvS theorem supplies no certificate and
no beyond-bandwidth-one datum.

---

## 9. Recommended next steps for the program (persistence: redirect, do not abandon)

Per close-inclass-gap.md §5, attack-lpdual.md §6, attack-ceiling.md §4, and attack-multiplicity.md §4 —
unchanged by this note:

1. **Close 0.6725 → 0.6818 formally:** Lean-ize the exact certificate r = 1−x (inclass_attainment;
   ~1 theorem + ~4 lemmas, reusing Stability/Signed/NearCUE/CeilingLaw256 — close-inclass-gap §5).
   Bounded above by p₀ + 1/(6·256²) + τ/512; high verification value.
2. **Adversarially resolve EnclOK** — the single non-Lean link of the ceiling (regenerate the 256-law by
   re-solving its defining LP; validation-enclok.md).
3. **The one documented lever past the walls (attack-multiplicity §4):** attack the third moment tr Â³
   unconditionally in the Rudnick–Sarnak range kλ < 2 (λ < 1 admissible; missing input is the
   triple-correlation asymptotics). Honest framing: the paper says higher moments add nothing on
   (1/2, 1) unconditionally (§7.5(e)); fund only as a long-shot with a kill criterion.
4. **Do NOT re-fund the CvS import** (this note). The CvS/CCM/Suzuki spectral program is tracked as
   G6-adjacent; if the Riemann program ever funds the RH-horizontal line, the correct first tasks are
   (a) Suzuki Thm 1.4-style results for larger a, (b) the limit formulas (1.2)/(1.12) — both open, both
   outside the proportion-certificate framework.

---

## 10. Honesty footer

- **Scripts saved with this note:** `tools/cvs-import/check_divided_difference.py`,
  `tools/cvs-import/check_cvs_mechanism.py`, `tools/cvs-import/shadow_price_probe.py` (self-contained,
  runnable; commands cited in §5). No canonical `tools/` paths owned by other agents were edited.
- **PROVEN (read at source):** CvS Thm 1.2/6.1 and the proof chain; Remark 2.3; Remark 4.3; Prop 4.1
  (matrix (11)); Thm 5.6; Groskin Thm 2.5 and Cor 3.3; Suzuki Thm 1.4, Thm 1.5, Cor 1.6; close-inclass-gap
  exact certificate + ceiling tightness; paper Thms A–D, Prop 4.1/4.4, §7.5(f).
- **CHECKED NUMERICALLY (code run this session, command cited):** Check A table (§5.1), Check B tables
  (§5.2), Check C shadow-price table (§5.3); the attack-finitet model is reproduced to 6 decimals as a
  faithfulness gate; the two off-by-one bugs found in my own probe (Ψ denominator, validity pairing) were
  fixed and are recorded — the check, not the claim, was suspect first.
- **CHECKED NUMERICALLY (cited from prior rounds, scripts exist):** attack-lpdual LP/duals
  (`tools/lpdual/`), finitet tables (`tools/finitet/`), verify_exact_cert.py (exact rationals).
- **CONJECTURED (explicitly open in the sources):** limit formulas (1.2)/(1.12); the Hilbert–Pólya-via-Weil
  operator; the spectral hypotheses for large a; convergence of ground-state zeros to Riemann zeros as
  c → ∞; everything on F(α) for α > 1.
- **ARGUED (this note):** the three blockers B1–B3 and the mapping table; the claim that even RH does not
  move the ceiling (supported by Check C and paper §7.5(f)).
- **No fabrication:** every theorem, constant, and open question cited was read in the listed sources this
  session; the CvS text extraction is preserved at
  `research/papers/cvs-2511.23257-quadratic-forms-real-zeros.txt`.
