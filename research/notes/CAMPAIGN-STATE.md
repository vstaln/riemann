# Campaign State — Full Audit Trail (2026-08-17, wave 3)

**Purpose:** This is the memory document. It records WHAT FAILED, WHAT BROKE, WHAT'S PROMISING,
and the exact state of every thread, so any future session (or any sub-agent) can resume from
disk without re-deriving. Every claim cites its source note. Labels: PROVEN / CHECKED NUMERICALLY
/ CONJECTURED / ABANDONED / INCONCLUSIVE.

---

## 0. The mission and the target (PROVEN, from verified sources)

- **Mission:** find and fully verify a proof of RH, or unconditionally raise the world-record
  lower bound for the proportion of zeros on the critical line.
- **Published unconditional record:** 41.7% (PRZZ 2020).
- **Anthropic Aug-2026 claim (the live target):** ≥ 2/3 of nontrivial zeros simple and on the
  critical line, ≥ 5/6 distinct, unconditionally. Constants with Montgomery–Taylor window:
  0.6725 and 0.8362. Method: rank–trace inequality on a finite compression of Weil's Hermitian
  form, Sylvester's law of inertia handling off-line pairs. Lean-formalized
  (github.com/anthropics/zeta-23-lean).
- **Source verification (2026-08-17):** all 6 user-supplied URLs re-verified HTTP 200.
  4 CDN PDFs downloaded fresh to research/papers/: main paper (anthropic-95c24693.pdf),
  campaign narrative (anthropic-d7f3ecf1.pdf), E2 transcript (anthropic-8a0d1add.pdf),
  informal theorem note (anthropic-23455459.pdf). All text-extracted.
- **Honest status:** docs are real; community acceptance UNVERIFIED. The campaign's own ledger
  entry says the result "needs a human expert" and was "refereed only by other instances of
  itself". Treat as live target, not established fact.

## 1. What we PROVED / verified ourselves (our own results)

1. **Marked moment inequality m₃ ≥ m₂² — THEOREM PROVEN** (wave 2, main-loop fallback):
   on ANY PSD Gram config, marked third moment ≥ marked second moment squared
   (Cauchy–Schwarz on eigenvalues of A = M^{1/2}GM^{1/2}; sinc & torus kernels both PSD).
   Verified: 20 random torus configs at λ=1/2, 2/3 (held, min gap +0.87); GUE synthetic
   family at ALL p₁, both conventions; real zeros 5.3733 ≥ 4.9256 (gap +0.45).
   File: research/notes/marked-moment-inequality-2026-08-17.{md,py}.
   Script: `uv run --quiet --with numpy python3 research/notes/marked-moment-inequality-2026-08-17.py`
2. **Convention-locking consequence — PROVEN:** in the certificate's formal setting (torus
   kernel), pair rows pin E[m₂] = 2.480620 (**p₁-INDEPENDENT**, exact to 4e-16), so by the
   theorem S₃(law) ≥ 6.153476 > 5.44 (read window 5+ε) → **"flat rows + m₃ ≤ 5.44" is EMPTY in
   the torus convention, by theorem, margin +0.71**. The m₃ = 5 read is a sinc-convention
   constant; the torus-kernel certificate LP cannot consume it as-is.
3. **m₃-separation reproduced adversarially:** super-law marked-windowed m₃(1/2)=7.935±0.041
   (theory 8.148) vs real zeros ≈ 5.37; m₃(2/3)=5.36 vs 13/4=3.25; ≥88σ; above pinned bottoms
   5.4419/3.9825. Two honesty corrections filed: m₃=5 is RH-conditional as a theorem;
   convention adjudication. File: research/notes/adversarial-m3-reverify-2026-08-17.{md,py}.
4. **BHB (Baluyot–Heath-Brown) input verified by adversarial validator:** the analytic input
   behind the certificate's prime side is unconditional and correct as used.
   File: research/notes/bhb-adversarial-validator-af-2026-08-17.md.
5. **Anthropic method extracted (PROVEN, from narrative):** coordinator-led campaign, research-memo
   briefs, blind disjoint referees, orphaned-proof rescue, "point the mechanism the wrong way",
   4-class ledger triage, proportion≠RH firewall. File: research/notes/anthropic-campaign-method-2026-08-17.md.

## 2. What FAILED / was CLOSED (with reasons — do not re-attack blindly)

