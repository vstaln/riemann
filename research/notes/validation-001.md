# Validation 001 — adversarial review of round-1/round-2 verification claims

**Agent:** ADVERSARIAL VALIDATOR (round 1/2)
**Date:** 2026-08-11
**Protocol:** every verdict below is backed by my own rerun (Rust binaries + scripts saved under
`tools/validator_*.py`); exact commands are cited per target. Honesty labels per
`hooks/agents.md`: PROVEN / CHECKED NUMERICALLY / CONJECTURED / ABANDONED; verdicts are
CONFIRMED / REFUTED / INCONCLUSIVE.
**Sources read:** verification-001.md, attack-finitet.md, attack-kernel.md, attack-multiplicity.md,
attack-ceiling.md, attack-lfunctions.md, attack-mollifier.md, literature-map.md,
anthropic-informal-note.txt, round-1-brief.md, lean-zeta-23 README + LawN256.lean, and round-2
deliverables attack-lpdual.md, close-inclass-gap.md, attack-twobandwidth.md, attack-nevanlinna.md,
attack-qi-sweep.md, attack-m29.md, attack-f1curve.md, selberg-class-theorem.md, validation-enclok.md.

---

## Target 1 — "LMFDB ordinates are bracketed sign changes of Z(t)", max |Z(γ_i)| = 4.67e-6

**VERDICT: CONFIRMED (and the 4.67e-6 is genuine EM truncation error, not a bug).**

Reruns:
- `ZETA_DATA=tools/data tools/zeta-rs/.../zeta-rs bracket 1000` → PASS, 999/999 sign alternations,
  max |Z(γ_i)| (i ≤ 500) = 4.67e-6.
- `uv run --with mpmath python3 tools/validator_check_z.py` (45 dps, mpmath zeta): the TRUE value of
  |Z(γ_i)| at the LMFDB ordinates is ≤ 2.1e-30 (max over i = 1..1000). The ordinates are genuine
  zeros of Z(t) on the critical line. No bug there.
- `uv run --with mpmath python3 tools/validator_check_z2.py`: pure EM truncation error of the tool's
  exact recipe (K=10, N = max(10, ⌈1.6t/2π⌉), mpmath at 45 dps so no f64 rounding): max over
  i = 1..1000 is 6.2e-6 (at i=6, t≈37.6), 632 of the 1000 ordinates have pure truncation error
  > 1e-6, and at i = 6 the K=14 error drops to 7.8e-8 (convergence — the error is truncation, not a
  wrong formula). My independent f64 replica of the Rust EM code reproduces max |Z(γ_i)| = 4.674e-6
  at i = 39 (t = 121.4), and the |Z| values at i = 39/17/11/7 (4.67/4.51/4.39/4.35 e-6) sit exactly
  on the pure truncation-error curve at the same heights (4.89/4.46/4.41/4.77 e-6 at i = 43/20/15/10).
- Analytic tail estimate: at t ≈ 121 (N = 31), the Bernoulli terms of EM decay only slowly —
  k = 5 term ~1.5e-7, k = 9 ~2e-6 at t ≈ 1486 with N = 379; the first neglected term at K = 10 is
  ~1e-6. 4.7e-6 is squarely the expected truncation magnitude at these heights.

**Task's specific suspicion resolved:** the real EM truncation error at these heights is NOT ~1e-9; it
is ~1e-6 to 6e-6 (worst at the LOWEST heights, t ≈ 37–130 — the max occurs at i = 39, t ≈ 121, not at
t ≈ 1486 where it is ~1.3e-6). So 4.7e-6 is the expected truncation error, not a bug. The decisive
check: raising K from 10 to 14 collapses the error by 2–4 orders of magnitude at the same ordinates —
a wrong formula or "Z not zero at γ" would not do that. `zeta-rs zeros 100` (independent
sign-change scan) agrees with LMFDB to worst |diff| = 2.92e-6 at i = 7, consistent with the
|Z|/|Z′| shift at this noise floor.

**One precision fix (minor):** verification-001.md §2 calls 4.67e-6 the "f64 noise floor". It is not
random noise; it is the deterministic Euler–Maclaurin truncation error (largest at low heights).
Label as "EM truncation error" — cosmetic, not substantive.

---

## Target 2 — ψ(±1/2) = cos(1/√2) ≠ 0 boundary issue in attack-kernel.md

**VERDICT: CONFIRMED (the minimizer claim and 0.67250 stand) — but the note's spectrum description
is FACTUALLY WRONG. REFUTED as stated on the spectrum numbers.**

