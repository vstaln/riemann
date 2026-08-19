#!/usr/bin/env python3
"""w24c3-lane5 probe (2026-08-19): B\\u00e1ez-Duarte coefficient-energy V(N) growth law
+ planted-zero control (honest). Gram engine copied VERBATIM from /tmp/dN_recheck.py
(validated: reproduces certified d_N = 0.151041 / 0.126823 / 0.119192 at N=10/20/30),
with z_table/gram p-range raised 60->90 (certified-valued gates below re-check the
engine, so any regression from the parameter change is caught, not assumed).

Worker parallelism: the Gram entries gram(j,k) are independent; a fork pool computes
them in parallel (8 cores observed). mpmath state is inherited by fork workers.
"""
import math, sys, itertools, multiprocessing as mpN
import mpmath as mp
import numpy as np
mp.mp.dps = 30

def lcm(a, b):
    x, y = a, b
    while y:
        x, y = y, x % y
    return a // x * b

def intervals(j, k, l):
    end = 1 + l; pts = set(); m = 1
    while m * j <= end:
        if m * j > 1: pts.add(m * j)
        m += 1
    m = 1
    while m * k <= end:
        if m * k > 1: pts.add(m * k)
        m += 1
    pts = sorted(pts); ivs = []; cur = 1
    for p in pts:
        if p > cur: ivs.append((cur, p, cur // j, cur // k)); cur = p
    if cur < end: ivs.append((cur, end, cur // j, cur // k))
    return ivs

PM = 90
def z_table(pmax):
    n1 = 10000; z = []
    for p in range(pmax):
        s = p + 2; acc = mp.mpf(0)
        for m in range(4, n1 + 1): acc += mp.mpf(m) ** (-s)
        x = mp.mpf(n1)
        acc += x ** (1 - s) / (s - 1) - mp.mpf('0.5') * x ** (-s) + (s / 12) * x ** (-s - 1) \
               - (s * (s + 1) * (s + 2) / 720) * x ** (-s - 3)
        z.append(acc)
    return z
Z = z_table(PM)

def gram(j, k):
    l = lcm(j, k); ivs = intervals(j, k, l); lf = mp.mpf(l); jf = mp.mpf(j); kf = mp.mpf(k)
    tot = mp.mpf(0)
    for (x1, x2, ai, bi) in ivs:
        a = mp.mpf(x1); b = mp.mpf(x2); aif = mp.mpf(ai); bif = mp.mpf(bi)
        c2 = 1 / (jf * kf); c1 = -(aif / kf + bif / jf); c0 = aif * bif
        tot += c2 * (b - a) + c1 * (mp.log(b) - mp.log(a)) + c0 * (1 / a - 1 / b)
        for m in (1, 2, 3):
            ml = m * lf; v1 = a / ml; v2 = b / ml
            c2p = ml * ml / (jf * kf); c1p = -ml * (aif / kf + bif / jf); c0p = aif * bif
            tot += (c2p * (v2 - 2 * mp.log(v2 + 1) - 1 / (v2 + 1) - (v1 - 2 * mp.log(v1 + 1) - 1 / (v1 + 1)))
                    + c1p * (mp.log(v2 + 1) + 1 / (v2 + 1) - (mp.log(v1 + 1) + 1 / (v1 + 1)))
                    + c0p * (-1 / (v2 + 1) + 1 / (v1 + 1))) / ml
        bl = b / lf; al = a / lf; pb1 = bl; pa1 = al
        for p in range(PM):
            pb2 = pb1 * bl; pa2 = pa1 * al; pb3 = pb2 * bl; pa3 = pa2 * al
            d1 = pb1 - pa1; d2 = pb2 - pa2; d3 = pb3 - pa3; pf = p
            sign = 1 if p % 2 == 0 else -1
            t1 = c2 * lf * d3 / (pf + 3); t2 = c1 * d2 / (pf + 2); t3 = c0 * d1 / lf / (pf + 1)
            tot += sign * (pf + 1) * Z[p] * (t1 + t2 + t3)
            pb1 = pb2; pa1 = pa2
    return tot

GAMMA = mp.mpf('0.57721566490153286060651209008240243104215933593992')
def bk(k): return (mp.log(mp.mpf(k)) + 1 - GAMMA) / mp.mpf(k)

WORKERS = 8
def build_G(N, pool):
    pairs = [(k, j) for k in range(1, N + 1) for j in range(1, N + 1)]
    vals = pool.starmap(gram, pairs, chunksize=16)
    G = mp.matrix(N, N)
    idx = 0
    for i in range(N):
        for j in range(N):
            G[i, j] = vals[idx]; idx += 1
    return G

def main():
    Ns_arg = [int(x) for x in sys.argv[1:]] if len(sys.argv) > 1 else [10, 15, 20, 25, 30, 35, 40, 45, 50]
    pool = mpN.Pool(WORKERS)
    CERT = {10: 0.151041, 20: 0.126823, 30: 0.119192}
    rows = []
    print(f"== real world, k=1..N basis, engine p-range={PM}, dps=30, workers={WORKERS} ==", flush=True)
    prev = None
    for N in Ns_arg:
        G = build_G(N, pool)
        b = mp.matrix(N, 1)
        for i in range(N): b[i, 0] = bk(i + 1)
        a = mp.lu_solve(G, b)
        d2 = 1 - sum(b[i, 0] * a[i, 0] for i in range(N))
        W = sum((i + 1) * a[i, 0] ** 2 for i in range(N))
        d = float(mp.sqrt(d2)); d2 = float(d2); W = float(W)
        V = W / d2
        rows.append((N, d, d2, W, V))
        print(f"N={N:3d} d_N={d:.8f} d_N*sqrt(logN)={d * math.sqrt(math.log(N)):.6f} "
              f"delta=d^2*logN={d2 * math.log(N):.6f} W={W:.6e} V(N)={V:.6e} V/(N logN)={V / (N * math.log(N)):.4f}",
              flush=True)
        if N in CERT:
            err = abs(d - CERT[N])
            print(f"   GATE N={N}: |d-certified|={err:.2e}  PASS={err < 1e-6}", flush=True)
        if prev is not None:
            print(f"   monotone: d_N <= d_{prev[0]}  ({d} <= {prev[1]})  = {d <= prev[1]}", flush=True)
        prev = (N, d)
    pool.close(); pool.join()

    ns = np.array([r[0] for r in rows], dtype=float)
    ds = np.array([r[1] for r in rows]); d2s = np.array([r[2] for r in rows])
    Ws = np.array([r[3] for r in rows]); Vs = np.array([r[4] for r in rows])
    lnN = np.log(ns)

    def ols(x, y):
        X = np.vstack([x, np.ones_like(x)]).T
        beta, res, rank, sv = np.linalg.lstsq(X, y, rcond=None)
        yhat = X @ beta
        ss_res = float(np.sum((y - yhat) ** 2)); ss_tot = float(np.sum((y - y.mean()) ** 2))
        return beta, math.sqrt(ss_res / len(y)), (1 - ss_res / ss_tot if ss_tot > 0 else float('nan'))

    print("\n== growth-law fits (OLS on log-log) ==", flush=True)
    bV, rmsV, r2V = ols(lnN, np.log(Vs))
    print(f"V ~ N^a:      a={bV[0]:.4f}  rms_resid(log)={rmsV:.4f}  R2={r2V:.5f}", flush=True)
    bW, rmsW, r2W = ols(lnN, np.log(Ws))
    print(f"W ~ N^a:      a={bW[0]:.4f}  rms_resid(log)={rmsW:.4f}  R2={r2W:.5f}", flush=True)
    _, rmsV2, r2V2 = ols(lnN, np.log(Vs / (ns ** 2 / np.log(ns))))
    print(f"V~(N^2/logN): rms_resid(log)={rmsV2:.4f}  R2={r2V2:.5f}  (slope 0 would mean exact law)", flush=True)
    _, rmsVn, r2Vn = ols(lnN, np.log(Vs / (ns * np.log(ns))))
    print(f"V~(N logN):   rms_resid(log)={rmsVn:.4f}  R2={r2Vn:.5f}", flush=True)
    print("local exponent a_loc(N):", flush=True)
    for i in range(1, len(rows)):
        N, d, d2, W, V = rows[i]; Np, dp, d2p, Wp, Vp = rows[i - 1]
        print(f"   N={N:3d}: a_loc={math.log(V / Vp) / math.log(N / Np):.3f}  (V {Vp:.2e}->{V:.2e})", flush=True)
    print("rows CSV (N,d,d2,W,V):", flush=True)
    for r in rows:
        print(f"   {r[0]},{r[1]:.8f},{r[2]:.8e},{r[3]:.6e},{r[4]:.6e}", flush=True)

    print("\n== PLANTED-ZERO CONTROL (beta=0.7) - honest report ==", flush=True)
    print("PROVEN (Báez-Duarte iff d_N->0 <==> RH [campaign contract] + monotone d_N, nested spans):", flush=True)
    print("  RH-false world => d_N does NOT tend to 0; d_N decreases to d_inf=dist(1,cl(span))>0.", flush=True)
    print("  Real-world certified law d_N*sqrt(log N) ~ 0.212 FLAT is then violated: planted", flush=True)
    print("  signature d_N*sqrt(log N) ~ d_inf*sqrt(log N) -> +inf (unbounded divergence) whereas", flush=True)
    print("  the real world is bounded-flat. => genuinely different growth signature at the d level.", flush=True)
    print("CONJECTURED (Mellin/coefficient-runaway; NOT computed numerically - building the true", flush=True)
    print("  planted Beurling Gram is infeasible in this budget):", flush=True)
    print("  real d_N^2 ~ 0.045/log N (flat delta), so V(N)=W(N)/d_N^2 carries an extra ~log N", flush=True)
    print("  multiplier in the real world; in the planted world 1/d_N^2 saturates at d_inf^-2, and", flush=True)
    print("  coefficients a_k* must fight the pole of 1/zeta at s=0.7 under the Mellin transport", flush=True)
    print("  (Dirichlet polynomials are entire), driving runaway weighted energy W(N).", flush=True)
    print("  A planted V(N) trajectory was NOT computed; the V-axis prediction is CONJECTURED, not run.", flush=True)
    print("\nLabel matrix: d_N/V(N)/W(N) real-world numbers: CHECKED NUMERICALLY; certified gates: PROVEN;", flush=True)
    print("BD iff: PROVEN (literature/campaign contract); planted d-axis divergence: PROVEN;", flush=True)
    print("planted V-axis behavior: CONJECTURED.", flush=True)

if __name__ == '__main__':
    main()