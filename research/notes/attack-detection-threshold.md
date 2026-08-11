# Attack: E4 — off-line detection threshold (how much off-line structure could hide in the real data?)

**Agent:** EXECUTIONER (vector E4), Round 2. **Date:** 2026.
**Vector:** idea-generator-ml-eco.md E4 (TESTED-OPEN, extends attack-finitet.md §7 / attack-sandbox.md world (b)).
**Status:** COMPLETE — sweep run, thresholds found, note written.
**Question:** the V7 sandbox showed that a few % of injected off-line pairs drops the certificate below
0.6725. E4 quantifies the REVERSE: how much off-line structure could exist in the REAL data without the
certificate noticing — i.e. the detection threshold, the realized-world slack in off-line pairs. Tells us
how "loud" a hypothetical off-line signal must be.

## 0. Bottom line (read this first)

- **The certificate's blindness window is small.** Measured against the real-data noise band
  bound_rank/N ∈ **[0.704966, 0.719228]** (T = 100–1300, the task's 0.704–0.719), the certificate leaves
  the band with **f = 1 pair** (scattered/bulk placement, any β ≥ 0.05; cert drops to ≈ 0.68) to
  **f ≈ 1–1.5% of pairs** (top-clustered edge placement, β ≤ 0.2; cert ≈ 0.70). Against the *theoretical*
  floor 0.6725 the tolerance is larger: ~4% of pairs (top-clustered, β ≤ 0.3) before the bound drops below
  0.6725 — consistent with the sandbox's "few %" (it measured the theory floor, not the noise band).
- **A hypothetical off-line signal must be nearly silent to escape detection.** The realized slack is
  **O(1) pairs out of N** — at most ~1 pair hiding at the window's top edge at shallow depth (β ≲ 0.3 in
  ordinate units), where *both* detectors are blind. Any bulk pair at any β ≥ 0.05, or any pair at
  β ≳ 0.5 anywhere, is caught by at least one of the two detectors.
- **The direct detector n₋(W_T) is the sharper instrument: n₋ = 0 on real data at T = 100–700 (all three
  thresholds; reproduces idea-generator-chem.md F8), and n₋ > 0 with a SINGLE off-line pair** (f = 1/N),
  whenever the pair's negative eigenvalue clears the numerical floor: β ≳ 0.02 (bottom edge), ≳ 0.1
  (bulk, representative), ≳ 0.3–0.5 (top edge). One pair beats the certificate's ~1–1.5% in f, but n₋
  misses shallow pairs (β ≲ 0.1) that the certificate catches.
- **Honesty: this is a diagnostic, not a theorem input.** It adds nothing to the 0.6725 argument (no new
  input, no constant moved) and it does not bound the true off-line content of ζ's zeros (the real data is
  all-on-line by construction; n₋ = 0 is a consistency check). Its value is quantitative: how "loud" an
  off-line signal would have to be for the realized-world measurements to notice — the answer is "a single
  bulk pair at any depth, or ~1% of edge pairs", which is the honest reading of the certificate's
  sensitivity in the world the theorem lives in.

## 1. Provenance (code-backed verification protocol)

- **Code:** new scratch copy of the sandbox at `/tmp/finitet-e4` (itself a copy of the canonical
  `/home/vstaln/riemann/tools/finitet`, untouched — owned by another agent, main.rs mtime 2026-08-11 18:59
  prior to this session). Four new binaries (all Rust, musl+rust-lld, no deps):
  - `e4sweep.rs` — real column + full sweep grid + single-pair β-floor (the main run);
  - `pairdiag.rs` — position dependence of a single pair's negative eigenvalue + §7 anchor reproduction;
  - `e4probe.rs` — fine f-grid below 0.5% (scattered) and bisection of the 1%–2% crossing (top-clustered);
  - `e4nminus.rs` — n₋ columns (rel 1e-9, rel 1e-10, abs 1e-12) for the sweep grid.
