# COBOUNDARY REDISTRIBUTION EXPLORER — α-transfer and re-optimization report

**Date:** 2026-08-13 (round 4, late-night continuation). **Agent:** EXPLORER.
**Status:** NEW RECORD — α-transfer of tawanerguo's coboundary redistribution beats tawanerguo.
Labels: PROVEN (interval-certified) / CHECKED NUMERICALLY (script+command) / CONJECTURED / ABANDONED.

## Headline (PROVEN)

Keeping tawanerguo's redistribution coefficients UNCHANGED but shifting the cosine window
α=1.47 → **α=1.49 certifies F_B ≥ 620/1e5** (eps=0.0062, interval verifier, 826,548 nodes) at
psum=1/320. This yields bound **0.6734350481349153** (m=171), beating tawanerguo's 0.6731929114731422
by **+2.42e-4**. At α=√2, eps=0.0060 certifies (739,794 nodes) → **0.6733846160683801** (m=176),
+1.92e-4. Both confirmed by the orchestrator with independent runs matching exactly.

## 1. Reproduced baseline (CHECKED NUMERICALLY)

`uv run --with mpmath --with python-flint python tools/verify_coboundary_floor.py`
- ainta sanity (uniform 7-pt MT, p=1/3000, target 19/5000): verified=True, 707,901 nodes.
- **tawan baseline (cosine 1.47, coboundary, target 577/1e5): verified=True, 209,236 nodes**
  (repo's own C++ verifier records 1,126,636 nodes; our Python re-implementation certifies the
  same target — reproduced).
- Bound arithmetic replicated to 29 digits: 0.67319291147314225351 via
  `uv run --quiet --with mpmath python /tmp/coboundary_bound.py`.
  tau = psum·(m−6)/m = (1/320)(177/183) = 59/19520 exactly (the tawan "pressure tax").

## 2. What the redistribution IS (PROVEN, decoded)

`uv run --quiet --with mpmath python /tmp/decode_U.py` reproduces tawan's p,q from the paper's U
(riemann.tex eq. coboundary) to 10+ digits:

```
F_B(g1..g6) = F_0 + U(g2..g6) − U(g1..g5)
U(g1..g5)   = (54g1 −123g2 +123g4 −54g5)/1920000
            + (5971/300000)(w(g1)+w(g2)−w(g4)−w(g5))
```

With l = (54,−123,0,123,−54)/1920000 and c = (5971,5971,0,−5971,−5971)/300000:

```
p_i = p0 + (l_{i−1} − l_i),  p0 = 1/1920   (l_0 = l_6 = 0)
q_i = 1/3 + (c_{i−1} − c_i), q0 = 1/3
p = (946,1177,877,877,1177,946)/1920000,  sum p = 1/320
q = (31343/1e5, 1/3, 105971/3e5, 105971/3e5, 1/3, 31343/1e5),  sum q = 2
```

The coboundary is a TELESCOPING correction: U(g2..g6)−U(g1..g5) shifts pressure and
nearest-neighbor w-mass between gaps while preserving global sums, so on periodic sequences the
infinite functional density is unchanged. The 10 free parameters are (l_1..l_5, c_1..c_5).

## 3. α-transfer table (PROVEN unless noted; interval verifier, grid=4000)

tawan's p,q held fixed; cap_scheme='coboundary'. Commands:
`/tmp/coboundary_decisive.py`, `/tmp/coboundary_high.py`, `/tmp/confirm_records.py`.

| α | target (eps) | verified | nodes | status | bound (best m) |
|---|---|---|---|---|---|
| 1.47 | 577/1e5 (0.00577) | **True** | 209,236 | ok | 0.6731929 (m=183) [tawan] |
| 1.49 | 577/1e5 | True | 189,136 | ok | — |
| 1.49 | 590/1e5 (0.0059) | True | 294,242 | ok | 0.6732404 (m=179) |
| 1.49 | 600/1e5 | True | 400,986 | ok | 0.6733053 (m=176) |
| 1.49 | 610/1e5 | True | 562,640 | ok | 0.6733702 (m=174) |
| 1.49 | **620/1e5 (0.0062)** | **True** | 826,548 | ok | **0.6734350 (m=171) — RECORD** |
| 1.49 | 630/1e5 | False | 214,843 | terminal-cell | — |
| 1.49 | 640/1e5 | False | 314,853 | terminal-cell | — |
| √2 | 577/1e5 | True | 307,314 | ok | — |
| √2 | 590/1e5 | True | 509,944 | ok | 0.6733197 (m=179) |
| √2 | **600/1e5 (0.0060)** | **True** | 739,794 | ok | **0.6733846 (m=176)** |
| √2 | 610/1e5 | False | 154,788 | terminal-cell | — |
| √2 | 620/1e5 | False | 230,943 | terminal-cell | — |

Max certifiable eps: α=1.49 ∈ (0.0062, 0.0063]; α=√2 ∈ (0.0060, 0.0061].
Both records re-confirmed by the orchestrator independently (620/1e5 @1.49: 826,548 nodes — exact
match; 600/1e5 @√2: 739,794 nodes — exact match).

## 4. Crystal-floor float probe (NON-RIGOROUS reconnaissance)

