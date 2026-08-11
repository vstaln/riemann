#!/usr/bin/env python3
"""Column generation at N=8: approach the true min p1 over ALL valid marked configs
with exact near-CUE rows + D(1) bound. Config search = random + local refinement.
Reports the min p1 and whether it can dip below Thm B's 0.6725."""
import numpy as np
from scipy.optimize import linprog
import time

N = 8
d1 = 0.82395317
Fb = N*N*(d1+0.5) - N*(N-1)//2      # fbar(8) bound from D(1)

def cfg_spectrum(xs, ms):
    j = np.arange(1, N+1)
    z = np.zeros(N, dtype=complex)
    for x, m in zip(xs, ms):
        z += m*np.exp(2j*np.pi*j*x/N)
    return np.abs(z)**2

def random_config(rng, d):
    s = N - 2*d
    npos = s + d
    base = rng.choice(N, size=npos, replace=False)
    u = rng.choice((0.0, 0.5, 0.25, 0.75, 1/3, 2/3, 0.125, 0.375), size=npos)
    xs = (base + u) % N
    ms = np.concatenate([np.ones(s), 2*np.ones(d)])
    return xs, ms

# ---- pool: big random family ----
rng = np.random.default_rng(7)
pool = []
for _ in range(20000):
    d = int(rng.integers(0, N//2+1))
    xs, ms = random_config(rng, d)
    pool.append((xs, ms))

# dedupe by rounded spectrum
uniq = {}
for xs, ms in pool:
    f = cfg_spectrum(xs, ms)
    key = tuple(np.round(f, 6))
    if key not in uniq:
        uniq[key] = (xs, ms, f)
items = list(uniq.values())
print(f"N=8: {len(items)} distinct configs in pool")
F = np.array([f for _, _, f in items])
sc = np.array([int((ms == 1).sum()) for _, ms, _ in items])
m = len(F)

A_ub, b_ub = [], []
for jj in range(N-1):
    A_ub.append(F[:, jj]); b_ub.append((jj+1)+3e-40)
    A_ub.append(-F[:, jj]); b_ub.append(-(jj+1)+3e-40)
A_ub.append(F[:, N-1]); b_ub.append(Fb)
A_eq = np.ones((1, m)); b_eq = [1.0]
res = linprog(sc, A_ub=np.array(A_ub), b_ub=np.array(b_ub), A_eq=A_eq, b_eq=b_eq, bounds=[(0,None)]*m, method='highs')
print(f"min p1 over {m}-config pool: {'INFEASIBLE' if not res.success else res.fun/8}")
if res.success:
    fbar = res.x @ F
    print(f"  min p1 = {res.fun/8:.10f}   (ThmB = 0.6725, grid LB = 3/2-d1 = {3/2-d1:.10f})")
    # E(1)
    E1 = (fbar @ np.array([1-(jj+1)/N for jj in range(N)]))/N**2 - 1/6
    print(f"  E(1) = {E1:.8f}  (M = {1/(6*N*N):.8f})")

# ---- column generation: search for configs violating the current certificate ----
print("\n--- column generation refinement ---")
cur_idx = list(range(m))
Fcur = F.copy(); scur = sc.copy()
cert_cache = {}
for it in range(6):
    A_ub, b_ub = [], []
    for jj in range(N-1):
        A_ub.append(Fcur[:, jj]); b_ub.append((jj+1)+3e-40)
        A_ub.append(-Fcur[:, jj]); b_ub.append(-(jj+1)+3e-40)
    A_ub.append(Fcur[:, N-1]); b_ub.append(Fb)
    A_eq = np.ones((1, len(cur_idx))); b_eq = [1.0]
    res = linprog(scur, A_ub=np.array(A_ub), b_ub=np.array(b_ub), A_eq=A_eq, b_eq=b_eq,
                  bounds=[(0,None)]*len(cur_idx), method='highs')
    if not res.success:
        print(f"  iter {it}: infeasible"); break
    p1 = res.fun/N
    # dual certificate: from the primal LP's duals (lambda for rows, nu for D(1), mu for sum w)
    # Build the certificate validity: c0 + sum_j (f(j)/N) r_j <= s_c/N ; max over configs.
    # Use the dual variables: reduced cost of config c = sum_j lam_j f_c(j) + lam8 f_c(8) - s_c/N (up to const)
    # Extract from res.eqlin (sum w = 1) and res.ineqlin (rows, D1).
    lam = np.zeros(N)
    ineqlin = np.asarray(res.ineqlin.marginals).ravel()
    mu = float(res.eqlin.marginals[0])
    # constraints order: for jj in 0..N-2: +row, -row; then D1 row.
    for jj in range(N-1):
        lam[jj] = ineqlin[2*jj] - ineqlin[2*jj+1]
    lam[N-1] = ineqlin[2*(N-1)]
    # reduced cost to MAXIMIZE: sum_j lam[j] f(j) - s_c/N  (c0, mu constants don't affect the argmax)
    best = (-1e9, None)
    rng = np.random.default_rng(it)
    for trial in range(40000):
        d = int(rng.integers(0, N//2+1))
        xs, ms = random_config(rng, d)
        f = cfg_spectrum(xs, ms)
        rc = float(lam @ f) - (ms == 1).sum()/N
        if rc > best[0]:
            best = (rc, (xs, ms, f))
    rc, cand = best
    if rc < 1e-8:
        print(f"  iter {it}: no violator (max reduced cost {rc:.2e}) -> min p1 = {p1:.10f}  DONE")
        break
    # add a few violators
    added = 0
    rng = np.random.default_rng(it+100)
    seen_keys = {tuple(np.round(f,6)) for f in Fcur}
    while added < 10:
        d = int(rng.integers(0, N//2+1))
        xs, ms = random_config(rng, d)
        f = cfg_spectrum(xs, ms)
        rc2 = float(lam @ f) - (ms == 1).sum()/N
        if rc2 > 0 and tuple(np.round(f,6)) not in seen_keys:
            Fcur = np.vstack([Fcur, f]); scur = np.concatenate([scur, [(ms==1).sum()]])
            seen_keys.add(tuple(np.round(f,6))); added += 1
    print(f"  iter {it}: min p1 = {p1:.10f}, max viol rc = {rc:.4f}, added {added}")
