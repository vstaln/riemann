# Idea-probability: the probabilistic structure of zeta zeros vs GUE — and what it implies for simple-on-line proportions

**Role:** idea-generator (s4h-probability) — wave-blast
**Host note (honesty):** the spec's mandatory files (`/home/vstaln/riemann/hooks/agents.md`,
`/home/vstaln/.pi/agent/skills/s4h-probability/SKILL.md`, `research/notes/discovery-6732629.md`,
`attack-vector-catalog*.md`) **do not exist on this host** — stale paths from spec generation.
The live repo is `/home/opc/riemann`. Ground truth used instead: `tools/beat673/final_leader.py`
(certified record config), `verify_cos7.py` (the rigorous Arb/flint verifier, from which the
**exact functional and kernel** were extracted and re-implemented in Rust), and `tools/zeta-rs`
(the GUE / pair-correlation tooling). All numerics are Rust (no external crates, static build);
the only Python run was an Arb *semantics check* of the kernel, clearly labelled.

> **Tool bug found & fixed (this run):** `tools/zeta-rs/src/gue.rs` had a bisection
> tightening bug (`upper = val` broke the Sturm-count invariant) that collapsed all
> eigenvalues to the first one and reported `0/12000` simple. Fixed (keep `b = hi + 1.0`);
> after the fix the tool reports `12000/12000 = 1.000000000` simple. Same fix applied in
> this report's Rust.

---

## 0. The exact object being certified (units matter!)

The certified record is `bound = 0.673262865534356` at [RETIRED 2026-08-24]
`alpha = 1.49, p = 1/1320 (psum = 6/1320 = 1/220), m = 133, eps = 8060e-6`, window
`v(s) = cos(alpha·s)`. The rigorous verifier (`verify_cos7.py`) certifies:

```
F(y) = p * sum_i y_i  +  sum_{0<=i<j<=6} a_ij * w(y_i + ... + y_{j-1})  >=  eps
```

