# Attack: transport of the 67.25% method to GL(2) / higher-degree L-functions

> Agent: EXECUTIONER (analogy-domain-transfer + creativity). Round 1.
> Sources read in full: anthropic-informal-note.txt (N), claude-riemann-paper.txt §§1–7 (C),
> baluyot-etal-2306.04799.txt (B24), bgst-2501.14545.txt (B25), lean-zeta-23/README.md (L),
> round-1-brief.md, hooks/agents.md. LMFDB zero data fetched live (below).
> Labels: **PROVEN** = theorem in a source we hold / verified here; **CHECKED NUMERICALLY** = verified
> by computation in this session; **CONJECTURED** = heuristic or extrapolation, not carried out;
> **MISSING** = no source. No invented references: anything not in the four held papers is labeled.

---

## 0. Bottom line (read this first)

**The 67.25% method does NOT transport to an individual GL(2) L-function — not because of a missing
analytic theorem, but because the certificate itself is provably empty at the bandwidth available to a
fixed form.** The prime side transports with only PROVEN inputs (Montgomery–Vaughan + Rankin–Selberg;
no pair-correlation theorem is needed anywhere). The obstruction is a factor of 2 in the zero density:
a fixed GL(2) form (elliptic curve, holomorphic newform, Maass form) has twice ζ's zero density
(**CHECKED NUMERICALLY** here from LMFDB zero data for 11a1 and 37a1), so the window can cover only
half a mean spacing (Λ* = 1/2), and the rank–trace certificate certifies at most (2 − 1/Λ)N ≤ 0 on-line
zeros (C Prop 7.4 / §7.5(a), **PROVEN** in C). This is a hard wall, independent of all analytic inputs —
even assuming the pair-correlation conjecture, the certificate stays empty for an individual form.

The only viable target is the **family-averaged** statement (e.g. ≥ 2/3 of the zeros of a family of
forms, counted across the family, on the line): the paper's Remark 7.2(iii) mechanism (averaging +
orthogonality restores bandwidth 1) is stated for Dirichlet characters and is **CONJECTURED** for GL(2)
— my extrapolation, explicitly not carried out in C, requiring the Gevrey-class taper of C Prop 4.2
plus a Petersson/Kuznetsov treatment of the off-diagonal prime sums. Difficulty: soft wall / unknown
(a genuine research program, not a corollary; every *ingredient* is standard, the *assembly* is not).

C Remark 7.2(ii) already contains exactly this verdict, as a heuristic: "it is a degree-one method.
For an individual GL(2) L-function (Λ* = 1/2, m_F = 1) one gets c = 6/13 < 1/2, i.e. nothing, whatever
the window." My contribution is (a) the ingredient-by-ingredient transport map, (b) the verification
that the prime side needs only Montgomery–Vaughan (no pair correlation), (c) the numerical confirmation
of the degree-2 density, and (d) the precise location of the wall (dimension ceiling, not analytic).

---

## 1. What exactly transfers (the method's ingredients, from N + C §2–6)

The method: Weil/Guinand explicit formula → finite-dimensional windowed space V (grid vectors
v_ρ[k] = φ̂_T(γ_ρ − T − (T/N)k), test functions supported on [−L/2, L/2], L = λ·l, X = e^L) →
Hermitian matrix W_T (on-line zeros: positive squares; off-line pairs (ρ, 1−ρ̄): hyperbolic (1,1)
planes, from the functional equation) → Sylvester inertia + rank–trace inequality (N Lemma 3.4 =
C Prop 4.4(ii)) → two analytic evaluations: tr W_T ≈ N(T,2T) (mean density) and ‖W_T‖²_HS ≈ κ·N,
κ = 1/2 + (1/√2)cot(1/√2) at the optimal (Montgomery–Taylor) window (C Thm D) → proportion
≥ 4 − 2 − κ = 3/2 − (1/√2)cot(1/√2) = 0.67250… (crude route: κ ≤ 4/3 gives 2/3).

## 2. Transport map: GL(2) L-functions (holomorphic newforms / elliptic curves / Maass)

Target: L(s, f) = Σ λ_f(n) n^{−s}, f a primitive GL(2) automorphic form (level N, weight k, or
Maass with Laplacian eigenvalue), normalized so the critical line is Re s = 1/2, functional equation
Λ(s,f) = ε·Λ(1−s, f̄) with completed function built from the archimedean factor(s) and N^{s/2}.

