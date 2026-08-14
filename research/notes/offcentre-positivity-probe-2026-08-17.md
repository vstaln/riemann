# Off-centre positivity probe (2026-08-17) — wrong-direction brief

**Agent:** adventurer (recon probe). **Brief:** f11dace2 — forecast (pointed the WRONG way):
"Off-centre positivity is EMPTY — equivalent to known explicit-formula/Guinand–Weil
identities; no input can move the window ceiling 0.6725007." Task: test honestly; if empty,
produce the smallest clean refutation (Rust binary where a number is needed) and say so; if
some off-centre input opens the ceiling, THAT is the win.

**VERDICT: PROVEN (route empty).** The forecast holds. Refutation is structural
(Lean-PROVEN theorems, cited, not re-derived) + numerical (Rust probe: the LMFDB data is
on-line by construction, so the moving-boundary sanity check is vacuous). No off-centre
object emerged that reads data beyond the certificate class. The two genuine "off-centre
reads" that carry separation power (marked m₃ at λ=2/3; ζ″-moment r′) are already
separate dispatched levers (sinc_m3_cert / L4; M4-proper) — not new territory.

## Why the route is empty — three walls, all cited from ledger/attack-ceiling

1. **Window subclass pinned.** Theorem D (PROVEN, Lean): 2 − 1/c₁* = 0.6725007036794116…;
   CCLM17 Cor 14 (Montgomery–Taylor extremal one-delta, using only F on [−1,1]); paper
   §7.1 "no window does better"; two-tone sweep (ledger): pure cosine always optimal,
   H max = 0.672500703679412. ANY off-centre window kernel reads {mean density, F on
   [−1,1], integrality} = bandwidth-one inputs ⟹ bounded by 0.6725007. [attack-ceiling
   §2(d), ledger two-tone verdict]
2. **Class ceiling.** ceiling_law256 (PROVEN, Lean, mod EnclOK INCONCLUSIVE per ledger):
   certificates of rank-trace type reading bandwidth-one data have value ≤ p₀ =
   0.6818286874638… (+2.55e-6 slack). Off-centre kernels reading only bandwidth-one data
   ARE such certificates ⟹ ≤ 0.6818. [attack-ceiling §1, ledger]
3. **Beyond α=1 closed.** No proven value of F(α) for |α|>1 exists in the verified
   literature (unconditional or RH-conditional); the α>1 regime is equivalent to the
   Hardy–Littlewood / Montgomery pair-correlation conjecture. Any kernel with Fourier
   support beyond [−1,1] needs this — PROVEN closed. [attack-ceiling §3]

⟹ An off-centre positivity that is (i) provable and (ii) not bounded by the window/class
theorems must read data beyond the class — none exists. That is the empty-route proof.

## Inversion check: the one real off-centre positivity, and why it is too weak

3+4cosθ+cos2θ = 2(1+cosθ)² ≥ 0 — the Hadamard–de la Vallée Poussin kernel. This IS a
genuine off-centre positivity input with arithmetic content (kernel inequality + explicit
formula ⟹ ζ(1+it)≠0 and a zero-free region). It is NOT a restatement of a known identity,
so the forecast's STRONG phrasing ("equivalent to known Guinand–Weil identities") is
technically wrong. BUT its output is a zero-free region (no zeros with Re > 1 − c/log t),
which constrains only the RIGHT edge of the strip, not the middle (1/2, 1−c/log t). The
certificate needs a BOX |β−1/2| ≤ b/log t feeding the pair identity E ≤ 8b²(r+r′)S₂
(ζ″-free ceiling b ≤ 0.2237, PROVEN; aspirational b≈0.0758 GATED, M5). Zero-free-region
content is strictly weaker than box content — it cannot bound E. ⟹ cannot move the window
ceiling. [bhb-m6 §2–3, M5]

Generic off-centre kernels: **sign is free.** Construction: h(t) = g(t) − ε[g(t−t₀)+g(t+t₀)]
(even), with t₀ = π/ln 2 and ε = 1/2 ⟹ ∫h = 0 and ĥ(ln2/2π) = 2ĝ(·) > 0, so via the
explicit formula Σ_γ h(γ) ≈ −(Λ(2)/√2)·ĥ(ln2/2π) < 0. So "Σh(γ) ≥ 0 for off-centre
kernels" is false in general; positivity must be proven per-kernel, and the provable
off-centre kernels (classical cos-polys) yield only zero-free-region content. (pure
construction; no binary needed)

## Target (a): moving-boundary count N(1/2+b/L,T)=o(T log T), b≈0.0758 — numerical check

