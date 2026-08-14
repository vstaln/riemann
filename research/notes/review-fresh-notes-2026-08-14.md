# Adversarial review — tangent-lp-decisive + gs-general-estimate (2026-08-14)

**Reviewer:** adversarial validator. **Scope:** break claims or validate; never weaken.
**Skills applied:** s4h-investigation-counter-hypothesis, s4h-logic-argument-validation.
**Verdicts:** (a) INCOMPLETE - script bug, headline independently re-confirmed.
(b) INCOMPLETE - faithful sources, but arithmetic errors in PROVEN bookkeeping + overlabeling.

---

## (a) tangent-lp-decisive-2026-08-14.md + tools/adv_lp_loop_v3.py

### Verdict: INCOMPLETE (right conclusion; the script's LP does not certify what the note says it does)

The headline - "the tangent-plane in-class path to beat 0.673481 is closed" - is CORRECT and I
independently re-certified it (below). But the specific LP certificate the note cites is buggy,
and one interpretive claim is directionally inverted. The note is therefore INCOMPLETE, not VALID
and not FLAWED-as-a-whole.

### Finding 1: sign inconsistency between `tangent_affine` and `solve_lp` (major, [fix])

`tangent_affine` (adv_lp_loop_v3.py) returns `A, C, const` where its own docstring claims
`tangent = const + A.l + C.c`. The returned A, C are in fact the NEGATIVES of the true (l,c)
gradients. Numerical check (sign_check3.py, terminal cell (4220,8007,8027,8027,7995,4220)):

```
A_script = [-0.94675, -0.00500, 0.00000, 0.00800, 0.94375]
C_script = [-0.000132, 0.000050, 0.000000, -0.000085, 0.000167]
dF/dl_0 = +0.946750   (= -A_script[0])      dF/dc_0 = +0.000132 (= -C_script[0])
dF/dl_k = -A_script[k],  dF/dc_k = -C_script[k]  for all k
```

So the true affine form is `tangent = const - A.l - C.c` with the script's A, C (i.e.
`A_script = -(true gradient)`). The `solve_lp` row construction

```python
A_rows = np.array([[-a for a in A] + [-c for c in C] ...])   # -A_script = +true_gradient
b_rows = np.array([const - target ...])
```

therefore enforces `const + A_script.l + C_script.c >= target`, i.e. `tangent(-l, -c) >= target`.
Combined with the κ/q rows (which are NOT symmetric under (l,c) -> (-l,-c)), the script's LP is a
*reflected sibling* of the stated problem, not the stated problem itself. As coded, the script's
"INFEASIBLE" certifies `{ tangent(-l,-c) >= target, κ(l)>=0, q(c)>=0, |c|<=0.06 }` infeasible,
not `{ tangent(l,c) >= target, κ(l)>=0, q(c)>=0, |c|<=0.06 }`.

Fix: either negate the returned A, C in `tangent_affine` (make it match its docstring), or change
the row to `[+a for a in A] + [+c for c in C]`. Both give the correct certificate (I ran the
latter - see Finding 3).

### Finding 2: the "strongest / most permissive filter" direction is inverted (major, [fix])

Note lines 72-74: "the tangent bound is the strongest available per-box lower bound ... the most
permissive consistent LP filter". This is backwards. The hierarchy is

```
tangent_lower  <=  F(midpoint)  <=  box minimum   (box_lower <= box minimum too)
```

`tangent_lower` is the WEAKEST of the per-box lower bounds (it is F(midpoint) minus a nonnegative
radius correction). Because the constraint is `lower >= target`, a weaker lower bound makes the
constraint HARDER to satisfy, hence a LESS permissive filter and a WEAKER infeasibility
certificate. The most permissive (strongest) certificate is the exact objective F(midpoint) at
point cells (no radius, no PD filter), which is exactly what I ran (Finding 3). The note's
narrative should be corrected to: infeasibility of the exact-F LP is the strongest statement,
and it subsumes the tangent LP.

### Finding 3: the headline is CONFIRMED by an independent, stronger, correct LP

I built a corrected LP with the TRUE gradients (`A = mid[k+1]-mid[k]`, `C = w(mid[k+1])-w(mid[k])`)
and the correct κ>=0 / q>=0 rows, over the exact objective F at point-cell midpoints (no tangent,
no radius, no PD filter). Commands and stdout (final_decisive.py, corrected_lp.py):

