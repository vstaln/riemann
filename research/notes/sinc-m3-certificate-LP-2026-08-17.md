# Sinc-kernel marked-m₃ certificate LP — the m₃ ≥ m₂² lever in the sinc convention

**Date:** 2026-08-17. **Agent:** builder (sinc-m3-cert).
**Task:** does a sinc-kernel certificate that READS marked-windowed m₃ ≥ m₂² (torus floor
E[m₂]=2.480620) have an in-class ceiling strictly above the PROVEN wall 0.6818?
**Crate:** `tools/sinc_m3_cert/` (Rust, minilp). Zero Python.
**Status:** INCONCLUSIVE (blocker: binary not yet run — minilp 0.2.2 API mismatch in the shadow-price block). Crate complete otherwise; exact scan + calibration + control code is written and compiles except the minilp block. **No LP optimum printed → none reported.** Hand-derivation below is labeled CONJECTURED, NOT a result.

---

## 1. The model (exact diagram computation, no simulation)

**Sinc² window kernel** (bandwidth b = 128 = the λ=1/2 convention, matching notes' B=129
blocks): on the 256-lattice x_i = i/256,

    K(x) = sinc(π·b·x)²,   K̂(m) = (1 − |m|/b)₊  (triangular spectrum, K̂ ≥ 0 ⇒ K positive-definite)

**Marked law** (certificate convention, reproduces the PROVEN pins): marks m ∈ {1,2},
P(m=2) = (1−p₁)/(1+p₁), P(m=1) = 2p₁/(1+p₁) ⇒ E[m] = 2/(1+p₁),
D = E[m³]/E[m] = 4 − 3p₁ (exact, matches the proven pin).
**Pair rows** (PROVEN for the real zeros on [0,1]): E|μ̂(k)|² = k (k=1..255), E|μ̂(0)|² = E[m]².
**Theorem** (PROVEN, marked-moment-inequality): per-config m₃ ≥ m₂² ⇒ S₃(law) ≥ (E[m₂])².
**Diagram decomposition**: m₂ = D₂ + u (pair part u pinned by rows);
S₃ = D + P₃ + T, P₃ = two-equal pinned part, T = connected part free,
T ≥ max(0, (E[m₂])² − D − P₃)  (theorem + T ≥ 0).
⇒ **S₃ floor = max(D + P₃, (E[m₂])²)** — the certificate reads S₃ ∈ [5−ε, 5+ε], feasible iff
floor(p₁) ∈ [5−ε, 5+ε]. min-p₁ over the admissible class ⇒ κ = p₁ + |E(1)|, |E(1)| = 1/(6·256²).

**Calibration targets (PROVEN, must reproduce):** torus kernel E[m₂] = 2.480620 p₁-independent;
D + 3u = 5.4419; torus floor = max(5.4419, 6.1535) = 6.1535 > 5.44 ⇒ torus m₃-read infeasible
(margin +0.71, matches L4 + marked-moment notes).

## 2. LP (minilp)

minimize p₁  s.t.
    D(p₁) + P₃(p₁) + T ≥ 5 − ε
    D(p₁) + P₃(p₁) + T ≤ 5 + ε
    (E[m₂](p₁))² − D(p₁) − P₃(p₁) ≤ T      (theorem row)
    T ≥ 0, 0 ≤ p₁ ≤ 1
coeffs from exact rows (evaluated per-p₁; minilp on the affine-linearized system for shadow prices;
exact min-p₁ by scan+bisection on floor(p₁) ∈ [5−ε,5+ε]).

## 3. RH-false control (mandatory)

Reads (m₂, m₃, pair rows) depend ONLY on (γ_k, marks) — the real parts σ_k never enter the Gram.
Fake Weil world B: same γ's + same marks, fraction f_on of zeros declared off-line (σ=0.7).
Reads IDENTICAL to world A ⇒ LP certifies the same κ for B. Report κ vs f_on: if κ ≥ 2/3 while
f_on < 2/3, the mechanism proves too much for the *on-line* claim (κ is a simple-fraction
ceiling; on-line needs an extra hypothesis). Davenport–Heilbronn: pair rows violate flat F ⇒
certificate inapplicable (labeled CONJECTURED, literature).

## 3.5 Remaining fix (one edit, then `cargo build --release --target x86_64-unknown-linux-musl` + run)

The minilp block in `src/main.rs` uses the 0.2.0-era API; the fetched minilp is 0.2.2 whose API is:
`add_var(obj_coeff, (min, max)) -> Variable`, `add_constraint(&[(var, coeff)], ComparisonOp::Ge|Le, rhs)`, `sol.var_value(var) -> &f64` (deref). Replace the `add_variable`/`add_constraint(lower,upper)`/`set_column`/`variable_value` calls accordingly (exact mapping: vp = add_var(1.0,(0.0,1.0)); vt = add_var(0.0,(0.0,INF)); rows via `&[(vp,d_dp),(vt,1.0)]`; read p1opt = *sol.var_value(vp)).

