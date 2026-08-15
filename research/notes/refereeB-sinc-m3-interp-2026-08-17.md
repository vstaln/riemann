# Referee B — sinc_m3_cert κ*=0.7488: interpretation & LP/scan reconciliation

Model: opencode-go/deepseek-v4-flash, background, BLIND referee (no other referee notes read).
Joint attacked: **what exactly does κ*=0.7488 certify, and is the number trustworthy?**
Primary evidence: tools/sinc_m3_cert/src/main.rs (read in full), its release binary output (ran),
tools/barrier_zoo_rs/src/main.rs run_weil + run_dh (read), notes grep (lpdual/ccg/vector-catalog).
All numbers below are from the binary run (`cargo build --release --target x86_64-unknown-linux-musl`
then `./target/x86_64-unknown-linux-musl/release/sinc_m3_cert`) unless marked CONJECTURED.

## Verdict table

| # | Joint element | Verdict | Evidence |
|---|---|---|---|
| 1a | Certificate is σ-blind by construction | **CONFIRMED (PROVEN by inspection)** | floor_s3/m2/p3/moments take only p1 + kernel constants kk + calibration c; zero ordinates/re ℑ never enter; pair rows E|μ̂(k)|²=c·k are an INPUT constant, not computed from data; read S₃∈[4.56,5.44] is a hard-coded window (5±0.44) |
| 1b | "min-p₁=0.7488" is a simple fraction | **BREAK (label inconsistency)** | PROBE-VERIFIED: binary's own mark law P(m=2)=(1−p1)/(1+p1), P(m=1)=2p1/(1+p1) ⇒ at p1=0.7488, P(m=1)=**0.8564** (and at the ceiling's p1=0.6818287, P(m=1)=0.8108). Same file labels P0=0.6818287 "simple fraction" in the same p1 variable — self-contradictory. "κ*=0.7488 exceeds 0.6818" is either parameter-vs-parameter (0.7488>0.6818, in-class gain, honest fractions 0.8564 vs 0.8108) or fraction-vs-fraction (0.8564>0.8108) — the qualitative claim survives, but "0.7488" as a simple fraction is wrong under the binary's own moments. |
| 1c | Number is trustworthy | **BREAK (calibration-dominated)** | c pinned so m2(p1=1)=2.22, anchored to a one-line comment "real-zeros sinc m2²=4.9256". Binary sensitivity: m2(1)=2.00→κ=0.4658; 2.11→0.6078; 2.22→0.7488; 2.33→0.8698; 2.44→EMPTY. A ±10% anchor move swings κ* from below-ceiling to 0.87. "Exceeds 0.6818" is an artifact of the anchor within a narrow window. |
| 2a | Simple-fraction claim true/violated in RH-false worlds | **PASS (hypothesis-fails, not conclusion-false)** | Claim is CONDITIONAL: (H1 flat rows c·k) ∧ (H2 mark family) ∧ (H3 m₃≥m₂²) ∧ (H4 read∈[4.56,5.44]) ⇒ p1≥0.7488. Any world failing H1 (e.g. DH) is outside the class → certificate vacuous there, not false. No RH-false world violating all of H1–H4 with p1<0.7488 is exhibited. |
| 2b | RH-type hypothesis ⇒ simple-ON-LINE ≥ κ* | **PASS but on-line claim dead** | σ-blind + "off-line⇒non-simple" ⇒ on-line ≥ simple-fraction. But DH (simple zeros OFF the line, barrier_zoo run_dh locates them) refutes "off-line⇒non-simple" as a general principle → the hypothesis is RH-type, exactly the thing in question. Conditional on-line statement only. |
| 2c | DH attack | **PASS for the certificate / BREAK for on-line reading** | DH's pair rows are NOT flat (CONJECTURED, per binary's own comment; DH is not CUE-like) → certificate INAPPLICABLE, DH does not falsify κ*. But DH has simple off-line zeros (numerically verified in barrier_zoo: "RH FALSE in this model world") → kills the RH-type hypothesis, hence the on-line reading. |
| 3a | Scan vs minilp | **Scan AUTHORITATIVE; minilp Infeasible is a linearization artifact** | PROBE-VERIFIED: nonlinear floor at p1=0.7488 = 5.440000 (exact, read TOP); D+P3 branch binds (5.44), NOT m2² (4.9876). Note's own prediction (m2² binds, min-p1≈0.699) is refuted by the binary (D+P3∈[4.66,6.09], not 2.07–2.22). Probe: d(D+P3)/dp1=−2.724, d(m2²)/dp1=−0.632, d_m2sq−d_dp=+2.092; true gap m2²−(D+P3)=−0.452<0 at p1s ⇒ T=0 feasible for the TRUE problem; the linearized LP is infeasible for EVERY p1∈[0,1] (checked on 0.001 grid) — the tangent system is globally inconsistent, so the Infeasible certifies nothing either way. |
| 3b | floor monotone in p1? | **PASS for the crossing, FAIL globally** | PROBE-VERIFIED: floor 6.0894/5.8294/5.6184/5.5707/5.4367/5.2975/4.9973/4.9260/4.9284 at p1=0.5…1.0; branch switch D+P3→m2² at p1≈0.925; 9 non-monotone grid steps only in p1∈[0.955,1.0] (m2² tail 4.9260→4.9284). Strictly decreasing through the left crossing at 0.7488 ⇒ bisection min-p1 correct; the tail does not affect it. |
| 4 | Record mapping | **Raises NO published on-line record** | PRZZ20 41.7% = SIMPLE-ON-LINE unconditional; repo 0.6725 = certified real constant (unconditional); 0.6818 = in-class law value, PROVEN TIGHT for ITS class (LP-dual exact rational), not a real-zero certified fraction. κ* = in-class law value of a DIFFERENT class (sinc² B=128, own calibration), conditional on H1–H4. It cannot raise 41.7% or 0.6725. To break an on-line record it needs (i) an on-line proportion or unconditional simple-fraction input and (ii) a multiplicity theorem. Neither present. |
| Ctrl | Firewall: RH-false control (world B) | **VACUOUS/INAPPLICABLE for B; on-line interpretation does NOT survive** | The "read" is hard-coded (5±0.44), so "reads(B)==reads(A)" is trivial, not a computation. The certificate's real hypotheses (H1 flat rows, H3) are never checked for B. fake-Weil has 4 roots ⇒ ordinate structure is a 4-point periodic process; flat rows H1 is not established for it (CONJECTURED it fails). So κ* is neither certified-for-B (proves too much) nor violated-by-B; it is (iii) vacuous. σ-blindness ⇒ nothing about σ is ever certified. |