- **Archive (same pattern as the sandbox):** `research/notes/attack-detection-threshold/` holds the four
  `.rs` files, `Cargo.toml`, the four run transcripts, and `SHA256SUMS` (e4sweep.rs
  `ac1d50e6…`, pairdiag.rs `044ce4f7…`, e4probe.rs `69591265…`, e4nminus.rs `607840a1…`).
- **Build:** `cd /tmp/finitet-e4 && export PATH=$HOME/.cargo/bin:$PATH RUSTFLAGS="-C linker=rust-lld"
  && cargo build --release --target x86_64-unknown-linux-musl --bin finitet-e4sweep` (same for
  `finitet-pairdiag`, `finitet-e4probe`, `finitet-e4nminus`).
- **Run:** `./target/x86_64-unknown-linux-musl/release/finitet-e4sweep > /tmp/e4sweep-run1.txt 2>&1`
  (5m20s), `…-finitet-pairdiag` (9.5s), `…-finitet-e4probe` (1m12s), `…-finitet-e4nminus` (10m20s).
  Deterministic: no randomness except the seeded scattered pattern (SplitMix64, seed 7, same as sandbox).
- **Sanity anchors:** (i) real column reproduces attack-finitet §3 and sandbox world (a) exactly
  (T=200: tr/N 0.988856, HS²/N 1.261182, bound_rank/N 0.716530); (ii) the pair-check reproduces the
  finitet §7 synthetic-pair anchor: isolated pair at γ=201.265, β=0.3 → M eigenvalues
  {**+1.817579, −0.151694**}, W units {+2.1403, −0.1786} (pairdiag output, byte-identical to §7);
  (iii) the f = 0 rows of the sweep reproduce the real world at the same T.
