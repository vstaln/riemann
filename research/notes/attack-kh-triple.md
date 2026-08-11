# Attack: the Karle–Hauptman 3×3 triple-product bound as a P2 price-list on m₃ (vector A1, crystallography catalog)

**Agent:** EXECUTIONER (constraint-hardness-testing + investigation)
**Sources:** `research/notes/idea-generator-crystallography.md` §A1 (the K–H vector, TOP-10 #6),
`attack-nevanlinna.md` (m₃(law) = 1.9545 < 2 would-be separator; the gap is a second-moment gap),
`attack-twobandwidth.md` (m₃(1) = 2, m₃(1/2) = 5, PROVEN closed forms; A3 decomposition),
`attack-multiplicity.md` (m₃ = tr Â³/N, extremal world), `attack-ceiling.md` (§1: what S(j) is;
the 256-law near-CUE rows |256·S(j) − j| ≤ 3·10⁻⁴⁰, D(1) = 0.824).
**Compute:** `tools/kh_triple.py` — `uv run --quiet --with numpy python tools/kh_triple.py`
(new self-contained script; does not touch the shared `tools/m3_*.py`). Supplementary one-offs run in-session
(symbolic verification via sympy; synthetic-configuration and mpmath quadrature checks). Full main-script
output archived at `/tmp/kh_triple_out.txt` this session.

**Verdict up front: RESTATEMENT → DEAD as a new P2 constraint, with a documented clean negative and two
useful byproducts.** The 3×3 K–H determinant is a **tautology** for the true zero configuration (a principal
minor of the PSD Gram matrix — det ≥ 0 always, verified numerically). Its pair-data content — a lower bound on
the real part of every sum-zero triple product — is **strictly weaker than trivial bounds at every in-band
triple** in the near-CUE regime, so it constrains m₃ to nothing. The admissible range of m₃ from near-CUE pair
data **contains 2, 5, and 1.9545 and excludes nothing useful**; in particular it does **not** deliver the
m₃ ≥ 2 that would exclude the 256-law. Two byproducts: (i) an object-discipline clarification — the 256-law
separator m₃ = 4 − 3p₁ is a *multiplicity* (first-order) moment that pair data do not touch at all, so K–H is
the wrong object even in principle; (ii) the connected third moment vanishes exactly at the certificate window,
A3(1) = 0 (PROVEN closed form; CHECKED NUMERICALLY), so at λ = 1 the third moment is *already* two-point data.

---

## 1. The exact inequality (PROVEN — derived, symbolically and numerically verified)

Let the windowed zero measure be μ = Σ_ρ m_ρ δ_{x_ρ} on the rescaled ordinates (mean spacing 1), N = Σ m_ρ,
with structure factors

    E(α) = (1/N) Σ_ρ m_ρ e^{iαx_ρ},   E(0) = 1,   E(−α) = conj E(α).

For any two grid frequencies h, k the 3×3 principal minor of the Gram matrix on index set {0, h, k}
(M_ab = E(α_a − α_b)) is PSD, so its determinant is ≥ 0. Symbolic expansion (sympy, in-session) gives the
**exact K–H inequality**:

    det = 1 − |E(h)|² − |E(k)|² − |E(k−h)|² + 2 Re(E(h)·E(k−h)·E(−k)) ≥ 0          (KH)
    ⟺    2 Re(T) ≥ |E(h)|² + |E(k)|² + |E(k−h)|² − 1,

where the triple product T = E(h)·E(k−h)·E(−k) has frequency arguments h + (k−h) + (−k) = 0 — the
phase-carrying third-order object. Two concrete cases matching the task's "S(0), S(1), S(2), S(3)" rows:
index set {0,1,2} gives 2Re(E₁²·E(−2)) ≥ 2|E₁|² + |E₂|² − 1; index set {0,1,3} gives
2Re(E₁E₂·E(−3)) ≥ |E₁|² + |E₂|² + |E₃|² − 1 (verified numerically on the zeros, §4).

(KH) is an **identity** for the true configuration: the matrix is the Gram matrix of the vectors
(√m_ρ e^{iαx_ρ})_{α∈{0,h,k}}, so det ≥ 0 holds for any measure whatsoever — the phases carry no independent
constraint. This is exactly what the catalog flagged: the K–H *PSD* is automatic (it is B24's F ≥ 0 in matrix
form). The question is whether (KH) as a *pair-data-only* bound on the third-order object has any content.

## 2. The m₃ decomposition — where triple products live (PROVEN / CHECKED)

For the flat-window Gram matrix G_ij = sinc(λ(x_i − x_j)) (all marks simple on the real zeros; the extremal
world adds the mark moments), the trace expansion is exact:

    m₃(λ) := tr G³/N = 1 + 3·A2(λ) + A3(λ),      A2 = (1/N)Σ_{i≠j} G²_ij,   A3 = m₃ − 1 − 3A2,

with A2 the two-point (pair) part and A3 the connected (all-distinct triple-correlation) part — the only
piece (KH) could conceivably bound. Closed forms (PROVEN in `attack-twobandwidth.md`; re-verified here by
mpmath quadrature, in-session):

| λ | m₂ | m₃ | A2 = 1/λ − 2J2 | **A3 = m₃ − 1 − 3A2** |
|---|---|---|---|---|
| 1   | 4/3 | 2   | 1/3          | **0**   |
| 1/2 | 13/6 | 5   | 7/6          | **1/2** |

mpmath: A3(1) = 1.8·10⁻⁶ ≈ 0, A3(1/2) = 0.499995 ≈ 1/2; m₃(1) = 2.0000036, m₃(1/2) = 4.9999928
(CHECKED NUMERICALLY, in-session). **A3(1) = 0 exactly** — at the certificate window λ = 1 the entire third
moment is two-point data, so "the third moment as an independent P2 input" is a mirage at λ = 1 (consistent
with the paper's §7.5(e): odd moments don't lower Λ₁(0)). The connected freedom lives only at λ < 1
(A3(1/2) = 1/2 ≠ 0).

## 3. The admissible m₃ range from near-CUE pair data (CHECKED NUMERICALLY)

**The pair data** (PROVEN for the 256-law; empirically near-CUE for the zeros): grid masses s_j = S(j)/N at
j/N with |256·S(j) − j| ≤ 3·10⁻⁴⁰, i.e. cumulative pair mass C(x) ≈ x²/2, F ≡ 1 on [0,1]. In structure-factor
language this pins the **intensities** |E(α)|². On the real zeros (1000-zero file, flat window) the measured
intensities on the grid α_j = j/N are (CHECKED NUMERICALLY):

    |E(1/N)|² = 0.927   |E(2/N)|² = 0.733   |E(3/N)|² = 0.483   |E(8/N)|² = 0.024
    |E(128/N)|² = 1.1·10⁻⁴   |E(500/N)|² = 5.6·10⁻⁶   mean over j=1..N: 2.8·10⁻³ ≈ 2.8/N

The O(1) low-frequency intensities are the **box-window Fourier shape factor**, not pair-correlation
structure: they match (sin(j/2)/(j/2))² to 4–6 digits, and the same values appear for synthetic even-spaced
and Poisson configurations (0.9194 / 0.9194 / 0.9194 at j=1; CHECKED NUMERICALLY, in-session). Away from the
window's lowest modes the intensities are ≈ 1/N (the decorrelation floor).

**Consequence for (KH):** the RHS (|E(h)|²+|E(k)|²+|E(k−h)|²−1)/2 is ≤ 0 for 79,786 of 79,800 in-band
sum-zero triples (only 14 — the window-shape triples — have positive RHS), and **at every triple the K–H
bound is strictly weaker than the trivial bound** Re(T) ≥ −√(|E(h)|²|E(k)|²|E(k−h)|²) from the 2×2 minors
(min slack −0.5; CHECKED NUMERICALLY). The one place the K–H determinant is nearly tight — det{0,1,2} ≈
3.4·10⁻⁴ vs entries O(1) — is exactly the window-shape regime, and it is **identical for Poisson and
even-spaced configurations** (det ≈ 4.25·10⁻⁴ both), i.e. it carries zero pair- or triple-correlation
information: it is the window's own (two-point) content, already priced.

**Therefore:** the pair data fix the two-point part of m₃, 1 + 3A2 ≈ 1.96 (measured 1.96 on the 1000-zero
band, 1.91 on the 10⁴ high band), and leave the connected part A3 entirely unconstrained at the
|A3| ≤ C₀ level with capacity C₀ = (1/N)tr(|G|³) ≈ 2.1–2.2 at λ=1 (≈ 5.7–6.2 at λ=1/2). The admissible
range of m₃ given near-CUE pair data is therefore

    λ=1:   m₃ ∈ [1+3A2 − C₀, 1+3A2 + C₀] = [−0.17, 4.10]      (1000-zero band; [−0.14, 3.96] on 10⁴ band)
    λ=1/2: m₃ ∈ [1+3A2 − C₀, 1+3A2 + C₀] = [−1.56, 10.77]     (1000-zero band; [−1.29, 10.09] on 10⁴ band)

**Verdict on the three test values (CHECKED NUMERICALLY):**
- **2 is in the range** — the K–H bound does NOT prove m₃ ≥ 2, hence does **not** exclude the 256-law
  (m₃(law) = 1.9545 < 2 would have been excluded by a proven m₃ ≥ 2). The wall stands.
- **5 is in the range** — the corrected sine-kernel λ=1/2 value is admissible at that window.
- **1.9545 is in the range**, and **nothing useful is excluded**: the range is so wide that even the
  marks-restricted interval [1, 4] for the multiplicity moment (below) sits inside it.

**Object discipline (byproduct i):** the 256-law separator is the **multiplicity** moment
m₃^mult = Σ m³/N = 4 − 3p₁ (marks ∈ {1,2}), which is a *first-order* (mark-distribution) object, not a
triple-correlation object: m₃^mult(law) = 4 − 3p₀ = 1.9545, m₃^mult(extremal world) = 2. The near-CUE rows
constrain *positions*, not marks, so pair data do not constrain p₁ at all — the admissible m₃^mult range from
pair data is [1, 4] regardless of K–H. **Even in principle, the K–H triple bound cannot deliver
"m₃ ≥ 2 excludes the law": it bounds the wrong object** (the connected Gram third moment, not the
multiplicity moment). This sharpens the P8.1/nevanlinna conclusion: the only objects that separate the law are
mark moments, and those are first-order data the certificate already reads as p₁ = p₀.

## 4. Numerics on the real zeros (CHECKED NUMERICALLY — `tools/kh_triple.py`)

Data: `tools/data/zeros_1_1000.txt` (primary, N = 1000, γ ∈ [14.14, 1419.42], all simple, flat window) and
`tools/data/zeros_computed_10000.txt` band [9000, 9880] (cross-check, N = 1024). Command:
`uv run --quiet --with numpy python tools/kh_triple.py` (output archived at /tmp/kh_triple_out.txt).

| quantity | 1000-zero band | 10⁴ high band | closed / reference |
|---|---|---|---|
| m₂(1) | 1.3215 | 1.3029 | 4/3 (finite-height deficit, known pattern) |
| m₃(1) | 1.9407 | 1.8972 | 2 (matches attack-twobandwidth ≈ 1.90) |
| A3(1) connected | −0.0239 | −0.0115 | **0** (PROVEN closed form) |
| m₂(1/2) | 2.2025 | 2.1341 | 13/6 |
| m₃(1/2) | 5.1676 | 4.8020 | 5 (matches attack-twobandwidth ≈ 4.80) |
| A3(1/2) connected | 0.5601 | 0.3997 | 1/2 |
| K–H det{0,1,2} | +3.43·10⁻⁴ ≥ 0 | +4.25·10⁻⁴ ≥ 0 | tautology; = window-shape (Poisson same) |
| K–H det{0,1,3} | +2.77·10⁻³ ≥ 0 | +3.41·10⁻³ ≥ 0 | tautology |
| triples with positive K–H RHS | 14 / 79,800 | 14 / 79,800 | vacuous elsewhere |
| K–H vs trivial bound (min slack) | −0.5 | −0.5 | K–H strictly weaker everywhere |
| capacity C₀ = (1/N)tr(\|G\|³), λ=1 / λ=1/2 | 2.14 / 6.17 | 2.05 / 5.69 | pair data leave A3 free at C₀ level |

All determinants ≥ 0 (K–H tautology confirmed on data); the identity in §1 reproduces the literal 3×3
determinants; the empirical m₃ values sit at the finite-height deficit pattern already documented in
`attack-twobandwidth.md` §2.3 (10⁴-file m₃ ≈ 1.90 / 4.80 reproduced here: 1.8972 / 4.8020).

## 5. Constraint hardness (s4h-constraint-hardness-testing)

| Constraint as stated | Source | Consequence if violated | Precedent | Classification |
|---|---|---|---|---|
| "3×3 K–H determinant gives a provable upper bound \|T\| ≤ f(S(j₁),S(j₂),S(j₃)) on the third-moment object from pair data" | idea-generator §A1 (CONJECTURED) | none — the bound's direction is a *lower* bound on Re(T), and it is weaker than the trivial product bound | tested here: never binds; vacuous on 79,786/79,800 triples | **Assumed → refuted (phantom)** |
| "K–H gives an admissible m₃ range excluding the GUE value 2" | task hypothesis | would have killed the ceiling | refuted here: 2 ∈ [−0.17, 4.10] | **Assumed → refuted** |
| "m₃ ≥ 2 (if provable) excludes the 256-law" | attack-nevanlinna §4 | excludes the law | PROVEN true conditional, but m₃ ≥ 2 unprovable; K–H is the wrong object (multiplicity vs connected) | **Hard, but unreachable and mis-targeted** |
| "the connected third moment is a live P2 input" | attack-multiplicity §4 (levers) | — | A3(1) = 0 exactly for the sine kernel; the only freedom is at λ < 1 where K–H is vacuous | **Soft at λ=1 (already two-point), vacuous at λ<1** |

## 6. Bottom line

- **The K–H 3×3 determinant is a RESTATEMENT for the zeros**: det ≥ 0 is an identity (Gram PSD) — verified
  symbolically and on real-zero data (all determinants ≥ 0; the formula of §1 matches the literal minors).
- **As a pair-data constraint on m₃ it is DEAD**: the bound 2Re(T) ≥ Σ|E|² − 1 is strictly weaker than the
  trivial bound at every in-band triple; the admissible m₃ range from near-CUE pair data is
  [−0.17, 4.10] at λ=1 (containing 2 and 1.9545) and [−1.56, 10.77] at λ=1/2 (containing 5);
  **nothing useful is excluded**. The near-tightness of the lowest-frequency determinant is the box-window
  shape factor (identical for Poisson / even-spaced / real zeros) — window content, not third-moment content.
- **Byproduct (i) — object discipline:** the 256-law separator m₃ = 4 − 3p₁ is a *multiplicity* moment; pair
  data do not constrain it (marks ≠ positions), and the K–H triple bound cannot reach it. The m₃ ≥ 2 route
  to excluding the law is closed twice over: unprovable (paper §7.5(e), attack-nevanlinna) and mis-targeted
  (a connected-third-moment bound cannot deliver a mark-moment statement).
- **Byproduct (ii) — structural:** A3(1) = 0 *exactly* for the sine kernel (PROVEN closed form, mpmath-
  verified), i.e. at the certificate window the whole third moment is two-point data — an independent
  confirmation of §7.5(e)'s "odd moments add nothing" from the moment side.
- **Labels:** PROVEN — (KH) determinant identity; A3(1) = 0, A3(1/2) = 1/2 (closed forms, from
  attack-twobandwidth's m₃ forms; mpmath-re-verified). CHECKED NUMERICALLY — all numbers in §§2–4
  (script `tools/kh_triple.py`, command cited; synthetic checks in-session). REFUTED — the A1 hypothesis that
  K–H prices m₃. VERDICT: **RESTATEMENT → DEAD as a new P2 input; the 5/6 (distinct) and 0.6818 (simple)
  walls stand.**

*Persistence note: a documented negative, not a stop. The catalog's A1 probe is closed; the live P2 levers
remain the beyond-bandwidth-1 arithmetic input (M29/B10 flank) and the λ < 1 Gram-moment machinery where the
connected part is nonzero but unconditionally inaccessible past the Rudnick–Sarnak range — both already on the
standing roadmap. The crystallographic transfer's *diagnostic* siblings (A2 Sayre-residual, A4/A5 window
decomposition) remain untouched and cheap.*
