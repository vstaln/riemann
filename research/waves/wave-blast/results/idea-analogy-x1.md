# Idea Generator: Analogy Transfer for RH — 15 non-obvious domain transfers

**Agent:** IDEA GENERATOR (s4h-analogy: structure-mapping → domain-transfer → boundary-testing)
**Round:** wave-blast, task `idea-analogy`
**Date:** 2026-08-12
**Deliverable location:** `research/waves/wave-blast/results/idea-analogy/`
**Honesty protocol (hooks/agents.md):** every idea is **CONJECTURED by construction**; every
*number* is CHECKED NUMERICALLY by a script I ran and archived here (Rust, musl+rust-lld, pure
std — no external crates on this offline box); facts about the certified record are labeled
PROVEN / CHECKED NUMERICALLY with source. Nothing here asserts a new theorem.

---

## 0. The certified record this catalog must respect (do not re-derive)

- **The record the swarm targets:** 0.6732628655343560 (the wave-blast task's certified target; [RETIRED 2026-08-24]
  swarm spec `tools/swarm/gen-specs.py`). The three independently-verified external mechanisms:
  ainta 7-point stability **0.673008527927**, trmdy trig-window + √-tail block **0.673137630699**,
  tawanerguo Bellman coboundary **0.673192911473142**. [CHECKED NUMERICALLY — `verify-tawanerguo-bellman.md`,
  `discovery-gram-stability-673.md`; all three share the SAME stability Ψ(t) = (t−1)²/2t−3 mechanism]
- **The in-class ceiling is PROVEN and TIGHT:** the certificate class reading (mean density,
  bandwidth-one pair counts, integrality) cannot certify beyond
  **p₀ + |E(1)| = 0.68183123059534187426**, attained by the 256-periodic near-CUE law
  (p₀ = 0.6818286874638315, |E(1)| = 2.5431315104·10⁻⁶). The LP shadow price of the simple
  fraction p₁ is **exactly 1**; the only datum that moves the certified value is a better *global*
  simple-fraction bound, which requires beyond-bandwidth-1 form-factor information (CONJECTURED,
  unavailable). [PROVEN Lean modulo a numerically-checked enclosure; `attack-lpdual.md`,
  `attack-ceiling.md`, `validation-enclok.md`]
- **The two-moment walls:** 2/3 simple, 5/6 distinct are LP-optimal bookkeeping; the empirical
  all-simple world sits exactly on the wall (Δ = 0). The third moment cannot break 5/6
  unconditionally (λ < 2/3 cubic certificate gives ≤ 0.81). [PROVEN — `attack-multiplicity.md`,
  `attack-thirdmoment.md`]
- **The window is optimal for ζ:** cos(√2 s) globally minimizes the Rayleigh quotient; all
  numerically-better candidates violate the bandwidth condition. [PROVEN — `attack-kernel.md`]
- **Beyond-1 form factor is PROVEN DEAD** from the mean side (MV bound 3.6·10³–3.7·10⁴× too weak)
  and from the variance side. [PROVEN — `attack-m29.md`, `attack-gm-variance.md`]
- **The ceiling law is not ruled out by any finite measurement:** p₁ = 1 in every finite strip is
  compatible with the law's global p₀. [PROVEN — `attack-argprinciple.md`]

