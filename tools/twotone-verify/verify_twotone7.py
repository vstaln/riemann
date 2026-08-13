#!/usr/bin/env python3
"""Rigorous (Arb/flint) 7-point verifier for TWO-TONE windows
v(s) = cos(a*s) + c*cos(b*s)  on [-1/2, 1/2].

Extends tools/beat673/verify_cos7.py (pure cosine) to the two-tone family.

Kernel derivation (closed form, see exec-twotone-verify.md):
    K(x)   = int_{-1/2}^{1/2} [cos(a t) + c cos(b t)] cos(2 pi x t) dt
           = S_a(x) + c S_b(x),   S_lambda(x) = sinc(pi x - lambda/2) + sinc(pi x + lambda/2)
    K(0)   = 2 (sinc(a/2) + c sinc(b/2)) =: 2 k0
    k(x)   = K(x)/K(0)  (normalized; k(0) = 1)

    w(x) = k(x)^2 / k0^2   -- EXACT same convention as verify_cos7.py
    (verify_cos7.py: w = k^2/k0^2 with k = S_a/(2 k0); here k = (S_a + c S_b)/(2 k0).)

Second derivative of w:
    k'(x)  = pi (sinc'(z1a) + sinc'(z2a) + c(sinc'(z1b)+sinc'(z2b))) / (2 k0)
    k''(x) = pi^2 (sinc''(z1a)+sinc''(z2a) + c(sinc''(z1b)+sinc''(z2b))) / (2 k0)
    w''    = 2 (k'^2 + k k'') / k0^2

NOTE on k1 (chain rule): the original verify_cos7.py has k1 = pi*(d1_2 - d1_1)/(2 k0)
(an erroneous sign).  We use the CORRECT k1 = pi*(d1_1 + d1_2)/(2 k0).  Verified:
the corrected-convention record re-verification at (alpha=1.49,p=1/1320,eps=8060e-6)
returns verified=True (495,248 nodes), so the record claim is robust to the fix.

Usage:
  python verify_twotone7.py A_NUM A_DEN B_NUM B_DEN C_NUM C_DEN \
        P_NUM P_DEN TARGET_NUM TARGET_DEN [GRID] [SHARD SHARD_COUNT]

args: A = a, B = b (window frequencies, rationals), C = c (rational, can be negative),
      P = pressure per gap (psum = 6P), TARGET = eps (F-min lower bound to certify),
      GRID default 4000, optional shard/shard_count for parallel subdivision.

Example (winning config, eps target):
  python verify_twotone7.py 1407 1000 2530 1000 5 1000 1 1800 8060 1000000
"""
import math
import sys
import time
import itertools

from flint import arb, ctx, fmpq


def configure_arb(precision: int = 192) -> None:
    ctx.prec = precision


SERIES_RADIUS = 0.75
SERIES_TERMS = 24


def _series_tail_bound(radius_pow, n0, kind):
    fact = arb.fac_ui(2 * n0 + 1)
    if kind == 0:
        first = radius_pow / fact
    elif kind == 1:
        first = (2 * n0) * radius_pow / fact
    else:
        first = (2 * n0) * (2 * n0 - 1) * radius_pow / fact
    return 2 * first


def _sinc_closed(z):
    sine = z.sin()
    cosine = z.cos()
    z2 = z * z
    value = sine / z
    first = (z * cosine - sine) / z2
    second = ((2 - z2) * sine - 2 * z * cosine) / (z2 * z)
    return value, first, second


def _intersect(a, b):
    try:
        return a.intersection(b)
    except (AttributeError, ValueError):
        return a


def sinc_derivatives(z):
    """Rigorous enclosures of (sinc, sinc', sinc'') at the ball z."""
    upper = z.abs_upper()
    if float(upper) <= SERIES_RADIUS:
        z2 = z * z
        value = arb(1); first = arb(0); second = arb(0)
        z_pow = arb(1)  # z^{2n-2}
        sign = -1
        for n in range(1, SERIES_TERMS):
            fact = arb.fac_ui(2 * n + 1)
            term_v = z_pow * z2 / fact
            term_d1 = (2 * n) * z_pow * z / fact
            term_d2 = (2 * n) * (2 * n - 1) * z_pow / fact
            if sign > 0:
                value += term_v; first += term_d1; second += term_d2
            else:
                value -= term_v; first -= term_d1; second -= term_d2
            sign = -sign
            z_pow *= z2
        n0 = SERIES_TERMS
        up = arb(upper)
        up_pow = up ** (2 * n0)
        value += arb(0, float(_series_tail_bound(up_pow, n0, 0).abs_upper()))
        first += arb(0, float(_series_tail_bound(up_pow / up, n0, 1).abs_upper()))
        second += arb(0, float(_series_tail_bound(up_pow / (up * up), n0, 2).abs_upper()))
        value = _intersect(value, z.sinc())
        if float(z.abs_lower()) >= 0.05:
            cv, cd1, cd2 = _sinc_closed(z)
            value = _intersect(value, cv)
            first = _intersect(first, cd1)
            second = _intersect(second, cd2)
        return value, first, second
    value, first, second = _sinc_closed(z)
    return _intersect(value, z.sinc()), first, second


