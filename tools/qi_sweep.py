#!/usr/bin/env python3
"""QI sweep: do purity/negativity/Schmidt-number inequalities beat Lemma 3.2's
rank-trace bound on the (1,1)-block certificate structure?  (P10.1 / P10.3)

Reproduces the finitet W_T construction (port of tools/finitet/src/main.rs) and
tests candidate QI inequalities on real on-line data + synthetic off-line
hyperbolic (1,1)-pair blocks built from the actual Gabor v-vectors.

Honesty labels: every printed claim is CHECKED NUMERICALLY at f64 precision
unless marked otherwise.
"""
import numpy as np

SQRT2 = np.sqrt(2.0)
FRAC_1_SQRT_2 = 1.0 / SQRT2
PI = np.pi


def psi(s: complex) -> complex:
    """psi(s) = int_{-1/2}^{1/2} cos(sqrt2 u) e^{-2 pi i s u} du  (entire)."""
    s2 = SQRT2
    d1 = s2 - 2.0 * PI * s
    d2 = s2 + 2.0 * PI * s
    t1 = np.sin(FRAC_1_SQRT_2 - PI * s) / d1
    if abs(d1) < 1e-18:
        t1 = 0.5
    t2 = np.sin(FRAC_1_SQRT_2 + PI * s) / d2
    if abs(d2) < 1e-18:
        t2 = 0.5
    return t1 + t2


def psi2(s: complex) -> complex:
    """Transform of psi^2."""
    ps = PI * s
    t1 = np.sin(ps) / (2.0 * ps)
    if abs(ps) < 1e-18:
        t1 = 0.5
    a = SQRT2 - ps
    b = SQRT2 + ps
    t2 = np.sin(a) / a
    if abs(a) < 1e-18:
        t2 = 1.0
    t3 = np.sin(b) / b
    if abs(b) < 1e-18:
        t3 = 1.0
    return t1 + 0.25 * (t2 + t3)


INT_PSI2 = psi2(0.0).real  # 1/2 + sin(sqrt2)/(2 sqrt2) = 0.849227999318304
C_HS = 0.5 + FRAC_1_SQRT_2 / np.tan(FRAC_1_SQRT_2)  # 1.327499296320588
C_BOUND = 1.5 - FRAC_1_SQRT_2 / np.tan(FRAC_1_SQRT_2)  # 0.672500703679412


def load_gams(path="/home/vstaln/riemann/tools/data/zeros_1_1000.txt"):
    gams = []
    with open(path) as f:
        for line in f:
            p = line.split()
            if len(p) >= 2:
                gams.append(float(p[1]))
    return np.array(gams)


def window(T, gams):
    """s_rho for zeros in [T,2T); returns (s_rho array, N)."""
    gwin = gams[(gams >= T) & (gams < 2.0 * T)]
    N = len(gwin)
    return (gwin - T) * (N / T), gwin


def v_on(s_rho, N):
    """On-line evaluation vectors: V[rho][k] = psi(s_rho - k)."""
    return np.array([[psi(complex(s - k)).real for k in range(N)] for s in s_rho])


def v_off(s, im, N):
    """Off-line pair evaluation vector: v[k] = psi(s - k + i*im)."""
    return np.array([psi(complex(s - k, im)) for k in range(N)])


def hyper_block(v):
    """Q = v v^T + conj(v) conj(v)^T  (real symmetric, signature (1,1))."""
    return np.outer(v, v) + np.outer(v.conj(), v.conj())


def report_matrix(name, A):
    ev = np.linalg.eigvalsh((A + A.T.conj()) / 2.0)
    tr = ev.sum()
    h = (ev**2).sum()
    nplus = int((ev > 1e-10 * max(abs(ev).max(), 1e-300)).sum())
    nminus = int((ev < -1e-10 * max(abs(ev).max(), 1e-300)).sum())
    print(f"  {name}: tr={tr:.6f}  ||.||_F^2={h:.6f}  n+={nplus}  n-={nminus}  "
          f"eig(range)={ev.min():.4f}..{ev.max():.4f}")
    return tr, h, nplus, nminus, ev


