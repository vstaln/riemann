# Selberg-class unification theorem (V19) — the axiomatic degree-one theorem

**Agent:** EXECUTIONER (s4h-logic-argument-validation + s4h-epistemology-epistemic-status).
**Vector:** V19 from attack-vector-catalog.md §3 #10 [catalog §3 #10].
**Date:** 2026-08-11 (round 2). **Status:** DELIVERABLE WRITTEN — no kill found (see §8).
**Inputs read in full:** literature-map.md §2 [litmap §2] (the ingredient map), attack-lfunctions.md §4–§5
[lfunctions §4–5] (the GL(2) death), claude-riemann-paper.txt §§1–8 + Appendices A–C [C], the round-1
death ledger [catalog §0, §4], idea-generator-crossdomain.md V19 [crossdomain V19], lean-zeta-23/README.md [Lean].
**Labels:** ingredients **PROVEN** [litmap §2]; the axiomatization **NEW/CONJECTURED** (this document);
the class-level GL(2) corollary **PROVEN** at the level of the formal computation (C Rem 7.2(ii), Prop 7.4),
with one **CONJECTURED** nuance flagged in §7.3. Nothing below claims a new analytic theorem; it is a
reorganization of already-verified results into one axiom-relative statement, plus the audit that V19 demands.

---

## 0. Bottom line (read this first)

There is an axiomatic degree-one theorem — call it **T** — of which the paper's Theorems A–E are instances:

> **T (informal).** Any "degree-one Selberg-class-type object" (an analytic function with a zero multiset,
> conductor datum, and Λ-coefficients) satisfying the five axioms — (A1) functional-equation zero symmetry,
> (A2) Riemann–von Mangoldt density + local density bound, (A3) the explicit formula in spectral form
> (with its archimedean/Stirling data and pole data), (A4) Chebyshev-class coefficient sums, (A5)
> Montgomery–Vaughan off-diagonal control — has, unconditionally from those axioms alone:
> ≥ H(λ) − o(1) of its zeros on the critical line (distinct), ≥ H(λ) − o(1) simple on the line, and
> ≥ max(H_d(λ), F(λ)) − o(1) distinct, for every band-width λ ≤ 1; with the optimal (Montgomery–Taylor)
> window the three constants become 0.6725007…, 0.6725007…, 0.8362503… .

- **ζ satisfies the axioms** (each is a PROVEN theorem: C Prop 2.1, C (1.2), C (2.8)–(2.10), C Lemma 5.1,
  C Lemma 5.2) ⇒ **Theorems A–D are corollaries of T.** [C §1.3, §2–§6]
- **A fixed primitive L(s,χ) satisfies the axioms** (C Thm E proof items (i)–(iii)) ⇒ **Theorem E (and
  Theorem D for L(s,χ)) are corollaries of T.** [C Thm E]
- **A fixed GL(2) object satisfies ALL five axioms** — the death is not an axiom failure. The axioms are
  band-width-relative: the conclusion is H(Λ) with Λ the band in units of the object's mean spacing, and
  Λ ≤ Λ* := lim log T / log q_F(T) = 1/d. For d = 2, Λ* = 1/2 and H(1/2) = −1/6 < 0; the dimension cap
  (C Prop 7.4) bounds *any* certificate of this class at Λ*·N = N/2 on-line points. **The on-line theorem
  is empty for every fixed GL(2) object, whatever the window: the method is strictly degree-one.**
  [C Rem 7.2(ii), C Prop 7.4, lfunctions §4–5]
- **The adversarial audit (§8) finds no kill.** No Selberg-class function satisfies the axioms and violates
  the conclusion; the one axiom not implied by the bare Selberg axioms (S1)–(S5) — A4, the degree-one
  coefficient normalization — is *surfaced* by this document, not silently exploited: it holds for ζ and
  L(s,χ) by direct (Chebyshev–Mertens-level) computation, and the objects it excludes (Davenport–Heilbronn
  type, Σ|b(n)|²/n of the wrong size) are exactly those the method must not certify — and does not
  (the certificate is empty for them; C Rem 7.2(iii)).
- **Lean-ization verdict (§9): suitable, low-risk.** Every component of T is already formalized in
  zeta-23-lean for ζ and for Dirichlet L-functions (the analytic inputs appear as theorems in their own
  right; the linear algebra is a separate module); the incremental work is an abstraction layer
  (a structure type carrying A1–A5 + ζ/L(s,χ) instances), not new mathematics.

---

## 1. The ingredient map (recap, with one discrepancy resolved)

litmap §2 lists twelve ingredients (i)–(xii); the catalog's "11-ingredient map" (the 12-line summary of
[litmap §2]) drops (xii) Paley–Wiener/Gabor, treating it as packaging. We follow the 11-item list and
record the 12th separately. Each is labeled PROVEN in [litmap §2].

| # | Ingredient (PROVEN, [litmap §2]) | Location in C | What it supplies |
|---|---|---|---|
| 1 | Weil/Guinand explicit formula, spectral form | C Prop 2.1 (from [IK04 Thm 5.12], App A) | the bridge: zero-side quadratic form = integral against a prime-powered density |
| 2 | Riemann–von Mangoldt | C (1.2) | normalization: all counts in units of N(T,2T) ≍ (T/2π)log(T/2π) |
| 3 | Stirling for Γ′/Γ | C (2.8), (2.10) | archimedean density µ and its trace integrals ∫µ, ∫µ² |
| 4 | Montgomery–Vaughan generalized Hilbert inequality | C Lemma 5.2 (constant 3π/2) | the off-diagonal prime double sum; **forces λ ≤ 1** (C §7.5(a)) |
| 5 | Montgomery 1973 prime-side moments | C §5 opening, Rem 5.10 | the second-moment evaluation (1/λ + λ/3)N |
| 6 | BGSTB24/GS26 unconditional second moment | C Thm 5.8, Rem 5.10 | the same evaluation holding regardless of zero locations |
| 7 | BGSTB25 box machinery | C §7.4 | the "obstacle is termwise positivity off the line" framing C replaces |
| 8 | Bombieri 2000 negative index | C §1.4, §7.4 | the index/signature reading of truncations of Weil's form |
| 9 | Sylvester inertia + von Neumann rank–trace | C §3 (Lemmas 3.1–3.4) | the NEW linear-algebra engine (rank + positive index + two traces) |
| 10 | Variational window (optimal = Montgomery–Taylor) | C §7.1, Thm D | sharpens 2/3 → 0.67250…; window-only |
| 11 | Chebyshev–Mertens | C Lemma 5.1 | the diagonal prime sums (ΣΛ(n)²/n, ΣΛ(n)², ΣΛ(n)n^{−1/2}) |
| (12) | Paley–Wiener band-limit + Gabor sampling | C Lemma 2.2, (2.1) | window machinery: truncation to n ≤ X, frame identity Σφ̂² = aL² |

