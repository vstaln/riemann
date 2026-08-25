# SYNTHESIS — finite-T orchestrator: does the record's certificate hold for all finite T (P6)?

**Role:** SYNTHESIZER (wave-orch-phone, task-orch-finitet). Sub-swarm (READER, IDEA-GEN, EXECUTOR,
VERIFIER, THEORIST) completed inline before the orchestrator's agent died on a phone crash; the
graph was one step from complete. This note merges the 5 role files. Honesty labels per
`hooks/agents.md`; the role files and their scripts are the cited sources — **no number was
recomputed here** (ponytail rung 1: the role files agree on every shared number; executor
cross-validates prior notes' HS2 to all printed digits, verifier reproduces the record to 4.8e-14).

Record under test: **bound = (H − τ)/(1 − B/m) = 0.6732628655343560…**, H(1.49) = 0.6724218860964, [RETIRED 2026-08-24]
τ = (1/220)·(m−6)/m with m=133, B = Φ_m(ε(m−6)) with certified ε ≥ 0.00806 (Arb interval verifier).

---

## 1. Role-verdict table

| role | file / script | verdict (labeled) | one line |
|---|---|---|---|
| READER | `reader-finitet.md` | INCONCLUSIVE | Error structure extracted (E1–E6); formula is T-free; dominant open term is the CONJECTURED zero-statistics pair-sum deficit (E3); α=1.49 finite-T direction unprobed at the time. |
| IDEA-GEN | `idea-gen-finitet.md` | INCONCLUSIVE | Paper's chain has exactly two dropped terms: O(T^δ log T) δ=1e-10 (negligible) and the o_χ(1) smoothing error = P6; classical analogy says finite-T errors vanish/overshoot (safe); fix = prove o_χ(1) via super-algebraic decay (HIGH impact). |
| EXECUTOR | `executor-finitet.md` + `executor-finitet-probe.py` | CHECKED NUMERICALLY | Δ = bound/N − own-asymptotic-constant > 0 at every T ≤ 5000 for BOTH cos(√2) and the record's cos(1.49): Δ = +0.040…+0.066 (1.49), +0.025…+0.051 (√2), decaying slowly; trW/N → 1 cleanly; HS2/N still ~2% below its window constant at T=5000. |
| VERIFIER | `verifier-finitet.md` + `verifier-finitet-flip.py` | CONJECTURED (robust) | Certificate formula is T-FREE (PROVEN by inspection+arithmetic); margins +6.995e-5 vs tawanerguo, +7.622e-4 vs Theorem D; flip needs dropped terms ≥ 6.995e-5 NEGATIVE at T→∞ — none seen at any T; sensitive lever is B/m (margin 1.0e-4), not H. |
| THEORIST | `theorist-finitet.md` | CONJECTURED | Best lever to *certify*: o_χ(1) bound (Term 1, provable with repo tools = P6 closure); term that most *helps the constant*: HS2 pair-sum deficit (Term 2, direct but deep zero-statistics); practical constant lever: ε/B/m (margin 1.0e-4). |
| **SYNTHESIZER (this note)** | `synthesis-finitet.md` | **CONJECTURED (robust to finite T)** | see §2–§4. |

---

## 2. Does the certificate hold for all finite T? — the P6 answer

**The formula itself is T-free (PROVEN).** Every ingredient of bound = (H−τ)/(1−B/m) is an exact
rational (τ), a certified constant (ε → B), or a verified window value (H, verified to 1.7e-41).
No T-dependent dropped term appears in the formula. The finite-T content lives entirely in the
**derivation** of the liminf machinery (Claim 2.1 Poisson completion, Lemma 3.2 trW, Lemma 3.3
‖W‖²_HS) — i.e. in what "liminf_{T→∞}" forgets. This is the correct structure for a liminf
statement: a finite-T dip at accessible T does NOT refute it; only a finite-T error that survives
as T→∞ with the wrong sign would.

**The measured finite-T errors are safe-direction (CHECKED NUMERICALLY, T ≤ 5000).** The executor's
probe of the idealized cosine-window functional finds Δ = bound/N − (window's own T→∞ constant)
POSITIVE at every measured T for both windows — magnitude +0.04…+0.07 (α=1.49), three orders of
magnitude above the record's 6.995e-5 margin, in the overshoot (safe) direction. This extends the
prior notes' T≤600 finding 8× in T and confirms the record's own α=1.49 window behaves the same.

**The flip test (VERIFIER) concludes:** to drop the record below the previous record (tawanerguo),
the dropped terms would need magnitude ≥ 6.995e-5 with NEGATIVE sign at T→∞ (or B/m ≥ 0.007593,
i.e. ε forced down ~1.3% — B/m is the sensitive lever, currently 0.007696). No negative-sign
evidence exists in any probe, at any T, for either kernel.

**Residual risk (honest):** the asymptote level of Δ is INCONCLUSIVE (fits: 1/log²T intercept
+0.01…+0.03, 1/logT intercept −0.016…0, all comparable rss), so a slow negative drift at
T ≫ 10⁵ cannot be excluded from data — but classical numerology (Montgomery/GUE, Levinson-type
mollifiers) says the deficit shrinks, never flips. And the probes measure the *idealized*
functional vs its own constant, not the block-refined functional; a refined-functional probe at
larger T is the outstanding check.

**Single best answer to P6:** *the record 0.6732628655 is CONJECTURED robust to finite T — the [RETIRED 2026-08-24]
certificate is T-free by construction, every measured finite-T error (T ≤ 5000, both windows) is
positive/safe and an order of magnitude too large to hide a flip, and no mechanism produces a
negative T→∞ error; the honest ceiling on certainty is the unprobed o_χ(1) bound, provable with
the paper's C∞ construction + super-algebraic decay.*

---

## 3. tower_probe.py bug — impact note

`probe/tower_probe.py` (sibling derivative-tower probe, P5 territory) has a KNOWN BUG at line 87:
`find_roots` does `if f_prev * f_next < 0` where `f_prev`/`f_next` are mpmath `mpc` objects —
an `mpc`-vs-`int` `<` comparison, which raises `TypeError` at runtime. Confirmed in
`results/executor-probe.out`: the script **crashed on its very first root-scan call** (line 87 →
line 49) and produced **no output, no numbers, no JSON**.

**Impact: zero finite-T role numbers depend on it.** None of the 5 role files cite any tower_probe
output (grep confirms no Q1–Q5 or ξ′-tower number is referenced anywhere in `results/`). The finite-T
certificate analysis stands entirely on the executor/verifier scripts, which ran clean.

**What IS INCONCLUSIVE:** the whole derivative-tower line (task-orch-tower: Q1 interlacing of ξ′/ξ″
zeros, Q2 spacing statistics, Q3 signed-kernel pair correlation, Q4 stationary points of Z, Q5
kernel-zero pressure floor). Because the bug killed the run before the first result, **every
claimed number that tower probe was meant to produce is INCONCLUSIVE** — not because a number is
wrong, but because no number exists. Any future P5 claim must re-run a fixed `find_roots`
(e.g. compare real parts, or wrap f in `mp.re` / check `abs(f) < tol`), with the fix noted here.

---

## 4. Labels summary (honesty charter)

- Formula is T-free: **PROVEN** (inspection + verifier arithmetic, mpmath 80 digits).
- Measured finite-T overshoot Δ > 0 at all T ≤ 5000, both windows: **CHECKED NUMERICALLY**
  (`executor-finitet-probe.py`, data to γ ≈ 10726).
- Robustness to finite T: **CONJECTURED** (no negative-sign evidence; flip threshold 6.995e-5;
  asymptote of Δ and the block-functional probe outstanding — INCONCLUSIVE).
- Derivative-tower probe: **INCONCLUSIVE** (bug, crashed, no output).

RESULT: CONJECTURED — the 0.6732628655 certificate is T-free and finite-T robust at all measured [RETIRED 2026-08-24]
heights (safe-direction overshoot, flip needs ≥7e-5 negative error at T→∞, none seen); the
derivative-tower probe is INCONCLUSIVE due to the mpc-vs-int bug (no numbers produced).