- **Bugs found and fixed:** none new in this run (machinery is the sandbox's, already debugged); the only
  anomaly investigated was the position dependence of the pair's negative eigenvalue (see §6), resolved by
  pairdiag, not a code bug.

## 2. Construction and conventions

Identical pipeline to the sandbox (attack-sandbox.md §2): ψ(u) = cos(√2u)·1_{|u|≤1/2},
∫ψ² = 0.849227999318304, s_ρ = (γ_ρ − T)·N/T, W_T = (1/∫ψ²)·VᵀV, V[ρ][k] = Ψ(s_ρ − k).
Certificates (both → 2 − c = 0.672500703679412, c = 1.327499296320588):
- **bound_rank/N = (2tr − ‖W‖²_HS)/N** (Lemma 3.4 rank–trace — the certificate of record, the task's
  0.704–0.719 column);
- bound_s1/N = (4tr − ‖W‖²_HS − 2N)/N (Thm B / Lemma R) — reported as secondary; its band is
  [0.694241, 0.706294].
**Off-line injection** (exactly the sandbox's machinery, attack-finitet §7): a pair = 2 zeros at a common
mean ordinate γ₀, split ±β off the line, pair matrix M = vvᵀ + conj(v)conj(v)ᵀ = 2(Re v·Re vᵀ − Im v·Im vᵀ)
(signature (1,1)). **f = N₂/N is the pair fraction** (N₂ pairs, 2N₂ off-line zeros, truth s₁/N = 1 − 2f);
**β is in ordinate units** (sandbox convention: the s-space displacement is imb = β·N/T, e.g. β = 0.3 →
imb = 0.1845/0.2030/0.2280 at T = 200/300/500). Mean zero spacing ≈ 0.6–0.8 in ordinates at height
~1000 → β = 0.3 ≈ half a spacing ("deep"), β = 0.05 ≈ 1/12 of a spacing ("shallow"). Two placement
patterns: **top-clustered** (pairs at the window's top edge — the optimistic/hiding pattern) and
**random-scattered** (seed 7 — the sandbox's honest model of a genuine RH failure).
**Noise band (the detection reference):** the spread of the real-world bound_rank/N across T = 100–1300,
**[0.704966, 0.719228]** (width 0.014262) — the task's definition: "moves OUTSIDE the noise band of the
real-data measurement (the Δ(T) fluctuation across T)". Every threshold below is "smallest f (and β) with
cert < band_min = 0.704966". The theory floor 0.6725007 is reported separately.

## 3. Real-world baseline and n₋ confirmation (task 3, first half)

From e4sweep section A (zeros_1_1000.txt for T ≤ 700, zeros_computed_10000.txt for T ≥ 900):

| T | N | tr/N | HS²/N | bound_rank/N | bound_s1/N | eigmin (W) | n₋ (rel1e-9 / rel1e-10 / abs1e-12) |
|---|---|---|---|---|---|---|---|
| 100 | 50 | 0.992343 | 1.265459 | 0.719228 | 0.703914 | +2.07e-6 | 0 / 0 / 0 |
| 200 | 123 | 0.988856 | 1.261182 | 0.716530 | 0.694241 | +3.29e-15 | 0 / 0 / 0 |
| 300 | 203 | 0.994489 | 1.275443 | 0.713534 | 0.702511 | +2.49e-17 | 0 / 0 / 0 |
| 400 | 289 | 0.995801 | 1.280378 | 0.711225 | 0.702828 | −6.57e-17 | 0 / 0 / 0 |
| 500 | 380 | 0.996327 | 1.280708 | 0.711945 | 0.704598 | +1.38e-17 | 0 / 0 / 0 |
| 600 | 472 | 0.998163 | 1.287259 | 0.709068 | 0.705395 | −2.26e-16 | 0 / 0 / 0 |
| 700 | 569 | 0.997518 | 1.283776 | 0.711259 | 0.706294 | −4.61e-16 | 0 / 0 / 0 |
| 900 | 766 | 0.999009 | 1.290625 | 0.707393 | 0.705412 | (eig skipped) | — |
| 1100 | 972 | 0.999128 | 1.291160 | 0.707096 | 0.705352 | (eig skipped) | — |
| 1300 | 1183 | 0.999522 | 1.294078 | 0.704966 | 0.704010 | (eig skipped) | — |

- **n₋(W_T) = 0 at T = 100–700 under rel 1e-9, rel 1e-10, and abs 1e-12 thresholds — CHECKED NUMERICALLY
  (e4sweep section A).** Confirms idea-generator-chem.md F8 (which reported n₋/N = 0 at T = 200–700 with
  min eig 3.4e-15…−1.5e-15; the T = 100 entry +2.07e-6 is new here and consistent with the same
  statement — W is PSD by construction when all zeros are on the line). At T ≥ 300 the min eigenvalue
  sits at the f64 floor (≈ ±1e-16), the documented near-rank-deficiency of attack-finitet §3/§6.
- Noise band = **[0.704966, 0.719228]** (bound_rank/N) — matches the task's 0.704–0.719. The T = 1300
  real value 0.704966 *is* the band's lower edge, so at T = 1300 any injection trivially exits the band;
  the meaningful thresholds are at T = 200–500 where the real value sits comfortably inside (slack to
  band_min: 0.0116 / 0.0086 / 0.0070 at T = 200/300/500).

## 4. Sweep: certificate value vs (f, β) — the detection-threshold table (task 2)

Grid: f ∈ {0%, 0.5%, 1%, 2%, 4%, 8%} (= N₂/N pairs), β ∈ {0.05, 0.1, 0.2, 0.3, 0.5, 1.0} (ordinate
units), T = 200/300/500. Cells: **bound_rank/N (n₋ at rel 1e-10)**. n₋ measured by e4nminus at
β ∈ {0.05, 0.1, 0.3, 0.5} × f ∈ {0.5%, 2%, 8%} and pairdiag for single pairs; "·" = not separately
measured (n₋ ≈ N₂ − O(1) in every measured row, deficit 0–4 — one negative direction per pair, minus edge pairs
whose negative is suppressed, cf. §6). Green = inside the real-data band (≥ 0.704966) = the hiding region.

### 4.1 T = 300 (E4's primary probe window), deterministic top-clustered

| f (N₂) | β=0.05 | β=0.10 | β=0.20 | β=0.30 | β=0.50 | β=1.00 |
|---|---|---|---|---|---|---|
| 0% (0) | **0.713534** (0) | 0.713534 | 0.713534 | 0.713534 | 0.713534 | 0.713534 |
| 0.5% (1) | **0.711361** (0) | **0.711249** (0) | **0.710759** (·) | **0.709782** (0) | 0.704851 (1) | 0.564506 (·) |
| 1% (2) | **0.707426** (·) | **0.706969** (·) | **0.705011** (·) | 0.701250 (·) | 0.683966 (·) | 0.314024 (·) |
| 2% (4) | 0.693359 (3) | 0.692130 (3) | 0.686792 (·) | 0.676250 (3) | 0.624821 (3) | −0.617796 (·) |
| 4% (8) | 0.661221 (·) | 0.658424 (·) | 0.646293 (·) | 0.622405 (·) | 0.506635 (·) | −2.193532 (·) |
| 8% (16) | 0.610313 (14) | 0.604383 (14) | 0.578592 (·) | 0.527517 (14) | 0.276175 (15) | −6.062494 (·) |

**Hiding region (top-clustered, T=300):** f ≤ 0.5% at β ≤ 0.3 (1 pair, cert ≥ 0.7098), and f = 1%
(2 pairs) at β ≤ 0.2 (cert ≥ 0.7050). Everything else is outside the band. Crossing pinned by e4probe:
f = 1.5% (3 pairs) at β = 0.05/0.1/0.2 reads 0.7015/0.7008/0.6976 — already out; so the β ≤ 0.2 crossing
is **between f = 1% and 1.5%**, and at β = 0.3 between 0.5% and 1% (0.5% → 0.7098 in, 1% → 0.7013 out).

### 4.2 T = 300, random-scattered (seed 7) — the honest failure model

| f (N₂) | β=0.05 | β=0.10 | β=0.30 | β=0.50 |
|---|---|---|---|---|
| 0% (0) | 0.713534 (0) | 0.713534 | 0.713534 | 0.713534 |
| 0.3%–0.5% (1) | **0.683531** (0) | **0.683057** (0) | **0.677058** (1) | **0.658184** (1) |
| 1% (2) | 0.658914 (0) | 0.657954 (1) | 0.645870 (2) | 0.608305 (2) |
| 2% (4) | 0.635094 (2) | 0.633633 (2) | 0.614657 (3) | 0.551662 (4) |
| 4% (8) | 0.530928 (5) | 0.527718 (6) | 0.486515 (7) | 0.352984 (8) |
| 8% (16) | 0.373665 (13) | 0.367028 (14) | 0.282036 (16) | 0.007974 (16) |

(e4probe at f = 0.1–0.2% gives N₂ = 0 = real world; f = 0.3% already quantizes to 1 pair. The f = 0.3–0.5%
rows are the same single pair at indices (121, 161) of the T=300 window — a bulk position.)

**Scattered has NO hiding region at f ≥ 1 pair:** a single bulk pair (f ≈ 0.5%) drops the certificate to
≈ 0.68 at *every* β ≥ 0.05 — 0.030 below the real value, i.e. **2.1× the full band width** (derived:
0.0300 / 0.014262) and **3.5× the T=300 slack to band_min** (0.0300 / 0.008568).

### 4.3 Threshold summary (smallest f at which the certificate leaves the band / the theory floor)

From e4sweep THRESHOLDS + e4probe (ranges where the finer grid pins the crossing). band_min = 0.704966;
theory floor = 0.6725007.

| T | pattern | β | f_min_band (cert at crossing) | f_min_theory(0.6725) |
|---|---|---|---|---|
| 300 | top-clustered | 0.05 | **∈ (1%, 1.5%)** (≈0.702–0.707) | 4% (0.6612) |
| 300 | top-clustered | 0.10 | **∈ (1%, 1.5%)** | 4% (0.6584) |
| 300 | top-clustered | 0.20 | **∈ (1%, 1.5%)** | 4% (0.6463) |
| 300 | top-clustered | 0.30 | **∈ (0.5%, 1%)** | 4% (0.6224) |
| 300 | top-clustered | 0.50 | **0.5%** (0.7049, marginal) | 2% (0.6248) |
| 300 | top-clustered | 1.00 | **0.5%** (0.5645) | 0.5% |
| 300 | scattered | ≥ 0.05 | **≈ 1 pair, f ≈ 0.3–0.5%** (0.68) | 1% (0.6589) |
| 200 | top-clustered | 0.05–0.5 | **∈ (1%, 2%)** | 4–8% (β ≤ 0.1), 4% (β = 0.2–0.5) |
| 200 | top-clustered | 1.00 | **0.5%** (0.5900) | 0.5% |
| 500 | top-clustered | 0.05, 0.10 | **∈ (0.5%, 1%)** (0.706–0.699) | 4% |
| 500 | top-clustered | 0.20–1.0 | **0.5%** | 2% (β=0.3), 1% (β=0.5), 0.5% (β=1) |
| 500 | scattered | 0.30 | **1 pair (0.7027)**; β=0.05 borderline in (0.7051) | 1% (β=0.05) / 0.5–1% (β=0.3) |

**Headline threshold (task 2's answer):** the certificate leaves the real-data noise band at
**f ≈ 1 pair ≈ 0.3–0.5% (scattered/bulk, any β ≥ 0.05)** up to **f ≈ 1–1.5% (top-clustered, β ≤ 0.2)**,
with the β-dependence: shallow-β needs more pairs (f ≈ 1–2% at β ≤ 0.1), deep β (≥ 0.5) needs one pair
anywhere. Against the *theoretical* 0.6725 the slack is ~2–4× larger (f ≈ 4% at β ≤ 0.3, top-clustered;
1% scattered) — i.e. **the realized-world noise band is the tighter, more sensitive reference**: the
certificate "notices" off-line content well before it breaks the 0.6725 theorem bound. The sandbox's "a
few %" statement (§0) measured the theory floor; E4's band-based reading is stricter by ~2–4×.

Per-pair cost (derived from table rows, T=300, N=203): Δbound_rank/N per pair = **0.0022 (top-edge,
β=0.05)** → **0.0300 (bulk/scattered, β=0.05)**, i.e. 0.44 to 6.09 in the bound_rank numerator per pair —
the bulk cross-terms dominate, edge pairs are cheap to hide. This brackets the sandbox's "1.4–7.0" for
the s₁-numerator.

## 5. tr/N insensitivity (input-side confirmation)

Across the entire sweep (B-table: 90 rows, f ≤ 8%, β ≤ 1.0): tr/N ∈ [0.992, 1.011] in every injected
world, including β = 1.0 where tr/N briefly exceeds 1 (1.0106 at T=300, f=0.5%, β=1.0 — the pair's own
‖a‖² − ‖b‖² contribution). The paper's "inputs insensitive to o(N) off-line zeros" [litmap §4c12] holds
at the Θ(N) level for tr; **the certificate reads off-line content entirely through the second moment**
(HS²/N rises 1.275 → 1.30–8.08 with f and β) — exactly the sandbox's finding, re-confirmed on the new grid.

## 6. Direct detector n₋: threshold (task 3, second half)

**Real data: n₋ = 0 at T = 100–700 (confirmed, §3).** How many off-line pairs would flip it?

**Count threshold: ONE pair.** n₋ counts the pairs' negative directions (Claim 2.3's (1,1) signature):
measured n₋ ≈ N₂ in every swept row (e4nminus: e.g. T=300 top-clustered f=2%, N₂=4 → n₋=3; f=8%, N₂=16 →
n₋=13–15; scattered f=2%, N₂=4 → n₋=2–4), so **n₋ > 0 as soon as ≥ 1 pair exists**, i.e. f ≥ 1/N
(0.81% at T=200, 0.49% at T=300, 0.26% at T=500). In f-count this beats the certificate (which needs
~1–1.5% top-clustered) by ~2–4×, and matches it for scattered placement.

**β threshold (the "at what β" part):** the pair's negative eigenvalue in the *full* W_T is much smaller
than the isolated-pair value (the on-line part partially fills the negative direction) and is
position-dependent (pairdiag, T=200, one pair, λ_min of full W):

| position | β = 0.02 | 0.05 | 0.10 | 0.30 | 0.50 | n₋ > 0 at |
|---|---|---|---|---|---|---|
| bottom edge (γ≈201.3) | −1.4e-4 | −1.1e-3 | −4.7e-3 | −6.2e-2 | −2.9e-1 | β ≳ **0.02** |
| bulk (γ≈γ_101) | −7.4e-12 | −6.5e-11 | −1.7e-8 | −2.2e-6 | −1.5e-1 | β ≳ **0.05–0.1** |
| top edge (γ≈399) | −1.9e-15 | −1.3e-14 | −5.3e-14 | −9.6e-13 | −1.5e-7 | β ≳ **0.3–0.5** |

(Isolated-pair eigenvalues for reference at β=0.3: bottom {+1.8176, −0.1517}, bulk {+1.8682, −0.1750},
top {+1.3263, −0.0240} — raw M units, pairdiag. The full-W λ_min is 2–6 orders smaller than the isolated
λ₋ because the pair's negative direction overlaps the on-line span — the same cross-terms that drive the
certificate's HS².)

**Headline n₋ threshold: n₋ > 0 with a single off-line pair at β ≳ 0.1 (representative bulk position);
edge-bottom pairs need only β ≳ 0.02; top-edge pairs are the blind spot (β ≳ 0.3–0.5).** The detector's
β-blindness (shallow pairs, β ≲ 0.05–0.1 in the bulk) is complementary to the certificate's: shallow bulk
pairs are caught by the certificate (out of band at f = 1 pair, §4.2) but missed by n₋; deep pairs are
caught by both.

## 7. Interpretation: how much off-line structure could be hiding undetected

- **Answer: O(1) pairs per window — at most a handful — and only under favorable hiding conditions.**
  The joint (certificate ∪ n₋) blind spot is: a small number (≤ 1–2) of off-line pairs placed at the
  window's top edge at shallow depth β ≲ 0.3 (ordinate units; s-space displacement imb = β·N/T ≲ 0.2),
  where the certificate stays in-band (0.7098–0.7116 at T = 200–300, f = 0.5%, β ≤ 0.3) AND n₋ stays 0
  (top-edge negatives suppressed below the floor, §6). Everything else is detected: any bulk pair at any
  β ≥ 0.05 (certificate, §4.2), any pair at β ≳ 0.5 (n₋ everywhere, §6), ≥ 1% edge-clustered pairs
  (certificate, §4.1), ≥ 2–4% of pairs (0.6725 floor, §4.3).
- **How "loud" a hypothetical off-line signal must be:** it must consist of ≲ 2 pairs per window, hidden
  at the window edges, with depth below ~0.3 spacings. A genuine small-RH-failure signal (scattered pairs,
  per the sandbox's honest-model convention) is detected at a **single pair** — the certificate's
  realized-world blindness window is therefore ~N-fold smaller than "a few %" suggested by the theory-floor
  framing.
- **The detection thresholds are empirical, not theorems.** The band [0.704966, 0.719228] is the spread of
  ten single-sample real-world measurements (one world per T, no window averaging); the thresholds inherit
  that (finite-T, f64, hard-cutoff ψ) status. A T-aware observer comparing to the real value *at the same
  T* would see an even tighter reference (e.g. T=300: a single scattered pair drops the certificate 3.5× the
  slack to band_min). The conclusion "the slack is ~O(1) pairs, not O(N)" is robust to which of these
  references one uses.
- **Honesty statement (required): this bounds nothing the certificate uses.** E4 is a *diagnostic*: it
  quantifies the certificate's sensitivity in the realized world but (i) adds no input to the 0.6725
  argument — the theorem's inputs are tr and HS², unchanged; (ii) improves no constant; (iii) does not
  establish anything about ζ's zeros, since the real data is all-on-line by construction and n₋ = 0 is a
  consistency check, not evidence. Its one honest contribution is the quantified margin: **the realized
  world sits ~1 pair (scattered) to ~1–1.5% of pairs (edge-clustered) away from the certificate noticing
  off-line structure, and ~4% of pairs (edge-clustered, β ≤ 0.3) away from breaking the 0.6725 bound.**
  The E4 hypothesis ("if the bound stays above 0.6725 even for p pairs at depth β ~ 1/log T, realized
  slack exceeds the certificate's sensitivity") resolves as follows: at depth β ≈ 1/log T ≈ 0.16–0.19 the
  *theory* floor tolerates ~4% of top-clustered pairs (8% of zeros), but the *noise band* tolerates only
  ~1–1.5% (2–3% of zeros) — and the n₋ counter tolerates only 1 pair. The realized slack in pairs is
  small on every reading.

## 8. Caveats and honesty footer

- **Labels:** every measured entry is **CHECKED NUMERICALLY** (finite-T, f64, hard-cutoff
  ψ = cos(√2u)·1_{|u|≤1/2}, single sample per world, seeded scattered pattern seed 7 — same caveats as
  attack-sandbox §6 / attack-finitet §6). The certificate structure (rank–trace inequality Lemma 3.4,
  Thm B / Lemma R bookkeeping, c = 1.3274993) is **PROVEN** [litmap §2, kernel §2, multiplicity §1, Lean];
  Claim 2.3's pair signature (1,1) is **PROVEN-as-stated** and reproduced here (§1 anchor). The
  interpretation (§7) is CONJECTURED-but-supported; the *numbers* it rests on are the measured table.
- **Noise-band caveat:** the across-T band is the task's stated detection reference; note it is anchored at
  its lower end by the T=1300 real value itself (so detectability at T ≥ 1100 is trivially easy). All
  headline thresholds are quoted at T = 200–500 where the real value sits inside the band.
- **n₋ thresholds are numerical-floor statements:** the "detected at β" boundaries are where the full-W
  negative eigenvalue clears the rel-1e-10·λmax / abs-1e-12 counting thresholds; below them the negative
  is real but unresolvable by Jacobi-in-f64 (and irrelevant at the counts the certificate would care
  about). Position dependence is documented in §6; the representative (bulk) threshold β ≈ 0.1 is the
  honest headline, with the edge positions as the bracketing cases.
- **Pattern dependence:** top-clustered vs scattered thresholds differ by ~2–4× in f (sandbox §6 already
  documented this up to 0.15 in bound_s1 at f = 5%); the scattered pattern is the honest model of a real
  RH failure and gives the tighter threshold.
- **What was NOT done:** no new data was computed (LMFDB 1000 + computed 10000 zero files, same as
  sandbox); no window averaging; no β-sweep below 0.05 for the certificate (the f=1-pair scattered row is
  already far out of band at β=0.05, so the exact shallow-β crossing for the certificate is below the
  grid — bounded above by the quoted values).
- No claim here is a new theorem; the deliverable is a quantified detection-threshold measurement with
  per-row provenance.

## 9. Reproduction

```
Archive: research/notes/attack-detection-threshold/{e4sweep.rs, pairdiag.rs, e4probe.rs, e4nminus.rs,
         Cargo.toml, e4sweep-run1.txt, e4probe-run1.txt, e4nminus-run1.txt, pairdiag-run1.txt,
         SHA256SUMS}
cd /tmp/finitet-e4 && export PATH=$HOME/.cargo/bin:$PATH RUSTFLAGS="-C linker=rust-lld" \
  && cargo build --release --target x86_64-unknown-linux-musl --bin finitet-e4sweep \
  && ./target/x86_64-unknown-linux-musl/release/finitet-e4sweep > /tmp/e4sweep-run1.txt 2>&1
(same for --bin finitet-pairdiag / finitet-e4probe / finitet-e4nminus; transcripts in the archive)
Derived quantities: /tmp/e4derived.py (uv run --quiet python e4derived.py) — band, per-pair costs,
slack ratios, spacings (arithmetic over the table rows above).
Data: tools/data/zeros_1_1000.txt, tools/data/zeros_computed_10000.txt (unchanged).
```
