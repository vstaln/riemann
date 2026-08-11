# Idea Generator: ML & ecology attack catalog — diagnostics of the method's real slack, and honest constraint-checking

**Agent:** IDEA GENERATOR (ML + ecology angle). Round 2.
**Purpose:** feed the EXECUTIONER agents. The brief is explicit: these vectors are expected to
**change what we believe about the method's real slack in the realized world** (P7-diagnostics:
empirical form-factor noise; the W_T spectrum vs GUE vs the extremal law), not to prove new
constants. Anything that reads as a *new constraint* (P1/P2) is checked against the already-closed
questions and labeled honestly.
**Honesty protocol:** this file invents no proofs and asserts no new theorems. Facts are labeled
**PROVEN** (Lean / paper / cited attack note) or **CHECKED NUMERICALLY** (our own tools). Standard
facts from outside domains are named at "standard in the field — verify before citing" level;
nothing is claimed from memory as a theorem. Every invented vector is **CONJECTURED by
construction** and carries the label NEW / KNOWN-DEAD / KNOWN-OPEN / TESTED-OPEN plus a cheapest-
first probe (<1h).
**Cross-references:** crossdomain = `idea-generator-crossdomain.md` [CD-V#]/[CD-W#]/[CD-A#];
physics = `idea-generator-physics.md` [P#.#]/[W-P#]; attack notes: attack-kernel [AK],
attack-ceiling [AC], attack-finitet [AF], attack-multiplicity [AM], attack-lpdual [ALP],
attack-qi-sweep [QS], attack-nevanlinna [AN], attack-m29 [M29], attack-f1curve [AF1],
close-inclass-gap [CIG], verification-001 [VER].

---

## 0. The state of the art these vectors must respect (all PROVEN / CHECKED NUMERICALLY)

1. **The method.** Two-moment certificate: `tr W_T = N`, `‖W_T‖²_HS = (1/2 + (1/√2)cot(1/√2))·N =
   1.327499…·N`, `rank ≥ 2tr − ‖·‖²_HS` (Lemma 3.2) gives `s₁ ≥ 0.67250·N` (Theorem D); 2/3 flat,
   5/6 distinct, 0.83625 distinct (optimal window). [AK], [VER §1]
2. **The ceiling and the in-class gap are CLOSED.** The bandwidth-one ceiling `0.681828687…` is
   PROVEN in Lean [AC]; the class-optimal certificate `0.68183123…` is exact and rational, and the
   ceiling is TIGHT [ALP], [CIG]. The 0.6725 → 0.6818 gap is a **certificate-optimality gap, not a
   data gap**: no bandwidth-one datum moves the real-zeros constant. [CIG §0], [AN §0]
3. **No matrix inequality beats the rank–trace on (1,1)-blocks — CONFIRMED still true (this file
   re-checked).** [QS] closed P10.1/P10.3 with a documented negative: the strongest candidate
   (Cauchy–Schwarz on the positive part of Q, `(trQ₊−2b)²/b`) provably dominates Lemma 3.2 term-by-
   term yet vanishes exactly at the sharp configurations that attain the LP minimum. Every vector
   below that touches a matrix inequality is checked against this (§Pool 2, M4).
4. **Beyond-1 form factor is a proven dead end.** [M29]: the Montgomery–Vaughan Hilbert inequality —
   the sharpest proven tool — is ~3.6·10³–3.7·10⁴× too weak at T = 10⁴–10⁶. Any proven input beyond
   α = 1 is out. The F ≡ 1 support curve (0.70 @ 1.04, …) is reproduced [AF1].
5. **The realized finite-T world.** Δ(T) = bound/N − 0.6725 > 0 at every tested T, decaying ~1/log T
   (not 1/T), driven by the off-diagonal pair sum; `W_T` is full-rank in exact arithmetic but
   numerically near-rank-deficient at the f64 floor (rank at 1e-6 threshold is N−2..N−8 for T ≥ 200);
   single samples, idealized C⁰ cosine window (the hardest case). [AF §3–§5, §7]
6. **Empirical form factor noise.** The measured F(α) ≈ |α| on [0,1] is a *trend only* — sample noise
   at N = 3000 is large; beyond α = 1 nothing is resolved. [VER §4] This is the hole the signal-
   processing pool (§Pool 4) can fill.
7. **The extremal law's realized-world mismatch is structural, not just spectral.** All 103.8 billion
   verified zeros are simple and on the line; the extremal law has 1/6 *doubles* and exact
   periodicity. The certificate's moment class cannot see this; the diagnostics below are chosen to
   measure exactly which rigidity/repulsion dimension separates the realized world from the crystal.

**Consequence for ranking:** with the in-class gap closed and beyond-1 proven-dead, the only
high-EV work left is (i) *measurements that change our belief about the slack* (P7-diagnostics),
(ii) *methodological imports that make those measurements reliable*, and (iii) honest
re-confirmations that the "new-constraint" doors are shut. This file is dominated by (i) and (ii).

---

## Pool 1 — Ecology / May's stability theorem

Structural essence (abstracted): a large matrix whose *bulk spectrum* is known to be random, with a
handful of *structured* eigenvalues (spikes / hyperbolic pairs) sitting at the edge; the question is
always *which* eigenvalues are "real structure" and *how close the system sits to its stability
boundary*. That is W_T's exact situation: deterministic prime-side matrix, near-rank-deficient,
with the certificate's slack living at the bottom of the spectrum.

### E1. Spiked-model / outlier detection on the W_T spectrum — NEW (diagnostic)
**Idea:** In May/Girko ecology and Johnstone's spiked covariance model, an eigenvalue of a noisy
matrix is a genuine "signal spike" iff it lies outside the bulk-edge plus the √N-scale fluctuation
band; the *count and location of outliers* estimate the structured content. Map: W_T's spectrum
(finite-T "noise" plays the role of randomness) — count eigenvalues of W_T that fall outside the
null *bulk* predicted by the compression-ensemble model, and locate them relative to the extremal
law's atoms {0, 1, 2}. This is the spike-detection version of the task's "W_T spectrum vs GUE vs
extremal law" question: the extremal law is a 3-spike world, a GUE bulk is spike-free.
**Needs:** W_T spectra ([AF]/[CD-V1] code exists); the null bulk model (compression ensemble,
[P5.3]); a threshold rule (√N fluctuation band).
**Feasibility:** Low. **Cheapest probe (<1h):** finitet spectra → sorted eigenvalues vs the
quarter-circle/arcsine null-bulk band; count eigenvalues above bulk-edge + 2·band; compare with the
p = 0 Gabor model.

### E2. Leverage-score ("keystone") analysis of the zeros on the two-moment bound — NEW (diagnostic)
**Idea:** Ecology's keystone species = nodes whose removal collapses the system. Map: each zero ρ
contributes a rank-one `v_ρ v_ρᵀ` to `W_T = (1/∫ψ²)VᵀV`; its *leverage score* ℓ_ρ = |v_ρ|²/Σ|v_ρ|²
is its share of `tr W_T`, and its cross-terms drive `‖W_T‖²_HS`. Rank the zeros by leverage: does the
certificate's slack concentrate in a few "keystone" zeros (edge/boundary of the grid — an artifact)
or distribute uniformly (arithmetic)? [AF] already suspects the trace deficit is edge-truncation
(§3, §5); this quantifies it per zero.
**Needs:** the V matrix (exists); row norms (trivial).
**Feasibility:** Low. **Cheapest probe (<1h):** from finitet code, print per-zero ℓ_ρ and the per-zero
HS contribution; histogram + identify the top-10 movers and their heights (edge vs interior).

### E3. Local spacing-ratio null test of W_T's bulk vs GUE — NEW (diagnostic)
**Idea:** The Oganesyan–Huse adjacent-gap ratio ⟨r⟩ is a parameter-free universal discriminator:
Poisson ≈ 0.3863, GOE ≈ 0.5307, GUE ≈ 0.5996 (standard ABGR values — verify before citing). Map:
compute ⟨r⟩ on the *bulk* of W_T's eigenvalues (exclude the f64-floor artifact eigenvalues and the
top edge); the value places the compressed spectrum on the Poisson→GUE axis — a "how RMT-like is
the realized certificate matrix" measurement the two moments cannot make.
**Needs:** W_T eigenvalues (exists); a 5-line ratio statistic.
**Feasibility:** Low. **Cheapest probe (<1h):** finitet → ⟨r⟩ on the middle 80% of eigenvalues at
T = 200…700; report vs 0.386/0.531/0.600 and the T-trend.

### E4. Off-line detection-threshold sweep — the certificate's blindness window — TESTED-OPEN (extends [AF] §4.7)
**Idea:** May's boundary: at the stability threshold the system is blind to small structure. Map:
[AF] injected one synthetic off-line pair (β = 0.3) and confirmed the (1,1)-plane structure. NEW:
sweep pair *depth* β and *count* p and record, per (β, p), the smallest β/p at which the finite-T
bound drops below 0.6725 — the certificate's *detection limit* for off-line content in the realized
world. If the bound stays above 0.6725 even for p pairs at depth β ~ 1/log T, then realized-world
slack is larger than the certificate's sensitivity — a quantified "how much off-line structure could
exist without the method noticing".
**Needs:** [AF]'s synthetic-pair machinery (exists); a loop over (β, p).
**Feasibility:** Low. **Cheapest probe (<1h):** extend [AF] §4.7: inject p = 1..8 pairs at β =
0.05..1.2 into the T = 300 form; record bound/N; report the (β,p) where it crosses 0.6725.

### E5. Connectance → bandwidth: May's criterion as the λ ≤ 1 wall — KNOWN-DEAD (framing)
**Idea:** May's `σ√(SC) < 1` threshold makes "high connectance ⇒ generic instability". Map: W_T's
interaction-graph connectance is set by the kernel support = the bandwidth; "too much connectance
⇒ instability" is the λ ≤ 1 wall. Verdict: reframing of the PROVEN wall only — the off-diagonal
prime sums beyond X = T are HL-strength [M29], [CD-A1], [CD-A5]; no new input. Kept on file so
executioners don't re-derive it.

---

## Pool 2 — Machine learning spectral methods

Structural essence: a kernel matrix whose *spectrum* is believed to explain the behavior of a
learner, with a cottage industry of rank/trace/Hilbert–Schmidt bounds and a "double descent"
transition at the interpolation threshold. The certificate is literally a rank–trace bound on a
kernel-like matrix — the transferable content is the *measurement methodology*, not the bounds.

### M1. Eigenvalue counting function of W_T vs the 3-atom extremal law vs GUE — NEW (diagnostic)
**Idea:** The NTK "spectral bias" literature reads the whole eigenvalue *decay curve*, not just two
moments. Map: plot the eigenvalue counting function `N_W(λ) = #{i : λᵢ > λ}` of W_T against (i) the
extremal law's 3-atom step CDF (masses 1/6 at 0, 2/3 at 1, 1/6 at 2), (ii) a GUE bulk CDF. Note the
participation ratio `tr²/‖·‖² = 0.7533·N` is *identical* for the extremal world and the certificate
world (it is a function of the two moments) — the ML "rank-collapse" diagnostic is provably blind
here; the counting function is the first quantity that can actually separate the worlds spectrally.
**Needs:** full spectra (exists).
**Feasibility:** Low. **Cheapest probe (<1h):** finitet → `N_W(λ)` on a log λ grid; report the counts
in [0.9,1.1], [1.9,2.1], [0,1e-6] vs the two models.

### M2. Δ(T) as a "generalization gap": margin distribution over T-windows — NEW (diagnostic; overlaps [P9.1])
**Idea:** DL generalization theory: norm-based bounds are provably loose; the *distribution* of the
data-dependent margin over samples is what matters. Map: Δ(T) is the realized margin; measure its
distribution over adjacent T-windows (variance, min, tail) at fixed scale, and check the "double
descent" shape — is there a scale where the realized slack dips (an interpolation-threshold
signature where W_T's numerical rank drops)? Honest: single-sample noise dominates at [AF]'s heights;
the value is the *variance* measurement (P9.1's probe) plus a double-descent-shaped fit on the
C∞-window data ([AF] §7's recommended next run).
**Needs:** [AF]'s Δ(T) machinery + the C∞ window extension.
**Feasibility:** Low–Med. **Cheapest probe (<1h):** reuse the [AF] table; compute var(Δ) over
overlapping windows at fixed T and fit the log-log slope; report the T where rank(1e-6) − N crosses
−4.

### M3. Nyström tail-trace → inertia-stability budget for measured n₊ — NEW (methodological)
**Idea:** Nyström/random-feature approximation theory bounds the spectral error of a finite-rank
compression by the *tail trace* `Σ_{k>r} λ_k`. Map: W_T is a finite compression of the infinite Weil
form; the tail mass below the certificate's resolution bounds how much the *inertia* (n₊, n₋, n₀)
could shift under the finite-T approximation errors — i.e., a principled uncertainty budget for every
measured n₊/bound. Methodological hygiene for all V1-class diagnostics: near-rank-deficient matrices
have numerically unstable inertia; the tail mass is the honest way to say "n₊ is reliable at scale ε".
**Needs:** spectra (exists); a threshold sweep.
**Feasibility:** Low. **Cheapest probe (<1h):** finitet → tail mass `Σ_{λ<ε·λmax} λ/N` for ε =
1e-3..1e-17; compare with [AF]'s Δ scale; report the largest ε at which the tail exceeds Δ.

### M4. Rank–trace inequalities in deep learning vs Lemma 3.2 — KNOWN-DEAD (checked against [QS])
**Idea:** The brief's explicit question: does the NTK/rank-collapse literature's rank–trace machinery
beat Lemma 3.2 on block-structured matrices? **CHECKED: still no.** The DL participation-ratio /
stable-rank bounds (CS purity–rank, `(trR)²/‖R‖² ≥ 2trR − ‖R‖²`) are exactly the [QS] candidate #1 —
EQUAL in class, gain vanishes at the sharp configurations; Schmidt-number/nuclear-norm-type bounds
are functions of the two moments and cannot move the constant. The only remaining route inside the
method class is the *fourth moment from the prime side* (the paper's own one-sided Chebyshev remark;
HL*(4,λ) → 13/18) — an *arithmetic* input, not a matrix inequality — tracked as [CD-V3]/[P3.4].
Verdict: KNOWN-DEAD as an inequality vector; the M2/M3 measurement methodology above is the surviving
content of this pool.

### M5. IPR / eigenvector localization of W_T's modes — NEW (diagnostic)
**Idea:** In RMT the inverse participation ratio `IPR(u) = Σ|uᵢ|⁴` of eigenvectors separates
delocalized GUE modes (IPR ~ 3/N) from localized/structured modes (IPR = O(1)); spectral clustering
finds structure via top/bottom eigenvectors. Map: compute IPR per eigenvector of W_T — are the
near-null (f64-floor) directions *localized boundary modes* of the C⁰ window (artifact, confirming
[AF] §5's kernel-artifact suspicion) or delocalized arithmetic structure? Are the top modes localized
(spike-like, extremal-law-like)?
**Needs:** eigenvectors (Jacobi in finitet already produces them).
**Feasibility:** Low. **Cheapest probe (<1h):** finitet → IPR histogram per spectral region
(bottom 5%, bulk, top 1%); report the localization pattern at T = 300, 600.

---

## Pool 3 — Spectral graph theory

Structural essence: the certificate is a bound on the *mass* of a configuration given its moments;
graph theory is the science of what spectral structure is forced by combinatorial constraints. The
honest finding of this pool: the graph-theoretic constraint class (expanders, interlacing,
two-eigenvalue graphs, Alon–Boppana) adds **no** constraint on the certificate's data budget — but
the *sandbox* (G1) and *measurement* (G3, G5) transfers are genuinely valuable.

### G1. Ihara-zeta sandbox: run the two-moment pipeline on a known-RH-true finite object — NEW (strong, methodological)
**Idea:** For the Ihara zeta of a regular graph, RH is **proven** — the zeros lie on |u| = 1/√q iff
the adjacency spectrum satisfies |λ| ≤ 2√(q−1) (Ramanujan) — and everything is *finite and exact*
(no asymptotic, no error terms). This is the cleanest possible calibration of "is the 2/3 deficit
arithmetic or method-inherent": [CD-V7]'s sandbox idea, but with a *closed-form* object instead of a
compact hyperbolic surface. Port the two-moment pipeline (Ihara explicit formula = primitive-cycle
counts; density = the graph Weyl law; FE pairing = the Ihara functional equation; the two moments =
exact traces of the adjacency spectrum) and compute the certificate's value on a world where RH
*holds by theorem*: ≈ 1 ⇒ the method's deficit is arithmetic (the realized zeros are the problem);
≈ 2/3 ⇒ the method is inherently lossy (the 0.6725 is a method floor, not an arithmetic fact).
Ramanujan graphs = the crystal-like end; random regular graphs (Alon–Boppana-saturated) = the
GUE-like end.
**Needs:** Ihara zeta explicit formula for a few regular graphs (one page of classical math); the
pipeline port.
**Feasibility:** Med (probe <1h for closed-form graphs). **Cheapest probe (<1h):** K_n and C_n:
write the Ihara zeta, compute the two moments of the θ-configuration (from tr A, tr A² — exact
integers), evaluate `2tr − ‖·‖²` against the true on-line count (all of them, under graph-RH);
report the ratio.

### G2. Alon–Boppana / interlacing / two-eigenvalue constraints — KNOWN-DEAD (checked)
**Idea:** The brief's hint: "are there graph-theoretic constraints forcing MORE eigenvalues of a
pseudorandom graph onto a line?" **CHECKED: no.** (i) Cauchy interlacing for rank-2 updates *is*
Weyl's inequality — exactly Lemma 3.4, already shown optimal [QS §3 #1, #6]; (ii) Alon–Boppana
bounds the *second eigenvalue from below* (spectral gap can't be too large) — irrelevant: the
certificate reads masses, not gaps, and the atoms {0,1,2} have no gap to exploit; (iii) the
two-eigenvalue/strongly-regular classification concerns adjacency spectra with a *realizability*
constraint — the marks are free integer multiplicities, no graph-realizability binds the LP [ALP].
Verdict: KNOWN-DEAD (framing), kept so executioners don't re-derive.

### G3. Expander-mixing discrepancy duality → zero-count discrepancy exponent — NEW (diagnostic)
**Idea:** The expander mixing lemma: spectral gap ↔ set discrepancy. Map: the zero configuration's
"spectral gap" at scale 1/T is the small-α form factor (F(0) = 0 = rigidity); the *discrepancy* is
the deviation of the zero counting function from the smooth RvM law over dyadic boxes — the
Selberg-CLT object (variance ~ √(log log T)-scale fluctuations). NEW measurement: the count-variance
exponent of the real zeros over dyadic boxes vs (i) the GUE/sine-kernel prediction
(variance ~ (1/π²)log L, reported standard — verify), (ii) the extremal law (a periodic crystal:
variance O(1), i.e. *more* uniform in count but with exact *doubles*). The two rigidity notions —
count-variance vs repulsion — *separate the worlds*: the crystal is more rigid in count but less
rigid in repulsion. The certificate sees neither; the measurement tells us which world reality is
closer to, dimension by dimension — the honest "slack" belief update ([CD-V13]/W2 in quantified
form).
**Needs:** LMFDB zero data (exists); a dyadic-box count routine.
**Feasibility:** Low. **Cheapest probe (<1h):** count variance over dyadic boxes at scales T/2^k;
fit variance/mean vs box length; compare with (1/π²)log L and O(1).

### G4. Two-distance-set classification of the extremal law's atoms — KNOWN-DEAD as input; curiosity check
**Idea:** The extremal law's spectrum {0, 1, 2} with masses {1/6, 2/3, 1/6} is a *three-value* object
like the spectra of two-distance sets / strongly regular graphs; the classification literature
(Delsarte–Goethals–Seidel) bounds the sizes of such sets. Honest verdict: the LP is already solved
[ALP]; a constraint the optimum already satisfies changes nothing. The one curiosity: *is* the
(1/6, 2/3, 1/6)-weighted {0,1,2} configuration realizable as a two-distance set? If yes, the extremal
law has a known combinatorial home (a structural *explanation*); if no, it is a free construct and
the crystal is even less forced. Diagnostic/knowledge value only. **Cheapest probe (<1h):** a
literature-scoped check + the two-distance-set existence criteria on (2/3, 1/6) masses.

### G5. Four-point pseudorandomness probe (Chung–Graham–Wilson equivalence) — NEW (diagnostic)
**Idea:** Pseudorandomness theory (Chung–Graham–Wilson): many seemingly-different quasirandom
properties are *equivalent* — measuring ANY one certifies the others; the "4-cycle count" is the
canonical higher-order witness. Map: the zeros' 2-point pseudorandomness (F ≡ 1) is the PCC;
the 4-point analog (the "count of 4-cycles" = the empirical 4-point correlation statistic) is a
*higher-order* witness that is *computable from data* and NOT implied by the 2-point check — the
first empirical probe of the higher-order structure that the V4 moment-capacity roadmap ([CD-V4])
prices. If the empirical 4-point statistic is near its GUE value, the realized world is
"pseudorandom" to higher order — supporting the conjectural inputs' roadmap; if not, the
higher-moment route loses prior support.
**Needs:** the zeros' 4-point correlation with binning on differences (O(N²·bins²)-style sum —
feasible in Rust for N = 3000).
**Feasibility:** Med. **Cheapest probe (<1h):** diagonal-dominated 4-point statistic on the 1000
cached zeros (34 digits) vs the GUE Slater value; report the ratio.

---

## Pool 4 — Time series / signal processing

Structural essence: the zeros' form factor F(α) is the *Bartlett spectrum* of a point process; the
certificate is a single-window (single-taper) spectral estimate. The classical lesson of spectral
estimation — window choice controls leakage, multi-window averaging controls variance — maps directly
onto the two pain points we already measured: [VER §4]'s noisy empirical F and [AF]'s C⁰-window
artifact.

### S1. Multitaper (DPSS) estimation of the empirical form factor F(α) beyond 1 — NEW (methodological; directly serves the brief's "empirical form factor noise")
**Idea:** Thomson's multitaper method averages tapered periodograms over a bank of orthogonal
Slepian (DPSS) tapers with adaptive weights — the standard variance reducer at fixed bias. Map: the
zeros' pair correlation ↔ F is a point-process Bartlett spectrum; estimate F(α), α ∈ [0,3], with a
DPSS taper bank on the pair-correlation window. [VER §4]'s "trend only, large sample noise at
N = 3000" is exactly the regime multitaper fixes. The result is the first *resolved* empirical
statement about F beyond α = 1 — which [M29] proved unreachable *theoretically* but which still
calibrates belief: if F hugs 1 for α ∈ (1, 2) with tight error bars, the realized world is
consistent with the conjectural input that would crush the ceiling (supporting the conditional
roadmap [CD-V4]/[CD-V5]); if it dips, the conditional roadmap loses prior support.
**Needs:** `scipy.signal.windows.dpss`; the pair-correlation data (exists).
**Feasibility:** Low. **Cheapest probe (<1h):** DPSS (5 tapers) estimate of F(α) at α ∈ {0.5, 1.0,
1.2, 1.5, 2.0} vs the single-window estimate; report error bars.

### S2. DPSS multi-window *certificate* probe — [CD-V18]'s question, with the right windows — TESTED-OPEN (extends [CD-V18], [AF §7])
**Idea:** The brief asks whether a multi-window estimator beats the single-window certificate the way
[CD-V18] speculated. Honest mechanics: a bank of orthogonal windows at critical density enlarges the
compression block; the *ratio* tr²/‖·‖² sets the constant and the extremal configuration
re-normalizes — expectation: no asymptotic gain, cheap to check with DPSS (the natural orthogonal
multi-tapers). The genuinely useful fragment: DPSS windows have optimal out-of-band concentration —
they are the cleanest realization of [AF §7]'s recommended "smoothed C∞ window" for the *finite-T*
measurement, directly improving the Δ(T) trend (removing the boundary artifact that the C⁰ cosine
worst-case introduces). Two birds: settle [CD-V18]'s question AND upgrade the [AF] numerics.
**Needs:** DPSS windows; finitet machinery extended to a second window.
**Feasibility:** Low. **Cheapest probe (<1h):** build W_T with the flat window + one DPSS window at
the same bandwidth; compute the joint two moments; compare the ratio with the single-window ratio.

### S3. Coherence / cross-spectral residual between the zero side and the prime side — NEW (diagnostic)
**Idea:** Signal-processing coherence measures shared spectral power. Map: the explicit formula
couples the zero side and prime side — *perfect* coherence at the main-term level by construction;
the informative object is the *residual* coherence of the error terms: is the finite-T deficit Δ(T)
driven by zero-side pair-correlation ([AF]'s Ψ₂ diagnosis) or by prime-side fluctuation? A dyadic-
window cross-spectrum of (zero-side sums) vs (prime-side sums) localizes at which scale the identity
decorrelates — i.e., the effective range of the "kernel artifact" and where the slack concentrates.
**Needs:** finitet code extended to print both sides of the explicit formula per dyadic window.
**Feasibility:** Low–Med. **Cheapest probe (<1h):** correlation of the two sides' deviations over
dyadic windows at T = 100..700; report the scale at which the correlation first drops below 0.9.

### S4. Eigenvalue thresholding / robust n₊ — NEW (methodological)
**Idea:** Low-rank denoising (Donoho–Gavish-style optimal shrinkage) separates "signal eigenvalues"
from a "noise floor" by thresholding. Map: W_T is numerically near-rank-deficient; the near-null
eigenvalues are boundary/f64 artifacts — a *principled* threshold rule (with a documented rationale,
not a theorem — the standard thresholds assume iid noise, and W_T's "noise" is structured) gives a
robust way to report n₊ and to clean the spectrum for every V1-class diagnostic (E1, E3, M1, M5).
**Needs:** spectra (exists). **Feasibility:** Low. **Cheapest probe (<1h):** report n₊(W_T) under
thresholds ε·λmax for ε = 1e-3..1e-17; document the sensitivity (n₊ stable? n₋ stays 0?).

---

## Pool 5 — Epidemiology / branching

Structural essence: a process with a fixed *mean* density (the FE normalization = R0 = 1, critical)
whose *fluctuations* about the mean carry the information; the threshold theorems (PGF criticality,
extinction probability, next-generation spectral radius) are all *mean-based* — exactly like the
two-moment certificate. The transferable content: *variance-based criticality diagnostics* and the
*empirical-estimation methodology* (generation intervals, contact matrices).

### B1. Index of dispersion / count-variance exponent of the zeros vs crystal vs GUE — NEW (diagnostic; twin of G3)
**Idea:** Branching criticality: the index of dispersion var/mean is 1 for a Poisson process
(critical, random), > 1 for overdispersed, < 1 for rigid/underdispersed. Map: zero counts over boxes:
Poisson = 1; GUE/sine-kernel and ζ (Selberg-CLT) → (1/π²)log L / L → 0 *slowly* (the log factor is
the signature); the extremal crystal → O(1)/L → 0 *faster* (no log factor). The separator between
ζ/GUE (log L/L) and crystal (1/L) is the *log factor* — measurable at moderate box lengths. This is
G3's measurement from the branching angle; cross-referenced, run once.
**Needs:** LMFDB zeros; dyadic-box counts.
**Feasibility:** Low. **Cheapest probe (<1h):** var/mean of counts over dyadic boxes; fit vs L and
L/log L; report which family the exponent belongs to.

### B2. Renewal-equation / generation-interval reading of the explicit formula — KNOWN-DEAD (framing)
**Idea:** The epidemic renewal equation `I(t) = ∫ R0·g(τ)·I(t−τ)dτ` with the Euler–Lotka growth
criterion; the "generation interval" g is the kernel support. Map: the explicit formula is a renewal
equation; the λ ≤ 1 wall is the criticality boundary of the renewal. Verdict: reframing of the
PROVEN wall [M29], [CD-A1], [CD-A5]; no new input. On file to prevent re-derivation.

### B3. Extinction-probability / large-deviation "outbreak" reading — KNOWN-OPEN (overlaps [P9.4], [CD-V13])
**Idea:** The PGF criticality theorem: extinction probability = smallest fixed point of the PGF. Map:
"no off-line pairs" (RH at finite T) = "the zero process is extinct at criticality"; the probability
of an "outbreak" (a crystal-like fluctuation in a box) is a large-deviation object whose rate
function is *determined by the pair correlation* (the covariance). The NEW fragment: the *measured*
rate — if crystal-like fluctuations are astronomically unlikely at the count level, the realized
world is firmly anti-crystal in the counting dimension (complements E4's pair-level blindness).
Diagnostic only; the theory is [P9.4]'s third-moment content. **Cheapest probe (<1h):** from B1's
count data, estimate the empirical rate function's quadratic coefficient vs the covariance
prediction.

### B4. Empirical next-generation / contact-matrix criticality index — NEW (methodological)
**Idea:** Epidemic threshold theory: R0 is the spectral radius of the *next-generation matrix* built
from a *contact matrix*; the estimation methodology regularizes the empirical matrix and reads its
spectral radius. Map: discretize heights into boxes; form the empirical "contact matrix"
`M_ij` = the pair-correlation contribution between boxes i and j (or the explicit-formula
cross-terms); the spectral radius of the *regularized* matrix is a *measurable criticality index* —
"how far is the finite system from the ρ = 1 threshold", with a principled smoothing (shrinkage/
bandwidth) giving error bars. Honest: the content is the min-eigenvalue/margin measurement (E4) in
matrix form, but the contact-matrix *estimation methodology* yields a *stable estimator* of the
margin — a defensible way to report "measured distance to criticality" for the P7 slack story. A
PGF-flavored variant (the empirical offspring PGF of the prime cascade evaluated at s = 1, cf.
[P9.5]) is the same estimator in another guise; [P9.5] remains KNOWN-OPEN as a *route*.
**Feasibility:** Low–Med. **Cheapest probe (<1h):** from the finitet pair data, build the box-scale
contact matrix, row-normalize, report ρ − 1 and its shrinkage sensitivity.

---

## TOP 10 (expected value × feasibility × cheap-probe)

1. **G1 — Ihara-zeta sandbox** (the two-moment pipeline on a known-RH-true *finite exact* object:
   the single most informative "is the 2/3 deficit arithmetic or method-inherent" measurement; the
   probe for K_n/C_n is closed-form, <1h). Med.
2. **S1 — Multitaper empirical F(α) beyond 1** (directly fills the brief's "empirical form-factor
   noise" gap [VER §4]; the only resolved empirical statement available beyond α = 1, which M29 closed
   theoretically). Low.
3. **M1 — W_T eigenvalue counting function vs the 3-atom law vs GUE** (the cleanest "W_T spectrum vs
   GUE vs extremal law" measurement; also proves the ML participation-ratio diagnostic is blind).
   Low.
4. **E4 — Off-line detection-threshold sweep** (extends [AF §4.7]: quantifies how much off-line
   structure could exist without the method noticing — the realized-world slack in pairs). Low.
5. **E3 + M5 — spacing-ratio ⟨r⟩ and IPR of W_T's spectrum** (two parameter-free spectral classifiers:
   where the compressed spectrum sits on the Poisson→GUE axis, and whether the near-null modes are
   boundary artifacts or structure). Low.
6. **G3/B1 — count-variance/discrepancy exponent of the real zeros** (the log-factor separator
   between GUE-like and crystal-like rigidity; a quantitative belief update on the crystal as a model
   of reality). Low.
7. **S2 — DPSS multi-window probe** (settles [CD-V18]'s question AND realizes [AF §7]'s C∞-smoothing
   recommendation in one run — a numeric upgrade to the Δ(T) trend). Low.
8. **M3 — inertia-stability/tail budget** (methodological hygiene: the honest uncertainty for every
   measured n₊/bound at finite T). Low.
9. **M2 — Δ(T) margin distribution + double-descent-shaped check** (the variance of the realized
   slack over T-windows; the P9.1 probe under the ML margin framing). Low–Med.
10. **G5 — empirical 4-point pseudorandomness statistic** (the first higher-order empirical probe;
    feeds the V4 moment-capacity roadmap [CD-V4] with real data). Med.

**Strategic reading.** Every top item is a *diagnostic or a measurement methodology* — consistent
with the brief. The two belief-changing measurements are G1 (is the method itself the bottleneck?)
and S1 (is the realized world consistent with the conjectural beyond-1 input?). The matrix-inequality
and new-constraint doors are all documented shut (M4, G2, E5, B2 — each checked against [QS], [M29],
[ALP], [CIG]); nothing in this catalog proposes a way around Lemma 3.2 or the ceiling, because the
prior rounds proved there is none on the current data budget.

---

## WILD section (deliberately absurd premises; honestly evaluated; each labeled)

### W-E1. "The zeros are an ecosystem parked exactly at May's boundary; RH is the statement that the system is marginally stable" — CONJECTURED (framing)
**For:** W_T's measured min eigenvalue ~1e-17·λmax [AF] is literally "at the stability boundary";
May's lesson — marginally stable systems are generic at high connectance — matches the λ ≤ 1 wall.
**Against:** renaming RH as "marginal stability" adds no provable input; the stability boundary is
already the certificate's positivity boundary by definition. The honest fragment is E4's measured
margin. Verdict: the *measurement* survives (E4); the *claim* does not.

### W-M1. "The certificate is a generalization bound and Δ(T) is the generalization gap; double descent predicts a peak where W_T becomes rank-deficient" — CONJECTURED (framing; the check is real)
**For:** the certificate is literally a norm-based bound; the DL literature's lesson is that such
bounds are loose *because* they are worst-case — the realized slack Δ(T) is the "gap"; if Δ(T) shows
a dip at the T where the numerical rank drops (T ≈ 300 in [AF]), that is an interpolation-threshold
signature.
**Against:** single-sample noise at [AF]'s heights; the "peak" is probably an f64 artifact; no
mechanism lets the gap enter the theorem. Verdict: M2's double-descent-shaped fit is the honest
fragment; the analogy itself is decorative.

### W-G1. "The extremal law's {0,1,2} spectrum with masses {1/6, 2/3, 1/6} is a two-distance set; classification theorems force those masses" — CONJECTURED (likely-false as input; cheap curiosity)
**For:** three-value spectra ↔ two-distance sets / strongly regular graphs is the natural home; if
realizable, the extremal law is a *known combinatorial object*, not an artifact of the LP.
**Against:** no graph-realizability constraint binds the certificate's LP [ALP]; the masses are free
integer multiplicities. Verdict: G4's realizability check is a 1-hour curiosity; the "forced" claim
is KNOWN-DEAD as an input.

### W-S1. "RH + PCC = 'the zeros are spectrally white': F(α) ≡ 1 for all α is flat-spectrum, i.e. the zero process is white noise in the log domain" — CONJECTURED (it is the PCC renamed)
**For:** flat spectrum is the null hypothesis of spectral estimation; the multitaper machinery is
built to *test* whiteness — S1 is the right test statistic.
**Against:** this is the pair-correlation conjecture by another name; no test against the real data
can prove it. Verdict: S1's empirical whiteness test beyond α = 1 is the honest, valuable fragment.

### W-B1. "Off-line pairs are 'superspreading events' of the zero process; the certificate cannot price them because the two moments are mean-based, exactly as R0-threshold theory is mean-based" — CONJECTURED (framing; content is E4)
**For:** the epidemic lesson that *mean-based thresholds miss tail events* is exactly the certificate's
blindness to shallow off-line pairs ([CD-V10]'s "shallow off-line pairs are the irreducible
unknown"); E4 quantifies the blindness.
**Against:** no branching mechanism for off-line pairs is proven; "superspreading" is a metaphor.
Verdict: E4's detection-threshold sweep is the honest content; the metaphor is disposable.

---

## Label inventory

- **NEW** (invented here, untested; conjectured by construction): E1, E2, E3, M1, M2, M3, M5, G1,
  G3, G4 (curiosity), G5, S1, S3, S4, B1, B4, and the WILD fragments that survive as measurements
  (E4's margin, M2's fit, G4's realizability check, S1's whiteness test).
- **TESTED-OPEN** (extends existing measured results, not yet run): E4 (extends [AF §4.7]),
  S2 (extends [CD-V18], [AF §7]).
- **KNOWN-OPEN** (core is open; new framing only): B3 (overlaps [P9.4], [CD-V13]), B4's PGF variant
  (cf. [P9.5]).
- **KNOWN-DEAD** (checked against closed results; documented so executioners don't re-derive):
  E5 (May-connectance = the λ ≤ 1 wall; [M29], [CD-A1], [CD-A5]), M4 (rank–trace inequalities in DL;
  [QS] §2–3 — the brief's "check that no matrix inequality beats the rank–trace on (1,1)-blocks"
  re-confirmed), G2 (Alon–Boppana/interlacing/two-eigenvalue constraints; interlacing = Weyl =
  Lemma 3.4 [QS]), B2 (renewal-equation reframing of the wall), and the non-measurement halves of
  W-E1/W-M1/W-G1/W-S1/W-B1.
- **Cheapest-probe discipline:** every vector has a <1h numeric or literature probe on existing
  machinery (`tools/finitet`, `tools/zeta-rs`, LMFDB caches, scipy DPSS). Nothing here needs heavy
  compute to start.

**Honest closing note.** The two strongest NEW contributions are (i) **G1, the Ihara-zeta sandbox** —
a *finite, exact, RH-true* object on which to run the full two-moment pipeline and settle whether the
method's 0.6725 is arithmetic or inherent, and (ii) **S1, multitaper empirical F(α)** — the first
resolved measurement of the beyond-1 form factor in the realized world, filling the exact gap that
[VER §4] left open and that the brief prioritizes. Everything else is measurement methodology that
changes what we believe about the realized slack (M1, E3/M5, G3/B1, E4, M2) or methodological
hygiene that makes those measurements trustworthy (M3, S4, S2). No vector in this catalog claims a
new constant; the constraint doors are all documented shut, and this file re-confirms the [QS]
verdict the brief asked us to check.
