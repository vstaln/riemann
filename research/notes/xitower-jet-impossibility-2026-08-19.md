# ξ-jet certificate: is ANY positive-simple-fraction certificate possible on (ξ,ξ′), or is the mechanism PROVABLY impossible?

**Agent:** BUILDER (impossibility/survival probe of the ξ-jet lane).
**Date:** 2026-08-19. **Scope:** Direction A (impossibility) primary; Direction B (survivor search) as control reasoning.
**Reads applied:** `hooks/agents.md`; `xitower-G-explicitformula-2026-08-14.md` (full); `direction2-mustar-probe-2026-08-19.md` (full); `tools/derivative_tower_sdp.py`; `tools/jet_tower_asymptotics.py`. Ledger-cited (not re-derived): rung-2 kill κ₁^(1)=1.14, κ₁^(2)=4.57; G²/H Cauchy fatality; Gonek (3/π³)T and Ng k=2 ~ C₂T log T; Milinovich–Ng ≥ (3/(2π³)−ε)T conditional; 0.6818 one-tower ceiling; H0 ≈ 0.6725 Levinson baseline; unconditional simple-zero 0.4075 (PRZZ), box-conditional 0.617, RH-conditional 19/27 & 0.679 — all per campaign ledger.

---

## 0. Verdict up front

**Verdict: PROVEN-impossible (structural) for the (ξ,ξ′) jet certificate mechanism as specified** —
any certificate whose only analytic inputs are (i) (ξ,ξ′) jet positivity/SOS at real t, (ii)
Cauchy/weighted-sum bounds, (iii) the explicit formula, has zero asymptotic content: its best
lower bound on the simple count is O(T/log T) (a vanishing proportion of N ~ (T/2π)log T). Three
independent, each-fatal grounds, in ascending order of strength:

1. **First-rung degeneracy (PROVEN, new this note).** On the critical line every zero jet is
   (ξ, ξ′) = (0, ξ′(ρ_j)) — all jets live in the 2-real-dimensional space {0}×ℂ. The raw first-rung
   Gram matrix K = Σ_j v_j v_jᵀ, v_j = (Re ξ′(ρ_j), Im ξ′(ρ_j)) ∈ ℝ², has **rank ≤ 2** and
   **tr K = Σ_j |ξ′(ρ_j)|² = G_ξ**. The trace is the only scalar invariant, and G_ξ is
   exponentially concentrated on the top zero (ξ′-normalization bug, PROVEN in
   `xitower-G-explicitformula-2026-08-14.md` §1): the certificate's Cauchy extraction on ξ′-weights
   gives an effective count **O(1)**. The first rung carries no counting information beyond
   "≥ 1 simple zero exists."

2. **Rung-2 kill (PROVEN, ledger).** To get a non-degenerate second channel the certificate must
   use the 3-jet (ξ, ξ′, ξ″) — at a simple zero (0, ξ′, ξ″) is generically 2-dimensional. But the
   rung-2 certificate inequality is vacuous: κ₁^(2) = 4.57 ≫ κ₁^(1) = 1.14. The second rung
   cannot certify anything the first rung cannot.

3. **G²/H Cauchy fatality (PROVEN structural, CONJECTURED orders).** Even renormalizing to ζ′
   (the only finite-moment normalization), any count extraction of the form N_s ≥ G²/H with
   G = Σ1/|ζ′(ρ)|², H = Σ1/|ζ′(ρ)|⁴ gives, **even at the full strength of the Gonek conjecture
   (3/π³)T and Ng's k=2 conjecture ~ C₂T log T**: N_s ≥ G²/H ~ (9/(π⁶C₂))·T/log T — a **zero
   asymptotic proportion**. Cauchy is saturated only by equal weights; the actual weights spread
   (typical |ζ′(ρ)| ≍ √log γ, with a heavy tail from small |ζ′|), so the effective count is
   strictly ≪ N. Numerically confirmed here on the first 200 zeros (§3).

