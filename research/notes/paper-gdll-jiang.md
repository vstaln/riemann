# Paper assessment — GdLL 2303.01095 & Jiang 2507.20653 vs the program walls

**Date:** 2026-08-11 (round 2.5). **Agent:** EXECUTIONER (paper adjudication).
**Status:** BOTH READ IN FULL; verdict written; NO WALL MOVES. Arithmetic cross-checks CHECKED NUMERICALLY
(script below). No claim about the papers' *content* is made without the VERIFIED-FROM-PAPER label; their
*validity* is NOT independently validated here (GdLL is peer-reviewed, Math. Comp. 94 (2024) 2041–2058;
Jiang is arXiv v1 preprint, unrefereed — see §8).

**Sources read (full text, extracted with pypdf via uv — `pdftotext` binary absent on this machine):**
- `research/papers/gdl-2303.01095-multiplicity-higher-level-correlations.pdf` (18 pp; arXiv:2303.01095v2, 20 Mar 2025; published Math. Comp. 94 (2024) 2041–2058)
- `research/papers/jiang-2507.20653-hypothesis-H-rudnick-sarnak.pdf` (35 pp; arXiv:2507.20653v1, 28 Jul 2025)

**Verification script:** `research/notes/paper-gdll-jiang-verify.py`
**Command:** `uv run --quiet --with mpmath python research/notes/paper-gdll-jiang-verify.py`
(checks: Theorem-D constant; the identity 0.6725 = 1 − c₂,₁; Theorem-1 arithmetic for all three (n,m) rows;
the N₃ bound; the under-RH 67.92%; all comparisons.)

---

## 1. GdLL (2303.01095) — main theorems (VERIFIED-FROM-PAPER)

**Objects.** For an irreducible cuspidal automorphic representation π of GL_m/Q, its L-function L(s,π)
(generalizing Dirichlet L-functions at m = 1; ζ is the trivial-character case, see §8 caveat). Zeros
ρ_j = 1/2 + iγ_j (j ∈ Z), enumerated *repeated according to multiplicity*; N(T) = Σ_{γ_j ≤ T} 1;
m_ρ = multiplicity of ρ; N*(T) = Σ_{γ_j ≤ T} m_{ρ_j}; Z_n(T) = #{γ_j ≤ T : m_{ρ_j} ≤ n−1}.

**Input — the Hejhal/RS n-level correlation (eq. (1), VERIFIED-FROM-PAPER):** under GRH for L(s,π) and
Σ_p |a_π(p^k) log p|²/p^k < ∞ for all k ≥ 2 (the latter unconditional for m ≤ 3, RS Prop. 2.4):

```
(1/N(T)) Σ_{j_1,…,j_n distinct, γ ≤ T} f((m log T/2π)γ_{j_1}, …, (m log T/2π)γ_{j_n})
   → ∫_{R^n} f(x) W_n(x) δ((x_1+…+x_n)/n) dx_1…dx_n ,
```
with W_n(x) = det[sin π(x_i−x_j)/(π(x_i−x_j))] (Dyson GUE density) for admissible f with
supp(f̂) ⊆ {x : |x_1|+…+|x_n| < 2/m} (the RS support range). **This asymptotic is itself stated under GRH.**

**Theorem 1 (verbatim, VERIFIED-FROM-PAPER):**
> "Let L(s, π) be the L-function attached to an irreducible cuspidal automorphic representation π of
> GL_m/Q. Assuming GRH for L(s, π) we have
> lim inf_{T→∞} Z_n(T)/N(T) ≥ 0.9614 if n = 3 and m = 1, 0.2997 if n = 3 and m = 2, 0.9787 if n = 4 and m = 1,
> where the results for (n, m) = (3, 2), (4, 1) hold under the additional assumption that certain series of
> rational functions are summed correctly using Maple; see Section 6."

