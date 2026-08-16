# CORRECTED 2026-08-18 (night refutation): the unconditional transfer claim was WRONG - see wave9-9A-refutation-2026-08-18.md. The [0,1] datum exists unconditionally (BGSTB24 Thm 1) but for a DIFFERENT F: BGSTB24 F uses w(u)=4/(4-u^2) and complex argument (rho-rho'), agreeing with Montgomery's ordinate-only F only under RH. CGdL identity (8) needs the ordinate-only F; its [0,1] asymptotics remain Goldston-Montgomery, RH-conditional. Verdict downgraded: the candidate theorem is NOT established unconditionally. 67.92% simple-anywhere remains RH-conditional (CGdL, as published).

# (ORIGINAL DRAFT, SUPERSEDED)
9A agent analysis + direct source reads: research/papers/cgdl-1810.08843-paircorr-sdp.txt,
research/papers/baluyot-etal-2306.04799.txt (BGSTB24).

## The theorem (candidate)

**Candidate theorem (unconditional).** Let N(T) count nontrivial zeros of ζ with multiplicity and
N*(T) = Σ_{0<γ≤T} m_ρ. Then
    N*(T) ≤ (1.3208 + o(1))·N(T)   as T → ∞,
i.e. at least 67.92% of nontrivial zeros (counted with multiplicity, anywhere in the strip) are simple.

The constant 1.3208 is CGdL's SDP-optimized value of the functional Z over their class A_LP (RH
version). Structural claim: the bound NOT conditional on RH/GRH once BGSTB24 Theorem 1 is used in
place of Goldman–Montgomery's RH-conditional datum. The formal writeup (complete line-by-line
chain below) is the deliverable of this note; a certified re-run of the SDP optimization to confirm
1.3208 to more digits is listed as the single open numerical item.

## Full chain (each line verified from source)

Set-up, CGdL §3: w(u) = 4/(4+u²), Montgomery's
  F(x,T) = (1/N(T)) Σ_{0<γ,γ′≤T} T^{ix(γ−γ′)} w(γ−γ′).
A_LP (CGdL §3.1, lines 287–297): f even, continuous, L¹, f̂(0)=f(0)=1, f̂ ≥ 0, f eventually
non-positive; r(f) = inf{r : f ≤ 0 for |x| ≥ r} (last sign change).

Step 1 (Fourier inversion, CGdL (8), line 317): for suitable g,
  Σ g((γ−γ′)logT/2π)·w(γ−γ′) = N(T)∫ f̂(x)F(x,T)dx.   — UNCONDITIONAL.

Step 2 (kernel substitution, proof of Lemma 8): take g(x) = f̂(x/r(f))/r(f) so that
ĝ(y) = f(r(f)·y). Then the pair sum equals N(T)[ ĝ(0) + ∫_{−1}^{1} ĝ(x)|x|dx + ∫_{|x|>1} ĝ(x)F(x,T)dx + o(1) ]
where the [0,1] part uses the form factor on |x| ≤ 1 and the trailing o(1) uses
T^{−2|x|}logT → δ₀(x) distributionally.   — UNCONDITIONAL (the δ₀ limit does not need RH).

Step 3 (tail drop, sign argument): ĝ(x) = f(r(f)x) ≤ 0 for |x| ≥ 1 by definition of r(f)
(last sign change); F(x,T) ≥ 0 (BGSTB24 Thm 1: "F(α) is real, even, and nonnegative", line 49).
Hence ∫_{|x|>1} ĝ(x)F(x,T)dx ≤ 0, so the pair sum ≤ N(T)[ ĝ(0) + 2∫₀¹ ĝ(x)x dx + o(1) ].
  — UNCONDITIONAL. (NOTE: r(f) > 1 is allowed; the sign argument holds for any r(f). Earlier
  draft of wave9-9A restricted to r(f) ≤ 1 — CORRECTED: unnecessary, verified from the A_LP
  definition and the substitution ĝ(y)=f(r y).)

Step 4 (the [0,1] datum, the ONLY input CGdL need conditioned): CGdL (9) reads
  F(x,T) = (T^{−2|x|}log T + |x|)(1+o(1))  uniformly for |x| ≤ 1,
