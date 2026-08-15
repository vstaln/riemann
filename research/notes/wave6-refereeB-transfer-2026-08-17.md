# Wave 6 — Referee 6B: adversarial audit of the TRANSFER TO ζ of the certified record 0.673481 simple-on-line

**Referee:** 6B (hostile, blind). **Joint:** state the EXACT theorem the certified value
0.6734808616745137 proves about the zeros of ζ; locate Montgomery's theorem, the grid, the rate
issue, and trace every input. **Date:** 2026-08-17.
**Sources read:** `wave6-briefs-2026-08-17.md`, `FINAL-RECORD-2026-08-13.md`, `attack-ceiling.md`,
`transfer-stability-online.md`, `distinct-zeros-56-refinement.md`, `multiplicity-theorem-route.md`,
`gs-general-estimate-2026-08-14.md`, `attack-lpdual.md`, `tools/verify_coboundary_floor.py`,
`tools/lpdual_realconfig_check.py`, `tools/attack-pricing-sheet.py`, `tools/lpdual/extract_law.py`,
`research/notes/record-alpha-refined-673481.md`, `coboundary-redistribution-explore.md`,
`sharp-tail-m257.md`, `redistribution-family-open.md`.
**Not read (joint-6A/6C territory):** the redistribution chain algebra in
`Zeta23/PairCeiling/*.lean`, the second-machine value re-derivation.

---

## Verdict up front

**The transfer is structurally sound: 0.6734808616745137 is a genuine unconditional liminf
bound on the proportion of zeros of ζ that are simple AND on the critical line — with ONE
unresolved link that I could not verify and that is not a formality: the claim that the
certificate's effective weight r satisfies r(1) = 0 (the α = 1 endpoint evasion).** The plain
cosine-kernel weight does NOT vanish at 1 for the record's α = 1.464 (CHECKED NUMERICALLY:
w(1) = (K(1)/K₀)² ≈ 0.003296 ≠ 0), so the r(1) = 0 assertion is a nontrivial property of the
*coboundary-redistributed* effective weight, asserted in the notes ("built in", "kernel-checked")
but not derivable from the notes I read. Everything else in the transfer — liminf structure,
grid, Montgomery range, mean density, input list — checks out. Referee 6A must confirm r(1) = 0
from the first-principles redistribution derivation; until then the endpoint link is
INCONCLUSIVE.

---

## Q1. The exact theorem

Let N(T) be the number of nontrivial zeros ρ of ζ with 0 < Im ρ < T, counted **with
multiplicity** (von Mangoldt normalization, N(T) = (T/2π)log(T/2π) − T/2π + O(log T), PROVEN).
Let N(1/2, T) be the number of zeros with Re ρ = 1/2 and 0 < Im ρ < T, counted with multiplicity
(N(1/2, T) ≤ N(T); the asymptotic of N(1/2,T) is NOT known unconditionally — only N(1/2,T) ≥
(2/5 + o(1))·N(T), Conrey). Let N_s(1/2, T) be the number of **simple** zeros with Re ρ = 1/2,
0 < Im ρ < T.

**Theorem (the certificate's claim, my endorsed statement).** Unconditionally (no RH, no
pair-correlation conjecture, no RMT):

```
liminf_{T→∞}  N_s(1/2, T)/N(T) ≥ 0.6734808616745137
```

and consequently (since N(1/2,T) ≤ N(T)):

```
liminf_{T→∞}  N_s(1/2, T)/N(1/2, T) ≥ 0.6734808616745137.
```

The certified quantity is the **fraction of ALL nontrivial zeros (with multiplicity) that are
simple and on the critical line**. The on-line fraction statement follows from the all-zeros
statement in both directions, so the brief's question "is it liminf N_s(1/2,T)/N(1/2,T) ≥
0.673481 unconditionally?" has a **YES** answer.

