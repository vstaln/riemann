#!/usr/bin/env python3
"""First-prime Weil positivity probe.

Belief this changes: whether the archimedean spectral gap of Q_W at the
Yoshida threshold a = (log 2)/2 is large enough that the prime-2 term
(the first arithmetic correction) cannot drive λ_a negative before the
prime-3 threshold a = (log 3)/2.

Weil T[G] is Bombieri 2000, (12.3) / §12 (position-space explicit formula).
Q(v) := T[v * ṽ],  supp(v) ⊂ [-a,a],  Rayleigh r(v) = Q(v)/||v||².
Primes enter iff 2a ≥ log n, i.e. a ≥ (log n)/2.

# ponytail: M=12 even Dirichlet modes, N=801 grid; raise M if the lowest
# mode is not stable under M=8 vs M=12.
"""
from __future__ import annotations

import math

import numpy as np

GAMMA = 0.5772156649015328606  # Euler-Mascheroni
LOG4PI_GAMMA = math.log(4 * math.pi) + GAMMA
A2 = 0.5 * math.log(2.0)  # Yoshida / Suzuki threshold
A3 = 0.5 * math.log(3.0)


def von_mangoldt_upto(x: float) -> list[tuple[int, float]]:
    """(n, Λ(n)) for n ≤ x, n = p^k."""
    if x < 2:
        return []
    N = int(x)
    is_prime = [True] * (N + 1)
    is_prime[0] = is_prime[1] = False
    primes = []
    for p in range(2, N + 1):
        if not is_prime[p]:
            continue
        primes.append(p)
        for m in range(p * p, N + 1, p):
            is_prime[m] = False
    out = []
    for p in primes:
        pk, logp = p, math.log(p)
        while pk <= N:
            out.append((pk, logp))
            if pk > N // p:
                break
            pk *= p
    return sorted(out)


def even_basis(a: float, M: int, xs: np.ndarray) -> np.ndarray:
    """φ_k(x) = cos((k+1/2) π x / a) on [-a,a], 0 at ±a. Shape (M, len(xs))."""
    k = np.arange(M)[:, None]
    return np.cos((k + 0.5) * np.pi * xs[None, :] / a)


def autocorrelation(v: np.ndarray, dx: float) -> tuple[np.ndarray, np.ndarray]:
    """G = v * ṽ on lag grid τ ∈ [-2a, 2a] (len 2N-1)."""
    g = np.correlate(v, v, mode="full") * dx
    n = len(v)
    taus = (np.arange(2 * n - 1) - (n - 1)) * dx
    return taus, g


def T_parts(taus: np.ndarray, G: np.ndarray, a_v: float, primes: bool) -> dict:
    """Bombieri T[G] split into summands. Keys: cosh, const, arch_int, primes, T."""
    dx = float(taus[1] - taus[0])
    A = 2.0 * a_v  # support radius of G
    # interpolate G as even function of x ≥ 0
    def G_at(x: np.ndarray) -> np.ndarray:
        return np.interp(np.abs(x), taus, G, left=0.0, right=0.0)

    G0 = float(np.interp(0.0, taus, G))

    # ∫_{-A}^{A} 2 cosh(x/2) G(x) dx  (G compactly supported)
    xs = taus[(taus >= -A - dx) & (taus <= A + dx)]
    arch_cosh = float(np.trapezoid(2.0 * np.cosh(xs / 2.0) * G_at(xs), xs))

    # constant term
    const = -LOG4PI_GAMMA * G0

    # ∫_0^∞ [e^{x/2}(G(x)+G(-x)) - 2 G(0)] / (e^x - e^{-x}) dx
    # split [0, A] numerical + [A, ∞) closed form.
    n_int = max(400, int(A / dx) * 2)
    x_pos = np.linspace(0.0, A, n_int)
    Gx = G_at(x_pos)
    num = np.exp(x_pos / 2.0) * (Gx + Gx) - 2.0 * G0
    den = np.exp(x_pos) - np.exp(-x_pos)
    integ = np.empty_like(x_pos)
    integ[0] = G0 / 2.0  # even G: integrand → G(0)/2
    integ[1:] = num[1:] / den[1:]
    I_finite = float(np.trapezoid(integ, x_pos))
    # x>A ⇒ G=0, integrand = -G(0)/sinh x, ∫_A^∞ dx/sinh x = -log tanh(A/2)
    tanh_half = math.tanh(A / 2.0)
    I_tail = G0 * math.log(tanh_half)
    arch_int = -(I_finite + I_tail)

    prime_term = 0.0
    if primes:
        xmax = math.exp(A) + 1e-12
        for n, Lam in von_mangoldt_upto(xmax):
            lg = math.log(n)
            if lg > A + 1e-14:
                continue
            Gn = float(np.interp(lg, taus, G, left=0.0, right=0.0))
            # G even: G(log n)+G(-log n) = 2 G(log n)
            prime_term += -(Lam / math.sqrt(n)) * 2.0 * Gn

    return {
        "cosh": arch_cosh,
        "const": const,
        "arch_int": arch_int,
        "primes": prime_term,
        "T": arch_cosh + const + arch_int + prime_term,
    }


