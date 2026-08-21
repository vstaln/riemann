#!/usr/bin/env python3
"""Exact interval verification of 7-point (and coboundary) floor inequalities.

Re-implements the branch-and-bound verification of
    F(g1..g6) >= target   for all g_i >= 0
in Arb (python-flint), following the ainta/trmdy/tawanerguo design:
  * kernel table: rigorous binary64 lower bounds for w(x)=k(x)^2 on
    cells [i/grid, (i+1)/grid] via Arb interval enclosure of k on the cell;
  * range-minimum sparse table;
  * branch-and-bound over 6D cell boxes, pruning by the one-coordinate
    term U(g)=p g + q w(g), the interval lower bound, and the
    convex-tangent lower bound (arb, exact LDL) when convexity certifies.

This is a *re-implementation* from the published formulas (not a copy of any
repo verifier).  It is intended to certify F_B at candidate parameters where
the float probe found a higher floor.

Usage:
    uv run --with mpmath --with python-flint python tools/verify_coboundary_floor.py
"""

from __future__ import annotations

import hashlib
import itertools
import math
import struct
import sys
import time

from flint import arb, fmpq, ctx


def configure(prec: int = 128) -> None:
    ctx.prec = prec


# ---------------------------------------------------------------------------
# Kernel in Arb
# ---------------------------------------------------------------------------

def _sinc(z):
    return z.sinc()


class KernelArb:
    """K(x) = sum_j c_j (sinc((w_j-2pi x)/2)+sinc((w_j+2pi x)/2))/2."""

    def __init__(self, coeffs, omegas):
        self.coeffs = [arb(c) for c in coeffs]
        self.omegas = [arb(w) for w in omegas]
        k0 = arb(0)
        for c, w in zip(self.coeffs, self.omegas):
            k0 += c * 2 * (w / 2).sin() / w
        self.k0 = k0
        self.k0sq = k0 * k0

    def K(self, x):
        pi = arb.pi()
        total = arb(0)
        for c, w in zip(self.coeffs, self.omegas):
            a = (w - 2 * pi * x) / 2
            b = (w + 2 * pi * x) / 2
            total += c * (_sinc(a) + _sinc(b)) / 2
        return total

    def w_lower_on_cell(self, index, grid):
        """Rigorous lower bound of w = (K/K0)^2 on cell index."""
        cell = arb(fmpq(2 * index + 1, 2 * grid), fmpq(1, 2 * grid))
        k = self.K(cell)
        ratio = (k / self.k0).abs_upper() if False else (k / self.k0)
        low = ratio.abs_lower()
        if low <= 0:
            return 0.0
        return math.nextafter(low * low, -math.inf)

    def w_second_enclosure_on_cell(self, index, grid):
        """Rigorous [lower, upper] enclosure of w'' on cell index (floats)."""
        cell = arb(fmpq(2 * index + 1, 2 * grid), fmpq(1, 2 * grid))
        k, k1, k2 = self.kernel_derivatives(cell)
        second = 2 * (k1 * k1 + k * k2) / self.k0sq
        lo = math.nextafter(float(second.lower()), -math.inf)
        up = math.nextafter(float(second.upper()), math.inf)
        return lo, up

    def w_second_lower_on_cell(self, index, grid):
        """Rigorous lower bound of w'' = (k^2/k0^2)'' on cell index."""
        return self.w_second_enclosure_on_cell(index, grid)[0]

    def w_second_upper_on_cell(self, index, grid):
        """Rigorous upper bound of w'' on cell index."""
        return self.w_second_enclosure_on_cell(index, grid)[1]

    def kernel_derivatives(self, x):
        """Arb enclosures of K, K', K'' at ball x."""
        pi = arb.pi()
        two_pi_x = 2 * pi * x
        value = arb(0)
        first = arb(0)
        second = arb(0)
        for c, w in zip(self.coeffs, self.omegas):
            z_minus = (w - two_pi_x) / 2
            z_plus = (w + two_pi_x) / 2
            v_m, d1_m, d2_m = sinc_derivatives(z_minus)
            v_p, d1_p, d2_p = sinc_derivatives(z_plus)
            value += c * (v_m + v_p) / 2
            first += c * pi * (d1_p - d1_m) / 2
            second += c * pi * pi * (d2_m + d2_p) / 2
        return value, first, second

    def w_point(self, x):
        k = self.K(arb(x))
        return (k / self.k0) ** 2


