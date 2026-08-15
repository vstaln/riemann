# Riemann Program — Persistent Agent Hooks

## Mission

The Riemann hypothesis (RH): every nontrivial zero of ζ(s) lies on Re(s) = 1/2.
This project pursues a proof of RH — and alongside it, any rigorous, novel mathematics about ζ
and its zeros. **We never give up on the search for a proof.** The search persists across
sessions, attempts, and failures; a failed attack is a documented result, not a reason to stop.

**Standing directive (user, binding): attack RH DIRECTLY** via parallel waves of disjoint levers
on the classical equivalences — Li λ_n ≥ 0, Speiser ζ′ off-line zeros, Nyman–Beurling–Báez-Duarte
d_N → 0, Ξ/Turán–Pólya total positivity, de Branges spaces — each with an RH-false control
demand, hostile blind referees, the ledger as do-not-repeat, and RUST-ONLY compute.
The proportion record (repo-certified 0.673481 simple / 0.836740 distinct; terminal in-class,
0.6818 Lean-PROVEN ceiling) is the fallback, not the target. **A proportion theorem is ZERO
RH evidence in either direction — never describe it otherwise.**

## Non-negotiables (honesty guardrails — HARD RULES, never relaxed)

1. Never fabricate a proof, lemma, or numerical result. No exception.
2. Every claim is labeled: PROVEN / CHECKED NUMERICALLY / CONJECTURED / ABANDONED (reason) / INCONCLUSIVE (blocker).
3. Nothing counts as progress until adversarial validators fail to break it.
4. Never weaken a validator to make a result pass.
5. A wrong, confident result is worse than no result — it poisons the whole search.
6. Never let a self-authored check define correctness: if your check disagrees with the code's
   behavior, suspect the check first. (8C's "0/122 sign-correlation" was exactly this — the
   check compared +μ instead of the Nyman weights −μ; correct answer 19/19.)
7. An RH-false control must fire BEFORE the real case is trusted. Any claim that would also
   "prove" an RH-false model (planted zero, Epstein class-2, Davenport–Heilbronn, Beurling fake)
   is wrong.

## Compute discipline (BINDING — user directive 2026-08-17, hard rule)

**This machine is slow. Never write long-running scripts unless necessary.**
- Before any CPU-bound run: state in one line the belief it changes and the expected runtime.
- Open-ended sweeps, background jobs "to see what happens", multi-hour loops: FORBIDDEN.
- Cheap-first order: (1) closed-form math, (2) f64 scalar probes (<1 min), (3) one bounded
  verifier run, (4) only then a small loop — and kill it the moment it stops paying for itself.
- If a route needs >~20 minutes of compute to reach its next decision point, stop and rethink
  the route first, or write the state to a note and revisit cheaply.
- A note that says "I did not compute X because it would not change our beliefs, here's why"
  is a good note.

## Language policy — Rust-first for EVERYTHING numeric (binding)

Python is too slow for compute-bound work. **Rust is the default for all numeric and CPU-bound
code.** No exceptions without a documented one-line reason in the note label.

- CPU-bound / numeric work: Rust (`cargo build --release`; musl static target if needed:
  `export PATH=$HOME/.cargo/bin:$PATH RUSTFLAGS="-C linker=rust-lld -C link-self-contained=yes" && cargo build --release --target x86_64-unknown-linux-musl`).
- Arbitrary-precision / interval-rigorous: Rust `rug` (GMP/MPFR, correctly-rounded) for
  directed-rounding arithmetic; `arb-sys` (raw Arb/FLINT ball arithmetic) for certified
  enclosures. `rug` 1.30 is validated on this machine.
- Python is FORBIDDEN unless absolutely necessary: (a) bulk network I/O; (b) glue that shells
  out to Rust binaries; (c) **LangGraph swarm orchestration (user-sanctioned)**. Any Python that
  does a compute-bound loop is a violation — port it to Rust.
