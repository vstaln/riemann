#!/usr/bin/env python3
"""Mixed-pool Route-2 search: near-lattice (small spectra, below ramp) +
signature configs (d~41, 12 half marks) + heavy-defect configs, with and
without coincidences.  Measures the Chebyshev distance of the ramp to the hull.
"""
import numpy as np
from scipy.optimize import linprog
import time, sys

N = 256
j = np.arange(1, N + 1)
DFT_int = np.exp(2j * np.pi * np.outer(j, np.arange(N)) / N)
DFT_half = np.exp(2j * np.pi * j * 0.5 / N)[:, None] * DFT_int

def cfg_spectrum(int_pos, int_marks, half_q, dbl_at_half=()):
    z = DFT_int[:, int_pos] @ np.array(int_marks, dtype=float)
    if len(half_q):
        z = z + DFT_half[:, half_q].sum(axis=1)
    if len(dbl_at_half):
        z = z + 2.0 * DFT_half[:, dbl_at_half].sum(axis=1)
    return np.abs(z) ** 2

def gen_pool(n_total, seed):
    rng = np.random.default_rng(seed)
    pool = []
    ap_steps = [1, 2, 3, 4, 5, 8, 16, 32, 64, 128, 7, 9, 11, 13, 17, 21, 33]
    made = 0; tries = 0
    while made < n_total and tries < n_total * 50:
        tries += 1
        kind = made % 4
        if kind == 0:
            # near-lattice: few defects, small spectrum (below the ramp)
            d = int(rng.integers(0, 12)); n_h = int(rng.integers(0, 13))
        elif kind == 1:
            # signature configs
            d = int(rng.integers(28, 53)); n_h = int(rng.choice([11, 12]))
        elif kind == 2:
            # heavy defect
            d = int(rng.integers(53, 90)); n_h = int(rng.integers(4, 20))
        else:
            # mid defect, random half count
            d = int(rng.integers(12, 55)); n_h = int(rng.integers(0, 30))
        s = N - n_h - 2 * d
        if s < 0: continue
        dbl_at_half = []
        if rng.random() < 0.5 and s >= 1 and n_h >= 1:
            # coincidence: one extra mark at a half position, one fewer simple
            s = s - 1
        int_pos = rng.choice(N, size=s + d, replace=False)
        int_marks = np.array([1] * s + [2] * d, dtype=float)
        rng.shuffle(int_marks)
        if made % 4 == 1 and n_h >= 3:
            step = int(rng.choice(ap_steps)); q0 = int(rng.integers(0, N))
            half_q = [int((q0 + step * k) % N) for k in range(n_h)]
            if len(set(half_q)) < n_h:
                half_q = rng.choice(N, size=n_h, replace=False).tolist()
        else:
            half_q = rng.choice(N, size=n_h, replace=False).tolist()
        if dbl_at_half is not None and rng.random() < 0.0:
            pass
        # decide coincidence after positions chosen
        qc = None
        if len(half_q) and rng.random() < 0.4:
            qc = int(rng.choice(half_q))
        pool.append((int_pos, int_marks, half_q, [qc] if qc is not None else []))
        made += 1
    return pool

def run(pool, label):
    m = len(pool)
    print(f"[{label}] {m} configs; spectra...")
    t0 = time.time()
    F = np.zeros((m, N))
    for i, (ip, im, hq, dh) in enumerate(pool):
        F[i] = cfg_spectrum(ip, im, hq, dh)
    print(f"  spectra {time.time()-t0:.1f}s")
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
    print(f"  LP {time.time()-t0:.1f}s  success={res.success}  Chebyshev = {res.fun if res.success else float('nan'):.4f}")
    if res.success:
        fbar = res.x[:m] @ F
        d_ = np.abs(fbar[:255] - np.arange(1, 256))
        print("  worst rows:", [(int(w + 1), round(float(d_[w]), 3)) for w in np.argsort(-d_)[:6]])
        # min p1 with t pinned
        s_c = np.array([256 - 2 * sum(1 for mm in im if mm == 2) for (ip, im, hq, dh) in pool], dtype=float)
        c2 = np.zeros(nvar); c2[:m] = s_c
        res2 = linprog(c2, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=[1.0],
                       bounds=[(0, None)] * m + [(res.fun, res.fun)], method='highs')
        if res2.success:
            print(f"  min p1 at that distance = {res2.fun/256:.10f}   (p0 = 0.6818286874638315)")

if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 202
    pool = gen_pool(n, seed)
    run(pool, f"mixed pool seed {seed}")