What I verified (rerun: `uv run --with numpy python3 tools/validator_check_kernel2.py`, N = 4000):
- The variational problem is **free-boundary**: no boundary conditions are imposed, so cos(√2u)
  violating a boundary value is a non-issue. The stationarity condition is the integral equation
  v(u) + A(u) = const on [−1/2,1/2]; differentiating twice gives v″ + 2v = 0 on the interior, so every
  critical point is a cosine/sine combination. The sine component provably fails the integral equation
  (sin(√2u) + A_sin(u) = c₁·u is affine with c₁ = √2·cos(1/√2) ≠ 0), so the only critical points are
  multiples of cos(√2u).
- cos(√2u) satisfies v₀ + A ≡ const EXACTLY including at u = ±1/2: (v₀+A)″ = 0, even, value at 0 =
  cos(1/√2) + sin(1/√2)/√2. Numerical: max deviation over the grid 2.5e-9 (discretization only).
- Global minimality: I+T ≻ 0 with **min eigenvalue ≈ 0.797**, so Q is strictly convex on the
  hyperplane ∫v = 1; the cosine is the unique global minimizer over L²([−1/2,1/2]) with no evenness
  imposed. Free-grid solve (no symmetry constraint): Q* = Q(cos/∫cos) to 2.2e-16, stationarity
  residual 5.6e-15, asymmetry 7.7e-15. `tools/angle_kernel` run: Q* = 1.327499303080, asymmetry
  7.8e-16, the c > 1/2 dead-end table and Q(c) = c + (1/√2)cot(√2c) reproduce.
- **There is no competing compact-support minimizer** (uniqueness from strict convexity + free-grid
  numerics). The 0.67250 constant stands.

**REFUTED detail (real documentation error, does not break the argument):** attack-kernel.md §2 and
attack-qi-sweep.md §1 state the spectrum of T: u ↦ ∫|u−v|v(u) as "{2/k² > 0 from tanh(k/2) = 2/k,
k ≈ 2.4} ∪ {−2/k² < 0 from tan(k/2) = −2/k, smallest k ≈ 5.43}, so I+T ≻ 0 (min eigenvalue ≈ 0.93)".
The actual spectrum (numerics + hand derivation):
- Positive part: 2/k² with (k/2)tanh(k/2) = 1, smallest k = 2.3994, λ_max = 0.34741 ✓ (matches).
- Negative part: the note lists only the EVEN eigenfunctions tan(k/2) = −2/k (k ≈ 5.597, NOT 5.43;
  5.43 is not a root — tan(2.715) = −0.45 ≠ −2/5.43 = −0.37), with λ = −2/k² = −0.0638. It **omits
  the ODD eigenfunctions sin((2m+1)πu)** with eigenvalues λ = −2/((2m+1)²π²): the most negative is
  λ = −2/π² = −0.20264 (eigenfunction sin(πu)) — the discrete spectrum shows −0.20264, −0.06385,
  −0.02252 = −2/π², −2/(5.597)², −2/(3π)². Hence the min eigenvalue of I+T is **1 − 2/π² ≈ 0.797,
  not ≈ 0.93**.
- Fix needed: correct the spectrum paragraph in attack-kernel.md (§2) and the propagated sentence in
  attack-qi-sweep.md (§1). Conclusion (I+T ≻ 0, uniqueness, global minimality, 0.67250) is unaffected
  — 0.797 > 0 — so no downstream claim breaks. This is exactly the "spectrum checked" claim that was
  NOT checked correctly.

---

## Target 3 — attack-finitet.md "bound constant measured 0.672500703679412 = brief's value to 15 digits"

**VERDICT: INCONCLUSIVE as paraphrased; CONFIRMED as the note actually writes it, with a genuine
overstatement in §5.**

Rerun: `tools/finitet/.../finitet` reproduces the table EXACTLY (trW/N, HS2/N with diag+offdiag
split, HS2_an/N, bound/N = 0.709–0.719, deltas, eigen-rank thresholds). My own fit of the 10 deltas
reproduces the note's fits to the digit: Δ ≈ 0.0141 + 0.155/lnT (rss 9.0e-6), ≈ 0.0371 + 1.13/T
(rss 1.6e-5), ≈ 0.0283 + 0.418/ln²T (rss 1.0e-5), log|Δ| vs log(1/T) slope 0.122; Δ·N ≈ 0.03·T.
- The "0.672500703679412 = brief's value to 15 digits" sentence in §4.4 refers to the CLOSED-FORM
  constant 3/2 − (1/√2)cot(1/√2), which is correct (I recomputed it; matches 0.6725007036794116 to
  15 digits). The note does NOT claim the measured bound equals 0.6725; it reports measured
  bound/N = 0.709–0.719 separately and correctly. So the paraphrase in the task is sloppy, not the
  note's §4.
