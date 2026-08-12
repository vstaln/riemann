# Task: m3-min-frontier — the certificate value over the m₃=5±ε class (the T-frontier)

**Agent:** EXECUTOR (phone proot). **Charter:** ~/riemann/hooks/agents.md. **Mission:** the m₃-class door's open hinge. m3-price showed the pin is FREE on the max side (class contains high-p₁ configs, price ≈ 0) and p₁=0.70 needs T ∈ [−3.87−ε, −0.44+ε]. But the CERTIFICATE value = min over the class, and the class likely contains LOW-p₁ configs (D = 4−3p₁ grows as p₁ falls; pair ≥ 3p₁+1.44 shrinks; T can compensate within the realized range). THE QUESTION: what is min p₁ over {rows, marks, m₃ ∈ 5±ε, T ∈ realized-range}? If min-p₁ ≥ 0.70 the certificate is 0.70 (in principle); if not, the binding adversary must be identified and either excluded by a sharper read or accepted as the wall.

**READ (in order, STOP after):**
1. ~/riemann/research/waves/wave-phone-2/results/m3-price.md — the identity m₃ = D + pair + T, the pair-refund, the T-window, the N=64 pool LP methodology (reuse it!).
2. ~/riemann/research/notes/attack-twobandwidth.md §2 — m₃(1/2)=5 PROVEN three ways; the marked-m₃ machinery; A2/A3.
3. Find the m3-price scripts: ls ~/riemann/research/waves/wave-phone-2/results/ (m3_price*.py or similar) — reuse the pool generator + LP.

**THE WORK:**
1. **PIN THE REALIZED T-RANGE PRECISELY.** Where did [−3.93, −0.44] come from (m3-price's source)? Compute T for the real zeros directly at N=64/256 scale from tools/data/zeros_computed_10000.txt: T = the connected (non-diagonal) part of the marked third moment, T = m₃ − (D + pair). Report the realized T distribution (mean, min, max, per-window spread). This is a READ — it must be precise and honest.
2. **MIN-SIDE LP.** Extend the N=64 pool LP: objective min p₁ over the pool subject to {rows, marks, m₃ ∈ 5±ε, T ∈ [T_min, T_max]} for the same ε-grid {0.1, 0.44, 1.0, 2.98}. For each ε: report min-p₁, the binding config (its p₁, m₃, T), and the margin to 0.70. (If T isn't directly expressible per-config in the pool, bound it via m₃ − (D+pair) using the pool's per-config D/pair.)
3. **ADVERSARY IDENTITY.** If min-p₁ < 0.70: what is the worst config? (Low p₁ → high D, low pair, T ≈ +? — verify.) Can any SHARPER read exclude it? Candidates: (a) the T-window at finer ε; (b) the four-point (k=4) moment — is the adversary's k=4 out of the real zeros' range? (c) the pair part's identity is ≥ 3p₁+1.44 — is it EXACTLY 3p₁+1.44 at the adversary, or is the ≥ slack exploitable?
4. **VERDICT:** certificate value v(ε) over the class for each ε; does v ≥ 0.70 hold for any ε with the real T-window? State the number. If yes → the door is OPEN (document what remains: the certificate functional construction). If no → the binding adversary + what read would close it.

**HARD CAPS:** deliverable ~/riemann/research/waves/wave-phone-2/results/m3-min-frontier.md by your 15th tool use; write the verdict section EARLY (by 8th: identity-level analysis even before the LP); < 150K tokens; bash < 90 s (LP at N=64, 4000 configs = seconds with HiGHS or scipy linprog — check scipy: proot-distro login ubuntu -- python3 -c "import scipy; print(scipy.__version__)"); crash-proof (append after every computation); no subagents.

**Deliverable:** results/m3-min-frontier.md — realized T-range (numbers), min-p₁ table per ε, binding adversary, verdict.
**Report < 100 words:** realized T-range, min-p₁(ε) table, adversary identity, whether v ≥ 0.70 is reachable. End: RESULT: <status> — <one line>.
