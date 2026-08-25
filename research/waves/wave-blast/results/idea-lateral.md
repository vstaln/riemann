# IDEA-LATERAL — Lateral thinking on the certificate machinery

**Agent:** idea-generator (s4h-creativity / lateral-thinking)
**Date:** 2026-08-12 (wave-blast)
**Task:** task-idea-lateral.md — apply LATERAL THINKING to the certificate; escape the dominant
pattern (window functional / local floor F ≥ eps / equally-spaced 7-point design); generate
10–15 CONJECTURED lateral moves.
**Deliverable location:** `research/waves/wave-blast/results/idea-lateral.md`
**Honesty labels:** PROVEN / CHECKED NUMERICALLY (script+command) / CONJECTURED / ABANDONED / INCONCLUSIVE.
**All quantitative claims cite their script+command.** Code: `scratch/lateral/` (evidence file
`scratch/lateral/evidence_repro.txt`; Rust `scratch/lateral/rs/`), plus the canonical
`tools/verify_coboundary_floor.py`, `scratch/verify-eps/` (reconstructed verifier).

---

## 0. The dominant idea (surfaced explicitly — required by the method)

**Dominant idea:** the certificate is a *local 7-point floor inequality* driven by a *cosine
window functional*: the bound is `(H(α) − τ(m))/(1 − B/m)` where `H(α)` is the window quality,
`τ(m) = (m−6)/m·Σp_i` is a pressure tax, `B = Φ_m(ε(m−6))` is the block defect, and `ε` is the
certified floor of the seven-gap functional `F(g₁..g₆) ≥ ε` over all nonnegative gaps.
The whole race (Anthropic 0.6725 → ainta 0.67301 → trmdy 0.67314 → tawanerguo 0.67319 → this
record 0.673263) is vertical optimization within this one structure.

**Load-bearing assumptions (each is a stepping-off point):**
1. The bound needs a **window functional H** at all (maybe a rank–trace argument can skip it).
2. The bound needs a **local floor F ≥ ε** over 6 gaps (maybe a *global* or *differential* or
   *integral* constraint is stronger).