So for ζ (m = 1, n = 3): **under RH, ≥ 96.14% of zeros have multiplicity ≤ 2** (simple or double),
improving the Conrey–Ghosh–Gonek 95.5% [12] (both conditional). The (3,2) case is the first effective
multiplicity bound for GL2 L-functions. Mechanism: M_n(T) := Σ_{distinct, γ_j1=…=γ_jn ≤ T} 1 =
Σ (m_ρ − 1)⋯(m_ρ − n + 1); the diagonal f(1,…,1) term forces
limsup M_n/N ≤ c_{n,m} := inf (1/f(1,…,1)) ∫ f W_n δ; then Z_n/N ≥ 1 − c_{n,m}/(n−1)!.

**Constants (VERIFIED-FROM-PAPER):** c₃,₁ ≤ 0.077197284 (poly parametrization, degree 60, Table 1) and
≤ 0.077213324 (shift parametrization, Table 2, d = 5); c₃,₂ ≤ 1.400506625; c₄,₁ ≤ 447/3500 ≈ 0.1277
(λ = 0 only; numerically-estimated limit ≈ 0.026 → Z₄/N ≈ 0.9956). Moment bounds (6): limsup N₃/N ≤
2.0597 (3,1), 5.8984 (3,2), 3.8834 (4,1), "provided the hypothesis of Theorem 1 hold" (i.e., under GRH).

**Theorem 2 (verbatim, VERIFIED-FROM-PAPER):** "For n, m > 0 there exists a kernel K : C^{n−1} × C^{n−1} → C
such that g(w) = ∫ g(v) K(w,v) dν_n(v) for all g ∈ PW((1/m)H_{n−1}) … We have c_{n,m} ≤ 1/K(0,0), and equality
is attained if every nonnegative g ∈ L¹(Rⁿ) with supp ĝ ⊆ (2/m)H_{n−1} is a sum of squares" (condition (8)).
**n = 2 closed form (Section 3, VERIFIED-FROM-PAPER):** K(0,0) = 1/((1/√2)cot(1/√(2m)) − (2m−1)/(2m));
for m = 1 this gives c₂,₁ = 0.3274992963… (CHECKED NUMERICALLY — see §2(c), this is the CCLM-type
Hilbert-space pair-correlation constant).

---

## 2. GdLL — the three key questions

### (a) Unconditional bound on simple/multiple zeros of ζ? **NO.**
Theorem 1 is stated *under GRH*, and its input (1) (the Hejhal/RS n-level correlation) is itself a
GRH-conditional statement (the ordinates γ_j must be real for the correlation of ordinates to be defined).
**There is no unconditional multiplicity statement for ζ's zeros in this paper** (VERIFIED-FROM-PAPER; the
only unconditional content is the pure harmonic-analysis constant c_{n,m} and the combinatorial identity
Z_n/N ≥ 1 − c_{n,m}/(n−1)!). Under RH the paper gives (m=1): ≥ 96.14% simple-or-double (n=3) and ≥ 97.87%
multiplicity ≤ 3 (n=4); and it cites the under-RH pair-correlation SDP [8,9] N*(T) ≤ (1.3208+o(1))N(T),
hence **≥ 67.92% simple zeros under RH** (CHECKED NUMERICALLY: 2 − 1.3208 = 0.6792). All of these are
conditional reference points, not wall inputs. The (n=2, m=1) case would be the direct "simple zeros" row
and gives only the kernel bound 1 − c₂,₁ = 0.6725 (under RH) — the same constant as our unconditional
Theorem D, but conditional.

