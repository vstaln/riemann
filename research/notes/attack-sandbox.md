# Attack: V7 — method sandbox. Does the rank–trace certificate saturate at ≈1 (RH-true) or only at ≈2/3?

**Agent:** EXECUTIONER (V7 method sandbox), Round 2. **Date:** 2026.
**Vector:** attack-vector-catalog §3 #4 (V7). **Status:** COMPLETE — worlds run, interpretation written.

## 0. Bottom line (read this first)

- **In the real (RH-true) world the certificate does NOT saturate near 1.** It reads
  bound/N ≈ 0.70–0.72 at T = 100–1300, strictly above 0.6725, and trends DOWN toward the
  asymptotic constant 2 − c = **0.6725007** (c = 1/2 + (1/√2)cot(1/√2) = 1.3274993, the HS constant
  of Lemma 3.3). So V7's "≈2/3" horn is the measured behavior of the real arithmetic.
- **But the method is NOT structurally capped at 2/3.** The same inequality on a rigid-lattice
  all-on-line world reads bound/N = **0.9677 → 0.9754** (T = 200 → 1100), saturating near ≈0.977
  (Parseval asymptote 2 − ∫ψ⁴/(∫ψ²)² = 0.9769, CHECKED NUMERICALLY). A jittered lattice (rigidity +
  noise) reads 0.893–0.903. So the rank–trace certificate is a **repulsion-certificate**: its value
  is 2 − (HS constant), and the HS constant is the off-diagonal pair sum under the kernel — the
  zeros' pair-correlation arithmetic.
- **The gap 1 − 0.6725 = 0.3275 = c − 1 is exactly the asymptotic off-diagonal HS²/N.** The deficit
  of the real-world certificate from 100% is 100% arithmetic (the HS constant pinned by the real
  zeros' two-point statistics), i.e. the arithmetic that the extremal-law ceiling (0.6818, Lean
  `PairCeiling`) prices. The answer to V7: **arithmetic deficit, not structural lossiness** — with
  the caveat that "lossy" is accurate in the practical sense (the certificate under-reads the true
  100% on-line count because the two-moment bookkeeping is provably tight given the moments:
  `lemmaR_tight`, Δ = 0 in the real world, `[multiplicity §0, §2]`).
- **Off-line contamination is expensive.** Injecting a few % of off-line pairs (4–10% of zeros,
  β ≳ 0.1–0.3) drops the certificate BELOW 0.6725. tr/N stays ≈ 1 (the inputs are insensitive to
  off-line zeros at the o(N) level, exactly as the paper claims `[litmap §4c12]`); HS²/N rises, and
  the certificate reads the difference.
- **Clustering empties the certificate.** An all-on-line Poisson world (no repulsion) reads
  bound/N ≈ 0.10 → −0.05, i.e. an EMPTY certificate, reproducing the Davenport–Heilbronn "empty
  certificate" mechanism in a toy (C Rem 7.2(iii), PROVEN-as-stated). The certificate is therefore a
  repulsion statement, not an RH statement.
- **What round 3 should fund:** new inputs that move the moment constants — V3 (unconditional third
  moment tr Â³) first, V4/V5 (moment-order capacity LP) as the roadmap — plus the in-class V2
  (0.6725 → 0.6818 LP dual, the only proven-inputs constant gain), and a cheap new gate: any
  candidate input must separate ζ's arithmetic from the Poisson world.

## 1. Provenance (code-backed verification protocol)

- **Code:** scratch copy of the canonical finitet at `/tmp/finitet-v7` (canonical
  `/home/vstaln/riemann/tools/finitet` untouched — it is owned by another agent; its `main.rs`
  mtime 2026-08-11 18:59 is prior to this session; `bin_cinf.rs` was added by that agent, not here).
  New sandbox binary: `/tmp/finitet-v7/src/sandbox.rs`.
  - Archive (sha256 `31ba07e962977dccd8561a0ad28f6aae055d85e8bf5cc1e9b5b9e10c6668b2e8`):
    `research/notes/attack-sandbox/{sandbox.rs, Cargo.toml, cargo-config.toml, sandbox-run4.txt, sandbox-run2.txt}`.
