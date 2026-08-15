# WAVE 6 — ADVERSARIAL VALIDATION OF THE 0.673481 CERTIFIED RECORD (mission-critical)

**Context shift:** The repo holds certified records 0.673481 (simple-on-line) / 0.836740
(distinct), labeled UNCONDITIONAL in records-vs-anthropic-paper-2026-08-13.md — both above
Anthropic's claimed optimized constants (0.6725 / 0.83625) and far above the published PRZZ
record (0.417). IF these certificates survive adversarial validation, the campaign has ALREADY
achieved its headline goal. Therefore wave 6 = hostile blind referees on the record chain,
NOT a new-record hunt.

**Why the record is NOT yet trusted:**
1. FINAL-RECORD-2026-08-13.md honesty ledger: "NOT YET: Lean formalization of this specific
   α/redistribution; second-machine audit." Only CHECKED NUMERICALLY (Arb interval verifier,
   3 identical runs on one machine/one implementation).
2. The bound chain `bound = (H(α) − τ)/(1 − B/m)` with H(1.464) = 0.672467425578 produces
   0.673481 > the PROVEN window ceiling 0.6725007 — the gain comes from the redistribution
   denominator (1 − B/m). Any algebraic move that lifts a certificate above a proven ceiling
   of its own class is exactly where the sinc-m3 E[T]≥0 bug lived. Must be re-derived from
   first principles, not trusted.
3. The transfer to ζ rests on: Montgomery's theorem (F=1 on [0,1], unconditional, limit with
   no explicit rate), mean density (unconditional), integrality (trivial), and the stability
   inequality (Lean-PROVEN analytic identity). The liminf/error-structure of the transfer must
   be stated precisely and checked.

**Three disjoint referee joints (blind, forbidden to read each other's notes):**

- **6A — the redistribution algebra (builder):** Re-derive `bound = (H(α) − τ)/(1 − B/m)`
  from the rank–trace lemma + coboundary mechanism FIRST PRINCIPLES. What exactly is B, what
  is m, why is division by (1 − B/m) valid, and what inequality does the result certify?
  Cross-check against the source modules (PairCeiling/Stability/Ceiling/NearCUE/Bridge +
  verify_coboundary_floor.py). Attack the move: does it hide an invalid bound (like E[T]≥0)?
  Deliverable: verdict VALID / BROKEN with the exact step isolated.

- **6B — the transfer to ζ (builder):** State the EXACT theorem that 0.673481 proves about
  the zeros of ζ. Is it liminf_{T→∞} N_s(1/2,T)/N(1/2,T) ≥ 0.673481 unconditionally? Where
  does Montgomery's F=1 on [0,1] enter, and does the certificate need F at grid points j/N
  (j=1..N) — including j=N (α=1, the singular edge)? Is the rate issue (o(1), no explicit
  error) correctly handled as a liminf statement, or is there a hidden subsequence/eps
  problem? Deliverable: the precise theorem statement + verdict.

- **6C — second-machine independent re-derivation (builder):** Reimplement the certificate
  VALUE computation (H(α) at α=1.464, τ, B/m, eps=0.0062 floor certification, 0.673481) from
  scratch in a SEPARATE implementation (different library / different quadrature / direct
  interval-free float + separate check), WITHOUT reading verify_coboundary_floor.py's code
  (read only the math in the notes). Must reproduce 0.6734808616745137 (or explain the
  discrepancy) AND re-certify eps=0.0062 (630/1e5 must fail, 620/1e5 must pass).

**Discipline:** RUST ONLY for any new computation (Python only if mpmath-level precision is
unavoidable, one-line justification). Deliverable note after ≤3 file reads or first 5 tool
calls. No weakening anything. The 256-law's own ceiling (0.6818) must NOT be exceeded by any
claimed value — if your re-derivation gives >0.6818, you have a bug, not a discovery.

**Outputs:** three notes: wave6-refereeA-redistribution-2026-08-17.md,
wave6-refereeB-transfer-2026-08-17.md, wave6-refereeC-secondmachine-2026-08-17.md.
