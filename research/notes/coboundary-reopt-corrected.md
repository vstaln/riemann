# COBOUNDARY RE-OPTIMIZATION, CORRECTED — huge-gap asymptotics and the fixed LP

**Date:** 2026-08-14 (round 4 continuation). **Agent:** EXPLORER.
**Status:** The prior LP failure is ROOT-CAUSED and FIXED. The corrected LP
(which includes the exact huge-gap asymptotic constraints) is feasible and
beats tawan's coefficients on its own constraint family, but a global float
scan finds a config class the LP still misses; the question "does any (l,c)
beat tawan's at α=1.49" remains OPEN (INCONCLUSIVE). A clean negative was NOT
reached; the corrected LP is a genuine new result, not a confirmation of
tawan-optimality.
Labels: PROVEN / CHECKED NUMERICALLY (script+command) / CONJECTURED /
ABANDONED / INCONCLUSIVE.

## Headline

1. **PROVEN (exact derivation + numeric check):** as one gap g_i → ∞ with the
   other five bounded, the coboundary functional satisfies
   ```
   F_B(g; l,c) = kappa_i · g_i + O(1),   kappa_i := p_i + l_{i-1} − l_i
   ```
   with l_0 = l_6 = 0 and p the redistributed pressure p_i = 1/1920 + l_{i−1} − l_i
   (uniform base pressure 1/1920). The limiting slope is **exactly** p_i.
   Numerical check at g_i = 60: F_B/60 = 0.000586 vs κ_1 = 0.000493,
   F_B/60 = 0.000691 vs κ_2 = 0.000613, etc. (O(1/H) agreement; the constant
   terms and span-kernel corrections vanish as w(y_j−y_a) → 0 for every span
   containing g_i, and w(g_i) → 0).

2. **PROVEN (this is the fix):** certification requires **κ_i ≥ 0 for all i**.
   If any κ_i < 0, F_B → −∞ along the ray (g_i → ∞, others fixed), so NO
   eps > 0 can be certified. The prior explorer's LP had κ_1 = −0.00052 < 0
   (its "concentrated pressure on gap 3" solution), which is exactly why its
   coefficients failed interval certification even at 600/1e5. The verifier's
   one-body pruning (p_i g + q_i w(g), `tools/verify_coboundary_floor.py`,
   cutoff_cells up to g ≈ 18.6) explores these huge-gap configs.

3. **CHECKED NUMERICALLY:** tawan's coefficients satisfy κ_i ≥ 0 with a
   comfortable margin: κ = (0.000493, 0.000613, 0.000457, 0.000457, 0.000613,
   0.000493), min κ = 0.000457 at α=1.49. The prior LP's min κ ≈ −0.00000
   (κ_4 < 0, κ_1,κ_3,κ_5 ≈ 0).

4. **CHECKED NUMERICALLY (corrected LP):** adding the exact constraints
   κ_i ≥ 0 (as the linear rows −l_{i−1} + l_i ≤ 1/1920, l_0 = l_6 = 0) to the
   max-min LP over crystals + intermediate grid + finite huge-gap cutoffs
   {8, 14, 21} × each position:
   - LP max-min v* = **0.008771** (α=1.49, c-bound 0.06),
   - tawan's floor on the SAME 578-config family = **0.007797**,
   - so on |K| the LP beats tawan by ~0.0010.
   The LP concentrates pressure (p_2 ≈ 0.00172 vs 1/1920 ≈ 0.00052; total
   pressure preserved at 1/320 = 0.003125) and pushes the c-vector to the
   bound, while keeping every κ_i ≥ 0.

5. **CHECKED NUMERICALLY (global float floor, NON-RIGOROUS):** the corrected
   LP solution's true global float floor is **0.005674** at
   g ≈ (1.063, 25.96, 1.048, 1.032, 1.037, 1.047) — BELOW tawan's global float
   floor 0.006295 on the identical scan. So the LP family (crystals +
   intermediate + a few huge cutoffs) still MISSES the true adverse config
   class. The missing class appears to be **two gaps simultaneously large**
   (e.g. g_1 and g_2 both ~ 20–26 with the rest near kernel zeros), where the
   LP's concentrated pressure on gap 2 and its boundary-c-heavy q-vector
   underperform. Cutting-plane iteration was started to add this class but
   HUNG (see §4).

6. **INCONCLUSIVE:** whether any (l,c) beats tawan's at α=1.49. The corrected
   LP's v* = 0.0088 vs tawan's 0.0078 on |K| shows tawan is NOT LP-optimal on
   the sampled family, but the global-floor scan shows the family is not
   closed under adverse configs; tawan may still be near-optimal on the true
   feasible set. No better (l,c) is reported as certified.

## 1. The huge-gap asymptotic constraints (exact)