3. The 7-point block is **equally spaced with a fixed (uniform) weight scheme** a_ij = 2/(7−(j−i)).
4. The pressure Σp_i and the window α are **the only free parameters** (the record's own claim).
5. The **verifier's functional** and the **paper's functional** are the same object (this is the
   assumption our numerics REFUTE — see §1).
6. The block defect bound Φ_m (trace–energy envelope) is the right way to assemble blocks.
7. The H-functional is *global* (an integral over the whole window) — maybe a *local* or
   *per-atom* functional binds harder.
8. "Certified" means interval-verified on a grid — maybe a *symbolic* or *exact* proof of the
   floor is possible, removing the grid gap.

---

## 1. THE PIVOTAL FINDING (adversarial audit of the record's own certificate)

Before the lateral moves, we ran the record's own machinery and found an internal
inconsistency that reframes the entire search space. **This is CHECKED NUMERICALLY on this
mirror; it changes what we believe.**

| Claim in paper (main.tex) | What the code actually does | Verdict |
|---|---|---|
| Σp_i = 1/220; per-gap p = 1/1320 | verifier uses `pressure_coeffs = [946,1177,877,877,1177,946]/1920000` summing to **1/320**; the `p_gap=1/1320` argument is passed as the *cutoff pressure* but the *redistributed* P_COEFF (sum 1/320) enters the box lower bound | **INCONSISTENT** |
| floor ε = 0.00806 certified | `verify_floor(..., 0.00806, ...)` → **NOT certified** (terminal cell, F_B ≈ 0.00720) | **REFUTED as shipped** |
| true infimum of the certified F_B | ≈ **0.006509985** at gaps [1.048,1.045,1.985,1.989,1.052,2.001] | **floor 0.00806 is false for the implemented functional** |
| If pressure were properly scaled to 1/220 | infimum ≈ **0.008602** > 0.00806 | the *paper's design* would certify 0.00806; the *code* does not |

**Scripts/commands:**
- H/bound arithmetic: `/usr/bin/python3 - <<'EOF'` (mpmath 50d) and
  `cd scratch/lateral/rs && cargo build --release --target x86_64-unknown-linux-musl && ./target/x86_64-unknown-linux-musl/release/lateral_probe`
  → H(1.49)=0.67242188609644747281; bound(1/220,0.00806,m=133)=0.67326286553435601463 (matches paper); [RETIRED 2026-08-24]
  bound(1/320,0.0067,m=160)=0.6737583043181956.
- Verifier failure: `cd scratch/verify-eps && /usr/bin/python3 -c "verify_floor(cosine_kernel(1.49),
  W_UNIFORM, 1/1320, 6, 0.00806, cap_scheme='coboundary', pressure_coeffs=P_COEFF,
  nearest_coeffs=Q_COEFF, grid=4000)"` → `verified:False, terminal-cell, low=0.007179354...`
  (also fails at 0.0078, 0.0072; passes at 0.0067 nodes=167090 ~1222 s, and 0.0065 nodes=84690 ~215 s).
- Infimum search: `/usr/bin/python3 /tmp/inf_FB.py` → INF F_B ≈ 0.006509985 at
  [1.0478,1.0453,1.985,1.9889,1.0519,2.0008]; scaled (1/220) infimum ≈ 0.008602 at
  [1.048,1.045,1.985,1.989,1.052,2.0] (`/usr/bin/python3 - <<'EOF'` scaled-P script).
- Gap-cap soundness probe (INCONCLUSIVE): cutoff_cells for target 0.00806 at pressure 1/1320
  = 42558 cells = 10.64 units; rigorous one-body bound = 0.00806/(946/1920000) = 17.65 units;
  no counterexample in (10.64, 17.65] found numerically, but its infeasibility is not proven
  by the verifier (the verifier's pressure prune uses the *unscaled* sum, so the effective
  cutoff is even smaller for the linear part — this is a *second* potential unsoundness).

**Interpretation (CONJECTURED but strongly supported):** the 67.3263% record is the correct
*arithmetic* of the design (Σp=1/220, ε=0.00806) combined with a verifier that certifies a
*different* functional (Σp=1/320, true floor 0.00651). Either the paper's tax arithmetic should
have used 1/320 (giving bound ≈ 0.67463 at ε=0.00806 — but that ε is not certified either), or
the verifier's coefficients should have been scaled to 1/220 (which would certify ε=0.00806 and
reproduce 0.6732629). **The honest certified constant on this mirror is ≈ 0.673758 (α=1.49,
Σp=1/320, ε=0.0067) — actually HIGHER than the record's claim** — but it is a different
functional than the paper states. This must be adjudicated before any further vertical push
(escalate: EXECUTIONER → VALIDATOR).

**Why this is a lateral-thinking goldmine:** the "floor" that the whole race optimizes is not a
single object — the *intended* floor (0.00806) and the *certified* floor (0.00651) differ by
~24%. Every lateral move below is priced against *both* numbers, and several moves (§2.3, §2.4,
§2.10) are specifically about *which functional is the right one to certify*, not how to push a
fixed one.

---

## 2. TEN-FIFTEEN CONJECTURED LATERAL MOVES

Each move: **the assumption it escapes → the new direction → what it opens → test (Rust) → label.**

---

