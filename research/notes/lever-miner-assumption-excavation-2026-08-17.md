# Lever-Miner: Assumption Excavation on the Five Walls

**Date:** 2026-08-17 · **Method:** s4h-creativity-assumption-excavator (read-only, no computation)
**Sources read:** structural-final-verdict.md, attack-ceiling.md, structural-thread-newinput-2026-08-14.md; plus M6 synthesis context as supplied. File citations verified present in research/notes/ (ls). Every claim labeled PROVEN / CHECKED NUMERICALLY / CONJECTURED / INCONCLUSIVE per source labels; I did not run any computation.

## 1. Per-wall assumption table

### Wall 1 — in-class certificate ceiling 0.6818 (Lean LP-dual, shadow price of p₁ = 1)

| Embedded assumption | HARD/SOFT | Why (one line) | What would relax it |
|---|---|---|---|
| A1 Certificate class = rank-trace, reading bandwidth-one data (mean density, F on [0,1], integer multiplicity atoms ≤ 2) | HARD within class; boundary is SOFT | Ceiling is PROVEN for exactly this class; but "the class" is a definitional convention — a certificate reading more data is a *different* class with a different ceiling | A new class reading marked/multiplicity-weighted moments (marked-m₃); super-law separation is the first probe |
| A2 The 256 near-CUE law is admissible (|256·S(j)−j| ≤ 3e-40, marks ≤ 2, Σ marks = 256, p₀ = 0.68182868746…) | SOFT | Admissibility rests on EnclOK = INCONCLUSIVE: law's exact weights live only in authors' private cert (sha256 cc3de991), not independently re-derived; NOT REFUTED, single non-Lean link | Regenerate the law by re-solving its defining LP (regenerate-256law.md, in flight): match → EnclOK CHECKED; differ → ceiling REFUTED |
| A3 A certificate valid against ALL configurations is valid against this one law | HARD (PROVEN) | Configuration-free stability identity + single-law instance; no arithmetic content | — |
| A4 The law is the worst case for the whole class | HARD-but-argued (CHECKED NUMERICALLY) | LP optimum over 256-periodic marked configs; formalized statement is the single-law instance only | — (not needed for the ceiling argument itself) |
| A5 Rank-trace at c=2 cannot separate on-line doubles from tight off-line pairs (TightMult) | HARD (PROVEN) | k₂(2) = 4 = c² in Lean | A different inequality consuming more inputs (eigenvalues, marked moments) = different class (A1) |

### Wall 2 — window ceiling 0.6725007 (2 − 1/c₁* = 0.672500703679…, Theorem D)

| B1 Window subclass = block structure + two traces + primes up to T, one-delta kernel | SOFT | Window optimum (0.6725) is NOT the class optimum (0.6818); §7.1 "no window does better" is optimality *within the window subclass only* | Any in-class certificate above 0.6725, e.g. the 256-law dual / marked-m₃ reading; gap 0.6725→0.6818 is PROVEN-open |
|---|---|---|---|
| B2 Variational optimum reads only F on [−1,1]; Montgomery–Taylor kernel extremal (CCLM17 Cor 14) | HARD (PROVEN) | Proven optimal for that input set | Beyond-bandwidth-1 input (Wall 3) — none proven |

### Wall 3 — beyond-α=1 pair correlation closed from every direction

| C1 BGSTB unconditional Montgomery theorem only for 0 ≤ α ≤ 1 (uniform); no evaluation for α > 1 (off-diagonal terms need prime-pair info) | HARD (PROVEN) | Root of the ceiling (2501.14545; paper §7.5(a)) | Proven estimate for F on some (1, 1+δ), or proven bound on Σ_m (Λ∗Λ)(m)(Λ∗Λ)(m+h), h ≤ X²/T (HL-equivalent) |
|---|---|---|---|
| C2 F ≥ 0 for all α is only an inequality (bounds kernels from above), not a value | HARD (PROVEN) | bgst (3.4); insufficient for positive-kernel lower bounds | Unconditional SDP majorant of the CGdL type |
| C3 α > 1 regime ≡ Hardy–Littlewood prime-pair conjecture (GM87) | HARD (PROVEN-as-cited) | Cited equivalence | Conjectural input only |
| C4 Gram moments: diagonal method only in Rudnick–Sarnak kλ < 2; k ≤ 3 only λ < 2/3; odd moments don't lower Λ₁(0); Prop 7.4 (rank ≤ d) kills λ ≤ 1/2 | HARD (PROVEN, paper §7.5(e)) | Structural facts of the unmarked moment machinery | Marked (multiplicity-weighted) moments — different object, transfer UNTESTED (Lever 1) |
| C5 ξ′ transport (FGL) is a different function | HARD (PROVEN) | Different certificate target | — |

### Wall 4 — third moment does not break the 5/6 distinct wall (5/6 target per mission contract; "5/6" not found verbatim in the three read files — files give ours 0.836740 = (1+H)/2 and N_d ≥ 0.85082 under RH via triple correlation)

| D1 Distinct bound = (1+H)/2 affine corollary | HARD (PROVEN) | Proven affine identity | Only via H (Wall 1) |
|---|---|---|---|
| D2 Odd (third) moment does not lower Λ₁(0) | HARD for unmarked moments (PROVEN) | Structural fact of the unmarked machinery | Marked-m₃: transfer UNTESTED — the soft crack |
| D3 Hejhal triple correlation (RH) only in kλ < 2; serves distinct counts, not simple-on-line | HARD (PROVEN-conditional) | Conditional, wrong target type | Unconditional triple-correlation input — none |

