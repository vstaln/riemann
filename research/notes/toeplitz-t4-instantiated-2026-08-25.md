# Toeplitz T₄ at rung b=4 — First Instantiation Attempt (Shared Normalization m₀=1)

**Date:** 2026-08-25
**Source lens:** `toeplitz-b4-probe-2026-08-25.md` (Tier 3, rung b=4 — the
NEVER-INSTANTIATED Borodin–Okounkov reduction, §4, tasks 1–3)
**Method:** exact rational arithmetic only (`fractions.Fraction`; Bareiss
determinants cross-checked against full Leibniz expansion on every 4×4),
read-only.
**Verdict (label):** **INSTANTIATED_BROKEN** — the moment-to-Fourier map
fails provably; no positive symbol exists for either side in any
normalization. Precise failure point: entry condition `|a₁| ≤ a₀` of
Toeplitz-PSD (CUE saturates `|a₁|=a₀=1`, which forces a single point mass
and contradicts a₂=4/3; extremal violates it outright). T₄(CUE) = −5/81 < 0,
NOT > 0.

---

## 0. Bottom line

| Object | CUE (sine-kernel moments) | Extremal 5/6 config | Status |
| :--- | :--- | :--- | :--- |
| moments m₀..m₄, shared m₀=1 | (1, 1, 4/3, 2, 346/105) | (1, 6/5, 8/5, 12/5, 4) | PROVEN |
| det H₃ (Hamburger Hankel) | +58/945 (> 0, PD) | 0 (rank 2 collapse) | PROVEN |
| det T₄ (Toeplitz, a_k=m_|k|) | **−5/81** | **−27/625** | PROVEN |
| leading minors det T₁..T₄ | 1, 0, −1/9, −5/81 | 1, −11/25, +21/125, −27/625 | PROVEN |
| positive symbol exists? | **NO** (PROVEN) | **NO** (PROVEN) | REFUTED |

The b=4 probe's §4 requirement — "compute T₄ > 0 with the correct sign
signature for the CUE/sine-kernel symbol" — **fails at the identification
step**: T₄(CUE) = −5/81 < 0, and no positive symbol can exist whose Fourier
coefficients are the moment sequence. The Hankel-side discriminator
(58/945 vs 0) survives intact, but it is a Hamburger-moment statement, not
a Toeplitz/Borodin–Okounkov statement.

---

## 1. Task 1 — the atom weights behind m₄ (PROVEN, but asymmetric)

**Extremal 5/6 config (PROVEN).** Weights (2/3, 1/6) at multiplicities
{1, 2}, from `fourth_moment_analysis.md` §3.1: s₁ = 2N/3 simple atoms of
weight 1, s₂ = N/6 double atoms of weight 2, total N_tot = N, distinct mass
N_d = 5N/6. Power sums m_k = (2/3)·1^k + (1/6)·2^k:
m₀ = 5/6, m₁ = 1, m₂ = 4/3, m₃ = 2, m₄ = 10/3. ✓ (m₄ = (2/3)·1⁴ + (1/6)·2⁴.)
Shared normalization m₀=1: divide by 5/6 → probability weights (4/5, 1/5)
at {1,2}: m = (1, 6/5, 8/5, 12/5, 4).

**CUE m₄ = 346/105 (PROVEN: NO finite-atom representation).** 346/105 is a
*continuous-process* trace moment of the sine-kernel determinantal process,
assembled from diagram pieces (1 + 6A₂ + B₂ + 4A₃ + 2C₃ + A₄ = 1 + 2 + 2/3 −
13/35), per `fourth_moment_analysis.md` §2. It has **no atom-weight reading**,
by two independent arguments:
1. Any atom config on positive integers with m₀ = m₁ = 1 must be the point
   mass at 1 (Σw = 1, Σw·x = 1, x ≥ 1 ⇒ all x = 1), forcing every moment
   = 1 ≠ 4/3. No finitely-supported multiplicity config can match CUE m₀..m₄.
2. The 2-atom fit at {1,2} (which is precisely the extremal) is pinned by
   (m₁,m₂,m₃) and gives m₄ = 10/3 ≠ 346/105.

So "atom weights behind 346/105" do not exist; the CUE side is a measure,
the extremal side is a sub-mass atom configuration — exactly the m₀ caveat
the probe flagged (§2), now proven to be unfixable by any atom model.

---

## 2. Task 2 — Hankel moment matrices on shared normalization m₀=1 (PROVEN)

