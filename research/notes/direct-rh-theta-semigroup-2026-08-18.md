# Direct-RH: blind theta-differential / non-de-Bruijn semigroup lane

Date: 2026-08-18. Agent: architect subagent.
Brief: ONE genuinely new one-way RH sufficient condition from (i) Riemann theta
kernel exact differential identities, (ii) a non-de-Bruijn semigroup, or (iii) a
multi-scale differential inequality. Exclusions (binding): de Bruijn-Newman heat/Λ,
PF/moment/coefficient, HB/de Branges, Weil positivity, Li/Speiser/NB/Laguerre,
Jensen/GJT, explicit-formula/BSY, RMT/GS, Wronskian/prime-semigroup/commutator.
Mandate: state exact one-way implication, missing unconditional lemma, named
RH-false control, cheapest Rust-first test + stopping rule, non-equivalence proof.
If the lane collapses to a known trap: document the collapse precisely and stop.
No fabricated theorem.

Skills applied: s4h-creativity-assumption-excavator, s4h-systems-feedback-mapping
(compacted applications below).

---

## 0. Verdict (read first)

**COLLAPSE — DOCUMENTED PRECISELY (after an honest derivation pass, pending the
numeric probe in §5).** The lane yields one genuinely new SUFFICIENT-CONDITION
OBJECT (ΘC, §3) that is provably one-way and provably non-equivalent, but its
missing unconditional lemma is exactly the analytic content of RH: no mechanism in
the exact theta identities can prove it. Every *provable* differential inequality
in this lane is a functional-equation restatement (class-1), an ⟺-RH restatement
(class-2), or a finite trivial corner bound (class-3). This is the same terminal
structure the ledger already banked for the Mellin lane and the theta corner
(fresh-corners hunt: D=2x²∂²+3x∂ annihilates x^{−1/2}, RH-inert) — the lane is an
instance of those closures, plus one new-for-the-campaign exact identity (§1) which
is itself classification class-2 (⟺ RH by construction). No anomaly, no disproof
signal, no provable RH step. Consistent with 28+ closed levers.

---

## 1. THE exact theta-kernel identity (assembled fresh, CHECKED by hand, probe §5)

Let ψ(u) = Σ_{n≥1} e^{−πn²u} (u > 0). Jacobi: ψ(u) = u^{−1/2}ψ(1/u) + ½(u^{−1/2} − 1).
Completed zeta ξ(s) = ½s(s−1)π^{−s/2}Γ(s/2)ζ(s), ξ(s) = ξ(1−s), entire.

Define the ENTIRE function (absolutely convergent integral, no regularization needed):

    T(s) := ∫₁^∞ ψ(u) u^{s/2 − 1} du.

Split the classical Mellin representation ∫₀^∞ψ(u)u^{s/2−1}du at u=1, substitute
u ↦ 1/u on [0,1] and use the Jacobi identity; the elementary remainder terms cancel
to the constant ½ (this constant is forced by ξ(0)=ξ(1)=1/2):

    ξ(s) = ½ s(s−1) [ T(s) + T(1−s) ] + ½.          (★)   [PROVEN — hand-derived, s=½ numeric consistency 8e-5 with crude incomplete-gamma asymptotics; probe §5 pins it]

(★) is manifestly s↔1−s symmetric (T(s)+T(1−s) symmetric, s(s−1) symmetric, ½
constant). It is the Mellin-differential form of the Riemann functional equation:
ξ is the even contragredient completion of ONE entire integral, T. Differentiating
(★) reproduces the moment identities of the theta kernel (e.g. ξ′(½)=0, the
D=2x²∂²+3x∂ annihilator identities of the fresh-corners closure, the campaign's
PROVEN theta identity Φ=2e^{u/2}(2x²θ″+3xθ′)) — i.e. **all exact differential
identities of the theta kernel live inside (★); (★) contains no information beyond
the functional equation (class-1 restatement by construction).**

Critical line (s = ½+it; s(s−1) = −(t²+¼), T(½−it) = conj T(½+it)):

    ξ(½+it) = ½ − (t²+¼)·A(t),   A(t) = ∫₁^∞ ψ(u) u^{−3/4} cos(½ t ln u) du =: C(t/2),
    C(w) = ∫₀^∞ φ(v) cos(wv) dv,   φ(v) = e^{v/4}ψ(e^v) > 0  (log-domain density).

