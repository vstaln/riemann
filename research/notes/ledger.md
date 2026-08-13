# Wave Ledger — shared state for swarm agents

**Rule (ledger protocol):** every completed agent appends a ≤5-line verdict here: result, labels, file, next move. New agents read ONLY this ledger + their task slice — do not re-read the full wave notes (ponytail rung 1-2; the re-read tax was the swarm's #1 waste). Never re-derive a ledger verdict — cite it.

---

## Status: PHONE-BRAIN ARCHITECTURE (2026-08-12, after freeze)
The phone is the ONLY brain: it funds, specs, judges, synthesizes. Laptop + boxes are compute workers — dispatched jobs only, no autonomous swarms (laptop swarm confirmed OFF: no crons/services/tmux; box orphans killed 2026-08-12). Contract: `tools/swarm/phone-brain.md`; dispatch: `tools/swarm/phone-dispatch.sh`. Waves ≤3 agents, ledger-gated, <2M tokens/wave.

## Status: SWARM FROZEN — vertical mode (2026-08-12)
After ~800M tokens across waves 1/blast/local/orch/phone with **zero certified record improvement**, the swarm is frozen. Surviving lines: **(a) eps-certification push on the record config** (attack-record), **(b) m₃-separation / new certificate class** (super-law S₃). All other lines killed (see verdicts below — they're dead for stated reasons, not abandoned silently).

## Record (current certified): 0.673262865534356014645368000853343519319712248
config: α=1.49, psum=1/220, m=133, eps=0.00806 (certifies; 0.008065 FAILS). H(1.49)=0.6724218860964. τ=psum·(m−6)/m. B=Φ_m(ε(m−6)).

## Completed verdicts (append-only)

- **history-transport** (a20deff9, wave-phone-local) — CHECKED: ceilings break by NEW OBJECTS via partial bridges; top transports: 256-law S₃ (blocked: private data), Dirichlet-family averaging (bandwidth-1 restored, probes passed), derivative tower, Christoffel–Darboux. File: results/history-transport.md.
- **ceiling-ideas** (83405200, wave-phone-local) — CONJECTURED: two-moment ceiling UNIVERSAL — any certificate reading {mean, in-band F, integrality} is valid against the 256-law, value ≤ p₀=0.68182868746 regardless of algebraic form. Escapes: beyond-1 reads or arithmetic admissibility. Top idea: super-law+S₃ rigidity. File: results/ceiling-ideas.md.
- **finitet-synthesis** (9dbb2f9b, wave-orch-phone) — record CONJECTURED finite-T robust: formula T-free (PROVEN); measured finite-T errors positive (overshoot) at all T≤5000, flip needs ≥6.995e-5 negative error at T→∞, none seen. P5 tower probe INCONCLUSIVE (bug: mpc-vs-int at line 87 of probe/tower_probe.py, crashed, no output). File: results/synthesis-finitet.md.
- **two-tone sweep** (laptop wave-local) — two-tone windows REFUTED: c=0 (pure cosine) always optimal, H max = 0.672500703679412. The 0.6745091759 commit claim used eps CONJECTURED at psum=1/300 — NOT a record. File: wave-local/results/exec-two-tone.md.
- **eps-max search** (laptop wave-local) — p=1/1320 (psum=1/220): max certified eps ≈ 0.008064; p=1/1350 (psum=1/225): ≈ 0.007916. Marginal; the record's real lever. File: wave-local/results/exec-eps-max-runs.log.
- **idea-network** (laptop oracle-old) — 12 network ideas, 10 Rust probes reproduced (V/M=0.219, min floor 77x eps). UNFUNDED.
- **wave-blast** (laptop) — 20 idea catalogs (constraint/provocation/random/historical/systems/analogy-x1). UNFUNDED — catalogs, not results.

## Results landed (2026-08-12)
- **NEW CERTIFIED RECORD (pending re-cert): 0.67326543649552352207990181282271996377681849486392** — eps=0.008064 certified at grid=4000 (verifier log: True, 1116906 nodes); bound at m=133 = (H−τ)/(1−B/m); gain +2.5709611675e-6 over 0.6732628655. Artifact probe: eps=0.008070@g6000 FAILS at the same ~0.0080606 floor (failing box = grid-scaled image of g4000's) → boundary GENUINE, not artifact. Headline formula reproduced to 42 digits (residual 3.9e-46 = print truncation). Re-certification of 8064 in flight (attack-record, file research/waves/wave-phone-2/results/attack-record.md).
- **m₃-SEPARATION (CHECKED NUMERICALLY, ONE implementation — adversarial re-verify PENDING): super-law marked-windowed m₃(1/2)=7.98 (theory 8.148) vs real zeros PROVEN 5; m₃(2/3)=5.36 vs 13/4=3.25; ≥88σ; above pinned bottoms 5.4419/3.9825.** Verdict: super-law excluded as adversary for marked-m₃-reading certificates → NEW CERTIFICATE CLASS OPENS. Scaling bug in inherited probe fixed (prior S₃-FAIL verdicts VOID); unmarked S₃ = sine-kernel confirmed. File: research/waves/wave-phone-2/results/superlaw-s3.md. **Caveat: box independent re-verification DID NOT run (box pi hangs headless — boxes dropped 2026-08-12).**
- **Boxes: pi -p hangs headless on all 3 boxes (provider/no-tty issue); box dispatch ABANDONED for now.** Laptop = Rust/verifier worker via ssh only.
- **tower-method v1 DIED on output-limit (253K tok, 29 tools, no deliverable).** Prior art found: A4 interlacing-LP DEAD (gives no upper constraint); **T-2 derivative-tower (ξ″/ξ‴ cert + weighted distinct-ζ) ALIVE, score 375, target Farmer 0.6603 distinct-ζ record; interlacing CHECKED at 60 digits (one ξ″-zero per ξ′-gap, 20/20).** Relaunched as tower-t2.

## In flight
- **attack-record v2** (a13b96b0, wave-phone-2): prior run (killed by mobile-data loss) independently re-verified eps=8060/1e6 certifies at grid=4000 (942,944 nodes, matches discovery note), 8066 FAILS. Now: resolve 8065, probe grid-artifact question (finer grids), certified (psum,m,α) sweep. **THE priority — boundary is artifact-vs-genuine-floor.**
- **superlaw-s3 v4** (995699c4, wave-phone-2): prior run found superlaw_s3.py has FATAL scaling bug (global vs per-block spacing → counts→0 → all prior S₃-FAIL verdicts VOID); pointwise R₃ is a poor discriminator; decisive probe = WINDOWED MARKED m₃. Partial file: research/waves/wave-phone-2/results/superlaw-s3.md. Pinned bottoms: m₃ ≥ 5.4419 (λ=1/2), ≥ 3.9825 (λ=2/3) vs sine-kernel 5, 13/4 — if super-law realizes the bottom, m₃ input SEPARATES it → new certificate class.
- **tower-method (P5, THE METHOD line)** (4e423498, wave-phone-2): user directive — find a METHOD for zeros on the line, no brute force. Derivative tower: ξ′ zeros on line (FGL-family, Lean ≥0.85838 for ξ′), Rolle interlacing + N(T) count → force ξ zeros on line; missing lemma being worked out. tower_probe.py bug (line 87 mpc-vs-int) to fix.

## Resilience note (2026-08-12)
Phone mobile data dropped mid-wave (killed 2 agents). All specs now mandate crash-proofing: write deliverable EARLY, append per result, bash calls < 90 s, nohup+poll long jobs. attack-record v1 died with no file (spec lacked the mandate) — seed findings in the relaunch prompt instead.

## In flight (superseded)
- **attack-record** (d3fc79e9, wave-phone-2): adversarial re-verify + eps-max push. **THE priority.**
- **superlaw-s3** (f10a8b2b, wave-phone-2): S₃=sine-kernel check + m₃-separation test (m₃(1/2)=5 proven for real zeros vs super-law marked m₃≥5.44 → new certificate class if separated). Crash-proofed (incremental file writes).

- **weil-first-prime** (2026-08-13) — RH-horizontal. PROVEN: λ_a>0 for a<(log 2)/2, continuous, RH ⇔ λ_a>0 ∀a. CHECKED: crude |G(log 2)|≤G(0) bound = 0.980 is 620× the Ritz gap at a₂, so it cannot cross the first prime; actual G(log 2)/G(0)=7.2e-3 (overlap). Ritz stays positive through (a₂,a₃) but is an UPPER bound after O(1) cancellation to 10^{-5} — INCONCLUSIVE for positivity past a₂. File: research/notes/attack-weil-first-prime.md. Next: Yoshida finite calculation with the prime-2 rank-one update (interval K-split). Coboundary grind not resumed.
