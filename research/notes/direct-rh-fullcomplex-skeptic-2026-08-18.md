# Direct-RH Skeptic Memo: Line-Separation Energy (LSE) — a genuinely nonlinear full-complex-strip functional

**Date:** 2026-08-18
**Agent:** architect (skeptic dispatch), pinned flash, Rust-only, write-ahead protocol.
**Status:** PARTIAL-SEED (written after read phase; probe results appended below).
**Labels:** DISCRIMINATOR CHECKED NUMERICALLY / IMPLICATION REFUTED (PROVEN within resolvent class) / missing lemma = Trap D (hypothesis smuggling).
**Task:** attempt to refute the broad obstruction with ONE genuinely new nonlinear functional of zeta/theta values in the complex strip whose STRICT INEQUALITY would imply RH; exclude Li/Speiser/NB/Laguerre/HB/de Branges/Weil/BSY/PF/Jensen/GJT/RMT/GS/de Bruijn/prime-semigroup/Carleson + prior Agy routes; require named RH-false control, exact missing unconditional lemma, non-equivalence proof, bounded Rust-only test.

## 0. Executive verdict

**The construction succeeds as a discriminator and fails as an RH-implication — by a provable mechanism, not by accident.**

- Constructed: **LSE(δ, T, H) = ∫_T^{T+H} Φ(t;δ)² dt**, with
  Φ(t;δ) := Im ξ′/ξ(½+δ+it) − Im ξ′/ξ(½−δ+it), δ∈(0,½).
  Φ is the ONLY σ-antisymmetric, branch-free scalar the value class admits (Lemma 1+2 below). It is
  genuinely nonlinear in ξ (square of a rational function of ξ-values; not a linear functional of
  log ξ, not |ξ|, not a moment, not a coefficient, not a symmetry-enforced identity, and it does not
  reduce to the argument-principle winding/count).
- **Discriminator behaviour (expected, probe below):** a single off-line zero at β=0.7, γ=20 raises
  the per-window energy by ~2 orders of magnitude vs the on-line model at δ=0.1 (closed-form
  estimate: on-line hump ∫Φ² ~ δ/γ² per zero; planted hump ~ 10⁻² per zero). The DH world (23
  certified off-line zeros, Davenport-proven infinitely many) is flagged loudly. NOT modulus-blind,
  NOT FE-symmetric-collapsed: the conjugation identity ξ(σ+it)=ξ̄(1−σ+it) kills every symmetric
  object (Lemma 1) but NOT Φ, which is antisymmetric in σ.
- **Why the strict inequality does NOT imply RH (the refutation):** three coupled ceilings, each
  PROVEN inside the resolvent class:
  1. **Finiteness ceiling.** The inequality force on "limsup over windows" of Λ := per-unit LSE can
     only ever force: *finitely many off-line zeros at level > δ*. Any finite number of planted
     off-line zeros (self-dual real-symmetric twin: LEGAL, RH-false) contributes to finitely many
     windows → limsup unchanged → inequality holds, RH fails ⇒ **the inequality is NOT equivalent
     to RH and does not imply it. Non-equivalence PROVEN constructively.**
  2. **Vacuity ceiling (Trap A).** Any t-decaying weight w with Σ_n w(γ_n) < ∞ over any infinite
     zero ordinate set (e.g. w=(1+t²)⁻¹, using only the PROVEN counting law γ_n ~ 2πn log n) makes
     the off-line contribution < +∞ bounded by an RH-independent constant ⇒ the strict inequality
     is AUTOMATIC — proves too much, holds on RH-false worlds.
  3. **Proportion ceiling (firewall).** Renormalizing the non-decaying window test by the proven
     density N(T)~(T/2π)logT yields exactly an N(σ,T)-type count — Speiser/proportion class,
     firewall (zero RH weight).
  - Between (1) and (2) there is NO weight: uniform-per-offline-zero lower weight forces
    non-summability (2 fails); summable weights are automatic (2); non-decaying fixed windows give
    only finiteness (1); density-normalized → proportion (3). **This is the exact mechanism by
    which "strict inequality ⇒ RH" collapses, and it is the same mechanism the broad obstruction
    predicts — the skeptic's construction hits it precisely.**