### (b) Does it use the SDP/linear-programming machinery (the CGdL line)? **YES — it is the CGdL line.**
(VERIFIED-FROM-PAPER, §2–§6.) Exact template: sum-of-squares parametrization g(x) = Σ X_{i,i′} g_i(x) g_{i′}(x),
X ⪰ 0 PSD; the SDP (4) "minimize ν_n(g) subject to g(0) = 1, X ⪰ 0"; constraints fed: (i) Paley–Wiener
support supp ĝ ⊆ (2/m)H_{n−1} — this IS the RS-range support constraint |x₁|+…+|x_{n−1}|+|x₁+…+x_{n−1}| < 2/m
(equivalently the correlation theorem's test-function range); (ii) g ≥ 0 (via the SOS/PSD form); (iii) g(0) = 1
(normalization). Supporting machinery: Γ_n symmetry reduction + block diagonalization (Schur's lemma;
Lemma 3: non-trivial irreps vanish at 0, so only the trivial irrep survives); Lemma 4 (single-constraint SDP
has rank-1 optimum found by solving the linear system Ax = b); Hejhal's explicit ν₃ formula
ν₃(g) = 2 + ĝ(0) + 6∫₀¹ ĝ(x,0)(x−1)dx − 12∫₀¹∫_{−x₂}⁰ ĝ(x₁,x₂) x₂ dx₁dx₂; rigorous certification in
ball arithmetic (Julia; exact GAP polynomials; Maple series sums with a 0.1%-truncation consistency check
against the Maple bug). This is structurally the same certificate family as
`cgdl-1810.08843-paircorr-sdp.pdf` (Chirre–Gonçalves–de Laat 2020), lifted from the pair to the triple level.

### (c) Connection to the Gram-stability discovery (tr Ψ(M))? **Structural kinship only; no existing combination.**
- The stability term tr Ψ(M) lives inside the **pair (two-moment) data** of the rank–trace inequality
  (M = V*V, the Gram matrix of simple-zero atoms; Ψ(t) = (t−1)² on [0,2], 2t−3 beyond). GdLL's Z₃ bound
  lives inside the **triple-correlation value** (W₃-weighted functional), which for ζ is RH-conditional.
- Code-backed connection found (CHECKED NUMERICALLY): **our wall constant 0.6725 is exactly the GdLL/CCLM
  n=2 pair-kernel bound**: 3/2 − (1/√2)cot(1/√2) = 0.6725007036794116… and 1 − c₂,₁ = 1 − 0.3274992963205884… =
  0.6725007036794116… (identity verified to 50 digits: diff = 0.0). I.e., Theorem D's constant IS the
  one-delta extremal pair-correlation bound from the same machinery line; the discovery's 0.67319 is the
  *pair-level Gram correction* to it. So the two "papers vs discovery" inputs are not independent: they sit
  on the same base constant.
- **Combination: does not exist in the literature and is not immediate.** To combine one would need either
  (i) a stability-type correction to the *equality case* of GdLL's SDP (its rank-1 solution
  g = (Σ c_i g_i)²/(cᵀb)², Lemma 4 — the analogue of the "orthogonal atoms" equality case that the discovery
  broke for the pair inequality), or (ii) feeding the triple correlation into the marked-configuration
  certificate. Both are CONJECTURED directions, not results. Note the pricing-sheet prior: within the
  certificate class, the triple-moment (m₃) input is negative-priced (−1/3 per unit for the simple-fraction
  cap) or neutral (5/6 distinct) — a strong prior that (ii) has negative yield; the discovery's positive-priced
  input (tr Ψ(M)) is at the *pair* level, which GdLL's machinery does not read.

---

## 3. Jiang (2507.20653) — main theorems (VERIFIED-FROM-PAPER)

**Objects.** F a number field; F_n = cuspidal automorphic representations π of GL_n(A_F), unitary central
character; L(s,π) = Σ λ_π(n) Nn^{−s}; a_π(p^k) = Σ_{j=1}^n α_{j,π}(p)^k (Satake power sums); π̃ the
contragredient; C(π) the analytic conductor.

**Hypothesis H (verbatim):** "For any fixed k ≥ 2 and any fixed π ∈ F_n, Σ_p (log Np)² |a_π(p^k)|² / Np^k < ∞."

**Theorem 1.2 (verbatim):** "Hypothesis H is true for all n ≥ 1."

**Theorem 1.3 (verbatim):** "For any ε > 0 and any π ∈ F_n, we have
∏_p (1 + Σ_{k≥2} λ_{π×π̃}(p^k)/Np^{kσ}) ≪ C(π)^ε  and  ∏_p (1 + Σ_{k≥2} a_{π×π̃}(p^k)/Np^{kσ}) ≪ C(π)^ε
for any σ ≥ 1 − 1/(n²+1) + ε," implied constants depending only on [F:Q], n, ε. (This is the *effective,
uniform-in-conductor* strengthening; Hypothesis H follows as the corollary.)