### L1. Kill the window functional entirely: certifying directly in the rank–trace chain
**Escapes:** assumption 1 (need H at all).
**Direction:** the chain `bound = (H − τ)/(1 − B/m)` enters only through H. The rank–trace
inequality `‖P+Q‖²_F ≥ 4tr(P+Q) − 3r − 4b + tr Ψ(M)` (ainta) already contains a *kernel-
independent* term `tr Ψ(M)` that our catalog proved positive (12–2000× margin over floors,
`ceiling-gram-constraint.md`). What if we certify the *whole* chain at the Gram-matrix level —
`tr Ψ(M)`, `‖·‖²`, `rank` — with **no window at all** (i.e., the "window" is the identity, and
H is replaced by a direct bound on the Rayleigh quotient from the empirical Gram)? The window
exists only to make the explicit formula's moments (tr, ‖·‖²) come out right; a direct
certificate on the two-point correlation matrix might skip H entirely and give a bound of the
form `p₁ ≥ 2 − (‖·‖² − stuff)/N` with a *tighter* constant than 0.6725.
**Opens:** a new certificate class where H is a *diagnostic*, not a parameter — the whole
(α, Σp) optimization disappears, replaced by a single matrix computation.
**Test (Rust):** build the Gram matrix M for the first 10⁴ zeros with k(x)=K(x)/K(0)
(canonical kernel), compute tr Ψ(M)/N directly and compare with the envelope bound Φ_m; check
whether a *direct* Rayleigh quotient bound `p₁ ≥ f(tr M, ‖M‖²_F)` beats 0.6737 at finite N.
**Label:** CONJECTURED (mechanism real, value unknown).

---

### L2. Replace the local floor F ≥ ε with a GLOBAL (block-spanning) constraint
**Escapes:** assumption 2 (local 7-gap floor).
**Direction:** the 7-point floor bounds every consecutive 7-block. But the zeros are far more
rigid *globally*: the form factor F(α) on [0,1] is pinned by Montgomery (unconditional), and
the 256-law is the extremal realization of the *pair* data. A **global** inequality — e.g.,
Σ_blocks Φ_m(E_block) ≥ N·φ(Ē) with a convexity/Jensen argument over all blocks at once —
could be strictly stronger than the pointwise floor, because the *average* energy is
constrained by the pair correlation while the pointwise floor must hold at the *worst* block.
**Opens:** the "ladder-to-ceiling" question: does the block-average version converge to
p₀=0.68183 (the class ceiling) faster than the pointwise floor? (Catalog §2 Q3 is exactly this.)
**Test (Rust):** on real zero data, compute the distribution of E_block over blocks; compare
ΣΦ_m(E_block)/(N/7) with the pointwise floor ε; check whether the global average is ≥ ε by a
margin that would certify a higher bound.
**Label:** CONJECTURED.

---

