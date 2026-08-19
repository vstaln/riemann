#!/usr/bin/env python3
"""Wave-25 next-move probe (clean rewrite): does the prime-truncated Weil form
W_{X,B} develop a negative eigenvalue when prime depth X < exp(B)?

Weil explicit formula (Bombieri 2000, even h):  RH  <=>  W(h) >= 0 for all h,
W(h) = -log(pi)*h(0)
       - sum_{p,m>=1} (log p)/p^{m/2} [h(m log p) + h(-m log p)]
       + (1/2pi) int phihat(t) arch(t) dt,  arch(t)=Re Psi(1/4+it/2).

Discretize on wavelet basis phi_j on [-B,B] (prime-log variable), truncate the
prime sum at p <= X, form W_{X,B}[jk] = W(phi_j phi_k).  Split interior/boundary,
compute Schur complement.  Question: is lambda_min(W_{X,B}) < 0 when log X < B
(the wave-25 g0-0 'boundary prime resonance' claim)?

Controls: DH weights (non-multiplicative) must behave DIFFERENTLY, else the
mechanism is not RH-separating.
"""
import math
import numpy as np
import mpmath as mp

mp.mp.dps = 30

def sieve_to(n):
    """primes <= n (n is an INTEGER bound)."""
    if n < 2:
        return []
    s = bytearray(b'\x01') * (n + 1)
    s[0] = s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i*i::i] = b'\x00' * (((n - i*i) // i) + 1)
    return [i for i in range(2, n + 1) if s[i]]

def arch(t):
    """Re Psi(1/4 + i t/2)."""
    return float(mp.digamma(mp.mpf('0.25') + mp.mpc(0, 1) * t / 2).real)

def phi(x, j, B, M):
    """Gabor packet on [-B,B]; last two are boundary packets at +-B."""
    if j == M - 2:
        return math.exp(-((x - B) ** 2) * 0.5)
    if j == M - 1:
        return math.exp(-((x + B) ** 2) * 0.5)
    s = -B + 2 * B * j / max(1, M - 3)
    return math.cos(math.pi * (j + 1) * (x - s) / (2 * B)) * math.exp(-((x - s) ** 2) * 0.5)

def W_matrix(B, M, X, dh=False):
    """W_{X,B}; if dh=True use Davenport-Heilbronn-style non-multiplicative weights
    c(n) (character-mod-5, |c(n)|<=1) instead of Lambda(n)/sqrt(n)."""
    W = np.zeros((M, M))
    P = sieve_to(int(math.floor(X)) + 1)
    for p in P:
        lp = math.log(p)
        w = math.log(p) / math.sqrt(p)
        pm = p
        m = 1
        while True:
            a = m * lp
            if a > B + 2:
                break
            for sgn in (1.0, -1.0):
                x = sgn * a
                col = np.array([phi(x, j, B, M) for j in range(M)])
                W += w * np.outer(col, col)
            pm *= p
            w /= math.sqrt(p)
            m += 1
            if m > 40:
                break
    if dh:
        # replace weights with character-mod-5 coefficients c(n) (|c|<=1, not
        # multiplicative) at the same points -> W_DH
        W = np.zeros((M, M))
        chi5 = {1: 1, 2: 1j, 3: -1j, 4: -1}
        for p in P:
            lp = math.log(p)
            for m in range(1, 10):
                a = m * lp
                if a > B + 2:
                    break
                w = 1.0 / math.sqrt(p ** m)  # c(p^m)/p^{m/2}, |c|<=1
                for sgn in (1.0, -1.0):
                    x = sgn * a
                    col = np.array([phi(x, j, B, M) for j in range(M)])
                    W += w * np.outer(col, col)
    # -log(pi) at 0
    col0 = np.array([phi(0.0, j, B, M) for j in range(M)])
    W -= math.log(math.pi) * np.outer(col0, col0)
    # Archimedean diagonal (Gamma term), mild: arch(0)/(2pi) per basis fn
    for j in range(M):
        W[j, j] += arch(0.0) / (2 * math.pi)
    return W

def schur(W, B, M, delta):
    int_, bnd = [], []
    for j in range(M):
        if j >= M - 2:
            bnd.append(j)
            continue
        s = -B + 2 * B * j / max(1, M - 3)
        (int_ if abs(s) <= B - delta else bnd).append(j)
    if not int_ or not bnd:
        return float(np.linalg.eigvalsh(W)[0]), None
    Wii = W[np.ix_(int_, int_)]
    Wbb = W[np.ix_(bnd, bnd)]
    Wib = W[np.ix_(int_, bnd)]
    S = Wbb - Wib.T @ np.linalg.inv(Wii) @ Wib
    return float(np.linalg.eigvalsh(W)[0]), float(np.linalg.eigvalsh(S)[0])

def main():
    print("Wave-25 next-move: prime-truncated Weil form negativity (clean probe)")
    print(f"{'B':>4} {'M':>3} {'logX':>5} {'lam_min W':>10} {'lam_min S':>10}  (control DH lam_min W)")
    for B in (1.2, 1.8, 2.5):
        for M in (8, 10):
            for logX in (B/2, B, B + 1.5):
                W = W_matrix(B, M, math.exp(logX))
                lamW, lamS = schur(W, B, M, 0.5)
                Wdh = W_matrix(B, M, math.exp(logX), dh=True)
                lamWdh, _ = schur(Wdh, B, M, 0.5)
                print(f"{B:>4.1f} {M:>3} {logX:>5.1f} {lamW:>+10.4f} {str(lamS if lamS is not None else 'n/a'):>10}  {lamWdh:>+10.4f}")

if __name__ == "__main__":
    main()