def T_of_G(taus: np.ndarray, G: np.ndarray, a_v: float, primes: bool) -> float:
    """Bombieri T[G], G sampled on `taus` (even spacing). supp G ⊂ [-2 a_v, 2 a_v]."""
    return T_parts(taus, G, a_v, primes)["T"]


def rayleigh_matrix(a: float, M: int, N: int, primes: bool) -> tuple[np.ndarray, np.ndarray]:
    """H, B with Q(c) = c^T H c, ||v||² = c^T B c, v = Σ c_k φ_k."""
    xs = np.linspace(-a, a, N)
    dx = float(xs[1] - xs[0])
    Phi = even_basis(a, M, xs)  # (M, N)
    # mass matrix B_ij = ⟨φ_i, φ_j⟩
    B = (Phi @ Phi.T) * dx
    # Q via polarization
    H = np.zeros((M, M))
    cache = {}

    def Q_of_c(c: np.ndarray) -> float:
        key = tuple(np.round(c, 12))
        if key in cache:
            return cache[key]
        v = c @ Phi
        taus, G = autocorrelation(v, dx)
        val = T_of_G(taus, G, a, primes)
        cache[key] = val
        return val

    for i in range(M):
        ei = np.zeros(M)
        ei[i] = 1.0
        H[i, i] = Q_of_c(ei)
    for i in range(M):
        for j in range(i + 1, M):
            ei = np.zeros(M)
            ej = np.zeros(M)
            ei[i] = 1.0
            ej[j] = 1.0
            H[i, j] = H[j, i] = 0.5 * (Q_of_c(ei + ej) - H[i, i] - H[j, j])
    return H, B


def lowest_rayleigh(a: float, M: int, N: int, primes: bool) -> float:
    H, B = rayleigh_matrix(a, M, N, primes)
    # generalized: H c = λ B c; symmetrize H against roundoff
    H = 0.5 * (H + H.T)
    B = 0.5 * (B + B.T)
    evals = np.linalg.eigvalsh(np.linalg.solve(B, H))
    return float(np.min(evals.real))


def overlap_bound_prime2(a: float, v: np.ndarray, xs: np.ndarray) -> float:
    """|G(log 2)| ≤ ||v||_{I1} ||v||_{I2} on the length-(2a-log 2) overlap."""
    dx = float(xs[1] - xs[0])
    lag = math.log(2.0)
    # overlap of [-a,a] and [-a,a]+lag is [ -a+lag, a ]
    left, right = -a + lag, a
    if right <= left:
        return 0.0
    mask1 = (xs >= left) & (xs <= right)
    mask2 = (xs >= left - lag) & (xs <= right - lag)
    n1 = math.sqrt(float(np.sum(v[mask1] ** 2) * dx))
    n2 = math.sqrt(float(np.sum(v[mask2] ** 2) * dx))
    return n1 * n2


def self_checks() -> None:
    # Linearity of T in G: T[2G]=2 T[G]
    a = 0.20
    xs = np.linspace(-a, a, 401)
    dx = float(xs[1] - xs[0])
    v = np.cos(0.5 * np.pi * xs / a)
    taus, G = autocorrelation(v, dx)
    t1 = T_of_G(taus, G, a, primes=False)
    t2 = T_of_G(taus, 2 * G, a, primes=False)
    assert abs(t2 - 2 * t1) / max(1.0, abs(t1)) < 1e-6, (t1, t2)
    # G(0) = ||v||²
    g0 = float(np.interp(0.0, taus, G))
    nrm = float(np.sum(v**2) * dx)
    assert abs(g0 - nrm) / nrm < 1e-3, (g0, nrm)
    # below first-prime threshold, primes do not change T
    t_p = T_of_G(taus, G, a, primes=True)
    assert abs(t_p - t1) < 1e-9 * (1 + abs(t1)), (t1, t_p)
    # small-a positivity of the lowest mode
    lam = lowest_rayleigh(0.15, M=4, N=401, primes=False)
    assert lam > 0, lam


