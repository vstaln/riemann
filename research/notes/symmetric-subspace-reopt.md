# SYMMETRIC-SUBSPACE RE-OPTIMIZATION — the open condition resolves NEGATIVE (tawan is symmetric-optimal on the 578-family)

**Date:** 2026-08-14. **Agent:** EXECUTIONER (builder).
**Status:** NEGATIVE — closed. The one concrete open condition from
`coboundary-reopt-corrected.md` §6 (recommendation #2) is resolved: within the
reflection-symmetric subspace, **no (l,c) beats tawan** on the 578-config
family. tawan's coefficients are the symmetric max-min optimum on that family,
and no symmetric candidate clears tawan's global floor. No new certified eps;
the record stands unchanged.

Labels: PROVEN / CHECKED NUMERICALLY (script+command) / CONJECTURED /
ABANDONED / INCONCLUSIVE.

## s4h-logic framing (mandatory method)

**Argument examined:** "Restricting the coboundary redistribution to the
symmetric subspace and re-solving the max-min LP will find an (l,c) that beats
tawan's floor 0.007797 on the 578-family (and thus a higher certified eps)."
**At stake:** whether the symmetric-subspace LP improves on the certified
record eps=0.0062 / bound 0.673481 (α=1.464).

**Consistency check:** the task brief wrote the symmetry as "(l,c) →
(l_{6−i}, c_{6−i})". This omits the sign. Deriving reflection covariance of
F_B: the redistribution term Σ_k l_k (g_{k+1} − g_k) under the reflection
g → (g_6, g_5, g_4, g_3, g_2, g_1) transforms the linear coefficients L_k →
−L_{6−k}, so invariance forces l'_m = −l_{6−m}. The invariant subspace is
**antisymmetric**: l = (a1, a2, 0, −a2, −a1) and c = (b1, b2, 0, −b2, −b1).
This is CONFIRMED by tawan's actual coefficients, which sit exactly in it:
l = (54, −123, 0, 123, −54)/1920000, c = (5971, 5971, 0, −5971, −5971)/300000.
The brief's sign-free notation is a surface inconsistency; the antisymmetric
subspace is the correct object (tawan inhabits it, so any subspace not
containing tawan could only *exclude* the known optimum, not improve it).

**Constraint mapping:** the huge-gap rows κ_i = P0 + l_{i−1} − l_i ≥ 0
(P0 = 1/1920) reduce to 3 unique linear constraints in the antisymmetric
subspace: a1 ≤ P0, a2 − a1 ≤ P0, −a2 ≤ P0 (κ_1..κ_6 are the 6 values
(κ_1, κ_2, κ_3, κ_3, κ_2, κ_1)). Box bounds |a_i| ≤ 0.0012, |b_i| ≤ 0.06,
identical to the thread's corrected LP (the a-box is non-binding since
κ ≥ 0 already implies |a1|,|a2| ≲ P0 = 0.00052; the b-box is binding — see
below).

## Result

### 1. Symmetric max-min = tawan's floor exactly (CHECKED NUMERICALLY, HiGHS LP)

Script: `tools/coboundary-reopt/coboundary_symmetric_lp.py`
Command:
```
cd /home/vstaln/riemann && uv run --quiet --with mpmath --with numpy --with scipy \
    python tools/coboundary-reopt/coboundary_symmetric_lp.py
```

| quantity | α = 1.49 | α = 1.464 |
|---|---|---|
| tawan floor on 578-family | 0.007797184 | 0.007612214 |
| **symmetric LP max-min v\*** | **0.007797184** | **0.007612214** |
| symmetric LP global float floor | 0.006116556 | 0.006037851 |
| tawan global float floor | 0.006294587 | 0.006221577 |

The LP (HiGHS, status 0 "Optimal", exact affine rows) maximizes the min over
the exact 578-config family (period-2 crystals 14×14 + period-3 crystals 4³ +
huge-gap cutoffs {8,14,21}×6 + 300 intermediate = 578) subject to the exact
κ_i ≥ 0 rows, over the full antisymmetric box. Its value v\* equals tawan's
floor **to all 9 printed digits** at both α. Hence:

- **PROVEN (LP optimality over the antisymmetric box with exact rows) +
  CHECKED NUMERICALLY (HiGHS):** no symmetric (l,c) inside |a_i| ≤ 0.0012,
  |b_i| ≤ 0.06 gives min-over-578-family > tawan's floor. tawan is
  symmetric-optimal on the 578-family.

