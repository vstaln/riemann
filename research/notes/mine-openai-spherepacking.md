# Mining OpenAI's "Ten Advances" — the Cohn–Elkies LP exact evaluation (transfer test for our certificate class)

**Agent:** EXECUTIONER (analogy-domain-transfer + investigation + epistemology lens)
**Date:** 2026-08-12 (round 2.5). **Status:** complete — technique extracted, mapped, numerically tested, verdicts issued.
**Sources mined:** `research/external-results/openai-ten-proofs/SpherePacking.lean` (55,616 lines; key sections 1–280, 188–260, 1880–2050, 2940–3080, 4890–5010, 53440–53600, 55376–55616); `research/papers/openai-ten-proofs.pdf` (markitdown → /tmp/openai-ten-proofs.md); `research/papers/openai-reasoning-walkthroughs.pdf` (→ /tmp/openai-walkthroughs.md).
**Code:** `scratch/mine_openai/mine_openai_numerics.py` (final copy `research/notes/mine-openai-spherepacking.py`).
**Command:** `cd /home/vstaln/riemann && uv run --quiet --with mpmath python scratch/mine_openai/mine_openai_numerics.py` (all numbers below from that run; a second sympy exact check for the kernel identities is inline in the round transcript).

---

## 0. The program's goal (stated)