**Theorem 6.1 (verbatim):** "Let π ∈ F_n over Q, and let f and h be functions as defined above. Assume the
support of f̂ is contained in Σ_{j=1}^m |ξ_j| < 2/n. Then as T → ∞,
R_m(T, f, h) ∼ (n/2π) T log T ∫ h(r)^m dr ∫_{R^m} f(x) W_m(x) δ((x₁+…+x_m)/m) dx₁…dx_m,"
where R_m(T,f,h) is the **smoothed** m-level correlation sum, "which does not require GRH". Proof (verbatim):
"This is Theorem 1.1 in Rudnick and Sarnak [42], whose proof is conditional on either n ≤ 3 or the validity
of Hypothesis H. Since Our Theorem 1.2 establishes Hypothesis H for all degrees n, the result now holds
unconditionally."

**Theorem 6.2 (verbatim):** the GRH-normalized correlation R_m(B_N, f) → ∫ f W_m δ — "with the notation in
Theorem 6.1 **and also GRH for L(s,π)**" (so this one still needs GRH).

**Other applications:** Theorem 7.5 (strong multiplicity one for coefficients: N(π,π′) ≪ Q^{7n³−5n²+8n−5+ε});
Theorem 8.6 (Selberg orthogonality conjecture, unconditional, with the three-case error terms); Theorems
8.2–8.4 (PNT for Rankin–Selberg L-functions, uniform and fixed-representation versions); Theorem 8.8
(Hoheisel-type: Σ_{x<Np≤x+h} |a_π(p)|² log Np over primes, all n). **Method:** a power sieve over number
fields (ray-class characters of exact order k via Chebotarev, Lemma 4.4) + an Iwaniec-style iterative
conductor-exponent reduction + convexity for twisted RS L-functions; bypasses the functoriality barrier
(exterior-power lifts) that restricted Hypothesis H to n ≤ 4.

---

## 4. Jiang — the three key questions

### (a) What "unconditional GUE statistics", for which zeros?
**The smoothed m-level correlation of the zeros of a single automorphic L-function L(s,π), π ∈ F_n over Q,
for ALL n ≥ 1, with test-function Fourier support Σ|ξ_j| < 2/n, and WITHOUT GRH** (Theorem 6.1). New content
is n ≥ 4 (n ≤ 3 was already unconditional; Hypothesis H had been verified for n ≤ 4 via Rankin–Selberg/Kim).
The GUE statistics are the family of m-level correlation values W_m with the centroid δ. Family-level? No —
fixed π, not averaged over a family; but "family-level" in the sense that it concerns automorphic
L-functions in general, not ζ specifically.

### (b) Does anything transfer to ζ's zeros individually? **NO.**
ζ is the GL₁ (m = 1) case, where Hypothesis H is trivially true (a_ζ(p^k) = 1) and the correlation results
are the classical RS/Hejhal content. Jiang's genuinely new statements (n ≥ 4, effective bounds, strong
multiplicity one, Selberg orthogonality, PNT) concern automorphic representations, not ζ. For ζ, Theorem 1.3
is vacuous (n = 1: the Euler product Σ_{k≥2} Np^{−kσ} converges for σ > 1/2 trivially, and C(ζ) is fixed).
Nothing in the paper constrains ζ's actual zero configuration beyond the RS-range data already known.

### (c) Any statement beyond bandwidth 1? **NO.**
The correlation support condition is Σ|ξ_j| < 2/n ≤ 1 (equality only at n ≤ 2, and with the centroid
constraint the pair reduces to |ξ| < 1 — Montgomery's classical range; for n ≥ 2 the range is *strictly
inside* bandwidth one). The effective bound Theorem 1.3 concerns prime-power Euler products at
σ ≥ 1 − 1/(n²+1) (a subconvexity-type barrier, not a zero-statistics bandwidth). **No unconditional form-factor
data for |α| > 1 is provided.** The beyond-1 wall is untouched by this paper.

