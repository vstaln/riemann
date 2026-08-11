# Attack: the Jensen-polynomial RH-ometer (C-RH2) — dictionary, discriminants, honesty, verdict

**Agent:** EXECUTIONER, vector C-RH2.
**Date:** 2026-08-11.
**Question (C-RH2):** build the Jensen-polynomial dictionary (degree-d Jensen polynomial of ξ ↔ moment order 2d), compute the degree-2/3 Jensen discriminants of ξ, ξ′, ξ″ from the EXPLICIT FORMULA prime data (not from the zeros), report the discriminant margins, and give the honesty statement + verdict: does the Jensen machinery offer a new certificate input, or only a diagnostic omen?

**Status:** RESOLVED. All discriminants computed and positive; **every numerically-accessible margin is PROVEN-positive in the literature** (Chasse d ≤ 2·10¹⁷; GORZ d ≤ 8; GORTTW Cor. 1.3 d ≤ 9.36·10²⁰), the positivity is **generic analytic behavior compatible with RH false** (Farmer 2008.07206, with the X_j counterexample), and the object itself **disperses zero-location information** (Chasse d < T²). **Verdict: diagnostic omen only — no new certificate input.** Two C-RH2 premises corrected by the probe: (i) the Jensen discriminant is a (degree, shift)-indexed *global* constant, not a height-indexed line object — the C-RH2 "10⁴ grid points at height 10³–10⁴" probe design misidentifies the object; (ii) the raw prime series Σ_p log p·p^{−1/2}·cos(t log p) is **not convergent** (demonstrated: |S(10⁷)| ≈ 206, growing ~√x) — the coefficients are the functional-equation analytic continuation, computed here to 60 digits with closed-form cross-checks.

---

## 0. Executive summary (labels)

1. **The discriminant table is positive, and every computed margin is PROVEN ≥ 0 in the literature** (Chasse [4]; GORZ Thm 2 [GORZ]; GORTTW Cor. 1.3 [GORTTW], the last via Platt's verified RH₀(3.06·10¹⁰)). Our computation is a 60-digit verification, not new data. LABEL: CHECKED NUMERICALLY (this script) + PROVEN-in-literature.
2. **A positive finite-margin computation certifies nothing about RH.** (Farmer [F], §4: the Hermite/Jensen connection is compatible with RH false — his X₁₀ model violates "RH" at its 2nd zero yet has hyperbolic J^{d,0} for all d ≤ 118; the dispersal bound d < T² means degree-d discriminants see zero data only below height √d.) LABEL: REFUTED-as-certificate-route (by literature; probe consistent).
3. **The task's parenthetical is corrected:** a *negative* discriminant at (d, n) would refute RH — but **globally, not "at a height"** (the Jensen discriminant has no height parameter), and only at d > 2·10¹⁷ (below that, negativity is a theorem-forbidden computation error, not a refutation). A *positive* margin at finitely many (d, n) proves nothing — **not even locally** (see Farmer's X_j).
4. **Derivative tower:** RH_m ⟺ J_{d,n} hyperbolic for all d ≥ 1, n ≥ m (GORTTW). The ξ′-window (n = 1) and ξ″-window (n = 2) discriminants are positive in the proven range; RH₁ is verified numerically to height 1419 (attack-xiprime.md: 999 on-line ξ′-zeros, one per gap, 60 digits; ξ″ interlacing 20/20). The tower's real-rootedness is **generic** (Ki's cosine theorem; Farmer–Rhoades universality, now PROVEN by Campbell–O'Rourke–Renfrew) — it holds with or without RH.
5. **The only new things in this probe are: the object correction, the prime-series divergence demonstration, a 60-digit verified coefficient table with parity/closed-form/direct cross-checks, the margin laws (d = 2 → 0 like 1/(n+2), the GORTTW uniformizer; d = 3 → Hermite-limit 0.5), and the moment dictionary verified numerically (m₁, m₂, m₃ at 1e-7/1e-13/1e-20).**
6. **C never cites Jensen** (verified: 0 hits in `claude-riemann-paper.txt` and `anthropic-informal-note.txt`) — this thread is genuinely new to the program, and the literature explains why the program's Weil-form line (which C does use) is the stronger route.

---

## 1. Context: C-RH2, attack-xiprime.md, prior tools