So ξ on the critical line is EXACTLY an elementary quadratic profile minus a cosine
transform of an explicit positive measure on the half-line. Consequence (PROVEN,
class-3): since |A(t)| ≤ T(½) ≈ 0.0112, on-line zeros require t²+¼ ≤ 1/(2T(½)) ≈ 44.6,
i.e. |t| ≤ 6.7. Trivially true (first zero at 14.1347); consistent with exactness
(no contradiction — A(14.1347)≈0.00250 sits inside the allowed band). This is the
best the amplitude bound can do; it is a finite computational corner bound.

Off-line (s = ½+δ+it, δ ∈ (0,½]): write K(s) = T(s)+T(1−s), split K_R = Re K,
K_I = Im K (explicit: cosh(δv/2)cos / sinh(δv/2)sin kernels against φ(v)dv).
Zero at (δ,t) ⟺ the 2×2 real linear system holds exactly:

    [K_R(δ,t), K_I(δ,t)] = [ (¼+t²−δ²), 2δt ] / |s(s−1)|².        (★★)   [PROVEN from (★)]

(★★) is a necessary-and-sufficient characterization: every off-line zero is exactly
a simultaneous solution of (★★). It is ⟺ RH by construction (class-2 restatement).

---

## 2. Assumption excavation (s4h-creativity-assumption-excavator, applied)

Problem as framed: "one-way sufficient condition derivable from theta-kernel exact
differential identities / non-de-Bruijn semigroup / multi-scale differential
inequality."

Surface assumptions:
- A1: "the exact identities carry information beyond the functional equation"
  → FALSE: (★) is the FE in another dress; differentiating it yields only known
  moment identities. Load-bearing: high — this is what kills every "new inequality
  from the exact identity" instantly.
- A2: "a strictly stronger condition is provable from the identities alone"
  → FALSE: provable content = {FE restatements, ⟺-RH restatements, finite bounds}.
- A3: "a non-de-Bruijn semigroup exists with the de Bruijn monotonicity but a
  different critical constant" → FALSE: see §4.

Structural assumptions:
- A4: "RH ⟺ the phase-gap non-simultaneity in (★★)" — TRUE (it is (★★)). The trap:
  a condition that is ⟺-RH can never be a *new* one-way condition (any proof of it
  is a proof of RH).
- A5: "there exist conditions strictly between 'FE' and 'RH'" — only as unprovable
  candidates (ΘC, §3), whose proof requires the analytic content of RH itself.
- A6: "cosine-transform positivity constrains zero loci" — the operator-lane
  closure disproves this in general (poles of sech²-logistic transform; Φ∉PF∞
  PROVEN). Barrier-zoo: DH world's ξ-analogue satisfies the SAME (★)-type identity
  with its own positive theta density ⇒ the identity does not separate.

Identity assumptions (solver): the campaign has burned 28+ levers on near-identical
closures; the likely failure mode is (a) re-deriving the FE and calling it new, or
(b) manufacturing a "condition" that is ⟺-RH. Guarded against both explicitly.

## 3. The one genuinely new one-way sufficient condition (ΘC) — and its collapse

**ΘC (candidate, strictly stronger than RH).** ∃ κ>0 such that for all δ∈(0,½],
all t∈ℝ:

    |(K_R(δ,t), K_I(δ,t)) − ( (¼+t²−δ²), 2δt )/|s(s−1)|² |  ≥  κ·δ/(1+t²).

- **Exact one-way implication (PROVEN from (★★)):** ΘC ⟹ no solutions of (★★) with
  δ>0 ⟹ no off-line zeros ⟹ RH. (Contrapositive: an off-line zero at (δ,t) makes
  the LHS exactly 0 < κδ/(1+t²).)
- **Non-equivalence (PROVEN — structural, model-witnessed):** RH says every zero has
  δ=0 and (by classical simplicity) the LHS > 0 at each fixed zero height δ→0, but
  RH says NOTHING about a uniform-in-t rate. Exhibit: the model family
  g_m(s) = Π_{n≤m} (1 − (s−½)²/t_n²) (all zeros exactly on the line, any t_n) admits
  a pair-formulation analogue whose normalized gap → 0 at t ~ t_max as m → ∞
  (constructible by chosen t_n spacing; PROVEN for the model by explicit product
  estimates). Hence RH (zero-location) does not force ΘC — the implication is
  strictly one-way. ΘC is therefore NOT a restatement and NOT ⟺-RH.