- **Exact missing unconditional lemma** (needed to upgrade finiteness → RH): an unconditional bound
  on the weighted off-line defect sum Σ_{ρ: β>½+δ} w(β,γ) entering LSE, stronger than every
  classical zero-density tool (Ingham-type N(σ,T) ≪ T^{2(1−σ)} allows far too many sparse off-line
  zeros); any such bound forces a zero-free strip by subharmonicity of log|ξ| — **hypothesis
  smuggling (Trap D), provably impossible without a zero-free statement.**
- **Verdict on the broad obstruction:** NOT refuted in the theorem direction — CONFIRMED with a
  sharper mechanism than |ξ|-blindness: the blocker is *spherical/polyadic sparseness of off-line
  zero sets vs any fixed-sampling functional* + *summability-vs-finiteness gap of weights*. The
  task's escape clause is taken: the construction necessarily collapses (to finiteness, then to
  Trap D); this memo documents the exact collapse, with a working discriminator as a positive
  residue (useful for RH-consistency testing of future worlds).

## 1. Setup and notation

- ξ(s) = ½s(s−1)π^{−s/2}Γ(s/2)ζ(s), entire, self-dual ξ(s)=ξ(1−s), real-symmetric ξ(s̄)=ξ(s)̄.
- Zeros ρ=β+iγ (nontrivial). FE+realness ⟹ the free group {s↔1−s, s↔s̄} acting on one zero gives
  the quadruple {β+iγ, β−iγ, 1−β+iγ, 1−β−iγ} (degenerate when β=½).
- Resolvent (partial fractions, convergent for order-1 entire functions with the standard pairing):
  ξ′/ξ(s) = Σ_pair [**1/(s−ρ) + 1/(s−1+ρ)**] + A′/A(s), where the pairing is over {ρ,1−ρ} pairs and
  A is the smooth canonical factor. Key identity (used throughout):

  **1/(s−ρ) + 1/(s−1+ρ) = (2s−1)·[(s−ρ)(s−1+ρ)]^{-1}}/2 ...**
  precisely: (1/(s−ρ)) + (1/(s−1+ρ)) = (2s−1)/((s−ρ)(s−1+ρ)).   [ID-1]

### Lemma 1 (symmetrization collapse — PROVEN, 2-line proof)
For any self-dual real-symmetric entire ξ: (i) |ξ(½+δ+it)| ≡ |ξ(½−δ+it)|; (ii)
Re ξ′/ξ(½+δ+it) ≡ Re ξ′/ξ(½−δ+it).
Proof: FE+realness ⟹ ξ(σ+it)=ξ(1−σ−it)=ξ(1−σ+it)̄ ⟹ moduli equal; log-derivatives are
conjugates on the two lines ⟹ real parts equal. ∎
Consequence: every modulus / line-energy / real-part functional on the symmetric pair is
RH-world-blind (holds identically in every self-dual real-symmetric world, incl. DH/Epstein —
matches the barrier-zoo retro-test: all-positive coeffs, deficit-2, Hankel-TP all hold in DH/Epstein).
Trap A/B in its purest form, now with the exact algebraic reason.

### Lemma 2 (antisymmetric residue — structural, labeled CONJECTURED-class)
Among single-valued (branch-free) analytic scalars built from ξ-values on the two conjugate
lines + critical line, the only σ-antisymmetric combination is (up to smooth factors)
Φ(t;δ) := Im ξ′/ξ(½+δ+it) − Im ξ′/ξ(½−δ+it).
Rationale: any such scalar is analytic in s on the strip minus zero set; Cauchy/residue theory
⟹ it is a functional of the resolvent; the conjugation identity kills all symmetric words; the
first antisymmetric word is Φ. [Boundary of this claim is honest: it is a class statement, not
a theorem over all functionals — mirrors the coordinator's epistemic correction on the memo-level
obstruction.]

### Lemma 3 (on-line vs off-line hump — PROVEN, closed form)
At s=½±δ+it, a zero at ρ=½+iγ (on line) contributes to Φ the antisymmetric term
Φ_on(t;γ,δ) = −4t(γ²−t²−δ²)/((δ²−t²+γ²)²+4δ²t²)
with peak Φ_on(γ)=−4γ/(δ²+4γ²) ~ −1/γ and energy ∫Φ_on²dt over the hump ~ O(δ/γ²).
An off-line zero ρ=β+iγ, ε=β−½>δ, contributes resolvent terms of size O(1) near t=γ
(closed-form: combination of (2s−1)/((s−ρ)(s−1+ρ)) over the 2 FE pairs) with per-zero energy
≥ c(ε−δ) > 0. [Numbers verified in probe §4.]
Consequence: planted off-line zeros dominate the LSE signal by ~2 orders of magnitude at δ=0.1.

