# POSTMORTEM — stale claims / contradictions after F_V vs F_T retirement (2026-08-24)

**Date:** 2026-08-24. **Agent:** adventurer (contradiction + misattribution hunt).
**Trigger:** record retired twice — (1) cert-bug-2026-08-21.md (LDL convexity cert unsound), (2) 2026-08-24 F_V vs F_T functional mismatch + 2026-08-24 final mass-conditions HARD (see ledger.md ~L2100-2157, dispute-vstalin-code-2026-08-24.md, dispute-vstalin-tawan-2026-08-24.md).

**Ground truth (PROVEN, ledger 2026-08-24 final):** every coboundary-floor record certified via
`verify_coboundary_floor.py` coboundary branch implements F_V (21 pairs + q·w terms); Tawan's
local-to-global lemma requires F_T (span-one pairs removed). F_V ≥ F_T strictly on the interior, so
NO F_T bound follows from any F_V certificate. Retired: 0.6735633 (08-18), 0.6734729658195391 +
0.6735117054871194 (08-21 re-certs), 0.6735471309049393 (08-23), and the 08-24 F_T re-certs
0.67296645387858 / 0.6730965989022086 (INADMISSIBLE, Σq≠2). **Surviving floors:** Tawan published
0.6731929114731422 [PROVEN, his verifier]; Devine-reported 0.673399 (unaudited). Dual side
UNAFFECTED: ceiling 0.68182868746, distinct-proportion 0.8367817. Earlier verify_cos7-era records
(0.6732628655 / 0.6732666023780 / 0.6732654364955235) were already RETRACTED 2026-08-12 for the
kernel double-normalization bug (retraction-673-invalid.md).

## Stale-claim table

