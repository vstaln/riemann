# Idea Generator: physics & applied-math attack catalog on RH and the on-line-zero constants

**Agent:** IDEA GENERATOR (physics angle). Round 1.
**Purpose:** feed the EXECUTIONER agents. Every vector is concrete enough to attack.
**Honesty protocol:** this file invents *no* proofs and asserts *no* new theorems. Physics facts below are
standard results (SFF, Dyson jellium, Fisher–Hartwig, RH method, de Finetti, negativity, etc.) named at
the level of "standard in the field"; anything I cannot verify from the sources we hold is labeled
"reported standard — verify before use". Every *idea* is CONJECTURED by construction, labeled
**NEW** (invented here, not in previous catalogs) / **KNOWN-DEAD** (killed in earlier rounds; cite) /
**KNOWN-OPEN** (a known open problem, or a route already flagged in our notes; cite the crossdomain
numbering) / **TESTED-OPEN** (numerically tested by our own tools or attack notes, still open).
Overlap discipline: crossdomain catalog = idea-generator-crossdomain.md, cited as [CD-V#]/[CD-W#]/[CD-A#];
attack notes = attack-kernel [AK], attack-ceiling [AC], attack-multiplicity [AM], attack-finitet [AF],
attack-lfunctions [AL].

**State of the art the physics must respect (PROVEN):**
- Two-moment method: tr W_T = N, ‖W_T‖²_HS = (1/c₁)N, 1/c₁ = 1/2 + (1/√2)cot(1/√2) = 1.3274993…, certificate
  value 2 − 1/c₁ = 0.67250070… (Theorem D); 2/3 (flat), 5/6 distinct, 0.83625 distinct (optimal window).
- Bandwidth-one ceiling 0.68182868746… realized by an exact-rational 256-periodic marked law with F ≡ 1 on
  [0,1] (PROVEN in Lean, [AC]); every certificate of the class reads only (mean density, F on [0,1],
  integrality). λ ≤ 1 is a HARD wall (off-diagonal prime sums need Hardy–Littlewood beyond X = T) [CD-A1,A5].
- 5/6 distinct wall: the all-simple world and the "2/3 simples + 1/6 doubles" world are spectrally
  identical in (tr, ‖·‖²); the two-moment certificate provably cannot separate them (PROVEN, [AM]).
- tr Â³ is unconditionally evaluable exactly in the Rudnick–Sarnak range kλ < 2 (λ < 2/3) [CD-V3]; odd
  moments do not lower Λ₁(0) for the *on-line* functional (§7.5(e)); the *distinct* (c=3) functional is a
  different object — P2.
- Finite-T: bound/N − 0.6725 = Δ(T) > 0 at every tested T, decaying like ~1/log T (TESTED, [AF]).
- ξ′: 0.85838/0.86864 simple-on-line, 0.92919/0.93432 distinct (PROVEN); ξ″/ξ‴ mechanical extension
  [CD-V9]; naive interlacing LP empty [CD-A4].
- Families: Thm E (fixed χ, 2/3/2/3/5/6) PROVEN; family-averaged (q → ∞, T = (log q)^c) CONJECTURED,
  needs Gevrey taper [CD-V12]; GL(2) individual = hard wall (bandwidth 1/2) [AL].

---

## Pool 1 — RMT beyond GUE: soft edge, Tracy–Widom, crossover, finite-N ≈ finite-T, DBM, resolvent moments

### P1.1 Resolvent (Stieltjes) moments as a certificate input — NEW
**Idea:** Replace the moment pair (tr, ‖·‖²) by a *resolvent* statistic G(z) = (1/N)tr(W_T − zI)^{-1} of the
compressed Weil form, combined with a contour-integral representation of the positive-index count,
n₊(W) = (2πi)^{-1}∮ tr(W − z)^{-1}·d(log det)… type objects. In free probability, the Stieltjes transform
of a large matrix satisfies a closed equation (Marchenko–Pastur); for W_T the *symbol* (the |u−v|-kernel
compression) is explicit, so the resolvent at complex z is constrained by the same prime-side data that
fixes the moments — possibly with *different* error structure (a resolvent identity is exact; the moments
are its expansion).
**Analogy:** eigenvalues ↔ eigenvalues of a random matrix; resolvent = Green's function; certificate =
positive-spectrum counting via the Cauchy/argmax formula — the inertia is read off the *Green's function's
pole structure* rather than two scalar traces.
**Needs:** (i) prime-side evaluation of tr(W_T − z)^{-1} at complex z (a *matrix* of prime sums with the
resolvent kernel — new diagonal computation, off-diagonal still MV-bounded); (ii) a proof that the
resolvent's pole structure gives strictly more than (tr, ‖·‖²) *within the same bandwidth*.
**Feasibility:** Low–Med. The danger (honest): the resolvent at bandwidth one is determined by the moment
sequence through a continued fraction, and the moments beyond 2 are exactly the missing input — so the
resolvent likely *reduces* to the moment problem (see P8.4). If so, the vector's value is diagnostic (it
shows the certificate class = "two-moment truncation of the Green's function").
**Cheapest probe:** build W_T at T = 200–600 (code exists in tools/finitet), compute G(z) for a grid of
complex z, and check whether Im G or the arg of the resolvent's determinant carries information beyond the
two moments — i.e., whether two configurations with equal (tr, ‖·‖²) but different spectra give visibly
different resolvents at bandwidth one (they do trivially — the *question* is whether any such difference is
*provable from the prime side*).

### P1.2 Finite-N GUE corrections as a template for the finite-T deficit — TESTED-OPEN (extends [AF])
**Idea:** For GUE, the *mean* of a smooth linear statistic has O(1/N) corrections and the covariance is
fixed by the sine kernel (classical). The zeros' finite-T deficit Δ(T) = (‖W‖²/N − 1.3275) has measured
shape ~1/log T with single-sample wiggle [AF]. The physics question: does the deficit follow the *GUE
prediction* (kernel/boundary-driven, would be ~1/T²-class for a C∞ statistic — it is NOT) or is it
*arithmetic* (pair-correlation error, ~1/√log T per B24 Thm 1)? The measured 1/log T says: neither — it is
dominated by the *off-diagonal pair sum* (the Ψ₂-approximated pair sum reproduces it, [AF]).
**Analogy:** finite-N corrections in RMT ↔ finite-T corrections in number theory; the *order* of the
correction identifies which "mechanism" (boundary, arithmetic mean, fluctuation) is active.
**Needs:** (i) extend [AF]'s trend to larger T (smoothed C∞ φ_T, more zeros); (ii) the exact GUE prediction
for the same statistic (the pair-sum under the Ψ₂ kernel for the sine process — computable by quadrature);
(iii) a decomposition of the deficit into kernel-boundary + arithmetic parts.
**Feasibility:** Med (mostly compute already half-done). Value: decides whether the *asymptotic* slack is
zero (certificate saturates the crystal under PCC — no room) or positive (systematic slack).
**Cheapest probe:** Rust: compute the sine-process pair sum under Ψ₂ at N = 50…500 and compare its
approach to 1.3275 with the ζ-data approach in [AF] (both ~1/log T or not).

