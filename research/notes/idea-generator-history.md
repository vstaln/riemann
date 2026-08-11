# Idea Generator: how PROVEN-TIGHT walls have been broken in the history of mathematics

**Agent:** IDEA GENERATOR (meta-strategic; historical-lesson-extraction + analogy-domain-transfer + brainstorm + epistemology).
**Round:** 2. **Purpose:** mine the history of mathematics for the *method transitions* that broke walls that
looked proven-tight — not for sharper results inside a class. Convert each into concrete candidate moves for
the Riemann program's walls.
**Honesty protocol (hooks/agents.md + task brief):** all historical narrative claims are
**TEXTBOOK-LEVEL / UNVERIFIED-FROM-HELD-SOURCES** — we hold no function-field, spectral-geometry, topology,
FLT, or LP-history papers in `research/papers/`. The *structural lessons* are the point, and every mapping to
*our* walls is grounded in the held notes read this session: attack-lpdual.md, attack-ceiling.md, attack-m29.md,
attack-gm-variance.md, attack-sandbox.md, attack-cvs-import.md, attack-lfunctions.md, attack-twoform.md,
attack-ihara-sandbox.md, idea-generator-crossdomain.md, idea-generator-literature.md, idea-generator-physics.md
(P2.1, V13), idea-generator-earth.md (E5.4), attack-vector-catalog.md (V17, V2–V20, L1–L9).
**Vector labels:** NEW (invented here, untested) / KNOWN-DEAD (death documented in held notes) /
KNOWN-OPEN (documented open in held notes) / TESTED-OPEN (existing probe, tested, asymptote open).
Every vector gets a 1-line cheapest-first probe.

---

## 0. The walls, restated precisely (so every historical lesson has a target)

From the held notes (all PROVEN-in-Lean or CHECKED-NUMERICALLY as cited):
- The 0.6818 ceiling (`ceiling_law256_signed`, Lean) bounds the (c₀, r) certificate class — value
  v = c₀ + ∫₀¹ r(x)x dx, valid iff c₀ + Σ sⱼr(j/N) ≤ p₁ — reading exactly: mean density, form factor on
  bandwidth one, integrality of multiplicities, block structure. (attack-ceiling §1)
- The in-class optimum is **attained** at v* = p₀ + |E(1)| = 0.68183123 (LP, HiGHS; shadow price of p₁ = 1:
  the ONLY datum that moves v is the certified simple fraction p₁). (attack-lpdual §3–5)
- Beyond-bandwidth-1 mean input: **DEAD** (M29: MV Hilbert inequality exceeds the tolerance by 3.6·10³–3.7·10⁴×).
- Beyond-bandwidth-1 variance input: **DEAD** (attack-gm-variance: dictionary inverted, no unconditional
  statement reaches α > 1 with content, orthogonal to the certificate's mean-read).
- Even RH does not move the ceiling (attack-cvs-import B3: RH supplies only F ≡ 1 on [0,1], which the
  near-CUE law already encodes).
- The sandbox reading: the certificate is a **repulsion certificate** — value = 2 − HS²/N, the HS constant is
  the pair-correlation arithmetic; real world reads 0.6725 (asymptotic), lattice 0.977, Poisson ≈ −0.02.
  Deficit = arithmetic, not structural lossiness. (attack-sandbox §4; attack-ihara-sandbox: the certificate
  takes values −22.9…+0.98 across RH-true objects, pinned by pair structure, not RH.)
- The one proven *beyond-two-moment* input in the verified corpus: the **λ < 2/3 triple correlation**
  (Rudnick–Sarnak / Hejhal; paper §7.5(e) — useless for the n₊-functional, unevaluated for the distinct
  count / for excluding the extremal law). (attack-ceiling §3; crossdomain V3; catalog V3/V4.)

**The frame for every historical case below:** our walls are *class-optimality* statements (the certificate
class is tight, the data is exhausted in-class). History's consistent meta-pattern: tight-looking class limits
are broken by **a new object**, **a transfer to a world with more structure**, or **a dynamical/family view** —
rarely by a sharper inequality inside the class. Each pool below extracts one such transition and maps it.

---

## 1. Pool 1 — Weil conjectures over function fields: new OBJECT, not sharper inequality

**Case (TEXTBOOK-LEVEL / UNVERIFIED-FROM-HELD-SOURCES):** Weil's 1949 conjectures (rationality, functional
equation, Betti numbers, RH for |α| = q^{w/2} — the "weights"). For curves Weil proved RH himself (~1948) by
**canonical polarization**: RH ⟺ positivity of the intersection form on the Jacobian (Hodge-index). Dwork
(1960) proved rationality by **p-adic analysis** — a fragment tool that could not reach the weights.
Grothendieck (~1960s) built **ℓ-adic cohomology** — a new object: a finite-dimensional ℚ_ℓ-vector space with a
Frobenius endomorphism, making rationality/FE/Betti *formal*. Deligne (1974, 1980) proved the weights by a
**family/bootstrap** argument: RH for the generic fiber of a Lefschetz pencil (a curve — the known case)
propagates to all fibers via the weight filtration and the trace formula; algebraic-integrality of the
Frobenius eigenvalues turns bounds into exact weights.

