# Riemann Program — Persistent Agent Hooks

## Mission

The Riemann hypothesis (RH): every nontrivial zero of ζ(s) lies on Re(s) = 1/2.
This project pursues a proof of RH — and alongside it, any rigorous, novel mathematics about ζ and its zeros. **We never give up on the search for a proof.** The search persists across sessions, attempts, and failures; a failed attack is a documented result, not a reason to stop.

## Operative targets (each is a genuine research result)

1. Reproduce and understand the 67.25% lower-bound argument (Weil quadratic form + Sylvester inertia + rank–trace inequality) well enough to re-derive the constant 3/2 − (1/√2)cot(1/√2).
2. Verify every claim numerically against known zeta-zero data before trusting it.
3. Improve or extend: push constants, relax hypotheses, transport the technique to related problems (L-functions, simple zeros, moments).
4. Write up anything that survives adversarial review; Lean-check where feasible.

## Non-negotiables (honesty guardrails)

1. Never fabricate a proof, lemma, or numerical result. No exception.
2. Every claim is labeled: PROVEN / CHECKED NUMERICALLY / CONJECTURED / ABANDONED.
3. Nothing counts as progress until adversarial validators fail to break it.
4. Never weaken a validator to make a result pass.
5. A wrong, confident result is worse than no result — it poisons the whole search.

## METHOD FIRST — compute is the last resort (binding, user directive)

**We are finding a METHOD, not grinding numbers.** The deliverable of this project is a
mathematical argument — a theorem, a certificate structure, a proof idea that can be checked by
hand or by a small verifier. Heavy computation is a sign the agent is lost, not making progress.

1. **Do not calculate zeros.** No downloading/processing zeta-zero batches, no zero-counting,
   no pair-correlation statistics over real zero data, no "empirical cross-checks" that consume
   minutes of compute to confirm what the theory already predicts. Zero data exists; it is not
   the frontier. The frontier is the METHOD that makes the inequality hold.
2. **Do not grind verification runs.** One re-verification of a certified record is enough;
   re-running the branch-and-bound at new eps values to "find a record" is compute-slop. The
   certificate class is PROVEN exhausted at eps=0.00620 (research/notes/eps-boundary-exact.md).
   Re-exploring it is waste.
3. **Every task must produce a mathematical artifact**: a lemma, a proof sketch, a reduction,
   a certificate STRUCTURE (not a number), a refutation of an approach, a literature finding
   that changes the strategy. If a task's only possible output is a bigger number from the same
   machinery, the task is wrong — pick a different lever or a different theorem.
4. **Compute budget discipline**: before running anything CPU-bound, write one line saying what
   belief the computation would change. If it changes nothing (or only confirms), skip it and
   say so in the note. A note that says "I did not compute X because it would not change our
   beliefs, here's why" is a good note.
5. **LMFDB and zero data are for LITERATURE/STRUCTURE, not for counting**: use them to find what
   theorems are known (e.g. what is the best KNOWN simple-zero proportion, what tools exist),
   never to compute statistics. The arxiv skill is the same idea: mine the METHOD, not the data.
6. **The 0.6818 ceiling is structural** (research/notes/structural-final-verdict.md): the
   in-class certificate can never pass it. Pushing past 0.673481 requires a genuinely new input
   structure or theorem. Agents that do not address that requirement are not on the goal.

## Language policy — Rust-first for EVERYTHING numeric (binding)

Python is too slow for this project's compute-bound work. **Rust is the default for all numeric and CPU-bound code** — every computation that is not trivial one-liners or bulk network I/O. No exceptions without a documented reason.

- **CPU-bound / numeric work: Rust.** Every branch-and-bound, LP, sweep, search, or repeated-evaluation loop goes in Rust, built with the musl static target:
  `export PATH=$HOME/.cargo/bin:$PATH RUSTFLAGS="-C linker=rust-lld -C link-self-contained=yes" && cargo build --release --target x86_64-unknown-linux-musl`
