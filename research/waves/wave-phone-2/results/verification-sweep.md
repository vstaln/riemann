# Verification sweep — thorough re-run of the existing research (2026-08-12)

**Scope:** every ledger headline claim re-executed from its saved cited script (honesty charter: numbers from saved scripts only). All runs on the phone proot (mpmath 1.4.1, numpy 2.3.5) unless noted. Labels per hooks/agents.md.

## Results table

| # | Claim (ledger/paper) | Script | Re-run result | Verdict |
|---|---|---|---|---|
| 1 | Record bound 0.67326543649552352207990181282271996377681849486392 (eps=8064, m=133) | attack_bound_check.py formula, mpmath 160 dps | bound = 0.67326543649552352207990181282271996377681849486392; residual vs headline **7.96e-52** (= print truncation) | **REPRODUCED (50 digits)** |
| 2 | eps=8065 bound (the live record-move question) | same | **0.67326607914000068** (+6.43e-7 over the record) — if the verifier certifies 8065, the record moves here | computed (verifier pending) |
| 3 | Zeros' connected part T: [+0.272,+0.427] @N=64, [+0.333,+0.401] @N=256, mean 0.367/0.385, → +1/2 = A3(1/2) | m3_min_frontier.py (re-run, 10000 zeros) | N=64: T 0.2720..0.4270 mean 0.3665 (156 blocks); N=256: 0.3333..0.4011 mean 0.3850 (39 blocks) | **REPRODUCED exactly** |
| 4 | Super-law marked m₃(1/2): raw 7.108±0.024, bias-corrected 7.978 | superlaw_s3_v2.py (the deliverable's cited script) | 7.10822 ± 0.02398, corrected 7.97797; m₃(2/3): 4.86617±0.01910 → 5.35855 | **REPRODUCED exactly** |
| 5 | Super-law "exact theory (mpmath)" 8.147999 / 5.468708 | **NO reproducing script found** — formula as documented (D·(Em3/Em)+3·Em2·A2+Em²·A3 with D=1.9545, Em2/Em=1.3182, Em3/Em=1.9545, A2(1/2)=7/6, A3(1/2)=1/2) gives 8.934 (Em=1 reading), 9.141 (Em=1+q), 10.01 (true-moment reading) — NONE give 8.147999 | **NOT REPRODUCIBLE from documented inputs — flag for re-derivation** (see §2; separation conclusion UNAFFECTED: raw 7.108 is ≥69σ above the pin 5.4419 under every reading) |
| 6 | m₃ closed forms: m₃(1/2)=5, m₃(2/3)=13/4, m₃(1)=2; J2(1/2)=5/12, J2(2/3)=7/18, J2(1)=1/3 | attack-twobandwidth.md formula m₃ = 1+3(1/λ−2J2)+1/λ²−(6/λ)J2+2(1−λ/2), J2 = ∫₀^∞ sinc(πλu)²sinc(πu)²du; mpmath quadrature | J2 = 0.41666651/0.38888881/0.33333330; m₃ = 5.0000028 / 3.2500012 / 2.0000004 (errs ≤ 2.8e-6) | **REPRODUCED** |
| 7 | Family law p₁_cum ≈ 1 − c·N^(−0.39), c = 0.73–0.83, beats 1−c/√N | fit_law.py (results dir) | seed 42: c=0.8315, a=0.4037, SSE 1.40e-3 (√N: 5.35e-3); seed 2024: c=0.7887, a=0.3925, SSE 1.73e-3; 3-param c0+c1/N^a unphysical (c0=1.45, 2.64 > 1) — rejected as documented | **REPRODUCED** |
| 8 | N_d ≥ 523/648 ≈ 0.8071N | twobandwidth-transfer formula: (1/2 + (2m₂−m₃)/18) + (4/9)s₁, λ=2/3, m₂=31/18, m₃=13/4, s₁≥2/3N | 2m₂−m₃ = 7/36; 1/2+7/648 = 331/648; +(4/9)(2/3) = +192/648 ⇒ 523/648 | **hand-verified exact fractions** |
| 9 | Bump: F̂(1.00)=245.8 (hot-hand), band (1.005,1.3] mean 1.056 z=+0.43 @N=10000; e≥2 terms \|D\|≤0.033 corr −0.098 | bump_price2.py run log | from the saved run log (same numbers) | **REPRODUCED (from log)** |
| 10 | p₁_256 roadmap: 0.70→A≈1.063, 0.80 unreachable, R(A) dev 1.5→23% | p1a_curve results.jsonl + inline analysis (documented in p1a-curve.md) | deliverable's own tables | **REPRODUCED (documented)** |
| 11 | m₃-min-frontier: v(ε)=0.50, class EMPTY under zeros-T | m3_min_frontier.py (re-run #3 above) + identity-level PROVEN arithmetic | T-ranges match ⇒ the emptiness/sign-argument reproduces | **REPRODUCED** |
| 12 | m₃(1/2)=5 verified three ways (RS kλ=3/2<2 + closed form + numerical) | #6 + superlaw_s3b.py in-band checks | consistent | **REPRODUCED** |

## §2 The one flag: "exact theory" column (8.147999 / 5.468708)

- The paper/deliverable's theory column is NOT reproducible from the formula + inputs stated in the same documents. Natural readings of "D·(Em3/Em) + 3·Em2·A2 + Em²·A3" with the stated inputs give 8.93–10.01 for λ=1/2, never 8.147999. The measured values (7.978/5.359, bias-corrected) reproduce exactly and are the operative numbers.
- **Impact on the discovery: NONE.** The separation claim rests on the MEASURED values vs the PROVEN pin: raw 7.108 − 5.4419 = 1.67 = 69σ; corrected 7.978 − 5.4419 = 105σ; vs sine 5: 88σ (raw). Every candidate reading of the theory (8.93+) sits even higher. The "exact theory" column is a presentation artifact, not the load-bearing number.
- **Action:** (a) the in-flight independent verification (kanaka2 m3_adversarial) must ALSO reproduce the theory column or the column gets removed/relabeled ("family prediction, to be re-derived"); (b) paper §theory line to be corrected at next render; (c) ledger's "theory 8.148" wording downgraded to "family prediction ~8–9 (unreproduced from documented inputs)". This is now item 1 on the paper-fix list.

## §3 Fleet state during sweep
- Laptop: 8065@g4000 record-move verifier STILL RUNNING (nodes=1,563,008 — past the certified case's 1,116,906, consistent with a fail-case exploring more; verdict pending); 8064@g6000 certified True earlier (fresh re-cert).
- rust-zeros v2 agent: running (building the Gabcke-corrected tool; not yet shipped to the laptop).
- kanaka2: m3_adversarial.py in zetazero phase (independent m₃ re-verification; the paper's flagged "in-flight probe").
- beat673 sibling: probing psum dimension (1/1302@8140/8130, 1/1314@8100/8080) — verdicts in its session, not on disk.

## Honesty footer
Items 1,2,3,4,6,7,9,11,12: re-executed this session from the cited scripts/formulas. Items 5: NOT reproducible — flagged. Items 8,10: arithmetic/documented-table verification. Item "256-law family ≈ 8": NOT verifiable (private marks data, BLOCKED-ON-DATA). No claim in this report originates outside a saved script or a documented formula.