```
EXACT-F LP, pressure-relevant point cells (3640): False  (HiGHS Status 8: infeasible)
EXACT-F LP, ALL 3663 point cells:                   False  (infeasible)
CORRECTED tangent LP (const - A.l - C.c >= eps):    False  (infeasible)
min F(base) over pressure-relevant cells = 0.00561239   (gap to target 0.005991 = 3.786e-4)
```

Since `tangent_lower <= F(midpoint)` on every box (radius correction is nonnegative), infeasibility
of the exact-F LP at point cells implies infeasibility of the tangent LP on the same set, and a
fortiori on the full 14652-box adverse set. So the note's claim #2 ("no (l,c) with |c|<=0.06 makes
tangent_lower >= 0.005991 on the adverse set") is TRUE - but it is certified by MY corrected LP,
not by the script as written.

Corroborating 1-d evidence (move_check.py): a scan of l0 in [-0.06, 0.06] at c=0 finds 100-885
boxes violating the target at EVERY l0 (minimum 100 at l0=+0.005), confirming the handoff's "two
binding cell families conflict" - no single l0 move fixes the terminal cell without breaking
another. The terminal cell's tangent at base is 0.00561058 (gap 3.8e-4), satisfiable in isolation;
the full set is what is infeasible.

### Finding 4: PD-at-base exclusion is NOT a hole (minor, [dismiss])

Only 3499 of the 14652 adverse boxes pass the base-PD check (so the note's "14652 rows" is really
3499). The task asked whether a base-non-PD box could BECOME PD at the solution with a low bound,
escaping the filter. Ruled out: my exact-F point-cell LP imposes NO PD condition at all and is
still infeasible, so no such escape exists. The adverse-set-sufficiency question is likewise moot
for the negative direction: infeasibility on a subset (point cells) implies infeasibility on any
superset.

### Finding 5: κ>=0 / q>=0 rows are faithful (minor, no action)

`kappa_i >= 0 <=> -l_{i-1}+l_i <= p0` and `q_i >= 0 <=> -c_{i-1}+c_i <= q0` (l_0=l_6=c_0=c_6=0)
match the verifier's `pressure_coeffs/nearest_coeffs` monotonicity requirement
(verify_coboundary_floor.py lines 256-263, 400-419). Correct. (This faithfulness is exactly why
Finding 1's reflection matters: the κ/q rows break the (l,c)->(-l,-c) symmetry.)

### Finding 6: float caveat is disclosed but under-weighted (minor, [fix])

The note honestly discloses IEEE-double rounding of Arb coefficients. My exact-F LP used Arb at
base and float only for the small affine coefficients, still infeasible. For a PROVEN-level
certificate an interval/rational LP pass is still required (the note already says this).

### (a) claim-label audit

| Claim | Label given | Assessment |
|---|---|---|
| #1 "the tangent-plane LP ... is infeasible" | CHECKED NUMERICALLY | **MISLABELED for the object named**: the script prints INFEASIBLE but certifies a reflected sibling; the stated problem's infeasibility is established only by my corrected LP |
| #2 "no (l,c) makes tangent_lower >= 0.005991 on the adverse set" | CHECKED NUMERICALLY | **TRUE but not certified by the cited script** (certified by my corrected LP) |
| #3 "tangent-plane path cannot beat record in-class" | CONJECTURED | **Appropriate, now backed by a correct certificate**; upgrade toward PROVEN via interval/rational LP |
| #4 "0.6818 ceiling structural" | PROVEN | Unchanged (out of scope; already established elsewhere) |

### (a) bottom line
Right conclusion, wrong certificate in the script, inverted "permissiveness" narrative. The
exact-F point-cell LP I ran is the correct decisive certificate; the note should cite it (and the
corrected tangent LP) instead of the buggy `solve_lp`.

---

## (b) gs-general-estimate-2026-08-14.md

### Verdict: INCOMPLETE (sources faithful; scale-mismatch thesis sound; PROVEN bookkeeping has errors)

### What is FAITHFUL (verified against the actual arXiv sources)

Fetched arXiv:2511.20059 abs page + ar5iv full text. The note's §1a is faithful:
- **Theorem 2** = the note's statement (1 <= C < 2; (4.4) => 2-C simple, 2-C on the line, and
  3-2C both if C < 3/2). Verified verbatim (ar5iv §4, Thm 2, eq. 4.4).
- **eq. (4.3)** decomposition = `Sum_{gamma=gamma'} 1 = Sum_rho m_rho + Sum_{rho: beta!=1/2} m_rho
  + Sum_{rho != rho', beta+beta' != 1, gamma=gamma'} 1`. Verified verbatim (ar5iv eq. 4.3).
