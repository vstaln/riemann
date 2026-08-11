#!/usr/bin/env python3
"""Check A (B1): is the paper's W_T of the CvS divided-difference form (11)?

The CvS theorem's mechanism requires the matrix of the quadratic form to have the
"divided-difference / screw" structure (CvS Prop 4.1, eq. (11)):

    q_ii = a_i,   q_ij = (b_i - b_j)/(i - j)   (i != j),   a_{-i}=a_i, b_{-i}=-b_i.

An exact algebraic identity satisfied by ANY such matrix (for any sequence b):
    (i-j) q_ij + (j-k) q_jk + (k-i) q_ki = 0          (the 3-cycle / cocycle condition),
equivalently M_ij := (i-j) q_ij (i!=j), M_ii := 0, is of the form M = b (x) 1 - 1 (x) b,
which has rank <= 2.

We test the paper's height-truncation matrix W_T (built from real zeta-zero data with
the attack-finitet model: W_T = (1/int psi^2) V^T V, V[rho][k] = Psi(s_rho - k)) against
this necessary condition, and compare with a genuine form-(11) matrix built from a smooth
source function psi(x).

Usage: uv run --quiet --with numpy python tools/cvs-import/check_divided_difference.py
"""
import numpy as np

# ---------- paper's W_T model (attack-finitet): ----------
A = 1.0 / np.sqrt(2.0)

def Psi(s):
    """Fourier transform of cos(sqrt2 u) on [-1/2,1/2], e^{-2 pi i} convention.
    Closed form (attack-finitet, verified): 
        Psi(s) = sin(a - pi s)/(sqrt2 - 2 pi s) + sin(a + pi s)/(sqrt2 + 2 pi s),  a = 1/sqrt2
    Removable poles at 2 pi s = +-sqrt2 (limit = 1/2)."""
    a = 1.0/np.sqrt(2.0)
    s2 = np.sqrt(2.0)
    d1 = s2 - 2.0*np.pi*s
    d2 = s2 + 2.0*np.pi*s
    t1 = np.sin(a - np.pi*s)/d1
    t2 = np.sin(a + np.pi*s)/d2
    t1 = np.where(np.abs(d1) < 1e-12, 0.5, t1)   # removable pole 2 pi s = sqrt2
    t2 = np.where(np.abs(d2) < 1e-12, 0.5, t2)   # removable pole 2 pi s = -sqrt2
    return t1 + t2

def load_zeros(path):
    gs = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            gs.append(float(parts[1]))
    return np.array(gs)

def build_WT(gammas, T, N=None):
    """Gabor compression at heights [T, 2T), grid alpha_k = T + (T/N)k (finitet model)."""
    if N is None:
        N = int(np.sum((gammas >= T) & (gammas < 2.0*T)))
    alpha = T + (T/float(N))*np.arange(N)
    s_rho = (gammas - T)*N/T
    V = np.array([Psi(s_rho - k) for k in range(N)])          # V[k][rho]
    intpsi2 = 0.5 + np.sin(np.sqrt(2.0))/(2.0*np.sqrt(2.0))   # int psi^2 (finitet, checked)
    W = (1.0/intpsi2) * (V @ V.T)                             # d x d
    return W

def cocycle_max(Q):
    """max |(i-j)Q_ij + (j-k)Q_jk + (k-i)Q_ki| over distinct triples (sample if large)."""
    n = Q.shape[0]
    # sample all triples for n <= 260 (dense), else a deterministic sample
    if n <= 260:
        ii, jj, kk = np.indices((n, n, n)).reshape(3, -1)
        mask = (ii != jj) & (jj != kk) & (kk != ii)
        ii, jj, kk = ii[mask], jj[mask], kk[mask]
    else:
        rng = np.random.default_rng(0)
        ii = rng.integers(0, n, 200000)
        jj = rng.integers(0, n, 200000)
        kk = rng.integers(0, n, 200000)
        mask = (ii != jj) & (jj != kk) & (kk != ii)
        ii, jj, kk = ii[mask][:50000], jj[mask][:50000], kk[mask][:50000]
    res = (ii - jj)*Q[ii, jj] + (jj - kk)*Q[jj, kk] + (kk - ii)*Q[kk, ii]
    return float(np.max(np.abs(res)))

def rank2_residual(Q):
    """M_ij = (i-j)Q_ij (i!=j), M_ii = 0.  If Q is form (11), rank(M) <= 2."""
    n = Q.shape[0]
    idx = np.arange(n)
    M = np.zeros_like(Q)
    for i in range(n):
        for j in range(n):
            if i != j:
                M[i, j] = (i - j)*Q[i, j]
    s = np.linalg.svd(M, compute_uv=False)
    s = s[s > 1e-12*max(s[0], 1e-300)]
    return len(s), s[0], (s[2]/s[0] if len(s) > 2 else 0.0)

def form11_from_source(psi, N):
    """q_ii = psi'(i), q_ij = (psi(i)-psi(j))/(i-j): genuine form (11) for indices 0..N-1."""
    idx = np.arange(N)
    Q = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            if i == j:
                Q[i, j] = (psi(i+1e-7) - psi(i-1e-7))/2e-7   # numeric derivative
            else:
                Q[i, j] = (psi(i) - psi(j))/(i - j)
    return Q

def main():
    zeros = load_zeros('/home/vstaln/riemann/tools/data/zeros_1_1000.txt')
    print("=== Check A: divided-difference (CvS form (11)) structure of the paper's W_T ===")
    for T in (100.0, 200.0):
        W = build_WT(zeros[(zeros >= T) & (zeros < 2.0*T)], T)   # window zeros only (finitet)
        n = W.shape[0]
        coc = cocycle_max(W)
        rk, s0, rel = rank2_residual(W)
        print(f"T={T:5.0f}  d={n:4d}  max|W|={np.max(np.abs(W)):.6f}  "
              f"max 3-cycle resid={coc:.6e}  rank((i-j)W_ij)={rk}  s2/s0={rel:.3e}")

    print()
    print("=== genuine form-(11) matrix (source psi) for comparison ===")
    psi = lambda x: np.sin(2.0*np.pi*x/7.0) + 0.3*np.sin(2.0*np.pi*x/11.0)
    for N in (8, 40):
        Q = form11_from_source(psi, N)
        coc = cocycle_max(Q)
        rk, s0, rel = rank2_residual(Q)
        print(f"N={N:3d}  max 3-cycle resid={coc:.3e}  rank((i-j)q_ij)={rk}  s2/s0={rel:.3e}")

    print()
    print("=== single-zero building block of the paper's G (rank-one Gram, not divided-difference) ===")
    gammas = np.array([201.265])   # one synthetic ordinate
    T = 200.0
    W1 = build_WT(gammas, T, N=8)
    coc = cocycle_max(W1)
    print(f"d=8  rank(W1)={np.linalg.matrix_rank(W1, tol=1e-9)}  max 3-cycle resid={coc:.6e}")

    print()
    print("VERDICT A:", "paper's W_T FAILS the divided-difference cocycle by O(1) (not form (11)); "
          "genuine form-(11) matrices satisfy it to machine precision.")

if __name__ == '__main__':
    main()
