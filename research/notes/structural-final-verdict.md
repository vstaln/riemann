# STRUCTURAL FINAL VERDICT — the bound frontier and the exact remaining gap

**Date:** 2026-08-13 (overnight). **Status:** PROVEN arithmetic + cited literature.

## Where we are (all certified, all pushed)

- **Simple-on-line: 0.673481** (α=1.464, coboundary redistribution, psum=1/320, eps=0.0062) — 3× verified.
- **Distinct: 0.836740** (=(1+H)/2, proven affine corollary).
- Coboundary lever EXHAUSTED: α, psum, coefficients all at the certified frontier.

## The exact remaining gap (PROVEN arithmetic)

The class ceiling is v\*(p₁) = p₁ + |E(1)|, |E(1)| = 1/(6·256²) = 2.54e-6, with shadow
price of p₁ exactly 1 (lpdual-realconfig-check.md, CHECKED NUMERICALLY). The ceiling
0.68183123 is attained at p₁ = p₀ = **0.6818287** (the 256-law's simple fraction).

To push the bound past 0.6818, one needs a certified simple-fraction bound p₁ > p₀:

| input | p₁ | v = p₁ + 2.54e-6 | source |
|---|---|---|---|
| 256-law (ceiling) | 0.68183 | 0.681831 | PROVEN (Lean, in-class optimal) |
| **unconditional best** | **~0.405** | 0.405 | Bui–Heap–Turnage–Young |
| **RH-conditional best** | **19/27 ≈ 0.70370** | **0.70371** | Bui–Heath–Brown 2013 |
| our certified (this session) | — | 0.673481 | coboundary, unconditional |

## Verdict

1. **Unconditionally, the ceiling 0.6818 is UNBREAKABLE with current inputs.** The best
   unconditional simple-fraction theorem (~0.405, BHTY) is far below p₀ = 0.6818. The gap
   0.6725 → 0.6818 (our record 0.673481 sits inside it) is certificate-class-limited, and the
   class cannot be exited without a beyond-bandwidth-1 p₁ that does not exist unconditionally.

2. **Under RH, the bound jumps to ~0.7037** (p₁ = 19/27 > p₀), but this is conditional on RH —
   a strictly stronger statement than what it proves. Not an unconditional result.

3. **Our record 0.673481 is the unconditional frontier of the coboundary certificate family.**
   It beats every published unconditional mechanism (tawanerguo 0.673193, trmdy 0.673138,
   ainta 0.673009) by ≥ +2.9e-4.

## The only remaining (non-circular) lever

A new UNCONDITIONAL theorem certifying the true zeros' simple fraction p₁ above ~0.6818. The
empirical evidence is overwhelming (all zeros simple in checked ranges, first 10¹³), but no
proof exists. This is a deep analytic number theory problem (equivalent in difficulty to a
strong zero-density / multiplicity theorem), NOT a certificate-optimization problem. It is
outside the reach of the current certificate machinery and would require a genuinely new
analytic input (e.g. a strengthening of Montgomery's pair-correlation to multiplicity
information, or an explicit-formula bound on Σ (m_ρ − 1) with m_ρ the multiplicity).

**s4h classification: HARD constraint (genuine limit, not assumption).** The certificate
machinery has been pushed to its unconditional frontier; further progress requires new
mathematics, not more optimization.