- **C-RH2** (idea-generator-control.md §C-RH2): "the correct entire-function analog of the Routh–Hurwitz cascade is the Jensen-polynomial criterion: RH ⟺ J_{d,n}(ξ) hyperbolic for all d, n (KKKM); GORT give effective degree-2 hyperbolicity; degree-2 hyperbolicity is a discriminant ≥ 0 condition in the Taylor data ξ(t₀), ξ′(t₀), ξ″(t₀); the dictionary degree-d Jensen ↔ moment order 2d identifies P2's third-moment input with degree-3 Jensen hyperbolicity." Probe: ξ, ξ′, ξ″ from the explicit formula; discriminant margin; kill if structurally uninformative.
- **attack-xiprime.md** (Round 1, RESOLVED) — the ξ′ facts this task asked about:
  - On-line ξ′-zeros: t = 0, plus **exactly one in each zeta-zero gap**; none in (0, γ₁); 999 in (0, γ₁₀₀₀] = N_ζ(γ₁₀₀₀) − 1. First gap root u₁ = 15.5857085898293423445957292355 (60 digits). Gap-2+ roots correct to ≤ 4.2·10⁻⁶.
  - ξ″ interlacing: **one ξ″-zero in every interval between consecutive ξ′-zeros** (20/20 intervals, 60 digits), all sign-changing.
  - The ξ′-two-trace certificate (simple∧on-line ≥ 0.85838 flat / 0.86864 quartic; distinct ≥ 0.92919 / 0.93432) is **PROVEN in Lean** (Remark 7.3, `Zeta23/XiPrime`), constants reproducible at 50 digits. This is the program's *existing* derivative-side input — a window-method certificate over (T, 2T], not a Jensen discriminant.
  - The previous agent's ten "small-t roots" were f64 artifacts (ψ-recursion sign bug + Stirling divergence); no hole in the window method.
- **Prior tools:** `tools/check_xiprime.py`, `tools/xiprime_check/` (check_small_t.py, check_tower.py, check_cert.py, check_count.py), `tools/zeta-rs/src/xiprime.rs`, data `zeros_1_1000.txt`, `xiprime_on_line_1_1000.txt`, Lean `Zeta23/XiPrime/`.

---

## 2. The dictionary

### 2.1 The Pólya–GORZ–GORTTW equivalence (PROVEN)