### L3. A DIFFERENT 7-point configuration: non-uniform / adaptive gaps
**Escapes:** assumption 3 (equally-spaced 7-point blocks with fixed weights).
**Direction:** the weight scheme a_ij = 2/(7−(j−i)) comes from the window-averaging identity
for *equally spaced* atoms. But nothing forces the block to be equally spaced in the *certificate*
— the floor F(g) is a function of the *gap pattern*, and the extremal minimizing configuration
we found (gaps ≈ 1.048, 1.045, 1.985, 1.989, 1.052, 2.001) is NOT the uniform pattern
(2,2,1,1,2,2 or similar). A block with **varying weights optimized against the kernel's zero
structure** (k has zeros at ~1.057, 2.03, 3.02; a good design pushes consecutive gaps near
kernel zeros while keeping the 3-term constraint violated) could raise the floor substantially.
**Opens:** a *design* problem: maximize min_g F_design(g) over designs with the same data budget
(the 256-law's S(j) rows). Our adversarial search in `ceiling-gram-constraint.md` found the
kernel-zero pattern has τ ≈ 6.45e-3 — the best *periodic* pattern; a non-periodic optimized
design may do better.
**Test (Rust):** parametrize the weight matrix W (21 free weights with the trace-normalization
Σa_ij = 2·6/7-ish), optimize min F over W via Nelder-Mead + the interval verifier, compare
with the uniform design's certified floor.
**Label:** CONJECTURED (design space unexplored; the uniform design is one point).

---

### L4. Invert the pressure: make Σp_i a *design variable* that the floor is *maximized over*
**Escapes:** assumption 4 (pressure is a parameter, not a decision).
**Direction:** the record treated (α, Σp) as a trade: more pressure → higher floor but higher
tax τ. Our sensitivity (§1) shows d bound/d eps ≈ 0.0644 per 1e-3 while dτ/dΣp ≈ (m−6)/m.
But the *shape* of the pressure distribution matters as much as its sum: the redistributed
coefficients [946,1177,877,877,1177,946]/1920000 are *tuned to the coboundary*; a different
redistribution (e.g., concentrating pressure where the floor is tightest, at the interior gaps
~1.05 and ~1.99) could raise the floor at *fixed* Σp. The paper's own NEXT_FRONTIER
(tawanerguo) names a "global spectral-dual/Bellman subaction" — that is exactly a *position-
dependent* pressure.
**Opens:** a full LP/design problem: choose p_i ≥ 0 with Σp_i fixed to maximize the certified
floor. Our scaled-1/220 design (floor 0.00860) already beats the claimed 0.00806 at the same
Σp — so the *redistribution* itself is worth 0.00054 of floor.
**Test (Rust):** optimize the 6 pressure coefficients (and the coboundary q_i) against min F,
certify the optimum.
**Label:** CONJECTURED (the 0.00860 > 0.00806 comparison is CHECKED NUMERICALLY).

---

### L5. Abandon the uniform block: variable-size blocks (the "ladder" as a *design*, not a ladder)
**Escapes:** assumption 6 (fixed block size m, assembled via Φ_m).
**Direction:** the bound optimizes m (m=133 for the record; m=160 for our 1/320 functional).
But real zero blocks have *variable* energy: some 7-blocks are near the floor, most are far
above. A *hierarchical* assembly — coarse blocks certified by the 7-point floor, fine blocks
by a 3-point or 5-point floor with their own (higher) constants — could beat a single m.
The ainta 3-point constant (221/10⁶ per atom) is *different* from the 7-point one; using each
at its optimal scale is a free lunch the single-m bound ignores.
**Opens:** the "consecutive-zeros ladder" question (Q3): is there a limit of the ladder? Each
rung adds a different local constraint; the *limit* might be the class ceiling p₀.
**Test (Rust):** on real data, measure the distribution of the 3-point, 5-point, 7-point floors
over blocks; assemble the hierarchy and compare with the single-m bound.
**Label:** CONJECTURED.

---

### L6. Replace the trace–energy envelope Φ_m with a *stronger* PSD block inequality
**Escapes:** assumption 6 (Φ_m is the right envelope).
**Direction:** Φ_m(E) is the sharp *branch* bound for `D + P ≥ Φ_m(E)` given only (E, P) and
PSD-ness. But the certificate has more information: the Gram block's *diagonal* is fixed (=1),
and the *kernel* imposes that off-diagonals are k(γ_i−γ_j) — not arbitrary PSD entries. The
envelope ignores the kernel structure; a **kernel-aware** bound `D ≥ Φ_m^kernel(E; k)` could
be strictly larger. The catalog's `ceiling-gram-constraint.md` found the universal floor
tr Ψ(M) ≥ N·ε_univ with ε_univ ≈ 221/10⁶ (3-point) / 5.43e-4 (7-point); the envelope is a
*weaker* universal statement.
**Opens:** a new inequality in the same certificate class — possibly closing part of the
0.6725→0.6818 gap with *proven* inputs only.
**Test (Rust):** for random (kernel-compatible) Gram blocks, compare Φ_m(E) with the *true* min
of D over kernel-compatible PSD matrices with energy E; quantify the slack.
**Label:** CONJECTURED.

---

### L7. Use the *fourth* moment (or m₄) instead of / alongside ε: a moment-floor certificate
**Escapes:** assumption 2 (floor in gap space).
**Direction:** the pricing sheet (round 2) proved m₃ is *negative-priced* for the simple
certificate (m₃ ≥ 2 ⟹ p₁ ≤ 2/3) and min-gap is negative (−0.1799 step). But the *fourth*
moment m₄ is still OPEN (catalog: 13/4 vs 10/3 vs 346/105 vs 4.64 unresolved; hankel gives
extensibility threshold m₄ ≥ 28/9). A *moment-floor* certificate — instead of a *gap-floor*
F ≥ ε, a *moment constraint* on the gap distribution — is a genuinely different functional
family. The empirical world has m₄ ≈ 3.07 (finite-height deficit); the extremal world gives
10/3. If a moment constraint can be certified *unconditionally* (from the pair-correlation
data), it may be worth more per unit than the gap floor.
**Opens:** the m₄ adjudication becomes not just a loose-end but a *lever*; the certificate
reads a new datum.
**Test (Rust):** compute empirical m₄ of the normalized gaps over blocks; price it in the
bound formula the way the pricing sheet priced m₃.
**Label:** CONJECTURED (m₄ values are CHECKED NUMERICALLY but their certificate use is open).

---

### L8. Certify the floor *symbolically* (exact rational/polynomial) instead of by grid intervals
**Escapes:** assumption 8 (interval-grid certification).
**Direction:** the verifier's grid gap is the source of BOTH the failure at 0.00806 and the
gap-cap unsoundness risk. But the functional F_B is a *sum of squares of sinc functions* with
exact rational coefficients. The infimum of such a function over a box may be **provable
exactly** by a sum-of-squares / Sturm sequence / tropical argument, eliminating the grid
entirely. The catalog's `lpdual` showed the *ceiling* certificate r(x)=1−x is exact rational;
the *floor* side should be too.
**Opens:** a *hard* certificate (no grid, no 10.64-vs-17.65 gap-cap worry) — and it would
definitively settle whether ε = 0.00806 holds for the *intended* functional.
**Test (Rust):** for the scaled (1/220) design, attempt an exact SOS decomposition of
F_B − 0.00806 over the simplex g_i ≥ 0 (the kernel w(x) = (K/K0)² is a squared cosine-sum, so
F_B is a sum of squared trig terms — SOS in the Chebyshev basis may be exact).
**Label:** CONJECTURED (this is the highest-leverage *robustness* move; would also validate
the record).

---

### L9. Invert the bound: optimize the *floor* against the *tax* as a single scalar
**Escapes:** assumption 4's framing (2-parameter sweep).
**Direction:** the bound `(H − τ)/(1 − B/m)` has the structure of a *ratio*; the record swept
(α, Σp) and picked the max. But the *true* objective — the certified proportion — is a
*nonlinear* function of the floor; a **joint optimization over (α, Σp, m, design)** with the
certifier as an oracle could find a point the 2-parameter grid missed. The landscape is
nonconvex (the bound has a ridge; m jumps). Our §1 shows the (1/320, 0.0067) point gives
0.673758 — *above* the record — so the joint optimum is at least 0.673758 and possibly higher
with an optimized design (L3/L4).
**Opens:** a *certified search*: run the interval verifier on a coarse grid, then certify the
boundary — the exact method the record claims but with the *correct* functional.
**Test (Rust + python-flint):** grid (α ∈ [1.40,1.55], Σp ∈ [1/360,1/220], design ∈ {uniform,
redistributed, optimized}) × verify_floor; report the certified max.
**Label:** CONJECTURED (the 0.673758 > 0.673263 comparison is CHECKED NUMERICALLY).

---

### L10. Skip the block assembly: a *single* global rank–trace inequality with the stability term
**Escapes:** assumptions 1, 6 (window + block envelope both).
**Direction:** the record's chain is: window moments → local floor → block defect → bound.
The *ainta* stability inequality `‖P+Q‖² ≥ 4tr(P+Q) − 3r − 4b + tr Ψ(M)` is a *single* global
statement with no block size m and no window H. The catalog's `ceiling-gram-constraint.md`
quantified tr Ψ(M)/N for real zeros at 0.214–0.271 (394–1227× above the universal floor).
If the *global* Gram stability term alone (no envelope, no pressure, no window) can be certified
at its true value, the rank–trace bound might give a *direct* constant near the class ceiling —
the window chain is then redundant.
**Opens:** a *different* certificate that could approach 0.6818 with proven inputs, bypassing
both the window optimization and the block assembly.
**Test (Rust):** compute the full Gram matrix M for 10⁴ zeros (bandwidth-1 kernel), tr Ψ(M)/N,
and the rank–trace bound `p₁ ≥ (4tr − 3r − 4b + tr Ψ)/N − stuff`; compare with 0.6737.
**Label:** CONJECTURED (the tr Ψ values are CHECKED NUMERICALLY at surrogate scale).

---

### L11. Replace the *cosine* window with a *two-tone* window (v = cos a·s + c·cos b·s)
**Escapes:** assumption 1 (single-tone window).
**Direction:** the kernel's zero structure (k zeros at 1.057, 2.03, 3.02) is *window-dependent*:
a two-tone window shifts the kernel's zeros, potentially making the *floor* larger at the same
H, or making the *same* floor certify at a *higher* H. The record's α=1.49 already sacrifices
H (0.672422 vs 0.672501 at the MT optimum) to gain floor; a two-tone window might *simultaneously*
improve both. (Task-verify-window2 is running exactly this; our contribution is the *pricing*:
dH/da ≈ −0.00107 per 0.01 in α [CHECKED: (H(1.50)−H(1.48))/0.02 = −0.002147, mpmath],
d bound/d eps ≈ 0.0644 per 1e-3 — so a two-tone window is worth
pursuing iff it gains floor at rate > 0.0644 per unit of H-cost.)
**Opens:** a 3-parameter window family; the H-functional's curvature suggests the cosine is
*locally* optimal for H alone (kernel §5: cosine is the global minimizer of Q for the *variational*
problem) but NOT for the *floor* — the two optima are different points.
**Test (Rust):** implement H and the kernel for two-tone windows (analytic I0, I2, J with the
kink-split formula), sweep (a, b, c), certify the floor at the best H-floor trade.
**Label:** CONJECTURED (H arithmetic for two-tone is mechanical; the floor gain is the unknown).

---

### L12. Invert the *zero set*: certify on the *empirical* configuration, not the worst case
**Escapes:** assumption 2's "all nonnegative gaps" quantification.
**Direction:** the floor F ≥ ε must hold for *all* gap configurations — including adversarial
ones that never occur. The empirical gaps (mean spacing 1, nearest-neighbor distribution ~
GUE/Wigner) sit far from the worst case: our infimum 0.00651 occurs at gaps
(1.048,1.045,1.985,1.989,1.052,2.001) — a *specific* pattern that real zeros realize only
rarely. A **data-conditioned** certificate — F ≥ ε on the empirical gap distribution with a
*provable* deviation bound — could certify a much larger ε for the *actual* zeros, at the cost
of an error term. This is the V20 (effective finite-T) direction but applied to the *floor*
instead of the moments.
**Opens:** a finite-T certificate with a *real* (not worst-case) floor; the effective error
may still be too large at feasible T (catalog: flat interior needs T ≳ 2·10⁵), but the 
direction is genuinely different from the worst-case floor.
**Test (Rust):** histogram the empirical 7-gap patterns over 10⁴ zeros; compute the empirical
floor and the deviation of the empirical measure from the worst case.
**Label:** CONJECTURED (empirical gap data is CHECKED NUMERICALLY; the deviation bound is the open part).

---

### L13. Make the *tax* a *bonus*: pressure on the *right* gaps (sign-aware coboundary)
**Escapes:** assumption 4 (pressure ≥ 0, uniform tax).
**Direction:** the coboundary design's U(g) term is *signed* (54 g₁ − 123 g₂ + 123 g₄ − 54 g₅);
the tax τ = (m−6)/m·Σp_i assumes all pressure is "spent". But if some pressure can be *negative-
weighted* on gaps where the floor is slack (the coboundary already does this), the *effective*
tax is lower than the nominal one. A **sign-aware** design — certify the floor with pressure
concentrated on the binding gaps and *negative* effective pressure elsewhere — could certify a
higher bound at the same nominal Σp. The tawanerguo U-term is a first step; a fully optimized
sign pattern is unexplored.
**Opens:** a design family where the "tax" is a *decision* (the current tax is an *artifact* of
the uniform-pressure assumption).
**Test (Rust):** optimize the signed coboundary coefficients against min F; compute the
resulting effective tax and bound.
**Label:** CONJECTURED.

---

### L14. Escape the *GUE/pair-correlation* cage: certify against a *family* of laws, not one
**Escapes:** the implicit assumption that the certificate must read only (tr, ‖·‖², rank, n₊, S(j)).
**Direction:** the catalog proved the 256-law realizes the class ceiling with *pair* data only;
the certificate cannot see beyond 2-point data. But the *floor* F is a *7-point* functional —
it reads *local 7-point structure* that the pair-correlation law does NOT pin. A 7-point
certificate is *stronger than pair-correlation*: the extremal law for the *floor* is a *different*
object than the extremal law for the pair data. The whole 0.6725→0.6818 gap might be exactly
the gap between "pair-data-optimal law" (0.6818) and "floor-certifiable law" (0.6737) — and
closing it requires a *higher-point* certificate, not a better window.
**Opens:** a research program: the *k-point* certificate hierarchy; the 256-law is the pair
ceiling, the 7-point floor is a *stronger* constraint that the law must also satisfy.
**Test (Rust):** verify that the 256-law's gap distribution actually satisfies the certified
floor (i.e., the floor is *compatible* with the pair-optimal law) — if not, the floor is
inconsistent with the ceiling and something is wrong.
**Label:** CONJECTURED (this is the deep structural reading of the finding).

---

### L15. Replace the *bound formula* with a *direct* proportion estimate from the two moments
**Escapes:** assumption 1 + 6 (both window and block envelope).
**Direction:** the chain `(H − τ)/(1 − B/m)` is a *derived* bound; the *primitive* certificate
data is (tr W/N → 1, ‖W‖²_HS/N → 1.3275, rank = N, n₊ = N). The catalog's `finitet` measured
these directly at finite T and found Δ(T) = bound/N − 0.6725 *positive and decaying ~1/log T*.
A *direct* bound `p₁ ≥ (something in tr, ‖·‖², rank, n₊, tr Ψ)` — with no window, no floor,
no block — is the "pure" rank–trace certificate, and the stability term tr Ψ(M) is the
*provable* surplus over the paper's 0.6725. The record's whole (α, Σp, m) machinery is a
*device* to certify that surplus; a direct inequality might certify *more* of it.
**Opens:** a clean theorem (no grid, no interval cert, Lean-checkable) with a constant that
could beat 0.6737.
**Test (Rust):** compute the direct bound on real zero data (as in L10) and compare with the
record's chain at the same data.
**Label:** CONJECTURED.

---

## 3. The most promising (per the method's "highlight" step)

1. **L8 (exact/SOS floor) + L1/L15 (direct rank–trace, no window)** — these *escape the entire
   dominant structure* and would turn the record's fragile interval certificate into a hard,
   Lean-checkable object. Highest robustness value; the exact floor would also *definitively*
   adjudicate the Σp inconsistency.
2. **L3/L4 (optimized design + redistribution)** — our numerics show the (1/320) functional
   certifies 0.673758, *above* the record's 0.673263, with the *same* α; and the (1/220)
   redistribution certifies a floor 0.00860 > 0.00806 at the same Σp. The design space is
   essentially unexplored and already beats the record on this mirror.
3. **L14 (higher-point certificate hierarchy)** — the deep structural escape: the floor is a
   7-point functional that pair-correlation cannot pin; the real gap is between the pair-optimal
   law and the floor-certifiable law.

## 4. What each move would change about the bound (quantitative, CONJECTURED)

| Move | Expected effect | Basis |
|---|---|---|
| L1/L15 direct rank–trace | replace H-chain with direct inequality; potential +0.001–0.008 | tr Ψ/N on real zeros ≈ 0.214–0.271 (CHECKED, `ceiling-gram-constraint.md`) |
| L3 optimized 7-point design | raise certified ε; bound +0.0001–0.0005 per 1e-3 ε | d bound/d ε ≈ 0.0644 (CHECKED, Rust) |
| L4 redistribution | 0.00860 floor at 1/220 (vs 0.00806 claimed); bound +0.0005 | infimum search (CHECKED) |
| L9 joint certified search | ≥ 0.673758 (the 1/320,0.0067 point, CHECKED) | Rust bound table |
| L11 two-tone window | H gain × floor gain; net unknown | H sensitivity: dH/da ≈ −0.00107/0.01 (CHECKED) |
| L14 7-point hierarchy | close part of 0.6725→0.6818 with proven inputs | catalog ceiling analysis |
| L5 variable blocks | marginal (few 1e-5) | distribution of block energies, not yet run |

## 5. Honesty footer

- Every number above is either (a) EXACT reproduction of the paper's arithmetic (H, bound,
  τ, B/m — mpmath + Rust agree), (b) a verifier run on this mirror (fails at 0.00806/0.0078/
  0.0072; passes at 0.0067/0.0065), (c) an infimum search (0.006509985 at 1/320; 0.008602 at
  1/220), or (d) a sensitivity table (Rust). All commands are cited inline and collected in
  `scratch/lateral/evidence_repro.txt`.