H₃ = (m_{i+j})_{0≤i,j≤2}, and det H₂, det H₃:

| side | m₀..m₄ | det H₁ | det H₂ | det H₃ |
| :--- | :--- | :--- | :--- | :--- |
| CUE | (1, 1, 4/3, 2, 346/105) | 1 | 1/3 | **+58/945** |
| EXT raw (m₀=5/6) | (5/6, 1, 4/3, 2, 10/3) | 5/6 | 1/9 | **0** |
| EXT normalized (m₀=1) | (1, 6/5, 8/5, 12/5, 4) | 1 | 4/25 | **0** |

- Sign test passes: CUE PD (all principal/minor determinants > 0), extremal
  rank-2 collapse, in **both** normalizations. The 58/945 vs 0 separation is
  renormalization-invariant as a *structural* (PD vs rank) statement. ✓
- **Cost of the fix:** under shared m₀=1 the extremal moments become
  (6/5, 8/5, 12/5, 4) — the lower-moment degeneracy (m₁,m₂,m₃) = (1, 4/3, 2)
  that made the b=4 test sharp **evaporates**. The "identical lows, split at
  m₄" structure exists only in the unnormalized comparison the probe flagged.
  What survives is only the structural test (det > 0 vs det = 0).

---

## 3. Task 3 — the Borodin–Okounkov step: moments as Fourier coefficients (PROVEN: FAILS)

Standard identification tested: a_k = m_k for |k| ≤ 6 (real even moments ⇒
a_{−k} = a_k), giving the Toeplitz Tₙ(a) = (a_{i−j}) = (m_{|i−j|}).

**CUE** (m₀..m₃ = 1, 1, 4/3, 2):
T₄ = [[1,1,4/3,2],[1,1,1,4/3],[4/3,1,1,1],[2,4/3,1,1]]
- det T₁..T₄ = **1, 0, −1/9, −5/81** (Bareiss ≡ Leibniz). T₂ is singular
  (rows of [[1,1]] twice), T₃ and T₄ negative.
- **T₄(CUE) = −5/81 < 0** — the required "T₄ > 0" does NOT hold.
- Principal-minor PSD test: negative 2×2 minors (e.g. {0,2}: det = −7/9),
  negative 3×3 and 4×4 minors. Indefinite, not PSD.

**Extremal, normalized m₀=1** (m₀..m₃ = 1, 6/5, 8/5, 12/5):
T₄ = [[1,6/5,8/5,12/5],[6/5,1,6/5,8/5],[8/5,6/5,1,6/5],[12/5,8/5,6/5,1]]
- det T₁..T₄ = **1, −11/25, +21/125, −27/625**. det ≠ 0 (rank 4, indefinite);
  every 2×2 principal minor negative.
- Note: THIS side exhibits the strict alternating-sign leading-minor pattern
  (+, −, +, −) that the probe's §4 asked the *CUE* side to display — an
  inversion of the anticipated structure: alternation of det Tₙ is the
  fingerprint of a **non-positive** symbol, the exact opposite of what a
  sine-kernel/BO certification needs (positive symbol ⇒ det Tₙ > 0 for all n).

---

## 4. Precise failure point — why no positive symbol exists (PROVEN)

Necessary condition: if a(z) = Σ a_k z^k is the symbol of a **positive**
measure on the unit circle, then every Tₙ(a) is a Gram matrix of
{1, z, …, z^{n−1}} in L²(ν), hence PSD, hence |a₁| ≤ a₀ and det Tₙ ≥ 0.

- **CUE:** a₀ = a₁ = 1 ⇒ |a₁| = a₀ (equality). Equality in |a₁| ≤ a₀ for a
  positive measure forces ν to be the point mass at z₀ = a₁/a₀ = 1, whence
  a_k ≡ 1 for all k — contradicting a₂ = 4/3. Equivalently: det T₂ = 0
  (singular) but det T₃ = −1/9 < 0, impossible for a PSD Toeplitz. ∎
- **Extremal (m₀=1):** |a₁| = 6/5 > a₀ = 1 — violates the condition at the
  **first** nontrivial order. (Raw m₀=5/6 version fails the same way:
  a₁ = 1 > a₀ = 5/6.)

**Therefore no positive symbol exists for either side, in any normalization,
and the moment-to-Fourier map m_k = a_k is provably broken.** Root structural
cause: Fourier coefficients of a probability measure are bounded by a₀ = 1,
while Hamburger moments of a spread measure grow (m₂ = 4/3, m₃ = 2 > m₀).
The two sequences are different species of object; the b=4 probe's §4
conjectured identification cannot hold.