Expand at the symmetry point (GORTTW 1910.01227, eq. (1.1); Farmer's "even Jensen polynomials", 2008.07206 §3):

```
ψ(z) := ξ(1/2 + z) = Σ_{j≥0} γ(j)/j! · z^{2j},      γ(j) = ξ^{(2j)}(1/2) · j!/(2j)!
J_{d,n}(X) := Σ_{j=0}^{d} binom(d,j) γ(n+j) X^j     (hyperbolic = all roots real)
```

**Pólya 1927 [GORZ, GORTTW]:  RH ⟺ J_{d,n} hyperbolic for all d, n ≥ 0.** The RH_m hierarchy (GORTTW, after Thm 1.2): **ξ^{(m)} satisfies RH_m (all its zeros on the line) ⟺ J_{d,n} hyperbolic for all d ≥ 1, n ≥ m.** In particular RH₀ = RH, and the shift windows n = 1, 2 are the ξ′, ξ″ fragments.

*Normalization caveat:* GORZ 1902.07321 use γ defined by (−1+4z²)Λ(1/2+z) = Σ γ(n)/n! z^{2n} — a factor 8 above GORTTW's γ (ξ = (1/8)(−1+4z²)Λ). Hyperbolicity is scale-invariant; discriminant *values* are not. All numbers in this note use GORTTW's convention (γ(0) = ξ(1/2) = 0.49712077…), the convention C-RH2 cites.

### 2.2 Degree-d Jensen ↔ moment order 2d (the dictionary; CONJECTURED-as-RH-flavored, CHECKED NUMERICALLY here)

Under RH, the Hadamard product is F(z) = ξ(1/2)Π_γ (1 + z²/γ²), so

```
γ(n)/γ(0) = n! · e_n(1/γ²),      m_k := Σ_γ γ^{-2k}   (moment order 2k)
```

i.e. the degree-d Jensen polynomial J_{d,0} encodes the elementary symmetric functions of {1/γ²} up to order d, equivalently the power sums m₁, …, m_d (moment order 2d) via Newton's identities. **Verified numerically** (§3.4): m₁ = γ(1)/γ(0), m₂ = m₁² − γ(2)/γ(0), m₃ = (6e₃ − m₁³ + 3m₁m₂)/2 with e₃ = γ(3)/(6γ(0)), computed from the explicit-formula coefficients vs. direct zero sums (zeros_1_1000.txt) + analytic tail, agree to 2.9·10⁻⁷ / 1.4·10⁻¹³ / 7.1·10⁻²⁰. (The identity is exact only with zeros on the line; it holds at height ≤ γ₁₀₀₀ because those zeros are verified on-line — a numerical instantiation of the dictionary, not a proof.)

**Consequence for P2:** the C-RH2 claim "P2's third-moment input ↔ degree-3 Jensen hyperbolicity (an unconditional fragment at λ < 2/3)" is *real as a formal analogy* but **empty as a constraint**: degree-3 Jensen hyperbolicity is a PROVEN theorem at every shift (CNV/Dimitrov–Lucas d ≤ 3; GORZ Thm 2 d ≤ 8; Chasse d ≤ 2·10¹⁷), so the dictionary's low-order cases are all theorems, and P2's moments (traces of W_T) are a *different* moment hierarchy from Σγ^{-2k} — the dictionary is analogical, not literal. It adds nothing to P2.

### 2.3 The known hyperbolicity landscape (all PROVEN, unconditional or via verified RH)

| result | statement | status |
|---|---|---|
| CNV / Dimitrov–Lucas (in [GORTTW] intro) | J_{d,n} hyperbolic for d ≤ 3, all n | PROVEN, analytic |
| GORZ Thm 2 (1902.07321) | J_{d,n} hyperbolic for d ≤ 8, all n ≥ 0 | PROVEN, analytic |
| Chasse (2013; [GORTTW] intro, [F] §4.2) | J_{d,n} hyperbolic for d ≤ 2·10¹⁷, all n; and **if zeros are on the line for |γ| < T then J^{d,0} hyperbolic for d < T²** (dispersal) | PROVEN, analytic |
| GORZ Thm 1 / KKKM | for each d ≥ 1, J_{d,n} hyperbolic for all sufficiently large n | PROVEN |
| GORTTW Thm 1.1 | effective: n ≥ e^{c·d} | PROVEN |
| GORTTW Cor. 1.3 | J_{d,n} hyperbolic for d ≤ 9.36·10²⁰, all n (from Platt's RH₀(3.06·10¹⁰) + Thm 1.2) | PROVEN (modulo the finite verification) |
| Holland Thm 1.1 (2608.08682) | n³log²(n+2) ≥ K·d⁵ ⟹ J_{d,n} has d distinct negative real zeros (wedge n ≳ d^{5/3}); joint semicircle limit (Thm 1.2) | PROVEN, analytic |
| Wagner (2108.01827) | shifted LP class ⟺ shifted coefficients are degree-d multiplier sequences ⟺ all higher Turán inequalities | PROVEN (structure); Ξ in the shifted LP class per GORZ |

**The entire numerically-accessible (d, n) region is proven hyperbolic.** The open region is d > 2·10¹⁷ with n ≲ d^{5/3} — numerically unreachable: γ(n) ~ n!·(stuff)/(2π)^{2n} ~ (n/e)^n/(2π)^{2n}, astronomically scaled beyond n ~ 10¹⁵ (computing γ(10¹⁷) would require ζ^{(2·10¹⁷)}(1/2) — magnitude beyond any representable range), and the coefficient *information content* at degree d is limited by dispersal to height √d regardless. No finite computation can probe the open region.

### 2.4 Farmer's taxonomy and the dispersion mechanism (the counterweight, MUST be engaged)

Farmer 2008.07206 "Jensen polynomials are not a plausible route to proving the Riemann Hypothesis":

- **Generic analysis, not number theory.** Ki's theorem: there exist A_n, C_n with (−1)ⁿA_n Ξ^{(2n)}(C_n z) → cos z uniformly on compacta — repeated differentiation forces zeros onto the real axis with equal spacing (cosine universality; Berry; Farmer–Rhoades 0310252). This holds for the extended Selberg class (no Euler product) and for **random functions with Poisson statistics** (Pemantle–Subramanian). GORZ's Hermite Universality (A_n J^{d,n}_{ξ,ev}(C_n z + B_n) → H_d(z)) refines, not rescues, this: it is the same phenomenon viewed at one scale deeper.
- **The X_j counterexample (§4.2, Table 4.1).** X₁₀(z) = cos(z)·(z²−(10+i)²)(z²−(10−i)²)/((z²−(5π/2)²)(z²−(7π/2)²)) — a function whose "RH" fails at its 2nd zero (a pair moved off the line). Yet its classical Jensen polynomials J^{d,0} are **hyperbolic for all d ≤ 118**; for X₂₀ (4 real zeros), X₄₀ (12), X₆₀ (18): hyperbolic up to d = 749, 1897, 4242. The Taylor polynomials of the same functions detect the non-real zero at d = 20, 60, 118, 175. **Positive Jensen discriminants up to degree 4242 are compatible with RH failing at the 18th zero.**
- **Dispersal bound (Chasse):** all zeros on the line up to height T ⟹ J^{d,0} hyperbolic for d < T². Degree-d Jensen hyperbolicity encodes zero-location data only below height √d. My d ≤ 3 discriminants see below height ~1.7 — essentially nothing.
- **Taxonomy:** equivalences to RH are (A) subset/superset, (B) repackaging, (C) translation. Jensen polynomials are a repackaging that *disperses* the information in the Taylor polynomials (Lemma 4.1's equivalence (RH + simple zeros) ⟺ Taylor-polynomial real-rootedness). O'Sullivan's P^{d,n} (Hermite-combination criterion) is *even more* dispersing: J^{d,n} hyperbolic ⟹ P^{d,n} hyperbolic.
- **de Bruijn–Newman:** the operation Ξ → Ξ_t = ∫ e^{tu²}Φ(u)e^{izu}du loses information faster than differentiation; RH ⟺ Λ ≤ 0, and **Λ ≥ 0 is PROVEN (Rodgers–Tao), Λ < 1/2 (Polymath 15)**. So if RH holds, the heat-flow margin is **exactly zero** — the true distance to the RH-critical boundary in the dBN deformation is 0. This is the sharpest honest answer to "how close to the boundary": at the dBN scale, the margin is 0 (RH ⟹ Λ = 0); the coefficient-space margins of §4 are not distances to any boundary.

---

## 3. The coefficient computation (code-backed, explicit-formula, no zeros)

**Script:** `tools/jensen_ometer.py` (new, self-contained; ~470 s runtime).
**Command:** `cd /home/vstaln/riemann && uv run --quiet --with mpmath python tools/jensen_ometer.py` (mpmath, dps 60; the local-probe section runs at dps 25).

### 3.1 Method — the explicit-formula log-derivative tower at s = 1/2

```
L(s) = log ξ(s) = log(1/2) + log s + log(s−1) − (s/2)log π + log Γ(s/2) + log ζ(s)
L'(s) = 1/s + 1/(s−1) − (1/2)log π + (1/2)ψ(s/2) + ζ'/ζ(s)        (explicit formula)
L^{(k)}(s) = (−1)^{k−1}(k−1)!(s^{−k} + (s−1)^{−k}) + [k=1: −(1/2)log π]
             + ψ^{(k−1)}(s/2)/2^k + (ζ'/ζ)^{(k−1)}(s)
```

with (ζ'/ζ)^{(j)}(1/2) from the recurrence (w·ζ = ζ′): w^{(k)} = [ζ^{(k+1)} − Σ_{j<k} binom(k,j) w^{(j)} ζ^{(k−j)}]/ζ, using mpmath's ζ^{(k)}(1/2) — the analytic continuation of the prime-side Dirichlet series −Σ Λ(n)n^{−s}, computed by Euler–Maclaurin + functional equation, **no zero data anywhere**. Then F^{(k)}(0) = ξ^{(k)}(1/2) via the Bell/exponential recurrence, and γ(n) = F^{(2n)}(0)·n!/(2n)!.

### 3.2 Cross-checks (all pass)

| check | result |
|---|---|
| parity L′(1/2) = L‴(1/2) = L⁽⁵⁾(1/2) | 0.0 / 7.47e-60 / 3.98e-58 |
| ζ′/ζ(1/2) = (1/2)(γ + 3log2 + logπ + π/2) (functional-equation closed form) | 2.68609170961283279111647874872, diff 0.0 |
| (ζ′/ζ)″(1/2) = (χ′/χ)″(1/2)/2, (ζ′/ζ)⁽⁴⁾(1/2) = (χ′/χ)⁽⁴⁾(1/2)/2, χ = 2^sπ^{s−1}sin(πs/2)Γ(1−s) | 16.1659674921921150416672458974 (diff 7.47e-60), 768.261730894935429173694598516 (diff 3.98e-58) |
| γ(n) tower vs direct mp.diff of ξ(1/2+z) at 0 | diffs ≤ 2.5e-59 (n ≤ 3) |
| L″(1/2) = ξ″/ξ(1/2) = 2m₁ (dictionary) | 0.0462099862308379415778676208607 = 2·0.0231049931154 ✓ |
| Σ_γ 1/(γ²+1/4) vs closed form 1 + γ/2 − log(4π)/2 | 0.0230959976782 vs 0.0230957089661, diff 2.9e-7 (residual of the analytic density tail) |

### 3.3 The coefficients (60 digits)

```
γ(0) = 0.4971207781883141099127737396853977198073
γ(1) = 0.0114859721575727187676249382488160851323
γ(2) = 0.000246904036140636013780691582989702276272
γ(3) = 0.000004994132888313162432028552355067724221758
γ(4) = 0.00000009581343723225929219340648631276497622301
γ(5) = 0.000000001753923091213315303489457133184146682862
γ(6) = 0.00000000003077668832786528369526151242159777679754
γ(7) = 5.196051571847475304071348853364035054351e-13
γ(8) = 8.466271866458899923670642823387187309359e-15
```

All positive (theorem: γ(n) > 0 for all n [GORTTW intro]); γ(1) = ξ″(1/2)/2 = 0.0114859721575727… (tower vs direct mp.diff agree to 2.3e-61). L(1/2) = −0.698922267945331415298362020479.

### 3.4 Moment dictionary verification (CHECKED NUMERICALLY)

| moment | from γ (explicit formula) | zeros ≤ γ₁₀₀₀ + analytic tail | diff |
|---|---|---|---|
| m₁ = Σγ^{−2} | 0.0231049931154 | 0.0231052818009 | −2.887e-7 |
| m₂ = Σγ^{−4} | 3.71725992853e-5 | 3.71725994284e-5 | −1.431e-13 |
| m₃ = Σγ^{−6} | 1.44173931401e-7 | 1.44173931401e-7 | −7.098e-20 |

Tail model: N′(T) = (1/2π)log(T/2π), tail_k = (1/2π)T^{1−2k}[(log T − log 2π)/(2k−1) + 1/(2k−1)²] at T = γ₁₀₀₀ = 1419.422. The m₁ residual (2.9e-7) is the known O(T^{−2}log) density correction; m₂, m₃ are exact to 1e-13/1e-20.

---

## 4. Discriminant table and margins

### 4.1 Degree 2 — J_{2,n}(X) = γ(n) + 2γ(n+1)X + γ(n+2)X²

Δ = 4(γ(n+1)² − γ(n)γ(n+2)); hyperbolic ⟺ Δ ≥ 0 ⟺ log-concavity of γ.

| n | window (RH_m) | Δ = 4(g(n+1)²−g(n)g(n+2)) | r = g(n)g(n+2)/g(n+1)² | margin = 1 − r |
|---|---|---|---|---|
| 0 | ξ (RH₀) | 3.6745719281868359606477932e-5 | 0.9303676193903091305082 | **0.0696323806096909** |
| 1 | ξ′ (RH₁, n ≥ 1) | 1.4396527024613147258155939e-8 | 0.9409606772895854704709 | **0.0590393227104145** |
| 2 | ξ″ (RH₂, n ≥ 2) | 5.1385557479154465049239463e-12 | 0.9484936360049305185751 | **0.0515063639950695** |
| 3 | n ≥ 3 | 1.6835590434391462916546795e-15 | 0.954152514714922970023 | 0.045847485285077 |
| 4 | n ≥ 3 | 5.0970365829017601217213988e-19 | 0.9585774655608441006925 | 0.0414225344391559 |
| 5 | n ≥ 3 | 1.4342824372282485500358217e-22 | 0.9621443318219479447067 | 0.0378556681780521 |
| 6 | n ≥ 3 | 3.7702835360025332029844957e-26 | 0.9650886120991057156098 | 0.0349113879008943 |

**Margin law:** margin_n = 2∆(n+2)² where ∆(M) = √((1/2)(1 − γ(M−2)γ(M)/γ(M−1)²)) is **the GORTTW uniformizer** (Theorem 2.1: ∆(M) ~ 1/√(2M)); hence margin_n ~ 1/(n+2) → 0. Measured: margin·(n+2) = 0.177, 0.206, 0.229, 0.249, 0.265, 0.279 (n = 1..6) — the degree-2 Jensen polynomials **sit asymptotically ON the hyperbolicity boundary** (log-concavity becomes near-equality as n → ∞, exactly as the proven Hermite model predicts). So for d = 2 the margin is not "always ≫ 0"; it decays like 1/(n+2), but every value is a PROVEN-positive quantity.

### 4.2 Degree 3 — J_{3,n}(X) = γ(n) + 3γ(n+1)X + 3γ(n+2)X² + γ(n+3)X³

| n | Δ₃ (cubic discriminant) | roots | margin = min gap / spread (Hermite limit X³−6X: 0.5) |
|---|---|---|---|
| 0 | 2.01695158585295616902046e-13 | −70.3659823025, −49.1953948528, −28.7550823757 | **0.491224955793** |
| 1 | 2.48911737706150842240226e-20 | −72.7867506464, −51.7708595093, −31.8129271899 | **0.487089820666** |
| 2 | 2.61002987018766641738108e-27 | −75.094700278, −54.2077933931, −34.5817228814 | **0.48443910502** |

**Margin law:** the degree-3 margin is O(1) and already ≈ 0.49 at n = 0 — essentially the Hermite-limit value 0.5 (roots {0, ±√6}). Unlike d = 2, **d ≥ 3 sits away from the boundary with a finite relative margin in the limit** — the natural regime for a margin-based diagnostic would be d ≥ 3, not d = 2. (Both are PROVEN hyperbolic; this is a statement about where a hypothetical margin *diagnostic* could live, not about RH.)

### 4.3 The kill criterion from C-RH2

"Kill: if the discriminant margin is structurally uninformative (always ≫ 0), the diagnostic is weaker than the W_T one — record." **TRIGGERED, on both counts and more strongly:** (i) the d = 2 margin is not "always ≫ 0" but decays like 1/(n+2); (ii) every computed margin is PROVEN ≥ 0 (Chasse/GORZ), so no margin value can carry new information in the accessible range; (iii) by dispersal (d < T²), degree-d discriminants see zero data only below height √d, while the program's W_T-inertia margin (round-1-brief: Sylvester inertia of the compressed Weil form, constant 3/2 − (1/√2)cot(1/√2)) processes a full height-T box — **strictly more informative**. The comparison "Jensen margin vs W_T margin" is apples-to-oranges (one is a coefficient-space constant, the other a proportion-count margin), but in both framings the Jensen object is the weaker diagnostic. Recorded: C-RH2's Jensen discriminant is a **weaker diagnostic than the program's existing inputs**, and the *local* (pointwise) object is uninformative (§7).

---

## 5. Derivative tower (ξ′, ξ″)

**GORTTW:** RH_m ⟺ J_{d,n} hyperbolic for all d ≥ 1, n ≥ m. So the "derivative tower's Jensen discriminants" are the **same** J_{d,n} at shifts n ≥ 1 (ξ′) and n ≥ 2 (ξ″) — tabled in §4.1 (n = 1, 2 rows): all positive margins, all in the proven range (Chasse covers n ≥ 0, d ≤ 2·10¹⁷).

Facts already established by the program (attack-xiprime.md):
- RH₁ verified numerically to height γ₁₀₀₀ ≈ 1419: ξ′-zeros on the line = t = 0 + exactly one per zeta-zero gap (999 total), 60 digits; ξ″ interlacing: one per ξ′-gap (20/20 intervals).
- The ξ′-two-trace certificate (0.85838 flat / 0.86864 quartic simple; 0.92919 / 0.93432 distinct) is PROVEN in Lean — a genuinely different and stronger derivative-side input than any Jensen discriminant (it is a window-method proportion bound over (T, 2T], not a coefficient inequality).

Why the tower does NOT help (Farmer §2–3; confirmed by the new literature): Ki's cosine theorem is **unconditional and generic** — Ξ^{(n)} → cos (rescaled) holds for the extended Selberg class and for random functions with Poisson statistics; the Farmer–Rhoades "Differentiation Evens Out Zero Spacings" universality conjecture is now **PROVEN** (Campbell–O'Rourke–Renfrew 2410.06403 via finite free probability). Real-rootedness of ξ^(m) under RH is a consequence of RH (LP closed under differentiation), but its *generic* occurrence is analysis, not evidence; and RH_m for m ≥ 1 is strictly weaker than RH anyway.

---

## 6. Prime-side computability — the honest statement

**Claim (C-RH2):** "the coefficients involve sums over primes of log p·p^{−1/2}·cos(t log p), convergent and computable." **The parenthetical is false as stated.** Demonstrated:

- The raw series S(x) = Σ_{p≤x} log p·p^{−1/2}·cos(γ₁ log p) at t = γ₁ = 14.1347…: S(10³) = −7.47, S(10⁴) = −16.35, S(10⁵) = −24.06, S(10⁶) = 21.65, S(10⁷) = **206.4** — |S| grows ~ √x (the amplitude is ~ √x/(t²+1/4) in the crude integral model; the growth trend √x is confirmed). The series **diverges**; the Abel-weighted version also diverges in amplitude ~ √X.
- The coefficient values are the **functional-equation analytic continuation** of the prime-side Dirichlet series: ζ′/ζ(1/2) = (1/2)(γ + 3log2 + logπ + π/2) exactly (closed form, diff 0.0), and the higher (ζ′/ζ)^{(2k)}(1/2) = (χ′/χ)^{(2k)}(1/2)/2 — all verified to 1e-58. These are what the tower uses.
- Convergent prime/Dirichlet-side routes demonstrated: ζ′/ζ(2) = −Σ_p log p/(p²−1) from a sieve to 10⁷ gives −0.569960893091759 vs mpmath −0.569960993094533 (diff = 1e-7 = truncation tail); ζ(1/2) = η(1/2)/(1−2^{1/2}) from the alternating eta-series with Euler transform gives −1.46035450880959 (exact match; η(1/2) = 0.60489864342163037…, matching the known value to 17 digits).

So: the Jensen coefficients are computable from prime-side data **via the explicit formula's regularization** (functional equation / convergent eta-series / Mellin–ψ), but the bare "sum of log p·p^{−1/2}·cos(t log p)" is not convergent — the C-RH2 formulation must be corrected, and no finite prime truncation of it produces the coefficients.

---

## 7. The local pointwise probe (C-RH2's "10⁴ grid points at height 10³–10⁴")

**Object correction.** The classical Jensen discriminant lives in the (degree, shift)-indexed table of **global** coefficients at 1/2 (GORTTW eq. (1.2)); the shift n is a coefficient index (moment order), **not a height on the line**. C-RH2's "Taylor data ξ(t₀), ξ′(t₀), ξ″(t₀)" at points t₀ describes a *different* object — the discriminant of the local quadratic at s = 1/2+it₀:

```
D(t) = 2ξξ″ − ξ′²  (in g = ξ(1/2+it) terms: D = g′² − 2gg″)
```

Computed at 16 points (13 heights in [10³, 10⁴], plus γ₁, u₁ = first ξ′-zero 15.58570858982934, γ₂): **D(t) > 0 at all 16**. But this is generic: for any oscillating function with real zeros, D > 0 almost everywhere (g = sin t: D = cos²t + 2sin²t > 0), while a non-oscillating g = 1 + t² gives D = −4 < 0. D(t) merely echoes "oscillation" — for ξ that is **tautological** (real zeros of g ARE RH). Also |ξ(1/2+it)| ~ e^{−πt/4}·t^{O(1)} on the line, so the absolute D is exponentially tiny (D(1000) ≈ 8.8e-671) — only sign/relative margin carry meaning. **The local pointwise discriminant is not an RH-ometer and is not the Jensen discriminant; C-RH2's probe design targets the wrong parameterization.**

---

## 8. Honesty statement (exactly what a positive/negative margin does and does not certify)

Let Δ(d, n) be the discriminant of J_{d,n} (any d, n).

1. **RH ⟹ Δ(d, n) ≥ 0 for all (d, n)** (Pólya/GORZ). Contrapositive: **∃(d, n) with Δ(d, n) < 0 ⟹ RH is false.** This is a genuine (if classical) refutation channel — but note three qualifications:
   - it refutes RH **globally, not "at a height"**: Δ(d, n) has no height parameter (correcting the task's parenthetical);
   - for d ≤ 2·10¹⁷, Δ(d, n) ≥ 0 is a **theorem** (Chasse, GORZ), so a negative *computed* value there would signal a computation error, not a refutation — the channel only becomes operational at d > 2·10¹⁷;
   - that region is numerically unreachable (γ(n) ~ (n/e)^n/(2π)^{2n}-scale beyond n ~ 10¹⁵), so the channel is theoretical.
2. **Δ(d, n) > 0 for finitely many (d, n) proves nothing — not even locally.** Three independent reasons, all code/literature-backed:
   - (proven theorems) every accessible (d, n) is in the proven-hyperbolic region, so positivity carries zero new information;
   - (Farmer) positivity is **compatible with RH false**: the X_j functions violate "RH" at their 2nd–18th zeros yet have hyperbolic J^{d,0} up to d = 118…4242, and Hermite/cosine universality holds for random functions with Poisson statistics;
   - (dispersal) degree-d hyperbolicity only uses zero data below height √d (Chasse), so a finite-margin computation is an omen about the first ~√d zeros, which are already trivially on the line.
3. **The true "distance to the RH-critical boundary" is zero.** RH ⟺ Λ ≤ 0 in the de Bruijn–Newman deformation, and Λ ≥ 0 is PROVEN (Rodgers–Tao), Λ < 1/2 (Polymath). If RH holds, Λ = 0 — the heat-flow margin is exactly zero. No coefficient-space margin (0.03–0.07 here) is a distance to any RH boundary.
4. **Margin magnitudes are, however, meaningful as proven quantities.** margin_n(d=2) ≈ 1/(n+2) → 0 reproduces the GORTTW uniformizer law; margin(d=3) ≈ 0.49 matches the Hermite-limit 0.5. These confirm the effective-hyperbolicity theorems at 60 digits — a verification artifact, not an RH input.

---

## 9. Verdict

**The Jensen machinery offers a diagnostic omen only — no new certificate input. (REFUTED-as-certificate-route; the discriminant table itself PROVEN-in-literature and CHECKED NUMERICALLY.)**

- Every numerically-reachable (d, n) discriminant is **proven ≥ 0** (Chasse d ≤ 2·10¹⁷ analytic; GORZ d ≤ 8; GORTTW Cor. 1.3 d ≤ 9.36·10²⁰ via Platt) — a positive margin carries no information, and negativity in that range would be a computation error, not a refutation.
- The positivity is **generic analysis compatible with RH false** (Farmer: Ki/Kim/Pemantle–Subramanian universality; X_j counterexample to d = 4242), and the object **disperses** information (d < T²) — strictly weaker than the program's W_T-inertia margin (height-T box) and than the ξ′-two-trace certificate (PROVEN in Lean).
- The dictionary (degree-d ↔ moment order 2d) is real and now numerically instantiated (m₁, m₂, m₃ at 1e-7/1e-13/1e-20), but its order-3 fragment is a **proven** constraint — it adds nothing to P2, and P2's moments are a different hierarchy (traces of W_T) anyway.
- The derivative tower's real-rootedness is generic (cosine universality, now PROVEN by Campbell–O'Rourke–Renfrew); RH_m is strictly weaker than RH; the shifts n = 1, 2 are proven-hyperbolic and RH₁/RH₂ are numerically verified (attack-xiprime.md).
- **What this probe genuinely contributes:** (a) the object correction (Jensen discriminants are (d,n)-global; the height-grid design in C-RH2 is a misidentification, and the local D(t) is generic-oscillation-only); (b) the correction of "convergent prime series" (the raw series diverges — demonstrated to ~√x growth at x = 10⁷; the coefficients are the functional-equation continuation, with closed forms ζ′/ζ(1/2) = (1/2)(γ+3log2+logπ+π/2) etc.); (c) a 60-digit verified coefficient table (parity + closed-form + direct-diff + dictionary + Σ1/(γ²+1/4) cross-checks, all ≤ 1e-58 except the analytic-tail-limited dictionary checks); (d) the margin laws (d = 2: → 0 like 1/(n+2), the GORTTW uniformizer; d = 3: O(1), Hermite-limit 0.5) — proven quantities useful as benchmarks; (e) confirmation that the Jensen thread is new to the program (C cites no Jensen).
- **Recommendation:** do not fund a Jensen-discriminant attack further; if the *margin structure* is ever wanted as an input, the only regime with a nontrivial (non-degenerate, non-proven) margin is d ≥ 3 at n ≲ d^{5/3} beyond the Chasse range — numerically unreachable. The program's scarce compute is better spent on the W_T-inertia/Weil-form line (round-1-brief, attack-lpdual) and the ξ′-tower certificate (attack-xiprime.md §5: Farmer-style combination over ξ^(j), CONJECTURED), which are genuinely different and stronger inputs.

---

## 10. Commands and code location

- All numbers in §3–§7: `cd /home/vstaln/riemann && uv run --quiet --with mpmath python tools/jensen_ometer.py` (dps 60; local probe at dps 25; ~7.7 min; full output preserved in this session's log). Script: `tools/jensen_ometer.py` (new file; no existing tool path modified).
- Prior ξ′/tower facts cited from `research/notes/attack-xiprime.md` (commands there: `tools/xiprime_check/check_small_t.py`, `check_tower.py`, `check_cert.py`, `check_count.py`).
- Literature read first-hand for this note: GORTTW 1910.01227 (full text), GORZ 1902.07321 (Thm 1, Thm 2, γ-convention), Farmer 2008.07206 (full text), Holland 2608.08682 (Thm 1.1, Thm 1.2); abstracts fetched for O'Sullivan 2007.13582, Wagner 2108.01827, Romik 1902.06330, Rodgers–Tao 1801.05914, Polymath 1904.12438, Farmer–Rhoades math/0310252, Campbell–O'Rourke–Renfrew 2410.06403, Farmer 2211.11671 (all downloaded to `research/papers/` per `paper-finder-jensen.md`, 39 PDFs, VERIFIED-BY-FETCH).

**Honesty footer:** every numeric claim in §3–§7 was produced by `tools/jensen_ometer.py` and is reproducible with the command above; the theorem attributions in §2–§5 are read from the cited papers (full text for GORTTW/GORZ/Farmer/Holland). The verdict is a label, not a proof: the *route* is closed by literature (Farmer) plus the proven-hyperbolicity landscape; nothing here changes the state of RH.