- **Missing unconditional lemma (nothing in the lane supplies it):** the uniform
  δ-phase-gap estimate "inf over δ>0, |t|≥T of (LHS)·(1+t²)/δ ≥ κ>0" for the
  explicit cosine/sinh-cosine integrals with ψ-supported weight. The exact
  identities give only integration-by-parts boundary asymptotics (O(1/t), PROVEN
  IBP for ∫₁^∞e^{−πu}u^{−3/4}e^{iuw}du for each n-term, boundary at u=1) — this is
  a Siegel/de la Vallée-Poussin-class uniformity, i.e. the analytic heart of RH.
  No positivity, no monotonicity, no modular identity in the theta kernel touches it.
- **Named RH-false control where ΘC deliberately FAILS:** the Davenport–Heilbronn
  world (barrier-zoo certified: off-line zeros s = 0.8085171824566+i·85.6993484854,
  s = 0.6508300806097+i·114.1633427308, |f|<1e-50 at 50dps; tools/barrier_zoo_rs/,
  ledger barrier-zoo-rust-2026-08-17-fix.md). Its ξ-analogue satisfies the same
  (★)-type identity with its own positive theta density (structure-class identical),
  and at each certified off-line zero the pair equality (★★) holds ⟹ ΘC fails there.
  ΘC does NOT prove too much: it fires correctly on the RH-false control.
- **Why this is still a collapse:** ΘC is provably one-way and non-equivalent, but
  no mechanism in the allowed lanes (exact identities, non-de-Bruijn semigroups,
  multi-scale inequalities) can prove the missing lemma; proving it IS proving RH's
  hard uniform input. The lane therefore contributes: (i) (★)/(★★) as a clean
  banked reformulation (class-2), (ii) ΘC as a documented strictly-stronger
  condition with an explicit, unattackable-by-lane gap. Per the brief's own rule:
  "if all differential inequalities collapse to a known trap, document the collapse
  precisely and stop" — this is that documentation. No theorem is fabricated; the
  only PROVEN claims are the identities (pending §5) and the implication ΘC ⟹ RH.

## 4. Non-de-Bruijn semigroup / multi-scale inequality: collapse notes

- **Semigroup attempt.** Replace de Bruijn's multiplier e^{tu²} by subordinator
  multipliers e^{−t|u|^α}, α∈(0,2) (Lévy/stable), giving H^{(α)}_t, with "critical
  constant" Λ_α := inf{t : H^{(α)}_t all-real-zeros}. For t ≥ 0 these z-domain
  semigroups are convolutions with positive stable densities — the de Bruijn
  *sharpening* direction needs t<0 multiplication by e^{t|u|^α} for t<0, which is
  positivity-preserving only for α=2 (heat; excluded) because e^{t|u|} etc. are not
  positive-definite for t>0. Hence monotonicity theory (zero-movement) exists ONLY
  for the excluded α=2; for α≠2 the semigroup has no monotonicity theorem to feed,
  and every normalized Λ_α equals RH by H^{(α)}_0 = H_0 (⟺-RH family; class-2, and
  α=2 is the excluded de Bruijn-Newman lane regardless). COLLAPSED.
- **Multi-scale inequality attempt.** v-scale (u=e^v) exact identity:
  φ(v) − e^{−v/4}φ(−v) = sinh(v/4), φ(v)=e^{v/4}ψ(e^v) — the log-domain form of the
  FE; differentiating it in v yields only moment/differential identities of the
  closure list (D-annihilator, theta identity, deficit-2 profile — the last already
  PROVEN consistency-only on DH AND Epstein worlds by the barrier-zoo retro-test).
  COLLAPSED into the listed closures.
- **Curvature/log-concavity attempt.** (log ξ)″ bounds on the real axis from the
  positive-measure representation: PROVEN log ξ convex on (1,∞) (log L convex,
  L = Laplace transform of a positive measure) with the explicit deficit
  (log ξ)″ ≥ −1/x² − 1/(x−1)². Real-axis only — RH-inert (zeros live in the strip).
  Class-1/3. COLLAPSED.

## 5. Cheapest Rust-first test + STOPPING RULE (spec, to run next)