| # | Ingredient (ζ) | GL(2) analogue | Status | Source / note |
|---|---|---|---|---|
| (a) | Weil/Guinand explicit formula (N "Guinand–Weil"; C Prop 2.1, derived from [IK04 Thm 5.12] per C App. A) | Same completed-function argument for Λ(s,f); C Thm E's proof (iii) shows the pattern for degree-1 L(s,χ): µ → µ_χ = (1/2π)[log(q/π) + Re Γ′/Γ(...)], no pole term | **KNOWN** (classical; same contour-integration proof as C App. A; the general automorphic explicit formula is the standard Weil form, e.g. [IK04 5.12] as cited in C) | C Thm E proof; C App. A |
| (b) | Riemann–von Mangoldt N(T,2T) ~ (T/2π)log(T/2π) (N f.n. 1; C (1.2)) | N_f(T,2T) ~ (T/2π)·log(q_f·T²/2π): degree-2 law, **density TWICE ζ's** | **KNOWN** (argument principle; general form [IK04 Thm 5.31], as cited in C); **CHECKED NUMERICALLY** here: LMFDB zeros of 11a1 and 37a1 give N(10)=2, N(15)=5, N(20)=9 resp. N(5)=1, N(10)=5, N(15)=9, fitting (T/2π)log(cT²/2π) with near-constant c ≈ 0.22–0.27 resp. 1.2–1.45, and inconsistent with a log(T) law | LMFDB /L/Zeros/2/11/1.1/c1/0/0 and /2/37/1.1/c1/0/0 (fetched this session); the T² is the pivot of the whole analysis |
| (c) | Functional equation, zero pairing ρ ↔ 1−ρ̄ with multiplicities, zeros in 0<β<1, N(t+1)−N(t) ≪ log t | Same for L(s,f): multiset invariant under ρ → 1−ρ̄ (self-dual f: f̄ = f, so within one function; general f: pairs with f̄); (1,1) hyperbolic planes and real-symmetric W_T go through verbatim | **KNOWN** (classical; C Thm E proof (ii) is the degree-1 template, "Section 4 is otherwise verbatim") | C Thm E proof (ii) |
| (d1) | Montgomery PAIR CORRELATION (1973; unconditioned by B24/B25 under hypotheses) | No proven GL(2) pair correlation; RMT conjecture only; low-lying zeros in families (Iwaniec–Luo–Sarnak) is a *family-averaged* statement, **not in our sources** | **MISSING / CONJECTURED** — and **not needed** (see §3) | B24, B25 read in full: they treat ζ only, no GL(2) analogues anywhere |
| (d2) | Prime-side second moment: diagonal Σ Λ(n)²/n·g(y_n) (C Prop 5.6, from Chebyshev–Mertens (5.1)–(5.2)) | Diagonal Σ |b_f(n)|²/n·g(y_n), b_f = Λ-coefficients of L(s,f), b_f(p) = λ_f(p)log p; needs Σ_{n≤x}|b_f(n)|²/n = (1/2)log²x + O(log x) | **KNOWN / PROVEN** (Rankin–Selberg, Rankin 1939 / Selberg 1940 — classical, not in our four papers; m_F = 1 as in C Rem 7.2(ii)) | C Rem 7.2(ii) |
| (d3) | Off-diagonal prime sums via **Montgomery–Vaughan** generalized Hilbert inequality (N Thm 1.1; C Lemma 5.2, constant 3π/2; Lean L `Zeta23/MV/`) | Applies **verbatim**: same frequencies y_n = log n (same primes!), x_n = b_f(n)·n^{iT}/√n; needs only Σ_{n≤X}|b_f(n)|² ≪ X^{1+o(1)} | **PROVEN** (MV is a general Hilbert-space inequality; the GL(2) input is Rankin–Selberg, PROVEN) | C Lemma 5.2 + Prop 5.6 (O₁ step); N Claim 3.3; Lean `Zeta23/MV/` |
| (d4) | µµ density term (C Prop 5.5) + Stirling for Γ′/Γ (C (2.8)) | µ_f(τ) = (1/2π)Re[Γ′/Γ archimedean factors] + (1/2π)log(q_f/2π) ~ (1/π)log τ (twice ζ); Stirling identical | **KNOWN** (classical) | C (2.8), Prop 5.5 |
| (e) | Paley–Wiener / Poisson–Gabor identity (N Claim 2.1; C Lemma 2.2) and window support [−L/2, L/2] | Identical — depends only on the window φ_T, not on the L-function | **PROVEN in analogy** (mechanical) | N Claim 2.1; C Lemma 2.2 |
| (f) | Rank–trace / inertia / dimension (N Lemmas 3.1–3.4; C Prop 4.4, Prop 7.4) | Identical linear algebra | **PROVEN in analogy** (no change) | C §3, Prop 7.4 |

**Verdict of the map:** every *analytic* ingredient is KNOWN or PROVEN for GL(2) (a, b, c, d2–d4).
Nothing is missing at the level of theorems — which makes the failure purely structural.

## 3. The key question: does Montgomery–Vaughan suffice on the prime side (no pair correlation)?