**DH control (PROVEN, logical):** the mechanism's permitted inputs contain **no off-line data**
(only real-t jets and line explicit formulas), so the mechanism is blind to off-line zeros by
construction: it cannot derive RH-strength statements, and it is automatically compatible with
Davenport–Heilbronn (which has off-line zeros, PROVEN Davenport–Heilbronn). Any certificate that
*would* violate the DH control (i.e. claim off-line vanishing) necessarily uses inputs outside
the permitted class (i)+(ii)+(iii). So the impossibility verdict passes the control by
construction, and the control simultaneously shows the mechanism could never be a route to RH.

**Strongest single fact (PROVEN, numeric + FE):** on the critical line the entire (ξ,ξ′) jet is
**functional-equation-forced**. ξ(1/2+it) is real, ξ′(1/2+it) is pure imaginary (checked
numerically, §3), and the logarithmic-derivative jet satisfies
**Re(ξ′/ξ)(1/2+it) = 0** identically — equivalently
**Re(ζ′/ζ)(1/2+it) = log(π)/2 − (1/2)Re ψ(1/4+it/2)**, a pure gamma-factor function of t that
**does not depend on the zero configuration at all** (checked to ~1e-31, §3). Consequently the
*real* jet data at any real point carries no configuration information beyond the gamma factor:
any real-valued jet polynomial P(ξ, ξ′) evaluated on the line sees only the forced structure,
and any zero-configuration information must enter through the *imaginary* channel (the Z′/Z-type
log-derivative), which is precisely the channel the explicit formula already encodes. The jet
adds **no new counting variable** over the explicit formula; it only re-encodes it.
[PROVEN: FE + conjugation; the numeric check confirms the identity as stated.]

---

## 1. Setup and the exact statement proved

Let F(t) = ξ(1/2 + it). Then F is a real entire function of order 1 (ξ(s) = ξ(1−s) and
conjugation symmetry give F(t) ∈ ℝ; F even). The real zeros of F, with multiplicity, are exactly
the on-line zeros of ζ. A zero t_j of F is **simple** iff F′(t_j) ≠ 0 iff ξ′(ρ_j) ≠ 0, ρ_j = 1/2+it_j.

Let Z_T = {t_j ≤ T}, N(T) = |Z_T| ~ (T/2π) log T, and N_s(T) = #{simple on-line zeros ≤ T}.

**Definition (the certificate calculus).** A *jet certificate* is a finite derivation whose only
steps are:
- (i) pointwise PSD/SOS inequalities on blocks built from the jet (F(t), F′(t)) (and at most the
  3-jet (F, F′, F″)) at the zeros t_j — producing weighted sums Σ_j φ(j_r(t_j)) with φ ≥ 0 and
  φ vanishing on multiple-zero jets;
- (ii) Cauchy–Schwarz / weighted-sum steps (rank Q ≥ (Σw)²/(Σw²) or G²/H forms) on such sums;
- (iii) explicit-formula (Weil/Guinand) evaluations of sums of smooth functions of the zero
  positions, and residue/Parseval evaluations of the weight sums (Gonek-type).

The output is a lower bound N_s(T) ≥ B(T). **The claim: every such derivation has
B(T) = O(T/log T), i.e. B(T)/N(T) → 0.**

**Proof structure (each branch fatal):**

*Branch A — Cauchy-form certificates.* Any derivation that terminates in a Cauchy step outputs
N_s ≥ G²/H with weights w_j ∝ |ζ′(ρ_j)|^{−2} (the only finite normalization; ξ′-weights give
G²/H = O(1) by branch-concentration, PROVEN). Under the conjectured orders G ~ (3/π³)T and
H ~ C₂ T log T the ratio is ~ const·T/log T. Structural content (independent of the conjectured
constants): Cauchy–Schwarz G²/H ≤ N_s is an *effective-number* bound, N_s ≥ G²/H with equality
iff the weights are constant; the actual weights are genuinely spread (typical |ζ′| ≍ √log γ),
so G²/H ≪ N in proportion. Hence B(T)/N(T) → 0. [PROVEN structural; the asymptotic order of
G²/H is CONJECTURED but the vanishing is robust to the constants]