- **(4.5)** lower bound N(T) ~ (T/2pi) log T => C >= 1. Verified.
- The "diagonal double-sum estimate" reading is CORRECT: (4.4) is literally the ordered-pair sum
  with gamma = gamma', a double sum. The note's multiplicity caveat (m_rho vs m_rho^2) is correct
  and self-flagged: the paper's prose confirms a double zero is "counted 4 times" (m^2), matching
  Sum m_rho only when collapsed to distinct heights.

### Finding 1: §2a contains arithmetic errors inside PROVEN-labeled material (major, [fix])

Note §2a (lines 89-94):

1. "for the classical Ingham exponent A = 3/(2-sigma) -> 1": **WRONG.** 3/(2-sigma) -> 3/(3/2) = 2
   as sigma -> 1/2. The EXPONENT A(1-sigma) = 3(1-sigma)/(2-sigma) -> 1 is what tends to 1; the
   note conflates A with the exponent.

2. "N(sigma,T) << T^{1+o(1)}, which is larger than N(T) ~ T log T - i.e. vacuous": **WRONG as
   stated.** T^{1+o(1)} is SMALLER than T log T (log T dominates T^{o(1)}), so the estimate would
   be too strong (false) at sigma=1/2, not vacuous. (Ingham's actual bound carries a log^5 T
   factor, giving T log^5 T near sigma=1/2, which IS larger than T log T - so "vacuous" is
   defensible for the true Ingham bound, but not for the T^{1+o(1)} the note wrote.)

3. "the density hypothesis N(sigma,T) << T^{2(1-sigma)} log T is false at sigma=1/2: at sigma=1/2
   it would read N(1/2,T) << log T": **WRONG.** With the note's own written form (with the log T
   factor), sigma=1/2 gives T^{2(1/2)} log T = T log T, which is TRUE (von Mangoldt), not false.
   With the BGSTB form the note quotes in §1b, N = o(T^{2(1-sigma)}), sigma=1/2 gives o(T), which
   IS false (N ~ T log T). The note conflates the two forms and mis-evaluates both the exponent
   and the conclusion. The CORRECT statement: the density hypothesis (BGSTB form, o(T^{2(1-sigma)}))
   cannot be asserted at sigma=1/2 because there it reads o(T), contradicting von Mangoldt.

These three slips do NOT kill the thesis - the conclusion "zero-density is the wrong instrument
near the line" survives - but they are displayed as PROVEN bookkeeping and must be corrected.

### Finding 2: §2b arithmetic is CORRECT (no issue; flagging to preempt a common misread)

§2b's computation `T^{2*(1/(2 log T))} log T = T^{1/log T} log T = e * log T = O(log T)` is
RIGHT: T^{1/log T} = e (a constant), so the moving-boundary density-hypothesis extrapolation gives
O(log T) - essentially "all but O(log T) zeros inside the box", the RH-scale statement. This is the
correct observation and the core of the scale-mismatch argument. (Note: using the BGSTB little-o
form it is even stronger, o(1).)

### Finding 3: "GM cannot supply (A)/(B)" is OVERLABELED PROVEN (major, [fix])

The note labels (twice, in §2b/§2c and the §3 table) "zero-density is scale-blind / no fixed-sigma
family can imply the box / GM cannot certify (A)/(B)" as **PROVEN for the scale gap**. This is a
proof sketch, not a proof, and it has a genuine gap: a fixed-sigma zero-density estimate ALONE
cannot express the box (correct), but a fixed-sigma estimate COMBINED with a MOMENT input (e.g. a
weighted Sum (beta - 1/2)^2 bound, or a log|zeta| mean-square at the boundary) COULD constrain the
box. The note's own recommended sub-lemma (ii) - "prove no fixed-sigma zero-density family implies
N(1/2 + 1/(2 log T), T) = o(T log T)" - IS the missing proof. Until it is proven, the claim should
be **CONJECTURED (strongly motivated)**, not PROVEN. The note already labels GM's exact sigma-range
INCONCLUSIVE correctly; the scale-gap claim deserves the same downgrade.

### (b) claim-label audit

| Claim | Label given | Correct label |
|---|---|---|
| (4.4) => 2-C / on-line / 3-2C (GS Thm 2) | PROVEN (conditional) | **PROVEN** (verbatim; framework is a theorem) |
| RH => C=4/3 => 2/3 simple | PROVEN | **PROVEN** (Montgomery 1973, §3 verified) |
| Box (1.5) => density (1.6) => 61.7% | PROVEN (conditional) | **PROVEN** (BGSTB §6/§7, not re-derived here - correctly out of scope) |
| Density hypothesis false at sigma=1/2 | PROVEN | **Conclusion right, computation wrong** (o(T) not "log T"; fix §2a) |
| Ingham "A->1", "T^{1+o(1)} larger than N(T)" | PROVEN | **WRONG** (A->2; T^{1+o(1)} < T log T) |
| Zero-density scale-blind; GM cannot supply (A)/(B) | PROVEN (scale gap) | **CONJECTURED** (direction right; moment-argument gap; pending sub-lemma (ii)) |
| GM's exact sigma-range | INCONCLUSIVE | **INCONCLUSIVE** (correct as-is) |