---

## 5. Mapping onto the program walls

| Wall (current) | GdLL 2303.01095 | Jiang 2507.20653 | Moved? |
|---|---|---|---|
| (a) simple-zeros 0.6725 → 0.67319 (discovery) | **NO** — Theorem 1 is GRH-conditional; the RS/Hejhal input (1) is conditional; only conditional constants arise (under RH: 0.9614 simple-or-double; cited pair-SDP ≥ 0.6792 simple) | **NO** — new content is automorphic n ≥ 4; ζ = GL1 classical; nothing unconditional about ζ's zeros | **NO** |
| (b) on-line proportion 2/3 (Theorem A) | **NO** — same conditionality | **NO** — no on-line input for ζ; correlation support ≤ 1 | **NO** |
| (c) distinct-zeros 5/6 (Theorem C) | **NO** — Z₃ bound is multiplicity ≤ 2, conditional; under RH the RS triple correlation already gives N_d ≥ 0.85082 (ceiling-note §7.5(g)); both conditional | **NO** — family-level only | **NO** |
| (d) in-class ceiling 0.6818 | **NO as input** — provides the SDP *template* only; no unconditional triple-correlation data | **NO** — support Σ|ξ_j| < 2/n ≤ 1, strictly inside bandwidth one; the |α|>1 data needed to break the ceiling remains conjectural-only | **NO** |

**Precision on (d):** the ceiling is a proven upper bound for the *rank-trace/pair-correlation certificate
class* reading bandwidth-one data (Lean, `ceiling_law256`, modulo the numerically-checked EnclOK). Neither
paper supplies a new *unconditional* input to that class. GdLL's triple-correlation certificate is a
different class but is GRH-conditional; Jiang's correlations are inside the RS range. The ceiling's only
live vulnerability identified so far remains the **Gram-stability constraint tr Ψ(M)** (discovery Q2: does
the 256-law satisfy the stability bound, or does the strengthened inequality push the class ceiling up? —
adjudication still OPEN). These two papers neither confirm nor refute that; they are silent on it.

---

## 6. Verdict

**NO wall moves. Neither paper provides a new unconditional input to (a) 0.6725/0.67319, (b) 2/3,
(c) 5/6, or (d) 0.6818.**

- GdLL's multiplicity bounds are **under GRH** (the Hejhal/RS higher-level correlation input is itself
  conditional for ζ — the ordinates must be real for the correlation to be defined). Under RH it gives
  ≥ 96.14% simple-or-double and (via cited [8,9]) ≥ 67.92% simple — useful conditional reference points,
  not wall inputs.
- Jiang's unconditional GUE statistics are for **automorphic L-functions at all degrees n (new for n ≥ 4)**
  with Fourier support **strictly inside the RS range Σ|ξ_j| < 2/n ≤ 1**; for ζ itself they add nothing
  beyond the classical GL1 content. Nothing beyond bandwidth 1 appears anywhere.
- This is **consistent with, and reinforces, the corrected pricing picture**: the triple-moment (m₃ /
  higher-level correlation) input is negative-priced or neutral for our walls (GdLL confirms the triple
  correlation is the *conditional* input; its unconditional diagonal is already in the RS range and already
  priced); the positive-priced input identified so far is the *pair-level Gram-structure* term tr Ψ(M)
  (discovery), which neither paper addresses.

---

## 7. Recommended next step

**Fund a GdLL-style SDP for the PAIR certificate with the stability constraint.** Concretely:
1. Port GdLL's exact SDP machinery — SOS parametrization g = ΣX_{ii′}g_ig_{i′}, X ⪰ 0, Γ-symmetry reduction
   + block diagonalization, Lemma-4 rank-1 solve (Ax = b), ball-arithmetic certification (Julia) — to the
   marked-configuration certificate fed by the **unconditional** Montgomery pair-correlation input
   (F on [0,1]), with the **full Gram matrix M of the simple-zero atoms as the decision variable** and the
   stability constraint **tr Ψ(M) ≥ ε** (per discovery note: 3-point ε₄ ≥ 221/10⁶ → 67.2519767%;
   7-point six-variable bound ≥ 19/5000 → 67.3008528%) as an explicit affine constraint. Both `cgdl-1810.08843-paircorr-sdp.pdf` and `gdl-2303.01095` are already in
   `research/papers/` as templates; the existing external verifiers (`ainta`, `trmdy`) certify the discrete
   refinements, not the SDP-form Gram constraint.
