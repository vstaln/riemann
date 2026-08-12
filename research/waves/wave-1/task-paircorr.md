# Task: Pair-correlation route to RH (RESEARCHER — s4h-investigation)

You are a RESEARCHER agent in the Riemann swarm. You MUST use s4h thinking.

## MANDATORY first steps (do these before anything else)
1. Read /home/vstaln/riemann/hooks/agents.md — the persistence hook binds you: NEVER give up, document failures as results, escalate through PLANNER→EXECUTIONER→VALIDATOR→JUDGE→SYNTHESIZER.
2. Read /home/vstaln/.pi/agent/skills/s4h-investigation/SKILL.md and s4h-creativity/SKILL.md — apply their methods.
3. Read /home/vstaln/riemann/research/notes/discovery-6732629.md (the certified 67.3263% record).

## Your research task
Deep-research the pair-correlation route to RH. Use crawlee (cd ~/crawlee-research && node crawl-batch.mjs urls.txt with a urls.txt of arXiv pages) to fetch FULL text of:
- arXiv:2501.14545 (Pair Correlation of Zeros I: Proportions of Simple Zeros and Critical Zeros — pair correlation yields ≥2/3 simple AND ≥2/3 on critical line under narrow-box condition; ≥1/3 both unconditional)
- arXiv:2306.04799 (unconditional Montgomery theorem; 61.7% simple under thin-box)
- Search arXiv for follow-ups and "pair correlation simple zeros critical"

Then WRITE /home/vstaln/riemann/research/waves/wave-1/results/paircorr-findings.md:
1. Exact theorem statements (condition → proportion bound)
2. THE METHOD in detail: how does pair correlation yield on-critical-line results? (our certified bound is simple+on-line; theirs is simple OR on-line — can they combine?)
3. Is their narrow-box condition compatible with our rank-trace machinery? (this is the KEY question)
4. 3-5 CONJECTURED attack ideas combining pair-correlation with our machinery
5. Honesty labels on every claim (PROVEN / CHECKED NUMERICALLY / CONJECTURED)

Print at end: RESULT: <status> — <one-line summary>