- Exploratory f64 probes: Rust f64. Anything that feeds a claim needs the rug/arb interval pass
  before it is labeled CHECKED NUMERICALLY.
- Existing Python verifiers in `tools/` may be READ as reference but must be PORTED TO RUST as
  the first action of any lever touching them.

## Orchestration — two layers, both alive

**Layer 1 — pi subagents (the hands).** Subagents pinned `model="opencode-go/deepseek-v4-flash"`,
background, blind + disjoint briefs, ledger-gated. Write-capable: adventurer, architect, builder,
writer. Read-only: diagnose, planner, reviewer. Explore (default) is read-only — route any write
task to architect/builder/writer. Never dispatch the same lever twice — check `research/notes/`
first (duplicates waste the rate-limit budget).

**Layer 2 — LangGraph swarm (the adjudication skeleton, user-set-up, `tools/swarm_langgraph/`).**
StateGraph pipeline PLANNER → IDEA-GEN×N → GATE (novelty) → EXECUTOR×M (runs prebuilt Rust
binaries via `rust_cmd`) → VERIFIER×K (adversarial) → JUDGE → SYNTHESIZER → CRITIQUE →
(accept | next_round → PLANNER). Checkpointed to `research/waves/swarm.sqlite` (thread_id per
wave); resume by rerunning with the same `--wave`. File protocol under `research/waves/wave-<N>/`.
- **Use for**: idea generation at scale, adversarial re-derivation of claims, synthesis of
  partial results, crash-safe multi-round adjudication. Its verifier/referee has caught real
  flaws (Pfaffian category error; fixed-rank Fejér–Riesz objection) — that is its value.
- **Do NOT use for**: compute (its EXECUTOR only shells out to prebuilt binaries — build those
  in Rust first), or anything that needs <20 min (it's slower than one subagent).
- **Known traps (fixed, don't regress)**: round must increment via `next_round` node (was
  never incremented → infinite loop); `_safe_invoke` must `shutdown(wait=False)` (a context
  manager blocks forever on a hung LLM); verifier/executor/idea-gen must dedup by id (idempotent
  across resumes); file writes must carry the FULL accumulated list (append-only protocol).
- Run it with a real frontier (`--frontier "$(cat file.md)"`) and bounded `--max-rounds 1`.

## Campaign method — direct-RH wave protocol (BINDING)

Adapted from Anthropic's campaign method (distilled in
`research/notes/anthropic-campaign-method-2026-08-17.md`); repurposed for the direct-RH pivot.

1. **Briefs are research memos, not tickets.** Target + objects + reading list + coordinator's
   conjecture + stated forecast (deliberately possibly-wrong: the win is the inversion) + DEMAND
   for an RH-false control case. Agent sees nothing but its brief + the files it is told to read.
2. **RH-false control FIRST.** Every lever verifies its discriminator on a planted-zero/dh-type
   control BEFORE trusting real-case numbers (8A: λ′_n<0 at n=21848; 8B: winding=2; 8D: planted
   fails L₅(0)<0; 8C: pow2/squares saturate d′=0.3187/0.3912).
3. **Ledger = do-not-repeat list.** Never launch a ledgered idea again; never re-derive a ledger
   verdict — cite it.
4. **Referee architecture.** Extraordinary claims get hostile blind referees BEFORE the
   coordinator reads the proof; never weaken a validator.
5. **Orphaned-proof rescue.** If a sub-agent dies mid-write, read its directory, recognize the
   deliverable, resume the SAME agent with a checklist + launch checkers (or dispatch a finisher
   with the note + probes on disk).
6. **Proportion ≠ RH (firewall).** A proportion-on-the-line theorem is ZERO evidence about RH.
7. **Coordinator reads final messages, rarely files; does its own line-by-line checks at the
   decisive moments. When a coordinator check disagrees with an agent's reported statistic,
   suspect the agent's check first — then verify by hand.**

## Keep trying — always (the persistence hook)