## 4. Results (FILL FROM BINARY)

| quantity | value | vs |
|---|---|---|
| sinc E[m₂](p₁=1) | [ ] | real-zeros sinc m₂²=4.9256 |
| sinc floor(p₁=1) = max(D+P₃, m₂²) | [ ] | read window [4.56, 5.44] |
| min-p₁ over admissible class (ε=0.44) | [ ] | p₀ = 0.6818287 |
| κ* = min-p₁ + |E(1)| | [ ] | **0.6818** |
| binding constraint | [ ] | theorem row vs read row |
| control: κ* vs f_on | [ ] | proves-too-much? |

## 4.5 Hand-derived prediction (CONJECTURED, NOT printed — for the next run to confirm/refute)

With the calibration c chosen so m2(p1=1)=2.22 (real-zeros sinc m2²=4.9256): m2(p1) = 2.729/(1+p1) + 0.427(1+p1) (decreasing in p1). Theorem floor = max(D+P3, m2²); D+P3(p1) ≈ 2.07–2.22 (small vs m2²), so the THEOREM ROW binds. Crossing m2² = 5.44 (ε=0.44) gives min-p1 ≈ **0.699 > p₀ = 0.6818287** ⇒ κ* ≈ 0.699 > 0.6818 — the lever would FUND the simple-fraction ceiling. Torus floor (cited) = 6.1535 > 5.44 ⇒ infeasible (L4 re-derived). Control: reads are σ-blind ⇒ fake-Weil world (f_on=0.60) certified at same κ* ⇒ κ* is a SIMPLE-FRACTION ceiling; on-line claim needs RH-type hypothesis. All of this is hand-calc; the binary must confirm before any label above CONJECTURED.

## 5. Verdict (FILL)

- [ ] If κ* > 0.6818: lever FUNDED (CONJECTURED — family/rows input) — state the missing theorem.
- [ ] If κ* ≤ 0.6818: NEGATIVE RESULT with numbers — the m₃ ≥ m₂² sinc read does not break the wall.
- [ ] Control verdict: does the mechanism prove too much? Explicit statement.

## 6. Files
- Crate: `tools/sinc_m3_cert/` (Cargo.toml + src/main.rs).
- This note. Command: [FILL].

## 6. COORDINATOR POSTSCRIPT — binary ran (2026-08-17, main loop)

Fixed the minilp 0.2.2 API mismatch (§3.5 mapping: add_var/add_constraint/var_value), built
musl, ran. Full output at end of this section.

**WHAT THE BINARY PRINTS (CHECKED NUMERICALLY — every number below is printed by
tools/sinc_m3_cert, command: `./tools/sinc_m3_cert/target/x86_64-unknown-linux-musl/release/sinc_m3_cert`):**
- Scan (eps=0.44, window [4.56,5.44], sinc² kernel B=128 N=256): min-p1 = **0.748807**,
  floor = 5.440000 (binding at the read TOP 5+eps), kappa = **0.748809** — EXCEEDS 0.6818.