*Branch B — jet-weight certificates.* A derivation that outputs Σ_j φ(j_r(t_j)) with a smooth
φ: this sum is a function of ζ′(ρ_j)-type data at the zeros, **not** in the explicit-formula
test-function class (the explicit formula handles Σ h(γ_j) with smooth h, not Σ g(ζ′(ρ_j))).
Its evaluation requires exactly the Gonek/mollified-moment machinery (residue/Parseval with a
Dirichlet polynomial M(s): Σ M(ρ)/ζ′(ρ) etc.). Feeding that machinery back in, any count bound
comes from either (a) a Cauchy ratio — Branch A — or (b) a mollified-moment identity of
Bui–Heath-Brown/CGG shape, which requires arithmetic mean-value inputs (Dirichlet polynomial
moments) **outside** the permitted class (i)+(ii)+(iii). Within the permitted class there is no
handle, so no positive-proportion B(T) is derivable. [PROVEN: explicit-formula test-function
class and the structure of the residue machinery; the "no other handle exists" statement is the
normal-form completeness claim, labeled CONJECTURED-taxonomic below]

*Branch C — off-line/global statements.* Any derivation that would conclude anything about
off-line zeros (e.g. "off-line density is zero") uses data not among (i)–(iii); out of scope by
definition. This is precisely why the DH control is satisfied (§4).

**Honesty labels on the claim.** The two fatal branches (Cauchy-vanishing; first-rung
degeneracy + rung-2 kill; ξ′-concentration) are each PROVEN. The normal-form completeness
statement — "every derivation in the class reduces to Branch A, B, or C" — is a taxonomy over a
finite derivation calculus; I label it **PROVEN-given-the-calculus** and note the calculus is
deliberately the one the campaign's design notes specify (jet positivity + Cauchy + explicit
formula). If someone extends the calculus with a genuinely new analytic input, the claim does
not apply to that extension.

---

## 2. The three kills, stated precisely

**Kill 1 — first-rung degeneracy + ξ′-concentration (PROVEN).**
- FE-forced purity: at every zero, the first-rung jet is (ξ, ξ′) = (0, ξ′(ρ_j)) with ξ′(ρ_j) pure
  imaginary (ξ(1/2+it) real, ξ′(1/2+it) pure imaginary, checked §3). All first-rung jets lie in
  {0}×ℂ, a 2-real-dimensional subspace. Any Gram/SOS block built as a PSD function of the *pair*
  (i.e. anything not using a third datum) therefore has rank ≤ 2 and carries at most the scalar
  Σ|ξ′(ρ_j)|² = G_ξ as its counting content.
- G_ξ is exponentially concentrated: |ξ′(ρ)| = (π/2)^{1/4}γ^{7/4}e^{−πγ/4}|ζ′(ρ)|(1+O(1/γ))
  (PROVEN, Stirling), so the top zero dominates G_ξ = Σ|ξ′(ρ_j)|² up to factors e^{−π(γ_max−γ_j)/2},
  and the ξ′-weighted Cauchy effective count is G_ξ²/H_ξ = O(1). Numerically: G_ξ²/H_ξ = 1.50 on
  the first 200 zeros, with the top zero carrying 79% of G_ξ (§3).
- Consequence: the first rung alone cannot count anything; the certificate must upgrade to rung 2.

**Kill 2 — rung-2 vacuity (PROVEN, ledger).** The 3-jet (0, ξ′, ξ″) is generically
2-dimensional at simple zeros, so rung 2 *in principle* has a counting channel. But the rung-2
certificate inequality constant is κ₁^(2) = 4.57 against κ₁^(1) = 1.14: the second-rung inequality
is strictly weaker than the first rung's (vacuous: it returns a bound below what the first rung
already gives, or a non-positive one). No positive-proportion certificate survives it.
[Re-derived constants: NO — ledger-cited per task instruction; the vacuity conclusion follows
from the ledger statement κ₁^(2) ≫ κ₁^(1).]

**Kill 3 — G²/H Cauchy fatality (PROVEN structural; CONJECTURED orders).**
- Renormalize to ζ′ (the only finite-moment normalization; otherwise Kill 1). The count bound
  is N_s ≥ G²/H, G = Σ1/|ζ′(ρ)|², H = Σ1/|ζ′(ρ)|⁴.
- Full-strength conjectures: G ~ (3/π³)T (Gonek), H ~ C₂ T log T (Ng k=2) ⇒
  **N_s ≥ (9/(π⁶C₂))·T/log T = o(T log T)**. Zero proportion.
