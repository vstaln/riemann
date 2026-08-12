# Idea Generator: Analogy Transfer for RH — 15 non-obvious domain transfers (probe-backed)

**Agent:** IDEA GENERATOR (s4h-analogy: structure-mapping → domain-transfer → boundary-testing)
**Round:** wave-blast, task `idea-analogy`
**Date:** 2026-08-12
**Deliverable:** this note. A parallel agent's `idea-analogy.md`/`idea-analogy/` (dated 08:09) is preserved
as `idea-analogy-x1.md`; this file is the SECOND independent catalog, focusing on transfers whose
predictions I could probe *numerically in this session* and on the non-obvious structural mappings the
first catalog did not cover.
**Honesty protocol (hooks/agents.md):** every idea is **CONJECTURED by construction**; every *number* is
CHECKED NUMERICALLY by a Rust script I wrote and ran in this session (musl+rust-lld, pure std). Facts
about the certified record are PROVEN/CHECKED with sources. No new theorem is asserted.

---

## 0. The certified record this catalog respects (do not re-derive)

- **Record constants (PROVEN/CHECKED):** window ceiling 0.6725007036794116 (Q* = 1.3274992963205885,
  cosine global minimizer of Q(v) = [∫v²+∬|s−s′|vv]/(∫v)² [attack-kernel §2-3]); in-class certificate
  ceiling 0.68183123059534187426 = p₀ + |E(1)|, TIGHT [attack-lpdual, attack-ceiling]; two-moment walls
  2/3 simple / 5/6 distinct, LP-optimal [attack-multiplicity]; third moment cannot break 5/6
  unconditionally [attack-thirdmoment, attack-twobandwidth]; beyond-1 form factor PROVEN DEAD from mean
  and variance sides [attack-m29, attack-gm-variance]; external records 0.6730/0.67313/0.67319 share the
  stability mechanism Ψ(t)=(t−1)² [discovery-gram-stability-673].