**The structural lesson (the point, regardless of history verification):** three distinct transitions, each
adding what the previous framework *structurally lacked*: (i) a spectral realization of the zeros as
eigenvalues (Weil's framing), (ii) a geometric object with canonical positivity (Grothendieck — the 
polarization comes from geometry, not from moments), (iii) the reading of the *whole moment sequence through a
family* + integrality (Deligne). The crossdomain note (§3) already states our precise obstruction: the
number-field side has no canonical polarization; W_T is the finite-rank truncation of the would-be one, and
its 2/3 deficit *is* the missing Hodge structure. What the history adds is *which* moves were the ones that
actually broke walls — the object and the family — versus the Dwork move (fragment tool: rationality only).

### Vectors
- **H1.1 — The Deligne bootstrap for the moment sequence (NEW framing; overlap V12, KNOWN-OPEN assembly).**
  Deligne did not need the moments of a single object — he used the *family* to compute what is uncomputable
  per-object. Our analog: the family average (Dirichlet χ mod q) restores bandwidth 1 by orthogonality — the
  family-averaged *higher* moments are the Deligne "weights". Overlaps V12 (FUNDED-NEXT) and P2.3
  (quantum-ergodicity framing). **Probe:** the V12 numerical probe — family-averaged HS norm at fixed q,
  T = (log q)^c; does orthogonality kill the off-diagonal and restore the bandwidth-1 constant?
