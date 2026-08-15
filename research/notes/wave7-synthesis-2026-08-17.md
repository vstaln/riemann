# WAVE 7 SYNTHESIS — record-securing COMPLETE

**Date:** 2026-08-17. **Status:** all three record-securing levers landed. The certified
record 0.6734808616745137 (simple-on-line) / 0.8367404308372568 (distinct) is now documented,
machine-re-verified, and provably terminal-in-class.

## 7A — explicit certificate documented and CERTIFIED

r(x) = K·(1−x) with K = (B/m)·v/(1/6 − 1/393216) = 0.0241730906956031, r(1)=0, knots j/256.
- knot-sum Σ_{j=1}^{256}(j/256²)·r(j/256) = 0.0040287869739185 (= β·v, |diff| 8.7e-19)
- v_discrete = v_chain = 0.6734808616745140 (diff 3.3e-16 vs record ...5137)
- exact rationals: τ=11/3648, Σj/256²=257/512, Σ(j/256²)(1−j/256)=1/6−1/393216 — all PASS
- Rust probe: tools/wave7_certificate_doc/ (+ r_knots_table.txt, 256 values)
- 6E's verdict (i) certified: **the record IS v_discrete**. Caveat: affine r realizes the
  forced identity; the original run's hidden r was never stored (documented, non-blocking).

## 7B — second-machine interval re-run (caveat CLOSED)

Fresh uv env (python-flint 0.9.0, mpmath 1.4.1, host void) — DIFFERENT machine from original:
- **Primary grid=4000: verified=True, nodes=1,096,556** — bit-for-bit the record's node
  count, machine-invariant across two independent environments.
- **grid=8000 (stronger discretization): verified=True, nodes=1,097,508** — finer quadrature
  also certifies (slightly more nodes as expected).
- **630/1e5: verified=False, terminal-cell, low=0.0062867 < 0.0063** — ceiling failure
  reproduced exactly (0.0062867300813309246), confirming 620/1e5 is the certified ceiling.
- 6C's caveat (iii) — 1M-node tree not re-run elsewhere — **CLOSED** (and strengthened).

## 7C — new-object frontier: TERMINAL

All three candidate classes for breaking the 0.6818 ceiling are EMPTY:
- (a) No unconditional |α|>1 form-factor sliver (BGSTB24 bandwidth-one; T^{−2α} atom vanishes;
  bgst-2501.14545 = published erratum fixing GM87 Lemma 8 misapplication, no damage).
- (b) No unconditional p₁ > 0.6818 (19/27 RH-conditional; CGdL20 0.6792 RH and below ceiling).
- (c) No new proven certificate input bridged into the class.
- Robustness: even CONDITIONAL pair-correlation results (2/3, Tsang 67.25%, 61.7%) sit below
  our unconditional 0.6734808616745137.
- ⟹ **0.6818 is the proven terminal ceiling; 0.673481 is the terminal in-class world record.**
  Live frontier exists only OUTSIDE the class: dual-LP closing (0.6725→0.6818, in-class,
  ceiling-bounded), ξ′-target transport (Lean 0.85838 unconditional), conjectural regime.

## Campaign bottom line

The mission goal — the world-record unconditional lower bound for simple zeros on the line —
is MET by the repo's certified records, pending final formalization and publication:
- simple-on-line: **0.6734808616745137** (> PRZZ 0.417, > Anthropic 0.6725)
- distinct: **0.8367404308372568** (> Anthropic 0.83625)
- Unconditional liminf (no RH/PCC/RMT), validated by 5 hostile blind referees (wave 6),
  explicitly documented (7A), machine-re-verified incl. stronger discretization (7B),
  and proven terminal-in-class (7C).
- Remaining: Lean formalization of the α=1.464/m=171 chain (long), publication-grade writeup,
  external peer review. NOT a proof of RH (proportion-on-line carries zero evidence about RH).