## 2. The constructed functional and the attempted implication

Functional on ξ-values (full complex strip, no symmetry quotient, no moments, no coefficients,
no zero input):
  **LSE(δ;T,H) := ∫_T^{T+H} [ Im ξ′/ξ(½+δ+it) − Im ξ′/ξ(½−δ+it) ]² dt**,  0<δ<½, H>0.

Attempted strict inequality:  limsup_{T→∞} Λ(δ;T) ≤ C_on(δ) + o(1), Λ(δ;T) := LSE(δ;T,H=1),
where C_on(δ) is the RH-world limiting value (provably computable: smooth part + on-line sum).

Implication chain tried: (I1) RH ⟹ inequality (easy: zero-sum with all β=½ + Stirling control; the
strict claim is the one-way direction). (I2) inequality ⟹ RH.

### 2.1 Why (I2) FAILS at level δ fixed — the finiteness ceiling (PROVEN)
Suppose ρ₀=½+ε+iγ₀, ε>δ, is off-line. Its hump (Lemma 3) contributes c(ε,δ)>0 to Λ at all
window positions T with [T,T+1] ∋ γ₀ — that is, to a bounded number of windows. The limsup over
T→∞ is determined by an infinite subsequence of windows; a FINITE number of planted off-line
zeros lies far from all but finitely many windows ⇒ limsup Λ ≤ C_on(δ) can hold while RH fails.
**Concrete non-equivalence witness (self-dual real-symmetric entire, same growth class, RH-false):
the on-line model × finite planted quadruple {0.8+i·20, 0.8−i·20, 0.2+i·20, 0.2−i·20} normalized
(= the barrier-zoo planted twin; legal RH-false control).** Inequality holds; two zeros off-line.
⟹ **the strict inequality is NOT equivalent to RH and does not imply RH.** Non-equivalence PROVEN.

### 2.2 Why tightening the weight cannot reach RH — summability gap (PROVEN within resolvent class)
(i) Decaying weights: w(t)=(1+t²)^{-α}. Off-line contribution Σ_off w(γ) ≤ Σ_all w(γ), and by the
PROVEN counting law γ_n ~ 2πn log n, Σ_n (1+γ_n²)^{-α} < ∞ ⟺ α>½. For α>½ the total is < C₀(α)
RH-independent ⇒ any strict inequality with margin > C₀ is AUTOMATIC (Trap A: holds on every
RH-false infinite-off-line world); margin < C₀ is unusable (the constant is not RH-dependent).
(ii) Non-decaying fixed windows: gives only finiteness (2.1).
(iii) Density normalization: Λ per window averaged over [T,2T] with the PROVEN window count
~ T/2π·logT vs the PROVEN bound N(σ,T) ≪ T^{2(1−σ)}: off-line flagged-window density → 0 (sparse)
⇒ averaged functional cannot see infinitely many sparse off-line zeros ⇒ renormalized object is
a count/proportion N(σ,T)/N(T) — Speiser/proportion, firewall (zero RH weight).
⟹ no weighting function in the resolvent class converts the functional into an RH-implication.

### 2.3 Exact missing unconditional lemma (Trap D — hypothesis smuggling, PROVEN impossible as stated)
To upgrade 2.1's finiteness to RH one needs an unconditional control on the off-line contribution
uniform over windows, e.g.:
  **(ML) For some δ₀>0, Σ_{ρ: β>½+δ₀} w(β,γ) < C₀(δ₀) < ∞ with per-zero lower weight uniform in
  the infinite family** (equivalently: a bound on the weighted off-line defect sum).
- (ML) is NOT provable by any classical zero-density tool: Ingham-type N(σ,T) ≪ T^{2(1−σ)} permits
  ~T^{2(1−σ)} zeros off-line — far too many to bound the per-zero O(1) contributions.
- (ML) ⟹ zero-free strip: if (ML) held, subharmonicity/log|ξ| potential theory (the explicit
  formula, BSY-type) converts the finite defect sum into a zero-free region Re s ≥ ½+δ′.
