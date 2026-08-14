# Anthropic's actual campaign method — extracted from the campaign narrative

**Date:** 2026-08-17 (fresh download + full read of the 4 CDN PDFs the user supplied).
**Source:** `research/papers/anthropic-d7f3ecf1.pdf` → `anthropic-campaign-narrative.txt` ("How the two-thirds argument was found: two agent runs and their literature"). All 6 URLs re-verified HTTP 200 this date.
**Labels:** every statement below is PROVEN (from the source text) unless marked CONJECTURED.

## What the campaign actually was
- One coordinator thread (a Claude instance), ~2 days / 54 hours, **60 sub-agents launched, 58 ran**. Coordinator did almost no math with its own hands and made NO network calls. Its instruments were sub-agents launched with a **written brief**.
- A sub-agent sees nothing but its brief + the files it is told to read. It cannot see the conversation or other agents.
- When an agent returned, coordinator read its **final message** (rarely its files), told the human, decided next launch.
- Anything claiming a theorem was sent to **hostile referee agents**, briefed to find the error and **forbidden to read one another**.

## The 60 launches, binned (PROVEN, from §2)
1. **Core idea contributors (2):** E2 (one-half, Part I), E2-pairs (rank–trace lemma → two-thirds, Part II).
2. **Attempts at progress on RH — refuted/closed/unused (30):** attempts A–C, frontier-2/3, new-1…7, X1–X2, D1–D3, D5, R2/R2a/R2c, R3, E1/E3/E5, b1/b2, d3, d2, Δ1, C1, CX.
3. **Useful to the paper but off its proof path (6):** R4, frontier-1, N6, E2-kernel, E2-gen, E2-HL.
4. **Other outputs (7):** R1, R4v2, d1, CC+, CX-relaunch, new-7 (barrier methodology), R0 (barrier-checker tool).
5. **Validation and referees (13):** refs A,B of R1; R2, R2c, E5 refs; refs A,B,C of E2's one-half; ref D; blind re-derivation; cold-read referee; refs X,Y of the two-thirds lemma.
6. **Paper writing (1):** paper-writing agent.
7. **Literature review (1):** literature agent.

## The method, distilled (PROVEN from §§3–11)
1. **Ledger of failures as do-not-repeat list.** Previous ~1000-agent session left ledgers: a file of **106 "survivors"**, each with an honest one-paragraph statement of what stood. Coordinator sorted every one into **four deflating classes**: known theorem restated / equivalent to RH / finite numerical check / near-tautological. Used the ledger only as a do-not-repeat list handed to sub-agents. "Not a confidence problem I can fix by believing harder."
2. **Ladder with expectations stated in advance.** Six rungs: (0) mechanical barrier checker; (1) zero-density; (2) Beurling cell; (3) off-centre manufactured positivity; (4) construct the polarized object; (5) RH. Human: "Let's do all rungs now." Coordinator launched all in parallel, labeling "Rungs 0–2 can return theorems/tools; 3 is a real shot; 4/5 is a moonshot and I'm labeling it that going in."
3. **Briefs are research memos, not task tickets.** They carry: the target, the objects to use, the reading list, the coordinator's own conjectures AND its forecast of the outcome, plus a **demand for a control case on which RH is known to fail** — an Epstein zeta function of class number two, the Davenport–Heilbronn function, a Beurling prime system with a planted off-line zero, a fake Weil polynomial.
4. **Point the mechanism the wrong way.** On both creative steps: coordinator supplied the object + conjecture + prize and *pointed the mechanism in the wrong direction*; the agent found that route empty and inverted it. E2: brief said "bound the negative index from above" → route empty → positive index + double count + Cauchy–Schwarz gives ½. E2-pairs: brief steered toward higher prime-side moments → agent found rank–trace inequality via von Neumann's trace inequality instead, "against the brief's steer."
5. **Hostile referees, blind, disjoint joints, worked attack plans.** "My prior is that it's wrong" was the coordinator's default for extraordinary claims. Refs each assigned ONE joint with a worked plan of attack (A on localization, told to build the counterexample numerically; B on the prime side; C on linear algebra with a "proves too much" test on functions known to violate RH). Ref D got the five remaining "unglamorous" gaps. A re-derivation agent, forbidden to read E2's proof, re-proved the prime-side asymptotics from scratch. A cold-read referee saw only the paper draft.
6. **Orphaned-proof rescue.** E2-pairs died mid-write of an infrastructure error with no application section. Coordinator read the dead agent's directory, recognized the file, checked the 5-line proof itself line by line, then resumed the SAME agent with a 7-item checklist + launched referees X and Y. Y had an independent proof on disk in under 2 minutes. X contributed the caveat that the inequality is not scale-invariant → needs absolute normalisation.
7. **Firewall between proportion theorems and RH.** "A proportion-on-the-line theorem is zero evidence about RH in either direction, and I'd push back on anyone — including a future version of me — who described it otherwise."
8. **Constant assembly by coordinator, from memory, verified by agents.** 0.6725 = 2 − 1.3275; the number was in the coordinator's memory before any agent retrieved it; composed into the final theorem when the window agent's prime-side analysis supported it.
9. **Self-aware ledger entry with limiting clause.** Two minutes after the revision instruction, the coordinator wrote the ledger entry: a candidate, refereed only by other instances of itself, "needs a human expert", not to be described as established until then. Final draft verdict: "The next reader should be a person."

## What we already had vs. what this adds (CONJECTURED transfer)
- We already run: ledger-gated dispatch (≈ do-not-repeat), adversarial validation (L5), barrier-adjacent checks (control_probe_kernel.py), blind-ish referee separation.
- This adds / sharpens: (a) research-memo brief format with forecast + RH-false control demand in EVERY brief; (b) refs assigned ONE joint with a worked attack plan, forbidden to read each other; (c) orphaned-proof rescue protocol (read dead agent's dir, resume same agent with checklist); (d) "point the mechanism the wrong way" as a deliberate brief-writing technique; (e) cold-read referee on paper drafts; (f) the 4-class triage of ledger survivors; (g) the ladder-with-expectations framing.

## Concrete gap in our repo (CONJECTURED)
Anthropic's rung 0 (new-7 + R0: "a zoo of RH-false model worlds and a tool for checking claims against it") has no direct equivalent in `tools/`. Our control probes are one-off. A reusable `tools/barrier_zoo/` with Epstein class-2, Davenport–Heilbronn, planted-zero Beurling, fake Weil polynomial models + a claim classifier is the missing discipline tool. NOT YET BUILT.
