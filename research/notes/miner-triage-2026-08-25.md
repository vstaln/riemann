# Miner Triage — 2026-08-25 (A–L, M–Z, synthesis-day → action queue)

**Source:** /tmp/mine_A-L.md, /tmp/mine_M-Z.md, /tmp/synthesis-day.md (all 2026-08-24 deep-mining reports).
**Cross-check:** research/notes/ledger.md (through 2026-08-25 FT4 entry). Verdicts cited, not re-derived.
**Context anchor:** 0.6735471 RETIRED (F_V/F_T span-1 double-count, PROVEN 3 lanes); post-fix floors RETIRED (lambda-scaled q, INADMISSIBLE — mass conditions HARD: Sigma q = 2 exactly, span masses 2); surviving floors Tawan 0.6731929114731422 [PROVEN] / Devine-reported 0.673399 (unaudited); FT4 ascent wall eps∈[0.0056,0.0058), target rung eps>0.00577.

---

## 1. Surviving findings ranked by value-per-hour

| # | Finding (source report) | Why it survives | Status / gate |
|:--|:--|:--|:--|
| S1 | **F_T optimizer round-5, mass-pinned** (M-Z #1; synth Rank 3) | The only live vehicle for raising the certified floor: warm-start from best_ft4_theta.npy ∪ Tawan exact point, SMALL steps, Sigma q=2 + psum≈1/320 pinned, certify via tools/verifier-rs floor-pipeline. This IS the ledger's 2026-08-25 plan — continue, do not re-dispatch. | LIVE — current main line. Target wall > eps=0.00577. |
| S2 | **D1 dual-lens separation probe: adaptive Weil λ_min + b=4 Hankel H₃** (synth Rank 2, augmented) | Ledger already queues D1 (adaptive-growing-basis, <20 min, reuses wave25 probe + barrier_zoo, 4 RH-false controls). The mining reports add the repthy lens: H₃=det(m_{i+j}) benchmarks CUE +58/945 vs rank-collapse 0 (DH). One run, two falsification axes; decides non-separation vs rank-gap and whether b=4 Toeplitz is discriminatory. | LIVE — merge H₃ lens into queued D1. Do not dispatch as a second agent. |
| S3 | **m=257 square-root tail bound → recompute v*(p1) dual certificate** (M-Z #2) | Removes the O(1/m) truncation artifact at m=256 (residual <1.4e-7) from the LP shadow-price machinery. Ceiling_law256 is degree-independent (PROVEN) so this sharpens certificate optimization, not the ceiling — label it that way. Cheap, concrete. | LIVE — tooling sharpening. |
| S4 | **trmdy kernel-family sweep** (A-L #2; M-Z #4 contradiction resolved) | port-trmdy-2026-08-24 establishes 2 positive-definite mechanisms; trmdy-combinations-negative was naive/unregularized. Ledger plan item 3: sweep proceeds AFTER mass discipline (kernel choice orthogonal). | LIVE — gated behind S1's mass-2 discipline. |
| S5 | **Density-one Layer (b) trace-moment probe** (A-L #3) | Sole unformalized dependency of the density-one theorem (m_b(T)→m_b at every b); everything else refereed. xdom-repthy/funcfield prove RMT/geometric finite-rank models cannot close it — so run the probe as **falsification/diagnostic**, not a fix. | LIVE (diagnostic) — folds into S2's dataset; cheap. |
| S6 | **PF cosine-bank moments → exact tail bounds for kernel_family.py truncation** (A-L #6) | Certified PF moments M_k (1.6e-15) are banked; using them to bound truncation leakage in the exact-rational kernel family is a new, un-tried application (distinct from the DEAD Turán coefficient-margin route t_k·k→2). | LIVE — infra, low priority. |
| S7 | **wave8d MPFR Stirling fix → core eval libs** (M-Z #9) | Resolves the ledger's 8D open item (L_k t>0 needed zeta-direct evaluator): Stirling sign + factorial bugs fixed, L_18..L_20(t=40) positive, cert error <1e-33. Port to core libraries. | LIVE — tooling, closes 8D gap. |
| S8 | **Exact-rational Karle-Hauptman Gram SDP** (A-L #10) | Not in ledger (new). Exact-rational kernel family eliminates the float-SDP instability that killed the pre-C21 probe. **Firewall caveat:** Weil-subclass PSD positivity is ⟺-RH territory (fresh-object-hunt trap-inventory) — certify the Gram as a *diagnostic discriminator* against DH, not as RH evidence. | LIVE (low, with firewall label). |

## 2. Killed findings (11) — one-line causes

| Finding | Cause (ledger verdict cited) |
|:--|:--|
| 0.6735471 F_V/F_T retraction & fT-recert "first action" | ALREADY LEDGERED 2026-08-24 (3 PROVEN lanes); recert run happened and was itself retired (q-mass) — fully superseded. |
| Lambda-scaled coboundary floors / "cleanse LP generator" | ALREADY LEDGERED 2026-08-24: HOLD RESOLVED, mass conditions HARD; floors 0.672966…/0.673096… RETIRED (INADMISSIBLE). Action = S1's mass-pin, already planned. |
| De Branges / Lean-4 synthetic RH | ALREADY LEDGERED: NOT-RECORD, vacuous tautology (mercer_offline_zeros_elimination); crossdomain: de Branges route ⟺ RH by construction. |
| BHB ζ″ r′ pinning / "seal b≤0.2237" | ALREADY LEDGERED: M4-proper CLOSED (r′≥0 PROVEN, r′=3/5 refuted twice, b_pair≤0.2237 stands). |
| xi′→ζ distinct transport | ALREADY LEDGERED 2026-08-18: ξ′-transport distinct CLOSED (double zeta-zeros collapse to simple xi′-zeros). |
| GS25/BGSTB box re-open via sqrt-tail envelope | GS box lever CLOSED in ledger: no width reaches p₀ (needs C≤1.31817 vs best 1.32750, ΔC≈0.00933); sqrt-tail attacks 256-law truncation (S3), no mechanism shown to close ΔC. |
| BHB 19/27 re-open via trace moments | Blocked twice: E/S₂<3.11% needs moving-boundary count (k1-moving-boundary Type-1 NO, PROVEN) AND density-one Layer (b) (unresolved, not closable by RMT/geometric per xdom). |
| Speiser/LM clustering → off-centre probes | 8B census already done; application target off-centre positivity PROVEN EMPTY (wave-3C). |
| Q3 ladder pairwise pressure reinstatement | Basis note dilation-lambda-2026-08-18 is the retired q-scaling family; live ladder line is tower-method P5 (in flight) — different object. |
| wave8c d_N → c4 second-moment denominator | 8C-chain-complete already CHECKED/CERTIFIED; proposed application speculative, no coupling shown. |
| wave8e Beurling Gram basis for mollifier trials | Direct-RH lanes (8B–8E) closed as equivalence/diagnostic; speculative, no new input. |

Synthesis-day Rank 1 (document quarantine) — **mostly DONE** in ledger (retirements recorded, verifier patched span1_mode=replaced, F_T recert banked); residual = the mass-assertions guard → folded into A1.

## 3. Top-3 concrete first actions for next session (<30 min each)

1. **Add mass-condition assertions to verify_coboundary_floor.py** (ledger do-not-repeat guard #2): hard fail unless |Sigma q − 2| < 1e-12 AND span masses = 2 preserved, in the env branch; make the bug class that retired three record families unrepresentable. (~20 min, 0 compute.)
2. **Run D1 dual-lens separation probe** (S2): adaptive Weil Gram λ_min d=16..1024 + b=4 Hankel H₃, true-zeta vs DH certified zeros (barrier_zoo), reusing tools/wave25_schur_weil_probe.py. Verdict: separation (rank-gap falsified, lever) vs plateau (rank-infinity universal). (~20 min CPU.)
3. **Launch F_T optimizer round-5 warm-started** from best_ft4_theta.npy ∪ Tawan exact point, SMALL steps, mass-2 + psum≈1/320 pinned (S1); certify winners via verifier-rs floor-pipeline; target wall > eps=0.00577. (Dispatch <30 min; compute 10–20 min per ledger; m=257 sharp-tail recompute from S3 can run in parallel on the same LP.)

---
**Verdict (≤5 lines):** 8 survivors (S1–S8), 11 killed, 3 top actions. Main line unchanged: mass-pinned F_T optimizer round-5 (S1) is the record vehicle; S2 probe is the highest new-knowledge-per-compute; S3–S8 are cheap sharpenings/tooling. All kills are ledgered verdicts — no re-derivation, no duplicate dispatch.
