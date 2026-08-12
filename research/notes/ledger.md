# Wave Ledger — shared state for swarm agents

**Rule (ledger protocol):** every completed agent appends a ≤5-line verdict here: result, labels, file, next move. New agents read ONLY this ledger + their task slice — do not re-read the full wave notes (ponytail rung 1-2; the re-read tax was the swarm's #1 waste). Never re-derive a ledger verdict — cite it.

---

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

## In flight
- **attack-record** (d3fc79e9, wave-phone-2): adversarial re-verify + eps-max push. **THE priority.**
- **superlaw-s3** (f10a8b2b, wave-phone-2): S₃=sine-kernel check + m₃-separation test (m₃(1/2)=5 proven for real zeros vs super-law marked m₃≥5.44 → new certificate class if separated). Crash-proofed (incremental file writes).