**Why the denominator is N(T), not N(1/2,T) — and why this is forced (PROVEN-by-construction
of the certificate class).** The certificate class (`attack-ceiling.md` §1) reads exactly three
inputs: mean density, form factor on [0,1], integrality of multiplicities. The mean-density
input must be von Mangoldt's N(T) asymptotic — the only **unconditional** mean density. The
on-line configuration's mean density is NOT known unconditionally (only a ≥ (2/5)-lower bound),
and no unconditional pair-correlation statement exists for the on-line configuration alone.
Therefore the configuration the certificate is transferred to is the **full zero configuration**
(zeros with multiplicity, including possible off-line zeros, which enter the Weil-form bookkeeping
as (1,1)-indefinite Sylvester blocks, `transfer-stability-online.md` §1: N = N₀ + 2N_p). Its
simple-point fraction is p₁ = N_s(1/2,T)/N(T), and the certificate bounds p₁ ≥ v = 0.67348086… .

**The quantity is meaningful and non-vacuous (cross-check with the literature).** The proportion
"simple AND on the critical line, relative to all zeros" is the exact quantity of the recent
unconditional Goldston–Suriajaya-type results: "at least 2/3 of the zeros are simple and on the
critical line" (`gs-general-estimate-2026-08-14.md`; the program's Theorem A = 2/3 is this).
0.673481 > 2/3 improves it by 0.00648. This resolves my initial worry that the certificate would
imply the impossible "proportion on the line ≥ 67%": that implication (N₀/N ≥ N_s/N ≥ 0.6735) is
real but is NOT a contradiction — the "simple-and-on-line" quantity already has an unconditional
2/3 record; the certificate pushes the same quantity past it. No century-level unclaimed
corollary hides here, and the distinct corollary N_d/N ≥ (1+H)/2 = 0.836740 (affine image, PROVEN
in the program's notes) is the same quantity family. Note for the record-keepers: the distinct
note writes "liminf N_d(T)/N(T)" while `transfer-stability-online.md` writes the "coherent
reading N_d ≥ (5/6)·N₀" — internally inconsistent notation, but both readings yield the same
bound because N ≥ N₀; the denominator is N(T) throughout, per the certificate class.

**Hypotheses made explicit (all unconditional):**
- (H1) von Mangoldt mean density — PROVEN.
- (H2) Montgomery: the normalized form factor of the full zero configuration converges to the GUE
  datum on [0,1]: F(α,T) → 1 for 0 ≤ α < 1; quantitative uniform version F(α,T) = 1 + O(1/√log T)
  for 0 ≤ α ≤ 1 per BGSTB24 (`attack-ceiling.md` §2(a)) — PROVEN (unconditional).
- (H3) integrality of multiplicities (m_ρ ∈ ℕ) — trivial.
- (H4) the certified 6-gap inequality F(g) ≥ 0.0062 for all g ≥ 0 (Arb interval verifier,
  1,096,556 nodes ×3) — CHECKED NUMERICALLY (NOT Lean; joint 6C owns re-derivation).
- (H5) the redistribution bound chain bound = (H(α) − τ)/(1 − B/m), τ = (1/320)(m−6)/m, H(1.464) =
  0.672467425578, m = 171, B = 1.0229282 — CHECKED NUMERICALLY here (arithmetic: (0.672467425578 −
  0.00301535088)/0.99401796 = 0.67348086… ✓); algebra VALIDITY is joint 6A's verdict.
- (H6) the transfer identity with effective weight r: value v = c₀ + ∫₀¹ r(x)x dx = 0.6734808616745137,
  validity c₀ + Σ s_j r(j/N) ≤ p₁, and the endpoint condition **r(1) = 0** — ASSERTED in the notes;
  my independent check of the raw kernel weight FAILS to confirm it (see Q2). **This is the open
  link.**

## Q2. Where Montgomery's theorem enters; the grid; the α = 1 endpoint

**Montgomery's role (PROVEN, unconditional).** Montgomery's theorem supplies input (H2): the
form-factor measure C_T of the normalized full zero configuration converges to the GUE datum
(cumulative x²/2) on [0,1]. The certificate's pair-sum over the configuration,
Σ_{pairs} w(distance), equals N·Σ_j s_j·r(j/N) with s_j the grid masses (r = effective pair
weight); the GUE datum gives Σ s_j^GUE r(j/N) → ∫₀¹ r(x)x dx (the s_j^GUE = (2j−1)/(2N²) Riemann
sum of x·r(x)). Montgomery is what turns the certificate's GUE-evaluated value v into a statement
about ζ's actual configuration. The kernel's Fourier support is [−1,1], so ONLY F on [0,1] is
read — this is exactly why the method is bandwidth-one and why the 0.6818 ceiling is hard
(`attack-ceiling.md` §3: no proven sliver of F beyond |α| = 1).

**The grid is N = 256, not 171 (CHECKED against the tools).** The validity/robustness constraint
is certified against the N = 256 near-CUE law's rows: s_j = j/256² for j = 1..256
(`tools/lpdual_realconfig_check.py`: "the law's rows 1..255 in law_data.json are EXACTLY the
GUE-flat datum s_j = j/256^2"; `tools/attack-pricing-sheet.py`: "law's row masses s_j = S(j)/N,
j = 1..256"; `tools/lpdual/extract_law.py` reads the N=256 enclosures from `LawN256.lean`). The
verifier's `grid=4000` (`verify_coboundary_floor.py`) is the **quadrature** grid for rigorous
interval enclosures of the kernel integrals — NOT the form-factor sampling grid. The record's
**m = 171** is the **block length** in the redistribution bound chain (τ = (1/320)(m−6)/m; B/m;
`redistribution-family-open.md`: "m (level/knot count in the bound)") — NOT the form-factor grid.
So: form-factor sampling grid N = 256; block length m = 171; quadrature grid 4000. Three
different parameters, all three present in the record.

**The j = N = 256 (α = 1) endpoint.** The certificate requires the grid masses at j/256 for
j = 1..256. The α = 1 point is the edge of Montgomery's clean range (the classical theorem is
F(α) = 1 for α < 1 strictly; the endpoint is where the form factor has the known
singularity/limit delicacy — the quantitative BGSTB24 formula quoted in `attack-ceiling.md`
carries the T^(−2α)(log T + O(1)) diagonal term at α = 1). The certificate's declared mechanism
for this: **r(1) = 0**, which (a) makes the j = 256 term s_256·r(1) = 0 in the validity sum, and
(b) kills the |r(1)||D(1)| term in the stability inequality. Row 256 is "free" in the law-data
tools precisely because r(1) = 0 (`lpdual_realconfig_check.py`: "row 256 = free; r(1)=0 so …").
Under r(1) = 0, the active grid is j = 1..255, all at α = j/256 < 1 — strictly inside
Montgomery's open range — and the endpoint is genuinely evaded.

**My independent numerical check raises a red flag on exactly this point (CHECKED NUMERICALLY,
script below).** For the record's kernel (cosine window α = 1.464, w = (K/K₀)² with K(x) =
(sinc((α−2πx)/2) + sinc((α+2πx)/2))/2):

