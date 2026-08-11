# Verification record

Date: 2026-08-12 (Windows, Python 3.12.12, Strawberry MinGW g++ 13.2.0,
GMP, and local MPFR 4.2.1).

**Repository verification: PASSED.** The derivative table was independently
regenerated with directed MPFR, the verifier compiled with GMP-backed exact
dyadic-rational LDL, and all 64 boxes returned verified=true.

**External peer review: pending.** The source ZIP expected derivative-table
hash was not available, so the local CWD2 table is not claimed byte-identical
to that source artifact.

## Current result

The directed-MPFR evaluator reports

    bound_lower=0.6731929114731422
    bound_upper=0.67319291147314231
    certified_decimal_14=0.67319291147314

The exact high-precision expression is
0.6731929114731422535099843283718888..., corresponding to
67.3192911473142...%.

## Finite certificate

- Local target: F_B >= 577/100000.
- Window: alpha=147/100.
- Block size: m=183.
- Pressure tax: 59/19520.
- Kernel table SHA-256:
  13213b84960fa629db0eac3ed7891148066313cba84f4fa151cfcce749d8fc2c.
- Local derivative table SHA-256:
  035946b4368fbeab578720109039bb409877f2c3728b672a1c1daff6c3e6f375.
- Source-package expected derivative hash (audit only):
  53e7f31fdc12f60a393dd5cf3963b544e18916859cb7ac8ce9ad935f644e8a24.

The tracked 64-box log covers every code 0,...,63 exactly once.  Its totals
are:

    nodes=1126636
    splits=563286
    pressure=3477
    interval=318922
    tangent=240951
    maximum_depth=55
    unresolved_terminal_cells=0

The tree identity is
1126636 - 563286 = 3477 + 318922 + 240951 = 563350.

## Reproduce safely

Run scripts/verify.ps1 from this repository.  It creates a repository-local
.tmp_test_* workspace, regenerates the derivative table there, compiles the
verifier, checks the directed final-bound bracket, runs all 64 boxes, and
removes only that exact temporary directory.  It never overwrites tracked
binary data.

The previous 67.3101784721425...% joint-window result remains historical
material only.  The exploratory tools/explore_global_dual.py output is not a
certified lower bound.
