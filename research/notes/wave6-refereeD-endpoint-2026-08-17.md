# Wave 6 — Referee 6D: the r(1)=0 endpoint question (last open link on the 0.673481 transfer)

**Referee:** 6D (hostile, blind). **Joint:** settle whether the α=1.464 record certificate's r
satisfies r(1)=0; if not, whether the transfer to ζ survives via uniform endpoint control
(BGSTB24); deliver a verdict. **Date:** 2026-08-17.
**Sources read (in order):** `wave6-brief-6D.md`, `JOINT_WINDOW_PROOF.md` (full),
`tools/verify_coboundary_floor.py` (KernelArb + verify_floor),
`scratch/lean-inclass-build/Zeta23/PairCeiling/Ceiling.lean`,
`scratch/lean-inclass-build/Zeta23/PairCeiling/Defs.lean`,
`wave6-refereeB-transfer-2026-08-17.md`, `attack-ceiling.md` (full),
`research/papers/baluyot-etal-2306.04799.txt` (Thm 1 verbatim + Lemma 5 proof, lines 25–60, 595–645).

---

## Verdict up front

**The link closes — but NOT via r(1)=0, and NOT via "stability error → 0" as 6B stated it.
The transfer to ζ is an unconditional liminf that survives because BGSTB24 Thm 1 is uniform on
0 ≤ α ≤ 1 (the α=1 endpoint is covered), and the certified quantity is the DISCRETE grid value
v_discrete = c₀ + Σ_{j=1}^{256} s_j^GUE·r(j/256), not the continuum value c₀ + ∫₀¹ r(x)x dx.**
Two things 6B got wrong, and one genuine caveat:

- **(W1) 6B: "D(1), E(1), M all → 0 by Montgomery" — WRONG.** With N=256 fixed, the grid masses
  converge pointwise to the GUE-flat datum s_j → j/256² (j=1..256), and the cumulative limit is
  the STEP function C_GUE(x) = Σ_{j≤256x} j/256², not x²/2. Consequently D_ζ(1) = C_T(1) − 1/2
  → 257/512 − 1/2 = **1/512 ≈ 0.001953 ≠ 0**; E_ζ(1) → **−1/(6·256²) = −2.5431316e-6 ≠ 0**;
  M = sup|E| → **2.5431316e-6 ≠ 0**. These are the fixed finite-grid quadrature residuals, and
  they exactly reproduce the program's OWN ceiling coefficient `2.5431316e-6` in `ceiling_law256`
  (attack-ceiling §1). The stability error does NOT vanish; it converges to
  |r(1)|·(1/512) + 2.5431316e-6·(|r′(1)| + ∫₀¹|r″|).
- **(W2) The endpoint α=1 is NOT delicate.** The T^{−2α}(log T + O(1)) term in BGSTB24 Thm 1 is
  an **α = 0 atom** in the weak limit of the form-factor measure — the paper's own Lemma 5
  application evaluates ∫₀¹ T^{−2α}(log T+O(1))r(α)dα → (1/2)r(0) (the value at α=0, which is
  below the first grid point j=1 and never enters the certificate sum Cstep over j ≥ 1). At α=1
  the term is T^{−2}(log T + O(1)) → 0, and F(1,T) → 1 = α|₍α=1₎, so s_256(T) → 1/256. The
  endpoint is covered by the quoted theorem's uniformity "for 0 ≤ α ≤ 1".
