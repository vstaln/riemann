# WAVE 7 — RECORD-SECURING (after wave-6 validation of 0.673481)

Context: wave 6 (5 hostile blind referees + coordinator) validated the certified record
0.6734808616745137 (simple-on-line) / 0.8367404308372568 (distinct) as an UNCONDITIONAL
liminf bound (no RH/PCC/RMT). Remaining caveats are documentation/formalization/machine
re-runs, not math. Three disjoint levers:

- **(7A) Explicit certificate documentation (builder, high value):** write down the record's
  r (piecewise-linear on knots j/256, r(1)=0) with c₀ = H(1.464) − τ = 0.6694520747005951,
  and verify Σ_{j=1}^{256}(j/256²)·r(j/256) = 0.0040287869739185 exactly → 6E's verdict (i)
  becomes certified. Deliverable: research/notes/wave7-certificate-documented-2026-08-17.md
  + a self-contained Rust probe that reconstructs r from the tawan mechanism and evaluates
  the knot-sum. Read: wave6-synthesis, JOINT_WINDOW_PROOF.md, verify_coboundary_floor.py.

- **(7B) Second-machine interval re-run (builder):** re-run the full 1M-node Arb interval
  certificate (verify_floor at α=1.464, eps=0.0062, grid=4000) in an environment that is NOT
  the machine that produced the original (e.g., fresh uv venv, different Arb/mpmath build,
  or the Rust-flint route) and confirm verified=True + node count ≈ 1,096,556 (3 runs).
  Deliverable: research/notes/wave7-secondmachine-interval-2026-08-17.md. This closes 6C's
  caveat (1M-node tree not re-run elsewhere).

- **(7C) New-object frontier scan (adventurer, research):** the 0.6818 class ceiling is
  Lean-PROVEN; every in-class lever (m₃-read, off-centre, r′) is closed (waves 4–5). The
  ONLY possible ceiling breakers are NEW OBJECTS/INPUTS: (a) a PROVEN form-factor estimate
  for |α|>1 (literature: everything CONJECTURED — RMT, Hardy–Littlewood; BGSTB24
  T^(−2α)logT atom; GLSS25 100%-on-line-if-PCC-full); (b) a proven lower bound on the simple
  fraction p₁ of real ζ above 0.6818 (Bui–Heath-Brown 19/27 is RH-conditional; Farmer–Gonek–
  Lee ξ′ route is a different function); (c) a genuinely new certificate input outside
  {mean, F on [0,1], integrality} that is PROVEN for ζ. Scan the repo's verified-literature
  corpus (research/papers/, research/external-results/) for ANY such input; report each
  candidate's exact statement + citation + unconditional status. Deliverable:
  research/notes/wave7-newobject-scan-2026-08-17.md. Verdict: frontier open where, or closed
  everywhere (all three classes empty) — which would make 0.6818 the terminal ceiling and
  0.673481 the terminal in-class record.
