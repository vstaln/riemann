import sys; sys.path.insert(0,'.')
from joint_c21_ft import F_B, make_w, min_FB, bound_from, unpack
import numpy as np, json, time, os
theta0 = np.array([1.15, 946/6000*2, 1177/6000*2, 877/6000*2, 0.31343, 1/3, 0.353237, 1.464])
if os.path.exists("best_c21_theta.npy"):
    theta0 = np.load("best_c21_theta.npy")
    print(f"warm-started theta0 from best_c21_theta.npy: {theta0}", flush=True)
else:
    print("no best_c21_theta.npy; using hardcoded start", flush=True)
best_theta = theta0.copy()
best_e, _ = min_FB(*[x for x in unpack(theta0)[:2]], theta0[7], seed=11) if False else (None,None)
p,q,a,lam = unpack(theta0)
best_e, _ = min_FB(p, q, a, seed=11)
print(f"start eps={best_e:.7f}", flush=True)
rng = np.random.default_rng(42)
scales = np.array([0.04, 0.03, 0.03, 0.03, 0.012, 0.012, 0.012, 0.02])
T0=time.time()
for it in range(30):
    cand = best_theta * (1 + rng.normal(0,1,8)*scales)
    lam_c = cand[0]
    if not (0.5<=lam_c<=2.5 and 0.8<=cand[7]<=2.5): continue
    p,q,a,lam = unpack(cand)
    e,_ = min_FB(p,q,a,seed=it)
    b,m = bound_from(e,a,lam)
    tag=""
    if b > 0.6735633479946228: tag=" *** BEATS RETIRED ***"
    print(f"[it {it}] eps={e:.7f} bound={b:.10f} m={m} lam={lam:.4f} alpha={a:.4f}{tag}", flush=True)
    if e > best_e:
        best_e, best_theta = e, cand.copy()
        np.save("best_c21_theta.npy", cand)
print(json.dumps({"eps":float(best_e),"theta":list(map(float,best_theta))}))