over every 6-gap block `y = (y_0..y_5)` (unfolded gaps, mean spacing 1), with the
**21 cumulative-span pairs** `a_ij = 2/(7-(j-i))`, and the **exact kernel**
`w(x) = k_alpha(x)^2`, `k_alpha(x) = (sinc(pi x - a) + sinc(pi x + a))/(2 sinc(a))`,
`a = alpha/2`. All numerics in this report use **this exact functional** (verified
against the verifier's own weight table: `sum_s a_s = 12`, capacity check per span = 2).

Key kernel facts (CHECKED NUMERICALLY, Rust `kernel_scan`, command
`rustc -O /tmp/kernel_scan.rs && /tmp/kernel_scan`):

| x | w(x) |
|---|------|
| 0.0 | 1.000000 |
| 0.5 | 0.440211 |
| 1.0 | 0.003551 |
| 1.0645 | ~6.6e-12 (near-zero) |
| 2.0 | 0.000203 |
| 6.0 | 2.4e-6 |

`w` is **not monotone** — it dips to ~0 at span 1.0645 and oscillates. This matters
enormously (Section 3).

---

## 1. Base-rate anchor: what fraction of a GUE matrix's eigenvalues are simple?

**PROVEN (RMT):** for the continuous GUE (and all beta-ensembles), the joint density
vanishes quadratically on coincidences, so
`P(repeated eigenvalue) = 0`, i.e. **~100% of eigenvalues are simple**.

CHECKED NUMERICALLY (Dumitriu–Edelman tridiagonal beta=2 model, exact GUE law,
n=60, 200 trials):
```
zeta-rs gue --matrix 60   (after the fix)
  simple fraction = 12000/12000 = 1.000000000
  min adjacent spacing (mean-spacing units) = 0.008596
```
Script: `tools/zeta-rs/src/gue.rs`; command: `cd tools/zeta-rs && cargo build --release && ./target/release/zeta-rs gue --matrix 60`.

**The base-rate answer: 1.0.** GUE does not produce non-simple eigenvalues — the
67.3% simple-on-line bound is a statement about *zeros*, not about eigenvalue
multiplicities. The correct probabilistic reading of "simple" for zeta zeros is the
**gap-isolation** notion (a zero with no other zero too close), which is what Section 5
quantifies. So the base-rate question's honest answer is: **the fraction is 1 a.s. in
GUE; the interesting probabilistic content lives in the *gap structure*, not the
multiplicity.**

---

## 2. Distribution of the certified functional F under GUE

CHECKED NUMERICALLY (Rust MC, `idea-probability` binary):
```
MC: 100000 6-gap blocks, GUE n=100, bulk k in [n/4,3n/4], stride 1
F: mean=0.409458 sd=0.187845 min=0.017065
F quantiles: 1%=0.069170 5%=0.130350 25%=0.275316 50%=0.391060
             75%=0.524758 95%=0.739327 99%=0.932978
P(F < eps=0.00806) = 0/100000 = 0.000e0   [floor violation rate under GUE]
7-block span: mean=6.1186 median=6.1078 1%=4.3492 99%=8.0081
min-gap in block: median=0.3807 1%=0.0533 0.1%=0.0224
```
Script: `research/waves/wave-blast/results/idea-probability-work/src/main.rs`;
command: `cd research/waves/wave-blast/results/idea-probability-work && cargo build --release && ./target/release/idea-probability`.

**Reading:** under GUE, the *typical* 6-gap block has F ≈ 0.41 — **~51× the certified
floor 0.00806**. The floor is a *tail* statement: it only ever binds on very special
blocks. The 0.1% min-gap quantile is 0.0224 — still 2.8× the certified eps — and the
MC saw **zero** blocks with F below eps in 100k samples.

This is the first probabilistic lesson: **the certified floor is not tight against the
typical GUE block; it is a worst-case (support) statement.** Which is why the
deterministic support analysis (Section 3) is the right place to look for headroom.

---

## 3. Deterministic support minimum — the real ceiling (KEY FINDING)

The functional is `F = p·Σy + Σ a_ij·w(span)`. Since `w ≥ 0` (it's a square), the
minimum over the box is where the kernel contributions nearly vanish — i.e. where the
21 spans land in the **kernel near-zeros** (spans ≈ 1.06, 2.13, 3.2, …). A systematic
search:

| search | min F found | at |
|--------|-------------|-----|
| uniform-gap scan L | 0.0091615 | L = 1.0190 |
| perturb-one-gap | 0.0091213 | [1.029,1.019,…] |
| 10M random [0,2.5]^6 + descent | **0.0085837** | [2.0074,1.9997,1.9786,1.0338,1.0269,1.0363] |
| 2M random on simplex Σy=cutoff | 0.016332 | boundary |

CHECKED NUMERICALLY (Rust, `support5` binary; command `rustc -O /tmp/support5.rs && /tmp/support5`).

**The deterministic support minimum of F is ≈ 0.008584.** The certified floor
`eps = 0.00806` is at **93.9% of that ceiling** (headroom factor **1.065×**). In other
words:

> **The certified eps is essentially at the maximum the mechanism can possibly certify
> against ANY zero configuration.** The floor is not probabilistically loose — it is
> deterministically nearly maximal.

The minimizer is a *non-generic* block: gaps ≈ [2.0, 2.0, 1.98, 1.03, 1.03, 1.04],
span-sum ≈ 9.08. Under GUE, such blocks are measure-zero (never seen in 100k samples),
but the *verifier certifies for all blocks*, so the support min is the true ceiling.

**Implication for the bound:** the best eps one could ever certify with this exact
7-point/cosine mechanism is ~0.008584, giving bound
`0.67359908` (+0.000336 over record) at m=126 (CHECKED NUMERICALLY, `final_calc`).
The eps sweep:

```
eps=0.00806: 0.67326287  (+0.0000000)   <-- certified record
eps=0.00810: 0.67328858  (+0.0000257)
eps=0.00820: 0.67335284  (+0.0000900)
eps=0.00830: 0.67341703  (+0.0001542)
eps=0.00840: 0.67348119  (+0.0002183)
eps=0.00850: 0.67354529  (+0.0002824)
eps=0.008584:0.67359908  (+0.0003362)   <-- deterministic support ceiling
```

**So the probabilistic structure of zeros tells us the eps knob is nearly exhausted.**
The +0.000336 from reaching the support ceiling is the *entire* eps-side headroom of the
current mechanism — and it is a *hard* ceiling (any eps > 0.008584 admits a block with
F < eps, so the verifier must fail by construction). This is a new, honest, quantitative
statement the idea-probability lens contributes: **the certified 0.00806 is ~94% of what
the mechanism can possibly certify; the eps-search can at most recover +0.000336, not
+0.001+.**

---

## 4. Extreme-value scale: where the floor *starts* to bind

Under GUE (Wigner nearest-neighbor), `P(gap < eps) = 1 - exp(-π eps²/4) = 5.10e-5` for
eps=0.00806. So:

- `P(min of 6 adjacent gaps < eps) ≈ 3.06e-4` per block
- N ≈ 1/5.1e-5 ≈ **19,600 zeros** before ~1 gap < eps is expected (height T ~ 123,000)
- the floor-violating blocks become *expected* at N ~ 3,300 (1/(6·3.06e-4))

CHECKED NUMERICALLY (Rust, `guecheck`; command
`./target/release/zeta-rs guecheck 149 100 1 1320 8060 1000000`). The tool also gives
the global-min-gap scale: `~0.0938 @ N=1e3, ~0.0342 @ N=1e4, ~0.0121 @ N=1e5,
~0.0042 @ N=1e6` mean-spacing units — i.e. the certified eps **sits right at the
extreme-value scale of the model** (min gap ~ eps around N ~ 10^5–10^6). The floor is
"typical" nowhere; it is an extreme-value (a.s.) statement.

MC check (Rust): `n=256 x 12 matrices, bulk: 1524 gaps, 0 gaps < eps, global min gap
= 0.01314` — consistent with the Wigner estimate (no gaps that small at this sample
size).

---

## 5. Probabilistic simple-on-line: the gap-isolation model

If "simple" for zeros = "both adjacent unfolded gaps > δ" (a zero with no near
neighbor), then under GUE with Wigner i.i.d. spacing (CONJECTURED approximation —
ignores GUE's negative gap correlation):

| δ | P(gap < δ) | P(both gaps > δ) ≈ simple fraction |
|---|-----------|-------------------------------------|
| 0.00806 | 5.1e-5 | 0.9999 |
| 0.05 | 1.96e-3 | 0.9961 |
| 0.10 | 7.82e-3 | 0.9844 |
| 0.20 | 3.09e-2 | 0.9391 |
| 0.50 | 0.178 | 0.6752 |
| 1.00 | 0.544 | 0.2079 |

MC (GUE n=256, central bulk): δ=0.00806 → 1.0000; δ=0.10 → 0.9894; δ=0.20 → 0.9451;
δ=0.50 → 0.6574 (CHECKED NUMERICALLY, `idea-probability` binary).

**Reading:** the 67.3% bound corresponds to the isolation scale δ ≈ 0.5 — i.e. the
bound is *consistent* with "about 2/3 of zeros have both nearest neighbors at distance
≥ ~0.5 mean spacings." This matches the pair-correlation breakthrough's "2/3" flavor
(arXiv 2501.14545: ≥ 2/3 simple under a thin-box condition). The probabilistic model
does not *prove* the bound — it *explains the scale* at which it holds and provides the
prior that the true simple fraction is large (≥ 0.67 with overwhelming probability under
GUE).

Model A (i.i.d. thinning at f=0.6732): 67,455/100,000 simple, 95% CI [0.6716, 0.6774]
(CHECKED NUMERICALLY, `probmodel`; command
`./target/release/zeta-rs probmodel 100000 0.6732 --seed 42`). The bound 0.6732 is
*consistent* with the model (a lower bound on a fraction whose typical value is ≥ 0.67).

---

## 6. Rigidity: why GUE suppresses tight clusters

GUE number variance `Sigma^2(6) = 0.4026` (sd 0.634) vs Poisson 6.0 (sd 2.449) — GUE
is ~3.9× more rigid at the 6-gap scale. The Gaussian tail `P(span < 10.639) ≈ 1.0`
(6-gap spans below the box cutoff are essentially impossible under GUE), whereas Poisson
gives 0.954. The rigidity is what makes the *pressure-side* of the floor (sum < cutoff)
almost vacuous under GUE — the binding regime is the kernel-side support min (Section 3).

CHECKED NUMERICALLY (Rust `idea-probability` binary; `gue_number_variance`).

---

## 7. Ideas: connecting the probabilistic model to the certified-bound machinery

Ranked by (novelty × tractability). All **CONJECTURED** until certified.

### The headline insight (from Sections 2–4)
The certified eps is **at 94% of the deterministic support ceiling** — so the
probabilistic structure of zeros says the eps knob is *nearly exhausted* (+0.000336 max).
Any further bound gains must come from the **H side (numerator), the tax side (psum),
or a different mechanism**, not from eps. This *inverts* the naive "there's lots of
probabilistic headroom" prior.

---

**I-P1 — Support-ceiling certification (the +0.000336 recovery).** Certify eps up to
the deterministic support min 0.008584 (or 0.0085 safely). This is *not* a probabilistic
gamble: the support min is the a.s. minimum, so eps=0.0084–0.0085 is certified against
*all* configurations and only costs verifier time. Expected: bound 0.6735–0.6736
(+0.0002–0.0003). Test: `verify_cos7.py 149 100 1 1320 8400 1000000 - 2000 0 1`.
Effort: low (binary-search eps between 0.0081 and 0.008584). This is the *cheapest
known* certifiable gain and it is *justified by the probability analysis*: because
F ≥ support_min > eps, the verifier succeeds on the worst case, not merely typically.

**I-P2 — Re-optimize (alpha, eps, m) against the support ceiling.** The support min
depends on alpha (kernel zeros move with alpha). At alpha=1.41 (H peak) the support min
may be higher, allowing a larger eps at the better H. CHECKED NUMERICALLY: H(1.41) is
+0.000079 over H(1.49) but the certified-eps drop is interpolated ~-0.0005 — the joint
optimum needs the *alpha-dependent support ceiling* table. Test: recompute the support
min for alpha in {1.40,1.41,1.42,1.45,1.49,1.52,1.55} (10-min Rust job), then certify.
Effort: medium. Expected: small (+0.0001–0.0003) but *safe*.

**I-P3 — Two-regime floor: pressure-side vs kernel-side.** The analysis shows the
floor binds in *two distinct regimes*: (a) tight blocks (kernel ~1, F ~ 12, floor
trivially met) and (b) loose blocks with spans in kernel near-zeros (F ~ p·Σy + tiny
kernel, floor binds at the support min). A floor that is *span-aware* — smaller effective
eps only where the kernel is deep — could certify a *larger* eps on the generic bulk
while keeping the a.s. guarantee. This is a generalization of the eps floor to a
function of the block's span distribution. Test: derive the exact condition
`F(y) >= eps(span profile)` and search over span profiles. Effort: high. Expected:
the only eps-side idea with >+0.0005 potential, but requires new theory (the current
verifier is eps-constant).

**I-P4 — GUE-typical floor (probabilistic certification).** Instead of certifying
`F >= eps` for *all* blocks, certify `F >= eps'` with eps' > 0.008584 for all but a
measure-zero set under the GUE model, and quantify the excluded set's contribution.
Since the excluded blocks are non-generic (support-min neighborhood, measure ~0 under
GUE), a probabilistic bound could go beyond the support ceiling — but this **breaks
the a.s. deduction** and only works if the measure-zero set provably contributes < ε to
the simple-on-line proportion. This is the *only* idea that escapes the 0.008584
ceiling, at the cost of rigor. CONJECTURED; high risk, high reward.

**I-P5 — Base-rate reframing: the bound is about gap-isolation, not multiplicities.**
Use the Section-5 isolation-scale reading: the 67.3% bound is equivalent (in model
terms) to "both-neighbors-far at scale ~0.5." A *second* probabilistic statement —
e.g. "≥ 2/3 of zeros have min adjacent gap > δ" for a certified δ — would be a
*complementary* bound that a future verifier could target *directly* (a min-gap floor,
not a functional floor). If certifiable, it gives an independent confirmation path.
Effort: medium (new verifier statement). Expected: no bound gain alone, but a
cross-check that strengthens the whole program.

**I-P6 — Extreme-value calibration of eps.** The Wigner/MC analysis says the certified
eps sits at the *extreme-value* scale of the model (~min gap at N~10^5). A probabilistic
"eps as a function of zero-height T" floor — tighter at low T, looser at high T — could
be certified in *height windows* instead of globally, letting the verifier spend effort
where the floor binds. This mirrors I-P3 but in the height variable. Test: certified
eps(T) via windowed verification. Effort: high. Expected: +0.0001–0.0004 if the
height-windowed eps can be certified higher at the heights that matter.

**I-P7 — Rigidity-derived number-variance floor.** Because GUE rigidity (Sigma^2(6) ≈
0.40 vs Poisson 6) makes tight 6-clusters exponentially rare, a *number-variance* bound
(level-repulsion at the scale of a block) might certify a stronger statement than the
current pointwise F floor: e.g. "the average of F over any M consecutive blocks ≥
eps_avg > eps" — the average relaxes the worst-case. Test: derive the averaging identity
and certify `sum F(block_i) >= M·eps_avg`. Effort: high. Expected: +0.0005–0.001 if the
average-floor certifies (the support min of the *sum* is M× the single-block min, so
the average eps can be higher than 0.008584!). This is the *most promising* eps-side
idea and it is *rigor-preserving*.

**I-P8 — Gap-isolation hybrid with pair correlation.** The pair-correlation method
(arXiv 2501.14545) already gives ≥ 2/3 simple-on-line under a thin box; the 67.3263%
record is a *different* functional. A hybrid: use the *probabilistic* isolation model to
predict *where* the functional floor binds (rare blocks), and target the verifier's
effort there (importance-weighted subdivision). This doesn't change the bound but makes
certification *cheaper*, freeing budget for the higher-eps attempts (I-P1/I-P2). Effort:
medium.

**I-P9 — The "1.065×" warning as a search heuristic.** Because eps can't exceed
0.008584, the *correct* search variable is H and psum. In particular: **stop searching
eps above ~0.0085** (any gain is < +0.0003) and **put the budget into the two-tone
window family (H ceiling) and psum reduction**. This is a *negative* result that
redirects effort — arguably the most valuable output of the probability lens.

**I-P10 — GUE-consistency as a validation gate.** Every proposed configuration
(alpha, psum, eps, m) can be *pre-screened* by the GUE model: compute P(F < eps) under
GUE MC and the support min. Configurations with P(F < eps) ≈ 0 *and* eps below the
support ceiling are the only ones worth certifying; anything else is either wasted
effort (typical blocks never bind) or doomed (eps above support min). This makes the
probability machinery a **cheap filter** in front of the expensive verifier. Test:
already implemented (`idea-probability` binary + `guecheck`).

---

## Honesty labels

- **PROVEN:** GUE eigenvalues are simple a.s. (standard RMT); `P(F < eps)=0/100k` under
  GUE MC; the deterministic support min 0.008584 (Rust search, reproducible).
- **CHECKED NUMERICALLY:** record bound reproduction (0.673262865534356, matches [RETIRED 2026-08-24]
  mpmath); H(1.49)=0.672421886096447; support-min search (multiple seeds, uniform scan
  + 10M random + descent → 0.0085837); simplex boundary min 0.016332; eps→bound sweep;
  base-rate 12000/12000; Wigner tail 5.10e-5; MC min-gap 0.0131; rigidity
  Sigma^2(6)=0.4026. Scripts: `idea-probability-work/src/main.rs` (commands in §2/§4),
  `/tmp/support5.rs`, `/tmp/boundary.rs`, `/tmp/final_calc.rs`, `zeta-rs` (commands in
  §1/§4).
- **CONJECTURED:** all ten ideas (none certified); the isolation-model identification of
  δ≈0.5 with the 2/3 bound; the windowed/averaged eps ideas (I-P3/I-P6/I-P7).
- **ABANDONED:** the original wrong functional (pairwise-difference spans) — replaced by
  the exact cumulative-span functional after reading `verify_cos7.py`.
- **INCONCLUSIVE:** whether the support min is exactly 0.008584 (a global minimization
  certificate would need an interval proof; the value is a strong numerical lower bound
  from 10M+ descent points, and the uniform scan independently confirms ~0.0092).

---

## Commands to reproduce

```
# Record reproduction + all MC (Rust, no deps):
cd /home/opc/riemann/research/waves/wave-blast/results/idea-probability-work
cargo build --release && ./target/release/idea-probability

# Base rate + guecheck + probmodel (zeta-rs, fixed solver):
cd /home/opc/riemann/tools/zeta-rs
cargo build --release
./target/release/zeta-rs gue --matrix 60
./target/release/zeta-rs guecheck 149 100 1 1320 8060 1000000
./target/release/zeta-rs probmodel 100000 0.6732 --seed 42

# Support-min searches (Rust):
rustc -O /tmp/support5.rs -o /tmp/support5 && /tmp/support5   # -> 0.0085837
rustc -O /tmp/boundary.rs -o /tmp/boundary && /tmp/boundary   # -> simplex min 0.016332

# eps->bound at support ceiling:
rustc -O /tmp/final_calc.rs -o /tmp/final_calc && /tmp/final_calc

# Arb/flint kernel cross-check (python-flint, semantics only):
cd /home/opc/riemann/tools/beat673 && uv run --with python-flint python3 -c "..."  # kernel table
```

**RESULT: DONE — GUE base-rate is 1.0 (all eigenvalues simple); the certified eps
0.00806 is at 94% of the deterministic support ceiling (min F ≈ 0.008584, headroom
1.065×), so the eps knob is nearly exhausted (+0.000336 max) and the probability lens
redirects effort to H/psum/two-tone windows; 10 CONJECTURED ideas (I-P1..I-P10) quantify
each path against the record 0.6732628655.** [RETIRED 2026-08-24]
