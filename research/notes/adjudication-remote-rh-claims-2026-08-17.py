#!/usr/bin/env python3
"""Verify that CompleteRHProof.lean's elimination theorem is a VACUOUS TAUTOLOGY.

Theorem (CompleteRHProof.lean L525-528, L739-742):
    mercer_offline_zeros_elimination (C C_on : R) (N_off : Nat)
        (h_bound : forall d : Nat, C <= C_on - 4 * (d : R) * (N_off : R)) : N_off = 0

The honest mathematical content: for ANY finite reals C, C_on and ANY N_off >= 1,
the hypothesis is UNSATISFIABLE (as d -> inf, RHS -> -inf < C). So the theorem is
true-but-empty: it assumes its own conclusion. It carries zero information about
whether the ACTUAL zeta function has off-line zeros. This script proves the
unsatisfiability claim numerically.
"""
import itertools

print("=== The claim: forall d : Nat, C <= C_on - 4*d*N_off is UNSATISFIABLE for N_off >= 1 ===")
print("(regardless of how large C_on is or how negative C is)\n")

# For N_off >= 1: find the largest d for which the bound could hold given C, C_on.
# RHS is strictly decreasing in d at rate 4*N_off, so it must eventually fall below ANY C.
worst_cases = []
for N_off in [1, 2, 3]:
    for C, C_on in itertools.product([-1e9, -1e6, 0.0, 1e6, 1e9], repeat=2):
        # d where RHS first drops below C:
        # C > C_on - 4*d*N_off  <=>  d > (C_on - C)/(4*N_off)
        first_fail = int((C_on - C) / (4.0 * N_off)) + 1
        if first_fail < 0:
            first_fail = 0
        worst_cases.append((N_off, C, C_on, first_fail))

# Report the LARGEST first-failure d seen — i.e. the most generous case for the hypothesis
best = max(worst_cases, key=lambda t: t[3])
print(f"Most generous case found: N_off={best[0]}, C={best[1]:.0f}, C_on={best[2]:.0f}")
print(f"  -> hypothesis first fails at d={best[3]}; it fails for ALL larger d.")
print(f"  -> since d ranges over ALL of Nat (unbounded), the hypothesis is unsatisfiable.")
print(f"  -> hence N_off=0 follows from the hypothesis ALONE — the theorem is a tautology.\n")

print("=== Concrete sanity check: N_off=1, C=0, C_on=10 (the paper's abstract setting) ===")
for d in [0, 1, 2, 3, 4]:
    rhs = 10.0 - 4.0 * d * 1
    print(f"  d={d}: 0 <= {rhs:6.1f} ? {0.0 <= rhs}")
print("  fails at d=3. For any N_off>=1 it fails at some finite d. For N_off=0 it holds trivially.\n")

print("=== What the file does NOT do ===")
print("  - It never shows the actual Weil/spectral operator of zeta satisfies the bound")
print("    with finite C, C_on (that is the content of RH, assumed away).")
print("  - The same vacuous theorem 'proves' N_off=0 for Davenport-Heilbronn, Epstein")
print("    class-2, or any RH-false model — 'proves too much' in the strongest sense.")
print("\nVerdict: PROVEN (numerically above + structural inspection) — NOT a proof of RH.")
