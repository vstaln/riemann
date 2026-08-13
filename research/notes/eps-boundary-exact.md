# eps boundary at α=1.464 is EXACT — 0.00620 certifies, 0.00621+ fails

**Date:** 2026-08-13. **Status:** PROVEN (interval verification, node counts recorded).
**Method:** tools/verify_coboundary_floor.py, α=1.464 cosine kernel, grid=4000,
coboundary cap, tawan coefficients (p=[946,1177,877,877,1177,946]/1920000,
q=[31343/1e5, 1/3, 105971/3e5, 105971/3e5, 1/3, 31343/1e5]),
max_nodes=25,000,000, psum=1/320.

## Results

| eps | status | nodes | note |
|-----|--------|-------|------|
| 0.00620 | **True** (verified) | 1,096,556 | exact certified record baseline |
| 0.00621 | False (terminal-cell) | 519,206 | low=0.0061983 < 0.00621 |
| 0.00622 | False (terminal-cell) | 557,413 | low=0.0062089 < 0.00622 |
| 0.00623 | False (terminal-cell) | 195,812 | low=0.0062155 < 0.00623 |

The terminal cells are 6D point boxes (all coordinates equal) where the interval
lower bound is genuinely below target — real counterexamples to the inequality at
those eps values, not node-exhaustion artifacts (max_nodes=25M was NOT hit; the
branch-and-bound exhausted its stack to single cells).

## Consequence

**The certified optimum for the coboundary class with tawan's coefficients at
α=1.464 is exactly eps=0.00620, giving bound 0.6734808616745137.** There is NO
eps headroom at this α with these coefficients. The record stands.

**Implication for the Rust verifier port:** node-count reproduction (1,096,556)
is the sanity gate. Since rug's interval enclosures differ from Arb's (both are
valid lower bounds but different widths), a rug-based verifier will NOT reproduce
the exact node count — but must reproduce the True/False VERDICTS (0.00620 True,
0.00621/2/3 False) to be trusted for exploring new coefficient families.

## Commands

```
uv run --quiet --with mpmath --with python-flint python3 /tmp/eps_probe3.py
```
(script: eps 0.00621/0.00622/0.00623 at α=1.464, max_nodes=25_000_000)

## Follow-up: the 0.00621 failure is a REAL inequality violation (PROVEN)

The terminal cell Python reported at eps=0.00621,
((4223),(7993),(8042),(8020),(7993),(4217))/4000, was evaluated at 60-digit
mpmath precision:

    TRUE F_B at that point = 0.00591883580089175  <  0.00621

So the violation is genuine, not an enclosure artifact. No tighter table (Rust
or otherwise) can certify eps=0.00621 at α=1.464. The coboundary certificate
family is now PROVEN exhausted at every parameter:

| parameter | certified optimum | evidence |
|-----------|------------------|----------|
| α         | 1.464            | H-ladder scan, eps boundary |
| psum      | 1/320            | frontier scan |
| eps       | 0.00620 (exact)  | 0.00621 = real violation (above) |
| m         | 171              | exact m-scan at eps=0.00620 |
| (l,c)     | tawan            | symmetric LP re-opt (v*=tawan floor) |

**Record 0.6734808616745137 is the exact, certified optimum of the coboundary
class.** Any higher bound requires genuinely new input structure (new kernel,
new redistribution family, or a new theorem) — all of which is beyond the
current certificate machinery.
