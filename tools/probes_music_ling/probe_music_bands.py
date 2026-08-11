#!/usr/bin/env python3
"""Probe M2.4 (music-ling catalog): distance-banded off-diagonal decomposition of the
finite-T moment deficit ("temporal masking" / edge-vs-bulk).

Question: the measured m2 (flat-window Gram, lambda=1) sits below the GUE value 4/3 at
finite height ([AF]'s Delta(T) ~ 1/log T). Where does the deficit concentrate - at small
normalized distance u (close pairs, the "masking"/repulsion region) or at large u (the
window/kernel-edge region, the Fisher-Hartwig-style artifact)?

Method: off-diagonal sum O = sum_{i!=j} sinc^2(pi*(x_i-x_j)) (x density-1 rescaled),
computed EXACTLY in row chunks, decomposed into distance bands [k,k+1) for k=0..15 plus a
tail bucket u>=16. GUE expectation per band (DPP two-point function 1 - sinc^2):
E_k ~= lambda^2 * L * int_k^{k+1} sinc^2(pi u) (1 - sinc^2(pi u)) du.
Report (O_k - E_k)/n per band and cumulative deficit for u<1 vs u>=1.
Data: tools/data/zeros_computed_10000.txt.
"""
import numpy as np
from scipy import integrate

def load(fn):
    g = []
    with open(fn) as f:
        for line in f:
            p = line.split()
            if len(p) >= 2:
                g.append(float(p[1]))
    return np.sort(np.array(g))

def sinc2(u):
    s = np.sinc(u)
    return s * s

def main():
    x = load("data/zeros_computed_10000.txt")
    n = x.size
    L = x[-1] - x[0]
    sp = L / (n - 1)
    u = (x - x[0]) / sp
    lam = n / L
    print(f"n={n}  L={L:.1f}  lambda={lam:.4f}")

    # exact full off-diagonal (ordered pairs) in row chunks
    # O_k = 2 * sum over unordered pairs with dist in band k, weight sinc^2
    K = 16
    O = np.zeros(K + 1)  # last bucket = tail u >= 16
    for i in range(n):
        d = np.abs(u - u[i])
        # ordered-pair sum: iterating all j counts both (i,j) and (j,i) -> weight sinc^2
        w = np.where(d > 0, sinc2(d), 0.0)
        k = np.floor(d).astype(int)
        k = np.clip(k, 0, K)
        np.add.at(O, k, w)
    # note: pairs with d < 0.5 in the k=0 bucket include near-coincident pairs; fine.

    # GUE expectation per band (ordered pairs; two-sided integral -> factor 2)
    E = np.zeros(K + 1)
    for k in range(K):
        val, _ = integrate.quad(lambda t: sinc2(k + t) * (1.0 - sinc2(k + t)), 0.0, 1.0)
        E[k] = 2.0 * lam * lam * L * val
    tail, _ = integrate.quad(lambda t: sinc2(16.0 + t) * (1.0 - sinc2(16.0 + t)), 0.0, np.inf)
    E[K] = 2.0 * lam * lam * L * tail

    m2_exact = 1.0 + O.sum() / n
    print(f"\nm2 (exact, full off-diagonal) = {m2_exact:.5f}   deficit vs 4/3 = {m2_exact - 4/3:+.5f}")

    print("\n== banded off-diagonal: measured vs GUE expectation ==")
    print("band          O_k/n      E_k/n     (O-E)/n    cum(O-E)/n")
    cum = 0.0
    for k in range(K + 1):
        dO = (O[k] - E[k]) / n
        cum += dO
        lab = f"u in [{k},{k+1})" if k < K else "u >= 16 (tail)"
        print(f"{lab:15s}  {O[k]/n:9.4f}  {E[k]/n:9.4f}  {dO:+9.5f}  {cum:+9.5f}")

    dO0 = (O[0] - E[0]) / n
    dO1 = (O[1:K + 1].sum() - E[1:K + 1].sum()) / n
    print(f"\ndeficit u<1  (close pairs / masking region): {dO0:+.5f}")
    print(f"deficit u>=1 (kernel-edge + long-range):      {dO1:+.5f}")
    print("(positive dO0 = deficit concentrated at close pairs; negative = surplus)")

if __name__ == "__main__":
    main()
