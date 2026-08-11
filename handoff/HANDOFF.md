# HANDOFF — New Session Continuation Brief (RH swarm, phone mirror)

**Written:** 2026-08-12 ~01:00 (+0700) · **By:** previous session (coordinator)
**Read first:** `AGENTS.md` (phone conventions), `hooks/agents.md` (charter/guardrails), `PLAN.md`.
**This session starts with the subagents plugin WORKING and the commandcode provider configured.**

---

## 0. Why a new session was needed (read this first)

The previous session ran a 5-agent swarm by spawning separate `pi -p` processes (`nohup`).
That worked (4 of 5 delivered or partially delivered) BUT the in-session subagent plugin
(`@tintinweb/pi-subagents`) was NOT loading its tools. Root cause found and **fixed**:

- `settings.json` packages listed the OLD `pi-subagents` (v0.45.2, broken/auto-load-fails)
  instead of the working `@tintinweb/pi-subagents`.
- **Fix applied:** the packages list now contains **`npm:@tintinweb/pi-subagents`** (the
  `npm:` prefix matters — unprefixed entries silently fail to resolve).
- **Verified:** a fresh `pi` session now has the tools `Agent`, `get_subagent_result`,
  `steer_subagent` (confirmed via tool-listing probe).
- **Your session was started AFTER the fix, so you have these tools.** Use them for the
  swarm — do NOT spawn `nohup pi -p` processes unless you need truly parallel API workers.

### How to use the subagent tools (from the plugin)
- `Agent` — dispatch a subagent. Params: `task` (string, required), `description` (3–5 word
  label), `agent` (type; available: researcher/planner/builder/reviewer/… plus custom
  `.pi/agents/*.md` if present), `model` (optional override, e.g. `commandcode/deepseek-v4-flash`),
  `thinking` (low/medium/high), `maxTurns` (bound the work).
- `get_subagent_result` — poll/collect results. `steer_subagent` — redirect a running one.
- Subagents run as separate pi processes with their own sessions; keep tasks < 10 min wall,
  fully self-contained, and make them WRITE their deliverable to `research/notes/` (per
  `AGENTS.md`) so results persist even if the parent dies.

---

## 1. Provider change — Command Code (done on this machine, ready for laptop)

Configured in `~/.pi/agent/models.json` (this phone):

```json
"commandcode": {
  "name": "Command Code",
  "baseUrl": "https://api.commandcode.ai/provider/v1",
  "apiKey": "<the user_ key>",
  "api": "openai-completions",
  "models": [ /* 45 models: deepseek/*, gpt-5.*, kimi-*, glm-5.*, qwen3.*, google/gemini-*, xai/grok-4.5, xiaomi/mimo-*, … */ ]
}
```

- Base URL is **`https://api.commandcode.ai/provider/v1`** — note the `/provider/` segment
  (bare `/v1/*` 404s). Auth: `Authorization: Bearer <key>` (OpenAI shape). Also exported as
  `COMMANDCODE_API_KEY` in `~/.bashrc`.
- **Verified end-to-end:** `pi --no-session --model commandcode/deepseek-v4-flash -p "…"` → `CC-OK`.
- `commandcode/deepseek-v4-flash` has **1M context** (vs 200K cap on opencode-go) and is a
  reasoning model — a strong default for subagents.