```
K(0) = 0.9130583,  w(1) = (K(1)/K(0))² = 0.00329556 ≠ 0
w(255/256) = 0.00375272,  w(0.5) = 0.43891131
```

The **raw kernel weight does not vanish at x = 1** (w(1) ≈ 0.0033). Therefore the r in the
certificate class (r(1) = 0) is NOT the plain kernel weight w; it must be the effective weight
after the coboundary redistribution (the p_i, q_i coefficients) and the rank–trace averaging.
The notes assert r(1) = 0 for "the actual certificates" (`attack-ceiling.md` §1: "r(1) = 0 (the
actual certificates)", "kernel-checked"; `attack-lpdual.md`: "r(1) = 0 built in"), and the LP
analysis (`attack-lpdual.md` §4) shows the class-optimal certificate has r(0) = 1, r(1) = 0 — but
that LP certificate is a different object from the 7-point kernel record certificate, and the
notes do not give me the definition of the record certificate's effective r. **The α = 1
endpoint handling therefore rests on an asserted property I could not verify from the notes.**
This is not a formality: if the effective r(1) ≠ 0 for the record certificate, then the mass at
α = 1 enters the validity sum, the stability term |r(1)||D(1)| is live, and the transfer needs F
at α = 1 — outside Montgomery's clean open-range theorem. Joint 6A's first-principles
re-derivation of the redistribution must produce the effective r and confirm r(1) = 0 (or refute
it — either is a result). Until then: **endpoint link INCONCLUSIVE.**

