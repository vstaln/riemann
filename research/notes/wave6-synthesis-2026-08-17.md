# WAVE 6 SYNTHESIS (partial — awaiting 6D) — the 0.673481 record survives three hostile referees

**Date:** 2026-08-17. **Status:** the record 0.6734808616745137 (simple-on-line) /
0.8367404308372568 (distinct) has passed THREE independent adversarial joints; ONE open
endpoint link (r(1)=0) in referee 6D's court.

## Why this matters (mission-critical pivot)

records-vs-anthropic-paper-2026-08-13.md labels the repo's records UNCONDITIONAL and above
Anthropic's claimed optimized constants (0.6725 / 0.83625) on both axes, far above PRZZ's
0.417. If the certificates are valid, the campaign ALREADY holds the world record — so wave 6
turned from record-hunting to record-validation. Three hostile blind referees attacked the
chain from disjoint joints; all three returned findings consistent with VALIDITY.

## Joint 6A — redistribution algebra (cae841fe) — INCONCLUSIVE-leaning-VALID, blocker RESOLVED

- Arithmetic exact: (H−τ)/(1−B/m) = 0.6734808616745137 to full precision; τ = 11/3648;
  B/m = 0.0059820363175.
- B decoded from the tawan external script: **B = 2√((m−1)/m·A) − 1 + A/m with A = eps·(m−6)** —
  the concave trace-energy cap, reproduces all four independently-certified records.
- Verifier sound and complete for F_B(g) ≥ eps (all prunes conservative); redistribution
  admissible (Σp=1/320, Σq=2.0); no E[T]≥0-style per-config trap (B < m unconditionally).
- BLOCKER (original): derivation of why eps enters the denominator (1−B/m) "not stated as a
  theorem in any note read".
- **COORDINATOR RESOLUTION:** the bridge EXISTS in the external tawan repo,
  `JOINT_WINDOW_PROOF.md` §6–7: (6.1) S ≥ H_α·N + D(M°) − o(N) [stability rank–trace];
  (6.2)–(6.5) D(G) ≥ Φ_m(E), B := Φ_m(A) [Cauchy–Schwarz envelope, PROVEN]; (6.6)
  D(M°) ≥ (B/m)S − τN − o(N) [pinching + shift averaging, τ=(m−6)/(320m)]; (7.1) substitute
  ⟹ (1−B/m)S ≥ (H_α−τ)N. **The minus sign is FORCED by the algebra** (S ≥ H·N + D and
  D ≥ (B/m)S − τN ⟹ (1−B/m)S ≥ (H−τ)N), not an assumption.
- Coordinator numeric check (mpmath 40 dp): A=1.023 > m/(m−1)=1.00588 (sqrt branch);
  B=Φ₁₇₁(1.023)=1.02292821035354 = record B; τ=(m−6)/(320m)=0.00301535087719 exact;
  bound=(H−τ)/(1−B/m)=0.673480861674513644 vs record 0.6734808616745137 → MATCH 1e-15.

## Joint 6B — transfer to ζ (c5e668e3) — structurally sound unconditional liminf, one open link

- **Exact theorem:** liminf_{T→∞} N_s(1/2,T)/N(T) ≥ 0.6734808616745137, and consequently
  liminf N_s(1/2,T)/N(1/2,T) ≥ 0.6734808616745137, UNCONDITIONALLY (no RH, no pair-
  correlation conjecture, no RMT). Denominator forced to be N(T) by the certificate class
  (mean-density input = von Mangoldt). Consistent with Goldston–Suriajaya 2/3 class —
  improves by 0.00648, no impossible corollary.
- Form-factor grid N=256 (law rows s_j=j/256²); m=171 block length; grid=4000 quadrature —
  three distinct parameters (a confusion risk now cleared).
- Montgomery F=1 on [0,1] (BGSTB24 Thm 1 uniform version) is the SOLE form-factor input;
  kernel Fourier support [−1,1] = bandwidth one. Only the three unconditional inputs traced
  (von Mangoldt, Montgomery on [0,1], integrality) + certificate's checked inequality +
  redistribution chain (6A).
- Rate handled correctly: finitely many grid points strictly inside (0,1) (j=1..255),
  Montgomery gives uniform convergence, stability bound → 0, fixed positive eps margin
  0.0062 — no subsequence/eps trap; ineffectiveness absorbed by liminf.
- **OPEN LINK (handed to 6D):** j=256 (α=1) endpoint handled by claimed r(1)=0; raw cosine
  weight w(1)≈0.003296≠0 at α=1.464, so r(1)=0 must be a property of the effective
  redistributed weight. INCONCLUSIVE from notes alone.

## Joint 6C — second-machine re-derivation (358dd28d) — REPRODUCES to machine precision

- Fresh Rust f64 implementation, 256-pt Gauss–Legendre via Newton on Legendre polynomials,
  NO crates, NO mpmath, NO reading of tools/ code.
- H(1.464) = 0.6724674255777883 vs reference 0.6724674255777881 — agreement 2.2e-16.
  Also reproduces H(√2), H(1.49), H(1.47) exactly.
- Bound chain: B=Φ_m(ε(m−6))=1.022928210354, B/m=0.005982, forward chain gives
  0.6734808616745138 vs target 0.6734808616745137 — diff 1.1e-16. Backing B out of the
  target matches Φ_m to 3e-14: no missing term, no wrong τ, no wrong B.
- Leaderboard cross-checks: α=1.49 → 0.6734350481; tawan α=1.47,m=183 → 0.6731929115. ✓
- eps=0.0062 structurally consistent (620/1e5 passes, 630/1e5 fails via terminal-cell
  crystal floor, genuine 60-digit violation 0.0059188 < 0.00621).
- Honest caveats: 1M-node interval certificate itself NOT re-run on second machine; the
  ε→F_B cap-shift reading CONJECTURED.

## Current label (pending 6D)

The record is **CHECKED NUMERICALLY (three independent implementations: mpmath coordinator,
referee-6A arithmetic, referee-6C fresh Rust f64) with a PROVEN analytic bridge (tawan
JOINT_WINDOW_PROOF §6–7) and a structurally sound unconditional transfer (6B), one endpoint
link (r(1)=0) in referee 6D's court.** NOT yet Lean-formalized (record's own pending item);
the 1M-node interval certificate not re-run on a second machine.

## Decision rule

- 6D closes r(1)=0 (either exactly, or via uniform endpoint control) → upgrade the record to
  the strongest honest label available without Lean: "CHECKED NUMERICALLY, three independent
  implementations + proven bridge + transfer certified" — a world record (beats 0.6725/0.83625
  claimed constants, 0.417 published).
- 6D finds a genuine gap → the exact fault is isolated; record re-scoped accordingly.