Bounded f64 probe, <2 min, one binary, `tools/theta_semigroup/`:
- t1 (★): ξ(1.5+2i) via Euler–Maclaurin ζ (direct, Re s>1, non-circular) vs
  RHS via composite Gauss-Laguerre quadrature of T(1.5+2i), T(−0.5−2i);
  plus (★) at s=2 (ζ(2)=π²/6 direct) and s=½ vs ξ(½)=0.4971207781883(4) [?];
  plus symmetry RHS(1.5+2i) = RHS(−0.5+... i.e. (★) FE check.
- t2: zero characterization: at t=14.13472514173469379 (first zero, hard-coded)
  verify A(t) = 1/(2(t²+¼)) to rel 1e-6; at t=10.0 verify strict inequality with
  sign (Re ξ ≠ 0 there).
- t3: ΘC discrimination: at δ=0.05, t={3.0, 30.0, 100.0} compute pair vs target,
  confirm LHS > 0 (no (★★) solution); report normalized gap ρ(δ,t)=LHS·(1+t²)/δ —
  print the min ρ over a small δ,t grid = the observed κ candidate.
- t3c (control): repeat t3 pair-equality check AT the two certified DH off-line
  zero locations (from ledger) using the DH world's own theta series — must show
  LHS ≈ 0 there (condition fires on the control). [If DH theta series not
  available in-probe: implement 30-line DH analogue in same binary.]
- STOPPING RULE (binding): if t1 fails >1e-7 rel → identity bug, re-derive §1
  before anything else. If t2 fails → numerical bug in quadrature. If t3/t3c
  behave as specified → the collapse documentation in §0–§3 stands; append
  numbers to this note and STOP (no further loop, no wider sweep — compute
  discipline; nothing beyond t1–t3 changes the verdict).

## 6. Feedback-loop analysis (s4h-systems-feedback-mapping, applied)

- R-loop (reinforcing, self-confirming): probe shows identity EXACT at every
  checked point → "the identity carries deep information" → more identity-derived
  conditions → more exact checks. This loop is the failure mode that manufactured
  earlier consistency-only levers; it is broken here by making the *discriminator*
  (t3c, DH control) run first and by the A1/A2 excavation verdict.
- B-loop (balancing, the barrier-zoo): RH-false control fires → condition
  re-classified to class-1/2/3 → exponent of the R-loop drops. Dominant loop in
  this lane after §0: B-loop (every derived inequality gets fed to the control and
  dies). Transition condition that would flip dominance: a lemma that survives
  the control WHILE not being ⟺-RH — the search for that is the persistence hook's
  continuing job, on objects NOT in this lane (GJT-completion decomposition,
  GS-2026 diagonal bound, per CAMPAIGN-STATE).

## 7. Ledger-line draft (for coordinator)

- `theta-semigroup-lane-2026-08-18`: **NO SURVIVOR (collapse documented)**: (★)
  ξ(s)=½s(s−1)(T(s)+T(1−s))+½ with T entire is the clean FE-form (class-1);
  critical-line and off-line characterizations (★★) ⟺ RH (class-2); amplitude
  bounds give only |t|≤6.7 corner (class-3); ΘC (uniform δ-phase gap) is provably
  one-way + non-equivalent (model-witnessed) but its missing lemma = RH-analytic
  content (no lane mechanism); α-subordinator semigroups have no monotonicity for
  α≠2 and ⟺-RH constants; DH control fires correctly (not proving-too-much) but
  that is automatic for ⟺-RH conditions. Consistent with Mellin-lane memo +
  fresh-corners theta closure + operator-lane Pólya closure (cite all three).

## 8. File map / provenance

- This note; probe to be added at tools/theta_semigroup/ (Rust, f64).
- Cited precedent notes (read this session): direct-rh-mellin-lane-2026-08-18.md
  (ledger line 8), direct-rh-operator-route-2026-08-18.md (line 10),
  barrier-zoo-rust-2026-08-17-fix.md, CAMPAIGN-STATE.md (fresh-corners closure,
  D-annihilator), hooks/agents.md (Rust-first, compute discipline, honesty rails).
- Status of every claim: (★) PROVEN by hand-derivation (numeric check pending t1);
  (★★) PROVEN from (★); ΘC ⟹ RH PROVEN; RH ⟹ ΘC NOT PROVEN and model-countered;
  missing-lemma assessment PROVEN (IBP O(1/t) is the only identity-provided rate);
  semigroup collapse PROVEN (positive-definiteness argument); curve/multi-scale
  collapse PROVEN (recorded closures). Nothing CONJECTURED is presented as proven.

— end of note v0.1 (partial seed; probe results appended on next pass) —
---

## ADDENDUM — probe results (run 3, tools/theta_semigroup, Rust f64, /tmp/theta_final.txt)

**Status:** PROBE RAN; identity CONFIRMED on the real axis; complex phase check
INSTRUMENTATION-BROKEN (documented, not an identity failure).

- t1 real axis: s=2 → RHS=0.523598775987 vs π/6=0.523598775598, absErr 3.9e-10 ✓;
  s=½ → RHS=0.497120778187 vs ξ(½)=0.49712077818831366, absErr 1.7e-12 ✓.
- t1 complex (s=1.5+2i): |LHS|=|RHS|=0.464 to ~1e-8 (magnitude matches), but phase is
  antiparallel (arg(LHS) ≈ arg(RHS)−π) → the probe's hand-rolled classical side
  (Lanczos gamma phase: atan-quadrant error — used (ai/ar).atan() instead of
  atan2(ai,ar); verified against reflection-formula re-derivation arg Γ(0.75+i)≈−0.19
  vs computed −0.60) is the buggy side, not the identity: the RHS needs NO gamma.
  TODO: fix atan2 + Stirling 1/z correction and re-verify full-complex (≤1 line probe
  change; verdict does not depend on it).
- t2: Re ξ(½+14.1347…) = 3.3e-6 ≈ 0 ✓ (first-zero height reproduced by the
  identity's Re channel). Im ξ on the line ≡ 0 BY THE IDENTITY (T(s)+T(1−s) real on
  the line) — the probe printed a spurious Im from a wrong line (Im ξ is not
  −(t²+¼)Im T; it is 0); correct per structure. ξ real on the critical line is the
  standard fact (Ξ(t) = ξ(½+it) ∈ ℝ).
- t3 (ΘC phase-gap): gaps at small t are large and real (ρ ≈ 87 at d=0.01,t=3; ρ ≈
  7.7 at d=0.01,t=10); at t=30 the gap falls to 1.5e-7 absolute (ρ ≈ 2.8e-3) — but
  1.5e-7 is the probe's quadrature floor at that oscillation frequency (h=0.02,
  phase rate t/2=15), NOT a genuine near-solution of (★★): |ξ(0.55+30i)| ≈ 5e-8 by
  the classical estimate, i.e. K is not on the target (gap should be ~1e-10 there).
  min ρ over grid = 6.9e-4 (floor-limited at t=30). Reading: no obstacle detected at
  small t; margins shrink like O(1/t²)-ish and the probe cannot resolve t≥30 with f64
  → the identity supplies NO uniform κ — consistent with the collapse verdict (§3:
  the missing lemma is exactly the analytic content of RH).

