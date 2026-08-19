# WAVE-32 FRONTIER — genuinely-new one-way RH discriminators (2026-08-19)

## Mission
Find a genuinely NEW one-way computational object separating the RH world from RH-false
controls BY COMPUTATION. Every candidate gets its own probe + RH-false control (DH, Epstein
class-2, planted-zero Beurling) before any belief. Every claim labeled. No uncomputed numbers.

## PROVEN frontier facts (this session, verified; do NOT re-derive, DO build on)
1. **Re(zeta'/zeta)(1/2+it) = log(pi)/2 - 0.5 Re psi(1/4+it/2)** — pure gamma factor, ZERO
   config content (verified 1e-13). The real part of the log-derivative on the line is
   FE-forced. (commit d644dd4)
2. **FE-forced-ness is 0th-order ONLY**: 2Re((zeta'/zeta)') = 2/(t-gamma)^2 + ... (ratio
   1.0000 near poles) — the 1st log-derivative real part is pure zero-location content, a
   DIPOLE DETECTOR. Dipole detectors never separate RH from RH-false (on-line and off-line
   zeros give identical wells). (commit 50e0ba4)
3. **xi-jet certificate lane PROVEN-impossible**: jet positivity + Cauchy/weighted sums +
   explicit formula gives at best O(T/log T) simple-count lower bounds (zero proportion).
   (commit 732593f)
4. **d_N^2 <= 1 ALWAYS** (L^2 projection error): any divergence claim for d_N is false.
   (wave-28 g0-1)
5. **Re(-Z'/Z)(1/2+it) is FE-determined by the gamma factor** — invariant to off-line zeros.
   (wave-28 g1-1)

## CLOSED families (blocklist — if a candidate fits, reject before compute)
pole/zero-location restatements (radius, resolvent, multiplier poles, F(s+1/2)/F(s), nodal
count D(T)=N_zeros-N_signchanges = definition of RH); dipole-well mechanisms (midpoint
Hessians, log-derivative curvature, mollified wells, Fejer Im(-Z'/Z)); Euler-product
presuppositions (martingale-orthogonality, scale orthogonality — undefined for DH/Epstein);
short-window |zeta|^2/log|zeta| averages (Bohr-Toeplitz, commutators, prime-fiber, Slepian);
d_N bounds; Weil/dB form positivity (X-independent, fires on DH); Li; Gram spectral; Jensen
finite audits; explicit-formula projections; moment ratios at zeros (r', Q_3); B-D coefficient
energy; Hankel radius; Turan jets; prime-zeta holomorphy; Stieltjes moment Hankel (moment
matrix of positive measure always PSD = tautology); prime-cosh invariants (circular — needs
beta_k); ternary hyperdeterminants (FE-family); prime-zero cross-Gram (explicit-formula
restatement); shifted-zeta Hankel minors (pole-penetration).

## Unexplored classes (target these)
1. EXACT-IDENTITY-vs-NONZERO dichotomy: a determinant/expression IDENTICALLY zero on RH-world
   data, NONZERO when an off-line zero exists (not small-vs-large, but zero-vs-nonzero).
2. HIGHER-ORDER zero correlations (pair/triple ordinate correlations) as genuine separators,
   with an exact finite-N identity failing in a planted world.
3. UNCONDITIONAL arithmetic objects: exact finite sums over integers/primes whose value is a
   KNOWN constant under RH (EXACT, not asymptotic) and provably different without it.
4. FE + Euler product TOGETHER, so a planted zero breaks BOTH symmetries at once — as an
   EXACT break (finite identity), not a limit.
5. Rationality/algebraicity-class changes between worlds (differ in KIND, not degree).

## Controls
Davenport-Heilbronn (off-line zeros, no Euler product; f_plus slow — budget carefully),
Epstein class-2 Q=5x^2+2xy+13y^2 or x^2+5y^2 (off-line doublets, Euler product),
planted-zero Beurling (Euler product + planted zero).

## Constraints
- NO predicted numbers: every candidate's probe must be run before belief; agy-fabricated
  gaps are the known failure mode (wave-26: wrong by 5+ orders, wrong direction).
- Every verifier must produce: the exact statement checked, the numeric result, the RH-false
  control result, and a PROVEN/REFUTED/INCONCLUSIVE verdict.
- The swarm's generators historically collapse to duplicates (wave-23, wave-28): use 2
  maximally-different generator prompts and reject identical outputs.
- mpmath caution: mp.zeta(s, 1) is BROKEN (returns zeta(s)); use mp.diff(mp.zeta, s, n).