- **H1.2 — Weight-reading of W_T's full spectrum (NEW; probe; overlap V1, TESTED-OPEN).** Deligne read the
  *full* eigenvalue data (all power sums) against integrality, not just two moments. Our W_T's full spectrum
  is prime-side computable (V1); the 256-law is *explicit*, so its W_T spectrum is computable too. The new
  question: does the real spectrum *separate* from the law's spectrum in any proven structural way
  (multiplicities, gaps, tail, min eigenvalue)? **Probe:** compute both spectra (Rust, from the real ordinates
  and from the law's explicit ordinates) and compare — a pure measurement.
- **H1.3 — Canonical-polarization hunt (NEW; overlap L3 de Branges, V17; KNOWN-OPEN).** The char-p engine was
  positivity *independent of arithmetic data*. Candidates for a canonical positivity in our world: the
  de Branges-space structure of the Weil completion (L3 — ordering theorems), the sine-kernel's reproducing
  kernel, Groskin's tail budget (L4-adjacent). **Probe:** a scoped inventory of which of these is both proven
  and configuration-free (cheap documentation deliverable).
- **H1.4 — The Dwork fragment push (KNOWN-DEAD; crossref §7.5(e), attack-ceiling §3).** Proving more moments
  in the Rudnick–Sarnak range is the fragment-tool move; the paper proves higher moments add nothing to the
  n₊-bound on (1/2,1). **Probe:** none — do not re-derive; cite.

---

## 2. Pool 2 — Selberg trace formula / compact hyperbolic surfaces: transfer to spectral geometry

**Case (TEXTBOOK-LEVEL / UNVERIFIED-FROM-HELD-SOURCES):** Selberg (1956) proved the RH-analog for the Selberg
zeta of a compact hyperbolic surface by the **trace formula**: an exact identity between the spectrum of the
Laplacian and the length spectrum of closed geodesics. The "RH" follows because the Laplacian is self-adjoint
with positive spectrum — the zeros of the Selberg zeta *are* the spectral side. The transfer from analytic
number theory to spectral geometry *was* the move; the identity (not an estimate) plus a canonical positive
operator does the work.

**The structural lesson:** (i) the trace formula is an *identity* whose spectral side has canonical positivity
(our explicit formula is the analog identity; our missing piece is the canonical operator — Hilbert–Pólya,
KNOWN-DEAD as a proof route); (ii) Selberg's power also came from *kernel selection*: choosing the point-pair
invariant so only short geodesics contribute — our bandwidth-one window is the same move, already
proven-optimal in-class (attack-kernel); (iii) the spectral side carries *structure* the length side doesn't
(Weyl law, heat-kernel trace, multiplicity from symmetry) — the transferable content for us.

Program-side ground truth: the certificate is a functional of the pair-correlation law
(attack-ihara-sandbox: values −22.9…+0.98 across RH-true objects; ζ sits at 0.6725 because of GUE/Montgomery
pair correlation). So "spectral-geometry transfer" must not be re-run as the dead individual-GL(2) transport
(attack-lfunctions: Λ* = 1/2, dimension ceiling, PROVEN).

### Vectors
- **H2.1 — Spectral-certificate scope check (NEW; diagnostic, expected negative).** The (c₀,r) ceiling
  theorem bounds the *value functional* c₀+∫rx over grid-mass data. A certificate reading the *full W_T
  spectrum* (a different functional) is not literally covered by the proven ceiling — but the W_T entries are
  bandwidth-one data (window autocorrelation support [−1,1]), and the law's spectrum is pinned up to the
  |E(1)| residual, so a spectral certificate against the law is heuristically capped at p₀ + O(|E(1)|) too.
  **Probe:** compute the law's W_T spectrum and verify that any rank–trace-type functional on it is capped at
  p₀ + |E(1)| — an adversarial scope-check of the ceiling (cheap; fold into H1.2's computation).
- **H2.2 — Resolvent/heat-kernel reading of W_T (NEW; probe; overlap V1).** The trace-formula spectral side
  has a generating function (heat-kernel trace, resolvent) with a *geometric* evaluation. For W_T: the
  resolvent trace tr((W_T − z)^{-1}) is the spectral density (V1's object) re-read as a Cauchy kernel — the
  question whether any *identity* (not estimate) survives at finite T (overlap P2.1's integer-α SFF). **Probe:**
  fold into V1's spectrum run; report the resolvent's imaginary part against the GUE density prediction.
- **H2.3 — The individual-transport anti-vector (KNOWN-DEAD; crossref attack-lfunctions §4).** Do not re-fund
  an individual GL(2)/surface zero-density transfer: dimension ceiling Λ* = 1/2, certificate empty. Cited,
  not re-derived.
- **H2.4 — Selberg-zeta certificate prediction (NEW; probe, Med).** The certificate value is *predicted* by the
  empirical form factor on [0,1]: 2 − (HS constant). For the Selberg zeros of a compact hyperbolic surface the
  pair correlation is conjecturally GUE (Rudnick–Sarnak for L-functions does not cover it), and *empirically*
  computable from the Laplacian spectrum. The prediction: if the surface's form factor on [0,1] ≈ 1, the
  certificate reads ≈ 0.6725 again — a clean cross-world confirmation of the "deficit = GUE pair-correlation
  arithmetic" reading (completing the sandbox's lattice 0.977 / Ramanujan 0.32–0.36 / ζ 0.6725 / Poisson −0.02
  picture with the spectral-geometric world). **Probe:** compute the low eigenvalues of one compact surface
  (numerical spectral method, Rust) OR — cheaper — test the *prediction mechanism* on the existing Ihara data
  (the certificate value from the empirical form factor alone). If prediction == measured on the Ihara worlds,
  the Selberg prediction is trusted without the heavy eigenvalue computation.

---

## 3. Pool 3 — Poincaré conjecture / Perelman: the flow makes the obstruction dynamical

**Case (TEXTBOOK-LEVEL / UNVERIFIED-FROM-HELD-SOURCES):** Poincaré's conjecture (1904); ~100 years of
topological approaches (Smale n≥5 1961; Freedman n=4 1982) could not reach n=3 — the obstruction is invisible
to static invariants. Hamilton's Ricci flow (1982) + Perelman's surgery analysis (2002–03) proved it (via
Thurston's geometrization): a *dynamical system* on the space of metrics whose singularities *are* the
obstruction; Perelman's monotone quantities (reduced volume, entropy) forced the flow to converge or blow up
in *classified* singularity models (round sphere / cylinder / cigar), and surgery removed them.

**The structural lesson:** static certificate optima are fixed points; the question is whether a *flow* makes
the obstruction visible as a singularity, and whether the singularity set is *small and classified*. Our walls
are static: the 256-law is an LP vertex (a corner of the admissible configuration polytope). The existing
probes: V7's sandbox (worlds), V13's Selberg-CLT/fluctuation exclusion (per-T death documented),
E5.4's conditioning (Hessian of the functional at the cosine), P9.1's a.e.-certificate (averaging over T).
Extend, don't duplicate.

### Vectors
- **H3.1 — Singularity classification: enumerate the extremal configurations (NEW; probe, cheap).** Perelman's
  move was classifying the singularity models — few, standard. Ours: classify the *vertices* of the
  marked-configuration LP (configurations matching the near-CUE rows) at small N. Are they all
  crystals/periodic-with-doubles? If the obstruction set is a small, classified family sharing a structural
  property (periodicity, doubles, near-determinism), then "exclude the class by a proven structural statement
  about ζ" becomes a well-posed (hard) target; if the vertex set is rich, the law is an accident of the LP and
  the wall is less structural. **Probe:** exact-rational LP vertex enumeration at N = 32/64 (regenerate-256law
  machinery exists; cheap).
- **H3.2 — The flow from the law to the real zeros (NEW; probe; overlap P9.1, E5.4; TESTED-OPEN flavor).**
  Interpolate configurations law → real zeros (both match bandwidth-one data); watch the certificate value and
  the simple fraction along the path. The law end has p₁ = p₀ and pins the certificate; the real end has
  p₁ ≈ 1 (empirically all simple). Perelman's question: is the wall a *corner* artifact (removable by a
  small perturbation toward reality) or *stable* along the whole path? Measurable: how fast the certificate
  value moves as p₁ is raised along the interpolation — the shadow-price-1 structure says 1:1, so the path is
  a straight price; the *diagnostic* content is whether any path-invariant (a quantity constant along all
  such interpolations) exists that the certificate could read. **Probe:** the LP with an interpolation
  parameter between the law's masses and the real zeros' empirical masses; report the certificate value curve.
- **H3.3 — Monotone-functional hunt (NEW, weak; WILD-adjacent).** Perelman's engine was a *monotone* quantity.
  Our certificate value is trivially monotone in p₁ (shadow price 1); a nontrivial monotone along any natural
  flow is not identified. **Probe:** none (documented) — kept only as a reminder that the missing piece is a
  monotone, not an estimate.
- **H3.4 — Fluctuation-shape exclusion, averaged over T (KNOWN-OPEN; overlap V13 + P9.1; TESTED-OPEN probe
  exists).** The crystal's count fluctuation is O(1); ζ's is √(log log T) (Selberg CLT, unconditional). V13
  documents the death of the *per-T* certificate; the flow-over-T version (a.e.-certificate, P9.1) is the
  surviving form. `s_probe.py` exists and measures S(t) for real zeros vs the periodic law. **Probe:** extend
  s_probe.py to the a.e.-certificate question (does the certificate value's T-fluctuation admit an
  almost-everywhere validity statement?).

---

## 4. Pool 4 — Fermat's Last Theorem / Wiles: transfer to a world with more structure

**Case (TEXTBOOK-LEVEL / UNVERIFIED-FROM-HELD-SOURCES):** Kummer's ideals (1840s–50s) handled a class of
primes; 350 years of direct Diophantine attempts failed. The winning move was a **transfer between worlds**:
Frey's hypothetical counterexample → a semistable elliptic curve; Ribet's level-lowering (1986) tied it to
non-modularity; Wiles/Taylor–Wiles (1994) proved the *partial* bridge (modularity of semistable curves) — a
*partial* theorem sufficed. The question moved to a world (modular forms + Galois representations) with
structure (Hecke operators, deformation rings) the original world lacked.

**The structural lessons:** (i) the transfer is to a world where the *same objects* carry more structure;
(ii) a *partial bridge* (semistable only) suffices — you do not need the full conjecture; (iii) the
"counterexample-transport": build the hypothetical obstruction object and derive a contradiction with the
second world's structure.

Program-side ground truth: the 256-law is our "Frey curve" (the hypothetical configuration the certificate
must handle). The second worlds available: the DPP/point-process world (V17 — rigidity inventory, expected
empty), the operator world (P2.1/W-vectors — KNOWN-DEAD as proof route), the de Branges world (L3), the
*prime-arithmetic world* (already our certificate's home), and the *higher-order correlation world*.

### Vectors
- **H4.1 — Christoffel–Darboux / determinantal certificate (NEW; probe, cheap; likely negative).** The DPP
  world's canonical kernel (sine kernel) has a PSD reproducing-kernel structure (Christoffel–Darboux); a
  certificate built on the CD kernel's finite compressions is a different matrix than the Gabor Gram W_T. The
  FLT-structured question: does the CD world's structure give a *provable* beyond-two-moment constraint
  (determinantal correlations) — or is the determinantal structure for ζ's zeros exactly the conjectural
  triple-correlation content? (Honest expectation: the extremal law re-normalizes, like V18's multi-window —
  but it is the "second world" probe the FLT lesson demands.) **Probe:** build the CD-kernel compression,
  compute the two-moment ratio; if the ratio ≥ the Gabor ratio (worse certificate), dead (cheap).
- **H4.2 — The partial-bridge sufficiency (NEW framing; overlap V12, KNOWN-OPEN assembly).** Wiles proved only
  the semistable class. Our analog: the smallest family class where orthogonality provably kills the
  off-diagonal (Dirichlet χ mod q, then GL(2) weight aspect). The bridge's "semistable class" is the cheapest
  provable slice. **Probe:** the V12 numerical probe (shared with H1.1).
- **H4.3 — The Frey-curve move: the law's triple correlation vs the PROVEN sine-kernel value (NEW probe;
  overlap V4's step 1; the key live lever).** The 256-law is periodic with doubles; its *triple correlation*
  S₃ is computable from the explicit law. The real zeros' S₃ at λ < 2/3 is **PROVEN** = sine-kernel
  (Rudnick–Sarnak/Hejhal). If the law's S₃ provably ≠ the sine-kernel value, the law is excluded as an
  admissible configuration for any *third-moment* certificate — the ceiling's premise (the law is admissible)
  survives only for the two-moment class, and the third-moment class's ceiling is a *new* LP (V4's
  moment-order capacity LP). This is the ONLY proven beyond-two-moment input in the corpus (attack-ceiling
  §3; §7.5(e)'s "odd moments add nothing" is about the n₊-functional at λ ∈ (1/2,1), not about excluding the
  law from a higher-order certificate). **Probe:** compute the 256-law's S₃ statistic vs the sine-kernel value
  (pure arithmetic on the explicit law; cheap). If the law's S₃ is far from GUE (expected: periodic lattice
  structure), V3/V4 are confirmed live; if accidentally near-GUE, the "law saturates all higher moments"
  expectation needs revision — either way a finding.
- **H4.4 — The operator-world transfer (KNOWN-DEAD as proof route; P2.1/W1/W5 documented).** Cited, not
  re-derived: no accepted self-adjoint realization; exactness at eigenvalue level = RH.
- **H4.5 — De Branges ordering as rigidity (NEW; overlap L3; KNOWN-OPEN).** The de Branges world *has* a
  structure theory (ordering, canonical bases) — the modular-forms analog. Suzuki's completion isomorphism
  (2301.00421, ABSTRACT-FETCHED) is the bridge; the question is whether the canonical basis gives a positivity
  the Gabor basis hides. **Probe:** compute the Weil form in the de Branges canonical basis (Paley–Wiener-type
  basis) and compare the certificate constants (cheap; likely equal — the form is basis-independent, so the
  honest content is the *ordering theorems* L3 proposes, not the basis).

---

## 5. Pool 5 — Prime Number Theorem / Newman: the RIGHT OBJECT

**Case (TEXTBOOK-LEVEL / UNVERIFIED-FROM-HELD-SOURCES):** PNT conjectured ~1790s (Gauss/Legendre); Chebyshev
(1850s) got the right order; Riemann (1859) connected primes to zeros; Hadamard and de la Vallée Poussin
(1896) proved it via the **zero-free region** — the right object, not term-by-term control. Newman (1980)
reduced the proof to a single Tauberian step: the analytic continuation of ζ′/ζ past Re(s) = 1 IS the whole
content. The lesson: the right object (a *region* statement with structural/analytic character) made the old
content minimal and the proof simple.

**The structural lesson for us:** our certificate already found its in-class right object — the LP-dual shows
the class-optimal certificate r ≈ 1−x exploits exactly the integrated discrepancy E(1) (the stability
identity's boundary term), and the shadow price of p₁ is exactly 1. In Newman terms: *the object is right; the
data is missing.* The right-object version of the p₁/off-line question: p₁ is a count; the count's region
statement is the beyond-bandwidth-1 form factor F on (1, 1+ε) (the pair-correlation-conjecture sliver); the
wrong objects (documented dead): the off-diagonal prime-pair sums (M29), the variance flank (attack-gm-variance),
individual off-line counts (V10's shallow-pairs diagnosis — the irreducible unknown).

### Vectors
- **H5.1 — Right-object audit + RH-conditional upper-bound recheck (NEW probe; documentation + cheap
  literature check).** The minimal input that would move v is an *upper bound* on the beyond-1 pair integral
  (usable with F ≥ 0, CGdL20-style, but *unconditional or RH-conditional*). attack-ceiling §3 records "no
  pointwise statement for α > 1 even under RH" in the held sources; a recheck of Montgomery-1973-under-RH and
  GM87 for any RH-conditional beyond-1 bound is cheap and either confirms the void or finds a sliver.
  **Probe:** grep the held bibliography + fetch-check Montgomery/GM87 statements on F(α), α > 1, under RH.
- **H5.2 — The certificate is already Newman-minimal (diagnostic, documented; KNOWN-OPEN data).** The
  in-class closure (attack-lpdual, close-inclass-gap) shows the class-optimal certificate consumes exactly
  {validity at the law, box |r| ≤ 1, r(1) = 0} — the minimal inputs. Conclusion: do not re-search the
  certificate class for a better object (the LP is closed); the only live data hole is the certified real p₁
  (shadow price 1), and the only *proven* structural input that could raise it is the λ < 2/3 triple
  correlation (converges with H4.3). **Probe:** none (documentation; the LP-dual output is the evidence).

---

## 6. Pool 6 — Linear programming: duality, cutting planes, interior points

**Case (TEXTBOOK-LEVEL / UNVERIFIED-FROM-HELD-SOURCES):** simplex (Dantzig 1947) — exponential worst case
(Klee–Minty 1972); duality (von Neumann/Dantzig) gave certificates and shadow prices; cutting planes (Gomory
1958, Chvátal) for integrality; ellipsoid (Khachiyan 1979) — polynomial worst case, theoretical; interior
points (Karmarkar 1984; Nesterov–Nemirovski 1994) — polynomial worst case *and* practical, via **barrier
functions with self-concordance** (the barrier's Hessian dominates its third derivative — quantitative
convexity) and a **central path** that converges without touching vertices.

**The structural lessons:** (i) the dual was done (the LP-dual agent; shadow prices in hand) — the interior
point lesson is the *central path* and the *barrier*: a canonical smooth curve through the feasible set whose
geometry (Hessian metric) reveals the polytope's structure; (ii) self-concordance = quantitative convexity —
our stability identity is exactly the certificate's quantitative convexity (data-sensitivity controlled by
(r(1), r′(1), ∫|r″|)); (iii) cutting planes = integrality cuts — our k_c penalties are the Chvátal closure,
already priced.

### Vectors
- **H6.1 — Central-path certificate family (NEW; probe, cheap; engineering + diagnostics).** Solve the
  certificate LP with a self-concordant logarithmic barrier; compute the central path from the two-moment MT
  certificate to the class optimum. (i) Diagnostic: are the path certificates all ≈ 1−x shapes (1-parameter
  family — the class is boring) or do they pass through structurally different r (e.g., cosine-like at one
  end)? (ii) Engineering: the *regularized* (strictly interior) certificate has a clean positive validity
  margin — directly useful for the Lean certification of the in-class closure (the exact r = 1−x attains the
  ceiling with zero margin; a barrier certificate with margin ε is easier to verify and certifies
  0.68183 − ε). **Probe:** scipy interior-point LP on the existing lpdual data; report the path and the
  margin-certificate.
- **H6.2 — Configuration-polytope geometry: where is the law? (NEW; probe, Med).** Self-concordance on the
  *configuration* side: the admissible polytope (marked configurations matching near-CUE rows) has an
  analytic center and a face structure. Where does the 256-law sit — vertex, edge, facet? Is it unique?
  This is the interior-point reading of H3.1's singularity classification (the two probes share the LP).
  **Probe:** the exact-rational configuration LP at N = 64/256 (regenerate-256law machinery); report the
  law's position and the adjacent vertices.
- **H6.3 — Chvátal closure / integrality cuts (KNOWN-DEAD; crossref attack-multiplicity §0,§2).** The
  integrality (marks ∈ ℤ, k_c penalties, `lemmaR_tight` Δ = 0) is priced optimally; no further cutting-plane
  gain inside the class. Cited, not re-derived.

---

## TOP 10 — ranked: "new object" moves above "sharper inequality" moves

Ranking principle from the six pools: every historical wall-break was a new object / new world / dynamical
view — none was a sharper inequality in the tight class. Sharper-inequality moves in *our* class are already
documented dead or closed (LP-dual attained the ceiling; attack-multiplicity priced integrality; attack-kernel
proved window optimality). So the ranking favors: (1) the one proven beyond-two-moment object, (2) spectral
objects, (3) classification/geometry of the obstruction, (4) family/dynamical views, (5) engineering.

1. **H4.3 — The law's triple correlation vs the PROVEN sine-kernel value** (NEW probe; overlap V4 step 1;
   the only proven beyond-two-moment lever). The 256-law = our Frey curve; S₃ is the partial bridge that is
   *proven on the real side* (λ < 2/3). Compute the law's S₃; if non-GUE, the third-moment certificate class
   has a new ceiling (V4's LP) and the law's admissibility is broken at the first provable higher order.
   **Probe:** explicit arithmetic on the 256-law (cheap).
2. **H1.2 / H2.1 — The spectral object: real W_T spectrum vs the law's W_T spectrum** (NEW; probe; overlap
   V1). The trace-formula/Weil lesson: read the spectrum, not just two moments. Both spectra are computable;
   the comparison is a measurement with real information content (separation, min-eigenvalue margins,
   multiplicity structure), and it adversarially scope-checks whether the (c₀,r) ceiling extends to spectral
   functionals. **Probe:** Rust computation (folds into V1).
3. **H3.1 — Extremal-configuration classification** (NEW; probe, cheap). Perelman's singularity classification.
   Are the near-CUE-matching configurations all crystals-with-doubles? The answer determines whether "exclude
   the obstruction by a structural ζ-statement" is a well-posed target. **Probe:** small-N exact-rational LP
   vertex enumeration (shares H6.2's machinery).
4. **H6.2 — Configuration-polytope geometry** (NEW; probe, Med). The law's position (vertex/edge/facet),
   uniqueness, adjacent vertices. Interior-point geometry of the admissible set. **Probe:** the N = 64/256
   configuration LP.
5. **H6.1 — Central-path certificate family** (NEW; probe, cheap). Barrier certificates with clean validity
   margins → Lean-certifiable in-class closure; diagnostics on the certificate family's shape. **Probe:**
   scipy interior-point LP on `tools/lpdual/`.
6. **H1.1 / H4.2 — Family-average bootstrap probe** (KNOWN-OPEN assembly; already funded as V12; Deligne +
   Wiles + quantum-ergodicity motivation). **Probe:** the V12 numerical probe.
7. **H2.4 — Selberg-zeta certificate prediction** (NEW; probe, Med). Completes the sandbox's cross-world table
   (lattice 0.977 / Ramanujan 0.32–0.36 / ζ 0.6725 / Poisson −0.02) with the spectral-geometric world;
   tests the "deficit = pair-correlation arithmetic" reading on a genuinely different RH-true object.
   **Probe:** prediction-first (certificate value from the empirical form factor alone), eigenvalue
   computation only if the prediction mechanism passes on the Ihara data.
8. **H5.1 — Beyond-1 upper-bound recheck** (NEW probe; cheap documentation). Confirm/refute the "no RH-
   conditional beyond-1 statement" void in the held sources (attack-ceiling §3). A found sliver would reopen
   the SDP route with proven input. **Probe:** bibliography grep + fetch-check.
9. **H4.1 — Christoffel–Darboux determinantal certificate** (NEW; probe, cheap; likely negative). The FLT-
   structured second-world probe. **Probe:** CD-kernel compression two-moment ratio.
10. **H3.4 — Fluctuation-shape exclusion over T** (KNOWN-OPEN; overlap V13/P9.1; probe exists). The only
    surviving fluctuation-statistic route (per-T is documented dead). **Probe:** extend `s_probe.py`.

---

## WILD section (deliberately absurd; honestly evaluated; each labeled)

- **W-H1 — "The 256-law's prime-side inversion contradicts Chebyshev."** Invert the law's form factor to its
  implied prime structure and check against the full proven prime arithmetic (beyond the two moments the law
  matches by construction). **FOR:** the Frey move pushed to the prime side; a contradiction would kill the
  ceiling. **AGAINST:** the law's construction already matches the two moment-evaluations, which *are* the
  prime evaluations; higher prime correlations are HL-strength (conjectural), so no *proven* contradiction
  exists by construction. **Probe:** the inversion computation (cheap, documented negative expected). Label:
  NEW (expected dead).
- **W-H2 — "Ricci-flow-style monotone functional for the certificate."** Find a quantity monotone along any
  natural flow (configuration interpolation, λ-family, T-evolution) that forces the certificate to converge to
  a value above p₀. **FOR:** Perelman's engine was a monotone; none has been identified for our class.
  **AGAINST:** the certificate value is trivially monotone in p₁ (shadow price 1) and no nontrivial monotone
  exists along the natural flows (the data is pinned at bandwidth one). Label: NEW (weak, documented).
- **W-H3 — "ζ IS the Selberg zeta of some object."** If ζ were a spectral zeta of a canonical positive
  operator, RH would follow — the arithmetized versions (Ihara, bigraphs) exist and the sandbox already ran
  them. **FOR:** the Ihara worlds are proven-RH and the certificate calibrates on them. **AGAINST:** no such
  object exists for ζ; the transfer is Hilbert–Pólya renamed. Label: KNOWN-DEAD as stated; the calibration
  value is already banked (attack-ihara-sandbox).
- **W-H4 — "Interior-point path as a PROOF of the in-class optimum."** The central path's analytic structure
  yields a proven (not numerical) certificate for 0.68183 − ε — a Lean-certifiable witness. **FOR:** real
  engineering value (the exact r = 1−x has zero margin; a path certificate has ε-margin). **AGAINST:** no new
  math — the ceiling is already proven; this is certification logistics. Label: NEW (engineering).
- **W-H5 — "Newman contour-shift in λ: analytically continue the certificate past λ = 1."** The certificate
  functional as an analytic function of λ; continuation past the λ = 1 wall reads the beyond-1 F.
  **AGAINST:** the continuation of the functional IS the beyond-1 F, which is the conjectural input — dead by
  construction. Label: KNOWN-DEAD (by construction; recorded so it is not re-derived).

---

## Label inventory

- **NEW (invented here, untested; conjectured by construction, each with a probe):** H1.1 (framing/overlap
  V12), H1.2 (spectrum comparison), H1.3 (polarization hunt, overlap L3), H2.1 (spectral scope-check), H2.2
  (resolvent reading), H2.4 (Selberg prediction), H3.1 (singularity classification), H3.2 (law→real
  interpolation), H3.3 (monotone hunt, weak), H4.1 (Christoffel–Darboux), H4.3 (law's S₃ — the key lever),
  H4.5 (de Branges basis), H5.1 (beyond-1 upper-bound recheck), H6.1 (central path), H6.2 (configuration
  polytope), W-H1, W-H2, W-H4.
- **KNOWN-DEAD (documented in held notes; cited, not re-derived):** H1.4 (higher moments for n₊, paper §7.5(e);
  attack-ceiling §3), H2.3 (individual GL(2)/surface transport, attack-lfunctions §4 — dimension ceiling
  Λ* = 1/2), H4.4 (operator-world proof route, P2.1/W1/W5), H6.3 (Chvátal closure / integrality,
  attack-multiplicity §0,§2), W-H3 (ζ = Selberg zeta as stated), W-H5 (λ-continuation, dead by construction).
  Background deaths that bound this catalog's honesty: M29 (beyond-1 mean), attack-gm-variance (beyond-1
  variance), attack-cvs-import B1–B3 (even RH does not move the ceiling), V13-per-T (fluctuation shape
  excluded from per-T certificates).
- **KNOWN-OPEN (documented open in held notes):** the family-average assembly (V12 — H1.1/H4.2's target),
  the third-moment certificate ceiling (V3/V4 — H4.3's LP), the de Branges ordering theorems (L3 — H1.3/H4.5),
  the beyond-1 F values (attack-ceiling §3 — H5.1's recheck), the Selberg-spectral data (H2.4's computation).
- **TESTED-OPEN (existing probes, tested, asymptote open):** V1's real W_T spectrum (H1.2/H2.2 fold in),
  the Selberg-CLT `s_probe.py` (H3.4 extends), the Ihara sandbox (H2.4's prediction mechanism), E5.4's
  conditioning (H3.2-adjacent), the LP-dual closure (H6.1's endpoint).

---

## Meta-verdict: what the history of broken tight walls says our most promising move-class is

The six pools agree on one meta-pattern: **proven-tight class limits are broken by changing the class — a new
object (Weil/Grothendieck cohomology), a transfer to a world with more structure (Selberg's spectral geometry,
Wiles' modularity), or a dynamical/family view (Perelman's flows, Deligne's families) — and by *partial
bridges* to that new world (Wiles' semistable case, Newman's minimal analytic step). No case in the six was
broken by a sharper inequality inside the tight class; when the class was tight, the inequality was already
optimal (our LP-dual: shadow price of p₁ = 1; our stability identity: the certificate's self-concordance).

Translated to our walls, with full honesty about what is proven:

1. **The in-class class is closed and its object is right** — the LP-dual attained the ceiling, r ≈ 1−x
   exploits exactly E(1), and the shadow-price-1 structure says only p₁-data moves v. Re-searching the
   (c₀,r) class is Newman-wise pointless. This is a *diagnostic* conclusion, not a result.
2. **The single most promising move-class is the one PROVEN beyond-two-moment object: the λ < 2/3 triple
   correlation** (Rudnick–Sarnak/Hejhal). It is simultaneously (i) Deligne's family/weight reading (a proven
   higher-order datum where two moments exhausted the wall), (ii) Wiles' partial bridge (the semistable-class
   sliver — you do not need full S₃), (iii) Newman's right object (a structural, region-type statement rather
   than value-conjecture), and (iv) the Frey-curve move (exclude the 256-law — our counterexample — by the
   second world's structure). The cheapest decisive computation: **the 256-law's own triple-correlation
   statistic vs the sine-kernel value** (H4.3) — if non-GUE (expected: periodic lattice), the law's
   admissibility is broken at the first provable higher order and the third-moment certificate class (V3/V4)
   has a genuinely new ceiling; if near-GUE, the "the law saturates all higher moments" expectation is
   refuted and the moment-order roadmap (V4) is priced by that data.
3. **The second move-class is the spectral object** — the full W_T spectrum as a *different functional*
   (H1.2/H2.1). History (Weil: zeros as eigenvalues; Selberg: the spectral side carries structure the other
   side doesn't) says the spectrum is where the missing structure hides. It is computable for both the real
   zeros and the explicit law; the comparison is a measurement that changes what we believe about the wall's
   shape (and adversarially scope-checks whether the (c₀,r) ceiling bounds spectral certificates).
4. **The third move-class is classification** (H3.1/H6.2): Perelman's singularity classification and the
   interior-point polytope geometry converge on the same cheap question — is the extremal configuration a
   lone vertex or a facet of a rich admissible polytope? The answer fixes whether "exclude the obstruction by
   a proven structural ζ-statement" is a well-posed target (it is the only lever attack-ceiling §4 keeps
   alive) or a dead letter.
5. **Sharper-inequality moves are closed** (LP-dual attained; window optimal; integrality priced; M29 and the
   variance flank documented). Funding them again would repeat the Dwork mistake: sharpening a fragment tool
   that cannot reach the weights.

**Bottom line:** the history says to fund, in order: (1) the law's S₃ computation and, if non-GUE, the
third-moment certificate LP (V3/V4) — the one proven bridge past the two-moment wall; (2) the spectral
comparison (V1 + H1.2/H2.1); (3) the obstruction classification (H3.1/H6.2); (4) the family-average probe
(V12 — the partial bridge); (5) the engineering of a Lean-certifiable central-path certificate (H6.1). Every
one of these has a cheapest-first probe of under a day; every negative is a documented finding; none claims
to settle RH.

---

## Honesty footer

- All historical narrative (Weil/Dwork/Grothendieck/Deligne; Selberg; Poincaré/Perelman; FLT/Wiles; PNT/Newman;
  LP/interior-points) is **TEXTBOOK-LEVEL / UNVERIFIED-FROM-HELD-SOURCES** — the program holds none of those
  papers; dates, names, and attributions are from general knowledge and may contain textbook-level inaccuracy.
  The structural lessons are stated independently of the history's exact details.
- All program-side claims are grounded in the held notes read this session (cited inline): the ceiling
  (attack-ceiling, Lean), the in-class closure and shadow price (attack-lpdual), the beyond-1 deaths (M29,
  attack-gm-variance), the sandbox readings (attack-sandbox, attack-ihara-sandbox), the CvS orthogonality
  (attack-cvs-import), the GL(2) dimension wall (attack-lfunctions), the two-form complementarity
  (attack-twoform), the vector catalog (V1–V20, L1–L9, V17).
- The claim "the 256-law's S₃ is expected non-GUE" is **CONJECTURED** (a periodic lattice's higher
  correlations differ from the sine-kernel's — heuristic; the probe settles it). The claim "a spectral
  certificate is heuristically capped at p₀ + O(|E(1)|)" is **ARGUED** here (W_T entries are bandwidth-one
  data; the law's spectrum is pinned up to the |E(1)| residual) — not proven; the probe is the adversarial
  scope-check.
- No fabrication: every vector references a probe that is either already funded (V1, V3, V4, V12), an
  existing tool (`tools/lpdual/`, `tools/finitet`, `s_probe.py`, the regenerate-256law machinery), or a
  cheap computation on the explicit 256-law.
