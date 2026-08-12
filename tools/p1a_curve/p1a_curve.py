#!/usr/bin/env python3
"""p1(A) curve from the extended-row marked-config LP at N=64.

Family: regen_law.common2.gen_valid_family (VALID: s + 2d = N, sum marks = N, s_c = N - 2d).
NOT common.gen_family_vec (KNOWN BUGGY: sum marks = N+d). This is the family family_law.py
successfully solves at N=64 (pw_p1 ~0.909, seeds 42/1234/2024).
Extended rows: j = 1..M pinned to the near-CUE ramp f(j) = j (s_j = j/N^2), M up to 2N = 128
so the A >= 2 infeasibility (twisted-Parseval wall, f1curve §3c) is testable.
Wall at N=64 (integer-position, no-coincidence bound): second-period ramp sum_{j=64..M} j
<= 64*max sum m^2 = 64*96 = 6144 (d<=16) => M <= 127 => A_max = 127/64 = 1.984375
(N=256 had 511/256 = 1.9961). Jitter leaks Parseval slightly; empirical wall reported.
Objective: minimize p1 = sum_c w_c s_c / N  s.t. |sum w f_c(j) - j| <= tau, j = 1..M, sum w = 1.
Certified simple-on-line fraction under PCC (F=1 on [0,A]): p1(A) + 1/(6N^2) (f1curve §1 identity).
Crash-proof: appends one JSON line per (seed, A) immediately after each solve.
"""
import sys, os, json, time
import numpy as np
from scipy.optimize import linprog

sys.path.insert(0, "/root/riemann/tools/regen_law")
from common2 import gen_valid_family

N = 64
M_MAX = 128          # rows j=1..M_MAX available; f1curve wall at M = 127
P0_256 = 0.6818286874638315   # law_data.json, N=256 law (PROVEN Lean)
OUT = "/root/riemann/tools/p1a_curve/results.jsonl"

def spectra_ext(X, M_vec, N, M_MAX):
    """f_c(j) = |sum_k m_k e^{2pi i j x_k / N}|^2 for j = 1..M_MAX. Returns (n_configs, M_MAX)."""
    j = np.arange(1, M_MAX + 1)
    F = np.zeros((len(X), M_MAX))
    for c in range(len(X)):
        xs = X[c]; ms = M_vec[c]
        F[c] = np.abs(np.exp(2j * np.pi * np.outer(j, xs) / N) @ ms) ** 2
    return F

def solve(configs_F, s_c, A, tau):
    M = int(np.floor(A * N))
    m = len(configs_F)
    A_ub, b_ub = [], []
    for j in range(1, M + 1):
        row = configs_F[:, j - 1]
        A_ub.append(row);   b_ub.append(j * (1 + tau))
        A_ub.append(-row);  b_ub.append(-j * (1 - tau))
    A_eq = np.ones((1, m)); b_eq = [1.0]
    obj = np.array(s_c, dtype=float)
    res = linprog(obj, A_ub=np.array(A_ub), b_ub=np.array(b_ub),
                  A_eq=A_eq, b_eq=b_eq, bounds=[(0, None)] * m, method="highs")
    return res, M

def run_seed(seed, nc, As, taus):
    t0 = time.time()
    X, Mvec, s_c = gen_valid_family(N, n_configs=nc, seed=seed)
    F = spectra_ext(X, Mvec, N, M_MAX)
    print(f"seed={seed}: {len(F)} configs, gen {time.time()-t0:.1f}s", flush=True)
    rows = []
    for A in As:
        best = None
        for tau in taus:
            t1 = time.time()
            res, M = solve(F, s_c, A, tau)
            dt = time.time() - t1
            if res.success:
                p1 = float(res.fun) / N
                best = {"A": A, "M": M, "tau": tau, "success": True, "p1": p1,
                        "certified": p1 + 1.0 / (6 * N * N), "nz": int(np.sum(res.x > 1e-9)),
                        "time_s": round(dt, 1)}
                break
            else:
                print(f"  seed={seed} A={A} tau={tau}: INFEASIBLE {time.time()-t1:.1f}s", flush=True)
        if best is None:
            best = {"A": A, "M": int(np.floor(A * N)), "tau": None, "success": False,
                    "p1": None, "certified": None, "note": "infeasible in family at all tau"}
        rows.append(best)
        with open(OUT, "a") as fh:
            fh.write(json.dumps({**best, "seed": seed, "p0_256": P0_256}) + "\n")
        print(f"seed={seed} A={A}: p1={best.get('p1')}", flush=True)
    return rows

