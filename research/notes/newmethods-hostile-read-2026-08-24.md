# Hostile Read: agy-newmethods-report.md + agy-round2-report.md — 2026-08-24

Referee: diagnose (hostile, blind to prior adjudications, then cross-checked against ledger).
Ground truth sources read: `research/notes/ledger.md` (ceiling/terminal wording, wave-21, batch2,
BHB, dilation, F_T recovery), `research/notes/wave9-9A-sdp-paircorr-transfer-2026-08-18.md`
(+ its REFUTATION header), `tools/direction2_sdp/c21_ft_opt.py` / `c21_opt.py` (theta usage),
`results/ceiling-ideas.md` reference from ledger line 57.

## What the repo's certified chain actually is (the referee's frame)

- Target: N_0(T)/N(T) — proportion of SIMPLE zeros ON the critical line.
- Machinery: Bellman-coboundary window functional, interval-verified LP floor over a gap process
  with class = {mean, in-band F(alpha) (|alpha|<=1), integrality} — the "two-moment" / "in-class" class.
- Dual ceiling p_0 = 0.68182868746, attained by the 256-law adversary (r(x) = 1-x). Label:
  PROVEN, terminal. Ledger: "0.6818 proven terminal ceiling; 0.673481 is the terminal in-class
  record. Live frontier exists only OUTSIDE the class: dual-LP closing (in-class, ceiling-bounded),
  xi'-target transport (Lean 0.85838 unconditional), or conjectural regime (explicitly labeled)."
- "theta" in repo code is ONLY an optimizer variable-name for the 8-vector (p,q,a,lam):
  `unpack(theta0)` -> p,q,a,lam in c21_opt.py/c21_ft_opt.py. There is NO mollifier-length
  parameter anywhere in the certified chain. No mollifier, no Levinson moments, no zeta moments.

## Verdicts — agy-newmethods-report.md (5 proposals)

### R1 Bilinear Kloosterman-Spectral Dispersion, theta = 4/7 — CATEGORY_ERROR
Decisive: the report claims "the 0.6818 dual ceiling is proved strictly for the parameter regime
theta <= 1/2" and posits an in-class ceiling function p_0(theta) strictly increasing in theta
(0.6818 -> ~0.7324 at 4/7). The repo's ceiling is proven for OUR class {mean, in-band F,
integrality} against the 256-law gap measure — constraints that contain NO theta at all.
theta-as-mollifier-length is imported wholesale from the Levinson-Montgomery architecture, which
the repo does not run. So theta=4/7 does not evade our constraints; it evades constraints we do
not have. The 256-law is a point-process gap measure, not a "mollifier adversary"; the claim
that it "fails the extended spectral moment equations at theta=4/7" conflates two architectures.
Repo-side history: Levinson-class mollifier routes are pre-adjudicated CLOSED — wave-21 (4
candidates: duplicate/closed-by-convexity/abandoned/consistency-only), Bui-Heath-Brown "NO clean
partial unconditionalization clears p_0" and "theta<=6/11 is category error", Direction 1
(asymmetric bilinear mollifier) "blocked by RP-at-level-q (Kim-Sarnak 7/64)", 9B
levinson-variational-Q DUPLICATE-TRAP (Bettin-Gonek theta=infinity duplicates moment trap).
The proposed probe (evaluate Levinson variational integral H(alpha,4/7), floor > 0.6900?) tests
a functional the repo does not compute against a ceiling the repo does not have. The DI spectral
mechanism is real mathematics — in someone else's proof architecture.

### R2 Multi-Piece Derivative-Ensemble Mollifier Tower (Conrey-Bui-Heath-Brown lift) — ALREADY_IN_REPO (closed)
Decisive: the 3x3 (or 2x2) Gram-SDP variant is exactly the "soundstate 2x2 SDP with pinned Ingham
covariance" wave-21 candidate, already CLOSED BY CONVEXITY in the batch2 adjudication
(2026-08-18): extreme-ray collapse — matrix SDP reduces to scalar LP, C_2=0, corr absorbs into
the Levinson shift c~-0.7. The covariance input the tower would use (corr -> -sqrt(3)/2, rank-2
structure with fixed aspect ratio 1/sqrt(3)) is already pinned and already shown not to collapse
— and then shown not to matter (convexity collapse at constraint level). 9B also flagged the
whole Levinson-Variational-Q moment class as a duplicate-trap; "r' = 3/5 REFUTED twice"
(ledger line 174). Report's claim "the 256-law is an extreme ray only for the 1x1 projection"
misreads the collapse direction: it is the SDP that collapses to the scalar LP, not the adversary.

