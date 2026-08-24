#!/usr/bin/env python3
"""Round 4: warm-start at TAWAN's exact proven point; small steps, mass-2 + lam pinned to 1."""
import numpy as np, json, time
from joint_c21_ft2 import unpack, eps_of, bound_from
theta0 = np.array([1.0, 946.0, 1177.0, 877.0, 31343/100000, 1/3, 105971/300000, 1.47])
p,q,a,lam = unpack(theta0)
assert abs(q.sum()-2)<1e-12 and abs(p.sum()-1/320)<1e-12, (q.sum(), p.sum())
print(f"tawan point OK: psum={float(p.sum()):.9f} qsum={float(q.sum()):.12f} alpha={a}")
best_e,_ = eps_of(theta0, seed=11)
print(f"tawan surrogate eps={best_e:.7f}  (his certified floor was 577/100000=0.00577 under F_T)")
best_theta = theta0.copy(); rng = np.random.default_rng(2024)
scales = np.array([0.006,0.004,0.004,0.004,0.006,0.006,0.006,0.01]); T0=time.time()
for it in range(60):
    cand = best_theta*(1+rng.normal(0,1,8)*scales)
    e,pack_ = eps_of(cand, seed=100+it)
    if e>best_e:
        best_e,best_theta = e,cand
        p,q,a,lam = pack_
        b,m = bound_from(e,a,lam)
        print(f"[it {it}] eps={e:.7f} bound(m={m})={b:.10f} lam={lam:.4f} alpha={a:.4f} [{time.time()-T0:.0f}s]", flush=True)
        np.save('best_ft4_theta.npy', best_theta)
print(json.dumps({"eps": best_e}))