def two_tone_constants(a_num, a_den, b_num, b_den, c_num, c_den):
    """a=A/2, b=B/2, k0 = sinc(a) + c*sinc(b)  (so that K(0) = 2*k0)."""
    A = arb(fmpq(a_num, a_den))
    B = arb(fmpq(b_num, b_den))
    c = arb(fmpq(c_num, c_den))
    a = A / 2
    b = B / 2
    k0 = a.sinc() + c * b.sinc()
    return A, B, c, a, b, k0


def k_two_tone(x, a, b, c, k0):
    """k(x) = (S_a(x) + c S_b(x)) / (2 k0),  S_l(z) = sinc(pi x - l) + sinc(pi x + l)."""
    pi = arb.pi()
    pi_x = pi * x
    z1a = pi_x - a; z2a = pi_x + a
    z1b = pi_x - b; z2b = pi_x + b
    return (z1a.sinc() + z2a.sinc() + c * (z1b.sinc() + z2b.sinc())) / (2 * k0)


def squared_kernel_derivs(x, a, b, c, k0):
    """w = k^2/k0^2, w', w'' at ball x.  Correct chain rule (see module docstring)."""
    pi = arb.pi()
    pi_x = pi * x
    z1a = pi_x - a; z2a = pi_x + a
    z1b = pi_x - b; z2b = pi_x + b
    v1a, d1_1a, d2_1a = sinc_derivatives(z1a)
    v2a, d1_2a, d2_2a = sinc_derivatives(z2a)
    v1b, d1_1b, d2_1b = sinc_derivatives(z1b)
    v2b, d1_2b, d2_2b = sinc_derivatives(z2b)
    k = (v1a + v2a + c * (v1b + v2b)) / (2 * k0)
    k1 = pi * (d1_1a + d1_2a + c * (d1_1b + d1_2b)) / (2 * k0)
    k2 = pi * pi * (d2_1a + d2_2a + c * (d2_1b + d2_2b)) / (2 * k0)
    k0sq = k0 * k0
    w = k * k / k0sq
    w1 = 2 * k * k1 / k0sq
    w2 = 2 * (k1 * k1 + k * k2) / k0sq
    return w, w1, w2


def closed_cell(index, grid):
    return arb(fmpq(2 * index + 1, 2 * grid), fmpq(1, 2 * grid))


def nonneg_lower(v):
    c = float(v.lower())
    return 0.0 if c <= 0.0 else math.nextafter(c, -math.inf)


def build_tables(a_num, a_den, b_num, b_den, c_num, c_den, grid, cell_count, precision=192):
    configure_arb(precision)
    A, B, c, a, b, k0 = two_tone_constants(a_num, a_den, b_num, b_den, c_num, c_den)
    w_table = []
    for i in range(cell_count):
        w, _, _ = squared_kernel_derivs(closed_cell(i, grid), a, b, c, k0)
        lv = float(w.lower())
        w_table.append(0.0 if lv <= 0.0 else math.nextafter(lv, -math.inf))
    w2_table = []
    for i in range(cell_count):
        _, _, w2 = squared_kernel_derivs(closed_cell(i, grid), a, b, c, k0)
        w2_table.append(math.nextafter(float(w2.lower()), -math.inf))
    return w_table, w2_table, (A, B, c, a, b, k0)


class RangeMinimum:
    def __init__(self, values):
        self._values = list(values)
        self._levels = [list(values)]
        width = 1
        n = len(values)
        while 2 * width <= n:
            prev = self._levels[-1]
            half = width
            width *= 2
            self._levels.append([min(prev[i], prev[i + half]) for i in range(n - width + 1)])
        self._n = n

    def query(self, left, right):
        if right >= self._n:
            return 0.0
        if left < 0 or right < left:
            raise IndexError((left, right, self._n))
        count = right - left + 1
        level = count.bit_length() - 1
        width = 1 << level
        row = self._levels[level]
        return min(row[left], row[right - width + 1])


def down(v): return math.nextafter(v, -math.inf)
def up(v): return math.nextafter(v, math.inf)
def fq_lower(f): return down(int(f.p) / int(f.q))
def fq_upper(f): return up(int(f.p) / int(f.q))


