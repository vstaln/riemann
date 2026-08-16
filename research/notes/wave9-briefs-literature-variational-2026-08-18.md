# WAVE 9 BRIEFS — literature-driven variational / SDP directions (record-side + reformulation-side)

Date: 2026-08-18. Coordinator: pi. Method: fresh arXiv batch (10 PDFs downloaded this
session, research/papers/), closure-DAG-gated (both levers returned "No closure hit" —
genuinely open, never ledgered), LangGraph orchestrator wave (campaign_orchestrator
StateGraph, thread wave-9).

## Context (mandatory reading)

- Campaign record: 0.673481 simple-on-line / 0.836740 distinct, UNCONDITIONAL, certified,
  terminal in-class ceiling 0.6818 (wave 7). Record chain: BGST24/BGST25 unconditional
  Montgomery pair-correlation F=1 on [0,1] → H(1.464) → (1+H)/2 redistribution. UNCONDITIONAL
  is the differentiator — conditional SDP pair-correlation papers (CGdL 1810.08843) get
  N* ≤ 1.3208N (RH) → 67.92% simple, ABOVE our 67.3481%, but conditional.
- The new batch (this session, research/papers/):
  - conrey-et-al-2508.11108-short-mollifiers-zeta.{pdf,txt} — NEW variational family: optimized
    Q (linear combinations of ζ-derivatives via calculus of variations) makes Levinson's method
    give a positive proportion for ANY mollifier length θ>0; cites Bettin–Gonek "θ=∞ ⟹ RH";
    Siegel f-function connection.
  - cgdl-1810.08843-paircorr-sdp.{pdf,txt} — also in corpus as cgdl-1810.08843... (Aug 11):
    SDP (Cohn–Elkies style) improves pair-correlation bounds; N* ≤ 1.3208 (conditional RH).
    NEVER SWEPT INTO LEDGER — genuinely open.
  - przz-1802.10521-five-twelfths-critical-line.txt — classical record source (five-twelfths).
  - bui-1410.2433-critical-zeros-three-piece-mollifier.txt — three-piece mollifier idea.
  - preobrazhenskii-1403.5786, wu-1206.3737, gs-2511.20059, gs-2603.28104,
    rezvyakova-2411.18492, garunkstis-1904.03123 — context.
- Closure-DAG queries run this session: "SDP pair-correlation test functions proportion of
  zeros on the critical line" → No closure hit. "mollifier Levinson method linear combinations
  of derivatives" → No closure hit. "theta equals infinity implies Riemann Hypothesis
  reformulation" → No closure hit. (Note: crossdomain-hunt, barrierzoo-retrotest, S1-margin,
  lit-sweep are all CLOSED and must be cited — these new levers do NOT re-derive them.)

## LEVER 9A — SDP pair-correlation → UNCONDITIONAL transfer test (record-side)

**Question**: Can the CGdL SDP-optimized test-function family (Cohn–Elkies condition
f̂(x) ≤ 0 for |x| ≥ 1, replacing bandlimited supp f̂ ⊂ [−1,1]) enter the campaign's
UNCONDITIONAL BGST24/BGST25 machinery to strictly improve the pair-correlation constant,
and hence H(1.464) → 0.836740 distinct and/or 0.673481 simple?

**Why it might work (the ONE open record-side direction)**: the record chain uses
Montgomery F=1 on [0,1] (bandlimited). CGdL relax the bandlimited class to the LP/sphere-
packing class and get strictly better conditional constants (1.3275 → 1.3208). If the
unconditional BGST transfer survives the relaxed (signed/support) condition, the record
axis moves. The campaign has the machinery: verifier-rs, cert_floor, the BGST transposes
(6B note), Rust-only.

**Why it might be a trap (honest pre-mortem)**: CGdL constants are conditional; the
unconditional transfer may force bandlimitation back (BGST24 uniformity may not survive
the relaxed f̂). If so: DOCUMENT as ABANDONED/INCONCLUSIVE with reason — no fake record.

**Deliverable**: honest verdict PROVEN-impossible / CHECKED-NUMERICALLY / INCONCLUSIVE on
the transfer question, with the exact condition that breaks (or the new constant if it
survives). Rust-only compute. Cite: wave6-briefs, records-vs-anthropic-paper-
2026-08-13.md, 6B transfer note, closure-DAG no-hit.

## LEVER 9B — short-mollifier variational Q family + θ=∞ reformulation (RH-side)

**Question**: (a) Does the new variational Q-family (Conrey–Farmer–Kwan–Lin–Turnage-
Butterbaugh 2508.11108) constitute a sufficient-condition family NOT already closed by
S1-margin / logprofile-boundary / barrierzoo? (b) Is the Bettin–Gonek "θ=∞ ⟹ RH"
reformulation a genuinely new RH-equivalence (new trap class) or does it collapse into
an existing trap (GJT-completion, potential-theory/explicit-formula)?

**Why it might matter**: a NEW reformulation of RH is not a lever by itself (tap-trap),
but a new reformulation objects to the closure map: if θ=∞ ⟹ RH and the θ→∞ Levinson
limit is algebraically explicit, it may yield a NEW trap class OR, exceptionally, a
one-way input outside all 28 closures. The variational Q optimizer is a concrete new
family — the barrier-zoo discipline requires it be tested against the RH-false worlds
before it could ever be a claim.

**Why it is likely a trap (honest pre-mortem)**: Levinson method ⟺ RH reformulations are
classical; Bettin–Gonek is probably an equivalence the campaign's "reformulations are
traps" rule already covers. The likely value is (i) registering θ=∞ as a new trap class
in the closure-DAG, (ii) a documented negative.

**Deliverable**: honest classification. If new trap class → register in closure-DAG
(with coordinator). If genuinely one-way and unconditional → propose the minimal Rust
probe (barrier-zoo first: does the Q-optimizer family satisfy deficit-2 in the DH/Epstein
RH-false worlds? almost surely yes → consistency-only). No manufactured lever.

## Honesty / method hooks (binding)

- Every claim labeled PROVEN / CHECKED NUMERICALLY / CONJECTURED / ABANDONED / INCONCLUSIVE.
- Rust-only numeric compute. No fabrication of constants, theorems, or citations.
- Deliverable-first: commit a partial note after ≤3 reads / first 5 tool calls.
- Never weaken a validator. The referee layer runs if a claim smells.
- Run the closure-DAG query before proposing any sub-lever; cite the verdict in the note.