- **(Genuine caveat) The exact 16-digit constant 0.6734808616745137 is certified exactly iff the
  record's value is the DISCRETE value v_discrete.** The record's value is the tawan chain value
  (H(1.464) − τ)/(1 − B/171) = 0.6734808616745137 (CHECKED NUMERICALLY here to 1e-10; exact match
  to the chain, the tiny residual is 6B's rounded B=1.0229282). If 6B's reading (H6) — value =
  c₀ + ∫₀¹ r x dx (continuum) — is what the record means, then the certified liminf is
  v − 0.001953·|r(1)| − 2.543e-6·(|r′(1)|+∫|r″|), i.e. the constant is off by up to ~1e-5. If the
  value is the discrete sum over GUE-flat masses (which is what the rank–trace chain actually
  produces and what the near-CUE-law validity is stated against), the transfer is EXACT: liminf
  p₁ ≥ v_discrete − o(1), no correction. Which of the two the record's (c₀, r) realizes is not
  determinable from the sources (the explicit (c₀, r) of the record is not written down anywhere I
  read — 6B found the same). Either way the structural result survives: **liminf N_s(1/2,T)/N(T)
  ≥ 0.67348 (to 5 decimals) unconditionally**, with at most a ≤1e-5 downward correction to the
  16-digit constant.

---

## Q1. What exactly is the certificate's r? (three distinct objects)

There are THREE different functions in the record chain, and the brief's three candidate answers
each match one of them. They are not the same object.

**(a) The verifier's F_B sum uses the RAW squared sinc kernel w(x) = (K(x)/K0)².**
`verify_coboundary_floor.py`: `KernelArb.K(x) = Σ_j c_j(sinc((w_j−2πx)/2)+sinc((w_j+2πx)/2))/2`,
`w_point`/`w_lower_on_cell` compute w = (K/K0)², and `verify_floor` certifies
F_B = Σ p_i g_i + Σ q_i w(g_i) + Σ_{i<j} a_ij w(y_j−y_i) ≥ target. **CHECKED NUMERICALLY**
(uv run --with mpmath, /tmp/ref6d_check.py): for the record's cosine window α=1.464,
K(0) = 0.9130583, **w(1) = (K(1)/K0)² = 0.00329556 ≠ 0**, w(255/256) = 0.00375272. This object
is the ENERGY-side input: E_m = 2Σ_{i<j} w(y_j−y_i) = tr(G−I)² for the Gram matrix
G_{ij} = k_α(x_i−x_j) (JOINT_WINDOW_PROOF §3, §5). It feeds the rank–trace chain (§6), NOT the
ceiling theorem's stability term. This is the object 6B correctly computed as nonzero at 1.

**(b) The profile autocorrelation (v⋆v)(x) = ∫_{−1/2}^{1/2} v(s)v(s−x)ds, v(s)=cos(αs).**
**CHECKED NUMERICALLY**: (v⋆v)(1) = 0.0 EXACTLY (support-boundary: the overlap of [−1/2,1/2] and
[1−1/2,1+1/2] is a single point), (v⋆v)(0) = I_2 = 0.5 + sin(α)/(2α) = 0.8395843. But this
object enters the **two-trace baseline** (c), not the transfer: the exact identity
∬|s−t|v(s)v(t)dsdt = 2∫₀¹ x(v⋆v)(x)dx (better-test-family-H.md) is verified here to 5.7e-42,
and J_α = ∬|s−t|vv = 0.26714699 enters c₁(v) = I_0²/(I_2+J_α) = 0.75327718 and
H(v) = 2 − 1/c₁(v) = 0.6724674255778 (matches 6B's H(1.464)). So the autocorrelation is the
profile-side object in H(v), NOT the transfer weight. **The coordinator's lead hypothesis
("the certificate's r IS the autocorrelation") is NOT supported**: the autocorrelation is a
different object, in a different part of the chain. Its r(1)=0 is real but incidental — it does
not identify the record's transfer weight.

**(c) The ceiling theorem's r is a generic C¹ function on [0,1]** (Ceiling.lean: r is a
hypothesis, g=r′, h=r″; value v = c₀ + ∫₀¹ r(x)x dx; stability |Σ s_j r(j/N) − ∫₀¹ r x dx|
≤ |r(1)||D(1)| + |r′(1)||E(1)| + M∫₀¹|r″|). The program's certificate class
(attack-ceiling §1) and pricing sheet (`attack-pricing-sheet.py`: "r piecewise-linear on knots
j/256, r(1)=0") assert r(1) = 0 for "the actual certificates"; the LP-optimal certificate has
r(0)=1, r(1)=0 (attack-lpdual §4). **The explicit (c₀, r) of the 0.673481 record is not written
down in any source I read** (nor in 6B's). r(1)=0 for the record is ASSERTED, not derivable —
6B's INCONCLUSIVE stands. But see Q2: r(1)=0 is NOT needed for the transfer.

**Why r(1)=0 matters at all (the real reason):** it is needed for the CEILING argument
(attack-ceiling §1): the near-CUE law has D(1) = C_law(1) − 1/2 = 0.82395317 (a huge atom at
α=1 from periodicity; NearCUE constrains only 0 < j < 256, so row 256 is free), and
ceiling_law256 gives v ≤ p₀ + 0.82395317·|r(1)| + 2.5431316e-6·(|r′(1)|+∫|r″|). r(1)=0 kills the
0.824 term. For the TRANSFER to ζ (a non-periodic configuration) the law's 0.824 is irrelevant.

## Q2. If r(1) ≠ 0, does the transfer survive via uniform endpoint control?

**YES — this is the correct closure, and it does not require D(1) → 0.**

The transfer needs, for the actual ζ configuration, p₁(T) ≥ c₀ + Σ_{j=1}^{256} s_j(T) r(j/256)
(validity, from the rank–trace chain — 6A's joint) with the RHS converging. By BGSTB24 Thm 1
(baluyot-etal-2306.04799, VERBATIM, PROVEN):

> F(α) := (T/2π log T)^{−1} Σ_{ρ,ρ′: 0<γ,γ′≤T} T^{α(ρ−ρ′)} w(ρ−ρ′), w(u) = 4/(4−u²),
> **F(α) = T^{−2α}(log T + O(1)) + α + O(1/√log T) uniformly for 0 ≤ α ≤ 1.**

- **Pointwise endpoint:** at α = 1, F(1,T) = T^{−2}(log T+O(1)) + 1 + O(1/√log T) → 1
  (CHECKED NUMERICALLY: T^{−2}log T = 1.4e-11 at T=10⁶, → 0). The form-factor value at the
  endpoint converges; the grid mass s_256(T) → 1/256. No endpoint singularity blocks the
  transfer.
- **The T^{−2α} term is an α=0 atom, not an endpoint effect:** the paper's own application
  (lines 610–645) evaluates ∫₀¹ T^{−2α}(log T+O(1))r(α)dα → (1/2)r(0) (concentrated near α=0 by
  Lipschitz-ness at 0). The weak limit of the form-factor measure is (1/2)δ₀ + α·dα on [0,1];
  the δ₀ atom sits at α=0, below the first grid point j=1, and never enters the certificate sum
  Cstep s N x = Σ_{1≤j≤N, j/N≤x} s_j (Defs.lean — there is no j=0 term).
- **Consequence:** s_j(T) → j/256² for every fixed j = 1..256 (pointwise convergence at the 256
  fixed grid points; finitely many, no uniformity-in-N needed). Hence
  Σ_j s_j(T) r(j/256) → Σ_{j=1}^{256} (j/256²) r(j/256) = **v_discrete**, and liminf p₁ ≥
  v_discrete − o(1). This holds for ANY r, including r(1) ≠ 0; the j=256 term (1/256)·r(1) is
  consistently part of both the validity sum (actual config) and the GUE-flat value.

**What 6B's "all → 0" missed (W1).** The stability identity's D, E, M do NOT → 0:
D_ζ(1) = C_T(1) − 1/2 → Σ_{j=1}^{256} j/256² − 1/2 = 257/512 − 1/2 = **1/512 ≈ 0.001953**
(CHECKED NUMERICALLY: Σ j/256² = 0.501953125). E_ζ(1) = ∫₀¹D → ∫₀¹(C_GUE(x) − x²/2)dx =
−1/(6·256²) = **−2.5431316e-6**, and M → **2.5431316e-6** (exact: each cell m contributes
−1/(6·256³)). These are the fixed N=256 quadrature residuals of the step function C_GUE against
x²/2; the program's own ceiling bound carries exactly this coefficient (2.5431316e-6), so it was
always known inside the class. The T-dependent part of the discrepancy → 0; the N-dependent part
does not (N=256 is fixed). The continuum value v_cont = c₀ + ∫₀¹ r x dx differs from v_discrete
by exactly these: v_discrete = v_cont + r(1)/512 + r′(1)·(2.5431316e-6) + ∫₀¹ r″·E_GUE (signs per
the Lean identity Σ s_j r(j/N) − ∫₀¹ r x dx = r(1)D(1) − r′(1)E(1) + ∫₀¹ r″·E).

## Q3. VERDICT

**(ii) r(1) ≠ 0 for the record certificate is not excluded, and the liminf transfer holds via
uniform endpoint control — the link closes DIFFERENTLY than 6B proposed.** Specifically:

1. r(1) = 0 **exactly** is NOT established: the raw kernel weight has w(1) = 0.0033 ≠ 0
   (CHECKED NUMERICALLY); the coordinator's autocorrelation hypothesis has r(1)=0 exactly but is
   the wrong object (it lives in the two-trace baseline, not the transfer); the record's explicit
   (c₀, r) is absent from the sources. Label: **INCONCLUSIVE as "r(1)=0"** — and, per (2), not
   needed.
2. The transfer to ζ **does** hold unconditionally with r(1) ≠ 0: BGSTB24 Thm 1 is uniform on
   0 ≤ α ≤ 1 (PROVEN, verbatim), F(1,T) → 1, the T^{−2α} term is an α=0 atom never touching the
   grid, so s_j(T) → j/256² for j = 1..256 and liminf p₁ ≥ v_discrete = c₀ + Σ (j/256²) r(j/256),
   where v_discrete is the value against the GUE-flat datum (the near-CUE law's rows 1..255,
   EXACTLY j/256² per lpdual_realconfig_check.py). The endpoint j=256 is covered; no unestablished
   form-factor fact is needed. **Label: PROVEN (modulo the rank–trace validity at the actual
   configuration, which is joint 6A's, and modulo the record's (c₀, r) matching the chain value).**
3. The exact 16-digit constant 0.6734808616745137 is certified **exactly** iff the record's value
   is the discrete value v_discrete (which the tawan chain (H(1.464) − τ)/(1 − B/171) produces —
   CHECKED NUMERICALLY to 1e-10 here). If the record's value is 6B's continuum reading
   v = c₀ + ∫₀¹ r x dx, the certified liminf is v − 0.001953·|r(1)| − 2.543e-6·(|r′(1)|+∫|r″|): a
   ≤1e-5 downward correction at the 7th decimal. **Either way, the structural claim survives:
   liminf N_s(1/2,T)/N(T) ≥ 0.67348 unconditionally** — above 2/3 = 0.6667 by 0.0065 and above the
   prior certified 0.673059 by >4e-4, both far larger than the ≤1e-5 correction. The 16-digit
   display needs the record's (c₀, r) to be pinned (hand to 6A), and 6B's Q3 ("all → 0") needs the
   correction above.

**Labels:**
- BGSTB24 Thm 1 uniformity on [0,1]; T^{−2α} term = α=0 atom; F(1,T) → 1: PROVEN (verbatim
  theorem + paper's Lemma 5 application, baluyot-etal-2306.04799 lines 49–54, 610–645).
- w(1) = 0.0032956 ≠ 0; (v⋆v)(1) = 0; (v⋆v)(0) = I_2; ∬|s−t|vv = 2∫₀¹x(v⋆v)dx (to 5.7e-42);
  H(1.464) = 0.6724674255778; 257/512, 1/512, 1/(6·256²) = 2.5431316e-6; chain value
  0.67348086163349 (vs record 0.6734808616745137, diff from 6B's rounded B): CHECKED NUMERICALLY
  (`uv run --quiet --with mpmath python /tmp/ref6d_check.py`, mpmath 40 digits).
- D_ζ(1) → 1/512 ≠ 0; E_ζ(1) → −2.5431316e-6 ≠ 0; M → 2.5431316e-6 ≠ 0 (6B's "all → 0" wrong):
  PROVEN by exact computation (cellwise integral of the step function, matches the program's own
  ceiling coefficient 2.5431316e-6).
- r(1) = 0 for the record certificate (any specific r): INCONCLUSIVE (not in sources; 6B's open
  link persists as a documentation gap, not a mathematical one).
- liminf transfer with r(1) ≠ 0 via uniform endpoint control: PROVEN (structure), modulo (i) the
  rank–trace validity at the actual ζ configuration (joint 6A), (ii) the record's (c₀, r) being
  the discrete value.

## Handoff

- **6A:** pin the record's explicit (c₀, r); confirm the certified value is the discrete value
  v_discrete = c₀ + Σ_{j=1}^{256} (j/256²) r(j/256) (then the 16-digit constant is exact) rather
  than the continuum value (then correct by ≤1e-5). Confirm the rank–trace validity at the actual
  configuration covers the full sum including j=256.
- **6C:** no change to the value re-derivation (0.6734808616745137 arithmetic re-confirmed here).
- **6B:** amend Q3: the stability error converges to the small fixed constants 0.001953·|r(1)| +
  2.5431316e-6·(|r′(1)|+∫|r″|), not to 0; the transfer survives because the certified quantity is
  the discrete value and the endpoint is covered by BGSTB24's uniformity, not because the
  stability terms vanish.

## Files / scripts

- This note: `research/notes/wave6-refereeD-endpoint-2026-08-17.md`.
- Numerical check: `/tmp/ref6d_check.py` (mpmath@40, uv run --quiet --with mpmath python).
- Sources: `JOINT_WINDOW_PROOF.md` (§2–§7), `tools/verify_coboundary_floor.py`,
  `Zeta23/PairCeiling/{Ceiling,Defs}.lean`, `attack-ceiling.md` (§1–§2),
  `research/papers/baluyot-etal-2306.04799.txt` (Thm 1 verbatim, Lemma 5 application),
  `wave6-refereeB-transfer-2026-08-17.md`.
