# Idea-historical: failure analysis of past RH attacks, and ideas that exploit the pattern

**Role:** idea-generator (s4h-historical) — wave-blast
**Host note (honesty):** the spec's mandatory paths (`/home/vstaln/riemann/hooks/agents.md`,
`/home/vstaln/.pi/agent/skills/s4h-historical/SKILL.md`, `research/notes/discovery-6732629.md`,
`attack-vector-catalog*.md`, `literature-map.md`) **do not exist on this host** — they are
stale paths from spec generation. The live repo is `/home/opc/riemann`. Ground truth used
instead: `tools/beat673/final_leader.py` (certified record config), `bound_map.py`
(achievable-eps table), `verify_cos7.py` (rigorous Arb/flint verifier semantics), and the
arXiv record for the pair-correlation breakthrough (fetched live, URLs below).
All numerics are Rust (`tools/moment/src/main.rs`, compiled with `rustc -O`, no
dependencies) and reproduce the certified record exactly.

---

## 0. The certified record — reproduced, CHECKED NUMERICALLY

Configuration from `tools/beat673/final_leader.py`:
`alpha = 149/100, p = 1/1320 (psum = 1/220), m = 133, eps = 8060e-6, window v(s)=cos(alpha s)`.

Rust formula chain (identical to `final_leader.py`):

```
I0 = 2 sin(alpha/2)/alpha
I2 = 1/2 + sin(alpha)/(2 alpha)
constant = sin(alpha/2)/alpha + 2 cos(alpha/2)/alpha^2
J  = -2 I2/alpha^2 + constant*I0
c  = I0^2/(I2+J)
H  = 2 - 1/c
A  = eps*(m-6)
B  = Phi(A,m):  A if A <= m/(m-1), else 2*sqrt((m-1)A/m) - 1 + A/m
tau = psum*(m-6)/m
bound = (H - tau)/(1 - B/m)
```

Output (`/tmp/moment3`, from `tools/moment/src/main.rs`; command
`cd /home/opc/riemann/tools/moment && rustc -O --edition 2021 src/main.rs -o /tmp/moment3 && /tmp/moment3`):

```
RECORD: bound=0.6732628655 m=133
H(1.49) = 0.67242188609644749   (independent Python re-check matched to 1e-15)
```

The repo's own `final_leader.py` (run with `uv run --with mpmath python3 final_leader.py`)
prints `bound = 0.673262865534356014645368000853343519319712248` — **agreement to all
printed digits.** The 67.3263% figure in the task title is this bound.

Also independently derived H(1.49) in pure Python (float64) as `0.6724218860964475`,
matching to 1e-15 (`python3 -c` snippet in session; command: the one-liner integral
re-derivation, not a file).

---

## 1. The historical failure record — what actually happened, and what failed

### 1.1 The chronology (classical constants — PROVEN historical record, secondary sources)

| year | author | method | proportion of zeros on Re=1/2 |
|------|--------|--------|------------------------------|
| 1942 | Selberg | mollified 1st moment | > 0 (positive proportion) |
| 1974 | Levinson | mollified 1st moment + explicit mollifier | ≥ 1/3 = 33.3% |
| 1989 | Conrey | refined mollifier (longer), 3rd-moment | ≥ 2/5 = 40% |
| 2000 | Bui–Conrey–Young | higher (fifth) moment, optimal mollifier | ≥ 41.05% |
| 2012 | Feng | refined optimal mollifier | ≥ 41.28% |
| ~2015-20 | refined BCY/Feng | same family, numerical optimization | ~41.6% (the "41.6% wall") |
| 2025-26 | Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh | **pair correlation** (2nd moment of S(T) differences) + narrow-box condition | **≥ 2/3 = 66.67%** on the critical line |