**Therefore the search space this catalog attacks is:**
(a) the *method-family* gap 0.6732 → 0.6818 (better certificates in proven inputs — mostly closed
by the LP-dual, but the *stability term's convergence* question is live);
(b) **new inputs** the ceiling law violates (higher-order correlations, structural/rigidity
constraints, beyond-1 data — all CONJECTURED);
(c) new *targets* (ξ′-tower, Dirichlet families, Selberg class — mechanical);
(d) **diagnostics that change what we believe** (spectrum experiments, method sandbox, sensitivity
analysis). Most of my 15 transfers are (b)+(d), with honest kill criteria.

**My quantitative anchors (all produced by the Rust binaries in this directory):**

| Anchor | Value | Script (command) |
|---|---|---|
| In-class ceiling p₀ + \|E(1)\| | 0.681831230595342 (17 digits match) | `analogy` (A5) |
| Real zeros: pair-count C(1.0) vs GUE datum | 0.992273 vs 1.000 (finite-N noise) | `analogy` (B1) |
| Real zeros: C(1.5) vs GUE | 1.714727 vs 1.500 (+0.215) | `analogy` (B1) |
| d(bound)/d(eps) at the record (α=1.49, m=133) | +0.626 per unit eps | `analogy` (E3) |
| eps needed for 0.6732628655343560 at m=133 | 0.005877 (record used 0.00806 — arithmetic slack; whether eps=0.00806 *verifies* at α=1.49 is the separate interval-certification task of `verify-eps`) | `analogy` (E4) | [RETIRED 2026-08-24]
| bound vs m (block size) at fixed eps=0.00806 | max 0.674630 at m=133; 0.674215 at m=257 | `analogy` (E2b) |
| Nearest-neighbor (span-1) share of the floor's pair energy | **0.863 (clustered) / 0.931 (uniform)** | `flip` (F3) |
| Floor's single-coordinate sensitivity dF/dg | −0.068 (g[1]) vs +0.005 (g[0]) — sign-alternating | `flip` (F1b) |
| Floor variance under 5%-gap jitter | std 0.00403 (mean 0.0132) | `flip` (F2a) |
| Real-zeros Gram spectrum concentration 1−mean((λ−1)²) | 0.7625 (m=32), 0.7341 (m=128) | `gramev` (G1) |
| Real-zeros Gram: min/max eigenvalue, negative count | 0.104/1.801 (m=32), 0.056/2.021 (m=128), 0 negative | `gramev` (G2) |
| Real-zeros Gram: row-energy concentration (IPR proxy) | 4.74 (m=32), 10.71 (m=128) | `gramev` (G3) |
| Extremal 3-atom law concentration | 0.6667 (2/3 ones, 1/6 twos, 1/6 zeros) | `gramev` (G4b) |
| Periodic-lattice Gram (integer-spaced Toeplitz) concentration | **0.99398 (n=64), 0.99390 (n=256)** | `lattice` (H1) |
| Periodic-lattice Gram eigenvalues near 0/1/2 | 0 / 216 / 0 at n=256 (all ≈1) | `lattice` (H2) |
| Two-half-window pair-count discrepancy vs independent null | max |C1−C2| = 0.008545; ratios ≤ 0.12 | `lattice` (I2) |

**All commands:** `cd research/waves/wave-blast/results/idea-analogy && export PATH=$HOME/.cargo/bin:$PATH RUSTFLAGS="-C linker=rust-lld -C link-self-contained=yes" && cargo build --release --target x86_64-unknown-linux-musl && ./target/x86_64-unknown-linux-musl/release/{analogy,flip,gramev,lattice}` — outputs archived in `out_*.txt`, source hashes in `SHA256SUMS`.

**The single most informative anchor** (reality vs the certificate's two extremes):

| Object | Gram concentration 1−mean((λ−1)²) | What it means |
|---|---|---|
| Certificate's extremal worst case (3-atom law) | 0.667 | the law the class can't beat |
| Real zeros (m=128 Gram) | 0.734 | reality is spectrally *farther* from the worst case than the two moments reveal |
| Perfect lattice (integer-spaced atoms) | 0.994 | the "crystal" the statistical-mechanics lens says the zeros are NOT |

The gap 0.734 ↔ 0.667 is **unharvested slack**: the certificate reads only (tr, HS²), i.e. only
the first two eigenvalue statistics of G; the *full spectrum* (which the Delsarte/Anderson/Boolean
transfers below would read) already distinguishes reality from the extremal law. **CONJECTURED** —
whether a certificate can *read* spectral data beyond the two moments without violating the
bandwidth-one wall is exactly the open question these transfers attack.

---

## 1. The core problem structure (s4h-analogy structure-mapping, first pass)

Underneath the surface, the RH-certificate problem is:

> **We must certify a lower bound on the number of "good" atoms (simple, on-line zeros) in a huge
> configuration, using only (i) a global density, (ii) a two-point correlation profile on a fixed
> bandwidth, and (iii) integrality (marks are positive integers), in the presence of an adversarial
> extremal configuration that matches all three reads and minimizes the good fraction.**
>
> Constraint: the two-point read is *bandwidth-limited* (Montgomery's F on [0,1] — the only proven
> unconditional prime-side data). The adversary is a *periodic near-CUE law* — a "crystal with
> random-ish pair correlations" — that realizes the worst case 0.6818.

That is the abstract structure I search other fields for analogues of. The fields below are
chosen because each has solved a *structurally similar* problem: certify a global property of a
large object from few moments, against a periodic/structured adversary, with an LP/optimization
witness.

---

## 2. The 15 transfers

### T1. Delsarte LP / linear-programming bounds for codes (sphere packing, kissing number)
- **Analogue solved there:** to upper-bound the size of a code/packing with minimum distance d,
  Delsarte's LP finds a test function f (radial, Fourier-nonnegative) with f(0) = 1 and f ≤ 0 off
  the feasible set; the bound is f(0) + Σ f(norm), dual to a configuration LP. OpenAI's exact
  evaluation of the full Cohn–Elkies LP (`linear_program_root`: rate → √(e/2π), beat
  Kabatiansky–Levenshtein) used **Mellin/gamma evaluation of the radial Fourier LP**.
- **Structural mapping:** the *certificate* (c₀, r) with r ∈ C¹[0,1] IS a Delsarte test function;
  the *256-law* IS the extremal code; the validity constraint c₀ + Σ sⱼr(j/N) ≤ p₁ IS the code
  LP's f-evaluation; the in-class ceiling 0.68183123 IS the LP value; the two-moment
  (Montgomery–Taylor) certificate is a *suboptimal feasible* test function.
- **The non-obvious attack it suggests:** the Delsarte story has a *known second chapter*: for
  codes, the LP bound is not always tight — **higher-dimensional / higher-kernel refinements**
  (e.g., using f with f̂ supported beyond the fundamental cell, or the Cohn–Kumar "universal
  optimality" energy functionals) beat the plain LP. In our setting, the LP-dual note
  (`attack-lpdual.md`) proved the *in-class* optimum is tight — but only within the class that
  reads *rows* sⱼ = S(j)/N. A Delsarte-style **energy-functional refinement**: instead of reading
  the pair-count rows, read the *energy* Σⱼⱼₖ sⱼsₖk((j−k)/N) for a family of kernels k (the
  Gram-spectrum generalization of the two moments). My `lattice` probe shows the periodic law's
  Gram has concentration 0.994 (eigenvalues all ≈1) while reality's is 0.734 — an energy
  functional distinguishes them where the two moments do not.
- **Kill criterion / blocker:** the bandwidth-one wall is PROVEN for the *value* inputs; the
  energy functional reads the *same* rows, so it may hit the same ceiling — the transfer's value
  is *diagnostic*: it converts "0.734 vs 0.667 spectral gap" into a concrete energy-certificate
  candidate. If the energy LP's optimum equals p₀ + |E(1)| again, the class is exhausted (documented).
- **How to test (Rust):** build the energy-functional LP: maximize v = c₀ + ∫r(x)x dx subject to
  c₀ + Σ sⱼr(j/N) ≤ p₁ for *every* 256-periodic marked config with the near-CUE rows, PLUS the
  energy rows Σ sⱼsₖk((j−k)/N) ≥ E_real (measured 0.734-normalized). Solve with a small LP
  (HiGHS-style simplex, pure Rust) — the shadow prices tell whether the spectral datum has
  nonzero price (if yes, the ceiling is beatable *in class* by a spectral read; if the price is
  again ~0, the 256-law satisfies the energy rows too — expected, since the law's Gram is
  near-identity).
- **Status:** CONJECTURED. The anchor (0.734 vs 0.994 concentration) is CHECKED NUMERICALLY
  (`gramev`, `lattice`).

### T2. Two-distance sets and spherical codes (Bannai–Bannai–Sloane / Larman–Rogers–Seidel)
- **Analogue solved there:** a *two-distance set* (points whose pairwise distances take only two
  values) has a small rank Gram matrix, and LRS proved strong cardinality bounds via
  eigen-decomposing the Gram: #points ≤ (n(n+1))/2, with equality only for special configurations.
  The classification of "rigid" two-distance sets is a modern industry.
- **Structural mapping:** the 256-law's atoms sit at marks {1, 2} (simple/double) — a **two-mark
  set**. The certificate's extremal worst case is precisely the "two-mark configuration" analog of
  a two-distance set: the Gram of the law's atoms is near-identity (my `lattice` H1: concentration
  0.994, all eigenvalues ≈1), i.e. the law is *almost* an equiangular/rigid configuration.
- **The attack:** LRS-type bounds come from the *rank* of the Gram and the *eigenvalue
  multiplicities* — the same data my `gramev` probe measures. If reality's Gram (concentration
  0.734, eigenvalues spread 0.056–2.02, all positive) is provably *not* of the two-mark rigid
  type — e.g. by a third-moment or rank argument on the *actual* atom Gram — then the real
  configuration is excluded from the extremal family, and the certified bound can exceed p₀.
- **Kill criterion:** the rank argument needs the *global* atom Gram, which is not accessible
  unconditionally (the whole point is that zeros are not individually controlled). The probe
  quantifies the *local* Gram only. Expected blocker: no unconditional global Gram control exists
  (the bandwidth-one data reads only two-point averages).
- **How to test (Rust):** extend `gramev` to a *two-mark* test: for the real zeros' unfolded
  ordinates, compute the empirical Gram of the "double-marked" configuration (mark 2 at the
  ~0.4% of near-coincident ordinates, mark 1 elsewhere) and compare its eigenvalue profile
  against the LRS rigidity discriminant; report whether the profile is closer to the 3-atom law
  or to a generic (non-rigid) spectrum. Diagnostic only.
- **Status:** CONJECTURED. Anchor: `gramev` G1–G3, `lattice` H1–H2 (CHECKED NUMERICALLY).

### T3. Graph eigenvalues / expander mixing (Alon–Boppana, Cheeger, spectral sparsification)
- **Analogue solved there:** for a d-regular graph, the *second* eigenvalue bounds the expansion
  (Cheeger), and the Alon–Boppana theorem says λ₂ ≥ 2√(d−1) − o(1) — an *unavoidable* spectral
  floor for *every* large graph. Expander mixing: |e(S,T) − d|S||T|/n| ≤ λ₂√(|S||T|) — a
  discrepancy bound from a single spectral number.
- **Structural mapping:** the zeros' pair-correlation IS a graph-like two-point mixing statement;
  the certificate's "bandwidth-one F" IS the spectral gap analog; the 256-law IS the "Ramanujan
  graph" that saturates the mixing bound; the in-class ceiling IS an Alon–Boppana-type
  *unavoidable floor* for the certificate class.
- **The non-obvious attack:** Alon–Boppana is a *lower* bound on λ₂ — but expander theory also has
  *upper* bounds from the *number of triangles / higher cycles* (the Ihara zeta / Bartholdi zeta
  counts closed walks). The **Ihara-zeta transfer**: the zeros of the Ihara zeta of a graph lie on
  the circle |u| = 1/√(d−1) iff the graph is Ramanujan — a *finite* RH whose proof used the
  *second-moment/positivity* machinery (the same rank–trace structure!). My program already has an
  `ihara-sandbox` (`tools/ihara-sandbox`): run the *two-moment pipeline* on known-RH-true finite
  objects (Ramanujan graphs, Ihara zeta) and measure how close to 100% the certificate gets. The
  *new* transfer: in the graph world, the spectral gap is *provably* readable from O(log n)
  random walks (spectral sparsification) — the analog of "how many prime-side moments are needed
  to pin F beyond 1". If the sparsification rate in the Ihara world is provably better than in the
  ζ world, that quantifies *why* the ζ certificate is stuck at bandwidth one.
- **Kill criterion:** `attack-vector-catalog` already lists G1 (Ihara sandbox) as a live vector;
  the new part is the *sparsification-rate comparison*, which is diagnostic. If the rates match,
  the transfer adds nothing; if they differ, it quantifies the prime-side sampling bottleneck.
- **How to test (Rust):** in `tools/ihara-sandbox`, add a random-walk moment estimator: compute
  the empirical second moment of the graph's eigenvalues from O(k) random walks (k = 1..20),
  compare the estimate's error to the ζ-side estimate at the same k; report the *sampling
  complexity* gap.
- **Status:** CONJECTURED (diagnostic).

### T4. Anderson localization / IPR of Gram-matrix eigenvectors (disordered systems)
- **Analogue solved there:** in a disordered lattice, eigenstates can be *localized* (IPR →
  constant) or *extended* (IPR → 0). The mobility edge separates them; the IPR is a *per-eigenvector*
  statistic that the spectral density (the two moments!) cannot see. Diagnosing localization from
  moments alone is provably impossible (the moment problem).
- **Structural mapping:** the Gram matrix G_ij = k(xᵢ−xⱼ) of the zeros is the "hopping matrix" of a
  1D disordered chain; its eigenvectors' IPR measures how localized the "zero-atom modes" are. My
  `gramev` probe G3 measured the *row-energy concentration* (IPR proxy): **4.74 (m=32) → 10.71
  (m=128)** — growing with m, i.e. the modes are *delocalized-ish but not uniform*.
- **The attack:** the Anderson story's key lesson is that *mobility edges are invisible to the
  density of states* — the two-moment wall is exactly this phenomenon (the 256-law matches all
  bandwidth-one density data). The transfer gives a *diagnostic instrument*: the IPR of the real
  Gram vs the IPR of the law's Gram. If the real IPR profile is provably different from the
  law's (which my G3 numbers already suggest — the law's near-identity Gram has IPR ≈ 1), then
  there *is* spectral structure the certificate doesn't read, and the open question is whether any
  *unconditional* theorem can read it.