### Wall 5 — RH does not move the in-class ceiling

| E1 The near-CUE law matches ALL bandwidth-one data, including RH's F = 1 on [0,1] | HARD (PROVEN) | RH-conditional certificates read identical data → identical ceiling | Only outside the class |
|---|---|---|---|
| E2 RH moves the bound (→ ~0.7037) only via a different mechanism (Bui–Heath-Brown, p₁ = 19/27) | HARD (PROVEN, RH-conditional) | RH is inert in-class; lives at the class boundary | Unconditional discrete-moment mechanism (Lever 3) |

## 2. Top-3 ranked untested levers

### Lever 1 (TOP): Marked-m₃-reading certificate LP — extend the class, not the number theory
- **The lever:** solve the marked-m₃-reading certificate LP and test whether it separates the 256-law from the super-law adversary (adversarial-m3-reverify-2026-08-17.md exists and is live per M6 synthesis).
- **Exact assumption targeted:** A1 class boundary (SOFT) and D2 — "odd moments do not lower Λ₁(0)" is PROVEN only for *unmarked* moments; the marked object's uselessness is untested.
- **Checkable first probe:** (a) solve the marked-m₃ LP; (b) does the optimum exceed 0.6725 / approach 0.6818; (c) does the m₃ reading separate the super-law from the near-CUE law; (d) if separated, does real-configuration m₃ data rule out the super-law — a structural constraint on admissible configurations, directly attacking the ceiling's premise (the law's admissibility), i.e. attack-ceiling §4's "FUND" item.
- **Honesty label: INCONCLUSIVE** — lever is live but I have not read its outputs; the PROVEN ceiling theorem does not bound this extended class; whether marked-m₃ data is certifiable (ζ triple correlation under RH in kλ<2, or conjecturally) is unestablished.

### Lever 2: Goldston–Suriajaya double-sum/box estimate, supplied by Guth–Maynard zero-density
- **The lever:** do not attack Wall 3 with F(α>1) values; use BGSTB's hypothesis class — a general estimate on a double sum over zeros, or the box |β − 1/2| < 1/(2 log T) for T^{3/8} < γ ≤ T — and test whether Guth–Maynard's N(σ,T) near σ = 1/2 certifies it.
- **Exact assumption targeted:** C1 (HARD, the root of the ceiling) — but the GS framework has already reduced RH to a single explicit estimate (PROVEN framework, 2511.20059 / 2603.28104).
- **Checkable first probe:** quantify the box-strength/proportion tradeoff: BGSTB's box already yields 0.617 (PROVEN-conditional); determine what box size or positive-proportion guarantee pushes p₁ past p₀ = 0.6818, then check Guth–Maynard (PROVEN theorem, 2024) near σ = 1/2 against that requirement.
- **Honesty label: CONJECTURED / INCONCLUSIVE** — 0.617 < 0.6818 and the box is unproven; no theorem certifying the needed estimate exists in the surveyed literature (structural-thread §0).

### Lever 3: Partially unconditionalize the Bui–Heath-Brown discrete-moment mechanism
- **The lever:** 19/27 (RH-conditional) is the only known shape that clears p₀; decompose arXiv:1302.5018 into RH-essential vs control-suppliable estimates (on-line ζ/ζ′ averages, mollifier length) and identify any unconditional subset.
- **Exact assumption targeted:** Wall 1's premise "no unconditional simple-fraction theorem exceeds p₀" — a *literature fact* (best unconditional ~0.4075, PRZZ), not a theorem that no such input can exist.
- **Checkable first probe:** obtain and read 1302.5018 (not yet in local sources), tabulate which estimates are RH-only, and check whether a Guth–Maynard-supplied mollifier (θ past 6/11) or BGSTB box control covers any; compute the partial proportion.
- **Honesty label: CONJECTURED / INCONCLUSIVE** — removing RH here appears strictly harder than Lever 2 (structural-thread §2); no partial result in the surveyed literature.

*(Not ranked, in flight — avoid re-dispatch: EnclOK regeneration / adversarial ceiling check, regenerate-256law.md, agent d5af80ab. It is the single highest-value SOFT point: if the regenerated law differs, the ceiling is REFUTED.)*

## 3. SOFT assumptions — re-openable without new number theory

1. **A2 (EnclOK admissibility of the 256-law)** — INCONCLUSIVE verification gap, not a theorem. Regeneration can upgrade to CHECKED NUMERICALLY or REFUTE the ceiling. In flight.
2. **B1 (window subclass)** — 0.6725007 is a subclass artifact; the in-class gap 0.6725 → 0.6818 is PROVEN-open and needs only a certificate, no new number theory.
3. **D2-transfer (marked vs unmarked odd moments)** — untested; marked-m₃ may sidestep "odd moments useless" (Lever 1).
4. **A1 class boundary (all walls)** — "rank-trace bandwidth-one" is a convention; extended classes reading marked/multiplicity-weighted data carry new ceilings. The super-law separation is the first probe.

**Verdict: not all walls are pure theorem-level.** Three of the five carry at least one SOFT or INCONCLUSIVE embedded assumption (Wall 1: A2; Wall 2: B1; Wall 4: D2-transfer, plus the A1 boundary across all). A "no soft assumptions" verdict would have been wrong — I looked, and the soft spots are: one unverified-enclosure gap, one subclass convention, and one untested marked-moment transfer. Walls 3 and 5 are genuinely HARD as stated.