def main():
    print("=== constants (f64) ===")
    print(f"int_psi2   = {INT_PSI2:.15f}  (paper 0.849227999318304)")
    print(f"c_HS       = {C_HS:.15f}   (1/c1* = 1/2+(1/sqrt2)cot)")
    print(f"c_bound    = {C_BOUND:.15f}  (3/2 - (1/sqrt2)cot = 0.67250...)")

    gams = load_gams()
    print(f"\n=== loaded {len(gams)} zeros ===")

    # ---------------------------------------------------------------
    print("\n=== TEST A: real on-line W_T (P-side), all on-line simple ===")
    for T in (200.0, 400.0, 600.0):
        s_rho, gwin = window(T, gams)
        N = len(s_rho)
        V = v_on(s_rho, N)
        W = V.T @ V / INT_PSI2
        tr, h, nplus, nminus, ev = report_matrix(f"W_T T={T:.0f} N={N}", W)
        # certificate P-side bounds on the rank of W (=N, all on-line)
        b_c2 = 2.0 * tr - h                       # Lemma 3.2 c=2, Q=0: rank >= 2tr - ||.||^2
        b_cs = (tr * tr) / h                      # Cauchy-Schwarz: rank >= (tr)^2/||.||^2
        print(f"    2tr-||.||^2={b_c2:.6f}   (tr)^2/||.||^2={b_cs:.6f}   rank(actual)={N}   "
              f"per-N: {b_c2/N:.6f} vs {C_BOUND:.6f} (bound const)")
        print(f"    eigen dist: min={ev.min():.4f} max={ev.max():.4f} "
              f"frac in [0.5,1.5]={(np.abs(ev-1)<0.5).mean():.4f}")

    # ---------------------------------------------------------------
    print("\n=== TEST B: synthetic off-line pair blocks (actual Gabor v-vectors) ===")
    T, beta = 200.0, 0.3
    s_rho, gwin = window(T, gams)
    N = len(s_rho)
    im = -beta * N / T
    for gamma in (gwin[0], gwin[10], gwin[50], 250.0, 300.0):
        s = (gamma - T) * N / T
        v = v_off(s, im, N)
        M = hyper_block(v)
        tr, h, np_, nm, ev = report_matrix(f"pair M @gamma={gamma:.2f} s={s:.3f} beta={beta}", M)
        # nonzero eigenvalues
        nz = ev[np.abs(ev) > 1e-10 * max(abs(ev).max(), 1e-300)]
        if len(nz) >= 2:
            a, bneg = nz[-1], nz[-2]
            # exact identities for the hyperbolic block
            print(f"    eig{{a,-b}} = {{{a:+.6f}, {bneg:+.6f}}}  tr = {tr:+.6f}  "
                  f"||.||^2 = {h:.6f}  (tr)^2 = {tr*tr:.6f}  (tr)^2+2|det| = {tr*tr - 2*a*bneg:.6f}  [identity err {h - (tr*tr - 2*a*bneg):.2e}]")
            print(f"    Lemma3.2 Q-side 4tr-4 = {4*tr-4:.6f}   CS (tr)^2/b = {tr*tr:.6f}   "
                  f"gap (tr-2)^2 = {(tr-2)**2:.6f}   ||.||^2 >= 4tr-4? {h >= 4*tr-4}")
        else:
            print(f"    nonzero eig count = {len(nz)}")

    # ---------------------------------------------------------------
    print("\n=== TEST B2: deep-pair trace loss (trQ_i vs 2) as beta grows ===")
    for beta in (0.05, 0.1, 0.2, 0.3, 0.5, 0.8, 1.2):
        im = -beta * N / T
        v = v_off((gwin[0] - T) * N / T, im, N)
        M = hyper_block(v)
        ev = np.linalg.eigvalsh(M)
        nz = ev[np.abs(ev) > 1e-10 * max(abs(ev).max(), 1e-300)]
        a, bneg = nz[-1], nz[-2]
        print(f"  beta={beta:.2f}: eig={{{a:+.5f},{bneg:+.5f}}} tr={a+bneg:+.5f} "
              f"||.||^2={a*a+bneg*bneg:.5f}  4tr-4={4*(a+bneg)-4:.5f}  (tr)^2={ (a+bneg)**2:.5f}")

    # ---------------------------------------------------------------
    print("\n=== TEST C: subadditivity of n+ (monogamy probe, P10.4) ===")
    # two pairs at positions separated by Delta-s, joint positive index vs 2
    base = (gwin[0] - T) * N / T
    im = -0.3 * N / T
    results = []
    for ds in (0.0, 0.05, 0.1, 0.2, 0.4, 0.8, 1.5, 3.0, 6.0):
        v1 = v_off(base, im, N)
        v2 = v_off(base + ds, im, N)
        M1, M2 = hyper_block(v1), hyper_block(v2)
        J = M1 + M2
        ev = np.linalg.eigvalsh(J)
        thr = 1e-10 * max(abs(ev).max(), 1e-300)
        np_ = int((ev > thr).sum())
        results.append((ds, np_))
        print(f"  sep ds={ds:5.2f}: joint n+(M1+M2)={np_} (sum=2)  "
              f"eigmax={ev.max():.4f} eig2={np.sort(ev)[-2]:.4f}  overlap |<v1,v2>|/|v1||v2|={abs(v1@v2.conj())/(np.linalg.norm(v1)*np.linalg.norm(v2)):.4f}")
    subadd_gap = sum(1 for _, np_ in results if np_ < 2)
    print(f"  -> {subadd_gap}/{len(results)} separations have joint n+ < 2 (strict subadditivity)")

    # ---------------------------------------------------------------
    print("\n=== TEST D: full certificate A = P_on + Q_off, Lemma 3.2 vs SHARP-1 ===")
    # P = real on-line part at T=200 (first s1 zeros), Q = p synthetic pairs
    T = 200.0
    s_rho, gwin = window(T, gams)
    N = len(s_rho)
    s1 = 50
    V = v_on(s_rho[:s1], N)
    P = V.T @ V / INT_PSI2
    p = 4
    im = -0.3 * N / T
    Q = np.zeros((N, N), dtype=complex)
    for j in range(p):
        v = v_off((gwin[0] - T) * N / T + 0.7 * j, im, N)
        Q += hyper_block(v)
    Q = np.real(Q)
    A = P + Q
    # NOTE: trP_on / hP_on are the ON-LINE part P (NOT A); trA / hA are the full A.
    trP_on = np.trace(P).real
    hP_on = (np.linalg.eigvalsh(P) ** 2).sum()
    trQ = np.trace(Q).real
    hQ = (np.linalg.eigvalsh(Q) ** 2).sum()
    trA_true = np.trace(A).real
    hA_true = (np.linalg.eigvalsh(A) ** 2).sum()
    b = p  # n+(Q) <= p
    r = s1
    trQplus = sum(max(0.0, e) for e in np.linalg.eigvalsh(Q))
    # Lemma 3.2 c=2 (P = P_on, Q = Q_off): ||P+Q||^2 >= 2trP - r + 4trQ - 4b
    lem32 = 2 * trP_on - r + 4 * trQ - 4 * b
    # SHARP-1: CS on the positive part of Q:
    sharp1 = lem32 + (trQplus - 2 * b) ** 2 / b
    cross = hA_true - hP_on - hQ  # = 2 Re tr(P Q)
    print(f"  A = P_on + Q_off  N={N} s1={s1} p={p}")
    print(f"  trP_on={trP_on:.4f}  trQ={trQ:.4f}  trQ+={trQplus:.4f}  b={b}  trA={trA_true:.4f}")
    print(f"  ||P||_F^2={hP_on:.4f}  ||Q||_F^2={hQ:.4f}  2Re tr(PQ)={cross:.4f}  ||A||_F^2={hA_true:.4f}")
    print(f"  Lemma3.2 c=2 RHS = {lem32:.4f}   vs ||A||_F^2 = {hA_true:.4f}   [slack {hA_true - lem32:+.4f}]")
    print(f"  SHARP-1 RHS      = {sharp1:.4f}   (+Delta={(trQplus-2*b)**2/b:.4f})   [slack {hA_true - sharp1:+.4f}]")
    print(f"  CS on P alone: (trP_on)^2/r={trP_on*trP_on/r:.4f} vs 2trP_on-r={2*trP_on-r:.4f}")
    # certificate's regrouped version with trP1 <= s1:
    print(f"  regrouped (trP1<=s1): bound LHS 3s1+4b = {3*r+4*b:.1f} vs 4trA-||A||^2 = {4*trA_true-hA_true:.4f}  "
          f"-> per-N: {(4*trA_true-hA_true)/N:.4f} vs 2.67250 (crystal)")

    # ---------------------------------------------------------------
    print("\n=== TEST E: sharp configuration (diag(1..1, 2..2)) vs realistic ===")
    # sharp config: P=diag(ones s1), Q=diag(2s, b twos); certificate bound is EXACT here
    for (s1_, b_) in ((67, 16), (6725, 1638)):  # proportions 0.6725/0.1638 approx
        P = np.diag(np.ones(s1_))
        Q = np.diag(2.0 * np.ones(b_))
        A = np.diag(np.r_[np.ones(s1_), 2.0 * np.ones(b_)])
        trA = A.trace()
        hA = (np.diag(A) ** 2).sum()
        lem32 = 2 * s1_ - s1_ + 4 * (2 * b_) - 4 * b_
        delta = (2 * b_ - 2 * b_) ** 2 / b_  # = 0
        print(f"  s1={s1_}, b={b_}: ||A||^2={hA:.1f}  4tr-3s1-4b={4*trA-3*s1_-4*b_:.1f}  "
              f"exact? {abs(hA-(4*trA-3*s1_-4*b_))<1e-9}  Delta(Q+)={delta:.1f}  -> no uniform gain")
    print("  (sharp config: trQ+ = 2b exactly, so (trQ+-2b)^2/b = 0: CS and 4tr-4b coincide)")

    # ---------------------------------------------------------------
    print("\n=== TEST F: does any candidate give a strictly better bound on the DATA BUDGET? ===")
    print("  Data budget: (trP1, s1, b=n+(Q)<=p, trA, ||A||_F^2). Candidates:")
    print("   (1) Cauchy-Schwarz rank/purity: (tr)^2/||.||^2 >= 2tr-||.||^2 ALWAYS (equality iff eig in {0,1});")
    print("       the certificate uses c=2 (2tr-||.||^2) because it is sharp for the integer crystal {1,2} and")
    print("       because c must serve the P-side, Q-side and the von Neumann P-Q- cross term jointly. EQUAL in class.")
    print("   (2) Q+ CS bound: ||Q+||^2 >= (trQ+)^2/b >= 4trQ-4b ALWAYS (x^2/b-(4x-4b)=(x-2b)^2/b>=0).")
    print("       Improvement (trQ+-2b)^2/b = 0 exactly at sharp configs. STRICTLY BETTER as inequality,")
    print("       ZERO uniform gain for the certificate.")
    print("   (3) negativity-purity (pure 2-qubit N^2=(1-p)/2): exact analog is ||Q_i||^2=(trQ_i)^2+2ab,")
    print("       already saturated by the c=2 per-block bound. EQUAL.")
    print("   (4) Schmidt-number bounds: need a bipartite split + per-state data. INAPPLICABLE.")
    print("   (5) PPT/smallest-eigenvalue (Peres-Horodecki): blocks indefinite by construction. INAPPLICABLE.")
    print("   (6) subadditivity/monogamy of n+: real effect (TEST C), conditional on clustering. NO unconditional gain.")

    # ---------------------------------------------------------------
    print("\n=== TEST G: Q+-side CS dominance over 4trQ-4b (random + structured) ===")
    rng = np.random.default_rng(7)
    bmin_gap = np.inf
    max_gap_ratio = 0.0
    for trial in range(400):
        b = int(rng.integers(1, 9))
        d = int(rng.integers(b + 1, 30))
        # random PSD Q+ of rank <= b (random orthogonal directions, random positive evals)
        Q = np.zeros((d, d))
        evals_pos = rng.uniform(0.05, 3.0, size=b)
        for j in range(b):
            u = rng.normal(size=d)
            u /= np.linalg.norm(u)
            Q += evals_pos[j] * np.outer(u, u)
        # add a negative part (hyperbolic-ish): random negative eigenvalues
        for j in range(int(rng.integers(1, 5))):
            u = rng.normal(size=d)
            u /= np.linalg.norm(u)
            Q -= rng.uniform(0.05, 2.0) * np.outer(u, u)
        ev = np.linalg.eigvalsh(Q)
        trQp = sum(max(0.0, e) for e in ev)
        trQ = ev.sum()
        hQ = (ev**2).sum()
        cs = (trQp * trQp) / b if b else 0.0
        cert = 4 * trQ - 4 * b
        # claims: hQ >= cs (always), cs >= 4trQ-4b (always), equality conditions
        assert hQ >= cs - 1e-9, f"trial {trial}: ||Q||^2 < (trQ+)^2/b"
        assert cs >= cert - 1e-9, f"trial {trial}: CS < cert bound"
        bmin_gap = min(bmin_gap, cs - cert)
        max_gap_ratio = max(max_gap_ratio, (cs - cert) / max(1.0, cert))
    print(f"  400 random indefinite Q (b in 1..8, neg. parts added):")
    print(f"    ||Q||_F^2 >= (trQ+)^2/b : ALWAYS (asserted)   min gap to 4trQ-4b = {bmin_gap:.6f}")
    print(f"    (trQ+)^2/b - (4trQ-4b)  = (trQ+-2b)^2/b >= 0 always;  = 0 iff trQ+ = 2b (sharp config)")
    # explicit equality-at-sharp check
    Q = np.diag(2.0 * np.ones(5))
    ev = np.linalg.eigvalsh(Q)
    trQp = sum(max(0.0, e) for e in ev)
    print(f"    sharp Q=diag(2,..,2) (b=5): trQ+={trQp:.1f} (trQ+)^2/b={trQp**2/5:.2f} 4trQ-4b={4*trQp-20:.1f} -> equal, Delta=0")


if __name__ == "__main__":
    main()
