#!/usr/bin/env python3
"""C1 weight search — break the crystal adversary with non-uniform weights.

The 7-point certificate floor is F = p*sum(g) + sum a_ij k^2(g_j - g_i).
Validity requires (capacity): sum_i a[i,i+r] <= 2 for each span r=1..6.

The uniform weights a[i,i+s] = 2/(7-s) SATURATE capacity (total 2 per span).
The crystal adversary (alternating gaps at kernel zeros z1~1.0645, z2~2.0341,
z3~3.0230) achieves low F because MANY pairs simultaneously sit at k^2~0.

KEY INSIGHT: capacity bounds only the PER-SPAN SUM, not individual a_ij. The crystal
is worst for UNIFORM spreading (it makes every span-1 pair cheap at once). A
non-uniform redistribution WITHIN each span — concentrating weight on the positions
where the crystal CANNOT be cheap while de-weighting positions where it can — may
raise the certified minimum F.

The crystal's gap pattern (from gaps.rs, 7-atom minimizer at span 9):
  gaps ~ (1.0, 2.0, 0.01, 3.0, 1.0, 1.0)  (kernel-zero separations).
So consecutive pairs (span 1) at gaps 1.0, 2.0, 0.01, 3.0, 1.0, 1.0 have k^2 at
k(1.0)^2=0.0036, k(2.0)^2=0.0002, k(0.01)^2~0.98, k(3.0)^2=3.95e-5, ...
The crystal is NOT uniformly cheap on span 1 — only SOME span-1 gaps are cheap.

Redistribution strategy: the certificate must hold for ALL configs. We search for
the weight profile maximizing the minimum of F. Since the minimum is attained at the
crystal, and the crystal has a specific gap pattern, we want to CONCENTRATE weight
on the pairs that are expensive in the crystal and DE-WEIGHT the pairs that are
cheap in the crystal — subject to per-span capacity 2.

This is a small LP/saddle point. We do it by direct search: parametrize per-span
weight vectors w_r = (w_{0,0+r}, ..., w_{6-r,6-r+r}) with sum <= 2, and binary-
search eps for each candidate.

Candidates are chosen to (a) saturate capacity, (b) put weight where k^2 is large
at the crystal's gaps.
"""
import json
import subprocess
import sys
import math

VERIFIER = ["uv", "run", "--quiet", "--with", "python-flint", "python3",
            "/home/vstaln/riemann/tools/beat673/verify_cos7.py"]

ALPHA = (149, 100)
P = (1, 1320)
GRID = 4000

def default_weights():
    return {(i, i+s): (2, 7-s) for s in range(1, 7) for i in range(0, 7-s)}

def verify(target_num, target_den, weights, timeout=1200):
    wjson = {f"{i},{j}": [n, d] for (i, j), (n, d) in weights.items()}
    tmp = "/tmp/c1_weights.json"
    with open(tmp, "w") as f:
        json.dump(wjson, f)
    cmd = VERIFIER + [str(ALPHA[0]), str(ALPHA[1]), str(P[0]), str(P[1]),
                      str(target_num), str(target_den), tmp, str(GRID)]
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return None, None
    verified = "verified=True" in out.stdout
    lower = None
    for line in out.stdout.splitlines():
        if "lower=" in line:
            try:
                lower = float(line.split("lower=")[1].split()[0])
            except (IndexError, ValueError):
                pass
    return verified, lower

def capacity_ok(weights):
    for r in range(1, 7):
        total = sum(n/d for (i, j), (n, d) in weights.items() if j-i == r)
        if total > 2 + 1e-12:
            return False, r, total
    return True, None, None

def weights_from_span_vectors(span_vectors):
    """span_vectors[r] = list of numerators (len 7-r) over common denom 1000,
    r = 1..6. Sum over each span <= 2000 (capacity 2)."""
    D = 1000
    w = {}
    for r in range(1, 7):
        vec = span_vectors[r]
        for i, num in enumerate(vec):
            w[(i, i+r)] = (num, D)
    return w