§4 assigns each of these to an axiom or to the (non-axiomatic) method. The key structural observation,
already in [crossdomain V19] and confirmed here against C §§4–6: **the method consumes no analytic input
beyond the five axioms.** Everything else — the rank–trace inequality, the window optimization, the Gabor
packaging — is F-independent linear algebra / harmonic analysis that transfers verbatim.

---

## 2. The object and the axiom set (NEW/CONJECTURED as an axiomatization)

### 2.1 The object: a degree-one Selberg-class-type object

A **degree-one Selberg-class-type object** is a datum
F = (F, q_F, c_F, b_F, π_F) consisting of

- an analytic function F with a locally finite multiset of *nontrivial zeros*
  Z_F ⊂ {s : 0 < Re s < 1} with multiplicities m_ρ ≥ 1 (all other zeros disregarded);
- a conductor datum q_F ≥ 1 and a real constant c_F (archimedean data), so that the
  *logarithmic zero-counting function* is
  ℓ_{1,F}(T) := log(q_F T / 2π) + c_F;    [for ζ: q_F = 1, c_F = 2 log 2 − 1, ℓ₁ = log(T/2π) + 2log2 − 1]
- Λ-coefficients b_F : {prime powers} → C (b_F(p^k) the k-th power coefficient of −F′/F),
  extended by b_F(n) = 0 for non-prime-powers;
- a pole indicator π_F ∈ {0, 1} (π_F = 1 iff F has a simple pole at s = 1 of residue 1 in the
  completed-function normalization).

**Notation** (matching C §1.8): N_F(T₁,T₂) = number of ρ ∈ Z_F with T₁ < Im ρ ≤ T₂ counted with
multiplicity; N_{d,F} the same counting distinct points; N*₀,F distinct zeros with Re ρ = 1/2;
N^s₀,F simple zeros with Re ρ = 1/2. For a zero ρ write γ_ρ := (ρ − 1/2)/i = γ − i(β − 1/2), so
γ_ρ ∈ R ⟺ β = 1/2.

### 2.2 The axioms

