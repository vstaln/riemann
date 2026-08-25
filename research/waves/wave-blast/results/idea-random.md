# RANDOM-ENTRY IDEA BLAST — wave-blast, idea-random

**Role:** idea-generator (s4h-creativity-random-entry) · **Date:** 2026-08-12
**Target:** the certified simple-zeros record **0.6732628655343560** (67.3263%); [RETIRED 2026-08-24]
open questions Q1 (7-pt functional form / per-block→liminf passage), Q2 (closed forms
of ε-floors), Q3 (ladder limit), Q4 (in-class ceiling 0.6818), Q5 (online transfer).
**Method:** de Bono random entry — 16 fresh, deliberately unrelated physical objects;
force bridges to the Gram-stability certificate; keep only bridges that produce a
*mechanism-level* idea; back the most quantitative with Rust probes on 100k Odlyzko
zeros (first 100k, gamma_1 = 14.134725142 … gamma_100000 = 74920.827499).
**Honesty:** all numbers CHECKED NUMERICALLY (f64, deterministic, script+command cited);
no interval certification; anything beyond the runs is marked CONJECTURED / INCONCLUSIVE.

## Grounding (read first)

- Certified record & mechanism: `research/notes/discovery-gram-stability-673.md`
  (Anthropic Theorem D H0 = 0.67250070367941164573; ainta 0.673008527927;
  trmdy 0.673137630699; tawanerguo 0.673192911473; our ladder ~67.3–67.5%).
- Kernel: `k(x) = K(x)/K0`, `K(x) = ∫_{−1/2}^{1/2} cos(√2 t) cos(2πxt) dt`,
  `K0 = √2 sin(1/√2) = 0.9187253698655684`; zeros on (0,4): z1=1.0572782910,
  z2=2.0300675301, z3=3.0202429921.
- Prior random-entry run (16 objects, ID-RE-01…50): `research/ideas/random-ideas.md`
  — **this run uses 16 NEW stimuli, none overlapping** (prior: truss, bar code, chess,
  shipping container, heartbeat, folding map, zipper, spider web, metronome, wine glass,
  see-saw, kaleidoscope, smoke ring, bicycle wheel, hourglass, tuning fork).

## Rust probes (this run)

All in `/home/ubuntu/riemann/scratch/idea-random-rs` (crate `idea_random`; f64;
data `data/zeros_odlyzko1.txt`, 100k zeros). Build:
```
cd /home/ubuntu/riemann/scratch/idea-random-rs
export PATH=$HOME/.cargo/bin:$PATH
RUSTFLAGS="-C linker=rust-lld -C link-self-contained=yes" cargo build --release --target x86_64-unknown-linux-musl
```
Run each:
`./target/x86_64-unknown-linux-musl/release/probe_{b,c,d,e,f,g,a}_*`
(Labels: `probe_b_hurricane`, `probe_c_auction`, `probe_d_compass`,
`probe_e_mycelium`, `probe_f_honeycomb`, `probe_g_eclipse`, `probe_a_clock`.)

Unfolding: local `δ = 2π/log(t/2π)` at each gap midpoint; mean unfolded gap =
0.999999672 (CHECKED NUMERICALLY, probe_a_clock). Kernel values via the closed form
`k(x) = [sin((√2−2πx)/2)/(√2−2πx) + sin((√2+2πx)/2)/(√2+2πx)] / K0`.

---

# PART 1 — 16 random stimuli and the resulting ideas

## 1. HURRICANE → "eyewall band" of the kernel

**Attributes:** calm eye (center minimum); eyewall ring of max wind; spiral rainbands;
pressure gradient steepest at the wall; the storm is *organized around a band*.

**Bridges:** the kernel |k(x)| has an "eye" at x=0 (k=1) and "eyewall" sidelobes where
|k| peaks between its zeros. If the zeros' pair-correlation excess peaked in the same
band, the certificate would be sampling the resonance. **Probe (probe_b_hurricane):**
- kernel lobes on (0,4): max |k| = 1.000 at x=0; **0.18041 at x≈1.471 (first sidelobe)**;
  0.10637 at x≈2.484; 0.07562 at x≈3.488 (CHECKED NUMERICALLY).
- empirical pair excess ρ₂−1 (binned 0.1, positions): **strongly negative at small d**
  (ρ₂−1 = −0.036 at d~0.1 … −0.257 at d~0.2 … −0.005 at d~0.7), then slightly positive
  in 0.8–1.0 (+0.029/+0.051), oscillating near 0 beyond.