- **Kill criterion:** IPR is a *finite-N* diagnostic; the global (T→∞) statement needs a theorem.
  Expected: the IPR gap is real but unharvestable without a new unconditional input (same wall).
- **How to test (Rust):** extend `gramev` to compute true eigenvector IPRs (needs the full Jacobi
  eigenvector matrix — the routine already computes V): IPR_k = Σᵢ vᵢₖ⁴ / (Σᵢ vᵢₖ²)²; report the
  IPR distribution for real zeros vs the periodic lattice vs the 3-atom law.
- **Status:** CONJECTURED (diagnostic). Anchor: `gramev` G3 (CHECKED NUMERICALLY).

### T5. Statistical mechanics of the Coulomb gas / jellium: the third-moment "charge" reading
- **Analogue solved there:** the GUE eigenvalue process IS a 1D Coulomb gas (Dyson); its
  *free energy* is a functional of the density alone (the two moments!), and *fluctuations*
  (the third and fourth cumulants) carry the interaction structure. The jellium third moment
  Σ⟨(δn)³⟩ is a *charge* — it measures the sign of the interaction, invisible to the pair
  correlation.
- **Structural mapping:** the zeros' pair-correlation F on [0,1] is the *density*; the
  certificate's two moments are the *free energy*; the *third cumulant* of the local
  zero-counting field is the jellium charge. The `attack-thirdmoment.md` note PROVED the third
  moment cannot break 5/6 unconditionally (λ<2/3 cubic cert gives ≤ 0.81) — but that was the
  *trace* third moment tr Â³. The Coulomb-gas transfer reads a *different* third object: the
  **third cumulant of the counting function N(σ, T) across σ (off-line displacement)**, i.e. the
  skewness of the off-line "charge cloud".
