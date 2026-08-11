#!/usr/bin/env python3
"""Driver: certify coboundary-floor targets at candidate windows.

Usage:
  uv run --with mpmath --with python-flint python tools/cert_floor_driver.py \
      --alpha 1.55 --target 0.007

Tries to certify  F_B(g1..g6) >= target  for the cosine window v=cos(alpha s)
with the tawanerguo redistributed coboundary design (p_i, q_i coefficients).
Also prints H(alpha) and the joint bound at m=183 for comparison.

The interval certificate is the ground truth: if it verifies, the floor
inequality is CERTIFIED at that target.
"""

from __future__ import annotations

import argparse
import math
import sys

from verify_coboundary_floor import (
    cosine_kernel,
    verify_floor,
    mt_kernel,
)

# tawanerguo redistributed coefficients
P_COEFF = [946, 1177, 877, 877, 1177, 946]
P_COEFF = [c / 1_920_000 for c in P_COEFF]
Q_COEFF = [31343 / 100_000, 1 / 3, 105971 / 300_000, 105971 / 300_000,
           1 / 3, 31343 / 100_000]

W_UNIFORM = {(i, j): 2.0 / (7 - (j - i)) for i in range(7) for j in range(i + 1, 7)}


def H_cos(alpha):
    """H(alpha) in float (matches mpmath to ~1e-15)."""
    a = alpha
    i0 = 2 * math.sin(a / 2) / a
    i2 = 0.5 + math.sin(a) / (2 * a)
    const = math.sin(a / 2) / a + 2 * math.cos(a / 2) / (a * a)
    jv = -2 * i2 / (a * a) + const * i0
    c = i0 * i0 / (i2 + jv)
    return 2 - 1 / c


def phi_m(A, m):
    if A <= m / (m - 1):
        return A
    return 2 * math.sqrt((m - 1) * A / m) - 1 + A / m


def joint_bound(H, eps_local, m, tax):
    A = eps_local * (m - 6)
    B = phi_m(A, m)
    return (H - tax) / (1 - B / m)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--alpha", type=float, required=True)
    ap.add_argument("--target", type=float, required=True)
    ap.add_argument("--grid", type=int, default=4000)
    ap.add_argument("--max-nodes", type=int, default=8_000_000)
    args = ap.parse_args()

    H = H_cos(args.alpha)
    print(f"alpha={args.alpha}  H(alpha)={H:.12f}")
    print(f"target={args.target}  (tawan certified floor 0.00577 at alpha=1.47)")

    k = cosine_kernel(args.alpha)
    r = verify_floor(k, W_UNIFORM, 1.0 / 3000, 6, args.target,
                     grid=args.grid, cap_scheme="coboundary",
                     pressure_coeffs=P_COEFF, nearest_coeffs=Q_COEFF,
                     max_nodes=args.max_nodes)
    print("RESULT:", r)
    if r["verified"]:
        # joint bound: tax = (m-6)/(320 m) (sum p_i = 1/320), A = eps*(m-6),
        # B = Phi_m(A), bound = (H - tax)/(1 - B/m).
        best = None
        for m in range(64, 601, 1):
            A = args.target * (m - 6)
            B = phi_m(A, m)
            tax = (m - 6) / (320.0 * m)
            bb = (H - tax) / (1 - B / m)
            if best is None or bb > best[1]:
                best = (m, bb)
        b183 = (H - 59 / 19520) / (1 - phi_m(args.target * 177, 183) / 183)
        print(f"CERTIFIED: F_B >= {args.target} at alpha={args.alpha}")
        print(f"joint bound best (m={best[0]}): {best[1]:.15f}")
        print(f"joint bound (m=183, tax=59/19520): {b183:.15f}")
        print(f"  vs tawan committed 0.6731929114731423")
    else:
        print("NOT certified at this target:", r.get("status"), r.get("reason"))


if __name__ == "__main__":
    main()
