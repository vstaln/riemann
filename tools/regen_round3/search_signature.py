#!/usr/bin/env python3
"""ROUTE 2, ROUND-3 SEARCH: signature-seeded family at N = 256.

Seed (from regenerate-256law.md S6 + this round's structural analysis):
  - configs with ~244 integer marks + ~12 half-integer marks (n_h in {11,12});
    f_c(256) = (2 n0 - 256)^2 in {53824, 54756};
  - E[d] ~= 40.7 doubles (from p0),  s + 2d + n_h = 256, marks {1,2};
  - the recorded data forces E[cross] = +378.9 > 0, which int+half DISTINCT
    configs cannot supply (cross = -2(256-n_h) n_h <= 0); so the family must
    include near-coincident / coincident marks (cross > 0 possible).

New: a single LP minimizing the Chebyshev distance of the ramp R(j)=j to the
convex hull of the family spectra, plus a min-p1 LP at the best distance.

Run: uv run --with numpy --with scipy python3 search_signature.py
"""
import numpy as np
from scipy.optimize import linprog
import time, sys

N = 256
j = np.arange(1, N + 1)

# precompute DFT matrices
w = np.exp(2j * np.pi * j / N)              # (256,)  w^j for integer step 1
DFT_int = np.exp(2j * np.pi * np.outer(j, np.arange(N)) / N)     # 256 x 256
DFT_half = np.exp(2j * np.pi * j * 0.5 / N)[:, None] * DFT_int   # 256 x 256

def cfg_spectrum(int_pos, int_marks, half_q, dbl_at_half=()):
    """int marks (val 1/2) at integer positions; half marks (val 1) at q+0.5;
    optionally coincident half marks (two marks at q+0.5) given as dbl_at_half q's."""
    z = DFT_int[:, int_pos] @ np.array(int_marks, dtype=float)
    if len(half_q):
        z = z + DFT_half[:, half_q].sum(axis=1)
    if len(dbl_at_half):
        z = z + 2.0 * DFT_half[:, dbl_at_half].sum(axis=1)
    return np.abs(z) ** 2

def gen_family(n_cfg=9000, seed=101):
    rng = np.random.default_rng(seed)
    configs = []  # (int_pos, int_marks, half_q, dbl_at_half)
    dvals = list(range(28, 53))
    # structured half-mark patterns
    ap_steps = [1, 2, 3, 4, 5, 8, 16, 32, 64, 128, 7, 9, 11, 13, 17, 21, 25, 33, 43]
    made = 0
    tries = 0
    while made < n_cfg and tries < n_cfg * 40:
        tries += 1
        d = int(rng.choice(dvals))
        n_h = int(rng.choice([11, 12]))
        s = N - n_h - 2 * d
        if s < 0:
            continue
        # choose integer positions: s simples + d doubles
        int_pos = rng.choice(N, size=s + d, replace=False)
        int_marks = np.array([1] * s + [2] * d, dtype=float)
        rng.shuffle(int_marks)
        # half marks: structured (AP or random)
        if made % 3 == 0 and n_h >= 3:
            step = int(rng.choice(ap_steps))
            q0 = int(rng.integers(0, N))
            half_q = [int((q0 + step * k) % N) for k in range(n_h)]
            if len(set(half_q)) < n_h:
                half_q = rng.choice(N, size=n_h, replace=False).tolist()
        else:
            half_q = rng.choice(N, size=n_h, replace=False).tolist()
        # optional coincidence: ~2/3 of configs get one coincident half mark
        # (two marks at the same half position) => use s-1 integer simples
        dbl_at_half = []
        if rng.random() < 0.65 and s >= 1 and len(half_q) >= 1:
            qc = int(rng.choice(half_q))
            dbl_at_half = [qc]
            s = s - 1
            int_pos = rng.choice(N, size=s + d, replace=False)
            int_marks = np.array([1] * s + [2] * d, dtype=float)
            rng.shuffle(int_marks)
        configs.append((int_pos, int_marks, half_q, dbl_at_half))
        made += 1
    return configs

def run(pool, label):
    m = len(pool)
    print(f"[{label}] {m} configs; building spectra...")
    t0 = time.time()
    F = np.zeros((m, N))
    for i, (ip, im, hq, dh) in enumerate(pool):
        F[i] = cfg_spectrum(ip, im, hq, dh)
    print(f"  spectra in {time.time()-t0:.1f}s")
    # feasibility LP: min t s.t. |Fw - R| <= t, sum w = 1, w >= 0
    nvar = m + 1
    c = np.zeros(nvar); c[-1] = 1
    A_ub, b_ub = [], []
    for jj in range(N - 1):
        row = np.zeros(nvar); row[:m] = F[:, jj]; row[-1] = -1
        A_ub.append(row); b_ub.append(jj + 1)
        row = np.zeros(nvar); row[:m] = -F[:, jj]; row[-1] = -1
        A_ub.append(row); b_ub.append(-(jj + 1))
    A_eq = np.zeros((1, nvar)); A_eq[0, :m] = 1
    t0 = time.time()
    res = linprog(c, A_ub=np.array(A_ub), b_ub=np.array(b_ub), A_eq=A_eq, b_eq=[1.0],
                  bounds=[(0, None)] * nvar, method='highs')
    print(f"  LP in {time.time()-t0:.1f}s  success={res.success}")
    t = res.fun if res.success else float('nan')
    print(f"  Chebyshev distance of ramp to hull = {t:.6f}")
    if res.success and t < 100:
        fbar = res.x[:m] @ F
        worst = np.argsort(-np.abs(fbar[:255] - np.arange(1, 256)))[:8]
        print("  worst rows:", [(int(w + 1), round(float(np.abs(fbar[w] - (w + 1))), 4)) for w in worst])
        # min p1 at this distance
        s_c = np.array([256 - 2 * sum(1 for mm in im if mm == 2) for (ip, im, hq, dh) in pool], dtype=float)
        res2 = linprog(s_c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=[1.0],
                       bounds=[(0, None)] * nvar, method='highs')
        if res2.success:
            print(f"  min p1 at feasible rows = {res2.fun/256:.12f}   (recorded p0 = 0.6818286874638315)")
    return t

if __name__ == '__main__':
    pool = gen_family(n_cfg=int(sys.argv[1]) if len(sys.argv) > 1 else 9000,
                      seed=int(sys.argv[2]) if len(sys.argv) > 2 else 101)
    run(pool, "signature family")