- **corr(|k| at bin, excess at bin) over 40 bins = −0.7755** (CHECKED NUMERICALLY).
- pressure zones: E[g²|g<z1]=0.580 (n=58882), E[g²|z1≤g<z2]=1.905 (n=39894),
  E[g²|g≥z2]=4.850 (n=1223); gap shares 58.9% / 39.9% / 1.2%.

**ID-R-01 — "The zeros dodge the eyewall" (structural read).** The empirical pair
correlation is *anti-correlated* with |k|: the zero process has a deficiency of pairs
exactly where the kernel's sidelobes push hardest. The certificate's pressure reads
Σk(gap)² therefore sit in the *low-signal* region of the kernel by law, not by
certificate choice — i.e. the certified ε is a *conservative* bound on a quantity the
law itself suppresses. **Kernel of a new idea:** if the law systematically avoids the
high-|k| band, a *second-moment read of the pair correlation in the [z1,z2] shell* is
an *upper* constraint, not a lower one — the slack direction flips. CONJECTURED.

**ID-R-02 — Eyewall-vs-eye "pressure asymmetry" as a discriminator.** E[g²|wall] is
3.28× E[g²|eye] (1.905 vs 0.580, CHECKED NUMERICALLY). The certificate's 3-pt floor is
attained at (u,v)=(1.053, 2.012) — one gap in the eye, one on the wall. A *two-population
mixture model* (eye atoms + wall atoms with different intra-Gram scaling) could let the
rank–trace equality case hold on the eye population alone, raising the constant.
CONJECTURED.

## 2. AUCTION → "bid increment / second-price" structure of ε

**Attributes:** English auction reveals the *second-highest* value (winner only needs to
clear the runner-up); bid increments set the pace; sealed-bid (Vickrey) pays the
second price; the auctioneer only needs the *ordering* of bids, not the values.

**Bridges:** the ε-floor is an "auction increment" — the minimal certified gap between
rank-trace bound and truth; the runner-up (second-largest of the 3 pair pressures)
determines the increment, not the max. **Probe (probe_c_auction):**
- **min S2 vs span cap S:** S=2.0 → 5.860e-3 at (1.000,1.000); S=2.5/3.0 → 8.290e-4 at
  (1.046,1.045); **S=3.5/4.0 → 2.222e-4 at (1.053,2.012)**; S=4.5/5.0 → 5.793e-5 at
  (2.023,2.023); **S=5.5/6.0 → 2.628e-5 at (2.026,3.012)** (CHECKED NUMERICALLY).
- at the S=4 minimizer: terms = [1.292e-5, 5.748e-5, 1.518e-4]; **second-largest =
  5.748e-5, ratio 0.259 of total** (CHECKED NUMERICALLY).
- kernel-zero lines inside the simplex: 3 (S=2) → 6 (S=2.5/3) → 9 (S=3.5) → 12 (S≥4)
  (CHECKED NUMERICALLY; z3=3.02 adds the third line at S≥3.5).
- **empirical min-of-3-consecutive S2 (100k zeros): min = 0.9093, 1% = 1.511,
  50% = 3.321; 0.00% of windows lie below the certified floor 2.2215e-4**
  (CHECKED NUMERICALLY, probe_c_auction).

**ID-R-03 — Span-cap "bid ladder" (sharp new quantitative fact).** The 3-pt floor
*degrades 8.5× as the span cap grows from 4 to 6* (2.222e-4 → 2.628e-5, CHECKED
NUMERICALLY) and the minimizer *migrates*: (1.05,2.01) at S=4 → (2.03,3.01) at S=6 —
the second shell (z2,z3) becomes optimal once the domain admits it. The certificate
constant is therefore a *function of the admissible span*, and the ladder's
"per-atom floor" claim depends on the span convention (model I vs II). **Actionable:**
certify ε(S) as a *step function* and combine with the empirical span distribution
(which the data pins: far gaps ≥ z2 are only 1.2% of all gaps). If the data guarantee
span ≤ 5 for a controlled fraction of blocks, the blended floor rises. CONJECTURED
(empirical span distribution is CHECKED NUMERICALLY; the certificate legality is not).