def sinc_derivatives(z):
    """sinc, sinc', sinc'' via Arb's built-in sinc and its closed forms."""
    value = z.sinc()
    z2 = z * z
    first = (z * z.cos() - z.sin()) / z2
    second = ((2 - z2) * z.sin() - 2 * z * z.cos()) / (z2 * z)
    return value, first, second


def cosine_kernel(alpha):
    return KernelArb([1.0], [float(alpha)])


def mt_kernel():
    return KernelArb([1.0], [math.sqrt(2)])


def trmdy_kernel():
    c = [1_000_000_000, 3_322_500, -7_609_135, 1_190_194, -731_476, -1_680_572, 1_141_360]
    oms = [math.sqrt(2)] + [2 * math.pi * j for j in range(1, 7)]
    return KernelArb(c, oms)


# ---------------------------------------------------------------------------
# Range minimum
# ---------------------------------------------------------------------------

class RangeMinimum:
    def __init__(self, values):
        self.length = len(values)
        self._levels = [list(values)]
        width = 1
        while 2 * width <= self.length:
            prev = self._levels[-1]
            half = width
            width *= 2
            self._levels.append([min(prev[i], prev[i + half]) for i in range(self.length - width + 1)])

    def query(self, left, right):
        if left < 0 or right < left or right >= self.length:
            raise IndexError((left, right, self.length))
        level = (right - left + 1).bit_length() - 1
        width = 1 << level
        row = self._levels[level]
        return min(row[left], row[right - width + 1])


def table_sha256(values):
    d = hashlib.sha256()
    for v in values:
        d.update(struct.pack(">d", v))
    return d.hexdigest()


# ---------------------------------------------------------------------------
# Branch-and-bound verifier
# ---------------------------------------------------------------------------

def _down(v):
    return math.nextafter(v, -math.inf)


def _up(v):
    return math.nextafter(v, math.inf)