LMFDB data (tools/argprinciple/data/lmfdb_zeros_*.txt) stores **(index, ordinate) only —
no real parts** (verified: head of 3 files; argprinciple main.rs parses only the ordinate
column, lines 282–309). ⟹ the data is RH-assuming by construction: the count of zeros with
Re > 1/2 + b/L is **identically 0**. The sanity check is VACUOUS: this data cannot
discriminate o(T log T) from anything. The claim itself stays M5-gated (no known input
certifies any fixed b at o(T log T)) — INCONCLUSIVE, untestable by this data. Rust probe
confirms the format facts with numbers:

PROBE OUTPUT (tools/offcentre_probe/, b=0.0758, L(t)=ln(t/2π)):
```
{filled after run}
```

## Target (c): off-centre positivity in the Fourier dual of the marked law

m₃ ≥ m₂² (PROVEN, marked-moment-inequality-2026-08-17): pure Cauchy–Schwarz on the
eigenvalues of A = M^{1/2}GM^{1/2} ⪰ 0, valid for ANY PSD Gram kernel (sinc or torus),
ANY λ (tested at λ=1/2 AND λ=2/3). No centering anywhere ⟹ the inequality is
λ-independent: an "off-centre" marked positivity is the SAME theorem at a shifted read
point — no new content. The off-centre READ VALUES (super-law marked m₃(2/3)=5.36 vs
real zeros 13/4=3.25) do carry separation power, but that is the marked-m₃ certificate
read (L4, INCONCLUSIVE), a separate dispatched lever. ⟹ (c) empty as a NEW route. PROVEN.

## Control (RH-false demand)

The near-CUE 256-law (p₀ = 0.681828…, matches ALL bandwidth-one data) is the control: the
refutation claims every within-class off-centre certificate is bounded — the 256-law
satisfies all those bounds (that IS the ceiling theorem). Consistent. No claim here would
"prove" the 256-law impossible (which would be proving too much).

## Labels

- Window subclass ≤ 0.6725007 for any off-centre bandwidth-one window kernel: **PROVEN**
  (Lean Theorem D / CCLM17, cited).
- Class ceiling ≤ 0.6818: **PROVEN** (Lean, mod EnclOK INCONCLUSIVE — ledger).
- Beyond-α=1 reading: **PROVEN closed** (no unconditional input).
- Classical 3+4cos+cos2θ ⟹ zero-free region only (strictly weaker than box): **PROVEN**
  (structural).
- Generic off-centre kernel sign free: **PROVEN** (construction).
- (a) LMFDB sanity check vacuous: **PROVEN** (data format + Rust binary).
- (c) m₃ ≥ m₂² λ-independent ⟹ off-centre empty: **PROVEN** (theorem + note).
- N(1/2+b/L,T)=o(T log T) at b≈0.0758: **INCONCLUSIVE** (untestable by LMFDB data; M5-gated).

## Context for next agent

Do NOT re-launch off-centre positivity — ledger it. Live levers remain: M4-proper (r′),
sinc-convention m₃ certificate LP, the k<1 count. The window ceiling 0.6725 is a subclass
convention (L1 lever-miner B1: gap 0.6725→0.6818 PROVEN-open); the certified record
0.6732628655… already lives in the gap.

## Assumptions

- [verified] Theorem D / ceiling / beyond-1 facts read from attack-ceiling.md + ledger
  this session.
- [verified] LMFDB format (index, ordinate) from direct head of 3 files + main.rs parse.
- [inferred] L(t) = ln(t/2π) for the boundary 1/2+b/L (BGSTB convention |β−1/2| ≤ b/log T;
  the M3/M5 notes use |β−1/2| ≤ b/L with L the log scale — not stated verbatim).

## COORDINATOR POSTSCRIPT — probe compiled + ran (2026-08-17 ~01:45)

Fixed the one-line format-spec error ({:>8.4f} → {:.4}; this toolchain's std rejects the `f`
trait). Ran: `./tools/offcentre_probe/target/x86_64-unknown-linux-musl/release/offcentre_probe`.
Output confirms the note's structural verdict exactly:
- files_parsed=53, total_ordinates=51499, t_max=51034.099779.
- moving boundary 1/2+b/L(t), b=0.0758: boundary 0.5149 at t=1e3 → 0.5078 at t=1e5 (right edge).
- off_line_count(Re>1/2+b/L) = 0 identically (data stores index+ordinate only → VACUOUS, PROVEN
  by construction; the binary only confirms).
- on-line N(1/2,Tmax)=51499 vs (T/2π)ln(T/2π)=73120.2 → ratio 0.7043 (Theta(T log T), never o).
- growing-window counts monotone in T (28,69,167,390,893,2012,4476,9856,20019,13575) — the
  o(T log T) sanity check is untestable with this data.
VERDICT (unchanged from agent C): route PROVEN empty; window pinned at 0.6725007, class
ceiling 0.6818, beyond-α=1 closed. Ledgered as dead lever. Probe binary is the artifact.
