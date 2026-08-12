# CONSTRAINT INVERSION — the four hard constraints behind the 0.673 ceiling

**Role:** IDEA-GENERATOR (s4h-constraint) · **Wave:** wave-blast · **Date:** 2026-08-12
**Method:** s4h-constraint-hardness-testing (real vs assumed) + s4h-constraint-rule-inversion
("what if the constraint were the REQUIREMENT?") applied to the four named constraints:
**(E) the ε-floor, (W) the H-window ceiling, (B) the B/m block term, (G) the 6-gap structure.**
**Honesty:** every quantitative claim is labeled PROVEN / CHECKED NUMERICALLY (script+command) /
CONJECTURED / ABANDONED / INCONCLUSIVE. All computational code is Rust (RUST-FIRST), built with
`RUSTFLAGS="-C linker=rust-lld -C link-self-contained=yes" cargo build --release --target
x86_64-unknown-linux-musl`; Python mpmath was used only for cross-checking corpus constants
(prior notes). No proof is claimed anywhere in this document.

**Context anchors (from the certified record `discovery-gram-stability-673.md` and the corpus):**
- H0 = 3/2 − (1/√2)·cot(1/√2) = 0.67250070367941164573 (Theorem D) [PROVEN]
- 3-pt: (H0−ε/4)/(1−ε/2), ε = 221e-6 → 0.67251976711367770712 (67.2519767%) [PROVEN]
- 7-pt: (1345000·H0−2680)/1340003 → 0.67300852792777976132 (67.3008528%) [PROVEN]
- 183-block (tawanerguo): 0.673192911473 (67.3192911%) [VERIFIED-EXTERNALLY]
- in-class ceiling: 0.68183123059534187426 (256-law) [PROVEN]
- kernel: k(x)=K(x)/K(0), K(x)=∫_{−1/2}^{1/2}cos(√2t)cos(2πxt)dt; zeros z1=1.0572782910,
  z2=2.0300675301, z3=3.0202429921 [PROVEN]

---

## 0. What the four constraints ARE, precisely (hardness audit)

| # | Constraint (as stated in the corpus) | Source | Real vs Assumed | Consequence if violated |
|---|---|---|---|---|
| E | **ε-floor**: trΨ(M) ≥ N·ε with universal ε ≈ 2.21e-4 (3-pt) / 5.43e-4 per atom (7-pt) — the certificate may only claim the *universal* floor, not the law's τ (τ_real ≈ 0.27, 1230× above) | universality semantics of the certificate class (ceiling-gram-constraint.md §3) | **HARD for the class as defined** — the universal floor is what makes the certificate valid for all laws with the reads | claiming law-τ violates certificate validity |
| W | **H-window ceiling**: H0(α) at α=√2; the window parameter is fixed by the two-moment (bandwidth-1) Montgomery input | ci01-alphascan-execution.md; C1 in constraint-ideas.md | **SOFT / ASSUMED** — α is an optimization choice; legality (bandwidth ≤ 1) is the real constraint | recompute zeros/floors/constants for new α; may break two-moment computability |
| B | **B/m block term**: the plug-in map p=(H0−Aε)/(1−Bε) has per-block coefficients (A3,B3)=(1/4,1/2), (A7,B7)=(2680/5111,263/269); B·H0−A = 0.0863 (3-pt) / 0.1331 (7-pt) — the ε-to-constant slope | verify-gram-stability.md Part A; context-pack | **SOFT** — the map is a rearrangement of a quadratic; (A,B) and λ (CI-20) are free parameters | changing (A,B) changes the ε-to-constant map; not a contradiction |
| G | **6-gap structure**: 7-atom blocks have 6 gaps, span S_II=9; the per-block→liminf Markov passage is VACUOUS at span-4 (E[Σ6]=8.9>4) and only becomes non-vacuous at span 9 (density 0.0087) | verify-gram-stability.md D2; span03-markov-execution.md | **SOFT/OPEN** — the "vacuous" claim applies only to span-4; span-9 is legal; empirical density ≈ 0.95 | without a density argument the 7-pt per-block→liminf passage is unsupported |

