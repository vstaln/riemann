# Wave-25 next-move probe — prime-truncated Weil form negativity (2026-08-19)

**Question (from wave-25 "Single Next Move"):** does the truncated Weil form W_{X,B}
develop a negative eigenvalue when prime depth X < exp(B), as the wave-25 executor's
"boundary prime-resonance barrier" (g0-0) claimed?

**Tool:** tools/wave25_schur_weil_probe.py (clean rewrite; sieve semantics fixed).

## Result — REFUTED (CHECKED NUMERICALLY)

1. **No prime-depth barrier exists.** λ_min(W_{X,B}) is negative at ALL prime depths
   (log X = B/2, B, B+1.5) and — with the proper Archimedean integral — **identical
   across log X = 3.8 / 5.8 / 8.0** (e.g. B=1.8,M=8: −0.3343 at every logX; B=2.5,M=8:
   −0.6687 at every logX). Adding primes changes nothing. The claimed transition at
   log X = B (Archimedean O(B) vs prime −Ω(exp(B/2)/B)) does NOT appear.
2. **Negativity is a finite-basis discretization artifact, not a barrier.** With X→∞
   (logX=8 covers all primes ≤ exp(8)=2981 within support), λ_min stays negative and
   X-independent. The −log π mass + finite wavelet Gram of the Weil distribution
   naturally has negative modes — expected and harmless (a finite Gram of W is not
   the full positivity certificate over all admissible h).
3. **DH control is identical.** Replacing prime weights with non-multiplicative
   character-mod-5 weights (|c(n)|≤1) gives the same negativity to ±0.1 (−0.83..−2.65
   vs −0.82..−2.70 across the table). The construction never separates the RH world
   from the RH-false world — it "proves too much" (or rather proves nothing, since
   the negativity is basis-artifact on both sides).

## Verdict

- **Wave-25 g0-0 "boundary prime-resonance" claim: REFUTED by its own cheapest probe.**
  Consistent with the wave-25 verifier's statement-level kills (g0-0 Turán-counts-fire-
  on-DH + Paley–Wiener; g0-1 density attribution can't separate DH; g1-2 phase-adapted
  construction fires on DH/Epstein-2). The executed probe confirms the mechanism does
  not exist numerically.
- **Wave-25 "Single Next Move" (boundary Schur-complement LMI): ABANDONED.** Its
  foundation (the X < exp(B) barrier) is refuted; there is no transition to certify.
- No RH content either way: the negativity is a basis artifact, not a zero-location
  statement. Firewall intact.

## Files
- tools/wave25_schur_weil_probe.py (probe), /tmp/weil_sanity.py (Archimedean-integral
  variant), wave-25 artifacts in research/waves/wave-25/.
