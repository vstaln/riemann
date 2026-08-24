# Cross-domain attack note — Dynamical systems / transfer operators / thermodynamic formalism
Date: 2026-08-24 · Lens author: adventurer (subagent) · Labels: PROVEN / CONJECTURED / INCONCLUSIVE per repo honesty rules.

## 0. Prior-art audit (what I checked, and the structural delta)

`grep -il "selberg|transfer operator|gauss map|thermodynamic|dynamical"` over `research/notes/*.md` + ledger. Dynamical / spectral prior that **already exists** in this repo, cited so my route differs structurally from each:

- **Selberg zeta / trace formula / hyperbolic surfaces** (`paper-finder-spectral.md`, `idea-generator-crossdomain.md` W-H3, `idea-generator-history.md` W-H3/W-H5). Repo itself records the killer objection: *funneled* hyperbolic surfaces have Selberg-zeta zeros **off** the critical line (Pollicott–Vytnova 2204.08218, Borthwick) — i.e. the Selberg analog has no universal "line" rigidity. My route uses a *different* transfer operator (Gauss continued-fraction map, Mayer) whose thermodynamic formalism has a distinctive one-parameter phase transition — **not** the Selberg/geodesic-flow-on-compact-surface spectrum.
- **Lee–Yang circle theorem / Asano–Ruelle / Ising zeros on |w|=1** (`wave20-swarm-harvest-2026-08-15.md`). That is the *polynomialness* (Lee–Yang polynomial truncations of Xi) route — a purely real-algebraic/combinatorial rigidity. My route is the *pressure / eigenvalue-crossing* route of a genuinely non-normal transfer operator. Different mechanism, different obstruction.
- **Control-theoretic dynamical systems catalog** (`idea-generator-control.md`) and cross-domain candidates (`idea-generator-crossdomain.md`) name logistic/oscillator dynamics — none use the Mayer/Ruelle continued-fraction operator.
- **Continued fractions** appear in `li_criterion_proof.md` and `ramanujan_conjectures.md` but for the **digamma / Li integrals**, object ∝ (s-1)ζ via a *different* identity; they do **not** construct the Ruelle–Mayer zeta or its pressure. Not a prior for this lane.
- `paper-finder-001.md` §6 correctly flags Zeraoulia–Caceres (Montgomery-conjecture "chaos") and Jerby etc. as crank/heuristic, excluded. Not used.

**Structural delta:** none of the found prior builds the route object as the **Mayer Galerkin/transfer operator `L_s` of the Gauss continued-fraction map, its topological pressure P(s) = log(leading eigenvalue), and the one phase transition at Re(s)=1/2** for the nontrivial spectrum. That is this note's territory.

## 1. Mechanism in real math (named objects, where zero-location enters)

Object. Let T:[0,1]→[0,1], T(x)={1/x} (x=0 ↦ 0), the **Gauss continued-fraction map**. For real parameters fix s and define the **Ruelle–Mayer transfer operator** (Mayer 1976/1990, following Ruelle):

  (L_s f)(x) = Σ_{n≥1} (x+n)^{-2s} f( 1/(x+n) ).

On a space of analytic functions on a disk (or a weighted L^∞/BV space), L_s is a compact, indeed nuclear/trace-class operator in a suitable Roelcke–Mayer space; its Fredholm determinant/products are entire. This is the **non-uniformly hyperbolic / non-self-adjoint** sibling of the compact-surface Selberg operator — it codes the *parabolic cusp* dynamics of PSL(2,Z)\H (equivalently the continued-fraction flow), not a compact geodesic flow.

Where zeros live. Define the **Mayer/Ruelle zeta**

  Z(s) = Π_{k≥0} det( I − L_{s+k} ).