**YES — and this is precisely what the ζ proof already does.** Detailed analysis:

- The HS-norm computation (N Lemma 3.3 = C §5) splits ν_T·ν_T = (µ + λ_T + π_T)². The two main
  terms are (i) µ·µ (density; Stirling + RvM only) and (ii) λ_T·λ_T. The λ_T·λ_T term splits into
  *diagonal* n = m (partial summation from Σ Λ(n)²/n = (1/2)log²x + O(log x), C Prop 5.6/D) and
  *off-diagonal* n ≠ m. The off-diagonal is bounded by Montgomery–Vaughan applied to
  x_n = Λ(n)/√n · n^{iT}·g(log n/2π), y_n = log n, δ_n ≥ 1/(n+1) (N Lemma 3.3 proof; C Prop 5.6 O₁).
  Nothing else. In particular **Montgomery's 1973 pair-correlation theorem is never used** — it is
  needed only for the *speculative* range λ > 1 (X ≫ T), i.e. "information on prime pairs (the
  Hardy–Littlewood conjectures, or equivalently Montgomery's pair correlation conjecture for α > 1)"
  (C §7.5(a)). Within λ ≤ 1, MV is unconditional and self-contained (Lean-formalized, L).

- **Why this transfers to GL(2) unchanged:** MV (C Lemma 5.2) is a general Hilbert-space inequality
  on any separated frequencies λ_r. For L(s,f) the frequencies are the SAME log n. The x-sequence
  becomes x_n = b_f(n)n^{iT}/√n, and MV needs only Σ_{n≤X}|x_n|²·δ_n^{−1} ~ Σ_{n≤X}|b_f(n)|²
  ≪ X log X — which is Rankin–Selberg (PROVEN, classical), the GL(2) replacement for Chebyshev's
  Σ Λ(n)² ≪ x log x (C (5.1)). The diagonal needs Σ|b_f(n)|²/n = (1/2)log²X + O(log X), also
  Rankin–Selberg (m_F = 1, as C Rem 7.2(ii) states). So the whole of C §5 (P) transports with
  **zero new analytic input beyond the explicit formula and Rankin–Selberg**. This is also what the
  paper means by "the prime side is unconditional" (C §1.4: "Montgomery's prime-side evaluation is a
  mean value of a Dirichlet polynomial of length T, and hence is unconditional; what required the
  Riemann hypothesis was only the reading of the zero side").

- **So the pair-correlation theorem is a red herring for the transport.** Even where GL(2) pair
  correlation is missing, the method does not need it. The wall is elsewhere (§4).

## 4. Where it actually dies: density, bandwidth, and the dimension ceiling

- The window width is limited by the prime side to L ≤ log T·(1+o(1)) (X = e^L ≤ T^{1+o(1)},
  C Prop 5.6 O₁; same primes for GL(2)). The mean zero spacing of a fixed form is 2π/(density)
  = 2π/((1/2π)log(q_f T²)) ≈ π/log T — **half ζ's spacing** (row (b) of the map; verified
  numerically). Hence the bandwidth in units of mean spacing is
  Λ = L/log q_f(T) ≈ log T/(2 log T) = 1/2 (q_f(T) ~ q_f·T² is the analytic conductor at height T;
  C Rem 7.2(ii) calls this "Λ* = 1/2, m_F = 1").
- The certificate: rank of the on-line part ≤ dim V = λ₁N, and ‖Â‖²_F ≥ (tr Â)²/d forces the
  rank–trace lower bound to be at most (2 − 1/λ₁ + o(1))N — **non-positive for λ ≤ 1/2** (C Prop 7.4,
  §7.5(a), **PROVEN** in C). At the borderline λ = 1 (Λ = 1/2) the bound is exactly o(N). Even
  granting the pair-correlation conjecture (or all higher trace moments, HL*), the *dimension* caps
  any certificate on this V at λN ≤ N/2 < 2N/3 (C §7.5(d,e): higher moments are "useless" at
  λ ≤ 1/2). So: **unconditionally, the individual-form statement is empty; conditionally, capped at
  1/2 by dimension.** Both are walls of the method, not of the primes.
- Cross-check with the paper's heuristic: κ = ‖W‖²/N ≈ 1/Λ + m_FΛ/3 = 2 + 1/6 = 13/6 > 2 at
  Λ* = 1/2, i.e. c = 6/13 < 1/2 and proportion 2 − 1/c < 0 (C Rem 7.2(ii)). Consistent: the
  certificate is empty, whatever the window.

## 5. Target statement analysis