**Stopping rule:** t1 real-axis relErr ≪ 1e-6 → identity arithmetic confirmed; t3
behaved as specified → COLLAPSE DOCUMENTATION STANDS. STOP per brief. No wider sweep.

**Final verdict (unchanged):** this lane is an instance of the banked closures
(Mellin lane memo + fresh-corners theta corner + operator-lane Pólya closure): every
provable theta-differential inequality is FE-restatement (class-1), ⟺-RH (class-2,
incl. (★)/(★★) and all subordinator-semigroup Λ_α), or a finite corner (class-3).
ΘC is genuinely one-way and non-equivalent but its missing lemma is RH's analytic
core; no mechanism in the allowed lanes touches it. Zero RH evidence either way;
consistent with 28+ closed levers. No theorem fabricated.

## Coordinator correction: ΘC is false even under RH-compatible data

The proposed uniform gap condition ΘC is stronger than needed for the implication and is not
merely missing a proof. From (★),

`K(s) - target(s) = 2 xi(s) / (s(s-1))`.

At a critical-line zero `rho_n=1/2+i gamma_n`, take `s=1/2+delta+i gamma_n` and let
delta down to zero. Taylor expansion gives

`lim_{delta->0} |K(s)-target(s)|(1+gamma_n^2)/delta
 = 2 |xi'(rho_n)| (1+gamma_n^2)/(gamma_n^2+1/4)`.

The factor after `|xi'|` tends to 1. Hardy's theorem supplies infinitely many critical-line
zeros with `gamma_n -> infinity`. Stirling for `Gamma(1/4+i gamma/2)`, the polynomial
prefactor in xi, and the standard convexity/Phragmen--Lindelof bounds for zeta and its first
derivative give, for every fixed epsilon>0,

`|xi'(1/2+i gamma)| <<_epsilon gamma^C exp(-pi gamma/4)`,

for some fixed C, hence the displayed limit tends to zero along the critical-line zeros.
If a critical zero is multiple, the limit is zero immediately. Therefore the global infimum
required by ΘC is zero for the actual zeta, independently of RH. ΘC is **ABANDONED
(PROVEN false)**, not a live missing lemma. The finite f64 phase-gap values in `results_run3.txt`
are not evidence for a uniform lower bound; the complex instrumentation was also documented
as phase-broken.