- **The search is possible. Do not stop.** A failure is a documented result, not a reason to
  stop. This hook binds on every model in every session, forever.
- When a computation fails, times out, or disagrees with expectations: (1) record what was
  attempted and what actually happened; (2) find the root cause — a bug in the code, a wrong
  assumption, a real mathematical obstacle, or a broken claim; (3) try again by a different
  route (different formulation, precision, or attack direction).
- When a proof attempt stalls, do not conclude "impossible". Re-derive from the contract, weaken
  the claim, transport the method from a neighboring problem, or decompose the blocker.
- Only the honesty guardrails can stop a line of work: a claim may be labeled ABANDONED (with
  the documented reason) but the *search* is never abandoned.

## Code-backed verification + documentation (mandatory protocol)

1. **Confirm/deny only with code.** A "checked numerically" claim with no script behind it is
   not checked. Write the code FIRST, run it, report its output.
2. **Save the code with the note.** Every deliverable note cites the exact script + command.
3. **Document every finding**, including negatives and refuted inputs. A negative with a script
   is a result; a negative with no script is a rumor.
4. **Disagreements between agents are adjudicated with code** — both sides re-derive side by
   side; the resolution is written into both notes. Never leave an ambiguity standing.
5. **Verification tools are first-class artifacts** — self-contained, rerunnable, print verdicts.

## PONYTAIL: lazy-senior-dev mode (active for every probe you write)

1. Does it need to run at all? A number already saved in this repo → cite it, don't recompute.
2. Already in this repo? Reuse the existing script before writing anything new.
3. Stdlib / installed deps do it? Use them; never hand-roll numerics.
4. Can it be a few lines? A few lines. A wrong-but-10-line script you can audit beats a
   200-line one you can't.
5. Only then: the minimum code that works.

Rules: no unrequested abstractions; deletion over addition; cut a corner? mark it
`// ponytail: <ceiling>, <upgrade path>`; every non-trivial probe leaves ONE runnable
self-check; output the numbers first, then at most three lines. NEVER lazy about rigor:
labels, cited scripts, and error bounds are the honesty charter, not prose.

## Subagent operation (binding)

Config: `~/.pi/agent/agents/*.md` (adventurer, architect, builder, diagnose, planner, reviewer,
writer) — all pinned to `opencode-go/deepseek-v4-flash`, all background
(`run_in_background: true`), monitor via get_subagent_result; never block the main loop.

1. **Run in background always.** The main loop dispatches and monitors; it never blocks.
2. **Write-first context discipline (the fix for context death).** Write the deliverable after
   ≤3 file reads or the first 5 tool calls, whichever first; refine with ≤3 more reads. A
   committed partial note beats a dead agent.
3. **Compaction is normal — and now fires early.** `~/.pi/agent/settings.json` sets
   `compaction.reserveTokens: 48000` → subagents auto-compact at ~81% of the 256k window
   (was 93.6%, the death zone). Project-level `.pi/settings.json` mirrors it. A compacted agent
   keeps working, not restarts.
4. **Agent roles & write access.** Write-capable: adventurer, architect, builder, writer.
   Read-only: diagnose, planner, reviewer. Explore (default) is read-only — use
   architect/builder/writer for any write task.
5. **No duplicate levers.** Check `research/notes/` for an existing note before dispatching.
6. **Steer, don't kill.** A drifting background agent is steered with a message telling it to
   write NOW — never killed and relaunched if it can still deliver.

## Kill-robustness — survive process death (binding)

The host process can be KILLED at any moment. Context dies; THE DISK SURVIVES.

1. **Write-ahead deliverable**: note file in research/notes/ after ≤3 reads or first 5 tool
   calls — a partial note carrying plan + first findings + commit is the seed.
2. **Progress log**: after EVERY tool call append one line to research/notes/<task>.progress.
3. **State on disk**: every numeric result goes to a file as soon as it exists.
4. **Idempotent resume**: resumed agents read .progress + partial note first, continue from the
   last completed step; never restart from scratch.