- **Build:**
  `cd /tmp/finitet-v7 && export PATH=$HOME/.cargo/bin:$PATH RUSTFLAGS="-C linker=rust-lld" && cargo build --release --target x86_64-unknown-linux-musl --bin finitet-sandbox`
  (Rust 1.97.1; no deps; same musl+rust-lld toolchain as the canonical crate).
- **Run:** `./target/x86_64-unknown-linux-musl/release/finitet-sandbox > /tmp/sandbox-run4.txt 2>&1`
  (deterministic: a repeat run is bit-identical after stripping the wall-clock column).
- **Sanity anchors:** (i) the pair-check reproduces the canonical synthetic-pair result of
  attack-finitet §7: isolated pair eigenvalues {+1.817579, −0.151694} (in W units {+2.1403,
  −0.1786}); (ii) the REAL world column reproduces attack-finitet §3 exactly at T = 100–700
  (e.g. T=200: tr/N = 0.988856, HS²/N = 1.261182, bound/N = 0.716530); (iii) tr = Σλ and
  HS² = Σλ² from Jacobi eigenvalues agree with the direct sums to ≤ 2e-10 in all worlds.
- **Bugs found and fixed during the run** (documented for the record): (1) first build normalized
  by ∫ψ instead of ∫ψ² → all numbers wrong (tr/N ≈ 0.917); caught because the real-world column
  did not reproduce §3. (2) an initial random-injection variant ADDED pairs instead of REPLACING
  zeros (N + N₂ total), visible as tr/N > 1; fixed to a replace-world (N₁ + 2N₂ = N). Both fixed;
  the numbers below are from the corrected code.
- **Labels:** every measured entry below is **CHECKED NUMERICALLY** (finite-T, f64, hard-cutoff
  ψ = cos(√2u)·1_{|u|≤1/2}, single sample per world, no window averaging — same caveats as
  attack-finitet §6). Method structure (Lemma 3.4 rank–trace, Lemma R / Thm B bookkeeping, HS
  constant) is **PROVEN** `[litmap §2, kernel §2, multiplicity §1, Lean]`. The DH "empty
  certificate" is **PROVEN-as-stated** in C Rem 7.2(iii) `[litmap §4c12]`; the Poisson world below is
  a toy mechanism for it, not a proof. The interpretation section is CONJECTURED-but-now-supported
  by these numbers.

## 2. Construction (identical pipeline to attack-finitet, plus two certificates)

Same as finitet main.rs: φ_T(x) = ψ(xT/N), ψ(u) = cos(√2u)·1_{|u|≤1/2}, V[ρ][k] = Ψ(s_ρ − k),
s_ρ = (γ_ρ − T)·N/T, W_T = (1/∫ψ²)·VᵀV, ∫ψ² = 0.8492279993. Measured per world:
- tr/N, ‖W‖²_HS/N (diag + offdiag), rank (Jacobi, threshold 1e-6·λmax), n₊/n₋,
- **bound_rank/N = (2·tr − HS²)/N**  (Lemma 3.4: rank ≥ 2tr − ‖W‖²),
- **bound_s1/N = (4·tr − HS² − 2N)/N**  (Thm B / Lemma R, c = 2: s₁ ≥ 4tr − ‖W‖² − 2N,
  `[multiplicity §1]`),
both → 2 − c = 0.6725007 in the all-on-line limit. In all-on-line worlds bound_s1 is the
on-line-proportion certificate (rank = N₁ = N); in off-line worlds bound_s1 ≤ truth s₁ is checked
explicitly (validity — OK in every world below).