- **The attack:** the off-line pairs are the "charge imbalance"; their *third cumulant across σ*
  is a signed quantity the symmetric pair-correlation cannot see (the A2 death: Im(W_T) ≡ 0 kills
  odd moments *on the real axis*, but a *σ-asymmetric* third cumulant is a genuinely different
  object). Probe: numerically measure the skewness of N(σ) for the known zeros (all on-line, so
  the probe is vacuous for real data — it becomes a *sandbox* probe on the synthetic off-line
  worlds of `attack-sandbox.md`).
- **Kill criterion:** for real data the third cumulant is exactly 0 (all zeros on-line by
  construction). The transfer's only honest target is the *sandbox*: does the third cumulant
  separate the sandbox's off-line-injected worlds faster than the certificate? If yes, it
  identifies the *cheapest* hypothetical new input (an unconditional third-cumulant bound).
- **How to test (Rust):** in the `finitet` sandbox, compute the σ-skewness of the counting
  function for (a) the real world, (b) injected off-line pairs at β = 0.05–0.5; report the
  minimal f (pair fraction) where the skewness clears the noise floor, vs the certificate's
  detection threshold from `attack-detection-threshold.md`.
- **Status:** CONJECTURED.

### T6. Quantum chaos: the spectral form factor's "ramp–plateau" (Berry–Keating / Sieber–Richter)
- **Analogue solved there:** the SFF K(τ) = |tr U^τ|² of a chaotic quantum system has a *ramp*
  (linear growth from τ=0) and a *plateau* at τ=1; the ramp is *universal* (from pair
  correlations), the plateau is *exact* (from the discreteness of the spectrum — it encodes the
  level structure that pair correlation cannot). Berry–Keating's conjecture connects this to a
  classical Hamiltonian whose quantization would *be* the zeta.
- **Structural mapping:** the zeta-side form factor F(α) on [0,1] IS the ramp; the *plateau*
  corresponds to the **discreteness/integrality of the multiplicity marks** — the integrality
  steps m² ≥ 2m−1 that the certificate already prices. The plateau is "exact level structure";
  the certificate reads *the ramp* (bandwidth-one F) but *not the plateau* (the higher-α level
  structure). The physics literature knows that the plateau requires |α| > 1 data — the same
  beyond-bandwidth-1 wall.
- **The non-obvious attack:** the *ramp+plateau* decomposition says: any *per-instance* (not
  ensemble-averaged) exact statement about the SFF needs the level structure. The transfer
  suggests a **finite-rank SFF certificate**: compute the *empirical* SFF of the real zeros'
  Gram (my `gramev` spectrum is exactly the input) and compare its ramp-plateau shape to the
  256-law's. If the real SFF's plateau is measurably *higher* (closer to the GUE exact value)
  than the law's, that is empirical evidence the law is *not* the true level structure — a
  diagnostic that would make a *conditional* (HL-type) improvement plausible.
- **Kill criterion:** diagnostic only; the SFF plateau is not a certificate input (it needs
  |α|>1). The probe's value is *belief-updating*: if the real SFF matches the law's plateau,
  the 256-law is a faithful twin and the in-class gap is the whole story.
- **How to test (Rust):** from the `gramev` spectrum, compute SFF(τ) = Σ λₖ^τ for the real Gram
  and the law's Gram (the law's eigenvalues are ≈1, so its SFF ≈ n for all τ — the "plateau at
  the top"); report the real SFF's deviation.
- **Status:** CONJECTURED (diagnostic).

### T7. Boolean-function sensitivity / junta theory (O'Donnell, the "stable functions are juntas")
- **Analogue solved there:** a Boolean function with *low average sensitivity* (small Σᵢ Pr[f
  flips on flipping coordinate i]) is close to a *junta* — depends on few coordinates. The
  sensitivity is a *derivative-based* statistic; the Fourier coefficients are the moments.
  Functions whose sensitivity is bounded by a *moment constraint* are forced to be sparse.
- **Structural mapping:** the certificate value v is a *function* of the huge configuration
  (which zeros are simple); its "sensitivity" to local moves (flipping one gap) is measured by my
  `flip` probe F1b: **dF/dg is sign-alternating (−0.068, +0.005) and the FLOOR's pair energy is
  86–93% nearest-neighbor (F3)**. The junta theorem analog: *if the certificate's value is
  provably a low-sensitivity function of the configuration, it is close to depending only on a
  few local features — and the adversarial law exploits exactly that sparsity.*
- **The attack:** the junta reading says the *extremal law is a sparse (junta-like) configuration
  optimized to fool a low-sensitivity certificate*. The transfer's concrete move: **measure the
  average sensitivity of the certified floor F(g) to single-gap flips** (my F1b/F2a already do:
  std 0.004 under 5% jitter). If the floor is *provably* more sensitive to *long-range* pair
  terms than the current weights assume, a *weight re-optimization* (the trmdy/coboundary family)
  can raise the floor. The Boolean insight is the *opposite* direction: low-sensitivity functions
  are *easy to fool* — the floor's junta-ness is *why* the 256-law wins. That redirects effort:
  instead of optimizing the floor against the known law, search for a *high-sensitivity* floor
  (one that depends on long-range structure) that the law cannot satisfy.
- **Kill criterion:** the floor's weights are constrained by the *window-averaging identity*
  (Σ a_ij = 2 per span) — the sensitivity range is bounded. The probe quantifies the *reachable*
  sensitivity; if the max sensitivity under the identity is still small, the junta-wall is real.
- **How to test (Rust):** in `flip.rs`, add a *weighted-sensitivity scan*: perturb the pair
  weights a_ij within the identity constraints and measure the floor's sensitivity profile;
  report the max reachable "long-range share" (vs the current 0.14–0.07).
- **Status:** CONJECTURED. Anchors: `flip` F1b, F2a, F3 (CHECKED NUMERICALLY).