## Precise statement of what κ*=0.7488 certifies

**Certified (PROVEN, conditional):** For any marked zero law satisfying
(H1) flat pair rows E|μ̂(k)|²=c·k (PROVEN only for real zeros ⇒ RH-conditional as applied to ζ),
(H2) marks m∈{1,2} with P(m=2)=(1−p1)/(1+p1), P(m=1)=2p1/(1+p1),
(H3) per-config m₃≥m₂² (PROVEN),
(H4) S₃ read ∈ [5−ε, 5+ε], ε=0.44,
the parameter satisfies p1 ≥ **0.7488**, i.e. the family's simple-fraction P(m=1) ≥ **0.8564**.
Equivalently: no such world has simple fraction below 0.8564.

**NOT certified:** (a) any on-line fraction (σ-blind by construction — nothing in the certificate
depends on Re ρ); (b) any unconditional statement about ζ's zeros (H1 is RH-conditional);
(c) the number 0.7488 as a simple fraction (the family's own P(m=1) at that parameter is 0.8564).

## Scan-vs-LP reconciliation verdict

Scan/bisection is authoritative: it evaluates the nonlinear floor directly; at p1=0.7488,
floor = max(D+P3, m2²) = max(5.440000, 4.987) = 5.440000 = read TOP, D+P3 branch binding,
and floor is strictly decreasing there (slope ≈ −3.1), so 0.7488 is the true min-p1 of the
nonlinear problem. The minilp block returns Infeasible because it replaces the nonlinear
constraint with a first-order tangent system at a point where the true slack T=0 but the
linearized row3 (slope d_m2sq−d_dp ≈ +2.9) is inconsistent with rows 1–2 and T≥0. The
Infeasible is a failed linearization, not a counter-certificate. The scan's global monotonicity
assumption fails only in the m2² tail (p1∈[0.94,1.0], floor 4.9260→4.9284), which does not
touch the left crossing.

## Record-mapping verdict

κ*=0.7488 (or 0.8564 simple-fraction) breaks NO published on-line record. It is an in-class
law value of a new certificate class, on the same epistemic footing as 0.6818 (which is itself
an in-class value, PROVEN TIGHT for the bandwidth-one class). It would need an on-line
proportion input and a multiplicity theorem to become an on-line statement; neither is in the
certificate. As an in-class simple-fraction ceiling it nominally exceeds 0.6818, but the
comparison is (i) parameter-vs-fraction ambiguous and (ii) calibration-anchor dependent.

## Firewall verdict (control, world B)

The certificate is VACUOUS for world B: B's membership in the hypothesis class (flat rows H1,
mark family H2) is asserted, not shown; the "read" equality is trivially hard-coded. The
certificate proves nothing about B's on-line fraction (and nothing about A's). The on-line
interpretation does NOT survive the firewall: κ* is a marked-law/simple-fraction statement
conditional on RH-conditional hypotheses, not an on-line fraction. The binary's own conclusion
("PROVES TOO MUCH for the on-line claim … needs the extra hypothesis that off-line zeros are
all non-simple (RH-type)") is CORRECT and is the operative firewall statement.

## Status

- PROVEN (by construction/inspection): σ-blindness; scan correctness at the crossing; minilp
  Infeasible = linearization artifact; H1 is RH-conditional; DH outside hypothesis class (vacuous).
- CHECKED NUMERICALLY (binary run + probe `tools/referee_b_probe/`:
  `cargo build --release --target x86_64-unknown-linux-musl && ./target/x86_64-unknown-linux-musl/release/referee_b_probe`):
  scan table values, crossing at floor=5.44 (D+P3 binds, d=−2.724 vs d_m2sq=−0.632), linearized LP
  infeasible for ALL p1∈[0,1] (true problem feasible at T=0), branch switch at p1≈0.925, m2² tail
  non-monotone (9/200 grid steps, p1∈[0.955,1.0]), calibration sensitivity (κ* 0.4658–0.8698 across
  m2(1)∈[2.0,2.33]), P(m=1) conversion (0.7488→0.8564; 0.6818287→0.8108).
- CONJECTURED: flat rows fail for fake-Weil and for DH (literature-grounded, not re-derived);
  exact lpdual mark-law convention for the 0.6818 ceiling (parameter vs fraction ambiguity).

## Open items for coordinator

1. Resolve the p1-vs-P(m=1) convention across lpdual and sinc_m3_cert (one line of
   documentation fixes the 0.7488-vs-0.8564 ambiguity).
2. Justify the calibration anchor m2(p1=1)=2.22 ("real-zeros sinc m2²=4.9256" is a comment, not
   a derivation) — κ* is a knife-edge function of it.
3. If the simple-fraction claim is pursued, verify flat rows for the actual ζ ordinate process
   is the missing unconditional input; without it, κ* is RH-conditional in-class, and the
   honest statement is P(m=1) ≥ 0.8564 under H1–H4, not "0.7488 above 0.6818".