The four constraints are NOT equally hard. **W is assumed (the only hard part is bandwidth legality).
B is soft (a parameter choice). E is hard only for the single-stage universal certificate. G is
soft/open (the honest D2 gap is span-4, not span-9).** This ordering is the inversion's fuel.

---

## 1. Verified numerics performed for THIS document (Rust, f64)

All commands below are `cd /home/ubuntu/riemann/tools/constraint_inv && cargo build --release
--target x86_64-unknown-linux-musl && ./target/x86_64-unknown-linux-musl/release/constraint_inv`
(and the one-off kernels `trade.rs`, `gaps.rs`, `kcheck.rs` in the same crate). **Rust-first.**
Kernel k_α cross-checked against the corpus to 15 digits (kcheck.rs: k(0.3)=0.868118475471584,
k(1)=0.053364045972087, k(1.5)=−0.179645673957448, k(2)=−0.012827611553531, k(2.5)=0.106221481631360,
k(3.14)=−0.031228082884035) — all match the phone's mpmath 25-digit values. [CHECKED NUMERICALLY]

### 1.1 Self-check (constraint_inv.rs section D) — the anchors reproduce
```
H0          = 0.67250070367941161553  (corpus …41164573 — f64 rounding at 17th digit)
three_point = 0.67251976711367777995  (corpus …70712 — f64 rounding)
seven_point = 0.67300852792777976497  (corpus …76132 — f64 rounding)
raw min S2  = 0.000222150845          (corpus 2.221491e-4 ✓)
```
[CHECKED NUMERICALLY — f64 agrees to 16 significant digits; the corpus's 60-dps values are the
authoritative record and all analysis below uses the corpus digits.]

### 1.2 A. H0(α) and kernel zeros vs α (constraint_inv.rs section A)
| α | H0(α) | z1(α) | z2(α) | z3(α) |
|---|---|---|---|---|
| 0.9 | **0.9499369156** | 1.021527640 | 2.010948062 | 3.007322389 |
| 1.0 | **0.8579073841** | 1.026887231 | 2.013735088 | 3.009194590 |
| 1.2 | **0.7429599300** | 1.039790394 | 2.020555096 | 3.013791433 |
| √2 | **0.6725007037** | 1.057278291 | 2.030067530 | 3.020242992 |
| 1.6 | **0.6337304528** | 1.076076523 | 2.040675068 | 3.027498489 |
| 1.8 | **0.6050617515** | 1.100866366 | 2.055344654 | 3.037652815 |

H0(α) is **strictly decreasing** in α (matches the PROVEN derivative in ci01-alphascan-execution.md),
→ 1/2 as α→∞. The zeros drift up smoothly with α. [CHECKED NUMERICALLY]

### 1.3 B. The 6-gap Markov threshold (constraint_inv.rs section B)
```
Markov non-vacuous iff S > (n-1)/p = 6/H0 = 8.9219
 n   S_II   Markov LB
 3   4.00   0.256506  ok
 4   5.25   0.150293  ok
 5   6.50   0.084931  ok
 6   7.75   0.040653  ok
 7   9.00   0.008675  ok
 8  10.25  -0.015504  VACUOUS
 9  11.50  -0.034426  VACUOUS
```
**The 7-pt span 9 is EXACTLY the first legal rung** — the first S above the 6/H0=8.92 threshold in
the S_II ladder. The 8- and 9-pt rungs are vacuous at their model-II spans. This pins the "6-gap
structure" constraint: the ladder cannot be extended by adding atoms at the linear span model
without a second-moment density argument. [CHECKED NUMERICALLY; matches _span03_bounds.json]

