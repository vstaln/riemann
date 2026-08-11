# M29 — Beyond-bandwidth-1 probe: the off-diagonal prime-pair sum at X = T^{1+ε}

**Agent:** EXECUTIONER. **Round:** 2. **Date:** 2026-08-11.
**Question:** does any *known unconditional* upper bound on the off-diagonal prime-pair sum
Σ_{n,m ≤ T^{1+ε}} Λ(n)Λ(m) g(log n) h(log m) (over |log n − log m| ≤ δ, or the paper's actual form)
clear the certificate's O(1)-at-constant-scale tolerance (in-class gap 0.6725 → 0.6818 = 1.4%)?
**Expected outcome (per brief):** documented negative — closes the last live "is there a proven sliver
of form factor beyond α = 1" question.

**Verdict (up front):** **documented negative, PROVEN.** The Montgomery–Vaughan Hilbert inequality —
the sharpest proven tool, and the very engine of the λ ≤ 1 regime — gives |O_1| ≪ L²X, whose
normalized contribution to ‖Â‖²_F exceeds the certificate tolerance by a measured factor
**≈ 3.6·10³ – 3.7·10⁴** at T = 10⁴–10⁶ and is **30–230× the diagonal main term**, growing like
T^ε/poly(log T) → ∞ for any fixed ε > 0. Every other proven bound (trivial/sieve 2δX², Selberg sieve,
Vinogradov–Korobov-type savings) is equal or worse. The only input that *would* clear the tolerance is
a **value** (Hardy–Littlewood / Montgomery pair-correlation-conjecture), which is CONJECTURED.
All claims below carry honesty labels; nothing is re-derived beyond the numerics in §3.

---

## 1. The exact sum the certificate would need to bound

**Source objects** (paper = research/papers/claude-riemann-paper.txt; N = anthropic-informal-note.txt;
B24 = baluyot-etal-2306.04799.txt):
- The prime side of the second moment is M[P_X, P_X] with a_n = Λ(n)/√n, y_n = log n, X = (T/2π)^λ
  (paper §5; X = T^{1+ε} here). Prop 5.6 splits it as D + O_1 + O_2 with
  **D = (T/π)·Σ_{n≤X} a_n²·g(y_n)** (the diagonal; g(y) = (L−y)_+, L = log X, so D = (T/π)L³/6·(1+O(1/L))),
  and the off-diagonal
  **O_1 = (1/2π²)·Re Σ_{n≠m} a_n a_m · [ (n/m)^{2iT}(α⁺_m + α⁻_n) − (n/m)^{iT}(α⁺_n + α⁻_m) ] / (i(y_n − y_m))**
  where α±_n = ∫_{±} Φ(x)² n^{ix} dx, |α±_n| ≤ πbL (paper (5.10)–(5.11)). This is a combination of four
  sums of the shape Σ_{n≠m} x_n z_m/(y_n − y_m) with |x_n|,|z_n| ≤ a_n·πL.
- The equivalent additive form named in paper §7.5(f): a Hardy–Littlewood-type asymptotic for
  Σ_m (Λ∗Λ)(m)(Λ∗Λ)(m+h), |h| ≤ X²/T — at λ = 1+ε this constraint |h| ≤ X²/T = T^{1+2ε} exceeds X
  (X²/T > X ⟺ X > T, true), so it is **vacuous**: the "pair" restriction reduces to the full double sum
  with the 1/(y_n − y_m) kernel, whose dominant part is the multiplicative pair window
  **S(δ) = Σ_{n≠m ≤ X} a_n a_m g(y_n) g(y_m) 1_{|log n − log m| ≤ δ}**, δ = O(1) (the task's form, with
  h = g the certificate's window).
- What the certificate needs: the rank–trace inequality reads ‖Â‖²_F = C·M/L² with C = Θ(1) (C = 4/(1+ε)
  if N ≈ (T/2π)log(T/2π); the exact bookkeeping constant is not recoverable from the text extraction —
  O(1) uncertainty, immaterial to the conclusion: it would have to be wrong by a factor ~3500 to matter).
  The value moves by d‖Â‖²_F/N, so the in-class gap 0.0093 =
  0.6818 − 0.6725 (paper Rem 1.1; ceiling §1) means the off-diagonal's contribution must be provably
  **≤ 0.0093·N** in ‖Â‖²_F units, i.e. |O_1| ≤ 0.0093·(1+ε)N·L²/4 =: **budget** in M-units.

**Honesty labels:** the form of O_1 and its bound are PROVEN (paper Prop 5.6, Lemma 5.2; N Lemma 3.3);
the tolerance normalization is derived here from proven constants (paper §7.5(a), ceiling §1) — CHECKED
NUMERICALLY in §3; the "vacuous additive window" observation is PROVEN (algebra).

---

## 2. Numerics: setup

New Rust crate `/tmp/prime-pairs` (sieve to X ≤ 2·10⁶, exact double sums over prime powers; build:
`export PATH=$HOME/.cargo/bin:$PATH RUSTFLAGS="-C linker=rust-lld -C link-self-contained=yes"`
`cargo build --release --target x86_64-unknown-linux-musl`). Measured quantities (M-units):
- **D** diagonal main term; **budget** = 0.0093·(1+ε)·N(T,2T)·L²/4 (tolerance);
- **B_MV** = 4·(3π/2)·πL·Σ a_n²/δ_n, δ_n = min gap in log n — the paper's Lemma 5.2 bound on O_1
  (the "≪ L²X" claim with explicit constants);
- **S_full** = Σ_{n≠m} a_n a_m/|y_n−y_m| (exact phase-free off-diagonal);
- **S_pair(δ)** = Σ_{n≠m} a_n a_m g(y_n)g(y_m) 1_{|Δy|≤δ}, δ ∈ {1/L, 2/L, 1, 2} (task's pair form);
- **S_lam(δ)** = Σ_{n≠m} Λ(n)Λ(m) g g 1_{|Δy|≤δ} (literal task form; A5 object);
- **P(T)** = Re Σ_{i<j} 2 a_i a_j g g sin(TΔy)/Δy — phase-cancelled proxy for the true O_1
  (single-phase heuristic; **not** the certificate's tool — see §4).

Mertens-type checks (paper Lemma 5.1/(5.2)/(5.9)) reproduced: Σa_n² ≈ L²/2, Σa_n²g(y_n) ≈ L³/6,
ΣΛ(n)² ≈ X log X, Σa_n ≈ 2√X — all ratios 0.89–0.99 at these X (finite-size corrections). CHECKED NUMERICALLY.

---

## 3. Numerics: results

Table. T, ε → X = T^{1+ε}; ratios are vs the tolerance **budget** (in-class gap) and vs **D** (main term).
λ = 1 rows are the control (certificate works there).

| T | ε (λ) | X | B_MV/budget | B_MV/D | S_full/budget | S_full/D | S_pair(δ=1)/budget | S_pair(δ=1)/D | S_pair(δ=1/L)/budget | \|P(T)\|/budget | S_lam(δ=1)/budget |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 10⁴ | 0.00 (1.00) | 1.0·10⁴ | 5.27e3 | 33.2 | 63 | 0.40 | 12.2 | 0.077 | 1.56 | 0.88 | 1.4e4 |
| 10⁴ | 0.05 (1.05) | 1.6·10⁴ | 7.67e3 | 48.0 | 92 | 0.57 | 17.0 | 0.107 | 2.10 | 1.43 | 3.1e4 |
| 10⁴ | 0.10 (1.10) | 2.5·10⁴ | 1.13e4 | 70.5 | 133 | 0.83 | 23.8 | 0.148 | 2.82 | 1.28 | 6.8e4 |
| 10⁴ | 0.25 (1.25) | 1.0·10⁵ | 3.71e4 | 228.9 | 419 | 2.59 | 66.7 | 0.411 | 7.04 | 21.2 | 7.6e5 |
| 10⁵ | 0.00 (1.00) | 1.0·10⁵ | 3.58e3 | 22.9 | 40 | 0.26 | 6.4 | 0.041 | 0.68 | 0.26 | 7.3e4 |
| 10⁵ | 0.05 (1.05) | 1.8·10⁵ | 5.89e3 | 37.5 | 66 | 0.42 | 10.0 | 0.064 | 1.00 | 0.29 | 2.0e5 |
| 10⁶ | 0.05 (1.05) | 2.0·10⁶ | 4.90e3 | 31.6 | 51 | 0.33 | 6.5 | 0.042 | 0.54 | (m too large) | 1.5e6 |

Supporting absolute values (T = 10⁴, ε = 0.05): N = 1.235e4, D = 4.50e5, budget = 2.82e3,
B_MV = 2.16e7, S_full = 2.59e5, S_pair(1) = 4.80e4, P = −4.03e3. (T = 10⁶, ε = 0.05: D = 1.57e8,
budget = 1.01e6, B_MV = 4.95e9, S_full = 5.18e7, S_pair(1) = 6.62e6, S_lam(1) = 1.51e12.)

**Reading of the table (all CHECKED NUMERICALLY):**
1. **B_MV/budget ≈ 3.6–37·10³**, essentially flat in T at fixed ε (trend ∝ T^ε/(L_T·L) at these scales),
   and **never below ~3500** — the proven bound on the off-diagonal is thousands of times the tolerance.
2. **B_MV/D = 23–229, growing with ε** (33→48→70→229 at T = 10⁴). Asymptotically B_MV/D ∝ T^ε/(const·log²T)
   → ∞ for any fixed ε > 0; at λ = 1 (ε = 0) it → 0 (rate 1/L or 1/L² depending on the O(1) constants —
   either way → 0, matching the paper's §8 "O_1/D ≤ 6/(L·J_T) requires L ≫ 18"). This is the quantitative
   form of the wall (paper §7.5(a)): for X ≫ T the off-diagonal is provably **not dominated by the
   diagonal**.
3. **S_full/D = 0.26–2.59**: the phase-free off-diagonal sits at the main-term scale; the obstruction is
   real (not an artifact of a loose constant in the bound).
4. **S_pair(δ=1)/D = 0.04–0.41, /budget = 6–67**; even the *measured* pair sum (what HL would evaluate)
   exceeds the tolerance by 6–67×, and grows with ε.
5. **S_lam(δ=1)/budget = 1.4·10⁴ – 1.5·10⁶**: the literal task-form sum is astronomically over budget;
   the A5 trivial bound 2δX² (recorded PROVEN DEAD) is itself ~5× above the measured S_lam — i.e. A5's
   death is quantitative, not marginal.
6. **|P(T)|/budget = 0.26–1.43 for ε ≤ 0.1, 21 at ε = 0.25**: the phase-cancelled proxy *oscillates
   around the tolerance* at small ε (sign flips across T) and grows with ε. It is a measurement, not a
   bound (see §4) — it does not clear the tolerance robustly and cannot be certified.

---

## 4. Bound survey — can any unconditional bound clear the O(1) tolerance?

| Bound | Statement at X = T^{1+ε} (fixed ε > 0) | vs tolerance | Label | Source |
|---|---|---|---|---|
| Montgomery–Vaughan Hilbert inequality | \|O_1\| ≪ L²X = L²T^{1+ε}; norm. contribution ≍ X vs tolerance ≍ 0.0093·(T/2π)logT → ratio ∝ T^ε/poly(log T), **measured 3.6·10³–3.7·10⁴** | **FAILS** | PROVEN | MV74; paper Lemma 5.2 / Prop 5.6; N Lemma 3.3 |
| Trivial bound on literal pair sum (A5) | Σ_{Δy≤δ}ΛΛ ≤ 2δX² (measured S_lam ≈ 0.1–0.2·2δX²; S_lam/budget = 1.4e4–1.5e6) | **FAILS** | PROVEN (recorded DEAD, crossdomain §5) | idea-generator-crossdomain.md §5 |
| Selberg upper-bound sieve on prime pairs | #{p,q ≤ X, \|p−q\| ≤ H} ≪ H·X/log²X, H = X²/T > X (vacuous): ≪ X²/log²X; weighted ≪ X² | ≍ X² ≫ tolerance | PROVEN (standard, IK04 Ch. 7); vacuous here | standard; not in local set |
| Vinogradov–Korobov zero-free-region savings | linear sums (ψ, explicit formula) gain exp(−c log^{3/5}X); no theorem transfers this to the quadratic off-diagonal; even heuristically exp(−c log^{3/5}X) cannot offset T^ε = exp(ε log T) at fixed ε | **FAILS / not applicable** | VK region PROVEN; transfer NOT PROVEN and insufficient | standard; ceiling §3 |
| F(α) nonnegativity (B24 Lemma 3) | F ≥ 0 for all α — inequality, gives only upper constraints on kernels (CGdL20-style SDP, itself RH-conditional 0.6792), not values for support > 1 | **FAILS** (needs values) | PROVEN (B24); CGdL20 SDP RH-conditional | B24 Thm 1/Lemma 3; ceiling §3.2 |
| B24 Thm 1 formula | F(α) = T^{−2α}(log T + O(1)) + α + O(1/√log T) holds **only for 0 ≤ α ≤ 1**; nothing for α > 1 | **FAILS** (range ends at α = 1) | PROVEN-as-stated (range 0≤α≤1 explicit) | B24 Thm 1, §2 ("holds up to α = 1"); GM87 Lemma 8 |
| Hardy–Littlewood / Montgomery pair-correlation value | F(α) = 1 for α > 1; off-diagonal ≍ main-term value (measured S_pair(δ=1)/D = 0.04–0.41) — the one input that WOULD give the certificate a new constant (0.70@1.04, 0.80@1.26, 0.90@1.70, paper Rem 1.1) | **would clear, but CONJECTURED** | CONJECTURED | Montgomery 1973; GM87; paper §1.5, §7.5(a) |
| HL*(k₀, λ) (paper §7.5(f)) | tr Ĝᵏ main terms at λ > 1 via additive correlations; would give 13/18 (k₀=4), proportion 1 in the limit | **would clear, but CONJECTURED** | CONJECTURED (prime-pair statement) | paper §7.5(f) |
| Measured phase cancellation \|P(T)\| ≈ 0.3–1.4×budget at ε ≤ 0.1 | a numerical observation; MV is the sharpest general bound for Σ x_n z̄_m/(λ_n−λ_m) (optimal in general), so any improvement must exploit the prime structure = prime-pair info; the observed smallness is exactly the unprovable HL content, and it fluctuates (sign changes) and grows with ε | **not a bound** | CHECKED NUMERICALLY (this run); not usable | this run; paper §7.5(a) |

**Notes.** (i) MV's Hilbert inequality is *optimal in general* — there exist sequences realizing it — so no
constant-free improvement exists; beating it for our specific coefficients is precisely the Hardy–Littlewood
problem. (ii) The additive-correlation literature (e.g. Σ Λ(n)Λ(n+h) second moments) covers short ranges
h ≫ X^{5/8+ε}; our h-window X²/T = T^{1+2ε} ≫ X lies outside every proven range. (iii) The λ=1 control rows
show why the certificate *does* work at λ=1: B_MV/D ∝ 1/log T → 0 there (the paper's §8 "requires L ≫ 18"
comment is the finite-T face of the same statement).

---

## 5. Bottom line

**Documented negative — the "proven sliver beyond α = 1" question is closed.** For any fixed ε > 0
(X = T^{1+ε}, e.g. the 1.04 support needed for 0.70):

1. The only proven unconditional bound on the certificate's off-diagonal sum — Montgomery–Vaughan via the
   paper's Lemma 5.2 — exceeds the in-class tolerance by **3.6·10³ – 3.7·10⁴×** (measured, T = 10⁴–10⁶)
   and exceeds the diagonal main term by **23–229×**, asymptotically growing like T^ε/poly(log T) → ∞. **PROVEN.**
2. Every other proven bound is equal or worse (sieve 2δX² / X²-scale; VK savings sub-polynomial and not
   transferable to the quadratic sum; F ≥ 0 and the α ≤ 1 formula give no α > 1 values). **PROVEN.**
3. The only inputs that would clear the tolerance are **values** — Hardy–Littlewood / Montgomery
   pair-correlation (F = 1 beyond 1) or HL*(k₀,λ) — both **CONJECTURED** (paper §7.5(f); ceiling §3).
4. The measured phase-free pair sums sit at the main-term scale (S_full/D = 0.26–2.59; S_pair(1)/D =
   0.04–0.41), confirming the obstruction is real; the measured phase-cancelled proxy hovers near the
   tolerance at small ε but is uncertifiable, sign-fluctuating, and growing in ε.

**Consequences (validated, not changed):** the 0.6818 bandwidth-one ceiling (PROVEN in Lean modulo the
numerically-checked EnclOK, ceiling §1) and the roadmap 0.70/0.80/0.90 → supports 1.04/1.26/1.70
(PROVEN-as-stated, paper Rem 1.1) stand; the beyond-1 constants are conjectural-input territory exactly as
the catalog (§3 #13) and the mollifier analysis (§6) recorded. A1/A5 deaths re-confirmed quantitatively.
This closes M29; no escalation. If the program later wants a real constant gain on proven inputs, the
in-class gap 0.6725 → 0.6818 (V2) remains the only proven-inputs path.

---

## 6. Honesty footer

- **PROVEN:** wall statements (paper §7.5(a), Prop 5.6, Lemma 5.2; N Lemma 3.3); B24 Thm 1 range 0≤α≤1;
  B24 F real/even/nonnegative; all bound labels in §4 table; A5 death (crossdomain §5).
- **CHECKED NUMERICALLY (this run, /tmp/prime-pairs, Rust, musl+rust-lld):** all table entries; the
  Mertens-type identities Σa²≈L²/2, Σa²g≈L³/6, ΣΛ²≈X log X; the tolerance normalization; the phase
  proxy values (which are measurements, not theorems — labeled as such).
- **CONJECTURED:** HL / Montgomery pair-correlation beyond 1; HL*(k₀,λ); any use of the measured phase
  cancellation as a bound.
- No claim here is a new theorem; the deliverable is a documented negative with measured magnitudes.
- Sources: research/papers/claude-riemann-paper.txt (§1.5, §5, §7.5(a),(f), Rem 1.1); anthropic-informal-note.txt
  (Lemma 3.3); baluyot-etal-2306.04799.txt (Thm 1, Lemma 3); attack-ceiling.md (§1, §3); attack-mollifier.md
  (§5–6); idea-generator-crossdomain.md (§5 A5); attack-vector-catalog.md (§3 #13).