1. **In-class certificate ceiling 0.6818 — PROVEN structural (Lean):** no in-class certificate
   reading {mean, in-band F, integrality} passes p₀ = 0.68182868746 regardless of algebraic
   form. File: research/notes/structural-final-verdict.md.
2. **Window ceiling 0.6725007 — PROVEN (Lean + numeric):** every window family ≤ this
   (Montgomery–Taylor window is the optimizer). two-tone windows REFUTED: c=0 (pure cosine)
   always optimal.
3. **Beyond-α=1 pair correlation — CLOSED everywhere:** no bandwidth-1 escape.
4. **Third moment — PROVEN not breaking 5/6 distinct wall.**
5. **RH itself does not move the in-class ceiling — PROVEN.**
6. **L4 marked-m₃ certificate LP — HEADLINE NEGATIVE (honest):** m₃ read with ε<0.44 excludes
   the ENTIRE near-CUE marked family at p₁≤p₀ (the old ceiling's adversary mechanism destroyed —
   positive), but does NOT establish ceiling > 0.6818: restricted class's min-p₁ uncharacterized;
   family only reaches m₃≈5 as p₁→1 (all-simple) — would raise ceiling IF certified, but no
   multiplicity theorem. Missing input: bound on connected part T or rigorous marked-m₃
   enclosure with true multiplicities. Ceiling question INCONCLUSIVE at LP level.
   File: research/notes/marked-m3-certificate-LP-2026-08-17.{md,py}.
7. **L5 wave-2 adversarial — DIED at 100% context, no deliverable** (infra failure, not
   scientific). Targets A/B later resolved by the m₃≥m₂² theorem (convention mismatch explains
   the "tension": pin is torus, measurement is sinc). Targets C/D still need a verdict.
8. **L2 wave-2 — DIED at 103% context but script survived to disk** (deliverable-first saved it);
   main loop ran the script and wrote the note. Process lesson: deliverable-first WORKS.
9. **Prior-wave closures (from ledger):** history-transport (ceilings break by NEW OBJECTS only),
   finitet-synthesis (formula T-free PROVEN, flip needs ≥6.995e-5 error never seen),
   eps-max search (boundary genuine at ~0.00806), tower-method v1 (died on output limit).

## 3. What BROKE (infra — all fixed or logged)

1. **Subagent context death — THE #1 failure mode.** L2 at 103%, L4 at 111%, L5 at 100%.
   FIX: TOKEN BUDGET (HARD LIMIT) in goal + all 7 agent files (~200k tokens / ~15 tool calls /
   12 turns; deliverable-first; partial note = deliverable; stop at ~85%). L4 survived with
   deliverable because it wrote first. Still the top risk.
2. **Subagent dispatch auth failure (wave 1)** — fixed by pinning model
   opencode-go/deepseek-v4-flash.
3. **Pi skill inventory bloat — 1516 SKILL.md files scanned** (ECC 896, ruflo 350, addyosmani 48,
   hermes trees, s4h, superpowers, npm). FIXED 2026-08-17: ECC/addyosmani/ruflo quarantined to
   ~/.pi/agent/git-disabled/; global scan now 46 skills; s4h (212) moved project-local to
   /home/vstaln/riemann/.pi/skills/ (gitignored). Backups: settings.json.bak-pretrim.
4. **`.lake` Lean build artifacts tracked in git** — 2525 files / 1.7GB. FIXED 2026-08-17:
   git rm --cached + .gitignore; tracked size now 0.19GB (1468 files).
5. **Boxes (pi -p headless) hang** — box dispatch ABANDONED 2026-08-12; laptop = compute worker.

## 4. What's PROMISING / live levers (untested or in-flight)