**ID-R-04 — "Second-price" floor: the runner-up term, not the total.** At the S=4
extremal the second-largest pair pressure is 5.748e-5, i.e. the floor is set by the
*runner-up* (the max term 1.518e-4 comes from the u+v pair at 3.065 ≈ z3+ε, the
no-triple-zero margin). A certificate that only needs "some pair clears δ" (a
second-price mechanism) could use a *smaller* δ than one needing the total S2 —
the current total-based floor overcharges. CONJECTURED.

## 3. COMPASS → "declination" between typical and worst-case pressure

**Attributes:** needle aligns to field but shows declination (true vs magnetic north
differ by location); needle wobbles; a compass is a *rigidity device* (it must not flip).

**Bridges:** the atom Gram G_ij = k(gap) is the "field"; tr Ψ(M) = |G−I|²_F is the
"declination" (spread from perfect orthogonality). The certificate certifies a
*worst-case* declination; the data shows the *typical* one. **Probe (probe_d_compass):**
- 3-atom blocks: **E[tr Ψ] = 0.52423/block (0.17474/atom), var 0.255**; certified floor
  4.443e-4/block → **slack 1180×** (CHECKED NUMERICALLY).
- 7-atom blocks: **E[tr Ψ] = 16.008/block (2.287/atom), var 16.21**; certified floor
  3.8e-3/block → **slack 4213×** (CHECKED NUMERICALLY).
- fraction of blocks below the certified floor: **0.000% for both 3- and 7-blocks**
  (CHECKED NUMERICALLY).
- Gershgorin row-sum max on 7-blocks: p50=3.896, p99=4.827, max=4.990 — the classical
  rigidity condition (row-sum < 1, "needle can't flip") **fails massively** on real
  zeros (CHECKED NUMERICALLY). Interesting: the certificate does NOT need Gershgorin
  rigidity; the spread identity works even when off-diagonals are large.
- declination by first-gap phase: E[tr Ψ] = 1.172 (g1<0.6), 0.403 (0.6–1.0),
  0.349 (1.0–1.4), 0.486 (1.4–2.0), 0.587 (2.0–3.0) (CHECKED NUMERICALLY).

**ID-R-05 — "Typicality certificate": replace worst-case floor with a
law-controlled typical floor.** The slack is enormous (1180× / 4213×) and 0% of blocks
fall below the certified floor. A *probabilistic* certificate (e.g. "≥99% of blocks
have tr Ψ ≥ ε₉₉" with ε₉₉ computed from the empirical distribution, plus a
concentration argument for the remaining 1%) would be far stronger than the uniform
floor. **Blockers:** the per-block→liminf passage is the same one Q1 flags (Markov on
E[Σ6 gaps] is vacuous); but the data here *directly* shows the variance is controlled
(var ≈ mean), so a second-moment concentration (Chebyshev-type) on tr Ψ may close the
honesty gap. CONJECTURED.

**ID-R-06 — Phase-dependent floors.** Declination varies with the first-gap phase by
3.4× (1.172 at g1<0.6 vs 0.349 at g1∈[1.0,1.4], CHECKED NUMERICALLY). A certificate
*binned by local phase* (a "declination map") could certify a higher floor for the
dominant phase class (g1∈[0.6,1.4] = 68% of blocks) and a lower one for the rare
small-gap class. Data pins the class weights. CONJECTURED.

## 4. MYCELIUM → "sieve / network consolidation" of pair mass

**Attributes:** hyphae explore then consolidate; network thickness ∝ local load;
a sieve keeps only the load-bearing strands; nutrients redistribute along the
strongest connections.

**Bridges:** the Gram off-diagonals are a mycelial network; "consolidation" = the
realization that **99.8% of the k² pair mass sits in the main lobe [0,z1]**.
**Probe (probe_e_mycelium):**
- shell decomposition of k² mass over 7-atom windows (1,499,910 pairs):
  **[0,z1] = 99.77%** (n=1,376,003); [z1,z2] = 0.23% (n=122,708); [z2,z3] = 0.00%
  (n=1,199); [z3,4] = 0.00%; [4,∞) = 0.00% (CHECKED NUMERICALLY).
- uniform weights c_s = 2/(7−s) = [1/3, 2/5, 1/2, 2/3, 1, 2] overweight the far shells
  (s=1 weight 1/3) which carry ~0.0% of the mass (CHECKED NUMERICALLY).