- **Claude models (`claude-*`) are EXCLUDED**: they require the Anthropic-shape endpoint
  (`/provider/v1/messages`) and this key's plan gates them (`MODEL_NOT_IN_PLAN: … Pro and
  above plans or extra on demand usage`). If the plan is upgraded, add a second provider:
  `api: "anthropic-messages"`, same baseUrl, models = the `claude-*` ids.
- **Laptop (void, 192.168.1.50):** same models.json applies — copy this file to
  `/home/vstaln/.pi/agent/models.json` when the laptop is reachable (it is currently asleep;
  do not block on it — the phone mirror is authoritative for now).

---

## 2. Swarm status — what the previous wave produced

Workspace: `~/riemann` (= `/data/data/com.termux/files/home/riemann`; visible inside proot at the same path).

| # | Task | Status | Deliverable |
|---|------|--------|-------------|
| Q4 | Adversarial verification of external constants | **PARTIAL — finish me** | `tools/verify_gram_stability.py`, `scratch/q4_out.txt`; session has key finding (below) |
| Q1 | Transfer stability to on-line (A) / distinct (C) | ✅ DONE | `research/notes/transfer-stability-online.md` |
| Q2 | Does Gram constraint beat in-class ceiling 0.6818? | ✅ DONE | `research/notes/ceiling-gram-constraint.md` |
| Q3 | Consecutive-zeros ladder 3→7→9→11 | **PARTIAL — extend me** | `tools/ladder_probe1.py`, `tools/ladder_probe2.py`; key finding below |
| LIT | arXiv sweep (simple zeros / on-line / Weil-form) | ✅ DONE | `research/notes/literature-sweep-simplezeros.md` |

### Key results already banked

**Q1 (transfer):** Theorem C (distinct, 5/6): method-level transfer verified numerically —
stability term positive with same kernel-ε; constant-level needs C's rank–trace chain
(not on phone); hypothetical shift ≈ +1.9×10⁻⁵ (3-pt) / +3.3×10⁻⁴ (7-pt) — HYPOTHETICAL.
Theorem A (on-line w/ multiplicity, 2/3): **INCONCLUSIVE, blocker named** — stability term IS
positive (ε_A ≥ ε_D, 0 violations in 4000 samples) but A's equality case is doubly impossible
and the 2/3 deficit looks data-limited (pair-correlation content), not slack-limited → the
transfer may be vacuous. Discriminating experiments listed in the note.

**Q2 (ceiling):** **CEILING STANDS at 0.68183123059534187426.** PROVEN (under the LP framing):
a Gram constraint is a feasible-set restriction, so it cannot raise a maximization's optimum.
The 256-law satisfies the constraint with 12–2000× margin in every surrogate/adversarial
model (τ ≈ 0.21 for the thinned-CUE surrogate vs ε₇ ≈ 5.4e-4 floor). The stability refinement
moves the method's *certified* constant toward the ceiling (+5.1e-4 scale), not beyond it.
Caveat: the "constant-shift reading" would shift the ceiling by the stability term itself
(→ ~0.68234), which is not a structural breakthrough.

**LIT (sweep):** 22-item dated table + per-target verdicts in the note. Warm leads:
- **GS25** (arXiv 2511.20059, Goldston–Suriajaya) — RH-free Montgomery-style simple-zero proof;
- **GS26** (2603.28104) — narrow-box ⇒ ≥ 2/3 simple **and on the line** (feeds Q1 directly);
- **Alternative Hypothesis** (2508.10857, Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh) —
  consecutive-gap structure = the exact input to the Gram-stability refinement & Q3 ladder;
- **Groskin** (2607.02828) — finite Guinand–Weil dictionary, truncated Weil-form values are
  exact zero sums, certified (interacts with Q2/verification);
- **Connes** (2602.04022) — Weil-form extremization; **Chirre–Gonçalves–de Laat** (1810.08843)
  — SDP pair correlation (same certificate family as the LP dual).
- Crank flag: 2205.00811 (Suman, "100% of zeros on the line", RH claim) — ignore.
- **Negative result:** no arXiv paper beats the Anthropic 67.25% simple-zeros constant;
  the 67.30/67.31/67.32% extensions are repos, not papers.

### Partial work needing completion (do these FIRST, as subagents)

**Q4 (validator) — salvage & finish.** Session shows: a 4-part verification script ran in 15s;
key finding: **the true min of Σk² over the triangle (u,v>0, u+v≤4) is 2.2215e-4 — within
0.5% of the claimed certified 221/10⁶**. It was writing "v2" (harden the 7-point global min,
which SLSQP found worse than sampling) when it stopped. Finish:
1. Re-run `proot-distro login ubuntu -- python3 tools/verify_gram_stability.py`
2. Reproduce: H0 = 3/2 − (1/√2)cot(1/√2); 3-pt bound (H0−221e-6/4)/(1−221e-6/2) = 67.2519767%;
   7-pt (1345000·H0−2680)/1340003 = 67.3008528% (all previously confirmed to 30 digits).
3. Verify the "no triple zero-gap" kernel claim: no (u,v), u+v≤4 with k(u)=k(v)=k(u+v)=0
   (Q2 agent confirmed numerically: impossible; min max|k| = 1.066e-2).
4. Hunt flaws in the ainta/trmdy deduction (labels: PROVEN / CHECKED NUMERICALLY / CONJECTURED…).
5. Write `research/notes/adversarial-verify-constants.md` with every number code-backed.

**Q3 (ladder) — extend.** Session found the **span rules**: S(3) = 4 (Σ of pair-gaps ≤ 4) and
**S(7) = 9** (Σ ≤ 9, unweighted min 3.87e-3, ratio 1.018 vs certified 19/5000 = 3.8e-3;
NOT Σ≤4, NOT Σ≤12). 3-pt S2 min = 2.2215e-4 at (2.0121, 1.0531). Next: build the 9-point and
11-point pressure functionals (weighted pair-squares of the Gram entries over the span domain),
grid + local refine to estimate the floor, and estimate the limiting constant
`(H0 − ε/4)/(1 − ε/2)`-style conversion for each ladder rung. Note Q2's observed 4-atom
per-atom floor 2.2e-3 already exceeds the 7-point 5.4e-4 → larger blocks give better floors.
Write `research/notes/ladder-9-11-points.md`.

---

## 3. Recommended second-wave plan (after Q3/Q4 complete)

1. **Verify + synthesize** what exists (spot-check numbers independently, especially the
   span rules and the ε floors). Keep the honesty regime: every claim labeled, every number
   from a script you ran.
2. **Follow the LIT leads** — the highest-leverage open moves:
   - Q1 redo armed with GS25/GS26 (on-line 2/3 without RH) — is the Gram-stability transfer
     vacuous vs the data-limited deficit? (discriminators in the Q1 note)
   - Alternative-Hypothesis structure → does the AH constraint force or forbid the
     Gram-stability improvement at larger blocks (Q3 ladder)?
   - Groskin's certification budget B_T — can it certify the external 7-point/183-point
     constants with exact zero sums on the phone (scipy/mpmath only; no Lean)?
3. **Fresh angles** (not covered by laptop agents, which own S3-law/diag/adj2/null-baseline/
   mvnorm/Lean/sixth-moment): Weil-form screw-function survey (2606.09096), mollifier-vs-Weil
   comparison, explicit small-gap tools (2010.10675) for the ladder.

---

## 4. Environment & conventions (the phone mirror)

- **Python:** `proot-distro login ubuntu -- python3` (numpy 2.3.5, scipy 1.18.0, mpmath 1.4.1).
  No uv; pip is PEP-668-externally-managed → `--break-system-packages` if installing.
- **No internet restrictions** from bash here (curl worked for arXiv + commandcode API) — but
  spawned agents may hit the permission system for some commands; keep network needs in the
  task brief.
- **Guardrails (hooks/agents.md):** never fabricate; every result labeled
  PROVEN / CHECKED NUMERICALLY (script+command) / CONJECTURED / INCONCLUSIVE / ABANDONED;
  write notes to `research/notes/` with unique filenames; code-backed numbers; estimates
  flagged (Arb/python-flint NOT available — certified bounds are laptop work).
- **External repos (ainta/trmdy/tawanerguo) live on the laptop, NOT cloned on the phone.**
  Verify their math directly; do not assume their constants are right (that's Q4).
- **Syncing back:** when laptop (void) wakes, rsync `~/riemann` → `/home/vstaln/riemann/`
  (`pc` / `pc-lan` from proot, ssh config hosts: pc, pc-lan, pc-jump). Do not block on it.
- **Sessions:** every agent run has a session file under `~/.pi/agent/sessions/…-riemann-…/`;
  the previous wave's sessions hold reasoning you can `session_search` for context.

**Files layout:** `tasks/` (briefs), `research/notes/` (deliverables), `tools/` (scripts),
`scratch/` (raw outputs incl. lit-sweep XMLs, q4_out.txt), `handoff/` (this package).