| # | file:line | claim | status NOW | suggested edit |
|---|---|---|---|---|
| 1 | README.md:5-10 | "🏆 Current certified record (2026-08-23): N₀(T)/N(T) ≥ **0.6735471309049393** … eps=0.0079 … Gershgorin … 27,679,928 nodes" | STALE-RETIRED (F_V; retired 08-24) | Replace banner with surviving state: Tawan 0.6731929114731422 [PROVEN external]; Devine-reported 0.673399 (unaudited); local F_T restart in progress (ledger 08-24) |
| 2 | CAMPAIGN-STATE.md:429 | "**Exact theorem (unconditional):** liminf N_s(1/2,T)/N(T) ≥ 0.6734808616745137" | STALE-RETIRED (F_V cert; "unconditional" misleads) | Strike or re-label INVALID; point to ledger 08-24 |
| 3 | CAMPAIGN-STATE.md:462 | "line is ALREADY MET by the repo's certified records — 0.6734808616745137" | STALE-RETIRED | Same fix |
| 4 | CAMPAIGN-STATE.md:791-812 | "2026-08-18 (session 2) — lambda-dilation record raised: simple 0.6735633479946227 (certified eps 0.00703)" + "certifiable landscape" table | STALE-RETIRED (no retirement recorded anywhere in CAMPAIGN-STATE; file ledger ends 08-18) | Append retirement note; mark numbers INVALID |
| 5 | CAMPAIGN-STATE.md:827 | "Record 0.6735633479946227: CHECKED NUMERICALLY … certified eps via sanctioned arb verifier" | STALE-RETIRED | Same |
| 6 | FINAL-RECORD-2026-08-13.md:5-7 | "# CURRENT FINAL CERTIFIED RECORD — 2026-08-18 … ≥ **0.6735310829992681328867805395**" (verifier-rs + sanctioned arb reference runs, pair weights "all 0≤i<j≤6") | STALE-RETIRED (verifier-rs implements the same 21-pair F_V functional; cross-checked by the F_V arb path; CONJECTURED-level but high: no separate span-one audit of verifier-rs exists) | Header → RETIRED; note verifier-rs needs the same span1_mode audit |
| 7 | FINAL-RECORD-2026-08-13.md:51 | "Simple-on-line proportion: ≥ 0.6734808616745137" | STALE-RETIRED | Same |
| 8 | wave6-synthesis-2026-08-17.md:3,30-31 | "certified records — 0.6734808616745137 … **unconditionally** (no RH, no pair-correlation)" | STALE-RETIRED (F_V; the 5 hostile referees validated the bound chain, not the F_V eps certification) | Mark record INVALID; the "unconditional" framing drops |
| 9 | records-vs-anthropic-paper.md:22 | "simple-on-line 0.6734808616745137 vs 0.6725 +0.000981" | STALE-RETIRED | Re-point to surviving floors |
| 10 | session-synthesis-2026-08-19.md:42 | "(0.6735633 simple / 0.8367817 distinct) — firewalled, not RH" | STALE-RETIRED (simple half; distinct 0.8367817 is dual-side and UNAFFECTED — split the claim) | Simple → retired; distinct → keep |
| 11 | ledger.md:40 | "## Record (current certified): **0.673262865534356014645368000853343519319712248**" (α=1.49, psum=1/220, m=133, eps=0.00806) | STALE-RETRACTED (verify_cos7 kernel bug, retracted 08-12; ALSO below surviving Tawan floor) — **direct contradiction with ledger's own 08-24 entries** | Replace with 08-24 honest record line (Tawan 0.6731929 PROVEN / Devine 0.673399 unaudited / local restart) |
| 12 | ledger.md:48-50 | "Results landed: NEW CERTIFIED RECORD (pending re-cert): 0.6732654364955235 … boundary GENUINE, not artifact" | STALE-RETRACTED (same verify_cos7 verifier family; "boundary GENUINE" conclusion void) | Mark dead; cite retraction-673-invalid.md |
| 13 | epsmax-tight.md:1-10 (whole note) | "the boundary is TIGHT (PROVEN) … max certifiable eps = 8065/1e6 … 7874/7937 … 0.00607 … record config EXHAUSTED" | STALE-RETRACTED (all numbers from the double-normalized kernel; the "record config" is dead) | Re-label RETRACTED; eps-max values were for the inflated functional |
| 14 | eps-boundary-exact.md:26,62 | "α=1.464 is exactly eps=0.00620 … Record 0.6734808616745137 is the **exact, certified optimum** of the coboundary [class]" | STALE-RETIRED (exact-optimum conclusion derived under F_V; objective changed) | Re-derive under F_T before re-asserting optimality |
| 15 | coboundary-reopt-2026-08-18.md "FINAL VERDICT §1,3" | "Conclusion (PROVEN): tawan's (l,c) is the **global optimum of the redistribution class** — no (l,c) certifies eps > 0.0062" + "m=171 is the exact optimum" | STALE-RETIRED (LP/floor searches ran on the F_V functional; conclusion does not transfer to F_T). Note: the m-sweep bound chain (H−τ)/(1−B/m) is Tawan-arithmetic and survives as arithmetic — only the eps input is dead | Re-run under F_T; keep the bound-chain arithmetic, drop the global-optimum verdict |
| 16 | ladder_9point_results.md §6 rank 1 + §7.3 | "0.67348086 — Swarm Discovery, Coboundary redistribution" / "The highest certified bound (0.67348086) is obtained when…" | STALE-RETIRED (cites F_V record). The note's OWN 9-point bound 0.673096571 is a different (gram-ladder) machinery, NOT produced by verify_coboundary_floor.py — not directly implicated, but it now ranks BELOW surviving Tawan 0.6731929 | Re-rank leaderboard: Tawan 0.6731929 [PROVEN] top; Devine 0.673399 (unaudited) flagged; drop 0.67348086 |
| 17 | epsmax-tight.md vs ledger.md:48 | boundary point disagreement: "8065 verifies; 8067 fails" (epsmax-tight) vs "0.008064 certified … 0.008070 FAILS" (ledger) | CONTRADICTION (minor; both numbers from the dead verify_cos7 family) | Moot once both are marked dead — note it so nobody re-litigates |

## Status labels
- STALE-RETIRED (F_V): certified number/record produced by the coboundary F_V code path; dead per ledger 2026-08-24.
- STALE-RETRACTED (kernel): verify_cos7-era; dead per retraction-673-invalid.md.
- CONJECTURED: verifier-rs (row 6) and ladder_9point's own bound (row 16) not directly audited for F_V/F_T here; high suspicion but not proven in this pass.

## Claims that SURVIVE (do not edit)
- Dual ceiling 0.68182868746, distinct-proportion 0.8367817 (dual side) — UNAFFECTED (ledger 08-21/08-24).
- Tawan published 0.6731929114731422 [PROVEN, external verifier]; Devine-reported 0.673399 (unaudited).
- ζ′ zero-free Speiser lane, Li λₙ > 0 (n ≤ 10⁶) — unrelated lanes.
- Mass-condition finding itself (Σq=2 hard) — PROVEN, current basis for restart.
