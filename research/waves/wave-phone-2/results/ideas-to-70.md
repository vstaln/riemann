# IDEAS TO 70% — s4h orchestrated workflow (assumption-excavator → lateral-thinking → constraint-hardness → criteria)

**Date:** 2026-08-12 · **Brain:** phone · **Charter:** hooks/agents.md (honesty + PONYTAIL).
**Goal:** push the certified simple-on-line fraction past 0.70. Record 0.6732654365 (eps 8064, pending re-cert); in-class ceiling 0.6818312306 = p₀ + 1/(6·256²) < 0.70 ⟹ 70% REQUIRES a class change or new input.

---

## STEP 1 — ASSUMPTION EXCAVATION

**Problem as framed:** "Reach 70% simple-on-line for ζ via the certificate machinery."

### Surface (named constraints)
1. The bound formula (H−τ)/(1−B/m) is fixed; we tune (α, psum, m, eps). *(load: medium — eps-frontier line)*
2. eps is certified by the Arb verifier at grid=4000. *(load: medium — boundary shown genuine)*
3. The 256-law is the extremal config at p₀; EnclOK. *(load: high — private data)*
4. Marks ∈ {1,2}. *(load: low — ζ zeros are conjectured simple)*

### Structural (the framing itself)
1. **"The certificate's value is capped at p₀ by the 256-law"** — assumes the 256-law is IN every certificate class. The m₃-separation discovery (superlaw-s3.md: super-law marked m₃ = 7.98 vs proven 5; 256-law family position ≈ 8, pinned ≥ 5.4419) **excludes the 256-law too** from the m₃ = 5±ε class. The class's true extremal config is UNKNOWN — its p₁ could be above OR below p₀. **THE PRICE IS UNCOMPUTED.**
2. "Any certificate valid against all two-moment configs ≤ p₀" — true, but the m₃ read shrank the class (leg 2 of the wall fell).
3. **"Beyond-1 is out of the certificate's support (r lives on [0,1])"** — PARTLY FALSE: the f1curve wall says r may have support up to A = 511/256 ≈ 1.9961. The beyond-1 rows j/N (j ≤ 2N) are LEGAL LP data; only F ≡ 1 on [1,A] is unproven for ζ. The exact p₁(A) curve from the extended-row LP needs NO private family (idea 4 of ceiling-ideas).
4. **"The distinct-count lane was closed (P6.5 negative)"** — REFRAME: the twobandwidth note's "clean negative" means only "cannot beat the CONDITIONAL 5/6 wall". Its own computation gives **N_d ≥ 41/54 = 0.7593 (λ=1/2) and ≥ 0.8071 (λ=2/3) with PROVEN unconditional third moments** — both ABOVE 70% and above Farmer's 0.6603 distinct record — gated only on the CONJECTURED transfer of the paper's admissible-cubic Schur–Horn step to λ<1. Nobody checked whether 0.8071 itself is a headline number.
5. "Numerics are verification, never the product" — but the m₃=5 read and the S₃ = sine value are PROVEN asymptotics; their ε-budget (explicit RS/BGST error) is the only gap to a fully unconditional class.

### Identity
1. "We must prove unconditional bounds for ζ" — the conditional roadmap (0.70@A=1.04 under M2) is parked; it's a choice, not a law.
2. "The (c₀, r) simple-count certificate is THE architecture" — the c=3 distinct functional + moment-weight LP is a different architecture that ALREADY reads third moments.
3. "We race the simple-on-line record" — distinct-on-line is a different (weaker-but-bigger) statement; Farmer 0.6603 is the target to beat there.

---

## STEP 2 — LATERAL MOVES (dominant idea: "in-class certificates capped at p₀; only escape is conjectural beyond-1")

| # | Assumption escaped | Lateral move | Opens |
|---|---|---|---|
| L1 | "0.8071 is below the 5/6 wall, so useless" | Re-scope the distinct lane as the 70% route: verify the λ=2/3 admissible-cubic transfer | A new theorem ≥ 0.8071 distinct-on-line (or the transfer refuted with a script) |
| L2 | "The 256-law is in every class" | Compute the m₃=5±ε pinned LP optimum at N=64/256 — the price of the separation | Either the m₃ class value > p₀ (a real climb) or a documented exact price |
| L3 | "m₃=5 needs only asymptotic validity" | Carry the explicit RS/BGST ε-budget through the m₃ read (ε vs the 0.44/2.98 margins) | Unconditional class semantics; quantifies the error chain |
| L4 | "r lives on [0,1]" | Extended-row LP p₁(A) for A up to 1.996, public N=64 data only | Exact conditional roadmap (0.70@1.04) + tests whether public data moves the value |
| L5 | "The law is admissible" | Beurling/Vasyunin realization probe — can ANY generalized-prime zeta realize near-CUE in-band reads? | If no: arithmetic admissibility cracks the ceiling's premise (new class). If yes: rigidity win |
| L6 | "Certificates read configurations" | The pencil/inertia family (W_re + θW_im): joint structure across θ, not a moment | First candidate functional of MORE than two moments that's geometric, not moment-based |
| L7 | "Simple-on-line is the only goal" | Distinct-on-line ≥ 0.8071 + multiplicity bookkeeping ⟹ simple-on-line via N_d = s₁ + a₂ relations | Maps a provable distinct bound to the user's 70% simple goal |
| L8 | "The (α,psum) family is exhausted" | The α≈1.0–1.3 empirical bump (≥11σ) — decompose by τ-bin/prime-power, price under M3 | The only real sliver of beyond-1 structure; a conditional target with a price |