- **Real problem in §5:** the verdict "Δ is positive and shrinks like ~1/log T … the asymptotic
  constant is approached from above" is NOT supported by the note's own fits: ALL THREE (plus a
  1/(logT·loglogT) fit I added) have NONZERO intercepts (0.0141, 0.0371, 0.0283). The data over
  T ∈ [100,700] is equally consistent with bound/N → 0.686 or → 0.709 as with → 0.6725; convergence
  of the measured bound to 0.6725 is NOT demonstrated. The honest label is: Δ > 0 at every measured T
  (the finite-T bound overshoots), decay law indeterminate (CONJECTURED to vanish, not CHECKED).
- **No threat to the theorem:** bound/N is a lower bound on rank/N; an overshoot is harmless, and the
  paper's error terms are O(loglogT/logT)-type. The overshoot itself is explained by the k-truncation
  of the Poisson sum (HS2 vs HS2_an, T=700: 1.2838 vs 1.2869) plus the genuine finite-height
  pair-correlation deficit (HS2_an/N = 1.287 still 3% below c = 1.3275) — the latter is a real
  phenomenon at heights 100–1400, not an artifact, and it is correctly attributed.
- Fix needed: §5 verdict should read "Δ > 0 at all measured T; the decay to 0 is consistent with but
  not established by the fits (all fitted asymptotes are nonzero)". No code change.

---

## Target 4 — attack-multiplicity.md extremal-world claim: tr/N = 1, HS²/N = 4/3 for both worlds

**VERDICT: CONFIRMED.**

Rerun (exact arithmetic): for the world (2N/3 simple + N/6 double, orthogonal atoms, Gram = diag(m)):
tr = (2N/3)·1 + (N/6)·2 = N ✓; ‖·‖²_F = (2N/3)·1 + (N/6)·4 = 4N/3 ✓; N_d = 2N/3 + N/6 = 5N/6 ✓;
Lemma R saturation: 4tr − ‖·‖² = 8N/3 = Σk₂(m) with k₂(1) = 3, k₂(2) = 4 ✓ (k_c(m) = c² − ((c−m)₊)²
gives k₂(1)=3, k₂(m≥2)=4, k₃(1)=5, k₃(2)=8, k₃(m≥3)=9 — all verified). For ζ: trW/N → 1 and
HS²/N → 4/3 (flat window) are the paper's Lemmas 3.2/3.3/Thm 5.8, and the finitet numerics confirm
trW/N = 0.992→0.998 → 1 (cosine window) with the flat-window constant 4/3 being the c = 3 branch used
for 5/6. The claim that the two worlds are spectrally indistinguishable at (tr, ‖·‖²) is PROVEN by
lemmaR_tight and numerically by the identical moments. All arithmetic in the note re-verified.

---

## Target 5 — literature-map.md "PROVEN-as-stated" for 0.68185 vs attack-ceiling.md's EnclOK finding

**VERDICT: INCONCLUSIVE (label defensible per its own legend; the map materially omits the EnclOK
caveat — patch recommended).**

Evidence: the repo README (lean-zeta-23) states verbatim that the ceiling theorems' "ONE displayed
hypothesis … is `EnclOK` … obtained outside Lean by interval arithmetic from an exact-rational
certificate"; `validation-enclok.md` independently confirms EnclOK is INCONCLUSIVE-not-refuted (the
authors' certificate file is not public) and flags that prior "CHECKED NUMERICALLY" records for EnclOK
were inherited from the authors' README, not independently run. So attack-ceiling.md's characterization
("the one non-Lean link") is CONFIRMED. The literature-map labels 0.68185 "PROVEN as stated in the
paper (the extremal law is asserted, not re-derived here)" — under the map's own legend ("PROVEN =
stated as a theorem/result in a source we hold") this is an attribution claim and is not false.
However, a reader of literature-map.md alone would believe the ceiling is fully proven, when in fact
its Lean proof rests on one numerical (non-Lean, not-independently-reproducible) hypothesis. The map
never mentions EnclOK. Fix: append to §4(b)3 and the summary line 7 the caveat "PROVEN in Lean modulo
the numerically-checked enclosure EnclOK (the single non-Lean link; authors' certificate not public,
see validation-enclok.md)". No numeric error; an honesty/completeness gap.