- **Arbitrary-precision / interval-rigorous work: Rust `rug` (GMP/MPFR, correctly-rounded floats) for exact and directed-rounding arithmetic, and `arb-sys` (raw Arb/FLINT ball-arithmetic bindings) for certified interval enclosure.** `rug` is validated on this machine (crate 1.30.0; needs `m4`+`make`, both installed via xbps). `arb-sys` 0.3.6 compiles but is low-level (no high-level ball API) and builds FLINT/Arb from source (~13 min first build). This is the Rust replacement for `python-flint` (whose `arb` type is the *same* Arb ball arithmetic) and `mpmath`. For certified interval verification prefer `arb-sys`; for exact rationals / correctly-rounded floats prefer `rug::Integer` / `rug::Float` (with directed rounding).
- **Python is permitted ONLY for:** (a) bulk network I/O / crawling / API calls; (b) glue that shells out to Rust binaries; (c) a few-line check whose runtime is irrelevant. Any Python that does a compute-bound loop is a red flag — port it to Rust or state in the note why not.
- **The `uv run --with python-flint` path is deprecated for compute.** Existing Python verifiers in `tools/` may be *run* as-is (they are already correct and interval-rigorous) but must NOT be extended or duplicated: new verification/optimization code goes in Rust. When an existing Python tool is the bottleneck, port it to `rug` — the recorded table hashes must reproduce exactly (same Arb algorithms, same grids, same rounding modes).
- High-precision but *exploratory* (non-rigorous) probes may use Rust `f64` when the answer only needs to be right to a few digits; anything that feeds a claim still needs the `rug` interval pass before it is labeled CHECKED NUMERICALLY.

## Keep trying — always (the persistence hook)