def main() -> None:
    self_checks()
    M, N = 8, 601
    print(f"thresholds  a2={A2:.12f}  a3={A3:.12f}  gap={A3-A2:.12f}")
    print(f"LOG4PI+γ = {LOG4PI_GAMMA:.12f}")
    print(f"grid M={M} N={N}")

    # Stability: M=6 vs M=8 at a slightly below a2
    a_lo = A2 * 0.98
    lam6 = lowest_rayleigh(a_lo, M=6, N=N, primes=False)
    lam8 = lowest_rayleigh(a_lo, M=8, N=N, primes=False)
    print(f"stability a={a_lo:.6f}  M6={lam6:.8f}  M8={lam8:.8f}  rel={abs(lam8-lam6)/abs(lam8):.3e}")

    points = [
        ("below_a2", A2 * 0.95, False),
        ("below_a2_primes_on", A2 * 0.95, True),
        ("at_a2", A2, True),
        ("mid_first_prime", 0.5 * (A2 + A3), True),
        ("just_below_a3", A3 * 0.98, True),
        ("at_a3", A3, True),
        ("past_a3", A3 * 1.05, True),
        ("a=0.20", 0.20, False),
        ("a=0.10", 0.10, False),
    ]
    print("label a primes lambda")
    results = {}
    for label, a, pr in points:
        lam = lowest_rayleigh(a, M=M, N=N, primes=pr)
        results[label] = (a, pr, lam)
        print(f"{label:20s} {a:.10f} {int(pr)} {lam:.12f}")

    # Overlap vs actual G(log 2) for the ground mode at mid-window
    a = 0.5 * (A2 + A3)
    xs = np.linspace(-a, a, N)
    dx = float(xs[1] - xs[0])
    Phi = even_basis(a, M, xs)
    H, B = rayleigh_matrix(a, M, N, primes=True)
    evals, evecs = np.linalg.eig(np.linalg.solve(B, H))
    k = int(np.argmin(evals.real))
    c = evecs[:, k].real
    c /= math.sqrt(float(c @ B @ c))
    v = c @ Phi
    taus, G = autocorrelation(v, dx)
    Glog2 = float(np.interp(math.log(2.0), taus, G))
    ov = overlap_bound_prime2(a, v, xs)
    G0 = float(np.interp(0.0, taus, G))
    prime_coeff = math.log(2.0) / math.sqrt(2.0)  # Λ(2)/√2 ; even ⇒ ×2 in T
    print(f"mid-window ground: G0={G0:.8f} G(log2)={Glog2:.8e} overlap_bound={ov:.8e}")
    print(f"  |G(log2)|/G0={abs(Glog2)/G0:.8e}  overlap/G0={ov/G0:.8e}")
    print(f"  prime2_term_if_even={-2*prime_coeff*Glog2:.8e}  (vs Q ~ lambda*G0)")

    # Crude |G|≤G(0) bound: would the first prime kill positivity?
    crude = 2 * prime_coeff  # max |prime term| / G0
    print(f"crude |prime2|/G0 ≤ {crude:.8f}")
    # Component breakdown + M-convergence (Ritz is an UPPER bound on λ_true)
    print("components (ground even mode)")
    for label, a, pr in [
        ("a=0.20", 0.20, False),
        ("at_a2", A2, True),
        ("mid_first_prime", 0.5 * (A2 + A3), True),
        ("at_a3", A3, True),
    ]:
        xs = np.linspace(-a, a, N)
        dx = float(xs[1] - xs[0])
        Phi = even_basis(a, M, xs)
        H, B = rayleigh_matrix(a, M, N, pr)
        H = 0.5 * (H + H.T)
        B = 0.5 * (B + B.T)
        evals, evecs = np.linalg.eig(np.linalg.solve(B, H))
        k = int(np.argmin(evals.real))
        c = evecs[:, k].real
        c /= math.sqrt(abs(float(c @ B @ c)))
        v = c @ Phi
        taus, G = autocorrelation(v, dx)
        parts = T_parts(taus, G, a, pr)
        print(
            f"  {label:18s} T={parts['T']:+.6e} cosh={parts['cosh']:+.6e} "
            f"const={parts['const']:+.6e} arch_int={parts['arch_int']:+.6e} "
            f"primes={parts['primes']:+.6e}"
        )

    print("M-convergence (upper bounds) a=mid, primes on")
    a = 0.5 * (A2 + A3)
    for Mm in (4, 6, 8):
        lam = lowest_rayleigh(a, M=Mm, N=N, primes=True)
        print(f"  M={Mm}  lambda_Ritz={lam:.8e}")

    print("N-convergence M=6 a=mid")
    for Nn in (301, 601):
        lam = lowest_rayleigh(a, M=6, N=Nn, primes=True)
        print(f"  N={Nn}  lambda_Ritz={lam:.8e}")
    # fail loudly if the method-relevant claims are numerically false
    assert results["a=0.10"][2] > 0
    assert results["below_a2"][2] > 0
    assert abs(results["below_a2"][2] - results["below_a2_primes_on"][2]) < 1e-6


if __name__ == "__main__":
    main()