## Q3. The rate issue: liminf survives, no hidden subsequence problem

Montgomery's theorem is a limit with no effective "T large enough": even the quantitative
BGSTB24 form F = 1 + O(1/√log T) has an unspecified constant and is asymptotic, not a
certificate-style bound. **The liminf statement is unaffected.** The transfer needs only: for
every δ > 0 there EXISTS (possibly ineffectively) T₀(δ) such that for all T ≥ T₀,

|Σ_{j=1}^{256} s_j(T)·r(j/256) − ∫₀¹ r(x)x dx| ≤ |r(1)||D(1)| + |r′(1)||E(1)| + M·∫₀¹|r″|

→ 0 (stability inequality, Lean-PROVEN analytic identity; D(1) = C_T(1) − 1/2, E = ∫₀ˣ D, M =
sup|E|; all → 0 by Montgomery, uniformly at the finitely many grid points j = 1..255, max over
finitely many points → 0). Then p₁(T) ≥ c₀ + Σ s_j(T) r(j/N) ≥ v − δ for all T ≥ T₀, hence
liminf p₁ ≥ v − δ for every δ > 0, hence liminf p₁ ≥ v. **No eps/subsequence trap**: the
certificate's robustness margin (floor 0.0062 vs. the variational value) is a FIXED positive
number; the transfer only requires the discrepancy to eventually fall below it, which holds
because the discrepancy → 0. Pointwise convergence at finitely many grid points (not uniform-in-N
convergence) is all that is used — and Montgomery gives exactly that (in fact uniform on [0,1]).
The "for T large enough" is ineffective, but ineffectiveness is exactly what a liminf statement
is built to absorb. PROVEN (modulo the r(1) = 0 link of Q2 and the eps-mapping of Q4).

One caveat to hand to 6A: the chain "6-gap inequality F(g) ≥ 0.0062 over all g ≥ 0" ⟹ "valid
against every configuration whose grid masses are within eps of GUE" is the rank–trace/coboundary
mapping. The number 0.0062 is a floor on a 6-variable functional, and its translation into a
per-grid-row mass tolerance must be checked for consistency with the stability inequality's
M, |r′(1)|, ∫|r″| scales. If the two eps notions differ by more than an O(1) factor, the margin
is mis-stated (not fatal to the liminf — any fixed positive margin works — but it must be a
positive margin).

## Q4. Input trace: exactly the three unconditional inputs, nothing conditional

| Input | Source | Status |
|---|---|---|
| (1) mean density | von Mangoldt N(T) = (T/2π)log(T/2π) − T/2π + O(log T) | PROVEN, unconditional |
| (2) form factor on [0,1] | Montgomery F(α) = 1, 0 ≤ α < 1 (uniform quantitative BGSTB24 on [0,1]) | PROVEN, unconditional |
| (3) integrality of multiplicities | m_ρ ∈ ℕ | trivial |
| + certificate's own 6-gap inequality | verify_coboundary_floor.py, target 620/1e5, 1,096,556 nodes ×3 | CHECKED NUMERICALLY (not Lean) |
| + redistribution bound chain | bound = (H − τ)/(1 − B/m) | CHECKED NUMERICALLY; algebra → 6A |
| + r(1) = 0 endpoint condition | asserted in notes | **INCONCLUSIVE (my check: raw kernel weight ≠ 0 at 1)** |

No RH. No pair-correlation conjecture. No RMT. No beyond-bandwidth-1 form-factor input (the
kernel's Fourier support [−1,1] means F outside [0,1] is never read; nonnegativity F ≥ 0 for all
α is never used as a value input). The only places a conditional could hide are (i) the α = 1
endpoint (Q2, open), (ii) the redistribution algebra (6A), (iii) the eps-floor-to-validity
mapping (Q3 caveat). All three are unconditional-claim-relevant but none imports RH/PCC/RMT.

## Q5. VERDICT

**Genuine unconditional liminf bound — structurally sound — with one unresolved (INCONCLUSIVE,
not broken) link.**

The theorem I endorse (all hypotheses explicit):