### R3 Rolle-Wronskian Derivative Interlacing — ALREADY_IN_REPO (screened NOT-A-LEVER)
Decisive: batch2 adjudication (agy-batch2-adjudication-2026-08-18.md) screened Directions 3-7 as
NOT-A-LEVER/DUPLICATE, listing "Wronskian 4th-moment barrier" explicitly. The report's other
input, "proportion of critical-line zeros of xi' >= 0.85838", is already banked in the repo as
the xi'-target transport frontier (ledger wave-7 wording: "xi'-target transport (Lean 0.85838
unconditional)"). No new object; the interlacing LP that would convert pointwise Rolle/Wronskian
signs into integral bounds is precisely the unproven conversion step (report's own objection),
and it cannot touch the in-class {mean, in-band F, integrality} ceiling without a new certificate
input, which wave-7 7C found empty.

### R4 Christoffel-Darboux Spectral Level-Repulsion Sieve — ALREADY_IN_REPO (refuted)
Decisive: batch2 adjudication: "CD gap kernel duplicate of sdp-paircorr-transfer
CLOSED-REFUTED". The wave9-9A note carries the refutation in its own header: the pair-sum
identification uses CGdL identity (8) with Montgomery's F (w(u)=4/(4+u^2)), while the
unconditional BGSTB24 Thm 1 datum is about a DIFFERENT F (w(u)=4/(4-u^2), argument rho-rho');
they agree only under RH. The CD kernel is an L^2/point-process object with no grip on the
on-line rank-trace axis (wave9-9A: "the on-line record requires positive-in-strip kernels +
rank-trace machinery, where signed SDP functions give no purchase"). The report's own biggest
objection (band |v|<=1 caps the polynomial degree N ~ (1/2)log T) is exactly the in-class
bandwidth wall; the "detects GUE rigidity" claim requires |alpha|>1 data the repo has proven
unavailable unconditionally ("no unconditional |alpha|>1 form-factor sliver", wave-7 7C).

### R5 Unitary Family Transport via Dirichlet Character Ensemble — HAND_WAVING
Decisive: the transfer step — "the resulting family proportion bound is transferred back to
zeta(s) via an orthogonal sieve comparison identity" — is the entire theorem, and the report
concedes in its own biggest objection that family-to-single-L-function transfer without GRH
"typically loses all quantitative advantage via the sieve remainder." The proposed probe
("subtract worst-case Selberg sieve transport defect delta_sieve") presupposes the existence of
the very bound that is the open problem; no such delta_sieve is stated or derivable. Firewall:
family-averaged statistics are RH-inert for the single-ray claim. Nothing here is computable in
the repo's class; the mechanism is a named aspiration, not a step.

## Verdicts — agy-round2-report.md (5 actions)

These are all in-class, same-architecture, and the report is current (its baseline
F_T >= 0.0070 => bound 0.6729663177639583, m=151 matches ledger line 2137 exactly).

### P1 F_T corrected-objective re-optimization — MECHANISM_REAL
Matches the documented recovery plan (ledger 2131-2137): joint_c21.py F_B used PAIRS21 (wrong
objective); recovery = "C21 round 2 under corrected objective; then ladder"; F_T re-cert at
eps=0.0070 already done. Re-optimizing (alpha,p,q,lambda) against joint_c21_ft is the honest
next step; import-bug claim verified in code (c21_ft_opt.py exists, c21_opt.py is the PAIRS21
sibling). Ceiling-bounded at 0.6818, but the near-term target (recover ground above Devine's
0.673399 after F_V retirement) is real and cheap to probe. Expected gain magnitude
(+2.5e-4..+4.8e-4 eps) is optimistic but falsifiable in <5 min.

### P2 Asymmetric boundary-compensated (p_i,q_i) profiling — MECHANISM_REAL
Consistent with ledger 1066 ("In-class ceiling 0.6818 requires p/q re-optimization (12-param
max-min)"). Symmetry breaking from 3 to 6 parameters is a legitimate in-class expansion; the
boundary-gap deficit argument (g_1/g_6 lose span-one repulsion under F_T) is coherent with the
F_T drop of span-one pairs. Cheap differential-evolution probe with an explicit abort threshold
(+1.5e-5). Ceiling-bounded; no new object.

### P3 Sparsified Gershgorin Hessian pruner — MECHANISM_REAL (engineering)
Verifier-throughput optimization; the convex-ball-radius +25-35% figure is unverified assertion
but the sparsity premise (F_T drops 6 span-one pair terms => fewer cross-derivative couplings)
is structurally true, and the probe (node-count comparison on a real depth-18 subtree) is
well-defined. Gains are indirect (more ladder rungs per hour), not new mathematics. Run the
probe before touching the verifier.

### P4 Checkpointed frontier resumption with high-precision Arb — MECHANISM_REAL (engineering)
Standard near-miss salvage; honest failure mode named (terminal leaf may be a true mathematical
wall). Small gains; zero risk. Cheap.

### P5 Closed-form (lambda, m) envelope co-tuning — ALREADY_IN_REPO (saturated)
Ledger 1042: lambda-dilation record raise already executed 2026-08-18 (eps 0.00698 -> 0.00703,
m=152, 200-bit bound 0.6735633) with the verdict "The lambda-dilation class is saturated near
its local optimum, far below the proven-terminal in-class ceiling 0.6818." The report's own
probe accepts <5e-6 gain as "secondary polish" — i.e., it self-classifies as marginal. No new
work until P1/P2 exhaust.

## Bottom line

- newmethods R1 is a category error (imports a Levinson theta-parameterized ceiling our chain
  does not have; 0.6818 was proven for OUR constraints, which contain no theta). R2-R4 are
  already-in-repo closed/screened routes. R5 is hand-waving at its only load-bearing step.
  NONE of the five touches the certified on-line class; NONE justifies a probe, let alone the
  proposed Rust tools/probes spend.
- round2 P1/P2 are real in-class work already implied by the repo's own recovery plan; P3/P4
  are cheap engineering; P5 is done/saturated. Fund P1 then P2; skip P3-P5 unless probes move.
- No proposal offers any new certificate input outside {mean, in-band F, integrality}, so the
  terminal ceiling 0.68182868746 and record 0.673481 (Lean-proven in-class) are untouched by
  everything in both reports. Firewall respected by none of the five newmethods proposals that
  claim to reach zeta itself (all are proportion-on-line statements, RH-inert by the firewall,
  but all are also architecturally disjoint from the repo).