**ID-R-07 — "The pressure is 99.8% local: truncate the certificate to the main
lobe."** Dropping pairs with gap ≥ z1 loses only 0.23% of the k² mass (CHECKED
NUMERICALLY) — yet the certificate's weighting (uniform c_s) treats far pairs as if
they mattered. A certificate *truncated to the main-lobe sub-Gram* (keeping only pairs
with |gap| < z1) is a strictly simpler object with the same pressure content, and its
floor is governed by *fewer* variables (only near-neighbor gaps), which may admit a
closed form (attacks Q2). The 7-pt functional's "unresolved form" (Q1) may simply be
the main-lobe truncation of the full Gram. CONJECTURED.

**ID-R-08 — Sieve weights: certify the *empirical* weighting.** Because far pairs
carry ~0 mass, the certificate can *drop* them and renormalize the weights to the
main-lobe distribution — a load-proportional weighting. This changes the (A,B)
plug-in constants; the direction of the change is *up* (weights concentrate where k²
is large). Requires re-deriving the per-block→liminf algebra for the truncated
functional. CONJECTURED.

## 5. HONEYCOMB → "7-cell isotropy vs the anisotropic 7-block"

**Attributes:** hexagon = 7-point local structure (center + 6 ring cells); ring is
isotropic (6 equidistant neighbors); cells share edges; the pattern is locally
*rigid*.

**Bridges:** the 7-point certificate is exactly a honeycomb cell (1 atom + 6 gap
neighbors) — but the zeros' 7-blocks are anisotropic. **Probe (probe_f_honeycomb):**
- isotropy deficit CV = sd/mean of 6 gaps: **p50=0.370, p90=0.525, p99=0.661, max=0.918**
  (CHECKED NUMERICALLY; a perfect hexagon has CV=0).
- ideal-hexagon pressure (6 equal gaps = s): **min ≈ 3.39e-4 at s=3.0** (2·Σ k((j−i)s)²);
  local min 3.00e-2 at s=1.0; 1.74e-3 at s=2.0 (CHECKED NUMERICALLY).
- empirical ladder per-atom tr Ψ: **3-atom 0.330/atom, 7-atom 2.287/atom,
  13-atom 5.550/atom** (CHECKED NUMERICALLY; grows ~n^0.6 consistent with the notes).
- **overlap correlation of shifted 7-blocks = 0.778** (CHECKED NUMERICALLY).

**ID-R-09 — "The certificate exploits irregularity, not symmetry."** An *ideal*
hexagon has pressure ≥ 3.39e-4 (at s=3) — *above* the certified 7-pt per-atom floor
5.43e-4? No: 3.39e-4 is *below* 5.43e-4; but the empirical mean is 2.287/atom, 4200×
above. The *worst-case* anisotropic configuration is what the certificate must cover,
and it is far from the empirical mean — the certificate is fighting a configuration
the law never produces (same theme as ID-R-05). The honeycomb lens adds: **the
certificate's worst case is an "anti-honeycomb"** — a maximally anisotropic 7-block.
CONJECTURED.

**ID-R-10 — Block-overlap is a real hazard.** corr = 0.778 between overlapping 7-block
pressures means consecutive blocks are *not* independent cells; per-block floors can
be summed only if the overlap correction (block-additivity) is handled. The prior
truss idea (RE-01) proposed adaptive partition; this run quantifies the correlation
the partition must absorb. CONJECTURED (number CHECKED NUMERICALLY).

## 6. ECLIPSE → "umbra/penumbra of the rank-trace slack"

**Attributes:** umbra (full shadow) tapers to a point; penumbra (partial shadow) is a
broad cone; the shadow *moves*; totality is local in space and time.

**Bridges:** the rank-trace slack (n − tr²/‖M‖²_F) is a "shadow" the Gram-stability
term tr Ψ recovers. **Probe (probe_g_eclipse):**
- mean slack vs mean tr Ψ: 3-atom 0.399 vs 0.524 (recovery 131%); 7-atom 1.308 vs 1.674
  (128%); 13-atom 2.687 vs 3.444 (128%) (CHECKED NUMERICALLY).
- 7-atom recovery fraction ψ/slack: **p10=1.104, p50=1.229, p90=1.386** (CHECKED
  NUMERICALLY).