`uv run --quiet --with mpmath --with python-flint --with numpy --with scipy python /tmp/crystal_floor.py`
Float floor of F_B over period-2/3 crystals (tawan's U):

| α | period-2 floor | crystal (a,b) | period-3 floor @1.47 |
|---|---|---|---|
| 1.47 | 0.006465 | (1.049, 1.985) | 0.006299 (g≈(1.996,1.051,1.996)) |
| 1.49 | 0.006557 | (1.051, 1.984) | — |
| √2 | 0.006225 | (1.045, 1.986) | — |

Interpretation: tawan's certified target 577/1e5 is far below the true floor (~0.0063–0.0066);
the α=1.49 shift raises the crystal floor, which is why eps=0.0062 certifies. These floats are NOT
certified; the interval verifier is the ground truth (Section 3).

## 5. Re-optimization of the redistribution (CONJECTURED → ABANDONED as better-than-tawan)

F_B(g;l,c) is LINEAR in (l,c), so max-min over adverse configs is a linear program.
`/tmp/redistrib_fast.py`, `/tmp/lp_ppos.py`, `/tmp/reoptimize_full.py` (scipy linprog, HiGHS).

- Small-gap-only config set (period-2/3 crystals): LP max-min v≈0.013, dense floor 0.008 — looked
  better than tawan (0.0065). **BUT interval certification FAILED**: 700/1e5 → False in 6s;
  even 600/1e5 → False (4,920 nodes). Root cause: LP concentrated pressure on gap 3
  (p_3≈0.00276, 88% of total) and pushed c to the ±0.06 bound; configurations with a HUGE gap
  elsewhere (which the verifier's one-body pruning explores up to g≈21) lose support and dip to
  0.0048. My float scan bounded gaps at 3.5 and missed this. Adjudicated in code
  (`/tmp/huge_gap.py`): at g=(1.05,1.98,13.8,1.05,1.98,1.05), tawan F_B=0.0119 vs LP F_B=0.0048.
- Full-adverse config set (including huge gaps at every position): LP max-min v=0.0077 (α=1.49),
  but dense full-adverse floor check = 0.006126 — still BELOW tawan's 0.006467. The LP keeps
  hitting the c-bound and over-rotating.
- **Verdict: the LP re-optimization did NOT beat tawan's hand-tuned (l,c).** Tawan's redistribution
  is near-optimal for the full adverse structure (it keeps F_B growing as any gap → ∞; the LP's
  concentrated-pressure solutions do not). The LP solutions are CONJECTURED to be worse, PROVEN
  worse at certification. No better (l,c) is reported as certified — only the α-transfer (Section 3).

## 6. Why the α-transfer works (CONJECTURED mechanism, consistent with data)

At psum=1/320 the certified eps is limited by the crystal floor, which depends on α through the
kernel's zero structure. α=1.49 (vs 1.47) moves the kernel so the period-2/3 crystal floor rises
(0.006465 → 0.006557 float; certified 0.0062 → vs tawan's 0.00577-safe). α=√2's crystal floor is
lower (0.006225) but still > 0.0060. The bound gains come from (a) higher eps AND (b) the slightly
different H(α) and optimal m: H(1.49)=0.67242189, H(√2)=0.67250070, H(1.47)=0.67245871.

## 7. Honest labels

- PROVEN: baseline reproduction; α-transfer certifications (Section 3, interval verifier, both
  independently re-run); bound arithmetic (0.673435 @ α=1.49 eps=0.0062 m=171; 0.673385 @ √2
  eps=0.0060 m=176); p,q ← U mapping; LP-fails-certification.
- CHECKED NUMERICALLY: crystal floors (float, non-rigorous); H(α) values.
- CONJECTURED: the mechanism explanation in Section 6.
- ABANDONED: LP re-optimization as a source of better coefficients (documented reason: misses
  large-gap adverse structure; interval-verified worse than tawan).
- INCONCLUSIVE: whether any (l,c) beats tawan's at fixed α — the LP search space was not exhausted;
  a correct re-optimization must include the full huge-gap family (up to g~25) in the LP.

## Commands (exact)

```
uv run --with mpmath --with python-flint python tools/verify_coboundary_floor.py            # baseline
uv run --quiet --with mpmath --with python-flint python /tmp/coboundary_decisive.py        # α-sweep 577..620
uv run --quiet --with mpmath --with python-flint python /tmp/coboundary_high.py            # 630/640 @1.49, 590/600 @√2
uv run --quiet --with mpmath --with python-flint python /tmp/confirm_records.py            # independent re-runs
uv run --quiet --with mpmath python /tmp/coboundary_bound.py                               # bound arithmetic
uv run --quiet --with mpmath python /tmp/decode_U.py                                       # p,q ← U mapping
uv run --quiet --with mpmath --with python-flint --with numpy --with scipy python /tmp/crystal_floor.py
uv run --quiet --with mpmath --with python-flint --with numpy --with scipy python /tmp/reoptimize_full.py
uv run --quiet --with mpmath --with python-flint --with numpy --with scipy python /tmp/certify_lp.py
uv run --quiet --with mpmath --with python-flint --with numpy python /tmp/huge_gap.py
```

Scripts live in /tmp/ (scratch). Canonical verifier: tools/verify_coboundary_floor.py (owned by
the n-point agent — not modified). Recommend copying the /tmp scripts into a tools/ subdir on the
next pass.