def main():
    base = default_weights()
    print("=== baseline check ===", flush=True)
    v, lo = verify(7759, 1_000_000, base)
    print(f"baseline eps=0.007759 -> {v}", flush=True)

    # Crystal gaps (7 atoms, span 9): (1.0, 2.0, 0.01, 3.0, 1.0, 1.0)
    # Span-1 pairs are (g1,g2,g3,g4,g5,g6) = gaps between consecutive atoms.
    # k^2 at those gaps: 1.0->0.0036, 2.0->0.0002, 0.01->~0.98, 3.0->3.95e-5, 1.0, 1.0
    # So span-1: positions 2 (gap 2.0) and 3 (gap 3.0) are VERY cheap; others moderate.
    # CONCENTRATE span-1 weight on the cheap positions is WRONG (lowers floor).
    # CORRECT: concentrate on the EXPENSIVE positions (gap 0.01 has k^2~0.98, gaps 1.0 have 0.0036).
    # But the crystal is adversarial: it will RE-OPTIMIZE its gaps for our weights.
    # The saddle point is what the verifier finds. So we can't hand-pick; we search.

    # Candidate 1: put span-1 weight on the FIRST few positions (positions 0,1,2),
    # leaving positions 3,4,5 de-weighted. The crystal's cheapest span-1 gaps are
    # positions 2 (gap 2.0) and 3 (gap 3.0); de-weight those.
    # span-1 has 6 positions: total 2000 units.
    candidates = []
    # (name, span_vectors[1..6]) each a list of ints summing to 2000 per span (or less)
    uniform = {r: [2000 // (7-r)] * (7-r) for r in range(1, 7)}
    # fix remainder: uniform span-1: 6 positions -> 2000/6 = 333.33; use 334,333,333,333,333,334
    uniform[1] = [334, 333, 333, 333, 333, 334]  # sum 2000
    uniform[2] = [400, 400, 400, 400, 400]        # sum 2000
    uniform[3] = [500, 500, 500, 500]              # sum 2000
    uniform[4] = [667, 667, 666]                   # sum 2000
    uniform[5] = [1000, 1000]                      # sum 2000
    uniform[6] = [2000]                            # sum 2000
    candidates.append(("uniform(ref)", uniform))

    # Candidate A: de-weight span-1 positions 2,3 (the crystal's cheap gaps 2.0,3.0)
    a = {r: list(v) for r, v in uniform.items()}
    a[1] = [500, 500, 100, 100, 400, 400]  # sum 2000; positions 2,3 de-weighted
    candidates.append(("span1_deweight_crystal", a))

    # Candidate B: concentrate span-1 on position 0 (gap g1, crystal gap 1.0 -> k^2=0.0036, cheap-ish)
    b = {r: list(v) for r, v in uniform.items()}
    b[1] = [1200, 160, 160, 160, 160, 160]  # sum 2000
    candidates.append(("span1_concentrate_pos0", b))

    # Candidate C: spread span-1 evenly but de-weight span 1 entirely (total 1200)
    c = {r: list(v) for r, v in uniform.items()}
    c[1] = [200, 200, 200, 200, 200, 200]  # sum 1200 (under capacity)
    candidates.append(("span1_total1.2", c))

    # Candidate D: put ALL span-1 weight on positions 3,4,5 (far from crystal cheapness)
    d = {r: list(v) for r, v in uniform.items()}
    d[1] = [0, 0, 0, 700, 650, 650]  # sum 2000
    candidates.append(("span1_tail", d))

    for name, sv in candidates:
        w = weights_from_span_vectors(sv)
        ok, r, tot = capacity_ok(w)
        if not ok:
            print(f"{name}: CAPACITY VIOLATION span {r} total {tot}", flush=True)
            continue
        print(f"\n=== {name} ===", flush=True)
        # probe at baseline boundary 7759 and slightly above
        for t in [7759, 7800, 7850]:
            v, lo = verify(t, 1_000_000, w)
            print(f"  eps={t/1e6:.6f} -> {v} {('lower='+f'{lo:.6f}') if lo else ''}", flush=True)
            if not v:
                break

if __name__ == "__main__":
    main()