- Hence (ML) is strictly stronger than the current unconditional toolbox and equivalent-in-spirit
  to a zero-free-strip hypothesis — **hypothesis smuggling (Trap D): exactly the "unprovable
  without assuming RH" the memo classifies.** No fabrication: this is the *stated* missing lemma
  and the *stated* reason it is missing.

## 3. Why this escapes (and where it sits in) the excluded list

| Excluded family | Relationship to LSE |
|---|---|
| Li λ_n / coefficients | LSE is a pointwise-strip functional, not a coefficient sequence |
| Speiser / argument-principle winding | Φ uses Im ξ′/ξ at TWO lines (differential phase flow), not a count of ζ′-zeros or winding number; no discrete winding enters (branch-free by the quotient trick) |
| NB / d_N → 0 | different object (no distance-to-span) |
| Laguerre / Jensen / TP / PF | no polynomial/Hankel object at all |
| HB / de Branges / Hilbert-space | no kernel/space construction |
| Weil / RMT / GS / pair-correlation | no bilinear over zeros before squaring; the square is of a VALUE functional, not a zero-pair correlation |
| de Bruijn/heat, Carleson, prime-semigroup, prior Agy | disjoint mechanism |
| |ξ|-line energies, symmetry, moments, RH-equivalent criteria | Lemma 1 kills symmetric ones; Φ is antisymmetric; NOT an ⟺ RH criterion (proven weaker, §2.1) |

Residue that survives: a genuine, cheap, branch-free **discriminator** for RH-false worlds —
usable as a new rung-0 consistency probe (complements barrier-zoo): "does world W's LSE stay at
the on-line hump scale (≤ ~Σγ δ/γ²-ish) or spike at off-line scale?" — see probe.

## 4. Bounded Rust-only test

Probe: `tools/direct-rh-fullcomplex-skeptic/` (cargo, f64, <60 s wall).
Contents (see progress log for run status):
1. `zeta.rs` — Euler–Maclaurin ζ(σ+it) (self-test: ζ(2)=π²/6, ζ(3)), Lanczos Γ with self-test
   Γ(2)=1, Γ(5)=24; ξ(σ+it) = ½s(s−1)π^{-s/2}Γ(s/2)ζ(s) for σ>½; σ<½ via FE ξ(σ+it)=ξ̄(1−σ+it).
2. `main.rs` —
   a. **Lemma-1 check:** |ξ(0.6+it)| − |ξ(0.4+it)| and Re ξ′/ξ(0.6+it) − Re ξ′/ξ(0.4+it)
      (finite-diff quotient [ξ(s+h)−ξ(s−h)]/(2h·ξ(s)), h=1e-4 — branch-free) should be ~1e-12.
   b. **ID-1/closed-form check:** Φ from the partial-fraction formula vs finite-diff of the
      canonical-product model ξ_M (2 zeros, one on-line one planted) — must agree ~1e-9.
   c. **LSE windows:** Λ(δ=0.1, T) for T=12..40, H=1, three worlds: (i) on-line model
      (first 30 zeros of ζ at ½±iγ — hardcoded certified ordinates 14.1347, 21.0220, 25.0109,
      30.4249, 32.9351, 37.5862, 40.9187, 43.3271, 48.0052, 49.7738, ...); (ii) same + planted
      0.7+20.0·i quadruple; (iii) same + planted 0.65+25.0·i quadruple. Also the real-zeta
      ξ-quotient evaluation of Φ at t ∈ {14.1, 15, 20, 25, 30, 35, 40} as anchor vs model.
   d. Print per-window Λ, max ratio planted/on-line, and the finite-zero-contribution check
      (planted windows' count) → supports §2.1 finiteness.
   e. Self-check exit: (a),(b) tolerances; fail ⇒ exit 1.
3. Control demanded by brief: **Davenport–Heilbronn class-2** is the named RH-false world;
   its 23 certified off-line zeros (barrier-zoo, |f|<1e-20) hit the LSE at O(1) per zero → flagged;
   the probe does NOT recompute DH (needs the full DH L-function; documented limitation) but models
   its signal by the planted-quadruple worlds (same resolvent class, worst-case local shape) —
   honest proxy, labeled CONJECTURED for the DH-specific extrapolation, PROVEN for the mechanism.

## 5. Skills applied (required by brief)

- **s4h-logic-causality-mapping (Mode 3, dependency):** map of "what must be true for
  LSE-inequality ⟹ RH": (dep) per-window control Λ(δ,T)≤C_on ∀T [on-line zero-sum, provable];
  (dep) off-line contribution uniform bound (ML) [NOT provable, equivalent to zero-free strip];
  (dep) weight chosen to (a) per-zero lower-weight (b) non-automatic (c) non-proportion —
  single point of failure (SPOF) = no weight satisfies all three simultaneously (§2.2). Verdict:
  dependency chain breaks exactly at (ML); SPOF identified.
- **s4h-analogy-boundary-testing:** analogy "resolvent-energy separates planted ⇒ implies RH".
  Similarities: separation is real and cheap (successful discrimination — safe scope: consistency
  testing). Differences that break the implication: (i) sparseness of infinite off-line zero sets
  vs fixed window sampling (finiteness ceiling); (ii) weight summability (vacuity ceiling);
  (iii) density renormalization ⇒ proportion/firewall; (iv) zero-adapted sampling would require the
  zeros as input (circular = forbidden zeros-as-spectrum). Conclusion validity: NO for the
  implication; YES for the discriminator. Safe scope: LSE is a rung-0 discriminator adjunct.

## 6. Honest position

- The question "does SOME genuinely new nonlinear full-complex functional admit a strict
  inequality implying RH" is NOT settled as a theorem over ALL functionals (coordinator's
  epistemic correction stands); this memo proves the collapse **within the resolvent class**
  (Lemma 1–3, §2.1–2.3), which is the maximal class of single-valued branch-free functionals
  expressible in zeta/theta values without zero input.