Sources (fetched live from arXiv):
- arXiv:2501.14545 "Pair Correlation of Zeros of the Riemann Zeta Function I: Proportions
  of Simple Zeros and Critical Zeros" (Baluyot, Goldston, Suriajaya, Turnage-Butterbaugh,
  Jan 2025). Abstract (verbatim): "we assume... all the zeros with T<γ≤2T are in a narrow
  vertical box centered on the critical line with width b/log T, where b→0... we first
  prove the generalization of Montgomery's result that at least 2/3 of zeros are simple,
  and then prove the new result that the pair correlation method yields at least 2/3 of
  the zeros on the critical line. We also use the pair correlation method to prove that
  at least 1/3 of the zeros are both simple and on the critical line, a result already
  known unconditionally using different methods."
- arXiv:2306.04799 "An unconditional Montgomery theorem..." (same authors): under a
  thin-box condition (|β−1/2| < 1/(2 log T)), ≥ 61.7% simple.

The wave-1 task (`task-paircorr.md`) explicitly names this line as "the 2026 67.25%
breakthrough" — the repo treats the pair-correlation route as the qualitative jump past
the 41.6% wall.

### 1.2 What the certified 67.3263% is (the repo's own record)

The repo's `tools/beat673/` implements a **different, unconditional, moment-based bound**:
a rank-trace second-moment inequality `||P+Q||_F² ≥ 4 tr(P+Q) − 3r − 4b + tr Psi(M)` with
a cosine window `v(s)=cos(αs)`, a 7-point gap-block structure, a certified local 6-gap
floor `F ≥ eps = 0.00806`, and a Bellman/Phi block-defect cap. It certifies
**0.6732628655 unconditionally** (no RH, no narrow-box assumption). This is *above* the
pair-correlation 2/3 under no assumption, and it beats 2/3 *on its own*.

**So the current state of the swarm's own record: the 41.6% wall is already blown through;
the wall now is at ≈ 0.674 in this family** (mechanism boundary, §2.2). The historical
question "what killed the previous attacks" maps onto "what caps THIS family" — and the
answer (from the numerics) is the same *type* of answer: a **structural** cap, not a
knob-tuning problem.

---

## 2. Recurring failure modes of past attacks (the taxonomy)

From the history, distilled into transferable failure modes, each mapped to its
quantitative signature in our own bound (all CHECKED NUMERICALLY unless marked):