5. **Orchestrators**: the campaign state machine (tools/campaign_orchestrator/, SqliteSaver)
   and the LangGraph swarm (tools/swarm_langgraph/, `research/waves/swarm.sqlite`) both resume
   via checkpoint after a kill; kill_log keeps the honest audit trail.

## Skills (s4h + Hermes) — load and apply

- **s4h** — the master orchestration skill; route any open-ended "how do I think through this"
  through it. s4h-epistemology (label calibration), s4h-investigation, s4h-logic,
  s4h-constraint (hardness-test the walls), s4h-creativity/s4h-analogy (fresh attacks),
  s4h-strategy (which attack to fund). Every subagent brief MUST name at least one s4h skill.
- **Hermes research skills** — `research-paper-writing` (MANDATORY before drafting any
  publication-bound write-up; never hallucinate citations), `arxiv`, `duckduckgo-search`.

## Standing research context (verified 2026-08-17)

- RH: open since 1859 (Millennium Prize).
- Published unconditional record: 41.7% (PRZZ 2020). Anthropic Aug-2026 claims ≥2/3 simple /
  ≥5/6 distinct unconditionally (rank–trace inequality, Weil form + Sylvester inertia;
  Montgomery–Taylor window gives 0.6725/0.8362; sources verified real, community acceptance
  UNVERIFIED — treat as live target, not established fact).
- Repo-certified (our own): in-class 0.673481 simple / 0.836740 distinct; terminal in-class
  (0.6818 ceiling PROVEN in Lean; no unconditional |α|>1 form factor, no p₁>0.6818, no new
  certificate input found in wave-7C census).
- Direct-RH wave status (wave 8, all landed with probes on disk):
  - 8A Li λ_n: on-line pairs termwise nonneg; λ_n>0 ∀n≤1000; residual r_n ~ 0.26·n^0.246
    sub-√n; periodogram peaks at the three lowest-zero frequencies (the fluctuation IS the
    signal). NOT a proof (finite data).
  - 8B Speiser: ζ′ left half-strip [0.001,0.5]×[10,5000] EMPTY (winding 0, certified margins);
    **2651 ζ′ zeros in [0.5,1]×[10,5000], per-slab ratio 0.15→0.69 rising** — live future
    object; interlacing belongs to ξ′ (4521 = N(5000)+1).
  - 8C Nyman–Beurling: closed forms + d_N decay measured (slope −0.089, N=10..1000, no
    saturation); MPFR 256-bit certification FIXED and passing (rel 1e-15; the tail l-factoring
    bug); coefficients track −μ(k) (19/19, the Nyman weights); controls saturate
    (d′=0.3187, d″=0.3912). CHECKED NUMERICALLY, not a proof.
  - 8D Turán/Laguerre: controls validated (planted pair FAILS L₅(0)=−9.47e-9; all-real passes
    min 9.6e-11 at k=8,t=32.4); b₀=ξ(1/2) matched 1e-18. Real-case T_k/L_k table INCOMPLETE.
  - 8E Beurling operator: real d_N²=1.13e-2 vs control 5.28e-3 at N=60; control-direction
    question OPEN.
- Key inputs: Bombieri (2000); Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh
  (arXiv:2306.04799, 2501.14545); Montgomery pair correlation (1973).

## Workspace

- /home/vstaln/riemann — root
- research/papers/ — primary sources (.pdf + .txt)
- research/notes/ — proof map, literature map, verification reports, attack log, ledger
- research/waves/ — LangGraph swarm wave artifacts + swarm.sqlite
- tools/ — numerical toolkit (Rust-first; legacy Python where already certified)
- tools/swarm_langgraph/ — LangGraph adjudication swarm (user-set-up)
- PLAN.md — the plan; hooks/agents.md — these hooks (HARD RULE: read and obey)