---

## STEP 3 — CONSTRAINT HARDNESS (the walls the lateral moves must pass)

| Wall | Source | Consequence if violated | Hardness |
|---|---|---|---|
| Universal two-moment ceiling (value ≤ p₀) | Proven rigidity (256-law in class, super-law matches all two-moment reads) | — | **HARD for two-moment reads** — but SOFT as a statement about m₃-reading classes (the m₃ read is beyond-two-moment; separation already shown) |
| f1curve bandwidth wall (A ≤ 1.996) | Proven LP infeasibility ≥ 2 | — | **HARD** — L4 must stay below 1.996 |
| m₃ ≥ 2 priced −1/3 (simple cert) | Exact identity m₃ = 4−3p₁ | — | **HARD for the SIMPLE cert reading m₃ ≥ 2 as a one-sided constraint** — does NOT bind the marked-m₃ = 5 two-sided pin (different read) |
| No cross-window Schur–Horn inequality | LP-structure analysis (PROVEN) | — | **HARD for two-window mixing** — does NOT bind single-window λ=2/3 (the 0.8071 needs only ONE window) |
| Admissible-cubic transfer to λ<1 | Paper's §7.5(g) proven at λ=1; transfer UNTESTED | If false, 0.8071 → 41/54 or lower | **ASSUMED** (untested!) — the single most valuable thing to test |
| s₁ ≥ 2/3 (Thm B) | Classical unconditional | — | HARD (and the program's 0.6733 record beats it) |
| Beyond-1 F ≡ 1 for ζ | M29: proven bounds fail by 3.6·10³× | — | **HARD for ζ unconditionally** — but the beyond-1 EMPIRICAL bump (L8) is not a wall, it's data |
| 70% itself | — | — | Not a wall: 0.6818 ceiling < 0.70 means class change required; the m₃ class and the distinct lane are the two live doors |

---

## STEP 4 — RANKED FUNDING LIST (plausibility × novelty × probe cost)

1. **twobandwidth-transfer (L1+L7): the 0.8071 lead.** Verify the λ=2/3 admissible-cubic Schur–Horn transfer; pin N_d semantics (distinct-on-line?); map N_d → simple-on-line. **If the transfer holds: N_d ≥ 0.8071N unconditional — a result above 70% and above Farmer 0.6603.** Probe: reading + algebra + HiGHS LP + one numeric check. Cost: LOW. Value: HIGHEST.
2. **m3-price (L2+L3): the separation's price.** Marked-config LP at N=64/256 with the marked-windowed m₃ = 5±ε two-sided pin; compute the m₃-class optimum vs p₀(64). If > p₀: the m₃ class climbs toward 70%. Also carry the RS ε-budget. Probe: existing rgl/LP machinery. Cost: LOW. Value: HIGH (direct continuation of a landed discovery).
3. **p1A-curve (L4): exact conditional roadmap on public data.** Extended-row LP at N=64, A ∈ {1.0, 1.03, 1.26, 1.70, 1.99}. Cost: LOW. Value: MEDIUM (conditional, but makes the roadmap exact + checks the M2 model).
4. **bump-price (L8): the α≈1.1 sliver.** Decompose the ≥11σ empirical bump; price under M3. Cost: LOW-MED. Value: MEDIUM (only real beyond-1 data).
5. **beurling (L5): arithmetic admissibility.** Vasyunin realization probe. Cost: MED. Value: MED-HIGH if it cracks the ceiling premise.
6. **pencil (L6):** long shot. Cost: MED. Value: LOW-MED.

---

## RESULT (honest)

- **CONJECTURED NEW THEOREM within reach: N_d ≥ 0.8071N at λ=2/3 (distinct count) — gated on the transfer of the paper's admissible-cubic step to λ<1, untested by the prior P6.5 note (which only scored it vs the conditional 5/6).** Above 70% and above Farmer 0.6603.
- **CONJECTURED: the m₃=5 pinned class value may exceed p₀** (256-law excluded at ≈8); price uncomputed — the direct monetization of the m₃-separation discovery.
- HARD walls confirmed: two-moment ceiling (class-level), bandwidth ≤ 1.996, one-sided m₃ ≥ 2 for the simple cert, no cross-window inequality. All lateral moves route around or through the ASSUMED (testable) walls.
- Funded next: twobandwidth-transfer + m3-price (this session). p1A-curve + bump-price queued for the judge pass.