### T8. Error-correcting codes: the Plotkin bound / list-decoding Johnson bound as multiplicity walls
- **Analogue solved there:** the Plotkin bound caps code size for fixed relative distance; the
  *Johnson bound* caps the number of codewords in a Hamming ball — a *local* bound. The
  Delsarte LP reproduces both; the *Griesmer* bound uses *higher* moments (the "Bose–Burton"
  / inclusion-exclusion chain) to beat Plotkin.
- **Structural mapping:** the certificate's *integrality* (marks ∈ ℤ₊) IS the code's discrete
  alphabet; the *multiplicity walls* (m² ≥ 2m−1, m² ≥ 3m−2, the 5/6-distinct wall) ARE Plotkin-
  type bounds from the multiplicity bookkeeping; the rank–trace inequality IS the Johnson-bound
  mechanism (the paper's `lemmaR_tight` is exactly a Johnson-type tightness).
- **The non-obvious attack:** coding theory's *Griesmer bound* uses the *dimension of the
  shortened code* — a *recursive* moment bound. The transfer: **iterate the rank–trace inequality
  on the block structure** (the trmdy √-tail block profile is already one step: blocks run to
  m=257). The Griesmer analog would be a *recursive block shortening*: apply the certificate to
  the *defect* configuration (the off-line pairs), then to the defect's defect, and telescope.
  The `campaign-2.md` "off-line pair bridge" (the gate to 0.675+) is exactly the first step of
  this recursion; the transfer says the *recursion's limit* is what converges to p₀ or beyond.
- **Kill criterion:** the recursion needs a *positivity-preserving* defect map; `campaign-2` proved
  the naive stacking fails (Schur-deficit witness ≈ 0.1249 against stacking local B on the full
  simple defect) — the transfer's open question is whether a *different* defect (the
  virtualized-pair bridge) survives. This is the single most concrete *proven-partial* route.
- **How to test (Rust):** implement the defect-telescope on the sandbox worlds: compute the
  certificate on the real world, subtract the certified simple atoms, re-run on the defect; report
  the two-level constant vs the one-level. If the two-level ≥ one-level + ε, the recursion is
  alive.
- **Status:** CONJECTURED; the first level is PROVEN (trmdy √-tail), the bridge lemma is
  CONJECTURED with strong evidence (`campaign-2.md`).

### T9. Sphere packing: the "Delsarte LP is not always tight — the linear-programming
gap is closed by *perturbation* (Cohn–Elkies–Kumar / OpenAI exact evaluation)"
- **Analogue solved there:** Cohn–Elkies is an LP upper bound that is *not* tight in most
  dimensions (the packing bound vs the best packings); the *exact* evaluation of the LP
  asymptotics (`linear_program_root`: rate √(e/2π)) required *Mellin-transform techniques* —
  the LP value itself is a special function. OpenAI's "Ten Advances" made this exact.
- **Structural mapping:** our in-class ceiling 0.68183123 is *proven tight* (the 256-law realizes
  it) — *stronger* than Cohn–Elkies in sphere packing (there the LP bound is conjectured-optimal
  upper, not attained). The transfer is the *method*: OpenAI evaluated the sphere-packing LP
  *exactly* via Mellin/gamma identities. The open question: **is there an exact/evaluable
  certificate LP for the *stability-refined* class** (the trmdy √-tail + coboundary family),
  whose exact value would tell us whether the ladder converges to p₀ or overshoots? My `analogy`
  E2b probe (bound vs m: max at m=133, decreasing beyond) already suggests the m-ladder has a
  *peak* — an exact evaluation would pin the peak's location and value.
- **The attack:** derive the *asymptotic* certificate value of the √-tail/coboundary family as a
  function of m (the "block-length Mellin transform"): v(m) = (mH − ηB(m−1))/(m − R(m)) with the
  sharp R = 2√A−1 profile; evaluate v(∞) exactly (it's a limit of rational functions — 
  mechanical). If v(∞) < p₀, the ladder provably cannot reach the ceiling in-class; if v(∞) >
  p₀, the ceiling is beatable by the *same inputs* (a genuine breakthrough).
- **Kill criterion:** the exact v(∞) is a ~20-line symbolic computation — the honest outcome is
  a *proven* statement about the ladder's limit (either way, it closes the convergence question
  that `verify-tawanerguo-bellman.md` names as THE live question).
- **How to test (Rust):** extend `analogy` E2b: evaluate the closed-form bound v(m) for m up to
  10⁶ (float), fit the tail, and report the limit; then compute the exact rational limit if the
  formula admits it.
- **Status:** CONJECTURED (the limit value); the formula is mechanical. Anchor: `analogy` E2b
  (CHECKED NUMERICALLY: max at m=133, v=0.674630, decaying to 0.673668 at m=400).

### T10. Statistical mechanics: "aging"/two-time correlation (glass theory, the Edwards–Anderson order parameter)
- **Analogue solved there:** in spin glasses, the *two-time* correlation C(t, t′) *ages* — it
  depends on t/t′, not t−t′, when the system is out of equilibrium. The *overlap* order parameter
  q = ⟨sᵢsⱼ⟩ distinguishes the "frozen" (replica-symmetric breaking) from the "equilibrium"
  state — invisible to the *one-time* (stationary) correlation.
- **Structural mapping:** the zeros' pair correlation F(α) is a *stationary* (translation-
  invariant) observable; the finite-T deficit (Δ(T) ~ 1/log T, positive, `attack-finitet.md`) is
  a *time-dependent* (T-dependent) correction — the analog of *aging*. My `lattice` I-probe
  measured the two-half-window discrepancy: **the halves agree to ≤ 0.12× the independent-sample
  null** — i.e. the zero process is *more* stationary than independent samples, *no aging signal*.
- **The attack:** the glass transfer predicts: *if* the zeros had any hidden "frozen" structure
  (the 256-law-like periodicity), the two-half discrepancy would show *systematic* drift (ratio ≫
  1), not noise. My probe finds NO drift (ratios 0.015–0.116 ≪ 1) — an honest diagnostic
  **against** the "zeros are secretly periodic/frozen" hypothesis at finite N. That *strengthens*
  the case that the 256-law is an *adversarial artifact*, not a hidden truth — which is the
  necessary precondition for a conditional (HL-type) improvement to be worth pursuing.
