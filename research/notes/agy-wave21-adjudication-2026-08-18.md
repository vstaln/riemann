# agy wave-21 idea batch — adjudication (2026-08-18)

## Source and status

One fresh Antigravity one-shot (`agy -p`, gemini-3.7-flash-high, high effort) targeting the
wave-21 frontier (GS-2026 diagonal bridge, Goldston–Suriajaya/Guth–Maynard, Direction-2 SDP,
Báez-Duarte rate). All candidates labeled CONJECTURED/INCONCLUSIVE by the generator. This note
is the coordinator adjudication against the closure DAG + ledger. No RH proof claimed anywhere.

Candidates received: 4 (1: mollified cross-ordinate collision metric; 2: soundstate SDP with
pinned Ingham covariance; 3: Guth–Maynard log-derivative dispersion; 4: Báez-Duarte invariant
scaling ratio). Raw output: `/tmp/agy-wave21-output.txt`.

## Candidate adjudication

### 1. Mollified cross-ordinate collision metric — **DUPLICATE of the live GS-2026 input as stated**
`D(T,δ) = (1/N(T)) Σ_{γ,γ′≤T, |γ−γ′|≤2πδ/log T} 1`, condition `limsup D(T,1) ≤ 1 + c₀`.
This is a restatement of the diagonal pair count with a rebinned window — the object is the
SAME on-line-sensitive diagonal `Σ m_ρ`, just counted within a normalized window instead of
exactly. The claimed implication `C<2 ⟹ 2−C on the line` is precisely the banked GS-2026
framework (ledger `gs-2026-diagonal-bridge`). No NEW object; no new mechanism. The RH-false
control logic (DH off-line pairs share ordinates ⟹ collision metric ≥ 2) is correct but is
exactly the banked "diagonal = Σ m_ρ fails without RH" statement. Verdict: NOT-A-LEVER as
stated (re-statement). The windowed version is a legitimate *measurement* of the diagonal
(cheap probe could give a numeric basin for C<2 at finite T), but it can never certify C<2
unconditionally. Probe not funded for novelty; the finite-T measurement is what `wave8c`/8C
infrastructure can already do.

### 2. Soundstate SDP with pinned Ingham covariance — **DUPLICATE of Direction 2, CLOSED BY CONVEXITY (batch2) — NOT fundable**
`Σ = [[1, −√3/2],[−√3/2, 1]]`, condition `μ* = inf_{P≥0, P₁₁≥1 on |x|≤1} Tr(Σ P̂(0)) < 1` under
mollifier length θ = 0.55. **CORRECTION: this is NOT "the funded next probe".** agy-batch2
adjudication (`agy-batch2-adjudication-2026-08-18.md`, CLOSURE section, same session) already
answered the SDP-objective question at mechanism level: the 2×2 PSD bandlimited matrix minorant
**collapses by convexity** — zero detection is a codimension-1 scalar event, the objective and
the counting constraint are both linear over the PSD-kernel cone, extreme rays are rank 1
(Φ* = v*(s)v*(s′)ᵀ·uuᵀ), the Euler–Lagrange quotient concentrates on the dominant eigenvector
mode alone (C₂ = 0), and the measured corr = −√3/2 is exactly what the Levinson shift
parameter c ≈ −0.7 diagonalizes. No matrix test function can extract additional variance
(Choquet/extreme-point argument, structure-level PROVEN). The covariance probes were necessary
and stand (rank-2 real, phase-collapse absent, asymptotics −√3/2/1/√3 cross-validated vs
Ingham), but the SDP that would use them collapses to the scalar LP before any RH content.
agy's Epstein class-2 control claim (μ* ≥ 1.25) is consistent but moot under the collapse.
Verdict: **ABANDONED-FUNDING (closed mechanism); NOT-a-funded-probe.** Removed from the funded
list. Record-side alternatives remain long-mollifier (wave9-9B screened trap) or new
non-minorant objects — not this probe.

### 3. Guth–Maynard log-derivative dispersion — **INCONCLUSIVE / structurally deficient as stated**
`E(T,σ₀) = (1/T)∫_T^{2T} |ζ′/ζ(σ₀+it) + Σ_{n≤X} Λ(n)n^{−σ₀−it}|² dt ≤ K(σ₀)(log T)^{2(1−σ₀)/(3−2σ₀)}`.
Problems: (i) the proposed exponent is asserted without derivation (literature-unknown per the
generator itself); (ii) the claim "bound for all σ₀>1/2 ⟹ RH" replays the pole-residue
mechanism — an off-line zero at β forces a residue that the mean-square sees as a pole spike
in t, so the bound IS a zero-location statement in disguise (pole-interrogation ⟺ RH, the
explicit-formula trap already closed for the Gaussian-Perron lane: `direct-rh-gaussian-perron-
2026-08-18.md` — CITED, not re-derived); (iii) the planted-Beurling control cited (residue
⟹ Ω(T^{0.5}) mean-square) is the same residue mechanism, class-2 confirmer only. The honest
novelty test fails: it is a mean-square version of the closed pole-interrogation family.
Verdict: **ABANDONED as stated** (duplicate mechanism at the R2 level: mean-square smoothing
of ζ′/ζ still interrogates poles).

### 4. Báez-Duarte invariant scaling ratio — **CONSISTENCY-ONLY / not a new one-way**
`R_N = d_{2N}√(log 2N) / (d_N√(log N))`, condition |R_N − 1| ≤ 1.25/log N. Claimed direction:
uniform rate convergence → `c_N = o(N^{−1/4})` → RH. The rate-law is the Báez-Duarte sharp-rate
conjecture; R_N → 1 re-states it at dyadic scale. `d_N√(log N) ∈ [0.211,0.215]` is already
CHECKED NUMERICALLY through N=5000 (certified MPFR, `wave8c-burnol-rate-2026-08-18.md`). This
candidate adds no new object: it is the SAME finite-N rate law re-expressed dyadically. The
RH-false control (binomial differences diverge for DH at β>1/2) is consistent with the DH
off-line construction but never certifiable at finite N. Verdict: **CONSISTENCY-ONLY**; do not
fund (8C infrastructure already measures the object; a dyadic renormalization changes nothing
about the finite-N ceiling).

## Net result and next action

- No NEW one-way RH lemma survived. Batches 1–4 were: 1 duplicate-of-banked-framework,
  2 known-live-next-probe (with NEW additive control), 3 closed-mechanism re-play, 4 consistency-only.
- This matches the established pattern: agy batches produce useful alternatives but no
  surviving one-way lemma (cf. agy-ideas / agy-batch2 / agy-fresh2).
- **Funded next item (from candidate 2):** the soundstate 2×2 covariance SDP objective probe —
  this is the ledgered Direction-2 next probe with agy's Epstein class-2 control added. Rust,
  bounded (<1 CPU-min for dozen-var SOS/SDP). Belief it changes: if μ* < 1 at the pinned
  covariance with a genuine PSD matrix polynomial minorant, the Levinson-type barrier is
  reachable; if μ* ≥ 1 or the SDP is infeasible, Direction 2 dies at constraint level.
- Cross-check with wave-21 swarm claims (g0-1 Weil-Gram rank test, g0-2 dual LP) before
  funding anything.

Labels: everything above CONJECTURED/DUPLICATE/ABANDONED as labeled; no numbers computed in
this note beyond cited CHECKED NUMERICALLY ledger entries. No RH claim.