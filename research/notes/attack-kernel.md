# Attack: can a better kernel/window beat 0.67250…?

**Agent:** EXECUTIONER (creativity + constraint angle) — Round 1
**Question:** Is 3/2 − (1/√2)cot(1/√2) = 0.67250… improvable by a better test function ψ for the same method?
**Status:** The window choice is **PROVEN** to be at the ceiling of this method (0.67250 is the optimum of the variational problem the proof actually solves); every numerically-better candidate violates a proof constraint. The ξ′-quartic window improves a *different* (ξ′) functional and does not transfer to ζ.
**Compute:** one Rust program, `/home/vstaln/riemann/tools/angle_kernel/` (trapezoid quadrature, N=4001, f64; CG solve for the global minimizer). All numerics below reproducible with `cargo rustc --release --target x86_64-unknown-linux-musl -- -C linker=rust-lld && ./target/.../angle_kernel`.

---

## 1. The variational problem, exactly as posed (PROVEN — Lean)

The OCR-garbled informal note is ambiguous about the functional (it appears to mix a "φ⁴, φ²∗φ²" reading into the main-term claims of Lemma 3.3). The **definitive** statement is the Lean formalization, `Zeta23/ThmD/Functional.lean`, `[eq:cv]` — the scale-free functional of the paper §7.1:

```
c_λ(v) = λ(∫v)² / ( ∫v² + λ² ∬_{[-1/2,1/2]²} |s−s′| v(s)v(s′) ds ds′ ),        v : [−1/2,1/2] → ℝ
```

