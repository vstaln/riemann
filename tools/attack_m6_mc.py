#!/usr/bin/env python3
"""attack_m6_mc.py — sine-process Gram-matrix moments m2..m6 at lambda in {1/4, 1/3, 1}.
Extends tools/sine_sim.py to moments 5, 6 and smaller lambdas.
Normalization: G_ij = sinc(pi*la*(x_i - x_j)) over sine-process sample; m_k = tr(G^k)/n.
Cross-checks vs EXACT: m2 = 1/la + la/3 ; m3 = 1 + 1/la^2 (both verified identities).
Usage: uv run --quiet --with numpy python tools/attack_m6_mc.py
"""
import numpy as np, sys, time

def run(la, NSAMP=120, L=60.0, M=1200, seed=11):
    rng = np.random.default_rng(seed)
    xs = np.linspace(-L/2, L/2, M, endpoint=False)
    dx = L/M
    S = np.sinc((xs[:, None] - xs[None, :]))
    K = S * dx
    evals, evecs = np.linalg.eigh(K)
    mask = evals > 1e-10
    evals = evals[mask]; evecs = evecs[:, mask]
    Psi = evecs * np.sqrt(dx)
    r_max = Psi.shape[1]

    def sample_config():
        inc = rng.random(r_max) < evals
        if not inc.any():
            return np.zeros(0)
        PsiJ = Psi[:, inc]
        r = PsiJ.shape[1]
        Pmm = np.einsum('ij,ij->i', PsiJ, PsiJ)
        chosen = []
        while len(chosen) < r:
            if chosen:
                X = np.array(chosen); PX = PsiJ[X, :]; A = PX @ PX.T
                PmX = PsiJ @ PX.T
                sol = np.linalg.solve(A, PmX.T)
                corr = np.einsum('mk,mk->m', PmX, sol.T)
                diag = np.clip(Pmm - corr, 0, None)
            else:
                diag = Pmm
            tot = diag.sum()
            if tot < 1e-9:
                break
            m = rng.choice(M, p=diag / tot)
            chosen.append(m)
        return xs[np.array(chosen)]

    def moments(pts, la):
        n = pts.size
        if n < 6:
            return (0.0,)*5
        d = pts[:, None] - pts[None, :]
        G = np.sinc(la * d)
        G2 = G @ G
        Gk = G2
        out = [np.trace(Gk)/n]
        for _ in range(4):
            Gk = Gk @ G
            out.append(np.trace(Gk)/n)
        return tuple(out)   # (m2, m3, m4, m5, m6)

    acc = [[] for _ in range(5)]
    t0 = time.time()
    for s in range(NSAMP):
        pts = sample_config()
        if pts.size >= 6:
            vals = moments(pts, la)
            for i in range(5):
                acc[i].append(vals[i])
        if (s+1) % 40 == 0:
            print(f"  la={la} {s+1}/{NSAMP} ({time.time()-t0:.0f}s)", flush=True)
    res = []
    for i, a in enumerate(acc):
        a = np.array(a)
        res.append((a.mean(), a.std()/np.sqrt(a.size)))
    return res

if __name__ == "__main__":
    la_list = [float(x) for x in sys.argv[1:]] or [0.25, 1/3, 1.0]
    nsamp = int(sys.argv[-1]) if len(sys.argv) > 1 and sys.argv[-1].isdigit() else 120
    m2t = lambda la: 1/la + la/3
    m3t = lambda la: 1 + 1/la**2
    for la in la_list:
        res = run(la, NSAMP=nsamp)
        print(f"lambda={la}:  m2 = {res[0][0]:.4f} +- {res[0][1]:.4f}  (exact {m2t(la):.4f})")
        print(f"             m3 = {res[1][0]:.4f} +- {res[1][1]:.4f}  (exact {m3t(la):.4f})")
        print(f"             m4 = {res[2][0]:.4f} +- {res[2][1]:.4f}")
        print(f"             m5 = {res[3][0]:.4f} +- {res[3][1]:.4f}")
        print(f"             m6 = {res[4][0]:.4f} +- {res[4][1]:.4f}")
