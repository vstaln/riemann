#!/usr/bin/env python3
"""Evaluate the certified joint-window lower bound at high precision."""
import mpmath as mp

mp.mp.dps = 100
alpha = mp.mpf(147) / 100
I0 = 2 * mp.sin(alpha / 2) / alpha
I2 = mp.mpf(1) / 2 + mp.sin(alpha) / (2 * alpha)
constant = mp.sin(alpha / 2) / alpha + 2 * mp.cos(alpha / 2) / alpha**2
J = -2 * I2 / alpha**2 + constant * I0
c = I0**2 / (I2 + J)
H = 2 - 1 / c

m = 183
local = mp.mpf(577) / 100000
A = local * (m - 6)
block = 2 * mp.sqrt(mp.mpf(m - 1) * A / m) - 1 + A / m
pressure = mp.mpf(59) / 19520
bound = (H - pressure) / (1 - block / m)

anthropic = mp.mpf(3) / 2 - (1 / mp.sqrt(2)) / mp.tan(1 / mp.sqrt(2))
repo = (mp.mpf(1_345_000) * anthropic - 2680) / mp.mpf(1_340_003)
previous = mp.mpf("0.6731017847214250187272737655028151379")

for name, value in [
    ("alpha", alpha),
    ("I0", I0),
    ("I2", I2),
    ("J", J),
    ("c_window", c),
    ("H_window", H),
    ("local_constant", local),
    ("block_size", mp.mpf(m)),
    ("block_energy", A),
    ("block_defect", block),
    ("pressure", pressure),
    ("new_bound", bound),
    ("new_percentage", 100 * bound),
    ("gain_over_repo", bound - repo),
    ("gain_over_previous", bound - previous),
]:
    print(f"{name}={mp.nstr(value, 90)}")