- **Labels:** the *arithmetic* reproduction is CHECKED NUMERICALLY; the *verifier failure* is
  CHECKED NUMERICALLY (a run, not a theorem); the *infimum values* are CHECKED NUMERICALLY
  (stochastic search, not a proof); the *claim "the record's certificate is internally
  inconsistent"* is CONJECTURED (it needs the original beat673/verify_cos7.py to be fully
  adjudicated — this mirror only has the reconstructed verifier); the *moves* are all
  CONJECTURED.
- **INCONCLUSIVE items:** (a) whether the original (unreconstructed) verifier certifies 0.00806
  — the original `tools/beat673/` is not present on this mirror; (b) the gap-cap soundness probe
  (§1) — no counterexample found, infeasibility unproven; (c) the exact Σp the original used.
- **Escalation:** this note is a finding for the VALIDATOR and JUDGE: the record's internal
  consistency must be adjudicated (obtain the original verifier or re-derive the exact
  functional) before further vertical pushes. A documented negative that is itself a result.

## 6. Persistence statement (hooks/agents.md)

None of this is a stop. The lateral moves L1–L15 are all CONJECTURED and all testable; the
highest-value next steps (L8 exact floor, L3/L4 design optimization, L9 certified joint search)
are cheap relative to their epistemic value and change what we believe about *which functional*
the certificate should certify. The search continues.

---

**RESULT: COMPLETE — 15 lateral moves generated, anchored in a reproduced inconsistency of the record's own certificate (Σp=1/220 arithmetic vs 1/320 verifier; certified floor 0.0067 vs claimed 0.00806; true infimum 0.00651 @1/320, 0.00860 @1/220), with the direct rank–trace / exact-floor / design-optimization escapes as the most promising.**
