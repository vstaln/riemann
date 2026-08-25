#!/usr/bin/env python3
"""Round 5: lam pinned to 1.0 EXACTLY (joint_c21_ft5 unpack). Warm-start = better of
(a) Tawan exact proven point, (b) best_ft4_theta with lam forced to 1.0 (a_,b_,c_
renormalized so p sums 1/320). Scales halved vs round 4, iterations 50, rng seed 555."""
import sys; sys.path.insert(0,'.')
import numpy as np, json, time, os
from joint_c21_ft5 import unpack, eps_of, bound_from

cands = []
# (a) Tawan exact proven point (lam=1.0)
cands.append(("tawan", np.array([1.0, 946.0, 1177.0, 877.0, 31343/100000, 1/3, 105971/300000, 1.47])))
# (b) best_ft4_theta with lam forced to 1.0, a_,b_,c_ renorm so p sums 1/320
b4 = np.load("best_ft4_theta.npy").copy()
b4[0] = 1.0
p,_,a,_ = unpack(b4)
assert abs(p.sum()-1/320) < 1e-9, f"ft4 seed p-sum {p.sum()} != 1/320"
cands.append(("ft4", b4))

best_e, best_theta, best_src = -1e9, None, ""
for name, th in cands:
    e, pack = eps_of(th, seed=11)
    print(f"seed {name}: eps={e:.7f}", flush=True)
    if e > best_e:
        best_e, best_theta, best_src = e, th.copy(), name
print(f"warm-start winner: {best_src} eps={best_e:.7f}", flush=True)

p, q, a, lam = unpack(best_theta)
b, m = bound_from(best_e, a, lam)
print(f"start bound={b:.10f} m={m}", flush=True)

rng = np.random.default_rng(555)
scales = np.array([0.003,0.002,0.002,0.002,0.003,0.003,0.003,0.005])  # half of R4
T0 = time.time()
for it in range(50):
    cand = best_theta*(1+rng.normal(0,1,8)*scales)
    e, pack = eps_of(cand, seed=100+it)
    if e > best_e:
        best_e, best_theta = e, cand
        p,q,a,lam = pack
        b,m = bound_from(e,a,lam)
        print(f"[it {it}] eps={e:.7f} bound(m={m})={b:.10f} lam={lam:.4f} alpha={a:.4f} [{time.time()-T0:.0f}s]", flush=True)
        np.save('best_ft5_theta.npy', best_theta)
print(json.dumps({"eps": float(best_e), "src": best_src, "theta": list(map(float, best_theta))}))