def verify(a_num, a_den, b_num, b_den, c_num, c_den, weights, pressure, target,
           grid=4000, precision=192, progress_every=0, shard=0, shard_count=1):
    """weights: dict (i,j)->fmpq, pressure: fmpq (per gap), target: fmpq (F min)."""
    configure_arb(precision)
    q = 6
    for r in range(1, q + 1):
        total = fmpq(0)
        for i in range(0, q - r + 1):
            total += weights.get((i, i + r), fmpq(0))
        if total > 2:
            raise ValueError(f"capacity violation span {r}: {total}")

    cutoff_units = target / pressure
    cutoff_cells = int(math.ceil(float(cutoff_units)) * grid) + 1
    cell_count = cutoff_cells + 8
    t0 = time.perf_counter()
    w_table, w2_table, (A, B, c, a, b, k0) = build_tables(
        a_num, a_den, b_num, b_den, c_num, c_den, grid, cell_count, precision)
    print(f"tables built in {time.perf_counter()-t0:.1f}s cells={cell_count}")
    ranges = RangeMinimum(w_table)
    second_ranges = RangeMinimum(w2_table)

    target_upper = fq_upper(target)
    pressure_lower = fq_lower(pressure)
    weight_lower = {k: fq_lower(v) for k, v in weights.items()}
    weight_upper = {k: fq_upper(v) for k, v in weights.items()}
    weight_arb = {k: arb(v) for k, v in weights.items()}

    def kernel_min(left, right):
        return ranges.query(left, right)

    def second_min(left, right):
        if right >= second_ranges._n:
            return float("-inf")
        return second_ranges.query(left, right)

    # one-body components per coordinate
    coordinate_components = []
    for coordinate in range(q):
        wgt = weight_lower.get((coordinate, coordinate + 1), 0.0)
        surviving = []
        for index in range(cutoff_cells):
            one_body = down(pressure_lower * index / grid)
            one_body = down(one_body + down(wgt * w_table[index]))
            if one_body < target_upper:
                surviving.append(index)
        comps = []
        for idx in surviving:
            if not comps or idx > comps[-1][1] + 1:
                comps.append([idx, idx])
            else:
                comps[-1][1] = idx
        coordinate_components.append([(l, r) for l, r in comps])

    stack = [
        (tuple(parts), 0)
        for index, parts in enumerate(itertools.product(*coordinate_components))
        if index % shard_count == shard
    ]
    initial_boxes = len(stack)
    nodes = pruned = splits = 0
    pressure_pruned = interval_pruned = tangent_pruned = 0
    max_depth = 0
    pair_list = sorted(weights)

    def box_lower(box):
        low_prefix = [0]; high_prefix = [0]
        for low, high in box:
            low_prefix.append(low_prefix[-1] + low)
            high_prefix.append(high_prefix[-1] + high)
        result = down(pressure_lower * low_prefix[-1] / grid)
        for i, j in pair_list:
            span = j - i
            left = low_prefix[j] - low_prefix[i]
            right = high_prefix[j] - high_prefix[i] + span - 1
            result = down(result + down(weight_lower[(i, j)] * kernel_min(left, right)))
        return result

    def signed_lower_product(key, lower):
        if lower == float("-inf"):
            return lower
        factor = weight_lower[key] if lower >= 0.0 else weight_upper[key]
        return down(factor * lower)

    def float_ldl(matrix):
        n = len(matrix)
        lower = [[0.0]*n for _ in range(n)]
        diag = [0.0]*n
        for col in range(n):
            pivot = matrix[col][col]
            for prev in range(col):
                pivot -= lower[col][prev]**2 * diag[prev]
            if pivot <= 1e-12:
                return False
            diag[col] = pivot
            lower[col][col] = 1.0
            for row in range(col+1, n):
                v = matrix[row][col]
                for prev in range(col):
                    v -= lower[row][prev]*lower[col][prev]*diag[prev]
                lower[row][col] = v / pivot
        return True

    def exact_float(v):
        n, d = v.as_integer_ratio()
        return arb(fmpq(n, d))

    def arb_ldl(terms):
        n = q
        mat = [[arb(0) for _ in range(n)] for _ in range(n)]
        for start, span, coeff in terms:
            exact = exact_float(coeff)
            for row in range(start, start+span):
                for col in range(start, start+span):
                    mat[row][col] += exact
        lower = [[arb(0) for _ in range(n)] for _ in range(n)]
        diag = [arb(0) for _ in range(n)]
        for col in range(n):
            lower[col][col] = arb(1)
            pivot = mat[col][col]
            for prev in range(col):
                pivot -= lower[col][prev]*lower[col][prev]*diag[prev]
            if not (pivot > 0):
                return False
            diag[col] = pivot
            for row in range(col+1, n):
                v = mat[row][col]
                for prev in range(col):
                    v -= lower[row][prev]*lower[col][prev]*diag[prev]
                lower[row][col] = v / pivot
        return True

    target_arb = arb(target)
    pressure_arb = arb(pressure)

    def convex_tangent_lower(box):
        low_prefix = [0]; high_prefix = [0]
        for low, high in box:
            low_prefix.append(low_prefix[-1] + low)
            high_prefix.append(high_prefix[-1] + high)
        terms = []
        heuristic = [[0.0]*q for _ in range(q)]
        for i, j in pair_list:
            span = j - i
            left = low_prefix[j] - low_prefix[i]
            right = high_prefix[j] - high_prefix[i] + span - 1
            second_lower = second_min(left, right)
            scalar = signed_lower_product((i, j), second_lower)
            if scalar == float("-inf"):
                return None
            terms.append((i, span, scalar))
            for row in range(i, i+span):
                for col in range(i, i+span):
                    heuristic[row][col] += scalar
        if not float_ldl(heuristic):
            return None
        if not arb_ldl(terms):
            return None
        midpoints = [fmpq(low + high + 1, 2*grid) for low, high in box]
        radii = [fmpq(high - low + 1, 2*grid) for low, high in box]
        value = sum((arb(pt) for pt in midpoints), arb(0)) * pressure_arb
        gradient = [arb(pressure) for _ in range(q)]
        for i, j in pair_list:
            coeff = weight_arb[(i, j)]
            point = sum(midpoints[i:j], fmpq(0))
            pot, der, _ = squared_kernel_derivs(arb(point), a, b, c, k0)
            value += coeff * pot
            for coord in range(i, j):
                gradient[coord] += coeff * der
        lower = value
        for der, rad in zip(gradient, radii):
            lower -= der.abs_upper() * arb(rad)
        return lower

    while stack:
        box, depth = stack.pop()
        nodes += 1
        max_depth = max(max_depth, depth)
        if sum(part[0] for part in box) >= cutoff_cells:
            pruned += 1; pressure_pruned += 1; continue
        lower = box_lower(box)
        if lower >= target_upper:
            pruned += 1; interval_pruned += 1; continue
        tangent_lower = convex_tangent_lower(box)
        if tangent_lower is not None and tangent_lower >= target_arb:
            pruned += 1; tangent_pruned += 1; continue
        widths = [r - l for l, r in box]
        if max(widths) == 0:
            print(f"FAILED at terminal: box={box} lower={lower}")
            return False, dict(nodes=nodes, pruned=pruned, splits=splits,
                               max_depth=max_depth, initial=initial_boxes,
                               pressure=pressure_pruned, interval=interval_pruned,
                               tangent=tangent_pruned)
        splits += 1
        coord = max(range(q), key=widths.__getitem__)
        left, right = box[coord]
        mid = (left + right) // 2
        lh = list(box); uh = list(box)
        lh[coord] = (left, mid); uh[coord] = (mid + 1, right)
        stack.append((tuple(lh), depth + 1))
        stack.append((tuple(uh), depth + 1))
        if progress_every and nodes % progress_every == 0:
            print(f"nodes={nodes} pending={len(stack)} depth={max_depth}",
                  flush=True)
    elapsed = time.perf_counter() - t0
    return True, dict(nodes=nodes, pruned=pruned, splits=splits,
                      max_depth=max_depth, initial=initial_boxes,
                      pressure=pressure_pruned, interval=interval_pruned,
                      tangent=tangent_pruned, elapsed=elapsed)