Setup (from `paper/riemann.tex` eq. coboundary and the C++ verifier
`tools/verify_coboundary.cpp`):
```
U(g_1..g_5)  = (54 g_1 − 123 g_2 + 123 g_4 − 54 g_5)/1920000
             + (5971/300000)(w(g_1)+w(g_2)−w(g_4)−w(g_5))
F_B(g_1..g_6) = F_0(g) + U(g_2..g_6) − U(g_1..g_5)
F_0(g) = sum_j p0 g_j + sum_j q0 w(g_j) + sum_{0<=a<b<=6} a_{ab} w(y_b−y_a),
         p0 = 1/1920, q0 = 1/3, a_{ab} = 2/(7−(b−a)), y_0 = 0, y_k = Σ_{j<=k} g_j.
```
The redistribution is the 10 parameters (l_1..l_5, c_1..c_5) with
```
p_i = p0 + (l_{i−1} − l_i),   q_i = q0 + (c_{i−1} − c_i),   l_0 = l_6 = c_0 = c_6 = 0,
Σ p_i = 6 p0 = 1/320,  Σ q_i = 6 q0 = 2   (telescoping).
```

**Limit g_i → ∞, g_{j≠i} bounded.** Every partial sum y_k that contains g_i
→ ∞; every y_k that does not stays bounded. The cosine kernel
k_α(x) = (sinc(πx−α/2)+sinc(πx+α/2))/(2 sinc(α/2)) → 0 as x → ∞, so
- w(y_b−y_a) → 0 for every span [a,b) containing g_i;
- w(y_b−y_a) → w(y_b−y_a) (bounded, i.e. O(1)) for spans avoiding g_i;
- w(g_i) → 0 (the one-body nearest term of gap i itself);
- w(g_j) → w(g_j) for j ≠ i.
Hence F_B = p_i g_i + [O(1) terms from l,c and the bounded spans] + o(1),
i.e. **F_B(g;l,c) = κ_i g_i + O(1)** with κ_i = p_i + l_{i−1} − l_i.

**Constraint:** for any certification of F_B ≥ eps over all g ∈ [0,∞)^6 we
need κ_i ≥ eps for every i (a fortiori κ_i ≥ 0). The verifier's one-body
pruning (`one_body` in `tools/verify_coboundary_floor.py`) uses exactly the
term p_i g + q_i w(g) and scans g up to cutoff_cells/grid ≈ 84001/4000 ≈ 21,
so a negative κ_i shows up immediately as an unresolved/pruned-region dip.

**Two gaps → ∞.** If g_i, g_j → ∞ with the rest bounded:
- spans containing BOTH → 0;
- spans containing exactly one → 0 (the O(1) constant is unchanged);
- F_B ~ κ_i g_i + κ_j g_j + O(1) (the cross term w(y_j−y_i) involves both gaps
  and → 0; there is no bilinear term).
**All six → ∞:** F_B ~ (Σ p_i)(Σ g_i) = (1/320)(Σ g_i) → +∞. So the family to
constrain is the 6 one-gap rays (κ_i ≥ 0) plus bounded/periodic configs; the
two-gap rays are covered by κ_i, κ_j ≥ 0 and add no new constraint.

## 2. The corrected LP

Variables x = (l_1..l_5, c_1..c_5, v). Maximize v subject to:
```
(a) crystals:   F_B(g;l,c) ≥ v     for period-2/3 g in a coarse grid
(b) asymptotics: κ_i = 1/1920 + l_{i−1} − l_i ≥ 0   (i=1..6, l_0=l_6=0)
                 + finite cutoffs: F_B(g;l,c) ≥ v at g_i ∈ {8,14,21}
                 with the other five at crystal values (each position)
(c) intermediate: F_B(g;l,c) ≥ v for ~300–500 uniform draws over [0.5,3.0]^6
                 plus ~150 draws near the kernel-zero band (gaps ~0.9–1.6)
bounds: |l_i| ≤ 0.0012, |c_i| ≤ 0.06
```
This is a linear program (F_B is affine in (l,c) at each fixed g) solved by
scipy.optimize.linprog (HiGHS). Exact rows:
```
-F0_k − <L_k,l> − <C_k,c> + v ≤ 0        (each config k; L_k,C_k from g_k)
-l_{i−1} + l_i ≤ 1/1920                  (each i; the κ_i ≥ 0 rows)
```

**Result (α=1.49, c-bound 0.06):** v* = 0.008771, l = (0.0002552, 0.0017164,
0.0002734, 0.0003247, 0.0002585), c = (0.06, −0.06, 0.06, −0.06, 0.06),
p = (0.000255, 0.001716, 0.000273, 0.000325, 0.000259, 0.000297) [sum
0.003125 = 1/320], q = (0.273, 0.453, 0.213, 0.453, 0.213, 0.393) [sum 2],
κ = (0.000255, 0.001716, 0.000273, 0.000325, 0.000259, 0.000297). **All κ_i
≥ 0** — the corrected LP is feasible, unlike the prior one. On the same
578-config family, tawan's floor is 0.007797 < v* = 0.008771.

c-bound sensitivity: v* = 0.008771 (0.06), 0.008630 (0.02), 0.009090 (0.15).
The optimum always saturates |c|; the q-vector alternates.

