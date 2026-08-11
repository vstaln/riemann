"""Verify attack-m29 key ratios: MV bound vs tolerance budget and vs diagonal D,
plus phase-free pair sums, at T=1e4, eps=0 and 0.05. Independent numpy sieve.
Normalizations follow attack-m29: a_n = Lambda(n)/sqrt(n); y_n = log n; L = log X;
D = (T/pi)*sum_{n<=X} a_n^2 g(y_n), g(y)=(L-y)_+;
B_MV = 4*(3pi/2)*pi*L * sum a_n^2/delta_n, delta_n = min gap in log n over the set;
S_full = sum_{n!=m} a_n a_m / |y_n - y_m|;
S_pair(delta) = sum_{n!=m} a_n a_m g(y_n) g(y_m) 1_{|y_n-y_m|<=delta};
budget = 0.0093*(1+eps)*N*L^2/4 with N = zeros in [T,2T].
"""
import numpy as np, math

def sieve_lambda(Nmax):
    lam = np.zeros(Nmax + 1)
    isp = np.ones(Nmax + 1, bool)
    isp[:2] = False
    for p in range(2, Nmax + 1):
        if isp[p]:
            pk = p
            while pk <= Nmax:
                lam[pk] = math.log(p)
                isp[pk::pk] = False
                pk *= p
    return lam

def m29(T, eps):
    X = T ** (1 + eps)
    Nmax = int(X)
    lam = sieve_lambda(Nmax)
    nz = np.nonzero(lam)[0]
    a = lam[nz] / np.sqrt(nz)
    y = np.log(nz)
    L = math.log(X)
    g = np.maximum(L - y, 0.0)
    # N(T,2T) ~ (T/2pi) log(T/2pi)
    N = (T / (2 * math.pi)) * math.log(T / (2 * math.pi))
    budget = 0.0093 * (1 + eps) * N * L * L / 4
    D = (T / math.pi) * np.sum(a * a * g)
    # delta_n: min separation in log n
    dy = np.diff(y)
    delta = np.minimum(np.concatenate(([dy[0]], dy)), np.concatenate((dy, [dy[-1]])))
    B_MV = 4 * (3 * math.pi / 2) * (math.pi * L) * np.sum(a * a / delta)
    # S_full: sum_{n!=m} a_n a_m / |y_n - y_m|  (pairwise; n ~ X/log X points — use vectorized)
    yy = y[:, None] - y[None, :]
    A = a[:, None] * a[None, :]
    np.fill_diagonal(yy, 1.0)
    S_full = np.sum(np.abs(A / yy))  # includes diagonal with a_n^2/1 — remove
    S_full -= np.sum(a * a)
    # S_pair(delta=1): a_n a_m g_n g_m 1_{|y_n - y_m| <= 1}
    gA = (a * g)[:, None] * (a * g)[None, :]
    S_pair1 = np.sum(np.where(np.abs(yy) <= 1.0, gA, 0.0)) - np.sum((a * g) ** 2)
    S_pair_1oL = np.sum(np.where(np.abs(yy) <= 1.0 / L, gA, 0.0)) - np.sum((a * g) ** 2)
    return dict(T=T, X=X, N=int(N), L=L, D=D, budget=budget, B_MV=B_MV, S_full=S_full,
                S_pair1=S_pair1, S_pair_1oL=S_pair_1oL,
                BMV_budget=B_MV / budget, BMV_D=B_MV / D, Sfull_D=S_full / D,
                Sp1_budget=S_pair1 / budget, Sp1_D=S_pair1 / D, SpoL_budget=S_pair_1oL / budget)

for T, eps in [(1e4, 0.0), (1e4, 0.05), (1e5, 0.0), (1e5, 0.05)]:
    r = m29(T, eps)
    print("T=%.0e eps=%.2f X=%.2e  L=%.2f  N=%d" % (T, eps, r['X'], r['L'], r['N']))
    print("   D=%.3e budget=%.3e  B_MV=%.3e  S_full=%.3e S_pair(1)=%.3e S_pair(1/L)=%.3e"
          % (r['D'], r['budget'], r['B_MV'], r['S_full'], r['S_pair1'], r['S_pair_1oL']))
    print("   B_MV/budget=%.1e   B_MV/D=%.1f   S_full/D=%.2f   S_pair(1)/budget=%.1f  S_pair(1)/D=%.3f  S_pair(1/L)/budget=%.2f"
          % (r['BMV_budget'], r['BMV_D'], r['Sfull_D'], r['Sp1_budget'], r['Sp1_D'], r['SpoL_budget']))