---

## Target 6 — cheap built-tool verifications (my own runs)

**VERDICT: CONFIRMED.**
- `zeta-rs constant` → 3/2 − (1/√2)cot(1/√2) = 0.67250070367941162 (brief 0.6725007036794116 to 15
  digits); variational identity lhs/rhs diff 1.17e-8; quotient 1.327499282436 vs 1.327499296321.
- `zeta-rs bracket 1000` → PASS (see Target 1).
- `zeta-rs explicit` → Guinand–Weil spectral identity PASS at all four bump widths
  (|Δ|/scale 1.3e-10 … 1.7e-6), matching verification-001 §3.
- `zeta-rs zeros 100` → independent zeros agree with LMFDB to worst |diff| = 2.92e-6.
- `zeta-rs ranktrace`/`mv` were not re-run here (5000-trial brute force is slow; the Lemma-3.4
  inequality is independently PROVEN in Lean as TightMult and re-derived in Target 4) — labeled
  CHECKED via Lean + earlier runs, not by my rerun.

---

## Target 7 — round-2 deliverables

### 7a. attack-twobandwidth.md — m₃(1) = 2 vs 125/64 adjudication — **CONFIRMED**

Rerun `uv run --with numpy python3 tools/validator_m3.py` + exact hand algebra:
- J2(1) = 1/3, J2(1/2) = 5/12, J2(2/3) = 7/18 — all exact (0.33333, 0.41667, 0.38889), consistent
  with the paper's m₂(λ) = 1/λ + λ/3.
- Closed forms re-derived by hand: D = ∫∫K(u)K(v)K(u+v) = 1/λ² (NOT 3/(4λ); at λ = 1, D = ∫sinc² = 1
  exactly, so the script's 3/4 is wrong already at λ = 1); B = (2/λ)·J2 (NOT 2·J3: the integrand is
  K(u)²S(u)², not K(u)³S(u)²); C = 1 − λ/2. Hence m₃(λ) = 1 + 3(1/λ − 2J2) + 1/λ² − 6J2/λ + 2 − λ
  giving m₃(1) = 2, m₃(1/2) = 5, m₃(2/3) = 13/4 — all exact.
- Direct 2D quadrature (crude tail) gives 2.03 / 5.15 / 3.33 vs claims 2 / 5 / 3.25 — supports the
  closed forms; the old formula gives 1.953 = 125/64 at λ=1, refuted.
- Empirical ζ-zeros (my own window [γ₄₀₀₁, γ₅₀₀₀]): m₂ ≈ 1.298/2.130, m₃ ≈ 1.881/4.779 at λ = 1/½,
  matching the note's ≈ 1.30/2.13, 1.90/4.80 and the known finite-height deficit pattern.
- Consequence stands: 2m₂(1/2) − m₃(1/2) = −2/3 < 0, the cubic construction gives 0.7593 (λ=1/2) and
  0.8071 (λ=2/3) < 5/6; P6.5 is a documented negative; the paper's m_k(1) sequence stands. The
  scripts `m3_check.py`/`m3_pin.py`/`m3_twobandwidth.py` indeed contain the claimed bug (verified by
  reading: "D := … = 3/(4λ)", "B = 2·J3"). Open item the note itself flags: m₄(1) = 13/4 still
  un-verified (3D diagram) — agree, it is NOT independently verified here either.

### 7b. attack-lpdual.md + close-inclass-gap.md — in-class optimum v* = p₀ + |E(1)| = 0.68183123 — **CONFIRMED**