- maximized over windows v; at λ = 1 this is Montgomery's functional K(0)/(K̂(0)+∫|α|K̂(α)dα), K = |v̂|² (paper §7.1), i.e. **1 / Q(v)** with the quadratic Rayleigh quotient
  **Q(v) = [∫v² + ∬|s−s′|v(s)v(s′)]/(∫v)²**  (this is footnote 3's quotient).
- The HS-norm constant of Lemma 3.3 equals Q(v) (equivalently ‖W‖²_HS = (1/c₁)·N); the rank–trace step then converts it to the proportion **2 − 1/c₁(v) = 2 − Q(v)**. (The brief's c₁* = √2tanϑ/(1+ϑtanϑ), ϑ=1/√2, satisfies 1/c₁* = 1/2 + (1/√2)cot(1/√2).)
- **Constraints of the proof** (all must hold simultaneously): (i) **bandwidth ≤ 1**: supp v ⊆ [−1/2,1/2] (equivalently λ ≤ 1) — needed for Claim 2.1 / the Poisson completion Σₖ φ̂(τ−αₖ)φ̂(τ′−αₖ) = (N/T)φ̂²(τ−τ′), i.e. supp φ_T + supp φ_T ⊆ [−N/T, N/T]; (ii) **evenness** (W_T real symmetric; the identity ∬|s−s′|vv = 2∫₀¹w(v∗v)dw); (iii) **positivity** v ≥ 0 on support ("the constraint v ≥ 0 is inactive" at the cosine — paper §7.1); (iv) C∞ compact support (achieved by the fixed-width end ramp at cost O(1/L), any window).

## 2. Re-derivation of the minimizer and the constant (PROVEN)

Euler–Lagrange for min Q(v), ∫v ≠ 0 (scale-fixed): with A(u) = ∫|u−v|v(v)dv, the first variation gives
**v(u) + A(u) ≡ Q(v)·∫v  on [−1/2,1/2]** (Lagrange multiplier). Since A″ = 2v, differentiating twice forces **v″ + 2v = 0** on the interior: every interior critical point is a cosine **v(u) = a·cos(√2u)** (evenness kills the sine; odd perturbations strictly increase Q by parity, and ∫sin = 0 anyway). For v₀ = cos(√2u)·1_{|u|≤1/2}: v₀ + A ≡ const (value at 0: cos(1/√2) + (1/√2)sin(1/√2)); ∫v₀ = √2 sin(1/√2); so
**Q(v₀) = 1/2 + (1/√2)cot(1/√2) = 1.3274992963205885**, and 2 − 1/c₁* = **0.6725007036794115** (brief: …4116; f64 rounding).

**Global minimality:** the operator I+T, T: v ↦ ∫|·−s′|v(s′)ds′, has spectrum {2/k² > 0 from tanh(k/2)=2/k, k≈2.4} ∪ {−2/k² < 0 from tan(k/2)=−2/k, smallest k≈5.43}, so I+T ≻ 0 (min eigenvalue ≈ 0.93). The constraint ∫v = 1 is a hyperplane; a strictly convex quadratic form with a unique critical point ⟹ the cosine is the **global** minimizer of Q over L²([−1/2,1/2]) — no evenness imposed. Confirmed numerically (below). The paper's "no window does better" cites [CCLM17, Cor. 14] (one-delta extremal problem on [−1,1]).

## 3. Numerics (CHECKED NUMERICALLY — all to ≤ 7·10⁻⁹ of the analytic values)

- Q_quad(v₀) = 1.327499303080 (analytic 1.327499296321); the identity ∫v² + 2∫₀¹w(v∗v)dw = Q₀(∫v)² holds to 5.7·10⁻⁹. Lean moments a* = 0.91872537, b* = 0.84922800, J* = 0.27125615, a*²/(b*+J*) = 0.75329607 ✓.
- **Global minimizer over the free grid (no evenness imposed): Q\* = 1.327499303080; equals cos/∫cos to 1.9·10⁻⁹, max asymmetry 7.8·10⁻¹⁶ (i.e. the unconstrained minimizer is even and is the cosine).**
- c*_λ strictly increasing on λ ∈ (0,1]; max at λ = 1 (the boundary; "λ=1 is forced by the diagonal (Montgomery–Vaughan) evaluation" — transcripts).

### Candidate table (objective Q_quad; proportion 2 − Q_quad)

| window ψ on [−1/2,1/2] | Q_quad | 2 − Q_quad | constraints OK? | verdict |
|---|---|---|---|---|
| flat 1 (box) | 1.333333 | 0.666667 = 2/3 | yes | baseline ("simpler argument") |
| **cos(√2u)** (Montgomery–Taylor) | **1.327499** | **0.672501** | yes (positivity: ≥ cos(1/√2)>0) | **OPTIMUM** |
| cos(λu), λ = 1.0 / 1.2 / 1.6 / 2.0 / π | 1.3290 / 1.3280 / 1.3280 / 1.3346 / 1.4837 | 0.6710 / 0.6720 / 0.6720 / 0.6654 / 0.5163 | yes | worse; min over λ at √2 (Euler–Lagrange) |
| (1−4u²)^k, k = 1..4 | 1.457 / 1.645 / 1.822 / 1.986 | 0.543 / 0.355 / 0.178 / 0.014 | yes | worse (not critical points) |
| ξ′-quartic 1−0.07(2s)²−0.255(2s)⁴ | 1.328182 | 0.671818 | yes | worse on ζ (0.6718 < 0.6725) |
| 1 + u (tilt, non-even) | 1.400000 (= 4/3 + 1/15 exactly) | 0.600 | no (evenness) | worse |
| cos(√2u) + ½sin(πu) (non-even) | 1.445583 | 0.554 | no (evenness) | worse |
| cos(√2u)·1_{|u|≤c}, c = 0.30/0.40/0.45/0.50 | 1.865/1.514/1.407/**1.3275** | 0.135/0.486/0.593/**0.6725** | yes | strictly worse for c < 1/2 |
| c = 0.55/0.60/0.80/1.00/π/(2√2)=1.1107 | 1.268/1.223/1.132/1.112/**1.1107** | 0.732/0.777/0.868/0.888/**0.8893** | **NO — bandwidth** | CONJECTURED DEAD END |

The support formula Q_quad(c) = c + (1/√2)cot(√2c) is exact (analytic, matches numerics to 6 digits); dQ/dc = 1 − csc²(√2c) < 0 on (0, 1/2], so **c = 1/2 is the boundary optimum**, and c > 1/2 keeps improving down to Q = 1.1107 (proportion 0.8893) at the stationary point c = π/(2√2) — **but every c > 1/2 breaks Claim 2.1**: supp φ_T + supp φ_T ⊄ [−N/T, N/T], the Poisson completion acquires aliased modes, and the entire HS main-term derivation collapses. This quantifies exactly what Montgomery's bandwidth-one costs (0.6725 vs 0.8893).

## 4. What the ξ′-quartic window actually does (TASK 4)

Paper Remark 7.3: applied to ξ′ in place of ξ, the same §§4–6 machinery gives ≥ 0.85838 simple-on-line and ≥ 0.92919 distinct (flat window), and **0.86864 / 0.93432 with the quartic window v(s) = 1 − (7/100)(2s)² − (51/200)(2s)⁴**. The flat constant 0.85838 is exactly Farmer–Gonek–Lee's RH-conditional Montgomery constant made unconditional.

- **Mechanism (CONJECTURED — the paper states the constants without derivation; the technical supplement is not in the repo):** for ξ′ the explicit formula has different coefficients (−ξ′/ξ has prime coefficients Λ(n)/√n·(log n + c)-type and a different Stirling/µ part), so the trace ratio functional is *not* c₁ of §2; the ζ-optimal cosine is therefore not optimal there, and a numerically-optimized quartic polynomial (a smooth, positive, bandwidth-one profile) approximates the ξ′-optimizer better than the flat box does.
- **Does the same trick apply to ζ? PROVEN NO.** For ζ the functional is c₁ (Lean-formalized) and its optimizer is the cosine; a polynomial of any degree gives a *worse* quotient (table: 0.6718 and below), consistent with [CCLM17, Cor. 14] ("no window does better"). The quartic trick works for ξ′ precisely because ξ′'s functional is a different object.

## 5. Bottom line (honest)

- **0.67250 is the ceiling of the window choice inside Theorem D's method.** PROVEN: (i) the HS-norm constant equals Q(v) = 1/c₁(v) with the cosine the unique global minimizer of Q (Euler–Lagrange + I+T ≻ 0 convexity; numerically confirmed on a free 4001-point grid to 6.8·10⁻⁹, evenness not assumed); (ii) every candidate that numerically beats the cosine (c > 1/2, λ > 1) violates the bandwidth condition that the proof's Fourier-summation step (Claim 2.1) requires — those are CONJECTURED DEAD ENDS, not improvements.
- The interesting *remaining* gap is **not window-shaped**: the paper's own bandwidth-one ceiling for simple-zero certificates is 0.68185 (PROVEN, Lean `Zeta23/PairCeiling`), while Theorem D reaches 0.6725 — closing 0.6725 → 0.68185 needs a different certificate (more of the configuration/multiplicity structure), not a different test function.
- The quartic window is a real lever for ξ′ (constants PROVEN; mechanism CONJECTURED; source: different explicit-formula coefficients) but does not transfer to ζ.

**Single most promising next step:** attack the 0.6725 → 0.68185 certificate gap (PairCeiling) — e.g. is there a certificate exploiting multiplicity information or higher moments that reaches the ceiling within bandwidth one, without touching the window?

---

## ROUND-3 VALIDATOR CORRECTIONS (from validation-001.md, adversarial pass, all rerun-backed)

- VALIDATOR TARGET (a): the I+T spectrum numbers in this note are CORRECTED — the odd eigenfunctions sin((2m+1)πu) with eigenvalue −2/((2m+1)²π²) were omitted. Min eigenvalue is ≈ 0.797 (not ≈ 0.93); the even root is k ≈ 5.60 (not 5.43). The conclusion (I+T ≻ 0, cosine is the global minimizer) SURVIVES. See validation-001.md target 2.
- VALIDATOR TARGET (b): the "Δ decays to 0 at ~1/log T" reading is INCONCLUSIVE as stated — the note's own fits have nonzero asymptotes (0.014, 0.037, 0.028). Convergence of bound/N to 0.6725 is not demonstrated by the reported data. See validation-001.md target 3.
- VALIDATOR TARGET (c): this note does not mention that EnclOK is the one non-Lean numerical hypothesis in the 0.68185 ceiling; see validation-enclok.md (INCONCLUSIVE, not refuted). See validation-001.md target 5.
- VALIDATOR TARGET (d, verification-001 only): "noise floor" → "Euler–Maclaurin truncation error" (max 6.2e-6 over i≤1000, K=10; collapses at K=14). See validation-001.md target 1.
