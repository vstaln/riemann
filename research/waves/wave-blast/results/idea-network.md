# Idea Network — zeros as a network: centrality, contagion, communities, weak ties

**Role:** idea-generator (s4h-network). **Date:** 2026-08-12. **Lens:** network science on the
zeta-zero ordinates as nodes, correlations as edges. **Status:** 12 CONJECTURED ideas + numeric
checks on real zeros (100k ordinates).

**Honesty preamble — the task's cited record does not exist in this repo.**
The task says to read `/home/vstaln/riemann/research/notes/discovery-6732629.md` (a "certified
67.3263% record") and `attack-vector-catalog*.md`. A full-repo search finds **no such files and no
67.3263% number anywhere** (`grep -rn "6732629\|67.326" research/ scratch/` — only task files
reference the path). I do **not** fabricate this record. I ground every constant in the verified
notes that DO exist:
- `research/notes/discovery-gram-stability-673.md` — the real certified record:
  H0 = 3/2 − (1/√2)cot(1/√2) = **0.67250070367941164573** (Theorem D), 3-pt
  (H0−ε/4)/(1−ε/2), ε=221/10⁶ → **0.6725197671136777**, 7-pt (1345000·H0−2680)/1340003 →
  **0.67300852792777976**, in-class ceiling 0.68183123059534187426.
- `research/notes/verify-gram-stability.md` — adversarial Q4: constants OK, kernel mechanism holds
  (3 zeros of k on (0,4): z1=1.0572782910, z2=2.0300675301, z3=3.0202429921; min S2 = 2.221491e-4
  tight to 0.52% vs 221/10⁶), 7-pt functional UNRESOLVED (19/5000 unidentified), per-block→liminf
  unverified (E[Σ6 gaps]≈8.9 > 4 → Markov vacuous).
- `research/notes/transfer-stability-online.md` — Theorem A transfer INCONCLUSIVE (blocker named:
  data-limited vs slack-limited).
- `research/ideas/idea-factory-master.md` — 753 ideas, top-30 EV; several overlap my network
  lens (SPAN-01, CI-74, ATOM-02, RE-63, OS-13). I mark overlaps REPEAT-adjacent where honest.

**Data used:** `scratch/idea-network-rs/data/zeros_100k.txt` (100,000 ordinates, γ₁=14.134725142 …
γ₁₀₀₀₀₀=74920.827498994; `tools/data/` is empty — the task's stated location does not hold data;
the zeros live in `scratch/idea-network-rs/data/`). All probes: Rust binaries
`scratch/idea-network-rs/target/x86_64-unknown-linux-musl/release/probe_{a..f}`, sources
`scratch/idea-network-rs/src/bin/`. Rust 1.97.1; build:
`export PATH=$HOME/.cargo/bin:$PATH; RUSTFLAGS="-C linker=rust-lld -C link-self-contained=yes"; cargo build --release --target x86_64-unknown-linux-musl`.

---

## 1. The network model (and its honest limits)

**Nodes** = zero ordinates γᵢ. **Edges** = correlations. I used two edge families:
1. **Distance graph** at radius R (mean-spacing-1 scale): edge (i,j) if |γᵢ−γⱼ| ≤ R.
2. **Kernel-weight graph** (the certificate's own geometry): edge weight wᵢⱼ = k²(γᵢ−γⱼ) for
   |γᵢ−γⱼ| ≤ 4, k(x) = K(x)/K(0), K(x) = ∫_{−1/2}^{1/2} cos(√2t)cos(2πxt)dt, closed form
   k(x) = [sinc((√2−2πx)/2)+sinc((√2+2πx)/2)]/(2K0), K0 = 0.91872536986556843778.

**Why a network at all?** The certificate's load-bearing objects are *blocks* of consecutive zeros
(3-pt spans 4, 7-pt spans 9, ladder n=9→11.5 … n=15→19). The two-moment data (t = tr, t₂ = ‖·‖²_F)
are sums over these blocks; the Gram-stability refinement adds tr Ψ(M) > 0 where M is the Gram
matrix of zero-atoms — literally a *weighted adjacency matrix* of the zeros with edge weights
k(γᵢ−γⱼ). So the pair-correlation structure that forces simple+on-line **is already a network
property of the Gram graph**: the rank–trace inequality is a bound on how much energy a connected
Gram graph can hold, and the refinement measures its "community density" (tr Ψ = 2·Σ_{i<j} k² =
twice the intra-block k²-energy). Network analysis is not decoration; it re-reads the existing
machinery.

**Honest limit (CHECKED NUMERICALLY):** the zeros in `zeros_100k.txt` are all *computed simple
zeros on the line* — by construction they contain **no off-line zeros and no multiple zeros**.
So the network cannot *measure* the simple-zeros proportion; it can only measure *pair-correlation
geometry* (degree, clustering, communities, energy) that the certificate's inequality uses. Every
"forces simple+on-line" claim below is CONJECTURED at the level of a *mechanism proposal*, not a
measured proportion. Where I test a quantitative claim, it is about the *Gram/kernel geometry* the
certificate uses.

---

## 2. Numeric results (all CHECKED NUMERICALLY, script + command)

### 2.1 Distance-graph statistics (probe_a)
Command: `scratch/idea-network-rs/target/x86_64-unknown-linux-musl/release/probe_a data/zeros_100k.txt 0`

| R (mean-spacing-1) | avg deg | median | clustering | frac deg≥2 | frac deg0 |
|---|---|---|---|---|---|
| 0.5 | 0.205 | 0 | 0.0000 | 0.0019 | 0.797 |
| 1.0 | 1.106 | 1 | 0.0107 | 0.2647 | 0.161 |
| 1.5 | 2.086 | 2 | 0.1334 | 0.8377 | 0.0095 |

- R=1.5: degree V/M = **0.2189** (probe_b) — **sub-Poisson** (Poisson V/M = 1.01 on the Exp(1)
  null, probe_e §4) = level repulsion, the *opposite* of a clustered/contagious network. Unfolded
  scale V/M = 0.1757 (probe_c §A).
- Clustering at R=1.5 = 0.133 (vs 0.30 on the Poisson null) — zeros *avoid* triangles; the
  geometric graph on a line with repulsion is nearly planar-path-like.

### 2.2 Pair correlation (probe_b §1, probe_c §A)
- R2(α) at small α is far **below** GUE (0.0168 @0.1, 0.0666 @0.2 — the famous "too few close
  pairs" deficit vs GUE 0.0325/0.1249); crosses 1 near α≈1.0, overshoots to 1.55 @2.0. Same
  shape unfolded. CHECKED NUMERICALLY.
- **Interpretation for the certificate:** the two-moment data (t, t₂) are *positive-density* in
  the kernel's span (≤4): 7-atom windows have Σ6-gaps mean 5.93, median 5.83, and **100% of
  span≤9 windows have Σ6-gaps > 4** (probe_c §D) — the Q1 Markov-vacuity (E[Σ6]≈8.9>4) is
  empirically confirmed: blocks are *never* span-4-closed at 7 atoms; the certificate's span-9
  model-II is the operative one.

### 2.3 Kernel-sign "frustration" (probe_c §B)
- On 99,997 consecutive gap-triples (u,v,u+v ≤ ~4 window): **95.0% mixed-sign, 5.0% all-same-sign,
  0 zero** (of k(u), k(v), k(u+v)). The kernel's sign-alternation makes the Gram graph a
  **frustrated (antiferromagnetic-like) weighted graph** — atom orthogonality is impossible
  because you cannot make all three edges of any triangle vanish (triple-zero impossible, verified
  in verify-gram-stability.md B: min max|k| = 9.42e-3).

### 2.4 Kernel-edge / weak-tie structure (probe_b §4–5)
- |k| on consecutive gaps: 75% strong (≥0.1), 22.6% mid, 2.40% weak (<0.01). Gaps within 0.05 of
  kernel zeros: 9.02% near z1=1.057, 0.65% near z2=2.030, 0.01% near z3=3.020. So **near-zero-k
  edges (weak ties) are rare** (2.4%) and concentrate near the *first* kernel zero.
- Bridge test (R=1.5, remove |k|<0.05 edges = 11.1%): weak-removal → 1.73× components, random
  removal (same count) → 1.93×. **Weak ties are NOT bridges** — removing them fragments *less*
  than random removal. The graph is robust to weak-tie removal (no Granovetter weak-tie bridges).

### 2.5 Contagion — the headline negative (probe_d §2–3, probe_e §1–3)
- **Global-mean rescaling artifact:** on the raw-mean-spacing scale the longest gap-sign run is 70
  at zero index 1 (γ=21.022) — but this is a rescaling artifact: near the first zero the
  global-mean spacing (0.749) is too small, so early gaps look systematically "long". Mean
  position of runs ≥10 = **0.060** (far from uniform 0.5) — edge contamination.
- **Unfolded scale (physically correct):** longest run = **7** (at index 96309, γ=72446.675);
  mean +run 1.546 (iid-exp 1.835), −run 1.852 (iid-exp 2.198) — no long contagion runs.
- **Gap-anomaly autocorrelation (unfolded):** ac(1) = **−0.357** (GUE-consistent, literature
  ≈ −0.24–0.36), ac(2) = −0.079, ac(≥10) ≈ 0. So correlation is *short-range and anti-correlated*,
  not contagious. Shuffled-gap null: ac(1) = +0.0009 ± 0.0007 → the −0.357 is genuine order
  (repulsion), not noise.
- **Verdict:** "contagion" as network dynamics does NOT exist in the zeros. The apparent 70-run is
  an edge effect (ABANDONED as a phenomenon; the honest stat is the unfolded longest run = 7).

### 2.6 Community structure — the span-4 tiling IS a community (probe_c §E, probe_e §5, probe_f)
- Span-4 greedy tiling: 21,773 blocks, avg size 4.59; intra-block k²-energy = 1.2450e4 over
  185,359 pairs; inter (adjacent cut, span≤4) = 2.4621e3 over 170,392 pairs;
  **intra/(intra+inter) = 0.8349**.
- Random-partition null (same block count): mean 0.7627, max 0.7644 (20 draws) → the real tiling
  is **+9.5% above the null max** — the certificate's span-4 blocking is a *genuine community
  structure* of the Gram graph, not an arbitrary tiling. z ≈ (0.8349−0.7627)/σ ≫ 10 (σ ≈ 0.0003).
- Tiling variants (probe_f §1): intra-frac monotone in span: span-3 0.787, span-4 0.835, span-5
  0.868, span-6 0.893. Bigger span → more intra-energy (no penalty in this metric — but the
  *certificate* fixes span by the window, so the free tiling is not the certificate's).
- Louvain greedy on 4000-window (probe_f §2): 1589 communities, modularity Q = 0.428, max size 9,
  intra-frac 0.428 — **weak** modularity: the Gram graph is a *chain-like weighted path*, not a
  clustered network. Communities are local clumps of ≤9 zeros, not mesoscale structure.

### 2.7 Per-atom energy centrality (probe_c §F, probe_d §4)
- wᵢ = Σ_j k²(γᵢ−γⱼ), span ≤ 4: mean 0.298, median 0.211, p05 0.037, p95 0.835 (heavy right tail).
- Pearson corr(wᵢ, local gap anomaly²) = 0.152 — weak positive: high-energy atoms sit near
  anomalous (large) gaps, mildly.
- Nearest-neighbor energy assortativity = **0.402** — energy is *assortative* along the line
  (high-wᵢ atoms cluster together). CHECKED NUMERICALLY. This is the single most
  certificate-relevant network number: the Gram graph's energy is positively autocorrelated, which
  means tr Ψ(M) per block is *clumped*, not Poisson — relevant to the per-block→liminf passage.

### 2.8 The ε-floor closed form (probe_d §1) — CHECKED NUMERICALLY
- Constrained min S2(u,v), u,v≥0, u+v≤4 = **2.221575e-4** at (u,v) = (1.053, 2.012) (matches the
  verified 2.221491e-4 at (2.012057,1.053089); the doc's floor reproduced to 0.52% margin).
- Decomposition at the minimizer: k(u)² = 1.42e-5, k(v)² = 5.88e-5, k(u+v)² = 1.49e-4 (the
  dominant term is k²(u+v) — the *sum* gap is the binding constraint, not the individual gaps).
- **Commensurability defect:** z1+z2 = 3.0873, z3 = 3.0202, defect = **+0.0671**; k²(z1+z2) =
  3.276e-4; floor/k²(z1+z2) = 0.678 — the floor is NOT simply k² at a kernel-zero pair-sum; the
  defect (0.067) is what forces the interior minimum below the "locked" value. This is the
  network-geometric reason the 3-pt floor is 2.22e-4 and not 0: three zeros cannot all sit at
  kernel zeros because z1+z2 ≠ z3. (Grid min 5.83e-5 in probe_c §C violates u+v≤4 — probe_c's
  grid bug; probe_d's constrained search is the correct one. Flagged for honesty.)

---

## 3. What a "community of zeros" would mean (s4h abstraction)

Strip the domain vocabulary. **The problem:** a rank–trace inequality upper-bounds the fraction of
"bad" atoms by comparing a trace t (total mass) with a Frobenius norm t₂ (squared energy) over a
Gram matrix. The refinement adds a positive correction tr Ψ(M) — the energy that the atoms' mutual
non-orthogonality contributes. **The constraint:** the atoms live on a line with repulsion
(level-repulsion), and their mutual correlations are set by a sign-alternating kernel k with zeros
at z1,z2,z3.

**What a "community" is in this geometry:** a *block of consecutive zeros whose intra-block
k²-energy is anomalously high relative to the inter-block energy* — precisely the span-4 tiling's
0.835 intra-fraction. Communities = the certificate's blocks. There is no mesoscale clustering
(Q=0.43, max size 9): the graph is a chain of weakly-overlapping clumps, exactly as the window
method assumes. A "community of zeros" is therefore **not** a mysterious structure — it is the
unit the certificate already counts (a good block), and its meaning is: *a place where the
two-moment data saturate the rank–trace inequality locally*.

**Can pair-correlation structure force simple+on-line?** The mechanism is already live: the
refinement's positivity is a *network property* — the Gram graph cannot be orthogonal (frustrated
triangles, §2.3) and cannot be zero-energy (kernel zeros not commensurate, §2.8). The open
question is whether the *magnitude* of tr Ψ(M) (the network's "energy density") can be converted
into a proportion bound that beats 0.6725/0.6730 — that is Q1/Q2, and the network lens sharpens
three sub-questions:
- The per-block→liminf passage needs a positive-density argument for good blocks. §2.7 shows the
  per-atom energy is **assortative** (0.402) — if energy clumps, good blocks are *rarer but more
  massive*; a Poisson/independent-block model is wrong. This is a network-statistics correction to
  the Markov-vacuity problem (Q1).
- §2.2 shows Σ6-gaps > 4 for **100%** of span≤9 windows — the span-4 reading of the 7-pt
  per-block floor 3.8e-3 is empirically dead; the operative span is 9 (consistent with
  SPAN-03 in the master list).
- The floor's *binding* term is k²(u+v) (§2.8) — the *sum* gap, i.e. a *triangle* in the network.
  The 3-pt floor is set by a frustrated triangle, not by a single edge. Any attempt to beat the
  floor must attack the triangle geometry (e.g., 4-atom anchors), not single-gap statistics.

---

## 4. Twelve CONJECTURED ideas + how to test each

Test data: `scratch/idea-network-rs/data/zeros_100k.txt` (and `zeros_odlyzko1.txt`, 100k, same
count — a second dataset for robustness). All tests below are S/M-effort Rust or Python (mpmath
for exploration only, never final).

### NET-01 — Assortativity-aware per-block→liminf passage (Q1 attack)
**Idea:** replace the vacuous Markov density argument (E[Σ6]≈8.9>4) with a *concentration bound on
the intra-block energy* using the measured energy assortativity (0.402): if good blocks (low
intra-energy) are clumped, their density can be bounded by a Chebyshev/moment argument on the
assortative sequence instead of by independence.
**Why might work:** the master list's SPAN-01/A6-01 need the same density; assortativity is a
measurable, certificate-relevant statistic that the current argument ignores.
**Why might fail:** concentration on dependent sequences may need higher moments we can't certify;
assortativity may be a finite-data artifact.
**Test (S):** compute the empirical density of good 7-blocks (intra-S2 below 3.8e-3 and below
7·5.43e-4) in sliding windows; compare against the assortativity-corrected prediction and the
independence prediction. Extend `probe_c §D`.
**Status:** CONJECTURED (statistic CHECKED NUMERICALLY, §2.7).

### NET-02 — Community-block certificate: use the detected Louvain blocks as certificate atoms
**Idea:** instead of the fixed span-4 tiling, run the rank–trace chain on the *Louvain-detected*
blocks (which maximize intra k²-energy) and compare the per-atom ε. If detected blocks have higher
intra-energy, the certificate's ε per block is higher → potentially a better constant.
**Why might work:** the span-4 tiling is only *near*-optimal (0.835 vs span-6 0.893); a
community-aware tiling may capture more energy per atom at fixed span-9.
**Why might fail:** the certificate's window (span ≤ 4 for 3-pt, ≤ 9 for 7-pt) is fixed by the
*data* (the two-moment sums), not by the tiling; arbitrary blocks may not satisfy the window's
span bound → the ε doesn't apply.
**Test (M):** in `probe_f`, replace the span-4 tiling with Louvain blocks of span ≤ 9, recompute
intra-fraction and per-atom S2 distribution; compare vs the span-4/span-6 tilings.
**Status:** CONJECTURED.

### NET-03 — Weak-tie (kernel-zero) edges as "repair" probes
**Idea:** the 2.4% weak edges (|k|<0.01, concentrated near z1=1.057) are the *only* places where
the Gram graph is nearly orthogonal. If the certificate's atoms were placed at kernel zeros, the
rank–trace inequality would be *looser* (orthogonality ≈ equality case). Test whether excluding or
reweighting these weak-edge atoms changes the constant — a "structural hole" analysis.
**Why might work:** §2.4 shows weak ties are rare and non-bridging; they may be the *only* slack
the certificate has, so targeting them (via a block design that avoids them) could tighten ε.
**Why might fail:** the certificate sums over ALL atoms; you can't exclude atoms without changing
the two-moment data (t, t₂) which are fixed by the window.
**Test (S):** histogram wᵢ and its weak-edge contribution; run the rank–trace with the weak-edge
pairs removed and see if the inequality is tighter (i.e., a smaller ‖·‖²_F at fixed t).
**Status:** CONJECTURED.

### NET-04 — Frustration index as a per-block penalty
**Idea:** define a "frustration index" F(block) = fraction of sign-mixed triangles (§2.3: 95% of
triples are mixed). Use F as a *covariate* to weight blocks: blocks with more frustration have more
orthogonality-breaking, hence higher tr Ψ. Feed the F-weighted ε into the constant formula.
**Why might work:** §2.3 shows the Gram graph is maximally frustrated; the refinement's positivity
is exactly the frustration's trace. Weighting by frustration may extract more mass than the flat
per-atom ε.
**Why might fail:** the certificate's ε is already a *lower bound* on tr Ψ over the domain; a
covariate that's positive everywhere doesn't increase the certified bound unless it's also a
certifiable lower bound per block.
**Test (S):** compute F per span-4 block and regress intra-S2 on F; check whether F is a
consistent predictor (i.e., could serve as a certified per-block minorant).
**Status:** CONJECTURED.

### NET-05 — Triangle-bound improvement: attack the k²(u+v) term
**Idea:** §2.8 shows the 3-pt floor's binding term is k²(u+v) at the sum gap. The floor is
2.22e-4 because no (u,v) with u+v≤4 can put all three gaps near kernel zeros (defect z1+z2−z3 =
0.067). Improve the floor by *proving* a better lower bound on k²(u+v) over the domain (a
triangle-inequality in the network), not by searching (u,v).
**Why might work:** the floor is near-tight (0.52% margin, verified); the defect is structural
(commensurability), so a *proof* of the defect bound is plausible and would replace the
numerical/0.52%-margin worry (the top honesty risk in verify-gram-stability.md flaw (b)).
**Why might fail:** the defect 0.067 is a number, not an inequality; proving k²(u+v) ≥ c over the
domain may require a nontrivial estimate on the sinc closed form.
**Test (S):** on the closed form, certify min k²(u+v) over u,v≥0, u+v≤4 (extend `probe_d §1` with
finer grid + interval arithmetic); check whether the minimizer's u+v is a *fixed* value (3.065, so
k²(3.065) = 1.49e-4 is the binding term).
**Status:** CONJECTURED (floor CHECKED NUMERICALLY, §2.8).

### NET-06 — Longest-run statistic as an RH-flavored diagnostic (source-trace honesty)
**Idea:** the unfolded longest gap-sign run is 7 (not 70; the 70 is a global-mean artifact). Use
the *distribution* of long runs (not their existence) as a null diagnostic: GUE predicts
specific run-length statistics; deviations would signal non-GUE structure in the zeros that the
certificate's pair-correlation data might be missing.
**Why might work:** run-length statistics are a cheap, sensitive probe of level repulsion vs
contagion; the master list's ATOM-02/NUM-05 (empirical S2 distribution) is the same class.
**Why might fail:** run statistics are a *consequence* of pair correlation, not an independent
input; they add no new constraint to the two-moment certificate.
**Test (S):** extend `probe_d §2` to full run-length distribution (not just longest), compare to
GUE-simulated run statistics.
**Status:** CONJECTURED (unfolded longest run = 7 CHECKED NUMERICALLY, §2.5).

### NET-07 — Assortativity of wᵢ as a mixing-layer for the per-block→liminf proof
**Idea:** the 0.402 energy assortativity is a *mixing* signal: high-wᵢ atoms cluster. A
per-block→liminf proof could exploit this as a "slowly-varying energy field" (block energies are
positively correlated), turning the vacuous first-moment Markov into a *second-moment* statement
via the empirical variance of wᵢ (var wᵢ = ? measured: p95/p05 ratio ~ 22).
**Why might work:** the master list's A6-01 (Selberg-variance bridge) is the same idea; the
network lens adds the *measured* assortativity as a quantitative input, potentially sharpening the
second-moment bound.
**Why might fail:** positive correlation can *hurt* a second-moment bound (clumping reduces the
effective sample size); the direction of the effect needs care.
**Test (S):** compute var(wᵢ) and the block-energy variance explicitly; fit a lag-1 AR model to
wᵢ and estimate the effective sample size for block-density.
**Status:** CONJECTURED (assortativity CHECKED NUMERICALLY, §2.7).

### NET-08 — Betweenness/centrality on the Gram graph: are some zeros "keystone"?
**Idea:** compute betweenness centrality of zeros in the span-4 Gram graph. If a few zeros carry
disproportionate k²-bridges (inter-block connectors), the certificate's block decomposition may be
suboptimal *at the cuts*, and a keystone-aware cut could reduce inter-block energy leakage
(currently 16.5% of total).
**Why might work:** inter-block energy (2.46e3) is 16.5% of the total; if it concentrates on few
edges, targeted cuts could push intra-fraction from 0.835 toward the span-6 value 0.893 *at fixed
span-4*.
**Why might fail:** the graph is a path; betweenness on a path is trivially high at all interior
nodes (no keystone structure).
**Test (M):** exact betweenness on a downsampled window (4000 zeros, R=2.0 graph) via
`probe_f`-style; compare edge-centrality vs k²-weight.
**Status:** CONJECTURED.

### NET-09 — Multi-scale community (block-in-block): nested span-4 ⊂ span-9
**Idea:** the certificate uses span-4 (3-pt) and span-9 (7-pt) blocks. Treat these as *nested
communities* and check whether the intra-energy of a span-9 block is the sum of its span-4
sub-blocks' energies plus a *cross term* that is systematically positive/negative. A systematic
cross-term sign would give a *free* correction to the 7-pt ε (the master list's CI-80
mixed-certificate frontier is adjacent).
**Why might work:** §2.2 (100% Σ6>4) says span-9 blocks are the operative units; a nesting
identity (energy additive + cross-term) could upgrade the 7-pt ε from per-atom 5.43e-4 to a
provably larger value.
**Why might fail:** the cross term is k(u+v)-type energy across the sub-block cut — exactly the
inter-block energy the current certificate ignores; it may be negative on average (anti-assortative
cuts).
**Test (S→M):** compute the cross-term distribution over all span-9 windows (extend `probe_c §D`);
test sign and magnitude.
**Status:** CONJECTURED.

### NET-10 — Degree-assortativity as a proxy for the "arithmetic" 2/3 (Theorem A discriminator)
**Idea:** the master list's A2 blocker says Theorem A's 2/3 may be data-limited ("2/3 is
arithmetic"). A network proxy for data-saturation: compute the rank–trace ratio t²/(r·t₂) on the
*real* Gram data (with the correct t = N₀ with-multiplicity count, r = distinct count) — the Q1
discriminator R. If R is already ~1 on real data, the 2/3 is saturated and the refinement transfer
is vacuous (matches transfer-stability-online.md §5 A2).
**Why might work:** it's the exact discriminator named in the notes; the network lens just computes
it on real zeros (which exist), where the with-multiplicity count is trivially = simple count
(all computed zeros are simple).
**Why might fail:** real zeros are all simple → R = t²/(r·t₂) with r = t = N₀ measures only the
simple-atom ratio, not the multiplicity obstruction.
**Test (S):** compute R = t²/(r·t₂) for the span-4/span-9 Gram blocks of the 100k zeros; compare
to the certificate's data-saturation threshold.
**Status:** CONJECTURED (compute is S; see also NET-11).

### NET-11 — Data-saturation read: the rank–trace ratio on real Gram blocks (Q1 discriminator)
**Idea:** for each span-4 block, compute the block's rank–trace ratio ρ = t²/(r·t₂). If the
*typical* block has ρ close to 1 (data-saturated), the refinement's ε has little room; if ρ is
far below 1 (slack-limited), the ε-term can bite. This is the "read" the master list's CI-74
(read-constrained τ-floor) and RE-13 (data-limited ceiling) need, computed on real zeros.
**Why might work:** it's cheap (per-block 3×3 and 7×7 Gram eigen-decompositions on 100k zeros)
and directly measures the certificate's slack — the single most decisive number for whether the
refinement can move the constant.
**Why might fail:** the real zeros' Gram blocks may not be the same as the *worst-case* blocks the
certificate bounds (the certificate's ε is a domain infimum, not a data average); a high data ρ
doesn't contradict a low worst-case ρ.
**Test (M):** Rust eigendecomposition of Gram blocks (span-4 and span-9) over the 100k zeros;
report the distribution of ρ and of tr Ψ(M).
**Status:** CONJECTURED.

### NET-12 — "Zero graph Laplacian" spectral read: λ₂ as a block-connectivity witness
**Idea:** the Gram graph's normalized Laplacian's second eigenvalue λ₂ (algebraic connectivity)
measures how tightly the span-4 blocks are connected. If λ₂ is systematically *large* (blocks
well-connected), the inter-block leakage is unavoidable → the certificate's block decomposition is
as good as it gets; if λ₂ is small (blocks nearly disconnected), a better decomposition exists.
**Why might work:** gives a principled, spectral answer to "is the span-4 tiling a real
community?" (currently answered empirically, §2.6).
**Why might fail:** the Gram graph is a path (probe_f shows chain-like), so λ₂ → 0 in the limit;
the read may be trivially small and uninformative.
**Test (M):** compute λ₂ of the span-4 Gram graph on a downsampled window; compare to the random
tiling's λ₂ null.
**Status:** CONJECTURED.

---

## 5. Cross-references to the master list (avoid repeats)

- NET-01/NET-07 ≈ SPAN-01/A6-01/PC-01 (density passage) — my contribution: the *measured*
  assortativity (0.402) and the 100% Σ6>4 fact as quantitative inputs.
- NET-11 ≈ CI-74/RE-13 (data-saturation read) — my contribution: compute on real Gram blocks.
- NET-09 ≈ CI-80 (mixed-certificate frontier) — nested-block cross-term.
- NET-03 ≈ OS-13 (commensuration test) — the defect z1+z2−z3 = 0.067 as a mechanism.
- NET-05 ≈ Q2 (closed forms for floors) — the binding k²(u+v) term.
- NET-06 ≈ ATOM-02/NUM-05 (empirical S2) — but framed as run/contagion honesty.

---

## 6. Honesty register (labels)

- **CHECKED NUMERICALLY:** all §2 numbers (script+command in §2 headers); floor 2.221575e-4
  reproduces the verified 2.221491e-4 (0.52% margin); unfolded longest run 7; ac(1) = −0.357 vs
  shuffled null +0.0009; intra-fraction 0.8349 vs null max 0.7644; 100% Σ6>4; 95% frustrated
  triples; weak ties non-bridging; energy assortativity 0.402; Louvain Q=0.43.
- **CONJECTURED:** all 12 ideas (by design — they are proposals with test protocols, not results).
- **ABANDONED:** the "70-run contagion" phenomenon — shown to be a global-mean rescaling artifact
  (unfolded longest run = 7, edge-positioned). The *honest* contagion question is the unfolded
  statistic.
- **INCONCLUSIVE:** whether the network statistics (assortativity, communities) can actually be
  converted into a *proven* constant improvement — the conversion requires the certificate's chain
  algebra (Q1/Q2), which is open.
- **NOT FOUND / NOT FABRICATED:** the task-cited `discovery-6732629.md` (67.3263%) and
  `attack-vector-catalog*.md` do not exist in this repo; all constants cited here come from the
  verified `discovery-gram-stability-673.md` and `verify-gram-stability.md`. A 67.3263% record
  would be a **new constant** (above 0.673008527927…); it is not something I claim.

---

## 7. Files

- `scratch/idea-network-rs/src/bin/probe_{a..f}.rs` — all probes (Rust, compiled to
  `target/x86_64-unknown-linux-musl/release/`).
- `scratch/idea-network-rs/data/zeros_100k.txt` (+ `zeros_odlyzko1.txt` in
  `scratch/idea-random-rs/data/`) — the zeros data (the task's `tools/data/` is empty).
- This file: `research/waves/wave-blast/results/idea-network.md`.

---

RESULT: CONJECTURED — 12 network-theoretic ideas delivered; zeros form a frustrated, sub-Poisson,
chain-like Gram network with no contagion (longest unfolded run 7, not 70), no weak-tie bridges,
and genuine but weak block communities (span-4 tiling 0.835 intra-energy vs 0.763 random null);
the certificate's span-4 blocking is a real community structure, energy is assortative (0.402),
and every 7-atom span≤9 window has Σ6-gaps > 4 — but the task-cited 67.3263% record and
attack-vector catalog do not exist in this repo, so all claims are grounded in the verified
0.6725/0.6730 constants.

---

# VERIFICATION SUPPLEMENT — idea-network (round 2, independent probe set g–j)

**Agent:** idea-generator (s4h-network), second pass. **Date:** 2026-08-12.
**Purpose:** the file above (round 1) delivered 12 CONJECTURED ideas with probes a–f. This
supplement adds an independent set of probes (g–j) that (i) confirm the round-1 headline
statistics, (ii) add four new decisive facts (energy backbone, no giant component, 100× floor
margin, convergence of ac(1)), and (iii) reports one honest probe bug (probe_h class index) and
its fix. All claims CHECKED NUMERICALLY via Rust binaries in
`scratch/idea-network-rs/src/bin/probe_{g,h,i,j}.rs`, outputs in
`scratch/idea-network-rs/out/probe_{g,h,i,j}.txt`.

Build command (all four):
```
cd scratch/idea-network-rs
export PATH=$HOME/.cargo/bin:$PATH
export RUSTFLAGS="-C linker=rust-lld -C link-self-contained=yes"
cargo build --release --target x86_64-unknown-linux-musl --bin probe_g --bin probe_h --bin probe_i --bin probe_j
./target/x86_64-unknown-linux-musl/release/probe_g data/zeros_100k.txt
./target/x86_64-unknown-linux-musl/release/probe_h data/zeros_100k.txt
./target/x86_64-unknown-linux-musl/release/probe_i
./target/x86_64-unknown-linux-musl/release/probe_j data/zeros_100k.txt
```

---

## S1. The energy backbone — 88% of the Gram's k²-energy is on CONSECUTIVE pairs (probe_h §1)

**CHECKED NUMERICALLY** — `probe_h data/zeros_100k.txt`:

| pair class | energy share | pairs |
|---|---|---|
| \|i−j\|=1 (consecutive) | **87.99%** | 99,978 |
| \|i−j\|=2 | 7.83% | 99,560 |
| \|i−j\|=3 | 2.96% | 94,249 |
| \|i−j\|=4 | 1.15% | 56,401 |
| \|i−j\|=5 | 0.06% | 5,566 |
| \|i−j\|≥6 | 0.00% | 0 |
| **top-3 classes** | **98.79%** | — |

**Interpretation.** The certificate's Gram energy (tr Ψ(M) = 2Σ k² over the span-4 window) is
**dominated 88% by the nearest-neighbor edges** — the consecutive-gap pairs. The network is a
**1-D chain backbone**, not a dense graph: the entire two-moment/refinement content is
effectively a *function of the consecutive-gap sequence alone* (98.8% of energy in |i−j|≤3).
**Consequence for the certificate:** any "community" refinement must be a *nearest-neighbor*
(chain) statement; a 2-D/loopy community model would be adding energy that isn't there. This
quantifies, from the data side, why the window method (consecutive-atom blocks) is the natural
object — the network lens *confirms* the chain ansatz rather than offering an alternative
topology.

**Caveat (honesty):** this is energy under the certificate's OWN kernel k; it is a statement about
how the *Gram network* concentrates, not about all possible pair correlations.

## S2. No giant component — the line fragments into clumps (probe_j)

**CHECKED NUMERICALLY** — `probe_j data/zeros_100k.txt`:

| R (mean-spacing-1) | components | largest | largest % | second |
|---|---|---|---|---|
| 1.0 | 45,501 | 12 | 0.01% | 11 |
| 1.5 | 11,825 | 68 | 0.07% | 62 |
| 2.0 | 2,109 | 672 | 0.67% | 648 |
| 3.0 | 107 | 95,195 | 95.19% | 835 |

- At R=1.5 (the certificate-relevant interaction range), the distance graph has **no giant
  component**: 11,825 components, largest = 68 nodes (0.07%), mean component size = 8.46, edges =
  104,304.
- Percolation threshold sits between R=2 (0.67% largest) and R=3 (95% largest) — the zeros'
  distance graph crosses the giant-component transition in a narrow band, exactly as the mean gap
  ≈ 0.75 (raw scale) / 1 (unfolded) suggests (critical R for a line Poisson is ~ the mean gap
  times log N; for repelled zeros it's pushed up by level repulsion).
- **Interpretation:** at certificate-relevant radii the "network of zeros" is a **fragmented
  chain of clumps**, not a connected society. Contagion/community/weak-tie language at R≤2 is
  vacuous *topologically* — there is no giant component for anything to spread through. The
  meaningful units are the small clumps (component size ~8), which matches the certificate's
  block size 4–9 atoms. **This is a structural argument FOR the window method**: the zeros'
  interaction graph self-fragments at exactly the certificate's block scale.

## S3. The 7-atom window energy is ~100× above the ε-floor (probe_g §1)

**CHECKED NUMERICALLY** — `probe_g data/zeros_100k.txt`:

| span | windows | mean S2_7 | min S2_7 | p1 | frac < 3.8e-3 |
|---|---|---|---|---|---|
| 6 | 59,111 | 1.0371e0 | 3.1691e-2 | 2.856e-1 | 0.00000 |
| 7 | 89,892 | 9.2559e-1 | 2.9217e-2 | 1.721e-1 | 0.00000 |
| 8 | 96,663 | 8.9502e-1 | 2.9217e-2 | 1.430e-1 | 0.00000 |
| 9 | 98,625 | 8.8425e-1 | 2.9217e-2 | 1.305e-1 | 0.00000 |
| 11.5 | 99,707 | 8.7718e-1 | 1.2025e-2 | 1.190e-1 | 0.00000 |

- The empirical minimum S2_7 over **98,625 span≤9 windows is 2.92e-2** — a factor **~77 above**
  the per-block floor 3.8e-3 (and ~54× above the 7×5.43e-4 per-atom reading). **Zero** windows
  fall below either floor reading.
- The empirical mean S2_7 is 0.884 — **230× above the floor**.
- **Interpretation (the big one):** the ε-floor 3.8e-3 (per-block) / 5.43e-4 (per-atom) is
  **nowhere near tight on real zeros** — the real 7-atom windows carry 100× more energy than the
  worst case. This is a *slack* signal: if the certificate could use the *empirical* (positive-
  density) energy rather than the domain-infimum floor, the ε-term would be ~100× larger and the
  constant shift proportionally larger. The gap between "domain-infimum floor" (certified but
  pessimistic) and "data-typical energy" (100× larger) is **the quantitative frontier the network
  lens exposes**. It is exactly the Q1 per-block→liminf passage: the certificate needs a
  *density* argument (what fraction of blocks have energy near the floor?) rather than a *floor*
  argument (all blocks ≥ floor). Round 1's NET-01/NET-07 are the right targets; S3 gives the
  magnitude of the prize.
- Note the earlier Q1 note ("E[Σ6]≈8.9>4 → Markov vacuous") is **confirmed empirically**: mean
  Σ6-gaps over span≤9 windows = 5.93, and **100% of windows have Σ6 > 4** (probe_c §D) — a
  first-moment Markov argument on the 7-pt span is not just weak, it is *strictly vacuous* (the
  event is certain).

## S4. ac(1) converges but is NOT GUE — and the gap is real (probe_h §2)

**CHECKED NUMERICALLY** — `probe_h data/zeros_100k.txt`:

| N | ac(1) (unfolded) |
|---|---|
| 1,000 | −0.4042 |
| 5,000 | −0.3775 |
| 20,000 | −0.3646 |
| 100,000 | −0.3571 |
| GUE (lit.) | ≈ −0.2448 |

- ac(1) converges (slowly, −0.404 → −0.357) and is **robustly negative**, while the shuffled-gap
  null gives +0.0009 ± 0.0007 (probe_e §3). The value −0.357 is **~1.5× more anti-correlated than
  the GUE literature value −0.2448**.
- **Interpretation:** consecutive-gap anti-correlation in the real zeros is *stronger* than the
  standard GUE ensemble prediction. This is a *potential non-GUE signal* — but it is NOT a new
  certificate input (the certificate's two-moment data use pair correlation, not consecutive-gap
  correlation). **Honest label:** CHECKED NUMERICALLY as a statistic; INCONCLUSIVE as a
  mechanism (finite-N convergence is slow; the literature constant itself is ensemble-dependent).
- This strengthens round-1 §2.5's verdict: short-range anti-correlation is the only "contagion"
  structure, and it is *negative* (repulsive), i.e. the opposite of spreading.

## S5. Sign-pattern does NOT determine the floor (probe_h §3)

**CHECKED NUMERICALLY** — `probe_h data/zeros_100k.txt`:

- Real gap-triples (u+v≤4): all-same-sign 4,900 (min S2 = 2.954e-4); mixed 94,660 (min S2 =
  2.384e-4). Both classes have minima **above** the continuum floor 2.2216e-4.
- The floor is attained only in the continuum; real triples never reach it (min real S2 ~ 2.4e-4
  vs continuum 2.22e-4 for 3-atom; for 7-atom the margin is ~100×).
- **Interpretation:** a *sign-only* (topological/frustration) lower bound cannot reproduce the
  certified ε-floor — magnitudes of |k| matter. This rules out the cheap "frustration index as
  penalty" route (round-1 NET-04) as a *certified* bound (it remains useful only as a covariate
  for the density/assortativity arguments, NET-01/NET-07).

## S6. Floor precision and the k²(u+v) binding term (probe_i)

**CHECKED NUMERICALLY** — `probe_i` (adaptive refinement):

```
coarse: min S2 = 2.22853828e-4 at (1.0540, 2.0120)
refined: min S2 = 2.22157504e-4 at (1.053000, 2.012000)
k(u)^2 = 1.422664e-5, k(v)^2 = 5.878857e-5, k(u+v)^2 = 1.491423e-4
doc floor: 2.221491e-4; delta = 8.40e-9
```

- The constrained min S2 = **2.22157504e-4** matches the documented 2.221491e-4 to 8.4e-9
  (0.52% margin as documented) — floor independently confirmed.
- **k²(u+v) = 1.491e-4 is 67.1% of the floor** at the minimizer (1.491e-4 / 2.2216e-4). The
  binding term is the *sum-gap* k²(u+v) — a triangle in the network, confirming round-1 §2.8 and
  sharpening NET-05: the floor is dominated by the u+v ≈ 3.065 (off the kernel zero 3.020) edge,
  i.e. by the **commensurability defect z1+z2−z3 = +0.0671**.

## S7. Honest bug report (probe_h class index)

- probe_h initially indexed pair-classes with an off-by-one (consecutive pairs written to slot 0,
  reported as 0%). Fixed by re-indexing to `by_class[c]` with c = |i−j|. The corrected output
  (§S1) is the honest one: **consecutive pairs carry 87.99%**, not 0%.
- probe_c §C's "grid min 5.83e-5 at (2.022,2.024)" **violates u+v≤4** (2.022+2.024=4.046>4) —
  an unconstrained-grid bug already flagged in round-1 §2.8; probe_d/probe_i's constrained search
  (2.2216e-4) is correct. Restated here so no future agent re-quotes the 5.83e-5.

---

## S8. What the supplement changes (synthesis)

1. **The certificate's unit is the chain, confirmed by data.** 88% of Gram energy on consecutive
   pairs (S1) + no giant component at R≤2 with mean clump size ≈ 8.5 (S2) = the zeros' interaction
   network is a *fragmented 1-D chain whose clumps are exactly the certificate's block scale*. A
   "community of zeros" is real, but it IS the window block — there is no alternative mesoscale
   structure to find (round-1 §2.6, Louvain Q=0.43, reinforced).
2. **The ε-floor is not tight on real data — by 100×.** S3's min-S2_7 = 2.92e-2 vs floor 3.8e-3
   (and mean 0.884) is the single most actionable number: it quantifies the prize of replacing the
   worst-case floor with a *density* argument (the Q1 per-block→liminf passage). Round-1 NET-01
   and NET-07 are upgraded from "might work" to "the frontier, with the magnitude known".
3. **Weak ties, communities, contagion: all vacuous at certificate scale.** Weak edges
   non-bridging (round-1 §2.4), no giant component (S2), longest unfolded run 7 (round-1 §2.5),
   ac(1) = −0.357 anti-correlated (S4). The network lens's standard vocabulary (Granovetter,
   percolation, spreading) has **no purchase on the zeros at the interaction range the certificate
   uses** — the honest network facts are the chain/energy ones (S1, S2, S3), not the sociology.
4. **The floor is set by a frustrated triangle.** k²(u+v) dominates the 3-pt floor (S6); the
   defect z1+z2−z3 = 0.067 is the mechanism. NET-05 (prove a bound on k²(u+v) over the domain)
   remains the cleanest closed-form target.
5. **New data-backed proposal (upgrade to NET-01):** the 100× margin (S3) suggests a
   *two-tier certificate*: certify the floor ε over the domain (as now), but ALSO certify the
   *empirical density* of blocks with energy ≤ C·floor for a fixed C (e.g. C=2). If the density is
   ≥ p₀ > 0 with C·floor still ≪ mean (0.884), the per-block→liminf passage can use the
   two-tier (floor for all, density for the good ones) instead of the vacuous Markov. **Test:**
   extend probe_g §1 to compute, for C ∈ {2, 5, 10, 100}, the empirical fraction of span≤9
   7-windows with S2_7 ≤ C·3.8e-3; fit the density curve. CONJECTURED; the statistic is
   CHECKED NUMERICALLY to exist (fraction at C=1 is 0; at C≈8 (2.92e-2) it is 1/98,625 ≈ 1e-5).

---

## S9. Files

- Probes g–j: `scratch/idea-network-rs/src/bin/probe_{g,h,i,j}.rs`; outputs:
  `scratch/idea-network-rs/out/probe_{g,h,i,j}.txt`.
- Build + run commands: §supplement header.
- This supplement: appended to `research/waves/wave-blast/results/idea-network.md`.

---

RESULT: CONJECTURED — verified supplement: zeros form a fragmented 1-D chain (no giant component
at R≤2, mean clump ~8.5) with 88% of Gram k²-energy on consecutive pairs; the 7-atom window
energy is ~100× above the ε-floor (min 2.92e-2 vs 3.8e-3, mean 0.884) — the quantitative prize
for a density-based per-block→liminf passage (Q1); ac(1) = −0.357 (anti-correlated, 1.5× stronger
than GUE lit.); floor 2.221575e-4 confirmed to 8.4e-9 with k²(u+v) the 67%-binding frustrated-
triangle term; sign-pattern alone cannot reproduce the floor (magnitudes matter). Round-1's 12
ideas stand; NET-01/NET-07 upgraded to the live frontier with the magnitude known.

---

# EXECUTION VERIFICATION (independent re-run, 2026-08-12 15:17–15:18 +07)

**Verified by a fresh agent pass** (this execution): all ten Rust binaries
`probe_{a..j}` were re-run from source against `data/zeros_100k.txt` and every headline
number in rounds 1–2 reproduces exactly. Key re-run outputs (identical to the claims):

- `probe_a`: R=1.5 avg_deg=2.0861, clustering=0.1334, frac_deg0=0.0095; R2(0.1)=0.0168.
- `probe_b`: V/M=0.2189 @R=1.5 (sub-Poisson); weak |k|<0.01 edges = 2.40%;
  gaps within 0.05 of kernel zero z1 = 9.02%; longest raw run = 70 (edge artifact).
- `probe_c`: unfolded V/M=0.1757; frustrated triples 95.02%; z1+z2−z3 = +0.067103;
  span≤9 windows 98,625, 100% with Σ6-gaps > 4 (Markov-vacuous), min S2_7 = 2.9217e-2;
  span-4 intra-frac = 0.834894; per-atom energy mean 0.298, corr(w_i, gap-anom²)=0.1523.
- `probe_d`: constrained floor = 2.221575e-4 at (1.053, 2.012); k²(u+v)=1.4914e-4
  (67.1% of floor); energy assortativity = 0.4021; longest run = 70 at index 1
  (global-mean artifact — mean position of runs ≥10 = 0.060).
- `probe_e`: unfolded longest run = **7** (index 96309, γ=72446.675); ac(1) = −0.3571;
  shuffled null ac(1) = +0.0009 ± 0.0007; random-partition null intra-frac max 0.7644
  vs real 0.834894 (z ≫ 10).
- `probe_f`: span tilings intra-frac 0.787/0.835/0.868/0.893; Louvain-like Q = 0.428.
- `probe_g`: S2_7 min 2.9217e-2 (77× floor 3.8e-3), mean 0.884 (230×), frac < 3.8e-3 = 0;
  weak-edge cascade: theta=0.05 → 20,408 components, giant 45 nodes (0.04%).
- `probe_h`: consecutive-pair |i−j|=1 energy share = **87.99%** (top-3 classes 98.79%);
  ac(1) convergence −0.4042 (N=1k) → −0.3571 (N=100k); sign-only min S2 (2.95e-4 all-same,
  2.38e-4 mixed) both ≫ continuum floor 2.2216e-4 → sign pattern alone cannot set the floor.
- `probe_i`: floor = 2.22157504e-4, delta vs doc floor 8.40e-9. **Note:** `out/probe_i.txt`
  was missing from the inventory; written this pass (content above).
- `probe_j`: no giant component at R≤2 (R=1.5: 11,825 components, largest 68 = 0.07%,
  mean size 8.46); giant forms between R=2 (0.67%) and R=3 (95.19%).

**Data authenticity:** `data/zeros_100k.txt` (symlink → `scratch/idea-random-rs/data/zeros_100k.txt`)
spot-checked against known Riemann zeros: γ₁=14.134725142, γ₂=21.022039639,
γ₃=25.010857580, γ₁₀=49.773832478, γ₁₀₀₀₀₀=74920.827498994 — all correct. The zeros are
computed simple zeros on the line (no off-line/multiple zeros by construction), so the
network lens measures pair-correlation geometry, not the proportion itself.

**Verdict:** deliverable is complete, honest, and numerically grounded. All 12 CONJECTURED
ideas (NET-01…12) + 7-section verification supplement stand as written. The one corrected
file: `out/probe_i.txt` now exists.

RESULT: VERIFIED — re-ran all 10 probes (probe_a–j) from source; every headline claim
reproduces exactly (sub-Poisson chain V/M=0.219, no giant component at R≤2, 88% Gram energy
on consecutive pairs, min S2_7 = 77× the ε-floor, ac(1)=−0.357, floor 2.221575e-4 to 8.4e-9);
data spot-checked against known zeros; 12 CONJECTURED network ideas delivered with test
protocols; missing out/probe_i.txt inventory gap fixed.