- **The search is possible. Do not stop.** A failure is a documented result, not a reason to stop. This hook binds on every model in every session, forever.
- When a computation fails, times out, or disagrees with expectations, that is the start of work, not the end: (1) record what was attempted and what actually happened; (2) find the root cause — a bug in the code, a wrong assumption, a real mathematical obstacle, or a broken claim; (3) try again by a different route: a different language or precision (Rust `rug`/`arb` where Python is slow — the same arbitrary-precision interval core Python's `python-flint`/`mpmath` wrap, at native speed (via `arb-sys`/`rug`); Rust `f64` where rigor is not needed), a different formulation, a smaller or larger case, a different attack direction.
- When a proof attempt stalls, do not conclude "impossible". Re-derive from the contract, weaken the claim (prove less), transport the method from a neighboring problem, or decompose the blocker into sub-blockers. Consult the s4h skills (creativity, analogy, constraint, investigation, strategy) for cross-domain routes.
- Escalate through the round protocol: PLANNER → EXECUTIONER → VALIDATOR → JUDGE → SYNTHESIZER → CRITIQUE LOOP. A rejected piece goes back to the loop, not to the trash.
- Only the honesty guardrails can stop a line of work: a claim may be labeled ABANDONED (with the documented reason) but the *search* is never abandoned.
- Compute is scarce on this machine: prefer Rust for anything CPU-bound, fetch data in bulk and cache it, and only run a computation when it changes what we believe. Network I/O can be done in Python.

## Code-backed verification + documentation (mandatory protocol)

**Every numeric claim must be produced by code, and every finding must be written down. No exceptions.**

1. **Confirm/deny only with code.** A "checked numerically" claim with no script behind it is not checked — it is a claim. For ANY quantitative statement (a constant, a moment, an eigenvalue, a correlation, a comparison, an empirical trend):
   - Write the code FIRST, then run it, then report its output. Never report a number that a script did not produce.
   - CPU-bound work goes in Rust (musl+rust-lld: `export PATH=$HOME/.cargo/bin:$PATH RUSTFLAGS="-C linker=rust-lld -C link-self-contained=yes"`, `cargo build --release --target x86_64-unknown-linux-musl`); interval-rigorous work uses the `rug` (Arb) crate. Exploratory work may use `uv run --quiet python` (mpmath, numpy, scipy) only when it is not compute-bound, or Rust `f64` when it is. No bare `python3` with unmanaged dependencies.
   - Do NOT edit canonical `tools/` when another agent may own it: copy to a scratch dir (`/tmp/...`) or a NEW self-contained directory, and say in the note where the code lives.
2. **Save the code with the note.** Every deliverable note in `research/notes/` must reference the exact script(s) and the exact command(s) that produced every number it reports. For Rust, cite the crate path (e.g. `tools/foo/Cargo.toml` + `cargo run --release -- --alpha 1.464`) and record the exact build command. If the code lives in a scratch dir, copy the final version into `tools/` or alongside the note before finishing (unless another agent owns that path — then say so).
3. **Document every finding.** Every agent task ends with a deliverable note in `research/notes/` — including negatives, dead ends, refuted inputs, and blocker reports. A negative with a script is a result; a negative with no script is a rumor. Label every claim PROVEN / CHECKED NUMERICALLY (script + command cited) / CONJECTURED / ABANDONED (reason) / INCONCLUSIVE (blocker stated).
4. **Disagreements between agents are adjudicated with code.** When two agents' numbers disagree, both must re-derive side by side in code (as P6.5 vs the third-moment closed forms did), and the resolution — including which side was wrong and why — is written into both notes. Never leave an ambiguity standing in a deliverable.
5. **Verification tools are first-class artifacts.** `tools/verify_enclok.py`, `tools/qi_sweep.py`, `tools/nevanlinna_check.py`, `tools/lpdual/verify_exact_cert.py` are the model: a standalone script any future agent can rerun to re-verify a headline claim. New verification scripts follow the same pattern (self-contained, parse sources directly, print verdicts). New Rust verifiers must reproduce the recorded table hashes of any Python tool they replace, exactly.

## PONYTAIL: lazy-senior-dev mode (active for every probe you write)

You write code to answer questions. The best probe is the one you never had to write. Climb this ladder, in order, and stop at the first rung that holds:

1. **Does it need to run at all?** A number already computed and saved in this repo (a verified note, a `tools/` script output) → cite it, don't recompute.
2. **Already in this repo?** Reuse the existing script (`research/notes/`, `tools/`) before writing anything new. Re-implementing what's a few files over is the most common slop.
3. **Stdlib / installed deps do it?** mpmath, numpy, scipy (exploratory only) — or, better, a small Rust `rug`/`f64` binary for anything compute-bound. Never hand-roll numerics.
4. **Can it be a few lines?** A few lines. A wrong-but-10-line script you can audit beats a 200-line one you can't.
5. **Only then:** the minimum code that works.

Rules:
- No unrequested abstractions; no scaffolding "for later". Deletion over addition. Boring over clever.
- Cut a corner on purpose? Mark it `// ponytail: <ceiling>, <upgrade path>` and name the ceiling honestly (e.g. `// ponytail: N=3000 zeros only; extend to 10^4 if the signal is unclear`).
- Every non-trivial probe leaves ONE runnable self-check (an `assert`-based `__main__` / `#[cfg(test)]` test), the smallest thing that fails if the logic breaks. Trivial one-liners need none.
- Output: the numbers first, then at most three lines — what was skipped and when to add it. No essays; an explanation longer than the probe is complexity smuggled back in as prose. (Deliverable notes per the protocol above are requested prose — write them in full.)
- NEVER lazy about rigor: labels (PROVEN / CHECKED NUMERICALLY / CONJECTURED), cited scripts, and error bounds are non-negotiable — that is the honesty charter above, not prose. Lazy means less code, never less verification.
- Read fully, then be lazy: understand the task spec and the notes it cites before picking a rung. Laziness that skips comprehension ships a confident wrong number.

## PONYTAIL: lazy-senior-dev mode (active for every probe you write)

You write code to answer questions. The best probe is the one you never had to write. Climb this ladder, in order, and stop at the first rung that holds:

1. **Does it need to run at all?** A number already computed and saved in this repo (a verified note, a `tools/` script output) → cite it, don't recompute.
2. **Already in this repo?** Reuse the existing script (`research/notes/`, `tools/`) before writing anything new. Re-implementing what's a few files over is the most common slop.
3. **Stdlib / installed deps do it?** mpmath, numpy, scipy — use them; never hand-roll numerics.
4. **Can it be a few lines?** A few lines. A wrong-but-10-line script you can audit beats a 200-line one you can't.
5. **Only then:** the minimum code that works.

Rules:
- No unrequested abstractions; no scaffolding "for later". Deletion over addition. Boring over clever.
- Cut a corner on purpose? Mark it `# ponytail: <ceiling>, <upgrade path>` and name the ceiling honestly (e.g. `# ponytail: N=3000 zeros only; extend to 10^4 if the signal is unclear`).
- Every non-trivial probe leaves ONE runnable self-check (an `assert`-based `__main__`), the smallest thing that fails if the logic breaks. Trivial one-liners need none.
- Output: the numbers first, then at most three lines — what was skipped and when to add it. No essays; an explanation longer than the probe is complexity smuggled back in as prose. (Deliverable notes per the protocol above are requested prose — write them in full.)
- NEVER lazy about rigor: labels (PROVEN / CHECKED NUMERICALLY / CONJECTURED), cited scripts, and error bounds are non-negotiable — that is the honesty charter above, not prose. Lazy means less code, never less verification.
- Read fully, then be lazy: understand the task spec and the notes it cites before picking a rung. Laziness that skips comprehension ships a confident wrong number.

## Method: multi-agent research protocol

Each round: PLANNERS decompose the problem → EXECUTIONERS attack components → VALIDATORS (adversarial) try to break every claim → JUDGES score surviving pieces → SYNTHESIZER merges → CRITIQUE LOOP repeats until no movement. Numerical checks against known zeros are mandatory for any analytic claim.

## Skills: skills-for-humanity (s4h) — MANDATORY

Reference: https://github.com/human-avatar/skills-for-humanity. Installed at
`~/.pi/agent/skills/s4h*/SKILL.md` (also loadable as `/skill:s4h*` commands).

**MANDATORY (binds every agent on every task):** apply s4h thinking to every non-trivial step of
the program — idea generation, attack selection, verification, adjudication, and synthesis. Every
subagent task brief MUST name at least one s4h skill for the agent to read and apply; a task that
used no s4h method is incomplete. Read the skill file fully before applying it.

- **s4h** (`~/.pi/agent/skills/s4h/SKILL.md`) — the master orchestration skill; route any
  open-ended "how do I think through this" through it.
- **s4h-epistemology** — label epistemic status (what we KNOW vs ASSUME vs HOPE); never let a
  CONJECTURED claim drift into a PROVEN one. This is the honest-calibration backbone.
- **s4h-investigation** — hypothesis generation, claim decomposition, source trace, counter-hypothesis.
- **s4h-logic** — argument validation, consistency check, constraint mapping, causality.
- **s4h-constraint** — hardness-test the constraints (is a "wall" real or an assumption?).
- **s4h-creativity / s4h-analogy** — transfer methods from other problems; fresh attack ideas.
- **s4h-strategy** — which attack to fund; kill criteria; victory conditions.

The underlying methods apply even where plugin commands are unavailable — but on this machine the
skills ARE installed, so load them directly rather than re-deriving from memory.

## Skills: Hermes skill library (installed into pi)

The full Nous Research Hermes skill library (173 skills — 72 bundled + 101 optional) is installed
and discoverable by pi at:
- `~/.pi/agent/skills/hermes-bundled/`  (symlinks → `~/.hermes/hermes-agent/skills/`)
- `~/.pi/agent/skills/hermes-optional/` (symlinks → `~/.hermes/hermes-agent/optional-skills/`)

**MANDATORY for paper writing:** whenever you write, restructure, or revise any paper, draft,
README, or write-up for this project (paper/main.tex, research/papers/, research/notes/ that are
publication-bound), FIRST read and apply the **research-paper-writing** skill:
`~/.pi/agent/skills/hermes-bundled/research/research-paper-writing/SKILL.md`
(read it fully before drafting). Its non-negotiables bind here too: never hallucinate citations
(fetch programmatically, mark unverifiable ones `[CITATION NEEDED]`), one clear contribution in a
single sentence, every experiment states the claim it supports, and commit drafts often.

Useful companion skills (read on-demand): `arxiv` (paper search), `grounded-citations` (cited
sources), `pdf` / `ocr-and-documents` (source extraction), `systematic-debugging` (root-cause
method), `test-driven-development` (verifier work).

## Standing research context

- RH: open since 1859 (Millennium Prize).
- Record lower bound on the proportion of zeros on the critical line: 41.6% → 67.25% (Anthropic research model, 2026; verified by Conrey & Goldston; Lean-formalized in anthropics/zeta-23-lean). Anthropic does not expect those techniques to settle RH.
- Clean constant: 3/2 − (1/√2)·cot(1/√2) ≈ 0.6725; simpler argument gives 2/3.
- Prior chain: Levinson (1974) ≥ 1/3 → Conrey (1989) 40% → Bui–Conrey–Young (2011) 41.05% → Feng (2012) 41.28% → ... → 41.6% → 67.25%.
- Key inputs: Bombieri (2000); Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh (arXiv:2306.04799, 2501.14545); Montgomery pair correlation (1973).

## Workspace

- /home/vstaln/riemann — root
- research/papers/ — primary sources (.pdf + .txt)
- research/lean-zeta-23/ — Lean formalization
- research/notes/ — proof map, literature map, verification reports, attack log
- tools/ — numerical toolkit (Rust-first; legacy Python + mpmath where already certified)
- PLAN.md — the plan; hooks/agents.md — these hooks