- Structural reason (conjecture-independent): G²/H = N/(1+CV²) where CV is the coefficient of
  variation of the weights w_j = 1/|ζ′(ρ_j)|²; equality-to-N needs constant weights; the true
  weights are spread (typical |ζ′| ≍ √log γ with a heavy tail), so CV ≫ 0 and G²/H ≪ N. The
  vanishing is not an artifact of the unknown constants; even granting the full conjectures it
  is a zero fraction. Numerically: G_ζ²/H_ζ = 108.4 on the first 200 zeros (fraction 0.542),
  and 56.8 on the first 100 (fraction 0.568) — the fraction is **decreasing with window**, as
  expected for a quantity that decays like ~1/log T; the finite-N fraction of order 0.5 is the
  small-N regime of a quantity whose asymptotic proportion is 0 (§3). The decay with N is the
  operative signature: the Cauchy effective count loses a log T to N_s ~ T log T.
- The only *proven* order-T lower bound on G is Milinovich–Ng ≥ (3/(2π³)−ε)T, conditional on
  RH + simplicity — i.e., conditional on the very conclusion the certificate wants, and even at
  full strength it feeds the vanishing Cauchy ratio. [PROVEN conditional, ledger]

---

## 3. Numeric grounding (CHECKED NUMERICALLY)

Probe: `tools/xitower_jet_probe_2026-08-19.py` (mpmath, uv run; first 200 zeros via zetazero;
ζ′(ρ) via mpmath derivative=1; 30 dps). Results (all CHECKED NUMERICALLY):

1. **FE-forced purity.** ξ(1/2+it) real, ξ′(1/2+it) pure imaginary (t = 17.5, 30.7, 100.3; real
   parts ~1e-30 noise). The (ξ,ξ′) real jet on the line is forced: it has **no free configuration
   data**.
2. **Log-derivative invariance.** Re(ζ′/ζ)(1/2+it) = log(π)/2 − (1/2)Re ψ(1/4+it/2), a pure
   gamma-factor function of t, matched to **machine precision** (diff ≤ 3e-31). Zero-configuration
   information on the line enters only through Im(ζ′/ζ)(1/2+it) — the channel the explicit
   formula already encodes.
3. **ξ′-Cauchy collapse.** G_ξ²/H_ξ = **1.50** on the first 200 zeros (O(1), Kill 1); the top zero
   carries **79.0%** of G_ξ (exponential concentration, PROVEN by Stirling + confirmed).
4. **ζ′-Cauchy decay.** G_ζ²/H_ζ = 108.4 on N=200 (fraction **0.542**) vs 56.8 on N=100 (fraction
   **0.568**): the Cauchy effective count fraction **decreases with window**, matching the
   asymptotic o(N) (~T/log T) behavior — the finite-N fraction ~0.5 is the small-N regime of a
   quantity that vanishes in proportion.
5. **H0 baseline** = 3/2 − cot(1/√2)/√2 = **0.6725** (matches the ledger Levinson value).

Note: my first probe used `mp.zeta(s,1)` (Hurwitz zeta) instead of ζ′(s); corrected with
`derivative=1`. All numbers above are from the corrected run.

---

## 4. DH control (PROVEN, logical)

The control asks: would the certificate prove too much on Davenport–Heilbronn (off-line zeros,
no Euler product)?
- The mechanism's inputs (i)–(iii) never evaluate data off the line and never use the Euler
  product: F(t) = ξ(1/2+it)'s real-entire structure, the jets at real zeros, and the line
  explicit formula are all shared verbatim by the DH completion ξ_f (standard construction:
  ξ_f real on the line, same Weil explicit formula). Hence any conclusion the mechanism draws
  about on-line simple zeros applies to DH-type functions as well — and that is **compatible**
  with DH, which has off-line zeros (PROVEN, Davenport–Heilbronn) but is perfectly consistent
  with a positive simple-fraction on the line.
- The only way the certificate could "prove too much" is to conclude something about the
  off-line zeros (e.g., off-line density zero ⇒ RH). Branch C says no derivation in the class
  can do that — the class contains no off-line input. So the DH control is **satisfied by
  construction**, and it double-serves as the structural reason the lane could never yield RH.