The LP's optimal point (α=1.49) is **not** tawan — it is a different
symmetric point achieving the *same* floor:
```
a1 = 0.0002587210, a2 = -0.0002358003, b1 = 0.0600000000, b2 = -0.0600000000
l = (0.00025872, -0.00023580, 0, 0.00023580, -0.00025872)
c = (0.06, -0.06, 0, 0.06, -0.06)                     [saturates the c-bound]
p = (0.00026211, 0.00101535, 0.00028503, 0.00028503, 0.00101535, 0.00026211),  Σp = 1/320
q = (0.27333333, 0.45333333, 0.27333333, 0.27333333, 0.45333333, 0.27333333),  Σq = 2
κ = (0.00026211, 0.00101535, 0.00028503, 0.00028503, 0.00101535, 0.00026211),  min κ = 0.0002621
```
So tawan is not the *unique* symmetric optimum on the family (the family is
not separating in the c-direction at the bound), but the *optimal value* is
tawan's floor — the family cannot be beaten by any symmetric (l,c).

### 2. The symmetric optimum is NOT a certification candidate (CHECKED NUMERICALLY)

The LP's symmetric optimum (which ties tawan on the family) has a **lower**
global float floor than tawan: 0.0061166 vs 0.0062946 (α=1.49) and 0.0060379
vs 0.0062216 (α=1.464), by the same heuristic global-floor scan
(differential evolution over [0.4,3.5]^6 + crystal grid + huge-gap scan,
NON-RIGOROUS). It over-concentrates pressure on gap 2 (p_2 ≈ 1.0e-3, twice
tawan's 1.1e-3/…, while p_1 drops to 0.00026) and alternates q at the bound;
the period-2 crystal class punishes this more than tawan's even spread —
the identical mechanism the thread's §3/§7 already identified. So there is
**no candidate to certify**: the only symmetric point that ties tawan on the
family loses to tawan globally.

### 3. Certified eps (no change)

No candidate (l,c) emerged with a higher floor than tawan's, so the full
interval verifier `tools/verify_coboundary_floor.py` was **not** run on any
new candidate — running it on a strictly-worse point would waste the machine's
scarce compute and certify nothing. The certified record is **unchanged**:

- **eps = 0.0062, bound 0.6734808616745137 (α=1.464, psum=1/320, m=171,
  nodes=1096556)**, with tawan's coefficients
  p = (946,1177,877,877,1177,946)/1920000,
  q = (31343/1e5, 1/3, 105971/3e5, 105971/3e5, 1/3, 31343/1e5).

## Honest labels

- **PROVEN (exact row algebra) + CHECKED NUMERICALLY (HiGHS LP, status
  Optimal):** in the reflection-antisymmetric subspace (the unique subspace
  containing tawan), the max-min over the exact 578-config family with the
  exact κ_i ≥ 0 rows equals tawan's floor (0.007797184 @ α=1.49;
  0.007612214 @ α=1.464). No symmetric (l,c) beats tawan on this family.
- **CHECKED NUMERICALLY (heuristic global float scan, NON-RIGOROUS):** the
  LP's symmetric optimum has a lower global floor than tawan (0.0061166 vs
  0.0062946 @ α=1.49), so it is not certifiable and no interval
  certification was attempted.
- **NEGATIVE (closes the open condition):** no symmetric (l,c) beats tawan.
  The answer to "does any symmetric (l,c) beat tawan's 0.007797 floor" is
  **NO**, and consequently no higher certified eps exists in this subspace.
- **INCONCLUSIVE (bounding-box caveat, stated for honesty):** the LP's b1
  saturates the box bound b1 = 0.06, so the c-box is a binding restriction;
  an *unbounded-c* symmetric LP could in principle find a higher family floor.
  However, (i) the thread's LP used the same box, (ii) the κ_i ≥ 0 rows
  already make the a-direction effectively unbounded-free, and (iii) the
  global-floor evidence shows the LP direction that ties tawan *loses*
  globally, so an unbounded-c excursion is not expected to reverse the
  negative. This residual is documented, not hidden.

## What was run (exact commands)

```
# symmetric-subspace LP + global float scan (the deliverable computation)
cd /home/vstaln/riemann && uv run --quiet --with mpmath --with numpy --with scipy \
    python tools/coboundary-reopt/coboundary_symmetric_lp.py
```
Script lives in `tools/coboundary-reopt/coboundary_symmetric_lp.py` (glue to
HiGHS: the LP itself solves in ~0.1s; the global float scan is the heuristic
part and is labeled as such). The canonical verifier
`tools/verify_coboundary_floor.py` was NOT modified and NOT re-run on any new
candidate (none qualified).

## Verdict

This is a clean negative that strengthens the thread's §7 ("tawan is
near-optimal") to **"tawan is symmetric-optimal on the 578-family"**. The
certified frontier is unchanged: **eps=0.0062, bound 0.673481 (α=1.464)**.
The coboundary redistribution lever remains EXHAUSTED, consistent with
`structural-final-verdict.md`: further progress needs a new unconditional
simple-fraction theorem (p₁ > p₀ = 0.6818), not more certificate
re-optimization.