1. **Sinc-kernel certificate LP with the m₃ read — THE single most valuable untested
   computation.** The certificate must be reformulated in the continuum sinc kernel (where
   m₃ = 5 is a genuine read and L4's super-law exclusion applies). Check if the LP machinery
   (tools/lpdual-realconfig-check, attack-law-s3) ports to the continuum kernel.
2. **tools/barrier_zoo/ — IN FLIGHT (sub-agent cbe8ab6f).** Anthropic rung-0 discipline tool:
   RH-false model worlds (Epstein class-2, Davenport–Heilbronn, planted-zero Beurling, fake
   Weil polynomial) + 4-class claim classifier. Every future brief gets checked against it.
3. **Goldston–Suriajaya double-sum + Guth–Maynard zero-density** (L1's lever #2) — untested.
4. **Bui–Heath-Brown partial unconditionalization** (L1's lever #3) — untested.
5. **T-2 derivative-tower (ξ″/ξ‴ cert + weighted distinct-ζ)** — ALIVE, score 375, target
   Farmer 0.6603 distinct-ζ record; interlacing CHECKED at 60 digits (20/20).
6. **Binding open inputs (M6):** k<1 moving-boundary count N(1/2+b/L,T)=o(T log T) at b≈0.0758;
   M4 ζ″-moment r′; pair-correlation box-width inputs; BGSTB strong ZDH.

## 5. The method going forward (what to do every session)

1. Read THIS document + ledger.md (do-not-repeat) + the day's notes. Never re-derive a verdict.
2. Pick the highest-value UNTESTED lever (new objects > in-class sharpening).
3. Write a research-memo brief: target, objects, reading list, conjecture, forecast,
   RH-false control demand. Dispatch 1–2 background sub-agents, pinned
   opencode-go/deepseek-v4-flash, budget-capped.
4. Test every number with a script (Rust musl for CPU-bound; uv run --quiet python for probes).
5. Document: research/notes/<idea>-<date>.md with honesty labels. Update ledger (≤5 lines).
6. Adversarial validation before any claim is ledgered as verified: blind referee, one joint,
   worked attack plan.
7. If a sub-agent dies, read its directory, rescue the deliverable, resume with a checklist.

## 6. File map (where everything lives)

- Goal: /goal (persistent working goal; updated to Anthropic method 2026-08-17).
- Charter: hooks/agents.md (updated 2026-08-17: corrected record context + campaign method).
- Agent files: ~/.pi/agent/agents/*.md (7 agents; method block appended 2026-08-17).
- Ledger: research/notes/ledger.md.
- Method playbook: research/notes/anthropic-campaign-method-2026-08-17.md.
- Sources: research/papers/anthropic-{95c24693,d7f3ecf1,8a0d1add,23455459}.pdf (+ .txt).
- Live lever notes: marked-moment-inequality-2026-08-17, marked-m3-certificate-LP-2026-08-17,
  sos-hierarchy-transfer-2026-08-17, lever-miner-assumption-excavation-2026-08-17,
  adversarial-m3-reverify-2026-08-17, bhb-adversarial-validator-af-2026-08-17.
- Walls: research/notes/structural-final-verdict.md, attack-ceiling.md.

---

**End of memory document.** Any future agent reading only this file + the cited notes has the
full state. No fabrication; every line traces to a file in this repo.

---

## UPDATE 2026-08-17 (late) — Rust-only directive + parallel wave 3

**Directive (user, binding, all sessions):** Python FORBIDDEN unless absolutely necessary (mpmath-level
arbitrary precision with no Rust equivalent, justified one line in the note label). No numpy/scipy/mpmath
in new deliverables. Existing Python verifiers (`tools/barrier_zoo/`, `tools/lpdual/`) are reference-only;
port to Rust as the first action of any lever touching them. Cargo has network + registry cache (verified
2026-08-17: minilp 0.2 fetches; zeta-rs builds in 0.03s cached). Rust musl: `export
PATH=$HOME/.cargo/bin:$PATH RUSTFLAGS="-C linker=rust-lld -C link-self-contained=yes"` + `cargo build
--release --target x86_64-unknown-linux-musl`. Goal + hooks/agents.md updated to match.

**Parallel thinking is now mandatory** (goal §OUR COMBINED METHOD): dispatch ≥2–3 disjoint background
sub-agents per turn, never inline everything in the coordinator loop.

**Wave 3 dispatched (all background, pinned opencode-go/deepseek-v4-flash, Rust-only, deliverable-first):**
- (A) `d629da85-ae98-4d8` builder — barrier zoo → Rust port `tools/barrier_zoo_rs/`: must reproduce the
  certified DH off-line zeros s=0.8085171824566+i·85.6993484854 and s=0.6508300806097+i·114.1633427308
  (|f|<1e-50 @50dps, Titchmarsh κ-combination; also zeros of f_plus c=+ε), t_hi≥130.
- (B) `b333a18a-660e-440` builder — sinc-kernel certificate LP with m₃ read `tools/sinc_m3_cert/`
  (minilp): does the PROVEN m₃≥m₂² theorem break the in-class ceiling 0.6818 when the certificate is
  reformulated in the sinc/Montgomery–Taylor window? + RH-false control. THE live mathematical lever.
- (C) `f11dace2-4faa-458` adventurer — off-centre positivity wrong-direction brief (empty-route forecast;
  inversion = win; k<1 moving-boundary b≈0.0758 count vs LMFDB zeros).

**Adjudicated this session:** the 9 rebased-in remote commits claiming a complete Lean RH proof / 90%+ /
De Branges / Li are NOT RECORDS — CompleteRHProof.lean's core theorem is a vacuous tautology (hypothesis
∀d C≤C_on−4·d·N_off forces N_off=0 by itself; never proved for actual ζ); GramStability.lean has 8 sorries;
"90%+" contradicts PROVEN walls. File: research/notes/adjudication-remote-rh-claims-2026-08-17.md.

## UPDATE — wave 3 verdicts + wave 4 dispatch (2026-08-17 ~02:00)

### Wave 3 results (all three agents landed; coordinator post-verified each)
- **(A) barrier-zoo Rust port — ABANDONED as deliverable, stub kept.** Build fixed by
  coordinator (8 adjacent-string-literal errors + 1 borrow-move); run shows MATH CORES BROKEN:
  Γ(2)=1.5054 (expect 1) → Lanczos misimplemented; ε(ψ)=−13.877+66.587i (|ε|=68, expect |ε|=1,
  GaussSum/(i√5)); certified DH zeros NOT reproduced (|f_plus|=641/232 at the certified spots,
  need <1e-9); Epstein modularity rel-diff 0.59–0.91, continuation off 3–6 orders, Dedekind
  false. Weil + Beurling + classifier mostly correct. NOT rung-0 usable; acceptance test =
  reproduce the certified DH zeros. Wave-4 agent f0f32ad5 fixing Γ→ε→zeros now.
  File: research/notes/barrier-zoo-rust-2026-08-17.md.
- **(B) sinc-kernel m₃ certificate LP — CONJECTURED (binary ran; 2 hostile referees dispatched).**
  Scan (eps=0.44, sinc² B=128 N=256): min-p₁=0.748807, κ=0.748809 — EXCEEDS 0.6818.
  Honesty flags: (i) minilp shadow block `Infeasible` (linearized LP invalid at the max-kink;
  scan/bisection is the real optimum); (ii) torus-convention floor 6.1535 → INFEASIBLE read
  (expected — the read is sinc-convention; route (a) reformulation is exactly this binary);
  (iii) RH-false control: sinc² Gram σ-blind → reads(B)==reads(A) for the 60%-on-line fake-Weil
  world → PROVES TOO MUCH for the on-line claim: κ* is a SIMPLE-FRACTION ceiling, the on-line
  reading needs an RH-type hypothesis (off-line zeros all non-simple). Firewall intact.
  Calibration-fragile: κ>0.6818 only for m₂(1)≥~2.17; real-zeros sinc m₂²=4.9256→m₂(1)=2.2198≈2.22,
  so the feasible branch IS the real-zeros branch — the most promising reading.
  At the optimum the binding constraint is D+P₃=5.44 (read TOP), m₂²=5.02 SLACK — the theorem
  m₃≥m₂² is NOT the active constraint; the m₃ READ is. The claim's real content:
  "m₃-read ≤ 5.44 forces p₁ ≥ 0.7488 in the sinc marked-law model." File: sinc-m3-certificate-LP-2026-08-17.md.
- **(C) off-centre positivity — PROVEN EMPTY (route dead), forecast held.** Window pinned
  0.6725007, class ceiling 0.6818, beyond-α=1 closed; the one real positivity (3+4cosθ+cos2θ)
  gives only the zero-free-region right edge — weaker than the box certificate needs. LMFDB
  data stores (index, ordinate) only → off-line count ≡ 0, sanity check VACUOUS by construction
  (probe run: 0/51499, ratio 0.7043, Θ(T log T) never o). m₃≥m₂² is λ-independent (CS on PSD A)
  → off-centre marked positivity = same theorem shifted, empty. File: offcentre-positivity-probe-2026-08-17.md.

### Wave 4 in flight (all background, flash, Rust-only, disjoint)
1. d273aacb Referee-A — hostile, joint = sinc-m3 marked-law model correctness (normalization
   E[m]=2/(1+p₁) vs 2−p₁, row-0, pair rows, P₃, floor completeness, calibration, is the
   theorem row really slack at the optimum). Control: 256-law at p₁=0.6818287 must be excluded.
2. 81636ce4 Referee-B — hostile, joint = interpretation + LP/scan reconciliation (σ-blindness,
   what exactly κ* certifies, find an RH-false world where the conclusion is FALSE — DH
   candidate, scan-vs-minilp, record-mapping). Control: fake-Weil world B.
3. f0f32ad5 barrier-zoo math cores (Γ, ε, DH zeros, Epstein, Beurling, classifier 10/10).
4. 7f447497 re-derivation m₃≥m₂² from scratch (FORBIDDEN to read the 3 marked-moment notes;
   load-bearing output = which m₂ convention the theorem binds in).

### Open items
- L5 targets C/D: still need a verdict (low priority; behind the live sinc-m3 thread).
- Pending after wave 4: ledger the referees' verdicts; if model+interpretation survive,
  dispatch a re-derivation of the certificate's min-p₁ + a blind referee on the record claim;
  fix barrier-zoo then it becomes the rung-0 discipline tool for all briefs.

## UPDATE — wave 4 verdicts + wave 5 dispatch (2026-08-17 ~02:25)

### Wave 4 verdicts (all four agents landed; coordinator verified each)
- **sinc-m3 certificate LP — REFUTED as a ceiling-breaker.** Two hostile blind referees,
  independent re-derivation, coordinator hand-check: (1) Referee-A — the binding constraint
  D+P₃=5.44 needs E[T]≥0 which is UNPROVEN and FALSE per-config (3×3 PSD a=−0.2 counterexample:
  m₃=1.224≥m₂²=1.1664 theorem HOLDS yet T=−0.016<0; coordinator verified trG²=3.24, trG³=3.672,
  P₂=0.24). Under the ONLY proven floor (S₃≥m₂²): min-p₁=0.4224 (mass)/0.5939 (count) < 0.6818.
  Convention mix: model p₁ MASS vs wall p₀ COUNT (count recompute 0.8564). Calibration
  knife-edge (±5% flips). Control EXHIBITED: 256-law (mass 0.5173) has proven floor 5.2488 ∈
  window → admissible under proven inputs. (2) Referee-B — σ-blindness PROVEN; "0.7488" loose
  label (P(m=1)=0.8564 there); scan AUTHORITATIVE, minilp `Infeasible` is a global
  linearization artifact (tangent system infeasible ∀p₁); raises NO published on-line record;
  on-line interpretation does NOT survive the firewall; DH simple off-line zeros kill the
  RH-type hypothesis. (3) Re-derivation — m₃≥m₂² PROVEN independently via Parseval+CS
  (m₃−m₂²=N²M²Var(T1)≥0, equality ⟺ uniform marks; probe PASS all configs, position-blind);
  theorem binds the sinc branch legitimately; torus 2.480620 infeasibility OUTSIDE theorem
  scope (INCONCLUSIVE). **Lever CLOSED. No on-line record affected.**
  Files: wave4-synthesis-2026-08-17.md, refereeA-sinc-m3-model-2026-08-17.md,
  refereeB-sinc-m3-interp-2026-08-17.md, rederivation-m3-2026-08-17.md.
- **barrier-zoo Rust — PROVEN, rung-0 tool OPERATIONAL.** Builder fixed 8 root causes
  (Gamma off-by-half, C::exp angle real slot, q^{+s} vs q^{-s}×3, DH grid dt, theta origin,
  classifier regex parens). Acceptance (coordinator re-ran): Γ(2)=1.0, Γ(5)=24.0, |ε|=1,
  FE both signs true, |f_plus|=3.1e-14 at both certified DH zeros, 2/2 matched, 6 off-line
  zeros, Epstein modularity 1e-15–1e-13 + Dedekind true, planted zeros 2.3e-16/1.5e-16,
  classifier 10/10. Caveat: Epstein's own off-line zero search grid-limited (fine grid ~1000×
  too slow; VERDICT text overclaims). **All briefs now disciplined through this zoo.**
  File: barrier-zoo-rust-2026-08-17-fix.md.

### Wave 5 in flight (3 disjoint levers, all with RH-false controls via the working zoo)
1. d2d5db17 M4-proper ζ″-moment r′ (closed-form BHB Lemma-1 re-derivation with ζ′→ζ″).
2. 0a0236b5 k<1 moving-boundary Type-1 decision (prove empty or invert, E2 playbook).
3. 623d88bf exact-identity m₃ certificate (valid revival: m₃=m₂²+N²M²Var(T1) instead of the
   broken D+P₃ floor; exact min/max-S₃ envelopes; 256-law exact-S₃ control).
Briefs on disk: wave5-briefs-2026-08-17.md.

### Open items
- Torus E[m₂]=2.480620 exact definition (INCONCLUSIVE; outside theorem scope).
- Epstein off-line zero search resolution (grid-limited; needs fast I(s) evaluator).
- Lesson reinforced: ceilings break by NEW OBJECTS/INPUTS, never sharper in-class
  inequalities — sinc-m3 was another sharpening and died, consistent.

## UPDATE — wave 5 verdicts + wave 6 mission-critical pivot (2026-08-17 ~03:00)

### Wave 5 verdicts (all landed; coordinator probe-verified)
- **5A M4-proper ζ″-moment r′ — lever CLOSED**: r′ ≥ 0 PROVEN by positivity (c(S₂)=57/64);
  r′=3/5 REFUTED twice (moment is ℒ⁶/90-scale not ℒ⁵/5; 1/(2k+1) pattern false); r′ value NOT
  pinned by this route (honest); new constant −X·ℒ⁶/180 CHECKED NUMERICALLY (probe 0.445→0.485,
  ζ′-control reproduces Gonek exactly). b_pair ≤ 0.2237 ceiling STANDS.
- **5B k<1 Type-1 decision — NO (HIGH confidence)**: count > density hypothesis by two gaps
  (only log-free ε-free DH certifies, ratio 3.7e-2 @1e10; Montgomery k=13 → 1.9e16, Ingham k=44
  → 1e59); crossover b*(T) grows 54→283, never fixed; all six inversion duals EMPTY. Route
  closed, question open.
- **5C exact-identity m₃ certificate — m₃-read lever FINALLY CLOSED**: identity verified to
  5.82e-11; only certified consequence min-p₁=0.4224 mass/0.5939 count < 0.6818, independently
  reproducing Referee-A; old 0.7488 was pure E[T]≥0 artifact. DH control clean.
- **Synthesis**: three consecutive in-class levers closed; 0.6818 needs a NEW OBJECT.

### ⚠️ Wave 6 PIVOT — the campaign may ALREADY hold the record (mission-critical)
The repo's certified records **0.673481 simple-on-line / 0.836740 distinct** are labeled
UNCONDITIONAL (records-vs-anthropic-paper-2026-08-13.md) and exceed Anthropic's claimed
optimized constants (0.6725 / 0.83625) on BOTH axes, far above PRZZ 0.417. Coordinator
independently verified the arithmetic: distinct=(1+H)/2=0.83674043083725685 ✓,
H(1.464)=0.672467425577788142 ✓, bound chain (H−τ)/(1−B/m) with τ=0.00301535, B/m=0.005982
→ 0.6734809 ✓. BUT: FINAL-RECORD honesty ledger says "NOT YET: Lean formalization, second-
machine audit"; the record's gain over the PROVEN window ceiling 0.6725007 comes entirely from
the redistribution denominator (1−B/m) — exactly the class of algebraic move that killed
sinc-m3 (E[T]≥0). **Therefore: before any new-record hunt, three hostile blind referees on
the record chain itself.** Wave-6 joints:
- 6A redistribution algebra (bound=(H−τ)/(1−B/m) first-principles re-derivation; attack the
  division move) — cae841fe
- 6B transfer to ζ (exact theorem 0.673481 proves; Montgomery F=1 on [0,1] incl. j=N edge;
  liminf/rate handling; every input traced) — c5e668e3
- 6C second-machine re-derivation (fresh implementation, reproduce 0.6734808616745137 + eps
  0.0062: 630 fails/620 passes, without reading the verifier code) — 358dd28d

### Decision rule (pending referee verdicts)
- All three PASS → 0.673481/0.836740 are a verified UNCONDITIONAL world record; campaign
  shifts to formalization + writeup + publication-grade adversarial audit.
- Any referee BREAKS it → we learn the exact fault; fix or re-scope; record hunt continues
  with the NEW-OBJECT requirement.
