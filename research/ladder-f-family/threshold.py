#!/usr/bin/env python3
"""Validation of the generalized ladder deduction + threshold analysis.

Generalized deduction (trmdy proof.md §4, n points / q=n-1 gaps):
  F_n(g) = p*sum g_i + sum_{i<j} a_ij w(y_j-y_i) >= eps  (all g >= 0),
  uniform weights a_ij = 2/(n-(j-i)), span capacities exactly 2.
  Block of m consecutive simple zeros, q = n-1:
    A = eps*(m-q),  R = A (A<=1, unit cap) else 2*sqrt(A)-1,
    eta = R/A,  B_p = q*p = (n-1)*p,
    bound = (m*H - eta*B_p*(m-1)) / (m - R).

(1) Reproduces trmdy's certified 0.6731376306993446 at n=7, eps=1/200, m=257,
    and ainta's 0.673008527927 at their params (gate validation).
(2) For each n, computes the eps* (at each m) needed to reach
    tawanerguo's 0.6731929114731422.

Usage: uv run --quiet --with mpmath python threshold.py
"""
import math

H_CERT = 0.6724570414145443  # trmdy certified H(v)
TAWANERGUO = 0.6731929114731422


def bound(n: int, eps: float, m: int, p: float = 1.0 / 2300.0) -> float:
    q = n - 1
    B_p = q * p
    A = eps * (m - q)
    if A <= 1.0:
        R = A
    else:
        R = 2.0 * math.sqrt(A) - 1.0
    eta = R / A
    return (m * H_CERT - eta * B_p * (m - 1)) / (m - R)


def main() -> None:
    # (1) reproduce trmdy
    b = bound(7, 1.0 / 200.0, 257)
    print(f"trmdy repro: bound(7, 1/200, 257) = {b:.16f}  "
          f"(expect 0.6731376306993446)")
    # ainta gate: MT window H0, unit cap, eps=19/5000, p=1/3000, m=269
    H0 = 0.6725007036794116
    q, eps_a, p_a, m_a = 6, 19.0 / 5000.0, 1.0 / 3000.0, 269
    A = eps_a * (m_a - q)
    assert A < 1.0
    B_p = q * p_a
    b_ainta = (m_a * H0 - B_p * (m_a - 1)) / (m_a - A)
    print(f"ainta repro: bound = {b_ainta:.16f}  (expect 0.673008527927)")

    # (2) thresholds: eps* such that bound(n, eps*, m) >= TAWANERGUO
    print("\n--- eps* to beat tawanerguo 0.6731929114731422 ---")
    for n in [7, 9, 11, 15]:
        q = n - 1
        best_eps = None
        best_m = 0
        best_b = 0.0
        for m in range(q + 1, 5000):
            # bisect eps in (0, 0.1]
            lo, hi = 0.0, 0.1
            for _ in range(80):
                mid = 0.5 * (lo + hi)
                if bound(n, mid, m) >= TAWANERGUO:
                    hi = mid
                else:
                    lo = mid
            if hi < 0.1:
                if best_eps is None or hi < best_eps:
                    best_eps = hi
                    best_m = m
                    best_b = bound(n, hi, m)
        print(f"n={n:2d}: min eps* = {best_eps:.8f} at m={best_m} "
              f"(bound={best_b:.10f})")
        # show a few eps values at a practical m
        print(f"       bound at eps=0.005, m=200: {bound(n, 0.005, 200):.10f}")
        print(f"       bound at eps=0.007, m=200: {bound(n, 0.007, 200):.10f}")
        print(f"       bound at eps=0.010, m=200: {bound(n, 0.010, 200):.10f}")


if __name__ == "__main__":
    main()
