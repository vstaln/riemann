# agy battery adjudication — /tmp/rh_wave3/b{1..8}.out (2026-08-21)

Adjudicated against DEAD-LEVERS.md and independent numerical recheck (this session).

## b1 — Weil prime-error budget, from-scratch derivation → **UPGRADE: CHECKED NUMERICALLY**
- Gaussian-modulated test function φ̂₀(t)=√π·σ²(t−t₀)e^{−σ²(t−t₀)²/2}, symmetrized; prime tail
  R₁(X)=2Σ_{p>X}(log p)H(p); integration by parts with Dusart θ(x)≤1.000028x.
- **Independent recheck (this session, sieve to 10⁷)**:
  - Non-oscillatory bound at X=808: direct sum = **0.002753 < 0.01** ✓ (b1's analytic bound conservative)
  - Oscillatory R(100)=2Σ(log p)H(p)cos(50 log p) = **+0.005595** vs b1's 0.006123 ✓ (cutoff diff)
- Consequence: the earlier W_X=0.39058731 (T=50, X=10⁶, σ=1) is NOT vacuous — prime-error budget
  orders below signal. Weil-truncated-inside-Jensen lane upgraded CONJECTURED → CHECKED NUMERICALLY.
- Honest limitation (b1's own label, correct): a SINGLE test function certifies one scalar inequality,
  not RH-below-T; need dense Galerkin family (Bombieri 2000 Thm 10: finite Q_N negative eigenvalue ⟺
  off-line zeros in band). That Galerkin direction is the live follow-up.

## b2 — Two-case covering detection floor → NOTED (conditional)
Formalizes the c=0.75/r=0.30 disc with corrected L=5√11/9: cert 0.182322+L·Δt covers RH case;
planted worst-case 0.6281. Sound but conditional — collapses to classical zero-counting when made
unconditional (known dead end). Keep as machinery, not a lane.

## b3 — Beurling defect residue lemma → **REFUTED [PROVEN by agy, accepted]**
The claimed lemma d_N²(β₀) ≥ C/N^{2(1−β₀)} justified by "ζ(ρ₀)=0 kills ζ∗P_N so M[f_N](ρ₀)=1/ρ₀"
does NOT follow — the residue argument does not apply to the proposed convolution normalization.
Lane killed; added to DEAD-LEVERS. (Consistent with builder's beurling_defect_floor.rs being
pre-asymptotic only.)

## b4 — λ_n spectral phases to n=10⁵ → LIVE, unfunded
Correctly avoids Lipschitz/residue traps; uses proven Li identity λ_n=Σ_ρ[1−(1−1/ρ)^n] with the
CORRECT variable z=1−1/ρ (post-audit-b8). Spectral engine (li_lambda_spectral.rs) already validated
to n=8000; extension to 10⁵ is O(N) phasor recurrence — cheap Rust work, queued.

## b5 — Info-geometric KL formulation → CONCEPTUAL, no discriminator
Avoids known traps rhetorically but produces no falsifiable number. Parked.

## b6 — GUE form factor K(n) → INCOMPLETE
agy launched a background calc that never returned in-output. No numbers to adjudicate. Re-run if the
spectral-engine extension (b4) lands.

## b7 — de Branges Hermite-Biehler obstruction → CONFIRMS KNOWN DEAD END
HB class requires |E(z)|>|E(z̄)| in C⁺; ζ-paired E functions fail this structurally. Matches
DEAD-LEVERS de Branges entry. No new opening.

## b8 — Adversarial audit of L=5√11/9 → **VERIFIED & SOUND**
Confirms the corrected Lipschitz constant geometry (d₀=1/4, support √0.0275≈0.16583, disjoint
neighborhoods since min spacing 1.219 > 2·0.16583). Already committed (bd0895a).

## Net session effect
+1 lane upgraded (Weil-truncated w/ real budget), +1 lemma refuted (NB residue), 1 queue item
confirmed live (λ_n→10⁵), everything else consistent with existing dead-lever map.