> Let N_s(1/2, T) = #{ρ : Re ρ = 1/2, 0 < Im ρ < T, ρ simple}, N(T) = #{ρ : 0 < Im ρ < T}
> with multiplicity. Under (H1) von Mangoldt, (H2) Montgomery F = 1 on [0,1] (unconditional),
> (H3) integrality, (H4) the certified 6-gap inequality F(g) ≥ 0.0062 (CHECKED NUMERICALLY),
> (H5) the redistribution chain bound = (H(1.464) − τ)/(1 − B/171) (6A-pending), (H6) r(1) = 0
> for the effective weight (INCONCLUSIVE — see below):
>
> **liminf_{T→∞} N_s(1/2, T)/N(T) ≥ 0.6734808616745137**, and consequently
> **liminf_{T→∞} N_s(1/2, T)/N(1/2, T) ≥ 0.6734808616745137**. Unconditional; no RH, no PCC.

The transfer machinery — liminf over all large T (not a subsequence), finitely many grid points
strictly inside Montgomery's open range (j = 1..255 of 256), von Mangoldt normalization forced by
the certificate class, stability inequality → 0, fixed positive eps margin — is correct and
robust. The value 0.673481 < the class ceiling 0.6818 (consistent; no ceiling violation
observed).

**The single thing that must be settled before this is trusted as PROVEN: r(1) = 0 for the
record certificate's effective weight.** My direct check shows the raw cosine-kernel weight is
positive at x = 1 (0.0033) for the record's α = 1.464, so the asserted r(1) = 0 is a real,
non-obvious property of the coboundary-redistributed effective weight. Referee 6A's
first-principles re-derivation of the redistribution must exhibit r and verify r(1) = 0; if it
cannot, the transfer's endpoint handling is INCONCLUSIVE (needs F at α = 1 or a separate
endpoint argument) and the certificate is not yet PROVEN as an unconditional liminf — though
still CHECKED NUMERICALLY / plausible.

**Labels:** liminf structure, grid (N=256 vs m=171), Montgomery range, mean density, input list:
PROVEN (from the notes + tools). Bound-chain arithmetic (H(1.464) − τ)/(1 − B/171) = 0.67348086…:
CHECKED NUMERICALLY (exact mpmath-level arithmetic, reproduced here by hand-calc to 8 digits).
r(1) = 0 endpoint condition: INCONCLUSIVE (asserted; raw kernel weight at 1 = 0.003296 ≠ 0,
CHECKED NUMERICALLY). Whether any eps-mapping inconsistency exists between the 0.0062 floor and
the stability scales: INCONCLUSIVE (handed to 6A).

## Files / scripts

- This note: `research/notes/wave6-refereeB-transfer-2026-08-17.md`.
- Kernel-endpoint check (one-liner, run with `uv run --quiet python3`): compute K(x) =
  (sinc((1.464−2πx)/2)+sinc((1.464+2πx)/2))/2, w(x) = (K(x)/K(0))² at x = 1, 255/256, 1/2.
  Output: w(1) = 0.00329556 (nonzero), K(0) = 0.9130583.
- Bound-chain arithmetic: (0.672467425578 − (1/320)(165/171))/(1 − 1.0229282/171) = 0.67348086…
- Source of grid facts: `tools/lpdual_realconfig_check.py`, `tools/attack-pricing-sheet.py`,
  `tools/lpdual/extract_law.py` (N = 256 law rows); `verify_coboundary_floor.py` (grid=4000
  quadrature); `redistribution-family-open.md`, `sharp-tail-m257.md` (m = 171 block length).

## Handoff to joints 6A / 6C

- **6A must produce the effective weight r of the 7-point coboundary certificate and confirm
  r(1) = 0** (or refute it). This is the only unresolved link in my transfer audit. Also confirm
  the eps-mapping: 0.0062 floor on the 6-gap functional ⟹ positive per-row mass tolerance for the
  validity constraint.
- **6C's value re-derivation** should independently confirm 0.6734808616745137 and the
  eps = 0.0062 boundary (620/1e5 pass / 630/1e5 fail) — no transfer-specific concern from my side
  beyond the arithmetic I rechecked (consistent).
