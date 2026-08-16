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
- **li-literature-audit** (wave-phone-2, 2026-08-14) — SOTA audit DONE (research only): λ_n record = Johansson 2013 n=10^5 rigorous (~0.1n bits, Arb; λ_100000^K=4.6258078240690…); γ_k record = Johansson (all ≤10^5, ~10^4 digits) + Tyagi 2022 huge-n (non-rigorous); digits ≈ 0.30n+; λ_1,λ_2>0 UNCONDITIONAL (BPY 2001); RH-fail threshold n≳T²/|t| ≥ 10^25 (Voros 2022) ⟹ finite-n positivity = heuristic only; Hankel-PSD/moment claim in method-frontier-synthesis CORRECTED (no such theorem; true anchors: B–L Weil-form 2λ_n=W(g_n∗x⁻¹g_n(x⁻¹)), Suzuki L²-norm criterion 2301.05779, sin²/Chebyshev reps). File: results/li-literature-audit.md. Next: implement Johansson pipeline (Arb/python-flint, laptop) for certified λ_n≤10^3–10^4 + Hankel inertia; phone 2500–3000 dps mpmath route as independent cross-check; structural (moment/Weil) hunt is the genuinely new surface, not the record.

## Results landed (2026-08-12)
- **NEW CERTIFIED RECORD (pending re-cert): 0.67326543649552352207990181282271996377681849486392** — eps=0.008064 certified at grid=4000 (verifier log: True, 1116906 nodes); bound at m=133 = (H−τ)/(1−B/m); gain +2.5709611675e-6 over 0.6732628655. Artifact probe: eps=0.008070@g6000 FAILS at the same ~0.0080606 floor (failing box = grid-scaled image of g4000's) → boundary GENUINE, not artifact. Headline formula reproduced to 42 digits (residual 3.9e-46 = print truncation). Re-certification of 8064 in flight (attack-record, file research/waves/wave-phone-2/results/attack-record.md).
- **m₃-SEPARATION (CHECKED NUMERICALLY, ONE implementation — adversarial re-verify PENDING): super-law marked-windowed m₃(1/2)=7.98 (theory 8.148) vs real zeros PROVEN 5; m₃(2/3)=5.36 vs 13/4=3.25; ≥88σ; above pinned bottoms 5.4419/3.9825.** Verdict: super-law excluded as adversary for marked-m₃-reading certificates → NEW CERTIFICATE CLASS OPENS. Scaling bug in inherited probe fixed (prior S₃-FAIL verdicts VOID); unmarked S₃ = sine-kernel confirmed. File: research/waves/wave-phone-2/results/superlaw-s3.md. **Caveat: box independent re-verification DID NOT run (box pi hangs headless — boxes dropped 2026-08-12).**
- **Boxes: pi -p hangs headless on all 3 boxes (provider/no-tty issue); box dispatch ABANDONED for now.** Laptop = Rust/verifier worker via ssh only.
- **tower-method v1 DIED on output-limit (253K tok, 29 tools, no deliverable).** Prior art found: A4 interlacing-LP DEAD (gives no upper constraint); **T-2 derivative-tower (ξ″/ξ‴ cert + weighted distinct-ζ) ALIVE, score 375, target Farmer 0.6603 distinct-ζ record; interlacing CHECKED at 60 digits (one ξ″-zero per ξ′-gap, 20/20).** Relaunched as tower-t2.

- **li-structure-audit** (wave-phone-2) — PROVEN: zero-sum/Weil-pairing/Chebyshev forms of lambda_n are the same identity (pairing partial sums -> probe lambda_n at N=1500, tail bound 3.2e-4); B-L square-root factorization verified to 1e-60; Suzuki L2 equality shape-consistent (0.34 x lambda_n at R=100, heavy t^-1log^-2t tail); Jensen J^{d,n} hyperbolic d<=10. CHECKED NUMERICALLY: {lambda_n} and {gamma(j)/j!} are TOEPLITZ-type, NOT Hankel moment sequences (Hankel minors negative: -3.73e-3, -7.06e-5) — "Hankel PSD iff lambda_n>=0" is FALSE; Jensen criterion = PF (Toeplitz TP), never Hankel. g_n/f_n lie outside ALL unconditional Weil-positivity classes (full spectrum, |hhat|~n^2/t^2). Sharp band d~sqrt(n) = folklore, NOT theorem. Ranked certificates: Suzuki equality (quantitative refutation) > Li probes > Jensen PF; R4 Hankel-inertia ABANDONED. File: results/li-structure-audit.md.

## In flight
- **attack-record v2** (a13b96b0, wave-phone-2): prior run (killed by mobile-data loss) independently re-verified eps=8060/1e6 certifies at grid=4000 (942,944 nodes, matches discovery note), 8066 FAILS. Now: resolve 8065, probe grid-artifact question (finer grids), certified (psum,m,α) sweep. **THE priority — boundary is artifact-vs-genuine-floor.**
- **superlaw-s3 v4** (995699c4, wave-phone-2): prior run found superlaw_s3.py has FATAL scaling bug (global vs per-block spacing → counts→0 → all prior S₃-FAIL verdicts VOID); pointwise R₃ is a poor discriminator; decisive probe = WINDOWED MARKED m₃. Partial file: research/waves/wave-phone-2/results/superlaw-s3.md. Pinned bottoms: m₃ ≥ 5.4419 (λ=1/2), ≥ 3.9825 (λ=2/3) vs sine-kernel 5, 13/4 — if super-law realizes the bottom, m₃ input SEPARATES it → new certificate class.
- **tower-method (P5, THE METHOD line)** (4e423498, wave-phone-2): user directive — find a METHOD for zeros on the line, no brute force. Derivative tower: ξ′ zeros on line (FGL-family, Lean ≥0.85838 for ξ′), Rolle interlacing + N(T) count → force ξ zeros on line; missing lemma being worked out. tower_probe.py bug (line 87 mpc-vs-int) to fix.

## Resilience note (2026-08-12)
Phone mobile data dropped mid-wave (killed 2 agents). All specs now mandate crash-proofing: write deliverable EARLY, append per result, bash calls < 90 s, nohup+poll long jobs. attack-record v1 died with no file (spec lacked the mandate) — seed findings in the relaunch prompt instead.

## In flight (superseded)
- **attack-record** (d3fc79e9, wave-phone-2): adversarial re-verify + eps-max push. **THE priority.**
- **superlaw-s3** (f10a8b2b, wave-phone-2): S₃=sine-kernel check + m₃-separation test (m₃(1/2)=5 proven for real zeros vs super-law marked m₃≥5.44 → new certificate class if separated). Crash-proofed (incremental file writes).

## Adversarial re-verify (2026-08-17, main loop)

- **m3-separation re-verified** — superlaw-s3's marked-m3 separation REPRODUCED with independent implementation (own GUE sampler, seed 99, n=300): super-law marked m3(1/2)=7.935±0.041, m3(2/3)=5.348±0.033 (bias-corr) vs real zeros ≈5/3.25; gap ~2.9 ≫ noise. File: adversarial-m3-reverify-2026-08-17.md. **TWO CORRECTIONS: (1) "m3=5 PROVEN (RS96)" is RH-CONDITIONAL as a theorem (attack-ceiling §7.5(e)); certificate must read m3 as numerical enclosure (ε≈0.5-1.0), not unconditional theorem. (2) theory-formula 8.148 vs my 7.69 adjudicated: 8.148 uses mass-density-1 rescale (λ→λ·Em); measured 7.94 confirms; no contradiction.** NEXT LEVER: marked-m3-reading certificate LP — add m3=5±ε constraint (ε<0.44) to lpdual certificate, compute new in-class ceiling vs 0.6818. CONJECTURED > 0.6818, NOT YET COMPUTED.

## Wave 1 (2026-08-17, subagent army) — all deliverables verified on disk

- **L3 sos-hierarchy-transfer (d6e00e54)** — same-data Lasserre/SoS lift FAILS structurally: ceiling_law256 bounds every certificate, ceiling is degree-INDEPENDENT (PROVEN, Lean); config set non-semialgebraic (integrality not a polynomial inequality). New-data lift = marked-m₃ read (LIVE). File: sos-hierarchy-transfer-2026-08-17.md.
- **L1 lever-miner (c5401373)** — assumption-excavation on 5 walls: walls 3 (beyond-α=1) and 5 (RH-inert) genuinely HARD; THREE SOFT spots found: (A2) EnclOK is the single non-Lean link (256-law weights private), (B1) window 0.6725 subclass is a convention not a theorem (gap 0.6725→0.6818 PROVEN-open, needs only a certificate), (D2) marked-moment transfer untested. Top-3 levers: marked-m₃ LP, GS double-sum + Guth–Maynard, Bui–Heath-Brown partial unconditionalization. File: lever-miner-assumption-excavation-2026-08-17.md.
- **L4 marked-m3-certificate-LP (f7e6c7bd)** — HEADLINE NEGATIVE (honest): m₃ read with ε<0.44 excludes ENTIRE near-CUE marked family at p₁≤p₀ (old ceiling's adversary mechanism destroyed — positive), but does NOT establish ceiling > 0.6818: restricted class's min-p₁ uncharacterized; family only reaches m₃≈5 as p₁→1 (all-simple) — would raise ceiling IF certified, but no multiplicity theorem. Missing input: bound on connected part T (attack-law-s3 §6) or rigorous marked-m₃ enclosure with true multiplicities. TENSION: real-zeros m₃=5.373 sits 0.069 BELOW pinned bottom 5.4419 (needs T≈−0.07, opposite sign to sine A3=+1/2) — within noise, no contradiction. Ceiling question INCONCLUSIVE at LP level. Files: marked-m3-certificate-LP-2026-08-17.{md,py}.
- **Process note**: L4 hit 111% context (18 tool uses / 190k tokens) but wrote deliverable first → survived. TOKEN BUDGET now enforced in goal + all 7 agent files (~200k / ~15 tools / 12 turns; deliverable-first; partial note = deliverable).

## 2026-08-17 — Anthropic campaign method extracted (wave 3 foundation)
- **anthropic-method** — PROVEN: all 6 user-supplied URLs re-verified HTTP 200; 4 CDN PDFs downloaded fresh to research/papers/ (main paper 95c24693, campaign narrative d7f3ecf1, E2 transcript 8a0d1add, informal note 23455459). Full playbook extracted to research/notes/anthropic-campaign-method-2026-08-17.md: coordinator-led, research-memo briefs with forecast + RH-false control demand, blind disjoint referees with worked attack plans, orphaned-proof rescue, "point the mechanism the wrong way", 4-class ledger triage, cold-read referee, proportion≠RH firewall. /goal rewritten to this method.
- **GAP FOUND (unbuilt lever):** Anthropic rung-0 = "barrier checker" — zoo of RH-false model worlds (Epstein class-2, Davenport–Heilbronn, planted-zero Beurling, fake Weil polynomial) + claim classifier. No equivalent in tools/ (only one-off probes). Candidate next build: tools/barrier_zoo/. File: anthropic-campaign-method-2026-08-17.md.
- **Next:** either (a) sinc-kernel certificate LP with m₃ read (live mathematical lever), or (b) build tools/barrier_zoo/ (rung-0 discipline tool). Both UNTESTED. Ledger-clean, no duplicate lever.
- **CAMPAIGN-STATE.md written** — full audit trail: what failed/broke/promising, method, file map. Read this + ledger before any session work. File: research/notes/CAMPAIGN-STATE.md.
- **Infra fixes (2026-08-17):** `.lake` build artifacts (2525 files/1.7GB) untracked + gitignored (tracked now 1468 files/0.19GB); global skill inventory trimmed 1516→46 (s4h → project-local .pi/skills/); goal + hooks/agents.md + all 7 agent files updated to Anthropic campaign method (research-memo briefs, blind referees, barrier zoo, proportion≠RH firewall).
- **In flight:** barrier-zoo builder (cbe8ab6f, background) — rung-0 RH-false model zoo + 4-class claim classifier. Next lever after it lands: sinc-kernel certificate LP with m₃ read.

## 2026-08-17 — remote-claims audit + Rust-only directive + parallel wave (wave 3)

- **ADJUDICATION: remote "complete RH proof" + "90%+" claims are NOT RECORDS.** 9 commits rebased in from another machine (/root/riemann, 2026-08-12..14) claim: machine-checked Lean RH proof, 90%+ simple zeros, De Branges spectral, Li positivity. Audit (research/notes/adjudication-remote-rh-claims-2026-08-17.{md,py}): CompleteRHProof.lean's core theorem mercer_offline_zeros_elimination is a VACUOUS TAUTOLOGY — hypothesis (∀d, C ≤ C_on − 4·d·N_off) is unsatisfiable for N_off≥1 (RHS→−∞), so it assumes its own conclusion; never proves the bound for actual ζ. Verified numerically: even with C=−1e9, C_on=1e9 the hypothesis fails at d=5e8+1. GramStability.lean has 8 sorries. "90%+" contradicts PROVEN walls (beyond-α=1 closed; 5/6 distinct; in-class 0.6818). Li note proves only the trivial 1997 direction; λ_n≥0 for actual ζ (=RH) checked n≤50 only. Label: NOT-RECORD; no dispatch may build on them without independent re-derivation. PROVEN (structural + numeric).
- **barrier-zoo (Python reference) built + DH zeros certified** — rung-0 zoo landed (cbe8ab6f aborted at 95% but wrote deliverable first): 4 model worlds + 4-class classifier (tools/barrier_zoo/, note barrier-zoo-2026-08-17.md). Coordinator re-certified the Davenport–Heilbronn off-line zeros the model's t_hi=40 grid missed: **s=0.80851718245663737319+i·85.699348485377592166 and s=0.65083008060973707137+i·114.16334273075698091, |f|<1e-50 @50dps, Titchmarsh κ-combination; same zeros in f_plus (c=+ε); f_minus doesn't vanish there.** PROVEN.
- **RUST-ONLY DIRECTIVE (user, binding):** Python FORBIDDEN unless absolutely necessary (mpmath-level arbitrary precision with no Rust equivalent, justified one line in the label). No numpy/scipy/mpmath in new deliverables. Existing Python verifiers (barrier_zoo, lpdual) = reference-only, MUST be ported to Rust as the first action of any lever touching them. goal + hooks/agents.md updated.
- **PARALLEL WAVE 3 dispatched (3 disjoint levers, background, flash, Rust-only):** (A) d629da85 barrier-zoo Rust port (tools/barrier_zoo_rs/, reproduce certified DH zeros, t_hi≥130); (B) b333a18a sinc-kernel certificate LP with m₃ read (tools/sinc_m3_cert/, minilp, does m₃≥m₂² theorem break 0.6818 in sinc kernel? + RH-false control) — the LIVE lever, untested since marked-moment-inequality PROVEN; (C) f11dace2 off-centre positivity wrong-direction brief (empty-route forecast; invert = win; k<1 moving-boundary b≈0.0758 count vs LMFDB data). All deliverable-first, ≤12 turns.

## 2026-08-17 — WAVE 3 VERDICTS (all three agents landed; coordinator post-verified)

- **(A) barrier-zoo Rust port (d629da85, tools/barrier_zoo_rs/) — ABANDONED as deliverable, stub kept.** Agent died at 108% with 8 string-literal compile errors; coordinator fixed build (8 joins + 1 borrow-move). Run verdict: **math cores BROKEN — does NOT reproduce the certified DH zeros.** Gamma(2)=1.5054 (expect 1), Gamma(5)=32.4 (expect 24) → Lanczos broken, poisons all FE checks; eps(psi)=−13.877+66.587i with |eps|=68.0 (reference: |eps|=1, GaussSum/i√5) → ε wrong by construction; DH certified zeros NOT matched (|f_plus|=641, 232 at the certified locations; need <1e-9); Epstein modularity rel-diff 0.59–0.91, continuation off 3–6 orders, Dedekind false. Weil + Beurling(planted) + classifier 9/10 correct. STATUS: NOT rung-0 usable. Acceptance test (must pass before any argument is disciplined by it): reproduce certified DH zeros s=0.80851718245663737319+i·85.699348485377592166 and s=0.65083008060973707137+i·114.16334273075698091 at |f|<1e-9. Fix order: Γ first (self-test pins it), then ε(ψ)=GaussSum/(i√5), then re-run. File: barrier-zoo-rust-2026-08-17.md.
- **(B) sinc-kernel m₃ certificate LP (b333a18a, tools/sinc_m3_cert/) — CONJECTURED (binary ran; referees pending).** Coordinator fixed minilp 0.2.2 API per note §3.5; scan (eps=0.44, sinc² B=128 N=256): **min-p1 = 0.748807, κ = 0.748809 — EXCEEDS 0.6818**; eps=0.20/0.10/0.05 → κ=0.834/0.867/0.883. BUT: (i) minilp shadow-price block `Infeasible` — linearized LP at the boundary contradicts the nonlinear scan (LP encoding broken at boundary; scan/bisection is the real optimum); (ii) torus-convention read (E[m₂]=2.480620 PROVEN, theorem floor 6.1535) → INFEASIBLE — the m₃≥m₂² theorem as stated does NOT bind on the feasible branch; (iii) RH-false control: sinc² Gram σ-blind → reads(B)==reads(A) by construction, LP certifies κ*=0.7488 for a world with true on-line fraction 0.60 → **PROVES TOO MUCH for the on-line claim: κ* is a SIMPLE-FRACTION ceiling** (firewall holds: proportion-on-line theorems are zero evidence about RH); (iv) calibration-fragile: κ>0.6818 only for m₂(1)≥~2.17 (2.00→0.466, 2.11→0.608, 2.22→0.749, 2.33→0.870, 2.44→EMPTY). Real-zeros sinc m₂²=4.9256→m₂(1)=2.2198≈2.22, so the calibrated branch IS the real-zeros branch — the most promising reading, but NOT yet PROVEN. File: sinc-m3-certificate-LP-2026-08-17.md. **Next: hostile referee (blind, disjoint) on (i) marked-law model correctness, (ii) calibration convention (which m₂ does the PROVEN theorem bind in?), (iii) σ-blindness refutes on-line reading.**
- **(C) off-centre positivity wrong-direction brief (f11dace2, tools/offcentre_probe/) — PROVEN EMPTY (route dead), forecast held.** Window subclass pinned at 0.6725007 (Theorem D, Lean); class ceiling 0.6818 (ceiling_law256); beyond-α=1 closed (no proven F(α) for |α|>1). One real off-centre positivity (3+4cosθ+cos2θ=2(1+cosθ)²≥0) yields only the zero-free-region right-edge, strictly weaker than the box |β−1/2|≤b/log t the certificate needs. LMFDB data stores (index, ordinate) only → off-line count ≡ 0 → sanity check VACUOUS by construction (PROVEN; probe run confirms 0/51499, on-line ratio 0.7043, Theta(T log T) never o). m₃≥m₂² is λ-independent (Cauchy–Schwarz on eigenvalues of PSD A) → off-centre marked positivity = same theorem at shifted read point, empty as new route. File: offcentre-positivity-probe-2026-08-17.md.

## 2026-08-17 — WAVE 4 DISPATCH (4 disjoint levers, background, flash, Rust-only)
- **(1) Referee-A (d273aacb)** — hostile blind referee, joint = sinc-m3 marked-law model correctness: normalization question (certificate uses P(m=1)=2p₁/(1+p₁), E[m]=2/(1+p₁); zero-based would be E[m]=2−p₁ — which is right for the certificate's semantics?), row-0 formula, pair rows, P₃ algebra, floor=max(D+P₃,m₂²) completeness (any omitted T≥0 term?), calibration m₂(1)=2.22 (vs torus 2.480620), and the coordinator observation that at p₁*=0.7488 the binding constraint is D+P₃=5.44 (read top) with m₂²=5.02 SLACK — so the theorem is NOT doing the work, the read is. Control: 256-law at p₁=0.6818287 must be excluded (or the claim breaks). Deliverable: refereeA-sinc-m3-model-2026-08-17.md.
- **(2) Referee-B (81636ce4)** — hostile blind referee, joint = interpretation + LP/scan reconciliation: σ-blindness proof; what exactly κ*=0.7488 certifies (simple-fraction vs simple-on-line; find an RH-false world where the conclusion is FALSE — DH with certified off-line zeros is the candidate); minilp `Infeasible` vs scan (linearization invalid at max-kink? monotonicity of floor in p₁?); record-mapping (which published record would κ* break, and what input it would need). Control: fake-Weil world B. Deliverable: refereeB-sinc-m3-interp-2026-08-17.md.
- **(3) barrier-zoo math-core fix (f0f32ad5)** — fix Γ (Lanczos: Γ(2)=1.505≠1, Γ(5)=32.4≠24), ε(ψ)=GaussSum/(i√5) (|ε|=1, not 68), reproduce certified DH zeros at |f|<1e-9, Epstein modularity <1e-3, Beurling planted zero |Z(s0)|<1e-6, classifier 10/10. Acceptance = binary output. Deliverable: barrier-zoo-rust-2026-08-17-fix.md.
- **(4) re-derivation m₃≥m₂² (7f447497)** — independent proof from scratch, FORBIDDEN to read the 3 marked-moment notes; load-bearing output = which m₂ convention (marks-on-zeros E[m]=2−p₁ vs certificate's 2/(1+p₁)) the theorem binds in — decides the certificate's feasibility branch. Control: RH-inert (holds in fake-Weil world). Deliverable: rederivation-m3-2026-08-17.md.
- **L5 targets C/D (open item closed-as-superseded):** original dispatch text lost (79e96547
  died at 100% context; transcripts not recoverable by grep). A/B resolved by the m₃≥m₂²
  theorem (convention mismatch). C/D pointed into the same convention/interpretation space,
  which wave-4 referees (d273aacb model-correctness, 81636ce4 interpretation+firewall) now
  cover with fresh joints. Verdict: SUPERSEDED, do not re-dispatch.

## 2026-08-17 — WAVE 4 VERDICTS (2 hostile referees + re-derivation + barrier-zoo fix)

- **sinc-m3 certificate LP — REFUTED as a ceiling-breaker (hostile referees + coordinator check).** Both blind referees break the κ*=0.7488>0.6818 claim: Referee-A (d273aacb): the binding constraint D+P₃=5.44 needs E[T]≥0, UNPROVEN and FALSE per-config (3×3 PSD counterexample a=−0.2: m₃=1.224≥m₂²=1.1664, theorem HOLDS, yet T=−0.016<0; coordinator hand-verified trG²/trG³/P₂). Under the ONLY proven floor (S₃≥m₂²): min-p₁=0.4224 (mass)/0.5939 (count) < 0.6818 — the 0.7488 is an artifact of an unproven inequality. Convention mix: model p₁ is MASS, wall p₀=0.6818287 is COUNT (count recompute: 0.8564). Calibration knife-edge (±5% flips). Control EXHIBITED: 256-law mass-p₁=0.5173 has proven floor 5.2488 ∈ window → admissible under proven inputs. Referee-B (81636ce4): σ-blindness PROVEN; "0.7488" is a loose label (P(m=1)=0.8564 at that p₁); scan AUTHORITATIVE, minilp `Infeasible` is a global linearization artifact (tangent system infeasible ∀p₁, true problem feasible at p₁*); floor monotone through the crossing; raises NO published on-line record; on-line interpretation does NOT survive the firewall; DH simple off-line zeros kill the RH-type hypothesis. Re-derivation (7f447497): m₃≥m₂² PROVEN independently (Parseval+CS: m₃−m₂²=N²M²Var(T1)≥0, equality ⟺ uniform marks); theorem binds the sinc branch legitimately; torus 2.480620 infeasibility is outside the theorem's scope (INCONCLUSIVE). **Ledger: sinc-m3 lever CLOSED as ceiling-breaker; m₃≥m₂² theorem genuine but contributes nothing (slack at optimum). No on-line record affected.** Files: wave4-synthesis-2026-08-17.md, refereeA-sinc-m3-model-2026-08-17.md, refereeB-sinc-m3-interp-2026-08-17.md, rederivation-m3-2026-08-17.md.
- **barrier-zoo Rust — PROVEN (rung-0 tool now operational).** Builder f0f32ad5 fixed 8 root causes (Gamma off-by-half, C::exp angle in real slot, q^{+s} vs q^{-s} ×3, DH grid dt, theta origin, classifier regex). Acceptance: Γ(2)=1.0/Γ(5)=24.0, |ε|=1, FE both signs true, |f_plus|=3.1e-14 at both certified DH zeros, 2/2 matched, 6 off-line zeros found, Epstein modularity 1e-15–1e-13 + Dedekind true, planted zeros 2.3e-16/1.5e-16, classifier 10/10. Caveat: Epstein's own off-line search grid-limited (fine grid ~1000× too slow; VERDICT text overclaims there). **All briefs now disciplined through this zoo (rung-0).** File: barrier-zoo-rust-2026-08-17-fix.md.
- **Wave-5 briefs written (not yet dispatched):** M4-proper ζ″-moment r′ pin (closed-form, cheap, never dispatched) + k<1 moving-boundary Type-1 decision (empty-route proof or inversion hunt). File: wave5-briefs-2026-08-17.md.

## 2026-08-17 — WAVE 5 DISPATCH (3 disjoint levers, background, flash, Rust-only, barrier-zoo-disciplined)
- **(5A) M4-proper ζ″-moment r′ (d2d5db17)** — mechanical re-derivation of BHB Lemma 1 with
  ζ′→ζ″ (diagonal + ℳ-analogue₁,₂,₃ + convexity). Pins r′ (unknown O(1); r′=3/5 already
  REFUTED via Gonek's theorem). Forecast: r′≠3/5; outcomes (a) O(1) keeps b≤0.2237 → closed,
  (b) r′=0/negative → box-form break (surprise), (c) ζ″-moment diverges → box reduction
  invalid structurally. Control: DH + fake-Weil (working zoo). File target:
  m4-proper-zdouble-2026-08-17.md.
- **(5B) k<1 moving-boundary Type-1 decision (0a0236b5)** — is N(1/2+b/L,T)=o(T log T) at
  b≈0.0758 reachable by ANY known route? Reproduce the 3 PROVEN walls (scale-gap lemma,
  Ingham k=5, GM Littlewood–Jensen obstacle), then the E2-style inversion hunt (dual of the
  empty count; pair-identity push; BGSTB strong ZDH). Control: DH violates/weakly satisfies
  the count? File target: k1-moving-boundary-decision-2026-08-17.md.
- **(5C) exact-identity m₃ certificate (623d88bf)** — the VALID revival of the refuted sinc-m3
  lever: build on m₃ = m₂² + N²M²·Var(T1) (exact, PROVEN by wave-4 re-derivation) instead of
  the broken floor max(D+P₃, m₂²). Compute exact min/max-S₃ envelopes per p₁ (mass + count),
  recompute min-p₁, 256-law exact-S₃ control (super-law says ≈7.9 — does it survive exact
  computation?), DH flat-rows control. Verdict: beats 0.6818 or finally closes the m₃-read
  lever. File target: exact-s3-certificate-2026-08-17.md.
- **(5C) VERDICT (exact-s3-certificate-2026-08-17.md) — m₃-READ LEVER FINALLY CLOSED, does
  NOT beat the wall.** Identity VERIFIED (|m₃−(m₂²+N²M²Var(T1))| ≤ 5.8e-11, Rust probe
  tools/exact_s3_probe). Its only certified consequence is min S₃(p) ≥ (E[m₂](p))² ⇒
  min-p₁ = 0.422384 (mass) / 0.593909 (count) < wall 0.6818287 — reproduces referee-A
  proven-floor exactly. The Var(T1) term (≥0) needs a class-level lower bound ≥ 0.19 at the
  wall's mass-p₁=0.5173 to beat the wall; the identity gives none; per-config search finds
  NO in-class law at p₁≈0.68 (simple families violate flat rows 19–110×; exact-CUE ramp
  unachievable, cf. regenerate-256law). 256-law exact marked S₃ INCONCLUSIVE (config
  private); super-law ≈7.9 is excluded by its exact value but sits ABOVE min-p₁ so cannot
  lift the ceiling. DH control: barrier_zoo_rs dh works (6 certified off-line zeros, RH
  false); DH violates flat rows (CONJECTURED, literature) ⇒ outside class ⇒ certificate
  vacuous for DH, no proves-too-much. The old 0.7488 was entirely the D+P₃ artifact of the
  false E[T]≥0. Do NOT re-run this lever.


## 2026-08-17 — k<1 moving-boundary Type-1 decision (wave-5 B, tools/k1_count_probe/)
- **k1-moving-boundary** — **Type-1 NO (HIGH)**: N(1/2+b/L,T)=o(T log T) at fixed b NOT reachable by any known route. (i) Shape-1 blind (PROVEN, scale-gap); (ii) count strictly stronger than density hypothesis by TWO gaps — probe CHECKED: only (eps=0,k=0) log-free ε-free DH certifies (ratio 3.7e-2→0); every known class fails ((k=13)→1.9e16, Ingham k=44→1e59); (iii) GM loses fixed log power (PROVEN, gm-box). Inversion EMPTY (D1-D6: circular/Shape-1-walled/conjectural/vacuous). DH control: box FAILS for DH (both certified zeros β−1/2=0.3085/0.1508 beyond b/L at all sampled T; zoo re-run 2/2 matched, |f|<1e-13); firewall either branch (needs zeta-specific input, absent). Plan reallocates: M4-proper (r′) stays the live lever; 0.6818 needs a NEW OBJECT. File: k1-moving-boundary-decision-2026-08-17.md.

## 2026-08-17 — WAVE 5 VERDICTS (all three agents landed; coordinator probe-verified)

- **(5A) M4-proper ζ″-moment r′ — lever CLOSED (forecast outcome (a) confirmed).** r′ ≥ 0
  PROVEN by positivity (M=Σ|Bζ″(ρ)|²≥0 pointwise, c(M)≥0, c(S₂)=57/64) → negative r′
  impossible, quadratic form cannot be broken. r′ = 3/5 REFUTED twice: un-mollified ζ″-moment
  is (T/2π)ℒ⁶/90-scale not ℒ⁵/5 (FE substitution bracket terms carry pole orders 7/6/5 at
  s=1 → ℒ⁶); 1/(2k+1) pattern false (k=1 gives Gonek's 1/12 not 1/3). r′ VALUE not pinned by
  this route (needs ℳ₂,₁^ζ″ (log n)⁴-weighted character-sum, not in 1302.5018). New constant
  −X·ℒ⁶/180 (B=1 partial-sum, Perron residue order-7 pole) CHECKED NUMERICALLY (probe ratios
  0.445→0.485, ζ′-control reproduces validator's Gonek numbers). Consequence: b_pair ≤ 0.2237
  ceiling STANDS; b≈0.0758 dead; binding input remains the k<1 count. Control: DH + Weil PASS;
  firewall: world-independent positivity only, cannot force b≤0 anywhere.
  File: m4-proper-zdouble-2026-08-17.md.
- **(5B) k<1 moving-boundary Type-1 decision — NO (HIGH confidence): route closed, question open.** Three
  walls PROVEN: (i) scale-gap lemma (Shape-1 blind at widths < c₀/L); (ii) NEW elementary
  derivation (probe-checked): ratio of any density bound T^{A(1/2−b/L)}L^k to T log T is
  T^{A(1/2−b/L)−1}L^{k−1}, with A≥2 forced → count is strictly stronger than the density
  hypothesis by two gaps; only log-free ε-free DH (eps=0,k=0) certifies (ratio 3.7e-2 @1e10);
  Montgomery k=13 → 1.9e16, Ingham k=44 → 1e59; crossover b*(T) grows 54→283, never fixed;
  (iii) GM Littlewood–Jensen loses a fixed log power. Inversion hunt EMPTY (all 6 duals: D1
  circular, D2 Shape-1-walled, D3 needs N(1/2,T) open, D4 0.6818 already proven, D5 BGSTB
  open no unconditional input, D6 b≤0.2237 proven). DH control: box FAILS for DH at all
  sampled T (b=0.0758 AND 0.2237; β−1/2=0.3085/0.1508, 2/2 matched) → count needs zeta-
  specific input (absent) or holds for RH-false object (zero evidence); firewall holds either
  branch. Plan action: 0.6818 needs a NEW OBJECT, not an in-class sharpening.
  File: k1-moving-boundary-decision-2026-08-17.md.
- **(5C) exact-identity m₃ certificate — m₃-read lever FINALLY CLOSED.** Identity
  m₃=m₂²+N²M²Var(T1) verified to 5.82e-11 (probe); its only certified consequence is
  min S₃(p) ≥ (E[m₂](p))² → min-p₁=0.4224 mass / 0.5939 count, INDEPENDENTLY reproducing
  Referee-A's proven-floor numbers; count 0.5939 < 0.6818 → does NOT beat the wall. Old
  0.7488 entirely an artifact of the false E[T]≥0. 256-law exact marked S₃ INCONCLUSIVE
  (config private); super-law sibling 7.9 excluded by exact value but its count-p₁=0.679 sits
  above min-p₁ so cannot lift ceiling. DH control: violates flat rows (CONJECTURED, lit) →
  outside class → certificate vacuous for DH, no proves-too-much. Variance term can only
  raise min-p₁ but the identity provides no class-level lower bound.
  File: exact-s3-certificate-2026-08-17.md.
- **SYNTHESIS: three consecutive in-class levers (marked-m₃ LP, off-centre positivity, M4-r′,
  k<1 count) all closed; lesson reinforced — the 0.6818 wall needs a NEW OBJECT/INPUT, not a
  sharper inequality.** Live threads for next wave: (i) new-object hunt (what object/input is
  NOT in the certificate's {mean, in-band F, integrality} class?); (ii) Anthropic's own route
  (rank–trace on finite compression of Weil's Hermitian form — the repo has 0.673481 via
  7-point stability; pushing THAT toward 0.6818 with a better compression/weight is an
  in-class-but-unexplored direction, distinct from the closed certificate class); (iii) the
  torus E[m₂]=2.480620 definition (INCONCLUSIVE, cheap).

## 2026-08-17 — WAVE 6 DISPATCH (mission-critical: adversarial validation of the 0.673481 record)
Context: records-vs-anthropic note labels 0.673481/0.836740 UNCONDITIONAL and above Anthropic's
0.6725/0.83625 — if true, we already hold the record. But FINAL-RECORD: no Lean formalization,
no second-machine audit; the (1−B/m) redistribution lifts above the proven window ceiling
0.6725007 — a sinc-m3-style algebraic-move risk. Wave 6 = hostile blind referees on the
record chain BEFORE any new-record hunt:
- **(6A) redistribution algebra** — re-derive bound=(H(α)−τ)/(1−B/m) from first principles;
  isolate the exact certified inequality; attack the division move.
- **(6B) transfer to ζ** — state the exact theorem 0.673481 proves (liminf N_s/N ≥ 0.673481
  unconditionally?); Montgomery F=1 on [0,1] at grid points incl. j=N edge; rate handling.
- **(6C) second-machine re-derivation** — fresh implementation, reproduce 0.6734808616745137
  AND re-certify eps=0.0062 (630 fails / 620 passes) without reading the verifier's code.
Blind, disjoint. Files: wave6-briefs-2026-08-17.md, wave6-referee{A,B,C}-2026-08-17.md.

## 2026-08-17 — WAVE 6 partial: 6A landed INCONCLUSIVE-leaning-VALID; coordinator RESOLVES the blocker
Referee 6A (cae841fe): arithmetic exact; B decoded = 2√((m−1)/m·A)−1+A/m (A=eps·(m−6)) — the
concave Bellman cap, reproduces all four certified records; verifier sound; no E[T]≥0 trap;
1−B/m=0.994018>0 unconditionally. BLOCKER: the derivation of why eps enters the denominator
(1−B/m) was "not stated as a theorem in any note read" — verifier certifies only F_B≥eps, not
the rank–trace bridge.

COORDINATOR RESOLUTION — the bridge EXISTS in the external tawan repo:
research/external-results/tawanerguo-zeta-simple-zeros/archive/original/JOINT_WINDOW_PROOF.md
§6–7 is the full analytic chain: (6.1) S ≥ H_α·N + D(M°) − o(N) [stability rank–trace];
(6.2)–(6.5) D(G) ≥ Φ_m(E), B := Φ_m(A), A=eps·(m−6) [PROVEN Cauchy–Schwarz envelope, two
branches, k≥2 and k=1 cases fully derived]; (6.6) D(M°) ≥ (B/m)S − τN − o(N) [pinching,
shift averaging, τ=(m−6)/(320m)]; (7.1) substituting ⟹ (1−B/m)S ≥ (H_α−τ)N. **The minus sign
is FORCED by the algebra: S ≥ H·N + D and D ≥ (B/m)S − τN ⟹ (1−B/m)S ≥ (H−τ)N.** The repo's
record instantiation (α=1.464, m=171, eps=0.0062, psum=1/320) checks numerically:
A=1.023 > m/(m−1)=1.00588 (sqrt branch correct), B=Φ₁₇₁(1.023)=1.02292821035354 (record's B
1.02292821), τ=(m−6)/(320m)=0.00301535087719 (record's τ exact), bound=(H−τ)/(1−B/m)
=0.673480861674513644 vs record 0.6734808616745137 → MATCH 1e-15. Coordinator command:
uv run --with mpmath python3 heredoc (in transcript).
⇒ 6A's blocker RESOLVED: the record's value rests on a PROVEN analytic chain (external tawan
proof §6–7 + local Bellman certificate F_B≥eps + coordinator-verified arithmetic). Remaining
honest caveats (tawan §8 trust boundary, verbatim): general-window import, central-overlap
asymptotics, independent-implementation audit → these are exactly joints 6B and 6C.

## 2026-08-17 — WAVE 6 VERDICTS (record-validation wave — 4 of 5 joints landed)
Mission-critical pivot: the repo's certified 0.673481/0.836740 may ALREADY be the world record
(beats Anthropic 0.6725/0.83625 and PRZZ 0.417). Wave 6 = hostile blind referees on the chain.

- **6A redistribution algebra (cae841fe):** INCONCLUSIVE-leaning-VALID → **BLOCKER RESOLVED by
  coordinator**: the (1−B/m) division is PROVEN via tawan JOINT_WINDOW_PROOF §6–7 ((6.1) S ≥
  H_α·N + D(M°) − o(N); (6.2)–(6.5) D(G) ≥ Φ_m(E), B := Φ_m(A); (6.6) D(M°) ≥ (B/m)S − τN;
  (7.1) ⟹ (1−B/m)S ≥ (H_α−τ)N). Minus sign FORCED by algebra, verified to 1e-15.
- **6B transfer to ζ (c5e668e3):** structurally sound unconditional liminf (no RH/PCC/RMT);
  exact theorem: liminf N_s(1/2,T)/N(T) ≥ 0.6734808616745137; only three unconditional inputs.
- **6C second machine (358dd28d):** REPRODUCES to 1e-16 (fresh Rust f64, Gauss–Legendre,
  no mpmath, no tools/ code): H(1.464)=0.6724674255777883 (2.2e-16), bound chain
  0.6734808616745138 (1.1e-16), B=Φ_m to 3e-14, leaderboard cross-checks pass, eps=0.0062
  consistent (620 pass/630 fail).
- **6D endpoint r(1)=0 (f6ae43df):** link CLOSED with a CORRECTION to 6B. With fixed N=256 the
  cumulative form-factor limit is the step function Σ_{j≤256x}j/256², NOT x²/2 — so
  D_ζ(1)→1/512=0.001953125≠0, E_ζ(1)→−1/(6·256²)=−2.5431315104e-6≠0 (coordinator re-verified
  exactly — reproduces ceiling_law256's own coefficient 2.5431316e-6, a striking internal
  consistency check). 6B's "all → 0 by Montgomery" was WRONG (W1); the transfer survives
  instead via BGSTB24 Thm 1's UNIFORMITY at α=1 (F(1,T)→1, s_256(T)→1/256): s_j(T)→j/256²
  for all 256 points, liminf p₁ ≥ v_discrete = c₀+Σ(j/256²)r(j/256) unconditionally.
  r(1)=0 NOT needed. The certified quantity is the DISCRETE value; the 16-digit constant is
  exact iff the record is v_discrete, else corrected downward by ≤1e-5 (still ≫ 2/3).
- **6E (4f6d7b7b)** in flight: pin explicit (c₀,r), settle discrete-vs-continuum identity.

**Current label:** CHECKED NUMERICALLY (three independent implementations) + PROVEN analytic
bridge (tawan §6–7) + structurally sound unconditional transfer (6B, corrected by 6D) + 6C
machine-precision reproduction. NOT yet Lean-formalized; 1M-node interval certificate not
re-run on a second machine. Pending 6E: the discrete-value identity of the exact 16 digits.
Files: wave6-synthesis-2026-08-17.md, wave6-referee{A,B,C,D}-2026-08-17.md,
wave6-briefs-2026-08-17.md.

## 2026-08-17 — WAVE 7 DISPATCH (record-securing phase, 3 disjoint levers, background, flash)
After wave-6 validated the 0.673481 record through 5 hostile blind referees (unconditional
liminf, discrete-value identity pinned), the campaign shifts from record-hunting to
record-securing. Remaining caveats are documentation/formalization/machine-reruns, not math.
- **(7A) explicit certificate documentation (0ef045ad)** — write down the record's (c₀, r):
  c₀=H(1.464)−τ=0.6694520747005951, r piecewise-linear on knots j/256, r(1)=0; Rust probe
  verifies Σ(j/256²)r(j/256)=0.0040287869739185 → 6E's verdict (i) certified. File:
  wave7-certificate-documented-2026-08-17.md.
- **(7B) second-machine interval re-run (0345ba1e)** — re-run the 1M-node Arb interval
  certificate (α=1.464, eps=0.0062, grid=4000) under a DIFFERENT numerical configuration
  (fresh Arb build / grid=8000 / independent core); confirm verified=True, ~1,096,556 nodes
  (3 runs), 630/1e5 fails. Closes 6C's caveat. File: wave7-secondmachine-interval-2026-08-17.md.
- **(7C) new-object frontier scan (81533131)** — is 0.6818 the terminal ceiling? Scan the
  verified-literature corpus for (a) PROVEN |α|>1 form-factor slivers, (b) PROVEN simple-
  fraction p₁>0.6818, (c) genuinely new certificate inputs; verdict per class. File:
  wave7-newobject-scan-2026-08-17.md.

## 2026-08-17 — WAVE 7 VERDICTS (7A done, 7B died → re-dispatch, 7C terminal)
- **7A (0ef045ad) — CERTIFIED.** Explicit certificate documented: r(x)=K·(1−x),
  K=(B/m)·v/(1/6−1/393216)=0.0241730906956031, r(1)=0, knots j/256; knot-sum
  Σ(j/256²)r(j/256)=0.0040287869739185 (=β·v, |diff| 8.7e-19); v_discrete=v_chain=
  0.6734808616745140 (diff 3.3e-16); exact rationals PASS (τ=11/3648, Σj/256²=257/512,
  Σ(j/256²)(1−j/256)=1/6−1/393216). 6E's verdict (i) certified. Rust probe:
  tools/wave7_certificate_doc/ (+ r_knots_table.txt 256 values). Caveat: affine r realizes
  the forced identity (the original run's hidden r was never stored) — documented.
- **7B (0345ba1e) — DIED, no deliverable** (6 tool uses, 62% context, no output; the 1M-node
  Arb run likely timed out). RE-DISPATCHING with a lighter contract: partial note first,
  run the verification as a background process, allow grid=8000/different Arb build as the
  second-machine proxy, report node count + verified=True/False.
- **7C (81533131) — TERMINAL VERDICT.** All three new-object classes EMPTY:
  (a) no unconditional |α|>1 form-factor sliver (BGSTB24 bandwidth-one; T^{−2α} atom vanishes;
  bgst-2501.14545 = published erratum fixing GM87 Lemma 8 misapplication, no consequential
  damage — foundational input survived); (b) no unconditional p₁>0.6818 (19/27 RH-conditional,
  CGdL20 0.6792 RH + below ceiling anyway); (c) no new proven certificate input bridged
  (moments proven to add nothing in-range, kλ<2). Even CONDITIONAL pair-correlation results
  sit below our unconditional 0.6734808616745137. ⟹ **0.6818 is the terminal ceiling;
  0.673481 is the terminal in-class record.** Live frontier exists only OUTSIDE the class:
  dual-LP closing (0.6725→0.6818, in-class, ceiling-bounded), ξ′-target transport (Lean
  0.85838 unconditional), or conjectural regime (explicitly labeled).

## 2026-08-17 — WAVE 7 COMPLETE (synthesis committed)
- 7A CERTIFIED (explicit (c₀,r), knot-sum 8.7e-19, v_discrete=v_chain 3.3e-16).
- 7B CLOSED: primary grid=4000 re-verified True/1,096,556 nodes on a DIFFERENT machine
  (python-flint 0.9.0, host void); grid=8000 also True/1,097,508 (stronger discretization);
  630/1e5 fails terminal-cell low=0.0062867<0.0063 — 6C caveat (iii) closed and strengthened.
- 7C TERMINAL: all new-object classes empty; 0.6818 proven terminal ceiling; 0.673481
  terminal in-class record. Even conditional pair-correlation results < 0.673481.
- Campaign: record-securing COMPLETE. Record = 0.6734808616745137/0.8367404308372568
  unconditional, documented, machine-re-verified, terminal-in-class. Remaining: Lean
  formalization (long), writeup, external review. File: wave7-synthesis-2026-08-17.md.

## 2026-08-17 — WAVE 8 DISPATCH (DIRECT RH ATTACK — the pivot)
User directive: "instead of increasing the bounds, let's just prove it directly." The
proportion-on-line campaign is terminal (0.6818 ceiling Lean-PROVEN; 0.673481 record
secured). Five disjoint DIRECT attacks on classical RH equivalences launched in parallel
(background, flash):
- **8A Li criterion (a6ea1424)**: RH ⟺ λ_n ≥ 0 ∀n (Li 97, Bombieri–Lagarias 99); λ_n from
  ξ-derivatives/power sums, n ≤ 10⁴; residual-vs-low-zeros fingerprint; planted-zero control.
- **8B Speiser (3a3734c9)**: RH ⟺ ζ′ ≠ 0 in 0<Re<1/2; certified ζ′ census in left half-
  strip to T=5000; DH-type control must show off-line ζ′ zeros.
- **8C Nyman–Beurling/Báez-Duarte (3e92e7ee)**: RH ⟺ d_N → 0, d_N = dist(1, span{{1/(kx)}})
  in L²(0,1); Gram closed forms, decay fit, optimal-coefficient structure; control saturates.
- **8D Turán/Laguerre (dccc6955)**: LP necessary conditions on Ξ's Taylor coeffs from the
  Φ-moment integral; ANY negative T_k or L_k(t) ⟹ non-real zeros (unconditional disproof
  route); min-margin order; control fails at some order.
- **8E Beurling operator (3a4ef80f)**: structural twin of 8C; λ_min(G_N) decay + eigenvector-
  content vs Burnol's explicit-formula kernel; RH ⟺ λ_min(N) → 0 at cited rate.
Firewall: none of these uses the 0.673481 proportion theorem as input — these are the real
thing (proportion theorems are zero RH evidence).
Briefs: wave8-briefs-direct-RH-2026-08-17.md. Goal reset to direct-RH mission.

## 2026-08-17 — KILL-ROBUSTNESS + LANGGRAPH ORCHESTRATOR (infrastructure)
- User killed the session to install a plugin (langgraph). Two infrastructure upgrades:
  1. **agents.md kill protocol** (all 7 agent configs + hooks/agents.md): write-ahead
     deliverable (note after ≤3 reads / first 5 tool calls), progress log
     (research/notes/<task>.progress appended after EVERY tool call), state-on-disk
     (numeric results to files immediately), idempotent resume (read .progress first,
     continue, never restart), coordinator rescue after any kill.
  2. **Checkpointed LangGraph orchestrator** (tools/campaign_orchestrator/): campaign
     state machine (DEFINE→DISPATCH→MONITOR→CONSOLIDATE) on SqliteSaver — every
     super-step durable; `resume`+`step` continues exactly where a killed process died;
     kill_log keeps the honest audit trail. pi is the hands (subagent tool), LangGraph
     is the brain (state + decisions). Python sanctioned ONLY here (user authorized).
- Wave-8 (5 direct-RH levers) was killed mid-flight; re-dispatched as 8A-r2..8E-r2 with
  kill protocol in-brief: 8A Li (a17b490f), 8B Speiser (477dc8a8), 8C Nyman-Beurling
  (d52ca673), 8D Turán/Laguerre (67a787f2), 8E Beurling operator (d43bdc5a).
  Orchestrator tracks all five as DISPATCHED; kill-log empty.

## 2026-08-17 — WAVE 8 LEVER 8B (Speiser ζ′ census) — LANDED (CHECKED NUMERICALLY)
- **Verdict: ζ′ left-half-strip census EMPTY to T=5000** (two independent methods, certified
  contour margins > 4.8e-2, winding 0 on all 50 slabs over [0.001,0.5]×[10,5000]) —
  evidence consistent with RH; NOT a proof (finite computation). Control VERIFIED first:
  fake f=ζ·G with planted off-line zeros (0.3+15i, 0.25+28i) shows f′ left-strip winding=2.
- Theory corrections (the inversion): (i) ζ′(1/2+it)=e^{−iθ}(−θ′Z−iZ′) ⟹ ζ′ vanishes on the
  line ONLY at multiple zeros of ζ (simple: none); interlacing belongs to ξ′ — 4521 ξ′
  zeros on [10,5000] = RvM N(5000)+1, one per gap (matches xiprime). (ii) ζ′(σ)<0 on real
  (0,1). Right half-strip: **2651 ζ′ zeros in [0.5,1]×[10,5000]** (step-stable), ratio
  2651/N(5000)=0.59, per-slab ratio rising 0.15→0.69 — a live object for a future lever
  (the ζ′ strip-zero count theorem, cf. Levinson–Montgomery/Berndt).
- Files: tools/wave8b/ (em.rs certified Hurwitz ζ,ζ′ + winding + refine), 
  research/notes/wave8b-speiser-2026-08-17.md, wave8b-speiser.progress (18 lines).
- Orchestrator: lever 8B → DONE (first live closure through LangGraph).

## 2026-08-17 — WAVE 8 LEVER 8A (Li criterion λ_n) — LANDED (CHECKED NUMERICALLY)
- λ_n = Σ_pairs[2−(1−1/ρ)ⁿ−(1−1/ρ̄)ⁿ] over 924,715 cached zeros (γ≤5.6e5); n≤10⁴.
  On-line zeros ⟹ termwise 2(1−cos(nφ)) ≥ 0 (λ_n ≥ 0 automatic under RH); σ<1/2 ⟹
  |1−1/ρ|>1 → −∞ (control signature).
- Anchors: λ₁ = 1+γ/2−log(4π)/2 = 0.023095708966 — sum+tail matches to 2.7e-10; model
  self-check |direct−series| = 1.6e-14 (rug 192-bit); λ₂..λ₅ close to Keiper.
- Control VERIFIED first: planted 0.6±14.13i / 0.4±14.13i ⟹ λ'ₙ < 0 first at n=21848,
  envelope e^{0.00050n} exponential (way beyond polynomial RH prediction).
- Real case: λₙ > 0 ∀n ≤ 1000; residual |rₙ| ~ 0.26·n^0.246 (sub-√n); periodogram of rₙ
  peaks at the three lowest-zero frequencies φ(γ₁,γ₂,γ₃) — fluctuation IS the signal.
- Two Rust bugs caught by independent python cross-check and fixed (planted 1/ρ real part;
  RvM initial-guess NaN masked by f64::max). NOT a proof (finite data, tail corrections,
  residual-vs-RH-bound comparison is CONJECTURED-usage). Files: tools/wave8a/,
  wave8a-li-criterion-2026-08-17.md, wave8a-lambda-table.txt, .progress.
- Orchestrator: 8A → DONE.
- **stieltjes-sfraction (g1-2, 2026-08-15)** — lever = EXACTLY equivalent to RH (classical Stieltjes S-fraction theorem, Wall Ch.IX; same object as g1-1 foster-reactance, CITED, class 2 restatement; finite checks deflating class 3, no uniform control). WALL test EXECUTED (foster left it unrun): controls fail S-fraction positivity at small exact order — toy (1+t²)cos n*=0 (K_0=s_3<0, q_1=s_2/s_1<0), planted 2i n*=1, planted 1+50i n*=1, planted first-zero-shift 0.6+14.13i n*=1-2; REAL20/SEP20 all-real models PASS through k≈16-19 (numerics: f64 Hankel signs unreliable n≥7, reciprocal S-fraction exact at small k — documented); far pair |ρ|=1e6 INVISIBLE below fp noise (log-boundary, consistent). DH NOT RUN (needs L-function machinery). CORRECTION (coordinator, verified by re-running tools/foster_check/foster_check): the claimed 'foster pipeline broken, m_0=9.06' is FALSE — foster's actual output is m_0=0.023104993115419 (published 0.02310499311541837), b_0=0.4971=xi(1/2); its a_18+ collapse is a documented f64 precision limit caught by its own 200-digit cross-check (first non-positive = NONE). Stieltjes agent misread foster's output; suspect-the-check rule applied, foster result stands. Verdict: no new route; discrimination boundary measured for 4 control classes. Files: research/notes/stieltjes-sfraction-2026-08-15.md, tools/stieltjes_sfrac_controls.rs.
- **total-positivity (g0-0/g3-0, 2026-08-15)** — INVERSION delivered: the brief's "prove (b_{i+j}) TP" is PROVEN WRONG-DIRECTED — under RH the Hankel matrix is NOT TP; RH actually forces the ALTERNATING signature sign det(b_{i_a+j_b}) = (-1)^{r(r-1)/2} (Turán/Newton family, wave8d's lever). NEW VERIFIED DISCRIMINATOR (coordinator re-ran tools/tp_hankel_probe, output research/notes/total-positivity-2026-08-15.out): real case D_n alternates exactly for n=1..8, T_k>0, min t_k(k+1)=1.0696; planted control (gamma_2 -> 0.35±21.1i) breaks the alternation at D_4 (sign - , expected +) while T_k>0 still passes — D_4-alternation is STRICTLY SHARPER than Turán positivity. All-real control keeps alternation (consistent, RH-true). Edrei/ASW growth hypotheses auto-satisfied (F entire order 1/2, sum 1/gamma^2 < inf); the sign, not growth, kills TP. Status: discriminator CHECKED NUMERICALLY; needs hostile blind review before any claim. Files: research/notes/total-positivity-2026-08-15.md, tools/tp_hankel_probe/.
- **foster-reactance (g1-1, 2026-08-15)** — transfer PROVEN equivalent-to-RH (class 2 restatement): RH <==> Re F >= 0 for Re s>0, F = d/ds log Xi; <==> Foster partial fraction c_k>=0; <==> S-fraction of g = F/(2s) all-positive. Finite C-fraction check BUILT and PASSES (a_1..a_40 > 0 at 200-digit precision; f64 collapse past a_18 documented and caught by the 200-digit cross-check). Same object as g1-2 (stieltjes); no new route, working tool for reuse. Files: research/notes/foster-reactance-2026-08-15.md, tools/foster_check/.
- **lee-yang-asano (g2-1, 2026-08-15)** — VERDICT ABANDONED (section route): Lemma LY (all Taylor sections G_N disk-stable) is FALSE — CHECKED NUMERICALLY: min|root| of G_N dips below 1 at N=12 (0.982) -> 0.941 (N=16) -> 0.909 (N=30); 30 roots inside |w|<1 at N=30. (Coordinator fixed the agent's Phi bug: wrong exponents e^{9u}/e^{4u}/no-2 gave b_0=0.142 anchor FAIL; corrected to verified wave8d form e^{9u/2}/e^{5u/2}/e^{2u} x2 -> anchors PASS b_0=0.497120778188=xi(1/2), c_0=0.5=xi(1).) Each h_u = cosh(u(1+w)/(1-w)) IS circle-stable (PROVEN); G is the Phi-weighted integral over them; whether the integral preserves stability IS RH — residual CONJECTURED handle, no contraction mechanism (Asano needs products, we have a sum). RH untouched by the failure. Files: research/notes/lee-yang-asano-2026-08-15.md, tools/lee_yang_sections.rs.

- **8D-completion-harvest** (2026-08-17) — CHECKED NUMERICALLY (with artifact correction): T_k/t_k table k=1..200 VALIDATED (min t_k·(k+1)=1.06963238 at k=1 ≥ 1 ✓, no blow-up, two independent quadratures agree). L_k(0) k≤20 closed-form EXACT. **L_k k=9..20 t>0 negatives = ARTIFACT**: Taylor-derivative series with 201 b_k diverges at t≳35 (series Xi(56.5)=31.1 vs true 8.8e-18, off 10¹⁹); zeta-direct L_3(56.5)=+8.87e-32, L_3(40)=+1.66e-21 both POSITIVE. k=1..8 [0,60] min +9.6e-11 stands (control, product-form). Discriminator mechanism PROVEN (L_k fires RH-false via e₂·e₃). File: research/notes/wave8d-turan-laguerre-2026-08-17.md. Next: L_k t>0 extension needs zeta-direct evaluator (rug lacks Complex::zeta; would need EM-Hurwitz path) — LOW priority; T_k table already delivers the ≥1 margin bound.
- **lee-yang-integral-handle** (2026-08-17) — ABANDONED (exact proof): superposition principle of circle-stable {h_u} family FALSE — cosh(ζ)+ε·cosh(2ζ) (both exact h_u blocks, ε>0) has interior zeros ∀ε∈(0,1), Rust-verified (16/40 random superpositions fail); handle reduces (PROVEN) to Riemann's 1859 integral L(s)=½π^{−1/4−s/2}ζ(1/2+s)[2Γ(9/4+s/2)−3Γ(5/4+s/2)], RH ⟺ L(ζ)=−L(−ζ) unsolved. File: lee-yang integral note (agent). Next: none — closed.

- **8C-burnol-rate** (2026-08-18) — CHECKED NUMERICALLY: d_N·√(log N) ≈ 0.2131 ± 0.0018 (0.85% band) FLAT over N=100..1250 (f64 Cholesky, kappa≤1e5) ⟹ d_N ~ 0.213/√(log N) = Báez-Duarte conjectured sharp rate (log N)^(−1/2). Prior "d_N·√N·√(log N) doesn't stabilize" (2026-08-15) was the WRONG normalization: under d_N~c/√(log N) that product MUST grow like c√N — expected, not discriminating. Consistent with Burnol lower bound (strictly weaker). Trust limits: MPFR certification only to N=100 (d_N==f64 to 6.3e-13); N≥100 flatness rests on f64. File: research/notes/wave8c-burnol-rate-2026-08-18.md. Next: certified MPFR extension N∈{2000,3000,5000} (bounded, one N per run) to pin the constant past f64 regime — THE strongest live lever.
- **8C-certified-dN** (2026-08-18 night) — CHECKED NUMERICALLY + dd-refined to 1e-28: flat law d_N·√(ln N) ∈ [0.211,0.215] CERTIFIED at N=100,1000,2000,3000 (d_ref: 1.0013883664e-1/8.055653e-2/7.782135587726e-2/7.459524862924e-2) — Báez-Duarte sharp rate (log N)^(−1/2) c≈0.213 holds across 1.5 decades. hiN.rs REPAIRED (6 bugs: dd_sqrt repelling fixed-point, dd_add QD, EM half-term SIGN BUG in main.rs z_table_f64 → corrected d(50)=1.0793710431e-1, d(100)=1.0013883664e-1 (−7e-8 rel, flatness unaffected), adaptive P, overflow guards). validate ALL GREEN. mpfr-chol skip n>=3000 patched (46GB OOM on 9GB box). Files: research/notes/wave8c-burnol-rate-2026-08-18.md, research/notes/hiN-repair-report-2026-08-18.md, tools/wave8c/src/bin/hiN.rs. Next: prod 3000 rerun with patch (clean RESULT line), adjudicate 5000.

## 2026-08-18 — WAVE 8C HI-N CERTIFIED EXTENSION COMPLETE (burnol-rate note, coordinator+pi joint)
- d_N Baeez-Duarte certified to N=5000: d(2000)=7.782135587726e-2, d(3000)=7.459524862924e-2,
  d(5000)=7.252577566170e-2 — each dd-refined to residual ~1e-27 (exact solve of stored Gram),
  MPFR-256 independent solve at 2000 rel 0.0, full dd pipeline end-to-end gap 3.6e-12@2000,
  dd-vs-MPFR Gram entries 1e-27..1e-28 at N up to 5000. CHECKED NUMERICALLY.
- FLAT LAW d_N*sqrt(ln N) in [0.2111, 0.2149] (mean 0.2129) across N=50..5000 — the
  BD sharp rate (log N)^(-1/2) holds within +-1%; constant OSCILLATES +-1% (not monotone).
  Not RH evidence either way; strengthens the rate conjecture. Note updated with verdict.
- BUG CORRECTIONS (published values shift ~7e-8 rel; flatness unaffected): EM half-term
  sign bug in main.rs z_table_f64 (inherited by all published 8C d_N); P=32 tail truncation
  (6.6e-11 on G_11) -> adaptive P(L). d(50) 1.0793711120e-1 -> 1.0793710431e-1;
  d(100) 1.0013884399e-1 -> 1.0013883664e-1.
- hiN.rs pipeline bugs found+fixed by validation ladder (dd_add QD, dd_sqrt reciprocal-Newton
  anti-convergence, sampling rng range 2^43->2^53 [46GB crash root cause], counter-wrap race,
  false-sharing row claim). Coordination: pi session co-worked (repair + docs); coordinator
  overruled its "defer 5000" (conflated ddgram-5000 memory with prod-5000; refinement covers
  kappa~1e6 — confirmed by the landed run).
- NEXT (8C lever): nothing certified-blocking; natural follow-ons: (a) oscillation structure
  of c(N)=d_N*sqrt(ln N) vs low-zero frequencies (periodogram, cf. wave8a residual analysis);
  (b) N=8000+ needs only patience (f64+refinement; ~4.5h/N on this box).
- **8C-chain-complete** (2026-08-18 08:05) — CHECKED NUMERICALLY, CERTIFIED: d(5000)=7.252577566170e-2, d·√(ln N)=0.211661; flat law d_N·√(ln N)∈[0.211,0.215] at N=100/1000/2000/3000/5000 (1.7 decades, dd≤3.9e-27). Layer-D ddgram 2000 (9,758s): d_dd=7.782135587442e-2 vs d_ref 7.782135587726e-2 (abs gap 2.84e-12, rel 3.65e-11 — CORRECTED from earlier factor-10 "3.6e-10" slip at harvest) — full dd pipeline confirms; certification ladder closed at 2000 (f64+dd-ref+MPFR+layer-D). HARVEST.txt in tools/wave8c/results/. File: wave8c-burnol-rate-2026-08-18.md (UPDATE 3).

## SWARM WAVE-13 DISPATCH (2026-08-18 morning, pi-native background agents, Anthropic recipe)
- **R1 (f1e7a6f1) coboundary-reopt** — record lever: LP search for redistribution (l,c) certifying
  eps>0.0062 (tawan's eps ceiling; test-family PROVEN closed at H=0.6725007). Fallback: m-sweep on
  bound (H−τ)/(1−B/m). Ground truth = interval verifier tools/verify_coboundary_floor.py.
- **D1 (e4e01e05) 8C-chain-harvest** — harvest ddgram2000/prod5000/sample5000 → flat-law verdict N≤5000.
  (SUPERSEDED by coordinator's own commit 2698c23: chain already complete, N=5000 certified.)
- **D2 (7475232a) lk_zeta zeta-direct** — build+run tools/wave8d/src/bin/lk_zeta.rs, error-bound pass
  (Richardson h/2,h/4), verdict per flagged point; xi sanity check vs γ₁..γ₄ first. INCONCLUSIVE valid.
- **D3 (54250369) de Bruijn heat probe** — direction verdict first (t>0 direction EMPTY per DN-constant
  equivalence Λ≤0⟺RH; heating is the wrong side), then t<0 zero-tracking probe (RH-consistent evidence
  only, NOT a proof step).
- Referees: dispatch blind hostile referee per landed result (R1→bound arithmetic+verifier independence;
  D2→L_k sign; D3→DN-direction claim).
- **8D L_k zeta-direct COMPLETE** (2026-08-18, D2 7475232a) — NO RH DISPROOF. Certified evaluator
  (zeta_em_ders zeta^(0..21), n=600 EM override, Stirling polygamma, Bell composition; sin_cos phase
  bug found by sanity gate and FIXED). 4/7 decisive POSITIVE (L3(56.5)=+8.868e-32 mpmath 0.4%,
  L8(33.6)=+2.166e-17 CD 0.3%, L4(35.5)=+1.022e-18, L3(40)=+1.657e-21 mpmath 0.2%); 3/7 INCONCLUSIVE
  (k=18/19/20 @ t=40, error ≥ signal, one neg −3.95e-19 within 1.6e-18 error — no RH signal).
  ROOT CAUSE CONFIRMED: earlier L_k negatives = Taylor-truncation artifacts (series diverges t≳35).
  File: wave8d-lk-zeta-direct-2026-08-18.md (+ run txt). 8D closed: no disproof, no positive RH evidence either (positivity of L_k is NOT RH — known to hold numerically to 1e5).
- **de Bruijn heat lever CLOSED** (2026-08-18, D3 54250369) — DIRECTION VERDICT PROVEN: wave-20
  g2-2 t>0 route EMPTY (premise ⟺ Λ≤0 ⟺ RH by de Bruijn–Newman + Rodgers–Tao; proving it is RH).
  "Single t>0" version FALSE (Gaussian counterexample: H_0 all non-real → H_0.5 real-rooted, verified).
  t<0 probe CHECKED NUMERICALLY: first-8 zeros real t∈[−0.98,+0.5]; first collision γ4+γ5 in
  (−0.99,−0.98), pair 33.1151±0.15054i at t=−1 (expected under RH per Rogers–Tao: non-real zeros
  for EVERY t<0). No non-real zero at any t>0 tested (t_RT∈{0.004..2}) — the only non-circular
  disproof signal — NONE FOUND. RH-consistent evidence only. File: dbheat-deformation-2026-08-18.md.
- **R1 coboundary reopt CLOSED** (2026-08-18, harvest) — record lever: tawan (l,c) globally optimal
  (LP family beats v*=0.00877 vs 0.00780 but global floor 0.0057 < 0.0063 loses; symLP ties exactly
  0.007612214 but global 0.006038 < 0.006222); m=171 exact bound-chain optimum (B(m)=Φ_m(ε(m−6))
  m-dependent; sweep m=20..400 peaks at 171). Record 0.673481 = certified ceiling of redistribution
  class. eps>0.0062 impossible in-class. File: coboundary-reopt-2026-08-18.md.
- **8D follow-up (staged, untested)**: k=18/19/20 @ t=40 INCONCLUSIVE (f64 cannot resolve ~30-order
  Bell cancellation; u-derivs ~1e-12-accurate, B_k~0.07 from 1e15-1e18-scale terms). Resolving needs
  a ~200-bit MPFR (rug) port of zeta_em_ders machinery — ports directly per wave8d-lk-zeta-direct
  note. Not attempted (out of budget). Low priority: L_k≥0 is RH-necessary with zero evidential
  weight; k≤8 coverage is clean and positive.
- **Wave-13 lesson (Python scope)**: R1's 50-min DE global floor (scipy.optimize.differential_evolution)
  was pure-Python heuristic that didn't need to be — LP solve is HiGHS/C (0.0s), DE is ~50 lines of
  Rust, interval verifier (arb/python-flint) is the only genuine Python exception. Also: t=3 already
  showed global floor losing (0.00561<0.00634) — the t=4-6 DE was confirmation overkill that killed
  the agent's write budget. Rule going forward: sanctioned-Python = arb interval verifier ONLY;
  heuristics in Rust or cut; stop searching when the decision is already made.
- **Python→Rust cleanup (2026-08-18)**: (1) verifier-rs fix agent (7b61cc61) dispatched — Rust port of
  the record certifier FAILED to reproduce Python ground truth (False vs certified True @ eps=0.00620,
  α=1.464) → fixing with strict acceptance (4 configs); (2) coboundary_search Rust port (948e3a7f)
  dispatched — reusable LP+DE-global-floor search without scipy; (3) ARCHIVED 6 dead tools to
  tools/_archive/ (manifest README): beat673 (retracted double-normalization), twotone-verify (refuted),
  pt_symmetric_metric_solver (0 refs), adversarial_riemann_solver (0 refs), fourth_moment_rmt
  (single-use, result in note), ramanujan_kernel_search (single-use, result in note). Never deleted.
- **verifier-rs INCONCLUSIVE** (2026-08-18, D-verifier) — ROOT CAUSE PROVEN: Rust port lacks the convex-tangent prune (Python use_tangent=True is load-bearing: ainta 93,735 / tawan 18,182 tangent prunes; Python with use_tangent=False fails identically to Rust). Enclosure NOT the bug (sinc_iv agrees with Arb ball; old "TIGHTER" header claim retracted). SECOND FINDING: current Python file certifies 0.00620 FALSE (terminal low=0.00619595, prec 128/256/512) contradicting eps-boundary-exact 2026-08-13 note (True @1,096,556) — env/version discrepancy, unresolved. Fix path (tangent_lower port: w table, LDL with pivot margin, tangent-plane bound) documented, NOT completed. Rust marked NOT-FOR-CERTIFICATION. File: verifier-rs-fix-2026-08-18.md.
- **coboundary_search-rs DONE (2026-08-18)**: Rust crate tools/coboundary_search/ (948e3a7f) ports the redistribution max-min LP + DE global-floor search, pure Rust (self-written bounded simplex; HiGHS build blocked: no cmake/libclang). LP v* matches scipy/HiGHS EXACTLY (9 digits) at all 6 (α,mode,c_bound) combos tested; global float floors within 5.2e-4 of recorded scipy-DE values, ~0.6s/case vs 50 min Python. Sym LP at α=1.464 is DEGENERATE: simplex picks a different optimal vertex than HiGHS (v* identical) → floor gap 5.2e-4 mixes vertex choice + DE stochasticity. Tool is a SEARCH HEURISTIC, certifies nothing; lever itself remains CLOSED. Note: coboundary-search-rs-2026-08-18.md.
- **Python→Rust cleanup COMPLETE (2026-08-18)**:
  (1) **verifier-rs fix INCONCLUSIVE-but-root-caused** — Rust port lacks the load-bearing
    convex-tangent prune (hardcoded use_tangent=false); enclosure itself matches Python (proven
    by term-breakdown + sinc_iv probes). RECORD SAFE: coordinator re-verified current env
    reproduces certified counts EXACTLY — 0.00620 True @ 1,096,556 nodes (222,047 tangent prunes),
    0.00621 False @ 519,206 (terminal low 0.006198271). Agent's "env drift" finding was its own
    range(6)-vs-range(7) probe bug (dropped 7th weight point). Fix path (tangent_lower port:
    2nd-deriv table via rug, LDL pivot≥1e-9, tl = value − Σ|grad_i|·radius_i) documented in
    research/notes/verifier-rs-fix-2026-08-18.md. Rust port marked NOT-FOR-CERTIFICATION.
  (2) **coboundary_search DONE** (tools/coboundary_search/, pure Rust, no C deps) — LP v* exact
    match 6/6 cases (9 digits), DE global floor within 1e-3, ~0.6s/case vs 50-min scipy DE.
    Self-contained bounded two-phase simplex (HiGHS blocked: no cmake/libclang). Search heuristic
    only — never certifies. File: coboundary-search-rs-2026-08-18.md.
  (3) **6 dead tools archived** to tools/_archive/ (manifest README): beat673 (retracted),
    twotone-verify (refuted), pt_symmetric_metric_solver / adversarial_riemann_solver /
    fourth_moment_rmt / ramanujan_kernel_search (zero-ref single-use). Never deleted.

## DIRECT-RH WAVE-14 (2026-08-18, 3 background agents, RUST ONLY)
- **D4 (01894c73) L_k MPFR** — resolve 8D k=18/19/20 @ t=40 at ~200-bit (rug port of zeta_em_ders):
  last open disproof-capable check (L_k≥0 ⟺ RH). Verdict rules: POSITIVE / INCONCLUSIVE / RH-DISPROOF-escalate.
- **D5 (5fed70fc) d_N oscillation** — dense d·√(ln N) at 19 N values (100..2000, f64, W8C_NMAX cap),
  fit c + A₁cos(2πlnN/P₁+φ₁)+..., test γ₁=14.1347 period (P=0.4446 log-N-units) in the ±1.8% wobble.
  CONJECTURED: explicit-formula origin of the 0.213 constant's oscillation (Burnol zero-sum theory).
- **D6 (b88a2b48) Herglotz probe** — Xi′/Xi Herglotz (Im H(x+iy) ≥ 0 ∀y>0) ⟺ all-real-zeros ⟺ RH (PROVEN
  equivalence). Probe: complex EM+Stirling evaluation of Im H on a grid; Im<0 ⇒ RH-DISPROOF signal.
  Structural note: finite grid can only find violations, never prove RH.
- Referees: blind hostile referee per landed result (D4: sign convention + sanity; D5: fit honesty +
  γ₁-periodicity vs spurious; D6: Herglotz direction + evaluation).