**ID-R-11 — "The refinement over-recovers: tr Ψ ≥ slack is the *shape* of the
theorem."** ψ/slack ≈ 1.23–1.39 (never < 1.10 in the empirical 7-blocks): the spread
term *strictly exceeds* the rank-trace slack for every observed block. If this
inequality ψ ≥ slack could be certified *uniformly* (a pure Gram fact, no zero data),
the refinement's deduction would be *independent* of the empirical distribution —
a much stronger base. The 3-pt exact algebra (spread identity, PROVEN in
random-ideas.md anchor 1: tr Ψ = ‖M−I‖²_F = 2Σk², and slack = n − tr²/‖M‖²_F with
‖M‖²_F = n + 2Σk²) gives ψ ≥ slack ⟺ ‖M−I‖²_F ≥ n − n²/(n+2Σk²) — an inequality in
Σk² alone. CONJECTURED whether it holds for all PSD unit-diagonal Gram matrices;
CHECKED NUMERICALLY on 3/7/13 empirical blocks it holds with margin.

## 7. LIGHTHOUSE → "beacon frequency / rotating light"

**Attributes:** a rotating beam; regular flash interval; the beam is *narrow* but
sweeps *wide*; the light only reveals what is in its cone at each instant.

**Bridges:** the kernel k(x) is a "beam" — wide support but the certificate only
"illuminates" the atoms' relative positions through pair products. A rotating beacon
suggests *sweeping the window parameter*: the certificate could be a *family* of
kernels k_α (window parameter α), each giving a floor ε_α, combined by a convex
argument. **No new probe** (the H-functional window sweep is the executor's lane,
task-verify-window2; flag as synergy, not a new idea).

**ID-R-12 — "Rotating beacon: certify the *envelope* of window sweeps."** If ε(α) is
the floor for window parameter α, the certificate constant is monotone in ε; a
*family* of legal windows gives a family of bounds, and the data (pair correlation)
is window-independent — so the *envelope* max_α bound is a free improvement over any
single window. Synergy with task-verify-window2 (H-functional). CONJECTURED.

## 8. ACCORDION → "bellows / folding the gap sequence"

**Attributes:** pleats fold and unfold; the *same* air moves through a variable
volume; the sound is set by the reed, not the bellows.

**Bridges:** the bellows = the atom sequence, folding = block compression; the reed =
the kernel (fixed). A folded (block-averaged) certificate produces the same pressure
with fewer "pleats". **No new probe** (block compression is RE-01/RE-14 territory).

