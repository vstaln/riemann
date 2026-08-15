# WAVE 8 — DIRECT RH ATTACKS (five disjoint levers on classical equivalences)

**Date:** 2026-08-17. **Pivot:** proportion-bound hunting is terminal (0.6818 ceiling
Lean-PROVEN; 0.673481/0.836740 record secured, 5-hostile-referee validated). The mission
now attacks RH DIRECTLY, in parallel, on five classical equivalences. Each lever:
- target + objects + reading list + forecast (deliberately possibly-wrong direction, per
  Anthropic's protocol: the win is when the agent inverts the forecast)
- DEMAND for an RH-false control case (Epstein class-2 / Davenport–Heilbronn / Beurling
  planted zero / fake Weil polynomial) — every quantitative discriminator must be tested on
  the control first: the control must show the OPPOSITE of what RH predicts.
- RUST ONLY (musl+rust-lld release); rug (GMP/MPFR) available via tools/verifier-rs for
  high precision; f64 Euler–Maclaurin Z(t)/ζ(s) machinery in tools/zeta-rs + tools/argprinciple.
- Honesty: labels PROVEN / CHECKED NUMERICALLY (binary+cmd) / CONJECTURED / ABANDONED /
  INCONCLUSIVE. A no-go with a Rust binary is a result.
- Firewall: a proportion-on-line theorem (our 0.673481) is ZERO evidence about RH in either
  direction — do not use it as an input; these levers are the real thing.

---

## LEVER 8A — Li's criterion: RH ⟺ λ_n ≥ 0 for all n

**Target:** compute λ_n for n up to ~10⁴ at high precision (rug), find the SIGN STRUCTURE,
and probe the exact asymptotics. RH ⟺ λ_n > 0 ∀n (Li 1997, Bombieri–Lagarias 1999).

**Objects:** λ_n = Σ_ρ [1 − (1 − 1/ρ)^n] (sum over non-trivial zeros, Hadamard-regularized);
computable via ξ: λ_n = (1/(n−1)!)·(d/ds)^n[s^{n−1} log ξ(s)]|_{s=1}, or via the
power-sum / Newton-identity route from the Taylor coefficients of log ξ at s=1 (c_j =
ξ^(j)(1)/ξ(1) — get these from the functional equation + Euler–Maclaurin ζ values, or from
the Hadamard product form using the first ~10⁵ zeros from tools/data/zeros_*.txt).
Known asymptotics (Lagarias): if RH, λ_n = (n/2)(log n − log 2π + γ − 1) + O(√n·something)
or similar; the *fluctuation* around the main term is the interesting object (it encodes
the zero structure). Off-line zeros make λ_n oscillate with a larger envelope.

**Forecast (possibly wrong):** "λ_n will be positive and smooth; the fluctuation term is
noise with no structure." INVERT: the fluctuation IS the signal — decompose
λ_n − main_term and look for the fingerprint of the low-lying zeros (a periodic component
from the lowest zero pair ~14.13, 21.02). If RH is true the residual should be bounded by
the known unconditional partial-Sum control; the test is whether the residual's envelope
matches the prediction from the actual low zeros.

**RH-false control:** take the SAME ξ-product construction but move one low zero OFF the
line (e.g., replace the pair ρ, 1−ρ at γ≈14.13 with ρ=0.6+14.13i, ρ'=0.4−14.13i — a fake
ξ' with a planted zero). Compute its λ'_n. **The discriminator: RH (real ξ) must give
λ_n > 0 with residual ≤ predicted; the fake must show λ'_n < 0 for some n or residual
envelope way beyond prediction.** Verify the control shows the anomaly before trusting the
real case.

**Deliverable:** research/notes/wave8a-li-criterion-2026-08-17.md + Rust probe in
tools/wave8a/ (rug or f64+corrected terms). Numbers: λ_n table for n = 1..1000 (sample),
residual envelope, control comparison.

---

## LEVER 8B — Speiser's criterion: RH ⟺ ζ′(s) ≠ 0 in 0 < Re(s) < 1/2

**Target:** numerically hunt ζ′ (derivative of ζ) zeros in the left half of the critical
strip 0 < σ < 1/2, up to height T ≈ 5000, via argument principle / Newton on the
Euler–Maclaurin ζ′(σ+it) evaluation. RH ⟺ NO ζ′ zeros in that half-strip (Speiser 1934;
classical, unconditional equivalence).

**Objects:** ζ′(s) from the Euler–Maclaurin formula differentiated termwise (Rust complex
f64; error term must be bounded — use the same certified approach as tools/argprinciple);
scan grid over 0<σ<1/2, t∈[10,5000]; bracket candidate zeros by argument variation on
rectangles; refine with Newton; certify emptiness per box (arg winding = 0 with margin).

**Forecast (possibly wrong):** "the scan will find no ζ′ zeros in the left half-strip
(RH-compatible), and that's the end of the lever." INVERT: the interesting object is the
BOUNDARY behavior — ζ′ has known zeros ON the line σ=1/2 (if all simple zeros of ζ, by
the Fekete-type argument ζ′ interlaces) and in 1/2<σ<1 (there are known ζ′ zeros to the
right — e.g. near σ≈0.7+? by Hadamard/Rolle arguments); the lever's real content is (a)
confirming the classical picture numerically to T=5000 and (b) extracting the RATE at which
ζ′ zeros accumulate on the line vs the half-strip — and (c) the geometric reformulation:
the image of the critical line under ζ′ winds around the origin exactly when... (find the
equivalent statement).

**RH-false control:** Davenport–Heilbronn-type L-function (class-2, from barrier_zoo or
built fresh) with a planted/known off-line zero — **its ζ′_L MUST show zeros in the left
half-strip** (Speiser's equivalence holds per-L); verify the discriminator: control shows
off-line ζ′ zeros, real ζ must show none.

**Deliverable:** research/notes/wave8b-speiser-2026-08-17.md + Rust probe in tools/wave8b/.
Numbers: complete census of ζ′ zeros in 0<σ<1/2, T≤5000 (expected: EMPTY) + control census
(expected: NON-EMPTY) + certified error bounds.

---

## LEVER 8C — Nyman–Beurling / Báez-Duarte: RH ⟺ d_N → 0

**Target:** compute the Báez-Duarte distance d_N = dist(1, span{ρ_k : 1≤k≤N}) in L²(0,1)
where ρ_k(x) = {1/(kx)} (fractional part), for N up to ~10⁴, with rug/high precision, and
measure the decay rate. RH ⟺ lim_N d_N = 0 (Nyman 1950, Beurling 1955, Báez-Duarte 2003 —
unconditional equivalences).

**Objects:** the Gram matrix G_jk = ⟨ρ_j, ρ_k⟩ and the vector b_j = ⟨1, ρ_j⟩ have CLOSED
FORMS (the fractional-part inner products are computable exactly via the standard
{1/x} expansions — derive and verify numerically). d_N² = 1 − bᵀG⁻¹b. The decay rate is
known to be tied to RH: unconditional lower bound d_N ≥ c/√N (Burnol 2001); RH ⟺ d_N → 0,
and the rate d_N ≪ N^{−1/2}·(log N)^{1/2}·... is equivalent to RH (Báez-Duarte's
criterion is quantitative: RH ⟺ d_N = o(1); the finer rate is related to the Lindelöf-ish
input). Numerical d_N at N up to 10⁴ (rug for the linear algebra, or f64 with pivoting —
the Gram matrix is notoriously ill-conditioned, so rug/MPFR is justified: state one-line
reason).

**Forecast (possibly wrong):** "d_N will decay like 1/√N with the Burnol constant, flatly,
no structure." INVERT: the OBJECT is the sequence of OPTIMAL coefficients c_k(N) — they
have arithmetic structure (Báez-Duarte and successors: the coefficients relate to the zeros
via the explicit formula; the last coefficient c_N(N) ≍ something; the *discrepancy* of the
partial-remainder is the RH signal). Probe: does d_N·√N → c (what c? Burnol computed
c = 1/√(π·Σ...)? find it) or oscillate? Does the sign pattern of c_k(N) match the zeros'
argument?

**RH-false control:** same L²(0,1) construction but with a planted-zero fake ξ (as in 8A):
its d'_N must SATURATE at a positive limit (not →0) — the discriminator. (Note: the
Nyman–Beurling theorem is specific to ζ; for the control, construct the fractional-part
space for the fake's kernel and show d'_N ↛ 0.)

**Deliverable:** research/notes/wave8c-nyman-beurling-2026-08-17.md + Rust probe in
tools/wave8c/. Numbers: d_N table, decay fit, optimal-coefficient structure, control
saturation.

---

## LEVER 8D — Turán/Laguerre inequalities on Ξ's Taylor coefficients (LP-class necessary conditions)

**Target:** compute the Taylor coefficients of Ξ(t) = ξ(1/2 + it) (even, real) from the
Φ-integral: Ξ(t) = 2∫₀^∞ Φ(u)cos(tu)du with Φ the theta-moment function
Φ(u) = Σ_{n≥1} (2πn²e^{9u/2} − 3πn²e^{5u/2})e^{−πn²e^{2u}} (positive, classical), so
b_k = (−1)^k Ξ^(2k)(0)/(2k)! = 2∫Φ(u)u^{2k}du/(2k)! (moments of a positive measure!).
Test the NECESSARY conditions for all-real zeros (Laguerre–Pólya class): the Turán
inequalities b_k² − b_{k−1}b_{k+1} ≥ 0, and the full Laguerre inequality
(Ξ^(k)(t))² − Ξ^(k−1)(t)Ξ^(k+1)(t) ≥ 0 for all t ≥ 0.

**Objects:** moments M_k = 2∫₀^∞ Φ(u)u^{2k}du (rug/MPFR, truncate the u-integral with
rigorous tail bound — Φ decays doubly-exponentially, so the tail is tiny); b_k = M_k/(2k)!;
Turán T_k = b_k² − b_{k−1}b_{k+1}; Laguerre L_k(t) sampled on a grid. For a positive measure,
M_k is log-convex by Cauchy–Schwarz (M_k² ≤ M_{k−1}M_{k+1} is FALSE direction — check
which way CS goes: (∫f g)² ≤ (∫f²)(∫g²) gives M_k² ≤ M_{k−1}M_{k+2}·... the SIGN and the
extra factor (2k)! normalization decides whether T_k ≥ 0 is trivial or not — work it out
exactly).

**Forecast (possibly wrong):** "the Turán inequalities are automatic from moment
log-convexity and prove nothing." INVERT: the MARGINS carry the signal — compute the
normalized margin t_k = T_k/(b_k²) and find its minimum order and its asymptotics; the
function k ↦ t_k is an RH-sensitive quantity (Csordas–Norfolk–Varga, Csordas–Smith:
the Turán inequalities for Ξ ARE RH-related; finding where the margin shrinks fastest
localizes the "pressure"). Also test whether the FULL Laguerre inequality L_k(t) ≥ 0
holds numerically on t ∈ [0, 40] for k up to ~20 — if it ever dips negative, that's a
DISPROOF of RH (a negative Laguerre value at some (k,t) ⟹ non-real zeros, unconditionally);
if it stays positive, the shape of L_k(t) near its minima is the probe.

**RH-false control:** the planted-zero fake Ξ′ (from 8A's ξ′): its Turán/Laguerre values
MUST fail (negative T_k or L_k(t)<0) — the discriminator. (For a genuinely off-line zero
pair, the LP necessary conditions must be violated at some order — find that order.)

**Deliverable:** research/notes/wave8d-turan-laguerre-2026-08-17.md + Rust probe in
tools/wave8d/ (rug/MPFR justified for moments). Numbers: b_k, T_k, t_k, L_k(t) grid,
min-margin order, control failure order.

---

## LEVER 8E — Beurling / integral-positivity route: the "Nyman–Beurling + Beurling's theorem on the half-plane" chain

**Target:** the FUNCTIONAL-ANALYTIC route to RH: Beurling's theorem — RH ⟺ the functions
{θ_a(x) = {1/x}^a ... } or equivalently the "no zeros off-line ⟺ density of a fractional
span" — PLUS the modern reformulation via the operator F on L²(0,∞) (the "Fourier–Mellin"
route: RH ⟺ the span of {Λ_n} where Λ_n(x) = Σ... is dense, equivalently the linear
operator I − T is injective on the right space). Pin the EXACT modern statement
(Báez-Duarte 2003's quantitative version; Burnol's Hilbert-space reformulation with the
explicit formula), then test the FINITE-DIMENSIONAL shadows: the "Nyman condition" matrices
of ⟨Λ_j, Λ_k⟩ for the Beurling functions, the determinant growth / smallest eigenvalue
decay of the Gram matrices (RH ⟺ the smallest eigenvalue of the truncated system → 0 at a
specific rate tied to 1/2).

**Objects:** Λ_k(x) = {1/(kx)} (same as 8C) — 8E is the STRUCTURAL twin: instead of d_N
computation, study the OPERATOR side: the eigenvalues of the Gram system G_N (or the
Mellin-conjugate operator M = I − 2·(Poisson-sum) on L²(0,∞)), whose spectrum's
infimum over the right half is related to the zeros' real parts. Compute the smallest
eigenvalue λ_min(N) of G_N for N up to ~2000 and fit its decay; RH ⟺ λ_min(N) → 0 with
the precise rate (this is a known equivalent — find and cite it). Also compute the
"Beurling operator" B on ℓ²: (Bc)_k = Σ_j c_j·⟨Λ_k,Λ_j⟩-normalized — the norm ‖B_N‖ →
the RH signal.

**Forecast (possibly wrong):** "the eigenvalue decay is 1/N-ish and has no distinguishing
content vs 1/√N." INVERT: the eigenVECTORS of G_N (the optimal coefficient patterns) are
the signal — their low-frequency content must converge to the explicit-formula kernel
(Burnol's exact computation); the discrepancy between the empirical eigenvector and the
theoretical one is the RH probe, and the rate of convergence of λ_min(N)·√N·(log N)^{1/2}
to its limit constant is the discriminating number.

**RH-false control:** planted-zero fake (8A/8D): λ_min′(N) must saturate > 0 (not →0),
and the eigenvector content must be visibly different — verify.

**Deliverable:** research/notes/wave8e-beurling-operator-2026-08-17.md + Rust probe in
tools/wave8e/. Numbers: λ_min(N) fit, eigenvector content, control saturation, the exact
equivalent statement with citation.

---

## COMMON RULES

- RUST ONLY. rug (MPFR) justified for: high-precision moments/inner products / ill-
  conditioned Gram systems — state one-line reason per use. f64 with certified error
  bounds acceptable where the tool exists (argprinciple style).
- Deliverable-first: write research/notes/wave8?-...-2026-08-17.md after ≤3 file reads or
  first 5 tool calls (partial is a deliverable), then refine with ≤3 more reads.
- Budget: ≤12 turns, ≤15 tool calls, stop at ~85% context; scripts ≤80 lines where possible.
- Every claim labeled; every number from a run binary (cite command); the control case must
  be verified FIRST (show the anomaly) before trusting the real-case numbers.
- Never weaken anything; a wrong confident result is worse than no result.
