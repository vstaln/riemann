# ATTACK TREE — many sub-steps instead of frontal assault (2026-08-12)

**Context:** record 0.6732660791400006829 (eps=8065 @ P=1/1320, α=1.49, m=133). The frontal eps-frontier at the record's triple is CLOSED (8066 fails at cell 10.647). This doc decomposes the remaining ground into small, independently-verifiable sub-steps, each with a verdict. Two new dials discovered this session by reading the machinery instead of pushing eps.

## The machinery (from attack_bound_check.py + verify_cos7.py — both CHECKED NUMERICALLY)
```
H(α)   = 2 − 1/c,  c = I₀²/(I₂+J)                       [α only; H peaks near α≈1.41–1.45]
A      = eps·(m−6)                                      [eps = certified target /1e6]
B      = Φ_m(A),  Φ = E if E ≤ m/(m−1) else 2√((m−1)E/m)−1+E/m
τ      = psum·(m−6)/m,  psum = (n−1)·P                  [P = verifier pressure = psum/(n−1)]
bound  = (H − τ)/(1 − B/m)
```
**Cell-count identity (THE key read):** verifier's `cutoff_units = target/pressure = eps·P_den/1e6`. The record sits at **10.646 cells** (8065·1320/1e6); 8066 → 10.647 fails. **The certificate's real limit is the cell count** — eps and P are NOT independent; eps ≈ c·P·1e6 with c ≈ 10.6 the frontier.

## Sub-step tree

### LANE A — P-ascent at constant cell count (NEW this session; the record lane)
Moving to LARGER P and larger eps together keeps the cell count ≈10.6 but shifts the bound:
| sub-step | P | eps (cell-model) | bound if certifies | status |
|---|---|---|---|---|
| A1 | 1/1320 | 8065 | 0.6732660791 (record) | ✅ certified |
| A2 | 1/1284 | 8291 | ~0.67327 | beat673 probing 8258→8259 |
| A3 | 1/1200 | 8833 | **0.673311** | probe 8700/8800 RUNNING |
| A4 | 1/1100 | 9636 | **0.673353** | probe 9500 RUNNING, 9600 queued |
| A5 | 1/1000 | 10646 | **0.673385** | probes 10550/10650 queued |
| A6 | 1/900 | 11778 | 0.673385 (peak? falls after) | future |
- Verdicts: each cert = the cell-frontier holds at that P (model CONFIRMED → A6+ worth it); each fail = frontier shrinks, model breaks at that P.
- **Model check baked in:** if A3 (8700) certifies but A3 (8800) fails, the frontier at P=1/1200 is ~8750 → new cell-limit there.

### LANE B — α-move at the record P (H-lane)
H(α) peaks near α≈1.41–1.45 (H(1.41)=0.6725005 vs H(1.49)=0.6724219, +7.9e-5 headroom) BUT eps_cert falls as α drops below 1.49 (measured: 8050 @ α=1.485). Sub-steps: certify eps at (α, P=1/1320) ∈ {(1.47, 8065), (1.45, 8000), (1.51, 8100)} → map eps_cert(α) → optimize bound(α, eps_cert(α)). Joint with Lane A (α at the P-ascent point) is the full 2D frontier.

### LANE C — the n-family (NEW; verify_n9.py already running = the decisive probe)
n=7 (6 gaps, P = psum/6 = 1/1320) is the certified family. verify_n9.py: n=9 (8 gaps, P = psum/8 = 1/1760), kappa-model floor ≈ 0.00809 > record's 0.008065. If n=9 certifies: **a new family with a HIGHER floor** — the n=9 bound formula (its own H_n9, m_n9, τ) must then be derived. Sub-steps: C1 n=9 cert (RUNNING 40+ min); C2 derive the n=9 bound constants; C3 n=11 (P = psum/10) if C1-C2 land. n=9's floor 0.00809 → bound ≈ (H_9 − τ_9)/(1−B/m_9) — the constants decide whether it beats 0.67327.

### LANE D — zero-finder speed (DONE this session: parallel)
- D1 ✅ 100k in ~75 s single-core (step 0.2), validated 5.6e-4.
- D2 ✅ win-mode shards: 8-core [14, 5.6e5] → ~1M zeros niced, RUNNING.
- D3 future: height-adaptive step (12% saving — not worth it); Odlyzko Gram-block sieving (~100×, only if 10⁸+ zeros ever wanted).
- D4 next use: marked-T read at 1M (the 0.70 gap input) + clean small-gap regime.

### LANE E — the 0.70 decomposition (the long path, from ideas-to-70.md)
The identified missing input for 70%: a PROVEN bound on the marked connected part T = m₃ − D − pair (zeros-realized range [+0.333, +0.401] @ N=256; asymptotic A3(1/2)=+1/2 PROVEN). Decomposition:
- E1: high-N read of T (1M zeros, tight error) — empirical floor of the T-window.
- E2: prove the T-lower-bound (the third-order hole) — the actual theorem; E1 maps the target.
- E3: distinct-lane transfer (λ=2/3 admissible-cubic Schur–Horn, 0.8071N — untested hinge).
- E4: super-law/marked-m₃ exact theory column (the flagged 8.147999) — re-derive or remove.

## Honest state
- A3-A5 probes + C1 (n=9) are RUNNING on the laptop right now; verdicts are CHECKED-NUMERICALLY per probe.
- The cell-model (eps ≈ c·P·1e6, c ≈ 10.6) is CONJECTURED — A2/A3 will confirm or refute it at the first new P.
- The α-lane trade (B) is CONJECTURED until eps_cert(α) is mapped at more points.
- n=9 bound constants (C2) are NOT yet derived — if C1 certifies, C2 is the next sub-step.