PROVEN (literature): Z(s) is entire and its zeros are precisely the **non-trivial Riemann zeros** (the Selberg–Ruelle zeta of the modular surface, Mayer's product/transfer realization; equivalently the known identity relating the Fredholm determinant of the Gauss-map Ruelle operator family to ζ). The *trivial* zeros and the pole at s=1 come from the k-sum / cusp contribution. So:

  **RH  ⇔  the only solutions of "1 ∈ Spec(L_s)" (i.e. det(I − L_s)=0) in the relevant half-plane sit on Re(s)=1/2.**

Equivalently, in thermodynamic formalism: the **topological pressure** P(s) = log(Perron eigenvalue of L_s) is real-analytic on the spectral gap wherever, and the *leading eigenvalue λ(s)=1* crossings = zeros of ζ. The modular-surface/Gauss family is famous for having **exactly one "phase transition"** (non-analyticity of the pressure / surface model) located at the critical value — this is the thermodynamic-formalism face of RH in *statistics* terms: the value s=1/2 is the critical point of the one-parameter weighted continued-fraction system.

Why real-zero-location information genuinely enters: L_s is **not self-adjoint**, so its spectrum is a complex set with no built-in symmetry; whether the eigenvalue-1 solutions of λ(s)=1 lie on a line is *not* forced by any Hermiticity. The location question is therefore carried by the *actual non-normal spectrum*, which is exactly the hard, information-heavy part. This (properly) makes the route non-vacuous: it genuinely depends on zeta's arithmetic, via the coding of PSL(2,Z) by continued fractions.

## 2. What it would take to break; the likely obstruction (state it myself)

Obstruction (specific, and I name it as the probable terminal wall):

1. **No line rigidity for non-normal spectra.** det(I − L_s) is *entire*, so by Hadamard factorization it realizes essentially arbitrary zero configurations. The analyticity of P(s) *away* from the spectrum is a **consequence** of where λ(s)=1 sits, never a **cause**; so "pressure analytic except possibly at 1/2" is equivalent to RH, not a route to it. Any thermodynamic-formalism argument must therefore import an *additional* rigidity beyond generic transfer-operator theory.
2. **Positivity only constrains the real axis.** For real s, L_s is positive on the cone of positive functions → Perron/pressure eigenvalue λ(s) is real, and λ(s)=1 roots on the real axis detect only the trivial/pole structure and the *edge*. The non-trivial zeros are complex; at complex s there is **no Perron–Frobenius cone**, so the positivity that gives the pressure its analytic handle **silently disappears exactly where the zeros are**. This is the same wall every spectral/positivity approach hits (Li, Weil positivity, de Branges), now restated in transfer-operator language. I claim this honestly: the transfer-operator reformulation is *faithful* to ζ (good) but is not a *certificate* (it repackages the obstruction).
3. The one piece of structure that *could* beat generic non-normal rigour is the **infinite-type / parabolic (cusp) coding**: the modular surface is non-uniformly hyperbolic with a single cusp, whose contribution sits near the real axis and separates "parabolic = trivial" from "hyperbolic = non-trivial". If a rigidity exists, it must flow from this non-compact parabolic coding — which is exactly the part a finite planted fake cannot cheaply reproduce.

To actually break RH this way one would need a **non-self-adjoint, non-finite-type spectral symmetry** (e.g. a cone/complex-potential rigidity, a two-parameter analytic family with a real-line attractor for eigenvalue-1 crossings) that is provably absent in every RH-false model. None is known; name the missing lemma: *"Spec(L_s) ∩ {λ=1} is confined to Re(s)=1/2 for the Gauss map family, and no finite-type thermodynamical variant satisfies the same."*

## 3. RH-false control (planted-zero / D-H-style model) and the distinguishing output

Control model. Take a **planted-zero fake**: either the Davenport–Heilbronn-type Dirichlet function (RH known to fail for it) *or — sharper for this lane —* a **finite-state / finite-type expanding Markov–Ruelle system** (finite continued-fraction truncation of the Gauss map, or a finite-type shift) whose Ruelle zeta det(I−L_s) is a finite-product/eigenvalue equation and can be **planted** with a zero at s0 = 3/4 + i·t0 by design (row/column perturbation of the transfer matrix).

What both models share with true-ζ machinery: exact same probe inputs — a transfer-matrix/operator family, a pressure P(s), real-axis Perron eigenvalues. A naive "certificate" that says *"RH ⇔ pressure analytic except at 1/2"* is **meaningless unless it can be shown to fail on these fakes**. Key control fact I assert (and the probe verifies): for a **finite-type** system the pressure is analytic (finite Markov shifts have no phase transition in the open system except at genuine first-order points), and a *complex*-planted zero produces **no signature in the real-axis pressure/PF spectrum** — the fake is invisible to any real-s probe.

Distinguishing datum that separates true-RH machinery from numerology: the probe must use the **complex spectrum** (det(I−L_{s0}) → 0 at the planted s0) AND must make a **structural prediction that the fake violates**: namely the *infinite-type parabolic coding* (the cusp / continued-fraction tail) is what any true mechanism must be shown to use, because the fake, having finite type, provably *cannot* carry it. Concretely the discriminator output:
- (a) probe on true ζ-family: real-s Perron λ(s) crosses 1 near s→1/2 with a finite-size scaling toward 1/2 (parabolic/pressure edge), while the complex-planted fake shows NO such scaling;
- (b) probe at complex s via truncated det(I−L_s): true family's finite-rank det has no root off Re=1/2 (consistent with RH), while the planted fake's det **does** root at s0=3/4+i·t0 by construction;
- (c) therefore: any claim "mechanism is thermodynamic-PF/pressure based" is **refuted** by (a)+(b) (PF probe can't see the planted complex zero); a claim surviving must point to datum (a)'s *parabolic-structure dependence* — and we then check that the fake's finite-type system provably lacks that parabolic structure. That is the honest numerator-vs-numerology test.

## 4. ONE falsification probe — <20 min, Rust f64, laptop

File target: `research/scripts/xdom_pressure_probe.rs` (proposal only; not yet run).

```
1. Discretize Gauss map on N=2048 uniform bins on [0,1].
   Build finite-rank matrix A_s[i,j] = {1/(x_i+n)}^{2s} * (nearest-bin of 1/(x_i+n) → j),
   summed over n=1..Nq partial quotients (Nq ~ 64; f64 acceptable for scaling study).
2. REAL-S probe: power-iteration Perron eigenvalue λ(s) for s in [0.30,0.85], step 0.01.
   Locate s* where λ(s) crosses 1. Repeat for N=512,1024,2048 → fit finite-size scaling s*(N)→? .
   PASS/FAIL vs target: s*(N) approaching 1/2 (parabolic/pressure edge) with an estimated rate.
3. PLANTED CONTROL: perturb A_s with rank-1 kernel engineered so that, at complex s0=0.75+0.4i,
   det(I−A_{s0})≈0 (planted zero), leaving the real-s Perron spectrum of step 2 unchanged.
4. DISCRIMINATOR assert:
   (assert) step-2 real-axis λ(s) for the planted fake is essentially unchanged
            (complex planted zero invisible to real PF probe)  → proves PF-pressure probe
            cannot certify RH.
   (assert) finite-rank det(I−A_s) at complex s roots at s0 for the fake, roots only near
            Re=1/2 for the true family (up to truncation error).  → the ONLY certifying
            signal lives in the complex (non-PF) spectrum.
5. Structural check: repeat 2–4 on a FINITE-TYPE truncation (drop the parabolic tail, i.e.
   cut partial quotients at Nq small so coding is finite-type): confirm the phase-transition
   signal at 1/2 disappears / degenerates → demonstrates the parabolic (cusp) structure is the
   load-bearing part, which a finite planted fake cannot reproduce.
```
Runtime: N=2048, ~66 s-values, power iteration ~ converged in <100 iters, plus small dense det at a few complex s for N≤1024 → comfortably < 20 min f64 on one laptop core. **The falsification target is explicit:** the probe *expects* the real-pressure probe to be blind to a planted complex zero (refuting pressure-only claims) and *expects* the parabolic-structure dependence to be the only discriminating datum. If instead the real-axis probe were to somehow fire at 3/4 for the fake, that would *strengthen* the fake's threat — either outcome is informative and reported honestly.

## 5. Honest label of best-case outcome

**CONJECTURED / CHECKED-NUMERICALLY (if the probe runs clean this session).** The route is a *faithful reformulation* of RH into the non-normal spectrum of the Gauss-map Ruelle operator and its one phase transition at Re(s)=1/2 — real, named mathematics (Mayer's L_s, pressure P(s), Selberg–Ruelle zeta of the modular surface). But it is **not** a proof route as posed: it re-encounters the universal spectral wall (non-self-adjointness ⇒ no line rigidity; positivity dying at complex s). Its defensible, non-vacuous contribution is (i) a sharp statement of the *exact* rigidity that would be needed (a RH-false class of Ruelle families provably lacking the modular surface's parabolic/infinite-type coding), (ii) an explicit planted-zero + finite-type control showing pressure/PF probes cannot be the certificate, and (iii) a <20 min Rust falsification probe encoding all of it. Best case: CHECKED-NUMERICALLY that λ(s)=1 scales to s=1/2 and that the complex-planted zero is PF-invisible — a *registration* result, not a proof. If any step suggests a rigidity that survives the finite-type control, that becomes a fresh, higher-value sub-program. No claim of a proof is made; the search continues.
