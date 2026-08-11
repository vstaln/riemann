# Idea Generator: games & sports attack catalog on RH and the on-line-zero constants

**Agent:** IDEA GENERATOR (games/sports angle). Round 2.
**Purpose:** feed the EXECUTIONER agents. Every vector is concrete enough to attack or to kill cheaply.
**Honesty protocol:** this file invents *no* proofs and asserts *no* new theorems about ζ. Domain facts
(hot hand, CFR, Elo, komi, tablebases, etc.) are stated at the level of "standard domain knowledge" and
are labeled as such — **verify any citation before it enters a paper**. Every vector carries one of
**NEW** (invented here) / **KNOWN-DEAD** (death documented in earlier rounds; cited) /
**KNOWN-OPEN** (core is a known open problem or already flagged; cited) / **TESTED-OPEN** (numerically
probed by our tools, conclusion not final). No literature claim is fabricated; nothing below re-derives
a result — it mines domains for transferable structure and prices probes.
**Cross-references:** [CD-#] = idea-generator-crossdomain.md (V = tier, W = wild, A = abandoned);
[P#.#] = idea-generator-physics.md; [AC] = attack-ceiling.md; [AM] = attack-multiplicity.md;
[AF] = attack-finitet.md; [M29] = attack-m29.md; [lfunctions] = attack-lfunctions.md;
[multiplicity] = attack-multiplicity.md; [verif-001] = verification-001.md; [kernel] = attack-kernel.md;
[catalog] = attack-vector-catalog.md.

**State of the art the analogies must respect (PROVEN):**
- Two-moment method: tr W_T = N, ‖W_T‖²_HS = (1/2 + (1/√2)cot(1/√2))·N, certificate value 0.67250070…
  (Theorem D, window-optimal cosine); 2/3 flat; 5/6 distinct; 0.83625 distinct (optimal window).
- Bandwidth-one ceiling 0.68182868746… realized by an exact-rational 256-periodic marked law with
  F ≡ 1 on [0,1] — PROVEN in Lean [AC]. No certificate reading (mean density, F on [0,1], integrality)
  can certify more.
- The two-moment rank–trace prices multiplicity integrality optimally; `lemmaR_tight`; the empirical
  all-simple world has zero slack (Δ = 0) [AM, multiplicity §4].
- Beyond α = 1 form factor: **documented negative** — every proven bound exceeds the certificate's
  tolerance by 3.6·10³–3.7·10⁴× (M29). Only conjectural *values* (HL/Montgomery) would clear it.
- tr Â³ is unconditionally evaluable in the Rudnick–Sarnak range kλ < 2 (λ < 2/3) [CD-V3]; §7.5(e)'s
  "odd moments don't lower Λ₁(0)" is about the *on-line* functional; the *distinct* (c = 3) functional
  is the open target — P2.
- Finite-T: Δ(T) = bound/N − 0.6725 > 0 at every tested T, decaying ~1/log T with sample wiggle
  [AF] (TESTED-OPEN). ξ′: 0.85838/0.86864 simple, 0.92919/0.93432 distinct (PROVEN); ξ″/ξ‴ mechanical
  [CD-V9]. Empirical F̂(α): climbs to ≈ 0.93–1.0 near α = 1, decays beyond; sample noise large at
  N = 3000 — trend only, NOT a tight check [verif-001 §4].
- Open problems this catalog feeds: P1 (missing constraint = the in-class gap 0.6725→0.6818), P2 (third
  moment / distinct wall 5/6), P3 (beyond-scale-1 pair data), P5 (derivative tower), P6 (finite-T
  error terms).

---

## 0. The abstracted problem (structural essence, per s4h-analogy-domain-transfer)

> **Problem stripped of domain vocabulary:** I hold a *certificate* (a rule that scores a configuration
> of points) that provably certifies a lower bound f = 67.25% of points satisfying a hidden constraint
> (on a line). An *adversary* controls the configuration and must only match two aggregate statistics I
> can read exactly from outside data (mean density, pair-correlation on scale 1) plus integer
> multiplicity bookkeeping. The adversary's equilibrium configuration (a 256-periodic crystal with
> exact marks) caps any such certificate at 68.18% — a proven tight ceiling. The gap 67.25→68.18 is
> entirely a *second-moment* gap: a better certificate with the *same data* may or may not reach the
> ceiling (the LP-dual question). Breaking the wall requires reading *more* data the crystal cannot
> fake (a third moment, beyond-1 pair correlation, repulsion) — each is either unproven or
> documented-dead. The certificate must be valid for **every** admissible configuration (worst-case,
> dominant-strategy), and the adversary's crystal is a *bluff*: it emits the same observable moments as
> reality while hiding its off-line structure just past the data's horizon.

The five domains below are mined against this essence. The recurring structural matches: **horizon
blindness** (chess search depth, poker information streets, sports-model lag), **worst-case robustness**
(poker ranges, strategyproof mechanisms), **adversarial equilibrium vs our suboptimal strategy**
(the in-class gap = exploitability), and **the bluff/cheap-talk problem** (can the adversary fake the
next input?). Where each analogy breaks is stated per vector — that is where the transfer ends and the
ζ-specific wall resumes.

---

## Pool 1 — Chess / Go / combinatorial game theory

### G1.1 Horizon-effect taxonomy: which "search extensions" can see past the wall — NEW (framing)
**Idea:** Chess engines are blind beyond finite search depth; the *horizon effect* is a sacrifice that
looks winning at depth d but is refuted at d+1 — engines fight it with *quiescence search* (evaluate
only quiet positions) and *tactical extensions* (search deeper only where capture chains are active).
**Mapping:** our certificate searches only to "depth" = bandwidth-one data (F on [0,1], [AC]); the
256-law hides its crystal structure just beyond scale 1 — a textbook horizon sacrifice. The named fixes
map 1:1 to input types: quiescence = evaluate only at "quiet" (well-separated) configurations =
a repulsion/gap input, KNOWN-OPEN [CD-V17, P1.4]; extensions = add data beyond the horizon = third
moment (P2) or beyond-1 F (P3, documented dead [M29]). **Needs:** none — a taxonomy writeup that
assigns every candidate input to the chess fix it corresponds to, so future rounds know which
"extension" each input is. **Feasibility:** immediate. **Cheapest probe:** none (documentation).
**Label:** NEW (framing; the wall it names is PROVEN [AC, M29]).

### G1.2 Endgame tablebases = exhaustive finite-T computation; the 50-move rule = the bandwidth wall — NEW (framing, P6)
**Idea:** Chess tablebases are exact by *retrograde analysis* over the finite state space; their lesson
is that exactness at finite scale is achievable and the boundary (T → ∞) is where the real structure
lives. Chess's *50-move rule* (draw if no progress in 50 moves) is a rule-boundary: no new material,
no progress. **Mapping:** our finite-T W_T computation [AF] IS a tablebase — exact linear algebra at
every finite T (tr W/N → 1, ‖W‖²/N → 1.3275, Δ(T) ~ 1/log T, TESTED-OPEN). The 50-move rule = the
bandwidth-one rule: the certificate "draws" at 68.18% because no new data is admitted past scale 1.
P6's error terms are *tablebase-to-asymptotic* extrapolation error; the two known terminal values
(0.6725, 0.6818) bracket the extrapolation. **Needs:** the [AF] data + a bracketing writeup (does the
1/log T trend interpolate between the two terminal values, or overshoot?). **Feasibility:** Low.
**Cheapest probe:** fit Δ(T) against the two terminal constants; report which bracket the data favor.
**Label:** NEW (framing of P6).

### G1.3 Opening theory = certificate families; the book deepens per target, move by move — NEW (framing)
**Idea:** Opening books are memorized optimal lines, sound against all replies *within the book*; books
are built incrementally, one line at a time, never by solving the whole game. **Mapping:** our method's
"book" = the two proven moments + integrality bookkeeping, sound against all configurations matching
them. Each new target is a new opening with the same machinery: the derivative tower ξ′, ξ″, …
[CD-V9] (mechanical, PROVEN machinery) and Dirichlet families [CD-V12] (probe-first, [lfunctions §6]).
The chess funding lesson: books grow by cheap incremental lines, not by re-solving the game — which is
exactly the catalog's allocation (V9/V12 are funded as probes [catalog §5]). **Needs:** none.
**Feasibility:** immediate. **Cheapest probe:** none (funding framing only).
**Label:** NEW (framing).

### G1.4 Zugzwang: the obligation to read only bandwidth-one data is a forced move the adversary exploits — NEW (framing of V2)
**Idea:** Zugzwang = the player who *must* move is worse off; the fix is a *waiting move* that doesn't
worsen the position. **Mapping:** the certificate MUST certify from (mean, F on [0,1], integrality) —
a forced move — and the 256-law is built to punish exactly that forced move. The "waiting move" =
the LP-dual certificate: same data, better value, the in-class gap 0.6725→0.6818 [CD-V2]. New content:
the in-class program is precisely a *waiting-move search within the forced-move class* — a chess-readable
objective for the funded V2 LP-dual solve (find any move better than Theorem D's, or prove none exists).
**Needs:** the V2 solve (already funded, [catalog §3 #1]). **Feasibility:** Med (inherits V2).
**Cheapest probe:** the N = 256 dual LP value vs 0.6725 (V2's own first step).
**Label:** NEW (framing of V2).

### G1.5 Komi/handicap: the c²·p off-line penalty is a correctly-set komi — NEW (framing)
**Idea:** In Go, komi compensates the second player and is tuned to make the game fair; a *fractional*
komi (6.5, 7.5) exists precisely to break draws. **Mapping:** the certificate's "komi" = the
multiplicity penalty it pays per off-line pair (the (1,1)-plane cost c²·p in the rank–trace bookkeeping,
[AM]). `lemmaR_tight` proves the penalty is *exactly tight* — the komi is correctly calibrated — and the
empirical all-simple world sits at Δ = 0 (zero slack, [multiplicity §4]). The *fractional* refinement:
the 0.94%·N gap 0.6725→0.6818 is the difference between the window-optimal komi and the class-optimal
komi; the LP dual is the komi readjustment. **Needs:** nothing new (folds into V2). **Feasibility:** Low.
**Cheapest probe:** none beyond V2. **Label:** NEW (framing of V2; the tightness fact is PROVEN [AM]).

### G1.6 Life-and-death: is there a LOCAL criterion certifying a zero is "alive" on the line? — KNOWN-OPEN
**Idea:** In Go, a group is *alive* if it has two eyes — a local, checkable-by-local-search criterion;
dead groups have one eye. **Mapping:** our certificate is global (W_T involves all zeros at once). A
local "alive" criterion — a provable spacing/rigidity condition in a zero's neighborhood that forces it
on-line — would be a genuinely new input type, precisely the *repulsion/gap* input the ceiling forbids
as unproven [CD-V17, P1.4]. The "two-eyes theorem" analog: "a zero with two provably-separated
neighbors cannot be off-line." **Where the analogy breaks:** Go's life-and-death is provable by *local
exhaustive search because the board is finite*; our configuration is infinite and the only proven
spacing facts are weak gap bounds — no local rigidity statement exists. **Needs:** the repulsion/gap
inventory (already [CD-V17]'s deliverable), sharpened by the specific question "what would a local
alive-criterion have to look like?" **Feasibility:** Low (scoping/documentation).
**Cheapest probe:** none — record the sharpened question inside V17's inventory.
**Label:** KNOWN-OPEN (repulsion; [CD-V17, P1.4]).

### G1.7 "The game is won in the opening" (Weil's criterion): the certificate is opening theory, RH is the whole game — NEW (framing)
**Idea:** Some games are decided by opening principles; Weil's criterion says RH ⟺ the Weil form is
positive on ALL test functions. **Mapping:** the certificate plays a *finite* set of lines (the finite
compression W_T); RH is the demand that *every* line wins. The method's entire power is bounded by what
opening theory (finitely many test functions) can achieve against an adversary who knows the whole book.
The 256-law is the opponent who has memorized the book and plays its best reply. **Where it breaks:**
this is a restatement, not a mechanism — but it states *why* the ceiling is a certificate-class fact
(PROVEN [AC]) and *why* new data, not deeper opening theory, is the only exit (matches [CD-§0]'s map).
**Needs:** none. **Feasibility:** immediate. **Cheapest probe:** none (documentation).
**Label:** NEW (framing).

---

## Pool 2 — Poker / imperfect information games

### G2.1 CFR / regret matching as the certificate-search algorithm: the in-class gap IS exploitability — NEW (algorithm for V2)
**Idea:** Poker's GTO strategies are computed by *counterfactual regret minimization* (CFR, CFR+):
iterate best responses, accumulate regrets, and converge to a Nash equilibrium whose *exploitability*
→ 0; the method is battle-tested on exactly the "minimize the adversary's guaranteed gain" objective.
**Mapping:** our game is zero-sum: certificate (choose the majorant r) vs configuration-adversary
(choose a marked configuration matching the two moments + integrality); payoff = certified on-line
fraction. The certificate's exploitability = 0.6818 − 0.6725 = 0.94%·N — the in-class gap. CFR's
machinery (regret matching / multiplicative weights over the stability-inequality constraint set [AC])
is a route to the LP-dual certificate [CD-V2] that needs **no LP solver** and produces *rational
iterates with explicit convergence* — Lean-friendly, unlike a black-box LP optimum. **Needs:** the
N = 256 stability inequality as the game's constraint; a small MWU loop (Rust/Python, minutes).
**Feasibility:** High — this is V2's target with a triangulating algorithm and an audit metric.
**Cheapest probe:** run MWU at N = 256; report the converged value vs 0.6725 (Theorem D unexploitable?)
and vs 0.6818.
**Label:** NEW (algorithmic; supports funded V2).

### G2.2 Bluffing and information asymmetry: the 256-law is a bluff the certificate cannot call — NEW (framing)
**Idea:** A bluff succeeds exactly when the caller's information cannot refute it; poker strategy is the
management of exactly this asymmetry. **Mapping:** the crystal emits F ≡ 1 on [0,1] — it *looks*
GUE-like (honest) while hiding its crystal structure past scale 1; the certificate holds only
(mean, F-on-[0,1], integrality) and cannot see through it. The ceiling theorem (PROVEN [AC]) is the
formal statement that this bluff is *uncallable within the class*. **Where it breaks:** in poker the
caller can buy more information (call a bet); here, more information is exactly the unproven/dead input
[P3 = M29]. **Needs:** nothing new. **Feasibility:** immediate.
**Cheapest probe:** none (framing). **Label:** NEW (framing).

### G2.3 Multi-street betting: each moment order is a new street of information — NEW (framing of V3/V4)
**Idea:** Poker information arrives street by street (flop, turn, river); strategies re-evaluate at each
street, and the *value of the next street* is priced before paying for it. **Mapping:** the certificate's
"streets" are the moment orders: street 2 (mean, pair — current, PROVEN), street 3 (tr Â³ — the P2
input, unconditionally evaluable at λ < 2/3 [CD-V3]), street 4 (HL*-conditional, → 13/18 [AM]). The
poker question "is the next street worth its price?" = the V4 moment-order capacity LP [CD-V4] — what
each conjectural input is worth. New content: a *pre-registered street-pricing rule* — fund the third
moment iff the costly-signal test (G4.2) shows the crystal cannot fake it. **Needs:** the [CD-V3]/[P6.5]
LP and G4.2's S₃ run. **Feasibility:** Med (inherits V3/V4). **Cheapest probe:** G4.2's S₃
computation first (hours). **Label:** NEW (framing of funded V3/V4).

### G2.4 Ranges: the certificate plays the range, not the hand — NEW (framing)
**Idea:** Poker players evaluate *ranges* (all hands consistent with the betting), not specific hands;
robustness = worst-case value over the range. **Mapping:** the certificate must be valid for ALL
configurations matching the two moments — it plays the range. The adversary *range-reduces us*: it picks
the worst configuration against our specific certificate — that is the LP dual [CD-V2]. The 256-law is
the range's equilibrium hand; the certificate's robustness is its worst-case value. **Needs:** nothing
new. **Feasibility:** immediate. **Cheapest probe:** none (framing; the LP dual is V2).
**Label:** NEW (framing).

### G2.5 Pot odds and implied odds: the cost of each new input vs its payoff — NEW (framing, folds into V4)
**Idea:** Call only when pot odds beat win probability; *implied odds* = future-street earnings.
**Mapping:** the certificate's "pot" = the certified constant gain; its "call" = the analytic cost of a
new input (third moment: diagonal evaluation, cheap; beyond-1 F: dead [M29]; repulsion: no proof in
sight); "implied odds" = the roadmap it unlocks (13/18 → 1 [AM]). The V4 capacity curve IS the pot-odds
table. **Needs:** V4's curve. **Feasibility:** Low–Med. **Cheapest probe:** V4's runs.
**Label:** NEW (framing, folds into V4).

### G2.6 Bankroll / long-run profitability: the almost-everywhere certificate — NEW (overlaps P9.1; TESTED-OPEN status inherited)
**Idea:** A poker player can be profitable in the long run despite real downswings; the *variance* of
results is not the *mean* edge. **Mapping:** the certificate's finite-T value fluctuates (Δ(T) ~ 1/log T
with sample wiggle [AF]); the *mean* structure is the wall ([CD-A1]: variance is irrelevant, the mean is
Hardy–Littlewood-strength), but fluctuations ARE controllable (Selberg-CLT-type inputs). A "long-run"
certificate — "≥ 0.6725 for all T outside a density-zero set" — is a genuinely different target type
from the pointwise one, supportable by fluctuation bounds the pointwise statement cannot use.
**Where it breaks:** the sports/poker "long-run" intuition is exactly P9.1's a.s. certificate (physics
catalog); no new input, a new *target type*. **Needs:** var(Δ(T)) over adjacent T-windows (existing
[AF] data). **Feasibility:** Low (analysis of existing data). **Cheapest probe:** measure
var(Δ(T)) over windows; report the fluctuation exponent (1/T? 1/log T?).
**PROBE RUN (2026-08-11, code-backed):** the block-variance companion of `tools/hot_hand_calib.py`
(same command, same results file): split the 10⁴ zeros into 10 windows of 1000 and the GUE
null into 24 replicates; per-block F̂ spread at α∈{0.5,0.9,1.1,1.5,2.0}: zeta 0.709±0.101 /
0.970±0.134 / 1.558±0.537 / 0.999±0.061 / 0.970±0.125 vs GUE 0.763±0.064 / 0.939±0.105 /
1.015±0.159 / 0.943±0.097 / 0.988±0.114. At α≥1.5 the zeta block variance is fully
consistent with the sine-kernel null (no extra "luck"); the only excess variance sits at
α=1.1 where the arithmetic feature lives (zeta block mean 1.558, 3.4× the null's std) —
see G3.1's probe. The "luck" (fluctuation) budget is therefore null-consistent away from
the α≈1 arithmetic feature; no extra variance that could be harvested.
**Label:** NEW (framing of P9.1; fluctuation measurement now CHECKED NUMERICALLY [hot_hand_calib.py]).

### G2.7 Exploitability audit of Theorem D: know the leak before funding the fix — NEW (audit)
**Idea:** Poker discipline: quantify your exploitability before paying to fix it. **Mapping:** the single
number that decides the in-class program = the exploitability of Theorem D's certificate against the
worst admissible configuration = the LP-dual value (V2's DoD [catalog §3 #1]). If it equals 0.6725,
Theorem D is unexploitable (class-optimal) and the 0.6818 ceiling is unreachable by smooth certificates
— a documented finding; if it exceeds 0.6725, we hold a real constant gain. **Needs:** V2's LP solve.
**Feasibility:** High (same as V2). **Cheapest probe:** G2.1's MWU run doubles as this audit.
**Label:** NEW (same target as V2, audit framing).

---

## Pool 3 — Sports analytics

### G3.1 "Hot hand" calibration: is the empirical beyond-1 F decay real or finite-sample artifact? — NEW (probe; the underlying measurement is TESTED-OPEN [verif-001 §4])
**Idea:** The hot-hand debate's lasting lesson: aggregate/conditional statistics carry built-in selection
bias — Miller–Sanjurjo showed the naive "P(make | made previous shot)" statistic is *negatively biased*,
so a null effect can *look like* a real one (or vice versa) from the raw data alone. **Mapping:**
verif-001's empirical F̂(α) climbs to ≈ 0.93–1.0 near α = 1 then *decays beyond*, with large sample noise
at N = 3000 [verif-001 §4]. The hot-hand question, transplanted: *does the same estimator decay on a
process with F ≡ 1 exactly?* **New content (TESTABLE):** sample the sine-kernel process (known F ≡ 1),
compute the SAME normalized pair-count statistic at the same N and α-grid; if the sine-kernel
finite-sample curve shows the same "climb-then-decay" shape, the ζ-data decay is an artifact and there
is **no empirical hint against Montgomery (F = 1 beyond 1)** — changing what we believe about P3's
empirical status, and neutralizing any future "the data already show a decay" argument. **Needs:** a
sine-kernel sampler (rejection/determinantal, N ~ 3000) + the verif-001 estimator code.
**Feasibility:** High (Rust/Python, well under an hour). **Cheapest probe:** the sine-kernel
finite-sample F̂(α) curve vs the ζ-data curve, same bins.
**Label:** NEW (probe; null-model calibration — the GVT lesson applied to our own statistic).
**PROBE RUN — see §Round-2 R-1** (script `tools/hot_hand_calib.py`, results
`tools/data/hot_hand_calib_results.json`): no monotone decay beyond α=1 (verif-001 §4's "decay" not
reproduced by the standard pair-correlation estimator); a sharp, sample-dependent, zeta-specific
structure near α∈[1.0,1.3] (α=1.10 value flips 0.84→1.55 between N=3000 and N=10000, +11.6σ vs the
null) consistent with finite-height arithmetic corrections — cause not established (follow-up:
τ-bin/prime decomposition at higher height).

### G3.2 xG calibration: the certificate is an underconfident scoring model — NEW (framing of V7)
**Idea:** Expected-goals models must be *calibrated*: do predictions match realized rates? An
underconfident model wastes known structure. **Mapping:** the certificate "predicts" ≥ 0.6725 on-line;
reality scores ≈ 100% (10¹³ verified zeros on the line, [CD-W2]). The calibration gap 67–68% vs 100%
is model-lossiness (a certificate-class information limit), not mismeasurement — exactly what the V7
method-sandbox tests ([CD-V7]: certificate value on RH-true vs RH-false worlds decides whether the
method or the arithmetic is the bottleneck). **Needs:** V7's runs (reuse V1/[AF] code).
**Feasibility:** Med (inherits V7). **Cheapest probe:** V7's RH-true-world certificate value vs 0.6725.
**Label:** NEW (framing of V7).

### G3.3 Bradley–Terry → Plackett–Luce: pairwise models need a higher-order upgrade — NEW (framing of V3/V4)
**Idea:** Bradley–Terry models *pairwise* comparisons; Plackett–Luce generalizes to rankings of k items;
the ratings literature's rule is to pay for the higher-order model only when pairwise residuals show
structure. **Mapping:** the certificate's two moments are the "pairwise" model; the third moment is the
"k-wise" upgrade ([CD-V3], [P6.5] two-window λ=1 + λ=1/2). The checkable version of "do residuals show
structure": does pinning S₃ move the ceiling (V4)? If the 256-law's S₃ already equals the GUE value
(cheap talk — G4.2), the upgrade is worthless *for this adversary* — a clean negative that resets P2's
priority. **Needs:** V4's run. **Feasibility:** Med. **Cheapest probe:** G4.2's S₃-of-the-crystal
computation. **Label:** NEW (framing of V3/V4).

### G3.4 Luck/skill decomposition: the finite-T fluctuations are luck; the constant gap is skill — KNOWN-DEAD (as a route; live fragment = G2.6)
**Idea:** Sports analytics splits observed variance into luck and skill (Noll–Scully): with enough
observations luck averages out, but a skill (mean) gap persists. **Mapping:** the certificate's
finite-T wiggle (Δ(T) ~ 1/log T, sample noise [AF]) is "luck" (Selberg-CLT-governed fluctuations); the
asymptotic gap 0.6725→~1 is "skill" (mean structure). The transferable rule: *you cannot harvest skill
from luck* — no finite-T refinement closes a mean gap. This is the [CD-A1] death (variance is
irrelevant; the mean is the Hardy–Littlewood wall) in sports language, plus a *no-fund signal* for any
"better finite-T constants" idea. **Live fragment:** the a.s./long-run variant (G2.6 / P9.1) is the only
luck-based statement with value. **Needs:** none. **Feasibility:** immediate.
**Cheapest probe:** none (documented no-fund; cross-ref [CD-A1], P9.1).
**Label:** KNOWN-DEAD (as a constant-improving route); the a.s. fragment is NEW (G2.6).

### G3.5 Elo / PageRank: the certificate as the fixed point of a consistency iteration — NEW (framing; computational content already in V1)
**Idea:** Rating systems are fixed points of consistency equations computed by iteration; PageRank is
the principal eigenvector of a Markov matrix — an *iterative eigenvalue* method. **Mapping:** the
explicit formula is the consistency equation (prime-side moments ⟷ zero-side moments); the finite-T
certificate value is the fixed point's shadow. New content: (a) the fixed-point reading of Δ(T)'s
1/log T approach [AF] as an iteratively-converged object — the *rate of convergence* of the
"certificate iteration" is a measurable P6 object; (b) the isospectral-invariance point (physics
P1.5): no iteration can beat the two-moment fixed point, so iteration is a *computation* route, never
an *input* route. **Needs:** [AF]/V1 code. **Feasibility:** Low.
**Cheapest probe:** fit Δ(T)'s approach rate; compare with power-iteration convergence on W_T.
**Label:** NEW (framing; no new input — matches P1.5).

### G3.6 Clutch performance: the low-lying zeros are the "clutch" sample — NEW (framing; kill already recorded in CD-W2)
**Idea:** Clutch = performance in high-leverage moments; the literature mostly finds no clutch effect —
tested-sample performance does not license extrapolation. **Mapping:** our "clutch" sample = the
low-lying zeros (verified to 10¹³, all on the line); the asymptotic regime is untested. The clutch
lesson, applied: the verified 100% on-line-ness is a finite sample with *no statistical license to the
limit* — this is [CD-W2]'s kill ("a finite measurement cannot enter a liminf statement") stated as an
honesty reminder against "reality is ≈ 100%" arguments. **Needs:** none. **Feasibility:** immediate.
**Cheapest probe:** none (records the already-documented kill). **Label:** NEW (framing of CD-W2's kill).

### G3.7 Moneyball: new metrics break market inefficiency — NEW (framing)
**Idea:** The statistical revolution found underpriced skills by *inventing new metrics*; markets stay
inefficient until the metric exists. **Mapping:** the certificate class is "inefficient" (certifies
0.6725 against a ~1.0 reality) until a new input (metric) is invented. The efficient frontier for the
certificate = the V4 moment-order capacity curve; each metric (third moment, beyond-1 F, repulsion)
moves the frontier by a *priced* amount. New content: a "metric-invention roadmap" sorted by invention
cost — third moment (cheapest: diagonal evaluation at λ < 2/3 [CD-V3]), beyond-1 F (dead [M29]),
repulsion (no proof in sight [CD-V17]). **Needs:** V4's curve. **Feasibility:** immediate.
**Cheapest probe:** none beyond V4. **Label:** NEW (framing).

### G3.8 Strength of schedule: the moments' "opponents" are the primes; error terms are schedule effects — NEW (framing of V20)
**Idea:** SOS adjusts a team's stats for the strength of its opponents; honest stats are
schedule-adjusted. **Mapping:** the certificate's moments are computed against the primes; the error
terms (Montgomery–Vaughan constant, Stirling, Chebyshev errors) are the "schedule adjustment." The
effective finite-T theorem ([CD-V20], explicit E(T)) is the schedule-adjusted team stat — the honest
companion to the asymptotic constants. New content: a framing that makes [CD-V20]'s deliverable
readable as "the certificate's adjusted rating," and a check that the [M29] measured tolerance
violations (3.6·10³–3.7·10⁴×) are the "unadjusted" error the schedule correction would have to remove
(they are — it cannot). **Needs:** [CD-V20]'s assembly. **Feasibility:** Low.
**Cheapest probe:** none (framing of V20). **Label:** NEW (framing of V20).

---

## Pool 4 — Game theory / mechanism design

### G4.1 Strategyproof impossibility: the ceiling is a Gibbard–Satterthwaite-style theorem — NEW (framing of the PROVEN ceiling [AC])
**Idea:** GS: no non-dictatorial strategyproof social-choice function exists; Myerson–Satterthwaite:
no efficient + budget-balanced + individually-rational bilateral trade exists. Impossibility theorems in
mechanism design are *information bounds*, not search bounds: no cleverness within the type space can
beat them, and the only fix is enlarging the type space. **Mapping:** the certificate is a mechanism
reading the report space (mean, F-on-[0,1], integrality); the 68.18% ceiling is the impossibility
theorem for this report space (PROVEN [AC]) — no certificate, however clever, exceeds it. The fix is
the type space: ask for the third moment. **Where it breaks:** mechanism-design impossibilities have
constructive proofs via explicit manipulation; our ceiling is a *proven* extremal configuration, the
same kind of object. **Needs:** nothing new. **Feasibility:** immediate.
**Cheapest probe:** none (framing of [AC]). **Label:** NEW (framing; the ceiling is PROVEN).

### G4.2 Costly signaling: is the third moment a signal the crystal cannot fake? — NEW (decision rule for V4/P2)
**Idea:** A signal is informative iff it is *costly to fake*; cheap talk is uninformative. **Mapping:**
the two moments are cheap talk — the 256-law emits them identically to reality (F ≡ 1 on [0,1], [AC]).
The third moment's informativeness = whether the crystal's three-point statistic S₃ differs from the
GUE value S₃ = 2 (sine-kernel; PROVEN-conditional / available at λ < 2/3 by the diagonal method
[CD-V3], [P6.5]). **New content (pre-registered decision rule for P2):** compute S₃ of the 256-marked
periodic law first (hours). If S₃(crystal) = 2 (GUE), the third moment is *cheap talk for this
adversary* — the crystal fakes it — and P2's priority drops (the V4 run will show the ceiling
unmoved); if S₃(crystal) ≠ 2, the signal is costly and the wall may move — fund V3 hard. This is V4's
first step with the interpretation attached *before* the run, so the negative is a finding, not a
disappointment. **Needs:** the 256-law's triple-correlation statistic (from `Zeta23/PairCeiling/
LawN256.lean` / `NearCUE.lean`). **Feasibility:** High (hours). **Cheapest probe:** the S₃ computation.
**Label:** NEW (reframing of V4 with a decision rule; the "law's S₃ vs GUE" question is the open one
[P4.1-physics]).

### G4.3 Incentive design: P1's missing constraint is a missing "tax" — NEW (framing of V2/P5.1)
**Idea:** Mechanism design aligns incentives by *adding a tax* (a penalty on undesired behavior) that
good agents don't pay and bad agents can't avoid. **Mapping:** P1's "missing constraint" is exactly a
missing tax: a penalty on off-line configurations that the real zeros satisfy and the crystal violates.
The LP-dual certificate [CD-V2] IS the optimal tax — its dual variables are shadow prices (physics
P3.3's "defect chemical potential"; the equilibrium-measure shape predicted by physics P5.1's contact
set). New content: P1 restated as "find the incentive-compatibility clause"; the search is V2's LP dual;
the mechanism-design vocabulary predicts the optimal tax's *form* (a barrier/contact-set majorant), not
just its value. **Needs:** V2's solve. **Feasibility:** Med (inherits V2/P5.1).
**Cheapest probe:** the dual variables of the N = 256 LP; plot r(x), look for contact-set structure.
**Label:** NEW (framing of V2).

### G4.4 Nash equilibrium of certificate-vs-configuration: the game value is between 67.25 and 68.18 — NEW (framing of V2)
**Idea:** Zero-sum game theory: minimax = LP duality; a strategy's *ε-equilibrium quality* = its
exploitability. **Mapping:** the game: certificate chooses r ∈ C¹[0,1], adversary chooses a marked
configuration matching the moments; payoff = certified on-line fraction. The game value = the class
ceiling 0.6818 (upper bound PROVEN [AC]); Theorem D's certificate is an ε-equilibrium with
ε = 0.0093·N (exploitability, G2.1). The adversary's equilibrium strategy (the 256-law) is already
found; the remaining work is the certificate's best response — V2. **Needs:** V2. **Feasibility:** Med.
**Cheapest probe:** V2's dual value (the game value's lower bound). **Label:** NEW (framing of V2).

### G4.5 Revelation principle: the certificate is a dominant-strategy direct mechanism — NEW (framing)
**Idea:** The revelation principle: any mechanism's outcome is achievable by a *truthful direct*
mechanism; robustness means validity against all reports. **Mapping:** the certificate is direct (reads
raw moments) and must be valid for every admissible report (dominant-strategy). The 256-law is a
"non-truthful" report: correct moments, hidden off-line structure. The ceiling (G4.1) = the
impossibility of dominant-strategy implementation of 100% on this report space. **Where it breaks:** in
mechanism design, the principal can sometimes *verify* reports ex post; the certificate can never verify
the hidden structure (no beyond-1 data, [M29]). **Needs:** none. **Feasibility:** immediate.
**Cheapest probe:** none (framing). **Label:** NEW (framing).

### G4.6 Stable matching / blocking pairs: off-line pairs are blocking pairs of the FE involution — NEW (framing, near-WILD)
**Idea:** Gale–Shapley's deferred acceptance stabilizes matchings by *rejecting blocking pairs*.
**Mapping:** the functional equation pairs ρ ↔ 1−ρ̄ — a perfect matching ("the FE involution"); a pair is
"blocking" for the certificate's positivity exactly when it sits off-line (its (1,1)-plane is the
positivity-blocking structure [AM]). The certificate cannot reject blocking pairs — it can only *pay*
(the c²·p penalty, G1.5). **Where it breaks:** deferred acceptance works because preferences are
known; the certificate cannot even *identify* which pairs block without the very data it lacks.
**Needs:** none. **Feasibility:** immediate. **Cheapest probe:** none (vocabulary-level; keep as
framing, do not fund). **Label:** NEW (framing; low value, near-WILD).

---

## Pool 5 — Random-element board games / Markov chains

### G5.1 Absorbing chains: RH = no absorption off the line; the certificate counts recurrent states — NEW (framing)
**Idea:** In an absorbing Markov chain, states are transient (eventually leave) or recurrent (return
a.s.); the stationary structure is the recurrent class. **Mapping:** a zero's "state" = on-line
(recurrent) or off-line (transient, would leave). RH = every zero state is recurrent. The certificate
counts recurrent states from scale-1 transition data (the two moments); the 256-law's off-line pairs
are transient states that the scale-1 data cannot distinguish from recurrent ones. **Where it breaks:**
there is no actual chain (no transition law) — the vocabulary is a mnemonic for "the certificate is a
recurrence-counting statistic," and the ceiling says recurrence cannot be certified beyond 68.18% from
scale-1 data. **Needs:** none. **Feasibility:** immediate. **Cheapest probe:** none (framing).
**Label:** NEW (framing).

### G5.2 Hitting times: the first off-line zero — NEW (framing; content in CD-W2)
**Idea:** Hitting-time analysis asks when a process first enters a bad region. **Mapping:** RH = the
hitting time of the off-line region is infinite; the verified data (10¹³ zeros) = no hits observed; the
extremal law hits immediately (its crystal structure is off-line at every period). The finite-T runs
[AF] measure the hitting-time evidence (none). **Where it breaks (honest):** the hitting-time statistic
(first off-line height) is a KNOWN-OPEN target with *no certificate relevance* — a finite sample cannot
license the infinite hitting time ([CD-W2]'s kill). **Needs:** none. **Feasibility:** immediate.
**Cheapest probe:** none (records CD-W2's kill in game language). **Label:** NEW (framing of CD-W2).

### G5.3 Stationarity = the plateau: the beyond-1 region is the stationary regime — KNOWN-OPEN (no-fund signal for P3 within the class)
**Idea:** In stochastic processes, transient dynamics relax to a stationary regime; in SFF theory the
plateau (F ≡ 1 for α > 1) is the stationary regime and the ramp (α < 1) the transient. **Mapping:** the
zeros' conjectured mixing time is O(1) (F ≡ 1 beyond 1, Montgomery); the proven part is only the
transient regime (bandwidth 1). The honest transfer: *stationarity is exactly the beyond-1 region, and
no finite-rank (per-T, scale-1) argument reaches it* — the physics P2.4 exactness point restated in game
language. **Needs:** none. **Feasibility:** immediate.
**Cheapest probe:** none (no-fund signal; the class route is closed by [M29]).
**Label:** KNOWN-OPEN (as input; [M29] closes the class route).

### G5.4 Snakes-and-ladders exactness: finite board = exact linear algebra; the structure lives at the boundary — NEW (framing of P6)
**Idea:** Snakes-and-ladders is exactly solvable by inverting a finite transition matrix; the "snakes"
(backward jumps) are local structure the coarse transition data barely reveal. **Mapping:** the zeros'
finite-T certificate is the same: exact W_T linear algebra at every T [AF]. The transferable lesson:
exact solvability at finite scale does not license the infinite limit — the structure (the "snakes" =
the pair-correlation beyond scale 1) lives at the boundary. P6's error terms are finite-board-to-
infinite-board extrapolation; the measured 1/log T trend [AF] is the finite-size correction.
**Needs:** [AF] data. **Feasibility:** Low. **Cheapest probe:** fit the [AF] trend; report the
extrapolated limit vs 1.3275. **Label:** NEW (framing of P6).

### G5.5 Backgammon's doubling cube: the gap as a double-or-resign decision — NEW (framing, low value)
**Idea:** The doubling cube converts the underlying game into a risk decision: double when equity
exceeds a threshold; opponent accepts (plays for double) or resigns (pays the current stake).
**Mapping:** the certificate's "double" = certify 0.6818 (the ceiling); the opponent "accepts" if the
data support it (the LP dual reaches the ceiling — a real gain) or the position "resigns" if Theorem D
is class-optimal (the gap is irreducible). The position's equity = the LP-dual value (V2).
**Where it breaks:** the cube's correct play depends on *win probability*, which we are trying to
compute — circular; the content reduces to V2. **Needs:** V2. **Feasibility:** immediate.
**Cheapest probe:** none beyond V2. **Label:** NEW (framing; low value, near-WILD).

### G5.6 Propp–Wilson / coupling from the past: exact sampling of the stationary regime — KNOWN-OPEN (obstruction documented in M29)
**Idea:** CFTP samples *exactly* from a Markov chain's stationary distribution by running chains from
the past until coalescence — exactness without bias, at the price of needing the coupling to actually
coalesce. **Mapping:** exact evaluation of the zeros' beyond-1 correlations = "running from the past"
(the prime side) until the scale-1 data coalesce into beyond-1 data — an exact transition from scale 1
to the plateau. **Where it breaks:** the coalescence time (the mixing scale, G5.3) is conjectural; and
the exact transition is precisely what M29 showed is unavailable (every proven bound misses the
tolerance by 3.6·10³–3.7·10⁴× [M29]). **Needs:** none. **Feasibility:** immediate.
**Cheapest probe:** none (records the documented obstruction in sampling language).
**Label:** KNOWN-OPEN (obstruction documented [M29]).

### G5.7 Palm / regenerative structure: situational statistics conditioning on a zero at the origin — NEW (framing of V3)
**Idea:** In point-process statistics, the *Palm measure* conditions on a point at the origin; the
pair correlation IS the Palm intensity and the triple correlation is the second-order Palm intensity.
**Mapping:** the certificate's upgrade path (two moments → three moments) is literally a Palm-order
upgrade: tr Â³ is second-order Palm data [CD-V3]. The games framing: "situational statistics" — the
third moment conditions on two reference zeros, exactly as Palm conditions on one. New content: the P2
input is cleanly identified as second-order Palm data, which makes its unconditional availability at
λ < 2/3 ([CD-V3]'s claim) the *cheapest* Palm order available — a reason to run [P6.5]'s two-window LP
before any harder input. **Needs:** the [CD-V3]/[P6.5] LP. **Feasibility:** Med (inherits V3).
**Cheapest probe:** G4.2's S₃ computation (the Palm-order-2 value of the crystal).
**Label:** NEW (framing of V3).

---

## TOP 10 (EV × feasibility × cheap-probe)

1. **G3.1 — Hot-hand calibration of the empirical F̂(α)** (NEW, probe — **RUN, see §Round-2**). Sine-kernel
   finite-sample F̂ vs the ζ-data "climb-then-decay" trend [verif-001 §4]. Settles whether there is ANY
   empirical hint against Montgomery beyond 1 — a P3-status diagnostic, <1h, changes what we believe.
   Result: no monotone decay beyond α=1 (artifact); sharp α≈1 finite-height arithmetic feature found.
2. **G3.1-followup — τ-bin/prime decomposition of the α≈1 feature** (NEW, next probe). The probe found
   a sharp, sample-dependent zeta-specific structure near α∈[1.0,1.3] (α=1.10 value 1.55 at N=10000,
   +11.6σ vs the null), consistent with prime-side corrections; decompose by τ-bin / candidate
   resonance (log 2, log 3) and test height-dependence with higher-height zeros. Cheap, real, open.
3. **G2.6 — Bankroll: the almost-everywhere certificate** (NEW, overlaps P9.1; block variance RUN). A
   genuinely different target type — "≥ 0.6725 for all T outside a density-zero set" — supportable by
   fluctuation control where the pointwise statement cannot be. Block-variance data recorded (null-
   consistent at α≥1.5; excess only at the α≈1 arithmetic feature). The a.s. target itself remains
   open.
4. **G4.2 — Costly-signal test** (NEW decision rule — **CLOSED by `attack-twobandwidth.md`**): the
   third moment is cheap talk for the extremal world (tr³ = 2N at λ=1 matches GUE); at λ<2/3 the cubic
   construction ≤ 0.8071 < 5/6. P2 downgraded; record the closure.
5. **G2.1/G2.7 — Exploitability of Theorem D** (NEW algorithm/audit — **CLOSED by `attack-lpdual.md`**):
   the in-class optimum 0.68183123 is attained; Theorem D suboptimal; shadow price of p₁ = 1. The
   exploitability question is answered; do not re-fund.
6. **G3.3 — Bradley–Terry → Plackett–Luce: the moment-order upgrade path** (NEW, framing of V3/V4).
   The "is the higher-order model worth it" decision = the V4 capacity curve; the third-moment order is
   now decided negative (item 4), the 4th-moment order (m₄(1) = 13/4, HL* → 13/18) is the remaining
   priced step.
7. **G1.4 — Zugzwang: the waiting-move search** (NEW, framing of V2 — superseded). The in-class gap is
   precisely the search for a better move with the same forced data; the LP-dual already found the
   waiting move (0.68183123). Read as history.
8. **G4.1 — Impossibility framing** (NEW, framing of the PROVEN ceiling [AC]). Why no in-class
   cleverness can win (information bound, not search bound); a no-fund signal for in-class algorithmic
   gymnastics beyond V2, and a justification for the type-space fix (third moment — itself now
   decided negative, item 4).
9. **G1.2 — Tablebase/50-move framing of P6** (NEW, framing). The finite-T certificate is an exact
   tablebase; the 1/log T trend [AF] is tablebase-to-asymptotic extrapolation, bracketed by the two
   known terminal values. Probe: fit Δ(T) against both terminal constants.
10. **G1.6 — Life-and-death: what a local rigidity criterion must look like** (KNOWN-OPEN, scoping).
    The "two-eyes theorem" = a local, provable criterion for on-line-ness = a repulsion input; sharpens
    [CD-V17]'s inventory with a specific question instead of a survey.
11. **G5.3/G5.6 — Stationarity no-fund signals** (KNOWN-OPEN). The beyond-1 region is the stationary
    regime, unreachable by any finite-rank argument ([M29]); prevents re-funding P3 within the class.

**Strategic reading (updated 2026-08-11):** the games catalog's genuinely NEW contributions are (i) the
hot-hand calibration probe (G3.1) — RUN: the apparent beyond-α=1 "decay" is a measurement artifact
(null-calibrated curve is flat ≈1), and a sharp zeta-specific α≈1 feature was found (the next probe);
(ii) the block-variance "luck" measurement (G2.6) — RUN: null-consistent at α≥1.5, excess only at the
α≈1 arithmetic feature; (iii) the a.s./bankroll target type (G2.6) — still open; (iv) the
impossibility/cheap-talk framings (G4.1, G4.2) — G4.2's decision is now decided in the negative by
`attack-twobandwidth.md` (third moment is cheap talk; 5/6 wall stands). Two catalog targets were closed
by other round-2 agents and are recorded here as history, not open routes: the in-class gap
(G2.1/G2.7, closed by `attack-lpdual.md`: 0.68183123 attained) and the third-moment distinct wall
(G4.2/G5.7, closed by `attack-twobandwidth.md`). The persistent wall — beyond-1 F, repulsion — appears
in game language as the *bluff the certificate cannot call* (G2.2) and the *stationary regime no
finite-rank argument reaches* (G5.3). Nothing here claims to settle RH; the honest output is a ranked
set of probes whose negatives are documented findings, per hooks/agents.md.

---

## WILD section (deliberately absurd premises, honestly evaluated; each labeled)

### W-G1. "The gap 67.25→68.18 is a doubling-cube decision: double when your equity clears the threshold" — NEW (vocabulary; reduces to V2)
**For:** the equity of the position = the LP-dual value; the correct cube play is a clean decision rule.
**Against:** the cube's correct play depends on win probability, which is the object we are computing —
circular; the content is V2's solve wearing a cube. **Keep:** nothing beyond the equity metaphor.
**Label:** NEW (framing; do not fund beyond V2).

### W-G2. "Deferred acceptance: reject blocking pairs and the certificate stabilizes at 100%" — NEW (vocabulary; KNOWN-DEAD as a route)
**For:** off-line pairs are blocking pairs of the FE involution (G4.6); rejection would eliminate them.
**Against:** the certificate cannot even identify which pairs block without the beyond-1 data it lacks
([M29] documented); Gale–Shapley's preferences have no analog. **Keep:** the "blocking pair = (1,1)
plane" image as a mnemonic only. **Label:** NEW (framing; do not fund).

### W-G3. "Coupling from the past: sample the plateau exactly" — KNOWN-OPEN (obstruction documented [M29])
**For:** CFTP gives exact stationarity samples without bias — the beyond-1 dream in one algorithm.
**Against:** the coalescence time is the conjectural mixing scale (G5.3), and the exact scale-1→plateau
transition is the documented M29 negative (tolerance missed by 3.6·10³–3.7·10⁴×). **Keep:** the
"coalescence = the scale where F ≡ 1 is forced" phrasing as a mental model. **Label:** KNOWN-OPEN.

### W-G4. "The 256-law is a rent-extracting monopolist under regulation; the certificate is the regulator with only the filings" — NEW (vocabulary; content = V2's dual)
**For:** the adversary maximizes off-line "rent" subject to the regulatory constraints (the moments) —
the LP is the regulation, the dual variables are the regulator's audit weights; a clean picture of the
LP-dual (G4.3).
**Against:** the regulator cannot subpoena the books (no beyond-1 data); the "optimal audit rule" is V2
renamed. **Keep:** the regulator/audit image for P1's "missing constraint = missing tax" (G4.3).
**Label:** NEW (framing; do not fund beyond V2).

### W-G5. "RH is the claim that the zeros never fold; the certificate is the caller with a capped stack" — NEW (vocabulary)
**For:** the all-in/caller image captures the worst-case robustness of the certificate (G2.4) and the
finite information (capped stack = bandwidth-one data).
**Against:** pure vocabulary; no mechanism. **Keep:** nothing. **Label:** NEW (framing; discard).

### W-G6. "The zeros are a constraint-satisfaction puzzle (Sudoku-style): the moments are clues, and the crystal is a second solution the puzzle-setter must exclude" — NEW (vocabulary; content = G4.3/P6.2)
**For:** CSP with incomplete clues has multiple solutions (the crystal is the "other solution"); the
certificate is a puzzle solver that cannot break the tie; P1's missing constraint = the missing clue.
**Against:** this is the aliasing/undersampling reading of the compression ([CD-§3], physics P6.2)
renamed; no new constraint appears. **Keep:** the "missing clue" phrasing for P1. **Label:** NEW
(framing; content already in physics P6.2 / G4.3).

---

## Label inventory

- **NEW** (invented here, each with a cheapest-first probe or a kill/decision rule): G1.1, G1.2, G1.3,
  G1.4, G1.5, G1.7, G2.1, G2.2, G2.3, G2.4, G2.5, G2.6, G2.7, G3.1, G3.2, G3.3, G3.5, G3.6, G3.7,
  G3.8, G4.1, G4.2, G4.3, G4.4, G4.5, G4.6, G5.1, G5.2, G5.4, G5.5, G5.7, W-G1 … W-G6.
- **KNOWN-DEAD** (death documented elsewhere; recorded here as a no-fund signal): G3.4 (luck/skill as a
  constant route = [CD-A1]'s death restated; the live fragment is G2.6/P9.1), W-G2 (as a route).
- **KNOWN-OPEN** (core is a known open problem or already flagged): G1.6 (repulsion/local rigidity;
  [CD-V17], P1.4), G5.3 (stationarity/beyond-1; [M29] closes the class route), G5.6 (CFTP/plateau;
  [M29]), W-G3.
- **TESTED-OPEN** (numerically probed, conclusion not final): G1.2/G5.4 rest on [AF]'s measured
  Δ(T) > 0, ~1/log T (the trend, not the asymptote).
- **CHECKED NUMERICALLY (2026-08-11, code-backed):** G3.1's probe (no monotone decay beyond α=1;
  sharp α≈1 arithmetic feature; script `tools/hot_hand_calib.py`, results
  `tools/data/hot_hand_calib_results.json`, command `uv run --quiet --with numpy --with scipy python
  tools/hot_hand_calib.py`); G2.6's block-variance measurement (same script; null-consistent at
  α≥1.5, excess only at the α≈1.1 arithmetic feature). These vectors are now resolved-in-part and
  their status recorded in the Round-2 execution section below.
- **CLOSED BY OTHER AGENTS (2026-08-11, cross-referenced):** G2.1/G2.7 (in-class exploitability —
  `attack-lpdual.md`: v* = 0.68183123 attained, Theorem D suboptimal, shadow price of p₁ = 1); G4.2
  (third-moment cheap-talk test — `attack-twobandwidth.md`: m₃(1/2) = 5, extremal world matches
  tr³ = 2N at λ=1, cubic construction ≤ 0.8071 < 5/6). The related framings G1.4/G1.5/G4.3/G4.4/G3.3/
  G5.7 now point at closed targets and should be read as history, not as open routes.

---

## Round-2 execution status & probe findings (2026-08-11, code-backed, mandatory protocol)

**Protocol honored:** every number below was produced by a script that was run, saved, and cited; no
number was reported without code. CPU-bound work → Rust musl (none needed here); exploratory numerics →
`uv run --quiet --with numpy --with scipy python`. The script lives at `tools/hot_hand_calib.py`
(copied from `/tmp` after running; no canonical `tools/` file was edited); results at
`tools/data/hot_hand_calib_results.json`.

### R-1. G3.1 hot-hand calibration — PROBE RUN (script + command cited)
**Estimator (documented in the script):** smooth-unfolded pair-correlation form factor.
Unfold zeta ordinates by the Riemann–Siegel phase x_j = θ(γ_j)/π (mean spacing 1 by RvM); unfold the
GUE-bulk null (Dumitriu–Edelman β=2 tridiagonal, eigenvalues /√(2N), verified semicircle CDF to 4
decimals) by x = N·F_sc(λ); Poisson by cumulative Exp(1). R(τ) = boundary-corrected pair histogram;
F̂(α) = 1 + Σ(R−1)e^{2πiατ}Δτ, τ ≤ 30. (Raw periodogram on unfolded coordinates was rejected after
debugging: it aliases — a near-lattice sample's periodogram at α·N ∈ ℤ measures the fluctuation
spectrum, not the form factor.)

**Results (all CHECKED NUMERICALLY, `hot_hand_calib.py`):**
1. **No monotone decay beyond α=1.** zeta F̂ (N=3000): 0.730 (α=0.5), 0.880 (0.75), 0.757 (0.95),
   1.683 (1.00), 0.783 (1.05), 0.838 (1.10), 1.298 (1.30), 0.972 (1.55), 1.017 (2.05), 1.021 (2.55),
   1.062 (3.00). Beyond α≈1.3 the curve is flat ≈1 and statistically consistent with the GUE null
   (N=10000: zeta 1.019/0.964/1.011/1.024/0.973 vs GUE 1.006±0.030/1.000±0.030/1.005±0.017/
   1.010±0.037/0.981±0.019 at α = 1.30/1.55/2.05/2.55/3.00). verif-001 §4's "decay beyond" is **not
   reproduced** by the standard estimator.
2. **A sharp, sample-dependent, zeta-specific structure near α∈[1.0,1.3]** (spike at 1.00, dip at
   1.05, spike at 1.10; the α=1.10 value flips 0.84→1.55 between N=3000 and N=10000, +11.6σ vs the
   null at N=10000). Not present in the GUE null (flat 1.00±0.05 there). Consistent with finite-height
   arithmetic (prime-side) corrections to Montgomery's F; **cause not established by this probe** —
   the natural follow-up is a τ-bin/prime decomposition at higher height. Not a smooth decay.
3. **zeta vs GUE agree to ~2–3% in the ramp region (α<1)** — the zeta pair correlation is
   sine-kernel-like, as expected.
4. Caveat recorded: the pair-correlation estimator has a small-τ bias (R at bin center 0.55 reads
   ~0.72 vs sine-kernel 0.67 for both zeta and GUE equally; absolute small-α ramp values are inflated
   ~50% for both) — shifts F̂ by ≲0.01 and affects zeta and the null identically, so the beyond-α=1
   comparison stands while absolute small-α values should not be trusted.

**Verdict for G3.1:** the apparent "decay beyond α=1" is a measurement artifact (the hot-hand
conclusion); there is **no empirical hint of F < 1 beyond α=1**. What is real is a sharp finite-height
arithmetic feature near α≈1 — the object of the follow-up, not a decay.

### R-2. G2.6 "luck" block-variance — PROBE RUN (same script)
10 blocks of 1000 zeros vs 24 GUE replicates vs 24 Poisson replicates, per-block F̂ at
α∈{0.5,0.9,1.1,1.5,2.0}: zeta 0.709±0.101 / 0.970±0.134 / 1.558±0.537 / 0.999±0.061 / 0.970±0.125;
GUE 0.763±0.064 / 0.939±0.105 / 1.015±0.159 / 0.943±0.097 / 0.988±0.114. At α≥1.5 the zeta block
variance is null-consistent (no extra luck to harvest); the only excess sits at α=1.1 where the
arithmetic feature lives (zeta block mean 1.558 = 3.4× the null's std). The fluctuation budget away
from the α≈1 feature is fully explained by the sine-kernel null.

### R-3. Closures by other round-2 agents (cross-referenced, not re-derived)
- **V2 (in-class gap) — CLOSED:** `attack-lpdual.md` — the certificate-side LP at N=256 attains
  v* = p₀ + |E(1)| = 0.68183123, matching the Lean ceiling to ≤ 2·10⁻⁸; Theorem D (0.6725) is
  strictly suboptimal; the shadow price of the certified simple fraction p₁ is exactly 1 — only
  beyond-bandwidth-1 (or a multiplicity bound) moves the constant. The games-catalog vectors aimed at
  this (G2.1 exploitability, G2.7 audit, G1.4 zugzwang, G1.5 komi, G4.3 tax, G4.4 game value) are
  superseded; the exploitability question is answered.
- **V3/P6.5 (third moment / distinct wall 5/6) — CLOSED (documented negative):**
  `attack-twobandwidth.md` — m₃(1/2) = 5 (not 2; the task's input was REFUTED, the paper's m₃(1) = 2
  confirmed); the extremal world has tr³ = 2N at λ=1, matching GUE — the third moment is *cheap talk*
  for the extremal world where it is available; at λ<2/3 (unconditional) the cubic construction gives
  2m₂−m₃ ≤ 7/36 and the best bound 0.8071 < 5/6. G4.2's costly-signal decision rule is decided in the
  negative; P2's priority is downgraded.

### R-4. What remains open from this catalog
- G3.1's follow-up: the τ-bin/prime decomposition of the α≈1 finite-height feature (is it log 2 /
  log 3 resonance structure?) and its height-dependence (higher-height zeros, e.g. the 10⁵–10⁶
  range, to test the "finite-height correction decays" hypothesis).
- G1.6/G5.3/G5.6 (repulsion / stationarity / CFTP): KNOWN-OPEN, unchanged — no new input.
- G2.6's a.s.-certificate target (P9.1): still open as a target type; the variance data above is the
  input its fluctuation control would use.
- Everything else in this catalog was framed as diagnostic/framing and remains so; the two genuine
  probes (R-1, R-2) are run and recorded.

**Honesty footer:** all numbers in R-1/R-2 are CHECKED NUMERICALLY via `tools/hot_hand_calib.py`
(reproducible: `uv run --quiet --with numpy --with scipy python tools/hot_hand_calib.py`, ~4 min,
results `tools/data/hot_hand_calib_results.json`). Domain facts (GVT hot hand, sine-kernel pair
correlation, DE tridiagonal, semicircle unfolding) are standard mathematics used only as null models.
No claim here is a theorem; the deliverable is a documented, reproducible measurement and a documented
negative (no decay beyond α=1; third moment is cheap talk; in-class exploitability closed).

**Honest closing note:** the games angle's strongest NEW contributions are (i) the hot-hand calibration
probe (G3.1) — a sub-hour null-model test of the empirical beyond-1 trend that changes what we believe
about P3's empirical status; (ii) the CFR/MWU certificate-search algorithm (G2.1) — a solver-free,
Lean-friendly computational route to the funded V2 with exploitability as the objective; (iii) the
costly-signal decision rule (G4.2) — a pre-registered, computable test deciding P2's funding priority;
(iv) the almost-everywhere/bankroll target type (G2.6). The rest are framings (they sharpen funded
vectors and prevent re-derivation) and no-fund signals (G3.4, G4.1, G5.3, G5.6). The persistent wall —
beyond-1 pair correlation, third moments, repulsion — appears in game language as the un-callable bluff
(G2.2), the cheap talk the certificate cannot distinguish from a costly signal (G4.2), and the
stationary regime no finite-rank argument reaches (G5.3): three framings of one proven obstruction, each
with a different practical consequence. Nothing here claims to settle RH; the honest output is a ranked
set of probes whose negatives are documented findings, per hooks/agents.md.
