"""tools/kernel_family.py — exact-rational KernelSpec -> KernelArb-compatible kernels.

Port of the trmdy zeta-simple-zeros window/kernel design:
  research/external-results/trmdy-zeta-simple-zeros-673137/
    src/zeta_ext/kernel.py  (KernelSpec, _omegas, kernel_k0)
    src/zeta_ext/design.py  (WINDOW_NUMERATORS/DENOMINATOR, KERNEL)
into our pipeline's KernelArb (tools/verify_coboundary_floor.py). Ours uses the
same normalization w(x) = (K(x)/K(0))^2, so the port only generalizes our
single-term cosine_kernel to arbitrary exact-rational multi-term specs.
"""

from flint import arb, fmpq

from verify_coboundary_floor import KernelArb


def omegas_from_spec(omega_pi_multiples=(), has_sqrt2_term=False, zero_shift=0.0):
    """trmdy convention: optional leading sqrt(2) term, then omega_j = mult_j*pi.

    zero_shift: optional phase added to every omega. trmdy's design uses NO shift
    (sinc evals are exact at integers); default 0.0 reproduces it exactly.
    """
    oms = []
    if has_sqrt2_term:
        oms.append(arb(2).sqrt() + arb(zero_shift))
    pi = arb.pi()
    for mult in omega_pi_multiples:
        oms.append(mult * pi + arb(zero_shift))
    return oms


def kernel_from_spec(coeffs, omega_pi_multiples=(), has_sqrt2_term=False, zero_shift=0.0):
    """Build OUR KernelArb from a trmdy-style exact-rational spec.

    coeffs: sequence of exact fmpq (rational) coeffs, ordered left-to-right with the
    omegas (sqrt2 term first when has_sqrt2_term, then 2pi,4pi,...).
    """
    c = [arb(_) if isinstance(_, fmpq) else arb(fmpq(*_)) for _ in coeffs]
    oms = omegas_from_spec(omega_pi_multiples, has_sqrt2_term, zero_shift)
    return KernelArb(c, oms)


def trmdy_kernel(zero_shift=0.0):
    """TrMdy certified window KERNEL (design.py): 7 exact-rational coeffs /1e9,
    omegas = (sqrt2, 2pi, 4pi, ..., 12pi). Default zero_shift=0 reproduces their design."""
    WINDOW_DENOMINATOR = 10**9
    WINDOW_NUMERATORS = (
        1_000_000_000, 3_322_500, -7_609_135, 1_190_194,
        -731_476, -1_680_572, 1_141_360,
    )
    coeffs = tuple(fmpq(n, WINDOW_DENOMINATOR) for n in WINDOW_NUMERATORS)
    return kernel_from_spec(coeffs, omega_pi_multiples=(2, 4, 6, 8, 10, 12),
                            has_sqrt2_term=True, zero_shift=zero_shift)


def _demo():
    k = trmdy_kernel()
    # k0 = K(0) = sum c_j * 2 sin(w_j/2)/w_j ; w(0) = (K(0)/K(0))^2 == 1
    assert float(k.w_point(0.0)) == 1.0
    assert len(k.coeffs) == 7 and len(k.omegas) == 7
    print(f"trmdy_kernel: k0={float(k.k0):.6f}, w(0)={float(k.w_point(0.0))}")
    print("kernel_family demo OK")


if __name__ == "__main__":
    _demo()
