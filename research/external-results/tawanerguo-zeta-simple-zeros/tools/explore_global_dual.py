#!/usr/bin/env python3
"""Non-rigorous reconnaissance for the global spectral-dual program.

This script is deliberately separate from the certificate.  It uses ordinary
binary64 arithmetic and SciPy optimization only to identify adverse periodic
patterns and to guide a future Bellman/interval proof.
"""
from __future__ import annotations

import math
import numpy as np
from scipy.optimize import minimize_scalar

SQRT2 = math.sqrt(2.0)
K0 = SQRT2 * math.sin(1.0 / SQRT2)


def kernel(x: np.ndarray | float) -> np.ndarray:
    x = np.asarray(x, dtype=float)
    z1 = np.pi * x - 1.0 / SQRT2
    z2 = np.pi * x + 1.0 / SQRT2
    return 0.5 * (np.sinc(z1 / np.pi) + np.sinc(z2 / np.pi)) / K0


def period_two_pair_energy(a: float, b: float, neighbor_cutoff: int = 1000) -> float:
    """2 sum_{r>=1} mean_i k(x_{i+r}-x_i)^2, truncated in r."""
    total = 0.0
    period = a + b
    for r in range(1, neighbor_cutoff + 1):
        if r % 2 == 0:
            distance = (r // 2) * period
            total += float(kernel(distance) ** 2)
        else:
            m = (r - 1) // 2
            total += 0.5 * (
                float(kernel(m * period + a) ** 2)
                + float(kernel(m * period + b) ** 2)
            )
    return 2.0 * total


def capacity_normalized_reward(gaps: list[float], radius: int = 6) -> float:
    """Periodic evaluation of the explicit witness in equation (5.2)."""
    gaps_array = np.asarray(gaps, dtype=float)
    period_points = len(gaps_array)
    distances = np.zeros((period_points, radius))
    running = np.zeros(period_points)
    for r in range(1, radius + 1):
        running = running + np.roll(gaps_array, -(r - 1))
        distances[:, r - 1] = running

    overlaps = np.abs(kernel(distances))
    vertex_mass = np.zeros(period_points)
    for r in range(1, radius + 1):
        vertex_mass += overlaps[:, r - 1]
        vertex_mass += np.roll(overlaps[:, r - 1], r)

    reward = 0.0
    for r in range(1, radius + 1):
        other_mass = np.roll(vertex_mass, -r)
        denominator = np.maximum(1.0, np.maximum(vertex_mass, other_mass))
        q = 2.0 * overlaps[:, r - 1] / denominator
        reward += float(np.sum(2.0 * q * overlaps[:, r - 1] - 0.5 * q * q))
    return reward / period_points


def main() -> None:
    rho = 0.673
    mean_gap = 1.0 / rho

    result = minimize_scalar(
        lambda a: period_two_pair_energy(a, 2.0 * mean_gap - a),
        bounds=(0.5, 2.0 * mean_gap - 0.5),
        method="bounded",
        options={"xatol": 1e-13},
    )
    a = float(result.x)
    b = 2.0 * mean_gap - a

    print("status=NONRIGOROUS_RECONNAISSANCE")
    print(f"density={rho:.15g}")
    print(f"period_two_gap_a={a:.15g}")
    print(f"period_two_gap_b={b:.15g}")
    print(f"truncated_pair_energy_per_point={result.fun:.15g}")
    print(f"range_6_capacity_reward_per_point={capacity_normalized_reward([a, b], 6):.15g}")
    print("warning=These values are not certified lower bounds.")


if __name__ == "__main__":
    main()