**Worlds:**
(a) **REAL all-on-line**: LMFDB zeros `tools/data/zeros_1_1000.txt` (T = 100–700, N ≤ 569) +
`zeros_computed_10000.txt` (T = 900–1300, N ≤ 1183). (The real data IS an RH-true world
numerically: all 1000/10000 zeros on the line, simple.)
(b) **FORCED OFF-LINE**: inject N₂ = f·N off-line pairs (each pair = 2 zeros at the same ordinate,
split ±β from the line via the synthetic-pair machinery, pair form 2(Re v·Re vᵀ − Im v·Im vᵀ),
exactly attack-finitet §7). Two patterns: deterministic (lowest N₁ = N − 2N₂ ordinates stay
on-line, top 2N₂ form consecutive pairs) and random (2N₂ random ordinates, sorted into consecutive
pairs). Truth s₁/N = N₁/N = 1 − 2f. β ∈ {0.1, 0.3} in ordinate units (recall mean zero spacing at
height ~1000 is ≈ 0.6; β = 0.3 is a deep off-line zero, β = 0.1 shallow).
(c) **SYNTHETIC all-on-line**: rigid lattice (N midpoints, s = k + ½), jittered lattice (s = k + ½ +
U(−0.2, 0.2)), Poisson (N uniform points, no repulsion).

## 3. Worlds table

Constants: c = 1.3274992963, 2 − c = 0.6725007037. All quantities normalized per N.

### World (a) — REAL, all on-line (RH-true data)
| T | N | tr/N | HS²/N | diag+off | rank(1e-6) | bound_rank/N | bound_s1/N | Δ_s1 vs 0.6725 |
|---|---|---|---|---|---|---|---|---|
| 100 | 50 | 0.992343 | 1.265459 | 1.122+0.143 | 50 | 0.719228 | 0.703914 | +0.0314 |
| 200 | 123 | 0.988856 | 1.261182 | 1.113+0.148 | 121 | 0.716530 | 0.694241 | +0.0217 |
| 300 | 203 | 0.994489 | 1.275443 | 1.128+0.148 | 200 | 0.713534 | 0.702511 | +0.0300 |
| 400 | 289 | 0.995801 | 1.280378 | 1.122+0.159 | 284 | 0.711225 | 0.702828 | +0.0303 |
| 500 | 380 | 0.996327 | 1.280708 | 1.109+0.172 | 374 | 0.711945 | 0.704598 | +0.0321 |
| 600 | 472 | 0.998163 | 1.287259 | 1.137+0.150 | 465 | 0.709068 | 0.705395 | +0.0329 |
| 700 | 569 | 0.997518 | 1.283776 | 1.132+0.152 | 561 | 0.711259 | 0.706294 | +0.0338 |
| 900 | 766 | 0.999009 | 1.290625 | 1.140+0.151 | — | 0.707393 | 0.705412 | +0.0329 |
| 1100 | 972 | 0.999128 | 1.291160 | 1.137+0.155 | — | 0.707096 | 0.705352 | +0.0329 |
| 1300 | 1183 | 0.999522 | 1.294078 | 1.143+0.151 | — | 0.704966 | 0.704010 | +0.0315 |

Both certificates are above 0.6725 at every T by Δ ≈ +0.02…+0.05 and descend slowly toward
0.6725 (Δ(T) ≈ 0.014 + 0.155/lnT per attack-finitet §5 — the finite-T bound overshoots the
asymptotic constant from above). tr/N → 1, HS²/N → c = 1.3275 from below (deficit still ~2.5% at
T = 1300). rank = N (n₊ = N, n₋ = 0; W is PSD by construction). **The RH-true world reads ≈ 0.70,
NOT ≈ 1.**

### World (b) — FORCED OFF-LINE (T = 500, N = 380 unless noted; truth s₁/N = 1 − 2f)
| pattern | β | f (=N₂/N) | tr/N | HS²/N | bound_rank/N | bound_s1/N | Δ_s1 | n₋/N₂ | validity |
|---|---|---|---|---|---|---|---|---|---|
| det (top) | 0.1 | 0.01 | 0.996364 | 1.294020 | 0.698709 | 0.691438 | +0.019 | 2/4 | OK |
| det (top) | 0.1 | 0.02 | 0.996429 | 1.310087 | 0.682770 | 0.675627 | +0.003 | 6/8 | OK |
| det (top) | 0.1 | 0.05 | 0.996387 | 1.355808 | 0.636966 | 0.629739 | −0.043 | 16/19 | OK |
| det (top) | 0.3 | 0.01 | 0.996366 | 1.305811 | 0.686920 | 0.679652 | +0.007 | 3/4 | OK |
| det (top) | 0.3 | 0.02 | 0.996463 | 1.335324 | 0.657601 | 0.650527 | −0.022 | 7/8 | OK |
| det (top) | 0.3 | 0.05 | 0.996394 | 1.422578 | 0.570209 | 0.562997 | −0.110 | 17/19 | OK |
| rnd | 0.3 | 0.02 | 0.996352 | 1.417124 | 0.575580 | 0.568284 | −0.104 | 8/8 | OK |
| rnd | 0.3 | 0.05 | 0.996330 | 1.570069 | 0.422592 | 0.415252 | −0.257 | 18/19 | OK |