2. This is the single concrete route that (i) **adjudicates discovery Q2** — whether a full-Gram certificate
   beats the 0.6818 ceiling (if the 256-law violates tr Ψ ≥ ε, the strengthened inequality pushes the class
   ceiling up; if it satisfies it, the ceiling survives the Gram constraint and the in-class gap closes at
   the law), and (ii) has the concrete numeric goal of beating the current external best
   **0.673192911473** (tawanerguo-cn, Bellman coboundary) with a verified, self-contained script.
3. Second priority (monitor, do not fund yet): any unconditional n-level input for ζ beyond the RS diagonal
   term. Neither paper provides one; the beyond-1 form factor remains conjectural-only (RMT / Hardy–Littlewood
   / Montgomery pair-correlation conjecture), and per GLSS25 even the *full* pair-correlation conjecture
   would collapse the ceiling (100% simple) — so the honest status of the ceiling is unchanged.

**Also record (for the attack log):** the under-RH constants from GdLL's orbit — ≥ 0.9614 simple-or-double
(ζ, n=3), ≥ 0.9787 multiplicity ≤ 3 (n=4), ≥ 0.6792 simple (pair-SDP N* ≤ 1.3208N), N₃/N ≤ 2.0597 — as
conditional reference points, clearly labeled, so no future agent mistakes them for unconditional progress.

---

## 8. Honesty labels and epistemic status

- **VERIFIED-FROM-PAPER** (full text of both PDFs read and quoted): every theorem, constant, hypothesis,
  support condition, and method statement above (§1–§4).
- **CHECKED NUMERICALLY** (`paper-gdll-jiang-verify.py`, command in header): Theorem-D constant
  0.6725007036794116…; the identity 0.6725 = 1 − c₂,₁ (diff 0.0 at 60 digits); all three Theorem-1 rows
  (0.961401358 / 0.2997466875 / 0.9787142857 from the paper's c-values); N₃/N ≤ 2.059695173; 0.6792 > 0.6725;
  Jiang's σ-barrier (1/2 at n=1).
- **CONJECTURED** (analyst assessment): the payoff of the recommended GdLL-style-SDP-with-stability route;
  the structural kinship between the discovery's tr Ψ(M) and GdLL's SDP equality case; that combining the
  two is feasible at all.
- **ASSUMED (flagged):** that ζ is covered by the m = 1 / GL1 formalism in both papers. GdLL states such
  L-functions "generalize the classical Dirichlet L-functions (the case m = 1)"; Jiang's F_n is cuspidal
  GL_n data. ζ = L(s, trivial character) is the standard archetype in this formalism (RS's "principal
  L-functions" include ζ), but neither paper states ζ explicitly.
- **UNVERIFIED (flagged):** the *correctness* of Jiang's proofs (arXiv v1, 28 Jul 2025, unrefereed; a very
  strong claim — Hypothesis H for all n via a power sieve). Content reported faithfully; no adversarial
  validation of the argument was performed here. GdLL's (3,1) case is peer-reviewed (Math. Comp. 2024); its
  (3,2)/(4,1) rows rest on the Maple-series computation the paper itself flags as delicate.
- **No wall moved.** The search continues: the positive-priced lever remains the pair-level Gram-structure
  constraint; the next computation is the SDP-form stability certificate of §7.

**Persistent-hook note:** the two papers examined here are not a failure and not a stop — they are
intelligence: they confirm the m₃ input is priced where the pricing sheet says it is, they pin the
conditional-vs-unconditional boundary precisely, and they hand us a verified SDP template (GdLL) whose
machinery is the most direct route to adjudicating the discovery's Q2. That adjudication is the next
concrete deliverable.
