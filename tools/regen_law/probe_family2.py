#!/usr/bin/env python3
import numpy as np
import sys; sys.path.insert(0, '/home/vstaln/riemann/tools/regen_law')
from common import gen_family_vec, spectra, dedupe

# check s_c distribution at N=64
for N in (32, 64):
    X, M, s_c = gen_family_vec(N, 2500, seed=1)
    print(f"N={N}: min s_c = {s_c.min()}, max = {s_c.max()}, unique = {np.unique(s_c)[:12]}")

# what does a single-jitter config's spectrum look like?
N = 64
xs = np.arange(N).astype(float); xs[5] += 0.25
ms = np.ones(N)
F = spectra(xs[None], ms[None], N)[0]
print("single jitter eps=0.25, N=64: f(1..10) =", np.round(F[:10], 4))
xs = np.arange(N).astype(float); xs[[5, 20]] += 0.25
F = spectra(xs[None], ms[None], N)[0]
print("two jitter eps=0.25:         f(1..10) =", np.round(F[:10], 4))
xs = np.arange(N).astype(float); xs[[5, 21]] += 0.25
F = spectra(xs[None], ms[None], N)[0]
print("two jitter diff positions:   f(1..10) =", np.round(F[:10], 4))