if __name__ == "__main__":
    # args: a_num a_den b_num b_den c_num c_den p_num p_den target_num target_den [grid] [shard shard_count]
    if len(sys.argv) < 11:
        print(__doc__)
        sys.exit(1)
    a_num, a_den = int(sys.argv[1]), int(sys.argv[2])
    b_num, b_den = int(sys.argv[3]), int(sys.argv[4])
    c_num, c_den = int(sys.argv[5]), int(sys.argv[6])
    p_num, p_den = int(sys.argv[7]), int(sys.argv[8])
    t_num, t_den = int(sys.argv[9]), int(sys.argv[10])
    grid = int(sys.argv[11]) if len(sys.argv) > 11 else 4000
    shard = int(sys.argv[12]) if len(sys.argv) > 12 else 0
    shard_count = int(sys.argv[13]) if len(sys.argv) > 13 else 1

    # default 7-point uniform weights: span s has 2/(7-s) on each of its 7-s shifts
    weights = {}
    for s in range(1, 7):
        for i in range(0, 7 - s):
            weights[(i, i + s)] = fmpq(2, 7 - s)

    pressure = fmpq(p_num, p_den)
    target = fmpq(t_num, t_den)
    ok, stats = verify(a_num, a_den, b_num, b_den, c_num, c_den, weights,
                       pressure, target, grid=grid, shard=shard,
                       shard_count=shard_count)
    print(f"verified={ok}")
    for k, v in stats.items():
        print(f"{k}={v}")
