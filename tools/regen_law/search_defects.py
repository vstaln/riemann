#!/usr/bin/env python3
"""Search: mixtures of 'lattice + defects' configs approximating f(j)=j for j=1..255.
Defect types: moved points (offset eps, rational) and doubled points.
Question: can few configs span the ramp? What's the min residual?"""
import numpy as np
from scipy.optimize import linprog
import itertools

N = 256

def config_spectrum(moved, doubled, eps=0.5):
    """lattice 0..255, moved: list of base positions moved by +eps, doubled: list marked 2.
    Returns f(j), j=1..N."""
    j = np.arange(1, N+1)
    z = np.zeros(N, dtype=complex)
    for b in moved:
        z += np.exp(2j*np.pi*j*(b+eps)/N) - np.exp(2j*np.pi*j*b/N)
    for b in doubled:
        z += np.exp(2j*np.pi*j*b/N)   # mark 1->2 adds +1*e
    return np.abs(z)**2

def solve_weights(Fs, scs, tau=0.0, Fb=None):
    m = len(Fs)
    A_ub, b_ub = [], []
    for jj in range(N-1):
        row = np.array([F[jj] for F in Fs]); A_ub.append(row); b_ub.append((jj+1)+tau)
        row = -np.array([F[jj] for F in Fs]); A_ub.append(row); b_ub.append(-(jj+1)+tau)
    if Fb is not None:
        A_ub.append(np.array([F[N-1] for F in Fs])); b_ub.append(Fb)
    A_eq = np.ones((1,m)); b_eq=[1.0]
    res = linprog(np.array(scs), A_ub=np.array(A_ub), b_ub=np.array(b_ub), A_eq=A_eq, b_eq=b_eq,
                  bounds=[(0,None)]*m, method='highs')
    return res

# Candidate configs: all combinations of up to 2 moved + up to 2 doubled among a few positions,
# with a few offsets.
rng = np.random.default_rng(5)
base_pos = list(range(256))
cands = []
for eps in (0.5, 0.25, 0.75, 1/3, 1/6, 1/4+1/256):
    for _ in range(400):
        n_m = rng.integers(0, 3); n_d = rng.integers(0, 3)
        moved = rng.choice(256, size=n_m, replace=False).tolist() if n_m else []
        doubled = rng.choice(256, size=n_d, replace=False).tolist() if n_d else []
        # ensure disjoint
        doubled = [p for p in doubled if p not in moved]
        cands.append((moved, doubled, eps))

# evaluate a pool, run LP on random subsets to find best mix
best_res = None
best_mix = None
pool_size = min(len(cands), 120)
for trial in range(3):
    idx = rng.choice(len(cands), size=pool_size, replace=False)
    Fs = [config_spectrum(*cands[i][:2], eps=cands[i][2]) for i in idx]
    scs = [256 - 2*len(cands[i][1]) for i in idx]
    res = solve_weights(Fs, scs)
    if res.success:
        resval = res.fun/N
        fbar = np.array([F[j] for F in Fs]) @ res.x
        resid = np.max(np.abs(fbar[:255] - np.arange(1,256)))
        print(f"trial {trial}: feasible, min p1 = {resval:.6f}, max row resid = {resid:.4f}")
        if best_res is None or resid < best_res[0]:
            best_res = (resid, resval)
            best_mix = (idx, res.x)
    else:
        print(f"trial {trial}: infeasible")
if best_res:
    print(f"\nbest: max resid = {best_res[0]:.4f}, p1 = {best_res[1]:.6f}")
    idx, w = best_mix
    print("positive-weight configs:")
    for i, wi in zip(idx, w):
        if wi > 1e-9:
            moved, doubled, eps = cands[i]
            print(f"  w={wi:.4f} moved={moved} doubled={doubled} eps={eps} s={256-2*len(doubled)}")
