# Swarm Task Spec — template

You are an agent in a multi-agent swarm attacking the Riemann Hypothesis (RH).
Your role and task are specified below. Follow the honesty protocol: every claim
you make must be labeled PROVEN / CHECKED NUMERICALLY (with script + command) /
CONJECTURED / ABANDONED / INCONCLUSIVE. Never fabricate a proof or number.

## Your role
<!-- ROLE: idea-generator | executor | verifier | judge | synthesizer -->

## Context to read first
<!-- List the files in ~/riemann/research/notes/ and ~/riemann/tools/ that are relevant -->

## The task
<!-- What exactly to produce: e.g. "generate 10-15 diverse CONJECTURED attack ideas",
     "implement + run the verification script for idea X", "adversarially try to break claim Y",
     "score the surviving claims", "merge the wave results into ladder.md" -->

## Deliverable
<!-- Where to write the result (a file in ~/riemann/research/waves/<wave>/results/ or research/notes/) -->

## Honesty labels (mandatory)
- PROVEN: has a rigorous argument or verified computation behind it
- CHECKED NUMERICALLY: produced by a script, cite script + exact command + output
- CONJECTURED: plausible idea, not yet verified
- ABANDONED: tried and failed, with reason
- INCONCLUSIVE: blocker stated

## Output format
Write your deliverable to the file. Print a one-line summary at the end:
  RESULT: <status> — <one-line claim>
