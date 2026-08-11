#!/usr/bin/env python3
"""Local search: can a SINGLE marked config approximate the ramp f(j)=j
(j=1..255) pointwise?  Hill-climb over positions (moves + fractional-part
changes) minimizing the sup distance.  If even the best config is far, the
hull distance is bounded below by the family's spectrum shapes (documented
exhaustion evidence for route 2).
"""
import numpy as np, time

N = 256
j = np.arange(1, N + 1)
DFT_int = np.exp(2j * np.pi * np.outer(j, np.arange(N)) / N)
fracs = np.array([0.0, 0.5, 0.25, 0.75, 1/3, 2/3, 1/8, 3/8, 5/8, 7/8, 1/6, 5/6])
DFT_f = {u: np.exp(2j * np.pi * j * u / N)[:, None] * DFT_int for u in fracs}

def spectrum(poss, marks):
    z = np.zeros(N, dtype=complex)
    for x, m in zip(poss, marks):
        base = int(np.floor(x)) % N
        u = x - np.floor(x)
        z = z + m * DFT_f[round(u, 6)][:, base] if round(u, 6) in DFT_f else z + m * np.exp(2j * np.pi * j * x / N)
    return np.abs(z) ** 2

def spectrum2(poss, marks):
    z = np.zeros(N, dtype=complex)
    for x, m in zip(poss, marks):
        z = z + m * np.exp(2j * np.pi * j * x / N)
    return np.abs(z) ** 2

def supdist(f):
    return np.max(np.abs(f[:255] - np.arange(1, 256)))

rng = np.random.default_rng(77)
# start: signature config
n_h, d = 12, 41
s = N - n_h - 2 * d
int_pos = rng.choice(N, size=s + d, replace=False)
ms = [1] * s + [2] * d
rng.shuffle(ms)
half_q = rng.choice(N, size=n_h, replace=False)
poss = list(int_pos) + [q + 0.5 for q in half_q]
marks = ms + [1] * n_h

best = supdist(spectrum2(poss, marks))
best_poss = poss[:]; best_marks = marks[:]
t0 = time.time(); it = 0
while time.time() - t0 < 240:
    it += 1
    # random move: pick a mark, change its position (keep frac class options)
    i = int(rng.integers(0, len(poss)))
    new_poss = poss[:]
    op = rng.random()
    if op < 0.5:
        new_poss[i] = int(rng.integers(0, N))
    else:
        u = float(rng.choice(fracs[1:]))
        new_poss[i] = int(rng.integers(0, N)) + u
    new_poss[i] %= N
    # keep distinct? not enforced (allow coincidences)
    f2 = spectrum2(new_poss, marks)
    d2 = supdist(f2)
    if d2 < best:
        best = d2; poss = new_poss[:]; best_poss = poss[:]
print(f"local search: {it} iterations in 240s")
print(f"best single-config sup-distance to ramp = {best:.4f}")
f = spectrum2(best_poss, best_marks)
resid = f[:255] - np.arange(1, 256)
worst = np.argsort(-np.abs(resid))[:8]
print("worst rows:", [(int(w + 1), round(float(resid[w]), 3)) for w in worst])
print(f"sum_{{1..255}} f = {f[:255].sum():.1f} (ramp: 32640)   f(256) = {f[255]:.1f} (target 54126.6)")
