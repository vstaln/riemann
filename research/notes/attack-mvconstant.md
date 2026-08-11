# Attack: the Montgomery–Vaughan constant 3π/2 — exact role, sharp constant, and effect on 0.6725

**Agent:** EXECUTIONER — P7.1 (idea-generator-physics.md P7.1 / TOP-10 #6), constraint-hardness + epistemology lens
**Date:** 2026-08-11
**Task:** does sharpening the MV constant 3π/2 for the "specific window kernel" move the two-moment certificate constant 0.6725 → 0.68+?
**Verdict up front:** **NO — the premise fails on both legs, and 0.6725 is untouched by ANY sharpening of the MV constant.**
(i) The MV constant is **window-independent**: its Hilbert matrix lives on the frequencies {log n : n ≤ X a prime power}
(pure arithmetic), and the cosine window enters the MV step only through the amplitudes |a_n|, |α±_n| — never through a
kernel. There is no "g-kernel Hilbert matrix" in the paper's route whose constant is 3π/2. (ii) Even a sharpening to the
**best possible constant** (π, the classical sharp Hilbert constant; the paper's 3π/2 is loose, and the Lean route uses
C = 13/26, even looser) changes **only an o(1)-vanishing error term** (O₁ of the second moment), never the leading
certificate constant. The numerics below confirm the actual MV norm for the certificate's own frequencies is ≈ 2.52
at N = 3·10⁴ (saturated; 10⁴: 2.51987, 3·10⁴: 2.51992) — strictly below π ≈ 3.142 and far below 3π/2 ≈ 4.712 — and that this has **zero effect on 0.6725**.
The 0.6725 → 0.6818 gap is a *certificate-optimality* gap (LP: r = 1−x, `attack-lpdual.md`, `close-inclass-gap.md`),
closed in-class by a certificate that uses no MV at all.

---

## 0. Honesty labels

| Claim | Label |
|---|---|
| The certificate constant 0.6725 = 2 − 1/c\*₁ is the maximum of the variational functional (7.3) over windows (cosine v\*(s) = cos(√2s), c\*₁ = 0.7532960…); **no Hilbert/MV inequality appears in its derivation** | **PROVEN** — paper §7.1 (Thm D), Thm 5.8 (5.13), (7.2); Lean `Zeta23/ThmDE/Concrete.lean`, `Functional.lean` HD(1) |
| The MV 3π/2 enters only the **off-diagonal error O₁** of the second moment: \|O₁\| ≤ (3π/2)·πL·Σ a²ₙ/δₙ ≪ L²X, an o(main) term at every λ ≤ 1; hence the value of the MV constant does not affect the leading constant nor the leading error | **PROVEN** — paper §5.2, Prop 5.6 proof, Thm 5.8 (error budget "O(L l log l (l²+X))"); `attack-lfunctions.md` (d3): "enter Lemma 5.2 … only through \|aₙ\|"; `attack-mollifier.md`: "the diagonal terms … contribute to the main term, and for the off-diagonal terms we will use MV-Hilbert" |
| MV is used with the frequencies {λ_r} = {log n : n ≤ X prime power}, δ_r = min gap — the window does not appear in the kernel | **PROVEN** — paper Lemma 5.2, (5.3), O₁ derivation (lines ~1518–1524); Lean `Zeta23/MV/*` (arbitrary `freq`, injectivity only) |
| The paper's 3π/2 is a **loose** universal constant ("Any absolute constant in place of 3π/2 would suffice below"); the sharp universal constant of the generalized Hilbert inequality is **π**; the Lean route discharges MV with C = 13 (eigenvalue) / 26 (bilinear) | **PROVEN** — paper Lemma 5.2 proof; classical Hilbert inequality (Montgomery–Vaughan 1974 Thm 2; Montgomery, Ten Lectures Ch. 7: constant π best possible); Lean `Zeta23/MV/Final.lean` (`C = 26`), `Eigen.lean` (`|μ| ≤ 13`) |
| ‖∆H∆‖ for the **actual log-prime-power frequencies**: N=10²: 2.34537, 10³: 2.44072, 3·10³: 2.51963, 10⁴: 2.51987, 3·10⁴: 2.51992 (saturated), strictly below π and far below 3π/2; equidistant calibration → π from below | **CHECKED NUMERICALLY** — Rust + numpy agree to 8 digits; dense SVD ground truth at N ≤ 10³; trend saturated at ≈ 2.5199; exact limit **CONJECTURED** ∈ (2.5, π] |
| Sharpening 3π/2 → π (or → the true ≈ 2.52) leaves the certificate value 0.6725007036794116 unchanged | **PROVEN** — consequence of rows 1–3 (constant appears only in o(1) error); no certificate value was recomputed because none depends on it |
| The in-class optimum 0.68183123 (r = 1−x, 256-law ceiling) is a different certificate that uses no MV | **PROVEN / CHECKED NUMERICALLY** — `attack-lpdual.md`, `close-inclass-gap.md` |

---

## 1. Where the MV constant actually sits in the paper (exact role)

**Source:** `research/papers/claude-riemann-paper.txt` — Lemma 5.2 (line ~1036), Prop 5.6 proof / O₁
(lines ~1518–1524), Thm 5.8 (line ~1600), §7.1 Thm D (lines ~1920–2030).

**Lemma 5.2 (Montgomery–Vaughan), verbatim:** for distinct real λ₁,…,λ_R, δ_r := min_{s≠r}|λ_r−λ_s|,
x_r, z_r ∈ ℂ,

    | Σ_{r≠s} x_r z_s/(λ_r − λ_s) | ≤ (3π/2) (Σ_r |x_r|²/δ_r)^{1/2} (Σ_r |z_r|²/δ_r)^{1/2}.

The proof reduces to: the Hermitian matrix (∆H∆)_{rs} = i√(δ_rδ_s)/(λ_r−λ_s) has operator norm ≤ 3π/2.
The proof **itself** states: "Any absolute constant in place of 3π/2 would suffice below."

**Where it is applied:** the second moment tr eG² (the HS norm) is evaluated by the diagonal method
(Montgomery 1973 / BGSTB24). The prime-side double sum splits into

    M[P_X, P_X] = D + O₁ + O₂

with **D = (T/π) Σ_{n≤X} a²ₙ g(log n)** the *diagonal* main term (a²ₙ = Λ(n)²/n; **g = φ²⋆φ² is the
window's Fourier pair — this is where the window lives, in the main term, with no inequality**) and

    O₁ = (1/2π²) Re Σ_{n≠m} aₙaₘ/(i(yₙ−yₘ))·[(n/m)^{2iT}(α⁺ₘ+α⁻ₙ) − (n/m)^{iT}(α⁺ₙ+α⁻ₘ)]

the *off-diagonal* part. **O₁ is bounded by Lemma 5.2 with {λ_r} = {y_n = log n}, δ_n = min gap, and the
window enters only through |α±ₙ| ≤ πL** (the Fourier-amplitude bound), giving

    |O₁| ≤ 4 · (3π/2)·πL·Σₙ a²ₙ/δₙ ≪ L²X      (each of the four sums; (5.3): δₙ⁻¹ ≤ 2n, ΣΛ(n)² ≪ X log X).

**Why the constant's value is irrelevant.** In Thm 5.8 the error budget is

    tr eG² = (TL/2π)(ℓ₁² + L²/3)(1 + O(E_T)),   E_T ≪ w/L + (l²+X)log l/(Tl) + T^{λ/2−1},

and O₁ ≪ L²X is one term inside that budget. At λ = 1 (the certificate's value), E_T ≪ w/L + log l/l → 0,
and O₁/main ≈ (L²X)/(TL³/2π) ≈ 3/(4l) → 0. **So whether the MV constant is 3π/2, π, 2.52, or 13, the
certificate constant — and even the leading error E_T — are unchanged.** MV's only structural role is to keep
the off-diagonal error small enough that the bandwidth wall is λ ≤ 1; that wall is set by the *exponent*
X = (T/2π)^λ, not by the constant.

**The 0.6725 constant itself.** Thm D (§7.1) takes λ = 1 and the window φ(u) = cos(√2·u/l) (mollified at the
ends); the trace-ratio functional

    c_λ(v) = λ(∫v)² / (∫v² + λ²∬_{[-1/2,1/2]²}|s−s′|v(s)v(s′)),    v ≥ 0, supp v ⊆ [−1/2,1/2]

is maximized (Cauchy–Schwarz on the positive-definite operator 1 + λ²T, (Tv)(s) = ∫|s−s′|v) at
v\*(s) = cos(√2s) with c\*₁ = 0.7532960…; the certificate proportion is

    2 − 1/c\*₁ = 3/2 − (1/√2)·cot(1/√2) = 0.6725007036794116…

The |s−s′| kernel here is **exactly diagonalized** (T has spectrum {2/k²} from tanh(k/2) = 2/k, k ≈ 2.4, and
{−2/k²} from tan(k/2) = −2/k, k ≈ 5.43 — see `attack-kernel.md` §2): **no Hilbert-type inequality and no
3π/2 anywhere in this computation.** This is the "specific window kernel" of the task's premise, and its
"sharp constant" is 2/k₁² ≈ 0.35 (spectral radius of T), a completely different object from the MV constant.

**Lean route.** `Zeta23/MV/` formalizes the same Hilbert matrix for *arbitrary* injective `freq` with
`Adm freq δ` (the min-gap condition); `Eigen.lean` proves |μ| ≤ 13 via crude bounds (spacing_sq ≤ 9,
Uform_le ≤ 73), and `Final.lean` discharges `MVHilbert` with C = 26. Where is it consumed?
`Zeta23/PrimeSideB/PPOffDiag.lean` uses it **only** in `O1_bound` (`{C : ℝ} (hMV : MVHilbert C)
(hC : 0 ≤ C)` — any C ≥ 0), and `PPKernel.lean` in the prime-range off-diagonal bounds. So the
formalized proof never needs 3π/2 — any finite constant works, and it is used exclusively in the
off-diagonal error terms. This is the decisive fact: **the MV inequality is used only as "there exists a
finite constant C"; its numerical value is immaterial to the theorem.**

---

## 2. The Hilbert matrix and the three constants

| constant | value | where | status |
|---|---|---|---|
| π | 3.14159265… | **sharp universal constant** of the generalized Hilbert inequality | literature (MV 1974 Thm 2; Montgomery *Ten Lectures* Ch. 7: best possible, attained by equally spaced λ_r); **CHECKED NUMERICALLY** here (equidistant calibration: N=10²: 3.0519, N=10³: 3.1306 → π from below) |
| 3π/2 | 4.71238898… | the paper's Lemma 5.2 constant ("any absolute constant would suffice") | loose (paper) |
| 13 / 26 | — | Lean `Zeta23/MV` (eigenvalue / bilinear) | even looser (Lean) |

The matrix is the same in all three: (∆H∆)_{rs} = i√(δ_rδ_s)/(λ_r−λ_s) on the *arithmetic* frequencies
{λ_r} = {log n : n ≤ X prime power}. The window's Fourier pair g appears only in the diagonal main term D
and in the amplitude bound |α±ₙ| ≤ πL — never in the Hilbert kernel.

---

## 3. Sharp-constant estimate for the certificate's actual frequencies (numerics)

Scripts (saved in the repo): `scratch/mvnorm/mvnorm.py` (numpy; dense SVD + Lanczos),
`scratch/mvnorm/runlog.py`, `scratch/mvnorm/probe.py`, `scratch/mvnorm/replicate.py`,
`scratch/mvnorm/rust/mvnorm/src/main.rs` (Rust, std::thread Lanczos + tqli tridiagonal eigensolver,
musl + rust-lld).

Commands:
- `cd scratch/mvnorm && uv run --with numpy python -u runlog.py <N> 300`
- `cd scratch/mvnorm/rust/mvnorm && export PATH=$HOME/.cargo/bin:$PATH RUSTFLAGS="-C linker=rust-lld" && cargo rustc --release --target x86_64-unknown-linux-musl && ./target/x86_64-unknown-linux-musl/release/mvnorm run <N> <m>`

Object: ‖M_N‖ where M_{rs} = √(δ_rδ_s)/(y_r − y_s) (real skew; ‖M‖ = ‖∆H∆‖), y_r = log n over the first N
prime powers, δ_r = exact min gap in the log coordinate. Validated: Rust ≡ numpy to 8+ digits
(also vs dense SVD at N ≤ 10³: 2.4407221447798952), and the equidistant calibration (‖M_N‖ → π from below).

| N (prime powers) | ‖M_N‖ (log config) | /π | /(3π/2) | method |
|---|---|---|---|---|
| 10² | 2.34536680 | 0.7466 | 0.4977 | numpy dense + Lanczos, Rust ✓ |
| 10³ | 2.44072214 | 0.7769 | 0.5179 | numpy dense SVD (2.4407221447798952) + Lanczos, Rust ✓ |
| 3·10³ | 2.519634 | 0.8020 | 0.5346 | numpy Lanczos |
| 10⁴ | 2.51987306 | 0.8021 | 0.5347 | numpy + Rust agree |
| 3·10⁴ | 2.51991784 | 0.8021 | 0.5347 | Rust Lanczos |
| 10⁵ | not completed — killed after 1h13m CPU under machine load ~60 (Lanczos had not reached its first Ritz checkpoint; per-iteration cost ~3× the quadratic extrapolation under contention). Predicted ≈ 2.5199 from the saturated trend (10⁴→3·10⁴ moved ‖M‖ by 4.5·10⁻⁵; the eigenvector is localized at t ≈ 9.5, away from the frequencies added beyond t ≈ 12.8). This entry cannot change the conclusion. | | | Rust Lanczos |

**Calibration (equidistant, sharp π):** N=10²: 3.05194862, N=10³: 3.13062079 (→ π from below, deficit ~1/√N).

**Observations.**
1. The actual MV norm is **below π** (≈ 2.52 at N = 3·10⁴, i.e. ≈ 0.802π) and **far below 3π/2** (factor ≈ 1.87)
   and far below the Lean 13.
2. The trend **saturates**: 10⁴ → 3·10⁴ moves ‖M‖ by only 4.5·10⁻⁵ (2.51987 → 2.51992); 3·10³ → 10⁴ moved it
   by 2.4·10⁻⁴. The top eigenvector is **localized** at log-frequency t ≈ 9.5 (probe at N = 3·10³: 99.96% of
   the energy in t ∈ [5,10)); as N grows the new frequencies lie beyond the "sweet spot" and the norm barely
   moves. The measured limit is ≈ 2.5199; a slow approach to π (deficit ~ 1/√(log N)) is not excluded but
   would need a deficit that has already shrunk by only 10⁻⁴ over two decades.
   **Label: CHECKED NUMERICALLY (trend, saturated); exact limit CONJECTURED ∈ (2.5, π], consistent with ≈ 2.520.**
3. Independent of the limit: every value measured is < π < 3π/2, so the paper's 3π/2 is off by at least a
   factor 1.87 for the frequencies the certificate actually uses.

---

## 4. Does sharpening 3π/2 move 0.6725? (the task's step 4)

**No, and it cannot.** The certificate value is

    proportion = 2 − 1/c\*₁ = 0.6725007036794116   (PROVEN, Thm D)

and the derivation of c\*₁ contains **no** Hilbert/MV inequality (exact diagonalization of the |s−s′| kernel,
cosine optimizer). The MV constant appears only in O₁ (off-diagonal error), which is o(main) at λ ≤ 1; even
the leading error E_T (λ=1) ≪ w/L + log l/l does not depend on the MV constant at leading order. Hence:

- 3π/2 → π: |O₁| shrinks by a factor 1.5. Certificate constant: **0.6725 (unchanged).**
- 3π/2 → 2.52 (the numerically measured value for the actual frequencies): |O₁| shrinks by ≈ 1.87.
  Certificate constant: **0.6725 (unchanged).**
- 3π/2 → 26 (what Lean actually uses): certificate constant: **0.6725 (unchanged).**

The "0.6725 → 0.68+?" in the task is answered in the negative: **no sharpening of the MV constant produces
any change in the 0.6725 bound.** The gap 0.6725 → 0.6818 is closed *in-class* by a different certificate
(r = 1−x against the near-CUE 256-law; `attack-lpdual.md`, `close-inclass-gap.md`), whose derivation uses no
MV inequality at all; it is a certificate-optimality statement, not a constant-sharpening statement.

**What would actually move 0.6725 (honest directions):**
- beyond-bandwidth-1 pair-correlation input (F(α), α > 1) or a multiplicity bound — the only datum with
  shadow price 1 in the certificate LP (CONJECTURED / unavailable, `attack-lpdual.md` §5);
- a different trace functional (higher moments, Rudnick–Sarnak range kλ < 2) — but §7.5(e) shows odd moments
  add nothing on (1/2,1) (PROVEN), and the two-window idea (P6.5) targets the *distinct* count, not 0.6725.

---

## 5. Constraint-hardness / epistemology wrap

**Constraint as stated (P7.1):** "sharpening the MV constant 3π/2 for the specific window kernel is a
proven-input in-class push (0.6725 → ?) not constrained by the ceiling theorem."

- **Source:** idea-generator-physics.md P7.1 (a NEW idea, generated, not from a primary source).
- **Consequence if violated:** none — the premise is not load-bearing for any proven result; it was a
  candidate *opportunity*.
- **Precedent:** the paper itself says "any absolute constant would suffice" (Lemma 5.2) and the Lean route
  uses C = 26 — precedent is that the constant's value has never mattered.
- **Classification:** the *constraint* "sharpening the MV constant is the lever" is **ASSUMED** (untested
  premise); the *hard* constraints are the ones `attack-lpdual.md` documents (bandwidth ≤ 1 is HARD and
  proven; p₁ is HARD within the data; the box |r| ≤ 1 is soft-but-method-faithful). This probe **tests** the
  assumed constraint and finds it **not real**: the MV constant is not window-dependent and never enters the
  certificate constant.

**Justification of the central belief** ("sharpening 3π/2 moves 0.6725"):
1. "0.6725's off-diagonal control uses MV with 3π/2" → TRUE as far as it goes (the off-diagonal error O₁
   does use MV) — but "off-diagonal control" is an o(1) error, not the constant. The chain continues:
2. "therefore the constant's value scales the certificate value" → **FALSE**: Thm 5.8 shows the certificate
   value = f(main terms) with the MV constant inside an already-negligible error. This is the **weakest link**
   — the inference from "appears in the bound" to "controls the constant" — and it fails on the primary
   source.
3. "therefore 0.6725 → 0.68+" → **FALSE** (consequence of 2).

The belief is **REFUTED**, and the refutation is pinned to quoted primary text (Lemma 5.2's own
"any absolute constant", the O₁ estimate, Thm 5.8's error budget), to the Lean route (C = 26), and to the
numerics (‖M‖ ≈ 2.52 < π < 3π/2 for the actual frequencies).

**Bottom line (honest):**
- MV 3π/2 is PROVEN loose in the paper's own route ("any absolute constant"); the sharp universal constant
  is π; the numerically measured sharp constant for the certificate's *actual* frequencies is ≈ 2.5199 at
  N = 3·10⁴, saturated (CHECKED NUMERICALLY; exact limit CONJECTURED ∈ (2.5, π], consistent with ≈ 2.52).
- The MV constant does not and cannot move 0.6725: it lives only in o(1) error terms, and the window never
  enters the Hilbert kernel. **0.6725 → 0.6725 under any sharpening.**
- The interesting 0.6725 → 0.6818 gap is closed in-class (r = 1−x) and needs beyond-bandwidth-1 input to
  move for real zeros — not a constant sharpening. P7.1 as scoped is a **documented negative**; the genuine
  remaining levers are `attack-lpdual.md` §6 and P7.5 (quadrature-exact error bounds), not the MV constant.