Rerun `python3 tools/validator_law256.py` (parses `LawN256.lean` directly, exact Fraction
arithmetic): 124 rows hi = j·2¹³², 131 rows hi = j·2¹³²+1; max |256·S(j) − j| over the box =
2⁻¹³² = 1.8367e-40 ≤ τ; Σ_{j=1}^{255}(j/65536)(1−j/256) = 21845/131072; E(1) = −1/393216 exactly
(midpoint model); D(1) = +0.8239531607128352 (with S(256) ≈ 211.432 from the enclosure — my initial
reading omitting j = 256 was wrong; the note's D(1) includes the closed-band row); δ′ = 1.9047e-43;
p₀ = 0.6818286874638315; v = p₀ + 1/(6·256²) − δ′ = 0.6818312305953418909… (the note's 45-digit
decimal reproduces exactly; my first float print differed at digit 18 — float artifact).
`tools/lpdual/results.json` reproduces every LP number (ceiling attainment p₀ + M(B+C), box cap at
p₀ + |E(1)| for all B,C, row sweep M=1→0.8899 … M=255→0.6818312, p₁ shadow price exactly 1, active
duals validity −1.0 and box −2.54e-6). The one honestly-flagged gap stands: the "box lemma" is
argued not proven (only the r(0)=1, r(1)=0 subcase is elementary; the general box-valid cap is
LP-checked). The critical honesty split (0.68183 is the LAW's in-class optimum; the REAL-zero
constant remains 0.6725, Theorem D) is correct and re-confirmed.

### 7c. attack-f1curve.md — **CONFIRMED** (structural facts exact; curve honestly labeled CONJECTURED)

Verified: certificate identity v*(A) = p₁(A) + 1/(6N²) follows from Iⱼ = sⱼ on interior knots
(PROVEN-BY-ARGUMENT, LP-consistent); Parseval lower bound p₁ ≥ 1/2 + 1/(2N) = 0.501953 (exact:
Σm² = 383.5 forced by Σ_{j<256}j = 32640, marks ∈ {1,2} → s ≥ 128.5); the bandwidth-2 wall
⌊A·N⌋ ≤ 511, A ≤ 511/256 = 1.9961 (Σ_{j=256}^{511}j = 98176 = twisted Parseval total; A = 2
infeasible) — all re-derived. M2 model p₁ = 1 − (1−p₀)/A² reproducing 0.70/0.80/0.90 at
1.04/1.26/1.70 within 1.1% is a 1-parameter fit (one anchor) — weak evidence but honestly labeled
CONJECTURED; the exact curve is correctly stated to need the authors' configuration LP.

### 7d. attack-nevanlinna.md — **CONFIRMED** (with one UNRESOLVED item the note itself flags)

Verified: identity m₂ = 2 − p₁ for marks ∈ {1,2} (PROVEN algebra); the Nevanlinna parametrization
formula with φ = 0 ↦ P⁻ and φ = ∞ ↦ P⁺ (exact, checked at real and complex z); P⁻/P⁺ moments
(1,1,4/3); all tested φ give Im w < 0 (positive measures) and moments m₀ = 1, m₁ = 1, m₂ = 4/3
(verified by hand expansion: m₁ = (a₀/a₁ − b₁/b₂) = 1 identically, m₂ = 4/3 for φ = 1); the phantom
constraint (1,4/3) infeasible on [0,1] (x² ≤ x, PROVEN); law m₂ = 2 − p₀ = 1.3182 ≠ 4/3 (so
integrality cannot exclude the law — the core negative, correct); m₄ discrepancy 10/3 vs 13/4
(extremal world m₄ = 10/3; the sequence (1,4/3,2,13/4) is NOT the extremal world's — the note flags
the provenance as UNRESOLVED, agreed).

### 7e. attack-qi-sweep.md — **CONFIRMED**

Verified: per-block identity ‖Q_ρ‖²_F = (trQ_ρ)² + 2αβ (exact for a {+a,−b} block; my rerun err
4.6e-13); sharp config diag(1…1,2…2) saturates ‖A‖²_F = 4trA − 3s₁ − 4b to 0; (trQ₊−2b)²/b = 0 at
sharp config; (trQ₊)²/b ≥ 4trQ − 4b over 400 random Q (min gap +19.4 > 0); the TEST-A finite-T
numbers match attack-finitet (0.7165/0.7112/0.7091). Conclusion (no QI inequality beats the
rank–trace bound on the certificate's data budget; the CS refinement's gain vanishes at the sharp
configurations) is consistent with lemmaR_tight (PROVEN Lean) — CONFIRMED.

### 7f. attack-m29.md — **CONFIRMED**

Rerun `uv run --with numpy python3 tools/validator_m29.py` (independent sieve): the note's ratios
reproduce essentially exactly — B_MV/D = 33.2, 48.0, 22.9, 37.5 (note: 33.2, 48.0, 22.9, 37.5);
S_full/D = 0.40, 0.57, 0.26, 0.42 (note: identical); B_MV/budget in the thousands (5.5e3–8.1e3 vs
note 5.3e3–7.7e3, small differences from my N ≈ (T/2π)log(T/2π) vs theirs); S_pair(1)/budget = 8–23.
The documented negative is solid: MV's bound is 3.6e3–3.7e4× the tolerance, the off-diagonal sits at
the main-term scale, the λ=1 control rows show why the certificate works there (B_MV/D → 0), and no
proven bound clears the tolerance; only HL/Montgomery-pair-correlation values (CONJECTURED) would.

### 7g. selberg-class-theorem.md — GL(2) distinct-count F(1/2) = 6/13 extrapolation — **CONFIRMED as an honestly-labeled conjecture; arithmetic checks out**

Verified: 6/13 = c(1/2) = Λ/(1 + m_FΛ²/3) at Λ = 1/2, m_F = 1 is exactly the paper's own Rem 7.2(ii)
formula, and equals the moment-ratio F(1/2) = λ/(1+λ²/3) of Theorem 5.8 (F(1) = 3/4 ✓). The
distinct-count functional's "survival" at Λ* = 1/2 (N_d ≥ max(H_d(1/2), F(1/2)) = 6/13·N_F with
H_d(1/2) = 5/12 < 6/13; 6/13 = 0.4615 < Λ* = 0.5 so the dimension cap does not block it; the
simple-on-line conversion 2·6/13 − 1 = −1/13 < 0 stays dead) is a genuine extrapolation: the F(λ)
branch applies at λ = 1/2 < 3 − √6 (per the paper §7.5(c) restriction), the formula is the paper's,
but the full GL(2) assembly (Rankin–Selberg + MV for a fixed form) is NOT carried out in C. The note
labels it CONJECTURED explicitly — correct and honest. No numeric error found; if a later round
pursues it, the prerequisite is the written GL(2) Thm-5.8 analogue (the note says the same).