- Sensitivity: eps=0.20 → κ=0.8337; eps=0.10 → κ=0.8670; eps=0.05 → κ=0.8832.
- Torus convention: E[m₂]=2.480620 (PROVEN), theorem floor = max(5.4419, 2.480620²) = 6.1535
  > 5.44 → **INFEASIBLE read** (margin +0.71; matches L4's negative).
- RH-false control: Gram σ-blind → reads(B)==reads(A); LP certifies κ*=0.748809 for BOTH
  worlds; true on-line fraction of B = 0.60 < κ* → **PROVES TOO MUCH for the on-line claim**:
  κ* is a SIMPLE-FRACTION ceiling; the on-line interpretation needs the extra hypothesis
  (off-line zeros all non-simple — an RH-type hypothesis).
- Calibration sensitivity: m2(1)=2.00 → κ=0.4658; 2.11 → 0.6078; 2.22 → 0.7488 (>0.6818);
  2.33 → 0.8698; 2.44 → EMPTY. Real-zeros sinc m₂²=4.9256 → m₂(1)=2.2198 ≈ 2.22, so the
  calibrated branch IS the real-zeros branch.
- **minilp shadow-price block: `Infeasible`** — the linearized LP at the optimum contradicts
  the nonlinear scan. The linearization of the max-floor at the binding top is invalid at the
  boundary (floor(p1*) = 5.44 exactly; tangent rows are inconsistent). The scan/bisection is
  the actual optimum; the LP block is broken and MUST NOT be used for shadow prices.

**COORDINATOR VERDICT: NOT YET A RECORD.** The scan-based κ*≈0.7488 is a genuine numerical
result of the sinc-kernel marked-law model WITH the real-zeros calibration m₂(1)=2.22, but
(a) the minilp cross-check failed (LP encoding inconsistent at the boundary), (b) the RH-false
control shows the certificate is σ-blind and κ* is a simple-fraction ceiling, not an on-line
proportion, and (c) feasibility is calibration-fragile (m₂(1) ∈ [2.17, 2.44) needed; the PROVEN
torus m₂ gives INFEASIBLE). This is exactly the case for HOSTILE REFEREES before the claim can
be labeled PROVEN: (i) is the marked-law model (moments, D=4−3p₁, P3, m₂, floor=max(D+P3,m₂²))
correct and complete for the sinc kernel? (ii) is the calibration m₂(1)=2.22 the real-zeros
value in THIS normalization (vs the torus 2.480620 — which convention does the PROVEN
m₃≥m₂² theorem bind in)? (iii) does the σ-blindness refute the on-line reading, or only the
proportion-on-the-line reading (firewall)? Status: CONJECTURED (binary run, referees pending).

### Binary output (verbatim)
```
=== sinc-m3 certificate LP (sinc^2 kernel, B=128, N=256) ===
K̂(0) = 0.005856, Σ_m K̂(m) = 1.000000 (should be K(0)=1)
(K̂*K̂)(0) = 0.004232,  C = Σ_{k>=1}(K̂*K̂)(k)k = 127.458332
calibration c = 0.000035  (m2(p1=1) = 2.220000, m2^2 = 4.928400 vs real-zeros 4.9256)

=== p1 scan (eps = 0.44, window [4.56, 5.44]) ===
  p1        D+P3      (E[m2])^2   floor     in-window?
  0.5000   6.0894    5.2792    6.0894   no
  0.6000   5.8294    5.1263    5.8294   no
  0.6818   5.6184    5.0385    5.6184   no
  0.7000   5.5707    5.0230    5.5707   no
  0.7500   5.4367    4.9869    5.4367   YES
  0.8000   5.2975    4.9599    5.2975   YES
  0.9000   4.9973    4.9301    4.9973   YES
  0.9500   4.8338    4.9260    4.9260   YES
  1.0000   4.6600    4.9284    4.9284   YES

=== LP: min p1 over admissible class ===
  eps = 0.44: min-p1 = 0.748807, floor = 5.440000, kappa = 0.748809  [EXCEEDS 0.6818]
  eps = 0.20: min-p1 = 0.833659, floor = 5.200000, kappa = 0.833662  [EXCEEDS 0.6818]
  eps = 0.10: min-p1 = 0.866997, floor = 5.100000, kappa = 0.867000  [EXCEEDS 0.6818]
  eps = 0.05: min-p1 = 0.883216, floor = 5.050000, kappa = 0.883219  [EXCEEDS 0.6818]

=== minilp (linearized at optimum, eps=0.44) ===
  minilp solve failed: Infeasible

=== torus-convention floor (PROVEN, cited) ===
  E[m2](torus) = 2.48062 (p1-independent, PROVEN), theorem floor = 6.1535 vs read 5.44 -> INFEASIBLE (margin +0.71, matches L4)

=== RH-false control (fake Weil polynomial world) ===
  World A (all zeros on line): reads m2,m3,pair-rows from flat-row marked law
  World B (fake Weil): same imaginary parts + same marks, fraction f_on = 0.40 of zeros off the line
  Gram G_ij = sinc^2(pi*B*(x_i-x_j)) depends ONLY on x_i (gamma) -> reads(B) == reads(A) by construction (sigma-blind)
  LP certifies kappa* = 0.748809 for BOTH worlds
  true on-line fraction of B = 0.60  <  kappa* = 0.7488  =>  PROVES TOO MUCH for the on-line claim: kappa* is a SIMPLE-FRACTION ceiling; the on-line claim needs the extra hypothesis that off-line zeros are all non-simple (RH-type)
  (Davenport-Heilbronn: pair rows violate flat F => certificate inapplicable; CONJECTURED, literature)

=== calibration sensitivity (m2(p1=1) target) ===
  m2(1) = 2.00: c = 0.00003, min-p1 = 0.46582, kappa = 0.46583 <= 0.6818
  m2(1) = 2.11: c = 0.00003, min-p1 = 0.60782, kappa = 0.60782 <= 0.6818
  m2(1) = 2.22: c = 0.00003, min-p1 = 0.74881, kappa = 0.74881 > 0.6818
  m2(1) = 2.33: c = 0.00004, min-p1 = 0.86983, kappa = 0.86984 > 0.6818
  m2(1) = 2.44: EMPTY
```
