# Structural leverage synthesis — where the bound actually lives, and the single highest-leverage intervention

**Agent:** THINKER/SYNTHESIZER (systems-leverage-analysis)
**Date:** 2026-08-13 (overnight, user-asleep confirmed)
**Method:** s4h-systems-leverage-analysis applied to the corrected bound and its proven walls.
**Labels:** PROVEN / CHECKED NUMERICALLY / CONJECTURED / ABANDONED / INCONCLUSIVE per hooks/agents.md.
**Framing (per the skill's Step-1 check):** the system is the certified lower bound
`B = (H − τ)/(1 − B/m)` and its surrounding certificate class (rank–trace, bandwidth-one inputs);
the intervention set examined is {H-window tweaks, eps floor lifts, psum cuts, m-retunes, the
denominator upgrade I9, non-uniform/coboundary weight redistribution, beyond-bandwidth-1 data,
ruling out the 256-law}. As a sub-agent operating autonomously, I ran the full analysis rather than
the AskUserQuestion check-ins.

Every number below was produced by the scripts in §6 (this session, mpmath 40–50 dps) unless a
source note is cited. Every PROVEN wall is cited to its committed note.

---

## 0. The honest state, restated

- Corrected bound **0.6730690** at (α=1.49, psum=1/220, eps=0.007759, m=137) — CERTIFIED twice with the
  fixed single-normalization verifier (`retraction-673-invalid.md`). Beats ainta 0.6730085; **below**
  trmdy 0.6731376 and tawanerguo 0.6731929.
- Window ceiling **H = 0.6725007** at α=√2 — PROVEN (Lean, Theorem D / `Functional.lean` HD(1));
  robust across 8 window families at the numeric level (idea-systems §4; twotone-refuted).
- Class ceiling **0.6818287** (p₀ of the near-CUE 256-law) — PROVEN (Lean) modulo the numerically-checked
  enclosure EnclOK; **attained in-class** at p₀ + |E(1)| = 0.68183123 by the exact certificate r = 1−x
  (attack-lpdual.md, close-inclass-gap.md). In-class optimality is closed; real-zero constant is still 0.6725.
- Dead: third-moment (unconditional; PROVEN attack-thirdmoment.md), n-point (F_n/n falls with n), two-tone,
  beyond-1 form factor (only CONJECTURED — attack-ceiling.md §3).
- Breakthrough insight on file: tawanerguo wins via a **coboundary redistribution** that certifies
  psum=1/320; the untried combo = the same mechanism at α=1.49 or α=√2 (synthesis-combine-2026-08-13.md §7).

---

## 1. Systems map of the bound

```
        ┌──────────────────┐   H(alpha) ──────────────┐
        │  window kernel   │                          ▼
        │  cos(alpha·s)    │              ┌───────────────────────┐
        └──────────────────┘              │  numerator: H − tau    │
        ┌──────────────────┐   eps ──► A=eps(m−6) ──► B=Phi(A,m) ──► 1 − B/m  (denominator)
        │  6-gap floor F   │                            ▲
        └──────────────────┘                            │ concave Bellman cap
        ┌──────────────────┐   psum ──► tau=psum(m−6)/m  │ (the tax, in numerator)
        │   pressure       │                            │
        └──────────────────┘                            │
                 │                                      │
                 └──► certification effort (verifier) ◄──┘  eps ↔ psum COUPLED (loop 4)
```

### Amplifiers
| element | size | role | source |
|---|---|---|---|
| denominator 1 − B/m | ×1.0078 | the only amplifier; **nearly inert** | idea-systems §1/§2 (decomposition: B/m = 0.0076959) |
| H → numerator | ×1.0 | linear, capped | idea-systems §2 |
| eps → A → B (dB/deps = 126.008) | concave | amplifies eps into denominator defect | idea-systems §2 (CHECKED NUMERICALLY) |

### Saturators
| element | behavior | source |
|---|---|---|
| eps loop | strongly concave: d²B/deps² = −38.35; marginal gain decays 0.645→0.417 | idea-systems §2 (CHECKED NUMERICALLY) |
| H | hard cap 0.6725007, all 8 window families ≤ cap | PROVEN (Lean Thm D); idea-systems §4 (numeric) |
| m | flat optimum ~137 (uniform) / ~176–183 (coboundary) | idea-systems §2; this note §4 |

### Hard walls (PROVEN, cited)
| wall | value | label + source |
|---|---|---|
| window ceiling | H ≤ 0.6725007036794116 | PROVEN (Lean Thm D; attack-kernel.md, synthesis-crosscheck; re-confirmed this session §6) |
| class ceiling | v ≤ 0.681828687 + 2.55·10⁻⁶(·) ; attained 0.68183123 | PROVEN (Lean `ceiling_law256_signed`, modulo EnclOK INCONCLUSIVE); attack-ceiling.md, attack-lpdual.md, close-inclass-gap.md |
| third moment | 2m₂−m₃ ≤ 7/36 at λ<2/3; best cert 0.81 < 5/6 | PROVEN (attack-thirdmoment.md; corrected m₃(1)=2, adjudicated) |
| n-point | F_n/n falls with n | exec-npoint.md; retraction-673-invalid.md §3 |
| two-tone | max H = classic constant 0.6725007 | twotone-refuted.md; retraction §"also" |
| beyond bandwidth 1 | F(α) for α>1: none proven; = Hardy–Littlewood prime-pair problem | attack-ceiling.md §3 (literature-verified; everything CONJECTURED) |

### Feedback loops
1. **Reinforcing-but-saturating eps loop** — eps↑→A↑→B↑→bound↑; concave (saturates).
2. **Linear tax loop** — psum↓→τ↓→bound↑; exactly linear (d²B/dpsum² ≈ 2.7·10⁻³⁹), never saturates —
   the only loop with no saturation (idea-systems §1, CHECKED NUMERICALLY).
3. **Window loop** — α→H→bound; hard ceiling at √2.
4. **The governor: eps–psum negative coupling** — certifying a larger floor at a denser pressure is more
   expensive; empirically `eps_ach = C·pinv^{−k}` with **k ≈ 0.83 at α=1.49** (idea-systems §1/§8,
   CHECKED NUMERICALLY). Since k ≈ 1, eps and psum trade off ~1:1 in certification effort. **This is the
   single negative feedback loop that pins the bound to a Pareto ridge.**

**Meadows reading.** The default target of the program has been **parameters** (α, eps, psum, m sweeps) —
cheap, tooling-ready, and where the record arithmetic lives. The system's true structure is:
numerator capped (H), the floor concave (eps), the tax linear-but-coupled (psum ↔ eps via loop 4),
the denominator inert (×1.0078), and the *class* capped (0.6818). The high-leverage points that are
routinely under-funded are (i) the **feedback-loop structure** (loop 4 — break the coupling) and
(ii) the **information flow / rules of the system** (beyond-1 data; the certificate class itself) — the
latter two being hard walls (§2, §3 of attack-ceiling.md).

---

## 2. The Meadows intervention table

| Intervention | Leverage level | Type | Feasibility | Resistance source |
|---|---|---|---|---|
| α / m retunes | LOW | parameter | high (tooling ready) | H cap (PROVEN); m already optimal |
| eps lift, uniform weights | LOW–MED | parameter / flow | high | concave; crystal adversary saturates it |
| psum cut (tax) | MEDIUM apparent, LOW actual | parameter | high | **loop 4 coupling k≈0.83 cancels 1:1** (CHECKED NUMERICALLY) |
| **Coboundary / non-uniform redistribution (break loop 4)** | **HIGH (feasible set)** | **feedback-loop structure** | **medium — core verifier ready, coefficients need re-derivation** | the coupling itself; α-specific coefficients (see §4) |
| I9 second-moment denominator | HIGH ceiling (+0.6pp) | rules / structure (new functional) | LOW — pure theory | §7.5(e): odd moments add nothing; no unconditional even-moment evaluation outside Rudnick–Sarnak range (PROVEN) |
| Beyond-1 form factor | HIGHEST ceiling (shadow price 1:1, → ~1.0) | paradigm / information flow | **NONE** | HARD WALL — only CONJECTURED data exists (attack-ceiling §3) |
| Rule out the 256-law (multiplicity constraint) | HIGH (breaks 0.6818) | structure | **NONE** | nothing of the kind known or plausible (attack-ceiling §3) |

**Default level being targeted:** parameters — because the record-fixing happened there, the verifier
makes sweeps cheap, and the coupling's existence was only quantified recently (idea-systems loop 4).

**Ignored high-leverage options and why they are avoided:**
- **Beyond-1 data** — avoided because it is conjectural: the α>1 evaluation is equivalent to the
  Hardy–Littlewood prime-pair estimates (attack-ceiling §3.7.5(a)). It is the true attractor (shadow
  price 1.0, LP-probed, attack-lpdual §3), not an actionable lever.
- **Ruling out the 256-law** — avoided because no structural constraint on ζ's zeros excluding the law's
  shape is known (attack-ceiling §3).
- **I9 denominator** — avoided because the unconditional moment evaluation stops at the RS range kλ<2
  and odd moments do not lower Λ₁(0) (attack-thirdmoment, PROVEN).
- These are the paradigm-level points; they face maximum resistance because they require *new theorems*,
  not new arithmetic.

---

## 3. The SINGLE highest-leverage intervention (ranked)

**Rank 1 — the untried combo: coboundary redistribution re-optimized at α=1.49 / α=√2 with psum=1/320.**
This is the intervention with the highest leverage × feasibility product. Rationale:

1. **It targets the true governor.** Loop 4 (eps–psum coupling, k≈0.83) is the only non-saturating
   constraint pinning the family, and the psum loop is the only non-saturating amplifier of the bound.
   Breaking the coupling is the *only* move that frees both knobs at once (idea-systems I1; confirmed as
   the systems catalog's #1 lever after the window door closed).
2. **The mechanism is proven real.** tawanerguo's coboundary U(g₁..g₅) with redistributed coefficients
   p=(946,1177,877,877,1177,946)/1920000, q=(31343/100000, 1/3, 105971/300000, …) certifies F_B ≥ 577/1e5
   at psum=1/320 — a *looser* pressure than our 1/220 — with a 1.1M-node verified tree
   (BELLMAN_COBBOUNDARY_PROOF.md; reproduced in verify-tawanerguo-bellman.md). The coupling **has been
   broken once**; the untried part is re-deriving the coefficients for a better operating point.
3. **The payoff is quantified (CHECKED NUMERICALLY, §6).** At psum=1/320, m=183:

   | α | threshold eps to beat tawanerguo 0.6731929 |
   |---|---|
   | 1.49 | ≥ **0.0058271** |
   | √2 | ≥ **0.0057052** |
   | 1.47 (tawan's own) | > 0.00577 (its own floor) |

   The H-peak at √2 buys ~1.2·10⁻⁴ of eps budget. Representative outcomes:
   (1.49, 1/320, 0.0060, m=183) → **0.6733039** (+1.1·10⁻⁴ over tawan);
   (1.49, 1/320, 0.0065) → **0.6736164** (+4.2·10⁻⁴);
   (√2, 1/320, 0.0060) → **0.6733832** (+1.9·10⁻⁴);
   (√2, 1/320, 0.0058, m=182) → **0.6732547**. m-optimization adds a further ~1.4·10⁻⁶ (m* ≈ 176–182).
4. **Even a clean negative is a decisive result** (see §4): it proves the coupling is *structural*, not a
   certificate artifact, and closes the family at ~0.6731 with evidence — redirecting the search to the
   structural walls (I9 / beyond-1) on a documented basis.

**Rank 2 — C1 non-uniform weight search** (`tools/beat673/weight_search.py`, WEIGHTS_JSON ready): a
parallel, cheaper attack on the same loop-4 coupling via the pair weights a_ij (capacity Σ a_{i,i+r} ≤ 2).
Unproven mechanism (CONJECTURED) but tooling is fully ready; can run while the coboundary driver is built.
Expected: CONJECTURED, even +5·10⁻⁵ on eps moves the bound toward trmdy (need eps ≥ 0.00787 @ 1/220).

**Rank 3 — eps/psum/m re-optimization at fixed mechanism** (the parameter default): C3 (H-peak α) is DONE
and NEGATIVE (CHECKED NUMERICALLY, synthesis §6: α=√2 certifies 0.00745 → bound 0.672955 < record).
Remaining parameter moves are on the ridge and model-dependent; low value.

**Rank 4 — I9 (second-moment denominator).** Highest *ceiling* (×1.05 amplifier → 0.70+ territory,
idea-systems §6 CONJECTURED) but LOWEST feasibility: unconditional odd-moment evaluation dead (PROVEN),
no even-moment evaluation outside the RS range exists. **The long shot, not the right next spend.**

**Honest expected payoff of Rank 1:** CONJECTURED (synthesizer judgment) — a real chance to beat
tawanerguo (0.67319) and reach ~0.6733–0.6740 (the family ceiling, idea-systems §6 CONJECTURED), but
**not** 0.6818: the class ceiling requires p₁ ≥ 0.6818 for the *real* zeros, which is beyond-1
(CONJECTURED) — no in-class redistribution reaches it (attack-lpdual §5, attack-ceiling §3). The lever
closes the *tawanerguo gap* and tests the family's true ceiling; the 0.6818 wall is a separate,
structure-level problem.

---

## 4. The critical structural fact that governs the experiment (CHECKED NUMERICALLY, §6)

The tawan coboundary coefficients were optimized for **α=1.47's kernel near-minima**. They are not freely
transferable, because:

1. The kernel w(x) = (K(x)/K(0))² has **no zeros on (0,4]** for any of α ∈ {1.47, 1.49, √2} — the
   "crystal" sites z₁≈1.057, z₂≈2.03, z₃≈3.02 are *near-minima*, not zeros.
2. Their depths vary enormously with α:

   | α | w(1.057) | w(2.03) | w(3.02) |
   |---|---|---|---|
   | 1.47 | 2.34·10⁻⁵ | 1.54·10⁻⁶ | 3.75·10⁻⁷ |
   | 1.49 | 4.27·10⁻⁵ | 2.85·10⁻⁶ | 6.61·10⁻⁷ |
   | √2 | **5.97·10⁻⁸** | 8.07·10⁻¹⁰ | 4.56·10⁻⁹ |

   At α=√2 the crystal is **~715× deeper** at z₁ than at α=1.49. This is why C3 failed (√2's uniform floor
   0.00745 < 1.49's 0.007759): the crystal bites harder at the H-peak.

**Consequence for the combo:** the redistribution must be *re-derived* at each α (the whole point of the
coboundary is to push pressure off the crystal-occupied spans — a deeper crystal means more to gain if
the coefficients can de-weight those spans, but the search must find them). The two candidates trade:
α=1.49 has a shallower crystal (coefficients closer to tawan's, but needs eps ≥ 0.00583, i.e. a *better*
redistribution than tawan's own); α=√2 has a deeper crystal but needs only eps ≥ 0.00571 (tawan-level
transfer would already clear the bar, if it certifies at all).

---

## 5. Concrete next experiment for the top intervention

**Objective:** decide, with a certificate, whether the coboundary redistribution at psum=1/320 certifies
eps ≥ 0.00583 @ α=1.49 or ≥ 0.00571 @ α=√2 — i.e. beats tawanerguo. **Even a clean negative is a funded
result:** it proves the coupling is structural and closes the family at ~0.6731.

**Tooling status:** the verification core is READY — `tools/verify_coboundary_floor.py` implements
`verify_floor(..., cap_scheme="coboundary", pressure_coeffs=p_i, nearest_coeffs=q_i)` with Arb interval
branch-and-bound and exact-LDL tangent pruning (reproduces tawan's 577/1e5 tree). What is missing is a
thin driver that (i) swaps the kernel to α=1.49 / √2, (ii) sweeps coefficient families, (iii) binary-searches
the certifiable target. That driver is the deliverable of this experiment.

**Script (new, self-contained): `tools/redistribute_search.py`** (imports `verify_floor` from
`verify_coboundary_floor.py`; PONYTAIL-compliant, one `assert`-based self-check):

- **Stage 0 — sanity:** reproduce tawanerguo (α=1.47, p_i/q_i as in the repo, target 577/1e5,
  `verify=True`, tree identity 1126636−563286=563350). Guard: any code change that breaks this is a bug.
- **Stage 1 — cheapest probe (zero new coefficients):** run `verify_floor` with **tawan's own (p_i, q_i)**
  at α=1.49 and α=√2, uniform a_ij, psum=1/320, binary-search max certifiable eps (node budget ~5M like the
  repo cert, grid 4000). If eps ≥ threshold at either α → done, bound beats tawanerguo (m-optimize).
- **Stage 2 — coefficient re-optimization (only if Stage 1 fails):** parametrize the coboundary form
  U(g₁..g₅) = Σ a_k g_k + Σ b_k w(g_k) with the telescoping constraints Σp = 1/320, Σq = 2 (matching
  tawan's structure), and a float probe of the min of F_B over the 5-dim gap simplex (scipy multistart /
  SLSQP on the normalized simplex) to rank candidate (p_i, q_i) by float floor; take the top candidates
  through the interval verifier and binary-search the certifiable eps.
- **Stage 3 — bound:** for the certified (α, eps, psum=1/320), sweep m ∈ [120, 260] (mpmath, exact formula
  from `evaluate_coboundary_bound.py`) and report the best bound vs tawanerguo 0.6731929114731423.
- **Self-check:** `assert` tawan baseline reproduces; `assert` Σp = 1/320, Σq = 2 for every candidate.

**Command:** `uv run --quiet --with mpmath --with python-flint python tools/redistribute_search.py`
(prec 128 arb, as in the tawan tree). Heavy stage-1/2 runs can be sharded via the existing node-budget
parameter; do NOT touch `tools/verify_coboundary_floor.py` (another agent may own it — copy the driver
alongside and say so, per hooks).

**What each outcome proves:**
- **Success (eps ≥ threshold certified):** the coupling is a *certificate artifact*, breakable; bound
  moves to 0.6733–0.6740 (CHECKED NUMERICALLY arithmetic; the eps itself CERTIFIED). Beats tawanerguo,
  re-ranks the program's standing vs the external mechanisms, and demonstrates the family has slack
  toward the (in-class) ceiling.
- **Clean negative (no coefficient family certifies ≥ threshold at either α):** the untried combo is DEAD
  (documented negative with script). Combined with C3 (α=√2's uniform floor is worse), this proves the
  eps–psum coupling is **structural** at the family level, that 0.6730690 is within ~1·10⁻⁴ of the family
  ceiling (~0.6736–0.6740, CONJECTURED), and the search should stop funding in-family parameter moves and
  redirect to the structural walls: I9 (denominator), beyond-1 data, or ruling out the 256-law — each
  labeled as requiring a new theorem (CONJECTURED input absent), not more sweeps.

**Time/effort:** Stage 0–1 is a few hours of verifier time (tawan's tree was 1.1M nodes); Stage 2 is the
open-ended part (coefficient search). Run Stage 0–1 first; it is the honest cheapest decisive probe.

---

## 6. Scripts and reproducibility (every number in this note)

| Claim | Script / command | Label |
|---|---|---|
| tawanerguo 0.6731929114731423, ours 0.6730690301666756, all §7 combos, H(α), thresholds 0.0058271/0.0057052/0.00577, m-opt 176/182, bound table | mpmath 40–50 dps, inline heredoc (§4 of this session's transcript) — exact formula from `evaluate_coboundary_bound.py` and `final_leader.py` | CHECKED NUMERICALLY (reproduces both committed records to 45+ digits) |
| w(x) near-minima at α ∈ {1.47, 1.49, √2} (no zeros on (0,4]; depths 2.34e-5 / 4.27e-5 / 5.97e-8 at 1.057) | mpmath root-scan + point eval, inline heredoc | CHECKED NUMERICALLY |
| dH/dα ≈ 0 at √2 (H-peak is at √2) | mpmath central difference | CHECKED NUMERICALLY |

**PROVEN walls and their sources (cited, not re-derived here):**
- Window ceiling 0.6725007 — attack-kernel.md (PROVEN in Lean), synthesis-crosscheck-2026-08-13.md.
- Class ceiling 0.6818 / in-class optimum 0.68183123 — attack-ceiling.md (Lean, modulo EnclOK
  INCONCLUSIVE per validation-enclok.md), attack-lpdual.md, close-inclass-gap.md (exact rational certificate).
- Third-moment dead — attack-thirdmoment.md (PROVEN; m₃(1)=2 adjudicated vs P6.5).
- n-point dead — exec-npoint.md; retraction-673-invalid.md §3.
- Two-tone dead — twotone-refuted.md; idea-systems §4 (8 window families ≤ ceiling).
- Beyond-1 only CONJECTURED — attack-ceiling.md §3 (literature-verified).
- eps–psum coupling k≈0.83 — idea-systems §1/§8 (CHECKED NUMERICALLY, Rust `sens` + mpmath).
- Record 0.6730690 and C3 negative — retraction-673-invalid.md; synthesis-combine §6.

---

## 7. Bottom line

1. **Highest-leverage feasible intervention: the coboundary redistribution re-optimized at α=1.49/√2 with
   psum=1/320** — it attacks the only non-saturating negative feedback loop (eps–psum coupling), via a
   mechanism PROVEN to work (tawanerguo, reproduced), with quantified thresholds (eps ≥ 0.00583 @ 1.49,
   ≥ 0.00571 @ √2 beats tawanerguo) and ready core tooling.
2. **The honest ceiling of this lever is ~0.674, not 0.6818.** The class ceiling is attained in-class
   (attack-lpdual), and reaching 0.6818 for the real zeros requires p₁ ≥ 0.6818 — a beyond-bandwidth-1
   input that is CONJECTURED / absent (attack-ceiling §3). The 0.6818 wall is a structure-level problem
   (I9, beyond-1 data, or ruling out the 256-law), none of which is currently fundable with a theorem in
   hand.
3. **Run Stage 0–1 of `tools/redistribute_search.py` first** (tawan's coefficients at α=1.49/√2, certify,
   binary-search eps). It is the cheapest decisive probe; a clean negative is a funded result that closes
   the family and redirects the search.