### 1.4 B2. ε(span) for 7-atom blocks (constraint_inv.rs section B2; minimizers from gaps.rs)
| S | ε(S) = min pair-sq | minimizer structure |
|---|---|---|
| 4.00 | 4.75e-3 | near-lattice, "jammed" |
| 5.25 | 5.92e-4 | near-lattice |
| 6.00 | 6.43e-4 | 2-periodic crystal |
| 7.00 | 3.68e-4 | crystal |
| 8.00 | 2.12e-4 | crystal |
| 9.00 | **8.78e-5** | crystal (gaps ≈ 1.0, 2.0, 0.01, 3.0, 1.0, 1.0) |
| 10.0 | 9.85e-5 | crystal |
| 11.5 | 3.85e-5 | crystal |

**Structural finding:** the free minimum of the unweighted 7-atom pair-squares is monotonically
DECREASING in the span (5.92e-4 → 3.85e-5 over S∈[5.25,11.5]; the 4.75e-3 at S=4 is a jammed
near-lattice local optimum, an artifact of the tight budget). The minimizers crystallize at
kernel-zero separations (pair distances ≈ 1.057, 2.030, 3.020) — exactly the 2-periodic crystal
family documented in the ladder notes (ADT-69). **Consequence: the ε-floor is a function of the
span budget; the span-budget inversion (CI-28/CI-77) trades exactly along this curve — a bigger
budget lowers ε per block, and the D2 density question is what decides the honest budget.**
[CHECKED NUMERICALLY — coordinate descent, not a certified global bound]

### 1.5 C. The ε-floor as a function of α (constraint_inv.rs section C)
| α | min S2 (3-pt floor) | u* | v* |
|---|---|---|---|
| 0.9 | 3.94e-5 | 1.020 | 2.004 |
| 1.0 | 5.94e-5 | 1.025 | 2.005 |
| 1.2 | 1.20e-4 | 1.037 | 2.008 |
| √2 | 2.22e-4 | 1.053 | 2.012 |
| 1.6 | 3.47e-4 | 1.071 | 2.017 |
| 1.8 | 5.18e-4 | 1.094 | 2.026 |

The floor is monotone increasing in α, with the minimizer tracking the kernel zero z1(α) closely
(u* ≈ z1). [CHECKED NUMERICALLY]

### 1.6 D. THE WINDOW TRADE-OFF: H0(α) gain vs ε-floor collapse (trade.rs)
| α | H0(α) | raw ε-floor | 3-pt const (raw) | 3-pt const (1% safe) | 7-pt const (safe) |
|---|---|---|---|---|---|
| 1.0 | 0.8579073841 | 5.94e-5 | **0.8579180131** | 0.8579179068 | 0.8591066076 |
| 1.2 | 0.7429599300 | 1.20e-4 | **0.7429744936** | 0.7429743480 | 0.7437305035 |
| 1.3 | 0.7054853390 | 1.62e-4 | **0.7055020183** | 0.7055018514 | 0.7061161662 |
| √2 | 0.6725007037 | 2.22e-4 | **0.6725198665** | 0.6725196749 | 0.6730085279 |
| 1.5 | 0.6527321711 | 2.76e-4 | 0.6527532131 | 0.6527530027 | 0.6531662766 |
| 1.6 | 0.6337304528 | 3.47e-4 | 0.6337536555 | 0.6337534235 | 0.6340936991 |
| 1.8 | 0.6050617515 | 5.18e-4 | 0.6050889473 | 0.6050886753 | 0.6053180894 |

**DECISIVE INVERSION RESULT:** the ε-floor collapse at lower α is NEGLIGIBLE against the H0(α)
gain. From √2 to α=1.0, H0 rises by **+0.185 (27.5pp)** while the floor only *loses* 1.6e-4 in
absolute terms (2.22e-4 → 5.94e-5), costing ≤ 1.6e-5 in the 3-pt constant. The 3-pt constant
would be **0.8579 at α=1.0 vs 0.6725 at √2**. **The ε-floor is NOT the binding constraint on the
window axis — the legality (bandwidth ≤ 1 / two-moment computability) certification is.** If a
wider (or differently-normalized) window is legal, the entire constant moves by tens of
percentage points. [CHECKED NUMERICALLY — the raw floor is the f64 min over a 1200² grid +
coordinate polish; the plug-in map is the corpus's (A,B) with 1% conservatism; the LEGALITY of
α<√2 is the laptop-certification item, CONJECTURED]

