# Idea Generator: engineering-physics (structural/mechanical, electrical, antenna, microwave, aerospace, heat-transfer) attack catalog on RH and the on-line-zero constants

**Agent:** IDEA GENERATOR (engineering-physics angle; analogy-domain-transfer + creativity-brainstorm + constraint-hardness). Round 1.
**Purpose:** feed the EXECUTIONER agents. Every vector is concrete enough to attack.
**Honesty protocol:** this file invents *no* proofs and asserts *no* new theorems. Engineering facts (Koiter imperfection sensitivity, Foster/Brune synthesis, Thomson–Tait–Chetaev, critical radius, Dolph–Chebyshev, Friis cascade, supergain/Q-bounds) are standard textbook material named at that level; anything I cannot verify from sources we hold is labeled "reported standard — verify before use". Every *idea* is CONJECTURED by construction and carries a kill criterion. Labels: **NEW** (invented here, untested) / **KNOWN-DEAD** (killed here or in cited notes) / **KNOWN-OPEN** (core is open or already flagged; new framing or procedure only) / **TESTED-OPEN** (probed here with code, still open).
Overlap discipline: crossdomain = [CD-V#]/[CD-W#]/[CD-A#]; physics = [P#.#]; control = [C-XX]; music/ling = [M#.#]/[R#]; crystallography/astro = [A#]/[B#]; attack notes = [AK]=kernel, [AC]=ceiling, [AL]=lpdual, [AM]=multiplicity, [AF]=finitet, [snd]=attack-sandbox; validator = [val-001].

**Probes run this round (code-backed, scripts in `tools/ig-eng/`, all CHECKED NUMERICALLY):**
- **Probe A** (`probeA_imperf.py`): (i) exact identity bound/N = 1 − (1/N)Σ(λᵢ−1)² (the certificate is the spectral concentration of W_T's eigenvalue law around 1); (ii) imperfection-sensitivity fit of the documented sandbox off-line-injection curve (world b, β = 0.3): the certificate is **thresholded** (survives f = 0.01, breaks by f = 0.02) with superlinear damage (exponent ≈ 1.7–2 from 2 points — rough).
- **Probe B** (`probeB_boxsens.py`): **dv/dbox = |E(1)| = 2.5431315·10⁻⁶ exactly** — the in-class gain 0.6725 → 0.6818 is NOT superdirective-fragile: the gain (0.00933) lives in p₀ (the law's simple fraction), and the box |r| ≤ 1 modulates only the |E(1)| residual (a 10% box error moves the value by 2.5·10⁻⁷). Strong-form superdirectivity worry REFUTED.
- **Probe C** (`probeC_stefan.py`, `probeC2_robust.py`, `probeC3_lmfdb.py`): the u<1 finite-T pair-sum deficit has a **height-dependent sign profile**: ABOVE the sine-kernel value (positive deficit, over-correlation) for γ ≲ 1500 (+0.04…+0.09, LMFDB cross-checked), crossing to BELOW (extra repulsion) for γ ≳ 2500, with magnitude growing to ≈ −0.08 at γ ≈ 9000 (5 disjoint windows, internally rescaled to density 1). The deficit front is **pinned at u < 1** (no drift with height) — a stationary short-range structure, not a moving boundary. The deficit does not visibly decay over γ ∈ [2500, 9900] in this normalization — consistent with [val-001]'s INCONCLUSIVE on [AF]'s "Δ → 0".

---

## 0. The honest map (what engineering physics could possibly move)

Respected walls (all PROVEN/CHECKED, see [AL], [snd], [AF]):
1. Lemma 3.2 is tight on the data budget D = (tr, ‖·‖², block structure, tr P₁ ≤ s₁, n₊(Q) ≤ b) [QS]/[C-MU2] — no matrix inequality beats it inside D.
2. In-class ceiling 0.6818 attained; shadow price of p₁ = 1; no missing constraint inside bandwidth one [AL].
3. The 2/3 deficit is **arithmetic**: the certificate reads the zeros' two-point statistics (sandbox: real world → 0.6725, rigid lattice → 0.977, Poisson → empty; the certificate is a repulsion statement) [snd].
4. Finite-T: Δ(T) = bound/N − 0.6725 > 0 at all measured T, ~1/log T; decay-to-zero INCONCLUSIVE (nonzero fitted intercepts) [AF]/[val-001 target 3]; the deficit concentrates at u < 1, short-range pair structure [R6]; NEW this round: sign crossover with height (Probe C).

Therefore every engineering vector must either (a) add data outside D (zero-free boundary counts of off-line zeros, sign/Hadamard structure of the kernel, minimum-spacing/regularity constraints on configurations, derivative-tower data, higher moments), or (b) be a diagnostic/roadmap that changes what we believe (the method's real slack, the P6 error structure, the price of conjectural inputs). Engineering physics' genuinely outside-the-budget assets, in order of promise:
- **(i) zero-free boundary counting (the argument principle) as the aerospace/mechanical "stability margin" read per mode** — the p₁ datum at new heights [= C-NY1, now with an engineering "flutter margin" name and a level-dynamics probe];
- **(ii) a NEW measured P6 structure**: the u<1 deficit's height-sign-crossover (Probe C) — the first "where the finite-T deficit lives" profile with height;
- **(iii) the spectral-concentration identity** bound/N = 1 − mean((λ−1)²) — a cleaner reading of the certificate and a new edge/pin-fraction diagnostic;
- **(iv) the exact-in-class certificate via the elliptic (Cauer) machinery** — a concrete candidate for the 0.6818-achieving certificate [overlaps P5.4/P7.6];
- **(v) the reciprocal-defect (palindromic) off-line meter** under the Möbius map to the circle — a new zero-free diagnostic;
- **(vi) condition/margin reports** (input-conditioning audit, per-row gain margins, box-sensitivity) — P7 diagnostics that quantify how robust the closure really is.

---

## Pool 1 — Structural/mechanical: Euler buckling, vibration modes, SHM, metamaterials

### SM-1. Koiter imperfection-sensitivity template for the off-line injection curve — TESTED-OPEN (Probe A)
**Idea.** Buckling theory's signature quantitative law is imperfection sensitivity: a critical load collapses under a small imperfection with a characteristic exponent (Koiter: symmetric imperfection gives P/P_cr ~ 1 − C·f^{2/3}). The sandbox's off-line injection curve [snd world (b)] is the same object: the certificate (the "critical load") vs the injected off-line fraction f (the "imperfection"). **Probe A**: at β = 0.3 the certificate is **thresholded** (survives f = 0.01 at +0.007 above 0.6725, breaks by f = 0.02 at −0.022) and the damage grows superlinearly (≈ f^{1.7–2} from 2 points — rough, not the 2/3 Koiter law).
**Analogy.** Buckling critical load ↔ certificate value; imperfection amplitude f ↔ off-line pair fraction; collapse threshold ↔ the crossing fraction.
**Needs.** Finer sandbox runs (f = 0.005…0.03 grid, more β, both patterns) to pin the exponent and the crossing law; a model of why the damage is superlinear (pair×on-line cross terms are quadratic in f).
**Feasibility.** Low (existing sandbox harness). **Value.** A mechanism tag for the off-line sensitivity + a quantitative "margin curve" (what off-line fraction breaks 0.6725 at each depth) — the honest answer to "how robust is the theorem to a small RH failure".
**Cheapest probe.** Done (Probe A, documented data); extend with 2 more runs.

### SM-2. Spectral-concentration identity: bound/N = 1 − mean((λᵢ−1)²) — NEW (identity PROVEN, Probe A)
**Idea.** 2λ − λ² = 1 − (λ−1)², so bound/N = (1/N)Σ(2λᵢ−λᵢ²) = 1 − (1/N)Σ(λᵢ−1)². The certificate literally asks **how concentrated W_T's eigenvalue law is around λ = 1** (crystal: masses {1/6, 2/3, 1/6} at {0, 1, 2} give 1 − 1/3 = 2/3; real asymptote: 1 − 0.3275 = 0.6725). The finite-T deficit (R6: u<1, short-range) is "the eigenvalue law is over-diffuse around 1, driven by short-range pair sums".
**Analogy.** Modal concentration / participation ↔ the pin fraction of the eigenvalue law at 1.
**Needs.** [AF]/[CD-V1] W_T spectra (exists); compute the "pin fraction" (mass of eigenvalues within ε of 1) vs ε and T, and its decomposition into the u<1 pair-sum part.
**Feasibility.** Low (measure). **Value.** A cleaner statement of what P6's deficit is, plus a new edge diagnostic for P7 (the method's real slack).
**Cheapest probe.** <1h: [AF] code, print pin-fraction(ε) for ε ∈ {0.1, 0.2, 0.5} at T = 200–700.

### SM-3. SHM "damage localization" of the finite-T deficit — NEW (diagnostic, Probe C supplies the first measurement)
**Idea.** Structural health monitoring detects local stiffness loss from low-mode frequency shifts; the first-order perturbation δω/ω = φᵀδKφ localizes the damage. The analog: how much does a *band-limited* perturbation of the pair-sum kernel (a "local defect" at normalized distance u) move the certificate? Probe C gives the first "damage map": the u<1 deficit is positive at low height, negative and growing at high height — a height-dependent damage profile.
**Analogy.** Damage localization (which element's stiffness loss explains the mode shifts) ↔ which u-band's pair-sum defect explains the finite-T deficit.
**Needs.** Perturbation analysis of the W_T eigenproblem under band-limited pair-kernel perturbations (quadrature; the Ψ₂ kernel is explicit).
**Feasibility.** Low–Med. **Value.** P6 mechanism decomposition: which "modes" of the pair kernel carry the deficit, and whether the height-profile (Probe C) matches a specific kernel-defect model.
**Cheapest probe.** <1h: compute the certificate's response to a synthetic "defect kernel" δ(u) localized at u ∈ (0,1) and compare with the measured band profile.

### SM-4. Complementary-energy / Temple bracketing of the finite-T certificate — NEW (P6)
**Idea.** Structural analysis brackets true eigenvalues between Rayleigh (upper) and complementary-energy (lower) bounds; Temple's inequality bounds the eigenvalue error by the residual norm of a Rayleigh-Ritz pair. Applied to W_T: the finite-T measurements give approximate eigenpairs; Temple's inequality yields a *rigorous bracket* on the certificate's asymptotic constant from computable residuals — an honest effective P6 statement (brackets, not point values).
**Analogy.** Rayleigh–Ritz + Temple bracket ↔ upper/lower bracketing of the certificate value at finite T.
**Needs.** The empirical eigenpairs of W_T ([AF] code) and the Temple residual computation (‖W v − λ v‖).
**Feasibility.** Med. **Value.** The first rigorous finite-T bracket on how far the measured bound is from the asymptotic constant — addresses the [val-001] INCONCLUSIVE with error control instead of fits.
**Cheapest probe.** <1h: compute max eigenpair residuals for the [AF] W_T; plug into the Temple bound; report the bracket width vs T.

### SM-5. Acoustic-metamaterial band-gap engineering = the V4 capacity roadmap — KNOWN-OPEN (framing; content = [CD-V4])
**Idea.** Band gaps (forbidden spectral regions) ↔ the certificate's "empty region" (beyond bandwidth 1, where nothing is certified); metamaterial design shrinks band gaps by adding constraints — the certificate's "band-gap engineering" is the moment-capacity LP [CD-V4], which prices each conjectural input by how much band gap it closes.
**Analogy.** Metamaterial band-gap design ↔ the capacity curve over moment order.
**Needs.** None (the V4 LP is the content). **Feasibility.** Low. **Value.** Documentation; prevents re-funding "shrink the gap" without a priced input.
**Cheapest probe.** None.

### SM-6. Buckling bifurcation + the "data paradox": more bandwidth-one data LOWERS the certified value — KNOWN-OPEN (content = [AL] LP-B′)
**Idea.** The certificate is a critical load; the 256-law is the bifurcation point; the LP-B′ row sweep [AL] is the post-buckling branch: v(M) decreases with the number of near-CUE rows (0.89 with 1 row → 0.6818 with 255). This antimonotonicity — **more certified data ⟹ lower bound** — is the structural analog of "adding dissipation destabilizes" (AE-2) and of the critical-radius phenomenon (HT-2): collecting more bandwidth-one data does not raise the bound, it pins it down.
**Analogy.** Post-buckling load-deflection branch ↔ the row-sweep curve v(M).
**Needs.** None (the numbers are [AL]-computed). **Feasibility.** immediate. **Value.** A crisp, honest statement for P7: "gathering more in-class data is not a route to a higher bound" — prevents funding data-collection-only rounds.
**Cheapest probe.** None.

### SM-7. Half-power-bandwidth "damping" / glassy aging of the finite-T deficit — NEW (diagnostic; reframes [val-001] target 3)
**Idea.** The deficit's decay rate is a "damping ratio" of the certificate. The measured ~1/log T with **nonzero fitted intercepts** ([val-001]: Δ ≈ 0.014 + 0.155/lnT, etc.) is the classic signature of *glassy aging* — slow relaxation in a system with a hierarchy of timescales (the prime sums at all scales up to T). The fitted "intercepts" are the aging plateau, not a failure to converge.
**Analogy.** Glassy/logarithmic relaxation (spin glasses, aging) ↔ the deficit's slow, non-settling decay.
**Needs.** Extend [AF]'s Δ(T) trend to larger T (new zeros via tools/zeta-rs); fit the aging ansatz Δ = C/log^β T vs the intercept fits.
**Feasibility.** Low (existing data + new zeros). **Value.** A testable physical explanation of the INCONCLUSIVE — predicts the deficit will not settle at a power law.
**Cheapest probe.** <30min: refit [AF]'s 10 points against Δ = C/log^β T; report β (expect β ≈ 1).

### SM-8. Modal participation of the certificate (effective mass per mode) — NEW (diagnostic, P7)
**Idea.** Each eigenvector of W_T contributes λ_k(2 − λ_k) to the bound; the "effective certificate mass" per mode identifies which eigenvalues carry the bound. If the bound is carried by few modes, the method is fragile to those modes' accuracy.
**Analogy.** Modal participation factors ↔ per-eigenvalue certificate contribution.
**Needs.** W_T eigendecomposition (exists). **Feasibility.** Low. **Value.** P7 slack diagnostic: where the bound actually lives.
**Cheapest probe.** <1h: [AF] code, histogram λ_k(2−λ_k); report the participation concentration (top-10% fraction of the bound).

---

## Pool 2 — Electrical circuits/filters: Butterworth/Chebyshev/Cauer, LC ladders, z-transform

### EE-1. Cauer/elliptic exact solution of the in-class certificate — NEW (overlaps P5.4, P7.6; concrete machinery named)
**Idea.** The elliptic (Cauer) filter's design is the *exact* solution of the minimax/alternation problem in Jacobi elliptic functions — the same extremal class as the certificate LP's continuum limit ([P5.1]'s contact-set problem, [P7.6]'s alternation). The 256-law's active constraints determine a contact set; the Cauer machinery gives the *analytic* certificate r*(x) (elliptic modulus fixed by the contact geometry) rather than a numerical LP solution.
**Analogy.** Cauer filter (best rational approximation, equiripple in both bands) ↔ the class-optimal certificate (alternating r with minimal curvature budget).
**Needs.** The LP dual's active set ([AL] machinery); the elliptic-function solution of the two-cut variational problem.
**Feasibility.** Med–High. **Value.** The only route I see to an *exact* in-class 0.6818 certificate (same prize as [P5.4]/[P7.6], different toolkit).
**Cheapest probe.** <1h: read off the dual variables of the [AL] LP; identify the contact set; test whether r*(x) ≈ 1−x plus a small elliptic correction (compare with the LP-optimal r).

### EE-2. Foster/Brune synthesis: the certificate as minimum-reactance extraction — KNOWN-OPEN (content = [C-NY1])
**Idea.** Circuit synthesis decomposes a positive-real impedance into a minimum-reactance part plus an extracted reactance whose imaginary-axis poles are the "pure" reactive elements (Foster's theorem: reactance poles/zeros alternate on the axis). The analog: the certificate is the "minimum-reactance" part of the zero configuration; off-line pairs are the "extracted reactance" (the (1,1)-planes = imaginary-axis poles); the p₁ datum = the extracted pole count — the shadow-price-1 datum again.
**Analogy.** Brune/Foster reactance extraction ↔ separating on-line (minimum-reactance) from off-line (extracted) structure.
**Needs.** Nothing new (the p₁ datum's measurement is [C-NY1]'s contour counting). **Feasibility.** Low. **Value.** Circuit vocabulary for why the off-line count is the only lever.
**Cheapest probe.** None (fold into [C-NY1]).

### EE-3. Reciprocal defect: the palindromic (self-reciprocal) off-line meter under the Möbius map — NEW (diagnostic)
**Idea.** Under the Möbius map z = (s−1/2−i)/(s−1/2+i) the critical line becomes the unit circle, and a polynomial with all roots ON the circle is *self-reciprocal* (palindromic/anti-palindromic coefficients) — a necessary condition. The functional equation ξ(s) = ξ(1−s) is the self-reciprocality of the completed function; the **reciprocal defect** (distance from palindromicity) of finite partial products/Taylor data of ξ is a zero-free, prime-side-computable off-line meter. This addresses [C-RH5]'s "no natural disk structure" objection: the Möbius map supplies the disk; the Schur–Cohn test on the *defect* is the honest fragment (a pure stability test is equivalent to the moment cascade [C-RH1], but the *defect magnitude* is new).
**Analogy.** Self-reciprocal polynomials (all roots on the circle) ↔ ξ under the Möbius map; the palindromic defect ↔ the off-line content.
**Needs.** Taylor data of ξ at a point (prime-side explicit formula); the Möbius-transformed finite data; the defect norm.
**Feasibility.** Low (probe). **Value.** A new zero-free diagnostic with a different error structure than W_T's moments (cross-check for [CD-V1]/[C-RH2]).
**Cheapest probe.** <1h: from ξ, ξ′, ξ″ at a few points (explicit formula), build the degree-2/3 reciprocal defect; print its T-trend.

### EE-4. Filter-design taxonomy of certificates: Butterworth/Chebyshev/elliptic = flat/cosine/residual — KNOWN-OPEN (documentation)
**Idea.** The certificate history IS the classical filter taxonomy: the flat window (2/3) is Butterworth (maximally flat at u = 0); the cosine (Theorem D, 0.6725) is the Chebyshev-style extremal of the one-delta problem [AK]; the LP-optimal r ≈ 1−x residual [AL] is the elliptic-style equal-ripple solution. The taxonomy's lesson: each extremal class has an exact closed-form solution — the search for the 0.6818 certificate is the search for the elliptic member (EE-1).
**Analogy.** Filter synthesis taxonomy ↔ the certificate's window/residual hierarchy.
**Needs.** None (documentation; content = [AK]/[AL]/[P7.6]). **Feasibility.** immediate. **Value.** Organizes the in-class search and prevents re-deriving the flat/cosine optima.
**Cheapest probe.** None.

### EE-5. Group-delay / dispersion of the SFF argument — NEW (diagnostic, [P3])
**Idea.** In filter design the group delay d(arg H)/dω measures dispersion; the analog is the argument of the complex spectral form factor K(α) = Σ_ρ e^{iαγ}-weighted ([P2.1]): its derivative d(arg K)/dα over α is a "dispersion" statistic the intensity-only certificate never reads.
**Analogy.** Group delay ↔ d(arg K)/dα; dispersion compensation ↔ the missing phase data ([P6.4]).
**Needs.** The SFF computation ([P2.1]'s probe). **Feasibility.** Low. **Value.** A new beyond-1 region diagnostic.
**Cheapest probe.** <1h: extend [P2.1]; print d(arg K)/dα and its variation over α ∈ [0,8].

### EE-6. Coefficient-quantization / condition-number audit of the certificate map — NEW (P6/P7)
**Idea.** Fixed-point filter design measures pole sensitivity to coefficient quantization via condition numbers; the analog: the certificate value's sensitivity to its *inputs* (the prime-side moment data and their error terms). The Jacobian of the certificate with respect to (tr, HS², the rows sⱼ) — and the propagation of the O(loglogT/logT)-class errors ([AF]) — is a condition-number report.
**Analogy.** Pole-sensitivity-to-quantization ↔ certificate-sensitivity-to-input-errors.
**Needs.** The certificate as an explicit function of the moment data; the row shadow prices ([AL] drop-row analysis) as the sensitivity coefficients.
**Feasibility.** Low–Med. **Value.** Quantifies how much the P6 error terms can actually move the constant (distinct from [E5.4]'s *window*-conditioning — this is *input*-conditioning).
**Cheapest probe.** <1h: from [AL]'s drop-row shadow prices, propagate a δ = 1e-3 relative error in each row; report the worst-case certificate shift.

### EE-7. Diagonal loading: the loaded certificate as a conditioned measurement — NEW (numerical audit; formula PROVEN)
**Idea.** Capon/MVDR's standard robustness fix is diagonal loading (add εI before inverting); the analog for the finite-T measurements: W_T + εI shifts the certificate by bound(ε) = 2(tr+εN) − (HS²+2εtr+ε²N) = bound − ε²N + 2ε(N−tr) ≈ bound − ε²N (since tr ≈ N). The real W_T is numerically near-rank-deficient at the f64 floor ([AF]); loading stabilizes the eigen-solve without moving the constant by more than ε²N — a numerical-hygiene audit.
**Analogy.** Diagonal loading (robust MVDR) ↔ regularized W_T eigen-solve.
**Needs.** The [AF] machinery + a loading parameter. **Feasibility.** Low. **Value.** Confirms the finite-T numbers are conditioning-stable; documents the numerics floor.
**Cheapest probe.** <30min: [AF] code with ε = 1e-10…1e-6 loading; report the certificate shift (expect ε²N).

### EE-8. Grating-lobe-free condition = the bandwidth-one wall — KNOWN-OPEN (framing)
**Idea.** A phased array is grating-lobe-free iff the element spacing d ≤ λ/2; the certificate's analog is the bandwidth wall λ ≤ 1 (the Poisson completion [Claim 2.1] breaks beyond). The "grating lobes" are the aliased off-diagonal structure; seeing "through the grating lobes" is exactly the beyond-1 form factor (CONJECTURED).
**Analogy.** d ≤ λ/2 ↔ bandwidth ≤ 1; grating lobes ↔ off-diagonal aliasing.
**Needs.** None (framing; content = [CD-A5]/[P2.2]). **Feasibility.** immediate. **Value.** Documentation.
**Cheapest probe.** None.

---

## Pool 3 — Antenna/phased-array: beamforming, null steering, superdirectivity, MVDR

### AN-1. Superdirectivity fragility audit of the in-class gain — TESTED-OPEN (Probe B run; strong form REFUTED)
**Idea.** Superdirective arrays achieve high gain at the cost of enormous sensitivity (the supergain bound / Q-limit); the worry: the in-class gain 0.6725 → 0.6818 is a "superdirective" 1.4% bought with extreme conditioning. **Probe B refutes the strong form**: dv/dbox = |E(1)| = 2.54·10⁻⁶ exactly — the box |r| ≤ 1 modulates only the measure-zero residual, and the gain lives in p₀ (the law's simple fraction, fixed by the configuration LP). A 10% error in the box modeling assumption moves the value by 2.5·10⁻⁷. The in-class closure is robust to the modeling box.
**Analogy.** Supergain vs Q-limit ↔ certificate gain vs (slope + curvature + box) budgets.
**Needs.** Done (Probe B); extend to the slope/curvature budgets (perturb B, C) and to the validity-row p₀ (perturb the row data by δ and report dv/dp₀ — expected 1:1, [AL]).
**Feasibility.** Low. **Value.** An honest P7 statement: the fragile part of the closure is the *configuration datum* p₀ (which is exactly the shadow-price-1 fact [AL]), not the modeling box.
**Cheapest probe.** Done; add the row-perturbation sweep (30min).

### AN-2. Array factor = structure factor; null steering; Dolph–Chebyshev sidelobe certificate — KNOWN-OPEN (overlaps [P7.6])
**Idea.** The array factor is the same object as the crystallographic structure factor (already mined, [A-pool]); null steering places zeros of the array factor — the certificate "steers nulls" at off-line pairs. The Dolph–Chebyshev design gives the *exact* equal-ripple (alternating) solution in Chebyshev polynomials — a concrete closed-form candidate for the alternating certificate of [P7.6]. The certificate's "sidelobe level" is the |E(1)| ripple.
**Analogy.** Dolph–Chebyshev (equal sidelobes) ↔ the alternating optimal certificate.
**Needs.** The [AL] dual's contact set; a Chebyshev-polynomial ansatz for r*. **Feasibility.** Med. **Value.** A candidate closed form for the in-class certificate.
**Cheapest probe.** <1h: fit the [AL] LP-optimal r to a Chebyshev combination; report the residual.

### AN-3. MVDR/Capon: the inverse-covariance certificate — KNOWN-OPEN (content = [P1.1], folded with EE-7)
**Idea.** Capon's estimator uses the inverse covariance — higher-order statistics of the data; the certificate's Capon version is the resolvent route [P1.1], whose reduction to the moment problem [P8.4] is already flagged. The genuinely transferable fragment is the diagonal-loading robustness trick (EE-7).
**Analogy.** Capon (minimum-variance, inverse-covariance) ↔ the resolvent/Green's-function certificate.
**Needs.** Nothing new ([P1.1]'s probe). **Feasibility.** Low. **Value.** Documentation; prevents re-funding the resolvent route before its [P8.4] reduction check.
**Cheapest probe.** None.

### AN-4. Mutual-coupling compensation: the pair-sum as mutual impedance; coupling loss = the [CD-V5] support curve — KNOWN-OPEN (content = [CD-V5])
**Idea.** The off-diagonal entries of W_T are the "mutual impedance" of the Gabor elements (⟨v_ρ,v_ρ′⟩ = Φ(s_ρ−s_ρ′), [C-PF]'s explicit contraction). Array practice compensates known mutual coupling; the "unknown coupling" of the certificate is the beyond-1 pair correlation, and its effect on the gain is the [CD-V5] support curve (F ≡ 1 on [1,A]).
**Analogy.** Coupling-matrix compensation ↔ accounting for beyond-1 pair correlation.
**Needs.** None (the support curve LP [CD-V5] is the content). **Feasibility.** Low. **Value.** Documentation.
**Cheapest probe.** None.

### AN-5. Level dynamics / p-k tracking of the smoothed zeros — NEW (diagnostic family; merges AE-1, RF-3)
**Idea.** Dyson/Pechukas level dynamics study eigenvalue *velocities* under a parameter; the aerospace p-k method tracks aeroelastic modes as the reduced frequency varies, detecting flutter by mode coalescence. The analog: track the complex zeros of the *smoothed* zero-sum Z(t; σ) as the smoothing width σ varies (prime-side, zero-free): report the zero trajectories, the velocity distribution, and the minimal "clearance" of each zero from the line. RH = no crossing for any σ; the "flutter margin" per zero = its clearance. This probes beyond-pair-correlation statistics with a genuinely new object (the dynamics of the zeros under window variation).
**Analogy.** p-k / Dyson level dynamics ↔ zero trajectories under smoothing; mode coalescence (flutter onset) ↔ off-line pairing.
**Needs.** A smoothed zero-sum evaluator (Euler–Maclaurin ζ + a smoothing kernel — extend tools/zeta-rs or the music-ling probes) and a root-tracking loop at 2–4 σ values.
**Feasibility.** Low–Med (probe). **Value.** A new diagnostic of the zeros' statistics (velocity distribution, crossings) and a per-zero "RH margin" meter.
**Cheapest probe.** <1h: compute the zeros of the smoothed Z(t; σ) for σ = 0.1, 0.2, 0.4 (fraction of the mean spacing) at height 10³–10⁴; report max |Im| clearance and the velocity histogram.

### AN-6. Null-broadening robustness: the certificate's tolerance to off-line location — NEW (framing)
**Idea.** Robust beamforming broadens nulls so they survive position error; the certificate's "null" is at the off-line content, and its tolerance to the *location* of off-line pairs is measured by [P10.4]'s cross-pair subadditivity (clustered pairs cost less than p·(1,1)-planes).
**Analogy.** Broadened nulls ↔ tolerance to off-line pair location.
**Needs.** [P10.4]'s probe. **Feasibility.** Low. **Value.** Documentation; ties the null-robustness literature to the p-cost slack question.
**Cheapest probe.** None (fold into [P10.4]).

---

## Pool 4 — Microwave/RF: cavities, waveguides, S-parameters

### RF-1. Cavity Q / loss-tangent reading of the certificate — KNOWN-OPEN (framing)
**Idea.** bound/N = 2 − HS²/N = 2 − (1 + loss), where the "loss tangent" is the off-diagonal pair sum; the certificate is a Q-type figure (2 minus the loss). Improving the certificate = reducing the pair-sum "loss" (higher Q); P6's deficit is the finite-height loss.
**Analogy.** Cavity Q (stored/lost energy) ↔ on-line count / off-diagonal pair sum.
**Needs.** None (framing; content = [snd]'s arithmetic-deficit reading). **Feasibility.** immediate. **Value.** Documentation.
**Cheapest probe.** None.

### RF-2. Degeneracy splitting under symmetry breaking: the (1,1)-plane as mode splitting — KNOWN-OPEN (content = [P10.4])
**Idea.** In a symmetric cavity, degenerate modes split under symmetry-breaking perturbations (⟨φ₁|δH|φ₂⟩); an off-line pair splits the certificate spectrum into a (1,1)-plane (Claim 2.3, PROVEN) — the FE's ρ ↔ 1−ρ̄ symmetry broken by off-line zeros. The splitting magnitude = the cross-pair corrections ([P10.4]'s probe).
**Analogy.** Degeneracy splitting ↔ the off-line pair's signature.
**Needs.** [P10.4]'s probe. **Feasibility.** Low. **Value.** Documentation.
**Cheapest probe.** None (fold into [P10.4]).

### RF-3. Waveguide cutoff ladder + the "group velocity" of the zero beads — NEW (merged with AN-5)
**Idea.** A waveguide's cutoff frequencies form a spectral ladder (the transverse Laplacian's eigenvalues); the zeros' "cutoff ladder" is the RvM count N(T). The group velocity of a zero "bead" (its drift in height under a parameter) is the level-dynamics velocity — merged with AN-5's probe.
**Analogy.** Waveguide dispersion (phase vs group velocity) ↔ zero drift under smoothing.
**Needs.** AN-5's probe. **Feasibility.** Low–Med. **Value.** Folded.
**Cheapest probe.** AN-5's.

### RF-4. S-matrix unitarity / passivity: the plateau bound and the off-line "dissipation" — KNOWN-OPEN (content = [P2.1], [C-PS2])
**Idea.** A lossless network's S-matrix is unitary, giving the per-instance bound |tr U^τ|² ≤ N — the plateau ([P2.1]); off-line pairs are the "dissipation" (non-unitarity); the return loss / VSWR of the configuration is its mismatch vs the crystal.
**Analogy.** S-matrix unitarity ↔ the plateau protection; dissipation ↔ off-line content.
**Needs.** None (framing). **Feasibility.** immediate. **Value.** Documentation.
**Cheapest probe.** None.

### RF-5. Friis cascade of the moment hierarchy: the error budget is dominated by the first stage — NEW (framing for P6)
**Idea.** The Friis formula: a cascaded receiver's noise figure is dominated by the first stage (each later stage's noise is divided by the preceding gains). The certificate's moment hierarchy (m₁, m₂, m₃, …) is a cascade: the mean density (RvM, first "stage") dominates the error budget; each higher moment's error enters *divided by* the lower moments' contributions. P6's error bookkeeping has a cascade structure — the 2nd moment's O(1/√log T)-class error ([AF]) is suppressed by the 1st stage's "gain".
**Analogy.** Friis cascade (first stage dominates the noise figure) ↔ moment-order error suppression.
**Needs.** A P6 error-cascade writeup (which moment's error dominates at each order; the [AF] numbers as the first two stages). **Feasibility.** Low. **Value.** A principled reason the 2nd-moment constant is the robust one and the 3rd moment (P2) is the natural next "stage".
**Cheapest probe.** <1h: assemble the error-cascade table from [AF]/[CD-V3] numbers; check the suppression ratios.

### RF-6. Smith-chart / reflection-coefficient diagnostic — KNOWN-OPEN (folded into EE-3)
**Idea.** The certificate data mapped by the Möbius transform to the circle (EE-3) plotted as reflection coefficients; the "reflection" magnitude = the reciprocal defect.
**Needs.** EE-3's probe. **Feasibility.** Low. **Value.** Folded.
**Cheapest probe.** EE-3's.

---

## Pool 5 — Aerospace/control-adjacent: flutter, gyroscopics, topology optimization

### AE-1. Flutter boundary: the smoothed zeros' "aeroelastic margin" — NEW (merged with AN-5)
**Idea.** Flutter = a complex eigenvalue crossing the imaginary axis as a parameter grows; RH = no zero of the zero-sum function crosses the critical line for any smoothing. The p-k method tracks modes and detects onset by frequency coalescence (two modes coming together before departure) — the analog of off-line pairing. The deliverable: per-zero "aeroelastic margin" (minimal clearance from the line under smoothing variation) and the coalescence statistic.
**Analogy.** p-k tracking / flutter onset ↔ zero trajectories under smoothing; coalescence ↔ off-line pairing.
**Needs.** AN-5's probe. **Feasibility.** Low–Med. **Value.** A genuinely new per-zero margin meter.
**Cheapest probe.** AN-5's.

### AE-2. Thomson–Tait–Chetaev: "adding dissipation can destabilize" ↔ the data paradox — KNOWN-OPEN (content = [AL] LP-B′)
**Idea.** Gyrodynamics' TTC theorem: damping a stable gyroscopic system can make it unstable. The certificate-side analog is the measured antimonotonicity (SM-6): adding pair-correlation data (rows) LOWERS the certified value (0.89 → 0.6818, [AL] LP-B′). "More data ⟹ lower bound" is the counterintuitive, documented fact that any funding decision must respect.
**Analogy.** TTC destabilization-by-damping ↔ antimonotone certificate value in the data.
**Needs.** None (the LP-B′ numbers are [AL]-computed). **Feasibility.** immediate. **Value.** Documentation; a memorable name for the antimonotonicity.
**Cheapest probe.** None.

### AE-3. Topology-optimization "minimum member size": the checkerboard filter IS the missing repulsion input — KNOWN-OPEN (naming + pricing for [P1.4])
**Idea.** Topology optimization suppresses checkerboard patterns (fine-periodic artifacts) with a minimum-feature-size filter; the 256-law IS the checkerboard (fine 256-periodic marked structure). The analog filter on configurations — a minimum-zero-spacing / no-fine-periodicity constraint — is exactly the repulsion input [P1.4] (KNOWN-OPEN, the only proven-route-unblocking input). The engineering literature provides the *form* of such constraints and the tradition that fine-periodic optima are artifacts.
**Analogy.** Checkerboard suppression / minimum member size ↔ minimum zero spacing / no fine periodicity.
**Needs.** The [P1.4] LP with a min-gap constraint (existing [AC] machinery); the ceiling(ε) curve.
**Feasibility.** Low (probe). **Value.** The cleanest engineering name for the missing input, plus the pricing curve.
**Cheapest probe.** <1h: forbid adjacent occupied cells in the 256-law LP; re-solve; report the new simple fraction (the ceiling(ε) at ε = one cell).

### AE-4. Ground vibration test = the V1 spectrum experiment — KNOWN-OPEN (content = [CD-V1])
**Idea.** Modal-parameter extraction from a GVT ↔ the W_T spectrum measurement [CD-V1]; the modal effective mass ↔ SM-8's participation factors.
**Needs.** None. **Feasibility.** Low. **Value.** Documentation.
**Cheapest probe.** None.

### AE-5. Gain/phase-margin report: the row shadow prices as per-row margins — NEW (diagnostic on [AL] numbers)
**Idea.** Classical margins (gain margin, phase margin) quantify robustness; the certificate's per-row "gain margins" are the drop-row shadow prices ([AL]: rows 64–192 are the load-bearing ones, ~1.5–2·10⁻³ each; rows 254–256 near-zero). The "phase margin" is the unknown beyond-1 phase ([P6.4]). A margin report says which data is load-bearing and how much error each row tolerates.
**Analogy.** Gain/phase margins ↔ row shadow prices / unknown phase.
**Needs.** None (the drop-row numbers are [AL]-computed). **Feasibility.** Low. **Value.** P7 diagnostics: where the certificate is sensitive and where it is robust.
**Cheapest probe.** None (read [AL] §3).

### AE-6. Compliance duality: the certificate as compliance, the LP dual as the adjoint — KNOWN-OPEN (framing)
**Idea.** Structural optimization's compliance minimization has a duality (compliance = max over admissible stress fields of ...); the certificate (2 − bound is the "compliance") and its LP dual ([AL]) are the same primal/dual pair — the in-class closure is the "adjoint solve".
**Analogy.** Compliance duality ↔ the certificate LP duality.
**Needs.** None. **Feasibility.** immediate. **Value.** Documentation.
**Cheapest probe.** None.

---

## Pool 6 — Heat transfer/thermo: Stefan, critical radius, thermal buckling

### HT-1. Stefan-front measurement of the u<1 deficit: pinned front + height sign-crossover — TESTED-OPEN (Probe C run)
**Idea.** Stefan problems have moving boundaries whose position is a dynamical variable; the finite-T deficit's "front" (the largest normalized distance u where the pair sum departs from the sine-kernel value) would drift with height if it were a true moving boundary. **Probe C (code-backed)**: the front is **pinned at u < 1** at every height (no drift), and the deficit has a **height sign-crossover**: ABOVE the sine kernel (over-correlation, +0.04…+0.09) for γ ≲ 1500 (LMFDB cross-checked), crossing to BELOW (extra repulsion) for γ ≳ 2500 with magnitude growing to ≈ −0.08 at γ ≈ 9000 (5 disjoint windows, internally density-1-rescaled). The deficit does not visibly decay over γ ∈ [2500, 9900] in this normalization — consistent with [val-001]'s INCONCLUSIVE and sharper than [R6]'s global-rescale number.
**Analogy.** Stefan moving boundary ↔ the deficit front; the front's pinning ↔ a stationary short-range arithmetic structure.
**Needs.** Extend to larger heights (tools/zeta-rs zeros at 10⁵) to test whether the magnitude growth continues or turns; cross-check with the [AF] cosine-window normalization.
**Feasibility.** Low (probe run; extension needs new zeros). **Value.** The first height-profile of the finite-T deficit; qualifies the "Δ → 0" reading and relocates P6's mechanism (height-dependent short-range repulsion).
**Cheapest probe.** Done; extension = new zeros + same script.

### HT-2. Critical radius of insulation = the bandwidth-one wall — NEW (framing + diagnostic)
**Idea.** Insulation's critical radius r_cr = k/h is where adding insulation flips from helping to hurting (added surface area beats added resistance). The certificate's "critical radius" is the optimal bandwidth λ* = 1 (Theorem C, PROVEN): below λ* more window helps (more independent measurements, the λN dimension cap, Prop 7.4); above, the Poisson completion breaks and the off-diagonal pollution dominates. The two-term model value(λ) = (dimension gain λN) − (pair-pollution loss) flips at λ = 1.
**Analogy.** Critical radius ↔ optimal bandwidth; over-insulation loss ↔ beyond-1 pair pollution.
**Needs.** The [CD-V5] LP data extended over λ; plot value(λ) and locate the flip. **Feasibility.** Low. **Value.** A clean two-term mental model of the wall and a diagnostic confirmation.
**Cheapest probe.** <1h: [CD-V5] LP at λ ∈ {0.5, 0.75, 1, 1.04, 1.26, 1.70}; report the flip.

### HT-3. Glassy aging of the finite-T deficit — NEW (diagnostic; reframes [val-001] target 3)
**Idea.** The measured ~1/log T decay with nonzero fitted intercepts ([val-001]: all fits have intercepts 0.014–0.037) is the signature of glassy aging — a system with a hierarchy of relaxation timescales (the prime sums at all scales up to T) relaxes logarithmically and shows an apparent plateau in any finite window. The "intercepts" are the aging plateau, not a failure to converge; the prediction is that the deficit will not settle at a power law.
**Analogy.** Spin-glass aging (1/log t, plateau) ↔ the certificate deficit's decay.
**Needs.** Extend the [AF] trend to larger T; fit Δ = C/log^β T and compare with the intercept fits. **Feasibility.** Low. **Value.** A testable physical explanation of the INCONCLUSIVE; supports HT-1's "height-dependent, not decaying" reading.
**Cheapest probe.** <30min: refit [AF]'s 10 points against Δ = C/log^β T (expect β ≈ 1).

### HT-4. Thermal buckling margin: the distance of reality from the crystal — KNOWN-OPEN (content = [snd])
**Idea.** Thermal buckling occurs when the thermal load crosses the critical value; the certificate's "thermal margin" is the sandbox Δ (0.03–0.05 at T = 100–1300, [snd]) — the measured distance of reality from the crystal threshold.
**Analogy.** Thermal buckling margin ↔ the certificate's finite-T overshoot.
**Needs.** None. **Feasibility.** immediate. **Value.** Documentation.
**Cheapest probe.** None.

### HT-5. Lumped-model reduction of the moment hierarchy — KNOWN-OPEN (framing)
**Idea.** Thermal networks are lumped to few nodes for control; the moment hierarchy (m₂, m₃, m₄ ↔ 2/3, ?, 13/18, [AM]) is the "lumping" of the zero distribution — each moment pair is a lumped node of the certificate.
**Analogy.** Lumped thermal networks ↔ the moment-order capacity roadmap [CD-V4].
**Needs.** None. **Feasibility.** immediate. **Value.** Documentation.
**Cheapest probe.** None.

### HT-6. Fourier-number / time-constant report of the deficit — NEW (folded into HT-1/HT-3)
**Idea.** The dimensionless "time" at which the deficit decays below a threshold is a thermal time constant; for the certificate the "time constant" is itself growing (logarithmically) — the glassy reading.
**Needs.** HT-1/HT-3's probes. **Feasibility.** Low. **Value.** Folded.
**Cheapest probe.** HT-3's.

---

## TOP 10 (EV × feasibility × cheap-probe), engineering-specific

1. **HT-1/AN-5 — the height-profile of the u<1 deficit (PROBE RUN: pinned front + sign crossover) and the p-k/level-dynamics tracking of the smoothed zeros.** The first is the strongest *measured* P6 finding this round (the deficit is height-dependent, front pinned — qualifies [val-001]'s INCONCLUSIVE); the second is a new diagnostic family (per-zero "flutter margin", velocity distribution) probing beyond pair correlation. Probes: done (HT-1); AN-5 <1h.
2. **SM-1 — Koiter imperfection-sensitivity of the off-line injection curve (PROBE RUN: thresholded + superlinear).** A mechanism tag for how the certificate dies under small RH failure; extend with 2 sandbox runs. Cheap.
3. **AN-1/SM-4 — the robustness audit pair: box-sensitivity (PROBE RUN: dv/dbox = |E(1)| exactly — strong fragility refuted) and the Temple bracket on the finite-T certificate.** P7 diagnostics that state precisely how robust the closure and the finite-T measurements are. Cheap (Temple <1h).
4. **EE-1 — the elliptic/Cauer exact in-class certificate.** The concrete path to the exact 0.6818 certificate (same prize as [P5.4]/[P7.6], new toolkit). Probe: contact-set read-off <1h; solve Med–High.
5. **EE-3 — the reciprocal-defect (palindromic) off-line meter under the Möbius map.** A new zero-free diagnostic with different error structure than W_T's moments. Probe <1h.
6. **AE-3 — topology-optimization "minimum member size" = the repulsion input, priced.** The cleanest engineering name for the only input that breaks the ceiling ([P1.4]) plus the ceiling(ε) curve. Probe <1h (forbid adjacent cells in the 256-law LP).
7. **EE-6/AN-1-row — the input-conditioning audit (row-perturbation propagation, per-row gain margins).** Quantifies how much the P6 errors can move the constant. Probe <1h from [AL] numbers.
8. **SM-2 — the pin-fraction / spectral-concentration diagnostic** (bound = 1 − mean((λ−1)²), PROVEN; measure the pin fraction vs T). Cheap.
9. **HT-3/SM-7 — the glassy-aging reading of the deficit** (reframes the validator's INCONCLUSIVE into a testable ansatz; predicts no power-law settling). Cheap.
10. **EE-7 — the diagonal-loading numerical audit** (bound(ε) ≈ bound − ε²N, PROVEN; confirms the finite-T numbers are conditioning-stable). <30min.

**Strategic reading.** The engineering angle produced one genuinely new *measured* finding — the height sign-crossover and pinned front of the u<1 deficit (Probe C, HT-1), which sharpens [R6] and materially qualifies the "Δ → 0" reading of [AF]/[val-001]. It produced two honest robustness audits (Probe B: the in-class gain is NOT superdirective-fragile — the gain lives in p₀, not the box; Probe A: off-line damage is thresholded and superlinear). The rest is: one exact-in-class route with a new toolkit (EE-1), two new zero-free diagnostics (EE-3, AN-5), and a set of framings that re-derive the known walls in engineering vocabulary (SM-6/AE-2 data paradox, HT-2 critical radius, EE-8 grating lobes, RF-4 unitarity) — each useful to stop re-derivation. The persistent wall — beyond-bandwidth-1 F, third moments, repulsion — is unchanged; engineering physics adds names, margins, and one new measurement, not new proven inputs.

---

## WILD section (deliberately provocative; honestly evaluated; each labeled)

### W-E1. "The zeros are the flutter modes of a structure whose stiffness is the Weil form; RH ⟺ the structure never flutters at any speed" — CONJECTURED (argument-principle by construction)
**For:** the p-k tracking (AN-5/AE-1) is a genuine new probe; a flutter reading gives a "why" for the pairing structure.
**Against:** the "structure" is the explicit formula renamed; the provable content is RvM-style counting (C-NY1). Keep the probe, discard the proof claim.

### W-E2. "0.6818 is a superdirective gain; the certificate class is maximally fragile" — CONJECTURED (strong form REFUTED by Probe B)
**For:** the antenna Q-limit vocabulary fits the slope/curvature budgets.
**Against:** Probe B: dv/dbox = |E(1)| = 2.5·10⁻⁶ exactly; the gain lives in p₀, and a 10% box error moves the value by 2.5·10⁻⁷. The closure is robust to the modeling box; the fragile datum is p₀ itself (shadow price 1, [AL]) — which is a *configuration* input, not a modeling assumption. Honest verdict: the fragility worry is misplaced.

### W-E3. "The deficit is glassy aging; RH would be the structural glass transition" — CONJECTURED (the aging reading is testable)
**For:** the ~1/log T decay with nonzero intercepts is the textbook aging signature (HT-3); the plateau prediction is falsifiable with more zeros.
**Against:** the transition language is decoration; the content is a fit to ten data points (now sharpened by Probe C's height-profile). Keep HT-3's ansatz, drop the transition slogan.

### W-E4. "The 256-law is a checkerboard; topology optimization proves checkerboards are numerical artifacts and must be filtered" — CONJECTURED (the filter IS the missing input)
**For:** the law is a fine-periodic marked structure exactly of the checkerboard type; minimum-member-size filtering is the standard remedy (AE-3).
**Against:** no *proven* filter applies to the zero configuration — the law satisfies all proven inputs; a filter is a repulsion/regularity input ([P1.4]), which is KNOWN-OPEN. Honest verdict: the engineering analogy names the missing input; it does not provide it.

### W-E5. "RH is a lossless network; the explicit formula is the S-matrix; unitarity is the plateau" — CONJECTURED (renaming risk)
**For:** the S-matrix unitarity bound is per-instance exact ([P2.1]); off-line pairs read as dissipation.
**Against:** this is [P2.1]/[C-PS2] renamed; no new inequality appears. Keep the "off-line = dissipation" meter, discard the proof claim.

---

## Label inventory

- **NEW** (invented here, untested): SM-2 (identity PROVEN algebraically, measurement probe-now), SM-3, SM-4, SM-7, SM-8, EE-1, EE-3, EE-5, EE-6, EE-7 (formula PROVEN, audit probe-now), AN-5, AN-6, RF-5, AE-1, AE-5, HT-2, HT-3, HT-6, W-E1…W-E5 (conjectured by construction).
- **TESTED-OPEN** (probed this round with code, `tools/ig-eng/`): SM-1 (Probe A: thresholded + superlinear off-line damage), AN-1 (Probe B: dv/dbox = |E(1)| exactly; strong fragility refuted), HT-1 (Probe C: u<1 front pinned; height sign-crossover +0.04…+0.09 below γ≲1500 → −0.08 at γ≈9000; LMFDB cross-checked; 5 disjoint windows).
- **KNOWN-OPEN** (core already flagged; engineering framing/procedure only): SM-5 ([CD-V4]), SM-6 ([AL] LP-B′), EE-2 ([C-NY1]), EE-4 ([AK]/[AL]/[P7.6]), EE-8 ([CD-A5]/[P2.2]), AN-2 ([P7.6]), AN-3 ([P1.1]/[P8.4]), AN-4 ([CD-V5]), RF-1 ([snd]), RF-2 ([P10.4]), RF-4 ([P2.1]/[C-PS2]), RF-6 (folded EE-3), AE-2 ([AL]), AE-3 ([P1.4], naming + pricing new), AE-4 ([CD-V1]), AE-6 ([AL]), HT-4 ([snd]), HT-5 ([CD-V4]).
- **KNOWN-DEAD**: none newly derived this round (the two documented walls — Lemma 3.2 tight on D, in-class ceiling attained — were respected; every vector either adds data outside D, measures, or documents).
- **Cheapest-probe discipline:** every vector has a <1h probe (mpmath/Rust on existing machinery — tools/ig-eng/ scripts, the [AF] finitet crate, the [AL] LP, the [CD-V5] support LP). Nothing requires new heavy compute to *start*; the two extensions that change what we believe (HT-1 at higher heights, HT-3's larger-T trend) need new zeros from tools/zeta-rs.

**Honest closing note.** The engineering-physics angle's strongest contributions this round: (i) a **new measured P6 structure** — the u<1 deficit's height sign-crossover and pinned front (Probe C), which is the first height-profile of the finite-T deficit and materially sharpens the [val-001] INCONCLUSIVE; (ii) two **robustness audits** — the in-class gain is not superdirective-fragile (Probe B: the gain lives in p₀, not the box) and off-line damage is thresholded and superlinear (Probe A); (iii) an exact-in-class route with a new toolkit (EE-1, elliptic/Cauer); (iv) two new zero-free diagnostics (EE-3 reciprocal defect, AN-5 p-k/level dynamics). The framings (data paradox, critical radius, grating lobes, checkerboard filter, Friis cascade, TTC destabilization) independently re-derive the known walls with memorable names — they stop re-derivation and add margins, not new proven inputs. The persistent wall — beyond-bandwidth-1 F, third moments, repulsion — remains the only route to constants ≥ 0.70, and the engineering picture (imperfection sensitivity, supergain, checkerboard filtering) explains *why*: the certificate is a two-moment, intensity-only robust-margin readout, and every escape is a phase/structural/count datum — now with engineering vocabulary attached to each.