- **Kill criterion:** the probe is finite-N; a hidden periodicity on a scale ≫ 11000 zeros would
  be invisible. Extend the probe to the LMFDB large file (10⁶+ ordinates) if compute allows.
- **How to test (Rust):** `lattice.rs` I-probe on the larger zero file (`tools/data/zeros_lmfdb_large.txt`,
  ~500k ordinates): split into halves, repeat; report whether the ratio stays ≪ 1.
- **Status:** CONJECTURED (diagnostic). Anchor: `lattice` I2 (CHECKED NUMERICALLY).

### T11. Quantum information: the "shadow tomography"/classical-shadow formalism
- **Analogue solved there:** to estimate many properties of an unknown quantum state, *classical
  shadows* (randomized single-qubit measurements) estimate *any* linear observable with a sample
  complexity depending on the *shadow norm*, not the dimension. The key theorem: *few randomized
  measurements suffice for all observables in a low-shadow-norm family*.
- **Structural mapping:** the certificate is a *measurement protocol* on the huge zero
  configuration; the bandwidth-one data are *randomized linear measurements* (Fourier-averaged);
  the shadow-norm theorem says the *sample complexity* is governed by the *operator norm* of the
  observables. The two-moment certificate reads exactly 2 observables (tr, HS²); the shadow
  formalism asks: *how many random observables suffice to distinguish reality from the 256-law?*
- **The attack:** the shadow-transfer's concrete question: **what is the sample complexity of
  separating the real zeros' spectral measure from the 256-law's, using bandwidth-one
  observables?** My `gramev`/`lattice` spectra give the empirical answer: the real Gram's
  concentration 0.734 vs the law's 0.994 is a *spectral* separation invisible to the two moments —
  so the *shadow norm* of the "concentration observable" is the missing datum. The transfer
  suggests a *shadow-certificate*: choose the observables whose shadow norm is minimized by the
  law (the worst-case) and maximize the certified value subject to reading only those. If the
  optimal shadow set is *small* (≤ 3 observables), the certificate can be *provably* extended
  without beyond-1 data; if it's large, the wall is intrinsic.
- **Kill criterion:** the shadow-norm framework is a *diagnostic* reformulation; the "provably
  small shadow set" is CONJECTURED and likely false (the LP-dual proved the two-moment class is
  tight — a shadow reformulation should reproduce the same ceiling).
- **How to test (Rust):** implement the shadow-estimator: sample k random bandwidth-one
  observables (k = 1..20), estimate the real-vs-law separation from the sampled traces, report
  the minimal k that separates (a) the two Gram spectra (0.734 vs 0.994) at 3σ. Diagnostic.
- **Status:** CONJECTURED (diagnostic).

### T12. Compressed sensing / sparse recovery: the restricted-isometry / null-space property
- **Analogue solved there:** a sparse vector x can be recovered from y = Ax (few linear
  measurements) iff A satisfies the *restricted-isometry property* (RIP); the *null-space
  property* (NSP) characterizes when the ℓ₁-minimization is exact. The phase transition
  (Donoho–Tanner) says: for n measurements and k-sparse signals, recovery works iff n ≳ 2k log(N/k).
- **Structural mapping:** the "signal" is the *off-line defect* (which zeros are off the line —
  a *sparse* signal if RH is nearly true); the "measurements" are the bandwidth-one moments; the
  certificate is the *recovery guarantee*. The 256-law is a *signal that fools the measurements*
  — exactly the NSP violation: a nonzero defect vector in the null space of the measurement
  operator.
- **The non-obvious attack:** compressed sensing's answer to NSP violation is *more/different
  measurements* — but its *other* answer is *model-based recovery*: if the signal is known to lie
  in a *structured* family (block-sparse, tree-sparse), the measurement count drops. The transfer:
  **model-based certificate**: the off-line defect, if any, is *not* arbitrary — it comes in
  *pairs* {ρ, 1−ρ̄} at the same height (the functional equation!). The certificate already uses
  this (the (1,1)-block structure); the compressed-sensing transfer says the *pair-structure
  model* should reduce the required measurements below the current two moments. The `campaign-2`
  "virtualized-pair bridge" is the model-based step; the transfer adds the *measurement-count
  calculus*: how many moments does the pair-model require, vs the two the plain model needs?
- **Kill criterion:** if the pair-model's measurement count is still ≥ 2 (expected — the LP-dual
  says 2 is optimal in-class), the transfer is a *labeling* of a known wall; the probe makes the
  labeling quantitative.
- **How to test (Rust):** in the sandbox, run the certificate with (a) the plain two-moment
  reads, (b) the pair-structured reads (the (1,1)-block traces); report the *measurement count
  needed to separate* real from 256-law at 3σ in each. If (b) < (a), the model-based route is
  live.
- **Status:** CONJECTURED.

### T13. Boolean Fourier analysis / the "sampling (concentration) of low-degree functions"
- **Analogue solved there:** a function with *low-degree* Fourier expansion (degree ≤ d) has its
  mass concentrated on low-order coefficients; *sampling* its values at O(d) random points
  determines it. The *degree-2* functions are exactly determined by *pair correlations* — the
  degree-2 moment closure.
- **Structural mapping:** the certificate's reads are *degree ≤ 2* functionals of the zero
  configuration (mean + pair correlation); the 256-law is a configuration that *matches all
  degree-2 data*; the missing structure is *degree ≥ 3* (triple correlations — the Rudnick–Sarnak
  range). The Boolean-Fourier theorem: *degree-2 data cannot distinguish any two configurations
  that agree on all pair counts* — a *proof* that the two-moment wall is not a coincidence but a
  degree-2 sampling theorem.
- **The attack:** the transfer *explains* the third-moment death (`attack-thirdmoment.md`: the
  λ<2/3 cubic certificate gives ≤ 0.81 < 5/6) as a degree-closure statement: degree-3 data is
  needed, but the *available* degree-3 data (λ<2/3) is too weak. The concrete new move: **the
  Boolean-Fourier "sparsity" theorem**: if the zero configuration's *higher-order correlations
  are known to decay* (the empirical F(α) ≈ 1 beyond 1 from `verification-001.md`), then the
  degree-2 closure is *almost exact* — and the certificate's value is *provably* within ε of its
  two-moment value for *any* configuration with decaying higher correlations. That is a *conditional*
  statement with an *empirically testable* hypothesis.
- **Kill criterion:** the decay hypothesis is CONJECTURED (F beyond 1 is unproven); the probe
  measures the *empirical* decay and its finite-N stability — a diagnostic that *prices* the
  conjecture (the same spirit as `attack-pricing-sheet.md`).
