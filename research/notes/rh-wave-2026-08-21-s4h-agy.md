# RH Wave 2026-08-21 — s4h multi-agent session (agy one-shots + subagents)

**Verdict: NOT A PROOF.** No PROVEN claim advances RH itself. Honest advance: the Li λ_n stub is now a **genuine, literature-validated computation**, and two discriminators got real numbers. Labels throughout per hooks/agents.md.

## Method (s4h workflow executed)
1. **Idea generation** — 5 parallel `agy --effort high` one-shots (antigravity), each a distinct s4h lens attacking the known bottleneck (local-only Jensen disc, 133 waves, 0 global survivors). Outputs: `/tmp/rh_wave/p{A,B,C,D,E}.out` (5.4–8.1 KB each, all substantive; agy honestly corrected the prompt's wrong λ₁ literature value: λ₁=0.0231 not 0.0923).
2. **Adversarial ranking** — architect subagent (`research/notes/lever-ranking-2026-08-21.md`): **C (Weil bridge) > E (NB rate) > A (covering) > B (Li) > D (chain)**, with hole analysis (A/D hinge on unproven Lipschitz L; C needs derived prime-error budget; E pre-asymptotic; B control fires only at n≈10³).
3. **Implementation** — builder subagent died of context death (405k tok, no output) but left `beurling_defect_floor.rs`; `li_lambda_real` implemented in-session.
4. **Cheap Rust checks** — all <1 min except λ_n n=400 (3.5 min, hit f64 limit).

## Results (all CHECKED NUMERICALLY unless labeled)

### 1. Covering/island chain (levers A+D, s4h-logic-constraint-mapping / systems-leverage-analysis)
44 discs, c_re=0.75, r=0.30, t=14→100 step 2, 100k real zeros:
- RH world: **max E_RH = 0.182109** (at t≈14.13)
- Planted β0=0.85 @14.1347: **max E_false = 0.581116**
- Discriminator fires: any threshold B ∈ (0.182322, 0.581116) separates the worlds (agy's fine grid Δt=0.25 gives 0.206 vs ≥0.628).
**NOT a proof**: (i) Lipschitz L=0.19 is measured, not proven — non-circular proof likely impossible since E has log singularities at zeros (architect); (ii) detection floor β0 ≳ 0.55 (disc misses near-line zeros); (iii) finite window [0,100] only; (iv) at T→∞ requires r(T)=O(1/log T), M(T)~T log T. Honest ceiling: finite-window certificate CONDITIONAL on a proven L — open.

### 2. Real Keiper-Li λ_n (lever B, s4h-investigation-claim-decomposition) — **the session's main advance**
New bin `tools/jensen_probe/src/li_lambda.rs` (li_lambda_real): λ_n = n·Σ binom(n-1,n-m)·a_m from the ξ Hadamard product, a_m = Σ_j Σ_p (−1)^{p+1} binom(p,m−p) c_j^{−p}/p, c_j=¼+γ_j², plus Riemann-von Mangoldt tail T_N(n)=n²(ln(γ_N/2π)+1)/(2πγ_N).
- **VALIDATION (CHECKED NUMERICALLY, N=10k zeros, 0.55s):** λ₁=0.023096, λ₂=0.092346, λ₃=0.207639, λ₁₀=2.279340 — match literature to 6 decimals. The stub gap flagged by 133 waves of synthesis is closed.
- **RH-false control (plant β0=0.85 @14.1347):** perturbation δλ_n oscillates, first sign flip **n=90 (δλ₉₀=−0.284)**, dips grow like |z|ⁿ with |z|=|1−1/(ρ_p−1)|=1.0032>1. Predicted dip-overcomes-λ_n crossing **n≈3300 (CONJECTURED extrapolation)** — f64 catastrophic cancellation breaks the sum at n≥250 (binom·c⁻ᵖ ≈ 1e74·1e−575); needs f128/rug to watch the control fire. Documented, not done.
- **NOT RH evidence**: λ_n>0 for n≤100 is consistent with RH and with "control fires at n≈3300" — positivity in any finite range is zero RH evidence (Li is an all-n criterion).

### 3. Nyman-Beurling defect rate (lever E, dead builder's leftover, completed)
`beurling_defect_floor.rs`: exact Gram matrix for ρ_k={1/(kx)}, N≤200.
- RH slope d(ln d_N²)/d(ln N) = **−0.208** (≈ −1/ln N) vs planted floor power **−0.30** — rates separate at N≤200.
- **NOT a certificate**: pre-asymptotic (architect: "curve-fitting, not a rate certificate"). The residue lemma C(β0,γ₀)=1/[(2β0−1)(β0²+γ0²)|ζ'|²] is **CONJECTURED** — formula not independently re-derived. Binary's self-label "VERDICT: PROVEN" is inflated and rejected here.

### 4. Weil bridge (lever C) — designed, NOT implemented
agy delivered the φ-family (modulated Hermite-1, odd parity ⇒ off-line zero gives −|φ̂(ρ₀)|² deficit) and a sample W_X=0.39059>0 at T=50, X=10⁶ with error bound 0.12371. Architect: only lever that is a genuine equivalence in full form, but one φ family proves nothing and the prime-error budget is not yet derived. **Next session's top priority.**

## Key tension
Every local discriminant (Jensen, Coulomb, diffraction, persistence) fires on plants and stays silent on reality — because reality (so far) IS the RH world. The discriminators are real; the *proofs* they want to be are all conditional on an unproven analytic input (Lipschitz L, prime-error bound, asymptotic rate, all-n positivity). That input is the actual frontier, and it is analysis, not computation.

## Next actions (priority order)
1. **Weil bridge implementation** (lever C): derive the prime-truncation error budget for explicit X, 5-20 member φ family, real≥0 vs planted<0, control fires first.
2. **λ_n to n≈4000 in f128/rug** — watch the plant drive λ_n negative (control firing in-range would validate the Li mechanism end-to-end).
3. **Prove-or-abandon Lipschitz L** for E on the σ=0.75 line (if unprovable non-circularly, close levers A/D as ABANDONED-with-reason).
4. Verify or discard the NB residue lemma formula.