def verify_floor(kernel, weights, pressure, q, target, grid=4000,
                 precision=128, cap_scheme="h", use_tangent=True,
                 pressure_coeffs=None, nearest_coeffs=None, max_nodes=None,
                 progress_every=0):
    """Verify F(g) >= target.

    weights: dict (i,j) -> a_ij (float, exact rationals as floats)
    pressure: float p in the one-gap term p*sum g
    q: number of gaps (6)
    cap_scheme: 'h' (uniform 7-pt block cap) or 'coboundary' (use
                pressure_coeffs/nearest_coeffs redistributed design)
    pressure_coeffs: list of 6 floats for the redistributed p_i
    nearest_coeffs:  list of 6 floats for the redistributed q_i (w(g_i) terms)
    """
    configure(precision)
    q = int(q)
    cutoff_units = target / pressure
    cutoff_cells = int(math.ceil(_up(cutoff_units) * grid)) + 1
    cell_count = cutoff_cells + 8
    print(f"  grid={grid} cutoff_cells={cutoff_cells} cell_count={cell_count}")

    t0 = time.time()
    table = [kernel.w_lower_on_cell(i, grid) for i in range(cell_count)]
    print(f"  kernel table built in {time.time()-t0:.1f}s sha={table_sha256(table)[:16]}")
    ranges = RangeMinimum(table)
    t0 = time.time()
    second_lo = [kernel.w_second_lower_on_cell(i, grid) for i in range(cell_count)]
    second_up = [kernel.w_second_upper_on_cell(i, grid) for i in range(cell_count)]
    print(f"  second-derivative tables (lo+up) built in {time.time()-t0:.1f}s")
    second_ranges = RangeMinimum(second_lo)          # range-min of w''
    second_ranges_negup = RangeMinimum([-u for u in second_up])  # range-max of w''

    target_upper = _up(target)
    pressure_lower = _down(pressure)

    # One-coordinate pruning: U(g) = p g + a_{i,i+1} w(g) or the
    # redistributed p_i g + q_i w(g).
    def one_body(i, gcell):
        if cap_scheme == "coboundary":
            p_i = pressure_coeffs[i]
            q_i = nearest_coeffs[i]
        else:
            p_i = pressure
            q_i = weights.get((i, i + 1), 0.0)
        val = _down(p_i * gcell / grid)
        # w(g) lower bound over cell gcell
        wl = table[gcell] if gcell < len(table) else 0.0
        val = _down(val + _down(q_i * wl))
        return val

    components = []
    for i in range(q):
        surviving = []
        for index in range(cutoff_cells):
            if one_body(i, index) < target_upper:
                surviving.append(index)
        # group into contiguous components
        comps = []
        for idx in surviving:
            if comps and idx == comps[-1][1] + 1:
                comps[-1][1] = idx
            else:
                comps.append([idx, idx])
        components.append([(a, b) for a, b in comps])
        print(f"  coord {i}: {len(components[i])} components: "
              f"{[(a,b) for a,b in components[i][:4]]}...")

    # Build initial boxes: cartesian product of components (may be large;
    # cap at some number for the probe).
    pair_list = sorted(weights)
    initial = list(itertools.product(*components))
    print(f"  initial boxes: {len(initial)}")

    def box_lower(box):
        low_prefix = [0]
        high_prefix = [0]
        for low, high in box:
            low_prefix.append(low_prefix[-1] + low)
            high_prefix.append(high_prefix[-1] + high)
        if cap_scheme == "coboundary":
            # F_B = sum_i p_i g_i + sum_i q_i w(g_i)
            #       + sum_{i<j} a_ij w(y_j - y_i)   (uniform a_ij)
            result = 0.0
            for i in range(q):
                p_i = pressure_coeffs[i]
                result = _down(result + _down(p_i * (low_prefix[i + 1] - low_prefix[i]) / grid))
            for i in range(q):
                q_i = nearest_coeffs[i]
                low_i, high_i = box[i]
                if high_i < ranges.length:
                    result = _down(result + _down(q_i * ranges.query(low_i, high_i)))
            for i, j in pair_list:
                span = j - i
                left = low_prefix[j] - low_prefix[i]
                right = high_prefix[j] - high_prefix[i] + span - 1
                if right >= ranges.length:
                    continue
                result = _down(result + _down(weights[(i, j)] * ranges.query(left, right)))
            return result
        result = _down(pressure_lower * low_prefix[-1] / grid)
        for i, j in pair_list:
            span = j - i
            left = low_prefix[j] - low_prefix[i]
            right = high_prefix[j] - high_prefix[i] + span - 1
            if right >= ranges.length:
                continue
            result = _down(result + _down(weights[(i, j)] * ranges.query(left, right)))
        return result

    stack = initial
    nodes = pruned_interval = pruned_pressure = pruned_tangent = splits = 0
    depth = 0
    t_start = time.time()
    while stack:
        box = stack.pop()
        nodes += 1
        if max_nodes and nodes > max_nodes:
            return {"verified": False, "nodes": nodes, "status": "node-limit",
                    "reason": f"node limit {max_nodes} hit"}
        if progress_every and nodes % progress_every == 0:
            print(f"  nodes={nodes} splits={splits} depth={depth} "
                  f"pruned_i={pruned_interval} pruned_p={pruned_pressure} "
                  f"pruned_t={pruned_tangent} pending={len(stack)}", flush=True)

        # pressure prune: sum of gap lower bounds beyond cutoff
        if sum(part[0] for part in box) >= cutoff_cells:
            pruned_pressure += 1
            continue

        low = box_lower(box)
        if low >= target_upper:
            pruned_interval += 1
            continue

        # convex tangent prune (only if enabled; uses arb, exact LDL)
        if use_tangent:
            tl = tangent_lower(box, kernel, weights, pressure, grid,
                               pressure_coeffs, nearest_coeffs, cap_scheme,
                               second_ranges, second_ranges_negup)
            if tl is not None and tl >= arb(target):
                pruned_tangent += 1
                continue

        widths = [r - l for l, r in box]
        if max(widths) == 0:
            return {"verified": False, "nodes": nodes, "status": "terminal-cell",
                    "reason": f"unresolved terminal cell {box} low={low}"}
        splits += 1
        coord = max(range(q), key=widths.__getitem__)
        left, right = box[coord]
        mid = (left + right) // 2
        lo_box = list(box); hi_box = list(box)
        lo_box[coord] = (left, mid)
        hi_box[coord] = (mid + 1, right)
        stack.append(tuple(lo_box))
        stack.append(tuple(hi_box))

    elapsed = time.time() - t_start
    return {"verified": True, "nodes": nodes, "splits": splits,
            "pruned_interval": pruned_interval, "pruned_pressure": pruned_pressure,
            "pruned_tangent": pruned_tangent, "elapsed": elapsed}


