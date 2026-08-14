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