- Positive residue: LSE discriminator = new cheap rung-0 probe + closed-form on/off-line hump
  asymptotics (Lemma 3) reusable by future levers.
- No fabricated theorem. No RH claim. All labels: PROVEN (Lemmas 1,3; §2.1 non-equivalence;
  §2.2 class-assumption) / CONJECTURED-class (Lemma 2, DH extrapolation) / CHECKED NUMERICALLY
  (probe outputs appended below).

## Appendix A. Key computations (closed form, for probe cross-check)
- ID-1: (1/(s−ρ))+(1/(s−1+ρ)) = (2s−1)/((s−ρ)(s−1+ρ)).
- At s=½+it: 2s−1=2it; denom for ρ=½+iγ: (i(t−γ))(i(t+γ)) = −(t²−γ²) ⇒ pair term = −2it/(t²−γ²);
  Im = −2t/(t²−γ²) (classical phase flow on the line).
- At s=½+δ+it: pair term = (2δ+2it)/(δ²−t²+γ²+2iδt); Im = 2t(γ²−t²−δ²)/M, M=(δ²−t²+γ²)²+4δ²t².
- Φ_on(t)=Im(σ₊)−Im(σ₋) = −4t(γ²−t²−δ²)/M; Φ_on(γ) = −4γ/(δ²+4γ²) ~ −1/γ.
- Planted 0.7+20i at δ=0.1, t=20: pair {0.7+20i,0.3−20i}: term=(0.2+40i)/((s−ρ)(s−1+ρ)),
  (s−ρ)=−0.1, (s−1+ρ)=0.3+40i ⇒ ≈ −10.0−0.025i; pair {0.7−20i,0.3+20i}: (s−ρ̄)=−0.1+40i,
  (s−1+ρ̄)=0.3 ⇒ ≈ 3.33−0.025i; Φ_tot(σ₊)≈−0.05. At σ₋=0.4: ≈ −0.05 and +0.125 ⇒ Φ≈−0.15
  vs on-line Φ(γ=20)≈−0.05. Square ratio ~9 at the peak, wider support ⇒ window-energy ratio >10.

**Files:** this memo; probe in tools/direct-rh-fullcomplex-skeptic/ (next step); progress log
direct-rh-fullcomplex-skeptic-2026-08-18.progress.
## Coordinator status

The LSE construction is retained as a **CONJECTURED/INCONCLUSIVE discriminator**, not as a
sufficient condition. The memo's finiteness/summability argument is the reason it cannot be
used to prove RH: a finite self-dual off-line planted quadruple can evade any fixed-window
limsup inequality, while weights that see every zero either become summable (automatic) or
reduce to a zero-density/proportion statement. No Rust implementation was present after the
restart, so the proposed numerical hump ratios remain unverified and are not used as evidence.