### (b) fix recommendations
1. Correct §2a: A = 3/(2-sigma) -> 2; drop "T^{1+o(1)} is larger than N(T)"; restate the density
   hypothesis in the BGSTB form o(T^{2(1-sigma)}) and note sigma=1/2 gives o(T) (false).
2. Downgrade "GM cannot supply (A)/(B)" and "zero-density scale-blind" from PROVEN to CONJECTURED
   (strongly motivated), pending sub-lemma (ii).
3. Keep §1 (faithful) and §2b (correct); §2b's O(log T) computation is right.

---

## Overall verdicts (3-line summary for dispatch)
- **(a) INCOMPLETE** - headline survives (independent exact-F point-cell LP is infeasible at
  0.005991, gap 3.786e-4), but `solve_lp` has a sign inconsistency so its LP certifies a reflected
  sibling, not the stated problem; the "most permissive filter" narrative is inverted.
- **(b) INCOMPLETE** - GS Thm 2/(4.3)/(4.4)/(4.5) are faithful and the scale-mismatch thesis is
  directionally right, but §2a has arithmetic errors inside PROVEN material (Ingham A->2 not 1;
  density hypothesis at sigma=1/2 is o(T) not "log T") and "GM cannot supply it" is overlabeled.
- **Worst hole:** (a) the note's primary certificate (the script's LP) does not certify its stated
  claim (sign/reflection bug) - headline survives only via my independent corrected LP.

## What was verified (and what was NOT)
- VERIFIED (ran): the exact note command reproduces "LP INFEASIBLE at iter 0" verbatim (71902
  cells / 14652 boxes; stdout matches the note).
- VERIFIED (ran, new): corrected tangent LP infeasible; exact-F(mid) point-cell LP infeasible over
  all 3663 cells (and 3640 pressure-relevant); l0 scan shows 100-885 binding boxes at every l0;
  terminal-cell tangent at base = 0.00561058 (gap 3.786e-4).
- VERIFIED (fetched): GS Theorem 2, eqs. (4.3), (4.4), (4.5) from arXiv:2511.20059 abs + ar5iv.
- NOT verified: rigorous interval/rational LP certificate (float LP only); BGSTB §6/§7 constants
  (not re-derived, correctly out of scope in the GS note); the GM paper's exact sigma-range (only
  the survey abstract, as the note itself flags).
- NOT run: the interval verifier (correctly - the LP dies at iter 0, so no verifier was invoked).

## Verification commands
```
# (a) reproduce the note (verbatim match)
cd /home/vstaln/riemann && uv run --quiet --with mpmath --with scipy --with numpy --with python-flint \
  python3 tools/adv_lp_loop_v3.py 335 0.005991 1.464 --max-iters 4
# -> iter 0: LP INFEASIBLE (HiGHS Status 8: model_status is Infeasible)

# (a) decisive independent certificate (scratch probes, this review)
final_decisive.py -> "EXACT-F LP, pressure-relevant point cells: False (infeasible)"
                     "min F(base) over pressure-relevant cells = 0.00561239"
corrected_lp.py  -> "CORRECTED LP (const - A.l - C.c >= eps): False (infeasible)"
sign_check3.py   -> "dF/dl_k = -A_script[k], dF/dc_k = -C_script[k]" (sign inconsistency shown)

# (b) source check
curl -sL https://ar5iv.labs.arxiv.org/html/2511.20059   # Thm 2, eqs. (4.3)-(4.5)
```

## Handoff contract
- Deliverable: this note. Assumptions tagged [verified] (GS source text, script stdout, my probe
  outputs) / [inferred] (the "only remaining in-class path" framing is inherited from
  handoff-psum-lc-frontier.md, not independently re-derived here).
- Next step named: (a) fix `solve_lp` row direction + the "most permissive" narrative, and cite the
  exact-F point-cell LP (or corrected tangent LP) as the decisive certificate; (b) correct §2a's
  arithmetic and downgrade "GM cannot supply (A)/(B)" to CONJECTURED pending sub-lemma (ii).
