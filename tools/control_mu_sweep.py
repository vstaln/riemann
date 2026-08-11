#!/usr/bin/env python3
"""C-MU2: control-family inequality sweep vs Lemma 3.2 on the (1,1)-block certificate.

Independent, control-theory-side answer to the class-level question that
attack-qi-sweep.md closed from the quantum-information side:

  Does any inequality beat Lemma 3.2's rank-trace bound
      r >= 2 trP + 4 trQ - 4 b - ||P+Q||_F^2            (Lemma 3.2, c = 2)
  on the certificate's data budget D = (trP, trA, ||A||_F^2, rank P = r, n+(Q) = b)?

Candidates (control family, C-MU2):
  GLOVER    balanced-truncation 2*sum-sigma error bound (needs Hankel singular
            values = a transfer function; the certificate has none.  Even granted
            the full spectrum |lambda_i(A)| the family's natural lower bound on
            ||A||_F^2 -- the top-r eigenvalue energy (Eckart-Young / 2-sigma) --
            misses the Q-side charge and is strictly below Lemma 3.2's L at the
            sharp crystal).
  PERRON    Perron-Frobenius max-row-sum / rank-1 purity family (needs entrywise
            data = zero-side data, outside D; the D-only lambda_max >= trQ+/b
            form gives ||Q+||_F^2 >= (trQ+)^2/b^2, strictly weaker than the CS
            bound (trQ+)^2/b and than Lemma 3.2's flat charge at the sharp
            crystal for b >= 2).
  OSTR-SCH  Ostrowski-Schneider inertia transfer (needs the Hilbert-Polya
            dynamics A of the zeros -- RH itself; the finite content n+(A+Q) >=
            n+(A) for Q >= 0 is the monotonicity already consumed as Lemma 3.1).
  D-SCALED  inf_D ||D A D^-1|| D-scaled mu upper bounds (upper bounds on the
            robustness margin, C-MU1 confirmation of attack-lpdual; numerically
            inf_D ||DAD^-1||_F <= ||A||_F -- the scaled norm can only shrink,
            the wrong direction for a lower-bound certificate).

Expected verdict (task brief): NO -- independent confirmation of the QI sweep.
The certificate consumes the EXACT (trA, ||A||_F^2) from the prime side, so a
lower bound on ||A||_F^2 is moot at the certificate level, and any D-only bound
on the counts (s1, b) is capped by the sharp crystal diag(1^r, 2^b) (Lemma 3.2
equality case; lemmaR_tight / Prop 4.4(b), PROVEN).

Every printed number is CHECKED NUMERICALLY (f64, numpy) unless marked PROVEN.
Reproduce:  uv run --with numpy python tools/control_mu_sweep.py
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from qi_sweep import (  # noqa: E402
    INT_PSI2, C_HS, C_BOUND, load_gams, window, v_on, v_off, hyper_block,
)

PI = np.pi


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------

def nplus(ev, thr_rel=1e-10):
    thr = thr_rel * max(abs(ev).max(), 1e-300)
    return int((ev > thr).sum())


def tr_plus(ev):
    return float(sum(max(0.0, e) for e in ev))


def herm(A):
    return (A + A.T.conj()) / 2.0


def bounds_for(P, Q, r, b, evA=None, evQ=None):
    """Side-by-side L-form lower bounds on ||A||_F^2 for A = P + Q.

    Lemma 3.2 (c=2):   ||A||_F^2 >= L  = 2trP - r + 4trQ - 4b
    CS refinement (QI sweep (L')):  Lp = 2trP - r - 4trQ_- + (trQ_+)^2/b
    Perron lambda_max >= trQ_+/b:   Lper = 2trP - r - 4trQ_- + (trQ_+)^2/b^2
    Glover-family w/ full spectrum: Lglo = top-r eigenvalue energy of A
    (evA/evQ may be passed in to avoid O(d^3) eigendecompositions.)
    """
    trP = float(np.real(np.trace(P)))
    trQ = float(np.real(np.trace(Q)))
    if evQ is None:
        evQ = np.linalg.eigvalsh(herm(Q))
    tQp = tr_plus(evQ)
    tQm = tr_plus(-evQ)
    if evA is None:
        evA = np.linalg.eigvalsh(herm(P + Q))
    hA = float((np.abs(evA) ** 2).sum())
    L = 2.0 * trP - r + 4.0 * trQ - 4.0 * b
    qp_term = (tQp * tQp) / b if b > 0 else 0.0
    Lp = 2.0 * trP - r - 4.0 * tQm + qp_term
    Lper = 2.0 * trP - r - 4.0 * tQm + ((tQp * tQp) / (b * b) if b > 0 else 0.0)
    top = float(np.sort(np.abs(evA) ** 2)[::-1][:max(int(r), 0)].sum())
    return dict(trP=trP, trQ=trQ, tQp=tQp, tQm=tQm, hA=hA, L=L, Lp=Lp,
                Lper=Lper, Lglo=top, r=r, b=b, nAplus=nplus(evA))


def inf_D_Fnorm(A, iters=4000, tol=1e-13):
    """inf over diagonal D > 0 of ||D A D^{-1}||_F^2 (A Hermitian).

    Convex in x = log D; exact per-coordinate minimization
    (x_i <- 0.25*ln( sum_{j!=i} C_ji e^{2x_j} / sum_{j!=i} C_ij e^{-2x_j} ),
    C_ij = |A_ij|^2)."""
    n = A.shape[0]
    C = np.abs(A) ** 2
    x = np.zeros(n)
    obj_prev = None
    for _ in range(iters):
        for i in range(n):
            a = (C[i, :] * np.exp(-2.0 * x)).sum() - C[i, i]
            b = (C[:, i] * np.exp(2.0 * x)).sum() - C[i, i]
            if a > 0 and b > 0:
                x[i] = 0.25 * np.log(b / a)
        d = np.exp(x)
        S = (d[:, None] / d[None, :]) * A
        obj = float(np.real(np.trace(S @ S.T.conj())))
        if obj_prev is not None and abs(obj_prev - obj) < tol:
            break
        obj_prev = obj
    return obj, d


# --------------------------------------------------------------------------
# TEST 1: sharp crystal (Lemma 3.2 equality case) -- every candidate is <= L
# --------------------------------------------------------------------------

def test1_sharp():
    print("=== T1: sharp crystal A = diag(1^r, 2^b) (Lemma 3.2 equality case) ===")
    print("    (PROVEN: lemmaR_tight / Prop 4.4(b); the equality case of Lemma 3.2 is")
    print("     P = Pi_1, Q = 2*Pi_2, Pi_1 _|_ Pi_2, ranks r, b -- checked here)")
    for (r, b) in ((2, 1), (67, 16), (6725, 1638)):
        # sharp crystal: P = I_r, Q = 2*I_b (diagonal A = diag(1^r, 2^b));
        # spectrum is explicit -- no O(d^3) eigendecomposition needed.
        P = np.eye(r)
        Q = 2.0 * np.eye(b)
        evA = np.r_[np.ones(r), 2.0 * np.ones(b)]
        u = bounds_for(P, Q, r, b, evA=evA)
        exact = abs(u["hA"] - u["L"]) < 1e-9
        print(f"  (r,b)=({r},{b}): trP={u['trP']:.1f} trQ={u['trQ']:.1f} "
              f"trQ+={u['tQp']:.1f} ||A||^2={u['hA']:.1f}")
        print(f"    L(lemma3.2)={u['L']:.4f}  L'(CS)={u['Lp']:.4f} "
              f"Lper={u['Lper']:.4f}  Lglo(top-{r})={u['Lglo']:.4f}  "
              f"Lemma-exact? {exact}")
        print(f"    gains over L: CS {u['Lp']-u['L']:+.4f}  Perron {u['Lper']-u['L']:+.4f}  "
              f"Glover-top {u['Lglo']-u['L']:+.4f}")
    print("    -> at the sharp crystal: L == ||A||^2 (exact); CS gain = 0;")
    print("       Perron gain = 4-4b < 0 for b >= 2; Glover-top gain = -4b < 0.")


# --------------------------------------------------------------------------
# TEST 2: real on-line W_T (P-side): the family is capped by Cauchy-Schwarz
# --------------------------------------------------------------------------

def test2_online():
    print("\n=== T2: real on-line W_T (P-side, Q = 0): rank family cap ===")
    gams = load_gams()
    for T in (200.0, 400.0, 600.0):
        s_rho, gwin = window(T, gams)
        N = len(s_rho)
        V = v_on(s_rho, N)
        W = V.T @ V / INT_PSI2
        W = herm(W)
        ev = np.linalg.eigvalsh(W)
        tr = float(ev.sum())
        h = float((ev**2).sum())
        b_c2 = 2.0 * tr - h            # Lemma 3.2 c=2, Q=0: rank >= 2tr - ||.||^2
        b_cs = tr * tr / h             # CS: rank >= (tr)^2 / ||.||^2  (the family cap)
        print(f"  T={T:.0f} N={N}: 2tr-||.||^2={b_c2:.4f} (tr)^2/||.||^2={b_cs:.4f} "
              f"rank={N}  per-N: {b_c2/N:.6f} vs {C_BOUND:.6f}  "
              f"CS-win={b_cs-b_c2:.4f} = (tr-||.||^2)^2/||.||^2={(tr-h)**2/h:.4f}")
    print("    -> CS >= 2tr-||.||^2 always (equality iff eigenvalues in {0,1});")
    print("       the gap (r - trP)^2/r is a finite-T artifact (trP/N -> 1), not a")
    print("       uniform gain -- matches the QI sweep TEST A.")


# --------------------------------------------------------------------------
# TEST 3: synthetic hyperbolic (1,1) pair blocks (actual Gabor v-vectors)
# --------------------------------------------------------------------------

def test3_pairs():
    print("\n=== T3: synthetic off-line hyperbolic pair blocks (Gabor v-vectors) ===")
    T, beta = 200.0, 0.3
    s_rho, gwin = window(T, load_gams())
    N = len(s_rho)
    im = -beta * N / T
    for gamma in (gwin[0], gwin[10], 250.0, 300.0):
        s = (gamma - T) * N / T
        v = v_off(s, im, N)
        M = hyper_block(v)
        M = herm(M)
        ev = np.linalg.eigvalsh(M)
        nz = ev[np.abs(ev) > 1e-10 * max(abs(ev).max(), 1e-300)]
        a, bneg = nz[-1], nz[-2]
        tr = float(ev.sum())
        h = float((ev**2).sum())
        tQp = tr_plus(ev)
        L = 4.0 * tr - 4.0          # Lemma 3.2 Q-side, single block b = 1
        Lp = (tQp * tQp) / 1.0      # CS, b = 1
        Lper = (tQp * tQp) / 1.0    # Perron == CS when b = 1
        obj, d = inf_D_Fnorm(M)
        print(f"  pair @gamma={gamma:.2f}: eig={{+{a:.5f}, {bneg:.5f}}} tr={tr:.5f} "
              f"trQ+={tQp:.5f} ||Q||^2={h:.5f}")
        print(f"    L=4tr-4={L:.5f}  L'(CS)=(trQ+)^2={Lp:.5f}  "
              f"(trQ+-2)^2={(tQp-2)**2:.5f}  inf_D||DQD^-1||^2={obj:.5f} (vs {h:.5f})")
    print("    -> single block (b=1): CS == Perron; identity ||Q||^2 = (trQ)^2 + 2ab;")
    print("       deep pairs: both bounds very loose; D-scaling cannot shrink the")
    print("       F-norm at all (T6) -- it is a margin bound, not a certificate bound.")
    print("    -> Perron vs CS differ only for b >= 2 (T4/T5).")


# --------------------------------------------------------------------------
# TEST 4: mixed certificate A = P_on + Q_off (like QI TEST D), full table
# --------------------------------------------------------------------------

def test4_mixed():
    print("\n=== T4: mixed A = P_on(s1) + Q_off(p pairs), full side-by-side ===")
    T = 200.0
    s_rho, gwin = window(T, load_gams())
    N = len(s_rho)
    s1 = 50
    p = 4
    V = v_on(s_rho[:s1], N)
    P = herm(V.T @ V / INT_PSI2)
    im = -0.3 * N / T
    Q = np.zeros((N, N), dtype=complex)
    for j in range(p):
        v = v_off((gwin[0] - T) * N / T + 0.7 * j, im, N)
        Q += hyper_block(v)
    Q = herm(np.real(Q))
    A = herm(P + Q)
    u = bounds_for(P, Q, s1, p)
    print(f"  N={N} s1={s1} p={p} (b={p}): trP={u['trP']:.4f} trQ={u['trQ']:.4f} "
          f"trQ+={u['tQp']:.4f} ||A||^2={u['hA']:.4f} n+(A)={u['nAplus']}")
    print(f"    L(lemma3.2) = {u['L']:.4f}   (slack ||A||^2 - L = {u['hA']-u['L']:+.4f})")
    print(f"    L'(CS)      = {u['Lp']:.4f}   (gain {(u['tQp']-2*p)**2/p:.4f} = "
          f"(trQ+-2b)^2/b)")
    print(f"    Lper        = {u['Lper']:.4f}   (Perron gain {u['Lper']-u['L']:+.4f})")
    print(f"    Lglo(top-{s1}) = {u['Lglo']:.4f}   (Glover-family, full-spectrum grant; "
          f"gain {u['Lglo']-u['L']:+.4f})")
    print(f"    all candidates valid lower bounds? "
          f"{all(x <= u['hA'] + 1e-6 for x in (u['L'], u['Lp'], u['Lper'], u['Lglo']))}")
    # certificate level: the LP constraint 3s1+4b >= 4trA - ||A||^2 holds w/ slack
    cert = 4.0 * (u["trP"] + u["trQ"]) - u["hA"]
    print(f"    certificate: 4trA-||A||^2 = {cert:.4f} <= 3s1+4b = {3*s1+4*p:.1f} "
          f"(slack {3*s1+4*p-cert:+.4f}); bound/N = {(cert)/N:.6f} vs 2.67250 (crystal)")


# --------------------------------------------------------------------------
# TEST 5: gap distribution over random configurations
# --------------------------------------------------------------------------

def random_mixed(rng, d, r, b, beta_range=(0.05, 1.2)):
    P = np.zeros((d, d), dtype=complex)
    for _ in range(r):
        u = rng.normal(size=d) + 1j * rng.normal(size=d)
        u /= np.linalg.norm(u)
        P += np.outer(u, u.conj())
    Q = np.zeros((d, d), dtype=complex)
    for _ in range(b):
        v = rng.normal(size=d) + 1j * rng.normal(size=d)
        v *= rng.uniform(*beta_range)
        Q += np.outer(v, v) + np.outer(v.conj(), v.conj())
    return herm(P), herm(Q), herm(P + Q)


def test5_gap_distribution():
    print("\n=== T5: gap distribution over random (1,1)-block configs ===")
    rng = np.random.default_rng(11)
    M = 500
    d, r, b = 40, 12, 4
    stat = {k: [] for k in ("cs", "per", "glo")}
    n_beat = {"cs": 0, "per": 0, "glo": 0}
    valid_cs = True
    for _ in range(M):
        P, Q, A = random_mixed(rng, d, r, b)
        u = bounds_for(P, Q, r, b)
        stat["cs"].append(u["Lp"] - u["L"])      # = (trQ+-2b)^2/b >= 0
        stat["per"].append(u["Lper"] - u["L"])
        stat["glo"].append(u["Lglo"] - u["L"])
        if u["Lp"] > u["L"] + 1e-9:
            n_beat["cs"] += 1
        if u["Lper"] > u["L"] + 1e-9:
            n_beat["per"] += 1
        if u["Lglo"] > u["L"] + 1e-9:
            n_beat["glo"] += 1
        if u["Lp"] < u["L"] - 1e-9:
            valid_cs = False
    for k, lab in (("cs", "CS (L')"), ("per", "Perron"), ("glo", "Glover-top")):
        arr = np.array(stat[k])
        print(f"  {lab}: gain over L  min={arr.min():+.6f} median={np.median(arr):+.6f} "
              f"max={arr.max():+.6f}   #beats L: {n_beat[k]}/{M}")
    print(f"  CS >= Lemma always (asserted): {valid_cs}")
    print("    -> pointwise gains are common (non-sharp configs) but the uniform gain is 0:")
    print("       the sharp crystal diag(1^r,2^b) is in the class and has gain 0 (T1);")
    print("       Perron/Glover-top are < L there.  The certificate must cover all configs,")
    print("       so no D-only candidate moves the LP minimum (lemmaR_tight, PROVEN).")


# --------------------------------------------------------------------------
# TEST 6: D-scaling -- inf_D ||DAD^-1|| can only shrink (margin bound, not a
#         lower-bound certificate inequality)
# --------------------------------------------------------------------------

def test6_dscaling():
    print("\n=== T6: D-scaling: vacuous for the certificate's Hermitian data ===")
    print("    (PROVEN: (a) for Hermitian A and diagonal D > 0,")
    print("     ||DAD^-1||_F^2 - ||A||_F^2 = sum_{i<j} |a_ij|^2[(d_i/d_j)^2+(d_j/d_i)^2-2] >= 0,")
    print("     so inf_D ||DAD^-1||_F = ||A||_F, attained at D ~ I.")
    print("     (b) DAD^-1 is similar to A, so its spectrum equals A's; sigma_bar(X) >= rho(X)")
    print("     for any X, hence sigma_bar(DAD^-1) >= sigma_bar(A), equality at D = I:")
    print("     inf_D sigma_bar(DAD^-1) = sigma_bar(A) exactly.  Both certificate norms are")
    print("     D-scaling-invariant on Hermitian data -- the mu-analysis D-scaling bound")
    print("     inf_D sigma_bar is only nontrivial for NON-normal matrices (asymmetric")
    print("     singular values); the Weil form bA is Hermitian, so it never applies.)")
    rng = np.random.default_rng(3)
    for (d, r, b) in ((20, 6, 2), (40, 12, 4)):
        P, Q, A = random_mixed(rng, d, r, b)
        hA = float((np.abs(np.linalg.eigvalsh(A)) ** 2).sum())
        obj, D = inf_D_Fnorm(A)
        print(f"  d={d} r={r} b={b}: ||A||_F^2={hA:.4f}  inf_D||DAD^-1||_F^2={obj:.4f} "
              f"(ratio {np.sqrt(obj/hA):.8f} -- F-norm cannot shrink; D ~ I)")
    # spectral norm checks (svd -- DAD^-1 is not Hermitian for D != I)
    A2 = np.array([[3.0, 1.0], [1.0, 2.0]])
    sbarA2 = np.linalg.svd(A2, compute_uv=False).max()
    ts = np.geomspace(1e-3, 1e3, 2001)
    sbars = np.array([np.linalg.svd(np.array([[3.0, t], [1.0 / t, 2.0]]),
                                    compute_uv=False).max() for t in ts])
    print(f"    spectral: [[3,1],[1,2]] sigma_bar(A)={sbarA2:.6f}  "
          f"sigma_bar(DAD^-1) over t=d1/d2: min={sbars.min():.6f} (>= sigma_bar(A), "
          f"equality at t=1), max={sbars.max():.6f}")
    P, Q, A = random_mixed(rng, 40, 12, 4)
    d0 = A.shape[0]
    sbarA = np.linalg.svd(A, compute_uv=False).max()
    worst = sbarA
    for _ in range(400):
        d = np.exp(rng.normal(0, 1.0, size=d0))
        S = (d[:, None] / d[None, :]) * A
        worst = max(worst, float(np.linalg.svd(S, compute_uv=False).max()))
    print(f"    random mixed d=40: sigma_bar(A)={sbarA:.6f}; sigma_bar(DAD^-1) over 400 "
          f"random D: max={worst:.6f} (never below sigma_bar(A))")
    print("    -> the LP-level D-scaling reading (C-MU1: row reweighting r(j/N), the")
    print("       256-law as the worst-case real perturbation, |E(1)| = 2.54e-6) is a")
    print("       MARGIN statement confirming attack-lpdual; the matrix-inequality")
    print("       D-scaling family contributes nothing to ||A||_F^2 on Hermitian data.")


# --------------------------------------------------------------------------
# TEST 7: Ostrowski-Schneider -- the finite content is the monotonicity
#         n+(A+Q) >= n+(A) (Q >= 0), already consumed as Lemma 3.1
# --------------------------------------------------------------------------

def test7_ostrowski():
    print("\n=== T7: Ostrowski-Schneider inertia transfer -- finite content check ===")
    print("    (INAPPLICABLE as a certificate input: the equality form n+(X)=n+(A) needs")
    print("     the Lyapunov equation A*X + XA = -Q with the zeros as the spectrum of A,")
    print("     i.e. the Hilbert-Polya operator -- RH itself (C-LY1).  The usable finite")
    print("     statement n+(A+Q) >= n+(A) for Q >= 0 is the monotonicity already used")
    print("     as Lemma 3.1 (pull-back, PROVEN in Lean).  Checked here for sanity.)")
    rng = np.random.default_rng(5)
    bad = 0
    for _ in range(2000):
        n = rng.integers(2, 30)
        A = herm(rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)))
        Q = herm(rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)))
        Q = Q @ Q  # PSD
        if nplus(np.linalg.eigvalsh(A + Q)) < nplus(np.linalg.eigvalsh(A)):
            bad += 1
    print(f"  2000 random (A Hermitian, Q >= 0): violations of n+(A+Q) >= n+(A): {bad}")


# --------------------------------------------------------------------------

def main():
    print("=== control-family sweep vs Lemma 3.2 (C-MU2) — "
          "uv run --with numpy python tools/control_mu_sweep.py ===")
    print(f"constants: int_psi2={INT_PSI2:.15f} c_HS={C_HS:.15f} "
          f"3/2-(1/sqrt2)cot={C_BOUND:.15f}")
    test1_sharp()
    test2_online()
    test3_pairs()
    test4_mixed()
    test5_gap_distribution()
    test6_dscaling()
    test7_ostrowski()
    print("\n=== bottom line: no control-family bound beats Lemma 3.2 on D ===")
    print("    (independent confirmation of the QI sweep negative; see "
          "research/notes/attack-mu-sweep.md)")


if __name__ == "__main__":
    main()