def tangent_lower(box, kernel, weights, pressure, grid,
                  pressure_coeffs, nearest_coeffs, cap_scheme,
                  second_ranges=None, second_ranges_negup=None):
    """Arb convex-tangent lower bound; None if convexity not certified.

    SOUND convexity certificate (2026-08-21 fix; the previous LDL-on-lower-bounds
    certificate was INVALID: M built from entrywise lower bounds of w'' can be PD
    while the true Hessian is indefinite, since H = M + N with N >= 0 entrywise
    does not preserve positive definiteness — e.g. M=I, N=[[0,2],[2,0]]).

    Sound test (Weyl/Gershgorin): with H the true interval Hessian,
        lambda_min(H) >= min_i( H_ii^lo - sum_{j!=i} |H_ij|^up ) > 0
    where H_ii^lo uses w'' lower bounds (all coefficients positive) and
    |H_ij|^up uses max(|w''_lo|, |w''_up|) over the covering spans.
    Only when this holds is F convex on the box and the tangent plane at the
    midpoint minus the gradient-radius term a valid lower bound.
    """
    q = len(box)
    pair_list = sorted(weights)
    low_prefix = [0]
    high_prefix = [0]
    for low, high in box:
        low_prefix.append(low_prefix[-1] + low)
        high_prefix.append(high_prefix[-1] + high)

    def span_lo(left, right):
        return second_ranges.query(left, right)

    def span_absup(left, right):
        lo = second_ranges.query(left, right)
        up = -second_ranges_negup.query(left, right)
        return max(abs(lo), abs(up))

    if second_ranges is None or second_ranges_negup is None:
        return None

    # --- interval Hessian bounds
    diag_lo = [0.0] * q
    off_abs = [[0.0] * q for _ in range(q)]
    for i, j in pair_list:
        span = j - i
        left = low_prefix[j] - low_prefix[i]
        right = high_prefix[j] - high_prefix[i] + span - 1
        if right >= second_ranges.length:
            return None
        if span_lo(left, right) == float("-inf"):
            return None
        a_ij = weights[(i, j)]
        s_lo = _down(a_ij * span_lo(left, right))
        s_abs = _up(a_ij * span_absup(left, right))
        for a in range(i, i + span):
            diag_lo[a] += s_lo
            for b in range(i, i + span):
                if a != b:
                    off_abs[a][b] += s_abs
    if cap_scheme == "coboundary":
        for i in range(q):
            low_i, high_i = box[i]
            if high_i >= second_ranges.length:
                return None
            if span_lo(low_i, high_i) == float("-inf"):
                return None
            diag_lo[i] += _down(nearest_coeffs[i] * span_lo(low_i, high_i))

    # SOUND positive-definiteness certificate (Gershgorin-type)
    for i in range(q):
        if diag_lo[i] - sum(off_abs[i]) <= 0:
            return None

    # tangent plane at midpoint
    midpoints = [fmpq(low + high + 1, 2 * grid) for low, high in box]
    radii = [fmpq(high - low + 1, 2 * grid) for low, high in box]
    value = arb(0)
    gradient = [arb(0) for _ in range(q)]
    # linear pressure terms
    if cap_scheme == "coboundary":
        for i in range(q):
            value += arb(pressure_coeffs[i]) * arb(midpoints[i])
            gradient[i] += arb(pressure_coeffs[i])
    else:
        for i in range(q):
            value += arb(pressure) * arb(midpoints[i])
            gradient[i] += arb(pressure)
    for i, j in pair_list:
        coeff = arb(weights[(i, j)])
        point = sum(midpoints[i:j], fmpq(0))
        potential, derivative, _ = squared_kernel_derivatives(arb(point), kernel)
        value += coeff * potential
        for coordinate in range(i, j):
            gradient[coordinate] += coeff * derivative
    if cap_scheme == "coboundary":
        for i in range(q):
            q_i = arb(nearest_coeffs[i])
            potential, derivative, _ = squared_kernel_derivatives(arb(midpoints[i]), kernel)
            value += q_i * potential
            gradient[i] += q_i * derivative

    lower = value
    for derivative, radius in zip(gradient, radii):
        lower -= derivative.abs_upper() * arb(radius)
    return lower


def _arb_ldl_positive(terms, q):
    matrix = [[arb(0) for _ in range(q)] for _ in range(q)]
    for start, span, coefficient in terms:
        exact = arb(coefficient) if not isinstance(coefficient, arb) else coefficient
        for row in range(start, start + span):
            for column in range(start, start + span):
                matrix[row][column] += exact
    lower = [[arb(0) for _ in range(q)] for _ in range(q)]
    diagonal = [arb(0) for _ in range(q)]
    for column in range(q):
        lower[column][column] = arb(1)
        pivot = matrix[column][column]
        for previous in range(column):
            pivot -= lower[column][previous] * lower[column][previous] * diagonal[previous]
        if not (pivot > 0):
            return False
        diagonal[column] = pivot
        for row in range(column + 1, q):
            value = matrix[row][column]
            for previous in range(column):
                value -= lower[row][previous] * lower[column][previous] * diagonal[previous]
            lower[row][column] = value / pivot
    return True


