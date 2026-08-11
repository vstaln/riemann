"""V13 diagnostic: the fluctuation statistic S(t) = N(t) - smooth mean, real zeros vs periodic law.

Question this grounds: is there an unconditional fluctuation statistic that (empirically at least)
DISTINGUISHES the real zeros (Selberg scale sqrt((1/2 pi^2) log log t)) from a fixed periodic
configuration (the 256-law analogue: S identically O(1), in fact 0 for an exact periodic model)?

For the real zeros we measure S(t) = N(t) - [(t/2pi)log(t/2pi) - t/2pi + 7/8]  (Titchmarsh 9.4).
The Selberg 1946 prediction: E[S(t)^2] ~ (1/2 pi^2) log log t  (Goldston notes Sec 10, Thm 8, k=1).

A fixed periodic configuration of the same density has S(t) = O(1) for all t, by construction
(a periodic count has bounded deviation from its mean), so its RMS over any window is O(1/T^{1/2}) -> 0.

Run:  cd /home/vstaln/riemann/research/notes/attack-selberg-clt && timeout 120 uv run --quiet --with numpy python s_probe.py
Data: tools/data/zeros_computed_10000.txt (gamma_1..gamma_10000, gamma in [14.135, 9879.037])
"""
import math
import numpy as np

ZEROS = "/home/vstaln/riemann/tools/data/zeros_computed_10000.txt"
gammas = []
with open(ZEROS) as f:
    for line in f:
        parts = line.split()
        if parts:
            gammas.append(float(parts[-1]))
gammas = np.array(sorted(gammas))
N = len(gammas)
print(f"zeros loaded: {N}, gamma_1 = {gammas[0]:.3f}, gamma_N = {gammas[-1]:.3f}")

def mean_count(t):
    # (t/2pi) log(t/2pi) - t/2pi + 7/8  : smooth expected count (Titchmarsh)
    return (t / (2 * math.pi)) * math.log(t / (2 * math.pi)) - t / (2 * math.pi) + 7.0 / 8.0

def S_at(t):
    # S(t) = N(t) - mean(t)  (up to O(1/t))
    n = int(np.searchsorted(gammas, t, side="right"))
    return n - mean_count(t)

# Heights spread over the available range [2000, 9000]
ts = [2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0, 8000.0, 9000.0]
print("\n t        S(t)      sqrt((1/2pi^2) log log t)")
for t in ts:
    s = S_at(t)
    pred = math.sqrt((1.0 / (2 * math.pi ** 2)) * math.log(math.log(t)))
    print(f"{t:8.0f}  {s:8.3f}    {pred:8.3f}")

# RMS of S over a fine grid t in [2000, 9000]
grid = np.linspace(2000.0, 9000.0, 1401)
Ss = np.array([S_at(t) for t in grid])
rms = float(np.sqrt(np.mean(Ss ** 2)))
# Selberg prediction for the mean square over the range: (1/2pi^2) * <log log t>
ll = np.array([math.log(math.log(t)) for t in grid])
pred_rms = float(np.sqrt(np.mean((1.0 / (2 * math.pi ** 2)) * ll)))
print(f"\nRMS S(t) over t in [2000, 9000]:  {rms:.4f}")
print(f"Selberg 1946 prediction (RMS):   {pred_rms:.4f}   (ratio {rms / pred_rms:.3f})")

# Periodic-law contrast: a fixed periodic configuration (density matched to mean at T0) has S(t) a
# bounded PERIODIC function of t: O(1) amplitude, and its values repeat exactly from period to period.
# Real zeros: S(t) is O(1)-scale at any fixed height too (below), BUT it is asymptotically growing,
# E[S(t)^2] ~ (1/2pi^2) log log t -> infinity (Selberg 1946). The periodic law's S stays bounded forever.
# So the DISTINGUISHING content is purely asymptotic: bounded (periodic) vs unbounded-with-scale-sqrt(log log t).
# At any fixed finite height both look O(1) -- no finite-T certificate can see the difference.
print("\nPeriodic configuration of matching density: S(t) is a bounded periodic function (O(1) forever);")
print("Real zeros: S(t) is O(1)-scale at these heights but E[S^2] ~ (1/2pi^2) log log t -> infinity (Selberg).")
print("=> the distinguishing fact is ASYMPTOTIC (bounded vs sqrt(log log t) growth), invisible at fixed T.")