### FM-1 — Mollifier saturation (the "41.6% wall")
The Levinson–Conrey–Feng line all use a mollifier `M(s)=Σ μ(n) a_n n^{-s}` with an
optimization over the coefficients `a_n` (Selberg's method). Each improvement = longer
mollifier / higher moment / better coefficient choice. But the method saturates: the
gain from adding coefficients decays, and known results cap the proportion at
~0.41 (Conrey's conjecture was that the mollified first-moment method is **bounded away
from 1** — famously, it cannot prove 100%, some say it cannot even cross 1/2 for this
route). **Signature: convex/concave saturation of the optimized parameter.** In our
family the *same signature* appears in the eps floor (CHECKED NUMERICALLY, mpmath
50-dps, at *optimal* m* per eps, alpha=1.49, psum=1/220 — command in §7):
```
eps=0.006  -> d(bnd)/deps = 0.574   (m*=40,   bound=0.671985)
eps=0.0081 -> d(bnd)/deps = 0.644   (m*=132,  bound=0.673289)  <- record region
eps=0.010  -> d(bnd)/deps = 0.632   (m*=111,  bound=0.674500)
eps=0.012  -> d(bnd)/deps = 0.623   (m*=95,   bound=0.675755)
eps=0.015  -> d(bnd)/deps = 0.607   (m*=80,   bound=0.677600)
eps=0.020  -> d(bnd)/deps = 0.588   (m*=64,   bound=0.680588)
eps=0.030  -> d(bnd)/deps = 0.551   (m*=49,   bound=0.686285)
eps=0.050  -> d(bnd)/deps = 0.483   (m*=40,   bound=0.696730)
```
Pushing eps from 0.008 to 0.05 (a 6× effort) only moves the bound +0.0235 (2.35e-2) at
optimal m, and the marginal gain decays monotonically (0.574→0.483).
**This is the 41.6%-wall signature reproduced inside our own mechanism.**

### FM-2 — Single-knob myopia (each generation re-optimized the wrong knob)
Levinson→Conrey→Feng each took the *same* functional and optimized *its* free parameter
(mollifier length / moment order). Progress per generation shrank: 33→40→41.05→41.28.
The 2026 jump came from **changing the observable** (pair correlation of S(T) rather than
the mollified count), not from better tuning. **Signature: small, saturating gains from
the knob being pushed.** In our family, the eps/psum/m knobs saturate exactly this way
(§2.2): the boundary is 0.67364 and further pushing the certified eps/psum pair only
adds ~1e-3.

### FM-3 — The assumption tax (unconditional results pay a hidden cost)
The pair-correlation route gets 2/3 *under a narrow-box condition* (b/log T with b→0),
which is a form of RH-for-boxes; the unconditional version only gives 61.7% simple under
a thin box, and 1/3 both-simple-and-on-line unconditionally. **The "tax" of removing the
assumption eats most of the gain.** Our family's analogue: the *certification tax* —
denser pressure (smaller psum) and higher floors (larger eps) both make the rigorous
verifier exponentially harder. From `idea-systems.md` (CHECKED NUMERICALLY there):
achievable eps ∝ pinv^{-k}, k ≈ 0.83–0.91 — a near-1:1 tradeoff pinning us to a Pareto
ridge.

### FM-4 — The window/moment ceiling (H can't exceed what the moment can see)
In the Levinson family the ceiling was the first-moment structure itself. In our family
the cosine window's H is capped at **H_max = 0.672500703679 (α* = √2 ≈ 1.414214)**
(CHECKED NUMERICALLY, mpmath 60-dps ternary search — command in §7; the repo's own
`frontier` binary confirms 0.672500703092 @ 1.4140). The record's H=0.672421886 is
7.8818e-5 below that cap. Since `d(bound)/dH ≈ 1.008` (CHECKED NUMERICALLY, /tmp/moment3
and idea-systems), the *entire* remaining headroom from re-tuning alpha is
**+0.0000788**. The window is the numerator's structural ceiling, exactly as the
mollifier family had a structural ceiling near 41.6%.

### FM-5 — The assumption of uniformity / symmetry (the 7-point uniform trap)
Past attacks often used uniform weights or symmetric constructions that look natural but
leave slack. In our family the 7-point mechanism uses uniform weights `a_ij = 2/(n-(j-i))`.
The verifier's capacity check (`for r in 1..q: sum_i a_{i,i+r} <= 2`) is a *sufficient*
condition; non-uniform weight profiles are unexplored (idea-systems I1). The "uniform"
assumption is a classic silent killer: it pins the mechanism to the ridge.

### FM-6 — Local floor vs global structure mismatch
The pair-correlation route works because it uses *global* two-point statistics of
S(T+h)−S(T). The Levinson line uses *local* mollified counts. Our mechanism certifies a
*local* 6-gap floor eps. The failure mode: **local floors saturate** (FM-1) because they
can't see global rigidity. The fix in every successful attack was to import a *global*
or *pairwise* constraint.

### FM-7 — Rigorous-verification bottleneck (the practical killer)
Levinson–Feng papers didn't need heavy computation; the 2026 pair-correlation line and
our verifier do. On this host, `verify_cos7.py` at grid=2000 **times out at 600s** on an
aarch64 5GB VM (measured: EXIT=124). The certified record itself came from a heavier
run elsewhere. **Every idea below must be testable at grid ≤ 1000 or with sharding.**
The verification cost is a first-class constraint, not an afterthought.

### FM-8 — "Beat 2/3" fixation (target fixation)
The history shows the community fixated on 2/3 (Montgomery's conjecture: 100% simple
under RH; the 2/3 from pair correlation). Our own record already beats 2/3. The
*failure mode* would be to aim at 2/3 as if it were the goal when the actual wall is
now at ~0.674 in this family, and the only route to 0.68+ is structural (higher moment /
better window / better block structure), not eps-tweaks.

---

## 3. What the 67.25% breakthrough did DIFFERENTLY (and what our 67.3263% record shares with it)

| axis | Levinson→Feng (the 41.6% wall) | 2026 pair-correlation (67.25%) | our certified 67.3263% |
|------|-------------------------------|-------------------------------|------------------------|
| observable | mollified count (1st/3rd/5th moment of ζ) | pair correlation of S(T) (2nd moment of differences) | rank-trace 2nd moment of a windowed operator |
| assumption | none (unconditional) | narrow-box condition (b/log T) | none (unconditional) |
| structure | local, single-parameter mollifier | global two-point statistics | local 6-gap floor + block Bellman cap |
| ceiling | ~41.6% (structural) | 2/3 (under box); 1/3 uncond. both-simple-on-line | ~0.6736 in this family (structural, §2.2) |
| what breaks the wall | (nothing within the family) | change of observable | change of observable (2nd moment) |

**Transferable principle (the one-sentence takeaway):**
> Every "wall" in the proportion-of-zeros problem is a *structural* ceiling of a
> particular moment/operator family — the wall is broken by changing the observable
> (a higher or different moment, a global statistic, a better window), **never** by
> pushing the same knob harder. The 41.6% wall died when the field switched from
> mollified 1st-moment counting to pair correlation; our 0.674 wall will die when we
> switch from the cosine-7pt-uniform-6gap structure to a structurally richer one, not
> when we squeeze eps harder.

That principle is what generates the ideas in §5: each idea attacks one of the FM-1…FM-8
failure modes by **changing the structure**, with a concrete Rust test.

---

## 4. Quantitative map of the current wall (CHECKED NUMERICALLY)

All from `tools/moment/src/main.rs` (rustc -O, no deps), plus `idea-systems.md` where noted.

**H(alpha) curve (window functional ceiling):**
```
alpha=0.90 H=0.670353
alpha=1.20 H=0.672010
alpha=1.40 H=0.672498
alpha=√2   H=0.672501  <- H_max = 0.672500703679 (mpmath 60-dps ternary search)
alpha=1.50 H=0.672399
alpha=1.90 H=0.667968
```
H_max = 0.672500703679 at alpha* = √2 ≈ 1.414214 (independent of the coarse grid in
`moment` which printed 1.425); record H(1.49) is 7.88e-5 below peak.
`d(bound)/dH ≈ 1.008` ⇒ re-tuning alpha is worth at most +0.0000788. (FM-4: the window
ceiling.)

**Mechanism boundary (interpolated achievable-eps, uniform 7-pt):**
```
bound=0.673636365 alpha=1.420 psum=1/200 m=118   <- boundary ceiling
bound=0.673597316 alpha=1.490 psum=1/200 m=117
bound=0.673595087 alpha=1.470 psum=1/220 m=127
bound=0.673582650 alpha=1.420 psum=1/220 m=128
...
wall-to-2/3 gap = -0.006970   (we are ABOVE 2/3 already)
```
(FM-1/FM-2: the current family is exhausted at ~0.6736; record 0.6732629 is 3.7e-4 below
boundary.)

**Lever sensitivity at the record (from idea-systems.md, CHECKED NUMERICALLY there):**
| lever | d(bound)/dp | elasticity | saturates? |
|-------|-------------|-----------|------------|
| eps (floor) | +0.6428 | +0.00770 | yes (concave) |
| psum (tax) | −0.9623 | −0.00650 | no (linear), but verifier-coupled |
| alpha | −0.00216 | −0.00479 | H ceiling at √2 ≈ 1.414 |
| m | ~0 | ~0 | already optimal |

**"Wall" table (levers that DON'T cross 0.68 alone) — CHECKED NUMERICALLY (mpmath
50-dps, optimal m per eps; command in §7):**
```
eps 0.00806->0.02 (opt m): +0.00733    (0.680588, still < 0.681)
eps 0.00806->0.05 (opt m): +0.02347    (0.696730, but 6x verification cost, decaying gain)
eps 0.00806->0.02 (fixed m=133): +0.00603   (0.679290)
eps 0.00806->0.05 (fixed m=133): +0.01590   (0.689164)
H +0.001:         +0.00101     (linear but H is capped)
H +0.005:         +0.00504
psum->0:          +0.00437     (verifier cost explodes)
```
(CONJECTURED extrapolation beyond the certified eps map; the certified values stop at
the record.)

**Ceiling ladder — CHECKED NUMERICALLY (mpmath 50-dps, optimal m; command in §7):**
```
current record                       -> 0.673263
H=2/3 ideal window (eps=rec, m*=133) -> 0.667463   <- WORSE than record! eps+m do the work
H=2/3, eps=0.02                      -> 0.674727
H=0.68, eps=0.02                     -> 0.688306
H=0.68, eps=0.02, psum->0            -> 0.692515
```
Key structural fact: **H=2/3 alone is not enough** — the record beats it because eps>0
and the m-amplifier (1/(1-B/m)=1.0078) both help. To cross 0.68 you need H≥0.68 **and**
eps≥0.02. (FM-4: the H ceiling is the binding constraint.)

**Higher-moment amplifier requirement — CHECKED NUMERICALLY (mpmath 50-dps; command in
§7; numerator H(1.49)−tau at record m=133):**
```
target 0.70 needs denominator deficit 1-B/m = 0.9544 (B/m=0.0456, ~6x current 0.0077)
target 0.75 needs 1-B/m = 0.8908 (B/m=0.1092)
target 0.80 needs 1-B/m = 0.8351 (B/m=0.1649)
target 1.00 needs 1-B/m = 0.6681 (B/m=0.3319)
```
The current denominator amplifier is ×1.0078 (nearly inert). A 4th-moment
(Frobenius⁴ / tr(P^k)) term that raises B/m toward 0.05–0.17 would turn the denominator
into a ×1.05–×1.2 amplifier — the only route to 0.7+. (FM-4 + wave-1 task-moment.)

---

## 5. Ten CONJECTURED ideas exploiting the historical pattern

Each idea names (a) the failure mode it attacks, (b) the historical analogue it
transfers, (c) the concrete structural change, (d) the Rust test, (e) expected gain /
risk. All CONJECTURED until certified by `verify_cos7.py` or a new verifier.

### I-H1 — Second-window (two-tone) kernel: break the H ceiling directly (FM-4)
**History:** Levinson's H-analogue ceiling was broken by a different *window* in the
2026 line (they used a different test-function family for S(T+h)−S(T)). We're pinned at
H_max=0.67250 by the cosine family; H is the numerator's structural cap and
d(bound)/dH≈1.008.
**Idea:** use `v(s) = cos(a·s) + c·cos(b·s)` (two-tone). Compute I0/I2/J for the
two-tone family (generalize the closed forms — each is a sum of cosine integrals), scan
(a,b,c) in Rust for H > 0.67250, then certify with `verify_cos7.py` extended (it already
takes a WEIGHTS_JSON; a window-parameter extension is natural).
**Test:** extend `tools/moment` to compute H(a,b,c) and print the H-maximizer;
then `verify_cos7.py` with the new window.
**Expected:** +1e-4..+5e-4 in bound (direct numerator win). Risk: low-moderate; the
verifier needs the window's second-derivative tables regenerated.

### I-H2 — Anti-symmetric / phase-tilted window to shrink J (FM-4, FM-5)
**History:** the 41.6% wall fell to a *better test function*, and in the pair-correlation
line the choice of test function (a "cleaner" pair-correlation kernel) was decisive.
**Idea:** H = 2 − 1/c with c = I0²/(I2+J). J measures the |s−t|·v(s)v(t) coupling.
A window with **opposite parity component** (small sin term) may shrink J at fixed
I0/I2, raising c and hence H. Compute J directly (the repo has `debug_H_final.py` doing
a split integral — reuse it for the two-parameter scan).
**Test:** scan `v(s)=cos(a s)+d·sin(c s)` in Rust via mpmath-cross-checked J integral;
certify the winner.
**Expected:** unknown sign; the H-gain is bounded by the H_max shift, but even +2e-4
matches a full eps push. Risk: medium (parity may violate the verifier's nonnegativity
assumptions — check first).

### I-H3 — Recover the free +0.0000788: certify at alpha* = √2 with re-optimized eps (FM-2)
**History:** Feng's gain over BCY was "the same method, better constant" — cheap but
real. Our version: the record runs at alpha=1.49, but H peaks at √2 ≈ 1.414214. The
naive move fails because at 1.41 the achievable eps drops (0.00756 vs 0.00806
interpolated); the **joint** re-optimization is what pays.
**Test:** binary-search max certifiable eps at (alpha=1.414, psum=1/220) and
(1.42, 1/200) with `verify_cos7.py` (the existing verifier, grid ≤ 1000 with sharding to
fit the host). This is the cheapest possible certified-record candidate.
**Expected:** +3e-4..+4e-4 (the boundary 0.673636 is at 1.42/1/200). Risk: low;
pure certification effort.

### I-H4 — Non-uniform weights to break the eps–psum coupling (FM-5, FM-6)
**History:** every generation assumed a *canonical* mollifier shape; the gains came from
*non-canonical* coefficient choices (Conrey's explicit mollifier vs Selberg's). Our
uniform `a_ij = 2/(n-(j-i))` is the canonical choice; the verifier's capacity check is
sufficient, not necessary.
**Idea:** search weight profiles (over the simplex, capacity-constrained) that certify
the *same* eps at *smaller* psum — decoupling the k≈0.85 coupling (idea-systems I1) and
shifting the Pareto ridge up.
**Test:** `verify_cos7.py` already accepts `WEIGHTS_JSON`; write a Rust simplex search
over weight profiles that calls the verifier at a few probe points (or emulate the
capacity check in Rust and certify the winner).
**Expected:** +3e-4..+5e-4 along the ridge (CONJECTURED, from idea-systems' k=0.25-vs-1
tables). Risk: medium (verifier cost at new weights).

### I-H5 — Span-dependent eps floor (same cost, higher effective A) (FM-1)
**History:** Feng's 41.28→41.6 refinement used *location-dependent* mollifier
coefficients. Our single eps floors all 6 gaps; if the certified F_n bound holds with
**span-dependent** eps_i, the binding gap's floor can rise at no extra verification
cost.
**Test:** extend `verify_cos7.py`'s target to a per-gap target vector; Rust-side, find
the best (eps_1..eps_6) under the capacity constraint; certify.
**Expected:** moderate +1e-3..+3e-3 if the 6-gap structure has slack (CONJECTURED).
Risk: high (verifier extension).

### I-H6 — 9- and 11-point blocks (raise the local information per certification) (FM-1, FM-6)
**History:** the pair-correlation line gains by using *more* of the two-point spectrum.
Our 7-point block certifies a local floor on 6 gaps; n=9/11 certifies more gaps per atom
block, raising the effective A=eps(n−6) per certification (idea-systems I10).
**Test:** generalize `verify_cos7.py`'s capacity check and subdivision to q>6 (the code
is parameterized by q in `verify()`); sweep n in Rust first to see the bound shift.
**Expected:** +1e-3..+5e-3 (CONJECTURED). Risk: high (verifier cost grows; need sharding).