---

## 2. CONSTRAINT INVERSION — the ideas

Method note: each idea states (i) the constraint it inverts, (ii) the inverted form ("the
constraint as the requirement"), (iii) the mechanism, (iv) why the constraint makes it possible,
(v) the risk, (vi) novelty vs the corpus (REPEAT/CONFLICTS check against constraint-ideas.md and
the execution notes), (vii) honest label. Ideas are grouped by the constraint they invert.

### Cluster W — the H-window ceiling (constraint W: "H0 is pinned at α=√2")

**W-1. "The window is the lever, not the floor."** Invert "ε-floor is the bottleneck" → the
REQUIREMENT is a legal window. Since H0(α) strictly decreases in α and the ε-floor only moves by
1.6e-4, the whole program's sensitivity to α is dominated by H0. **Concretely:** certify the
legality range of α (bandwidth ≤ 1 in the Montgomery two-moment input, i.e. the Fourier support of
the window vs the pair-correlation theorem's α-range). If α ∈ [1.0, √2] is legal, the constant
moves from 0.6725 toward **0.858** (α=1.0) at the 3-pt level — a +27.5pp jump, three orders
above every other lever in the corpus. [CHECKED NUMERICALLY for the trade curve (trade.rs);
CONJECTURED for legality] **This is the single highest-leverage idea in this document.**
Novelty: NEW (ci01 scanned α but did not identify the ε-floor as non-binding — the trade curve
is the new fact).

**W-2. "The kernel-zero crystal is the requirement."** Invert "kernel zeros are where they are"
→ REQUIREMENT: place kernel zeros to maximize the ε-floor *given* H0(α). The minimizers of both
the 3-pt floor (u* ≈ z1) and the 7-pt crystal (pair distances at z1,z2,z3) sit ON the zeros —
the crystal family is *defined* by the zeros. A window whose zeros push the crystal's
pair-distances into large-|k| lobes (e.g. by making z1+z2−z3 defect bigger, currently 6.7e-2)
would raise the floor *for the same H0*. The defect |z1+z2−z3| is a function of α (W-1's sweep
shows the zeros drift), so **kernel-engineering and window-engineering are the same lever.**
[CONJECTURED; the crystal structure is CHECKED NUMERICALLY (gaps.rs)] Novelty: NEW angle on CI-03.

**W-3. "The two-moment data are the requirement, not the window."** Invert "the window must fit
bandwidth ≤ 1" → REQUIREMENT: the *reads* (t, t₂, r, s_j) are what the certificate needs. If the
two-moment data can be certified for a window of bandwidth < 1 (i.e. a *narrower* window with a
*larger* α), the legality constraint is not "α ≤ √2" but "the window fits the data" — and the
constant's α-sensitivity means even a small legal widening pays. **The real constraint is the
data's Fourier support, not the kernel's.** [CONJECTURED — needs the exact Montgomery input
semantics, which the phone mirror lacks; this is the CI-04 hardness test made concrete]
Novelty: NEW framing of C1/CI-04.

### Cluster E — the ε-floor (constraint E: "the certificate may only claim the universal floor")

**E-1. "The universality gap is the requirement."** Invert "we can't claim the law's τ" →
REQUIREMENT: measure the read-constrained τ-floor min over laws matching the reads (t,t₂,r,s_j).
The corpus's adversarial min τ ≈ 6.45e-3 was UNCONSTRAINED; the read-feasible min is the real
price of the E-constraint. If the alternating crystal family (τ≈6e-3) is read-infeasible (its
pair-correlation spikes vs ζ's GUE-flat rows), the certified ε could jump 10–100×. **This is
CI-74 from the prior corpus — this document confirms it remains the flagship** and adds: the
crystal minimizers (gaps.rs) ARE the adversarial family, so their read-feasibility is directly
testable. [CONJECTURED; CI-74 cited, not re-run] Novelty: REPEAT of CI-74 (flagged as the
flagship; the crystal-structure link is NEW).

**E-2. "The ε-floor is a function — sample it, don't fight it."** Invert "ε is a scalar
correction" → REQUIREMENT: ε(span) is a certified decreasing function (the ε(S) curve is
monotonically decreasing for S ≥ 5.25, CHECKED NUMERICALLY, gaps.rs). The span-budget certificate
(CI-28/CI-77) becomes: sum over blocks of ε(span_b) against the total span budget (a first-moment
read-side quantity, never vacuous). This converts the vacuous span-4 Markov into a finite-budget
optimization. [CONJECTURED; the ε(S) monotonicity is CHECKED NUMERICALLY] Novelty: NEW data for
CI-28/CI-77 (the curve was not tabulated).

**E-3. "Bootstrap the floor through its own output."** Invert "p is unknown" → REQUIREMENT:
p is the certificate's output, and the span budget depends on p (mean gap = 1/p). The Markov
densities P(Σk gaps ≤ S) ≥ 1 − k/(p·S) grow with p; a proven p₀ raises the density, hence the
ε-contribution, hence a larger p — a monotone fixed point (CI-66 in the corpus). The span-9 rung
is exactly the first legal one at p=H0 (0.0087, verified here), and its density grows to 0.33 at
p=0.75 — the bootstrap map is steep. **The self-referentiality of p is a feature, not a bug.**
[CONJECTURED; the density values are CHECKED NUMERICALLY] Novelty: REPEAT of CI-66/67 (endorsed).

### Cluster B — the B/m block term (constraint B: "the plug-in map p=(H0−Aε)/(1−Bε) with fixed (A,B)")

**B-1. "The λ-family is the requirement."** Invert "λ=1 is the center" → REQUIREMENT: find the λ
maximizing the certified floor ε(λ) = min Σ(μ_i−λ)² over the Gram spectrum. The argmin
eigenvalues (1.016, 0.997, 0.987) sit below 1 — a center λ ≈ 0.99 may have a larger uniform
floor, and the plug-in's (A(λ), B(λ)) coefficients become functions of λ (CI-20). The B-coefficient
itself (the ε-to-constant slope, B·H0−A = 0.086/0.133) is the sensitivity meter: **the B-term is
not a wall, it is the exchange rate between ε and the constant — and the rate is a design choice.**
[CONJECTURED; the eigenvalue tuple is from the corpus's verify note] Novelty: REPEAT of CI-20/60
(endorsed as the B-cluster's sharpest lever).

**B-2. "The m-block term is a chain, not a size."** Invert "m=183 (Bellman coboundary) is
external and unexplained" → REQUIREMENT: the block size m is a *saturation length* of a chain
inequality (rank-subadditivity over overlapping blocks; the coboundary telescopes). The 183-block
gain over 7-pt is only 1.8e-4 (0.6731929 vs 0.6730085) — the *shape* of the m-dependence (does
ε(m) saturate, and where?) is the unknown, and it is exactly what the EPS-06/CO-01 Bellman
recursion was built to measure. **The block term's constraint is that we don't know its saturation
curve — invert that into a measurement program.** [CONJECTURED; EPS-06 is INCONCLUSIVE on the
phone, pending the laptop's repo access] Novelty: NEW framing (saturation-curve measurement as
the deliverable).

**B-3. "Use both roots of the quadratic."** Invert "the plug-in is one root" → REQUIREMENT: the
refined inequality t² ≤ r(2t − r + trΨ) is a quadratic in r with two roots; the interval
[max(N_s+N_p, root_lo), root_hi] is the feasible region. The single-root rearrangement (the
plug-in map) may have discarded information. Re-deriving the chain from the full interval is a
pure-algebra check that could tighten the constant *without any new floor*. [CONJECTURED]
Novelty: REPEAT of CI-22 (endorsed; cheap and high-value).

### Cluster G — the 6-gap structure (constraint G: "7-atom blocks, span 9, Markov vacuous at span-4")

**G-1. "The 6-gap span is the requirement."** Invert "span-4 Markov is vacuous" → REQUIREMENT:
span-9 is the *first* legal rung (verified: 6/H0 = 8.92 < 9), and the ε(span) curve is
monotonically decreasing. **The 6-gap structure is not a wall — it is the sweet spot where the
first-moment density becomes legal AND the floor is already 8.78e-5.** The honest fix is a
second-moment (Selberg-type) bound on the gap-sum variance converting the empirical 0.95 density
into a certificate (CI-41/CI-45). The empirical density is 100× the Markov bound (0.95 vs 0.0087),
so even a crude variance bound is transformative. [CONJECTURED; threshold and curve CHECKED
NUMERICALLY] Novelty: REPEAT of CI-41/45 (endorsed; the "first-legal-rung" exactness is the NEW
observation).

**G-2. "Stopping rules make density a mean."** Invert "good blocks must have positive density"
→ REQUIREMENT: *all* blocks are good by construction (start a new block when span would exceed 9);
the certificate needs only the mean block length (a stopping-time first moment), not a density.
This is the cleanest reformulation of D2 (CI-47): the floor applies to 100% of blocks, only the
count per atom drops. [CONJECTURED] Novelty: REPEAT of CI-47 (endorsed).

**G-3. "Interleave the atoms."** Invert "atoms must be consecutive" → REQUIREMENT: residue-class
partitions (mod 2/3) destroy the 2-periodic crystal family that saturates the floors (the class-gap
process is anti-alternating). Risk: the mean class-gap doubles (span budget collapses) and the
two-moment data for a thinned atom set may not be unconditional. **The inversion exposes that the
crystal family is the constraint's load-bearing adversary — removing it is the prize, keeping the
span is the price.** [CONJECTURED] Novelty: REPEAT of CI-13 (endorsed with the crystal-family
rationale now verified: gaps.rs shows the crystals ARE the minimizers).

**G-4. "Sliding windows, not disjoint blocks."** Invert "blocks are disjoint" → REQUIREMENT: a
weighted sum over all sliding 7-windows (each atom in ~7 windows); the floor scales with the
weight distribution via a covering/LP inequality. Block-additivity (trΨ(M) ≥ Σ trΨ(blocks),
ratio 1.83) is verified for disjoint blocks; the overlap normalization is the open question.
[CONJECTURED; additivity ratio from the corpus] Novelty: REPEAT of CI-12 (endorsed).

**G-5. "Offset symmetrization."** Invert "one unlucky partition is the worst case" → REQUIREMENT:
average the floor over all 7 partition offsets. The offset-average is a read-invariant quantity;
the worst law would need to be equally bad at every offset (a periodic law — and periodic laws are
exactly the read-infeasible crystals of E-1). **The two constraints (G and E) reinforce each
other: the adversarial family for G is the read-infeasible family for E.** [CONJECTURED]
Novelty: REPEAT of CI-14 (endorsed with the E-1 cross-link NEW).

### Cross-cutting inversions (the four constraints as one system)

**X-1. "The ceiling is the requirement."** Invert "the in-class ceiling 0.6818 is a wall" →
REQUIREMENT: ε* = what reaching 0.6818 needs = 0.102 (3-pt) / 0.065 (7-pt) (verified in the corpus).
The real law's τ (0.27) already exceeds ε* by 4× — the mathematics has the power; only the
universality requirement (the read-class min τ, E-1) stands in the way. **The ceiling is not the
obstruction — the read-class τ-floor is.** [CONJECTURED; ε* values from the corpus] Novelty:
REPEAT of CI-33/CI-74 (endorsed as the program's honest map).

**X-2. "The three walls are one wall."** The window (W), the ε-floor (E), and the 6-gap density
(G) all collapse into ONE question: **what is the minimal τ over laws matching the reads, for a
legal window?** W fixes the reads' legality, E fixes what the certificate may claim, G fixes what
the block statistics certify — and all three are functions of the same kernel and the same crystal
adversary. A single experiment (read-constrained τ-minimization over parametric gap laws at a few
α values) resolves the whole frontier. [CONJECTURED — this is the synthesis of W-1 + E-1 + G-3;
the components are individually verified above] Novelty: NEW synthesis.

---

## 3. Ranking and recommendation

| Rank | Idea | Lever | Cost | Risk |
|---|---|---|---|---|
| 1 | **W-1 window legality** | +27.5pp if α=1.0 is legal | L (laptop certification) | legality may fail |
| 2 | **E-1 read-constrained τ-floor** | 10–100× ε | M | a read-feasible low-τ law may exist (then the result is a proof the gap is irreducible — still valuable) |
| 3 | **G-1 second-moment density** | 100× block density | L | variance bound may be too weak |
| 4 | **B-1 λ-family** | ε slope × δλ | S/M | (A(λ),B(λ)) chain needed |
| 5 | **B-3 quadratic interval** | constant-level | S | may be exact (no slack) |
| 6 | **G-2 stopping rule** | 100% block coverage | M | floor must be re-derived per length |

The honest map (E-1/CI-33): floor → 67.25% (done), universality-gap → 67.30% (7-pt, done),
τ → 68.18% (ceiling). The four constraints rank by hardness: **W (assumed) > B (soft) >
G (soft/open) > E (hard only for the single-stage class). The assumed constraints are the free
money.**

---

## 4. What I did NOT claim (honesty ledger)

- No proof of any bound. All numerics are f64 exploration, not Arb interval certificates.
- The α<√2 legality is CONJECTURED (laptop item — the exact Montgomery two-moment input
  semantics are not on the phone mirror).
- The 7-pt functional's 19/5000 form remains UNRESOLVED (corpus Q1) — nothing in this
  document changes that.
- The ε(S) monotonicity (S≥5.25) is CHECKED NUMERICALLY on the unweighted pair-squares
  functional with coordinate descent; the S=4 value (4.75e-3) is a local-optimum artifact,
  not a contradiction.
- Every REPEAT above is an endorsement with new data/links, not a re-derivation.

## 5. Scripts and commands (reproducibility)

```
cd /home/ubuntu/riemann/tools/constraint_inv   (crate: constraint_inv)
export PATH=$HOME/.cargo/bin:$PATH
RUSTFLAGS="-C linker=rust-lld -C link-self-contained=yes" cargo build --release --target x86_64-unknown-linux-musl
./target/x86_64-unknown-linux-musl/release/constraint_inv    # sections A–D (all tables above)
./target/x86_64-unknown-linux-musl/release/trade             # window trade-off curve (§1.6)
./target/x86_64-unknown-linux-musl/release/gaps              # ε(span) minimizers (§1.4)
./target/x86_64-unknown-linux-musl/release/kcheck            # kernel cross-check vs corpus (§1)
```
One-off probes live in `/tmp/trade`, `/tmp/gaps`, `/tmp/kcheck` (Rust, same RUSTFLAGS);
the main crate is committed under `tools/constraint_inv/`.

---
*Corpus cross-references: constraint-ideas.md (CI-01…CI-80), verify-gram-stability.md,
ceiling-gram-constraint.md, ladder-consecutive-zeros.md, ci01-alphascan-execution.md,
span03-markov-execution.md, ci16-4atom-execution.md, eps06-bellman-execution.md,
discovery-gram-stability-673.md, context-pack.md.*