**A1 (Functional equation / zero symmetry).** The multiset Z_F (with multiplicities) is invariant under
ρ ↦ 1 − ρ̄.  [Used at: zero-side block structure — each distinct on-line point contributes a real
rank-one positive form, each off-line pair {ρ, 1−ρ̄} a real 2×2 block of signature (1,1); the whole
zero-side reading of C §4.1. Note: A1 is the *content* of the functional equation that the method uses;
Bombieri's index observation (ingredient 8) is the historical origin of reading indices of truncations of
Weil's form, and the method uses rank + positive index, both consequences of A1.]

**A2 (Riemann–von Mangoldt + local density).** With N_F as above,
(i) N_F(T,2T) = (T/2π)·ℓ_{1,F}(T) + O_F(log(q_F T));   [the paper's (1.2) and Thm E's N_χ; for the
method only the relative-error-o(1) form is used];
(ii) N_F(t+1) − N_F(t) ≪_F log(q_F(t+3)) for t ≥ 0.  [the absolute-constant local bound that C Prop 4.2
needs for the tail estimate; for ζ it is "[Tit86, Theorem 9.2]", for L(s,χ) C Thm E proof (ii)]

**A3 (Explicit formula, spectral form, with archimedean and pole data).** For every f, g ∈ C_c²(R) with
supp f, supp g ⊂ [−L/2, L/2] (any L ≥ 1) and X := e^L,
```
W_F(f,g) := Σ_ρ m_ρ ĥ_f(γ_ρ) ĥ_g(γ_ρ) = ∫_R ĥ_f(τ) ĥ_g(τ) ν_F(τ) dτ,
ν_F := µ_F + Π_F + P_F ,
µ_F(τ) := (1/2π)[ log(q_F/π) + Re Γ′/Γ(σ_F + iτ/2) ]   (σ_F = 1/4 or 3/4 per the archimedean parity),
P_F(τ) := −(1/π) Σ_{n ≤ X} b_F(n) n^{−1/2} cos(τ log n),
```
with the pole density Π_F(τ) := (1/2π)(1/4+τ²)⁻¹ + (1/π)Re(X^s − 1)/s, s = 1/2 + iτ, if π_F = 1,
and Π_F ≡ 0 if π_F = 0; in both cases |Π_F(τ)| ≪ √X/(1+|τ|) (the C (2.9) bound).  [For ζ this is exactly
C Prop 2.1 with (2.3)–(2.5); for L(s,χ) it is C Thm E proof (i) with ν_{X,χ} = µ_χ + P_{X,χ} and no pole.
The derivation is [IK04 Thm 5.12] as carried out in C App A.]

The archimedean data (ingredient 3) are part of A3:
**A3′ (Stirling data).** µ_F is even, smooth, increasing in |τ|, ≥ µ_F(0) > −1, and
µ_F(τ) = (1/2π) log(q_F|τ|/2π) + O_F(τ⁻²), µ_F′(τ) ≪ |τ|⁻¹ (|τ| ≥ 1);
∫_T^{2T} µ_F = (T/2π)ℓ_{1,F}(T) + O_F(1), ∫_T^{2T} µ_F² = Tℓ_{1,F}²/(4π²)(1 + O_F(ℓ_{1,F}⁻²)).  [C (2.8), (2.10)]

**A4 (Chebyshev-class coefficient sums; the degree-one normalization m_F = 1).** For x ≥ x₀(F):
```
Σ_{n≤x} |b_F(n)|²/n  = (1/2)log²x + O_F(log x),
Σ_{n≤x} |b_F(n)|²   ≪_F x log x,
Σ_{n≤x} |b_F(n)| n^{−1/2} ≪_F √x .
```
[For ζ: C Lemma 5.1 (Chebyshev–Mertens, [MV07 §2.2]); for L(s,χ): C Thm E proof (iii), |b_F(n)| = Λ(n)1_{(n,q)=1}
with O_q errors, which are O(1) for fixed q.]

**A5 (Montgomery–Vaughan off-diagonal control).** The generalised Hilbert inequality holds for the
frequencies {log n : n ≤ X a prime power}, i.e. the off-diagonal prime double sums occurring in the
second-moment evaluation are bounded as in C Lemma 5.2 + Prop 5.6:
for distinct λ_r, δ_r := min_{s≠r}|λ_r − λ_s|, |Σ_{r≠s} x_r z_s/(λ_r − λ_s)| ≤ (3π/2)(Σ|x_r|²/δ_r)^{1/2}(Σ|z_r|²/δ_r)^{1/2};
with {λ_r} = {log n} one has δ_n⁻¹ ≤ 2n, so combined with A4 the O₁ off-diagonal term of the
second moment is O(L²X).  [C Lemma 5.2 is [MV74 Theorem 2] — a universal Hilbert-space inequality, no
hypothesis on F; the "axiom" is only that the framework uses it, and that its F-dependent input
(Σ|b_F(n)|² ≪ X log X) is supplied by A4.]

**Remark (what is NOT axiomatized).** Three parts of the method are deliberately not axioms about F:
- (ingredient 9) the linear-algebra engine — Sylvester inertia under pull-back, the rank–trace inequality
  (von Neumann), the thresholded Cauchy–Schwarz count, Weyl's inequality (C Lemmas 3.1–3.4). These are
  universal statements about Hermitian matrices;
- (ingredient 10) the window optimization — the variational functional c_λ(v) (C (7.3)) and its maximizer
  v*_λ(s) = cos(√2λs) (C (7.4)). Window-only;
- (ingredient 12) the Gabor/Paley–Wiener packaging — the frame identity Σ_k φ̂(τ−τ_k)φ̂(τ′−τ_k) = LΦ(τ−τ′)
  (C Lemma 2.2), the Paley–Wiener bounds (C (2.1)), and the taper profile (C §2.2). Window-only.
All three transfer verbatim to any F and are reused unchanged in the corollaries.

---

## 3. The axiomatic theorem

### 3.1 Statement

**Theorem T (Axiomatic Degree-One Theorem; NEW/CONJECTURED as stated, ingredients PROVEN).**
Let F = (F, q_F, c_F, b_F, π_F) be a degree-one Selberg-class-type object satisfying (A1)–(A5).
Fix 0 < λ ≤ 1 and set L := λ·ℓ_{1,F}(T), X := e^L. Then, for every fixed λ, as T → ∞:

```
(T-A)  N*₀,F(T,2T) ≥ ( H(λ) − o(1) ) · N_F(T,2T),                 [distinct zeros on the critical line]
(T-B)  N^s₀,F(T,2T) ≥ ( H(λ) − o(1) ) · N_F(T,2T),                 [simple zeros on the critical line]
(T-C)  N_{d,F}(T,2T) ≥ ( max(H_d(λ), F(λ)) − o(1) ) · N_F(T,2T),   [distinct zeros]
```
where
```
H(λ)  = 2 − 1/λ − λ/3,   H_d(λ) = (1 + H(λ))/2,   F(λ) = λ/(1 + λ²/3);
H(1) = 2/3,  H_d(1) = 5/6,  F(1) = 3/4,
H_d(λ) ≥ F(λ) ⟺ H(λ) ≥ 0 ⟺ λ ≥ 3 − √6 = 0.55051… .
```
The implied constants and the o(1) depend only on F and λ (through the conductor datum and the fixed
taper profile). **Theorem D form (window-optimal).** With the window ϕ(u) = cos(√2u/l)·ϱ(L/2 − |u|)
(C Thm D), the three constants become 2 − 1/c*₁, 2 − 1/c*₁, (3 − 1/c*₁)/2, where
c*₁ = √2·tan(1/√2)/(1 + (1/√2)tan(1/√2)) = 0.75329606…, 1/c*₁ = 1.32749929…,
2 − 1/c*₁ = 3/2 − (1/√2)cot(1/√2) = 0.67250070…, (3 − 1/c*₁)/2 = 0.83625035…
(all CHECKED NUMERICALLY in this session to 10⁻¹⁵, §10).

### 3.2 Proof assembly (verbatim C §§2–6 with F in place of ζ)

The proof is the paper's, with the only F-dependence occurring at the axiom-tagged points:

1. **Test family and matrix.** Window φ (§2.2, window-only), centers τ_k = T + kh, h = 2π/L,
   d = ⌊LT/2π⌋, f_k(u) = φ(u)e^{−iτ_k u}; define G_kl := W_F(f_k, f_l) via the two expressions of
   (A3) (equality is the content of A3), Ĝ := G/(aL²) with a := (1/L)∫φ².  [uses A3 only]
2. **Zero side (C §4).** Split G = A + E over ordinates in I′ = (T − T^{1/2}, 2T + T^{1/2}).
   - Block structure (Prop 4.1 analogue): by A1, on-line points give rank-one positive forms, off-line
     pairs give (1,1) blocks; by (A3′)-independent window machinery (Lemma 2.2), tr P ≤ N_{on,F}(I′),
     rank P ≤ s₁ + s₂, n⁺(Q) ≤ p.  [uses A1, and the local part of A2 only through the counting below]
   - Tail (Prop 4.2 analogue): ‖Ẽ‖ ≤ θ₀ ≪ l·T^{λ/2−1} using Paley–Wiener (window-only), A2(ii), and
     X^{1/2} = T^{λ/2}.  [uses A2(ii)]
   - Counting inequalities (Prop 4.4/4.5 analogues): the rank–trace device (ingredient 9) applied to the
     (P, Q) decomposition and the (P₁, Q′) regrouping.  [uses A1, A2(ii), method]
3. **Prime side (C §5).** With ν_F = µ_F + Π_F + P_F from A3:
   - tr Ĝ = N_F(T,2T)(1 + o(1))  [Prop 5.3 analogue: uses A3, A3′, A4 (Σ|b_F(n)|n^{−1/2} ≪ √X), π_F data]
   - tr Ĝ² = (1/λ + λ/3)·N_F(1 + o(1))  [Thm 5.8 analogue: Lemma 5.4 (end effects, window-only) +
     Prop 5.5 (M[µ,µ]: A3′), Prop 5.6 (M[P,P]: diagonal from A4, off-diagonal O₁ from A5 + A4, O₂ from A4),
     Prop 5.7 (cross terms: A4, A3′)]
   - (tr Ĝ)²/tr Ĝ² = F(λ₁)·N_F(1 + o(1)), λ₁ = L/ℓ_{1,F} → λ.  [(5.13) analogue]
4. **Assembly (C §6).** Theorem A form: N*₀,F ≥ 4tr Ĝ − ‖Ĝ‖²_F − 2N_F − o(N_F) = (H(λ₁) − o(1))N_F
   (Prop 4.4(ii) + the two trace asymptotics). Theorem B form: same inequality with P₁ (simple zeros only)
   on the rank side (Prop 4.4(ii) with s₁). Theorem C form: Prop 4.4(iii) gives H_d(λ₁) for λ ≥ 3−√6;
   the Cauchy–Schwarz count (Lemma 3.3 + Prop 4.5) gives F(λ₁) for λ < 3−√6; max of the two.
   Theorem D form: window-only optimization (C §7.1) with H replaced by 2 − 1/c*.

**Nothing else is used.** In particular: no zero-density estimate, no zero-free region, no mollifier, no RH,
no pair-correlation conjecture. The theorem is *unconditional given the axioms*, and the axioms are
themselves unconditional theorems for ζ and L(s,χ) (§5, §6).

### 3.3 Sharpness corollaries (class-level, PROVEN in C §7.5, transferred verbatim)

- **(S1) Optimality within the method.** Given only tr Ĝ, ‖Ĝ‖²_F and the block structure, the constants
  of (T-A)–(T-C) are sharp: the configuration of 2/3·N mutually orthogonal simple on-line zeros together
  with 1/6·N on-line doubles realizes tr = N, ‖·‖²_F = 4/3·N, s₁ = 2/3·N, N_d = 5/6·N (C §7.5(b);
  Lean `lemmaR_tight`). Replacing the doubles by off-line pairs of depth → 0 realizes Theorem A's 2/3.
- **(S2) The bandwidth-one ceiling.** No certificate reading only the bandwidth-one data of the method,
  holding configuration by configuration, can certify more than 0.68185 of simple zeros (C Rem 1.1;
  Lean `PairCeiling` modulo the CHECKED-NUMERICALLY `EnclOK` enclosure). So Theorem B's 2/3 sits 0.016
  below its own class ceiling; the gap 2/3 → 1 is structural, not a missing estimate.
- **(S3) The dimension cap.** For any window and any θ ≥ 0: n⁺θ(Ĝ) ≤ d = λ·N_F(1 + o(1)), so no
  certificate of this class can certify more than λ·N_F on-line points, and the Proposition-4.4(ii)
  certificate is at most (2 − 1/λ + o(1))·N_F — non-positive for λ ≤ 1/2 (C Prop 7.4). In particular the
  method cannot distinguish "two thirds" from "all"; RH itself is out of reach of the mechanism
  (C §7.5(a,f)).
- **(S4) Lower-bound nature.** The conclusions certify ≥ 2/3 on the line and say nothing about the
  remaining 1/3 − o(1); they are insensitive to o(N) off-line zeros, and are satisfied by objects with
  false RH analogues that meet the axioms (C §1.5; see §8.3).

---

## 4. Axiom–ingredient map

| Axiom | Ingredients it serves | Role in the proof |
|---|---|---|
| **A1** functional equation / zero symmetry | 8 (Bombieri index), part of 1 (explicit formula), part of 5 (Montgomery zero-side reading) | zero-side block structure: rank-one positive forms on-line, (1,1) hyperbolic blocks off-line; the rank/positive-index reading |
| **A2** RvM density + local bound | 2 (Riemann–von Mangoldt) | normalization to units of N_F; tail estimate (Prop 4.2); dyadic summation |
| **A3** explicit formula (spectral form) | 1 (Weil/Guinand), 3 (Stirling, as A3′), 5 (Montgomery prime-side moments, derived), 6 (BGSTB24/GS26 second moment, derived) | the bridge; the trace and HS-norm are integrals against ν_F; the second moment is *derived* (Thm 5.8), not assumed |
| **A4** Chebyshev-class coefficient sums | 11 (Chebyshev–Mertens) | diagonal prime sums (D-term of Prop 5.6, Prop 5.3's P-part, Prop 5.7 bounds) |
| **A5** MV off-diagonal | 4 (Montgomery–Vaughan) | the O₁ off-diagonal bound; **derives the essential restriction λ ≤ 1** (X ≤ T^{1+o(1)}) |
| (method) rank–trace engine | 9 (Sylvester + von Neumann) | Lemmas 3.1–3.4; not an axiom about F |
| (method) window optimization | 10 (variational window) | Theorem D; window-only, F-independent |
| (method) Gabor/Paley–Wiener packaging | 12 | Lemma 2.2, (2.1), taper; window-only, F-independent |
| (context) box machinery | 7 (BGSTB25) | not an input; the framing C replaces (termwise positivity fails off the line) |

**Key consequence of the map.** Ingredients 5 and 6 — Montgomery's prime-side moments and the BGSTB
unconditional second moment — are *derived statements* in the axiomatic framework: they are exactly the
content of Theorem 5.8, which follows from A3 + A3′ + A4 + A5. The paper's Remark 5.10 states this
explicitly ("Theorem 5.8 is the statement that this evaluation holds for the prime-side expression
regardless of where the zeros are, which is also the content of [BGSTB24, Theorem 1] and of [GS26, Lemma 2]").
The axiomatic theorem therefore does not need a pair-correlation input; it manufactures the second moment
from the axioms. (This is also why the GL(2) transport needs no pair correlation: [lfunctions §3].)

---

## 5. Corollary 1 — the Riemann zeta function (Theorems A–D of C)

**Claim.** ζ satisfies (A1)–(A5). Therefore Theorem T yields C's Theorems A, B, C, D as corollaries.

| Axiom | Instance for ζ | Source (PROVEN) |
|---|---|---|
| A1 | zeros in 0 < Re s < 1; ξ(s) = ξ(1−s) gives the multiset symmetry ρ ↦ 1−ρ̄ with multiplicities | C §1.8, §2.1, §4.1 |
| A2 | N(T,2T) = (T/2π)(l + 2log2 − 1) + O(log T); N(t+1) − N(t) ≤ A₀log(t+3) | C (1.2); C Prop 4.2 ("[Tit86, Theorem 9.2]") |
| A3 | Prop 2.1 with µ, Π_X, P_X from (2.3)–(2.5); A3′ from (2.8), (2.10) | C Prop 2.1, App A (from [IK04 Thm 5.12]) |
| A4 | Lemma 5.1 (Chebyshev–Mertens; [MV07 §2.2]) with b_F = Λ | C Lemma 5.1 |
| A5 | Lemma 5.2 with frequencies {log n}, δ_n⁻¹ ≤ 2n | C Lemma 5.2 + (5.3) ([MV74 Thm 2]) |

**Derivation.** T-A, T-B, T-C with λ → 1 give liminf N*₀/N ≥ 2/3, liminf N^s₀/N ≥ 2/3, liminf N_d/N ≥ 5/6
— exactly C Theorems A, B, C (the paper's H(λ₁) − O(loglogT/logT) error form and the λ<1 improvement come
from the paper's sharper error tracking, which the axiom-relative proof inherits verbatim). The window-optimal
form gives liminf ≥ 2 − 1/c*₁ = 0.67250…, 0.67250…, (3 − 1/c*₁)/2 = 0.83625… — exactly C Theorem D. The
sharpness corollaries §3.3 are C §7.5. [The Lean formalization of the ζ instances exists:
`Zeta23.thmA₀`, `thmB₀_mult`, `thmC₀_mult`, `ThmD.*` — [Lean README].]

---

## 6. Corollary 2 — primitive Dirichlet L-functions (Theorem E of C)

**Claim.** For fixed q ≥ 2 and primitive χ mod q, L(s,χ) satisfies (A1)–(A5). Therefore Theorem T yields
C's Theorem E (and Theorem D for L(s,χ)) as corollaries.

| Axiom | Instance for L(s,χ) | Source (PROVEN) |
|---|---|---|
| A1 | zeros in 0 < Re < 1; the multiset symmetry via the functional equation χ ↦ χ̄ composed with L(s̄,χ) = conj(L(s,χ̄)) | C Thm E proof (ii) |
| A2 | N_χ(T,2T) = (T/2π)log(qT/2π) + O(T) (paper's form; the sharper O_q(log qT) is standard); N_χ(t+1) − N_χ(t) ≪_q log(t+3) | C Thm E statement + proof (ii) |
| A3 | ν_{X,χ} = µ_χ + P_{X,χ}, µ_χ(τ) = (1/2π)[log(q/π) + Re Γ′/Γ(1/4 + κ/2 + iτ/2)], κ = (1 − χ(−1))/2, no pole (Π ≡ 0); A3′ with ℓ_{1,χ} = log(qT/2π) + 2log2 − 1 | C Thm E proof (i) |
| A4 | |b_F(n)| = Λ(n)1_{(n,q)=1}; Lemma 5.1 with O_q errors (finitely many primes removed) | C Thm E proof (iii) |
| A5 | unimodular factors χ(n)n^{±i·} enter the MV bound only through |a_n| | C Thm E proof (iii) |

**Derivation.** T-A/B/C give N*₀,χ ≥ (H(λ) − o(1))N_χ, N^s₀,χ ≥ (H(λ) − o(1))N_χ,
N_{d,χ} ≥ (max(H_d(λ), F(λ)) − o(1))N_χ — exactly C Theorem E; at λ → 1: ≥ 2/3 on the line, ≥ 2/3 simple
on the line, ≥ 5/6 distinct. The window-optimal form is "Theorem D holds likewise" (C Thm E). Note the
uniformity: the archimedean main term (1/2π)log(q|τ|/2π) is independent of the parity κ (the κ-shift lives
only in the O(τ⁻²) term), so A3′ holds uniformly over κ ∈ {0,1} — this is the honest reason the same
constants appear for even and odd characters. [The Lean formalization of the Dirichlet instances exists:
`Zeta23.ThmE.thmE_*`, `Zeta23.ThmDE.*` against Mathlib's `DirichletCharacter.LFunction` — [Lean README].]

**Remark (hybrid range, NOT claimed).** C Rem 7.2(i) notes the proof "appears" to go through uniformly for
q ≤ T^ϑ with band Λ < 1/(1+ϑ) — explicitly unclaimed in C; it is not part of the axiom statement as
formalized here (A2–A4 are stated with fixed conductor data). Honest scope: fixed q. [C Rem 7.2(i), OPEN]

---

## 7. Corollary 3 — the class-level GL(2) death (bandwidth-1/2 statement)

### 7.1 The axioms hold for GL(2); the death is not an axiom failure

Let F be a fixed degree-2 object — a holomorphic newform / elliptic-curve / Maass L-function, conductor
q_F, analytic conductor at height T: q_F(T) ≍ q_F·T². Then (all PROVEN at the level of the ingredients,
[lfunctions §2], [lfunctions §4–5]):

- A1 ✓ (functional equation of the completed function; ρ ↦ 1−ρ̄ symmetry — for non-self-dual forms the
  conjugation argument of §6 applies verbatim);
- A2 ✓ (N_F(T,2T) = (T/2π)log(q_F T²/2π) + O(log(q_F T)) — **twice ζ's density**; CHECKED NUMERICALLY
  against LMFDB zero data for 11a1 and 37a1 in [lfunctions §2(b)]); local bound N_F(t+1) − N_F(t) ≪ log(q_F(t+3));
- A3 ✓ (the standard automorphic explicit formula — the Weil form for GL(2); same contour-integration
  proof as C App A);
- A4 ✓ with m_F = 1 (Rankin–Selberg: Σ_{n≤x}|b_F(n)|²/n = (1/2)log²x + O(log x) and Σ|b_F(n)|² ≪ x^{1+o(1)});
- A5 ✓ (Montgomery–Vaughan is a universal inequality; the frequencies are the same {log n}; the
  F-input Σ|b_F(n)|² ≪ X·X^{o(1)} comes from A4).

**So the GL(2) death is NOT a failure of any axiom.** It is the conclusion of Theorem T becoming vacuous
under the degree-2 density normalization. This is the honest answer to the V19 kill question in the GL(2)
direction: the axioms are band-width-relative, and the band available to a fixed GL(2) object is half a
mean spacing.

### 7.2 The class-level statement

**Corollary 3 (class-level GL(2) bandwidth-1/2 statement; the formal computation is PROVEN in C
[Rem 7.2(ii), Prop 7.4], the assembly is [lfunctions §4–5]).**
For a fixed degree-2 object F with q_F(T) ≍ q_F·T²:
1. **Bandwidth:** the Montgomery–Vaughan wall (A5 + A4) forces the Fourier band L ≤ log T·(1+o(1))
   (X = e^L ≤ T^{1+o(1)}), so the band in units of the object's mean spacing is
   Λ ≤ Λ* := lim_{T→∞} log T / log q_F(T) = 1/2.
2. **Empty on-line certificate:** the (T-A)/(T-B) analogue reads H(Λ) with H(1/2) = −1/6 < 0; the
   dimension cap (S3) bounds any certificate of this class at Λ*·N_F = N_F/2 on-line points, and the
   Prop-4.4(ii) certificate is ≤ (2 − 1/Λ*)·N_F = 0. Hence **no positive proportion of on-line (resp.
   simple-on-line) zeros of a fixed GL(2) form can be certified by this method, unconditionally or
   conditionally** — even under the pair-correlation conjecture or all trace moments (HL*), the ceiling
   is Λ*·N_F = N_F/2 < 2N_F/3 (C §7.5(d,e)).
3. **Degree-one-ness:** the method is non-vacuous for the on-line theorem only if Λ* > 1/2 (and the
   Proposition-4.4(ii) form only if Λ* > 3 − √6 for m_F = 1), i.e. only if d < 2: "it is a degree-one
   method" (C Rem 7.2(ii)). The class-level corollary: **Theorem T is empty for every fixed GL(2) object,
   whatever the window.**
4. **Consistency with C's heuristic:** C Rem 7.2(ii) computes c = Λ/(1 + m_F Λ²/3) = (1/2)/(1 + 1/12) = 6/13
   < 1/2, giving on-line proportion 2 − 1/c = −1/6 < 0 — CHECKED NUMERICALLY here (§10). This is the
   same number as H(1/2) = −1/6.

### 7.3 A nuance the round-1 summary compressed (CONJECTURED)

The round-1 death summary "certifies at most (2 − 1/Λ)N ≤ 0 on-line zeros" [lfunctions §0, §4] is precise
about the **on-line/simple** functionals — and they do die. The **distinct-zero** functional (T-C) is a
different functional: the F(λ)-branch (Cauchy–Schwarz count, C Prop 4.5) at Λ = 1/2 formally gives
N_{d,F} ≥ max(H_d(1/2), F(1/2))·N_F = F(1/2)·N_F = (6/13)·N_F ≈ 0.4615·N_F, which is *not* blocked by the
dimension cap (6/13 < 1/2 = Λ*). **This specific computation is NOT carried out in C** (C Rem 7.2(ii)
computes only the on-line proportion 2 − 1/c and declares it "nothing"); it is my extrapolation of the
paper's Theorem C machinery to the GL(2) normalizations. Label: **CONJECTURED**. It does not resurrect the
on-line target (the s₁ ≥ 2n⁺ − N conversion still gives 12/13 − 1 = −1/13 < 0); it only notes that the
distinct-count functional survives weakly at Λ = 1/2. If a later round wants to pursue it, the honest
prerequisite is a written Rankin–Selberg + MV version of C Thm 5.8 for a fixed form (all ingredients
PROVEN, assembly not carried out anywhere we hold).

---

## 8. The silent-axiom audit (the V19 kill condition)

**Question.** Does any Selberg-class function fail an axiom in a way the method silently exploits — i.e.,
is the method using more than the axioms state, or is some axiom so weak that a bad object satisfies the
conclusions for the wrong reason?

**Verdict: no kill found.** The axioms are exactly the properties the proof consumes (verified line-by-line
against C §§4–6 in §3.2); no step uses an unaxiomatized property of F. Four findings, in increasing order
of significance.

### 8.1 K1 — A4 is not implied by the bare Selberg axioms (the surfaced silent axiom)

The standard Selberg axioms (S1) Ramanujan a(n) ≪ n^ε, (S2) analytic continuation/pole, (S3) functional
equation, (S4) Euler product, (S5) degree-1 normalization — do NOT by themselves force the degree-one
coefficient normalization Σ_{n≤x}|b_F(n)|²/n = (1/2)log²x + O(log x). Under Ramanujan with the *allowed*
θ < 1/2 one can have |b_F(p)| ≍ p^θ log p, for which Σ_{p≤x}|b_F(p)|²/p would not behave like (1/2)log²x.
For ζ and L(s,χ) it is a direct theorem (Chebyshev–Mertens-level, C Lemma 5.1 + Thm E (iii)) — no
classification is needed. **Honest consequence:** Theorem T is a theorem about objects satisfying (A1)–(A5),
NOT about the literal Selberg class as usually axiomatized; A4 is the axiom the method silently needs and
this document makes it explicit. This is exactly the deliverable V19 promised ("surfaces any axiom the
method silently exploits"), and it is surfaced, not exploited: nothing in the proof uses more than A4.

### 8.2 K2 — The control objects (Davenport–Heilbronn) fail A4, and the method under-certifies them (GOOD)

Davenport–Heilbronn-type functions satisfy A1 (functional equation), A2 (ζ-like density), A3 (explicit
formula), but the coefficients of −F′/F grow like x^{1+δ} (zeros exist in σ > 1), so Σ|b_F(n)|²/n is of the
wrong order: **A4 fails**, Prop 5.6 fails, and the certificate is empty (C Rem 7.2(iii)). The method is
therefore *not* fooled into over-certifying an object with provably off-line zeros — A4 is precisely the
boundary that separates genuine degree-one objects from DH-type objects, and the failure direction is the
honest one (under-certification). This is the "proves-too-much" control passing. [C §1.5, C Rem 7.2(iii)]

### 8.3 K3 — Objects satisfying all axioms with false RH analogues receive only a lower bound (no contradiction)

Epstein zeta functions of class number > 1 (degree 2) satisfy A1–A5 (they are GL(2)-type; A4 by
Rankin–Selberg), and their analogues of RH are false. They receive from Theorem T exactly the empty
conclusion of Corollary 3 (on-line certificate ≤ 0) — which is trivially true for them. ζ and L(s,χ)
receive the ≥ 2/3 lower bound, which is a *lower bound*: it remains true even if some of the remaining
1/3 − o(1) are off the line. So the axiom set does not imply RH (as it must not), and no object can make
the conclusion false while satisfying the axioms: the conclusion's only content is a lower bound on the
on-line count, and the on-line count of any zero multiset is ≥ 0. **There is no configuration-theoretic
way to violate (T-A)–(T-C) given (A1)–(A5).** (The axioms determine tr and ‖·‖²_F; the linear algebra
bounds any zero configuration with those two moments — this is the sharpness S1 and the §7.5(b)
extremal-configuration analysis, PROVEN in C and Lean.)

### 8.4 K4 — The A1 symmetry for non-self-dual objects (checked, holds)

For a non-self-dual primitive character (χ complex), the zeros of L(s,χ) are NOT paired within F by the
bare functional equation; the pairing ρ ↦ 1−ρ̄ within L(s,χ)'s own zeros requires the conjugation argument
L(s̄,χ) = conj(L(s,χ̄)) (C Thm E proof (ii), verified in §6). This is a genuine contentful step but it is
PROVEN and covered by C; it is why A1 is stated as "the zero multiset is invariant", not as "the functional
equation pairs zeros of F with zeros of F̄". No silent exploit.

### 8.5 Residual risks (honest, none blocks the theorem)

- The paper itself is the object under validation; Theorem T inherits its epistemic status. The paper is
  stated as PROVEN per its own Lean audit, but the Lean audit of *this* repository (round 1) verified the
  *statements* against the paper; the deeper verification (contour-integration steps, end-effect lemmas)
  is carried by the paper's own Lean files, which we hold but have not re-run. [litmap §5]
- The one non-Lean link in the *ceiling* (not the theorem) is the `EnclOK` enclosure of the 256-law
  (CHECKED NUMERICALLY, [ceiling §1], target M28). It does not affect Theorem T or Corollaries 1–3.
- A4 for L(s,χ) carries O_q errors; fixed-q scope is stated (§6 Remark).

---

## 9. Suitability as a basis for Lean-ization

**Verdict: suitable; low mathematical risk; moderate engineering effort.**

What already exists in zeta-23-lean (all sorry-free, axioms = {propext, Classical.choice, Quot.sound}):
- the linear-algebra core of C §3 (Zeta23/LinAlg: von Neumann trace inequality, both directions of Sylvester
  inertia, rank–trace inequality, Weyl) — written as a self-contained module, exactly the abstraction needed;
- the analytic inputs as theorems in their own right: Weil's explicit formula **for ζ and for primitive
  Dirichlet L-functions** (Zeta23/WeilEF, ExplicitFormula), RvM (Zeta23/RvM), Stirling/Γ′/Γ
  (Zeta23/GammaFacts), Chebyshev–Mertens (Zeta23/Chebyshev, FromPNTPlus), Montgomery–Vaughan (Zeta23/MV);
- the headline theorems for both instances: Thms A–D for ζ (Zeta23/Final, FinalMult, ThmD), Thm E + D for
  L(s,χ) (Zeta23/ThmE, ThmDE), against Mathlib's `riemannZeta` and `DirichletCharacter.LFunction`;
- the ceiling (Zeta23/PairCeiling, modulo EnclOK) — the Lean form of sharpness S2.

What a Lean-ization of Theorem T needs (the *new* work, all mechanical):
1. a structure `DegreeOneSelbergObject` carrying q_F, c_F, π_F, the zero multiset and the Λ-coefficients,
   with the five axioms A1–A5 as fields (propositions over the structure);
2. instances `zeta : DegreeOneSelbergObject` and `dirichlet χ : DegreeOneSelbergObject` — proofs that the
   existing formalized theorems instantiate the fields (A1–A5 are all already theorems in the repo);
3. re-parameterization of the assembly (Zeta23/Assembly, PrimeSideA/B, ZeroSide, Tail) by the structure
   fields — the current proofs are specialized to ζ; the Dirichlet versions already exist, so the
   parameterization is the main effort;
4. the negative GL(2) statement (Corollary 3) — a dimension/bandwidth argument, very Lean-friendly as a
   statement (it is a bound on a certificate from d = λN_F, Prop 7.4's proof being a one-line
   Cauchy–Schwarz), requiring a formal statement of the degree-2 density normalization.

Honest caveats: (i) the ε-form of the existing theorems (∀ε∃T₀∀T≥T₀…) must be lifted to the structure;
(ii) the error-term lemmas (Lemma 5.4 end effects, Prop 5.6 O₁, Prop 5.7 cross terms) are the least
abstracted parts and will take most of the re-parameterization effort; (iii) nothing in the Lean work can
change the epistemic status of the paper itself — Lean-izing T is Lean-izing an already-formalized pair of
instances under a shared header, i.e., low-risk reorganization, not new verification content.

---

## 10. Numerical grounding (all CHECKED NUMERICALLY, this session)

The constants asserted in §3.1 were re-computed (Python, double precision):

| Quantity | Value (this session) | Source value |
|---|---|---|
| c*₁ = √2tan(1/√2)/(1 + (1/√2)tan(1/√2)) | 0.7532960678560707 | C (7.4): 0.7532960… |
| 1/c*₁ | 1.3274992963205883 | C §7.1: 1.3274992… |
| 2 − 1/c*₁ = 3/2 − (1/√2)cot(1/√2) | 0.6725007036794117 (= 0.6725007036794116 via the closed form) | C Thm D: 0.67250… |
| H(1), H_d(1), F(1) | 2/3, 5/6, 3/4 | C (1.3) |
| 3 − √6 (crossing of H_d and F) | 0.5505102572168221; H = 0 (≈ 6·10⁻¹⁶), H_d = F = 1/2 there | C (1.3) |
| H(1/2), H_d(1/2), F(1/2) | −1/6, 5/12, 6/13 = 0.461538… | C Rem 7.2(ii) (c = 6/13) |
| GL(2): c = Λ/(1+m_FΛ²/3) at Λ=1/2, m_F=1; 2 − 1/c | 0.461538…; −0.166666… = −1/6 | C Rem 7.2(ii) |
| 2F(1) − 1 (Cauchy–Schwarz simple-zero ceiling) | 1/2 | C §7.5(c) |
| second-moment normalization 1/λ + λ/3 at λ=1 | 4/3 | C Rem 5.10 |
| 4 − 2 − (1/λ + λ/3) at λ=1 = H(1) | 2/3 | C §6 |

All agree with the paper to 10⁻¹⁵. No new computation was required by this vector (write-up only), per
the round-2 compute discipline ([catalog §5]).

---

## 11. Label inventory (honesty)

- **PROVEN** (in C / [litmap §2] / [lfunctions], as cited): the eleven ingredients; Theorem T's proof
  assembly (it is C §§4–6 re-read through the axioms); Corollaries 1 and 2 (C Thms A–E); Corollary 3's
  formal computation (C Rem 7.2(ii), Prop 7.4) and the degree-2 density (CHECKED NUMERICALLY,
  [lfunctions §2]); sharpness S1–S4; the DH under-certification (C Rem 7.2(iii)).
- **CHECKED NUMERICALLY** (this session): all constants of §10.
- **NEW/CONJECTURED**: the axiomatization itself — the object definition, the five axioms as a *single
  packaged statement*, and Theorem T as a theorem about that structure. (The content is a reorganization
  of PROVEN theorems; the packaging is new and has not been adversarially validated as a unit.)
- **CONJECTURED** (explicitly flagged): §7.3 — the distinct-count F(1/2) = 6/13 survival for a fixed GL(2)
  object (not computed in C); the hybrid q-range of C Rem 7.2(i) (OPEN in C, not claimed here).
- **NOT CLAIMED**: anything about RH itself; any improvement of the constants; any statement about GL(2)
  families (the family-averaged target remains a separate research program, [lfunctions §5]).

**Definition of done (from [catalog §3 #10]) — status:** a written theorem statement + axiom–ingredient
map + corollary derivations for ζ and Dirichlet ✓; the class-level GL(2) bandwidth-1/2 statement recorded
✓; the kill check performed with an honest negative ✓; suitability for Lean-ization assessed ✓. The one
caveat carried forward verbatim: the axiomatization is NEW/CONJECTURED — its components are all PROVEN, but
the packaged statement awaits VALIDATOR review, and the §7.3 nuance awaits a decision on whether to fund
it.

**Honesty footer (hooks/agents.md):** every PROVEN/DEAD/CONJECTURED claim above traces to a cited source
([C §…], [litmap §2], [lfunctions §4–5], [catalog §3 #10], [Lean]). No theorem, lemma, or numerical value
was invented; the axiomatization is presented as a reorganization whose status is labeled; the one new
mathematical extrapolation (§7.3) is labeled CONJECTURED and attributed as mine, not to C.