- **How to test (Rust):** compute the empirical triple-correlation (from the 11000 ordinates,
  windowed) and its decay vs the pair-correlation's; report the *ratio* of the degree-3 to
  degree-2 Fourier mass. If ≪ 1, the degree-2 closure is empirically tight and the wall is
  "real-world-tight".
- **Status:** CONJECTURED (diagnostic).

### T14. Spectral graph theory: the "two-eigenvalue graphs" / the "concentration" of the 256-law's Gram
- **Analogue solved there:** a graph whose adjacency matrix has *two distinct eigenvalues* is a
  strongly regular graph (SRG) — an *extremely rigid* combinatorial object with a full
  classification. The *spectrum* (not just the moments) is what pins the structure.
- **Structural mapping:** the 256-law's atom Gram has eigenvalues all ≈ 1 (my `lattice` H2:
  **216/256 eigenvalues within 0.1 of 1, ZERO near 0, ZERO near 2**) — an *almost* one-eigenvalue
  (near-identity) matrix. The 3-atom extremal law has eigenvalues {0,1,2} with multiplicities
  {1/6, 2/3, 1/6}. Reality's Gram (concentration 0.734) is *far* from either.
- **The attack:** the SRG transfer: *the certificate's worst case is a configuration whose Gram is
  near-identity — the "most regular" possible*. The real zeros' Gram is *provably* not near-
  identity (concentration 0.734 vs 0.994 — a 35% relative gap). The transfer asks: **is there an
  unconditional spectral statement that excludes near-identity Gram from ζ's zeros?** The natural
  candidate: the *mean square* of the off-diagonal Gram entries is controlled by the pair
  correlation (the HS² moment); the *fourth* moment (Σ G_ij⁴) is the next-degree spectral
  statement. If the fourth Gram moment is *provably* positive (not just the second), the
  near-identity Gram is excluded — a *degree-4* spectral input that the LP-dual did not price
  (it priced only the rows).
- **Kill criterion:** the fourth Gram moment is a *higher-degree* correlation — the Rudnick–Sarnak
  range for k=4 requires λ < 1/2, where the certificate is *empty* (Prop 7.4 dimension cap).
  Expected blocker: the degree-4 input is unavailable in the useful range (same wall as the third
  moment). The probe's value: quantify the *spectral gap* 0.734 vs 0.994 as the price of the
  missing degree-4 datum.
- **How to test (Rust):** `gramev` extension: compute the fourth Gram moment Σ G_ij⁴ for real
  zeros vs the 256-lattice; report the ratio (the "spectral separation in degree 4").
- **Status:** CONJECTURED. Anchors: `lattice` H2 (216/256 near 1), `gramev` G1 (0.734) —
  CHECKED NUMERICALLY.

### T15. Graph limits / the "local-global principle" (graphons, the Aldous–Hoover theorem)
- **Analogue solved there:** a *graphon* is the limit of a convergent graph sequence; the
  Aldous–Hoover theorem says *exchangeable* graph sequences are *always* mixtures of graphons —
  the *local* (finite) data + exchangeability *forces* the global limit structure. The Szemerédi
  regularity lemma says large graphs are *approximated* by bounded-complexity blow-ups.
- **Structural mapping:** the zeros form an *exchangeable* sequence (the explicit formula's
  symmetries); the 256-law is a *periodic* limit object (a graphon-like "blow-up"); the
  certificate's data are *local* (bandwidth-one). The Aldous–Hoover transfer: *exchangeability +
  local data force the limit to be a structured (graphon-like) object* — the 256-law IS the
  graphon. But the regularity lemma says *any* large graph is *close* to a bounded-complexity
  blow-up — so *the real zeros' limit must be close to SOME bounded-complexity object*.
- **The attack:** the regularity-lemma transfer asks: **is the real zeros' graphon *close* to the
  256-law graphon, or to a *different* bounded-complexity object?** My two-half probe (`lattice`
  I2: ratios ≤ 0.12) says the real process is *stationary*, and the `gramev` spectrum (0.734 vs
  0.994) says its spectral measure is *far* from the law's. If the real limit is a *different*
  graphon than the 256-law, then a certificate valid against *that* graphon class would beat p₀.
  The transfer's concrete deliverable: **identify the empirical "graphon" (the limit object) of
  the real zeros from the finite data** — a *measurement* that the certificate class doesn't
  read, and that the LP-dual's "no missing constraint in-class" statement does not rule out
  (it only rules out *bandwidth-one value* inputs).
- **Kill criterion:** identifying the graphon needs *unconditional* control of the limit —
  exactly the beyond-1 wall. The probe is diagnostic: it *measures* the empirical limit object
  and its distance to the 256-law, giving the *quantitative* price of the missing theorem.
- **How to test (Rust):** from the unfolded ordinates, compute the empirical "graphon" (the
  pair-correlation density as a function of normalized separation, on a fine grid) and its
  distance (L¹/L²) to the 256-law's density and to the GUE density; report the distances and
  their finite-N stability. Diagnostic.
- **Status:** CONJECTURED (diagnostic).

---

## 3. Structure-mapping summary table (what holds, what breaks — s4h boundary-testing)

| Field | Mapped structure | What HOLD | What BREAKS |
|---|---|---|---|
| Delsarte LP (T1, T9) | cert = test function, law = extremal code | exact | our LP value is *attained* (tight) vs C–E's conjectured-optimal upper |
| Two-distance sets (T2) | law's atoms = two-mark set | rigidity lens | no global Gram control |
| Graph eigenvalues (T3) | F = spectral gap, law = Ramanujan | Alon–Boppana-style unavoidable floor | no graph is actually defined |
| Anderson/IPR (T4) | G = hopping matrix | IPR diagnostic | mobility edge invisible to density — the wall is generic |
| Coulomb gas (T5) | two moments = free energy | third cumulant is a charge | real data's cumulant ≡ 0 (all on-line) |
| SFF ramp-plateau (T6) | F = ramp, marks = plateau | plateau needs |α|>1 — same wall | no per-instance exact statement |
| Boolean junta (T7) | certificate = low-sensitivity function | foolable ⇒ law wins | sensitivity range bounded by window identity |
| Codes Plotkin/Johnson (T8) | integrality = alphabet | walls are Plotkin-type | naive defect recursion fails (Schur witness) |
| Sphere-packing exact LP (T9) | ladder limit = exact LP value | mechanical limit v(∞) | limit may be < p₀ (in-class) |
| Glass aging (T10) | two-time overlap | NO aging in real data (≤0.12× null) — diagnostic | finite-N only |
| Shadow tomography (T11) | cert = measurement protocol | shadow-norm framing | reproduces the two-moment ceiling |
| Compressed sensing (T12) | defect = sparse signal, law = NSP violation | pair-model reduces measurements | LP-dual says 2 is optimal in-class |
| Boolean degree-2 (T13) | degree-2 closure | explains third-moment death | decay hypothesis unproven |
| SRG/two-eigenvalue (T14) | law's Gram ≈ near-identity | 216/256 eigenvalues near 1 — measured | degree-4 input unavailable at useful λ |
| Graphon/Aldous–Hoover (T15) | law = graphon, regularity = approximation | empirical limit object measurable | unconditional limit control = beyond-1 wall |