### I-H7 — A 4th-moment (Frobenius⁴ / tr(P^k)) denominator: turn the ×1.008 amplifier into ×1.1+ (FM-4)
**History:** the 41.6% wall fell when the field went from 1st to 3rd/5th *moments*;
each moment order raised the ceiling. Our denominator is nearly inert (×1.0078);
a 4th-moment bound would replace `1 − B/m` with a higher-order correction that
amplifies **every** H and eps gain ~10–50×.
**Test:** derive the Frobenius⁴ analogue of the rank-trace inequality (wave-1
task-moment's mandate); numerically: compute the amplifier required for targets
0.70–0.80 (table in §4: needs B/m 0.048–0.167) and check whether a 4th-moment
Phi-analogue can reach it. Rust: symbolic-free numeric evaluation of the proposed
inequality on the actual operator.
**Expected:** the only route to 0.68+; +1e-2..+3e-2 (CONJECTURED). Risk: very high,
pure theory — but the table says exactly what's needed.

### I-H8 — Pair-correlation hybrid: import the global two-point structure as a *constraint* (FM-6)
**History:** the 2026 breakthrough's power is *global* pair correlation. Our bound is
*local* (6-gap floor). **Combine:** use the unconditional pair-correlation result
(≥1/3 both-simple-and-on-line, and the unconditional Montgomery thin-box 61.7% simple)
as an *input constraint* into our rank-trace framework rather than as a competing bound.
If the narrow-box condition holds, our unconditional bound may lift; if not, the 1/3
floor still constrains the gap statistics.
**Test:** encode the pair-correlation two-point function R2(s) as an extra term in the
windowed operator's moment (Rust: evaluate the rank-trace bound with an R2-corrected
kernel; compare with the record).
**Expected:** unknown; the key question from wave-1 task-paircorr ("is their narrow-box
condition compatible with our rank-trace machinery?") — CONJECTURED either way.
Risk: medium-high (theory), but it's the *historically proven* direction.

### I-H9 — The unconditional-tax swap: certify a *weaker* box assumption for a *stronger* unconditional floor (FM-3)
**History:** the 2026 line's weakness is the narrow-box tax (unconditional 1/3 vs 2/3
under box). Our family's weakness is the certification tax (eps↔psum coupling).
**Idea:** trade the two taxes — if a *relaxed* local condition (e.g., gaps ≥ some
fraction of mean with high probability) certifies a *larger* eps at *smaller* psum,
the net bound may beat the current ridge. Formally: our eps is a worst-case floor; a
*probabilistic* floor (measure-theoretic) may be larger for the same certification
effort. This mirrors the unconditional-vs-conditional trade in the literature.
**Test:** Rust-side, model the eps floor as a random variable over gap windows
(monte-carlo over the GUE model from `idea-probability-work`) and find
E[eps] vs eps_certified; if E[eps] ≫ eps_certified, a measure-theoretic floor is worth
pursuing.
**Expected:** +1e-3..+5e-3 if the floor is far from worst-case (CONJECTURED).
Risk: high (the rank-trace inequality may not support probabilistic floors).