---

## 5. The natural sine-kernel symbol — sanity check (PROVEN)

The genuine sine-kernel Toeplitz (kernel S(x−y) = sin π(x−y)/(π(x−y))) has
entries a_k = S(kΔ) = sin(πkΔ)/(πkΔ) (Fourier coefficients of the symbol
1_{[−1/2,1/2]} at spacing Δ):
- Δ = 1: a_k = 0 for k ≥ 1 ⇒ Tₙ = Iₙ — trivially positive, carries **no**
  moment information.
- Δ = 1/2: a₁ = 2/π ≈ 0.637 ≠ m₁ = 1 — the moment sequence is not the
  symbol's coefficient sequence at any spacing.

The m_k(λ) are **trace moments of the windowed kernel operator**
(spectral statistics at separation λ), a different object from the Toeplitz
symbol coefficients. A real BO instantiation must compute the Fredholm
determinant of the sine kernel (via its eigenfunction symbol), not set
m_k = a_k — that route remains unformulated (probe §3 stands, with one repo
correction below).

---

## 6. Repo correction (honesty): the repo DOES contain a Toeplitz route — but not the BO object

Grep of `~/.cache/checkouts/github.com/JoshuaHKU/zeta-density-one-reproduction`
finds a real "Toeplitz–trace route": `repro/engines/p3_direct_sum.py`,
`repro/gates/g_tt.py`, `repro/engines/sample_model.py`. The probe's "no
Toeplitz anywhere" is outdated **in letter**. In substance the probe's finding
stands: that route computes the *Haar-random U(N) eigenangle* trace moments
m_b(N) via the isospectral Toeplitz G′_{mn} = t_{m−n} with t_k = (1/N) tr U^k
(mean t_k = 0 for k ≠ 0, so the mean matrix is the identity — the moments
come from walk expansions of tr(G′)^b, not from symbol-coefficient
determinants). It certifies m₄..m₁₄ / Σ₉..₁₁ (`paper.tex` conv (vii),
`certify91.py` — "Toeplitz–trace rungs"). The **Borodin–Okounkov sine-kernel
minor object** Tₙ = det(a_{i−j}) with symbol coefficients is still computed
nowhere in the repo or in `research/notes/` (this note's values are the first).

---

## 7. What INSTANTIATED_AND_CONSISTENT would have required — and the honest status

For the b=4 certification to go through via TO, one would need, for the
CUE/sine-kernel side, a genuine symbol (built from the kernel's
eigenstructure — the prolate/BO route, not moment-pasting) with det T₄ > 0
and all principal minors positive, matching the arithmetic side order by
order. That chain remains NOT_FORMULATED. What **is** now PROVEN:

1. The moment-Hankel discriminator 58/945 vs 0 is exact, renormalization-
   invariant as a structural test, but loses its low-moment sharpness under
   the m₀=1 fix (the probe's own caveat, now quantified: (1,4/3,2) →
   (6/5,8/5,12/5)).
2. The probe §4 identification (moments = Fourier coefficients) is
   **provably broken** for both sides in every normalization — the failure
   point is the Toeplitz-PSD entry condition (CUE: saturation |a₁|=a₀ ⇒
   point mass ⇒ contradiction at a₂; extremal: |a₁| > a₀ outright).
3. Under that identification, T₄(CUE) = −5/81 < 0 (NOT > 0), and the
   alternating-sign pattern the probe expected from CUE appears instead on
   the **extremal** T₄ — the signature of a negative symbol, the wrong sign
   for a sine-kernel story.

**Verdict: INSTANTIATED_BROKEN.** The Borodin–Okounkov reduction at rung
b=4, instantiated by the only identification the probe supplied, fails at the
moment-to-Fourier step with a *proof* of no-positive-symbol (not merely
"not found"). Sub-label: SYMBOL_NOT_IDENTIFIED for any alternative symbol;
the genuine BO kernel-eigenfunction route remains unformulated.

---
**Labels used:** PROVEN = exact rational arithmetic re-derived here (Bareiss
cross-checked vs Leibniz on all 4×4) or elementary proof. REFUTED = claim
contradicted by a proven fact above. INSTANTIATED_BROKEN = reduction fails at
a precise, pinned step. NOT_FORMULATED = no instantiating formula exists.