- **Individual form (fixed f): DEAD by this method.** An unconditional "≥ c of the zeros of L(s,f)
  on the line" is impossible via the rank–trace certificate (empty at Λ ≤ 1/2), and a conditional
  version is capped at 1/2 (dimension) and would need conjectural spectral-moment input. Note the
  contrast the brief asks about: ζ's 67.25% is about ALL zeros, no averaging; the analogous
  single-form GL(2) statement is out of reach of *this* method, not merely unproven.
- **Family-averaged (the honest target):** average over a family F with growing conductor, e.g. all
  holomorphic newforms of weight k ≤ K, level 1, K → ∞ (weight aspect), or all forms of level N ≤ X,
  weight 2. Statement: Σ_{f∈F} N₀,f(T,2T) / Σ_{f∈F} N_f(T,2T) ≥ 2/3 − o(1) (proportion across the
  family's zeros, counted with multiplicity; no per-form averaging of proportions — the same "all
  zeros" flavor as ζ). Mechanism (C Rem 7.2(iii), stated for Dirichlet characters; **my GL(2)
  extrapolation**): averaging makes tr and ‖·‖² commute linearly (C Lemma 3.2 is linear in both),
  and the orthogonality of the family (Petersson formula for GL(2)) kills the off-diagonal prime
  sums exactly-asymptotically, removing the X ≤ T constraint and restoring Λ* = 1. C explicitly says
  the character version "requires a different (Gevrey-class) taper in Proposition 4.2 and is not
  carried out here"; the GL(2) version additionally requires the Petersson/Kuznetsov trace formula
  with Kloosterman-term errors shown negligible. **CONJECTURED**; genuinely new work, not a corollary.
- **Individual vs averaged, one line:** the method is a degree-one mechanism; it can only be
  resurrected for GL(2) by averaging the prime-side orthogonality (families), never by sharpening
  analytic inputs on a single form.

## 6. Bottom line: the single missing ingredient and its hardness

- **The single missing ingredient for a GL(2) transport is not a theorem — it is bandwidth.** Every
  analytic input (a–d) is KNOWN/PROVEN (explicit formula, RvM, Stirling, Rankin–Selberg,
  Montgomery–Vaughan; verified for the density here). The obstruction is that a fixed GL(2) form's
  zeros are twice as dense, halving the available bandwidth to Λ* = 1/2, below the 1/2 threshold
  where the rank–trace certificate is empty (C Prop 7.4) — a **HARD WALL** (dimension argument,
  independent of all analytic inputs; even the pair-correlation conjecture does not move it).
- **Hardness classification:** individual form = hard wall (provably empty, no path). Family-averaged
  target = soft wall / unknown: the *ingredients* are standard and proven, but the *assembly*
  (Gevrey taper + Petersson/Kuznetsov + full uniformity, plus the Dirichlet-family version itself
  being unclaimed in C) is a real research program with no guaranteed constant better than 2/3.
- **Most promising next step (cheapest probe):** verify C Rem 7.2(iii) mechanism numerically for a
  small Dirichlet-character family first (e.g. all χ mod q for a fixed large q, T ~ (log q)^c): the
  family-averaged HS norm with the orthogonality-killed off-diagonal — this tests whether the
  bandwidth-1 restoration is real before committing to the GL(2) Petersson version. If it holds, the
  GL(2) weight-aspect family is the target; if the Kloosterman terms fail to be negligible, the
  family target dies too (then the method is degree-one in an even stronger sense).

## 7. Label inventory (honesty)

- PROVEN (in C): Thm E (Dirichlet L-functions); Prop 7.4 + §7.5(a) dimension ceiling (certificate
  ≤ (2−1/λ)N, non-positive at λ ≤ 1/2); Lemma 5.2 (MV, 3π/2); Rem 7.2(ii) formal computation for
  degree m (c = Λ/(1+m_FΛ²/3)); §7.5(e) higher moments useless at λ ≤ 1/2.
- CHECKED NUMERICALLY (this session): degree-2 zero density for fixed GL(2) forms — LMFDB zero lists
  for 11a1 (N(10)=2, N(15)=5, N(20)=9; first zero 6.3626…) and 37a1 (N(5)=1, N(10)=5, N(15)=9; first
  zero 3.5091…), both fitting (T/2π)log(cT²/2π) and inconsistent with (T/2π)log(cT/2π); this is the
  empirical anchor for Λ* = 1/2.
- CONJECTURED / extrapolated (mine, not in C): the GL(2) family-averaged statement and its Petersson
  treatment; C Rem 7.2(iii) itself is stated only for Dirichlet characters ("one expects…", unclaimed).
- MISSING / not in sources: any proven GL(2) pair-correlation analogue; the Iwaniec–Luo–Sarnak
  low-lying-zeros family machinery (not in our four papers; deliberately not cited as an available
  input); the primary sources [IK04], [MV74], Rankin–Selberg papers (known to exist, not in our
  possession — cited only "as cited in C" or as classical facts).
