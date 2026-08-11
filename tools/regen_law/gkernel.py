#!/usr/bin/env python3
"""Re G(Delta) = Re sum_{j=1}^{N} e^{2pi i j Delta / N} — sign of off-grid corrections."""
import numpy as np

for N in (8, 256):
    print(f"N={N}:")
    for d in np.linspace(0.0, 1.0, 21):
        j = np.arange(1, N+1)
        G = np.sum(np.exp(2j*np.pi*j*d/N))
        print(f"  Delta={d:.2f}: Re G = {G.real:+.4f}, |G| = {abs(G):.4f}")
    print()