β-sweep (det, f = 0.02, T = 500): β = 0.05 → 0.677453 (+0.005), 0.10 → 0.675627 (+0.003),
0.20 → 0.667484 (−0.005), 0.30 → 0.650527 (−0.022), 0.50 → 0.556505 (−0.116).
T = 200 runs (det): β = 0.1: f = 0.01/0.02/0.05 → 0.699096/0.689215/0.639463;
β = 0.3: 0.698640/0.681989/0.604581.

Reading: **tr/N is insensitive to off-line injection** (0.9963–0.9965 across every entry — the
paper's "inputs insensitive to o(N) off-line zeros" `[litmap §4c12]` holds at the Θ(N) level too
for tr). **HS²/N is sensitive** (1.281 → 1.42–1.57) and the certificate reads the difference. A
few % of off-line pairs drops the s₁-certificate below 0.6725: at β = 0.3 the crossing is between
f = 0.01 (holds, Δ +0.007) and f = 0.02 (breaks, Δ −0.02) for the scattered pattern, between 0.02
and 0.05 for the top-clustered pattern; shallow β = 0.1 survives to f ≈ 0.02–0.05. Deeper off-line
zeros cost more. All worlds satisfy the Lemma R validity check (bound_s1 ≤ truth s₁); n₋ ≈ N₂
(one negative direction per pair — Claim 2.3's (1,1) signature reproduces in the injected worlds).

### World (c) — SYNTHETIC all-on-line
| world | T | N | tr/N | HS²/N | rank(1e-6) | bound_rank/N | bound_s1/N | eigmin/λmax |
|---|---|---|---|---|---|---|---|---|
| lattice (rigid) | 200 | 122 | 0.989875 | 1.012061 | 122 | 0.967689 | 0.947439 | 5.6e-2 |
| lattice (rigid) | 500 | 379 | 0.996328 | 1.019170 | 379 | 0.973487 | 0.966143 | 4.3e-2 |
| lattice (rigid) | 1100 | 972 | 0.998435 | 1.021443 | — | 0.975427 | 0.972296 | — |
| jitter ±0.2 | 200 | 122 | 0.988973 | 1.084617 | 122 | 0.893328 | 0.871273 | 2.7e-2 |
| jitter ±0.2 | 500 | 379 | 0.996872 | 1.090390 | 379 | 0.903354 | 0.897098 | 2.6e-2 |
| poisson s=1 | 200 | 122 | 0.990201 | 1.770034 | 111 | 0.210369 | 0.190772 | ≈0 (n₋=0) |
| poisson s=1 | 500 | 379 | 0.998954 | 1.897908 | 339 | 0.099999 | 0.097906 | ≈0 (n₋=0) |
| poisson s=2 | 500 | 379 | 0.999047 | 2.042455 | 329 | −0.044361 | −0.046266 | ≈0 (n₋=0) |
| poisson s=1 | 1100 | 972 | 0.999550 | 1.982879 | — | 0.016220 | 0.015320 | — |

Reading: the certificate value is a monotone function of rigidity. Lattice (perfect repulsion):
HS²/N → 1.0231 (Parseval ∫ψ⁴/(∫ψ²)² = 1.0230935292, CHECKED NUMERICALLY — matches the finite-T
trend 1.012 → 1.021) and the certificate saturates at **2 − 1.0231 = 0.9769**, not 1 and not 2/3.
Jitter: intermediate (0.89–0.90). Poisson (no repulsion): HS²/N → 2.0231 (Parseval 1 + ∫ψ⁴/∫ψ²²,
CHECKED NUMERICALLY), certificate → **−0.0231: EMPTY**, and the rank drops (329–354/379 —
clustered points make V numerically near-rank-deficient). tr/N ≈ 1 in every world.

## 4. Interpretation (lossy-method vs arithmetic-deficit)

**What the certificate is.** bound/N = 2 − HS²/N asymptotically (tr/N → 1 in every world), and
HS²/N = 1 + (off-diagonal pair sum of Ψ₂ over the zero differences)/(∫ψ²)². So the certificate
value is **1 minus the zeros' pair-correlation integral under the kernel** — a two-point-statistics
readout. It is exactly the arithmetic that the form factor F(α) and the extremal-law ceiling
(0.6818, `[ceiling §1]`) price.

**Answer to V7's question, precisely stated.**
- In the real RH-true world the certificate reads ≈ 0.70 (finite T) and → **0.6725** asymptotically:
  the "≈2/3" horn, measured. It does not saturate near 1.
- But this is NOT because the rank–trace inequality is structurally capped at 2/3: the identical
  inequality on an all-on-line rigid-lattice world reads **≈ 0.977**. The two-moment method is not
  "inherently lossy" in the strong sense — its ceiling over the tested density-1 worlds is ≈ 0.977
  (the lattice world), far above 0.6725. Whether a non-lattice point set can push the HS constant
  below the lattice value 1.0231 is CONJECTURED (rigidity plausibly minimizes the pair sum, but not
  proven here).
- The deficit of the real-world certificate from 1 is **exactly the arithmetic**: 1 − 0.6725 =
  0.3275 = c − 1, the asymptotic off-diagonal HS²/N of the actual zeros. Given the real zeros'
  moments (tr, HS²), the bookkeeping cannot certify more than 2 − C (Thm B; `lemmaR_tight`,
  PROVEN; the real world has Δ = 0 slack `[multiplicity §0, §2]`). The extremal-law obstruction
  (pair-correlation arithmetic) is the whole story for the 0.6725 — *not* a structural cap of the
  inequality.
- The honest nuance that V7's dichotomy misses: the certificate is a LOWER BOUND, so "≈2/3 in an
  RH-true world" is compatible with "arithmetic deficit." Both V7 horns conclude "fund new
  inputs," and the sandbox says that conclusion is right — but for the arithmetic-deficit reason:
  the certificate is pinned by the moment vector, and only new inputs (higher moments) or a better
  certificate on the same inputs (V2: 0.6725 → 0.6818) move it.

**What the off-line world adds.** The certificate is sensitive to off-line contamination in a way
the inputs are not: tr/N ≈ 1 regardless (paper's claim, `[litmap §4c12]`), but each off-line pair
costs ≈ 1.4–7.0 in the s₁-certificate numerator (≈ 6.5 for the scattered pattern, cross-terms
included; ≈ 1.4–7.0 for the top-clustered pattern, growing with β) and inflates HS²/N by the same
amount per pair — so a few % of off-line zeros breaks the 0.6725 certificate. A genuine
small-RH-failure world would therefore read below 0.6725, consistent with the theorem's input
sensitivity being concentrated in the second moment.

**What the Poisson world adds (the DH control, mechanistically).** An all-on-line point set with
no repulsion gives HS²/N ≥ 2, hence certificate ≤ 0 — EMPTY, exactly as C Rem 7.2(iii) says for
Davenport–Heilbronn/Epstein functions ("the certificate is empty"; PROVEN-as-stated `[litmap
§4c12]`). The mechanism is visible in the toy: clustering inflates the pair sum and collapses the
rank. **Consequence: the certificate is a repulsion statement, not an RH statement.** 0.6725 for ζ
is ζ's zeros being (statistically) repulsive; a clustered object with RH-like moments gets nothing.

## 5. What round 3 should fund (recommendation)

1. **V3 — unconditional third moment tr Â³ (highest priority from this sandbox).** The sandbox
   shows the certificate ceiling is set by the moment vector; a third moment is the direct route
   past the two-moment wall (the only documented lever past it: `[multiplicity §4]`). The
   λ < 1 Rudnick–Sarnak admissibility was already confirmed; the missing input is the
   triple-correlation asymptotics.
2. **V4/V5 — moment-order capacity LP (the roadmap).** The certificate = 2 − C structure means the
   value of each new input is a curve over moment order; the capacity LP turns "which conjecture
   is cheapest" into a priced decision. Fund as the planning layer.
3. **V2 — in-class LP dual (0.6725 → 0.6818).** The sandbox shows the certificate under-reads the
   pair-correlation arithmetic by ≈ 0.01 (0.6725 vs the 0.6818 ceiling on the same class of
   inputs) — the only proven-inputs constant gain, unchanged by this sandbox.
4. **New gate for any candidate input (cheap, sharp):** a proposed input must separate ζ's
   arithmetic from the Poisson world — if it does not (Poisson would also satisfy it), it cannot
   raise the certificate. This is a 2-line filter in the sandbox harness.
5. **Keep the DH framing visible:** treat "≥ 67.25%" as a repulsion statement, not RH evidence;
   any round-3 claim about "the certificate at 0.6725 proves RH-ish structure" is a category error.

## 6. Negatives, caveats, and honest limits

- All measurements: finite-T, f64, hard-cutoff ψ, single sample per world (no window averaging);
  same caveats as attack-finitet §6. The finite-T certificate overshoots the asymptotic constant
  from above (Δ > 0, ~1/log T), so finite-T values ≠ asymptotic values; the asymptotic references
  (real 0.6725, lattice 0.9769, Poisson −0.0231) are theory/Parseval values, CHECKED NUMERICALLY
  by the finite-T trends.
- **Pattern-dependence in world (b):** deterministic top-clustered vs random-scattered injection
  differ by up to ≈ 0.15 in bound_s1 at f = 0.05 (scattered is more damaging, because the pair×
  on-line cross-terms are larger in the bulk). The direction is robust (a few % off-line breaks
  0.6725 under every pattern and β), the exact crossing fraction is not. The scattered pattern is
  the honest model of a genuine RH failure.
- The lattice world is a hard-rod idealization whose moments differ from ζ's (HS²/N → 1.0231 vs
  1.3275); it demonstrates the inequality's ceiling over worlds, not a claim about ζ's arithmetic.
- The Poisson world is a toy mechanism for the DH control, not a proof of it; the DH statement
  itself is PROVEN-as-stated in C (Rem 7.2(iii)) `[litmap §4c12]`.
- The interpretation (§4) is CONJECTURED-but-supported; the structural facts it rests on (rank–
  trace inequality, Thm B bookkeeping, lemmaR_tight, Δ = 0, c = 1.3275) are PROVEN
  `[kernel §2, multiplicity §1–§2]`.
- Two self-inflicted bugs were found and fixed during the run (wrong normalization; add-vs-replace
  injection) — each was caught because it broke an anchor (reproduction of attack-finitet §3;
  tr/N ≤ 1). The numbers in this note are from the corrected code (sha256 above).

## 7. Reproduction

```
git-style archive: research/notes/attack-sandbox/sandbox.rs (sha256 31ba07e9...)
cd /tmp/finitet-v7 && export PATH=$HOME/.cargo/bin:$PATH RUSTFLAGS="-C linker=rust-lld" \
  && cargo build --release --target x86_64-unknown-linux-musl --bin finitet-sandbox
./target/x86_64-unknown-linux-musl/release/finitet-sandbox > /tmp/sandbox-run4.txt 2>&1
```
Data files: `tools/data/zeros_1_1000.txt` (LMFDB, 1000 zeros) and `tools/data/zeros_computed_10000.txt`
(10000 computed zeros, γ ≤ 9879). Canonical pipeline for comparison:
`cargo build --release --target x86_64-unknown-linux-musl --bin finitet && ./target/.../finitet`.
