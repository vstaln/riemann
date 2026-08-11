#!/usr/bin/env python3
"""Directed-MPFR enclosure of the 67.3192911473... bound."""
from __future__ import annotations

import ctypes
import ctypes.util
import os
from pathlib import Path

if os.name == "nt":
    _dll = os.environ.get("ZETA_MPFR_DLL", r"C:\Strawberry\c\bin\libmpfr-6.dll")
    if Path(_dll).is_file():
        ctypes.util.find_library = lambda _name: _dll

import generate_joint_kernel_table as base

MPFR_RNDU = base.MPFR_RNDU
MPFR_RNDD = base.MPFR_RNDD
Num = base.Num
Interval = base.Interval
add = base.add
subtract = base.subtract
multiply = base.multiply
divide = base.divide
divide_unsigned = base.divide_unsigned
interval_add = base.interval_add
interval_subtract = base.interval_subtract
interval_multiply = base.interval_multiply
interval_divide = base.interval_divide
base.lib.mpfr_cos.argtypes = [base.P, base.P, ctypes.c_int]


def cosine(value: Num, rounding: int) -> Num:
    out = Num()
    base.lib.mpfr_cos(out.pointer, value.pointer, rounding)
    return out


def interval_cos(value: Interval) -> Interval:
    mid = divide_unsigned(add(value.lower, value.upper, base.MPFR_RNDN), 2,
                           base.MPFR_RNDN)
    radius = base.maximum([
        subtract(mid, value.lower, MPFR_RNDU),
        subtract(value.upper, mid, MPFR_RNDU),
    ]).copy()
    return Interval(
        subtract(cosine(mid, MPFR_RNDD), radius, MPFR_RNDD),
        add(cosine(mid, MPFR_RNDU), radius, MPFR_RNDU),
    )


def exact(numerator: int, denominator: int = 1) -> Interval:
    n = Num.unsigned(numerator)
    return Interval(
        divide_unsigned(n, denominator, MPFR_RNDD),
        divide_unsigned(n, denominator, MPFR_RNDU),
    )


def neg(value: Interval) -> Interval:
    zero = Num.unsigned(0)
    return Interval(
        subtract(zero, value.upper, MPFR_RNDD),
        subtract(zero, value.lower, MPFR_RNDU),
    )


def scalar_mul(numerator: int, denominator: int, value: Interval) -> Interval:
    return interval_multiply(exact(numerator, denominator), value)


def main() -> None:
    alpha = exact(147, 100)
    half = scalar_mul(1, 2, alpha)
    alpha_sq = interval_multiply(alpha, alpha)
    i0 = interval_divide(
        scalar_mul(2, 1, base.sine_of_tiny_interval(half)), alpha
    )
    i2 = interval_add(
        exact(1, 2),
        interval_divide(base.sine_of_tiny_interval(alpha),
                        scalar_mul(2, 1, alpha)),
    )
    constant = interval_add(
        interval_divide(base.sine_of_tiny_interval(half), alpha),
        interval_divide(
            interval_multiply(exact(2), interval_cos(half)), alpha_sq,
        ),
    )
    j = interval_add(
        neg(interval_divide(scalar_mul(2, 1, i2), alpha_sq)),
        interval_multiply(constant, i0),
    )
    c = interval_divide(interval_multiply(i0, i0), interval_add(i2, j))
    h = interval_subtract(exact(2), interval_divide(exact(1), c))
    m = 183
    local = exact(577, 100000)
    a = scalar_mul(m - 6, 1, local)
    b = interval_add(
        interval_subtract(
            interval_multiply(
                exact(2),
                Interval(
                    base.square_root(
                        divide(
                            multiply(
                                Num.unsigned(m - 1),
                                a.lower,
                                MPFR_RNDD,
                            ),
                            Num.unsigned(m),
                            MPFR_RNDD,
                        ),
                        MPFR_RNDD,
                    ),
                    base.square_root(
                        divide(
                            multiply(
                                Num.unsigned(m - 1),
                                a.upper,
                                MPFR_RNDU,
                            ),
                            Num.unsigned(m),
                            MPFR_RNDU,
                        ),
                        MPFR_RNDU,
                    ),
                ),
            ),
            exact(1),
        ),
        scalar_mul(1, m, a),
    )
    pressure = exact(59, 19520)
    bound = interval_divide(interval_subtract(h, pressure),
                            interval_subtract(exact(1), scalar_mul(1, m, b)))
    print("mpfr_version=" + base.lib.mpfr_get_version().decode())
    print("precision_bits=256")
    for name, value in [("H", h), ("B", b), ("bound", bound)]:
        lo = value.lower.binary64(MPFR_RNDD)
        hi = value.upper.binary64(MPFR_RNDU)
        print(f"{name}_lower={lo:.17g}")
        print(f"{name}_upper={hi:.17g}")
        print(f"{name}_lower_hex={lo.hex()}")
        print(f"{name}_upper_hex={hi.hex()}")
    lo = bound.lower.binary64(MPFR_RNDD)
    print(f"certified_decimal_14={lo:.14f}")


if __name__ == "__main__":
    main()
