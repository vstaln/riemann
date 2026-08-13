#!/usr/bin/env python3
"""
ADVERSARIAL LP-VERIFIER LOOP for the (psum, l, c) joint search.

Loop: solve max-min LP over current adverse config set (with tawan base +
free (l,c) perturbation), run the REAL interval verifier on the LP solution,
add any unresolved terminal cell to the config set, repeat until the LP
solution certifies the target eps (or the loop stalls).

Usage: python adv_lp_loop.py <D> <eps_target> [alpha] [--max-iters N]
"""
import sys, math
import mpmath as mp
mp.mp.dps = 40
import numpy as np
from scipy.optimize import linprog

sys.path.insert(0, 'tools')
from verify_coboundary_floor import verify_floor, cosine_kernel

ALPHA = float(sys.argv[3]) if len(sys.argv) > 3 else 1.464
D = int(sys.argv[1])
EPS_TARGET = float(sys.argv[2])
MAX_ITERS = int(sys.argv[4]) if len(sys.argv) > 4 else 12

def sinc(z): return mp.sin(z)/z if z != 0 else mp.mpf(1)
def K(x, a):
    w = a
    return (sinc((w - 2*mp.pi*x)/2) + sinc((w + 2*mp.pi*x)/2))/2
_K0 = float(K(mp.mpf(0), mp.mpf(str(ALPHA))))
def w(x): return float((K(mp.mpf(x), mp.mpf(str(ALPHA)))/_K0)**2)

def F_affine(g, D):
    """coeff = (l_1..l_5, c_1..c_5), const: F_B(g) = coeff·x + const."""
    p0 = 1.0/(6.0*D); q0 = 1.0/3.0
    a_ab = {(a,b): 2.0/(7-(b-a)) for a in range(7) for b in range(a+1,7)}
    y = [0.0]
    for gi in g: y.append(y[-1]+gi)
    wg = [w(gi) for gi in g]
    lc = [0.0]*5; cc = [0.0]*5
    const = sum(p0*gi + q0*wgi for gi, wgi in zip(g, wg))
    for k in range(1, 6):
        lc[k-1] = g[k] - g[k-1]
        cc[k-1] = wg[k] - wg[k-1]
    for (a,b), coef in a_ab.items():
        const += coef*w(y[b]-y[a])
    return lc+cc, const

def direct_FB(g, D, l, c):
    p0 = 1.0/(6.0*D); q0 = 1.0/3.0
    p = [p0 + (l[i-1] if i-1>=0 and i-1<5 else 0.0) - (l[i] if i<5 else 0.0) for i in range(6)]
    q = [q0 + (c[i-1] if i-1>=0 and i-1<5 else 0.0) - (c[i] if i<5 else 0.0) for i in range(6)]
    y = [0.0]
    for gi in g: y.append(y[-1]+gi)
    tot = sum(p[i]*g[i] + q[i]*w(g[i]) for i in range(6))
    for a in range(7):
        for b in range(a+1,7):
            tot += (2.0/(7-(b-a)))*w(y[b]-y[a])
    return tot

def base_configs(D):
    configs = []
    # period-2 and period-3 crystals
    for ia in np.linspace(0.8, 2.2, 35):
        for ib in np.linspace(0.8, 2.2, 35):
            configs.append((float(ia),float(ib),float(ia),float(ib),float(ia),float(ib)))
    for ia in np.linspace(0.8, 2.2, 12):
        for ib in np.linspace(0.8, 2.2, 12):
            for ic in np.linspace(0.8, 2.2, 12):
                configs.append((float(ia),float(ib),float(ic),float(ia),float(ib),float(ic)))
    # one huge gap
    for pos in range(6):
        for H in [5.0, 10.0, 21.0]:
            for s in [1.05, 1.5, 1.99]:
                g2 = [s,1.05,1.99,s,1.05,s]; g2[pos]=H
                configs.append(tuple(g2))
    # two huge gaps
    for p1 in range(6):
        for p2 in range(p1+1,6):
            for H in [8.0, 21.0]:
                g=[1.05]*6; g[p1]=H; g[p2]=H; configs.append(tuple(g))
    # near-uniform
    for i0 in np.linspace(1.9, 2.1, 10):
        for i1 in np.linspace(1.9, 2.1, 10):
            for i2 in np.linspace(1.9, 2.1, 10):
                configs.append((float(i0),float(i1),float(i2),float(i0),float(i1),float(i2)))
    return list(dict.fromkeys(configs))

def solve_lp(D, configs, target):
    m = len(configs)
    A_rows=[]; b_rows=[]
    for gg in configs:
        coeff, const = F_affine(gg, D)
        # constraint: F >= target  =>  -coeff·x <= const - target ... but we want
        # F(x) = const + coeff·x >= target => -coeff·x <= const - target
        A_rows.append([-c for c in coeff]); b_rows.append(const - target)
    A = np.array(A_rows); b = np.array(b_rows)
    # variable bounds on l, c
    bounds = [(None,None)]*5 + [(-0.06,0.06)]*5
    # feasibility only: objective 0
    c_obj = np.zeros(10)
    res = linprog(c_obj, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    return res

def main():
    scale = 320.0/float(D)
    configs = base_configs(D)
    print(f"== adversarial LP loop: D={D}, target eps={EPS_TARGET}, alpha={ALPHA} ==", flush=True)
    wdict = {(i,j): 2.0/(7-(j-i)) for i in range(7) for j in range(i+1,7)}
    for it in range(MAX_ITERS):
        res = solve_lp(D, configs, EPS_TARGET)
        if not res.success:
            print(f"  iter {it}: LP INFEASIBLE ({res.message[:60]})", flush=True)
            return
        x = res.x
        l = x[:5]; c = x[5:10]
        p0 = 1.0/(6.0*D); q0 = 1.0/3.0
        p = [p0 + (l[i-1] if i-1>=0 and i-1<5 else 0.0) - (l[i] if i<5 else 0.0) for i in range(6)]
        q = [q0 + (c[i-1] if i-1>=0 and i-1<5 else 0.0) - (c[i] if i<5 else 0.0) for i in range(6)]
        r = verify_floor(cosine_kernel(ALPHA), wdict, 1.0/3000, 6, EPS_TARGET,
                         grid=4000, cap_scheme='coboundary',
                         pressure_coeffs=list(p), nearest_coeffs=list(q),
                         max_nodes=25000000)
        print(f"  iter {it}: verified={r['verified']} nodes={r['nodes']}", flush=True)
        if r['verified']:
            print("  *** CERTIFIED ***")
            print("  l =", [f"{v:.9f}" for v in l])
            print("  c =", [f"{v:.9f}" for v in c])
            print("  p =", [f"{v:.10f}" for v in p])
            print("  q =", [f"{v:.10f}" for v in q])
            return
        reason = r.get('reason','')
        # extract terminal cell from reason string
        import re
        nums = re.findall(r'\d+', reason)
        if len(nums) < 12:
            print("  no terminal cell coords in reason:", reason[:120], flush=True)
            return
        # the 12 integers are (lo1,hi1),(lo2,hi2),... for 6 coords; take the lo's
        cell = tuple(int(nums[2*i])/4000.0 for i in range(6))
        print(f"  + adding terminal cell {tuple(round(v,4) for v in cell)}", flush=True)
        configs.append(cell)
        configs = list(dict.fromkeys(configs))
    print("  loop exhausted without certification")

if __name__ == '__main__':
    main()