**One discovery = a 1%+ lower bound**: beat the in-class ceiling **0.6818** (the bandwidth-one certificate class, `attack-lpdual.md`, `close-inclass-gap.md`) or push the *real* constant **+1pp over 0.6725** (Theorem D). Breaking the class requires (a) the Gram-stability refinement (`discovery-gram-stability-673.md` — the external repos that keep tr Ψ(M)), (b) beyond-bandwidth-1 form-factor data (the only positive-priced input, `attack-pricing-sheet.md`), or (c) a new global technique. This round mines the sphere-packing exact-LP evaluation for transferable technique. **Verdict: the Mellin/gamma machinery does NOT transfer; the one live thread is a methodological identification (CE's "keep the sign location" principle is the same move as Gram-stability), which re-fires the already-open adjudication question — it does not open a new attack.**

---

## 1. What OpenAI actually proved (extracted, code-cross-checked)

### 1.1 The exact LP evaluated
`CohnElkies.Admissible d` (Lean line ~60): f : ℝ^d → ℝ Schwartz, **radial**, real, with
`fourier_nonneg : ∀ξ, 0 ≤ (𝓕f)(ξ)` (Fourier transform nonneg on ALL of ℝ^d — the bandwidth-∞ analog), `fourier_zero_pos : 0 < (𝓕f)(0)`, `outside_nonpos : ∀x, ‖x‖ ≥ 1 → f(x) ≤ 0` (f ≤ 0 outside the unit ball). Quotient `q(f) = f(0)/(𝓕f)(0)`; `linearProgram d = (V_d/2^d)·sInf quotientSet`, V_d = π^{d/2}/Γ(d/2+1). This is exactly the paper's (2)–(3). `FullAdmissible` drops radiality; `fullLinearProgram_eq_radial : fullLinearProgram d = CohnElkies.linearProgram d` — **radialization is lossless** (rotational averaging preserves both sign conditions and both origin values).

**The result** (`SharpFullCohnElkiesManuscriptConclusions`, Lean line ~55431; paper Thm 1.1):
- `linear_program_root`: LP(d)^{1/d} → √(e/(2π)) = **0.6577446234794569…**;
- `base_two_decimal_certificate`: ½·log₂(2π/e) = **0.604400544291677695341677307053** (verified inside the Lean Ioo — the base-2 exponent; beats Kabatianskii–Levenshtein 0.59905576, first exponent improvement since 1978);
- `root_before_infimum`: sInf(quotient^{1/d})/√d → 1/π = 0.3183098861837907… (the sign-uncertainty constant, paper Thm 1.2);
- `universal_nonnegative_delta`: ∃ δ(d) → 0, δ ≥ 0, such that for ALL FullAdmissible f: 2^d/V_d·(√(e/2π) − δ(d))^d ≤ q(f) — a **uniform lower bound on every admissible function's quotient** ("no Cohn–Elkies function improves the exponent").

### 1.2 The Mellin method (the transfer candidate)
The whole machinery (Lean lines 188–260, 1880–2050; paper §2.2) reduces the infinite-dimensional radial FT to 1D Mellin analysis:
- Radial integration: ∫_ℝ^d g = S_d·∫₀^∞ g(r)r^{d−1}dr, so point evaluations/integrals of radial functions are 1D Mellin transforms of the profile.
- **Mellin–Hankel functional equation** (paper (9)–(10), Lean `radialMellinMultiplier`): with λ = d/2, X̂_g(t) = m_λ(t)·X_g(−t), **m_λ(t) = π^{it}·Γ((λ−it)/2)/Γ((λ+it)/2)**, and |m_λ(t)| = 1 on the real axis (a unitary gamma-ratio phase — verified numerically to 60 digits, §3-H). The continuation off the axis carries the high-dimensional information (walkthrough §1.3: "its continuation off that axis contains the high-dimensional information missing from norm inequalities").
- Gamma identities (paper eq. (7), Lean `integer_gamma_product`/`half_integer_gamma_product`): |Γ(ib)|² = π/(b·sinh πb), |Γ(½+ib)|² = π/cosh(πb) (verified, §3-B).

### 1.3 The universal (certificate-side) lower bound — paper §3
For any admissible F, set a = ((𝓕F)(0)/F(0))^{1/d}, h(x) = F(ax); then g = ĥ − h is anti-self-Fourier, ∫g = 0, g ≥ 0 for ‖x‖ ≥ 1/a, and **the whole negative half of its L¹ mass lies inside B(0, 1/a)** (walkthrough §1.2). Proposition 3.1: every radial Schwartz Fourier eigenfunction (ĝ = ςg, g(0) = 0) has *exponentially little* L¹ mass in B(0, c√d) when c < 1/π. The proof is a **Mellin-strip obstruction**: the normalized Mellin transform Z on |Im t| ≤ λ has upper boundary |Z(y+iλ)| ≤ 1 (total-mass control) and lower boundary from the FEQ, log|Z(y−iλ)| ≤ h_λ(y) = λlog(πR²) + log|Γ(−iy/2)| − log|Γ(λ+iy/2)|; harmonic measure / strip Poisson interpolation (kernel P_σ, mass M_σ = (1−σ)/2) with the sharp constant J_σ → log(π/2) forces the rate → log(π²c²) < 0 iff c < 1/π; shifted Mellin inversion turns the negativity into the interior-mass estimate. Hence 1/a ≥ (1/π − o(1))√d for every admissible F — the "universal" lower bound on the LP value, matching `universal_nonnegative_delta`.

### 1.4 The matching primal family — paper §4, the saddle ansatz
"The lower bound explains the target radius but does not construct a packing auxiliary function" (walkthrough §1.6). Construction: start from the Gaussian g_G(r) = 2π^{λ/2}e^{−πr²} (Mellin envelope E_G(t) = π^{it/2}Γ((λ−it)/2), already m_λ(t)E_G(−t) = E_G(t)); multiply by an even deformation e^{λh_ε(t/λ)}, h_ε(ζ) = ∫w(a)(cos(aζ)−1)da, determined by a **signed density** w = w_s + w_B (negative shell moves the sign radius in; distant positive shell restores decay). The **ideal density** (paper (32), Lean `saddleOriginValue`/`plusSaddleMellinData`)

  w∗(a) = e^{−2a}/(2a²·cosh a),   ∫₀^∞ w∗(a)·a·sinh(a)da = ½·log(π/2)   (Wallis/Frullani, verified §3-C),

saturates the pointwise damping constraint |w(a)|·cosh(a) ≤ e^{−2a}/(2a²) and displaces the Gaussian saddle: at u = 1, r/√d → (2π)^{−1/2}·exp(−½log(π/2)) = **1/π** (paper (33), Lean `root_before_infimum`). The actual functions are inverse Mellin transforms of gamma-product data (`plusSaddleFunction = mellinInv ℓ (Γ(z/2)·phase·polynomial)`), made Schwartz by truncating/tapering the ideal density. Stirling converts the radius to the exponent: LP^{1/d} ~ [V_d^{1/d}/2]·[(1/π)√d] → √(e/(2π)) (verified §3-D).

### 1.5 The classical bottleneck and what they added (task item 1c)
The bottleneck was **not** a missing bound but a missing coordinate system: the only available route (norm comparisons: Cauchy–Schwarz, Hausdorff–Young, Gaussian/Laguerre eigenfunctions) "reaches only R ≍ √(d/(2π))… corresponding to the linear-program root √(e/8)" = 0.583 < 0.599 (KL) (walkthrough §1.2; √(e/8) verified §3). The reason: **"A global norm forgets where the negative mass lies."** What they added: (1) the Mellin–Hankel FEQ as the coordinate system in which *location* is preserved (the strip's boundary values encode the local radial mass distribution); (2) a **local mass-exclusion** universal bound via the strip maximum principle with the computable sharp constant log(π/2) (not a global norm inequality); (3) the explicit saddle family achieving the matching value. The exact LP value came from **matching a universal certificate-side bound with an explicit witness family** — the same architecture our program already used to close the in-class gap (ceiling + r = 1−x).

---

## 2. Structural mapping (Cohn–Elkies ↔ our program)

| Cohn–Elkies object (Lean / paper) | Our object (`attack-lpdual.md`, `close-inclass-gap.md`, `attack-kernel.md`) |
|---|---|
| test function f : ℝ^d → ℝ, radial, Schwartz | certificate r on [0,1] (window v on [−1/2,1/2]) |
| admissible: 𝓕f ≥ 0 on ALL ℝ^d (**bandwidth-∞**); f ≤ 0 for ‖x‖ ≥ 1 | v ≥ 0, supp v ⊆ [−1/2,1/2] (**bandwidth-1**); kernel box \|r\| ≤ 1, r(1) = 0 |
| quotient q(f) = f(0)/(𝓕f)(0) — **point-evaluation ratio** | trace-ratio c_λ(v) = λ(∫v)²/(∫v² + λ²∬\|s−s′\|vv) — **L² quotient**; LP value v = c₀ + ∫₀¹ r·x |
| LP_d = (V_d/2^d)·inf q — density bound | in-class optimum = p₀ + \|E(1)\| = 0.6818312305953419 (**PROVEN TIGHT**, exact to 7.8·10⁻⁴³) |
| radialization: full LP = radial LP (lossless WLOG) | vacuous (already 1D/radial) |
| Mellin–Hankel FEQ: X̂_g(t) = m_λ(t)X_g(−t), m_λ = π^{it}Γ((λ−it)/2)/Γ((λ+it)/2), \|m_λ\| = 1 | **NO analog**: kernel \|s−s′\| has Fourier symbol −1/(2π²ξ²) (pole at 0, not a phase); spectrum = transcendental tan/cot roots + π-family (§3-G) |
| universal certificate-side lower bound (Mellin-strip obstruction + gamma identities) | Lean ceiling `ceiling_law256_signed` — uniform bound over ALL valid certificates, **PROVEN, TIGHT** (finite-N, exact: strictly stronger than the asymptotic δ-statement) |
| sharp family: inverse Mellin of gamma-product data + ideal density w∗ | optimal certificate r = 1−x — explicit, rational, exact (`close-inclass-gap`) |
| asymptotics d → ∞ (Stirling, gamma) | **fixed** dimension (bandwidth 1): no limit parameter to take |

---

## 3. Numeric reproductions (all from the cited script; 60-digit mpmath unless noted)

| # | Quantity | Value (script output) | Status |
|---|---|---|---|
| A1 | ½·log₂(2π/e) | 0.6044005442916776953416773070530575987959 | inside Lean Ioo ✓ |
| A2 | √(e/(2π)) | 0.6577446234794569140696787287714745150969 | matches `linear_program_root` |
| A3 | 1/π | 0.3183098861837906715377675267450287240689 | matches `root_before_infimum` |
| A4 | ½·log(e/(2π)) | −0.4189385332046727417803297364056176398614 | matches `natural_logarithmic_rate` |
| B | \|Γ(ib)\|² = π/(b·sinh πb); \|Γ(½+ib)\|² = π/cosh(πb) | residuals ≤ 3·10⁻⁶⁰ at b ∈ {0.3, 1.7, 5.43} | ✓ |
| C1 | ∫₀^∞ e^{−2a}tanh(a)/(2a)da | 0.225791352644727432363097614947 = ½log(π/2), 60-digit match | ✓ |
| C2 | (2π)^{−1/2}·exp(−½log(π/2)) | 0.318309886183790671537767526745 = 1/π, 60-digit match | ✓ (the saddle displacement) |
| C3 | w∗ saturation | w∗(a)·cosh(a) − e^{−2a}/(2a²) = 0 exactly | ✓ |
| D1 | V_d^{1/d}·√d → √(2πe) = 4.132731 | d=10³: 4.11612; d=10⁵: 4.13247 | O(1/d) trend ✓ |
| D2 | LP^{1/d} → √(e/(2π)) = 0.657745 | d=10³: 0.65510; d=10⁵: 0.65770 | O(1/d) trend ✓ |
| E1 | p₀ (law simple fraction, Lean rational) | 0.681828687463831474255951887239 | ✓ (`close-inclass-gap`) |
| E2 | E(1) = −1/(6·256²) | −2.5431315104166666666666666667·10⁻⁶ | ✓ |
| E3 | in-class optimum p₀+\|E(1)\| | 0.681831230595341890922618553905 | ✓ (matches exact rational 0.681831230595341890922618553905170067178979166…) |
| E4 | Thm D 3/2−(1/√2)cot(1/√2) | 0.672500703679411645734379790803 | ✓ |
| E5 | gap | 0.00933052691593 | ✓ |
| E6 | v*(p₁) = p₁+\|E(1)\| (shadow price 1) | 0.700002543132 / 0.800002543132 / 1.00000254313 | ✓ |
| E7 | curiosity: 1−p₀ vs 1/π | 0.318171312536 vs 0.318309886184, diff 1.386·10⁻⁴ | labeled COINCIDENCE (law is rational; no π in its construction) |
| F1 | Q(cos(√2u)) = ½+(1/√2)cot(1/√2) | 1.327499296320588354265620209196704811407; 2−Q = 0.6725007036794116 ✓ | ✓ |
| F2 | rescaled family Q(c) = c+(1/√2)cot(√2c) | c=0.30→1.86545, 0.40→1.51373, 0.45→1.40690, 0.50→1.32750, 1.1107→1.11072 | matches `attack-kernel` table |
| G1 | T(cosh(ks)) = λcosh(ks), λ = 2/k², tanh(k/2)=2/k | k = 2.39935728051547, λ = 0.347408269026898; numeric diff ≤ 3.9·10⁻⁶² | ✓ (sympy-verified identity) |
| G2 | negative even branch tan(k/2) = −2/k | k = 5.59677209156777, λ = −0.06384909579 | ✓ |
| G3 | π-family λ = −2/((2m+1)²π²) | m=0: −0.202642367285; m=1: −0.0225158185872; m=2: −0.00810569469139 | ✓ (even cos + odd sin, both) |
| G4 | T(sin(πs)) = −(2/π²)sin(πs) | verified to 60 digits; I+T min eigenvalue = 1−2/π² = 0.7973576327 | ✓ (matches validator-corrected ~0.797) |
| H | \|m_λ(t)\| = 1 (CE multiplier) | 1.0 at t ∈ {1, 3, 10}, 60 digits | ✓ |
| I | √(e/8) = 0.58291 (naive norm-route root) | binary exp −0.77865 | walkthrough-reported, computed |

**The kernel identities G1–G4** were derived exactly with sympy (round transcript): T(cosh ks) = sinh(k/2)/k − 2cosh(k/2)/k² + 2cosh(ks)/k² (eigenfunction ⟺ tanh(k/2)=2/k), T(cos ks) = sin(k/2)/k + 2cos(k/2)/k² − 2cos(ks)/k² (⟺ tan(k/2)=−2/k or k=(2m+1)π), T(sin ks) = 2s·cos(k/2)/k − 2sin(ks)/k² (⟺ k=(2m+1)π). The spectral data of our kernel is **transcendental tan/cot/π roots — no gamma products** — the precise structural reason the CE Mellin evaluation has no analog here.

---

## 4. Transfer verdicts (per mining question)

### Q1 (task item 3a): beyond-bandwidth-1 input — does the Mellin/gamma technique evaluate certificates with beyond-1 form-factor data? — **DEAD**
- The Mellin machinery evaluates *test-function quotients* (point evaluations and integrals of radial functions). In CE, "data" = the admissible class, and the technique computes the class's optimum. In our program, the beyond-1 datum is the second-moment value **F(α) at α > 1** — an *arithmetic* quantity (Hardy–Littlewood prime-pair / Montgomery-conjecture territory, `attack-m29.md`), which enters as a *hypothesis number*, not as an integral to evaluate. No Mellin/gamma identity produces prime-pair facts; the technique has no hook into F(α).
- Independently: our in-class LP is **already evaluated exactly** — v* = p₀ + 1/(6·256²) − δ′ = 0.6818312305953419 with exact rational arithmetic and the Lean ceiling tight to 7.8·10⁻⁴³ (`close-inclass-gap`, `verify_exact_cert.py`). There is no "beyond the numeric optimum" to reach in-class.

### Q2 (task item 3b, mining target 2): the 0.6818 ceiling robustness — does the "universal nonnegative delta" argument have an analog? — **PARTIAL: the analog already exists and is strictly stronger**
- CE's `universal_nonnegative_delta` is an *asymptotic* uniform lower bound on all admissible quotients (2^d/V_d·(√(e/2π)−δ_d)^d ≤ q(f) ∀f). Its logical role — "no certificate in the class beats the threshold" — is played in our program by the Lean **`ceiling_law256_signed`**: v ≤ p₀ + M(|r′(1)| + ∫|r″|) for every valid certificate, which is (i) uniform over the class, (ii) PROVEN (Lean), (iii) exact at finite N (not asymptotic), (iv) PROVEN TIGHT (attained by r = 1−x to 7.8·10⁻⁴³). The robustness question is **settled**: our ceiling is the CE-universal-bound's counterpart, and it is stronger.
- Transferable *architecture* lesson (already realized in our program): CE closed the rate gap by **matching a universal bound with an explicit witness family**; we matched (ceiling + r = 1−x). Nothing new to import. The residual 0.6725 → 0.6818 gap for the real zeros is a **data gap** (p₁, shadow price 1), not a technique gap — CE provides no mechanism that changes this.

### Q3 (task item 3c): bandwidth-restricted analog of the exact-LP technique — **DEAD (as a technique), and the question is already answered**
- The Mellin–Hankel FEQ is intrinsically **global in frequency**: the gamma-ratio multiplier is the Mellin transform of the Bessel/Hankel kernel over all frequencies; there is no band-[−1,1]-restricted gamma product (a band integral of the Hankel kernel is not a gamma). The strip-maximum/harmonic-measure argument needs *both* boundary values (the full FT). The saddle analysis lives on contours at height u ≈ 1 in the *frequency* plane — not a band. CE's exact evaluation is bandwidth-∞ by construction; there is no bandwidth-restricted version to import.
- The in-class LP is already exactly evaluated (Q1); "beyond attack-lpdual's numeric optimum" does not exist — the numeric optimum was upgraded to exact in `close-inclass-gap`. What moves the *real* constant is only p₁ (data, M29/CONJECTURED) or the Gram-stability structure (Q4).

### Q4 (mining target 3 / discovery-note mapping item c): is CE's radialization/symmetrization the SAME move as the Gram-stability refinement? — **NO — false analogy (and this is the useful finding)**
- CE radialization (§2.1, `fullLinearProgram_eq_radial`) is a **lossless WLOG reduction**: rotational averaging preserves every sign condition and both origin values, so the LP value is *unchanged*. It discards angular structure *without losing optimality*.
- Gram-stability (`discovery-gram-stability-673.md`: ainta/trmdy keep tr Ψ(M), moving 0.6725 → 0.6730/0.6731/0.6732) is the **opposite** move: it *recovers* a positive term that the rank–trace inequality's equality case discarded, **changing the value**. A value-preserving reduction ≠ a value-changing strengthening — different categories.
- The genuinely transferable *principle* (from the walkthroughs, §1.5/§1.2): **"a global norm forgets where the negative mass lies; keep the sign location"** — CE's breakthrough was replacing global norm estimates by location-preserving local estimates. That is *the same lesson* our program's Gram-stability discovery encoded (rank–trace = global-norm bound that discards the atom inner-product structure; tr Ψ(M) = the kept location/structure). Two independent programs (OpenAI sphere packing; ainta/trmdy on Riemann) converged on the same meta-move: **the discarded fine structure is the next source of value.** This re-confirms the priority of the open Gram-stability adjudication questions (Q1/Q2 of `discovery-gram-stability-673.md`), but it does not transfer a new technique into our class.

### Cross-checks against the pricing sheet
The mining leaves `attack-pricing-sheet.md`'s ranking intact: within the current certificate class the only positive-priced input remains the beyond-1 *range* (M2: dv*/dA = 0.6363/A³); m₃ and min-gap stay negative. The Mellin route (i) does not re-open the negative-priced inputs (its spectral-data claim is orthogonal), (ii) does not create a route to beyond-1 arithmetic data, (iii) confirms the in-class ceiling is the CE-"universal-bound" analog, i.e. the class is *exhausted* — consistent with `attack-lpdual.md` §5 ("no missing constraint inside bandwidth one").

---

## 5. Recommended next step (if anything transfers)

**Fund the Gram-stability adjudication, not a Mellin re-attempt.** The mining's only ALIVE thread is Q4's methodological identification: CE and the external Riemann repos both profited from *keeping* structure that a global bound discards. Concretely, the round-3 priority (per `discovery-gram-stability-673.md`, standing questions) is:
1. **Q2**: does tr Ψ(M) ≥ the stability bound hold for the 256-law — i.e. does the strengthened inequality beat the in-class ceiling 0.6818, or is the ceiling law robust to the Gram constraint? (This is the direct route to "beat 0.6818", the 1%-over-ceiling discovery; the mining confirms no *other* mechanism — Mellin included — offers one.)
2. **Q1**: does the stability refinement transfer to the on-line (2/3) and distinct (5/6) constants?
3. Negative-control: a full write-up that the CE exact-LP evaluation is bandwidth-∞-intrinsic (Q1/Q3 DEAD) so the round does not get re-funded on a false hope — this note is that write-up.

---

## 6. Honesty labels / epistemic status (s4h-epistemology)

| Claim | Label |
|---|---|
| All numbers in §3 (A1–I) | **CHECKED NUMERICALLY** — mpmath 60-digit / sympy exact, script `research/notes/mine-openai-spherepacking.py`, command in §header |
| Kernel identities G1–G4 (spectral data of \|s−s′\| = tan/cot/π roots) | **PROVEN** — sympy integration + numeric verification to 10⁻⁶² (the identities themselves; the "no gamma" reading is a direct consequence) |
| CE theorems cited (exact_limit, base_two_decimal_certificate, universal_nonnegative_delta, fullLinearProgram_eq_radial, root_before_infimum) | **PROVEN (Lean)** — OpenAI's formalization (this round read, not re-checked) |
| Our ceiling `ceiling_law256_signed` tight; in-class optimum 0.6818312305953419 | **PROVEN** (per `close-inclass-gap.md`, modulo the τ/512 + δ′ sliver ≈ 7.8·10⁻⁴³ and EnclOK) |
| Q1/Q3 DEAD ("no band-restricted Mellin"; "no Mellin route to beyond-1 F") | **JUDGMENT with supporting evidence** — (i) the FEQ is global by construction (paper §2.2), (ii) the in-class exact evaluation already exists (moot), (iii) beyond-1 F values are arithmetic/conjectural (M29). A fully general "no such technique exists" is not provable; the load-bearing part (our in-class evaluation is exact) is PROVEN. |
| Q4 "radialization ≠ Gram-stability" | **JUDGMENT** — structural comparison (value-preserving reduction vs value-changing strengthening), documented; the CE-walkthrough "keep the sign location" principle is quoted from the primary source |
| "The class is exhausted inside bandwidth one; only p₁ (data) or Gram-structure moves the constant" | **PROVEN** (shadow price 1, `attack-lpdual` §3/§5; in-class tightness) + **JUDGMENT** (the beyond-1/gram feasibility labels) |
| E7 (1−p₀ ≈ 1/π coincidence) | **COINCIDENCE**, no mechanism claimed — the law is exact-rational with no π in its construction; difference 1.386·10⁻⁴ (a curiosity line only) |

**Weakest links (justification chain):** (i) the CE-side reading rests on OpenAI's Lean (trusted as a source, not re-checked here — a validator could run `#print axioms` on SpherePacking.lean as a follow-up); (ii) the "no band-restricted Mellin analog" is a negative claim (JUDGMENT, per table); (iii) the Gram-stability priority re-statement inherits the open Q1/Q2 of `discovery-gram-stability-673.md` (ainta/trmdy verifiers passed our reruns; tawanerguo-cn unverified).

---

## 7. Files & commands

- Mining note: `research/notes/mine-openai-spherepacking.md` (this file)
- Numerics: `research/notes/mine-openai-spherepacking.py` (final copy of `scratch/mine_openai/mine_openai_numerics.py`)
- Run: `cd /home/vstaln/riemann && uv run --quiet --with mpmath python scratch/mine_openai/mine_openai_numerics.py`
- Lean: `research/external-results/openai-ten-proofs/SpherePacking.lean`
- Paper: `research/papers/openai-ten-proofs.pdf` (markitdown → /tmp/openai-ten-proofs.md); walkthroughs `research/papers/openai-reasoning-walkthroughs.pdf` (→ /tmp/openai-walkthroughs.md)
- Related: `attack-lpdual.md`, `close-inclass-gap.md`, `attack-kernel.md`, `attack-pricing-sheet.md`, `discovery-gram-stability-673.md`, `attack-m29.md` (referenced, unchanged)