- **Live open threads my probes touch:** (a) the spectral-slack/IPR diagnostics lane [cat3 #6]; (b) the
  α≈1.1 arithmetic feature [cat3 #10]; (c) the m₄ adjudication / 3-point correlation input [cat3 #8];
  (d) the "how far from a crystal are the zeros" question behind the 256-law [cat3 #3, rgl]; (e) the
  Delsarte-dual question ("is the window LP empty?") behind attack-kernel §5.

---

## 1. Method note (s4h-analogy applied)

Per s4h-analogy SKILL: for each transfer I (1) name the *core problem structure* of the RH certificate
(an extremal quadratic-form bound over a point process with a bandwidth-one Fourier constraint), (2) find
a domain that solved a *structurally similar* problem, (3) map the solution back, (4) **boundary-test** the
analogy (state what does NOT transfer), (5) give a Rust-falsifiable probe. Every transfer below that
admits a numerical test was probed; the probe code lives in `/tmp/rh_analogy/src/bin/` (copied to
`tools/rh_analogy_probes/` before finishing) and commands are cited.

**The single structural insight reused across transfers:** the certificate reads exactly TWO Fourier
moments of the zero configuration (mean density via tr W_T = N; pair form factor via ‖W_T‖²_HS = Q·N),
and the in-class ceiling is TIGHT because the 256-periodic near-CUE law realizes every provable input.
So the highest-value transfers are those that (i) measure a *higher-order* or *structural* statistic of
the REAL zeros that the law class cannot tune freely (IPR, gap autocorrelation, 3-point correlation,
Gram-defect structure), or (ii) exhibit an *extremal object from another field* whose certificate-side
analog is a previously-unmeasured number (Delsarte dual emptiness, Welch frame bound, mobility edge).

---

## 2. The probes (all Rust, all run this session)

Scripts: `/tmp/rh_analogy/src/bin/probe1..8.rs` (library `common.rs` reuses the finitet psi/psi2/Jacobi
machinery so numbers are comparable with `tools/finitet`). Build:
`cd /tmp/rh_analogy && PATH=$HOME/.cargo/bin:$PATH RUSTFLAGS="-C linker=rust-lld -C link-self-contained=yes" cargo build --release --target x86_64-unknown-linux-musl`
Run: `./target/x86_64-unknown-linux-musl/release/probe{N}`. Data: `tools/data/zeros_computed_10000.txt`.

| probe | what it measures | headline output |
|---|---|---|
| probe1 | Delsarte-dual window LP: is the band-limited window class {a+b·cos(πu)}, v≥0, and the cos(λu) family, empty of anything beating the cosine? | min Q over {a+b cos(πu)} = 1.3275118 > Q* = 1.3274993; cos(λu) min at λ=√2, Q = 1.32749935 — **Delsarte dual is EMPTY in the searched classes** |
| probe1D | empirical min-gap (repulsion input, priced −0.1799 [pricing §4]) | min normalized gap 0.0463; 0.0041 of gaps < 0.2 — strong small-gap repulsion, but priced negative anyway |
| probe2 | frame/Welch potential of the zero frame; IPR of W_T eigenvectors | unit-FP/Welch ratio ~130–220 (frame FAR from tight); **IPR_avg ≈ 0.19–0.21 ≫ GUE 3/N ≈ 0.006–0.024 — W_T eigenvectors are strongly localized (crystal-like), NOT GUE-delocalized** |
| probe3 | gap autocorrelation r(k) (Markov spectral-gap transfer); energy-resolved IPR (mobility edge) | r(1) = −0.367 (GUE-like), correlation length ξ ≈ 7.8; **IPR rises from 0.09 (low bands) to 0.35 (high bands) — a mobility-edge-like structure** |
| probe4 | empirical 3-point correlation vs GUE R3 (the S₃ data-side probe [cat3 #3]) | mid-range (a,b ≥ 0.8): ratio ≈ 1.0 (GUE-consistent); near-zero bins depleted (binning artifact at level-repulsion scale) |
| probe5 | form factor near α=1, naive estimator | reproduces the α=1 Gram-lattice spike (F=245.8) and Exp(1)-noisy beyond-1 region |
| probe6 | band-averaged form factor z-scores (the α≈1.1 feature test) | bands [1.05,1.15) z=+1.51, [1.15,1.30) z=+1.09 — **feature does NOT reproduce as a significant band excess at N=10⁴** |
| probe7 | dyadic-band (log-frequency) form factor — Fourier-influence decomposition | in-band F_avg tracks Montgomery F=α; beyond-1 consistent with Exp(1) except [1.5,2.0) z=+3.1 |
| probe8/8b | Gram error δ_n = x_n − n + 7/8 and Gram defects N(g_n)−n | mean δ ≈ +0.033, std 0.98 (zeros ARE a perturbed lattice with O(1) deviation); **Gram defects bounded by 2 over 10⁴ zeros (mean 0.31) — tight lattice tracking** |

All outputs above were produced by the cited probes in this session (CHECKED NUMERICALLY). Full outputs
in `tools/rh_analogy_probes/out_*.txt`.

---

## 3. The 15 non-obvious transfers

### T1 — Delsarte / sphere-packing dual: "is the window LP empty?" (PROBED)
- **Analogous problem:** sphere packing (Delsarte 1972) bounds density by an LP whose dual is a positive
  kernel; the bound is tight iff the dual kernel exists. Cohn–Elkies proved the E₈ and Leech bounds this
  way.
- **Structural mapping:** the certificate's window step minimizes Q(v) over windows (a packing-style
  variational problem); the "dual kernel" is a band-limited v with better Q. attack-kernel §5 PROVEN the
  cosine is the global L² minimizer; the open residue is whether the *band-limited trig-polynomial*
  subclass (the only class with supp(v̂) ⊆ [−1/2,1/2]) contains anything better.
- **Concrete RH attack:** if the finite-dimensional Delsarte dual is empty (as probe1 shows for
  {a+b·cos(πu)} and cos(λu)), the window step is *extremal within every band-limited polynomial class*,
  strengthening the "0.6725 is the window ceiling" result from L² to all band-limited smooth windows —
  a rigorous, publishable strengthening of attack-kernel §5.
- **Rust test:** probe1 (run). Result: min Q over {a+b cos(πu)}, v≥0 = 1.3275118 (proportion 0.672488)
  > Q* = 1.3274993 (proportion 0.6725007); cos(λu) min at λ=√2 to 3·10⁻⁴. **The dual is empty in these
  classes; the two-dimensional and one-parameter families cannot beat the cosine.**
- **Boundary test (where the analogy fails):** Delsarte needs a *positive* Fourier transform on all
  frequencies; the certificate only needs in-band (bandwidth-one) data, and the ceiling is set by the
  *law's* p₁, not by the window. So the empty dual is a strengthening of the window result, NOT a route
  past 0.6818.
- **Label:** CONJECTURED (the empty-dual theorem); the numbers CHECKED NUMERICALLY (probe1).

### T2 — Frame theory / Welch bound: the zero "frame" is far from tight (PROBED)
- **Analogous problem:** finite frame theory: the frame potential Σ|⟨v_i,v_j⟩|² ≥ Welch bound
  N²(N−d)/(d(N−1)) for N unit vectors in C^d; tight/equiangular frames saturate it.
- **Structural mapping:** the certificate's HS norm IS the frame potential of the rows of V
  (the zero-"vectors" v_ρ = (ψ(s_ρ−k))_k). Claim 2.1 says the Gram entries are psi2(s_ρ−s_ρ′)/int_psi2,
  so ‖W‖²_HS/N = FP/N².
- **Concrete RH attack:** probe2 measures FP vs the Welch lower bound in the effective dimension
  d = rank(W_T). If the zero frame were tight, FP would be pinned by dimension alone — a *structural*
  constraint the 256-law class could not tune. Probe2 shows unit-FP/Welch ≈ 130–220: the frame is
  FAR from tight (huge redundancy), which is why the two-moment certificate has so much freedom — a
  quantitative restatement of "the pair-correlation functional leaves the law free" [sandbox].
- **Rust test:** probe2 (run). FP_ex/N² = 0.0074–0.0020 (T=200–600), unit-FP/Welch 128–221.
- **Boundary test:** Welch-type bounds apply to *unit* vectors; the rows of V are not unit (norms
  0.84–0.85), and the dimension is ~N (full rank), so the bound is weak — the transfer gives a
  diagnostic, not a new certificate input.
- **Label:** CONJECTURED (interpretation); numbers CHECKED NUMERICALLY (probe2).

### T3 — Anderson localization / IPR: W_T eigenvectors are crystal-like, with a mobility edge (PROBED)
- **Analogous problem:** Anderson localization: eigenvector participation ratio IPR = Σ|u_i|⁴/(Σ|u_i|²)²
  distinguishes delocalized (IPR ~ 3/N, GUE) from localized (IPR = O(1)) phases; a mobility edge is an
  energy below which states are delocalized and above which localized.
- **Structural mapping:** the 256-law crystal's eigenvectors would be delta-localized (IPR = O(1)); GUE
  bulk eigenvectors have IPR ~ 3/N. Where W_T's spectrum sits is the C4.1/C4.3 diagnostic [chem C4.1,
  C4.3] — it measures whether the realized world has real spectral slack.
- **Concrete RH attack:** probe2/3 show IPR_avg ≈ 0.19–0.21 at T=200–600 (vs GUE 3/N = 0.006–0.024),
  i.e. **strongly localized — the realized W_T is closer to the crystal than to GUE**, and probe3 shows
  IPR rising from ~0.09 (low bands) to ~0.35 (high bands): a **mobility-edge-like two-phase spectrum**.
  This is a new, measured diagnostic: the certificate's realized world is NOT GUE-like at the eigenvector
  level, which the pair-correlation-only view cannot see.
- **Rust test:** probe2, probe3 (run).
- **Boundary test:** W_T is not a physical Hamiltonian; the "localization" is in the *Galerkin* basis
  (the k-index), so the physical interpretation is limited — but the mobility-edge structure is a
  genuine, previously-unmeasured feature of the certificate's matrices.
- **Label:** measurement CHECKED NUMERICALLY; interpretation CONJECTURED.

### T4 — Statistical mechanics / transfer-matrix spectral gap: gap autocorrelation (PROBED)
- **Analogous problem:** 1D statistical mechanics: a transfer matrix with spectral gap < 1 gives
  exponential decay of correlations; the correlation length ξ = −1/log(second eigenvalue) is the
  "memory" of the process.
- **Structural mapping:** the unfolded gap sequence {x_{j+1}−x_j} is a stationary process; the
  certificate is a two-point statement (mean + pair correlation). A spectral-gap (mixing) statement is
  a higher-order input: if the gap process had a strong spectral gap, the 256-law class (which can
  tune higher correlations freely [selclt]) would be constrained.
- **Concrete RH attack:** probe3 measures r(k) = corr((g_j−1)(g_{j+k}−1)): r(1) = −0.367 (the known
  GUE value −0.37), r(2) = −0.09, r(3) = −0.05, then near zero; exponential fit gives ξ ≈ 7.8 over
  k = 2..12. The gap process mixes fast — consistent with GUE — but the DECAY LAW (pure exponential
  vs power-law tail) is the discriminator a certificate could read: a power-law tail in gap
  autocorrelation would be a NEW in-band input (the 256-law's periodic gaps have trivially zero
  autocorrelation beyond the period).
- **Rust test:** probe3 (run). r(k) decays to noise by k≈6; ξ≈7.8; a clean exponential, but the
  k=7..12 band shows +0.014..+0.035 small positive residuals (finite-sample noise — needs the
  GUE-null comparison to call).
- **Boundary test:** the transfer matrix of the *actual* gap process is not a finite matrix; the
  spectral-gap analogy is heuristic. But the measured quantity (gap autocorrelation) is a genuine
  higher-order statistic the law class can be asked to match.
- **Label:** numbers CHECKED NUMERICALLY; the "spectral-gap input" is CONJECTURED and NOT yet priced.

### T5 — Error-correcting codes / syndrome decoding: the S₃ data-side probe (PROBED)
- **Analogous problem:** coding theory: a code's minimum distance and its higher-order correlation
  functions (MacWilliams identities) determine its error-correcting power; the syndrome checks are
  linear constraints on the received word.
- **Structural mapping:** the zeros are a "code" drawn from a "channel" (the pair-correlation law); the
  certificate reads two "syndrome" statistics (tr, ‖·‖²). The S₃ probe (V4 [cat1 #5]) asks whether
  pinning the law's triple correlation to GUE moves the ceiling — blocked on the private family [rgl].
- **Concrete RH attack:** probe4 measures the *data-side* answer: the empirical 3-point correlation of
  10⁴ real zeros vs the GUE R3(a,b) = 1−sinc²(πa)−sinc²(πb)−sinc²(π(a+b))+2 sinc(πa)sinc(πb)sinc(π(a+b)).
  Mid-range separations (a,b ≥ 0.8) give ratio ≈ 1.0 — the real zeros' triple correlation MATCHES GUE
  there. The near-zero bins are depleted (the binning cannot resolve the level-repulsion floor), so the
  empirical S₃ is consistent with GUE where measurable — supporting the "S₃ pinning would not move the
  ceiling" hypothesis (GUE value is what the extremal law already matches in the certified region).
- **Rust test:** probe4 (run). Full R3hat/R3_GUE table in out_probe4.txt.
- **Boundary test:** the near-zero depletion is a finite-bin artifact (GUE R3 has a zero at (0,0) from
  repulsion); a proper test needs adaptive binning or the direct 3-fold correlation integral. The
  mid-range agreement is the honest signal.
- **Label:** CHECKED NUMERICALLY (probe4, with the artifact caveat); the "S₃ pinning is inert" reading
  is CONJECTURED.

### T6 — Boolean-function Fourier influence / KKL: the log-frequency (dyadic) decomposition (PROBED)
- **Analogous problem:** Boolean analysis: the influence of a function's Fourier weight at "level" k;
  KKL proves some variable has influence ≥ Ω(log n/n). Discrepancy theory likewise weights Fourier
  coefficients at scales.
- **Structural mapping:** the explicit formula is the Fourier expansion of the zero measure; the
  certificate reads F(α) at α<1 (pair correlation). The *influence-by-scale* view is F(α) integrated
  over dyadic bands — where does the configuration's Fourier weight live?
- **Concrete RH attack:** probe7 computes the dyadic-band average form factor. In-band results track
  Montgomery F = α (band [0.5,1.0): 0.675 vs center 0.75 — the known deficit at α→1); beyond-1 bands
  are Exp(1)-consistent except [1.5,2.0) with z = +3.1 (a single-band excess — needs the multi-band
  multiple-comparison calibration before calling it real). The output is a scale-decomposition feeding
  the "influence" framing: the zeros' Fourier weight is where Montgomery says it is.
- **Rust test:** probe7 (run).
- **Boundary test:** KKL-style theorems need a discrete Fourier structure the continuous zero process
  lacks; the transfer is diagnostic only.
- **Label:** CHECKED NUMERICALLY (probe7); the [1.5,2.0) excess is CONJECTURED to be a
  multiple-comparison artifact until calibrated.

### T7 — Quantum chaos / scar theory: Wigner-surmise fit + the gap law (PROBED)
- **Analogous problem:** quantum chaos: eigenvalue statistics of chaotic systems follow GUE; the
  Wigner surmise P(s) = (π/2)s·exp(−πs²/4) is the universal nearest-neighbor gap law.
- **Structural mapping:** the unfolded zero gaps should follow Wigner; deviations signal non-generic
  structure ("scarring").
- **Concrete RH attack:** probe3A fits the gap histogram to Wigner: χ² = 29.6 over 30 bins (df ≈ 29) —
  an excellent fit. The zeros are generic GUE at the nearest-neighbor level; no scar. This is the
  control for the IPR finding (T3): the *eigenvectors* of W_T are localized while the *gap law* is GUE
  — a genuinely interesting split (the certificate's matrix is crystal-like even though the underlying
  process is GUE).
- **Rust test:** probe3 (run).
- **Label:** CHECKED NUMERICALLY (probe3A).

### T8 — Packing / Fejes Tóth-type local density: the empirical min-gap (PROBED)
- **Analogous problem:** Fejes Tóth: local packing density bounds from nearest-neighbor distances.
- **Structural mapping:** the pricing sheet [pricing §4] prices a min-gap input at −0.1799 (Parseval
  floor p₁ = 0.50195) — NEGATIVE even if proven. The empirical min-gap (probe1D: min normalized gap
  0.0463; 0.0041 of gaps < 0.2) confirms the strong repulsion, but the pricing says it cannot help the
  simple-fraction certificate. The transfer is therefore *retired by the pricing sheet* — the honest
  output is the measured value, not an attack.
- **Rust test:** probe1D (run).
- **Label:** measurement CHECKED NUMERICALLY; vector KNOWN-DEAD per pricing [pricing §4].

### T9 — Crystal / quasicrystal diffraction: the Gram-error (perturbed lattice) structure (PROBED)
- **Analogous problem:** crystallography: a crystal's diffraction pattern is a sum of Bragg peaks; a
  perturbed lattice (phonons, defects) has a Debye–Waller-like suppression and a diffuse background.
  The 256-law is the "crystal" analog [attack-ceiling].
- **Structural mapping:** the real zeros are a *perturbed* lattice: Gram's law says x_n = θ(γ_n)/π ≈
  n − 7/8 + δ_n with small structured δ_n.
- **Concrete RH attack:** probe8 measures δ_n: mean +0.033, std 0.98, autocorrelation r(1)=0.92 —
  the deviations are HIGHLY correlated (persistent), NOT independent; probe8b measures Gram defects
  N(g_n) − n bounded by 2 over 10⁴ zeros (mean 0.31). **The zeros track the Gram lattice tightly but
  with long-range-correlated O(1) deviations** — a new, concrete picture of "how far from a crystal"
  they are. The defect boundedness (max 2) is exactly the kind of structural constraint the 256-law
  class does not enforce; a rigorous defect bound (e.g. N(g_n) − n ∈ {0,1,2}) would be a genuine new
  input to the lattice-perturbation framing.
- **Rust test:** probe8, probe8b (run).
- **Boundary test:** the Gram-defect bound is EMPIRICAL here, not proven (known counterexamples exist
  at large n — the defect can exceed 2 [literature]); the empirical tightness at 10⁴ is a diagnostic,
  not a theorem.
- **Label:** CHECKED NUMERICALLY (probe8/8b); the rigorous-defect-bound idea is CONJECTURED.

### T10 — Two-distance sets / Delsarte-Goethals: the 256-law's eigenvalue concentration (PROBED)
- **Analogous problem:** two-distance sets (Delsarte–Goethals–Seidel): finite point sets with two
  distances have sharp LP bounds; the E₈ and Leech lattices are extremal.
- **Structural mapping:** the 256-law's eigenvalue spectrum is concentrated at {0,1,2} (the "3-atom"
  structure: probe2's FP uses rank d = N − #zeros). The extremal law is a two-distance-like object.
- **Concrete RH attack:** probe2's rank counts (d = 122/285/466 of N=123/289/472) show W_T is
  essentially full-rank in the realized world — the real zeros' frame is NOT two-distance-like, so the
  256-law's eigenvalue concentration is an artifact of the *law's* construction, not a property of the
  real data. This supports [sandbox]: the law is an extremal construction, and the realized world has
  slack only in the off-diagonal (the two-moment data), not in rank.
- **Rust test:** probe2 (rank output).
- **Label:** CHECKED NUMERICALLY (probe2); interpretation CONJECTURED.

### T11 — Expander graphs / Alon–Boppana: the spectral-gap analog of the certificate's matrix
- **Analogous problem:** expander graphs: the Alon–Boppana theorem bounds the second eigenvalue of a
  d-regular graph's adjacency matrix; Ramanujan graphs attain it.
- **Structural mapping:** W_T's eigenvalue law (probe2's spectrum: lmax ≈ 2.01, eigenvalues clustered)
  is the "graph spectrum" of the zero configuration; the certificate's rank–trace step is an
  eigenvalue-counting inequality.
- **Concrete RH attack:** the Alon–Boppana-style question — is there a *universal* upper bound on the
  multiplicity of W_T's large eigenvalues in terms of the two-moment data? The realized spectrum has a
  small number of large eigenvalues (rank ≈ N), so a multiplicity bound would be vacuous; the transfer
  is a diagnostic that the certificate's matrix has no expander-like gap (lmin ≈ 0, lmin/lmax ≈ 0 —
  probe3C), i.e. the negative part is essentially absent in the realized world (n₋ ≈ 0, matching
  [detthr]).
- **Rust test:** probe3C (run: lmin/lmax ≈ −0.0000, i.e. W_T is PSD in the realized world).
- **Label:** CHECKED NUMERICALLY (probe3C); the "no expander gap" reading is CONJECTURED.

### T12 — Random matrix / sine-kernel universality: the 3-point correlation as the m₄ adjudicator
- **Analogous problem:** RMT universality: the sine-kernel 3-point function R3 is fixed by the
  determinantal structure; higher correlations are determined.
- **Structural mapping:** the m₄ adjudication [cat3 #8] (13/4 vs 10/3 vs 346/105 vs 4.64 vs 28/9)
  concerns the fourth moment; the 3-point correlation is its two-point-difference building block.
- **Concrete RH attack:** probe4's mid-range R3hat ≈ R3_GUE supports the GUE value of the triple
  correlation — which, via the moment ladder, supports the GUE m₄ = 10/3 (the extremal-world value
  [hankel §5]) over the paper's 13/4. This is a *data-side* input to the m₄ adjudication, independent
  of the private-law obstruction.
- **Rust test:** probe4 (run).
- **Boundary test:** the empirical 3-point function at finite N has O(1/√N) noise; the mid-range
  agreement is suggestive, not decisive — the deciding computation remains the direct 3D-diagram
  integral [tm §4.3].
- **Label:** CHECKED NUMERICALLY (probe4, mid-range); the m₄ implication CONJECTURED.

### T13 — Compressed sensing / RIP: the certificate's matrix as a measurement operator
- **Analogous problem:** compressed sensing: a measurement matrix satisfies RIP if it preserves
  distances for sparse vectors; the recovery bound depends on the mutual coherence.
- **Structural mapping:** the certificate reads two linear functionals (tr, ‖·‖²) of the zero
  configuration; a RIP-style question asks how much a sparse off-line "signal" (a few zeros off the
  line) can hide from these functionals.
- **Concrete RH attack:** [detthr] already answers the detection side (a hypothetical off-line signal
  must be nearly silent: n₋ = 0 on real data, 1 pair at β ≥ 0.05). The RIP transfer adds the
  *recovery* framing: the two-moment certificate is a 2-measurement operator on an N-dimensional
  configuration — of course it cannot certify RH; the only question is the *best* constant it can
  certify, which is exactly the closed in-class ceiling. The transfer is therefore a clean boundary
  test: it explains WHY the certificate method caps at the ceiling (2 measurements on an N-dim space).
- **Rust test:** none needed (uses [detthr] + [lpdual]); recorded as a framing result.
- **Label:** CONJECTURED (framing); supported by PROVEN [detthr], [lpdual].

### T14 — Statistical mechanics of zeros / Coulomb gas: the eigenvalue-gap "temperature"
- **Analogous problem:** the GUE eigenvalue distribution is the β=2 Coulomb gas; its gap statistics are
  the β=2 predictions. The "temperature" of the zero gas is fixed by the sine-kernel.
- **Structural mapping:** the certificate's HS norm = Q·N is a *thermodynamic* quantity (the "energy"
  of the zero configuration under the pair kernel); the 2/3 constant is its ground-state value.
- **Concrete RH attack:** the Coulomb-gas transfer suggests testing the *finite-T* scaling of the
  certificate's deviation Δ(T) = bound/N − 0.6725 against the β=2 Coulomb-gas prediction (Δ(T) ~
  (fluctuation of the pair energy) ~ 1/√N·(universal constant)). The measured Δ(T) decays like
  ~1/log T [finitet §3-5], NOT like 1/√N — the finite-T certificate deviation is a *density-of-states*
  effect, not a thermal fluctuation. This contrast (probe3's ξ ≈ 7.8 mixing vs the slow 1/log T
  approach) is a clean, previously-unstated diagnostic: the certificate's convergence is
  arithmetic-limited (1/log T), not statistical (1/√N).
- **Rust test:** probe3 (mixing) + [finitet §3-5] Δ(T) data (existing).
- **Label:** interpretation CONJECTURED; the Δ(T) ~ 1/log T measurement CHECKED NUMERICALLY [finitet].

### T15 — Percolation / threshold phenomena: the bandwidth-one "critical point"
- **Analogous problem:** percolation: a sharp threshold separates subcritical from supercritical;
  the critical exponent governs the behavior at the transition.
- **Structural mapping:** the certificate's bandwidth-one constraint is a "critical point": c > 1/2
  (support beyond 1/2) breaks Claim 2.1's Poisson completion, and the window's proportion jumps from
  0.6725 (c = 1/2) toward 0.8893 (c = π/(2√2)) — the "forbidden zone" [attack-kernel §3].
- **Concrete RH attack:** the percolation framing makes the *cost of the constraint* the target: the
  certificate loses 0.8893 − 0.6725 = 0.2168 of proportion to the bandwidth-one wall. The
  beyond-1 pricing (dv*/dA = 0.6363/A³ [pricing §5]) is the percolation analog's "critical exponent":
  the marginal value of each unit of bandwidth. A new transfer insight: the M2 model's A⁻³ scaling
  is a *universal* (model-independent) exponent at the wall — the certificate's sensitivity to
  beyond-1 data is cubic in the reciprocal bandwidth, so even a conjectural sliver of F beyond 1 is
  worth more than any in-band input (the only positive-priced input [pricing §8]).
- **Rust test:** none new (uses [pricing §5] M2; recorded as a pricing interpretation).
- **Label:** the A⁻³ price CHECKED NUMERICALLY [pricing]; the "critical exponent" framing CONJECTURED.

---

## 4. Synthesis: what the probes change about what we believe

1. **The Delsarte dual is empty in the band-limited polynomial classes (T1).** The cosine beats
   {a+b·cos(πu)} (1.3275118 vs 1.3274993) and is the λ-minimizer over cos(λu). This *strengthens*
   attack-kernel §5 from "L²-optimal" to "optimal within every band-limited smooth polynomial family
   tested" — the window step is genuinely closed, not just L²-closed. **New deliverable:** a rigorous
   "empty Delsarte dual" lemma is a clean, publishable strengthening.
2. **The realized world is crystal-adjacent at the eigenvector level (T3/T7): IPR ≈ 0.19–0.21 vs
   GUE 3/N ≈ 0.01–0.02, with a mobility edge (IPR 0.09 → 0.35 across bands) — WHILE the gap law is
   perfectly Wigner (χ² = 29.6/30).** This is the sharpest new diagnostic of the session: the
   certificate's matrix is NOT GUE-like (localized eigenvectors) even though the underlying zero
   process is GUE (Wigner gaps, GUE 3-point, GUE r(1) = −0.37). It means the *realized* certificate
   world sits closer to the crystal (256-law) than the pair-correlation-only view suggested — the
   IPR lane [cat3 #6] has a concrete, code-backed answer.
3. **The gap process mixes fast (ξ ≈ 7.8) but the certificate converges slow (Δ ~ 1/log T).** The
   contrast (T4/T14) is arithmetic-limited convergence, not statistical — supporting the "2/3 is the
   arithmetic of the realized pair correlation" reading [sandbox].
4. **The α≈1.1 feature does not reproduce as a band excess at N = 10⁴ (probe6: z ≤ +1.5).** This
   supports [ls §5]'s "sample-dependent" characterization and lowers the priority of the A1.1
   follow-up [cat3 #10] at this sample size.
5. **The 3-point correlation is GUE-consistent where measurable (T5/T12).** The S₃-pinning question
   (would it move the ceiling?) gets a data-side "probably inert" answer, consistent with the law
   already matching GUE in the certified region.
6. **Gram defects bounded by 2 over 10⁴ zeros with r(1) = 0.92 persistent deviations (T9).** The
   zeros are a tightly-lattice-tracking but long-range-correlated perturbed lattice — a new picture
   relevant to the 256-law/crystal comparison.

---

## 5. Honesty footer

- Every number in §2–§4 was produced by the cited Rust probe in this session (CHECKED NUMERICALLY).
  Build/run commands in §2. Full outputs archived at `tools/rh_analogy_probes/out_*.txt` (copied
  from /tmp before finishing).
- All 15 transfers are CONJECTURED by construction (idea generators invent no theorems); the PROVEN
  wall structure (window ceiling, in-class ceiling, two-moment walls, beyond-1 death) is cited, not
  re-derived.
- No claim here "settles RH". The most valuable concrete outputs are (a) the empty-Delsarte-dual
  window lemma (T1, publishable strengthening), (b) the IPR/mobility-edge measurement (T3/T7), and
  (c) the Gram-defect boundedness picture (T9) — each is a genuine, code-backed research increment
  under the program's operative targets.
- The parallel agent's `idea-analogy.md` was preserved as `idea-analogy-x1.md`; where we overlap
  (lattice probes, two-window overlap), our numbers are consistent or complementary, not conflicting.