def squared_kernel_derivatives(x, kernel):
    k, k1, k2 = kernel.kernel_derivatives(x)
    value = k * k / kernel.k0sq
    first = 2 * k * k1 / kernel.k0sq
    second = 2 * (k1 * k1 + k * k2) / kernel.k0sq
    return value, first, second


# ---------------------------------------------------------------------------
# Main: probe candidates
# ---------------------------------------------------------------------------

def main():
    # Parameterized mode (driven from Rust via env vars; no numeric logic added —
    # this is argument plumbing only). Set VERIFY_ALPHA, VERIFY_TARGET, and any of
    # VERIFY_PRESSURE, VERIFY_LAMBDA, VERIFY_GRID, VERIFY_MAX_NODES, VERIFY_P1..P6,
    # VERIFY_Q1..Q6 (coeffs given in raw form, scaled by VERIFY_LAMBDA when set).
    import os
    if "VERIFY_ALPHA" in os.environ and "VERIFY_TARGET" in os.environ:
        alpha = float(os.environ["VERIFY_ALPHA"])
        target = float(os.environ["VERIFY_TARGET"])
        grid = int(os.environ.get("VERIFY_GRID", "4000"))
        max_nodes = int(os.environ.get("VERIFY_MAX_NODES", "8000000"))
        pressure = float(os.environ.get("VERIFY_PRESSURE", "1")) / 3000.0
        lam = float(os.environ.get("VERIFY_LAMBDA", "1"))
        w_uniform = {(i, j): 2.0 / (7 - (j - i)) for i in range(7) for j in range(i + 1, 7)}
        p_coeff, q_coeff = None, None
        if "VERIFY_P1" in os.environ:
            p_raw = [float(os.environ[f"VERIFY_P{i}"]) for i in range(1, 7)]
            p_coeff = [lam * c / 1_920_000 for c in p_raw]
        if "VERIFY_Q1" in os.environ:
            q_raw = [float(os.environ[f"VERIFY_Q{i}"]) for i in range(1, 7)]
            q_coeff = [lam * c for c in q_raw]
        ktw = cosine_kernel(alpha)
        r = verify_floor(ktw, w_uniform, pressure, 6, target,
                         grid=grid, cap_scheme="coboundary",
                         pressure_coeffs=p_coeff, nearest_coeffs=q_coeff,
                         max_nodes=max_nodes, progress_every=int(os.environ.get("VERIFY_PROGRESS_EVERY", "0")))
        import json
        print("VERIFY_RESULT " + json.dumps({k: r.get(k) for k in
              ("verified", "nodes", "status", "reason", "pruned_interval",
               "pruned_pressure", "pruned_tangent")}))
        return
    # sanity: ainta 7-pt (MT kernel, uniform weights, p=1/3000, target 19/5000)
    print("=" * 70)
    print("SANITY: ainta 7-pt (uniform, MT)")
    print("=" * 70)
    kmt = mt_kernel()
    w_uniform = {(i, j): 2.0 / (7 - (j - i)) for i in range(7) for j in range(i + 1, 7)}
    r = verify_floor(kmt, w_uniform, 1.0 / 3000, 6, 19.0 / 5000,
                     grid=4000, max_nodes=5_000_000)
    print(r)

    # --- tawan baseline: cosine 1.47, redistributed F_B, target 577/1e5 ---
    print("=" * 70)
    print("TAWAN BASELINE: cosine 1.47, coboundary, target 577/1e5")
    print("=" * 70)
    ktw = cosine_kernel(1.47)
    p_coeff = [946, 1177, 877, 877, 1177, 946]
    p_coeff = [c / 1_920_000 for c in p_coeff]
    q_coeff = [31343 / 100_000, 1 / 3, 105971 / 300_000, 105971 / 300_000,
               1 / 3, 31343 / 100_000]
    r = verify_floor(ktw, w_uniform, 1.0 / 3000, 6, 577.0 / 100_000,
                     grid=4000, cap_scheme="coboundary",
                     pressure_coeffs=p_coeff, nearest_coeffs=q_coeff,
                     max_nodes=5_000_000)
    print(r)


if __name__ == "__main__":
    main()