citing Goldston–Montgomery (RH-conditional in their paper). **BGSTB24 Theorem 1 (lines 49–60)
proves this unconditionally** (up to the harmless T^{−2α}(logT+O(1)) term that contracts to δ₀):
  F(α) = T^{−2α}(log T + O(1)) + α + O(...) up to α = 1 with explicit error terms,
and F real/even/nonnegative. So the ∫₀¹ ĝ(x)x dx term = (2/r(f)²)∫₀^{r(f)} f(u)u du + o(1) is
UNCONDITIONAL.

Step 5 (diagonal lower bound, CGdL (10)): Σ ≥ g(0)Σm_ρ = N*(T)/r(f) — from w > 0 and f̂ ≥ 0
(off-diagonal terms ≥ 0 are not needed; (10) drops them). — UNCONDITIONAL.

Step 6 (conclude): N*(T)/r(f) ≤ N(T)[1 + (2/r(f)²)∫₀^{r(f)} f(u)u du + o(1)] = N(T)·Z(f)/r(f) + o(1)N,
  Z(f) := r(f) + (2/r(f))∫₀^{r(f)} f(u)u du.
Cancelling 1/r(f): **N*(T) ≤ (Z(f) + o(1))·N(T) unconditionally for every f ∈ A_LP.**  ✚

Step 7 (numerics, CGdL §4): SDP over A_LP (f = polynomial × e^{−πx²}, SOS parameterization,
d = 40, interior-point solver, floating point; their §4.1.1 notes conditioning issues honestly)
minimizes Z → 1.3208 (RH functional). Existing known: bandlimited optimum (Montgomery–Taylor)
= 1.3275; relaxed class strictly improves (1.3275 → 1.3208). CONJECTURED (their certificate is
floating-point; independent certified re-run open).

## Consequences & honest boundaries

1. **Simple-anywhere ≥ 67.92% unconditionally** (via N_s ≥ 2N − N*, Montgomery's m² ≥ 2m−1).
   This is a NEW unconditional statement: the best previous unconditional simple-anywhere bound
   in our sources is PRZZ's on-the-line 40.7%-simple (different quantity); the anywhere bound has
   been 4/3-multiplicity folklore under RH (Montgomery) and BGSTB24's own applications only reach
   61.7% simple under the *thin-box hypothesis* (Theorem 2), not unconditionally. **This would be
   the campaign's first genuinely new unconditional theorem about ζ.**
2. **Firewall**: simple-ANYWHERE ≠ simple-ON-LINE. The campaigns' records 0.673481 simple-on-line /
   0.836740 distinct-on-line are untouched: the on-line axis runs through the rank–trace /
   compressed-Weil-form machinery (Theorem D, transfer-stability-online.md), a different
   functional that needs positive-in-strip kernels; signed (eventually non-positive) SDP
   functions give no purchase there. Anywhere-67.92% says nothing about on-line placement.
3. **Not RH evidence** (proportion ≠ RH charter firewall; c.f. barrierzoo-retrotest: even RH-false
   worlds can carry high simple/multiplicity data).
4. Rh-conditional literature (CGdL 0.6792, Bui–Heath-Brown 19/27) remains conditional; this note
   only makes the *SDP-relaxed-class* bound unconditional, up to the certificate exactness.

## Open numerical item (single, bounded)

Re-run the CGdL §4 SDP (Z functional, A_LP) with certified arithmetic to confirm the constant is
< 1.3275 (strictly beats Montgomery–Taylor's bandlimited optimum) and report its tight value.
Self-hosted solvers absent (no cvxpy/scs on toolchain tonight); feasibility: build a small Rust
SOS/SDP via eigenvalue oracle is a known-hard port (good_lp/HiGHS blocked). Item logged, not
funded tonight.

## Ledger line

9A-followup: unconditional N* ≤ (1.3208+o(1))N — PROVEN-STRUCTURAL (chain complete above,
all inputs unconditional via BGSTB24 Thm 1; r(f) restriction corrected/removed); constant
1.3208 CONJECTURED (literature-numeric). New unconditional theorem candidate (simple-anywhere
≥ 67.92%), first of its kind for the campaign. On-line records untouched. No RH evidence.
Closure-DAG: sdp-paircorr-transfer lever upgraded with this chain.