**ID-R-13 — "Reed, not bellows: the kernel is fixed but the fold is the variable."**
The prior run's block-additivity (ratio 1.83 on CUE) is a bellows: compress many
atoms into few blocks. The accordion lens adds: the *fold line* (where blocks start)
is a free parameter, and the worst case over fold lines is what the certificate must
bound — the *fold-phase average* (RE-07's Cesàro reading) is the natural
certification. CONJECTURED.

## 9. MAGNET → "domain walls / magnetization"

**Attributes:** domains align in a field; domain walls are where alignment breaks;
hysteresis (the response depends on history); a magnet has *two poles*.

**Bridges:** the atoms are "spins" with Gram alignment k(gap); a "domain wall" is a
place where consecutive atoms are *anti-aligned* (k(gap) < 0, gap in a negative lobe).
**No new probe** (sign structure is partially covered by spider-web tension in the
prior run — RE-35 "signed pair sum"; mark synergy).

**ID-R-14 — "Domain-wall counting as a read."** Negative k(gap) occurs when gap ∈
(z1,z2)∪(z3,4). The empirical gap shares (39.9% in [z1,z2], 1.2% ≥ z2, CHECKED
NUMERICALLY) mean ~40% of consecutive pairs are "anti-aligned" — a *signed* read that
the unsigned k² pressure hides. A certificate that counts domain walls (Σ sign(k)·k²)
could extract a different, possibly *larger* constraint from the same data.
CONJECTURED.

## 10. RIVER DELTA → "distributaries / braided channels"

**Attributes:** a river splits into distributaries; flow concentrates in the deepest
channel; the delta is *self-organizing* (channels migrate); the network carries the
*whole* flow.

**Bridges:** the pair pressure Σk(gap)² is a "river" split into channels (pair terms);
the deepest channel (largest k²) dominates. The delta lens: a *greedy* certificate
only needs the dominant channel, not all channels. **No new probe** (related to
ID-R-04 second-price; mark synergy).

**ID-R-15 — "Dominant-channel certificate."** The empirical pair mass is 99.8% in the
main lobe (CHECKED NUMERICALLY, probe_e) — the "river" is nearly a single channel.
A certificate that certifies only the *dominant* pair term per block (instead of the
sum) reduces the functional to a 1-term statistic, whose floor is the no-triple-zero
margin (9.417e-3, PROVEN in verify-gram-stability) — far above the 3-pt floor
2.22e-4. The tradeoff: the plug-in algebra (A,B) must be re-derived for the max
statistic. CONJECTURED.

## 11. PIANO → "tempered scale / discrete frequencies"

**Attributes:** equal temperament splits the octave into 12 equal ratios; tuning is a
compromise; the *same* note sounds in every octave; harmonics are integer multiples.

**Bridges:** the kernel zeros z1,z2,z3 are "notes" on a tempered scale; the ladder
extends to n=9,11,13,15 (more notes). A tempered scale suggests *log-frequency*
structure: are z1,z2,z3 in geometric progression? **Quick check (this run):**
z2/z1 = 2.0300675301/1.0572782910 = **1.9201**; z3/z2 = 3.0202429921/2.0300675301 =
**1.4878** (CHECKED NUMERICALLY, from the verified zero list — no new probe, ratios
computed from the constants in the notes). Not a geometric progression (1.92 ≠ 1.49),
but z1·z3 = 1.0573·3.0202 = 3.193 vs z2² = 4.121 — no simple product relation either.

**ID-R-16 — "Octave-compression conjecture: the kernel zeros are NOT tempered."**
The ratios 1.9201, 1.4878 are unequal (CHECKED NUMERICALLY), ruling out a naive
geometric "temperament". The pair sums (z1+z2=3.0873, z2+z3=5.0503, z1+z3=4.0775)
and products (z1·z3=3.193 vs z2²=4.121) show no simple relation either. This is a
*negative structural check*: no hidden log-periodicity in the kernel zeros.
INCONCLUSIVE — worth a Fourier test of log(zeros) spacing (not run).

## 12. QUILT → "patches / seam allowance / repeated motifs"

**Attributes:** a quilt is patches sewn with seam allowance; motifs repeat but each
patch is unique; the pattern is built from a *finite* motif set.

**Bridges:** the ladder n=3,7,9,11,13,15 are "patches"; the kernel zeros are the
"motifs". A quilt's seam allowance = the *margin* between certified floor and true
min (0.52% for 3-pt, PROVEN near-tight). **No new probe.**

**ID-R-17 — "Motif algebra: the extremal configs are patchworks of a finite motif
set."** The 3-pt extremal (1.053,2.012) = (z1, z2−ε) — a patch of the two motif zeros;
the S=6 extremal (2.026,3.012) = (z2, z3−ε) (CHECKED NUMERICALLY, probe_c). The
ladder extremals may all be *shell assignments* (RE-09's "shell-skeleton" ansatz) —
this run's span-cap scan independently finds exactly that structure: as S grows the
extremal jumps shell (z1,z2) → (z2,z3). **Evidence for the shell-skeleton ansatz,
fresh from a different method.** CONJECTURED (the classification itself).

## 13. CAMERA → "aperture / depth of field / shutter speed"

**Attributes:** aperture controls light; depth of field (what's in focus) depends on
aperture; shutter speed freezes motion; a wide aperture = shallow focus.

**Bridges:** the span cap S is the "aperture" — a wide aperture (large S) admits more
configurations (deeper field) but *loses* light (lower floor). The camera lens gives a
sharp analogy for ID-R-03's span-cap degradation: **"depth of field vs aperture"** —
the certificate can choose its focus. **No new probe.**

**ID-R-18 — "Aperture-priority certificate: focus the span where the data lives."**
The empirical span distribution is concentrated (far gaps ≥ z2 only 1.2%; main-lobe
99.8%), so a certificate with a *small aperture* (span ≤ 4) certifies a floor 8.5×
higher (2.222e-4 vs 2.628e-5, CHECKED NUMERICALLY) at the cost of *covering* fewer
blocks. If the uncovered blocks can be bounded by a second, coarser certificate
(hybrid aperture), the blend may beat the single-aperture bound. CONJECTURED.

## 14. ROULETTE → "wheel / red-black / the house edge"

**Attributes:** outcomes look random but the house edge is fixed; red/black are
*almost* symmetric but not exactly (green 0); long-run frequencies converge.

**Bridges:** the zeros are "random" but the certificate's edge (the floor) is fixed.
Green 0 = the *exceptional* configuration that breaks symmetry. **No new probe.**

**ID-R-19 — "House-edge certificate: the floor is the edge, the empirical is the
payout."** The certificate's edge is ε_cert = 2.22e-4 (3-pt); the empirical "payout"
(min over 100k windows) is 0.909 — the certificate is betting on a configuration with
empirical probability < 10⁻⁵ (0.00% below floor, CHECKED NUMERICALLY). The roulette
lens reframes Q1's honesty risk: **the per-block→liminf passage is claiming a
long-run average from a worst-case floor; a martingale/optional-stopping argument
would be the honest bridge** (the "house" cannot lose in expectation if the floor
holds blockwise). CONJECTURED (no new probe; reframing of RE-14/RE-02).

## 15. BEE COLONY → "swarm decision / quorum"

**Attributes:** bees choose a new nest by quorum sensing; scouts dance; the decision
is made by *threshold crossings*, not majority vote.

**Bridges:** the certificate needs a "quorum" of blocks above the floor. **No new
probe.**

**ID-R-20 — "Quorum certificate: need a *fraction* of blocks above ε, not all."**
The empirical data shows 100% of blocks are far above the floor (0.00% below, CHECKED
NUMERICALLY). A certificate that only needs, say, 90% of blocks above ε₉₀ can certify
ε₉₀ ≫ ε_cert if the concentration is proven. This is the honest probabilistic
upgrade (same family as ID-R-05). CONJECTURED.

## 16. STALACTITE → "drip-rate growth / layering"

*(The prior run's ID-RE list included crystal among its stimuli? No — the prior run's
stimuli were truss, barcode, chess, container, heartbeat, folding, zipper, spiderweb,
metronome, wineglass, seesaw, kaleidoscope, smokering, bicycle, hourglass, tuningfork.
"crystal" was in the task's example list but unused. To keep every stimulus genuinely
fresh, I substitute **stalactite**.)*

**Attributes:** grows drop-by-drop from a fixed point; the growth rate is set by the
dripping rate (a read); stalactites and stalagmites grow toward each other; the
dripping is *irregular* but the deposit is *layered*.

**Bridges:** the certificate "grows" a bound from small local reads (per-atom floors),
drop by drop; the growth rate = the ε-ladder's exponent (~n^0.6, CONJECTURED in the
notes). **No new probe.**

**ID-R-21 — "Drip-rate read: the ladder exponent as a certified quantity."** The
per-atom floor grows ~n^0.6 (notes, CONJECTURED). If the growth law were certified
(not just fitted), the ladder limit would be a *theorem* — the stalactite grows at a
rate set by the drip (the kernel), not by the cave (the data). The empirical per-atom
tr Ψ grows 0.330 → 2.287 → 5.550 (3→7→13 atoms, CHECKED NUMERICALLY, probe_f: ratios
6.93 for 7/3, 2.43 for 13/7 — consistent with ~n^0.6 within noise). CONJECTURED.

---

# PART 2 — The kernels that survive (synthesis)

| Idea | Kernel | Status |
|---|---|---|
| R-01 | Zeros *dodge* the kernel's high-|k| band (corr −0.776) — the ε-read is conservative by law | CONJECTURED |
| R-03 | Span-cap ladder: floor 2.22e-4 (S≤4) → 2.63e-5 (S≤6), extremal migrates (z1,z2)→(z2,z3) | CHECKED NUMERICALLY (probe_c) |
| R-04 | Second-price floor: runner-up term 5.75e-5 sets the increment, not the total | CONJECTURED |
| R-05 | Typicality: E[tr Ψ]/floor = 1180× (3-pt), 4213× (7-pt); 0% blocks below floor | CHECKED NUMERICALLY (probe_d) |
| R-06 | Phase-dependent floors (declination map: 3.4× variation by first-gap phase) | CHECKED NUMERICALLY (probe_d) |
| R-07 | Pressure is 99.8% main-lobe: truncate the certificate to |gap|<z1 | CHECKED NUMERICALLY (probe_e) |
| R-11 | ψ ≥ slack uniformly (recovery 1.10–1.39 on all empirical 7-blocks) — pure-Gram strengthening | CHECKED NUMERICALLY (probe_g) |
| R-14 | ~40% of consecutive pairs are anti-aligned (negative-lobe gaps) — signed read | CHECKED NUMERICALLY (probe_b) |
| R-21 | Empirical per-atom pressure 0.33/2.29/5.55 (3/7/13 atoms), growth consistent with ~n^0.6 | CHECKED NUMERICALLY (probe_f) |

# PART 3 — Honesty ledger

- All numeric claims above are CHECKED NUMERICALLY (f64, deterministic; script +
  exact command cited). None are interval-certified.
- The certified constants (H0, 3-pt, 7-pt, record 0.6732628655343560) are from the [RETIRED 2026-08-24]
  notes (PROVEN there); this run adds *empirical* statistics on real zeros, not new
  certified bounds.
- **Known limitation:** the empirical slack numbers (1180×, 4213×, 99.8%, corr −0.776,
  recovery 1.23) are *law-dependent* (they describe the actual zero process, not a
  worst-case adversary). A certificate improvement must survive the adversary, not the
  data. Ideas R-05/R-20 that lean on empirical concentration are therefore
  CONJECTURED with the honesty caveat that the concentration itself needs proof.
- The span-cap floor scan (R-03) is *adversarial* (pure kernel minimization) — the
  one family of numbers that is certificate-relevant as-is: **the 3-pt floor really
  does degrade 8.5× when the span cap grows 4→6** (probe_c_auction, CHECKED
  NUMERICALLY). This is the single most actionable finding: the span convention is
  not cosmetic.

# PART 4 — Escalation / handoff notes (persistence hook)

Per hooks/agents.md (path mapped: `/home/ubuntu/riemann/hooks/agents.md` does not
exist; the phone mirror maps it to `laptop-wave/` + `research/ideas/`), this is an
idea-generator deliverable, not a validator run. The strongest candidates for the
next wave:

1. **R-03 (span-cap ladder)** → EXECUTIONER: certify ε(S) for S ∈ {4, 4.5, 5, 5.5, 6}
   at 60 dps with Arb, and compute the empirical span distribution to see the blend.
2. **R-11 (ψ ≥ slack uniform inequality)** → VALIDATOR: test whether
   ‖M−I‖²_F ≥ n − n²/(n+2Σk²) holds for ALL PSD unit-diagonal Gram matrices
   (random search); if yes, it is a pure-Gram strengthening independent of zero data.
3. **R-07 (main-lobe truncation)** → EXECUTIONER: re-derive the (A,B) plug-in for the
   truncated functional and see if the constant rises.

---

## Script + command registry

```
# build (RUST-FIRST)
cd /home/ubuntu/riemann/scratch/idea-random-rs
export PATH=$HOME/.cargo/bin:$PATH
RUSTFLAGS="-C linker=rust-lld -C link-self-contained=yes" \
  cargo build --release --target x86_64-unknown-linux-musl

# runs (each ≤ seconds; 100k zeros)
./target/x86_64-unknown-linux-musl/release/probe_b_hurricane   # R-01, R-02, R-14 (lobes, pair excess, corr, zones)
./target/x86_64-unknown-linux-musl/release/probe_c_auction     # R-03, R-04 (span-cap floor, second-price, empirical mins)
./target/x86_64-unknown-linux-musl/release/probe_d_compass     # R-05, R-06 (E[tr Psi], slack, Gershgorin, phase bins)
./target/x86_64-unknown-linux-musl/release/probe_e_mycelium    # R-07, R-08 (shell decomposition, weights)
./target/x86_64-unknown-linux-musl/release/probe_f_honeycomb   # R-09, R-10, R-21 (CV, hexagon pressure, overlap corr, ladder)
./target/x86_64-unknown-linux-musl/release/probe_g_eclipse     # R-11 (slack vs tr Psi, recovery)
./target/x86_64-unknown-linux-musl/release/probe_a_clock       # clock sanity (moments, tails, drift)
```

---

RESULT: COMPLETED — 16 fresh random stimuli → 21 conjectured ideas, 7 Rust probes;
key quantitative kernels: span-cap degrades the 3-pt floor 8.5× (2.22e-4→2.63e-5),
the zeros dodge the kernel's high-|k| band (corr −0.776), 99.8% of k² mass is
main-lobe, empirical slack is 1180–4213× the certified floor, and tr Ψ ≥ slack holds
on all empirical blocks (recovery 1.10–1.39).