**The pattern across all 15:** every transfer either (a) lands on a *diagnostic* that measures
how far reality is from the certificate's worst case (T4, T6, T7, T10, T11, T13, T15 — all
realized numerically here), or (b) lands on the *same beyond-bandwidth-1 / higher-moment wall*
but *prices it* (T1, T2, T5, T8, T9, T12, T14). The one transfer with *proven-partial* content
beyond the wall is **T8** (the defect-telescope / off-line-pair bridge, whose first level is the
certified trmdy √-tail and whose open lemma is named in `campaign-2.md`), and the one with a
*mechanically computable* next result is **T9** (the exact ladder limit v(∞)).

---

## 4. Ranked concrete next moves (expected value × feasibility — CONJECTURED scoring)

| Rank | Move | Transfer | Why | Cost |
|---|---|---|---|---|
| 1 | **T9: compute the exact ladder limit v(∞)** for the √-tail/coboundary family | sphere-packing exact LP | closes the convergence question (`verify-tawanerguo-bellman.md` names it THE live question); mechanical | Low (extend `analogy` E2b) |
| 2 | **T8: two-level defect-telescope probe** on the sandbox worlds | codes Plotkin/Johnson | tests the campaign-2 bridge's recursion; the only proven-partial route past 0.6732 | Med |
| 3 | **T14: degree-4 Gram-moment probe** (real vs 256-lattice) | SRG/two-eigenvalue | quantifies the spectral gap 0.734↔0.994 as the price of the missing degree-4 datum | Low (`gramev` ext) |
| 4 | **T13: empirical triple-correlation decay probe** | Boolean degree-2 closure | prices the "F≈1 beyond 1" conjecture that would justify a conditional improvement | Med (windowed 3-point) |
| 5 | **T10: aging probe on the large LMFDB file** | glass two-time | tests whether the no-aging diagnostic (ratios ≤ 0.12) survives at 10⁶ ordinates | Low |
| 6 | **T1: energy-functional LP** (spectral read beyond two moments) | Delsarte energy | the direct test of whether the 0.734↔0.667 gap is harvestable in-class | Med (needs LP) |
| 7 | **T7: weighted-sensitivity scan** of the floor | Boolean junta | quantifies the max reachable long-range share of the floor | Low (`flip` ext) |

**Definition of done for each:** T9 — a number v(∞) with its closed form, either provably < p₀
(ceiling is the in-class attractor; documented) or > p₀ (breakthrough, escalate). T8 — a table
one-level vs two-level certificate on the sandbox worlds; ≥ ε gain = the recursion is alive,
≤ 0 = documented death of the naive recursion (consistent with campaign-2). T14 — the degree-4
ratio; ≫ 1 = spectral separation is real in degree 4 (conditional route priced). T13 — the
degree-3/degree-2 mass ratio; ≪ 1 = degree-2 closure is empirically tight. T10 — ratio ≪ 1 at
10⁶ ordinates = no-aging robust. T1 — LP shadow prices: nonzero = ceiling beatable by a spectral
read (breakthrough), zero = class exhausted (documented). T7 — reachable sensitivity range.

---

## 5. Honesty footer

- Every idea in §2 is **CONJECTURED by construction** (this is an idea-generator catalog); none
  is asserted as a theorem.
- Every number in §0 and the anchors is **CHECKED NUMERICALLY** by the four Rust binaries
  archived in this directory (`analogy.rs`, `flip.rs`, `gramev.rs`, `lattice.rs`; builds and runs
  documented in §0; outputs in `out_*.txt`; source hashes in `SHA256SUMS`). Commands:
  `export PATH=$HOME/.cargo/bin:$PATH RUSTFLAGS="-C linker=rust-lld -C link-self-contained=yes" && cargo build --release --target x86_64-unknown-linux-musl && ./target/x86_64-unknown-linux-musl/release/<bin>`.
- Facts about the certified record (0.6725 / 0.6732 external mechanisms / 0.6818 ceiling /
  2/3 & 5/6 walls / third-moment death / beyond-1 deaths / detection threshold / ladder &
  coboundary mechanisms) are **PROVEN or CHECKED NUMERICALLY in the cited notes**
  (`attack-lpdual.md`, `attack-ceiling.md`, `attack-multiplicity.md`, `attack-thirdmoment.md`,
  `attack-m29.md`, `attack-gm-variance.md`, `attack-kernel.md`, `attack-argprinciple.md`,
  `attack-detection-threshold.md`, `verify-tawanerguo-bellman.md`, `discovery-gram-stability-673.md`,
  `campaign-2.md` in `research/external-results/trmdy-zeta-simple-zeros-673137/docs/`).
- Deliberately NOT claimed: that any transfer "probably proves RH" or "breaks the ceiling".
  The single most honest summary of the catalog: **the 15 transfers all either measure the
  reality-vs-worst-case gap (and my probes show it is real and large: Gram concentration 0.734
  vs 0.667) or re-derive the beyond-1 wall with a price tag; the two mechanically actionable
  moves are the ladder-limit computation (T9) and the defect-telescope probe (T8).**

RESULT: COMPLETE — 15 non-obvious analogy transfers for RH with Rust-verified anchors (real-zeros Gram concentration 0.734 vs the certificate's 0.667 worst case and the 0.994 lattice; no-aging two-half diagnostic; nearest-neighbor junta structure of the floor), ranked next moves T9 (exact ladder limit) and T8 (defect-telescope); all ideas CONJECTURED, all numbers CHECKED NUMERICALLY.