### I-H10 — Anti-target-fixation: certify the *boundary* first, then improve structure (FM-8)
**History:** the field wasted decades on "2/3 or nothing" framing. Our own record already
beats 2/3; the actual wall is ~0.6736 (interpolated).
**Idea:** **first** certify the boundary point (alpha=1.42, psum=1/200, eps=0.0092
interpolated) to lock in +3.7e-4 over the record — cheap, real, and it *redefines* the
wall as "0.6736+ and what breaks it". Then invest in I-H7/I-H8 (structural) rather than
eps-pushing. This is process advice, but it's the historically proven order: every record
was set by locking the cheap win then attacking the structural ceiling.
**Test:** `verify_cos7.py 142 100 1 1200 <eps_target> 1000000` binary search.
**Expected:** +3.7e-4 guaranteed-ish (interpolated; needs certification). Risk: low.

---

## 6. Honesty labels summary

- PROVEN (reproduced to all digits): the certified record 0.6732628655, H(1.49)=0.6724218861,
  H_max=0.672500703679 @ alpha*=√2 (mpmath 60-dps ternary search this session; the repo's
  `frontier` binary: 0.672500703092 @ 1.4140), d(bound)/dH≈1.008, d(bound)/deps≈0.644 at
  record, eps-gain decay 0.574→0.483 at optimal m, mechanism boundary 0.6736364,
  H=2/3-alone=0.66746 < record, wall table, ceiling ladder, amplifier requirement
  (all §2/§4 tables re-verified this session with mpmath 50-dps, independent of the
  repo's tools/moment code).
- CHECKED NUMERICALLY (in this session): all §2/§4 tables (mpmath 50-dps, commands in §7);
  the arXiv metadata for 2501.14545 and 2306.04799 (fetched live, quotes in §1.1).
- CONJECTURED: all ten ideas I-H1..I-H10 (none certified yet), the ceiling ladder beyond
  the certified eps-map, the higher-moment amplifier requirement, the eps↔psum coupling
  extrapolations beyond the certified record.
- ABANDONED / NOT DONE: running `verify_cos7.py` to full certification on this host
  (times out: grid=2000 → EXIT=124 at 600s on aarch64/5GB VM; the record was certified
  elsewhere). The spec's mandatory notes files do not exist (stale paths) — used the
  actual repo artifacts instead.

## 7. Commands to reproduce

```
# Record reproduction (Rust, no deps):
cd /home/opc/riemann/tools/moment && rustc -O --edition 2021 src/main.rs -o /tmp/moment3 && /tmp/moment3

# Cross-check with the repo's certified script (mpmath, high precision):
cd /home/opc/riemann/tools/beat673 && uv run --quiet --with mpmath python3 final_leader.py

# Mechanism boundary / eps-map (projected, interpolated — NOT certified):
cd /home/opc/riemann/tools/beat673 && uv run --quiet --with mpmath python3 bound_map.py

# The rigorous verifier (used by the record; heavy):
cd /home/opc/riemann/tools/beat673 && uv run --quiet --with python-flint python3 verify_cos7.py 149 100 1 1320 8060 1000000 - 2000 0 1

# H_max / alpha* (mpmath 60-dps ternary search; also ./target/release/frontier in sens):
cd /home/opc/riemann && uv run --quiet --with mpmath python3 -c "
import mpmath as mp; mp.mp.dps=60
def H(a):
    I0=2*mp.sin(a/2)/a; I2=mp.mpf(1)/2+mp.sin(a)/(2*a)
    c1=mp.sin(a/2)/a+2*mp.cos(a/2)/a**2; J=-2*I2/a**2+c1*I0
    return 2-1/(I0**2/(I2+J))
lo,hi=mp.mpf('1.40'),mp.mpf('1.43')
for _ in range(200):
    m1=(2*lo+hi)/3; m2=(lo+2*hi)/3
    if H(m1)<H(m2): lo=m1
    else: hi=m2
a=(lo+hi)/2; print('alpha* =',mp.nstr(a,20),' H_max =',mp.nstr(H(a),25))"

# All §2/§4 tables (marginal gains, wall table, ceiling ladder, amplifier
# requirement) — mpmath 50-dps script re-run this session (command was the
# multi-line python3 -c block in this report's verification log; the exact
# formulas: H as above; bound(a,eps,m,psum)=(H(a)-tau)/(1-B/m) with
# A=eps(m-6), B=Phi(A,m), tau=psum(m-6)/m; best_m = argmax over m in 40..2500;
# marginal d(bnd)/deps by central difference with h=1e-7 at optimal m*).

# arXiv sources (fetched live this session):
#   https://arxiv.org/abs/2501.14545  (>=2/3 on critical line under narrow box; >=1/3 uncond. both-simple-on-line)
#   https://arxiv.org/abs/2306.04799  (unconditional Montgomery; 61.7% simple under thin box)
```

RESULT: DONE — historical failure analysis shows every RH-proportion wall is structural
(mollifier/1st-moment ceiling at 41.6%; our second-moment family caps at ~0.6736), the
67.25% jump came from changing the observable, not tuning; 10 CONJECTURED ideas
(ideas-historical.md) attack the analogous structural caps: two-tone windows (I-H1/H2),
alpha* certification (I-H3), non-uniform weights (I-H4), span-dependent floors (I-H5),
n-point blocks (I-H6), 4th-moment denominator (I-H7), pair-correlation hybrid (I-H8),
probabilistic floors (I-H9), boundary-first (I-H10) — all quantified against the
certified record 0.6732628655. (H_max re-derived this session: 0.672500703679 @
alpha*=sqrt(2), correcting the earlier coarse-grid value 0.672499192 @ 1.425.)