def analyze(seed_rows, As):
    """Normalized deficit R(A)=(1-p1(A))/(1-p1(1)); M2^64 fit to LP anchor; 256-scale roadmap."""
    feas = [r for r in seed_rows if r["success"]]
    anchor = next((r["p1"] for r in feas if r["A"] == 1.0), None)
    out = {"p0_64_anchor": anchor, "table": []}
    for r in feas:
        R = (1 - r["p1"]) / (1 - anchor) if anchor is not None and anchor < 1 else None
        m2 = 1 - (1 - anchor) / r["A"] ** 2 if anchor is not None else None
        out["table"].append({"A": r["A"], "M": r["M"], "p1": r["p1"],
                             "certified_N64": r["certified"], "R": R, "M2_fit64": m2})
    # 256-scale roadmap: certified_256(A) = 1 - (1-p0)*R(A) + 1/(6*256^2)
    tgt_R = {(1 - t) / (1 - P0_256) for t in (0.70, 0.75, 0.80)}
    interp = {}
    pts = sorted(out["table"], key=lambda r: r["A"])
    for tgt in (0.70, 0.75, 0.80):
        wantR = (1 - tgt) / (1 - P0_256)
        A_lo = A_hi = None
        for i in range(len(pts) - 1):
            a1, a2 = pts[i], pts[i + 1]
            if a1["R"] is not None and a2["R"] is not None and a1["R"] >= wantR >= a2["R"]:
                A_lo, A_hi = a1, a2
                break
        if A_lo is None:
            interp[str(tgt)] = {"A": None, "note": "R not bracketed"}
        else:
            t = (wantR - A_lo["R"]) / (A_hi["R"] - A_lo["R"])
            interp[str(tgt)] = {"A": round(A_lo["A"] + t * (A_hi["A"] - A_lo["A"]), 4),
                                "R_target": round(wantR, 5), "bracket": [A_lo["A"], A_hi["A"]]}
    out["interp_256scale"] = interp
    # M2 agreement: |R - 1/A^2| / (1/A^2) and |p1 - M2fit|/(1-anchor)
    agree = []
    for r in out["table"]:
        if r["R"] is not None:
            relR = abs(r["R"] - 1 / r["A"] ** 2) / (1 / r["A"] ** 2)
            relP = abs(r["p1"] - r["M2_fit64"]) / (1 - anchor)
            agree.append({"A": r["A"], "relR_vs_1oA2": relR, "relP_vs_M2fit": relP})
    out["m2_agreement"] = agree
    out["max_relR"] = max((a["relR_vs_1oA2"] for a in agree), default=None)
    out["max_relP"] = max((a["relP_vs_M2fit"] for a in agree), default=None)
    return out

if __name__ == "__main__":
    As = [1.0, 1.02, 1.03, 1.04, 1.05, 1.10, 1.126, 1.13, 1.20, 1.26, 1.30, 1.40,
          1.50, 1.60, 1.70, 1.80, 1.90, 1.95, 1.97, 1.98, 1.99, 2.00]
    taus = [0.0, 1e-6, 1e-4, 1e-3]
    seeds = [42, 1234, 2024]
    nc = 4000
    all_rows = {}
    for seed in seeds:
        rows = run_seed(seed, nc, As, taus)
        all_rows[seed] = rows
        with open("/root/riemann/tools/p1a_curve/partial.json", "w") as fh:
            json.dump(all_rows, fh, indent=1)
    summary = {"N": N, "M_MAX": M_MAX, "wall_A_f1curve": 127.0 / 64.0, "p0_256": P0_256}
    for seed in seeds:
        summary[f"seed{seed}"] = analyze(all_rows[seed], As)
    with open("/root/riemann/tools/p1a_curve/results.json", "w") as fh:
        json.dump(summary, fh, indent=1)
    print("=== SUMMARY ===")
    print(json.dumps({k: v for k, v in summary.items() if k != "seed2024"}, indent=1))
    print("DONE", flush=True)