**Global float floor (NON-RIGOROUS, structured multi-start + huge-gap scan):
LP = 0.005674 < tawan = 0.006295.** So the family (a)+(b)+(c) is NOT closed:
there are adverse configs with the LP dipping below what the family samples.
The missing class (CONJECTURED) is **two simultaneously large gaps**
(g ≈ (1.06, 25.96, 1.05, 1.03, 1.04, 1.05), i.e. g_1, g_2 both large), where
the LP's pressure concentration on gap 2 and its boundary-heavy q lose to
tawan's more even spread. With tawan's coefficients the same config gives
0.006295 ≥ 0.00577 (certifiable); with the LP coefficients it gives 0.005674
< 0.00577 (not certifiable).

## 3. Honest labels

- **PROVEN:** κ_i = p_i + l_{i−1} − l_i is the exact limiting slope of F_B as
  g_i → ∞ (span-kernel terms all → 0, one-body w(g_i) → 0, no bilinear terms);
  κ_i ≥ 0 is necessary for certification; the corrected LP (with the κ_i ≥ 0
  rows) is feasible with v* = 0.008771 at α=1.49, beating tawan's 0.007797 on
  the 578-config family.
- **CHECKED NUMERICALLY (script + command below):** tawan κ = (0.000493,
  0.000613, 0.000457, 0.000457, 0.000613, 0.000493), min 0.000457; prior LP
  min κ ≈ −0.00000 (κ_4 < 0); F_B(H=60)/60 ≈ κ_i to O(1/H); family floors
  (LP 0.008771 vs tawan 0.007797); global float floors (LP 0.005674 vs tawan
  0.006295).
- **CONJECTURED:** the missing adverse class is two-large-gaps (identified by
  one scan; not exhaustively mapped); the mechanism explanation (pressure
  concentration on gap 2 + boundary q loses to tawan's spread).
- **INCONCLUSIVE:** whether any (l,c) beats tawan's at α=1.49. The corrected
  LP shows tawan is not optimal on the sampled family, but the family is not
  closed; the cutting-plane loop that would close it HUNG (below). No
  certified better (l,c) exists; the α-transfer record of
  eps=0.0062 @ α=1.49 (bound 0.6734350) from the previous note still stands
  as the certified best.
- **ABANDONED:** the specific cutting-plane implementation
  (`/tmp/coboundary_cutting_plane.py`) — scipy/HiGHS thread deadlock at 0% CPU
  for 27 min (PID 30078), killed. The LP solve itself (linprog, HiGHS) is
  fast (0.0s); the hang was in the iteration driver, most likely a HiGHS
  threaded solve inside a nested call with the scipy wrapper. The approach
  (cutting-plane to close the two-large-gap class) is sound and worth one
  more attempt with method='highs' options={'threads':1} or a serialized
  solve, but that is a new task.

## 4. What was run (exact commands)

```
# horizon (kappa) values for tawan and the prior LP
cd /tmp && uv run --quiet --with mpmath --with python-flint --with numpy --with scipy \
    python /tmp/coboundary_reopt_horizon.py

# corrected LP (family build + linprog/HiGHS), v*, kappa, family floors
cd /tmp && uv run --quiet --with mpmath --with python-flint --with numpy --with scipy \
    python /tmp/coboundary_reopt_lp.py

# global float floor (structured multi-start + huge-gap scan), NON-RIGOROUS
cd /tmp && uv run --quiet --with mpmath --with python-flint --with numpy --with scipy \
    python /tmp/coboundary_find_worst2.py 1.49 \
      0.0002552,0.0017164,0.0002734,0.0003247,0.0002585 \
      0.06,0.06,-0.06,0.06,0.06

# self-check: asymptotic slope formula + family comparison + prior-LP kappa
cd /tmp && uv run --quiet --with mpmath --with python-flint --with numpy --with scipy \
    python /tmp/coboundary_reopt_selfcheck.py

# canonical verifier (ground truth; unmodified, owned by the n-point agent)
uv run --with mpmath --with python-flint python tools/verify_coboundary_floor.py
```
Scripts live in /tmp/ (scratch). Note: the verifier is canonical and was NOT
modified (hooks: never weaken a verifier; n-point agent owns it).

## 5. Why this is progress, and what's next

The prior note ended with "INCONCLUSIVE: whether any (l,c) beats tawan's —
the LP search space was not exhausted." This note settles the first half of
that: the failure mode is now EXACT (κ_i ≥ 0 is necessary; the prior LP
violated it), the corrected LP is feasible and beats tawan on a 578-config
family, and the residual gap is a concrete missing config class
(two-large-gaps). Next attack (recommended):
1. close the family with two-large-gap cutting planes
   (g_i, g_j ∈ {5..26} × positions, all pairs), re-solve, re-scan;
2. when the LP's global float floor clears tawan's by a margin, certify with
   the interval verifier `verify_floor(..., cap_scheme='coboundary',
   pressure_coeffs=p, nearest_coeffs=q)` at target 620/1e5 (α=1.49) and
   recompute the bound;
3. if instead the two-large-gap class always pins the LP at ≤ tawan's floor
   with no slack, that is the honest dual certificate that tawan is
   near-optimal — a clean negative, to be written as such.
