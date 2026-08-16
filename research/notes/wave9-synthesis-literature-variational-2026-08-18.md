# Wave-9 synthesis — LITERATURE BATCH FULLY ADJUDICATED (night session 2026-08-18)

Date: 2026-08-18 (night). Status: **wave-9 CLOSED**. All 10 batch papers classified, 9A refuted,
GS-2026 framework banked as new knowledge. No new lever survives; records untouched.

## Wave-9 verdict table (all 10 papers)

| paper | verdict | where |
|---|---|---|
| cgdl-1810.08843 (pair-correlation SDP) | 9A lever **CLOSED-REFUTED** at object-identity step | wave9-9A-refutation-2026-08-18.md |
| conrey-et-al-2508.11108 (variational mollifiers) | 9B DUPLICATE-TRAP (Levinson-Q = moment class; θ=∞ = levinson-theta-infinity trap member) | wave9-9B-*.md |
| baluyot-etal-2306.04799 (BGSTB24) | source read; their F ≠ Montgomery's F unless RH — the 9A breaker + unconditional datum for THEIR F only | refutation note |
| gs-2511.20059 (Feb 2026, critical zeros) | **NEW-FRAMEWORK-BANKED** — diagonal-count bridge | gs-2026-diagonal-bridge DAG node |
| gs-2603.28104 (narrow box) | same framework, thin-box version; no diagonal bound claimed | banked with above |
| przz-1802.10521 (five-twelfths) | below record; Levinson lineage | 9B context |
| bui-1410.2433 (three-piece mollifier) | Levinson-line (proportion-on-line class, 0.417 class); irrelevant to 0.673481 | 9B context |
| preobrazhenskii-1403.5786 | Levinson-line | 9B context |
| wu-1206.3737 (distinct 66.036%) | Farmer combination-method lineage; far below 0.836740 | this synthesis |
| rezvyakova-2411.18492 (Epstein pos proportion) | positive-proportion on-line for Epstein = consistency antecedent; barrier-zoo Epstein world already showed our identities consistency-only there | this synthesis |
| garunkstis-1904.03123 (extended Selberg class) | feeds ξ′-transport strand — CLOSED lever, no new content | 9B context |

## The 9A refutation (session's key honest result)

The drafted "unconditional N* ≤ (1.3208+o(1))N ⟹ ≥ 67.92% simple-anywhere" was WRONG and is
now REFUTED at the identification step, proven by reading the arXiv LaTeX of all three papers:

- CGdL's F (LPBandZETAV_17.tex line 444): ordinate-only Montgomery pair correlation
  `T^{ix(γ−γ')}w(γ−γ')`, `w(u)=4/(4+u²)` — the object in their identity (8).
- BGSTB24's F (UnconditionalPC_230606.tex line 141): `x^{ρ−ρ'}w(ρ−ρ')`, `w(u)=4/(4−u²)`,
  complex argument (ρ−ρ') — the real parts enter. Line 143: **"if RH holds then F agrees
  with [Montgomery's F]"** — coincidence only under RH.
- Therefore BGSTB24's unconditional [0,1] theorem does not plug into CGdL's (8); ordinate-only
  [0,1] asymptotics remain Goldston–Montgomery RH-conditional. Internal contradiction
  confirmed: BGSTB24's own §7 application of their Thm 1 (61.7% simple under thin box,
  sech/strip-positive kernels ≈1.38–1.39) sits BELOW the claimed-free 67.92%; and GS (Feb
  2026), AFTER both papers, still frames the RH-removal as open.

Verdict labels must include object-identity checks. The note was caught by the hostile-referee
protocol — exactly what the protocol is for.

## What genuinely survives from the wave

**GS 2511.20059 Theorem 2/3 (Feb 2026) — the real new structural content.** Montgomery's
simple-zero proof decomposes into (a) the Fejér-type pair-sum evaluation (needs the [0,1]
pair-correlation datum — RH-conditional as shown above) and (b) the step "γ=γ′ ⟺ ρ=ρ′"
(needs RH). GS's framework: IF the diagonal pair count (5.2) Σ_{γ=γ′}1 ≤ (C+o(1))N with
1≤C<2, THEN ≥ 2−C simple AND ≥ 2−C on the critical line. The decomposition is unconditional;
the hypothesis (diagonal bound) is the entire missing input.

**New attack surface (fresh formulation, not a lever).** An unconditional diagonal bound
C<2 would give unconditional simple ≥ 2−C AND critical ≥ 2−C. Our own record strength
0.673481 ⟺ C ≈ 1.3265; the redistribution chain does NOT provide the diagonal bound (it
bounds on-line pair sums via L(t)>0/coboundary, not Σ H(γ)²). Explicitly CONJECTURED open:
any unconditional C<2. Note the campaign's uncertified informal expectation from the 8228-zero
census: real-world diagonal ≈ 1+ (mostly simple zeros) — but empirical, consistency-only,
NOT a proof candidate (RH-false worlds can differ; barrier-zoo discipline applies).

## Night status
- 9A lever: CLOSED-REFUTED (was OPEN-STRUCTURAL) — 22 DAG nodes / 20 edges (commit ac046cc).
- GS-2026 framework: banked as knowledge node gs-2026-diagonal-bridge.
- Search state: 29 levers + coordinator probes CLOSED (9A added tonight; 9B was already
  closed). No disproof anywhere. Records 0.673481 / 0.836740 UNTOUCHED and remain the
  unconditional world records as certified.
- Honest progress this night: one false theorem prevented (9A), one genuine framework
  identified and banked (GS-2026 diagonal bridge), 4 remaining batch papers classified.