#!/usr/bin/env python3
"""
Li's criterion probe (v3): formal power series, no zeta(1) evaluation.

zeta(s) = 1/u + sum_{k>=0} (-1)^k gamma_k / k! * u^k,  u = s-1,  gamma_k = Stieltjes consts.
=>  F(s) = u * zeta(s) = 1 + sum_{m>=1} a_m u^m,  a_m = (-1)^{m-1} gamma_{m-1} / (m-1)!

log F(s) = sum b_m u^m via the series-log recurrence:
  b_m = a_m - (1/m) sum_{k=1}^{m-1} k * b_k * a_{m-k}

Then log xi(s) = log F(s) + log(s/2) - (s/2) log pi + log Gamma(s/2),
and Bombieri-Lagarias: log xi(1/(1-x)) = sum_{n>=1} lambda_n x^n / n.

With u = x/(1-x): log xi(1+u) = sum c_m u^m, substitute u = x + x^2 + ...,
collect coefficients of x^n => lam[n] = lambda_n / n, then lambda_n = n * lam[n].

Honesty: NUMERICAL probe (CHECKED NUMERICALLY), not a proof.
"""
import mpmath as mp
import sys

mp.mp.dps = int(sys.argv[1]) if len(sys.argv) > 1 else 60
N = int(sys.argv[2]) if len(sys.argv) > 2 else 150

def series_log(a, M):
    """a[1..M] = coeffs of A(u) (a_0 = 0). Return b[0..M] = coeffs of log(1+A)."""
    b = [mp.mpf(0)] * (M + 1)
    for m in range(1, M + 1):
        s = mp.mpf(0)
        for k in range(1, m):
            s += k * b[k] * a[m - k]
        b[m] = a[m] - s / m
    return b

def main():
    print(f"Li criterion probe v3: N={N}, dps={mp.mp.dps}")
    M = N + 2
    # a_m = (-1)^{m-1} gamma_{m-1} / (m-1)!  for m>=1
    a = [mp.mpf(0)] * (M + 1)
    for m in range(1, M + 1):
        g = mp.stieltjes(m - 1)
        a[m] = ((-1) ** (m - 1)) * g / mp.fac(m - 1)
    b = series_log(a, M)   # log F(s) = log[(s-1) zeta(s)]
    # h(s) = log(s/2) - (s/2) log pi + log Gamma(s/2),  u = s-1. Closed-form coeffs:
    #   log(s/2)        : m=0 -> -log2 ; m>=1 -> (-1)^{m-1}/m
    #   -(s/2) log pi   : m=0 -> -L/2 ; m=1 -> -L/2 ; else 0   (L = log pi)
    #   log Gamma(s/2)  : m=0 -> (1/2)log pi ; m>=1 -> polygamma(m-1, 1/2)/(m! * 2^m)
    L = mp.log(mp.pi)
    c = [mp.mpf(0)] * (M + 1)
    for m in range(M + 1):
        hm = mp.mpf(0)
        if m == 0:
            hm = -mp.log(2) - L/2 + mp.log(mp.pi)/2
        else:
            hm = ((-1)**(m-1)) / m          # log(s/2)
            if m == 1:
                hm -= L/2                    # -(s/2) log pi
            hm += mp.polygamma(m-1, mp.mpf(0.5)) / (mp.fac(m) * (2**m))  # log Gamma(s/2)
        c[m] = b[m] + hm
    # B-L substitution u = x/(1-x)
    lam = [mp.mpf(0)] * (N + 1)
    for k in range(1, M + 1):
        ck = c[k]
        if ck == 0:
            continue
        for n in range(k, N + 1):
            m = n - k
            lam[n] += ck * mp.binomial(k + m - 1, m)
    lam_n = [n * lam[n] for n in range(N + 1)]
    print("lambda_1..lambda_12:")
    for n in range(1, 13):
        print(f"  lambda_{n:3d} = {mp.nstr(lam_n[n], 18)}")
    neg = [n for n in range(1, N + 1) if lam_n[n] < 0]
    print(f"first negative n: {neg[:6] if neg else 'NONE (all >= 0 in 1..%d)' % N}")
    print(f"total negative in 1..{N}: {len(neg)}")
    # known exact values for sanity: lambda_1 = gamma_0 + 1 - log(2)/2 - ... 
    # (Bombieri-Lagarias: lambda_1 = gamma_0 - 1 + 1 - log(4 pi)/2 ... )
    # We cross-check lambda_1 against the closed form lambda_1 = 1 + gamma/2 - (1/2) log(4 pi)
    lam1_closed = mp.mpf(1) + mp.euler / 2 - mp.log(4 * mp.pi) / 2
    print(f"cross-check lambda_1: computed {mp.nstr(lam_n[1], 20)} vs closed {mp.nstr(lam1_closed, 20)}")
    # Hankel inertia via mpmath (avoid numpy dep here)
    size = 40
    H = mp.matrix(size, size)
    for i in range(size):
        for j in range(size):
            H[i, j] = lam_n[i + j + 1]
    try:
        ev = mp.eig(H, 'symmetric')  # may be slow
        evs = sorted([mp.re(x) for x in ev], reverse=True)
        nneg = sum(1 for x in evs if x < 0)
        print(f"Hankel(size={size}) inertia: min ev = {mp.nstr(evs[-1], 6)}, #neg = {nneg}")
    except Exception as e:
        print(f"Hankel eigen skipped: {e}")
    with open("/tmp/lambda_n.txt", "w") as fh:
        for n in range(1, N + 1):
            fh.write(f"{n} {mp.nstr(lam_n[n], 30)}\n")
    print("wrote /tmp/lambda_n.txt")

if __name__ == "__main__":
    main()
