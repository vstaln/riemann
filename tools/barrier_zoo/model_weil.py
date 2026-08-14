"""Model 4: fake Weil polynomial.

A Weil polynomial (function-field RH analogue) is a real self-reciprocal polynomial whose roots
all lie on the unit circle.  The EASY properties are:
  * real coefficients
  * self-reciprocal / palindromic  (functional equation:  x^d P(1/x) = P(x))
  * sign conditions P(1) > 0, P(-1) > 0 (and P(0) = leading coeff)
A FAKE Weil polynomial has all the easy properties but roots OFF the unit circle.  Any claim whose
mechanism uses ONLY the easy properties would "prove" the fake has roots on the circle -> proves
too much (RH-false model world).

Construction: P(x) = x^2 * Q(x + 1/x) with Q(y) = y^2 - 5y + 7.  Roots of P on |x|=1  <=>  roots
of Q in [-2,2] (x + 1/x = y with |x|=1 has y = 2 cos t in [-2,2]).  Q's roots (5 ± i sqrt3)/2 have
|y| = sqrt(7) > 2  ->  all four roots of P lie off the unit circle.
  P(x) = x^4 - 5x^3 + 9x^2 - 5x + 1 ;   P(1) = 1 > 0, P(-1) = 21 > 0, P(0) = 1.
Genuine contrast: x^4 + x^2 + 1  (Q = y^2 - 1, roots +-1 in [-2,2]) -> roots = 6th roots of unity,
all on the unit circle.

Run: uv run --quiet --with numpy python3 tools/barrier_zoo/model_weil.py
"""
import numpy as np

COEFFS_FAKE = [1.0, -5.0, 9.0, -5.0, 1.0]     # high -> low
COEFFS_GENUINE = [1.0, 0.0, 1.0, 0.0, 1.0]


def is_palindromic(c):
    return all(abs(c[i] - c[-1 - i]) < 1e-12 for i in range(len(c) // 2 + 1))


def properties(coeffs):
    c = np.array(coeffs, dtype=float)
    roots = np.roots(c)
    mod = np.abs(roots)
    return dict(
        palindromic=is_palindromic(coeffs),
        real_coeffs=bool(np.all(np.isreal(c))),
        P1=float(np.polyval(c, 1.0)),
        Pm1=float(np.polyval(c, -1.0)),
        P0=float(np.polyval(c, 0.0)),
        roots_off_circle=bool(np.all(np.abs(mod - 1.0) > 1e-8)),
        roots=roots, mod=mod,
    )


def verify():
    print("== model_weil: fake Weil polynomial (model 4) ==")
    for name, coeffs in [("FAKE", COEFFS_FAKE), ("GENUINE", COEFFS_GENUINE)]:
        p = properties(coeffs)
        print(f"[{name}] palindromic={p['palindromic']} real_coeffs={p['real_coeffs']} "
              f"P(1)={p['P1']:.6f} P(-1)={p['Pm1']:.6f} P(0)={p['P0']:.6f} "
              f"all_roots_off_unit_circle={p['roots_off_circle']}")
        print("    roots: " + ", ".join(f"{r.real:.6f}{r.imag:+.6f}i" for r in p['roots']))
        print("    |roots|: " + ", ".join(f"{m:.6f}" for m in p['mod']))
    fake = properties(COEFFS_FAKE)
    assert fake['palindromic'] and fake['real_coeffs'], "fake must be palindromic real"
    assert fake['P1'] > 0 and fake['Pm1'] > 0, "fake must satisfy the easy sign conditions"
    assert fake['roots_off_circle'], "fake Weil poly must have roots off the unit circle"
    print("VERDICT: FAKE Weil polynomial satisfies every EASY Weil property (palindromic/FE, real, "
          "positive at +-1, P(0)=1) yet ALL roots lie OFF the unit circle. RH FALSE in this model "
          "world (exact, algebraic). Any claim whose mechanism uses only the easy properties "
          "proves too much.")
    return {'status': 'PROVEN (exact)', 'off_circle_roots': fake['roots']}


if __name__ == '__main__':
    verify()
