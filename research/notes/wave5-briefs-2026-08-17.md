# Wave-5 Brief A — M4-proper: mechanical re-derivation of BHB Lemma 1 with ζ′ → ζ″

**Target:** Pin the constant r′ in the quadratic-form box bound. Current state: BHB in-class
certificate ceiling 0.6818 (PROVEN structural); the box form needs |β−1/2| ≤ b/L with
E/S₂ ≤ 8b²(r+r′), r = 99/1274 ≈ 0.0777 (PROVEN), and r′ is UNKNOWN (O(1)-scale). The
previously-claimed r′ = 3/5 (giving b ≈ 0.0758) was REFUTED as derived: its anchor
(T/2π)L³/3 contradicts Gonek's theorem Σ|ζ′(ρ)|² ~ (T/2π)ℒ⁴/12 (arXiv:1302.5032, verbatim).

**Objects to use:**
- research/notes/bhb-m6-synthesis-2026-08-14.md (the M4-proper spec, §3.2 and §5)
- research/notes/bhb-adversarial-validator-af-2026-08-17.md (the validator that broke r′=3/5)
- tools/zeta-rs (Rust, Euler-Maclaurin Z(t) critical-line; subcommand `explicit`/`mv` for
  moment verification), tools/bhb_synth/ or the bhb-* scripts if present
- BHB (Baluyot–Heath-Brown) Lemma 1 structure: diagonal + ℳ-analogue terms + convexity

**The task (closed-form, no heavy compute):**
Mechanically re-derive BHB's Lemma-1 moment with ζ′ replaced by ζ″: the diagonal, the three
ℳ-analogue terms, and the convexity step. Output: the exact constant r′ = lim (1/L²)·(1/N)Σ
contributions, or a PROOF that r′ is not pinned by this route (label each claim PROVEN /
CHECKED NUMERICALLY with a Rust binary / CONJECTURED).

**Coordinator's forecast:** r′ will NOT come out to 3/5 again (that value's anchor is dead).
Realistic outcomes: (a) r′ comes out to some O(1) constant that still keeps b ≤ 0.2237 ceiling
(box stays 2.2× narrower than BGSTB's b=1/2) — then the lever is CLOSED as unproductive;
(b) r′ is genuinely 0 or negative (breaks the quadratic form — unlikely, would be a surprise
win); (c) the ζ″-moment diverges in a way that invalidates the box-form reduction entirely —
that would be a real structural finding (the box approach needs a different form).

**RH-false control demand (mandatory):** run the SAME mechanical re-derivation for the
Davenport–Heilbronn function (tools/barrier_zoo_rs model_dh once fixed, or its certified
off-line zeros) and for the fake-Weil polynomial world. If the ζ″-moment route would "prove"
RH-incompatible behavior for those worlds (e.g., forces b ≤ 0 there), the route proves too
much and is dead. If it says nothing about them (their moments differ structurally), that's
the honest firewall position.

**Budget:** ≤12 turns, ≤15 tool calls, deliverable-first (note after ≤3 reads / 5 calls).
Note ≤150 lines, scripts ≤80. Rust ONLY. At ~85% context stop + finalize.
**Deliverable:** research/notes/m4-proper-zdouble-2026-08-17.md, labeled with r′ verdict +
the control output. Model: opencode-go/deepseek-v4-flash, background.

## Wave-5 Brief B — k<1 moving-boundary count: prove the route empty (Type-1 decision)

**Target:** The binding input N(1/2+b/L, T) = o(T log T) at b ≈ 0.0758 (moving boundary
1/2+b/log t). This is THE one-way-door decision point of the plan. The ledger says: Shape-1
families blind (PROVEN scale-gap lemma); Ingham k=5 gives only b ~ 3 log log T; GM-family is
Shape-1; a Shape-2 k<1 theorem via GM's method is CONJECTURED-impossible (gm-box obstacle (ii):
zero-detection loses a fixed log power via Littlewood–Jensen).

**Forecast (wrong direction, per Anthropic E2 playbook):** the route is EMPTY — no known method
gets k<1 at a fixed moving boundary. Your job is to prove the emptiness rigorously OR find the
inversion (the empty route's dual often IS the theorem — E2 found this twice).

**Objects to use:**
- research/notes/bhb-m6-synthesis-2026-08-14.md (§3.1, the scale-gap lemma, Ingham k=5 bound)
- research/notes/offcentre-positivity-probe-2026-08-17.md (why the LMFDB data route is vacuous)
- tools/argprinciple (Rust, zeros data), tools/zeta-rs (Rust, explicit formulas)
- Literature (fetch if network allows): Ingham's k=5 theorem; GM = Guth–Maynard zero-detection;
  Littlewood–Jensen identity

**The task:**
1. Reproduce the PROVEN walls: scale-gap lemma (Shape-1 families cannot see the moving
   boundary), Ingham k=5 → b ~ 3 log log T (only log-scale boundary, not fixed), GM
   zero-detection loses a fixed log power (Littlewood–Jensen). Each wall: PROVEN (with the
   argument written out) or CHECKED NUMERICALLY (Rust probe).
2. The inversion hunt: the empty-route dual. E2's pattern: bound the count in the NEGATIVE
   direction, find it empty, then its dual gives a lower bound on the on-line proportion.
   What is the dual of "N(1/2+b/L,T) = o(T log T)"? Candidates: (i) a lower bound on the
   number of zeros in the strip beyond the boundary — trivial (all off-line zeros are there);
   (ii) the pair-identity form E = Σ_pairs |F(ρ)−F(1−ρ̄)|² ≥ 0 — a sum-of-squares exposure
   (this is the structure that relaxed the box need 5.7×; can it be pushed further?);
   (iii) BGSTB strong zero-density hypothesis — is there any unconditional partial input?
3. VERDICT: is the k<1 fixed-boundary count reachable by any known route (Type-1 YES) or
   genuinely one-way-door closed (Type-1 NO)? Either way the decision is a result — the plan
   needs this decision to reallocate.

**RH-false control demand (mandatory):** the Davenport–Heilbronn function (certified off-line
zeros at σ=0.8085, t=85.7 and σ=0.6508, t=114.16) has off-line zeros with β−1/2 ≈ 0.31 — FAR
above any b/L boundary. Check: does DH satisfy or violate N(1/2+b/L,T)=o(T log T)? If DH
violates it, the count is NOT a universal analytic fact — it's specific to zeta and needs
zeta-specific inputs (fine, but say so). If DH satisfies it trivially, the count is weak
(holds for RH-false objects → zero evidence, firewall). No fake-Weil analogue exists (no
critical-line structure) — say so.

**Budget:** ≤12 turns, ≤15 tool calls, deliverable-first. Note ≤150 lines, scripts ≤80.
Rust ONLY (probes in tools/k1_count_probe/). At ~85% context stop + finalize.
**Deliverable:** research/notes/k1-moving-boundary-decision-2026-08-17.md: Type-1 decision
(YES/NO with evidence), each wall labeled, the inversion hunt result (empty or found), the
DH control verdict, the firewall statement. Model: opencode-go/deepseek-v4-flash, background.
