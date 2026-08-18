#!/usr/bin/env python3
"""gramlam_check.py — Báez-Duarte Gram λ_min scaling test (wave-22 verifier g1-0 check).

Question: for G_N(j,k) = <rho_{1/j}, rho_{1/k}> over j,k in 2..=N, what is the
scaling of λ_min(G_N)?  The wave-22 executor claimed diagonal dominance of
D_N G_N D_N (D_N = diag(sqrt(log k))) gives λ_min(G_N) >= c/log N and hence
d_N^2 <= C/log N.  The verifier corrected the scaling to c/(log N)^2 and noted
D_N's zero first entry (log 1 = 0) kills strict diagonal dominance.

This script measures the actual scaling with a faithful port of the trusted
wave8c Gram closed-form (including the m in 1..4 middle loop) and mpmath's
direct symmetric eigensolver (eigsy).

Usage: uv run --quiet --with mpmath python3 tools/wave8c/gramlam_check.py
"""
import math
import sys
import mpmath as mp
sys.stdout.reconfigure(line_buffering=True)

mp.mp.dps = 30


def lcm(a, b):
    x, y = a, b
    while y:
        x, y = y, x % y
    return a // x * b


def intervals(j, k, l):
    end = 1 + l
    pts = set()
    m = 1
    while m * j <= end:
        if m * j > 1:
            pts.add(m * j)
        m += 1
    m = 1
    while m * k <= end:
        if m * k > 1:
            pts.add(m * k)
        m += 1
    pts = sorted(pts)
    ivs = []
    cur = 1
    for p in pts:
        if p > cur:
            ivs.append((cur, p, cur // j, cur // k))
            cur = p
    if cur < end:
        ivs.append((cur, end, cur // j, cur // k))
    return ivs


def z_table(pmax):
    n1 = 10000
    z = []
    for p in range(pmax):
        s = p + 2
        acc = mp.mpf(0)
        for m in range(4, n1 + 1):
            acc += mp.mpf(m) ** (-s)
        x = mp.mpf(n1)
        acc += x ** (1 - s) / (s - 1) - mp.mpf("0.5") * x ** (-s) \
            + (s / 12) * x ** (-s - 1) - (s * (s + 1) * (s + 2) / 720) * x ** (-s - 3)
        z.append(acc)
    return z


Z = z_table(60)


def gram(j, k):
    l = lcm(j, k)
    ivs = intervals(j, k, l)
    lf = mp.mpf(l)
    jf = mp.mpf(j)
    kf = mp.mpf(k)
    tot = mp.mpf(0)
    for (x1, x2, ai, bi) in ivs:
        a = mp.mpf(x1)
        b = mp.mpf(x2)
        aif = mp.mpf(ai)
        bif = mp.mpf(bi)
        c2 = 1 / (jf * kf)
        c1 = -(aif / kf + bif / jf)
        c0 = aif * bif
        tot += c2 * (b - a) + c1 * (mp.log(b) - mp.log(a)) + c0 * (1 / a - 1 / b)
        # middle m-loop (1..4) — the piece my first draft omitted
        for m in (1, 2, 3):
            ml = m * lf
            v1 = a / ml
            v2 = b / ml
            c2p = ml * ml / (jf * kf)
            c1p = -ml * (aif / kf + bif / jf)
            c0p = aif * bif
            tot += (
                c2p * (v2 - 2 * mp.log(v2 + 1) - 1 / (v2 + 1) - (v1 - 2 * mp.log(v1 + 1) - 1 / (v1 + 1)))
                + c1p * (mp.log(v2 + 1) + 1 / (v2 + 1) - (mp.log(v1 + 1) + 1 / (v1 + 1)))
                + c0p * (-1 / (v2 + 1) + 1 / (v1 + 1))
            ) / ml
        bl = b / lf
        al = a / lf
        pb1 = bl
        pa1 = al
        for p in range(60):
            pb2 = pb1 * bl
            pa2 = pa1 * al
            pb3 = pb2 * bl
            pa3 = pa2 * al
            d1 = pb1 - pa1
            d2 = pb2 - pa2
            d3 = pb3 - pa3
            pf = p
            sign = 1 if p % 2 == 0 else -1
            t1 = c2 * lf * d3 / (pf + 3)
            t2 = c1 * d2 / (pf + 2)
            t3 = c0 * d1 / lf / (pf + 1)
            tot += sign * (pf + 1) * Z[p] * (t1 + t2 + t3)
            pb1 = pb2
            pa1 = pa2
    return tot


def eig_min(M):
    res, _ = mp.eigsy(M)
    return min(float(res[i, 0]) for i in range(res.rows))


def main():
    # validate the port against trusted values
    assert abs(gram(1, 1) - mp.mpf("0.2606614015078126")) < mp.mpf("1e-10"), gram(1, 1)
    print("port validated: G(1,1) matches trusted 0.2606614015")

    rows = []
    for n in (12, 15, 18, 24, 30, 40):
        dim = n - 1
        G = [[gram(i + 2, j + 2) for j in range(dim)] for i in range(dim)]
        M = mp.matrix(G)
        D = mp.matrix(dim, dim)
        for i in range(dim):
            D[i, i] = mp.sqrt(mp.log(mp.mpf(i + 2)))
        MD = D * M * D
        lg = eig_min(M)
        ld = eig_min(MD)
        ln = math.log(n)
        rows.append((n, lg, ld, ln))
        print(
            f"N={n:>3}  lmin(G)={lg:.6e}  *logN={lg*ln:.4f}  *(logN)^2={lg*ln*ln:.4f}"
            f"   lmin(DGD)={ld:.6e}  *logN={ld*ln:.4f}  *(logN)^2={ld*ln*ln:.4f}"
        )

    # power-law fit lmin ~ C * N^-a on last 6 points of G
    data = rows[1:]
    ns = [p[0] for p in data]
    lns = [math.log(p[1]) for p in data]
    x = [math.log(v) for v in ns]
    mx = sum(x) / len(x)
    my = sum(lns) / len(lns)
    a = sum((xi - mx) * (yi - my) for xi, yi in zip(x, lns)) / sum((xi - mx) ** 2 for xi in x)
    b = my - a * mx
    print(f"POWER FIT: lmin(G) ~ {math.exp(b):.4f} * N^({a:.3f})")
    for ni, lg, ld, ln in data:
        pred = math.exp(b) * ni ** a
        print(f"  N={ni}: actual={lg:.3e} pred={pred:.3e} ratio={lg/pred:.3f}", flush=True)

    # executor's own proposed threshold at N=2^16: 0.01/log N
    n16 = 65536
    thr = 0.01 / math.log(n16)
    pred16 = math.exp(b) * n16 ** a
    print(f"At N=2^16: claimed threshold 0.01/logN = {thr:.3e}; power-law prediction = {pred16:.3e} "
          f"(ratio {pred16/thr:.1e})")


if __name__ == "__main__":
    main()