### P1.3 Edge statistics / near-rank-deficiency as an off-line detector — NEW (diagnostic)
**Idea:** The measured W_T is numerically near-rank-deficient (min eigenvalue ~1e-17·λmax, [AF]) — the
*edge* of the empirical eigenvalue law encodes the (1,1)-plane structure of off-line pairs (a pair injects
one positive ~λ and one negative ~−λ' block). The *density of small positive eigenvalues* of W_T is a
direct, unconditional measurement of the off-line-pair content *without RH* (W_T is prime-side data!).
**Analogy:** Tracy–Widom governs the soft edge of RMT spectra; the *edge of the certificate matrix* is the
analogous universal object — here it measures "how many hyperbolic planes sit at the bottom of the
spectrum".
**Needs:** (i) full spectrum of W_T (V1 code, [CD-V1]); (ii) a model: p independent (1,1)-planes of the
measured v-structure have edge density computable by quadrature; compare the *measured* edge density with
the p = 0 prediction.
**Feasibility:** Low–Med, diagnostic only (a measurement cannot enter a per-T certificate). Value: it
calibrates how much off-line structure the two-moment method *would* miss; if the edge density is
consistent with p = 0, reality is on the "no off-line pairs" side and the certificate is pricing the right
thing.
**Cheapest probe:** reuse [CD-V1]/[AF] W_T code; histogram the smallest 5% of eigenvalues at T = 200–600 and
compare with the p = 0 Gabor-vector model.

### P1.4 Crossover / repulsion inputs: what a repulsion statement would have to look like — KNOWN-OPEN (core), NEW (quantification)
**Idea:** In the Rosenzweig–Porter / BGS crossover picture, spectral statistics interpolate between
Poisson (integrable) and GUE (chaotic) with a *repulsion exponent* β: P(spacing < ε) ~ ε^β, β = 2 for GUE.
The 256-periodic ceiling law is a *crystal* (β = ∞-like, exact doubles, atoms). Any *proven* lower-bound
repulsion for ζ's zeros — even "no two zeros closer than c/T" — would exclude the crystal and break the
ceiling. Known: only weak gap statements are proven; repulsion is KNOWN-OPEN [CD-V17]. The NEW part: a
*quantified* statement of what is needed — solve the certificate LP with the constraint "configuration has
no pairs closer than ε" and report the ceiling as a function of ε; this prices *any* future repulsion
input.
**Analogy:** BGS/Rosenzweig–Porter crossover: the level-repulsion exponent is the order parameter; the
certificate ceiling is a function of that order parameter.
**Needs:** (i) an LP solver over marked configurations with a min-gap constraint (extend the N=256
machinery); (ii) the curve ceiling(ε).
**Feasibility:** Low (compute); the *input* (a proven ε) is the hard open problem. Value: a roadmap —
"a repulsion input of strength ε buys you X".
**Cheapest probe:** perturb the 256-law LP: forbid grid configurations with adjacent occupied cells closer
than 2, re-solve, read the new simple fraction.

### P1.5 Isospectral invariance of the certificate: why deformations can't help — NEW (strategic)
**Idea:** tr W and ‖W‖²_F = Σλᵢ² are *isospectral invariants* (preserved by any unitary/conjugation
deformation), and the rank–trace value 2c·tr − ‖·‖² is a function of them alone. Dyson Brownian motion and
Toda flows are isospectral flows — so *no deformation dynamics can change the certificate value*. The
ceiling's extremal configuration is therefore a *fixed point of the whole isospectral family*, which is
why "evolving" the configuration (DBM, Toda, any interpolation) produces no new input.
**Analogy:** conserved quantities of integrable flows (Toda/DBM) ↔ the certificate inputs; the certificate
is a *constant of the motion*.
**Needs:** none (a proof-level observation: it explains *why* every isospectral/RMT-dynamics route to a new
input must fail, redirecting effort to genuinely new *data* (beyond-1 F, third moments)).
**Feasibility:** immediate (documentation). Value: kills a whole class of "let DBM tell us something"
ideas at the framing stage.
**Cheapest probe:** none needed (logical argument); record as a strategic note in the attack log.

### P1.6 The jellium defect-energy reading of the two moments — NEW (overlaps [CD-V2])
**Idea:** The 256-law is a *defect-laden Wigner crystal* (marks ≠ 1 are defects); the two-moment data fix
the *defect density* exactly (Σ marks = 256 fixes the deficit budget); the certificate is a *defect-count
inequality*. In jellium, defects carry *formation energy* (they cost free energy); for the zeros, the
analogous statement would be "defects repel / have positive chemical potential" — a *repulsion input*
(see P1.4). The NEW concrete idea: the *LP dual* of the marked-configuration problem (already the in-class
route [CD-V2]) is exactly a *defect chemical potential* — solve it, and read off the "defect energy" that
a *provable* repulsion statement would have to beat to close 0.6725 → 0.6818.
**Analogy:** Wigner crystal + defects; jellium ground states; the certificate = defect thermodynamics.
**Needs:** the LP dual solve (same as [CD-V2]); a statement "a repulsion input of strength E buys δ".
**Feasibility:** Med. Value: unifies the in-class LP route with a physical picture and produces the
"defect energy" target number.
**Cheapest probe:** the LP dual solve at N = 256 (exact rational, as in [AC]); report the certificate
value and the dual variables (the defect chemical potentials).

---

## Pool 2 — Quantum chaos / spectral form factors: the ramp+plateau and the beyond-1 region

### P2.1 The SFF plateau as a *per-instance exact* bound: is there a finite-rank analog? — NEW (probe), core KNOWN-OPEN
**Idea:** For a unitary U on an N-dimensional space, |tr U^τ|² ≤ N for every integer τ by Cauchy–Schwarz —
the plateau value N is *per-instance exact*, no averaging. For ζ, the analog would be an *unconditional
upper bound* on the α > 1 form-factor integral with a finite-support kernel, coming from the *finite rank*
of the compression (W_T is rank ≤ N; the "dimension" is N). B24 gives F ≥ 0 pointwise (an upper-kernel
input, exploited conditionally by CGdL20 [CD-V11]) but no *value* beyond α = 1. The probe: compute the
*SFF of W_T itself* — K(α) := |Σ_ρ Ψ(s_ρ)-weighted|²-type sums at "stroboscopic times" α ∈ ℤ — entirely
from the prime side — and test whether any exact identity (not inequality) survives at finite T.
**Analogy:** SFF ramp (diagonal) + plateau (off-diagonal, coherence); the plateau is *protected* by
unitarity — the zeros' analog would need a unitary realization, i.e., RH (honest: likely the "no free
lunch" statement again).
**Needs:** (i) the W_T-level SFF computed from primes (cheap — code exists); (ii) an examination of whether
any *identity* at α ∈ ℤ holds (e.g., trace-moment identities tr Â^k relate to integer-α SFF — that IS the
moment route [CD-V3, HL*]).
**Feasibility:** Low (compute); the transfer is KNOWN-OPEN and likely equivalent to RH by construction —
the *measurement* (how close W_T's SFF is to the ramp+plateau shape at finite T) is the honest deliverable
for P3.
**Cheapest probe:** Rust: compute K(α) for α = 0…8 from the [AF] W_T code; plot vs α and the GUE plateau
prediction.

### P2.2 Thouless-scale reading of the dimension cap — NEW (framing)
**Idea:** In MBL/SFF physics the *Thouless time* is the scale below which the system looks RMT; for the
compressed problem, Prop 7.4's dimension cap λ₁N ≤ N is the *Thouless/Heisenberg scale* — the certificate
reads only sub-Thouless (bandwidth-one) data. The SFF literature's central lesson: *beyond the Thouless
scale the spectrum is protected by exact degeneracy structure (the plateau), and the only model-dependent
input is the crossover*. For ζ, the "crossover" scale is where the off-diagonal prime sums stop being
diagonal-dominated — exactly X = T, the λ ≤ 1 wall [CD-A1,A5].
**Analogy:** MBL Thouless time ↔ the X = T prime-dominance wall; plateau protection ↔ the (unreachable)
beyond-1 F.
**Needs:** none (strategic framing). Value: a clean physical statement of *why* the wall is at λ = 1 and
*why* no sub-λ = 1 trick can reach the plateau.
**Cheapest probe:** none (documentation); attach to the attack log.

### P2.3 Gutzwiller periodic orbits ↔ explicit formula; quantum ergodicity ↔ family averaging — NEW (motivation for P4)
**Idea:** The explicit formula is a *Gutzwiller trace formula*: prime powers log p are the periods,
Λ(p)/√p the stability weights, zeros the spectrum ("primes as periodic orbits", standard dictionary). In
Gutzwiller theory the *off-diagonal* orbit-pair terms produce the ramp/plateau — for ζ they are the
X > T prime pairs (HL-strength). The genuinely useful import: *quantum ergodicity* — off-diagonal terms
vanish *on average* over ergodic ensembles. The ζ-analog: the off-diagonal prime sums vanish *on average
over a family* — this is *exactly* the family-transport mechanism of P4 ([CD-V12], [AL]): the Dirichlet
family average kills the off-diagonal by character orthogonality. So the physics gives a *first-principles
motivation* for funding the family route: "quantum ergodicity for the prime orbit gas."
**Analogy:** Berry diagonal approximation (ramp) ↔ Montgomery diagonal evaluation; quantum ergodicity
(off-diagonal suppression on average) ↔ family orthogonality.
**Needs:** no new math for ζ; a sharpened physical argument that the family average is the *right* ergodic
ensemble (the characters χ mod q as the "disorder" over which the orbit gas self-averages).
**Feasibility:** Med (framing + the P4 numerical probe below). Value: reframes [CD-V12]'s Gevrey-taper
machinery as a standard physics statement, sharpening expectations (self-averaging is *generic*, so the
family route is *likely* to work — an honest prior).
**Cheapest probe:** the P4.4 variance measurement (below) — it *is* the "self-averaging" test.

### P2.4 The plateau is exact for CUE at finite N — the "missing input is exact level structure" statement — KNOWN-OPEN (framing)
**Idea:** For the CUE ensemble the two-point function is *exactly* 1 at all scales (finite-N exact — it
follows from the Haar measure), not just asymptotically. The zeros' conjectured F(α) = 1 for all α is the
*infinite* version of this; the *exactness at finite N* is what makes the CUE plateau "protected". The
transfer: any *exact finite-T* statement about ζ's correlations would be the analog of CUE's exactness —
and the only exact finite-T structure we have is the *bandwidth-one* evaluation (B24/BGST). Conclusion
(honest): the plateau region (α > 1) is unreachable by *any* finite-rank exactness argument, because the
exactness we have is exactly the ramp.
**Analogy:** CUE Haar-measure exactness ↔ bandwidth-one explicit-formula exactness; the ramp is the exact
part, the plateau the "emergent" part.
**Needs:** none (documentation). Value: prevents funding "exactness" routes in the beyond-1 region.
**Cheapest probe:** none.

### P2.5 Stratospheric SFF: the ξ′-derivative tower as successive SFF "descendants" — NEW (speculative)
**Idea:** The SFF of the zeros of ξ^(j) (the derivative tower, P5) is a *different* statistic on the same
underlying configuration; the FGL constants rising with j (0.858 → 0.868…) suggest the derivatives' local
statistics are *more rigid* (fewer near-degeneracies) — the derivative zeros "repel more". The physics
analog: the zeros of the j-th derivative of the characteristic polynomial of a random matrix are the
*stationary points of the log|det| landscape* — a known object in the "random matrix landscape" literature
(stationary points of the log-modulus of random polynomials). The landscape statistics are *computable* and
are *not* the same as the eigenvalue statistics — a genuinely different input for P5's certificate.
**Analogy:** random polynomial landscapes (log|det| stationary points) ↔ zeros of ξ^(j).
**Needs:** (i) the explicit formulas for ξ^(j)/ξ^(j−1) (mechanical, [CD-V9]); (ii) the RMT landscape
prediction for the *joint* statistics of the derivatives' zeros; (iii) a numerical comparison.
**Feasibility:** Med–High. Honest risk: the landscape literature concerns *fixed* random matrices, whereas
the certificate needs *per-T* unconditional inputs — the transport is heuristic; still, it gives a
*prediction* to test (does the j-th derivative zero set's two-moment constant follow the RMT landscape
curve?).
**Cheapest probe:** compute the two moments of the ξ′ zero set from real zero data (Rust, from the ξ′/ξ
explicit formula) and compare with the landscape prediction at j = 1 before funding j ≥ 2.

---

## Pool 3 — Integrable systems / soliton theory: Bethe ansatz, Toda, Coulomb gas, jellium third moment

### P3.1 Dyson jellium third moment and the distinct wall — NEW (overlaps [CD-V3])
**Idea:** The β = 2 jellium / sine-kernel process has an *exact* three-point function (Dyson 1962;
standard) — the value tr Â³/N = S₃ for ζ's zeros under RH in the RS range is *that* number. The distinct
(c = 3) bookkeeping with tr Â³ input is [CD-V3]'s question. The NEW physics addition: the jellium *third
sum rule* — the third moment of the charge in a box is fixed by the *three-point* correlation (the
Stillinger–Lovett hierarchy). For ζ this says: the third moment of the *counting function* N(I) over
long intervals is *determined* by S₃ in the conjectural regime — so the *measured* counting-function
skewness (from the Selberg-CLT-order fluctuations) is a *numerical shadow* of tr Â³, testable with real
zeros *before* any theorem.
**Analogy:** Coulomb gas ↔ zeros as charged particles; charge-in-a-box sum rules ↔ counting-function
moments; compressibility sum rule ↔ the two-moment method itself.
**Needs:** (i) the exact S₃ value at finite rank (Slater-determinant formula, standard — see W-P2); (ii)
the empirical third moment of the counting function over many windows (Rust); (iii) the [CD-V3] LP.
**Feasibility:** Med. Value: a *cheap empirical decision* on whether the third moment can plausibly move
5/6 *before* investing in the hard evaluation.
**Cheapest probe:** mpmath/Rust: third moment of N(interval) over ~10⁴ windows at height 10³–10⁴ vs the
jellium prediction; if the skewness is structurally different, the three-point route to 5/6 is likely
futile — a documented negative.

### P3.2 Toda / isospectral flows preserve the certificate — NEW (strategic, overlaps [CD-V14])
**Idea:** The LeClair–Mussardo Bethe-ansatz heuristic [CD-V14] is one flavor of "zeros as integrable
particles". The physics structure that *is* rigorous: Toda and DBM are isospectral flows, and the
certificate value (2c·tr − ‖·‖²) is a *conserved quantity* — see P1.5. Any integrable-particle picture of
the zeros therefore *cannot* produce a new certificate input; it can only explain the *dynamics* behind
the two moments. The honest NEW angle: use the Toda/DBM picture to *predict the finite-T approach rate*
of ‖W‖²/N to 1.3275 (the "relaxation" of the isospectral flow), giving a physics prior for P6's error
terms.
**Analogy:** Toda relaxation time ↔ finite-T deficit exponent; action variables ↔ the two moments.
**Needs:** (i) the DBM/Toda prediction for the decay of the variance of the off-diagonal pair sum; (ii)
comparison with [AF]'s measured ~1/log T.
**Feasibility:** Low–Med (mostly framing + one numeric comparison). Value: a prior for P6; honesty flag:
the isospectral picture is heuristic for ζ, and "reported integrable zeros proposals" are folklore whose
sources we do not hold (verify before citing anywhere).
**Cheapest probe:** fit [AF]'s Δ(T) curve against the Toda-relaxation ansatz (1/T^θ and log laws) and
report the best exponent; no new compute beyond the existing data.

### P3.3 The free-energy/partition-function reading of the variational problem — NEW (overlaps [CD-V2], [AK])
**Idea:** The certificate functional c₁(v) = λ(∫v)²/(∫v² + λ²∫∫|s−s′|v(s)v(s′)) is a *Coulomb-gas free
energy* at temperature set by λ: ∫v² is the "kinetic/entropy" term, ∫∫|u−v|vv is the 1D Coulomb
interaction, (∫v)² is the normalization. The optimal window cos(√2u) is the *ground state* of the
particle-in-a-box with the |u−v| interaction ([AK] already computes the I+T spectrum). NEW: *extend the
functional with a defect term* — add a chemical potential μ for the off-line pairs / multiplicities (a
"defect field") — and solve the extended variational problem. The class-optimal certificate (the LP dual,
[CD-V2]) *is* the defect field; the physics predicts the *shape* of the optimal defect field (a constant
plateau with boundary layers — the complementarity/contact-set structure of equilibrium-measure theory,
see P5.1).
**Analogy:** free energy ↔ certificate value; chemical potential ↔ LP dual variable; ground state ↔
extremal configuration.
**Needs:** the LP dual solve + the equilibrium-measure identification (P5.1).
**Feasibility:** Med. Value: predicts the *form* of the missing constraint (a contact-set/barrier shape),
turning the LP dual from a numeric search into an analytic target.
**Cheapest probe:** numerically solve the dual LP at N = 256 ([AC] machinery) and *plot* r(x); check for
contact-set structure (where the constraint binds).

### P3.4 The moment sequence m₁..m₄ as a spectral measure: Christoffel function for the distinct wall — NEW (overlaps [CD-V3])
**Idea:** The HL*-moment sequence m_k = 1, 4/3, 2, 13/4, … (GUE values, [AM]/§7.5(f)) is the moment
sequence of a *positive measure on ℝ* (if HL* holds). Any such measure has a *Christoffel function*
K_m(x) (the extremal polynomial value), and the "Christoffel bound 1 − Λ_m(0)" [CD-V3] is the
mollifier-side shadow. NEW: compute the Christoffel function of the *HL*-moment measure* from m₁..m₄
alone and price it into the *distinct* (c = 3) bookkeeping. The moment sequence determines the first four
Hankels, and the Christoffel function at the *support points* of the crystal is an *upper* constraint on
the admissible masses — a constraint the crystal's masses must satisfy. If the HL* moments force a
Christoffel bound inconsistent with the crystal's mass distribution, the 5/6 wall moves.
**Analogy:** orthogonal polynomials / Gauss quadrature: the crystal's grid masses ARE quadrature weights;
the Christoffel function is the "maximum local weight" allowed by the moments.
**Needs:** (i) the 4×4 Hankel from m₁..m₄; (ii) the Christoffel function; (iii) the distinct-count LP with
the Christoffel constraint.
**Feasibility:** Med — this is the sharpest concrete form of P2's "third moment" question I found; note
the honest caveat: HL*(k₀,λ) is conjectural, and §7.5(e) proves odd moments don't lower Λ₁(0) for the
*n₊* functional — the *distinct* functional is the open target.
**Cheapest probe:** mpmath: from (m₁,m₂,m₃,m₄) = (1, 4/3, 2, 13/4), build the 3×3 Hankel, compute the
Christoffel function on [0,2], and test the crystal's masses {1/6, 2/3, 1/6} against the implied upper
bounds. If the crystal *passes*, the moment constraints don't exclude it (clean negative); if it *fails*,
the wall breaks.

### P3.5 The derivative tower as a SUSY ladder: Stieltjes/continued-fraction certificates — NEW (overlaps [CD-V9], [CD-A4])
**Idea:** The ratios ξ^(j)/ξ^(j−1) are the "superpotentials" of a 1D SUSY quantum-mechanics ladder whose
ground states are the ξ^(j) (real-rootedness is preserved by the derivative — Rolle/Laguerre). The NEW
structural claim: if ξ^(j) has only real zeros, then ξ^(j+1)/ξ^(j) is a *Herglotz/Stieltjes function*
(positive imaginary part off the real axis), and its *continued-fraction* (from the *moment sequence* of
the ξ^(j)-zeros via Newton identities) has *positive coefficients*. A *truncated* continued fraction with
positive coefficients is a *finite, checkable* certificate — the natural "finite shadow" of RH(ξ^(j)).
This is the operator Green's-function picture (see P8.3) applied to the tower.
**Analogy:** SUSY ladder ↔ derivative tower; superpotential ↔ log-derivative; Green's function (Stieltjes
transform) ↔ ratio of consecutive derivatives; positive CF coefficients ↔ real roots.
**Needs:** (i) the explicit formula for ξ^(j)/ξ^(j−1) (mechanical, [CD-V9]); (ii) the first two/three
moments of the ξ^(j)-zero set (unconditionally evaluable in the same RS range? — needs checking, the
derivative zeros' moments are *different* functionals); (iii) the CF-positivity check.
**Feasibility:** Med. Honest risk: the CF needs *all* moments for exactness (the truncated version is a
*necessary* condition only — it cannot be sufficient without infinitely many moments, a KNOWN-DEAD-adjacent
obstacle, cf. the Hankel route [CD-W3]). The *interlacing* LP is already dead ([CD-A4]). Value: the
*diagnostic* — how far does the truncated-CF positivity hold numerically for real ζ data (j = 1 first)?
**Cheapest probe:** from the first ~10⁴ zeros, compute the first 4 moments of the ξ′-zero set (via the
ξ′/ξ explicit formula) and the 2×2/3×3 Hankel; check PSD (positive CF coefficients).

---

## Pool 4 — Statistical mechanics: Coulomb gas / β-ensembles, free energy ↔ moments ↔ largest eigenvalue, replica

### P4.1 The marked-configuration LP in the thermodynamic limit (marks as an Ising spin field) — NEW (overlaps [CD-V2], [AC])
**Idea:** The 256-law's marks ∈ {1,2} are a *spin field* on a 256-site lattice; the certificate LP over
marked configurations with the two-moment + integrality constraints is a *constrained Ising ground-state
problem*. The honest NEW move: solve the LP at N = 512, 1024, 2048 (exact rational, Rust — the [AC]
machinery scales) and check (i) whether the simple fraction converges to a *thermodynamic limit* (if it
converges to < 0.6818, the ceiling *improves* — a real finding; if it stays ≥ 0.6818, the ceiling
law is confirmed as the thermodynamic limit), and (ii) whether the marks settle into *translation
invariance* (a 256-periodic law at N = 512 would be evidence the 256-structure is not an artifact).
**Analogy:** Ising ground states / thermodynamic limit; finite-size scaling; the marks as a magnetization
field with the two moments as the Hamiltonian constraints.
**Needs:** (i) LP solver (exists for N = 256 in the Lean repo as exact rational data); (ii) scaling runs.
**Feasibility:** Low–Med (compute). Value: adversarial validation of the ceiling + possible improvement;
this is the cleanest *cheap* path to "does 0.6818 move?"
**Cheapest probe:** N = 512 exact-rational LP solve; compare the simple fraction with 0.6818287.

### P4.2 The certificate value as a free-energy difference — NEW (framing)
**Idea:** The gap 0.6725 (window-optimal) vs 0.6818 (class-optimal) is the *free-energy gap* between two
certificate classes over the same configuration data; the gap to reality (measured Δ > 0 at finite T [AF])
is the free energy *released* by ζ's zeros relative to the extremal crystal. Free-energy language makes the
directionality of the walls precise: the crystal *minimizes* the free energy among admissible
configurations (it is the ground state), so every configuration has ≥ the crystal's certificate value.
**Analogy:** free-energy minimization ↔ LP optimum; ground state ↔ extremal law.
**Needs:** none (the LP duality [CD-V2] IS the free-energy duality). Value: a clean statement that the
*only* in-class gain is the LP dual (V2), now with a physics justification for why it's the ground-state
duality.
**Cheapest probe:** none (documentation; fold into P3.3/P5.1).

### P4.3 Largest-eigenvalue statistic as a third input — NEW (diagnostic)
**Idea:** The certificate reads tr and ‖·‖²; the *largest eigenvalue* λmax of the normalized Â is a third
statistic. The crystal has λmax = 2 (double marks → eigenvalue 2); a configuration with all λ ≤ 2 − ε would
be *excluded* from the crystal's spectral footprint. The trivial bound (λmax ≤ ‖·‖_F = √(1.3275N) ≫ 2) is
useless, so λmax is *not* provable from the two moments — but it is *measurable* from the prime side (W_T
is prime-side data!). Measure λmax of W_T at finite T: if it hovers near 2, the real spectrum is
crystal-like at the top edge; if well below, reality is spectrally far from the extremal law.
**Analogy:** largest eigenvalue of a Coulomb gas (the "edge"); Tracy–Widom fluctuations ↔ the fluctuation
of λmax(W_T) over T.
**Needs:** W_T spectrum (exists, [CD-V1]/[AF]); a careful normalization (the ideal-model W_T vs the
normalized Â).
**Feasibility:** Low (measure). Value: a *diagnostic* of how far reality sits from the extremal law
spectrally; if the edge is far, it motivates hunting for a *provable* edge input; if near, it confirms the
crystal is spectrally indistinguishable (consistent with the ceiling).
**Cheapest probe:** [AF] code: print λmax/λmean at T = 100…700 and its T-trend.

### P4.4 Annealed → quenched concentration for families (de Finetti / typicality) — NEW (P4, overlaps [CD-V12], [AL])
**Idea:** For the Dirichlet-character family (or any family), the family-averaged W_T is an *annealed*
object; the certificate value per member is *quenched*. Because both tr and ‖·‖² are linear, annealing
commutes — but the *per-member fluctuation* is what a per-form theorem needs. The physics: for ergodic
disorder, quenched = annealed + concentration, with the deviation controlled by the *variance* of the
family (a 4-point object). NEW: prove/measure the *concentration* — the variance of ‖W_{T,χ}‖² over
χ mod q — and combine with the annealed 2/3 (Thm E machinery) via Chebyshev to get *per-character*
statements near 2/3 for *most* characters. The de Finetti/typicality theorem bounds the distance between
the symmetrized (family-averaged) state and the product (single-member) state — a *quantitative* template.
**Analogy:** annealed vs quenched disorder; de Finetti / typicality; concentration of measure.
**Needs:** (i) numerical variance of the HS norm across χ mod q for q ~ 10⁴–10⁵, T = (log q)^c (cheap,
character sums via fast algorithms); (ii) a theorem bounding the 4-point family correlation (the variance
is a *4-character* orthogonality sum — genuinely new analytic work).
**Feasibility:** Med (probe cheap, theorem hard). Value: converts the "family 2/3" conjecture into a
*quantified* target ("the family certificate has variance V; hence most members are within V^{1/2} of
2/3") — the natural next theorem after Thm E, and the physics "self-averaging" prior (P2.3) says it should
work.
**Cheapest probe:** Rust/Python: for a few large q, compute ‖W‖²/N across 100+ characters χ mod q at
T = (log q)^c; report mean and std. If std ≪ gap-to-wall, fund the theorem; if std ~ 1, the per-member
statement is empty.

### P4.5 β-deformation: ζ as GUE-type, ξ′ as GOE-type? — NEW (speculative)
**Idea:** The window variational problem is solved by the cosine for ζ (kernel |u−v|, "β = 2"), but the
ξ′-functional's optimizer is *not* the cosine — the quartic beats the flat window there ([AK], [CD-V8]).
Physics: different symmetry classes (GOE/GUE/GSE, β = 1/2/4) have different *extreme statistics* and
different *optimal majorants*; the conjecture: ζ's certificate is the β = 2 (GUE) extremal problem, and
ξ′'s is a *β = 1-flavored* variant (the derivative has a different symmetry — the "real" vs "complex"
distinction of the underlying L-function). The NEW test: solve the *β-generalized* variational problem
(replace ‖·‖² by the β-scaled Frobenius norm) and check whether the ξ′-quartic's quotient matches the
β = 1 optimum.
**Analogy:** symmetry classes in RMT; extreme-value statistics at β = 1,2,4.
**Needs:** (i) the ξ′ functional (from the Lean XiPrime files, [CD-V8]); (ii) the β-generalized
variational problem solved numerically.
**Feasibility:** Low–Med. Value: a *classification* statement (which "symmetry class" each derivative
belongs to) that predicts the whole tower's constants P5 and explains *why* the quartic helps ξ′ but not
ζ.
**Cheapest probe:** mpmath: minimize the β-parametrized quotient for the ξ′ functional; compare the optimal
β and window shape with the paper's quartic constants.

---

## Pool 5 — Matrix models / orthogonal polynomials: Riemann–Hilbert method, equilibrium measures, external fields

### P5.1 The certificate function IS an external field of a 1D Coulomb gas — NEW (overlaps [CD-V2])
**Idea:** The LP-dual certificate r(x) (the object the class-optimal certificate is) plays the role of the
*external field* in a 1D Coulomb-gas equilibrium problem: the extremal configuration is the equilibrium
measure for the field r, and the stability inequality `ceiling_stability` [AC] is the *variational
inequality* of that equilibrium problem (the "Euler–Lagrange with a constraint: W^r(x) ≥ c on the
support"). Equilibrium-measure theory (Deift; the RH method) provides the *structure theorem*: the optimal
external field satisfies complementary-slackness with a *contact set*, and the certificate is determined
by the contact geometry. NEW: use the equilibrium-measure classification to *identify the class-optimal
certificate in closed form* — extending the cos(√2u) solution (the *one-delta* extremal problem [AK]) to
the *multi-constraint* problem that the marks/integrality impose. The RH-method exact solutions of such
variational problems are the standard machinery for exactly this.
**Analogy:** equilibrium measure with external field ↔ certificate LP; contact set ↔ alternation points of
the optimal majorant (Chebyshev alternation, P7.6).
**Needs:** (i) the discrete equilibrium problem for the marked law at N = 256; (ii) its continuum limit;
(iii) an RH/Steklov solution of the variational inequality.
**Feasibility:** Med–High, genuinely new math. Value: the *only* route I see to an *exact* in-class
certificate (0.6725 → 0.6818 exactly) rather than a numerical one; also unifies [CD-V2], P3.3, P7.6.
**Cheapest probe:** discretize the equilibrium problem (the [AC] LP dual at N = 256); check the contact
set is a union of intervals and record the free energy (the certificate value) — then compare with the
paper's 0.6725 and the ceiling 0.6818.

### P5.2 Christoffel–Darboux finite-rank corrections as the finite-T error template — NEW (P6)
**Idea:** The sine kernel is the Christoffel–Darboux kernel of the orthogonal polynomials of the
equilibrium measure; the *finite-rank* CD kernel has computable trace deficits (the O(1/N) approach of the
truncated kernel to its limit). The zeros' finite-T deficit is *measured* ~1/log T [AF], which is *not*
the O(1/N)-type CD deficit — the *comparison* cleanly separates "kernel truncation effects" (would be
1/T-class for a C∞ window) from "arithmetic pair-correlation effects" (1/√log T-class). NEW: compute the
CD trace deficit for the *actual* window (cosine, C⁰ at the boundary — the hard cutoff is the worst case
[AF]) and use it as the *baseline*: the *excess* deficit over the CD baseline is the arithmetic part,
testable at finite T.
**Analogy:** CD kernel truncation ↔ finite-rank Toeplitz asymptotics (Szegő + Fisher–Hartwig, P5.5);
sine kernel ↔ the equilibrium measure's local kernel.
**Needs:** (i) the CD/Toeplitz trace for the cosine window at rank N (quadrature); (ii) the same at the
*smoothed* (C∞) window — the [AF] recommended next step.
**Feasibility:** Low–Med (compute). Value: a quantitative decomposition of P6's error terms into
kernel-artifact vs arithmetic parts.
**Cheapest probe:** quadrature of the Ψ₂ pair sum for the sine process at N = 50…1000; fit the deficit
exponent; compare with [AF]'s ζ-data exponent.

### P5.3 The compression of a unitary: null-model spectrum of W_T — NEW (diagnostic)
**Idea:** W_T is a *compression* of the Weil form to a windowed space. Compressions of random unitaries
have explicit spectral laws (arcsine/quarter-circle-type, standard). As a *null model*: if the zeros were
"featureless" (the RMT null), the *fluctuation* of W_T's spectrum about its mean law would follow the
compression ensemble's; deviations are *arithmetic structure* (the actual pair correlation). NEW: compare
the level-spacing statistics of W_T's eigenvalues against the compression-ensemble prediction — a
*diagnostic* of how "RMT-like" the compressed spectrum is at finite T.
**Analogy:** compression ensembles ↔ the windowed/truncated structure of W_T; null-model testing.
**Needs:** W_T spectra (exists); the compression-ensemble spacing law (quadrature or small-numeric).
**Feasibility:** Low (compute). Value: diagnostic for P3 (how close reality is to RMT at the *compressed*
level).
**Cheapest probe:** reuse [AF]/[CD-V1] spectra; compute the spacing ratio statistic and compare with the
compression ensemble.

### P5.4 Two-cut equilibrium measure with a barrier (the marks constraint) — NEW (conjectured)
**Idea:** Equilibrium measures with an *obstacle/barrier* (a repulsive potential in a region) develop
*two-cut* (or multi-cut) supports, and the two-cut solution is often *exactly solvable* (elliptic
functions). The marks ≥ 2 / integrality constraint acts as a barrier on the configuration space; the
extremal law with the defect structure is plausibly the *two-cut equilibrium measure* of a quadratic-plusbarrier external field. NEW: identify the two-cut problem whose solution is the 256-law (or its continuum
limit) and compute its free energy in closed form — giving the class-optimal certificate *exactly*.
**Analogy:** two-cut equilibrium measures (hard-edge/barrier models) ↔ the marked crystal; elliptic exact
solutions ↔ the closed-form certificate.
**Needs:** (i) the continuum limit of the marked-configuration LP; (ii) the two-cut variational problem and
its RH solution.
**Feasibility:** Med–High, speculative but principled. Value: the exact in-class constant (same prize as
P5.1, different route).
**Cheapest probe:** fit the 256-law's mass profile to a two-cut equilibrium density (a one-line
least-squares); if the shape matches a known two-cut density, the closed form is within reach.

### P5.5 Fisher–Hartwig corrections to the Szegő limit: predicting the finite-T deficit exponent — NEW (P6)
**Idea:** The HS norm of a Toeplitz compression is a Szegő-type limit; *jump discontinuities* in the symbol
produce Fisher–Hartwig power-law corrections. The cosine window is C⁰ (it does not vanish at ±1/2 [AF]),
so its symbol has a *Fisher–Hartwig jump* — the *predictable* finite-rank deficit from the jump has a
specific exponent. The measured deficit ~1/log T [AF] is *slower* than any FH power law — the *excess*
over the FH prediction is the *arithmetic* (pair-correlation) part. NEW: compute the FH correction for the
cosine symbol; subtract it from the measured deficit; the remainder is the arithmetic error term — a
*clean decomposition* of P6's error, with a physics-grounded baseline.
**Analogy:** Szegő + Fisher–Hartwig asymptotics ↔ Toeplitz compressions; the hard cutoff's jump ↔ the
C⁰ window.
**Needs:** (i) the symbol of the W_T compression (known — the |u−v|-kernel/cosine structure [AK]); (ii)
the FH exponent computation; (iii) the deficit subtraction.
**Feasibility:** Low–Med (compute + one classical computation). Value: P6 error decomposition, and a
*checkable prediction* (the FH part must be 1/T-exponent-class; the measured 1/log T then isolates the
arithmetic part — consistent with B24's 1/√log T at a coarser scale).
**Cheapest probe:** compute the FH exponent for the cosine-window symbol (standard formula), then compare
with the [AF] data.

---

## Pool 6 — Signal processing / frames: wavelet packets of the Weil form, compressed sensing, phase retrieval

### P6.1 Tight wavelet-packet frames in place of the Gabor system — NEW (likely-dead, overlaps [CD-V18])
**Idea:** The certificate's Poisson-completion identity (Claim 2.1: Σ_k v_k v_k* = (N/T)·φ²-window) is the
*tight-frame* property of the Gabor system at critical density. A *multiresolution* (wavelet-packet) basis
of the same test-function space would give a *different* tight frame, with the frame bound entering the
rank–trace. The honest problem: the *exactness* of Claim 2.1 is load-bearing (tr and ‖·‖² are evaluated
against the exact identity); any approximate-frame error of size ε costs ε·N in the trace — and the
in-class gap is 1.4% of N, so ε must be < 1e-3. Tight wavelet frames have exactly bounded errors but
*multiscale* structure — the trace evaluation would mix scales, and the *prime-side* evaluation (the
explicit formula at each scale) picks up *different* error terms per scale — likely killing the constant.
**Analogy:** Gabor frames (critical density) ↔ wavelet tight frames; the frame bound ↔ the identity's
error.
**Needs:** a wavelet-packet version of Lemma 3.2/3.3 with uniform error control — a real analytic paper.
**Feasibility:** Low (likely dead — the exact identity is the load-bearing wall; cf. the [AK] bandwidth
analysis: every c > 1/2 window that numerically improves breaks Claim 2.1; wavelet frames have the same
support-sum issue at the boundary).
**Cheapest probe:** numerically build a two-scale tight-frame compression of the *ideal* model (T ~ 200)
and check the trace error against N; if the error is > 1e-3·N, kill (expected).
**Cheapest-probe verdict:** document as KNOWN-DEAD-likely after the probe.

### P6.2 Compressed sensing: the ceiling as a restricted-isometry/undersampling bound — NEW (strategic)
**Idea:** The explicit formula is a *linear measurement* of the zero measure: Σ_ρ F̂(γ_ρ) = RHS(primes).
Compressed sensing recovers a sparse signal from few linear measurements when the sensing matrix has
restricted-isometry properties; the off-line structure is "sparse" (we want to prove it is small). The
dimension cap (Prop 7.4: a λ-bandwidth window gives at most λN independent measurements) *is* the
undersampling bound: with λN < N measurements you cannot *recover* a configuration of size N — the ceiling
law is the "aliased" configuration that the undersampled system cannot distinguish from reality. NEW:
state the ceiling in CS language (the certificates = the recovery guarantees; the 256-law = the
aliasing/stability-barrier example; the missing input = *more measurements* = beyond-1 F — the same wall).
**Analogy:** undersampled recovery / aliasing ↔ bandwidth-one compression; RIP ↔ the stability inequality.
**Needs:** none (framing). Value: strategic clarity — *any* certificate class reading ≤ λN independent
bandwidth-one measurements *must* hit an aliasing obstruction; the only exits are more measurements
(beyond-1) or *priors* (repulsion, P1.4). Strong honest statement.
**Cheapest probe:** none (documentation).

### P6.3 Uncertainty-principle / annihilating-pairs local bounds — KNOWN-OPEN (framing, overlaps [CD-A3])
**Idea:** Paley–Wiener (the band-limit) is the uncertainty principle in the explicit formula: zeros
(frequency) vs primes (time). Local uncertainty (Donoho–Stark-type: concentration of the zero measure in
an interval forces prime-side concentration) would give *local* constraints — but the classical
small-support positivity [CD-A3] is the only such statement, and it lives below the first zero (no overlap
with the bandwidth-one regime). The honest verdict: the local-uncertainty route is KNOWN-OPEN with the same
wall ([CD-A3]).
**Analogy:** local uncertainty ↔ local zero bounds.
**Needs:** a local-uncertainty statement at scale ~1/log T (unknown — likely as hard as the mean).
**Feasibility:** Low. Value: none beyond [CD-A3]'s documented death.
**Cheapest probe:** none (already documented dead; do not re-fund).

### P6.4 Phase retrieval: the ceiling law is a phase-retrieval twin of reality — NEW (strategic)
**Idea:** The certificate reads *intensity-like* data: tr (the total), ‖·‖² (the intensity of the
compressed form). Phase retrieval is the science of "intensity-only measurements cannot distinguish
configurations that differ in phase"; the 256-law and the real configuration are *phase-retrieval twins*
at bandwidth one (identical intensities: same mean, same ‖·‖², same marks budget). The NEW framing: the
missing input (beyond-1 F) is precisely the *phase* information; the ceiling theorem is a *phase-retrieval
impossibility* theorem for the certificate class. Consequence: any new input must carry *phase*
(beyond-1 correlations, third moments — which ARE phase-sensitive — vs the intensity-only two moments).
**Analogy:** phase retrieval ambiguity ↔ the extremal twin; intensity ↔ (tr, ‖·‖²).
**Needs:** none (framing). Value: explains *why* third moments (phase-sensitive) are the natural next input
and *why* intensity-style statistics (variance, entropy) cannot move the wall — a guide for P2.
**Cheapest probe:** none (documentation).

### P6.5 Two-bandwidth joint certificate: λ = 1 (two moments) + λ = 1/2 (three moments) for the DISTINCT count — NEW (P2, overlaps [CD-V3])
**Idea:** §7.5(e) proves odd moments don't lower Λ₁(0) for the *on-line* functional at λ ∈ (1/2, 1), and
Prop 7.4 makes λ ≤ 1/2 useless *for the on-line bound*. But the *distinct* (c = 3) functional is a
different object, and the unconditional third moment exists at λ < 2/3 (RS range kλ < 2). NEW: run *two
windows on the same configuration* — window A at λ = 1 (optimal constant, tr and ‖·‖²) and window B at
λ = 1/2 (tr Â³ unconditionally evaluable, kλ = 3·(1/2) = 1.5 < 2 with margin) — and price *both* into the
distinct-count bookkeeping. The λ = 1/2 window alone gives (3 − C(1/2))/2 = (3 − 13/6)/2 = 5/12 (useless),
but the *joint* constraint set (A's two moments + B's third moment + integrality, all on the same
configuration) is strictly richer than either alone. This is the concrete attack on P2 that I have not seen
in our notes ([CD-V3] runs a *single* window at λ = 2/3(1−ε); the *two-window* combination is new).
**Analogy:** multi-window/frame compression (oversampling gives more constraints); joint spectral data from
two resolutions.
**Needs:** (i) the unconditional tr Â³ evaluation at λ = 1/2 (diagonal method, RS range — mechanical from
the §5 machinery); (ii) the joint (tr, ‖·‖², tr Â³, integrality, n₊) LP for N_d; (iii) numeric LP solve.
**Feasibility:** Med — the most promising P2 route I generated: it uses *proven inputs only* and targets
the *distinct* functional that §7.5(e)'s "odd moments don't help" claim does NOT cover.
**Cheapest probe:** the joint LP (symbolic/numeric) with m₃ = 2 (GUE value): does N_d beat 5/6? If the LP
is degenerate (the c = 3 inequalities saturate at 5/6 regardless), clean negative — document.

---

## Pool 7 — Numerical analysis: oscillatory quadrature, spline/isogeometric windows, exponential integrators

### P7.1 Sharpen the Montgomery–Vaughan constant 3π/2 for the specific window kernel — NEW (P1, overlaps [CD-V1] input)
**Idea:** The off-diagonal prime-sum bound uses MV's generalized Hilbert inequality with the universal
constant 3π/2 (C Lemma 5.2). Hilbert-type inequalities have *best constants* depending on the kernel; the
specific kernel here (the window's Fourier pair g) is fixed and smooth. NEW: numerically compute the *best
constant* for the MV inequality restricted to the actual g-weighted frequencies, and check whether it is
< 3π/2. If yes, the in-class constant 0.6725 moves *with proven inputs only* (the same class — the
constant is not part of the ceiling's input set, which only fixes the *configuration* data; the *inequality
constant* is a free parameter of the method!). Note: the ceiling theorem [AC] is about certificates reading
the *configuration* data; the *analytic constants* (MV constant, Stirling error, Chebyshev error) are
separate — improving them improves the certificate *for all configurations*, which the ceiling law does not
forbid (the ceiling law is about the best certificate *given* the class, and the class includes the
constants).
**Analogy:** best constants in Hilbert-type inequalities (the classical literature: Hardy–Littlewood–
Pólya, Wilf) ↔ the sharp MV constant for a given kernel.
**Needs:** (i) the exact statement of C Lemma 5.2's constant (in Lean, `Zeta23/MV`); (ii) a numeric
eigenvalue computation of the corresponding Hilbert matrix with the g-kernel; (iii) a proof of the improved
constant (matrix positivity, [the "best constant" machinery]).
**Feasibility:** Med. Value: a *proven-input* constant push — the only kind that survives [AC]; even a
0.1% gain is real.
**Cheapest probe:** mpmath: finite Hilbert-matrix eigenvalue for the g-kernel at N = 10³; compare the
spectral norm with 3π/2.

### P7.2 (reserved — see P7.1, P7.3, P7.5; exponential-integrator angle below)
**Idea (brief):** exponential-integrator / stiff-decay technology is about *evaluating* oscillatory
semigroups; the only relevant use here is the *numerical* evaluation of the finite-T sums (the ΛΛ·g sum is
a stiff oscillatory sum). Fold into P7.1's numerics; not a research vector on its own.
**Cheapest probe:** none.

### P7.3 Spline (isogeometric) windows: rational certificates and exact ξ′-optimizer search — NEW (P5, overlaps [CD-V8])
**Idea:** The flat window is a degree-0 B-spline; the cosine is not a spline. The *optimal* window in a
fixed spline space solves a *finite* E–L system (the |u−v| kernel against a B-spline basis has *explicit*
inner products — all rational/quadrature-exact), giving *rational* windows with provable bounds *near* the
cosine. Value: (i) Lean-friendly certificates (rational data, like the 256-law) rather than transcendental
windows; (ii) the *exact* optimal spline for the ξ′-functional — the paper's quartic is ad hoc [CD-V8];
the spline E–L solve finds the true optimizer in the polynomial space and may beat 0.86864.
**Analogy:** isogeometric analysis (B-spline/NURBS bases) ↔ spline windows; finite-element E–L solves ↔
rational certificate windows.
**Needs:** (i) the ξ′ functional in explicit form (Lean XiPrime files); (ii) the B-spline E–L solve
(numeric, then rational); (iii) a certificate re-verification.
**Feasibility:** Low–Med. Value: a concrete, checkable improvement path for P5 and Lean-friendlier
certificates for P1.
**Cheapest probe:** mpmath: optimal degree-3/4 spline for the ξ′ functional; compare the quotient with the
paper's quartic (0.86864).

### P7.4 (folded: the discrete variational problem of P5.1)
See P5.1 (equilibrium measure) and P4.1 (thermodynamic limit). The numeric LP solve is the shared engine.

### P7.5 Quadrature-exact refinement of the ceiling's stability inequality — NEW (overlaps [CD-V2], [AC])
**Idea:** The ceiling bound carries the term 2.54e-6·(|r′(1)| + ∫₀¹|r″|) [AC] — the *quadrature cost* of a
C¹ certificate. Certificates with *smaller* ∫|r″| (e.g., piecewise-linear with few knots, or polynomials
with small second-derivative norm) have *smaller* ceiling slack — the gap between the LP value 0.6818287
and what a certificate can actually certify is governed by this quadrature term. NEW: solve for the
*optimal low-curvature certificate* (minimize |r′(1)| + ∫|r″| subject to the stability constraints) —
interval-arithmetic in Rust, then Lean — closing part of the 0.6725 → 0.6818 gap with *explicitly bounded*
(rather than certified-by-enclosure) error.
**Analogy:** quadrature/approximation theory: optimal recovery with a smoothness penalty; Chebyshev
alternation.
**Needs:** the LP dual (P5.1) + an optimization over r with a ∫|r″| budget.
**Feasibility:** Med. Value: a real in-class constant push with provable bounds, independent of any new
arithmetic.
**Cheapest probe:** greedy/alternation search for r with bounded ∫|r″|; report the certified value vs
0.6725.

### P7.6 Chebyshev alternation identifies the optimal certificate — NEW (unifies P5.1, P7.5)
**Idea:** In extremal-problem theory (kissing numbers, the one-delta problem behind Theorem D [AK] via
CCLM17), optimal certificates satisfy *alternation* conditions — the constraint set touches the envelope at
alternating points. The class-optimal certificate r*(x) should satisfy a Chebyshev-type alternation on the
*contact set* of the equilibrium problem (P5.1). NEW: *guess* r* from the alternation conditions (the
contact set from the 256-law's active constraints), verify it exactly (rational/polynomial), Lean-check it.
This is the systematic way to *discover* the 0.6818-achieving certificate rather than search numerically.
**Analogy:** Chebyshev alternation ↔ optimal majorant certificates (the classical "extremal problem with
kernel |u−v|" literature — the same family as the one-delta problem).
**Needs:** the active-set structure of the 256-law LP (from the dual variables, P5.1).
**Feasibility:** Med. Value: the exact in-class certificate (same prize as P5.1/P5.4).
**Cheapest probe:** read off the dual variables of the [AC] LP; identify the active constraints (contact
set); test the alternation sign pattern numerically.

---

## Pool 8 — Spectral theory / Schrödinger: inverse spectral problems, de Branges / Burnol (cited honestly)

### P8.1 Inverse spectral problem: the operator whose spectrum has the zeros' moments — NEW (overlaps [CD-W3], [CD-W5])
**Idea:** The moment sequence m₁ = 1, m₂ = 4/3, m₃ = 2, m₄ = 13/4 (GUE values) is the moment sequence of a
measure on ℝ; by the Hamburger moment problem the *canonical* (Nevanlinna-extremal) measures with these
moments are *atomic* — the extremal configurations of the certificate *are* principal representations of
the moment problem. NEW: the inverse-spectral statement — *every* configuration consistent with the
two-moment data is a *principal representation of a (two-moment) moment problem*, and the certificate is a
*functional of the principal representation*. This identifies the "operator whose discrete spectrum has the
same two moments as the zeros" — it is the *Nevanlinna operator* of the moment problem; its free parameter
(the Nevanlinna function) is exactly the missing constraint of P1.
**Analogy:** inverse spectral theory (Krein/de Branges parametrization of all measures with given
moments) ↔ the certificate's admissible configurations.
**Needs:** the Nevanlinna parametrization for the (m₁, m₂) problem with integer masses — explicit
rational function computation.
**Feasibility:** Med. Value: a *clean reframe of P1*: "the missing constraint is a bound on the
Nevanlinna parameter function," and the two principal representations are computable — if any *proven*
positivity (e.g., the tr Â³ Hankel when it becomes unconditional at λ < 2/3) pins the Nevanlinna function,
the wall moves.
**Cheapest probe:** compute the two principal representations of the (1, 4/3) moment problem with integer
masses on the grid; check which one is the 256-law and which is excluded by any *provable* third-moment
inequality.

### P8.2 Burnol / scattering: the zeros as resonances; (1,1)-planes as S-matrix unitarity — KNOWN-OPEN (overlaps [CD-V16])
**Idea:** Burnol's framework presents the explicit formula as the spectral measure of a concrete unitary
map on L² (reported standard; [CD-V16] already flags the reformulation). The scattering/causality reading:
off-line pairs (ρ, 1−ρ̄) are *resonance pairs* of a 1D Schrödinger-type operator, and their (1,1)-plane
signature is *flux conservation* (S-matrix unitarity = the functional equation). NEW (physics-flavored
only): the Wigner *causality* constraints on S-matrix poles say resonances near the real axis come in
time-reversal pairs with *opposite* imaginary parts — which the FE already enforces; the *no-resonance*
statement (RH) is exactly "the S-matrix has no bound states." Honest verdict: the reformulation is KNOWN-
OPEN with no new provable fragment — the *finite* shadow is the paper's method renamed ([CD-V16]'s kill
criterion). Do not fund beyond the V16 check.
**Analogy:** scattering resonances ↔ off-line zeros; S-matrix unitarity ↔ the functional equation.
**Needs:** nothing new (V16's finite check).
**Feasibility:** Low (already scoped in [CD-V16]). Value: none beyond V16 — flagged to avoid re-derivation.
**Cheapest probe:** the [CD-V16] finite Hermite–Biehler shadow check (already specified).

### P8.3 Herglotz–Padé certificates for the derivative tower — NEW (diagnostic, overlaps [CD-V9], [CD-W3])
**Idea:** ξ^(j)/ξ^(j−1) is Herglotz-type iff ξ^(j) has only real zeros (standard: a real entire function
with real zeros has Herglotz logarithmic derivative). The *Padé approximants* of a Herglotz function are
Herglotz iff the denominator's roots are real — a *finite* condition. NEW: from the first moments of the
ξ^(j)-zero set (Newton identities), form the [k/k] Padé of ξ^(j)/ξ^(j−1), and check the denominator's
root reality *numerically* as a *diagnostic* of how much moment data would be needed for a Herglotz–Padé
certificate. Honest limit: a finite Padé is a *necessary* condition only; without all moments it cannot be
sufficient (the same wall as the Hankel route [CD-W3]).
**Analogy:** Padé approximation of Stieltjes/Herglotz functions; Routh–Hurwitz-type reality certificates.
**Needs:** the moments of the ξ′-zero set (same input as P3.5); a Padé code.
**Feasibility:** Low (diagnostic). Value: tells us whether the derivative tower's moment route has any
*finite* stopping criterion at all.
**Cheapest probe:** mpmath: [2/2] and [3/3] Padé of the ξ′/ξ ratio from real zero data; print the
denominator roots.

### P8.4 (see P8.1 — the Nevanlinna parametrization is the key P1 reframe; no separate vector)

---

## Pool 9 — Random walks / branching: primes as a branching process; martingales; Girsanov; large deviations

### P9.1 Martingale structure of the certificate value: fluctuation control for the effective theorem — NEW (P6, overlaps [CD-V20])
**Idea:** The finite-T certificate value (the [AF] Δ(T) curve) is a function of *fluctuating* prime sums
whose *variance* is the Goldston–Montgomery-type variance (known); the *mean* is HL-strength ([CD-A1] —
mean is the wall), but the *fluctuations about the mean* are *provably Gaussian-ish* (Selberg-type CLT
inputs). NEW: split the effective-theorem error E(T) ([CD-V20]) into *mean error* (uncontrollable) and
*fluctuation error* (controllable by martingale/second-moment bounds), and prove a *weaker but genuine*
statement: "≥ 0.6725 for all T outside a set of density zero" (or with an explicit exceptional set) —
an almost-everywhere certificate. This is a *new target type* (measure-theoretic rather than
configuration-theoretic) that the fluctuation structure *can* support even though the pointwise mean
cannot.
**Analogy:** martingale concentration / almost-sure theorems ↔ certificate validity for most T.
**Needs:** (i) the variance of Δ(T) over T-windows (measure — cheap); (ii) a second-moment bound on the
prime sums at the certificate's sensitivity scale (Borel–Cantelli-style).
**Feasibility:** Med–High. Value: an honest *new* theorem (a.s.-type 67.25%) if the pointwise effective
version is out of reach; also quantifies P6's error terms.
**Cheapest probe:** [AF] code extended: var(Δ(T)) over adjacent windows at fixed T; report the
fluctuation scaling (1/T? 1/log T?).

### P9.2 The zero-counting process as a sine-kernel Gaussian process: entropy of the slack — NEW (diagnostic, P6)
**Idea:** The normalized zero-counting process over dyadic boxes is (conjecturally, and at leading order)
a Gaussian process with the sine-kernel covariance (the pair correlation IS the covariance). The
certificate's measured slack Δ(T) is a *realization* of this process; its *entropy* (log-det of the
covariance) is *computable from the pair correlation alone* (which is the known F ≡ 1 on [0,1] + F ≥ 0).
NEW: quantify "how much of Δ(T) is fluctuation" by the process entropy, and predict the *scaling* of the
slack's *sample-to-sample* variance — a *variance prediction* for P6's error terms that the [AF] data can
test.
**Analogy:** Gaussian free field / local time ↔ zero counting; process entropy ↔ fluctuation budget.
**Needs:** the covariance model (from F) and a variance measurement (same probe as P9.1).
**Feasibility:** Low–Med (mostly analysis of existing data). Value: a *prediction* for the error-term
structure, testable immediately.
**Cheapest probe:** same as P9.1 (measure var(Δ(T)); compare with the sine-kernel covariance prediction).

### P9.3 Girsanov change of measure on off-line zeros — NEW (speculative, honest)
**Idea:** Model the off-line pairs as a *deformed measure* on configurations (the "off-line world" as an
absolutely continuous perturbation of the "on-line world"); the Girsanov density is exp(∫u dN − ...); the
certificate value is an *expectation under the deformed measure*. The honest transfer: the rank–trace
bound is a *relative-entropy-style* inequality (the free energy between the real configuration and the
crystal — see P4.2); Girsanov says the *KL divergence* between the worlds is the "cost" of the
deformation. But: the KL between the real zero configuration and the crystal is *not* bounded by any
proven input — so Girsanov contributes *no* new provable constraint. Verdict: NEW framing, no new input;
the only usable fragment is the *variance* language already in P9.1. Do not fund beyond P9.1.
**Analogy:** change of measure ↔ deforming the on-line world; KL ↔ certificate cost.
**Needs:** a provable entropy bound (does not exist).
**Feasibility:** Low. Value: none beyond P9.1 — documented to prevent re-derivation.
**Cheapest probe:** none (recorded as framing-only).

### P9.4 Large deviations: P2's third moment IS the skewness input — NEW (strategic, overlaps [CD-V3])
**Idea:** The B24 evaluation fixes the *second* moment of the pair-correlation sum at (4/3)N for *all*
configurations (on-line or not — that is the unconditional content). The distinct wall 5/6 is a
*mean-field* (second-moment) statement; beating it requires *skewness* — the third cumulant of the
zero-side fluctuation — which IS tr Â³ (the [CD-V3] input). Physics: in large-deviation theory, the
first correction to a Gaussian tail is the *third cumulant* (the Cramér series); P2 is literally the
"skewness correction to the certificate's large-deviation analysis." This reframes P2 as the natural
*next order* of a systematic expansion — and predicts that *fourth* moments (13/4) would be the *next*,
consistent with HL*(4,λ) → 13/18 [AM/§7.5(f)].
**Analogy:** Cramér/Edgeworth expansions ↔ the moment hierarchy of the certificate.
**Needs:** none (framing). Value: explains the hierarchy (2nd → 3rd → 4th moment ↔ 2/3 → ? → 13/18) and
shows P2 is the *cheapest* non-trivial next order.
**Cheapest probe:** none (documentation).

### P9.5 Branching process reading of the primes — KNOWN-OPEN (framing)
**Idea:** The multiplicative structure of the primes (each prime "spawns" its powers — the λ_T term is a
*cascade* weight) is a branching/cascade object; the honest content: the *diagonal* prime sums are the
"survivor" terms of the cascade, and the off-diagonal are the *correlations between branches*. The known
fact: the branch correlations at range X ≤ T are MV-bounded (the λ ≤ 1 wall); beyond, they are the HL
conjecture. Verdict: this is [CD-A1]/[CD-A5]'s death restated in cascade language — KNOWN-DEAD as a route,
useful only as mental imagery.
**Analogy:** multiplicative cascade ↔ the prime powers; branch correlation ↔ the off-diagonal.
**Needs:** none.
**Feasibility:** Low (dead). Value: prevent re-derivation.
**Cheapest probe:** none (already documented in [CD-A1], [CD-A5]).

---

## Pool 10 — Quantum information: entanglement spectra / negativity; Sylvester inertia as entanglement negativity

### P10.1 Negativity/purity tradeoffs from the QI literature vs Lemma 3.2/3.4 — NEW (P1 — the headline question)
**Idea:** The certificate's n₊(W_off) (positive index of the off-line part) is the *entanglement
negativity* of the zero-pairing "state" — each off-line pair is a (1,1)-plane, i.e., a *Bell pair* in the
language of the partial transpose. The QI literature contains *purity–negativity tradeoffs* and
*Schmidt-rank vs purity* inequalities that are sometimes *stronger* than the naive von Neumann trace
inequality for structured states. NEW: sweep that literature for inequalities of the form "given a PSD
block P with rank r and trace tr, and a complementary block Q with bounded positive index, ‖P + Q‖²_F ≥
…" and test *numerically* whether any known QI bound beats the paper's Lemma 3.2/3.4 constant *for the
specific (1,1)-plane block structure*. The honest prior: `lemmaR_tight` [AM] proves the *general* bound is
tight, so a win would have to come from the *special structure* (the v-vectors are Gabor vectors with
explicit inner products — see P10.4).
**Analogy:** entanglement negativity ↔ positive index; Bell pairs ↔ off-line (1,1)-planes; purity ↔
Frobenius norm; Schmidt rank ↔ rank.
**Needs:** (i) a targeted literature sweep (purity–negativity, Schmidt-number bounds); (ii) a numeric
check on the (1,1)-block structure.
**Feasibility:** Low (probe) → Med (if a candidate inequality appears). Value: the direct attack on P1's
"is the rank–trace inequality improvable *within the method's inputs*" — high EV if any strict
improvement survives.
**Cheapest probe:** linear-algebra sweep in mpmath: randomize p (1,1)-planes with the measured v-structure,
compute n₊, ‖·‖², tr, and test the *sharpest* QI-style bounds (Schmidt-number bounds, negativity-from-
purity inequalities) against the paper's constant; report any gap.

### P10.2 Entanglement entropy of the W_T spectrum as a third statistic — NEW (diagnostic)
**Idea:** Normalize W_T's eigenvalues to a probability vector and compute the von Neumann entropy
S = −Σ λᵢ log λᵢ. The crystal's law (2/3 at 1, 1/6 at 2, 1/6 at 0) has a fixed entropy; the real
configuration's entropy is *measurable* from the prime side. The certificate doesn't use S (it is not
provable from the two moments — max-entropy under (tr, ‖·‖²) is a *continuum* of laws). NEW: measure
S(W_T) over T and compare with the crystal's; if the real entropy is far, reality is spectrally distant
from the extremal law (motivating a search for a *provable* entropy-type input); if close, the extremal
law is spectrally indistinguishable (confirms the ceiling's robustness).
**Analogy:** entanglement entropy ↔ eigenvalue-law entropy; max-entropy inference ↔ the certificate class.
**Needs:** W_T spectra (exists).
**Feasibility:** Low (measure). Value: diagnostic for P1 (how much spectral slack reality has).
**Cheapest probe:** [AF]/[CD-V1] code: print S(W_T)/log N at T = 100…700 vs the crystal's H.

### P10.3 Schmidt-number / entangled-rank dual bounds — NEW (overlaps P10.1; the *dual* statement)
**Idea:** The certificate bounds the *on-line* rank from below (rank(W_on) ≥ …). The QI literature's
*Schmidt-number* inequalities bound, dually, how much "entangled rank" a state of given purity can carry
— an *upper* bound on the off-line (entangled) structure. NEW: test whether a Schmidt-number-type bound
gives an *upper* constraint on p (the number of off-line pairs) *stronger* than the certificate's own
c²·p bookkeeping, for the measured purity. Honest risk: `lemmaR_tight` [AM] shows the c²·p penalty is
achieved (tight) in the general case; the special v-structure is the only hope (P10.4).
**Analogy:** Schmidt number ↔ entangled pair count; purity ↔ ‖·‖².
**Needs:** the same literature sweep + numeric as P10.1.
**Feasibility:** Low–Med. Value: fold into P10.1 (one probe, two framings).
**Cheapest probe:** same as P10.1.

### P10.4 Cross-pair corrections to n₊(W_off) from the Gabor inner products — NEW (P1, concrete)
**Idea:** Lemma 3.1 gives n₊(W_off) ≤ p as an *upper* bound (a cost), and `lemmaR_tight` shows p is
achieved when the (1,1)-planes are *orthogonal*. The v-vectors are Gabor vectors with *explicit* inner
products: |⟨v_ρ, v_ρ′⟩| = |Ψ(s_ρ − s_ρ′)| (known formula, [AF]). If off-line pairs were *clustered*
(nearby heights ⇒ nearly parallel planes), the *joint* positive index of p planes would be < p
(subadditivity — the positive parts overlap), *lowering the cost* and raising the certificate. NEW:
compute, for synthetic off-line pairs at controlled separations, the joint n₊ of the block and measure the
subadditivity gap as a function of separation. The honest analysis: *worst-case* (far-apart) gives exactly
p, so no *unconditional* gain exists — but the *measurement* calibrates how much the p-bookkeeping
overcharges in clustered worlds, and if reality were ever shown to have *any* off-line pairs (it is not),
the certificate would improve. Diagnostic value: it tells us the certificate's slack against *partial*
off-line scenarios.
**Analogy:** monogamy of entanglement (CKW-type) ↔ subadditivity of the joint positive index; Bell-pair
overlap ↔ Gabor inner products.
**Needs:** the Ψ formula ([AF]) and a few synthetic pair configurations.
**Feasibility:** Low. Value: precise calibration of the p-cost term's slack; also tests whether "clustered
off-line pairs" could ever be *detected* by a subadditivity argument.
**Cheapest probe:** mpmath: two synthetic (1,1)-planes at separation s; compute n₊ of the sum vs 2, as a
function of s. If n₊ = 2 for all s > δ, the bookkeeping is exactly tight away from exact coincidence
(expected — document).

### P10.5 de Finetti / typicality for the family route (QI version of P4.4) — NEW (P4, overlaps P4.4, [CD-V12])
**Idea:** The family-averaged W_T (characters χ mod q) is the *symmetrized* ("de Finetti") state of the
ensemble; the per-character certificate is the *product* state. de Finetti bounds the *distance* between
the symmetrized average and the product state in terms of the *exchangeability* — for the character family,
the relevant distance is controlled by the *4-character* correlation (the variance of P4.4). NEW: state the
P4 concentration theorem as a *finite de Finetti bound*: the per-character certificate deviates from the
family average by at most (4-character variance)^{1/2} — a clean, quotable structure with a specific
analytic target (the 4-character sum).
**Analogy:** quantum de Finetti / typicality ↔ family averaging; exchangeability ↔ character orthogonality.
**Needs:** the 4-character sum evaluation (new analytic work); the numeric variance (P4.4's probe).
**Feasibility:** Med (probe cheap; theorem hard). Value: the same as P4.4 with a principled QI framing —
one probe, two framings.
**Cheapest probe:** P4.4's variance measurement.

---

## TOP 10 (EV × feasibility × cheap-probe)

1. **P6.5 — Two-bandwidth joint certificate (λ=1 two moments + λ=1/2 third moment) for the distinct count.**
   The only P2 route I generated that uses *proven inputs only* and targets the *distinct* functional that
   §7.5(e)'s "odd moments don't lower Λ₁(0)" claim does not cover. Probe: joint LP with m₃ = 2 — hours.
2. **P10.1/P10.3 — QI inequality sweep against Lemma 3.2/3.4 (purity–negativity / Schmidt-number bounds).**
   Direct P1 attack on the rank–trace inequality itself; the literature may contain a strictly stronger
   bound for the (1,1)-block structure. Probe: linear-algebra sweep — under an hour.
3. **P8.1 — Nevanlinna parametrization reframe of P1.** The missing constraint = a bound on the Nevanlinna
   parameter function; the two principal representations are computable now. Probe: principal
   representations of (1, 4/3) with integer masses — under an hour.
4. **P4.1 — Marked-configuration LP in the thermodynamic limit (N = 512/1024).** Adversarial validation or
   improvement of the 0.6818 ceiling; the cleanest cheap check of whether the ceiling law is an artifact.
   Probe: exact-rational LP at N = 512.
5. **P2.1/P5.3 — W_T-level spectral form factor and compression-ensemble null model.** The P3 diagnostic:
   how close reality's *compressed* spectrum is to RMT, and whether any exact beyond-1 identity exists at
   finite T. Probe: [AF] code extended — hours.
6. **P7.1 — Sharpen the MV constant 3π/2 for the window kernel.** A proven-input in-class push that the
   ceiling theorem does not constrain. Probe: Hilbert-matrix spectral norm for the g-kernel.
7. **P4.4/P10.5 — Family concentration (variance of the HS norm across χ mod q).** The quantified P4 target;
   physics prior (self-averaging, P2.3) says it should hold. Probe: variance across 100+ characters —
   hours.
8. **P5.5 — Fisher–Hartwig prediction of the finite-T deficit exponent.** Decomposes P6's error into
   kernel-artifact vs arithmetic parts; a checkable physics prediction against [AF] data. Probe: FH
   exponent + [AF] fit — under an hour.
9. **P7.3 — Optimal spline window for the ξ′ functional (and rational ζ-certificates).** A concrete P5
   improvement path (the paper's quartic is ad hoc) plus Lean-friendlier windows. Probe: spline E–L solve —
   under an hour.
10. **P3.4 — Christoffel function of the HL*-moment measure priced into the distinct wall.** The sharpest
    concrete form of the P2 third-moment question; a clean negative or positive in a day. Probe: 3×3
    Hankel Christoffel test against the crystal's masses.

**Strategic reading:** P6.5, P10.1, P8.1 are the only *P1/P2*-relevant vectors with proven-input
feasibility; P7.1 is the sleeper (a constant-improvement route the ceiling doesn't cover); P4.1 and P7.5
are the cheap ceiling validations; the diagnostics (P2.1, P5.3, P10.2, P4.3, P9.1/P9.2) change what we
believe about the method's real slack before any expensive funding; P4.4/P10.5 is the quantified P4
program. Nothing here claims to settle RH — the honest output is a ranked set of probes whose negatives are
documented findings.

---

## WILD section (deliberately absurd; honestly evaluated; each labeled)

### W-P1. "RH is the statement that the zero-pairing channel is entanglement-breaking; the certificate is the PPT bound; the 67.25% is the Werner bound" — CONJECTURED (likely equivalent-formulation)
**For:** W_T is the Choi matrix of a "zero channel"; PPT ⟺ W_T ⪰ 0 ⟺ RH; the certificate's n₊ is the
negativity; the rank–trace is the standard "bound on entangled dimensions given purity" — the QI machinery
is *exactly* the certificate's linear algebra, so the full weight of the negativity literature applies.
**Against:** the equivalence is by construction — the "channel" is W_T renamed; no *new* positivity input
emerges; the QI theorems reduce to Lemma 3.2-type statements. This is [CD-W4]'s "reformulation = no free
lunch" in QI clothing.
**Novel fragment worth keeping:** the *negativity as a quantifier of how far a configuration is from RH* —
a single number n₋(W_T) computable from the prime side that is *exactly zero iff* all zeros are on the
line (finite-T version). Even though it cannot be proven zero, its *measured* size is the cleanest single
"RH-ometer". (This is the [CD-V1] spectrum experiment, relabeled.)

### W-P2. "The zeros are a free Fermi gas: the sine-kernel process IS free fermions, so the exact finite-rank third moment is a Slater determinant — use it" — CONJECTURED (identification), formulas standard
**For:** the β = 2 sine-kernel process is *exactly* the position process of free fermions in a box (the
classical equivalence, standard); the n-point functions are Slater determinants *at finite N* — so the
*finite-rank* third moment tr Â³ has an *exact closed form* (a 3×3 Slater determinant), not just the
asymptotic RS value. If ζ's zeros matched the free-fermion process at finite T, tr Â³/N at finite T would
be *predictable exactly* — a sharp numerical test of the P2 input *before* the analytic evaluation.
**Against:** the identification is conjectural (it IS RH + the pair-correlation conjecture); the exact
Slater value is the *target* the primes must reproduce, not an input — testing it against real zeros is a
diagnostic (cheap, valuable), not a proof.
**Honest verdict:** the diagnostic is worth running (it prices P2's expected value numerically); the
"proof" part is the same wall.

### W-P3. "The zeros form a quantum error-correcting code; RH is the code achieving the quantum Singleton bound; the certificate is the Hamming bound" — CONJECTURED (likely-false as input)
**For:** the rank–trace inequality is structurally a *sphere-packing/Hamming-type* bound (rank vs purity);
the "code distance" is the minimal gap; beating 2/3 = a better code bound; the LP dual [CD-V2] is the
"linear programming bound" (the Delsarte/Plotkin machinery — literally the same LP family as the kissing
number).
**Against:** no *new* inequality appears — the QEC bounds are re-derivations of rank–trace-type statements;
the analogy adds vocabulary, not theorems. The one genuinely transferable fragment: the *LP bound*
machinery of coding theory (Delsarte) is *already* the certificate LP — confirming that the in-class route
(V2) is the right one and that *no* quantum-information inequality outside the LP family is likely to beat
it. That is a *negative* finding worth recording.

### W-P4. "Floquet/Hilbert–Pólya at stroboscopic times: the integer-α SFF is the moment sequence; find the exact unitary" — CONJECTURED (overlaps [CD-W5]; likely-dead)
**For:** the SFF at *integer* α is the power sums Σ_ρ e^{iαγ}-type — the *trace moments* tr Â^k of the
compressed form — which ARE the [CD-V3]/HL* input; a Floquet operator whose stroboscopic response is the
zero form factor would give the plateau *exactly* (per-instance unitarity, P2.1).
**Against:** this is Hilbert–Pólya renamed (the "phantom unitary" [CD-W5]); no construction is known; the
exactness at the eigenvalue level is as hard as RH. The *useful* fragment: the integer-α SFF *is*
computable from the prime side (P2.1's probe) — measure it; if it shows the plateau (F ≈ 1 for integer
α > 1) numerically, reality is consistent with a unitary-like mechanism — a diagnostic prior, nothing more.

### W-P5. "The 1/log T deficit is a Kondo-like RG flow: 0.6725 is the one-loop certificate; P2's third moment is the two-loop term" — CONJECTURED (framing; the content is real)
**For:** the finite-T data ([AF]'s Δ(T) curve) IS a renormalization-group flow of the certificate coupling
as a function of scale T; the *sign* of the flow (Δ > 0, decreasing) is measurable and extrapolatable; the
moment hierarchy (m₂, m₃, m₄ ↔ 2/3, ?, 13/18) is a *loop expansion* of the certificate — P2 is literally
the "next order". The physics vocabulary gives a *prediction*: the two-loop (third-moment) term has the
*opposite sign* of the one-loop (second-moment) term's correction — i.e., tr Â³ *raises* the distinct
bound (consistent with the general expectation that more moments → closer to 1).
**Against:** RG is an analogy; the "beta function" is a fit to ten data points; the sign prediction is
heuristic. But the *content* (third moment as the natural next order) is already P2 — this wild vector's
value is the *sign prediction* to check in the [CD-V3]/P6.5 LP: if the third moment *lowers* the distinct
bound, the analogy is false and we learn something.
**Honest verdict:** the sign check is a free by-product of the P6.5 probe — run it.

### W-P6. "Monogamy of zeros: an off-line pair 'uses up' entanglement; two off-line pairs cannot both be maximally entangled with the on-line system — prove subadditivity of n₊" — CONJECTURED (likely-false as an unconditional input)
**For:** P10.4's probe: for *clustered* pairs the joint positive index is < p — a real effect at finite
separation.
**Against:** the certificate must hold for *all* configurations; the worst case (orthogonal planes) is
exactly p; no *constraint* forces clustering, so no unconditional gain. The effect is real but
unexploitable without a clustering input (which would be a repulsion-type input, P1.4 — KNOWN-OPEN).
**Honest verdict:** the probe (P10.4) is worth running once to *quantify* the effect; the route as an
unconditional certificate input is closed.

---

## Label inventory

- **NEW** (invented here, untested): P1.1, P1.3, P1.5, P1.6, P2.1, P2.2, P2.3, P2.5, P3.1, P3.2, P3.3,
  P3.4, P3.5, P4.1, P4.3, P4.4, P4.5, P5.1, P5.2, P5.3, P5.4, P5.5, P6.1, P6.2, P6.4, P6.5, P7.1, P7.3,
  P7.5, P7.6, P8.1, P8.3, P9.1, P9.2, P9.4, P10.1, P10.2, P10.3, P10.4, P10.5, W-P1 … W-P6 (conjectured
  by construction).
- **KNOWN-OPEN** (core is open / already flagged in our notes; new physics framing only): P1.4 (repulsion;
  [CD-V17]), P2.4 (CUE exactness), P8.2 (Burnol; [CD-V16]), P6.3 ([CD-A3]), P9.5 ([CD-A1]/[CD-A5]),
  P3.2's integrable-zeros folklore (heuristic; sources not held).
- **KNOWN-DEAD** (framing-only, or documented in [CD-A#]): P9.3 (no provable entropy input), P9.5
  (cascade restatement of A1/A5), P2.2/P2.4 as *input* routes (plateau unreachable without a unitary
  realization), P6.3.
- **TESTED-OPEN**: P1.2 (extends [AF]'s measured Δ(T) > 0, ~1/log T — the trend, not the asymptote, is
  open); the diagnostics are all "probe-now" states.
- **Cheapest-probe discipline:** every vector above has a <1h probe (numeric via existing tools/finitet or
  [CD-V1] machinery, or a targeted literature sweep). Nothing here requires new heavy compute to *start*.

**Honest closing note:** the physics angle's two strongest NEW contributions are (i) the two-bandwidth
joint certificate (P6.5) — a proven-input attack on P2 that §7.5(e) does not obviously block, and (ii) the
QI inequality sweep (P10.1) — a direct probe of whether Lemma 3.2/3.4 is improvable within its inputs.
The rest of the catalog is dominated by *diagnostics and framings* (they change what we believe and stop
re-derivation) plus *exact-in-class* routes (P5.1/P5.4/P7.6) that all reduce to solving the LP dual —
the same object [CD-V2] identified. The persistent wall — beyond-1 form factor, third moments, repulsion —
remains the only route to constants ≥ 0.70, and the physics picture (P2.4, P6.4, W-P4) explains *why*:
those inputs are *phase* information, the plateau/coherence region, exactly what a two-moment intensity
certificate cannot see.