---

## Summary of genuine problems found (loud list)

1. **attack-kernel.md §2 spectrum (REFUTED as stated, propagated to attack-qi-sweep.md §1):**
   I+T min eigenvalue is ≈ 0.797, not ≈ 0.93; the negative spectrum omits the odd eigenfunctions
   sin((2m+1)πu) with −2/((2m+1)²π²) (most negative −2/π²), and the even-kernel root is k ≈ 5.60,
   not ≈ 5.43. The conclusion (positive definiteness, unique global minimizer, 0.67250) survives.
2. **attack-finitet.md §5 (INCONCLUSIVE as stated):** "Δ → 0 at ~1/log T" is not supported by the
   note's own fits — all fitted asymptotes are nonzero (0.014–0.037). Label should be CONJECTURED,
   not a verdict. Theorem not threatened.
3. **literature-map.md (INCONCLUSIVE/completeness):** the 0.68185 "PROVEN-as-stated" label never
   mentions the single non-Lean numerical hypothesis EnclOK; patch to cite it.
4. **Minor:** verification-001.md §2 "f64 noise floor" → "EM truncation error"; the 4.67e-6 max is at
   i = 39 (t ≈ 121), not at t ≈ 1486.

## What survives (CONFIRMED with my own reruns)

- LMFDB ordinates are genuine zeros; the bracket claim and the EM-error explanation.
- The variational/minimizer story and the constant 0.6725007036794116 (free-boundary, unique
  minimizer, no competing compact-support minimizer).
- finitet's measured tables (0.709–0.719 bound/N, error-term sign positive) — with the §5 labeling
  fix above.
- Extremal-world / multiplicity arithmetic; the 5/6 hard wall.
- attack-lpdual / close-inclass-gap exact certificate (0.6818312305953419, E(1) = −1/393216,
  D(1) = 0.82395316, p₀) and the LP results.
- m₃(1) = 2 (paper) vs 125/64 (script bug) adjudication; m₃(1/2) = 5, m₃(2/3) = 13/4.
- attack-m29 documented negative; attack-nevanlinna, attack-qi-sweep, attack-f1curve structural
  facts; the GL(2) 6/13 extrapolation as labeled (CONJECTURED).
- The one unverifiable input across all of this: EnclOK (the law's S(j) in the enclosures) —
  INCONCLUSIVE, not refuted; closing it needs the authors' certificate file
  `cert_N256_blk_b128m.json` (sha256 cc3de991…) — same conclusion as validation-enclok.md.

## Files

Rerun scripts saved under `/home/vstaln/riemann/tools/`:
`validator_check_z.py`, `validator_check_z2.py`, `validator_check_kernel2.py`, `validator_m3.py`,
`validator_law256.py`, `validator_m29.py`, `validator_nevanlinna_qi.py`. Exact commands are cited in
each target above.