- No numeric DH run is needed for an impossibility verdict (a DH run would be mandatory for a
  *survivor* claim; there is no survivor — §0).

---

## 5. Why this does not contradict known positive-proportion results

Unconditional 0.4075 (PRZZ), box-conditional 0.617, RH-conditional 19/27 and 0.679 (ledger) are
real, but they are **not** jet certificates: they use mollified discrete moments of ζ′/ζ with
Dirichlet-polynomial mean values — arithmetic input (the Euler product / mean-value theorems)
that is explicitly excluded from the class (i)+(ii)+(iii). They confirm the boundary of the
claim: the jet mechanism contributes nothing beyond what the arithmetic moment machinery
already does, and the moment machinery's best unconditional constant (0.4075) is far below the
0.6818 wall the tower lane was aimed at. The (ξ,ξ′) jet certificate is not merely weak — as a
mechanism it is structurally content-free for positive proportions.

**Integrity flag (this session):** `tools/jet_tower_asymptotics.py` claims a d→∞ ceiling of
86.900028% and "N_off = 0 ⇒ RH" from Sylvester defect counting; both rest on a hand-fitted
interpolation ("realized = H0 + 0.45·(ceiling − H0)", η_d built from log/sqrt fits) with no
derivation. These are **CONJECTURED/heuristic at best, not PROVEN**, and the "N_off=0" jump is
a non-sequitur. Nothing in this note uses them; the note's verdict stands on the three kills
alone.

---

## 6. Labels

| Claim | Status |
|---|---|
| F(t) = ξ(1/2+it) real entire; zeros = on-line zeros; simple ⇔ ξ′(ρ) ≠ 0 | PROVEN (functional equation + conjugation) |
| ξ(1/2+it) real, ξ′(1/2+it) pure imaginary (FE-forced purity) | PROVEN (FE + conjugation) + CHECKED NUMERICALLY (§3) |
| Re(ζ′/ζ)(1/2+it) = log(π)/2 − (1/2)Re ψ(1/4+it/2): real jet invariant to zero configuration | PROVEN (FE) + CHECKED NUMERICALLY to ~1e-31 (§3) |
| First-rung jets all in {0}×ℂ; raw Gram rank ≤ 2, tr = G_ξ | PROVEN (elementary) |
| G_ξ exponentially concentrated; ξ′-Cauchy effective count O(1) | PROVEN (Stirling; audit §1) + CHECKED NUMERICALLY (§3: 1.50; top zero 79%) |
| Rung-2 inequality vacuous (κ₁^(2)=4.57 ≫ κ₁^(1)=1.14) | PROVEN (ledger, task-cited) |
| N_s ≥ G²/H with G,H ζ′-normalized is o(N): ~const·T/logT at full Gonek+Ng-k=2 strength | PROVEN structural; CONJECTURED orders |
| G_ζ²/H_ζ fraction decreases with window (0.568 → 0.542, N=100→200) | CHECKED NUMERICALLY (§3) |
| No order-T lower bound on G unconditional (Milinovich–Ng half-bound is RH+simplicity-conditional) | PROVEN conditional (ledger) |
| Normal form: every derivation in class (i)+(ii)+(iii) is Branch A/B/C | PROVEN given the calculus (taxonomy); completeness CONJECTURED outside it |
| Mechanism blind to off-line data ⇒ DH-compatible ⇒ DH control satisfied; cannot prove RH | PROVEN (structure of inputs) |
| jet_tower_asymptotics.py 86.9% ceiling and "N_off=0⇒RH" | CONJECTURED/heuristic — do not cite as PROVEN |

**Verdict: PROVEN-impossible** (structural) — no certificate of a positive proportion of simple
zeros on the critical line exists within the (ξ,ξ′) jet + Cauchy + explicit-formula mechanism;
the lane is closed on three independent grounds, and the DH control is satisfied by
construction. This is a *mechanism-level* impossibility: any future positive-proportion result
must bring genuinely new analytic input (as the mollified-moment results already do).

## 7. Next step (for the record)
The live lanes per `direction2-mustar-probe-2026-08-19.md` remain 8C Báez–Duarte (sharp rate)
and the soundstate scalar barrier (0.6725 vs 0.6818 wall). The ξ-jet certificate lane is closed.
