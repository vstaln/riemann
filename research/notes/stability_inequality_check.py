#!/usr/bin/env python3
"""Numerical sanity check of ainta eq. (2.1) and its proof ingredients.

Every quantitative claim in `research/notes/lean-stability-inequality.md`
is checked here. Run:
    uv run --with numpy python research/notes/stability_inequality_check.py

Imports numpy only (no scipy). Verdicts printed per check.
"""
import numpy as np

rng = np.random.default_rng(20260811)

def frob_sq(A):
    return (np.abs(A) ** 2).sum()

def trace_re(A):
    return np.real(np.trace(A))

def herm_random(n, scale=1.0):
    A = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
    A = (A + A.conj().T) / 2
    return A * scale

def eigvals_h(A):
    return np.linalg.eigvalsh((A + A.conj().T) / 2)

def pos_part(A):
    w, V = np.linalg.eigh((A + A.conj().T) / 2)
    wp = np.clip(w, 0, None)
    return (V * wp) @ V.conj().T

def neg_part(A):
    w, V = np.linalg.eigh((A + A.conj().T) / 2)
    wn = np.clip(-w, 0, None)
    return (V * wn) @ V.conj().T

def psi(t):
    return np.where(t <= 2, (t - 1) ** 2, 2 * t - 3)

def check(name, ok, detail=""):
    ok = bool(ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))
    return ok

results = []

# (P3) positive part: ‖Q₊‖² ≥ 4·tr(Q₊) − 4b, for Q with ≤ b positive eigenvalues
print("== (P3) positive part ==")
ok3 = True
for n in (4, 8, 16):
    Q = herm_random(n)
    Qp = pos_part(Q)
    b = int((eigvals_h(Q) > 1e-9).sum())
    lhs = frob_sq(Qp)
    rhs = 4 * trace_re(Qp) - 4 * b
    ok3 &= (lhs >= rhs - 1e-9)
    results.append((f"n={n} b={b}: ||Q+||^2 >= 4tr(Q+)-4b", lhs >= rhs - 1e-9,
                    f"lhs={lhs:.4f} rhs={rhs:.4f}"))
Q = herm_random(6)
w, V = np.linalg.eigh((Q + Q.conj().T) / 2)
Qpsd = (V * np.abs(w)) @ V.conj().T
Qp = pos_part(Qpsd)
lhs, rhs = frob_sq(Qp), 4 * trace_re(Qp) - 4 * 6
results.append(("PSD Q (b=n): slack ~= sum(lambda-2)^2", lhs - rhs >= -1e-9,
                f"lhs-rhs={lhs-rhs:.4f}"))

# (P4) scalar min identity: min_{n>=0} (p-n)^2 + 4n = 2p - 1 + Psi(p)
print("== (P4) scalar min identity ==")
ok4 = True
for p in np.linspace(0, 4, 1001):
    ns = np.linspace(0, 6, 8001)
    mn = ((p - ns) ** 2 + 4 * ns).min()
    val = 2 * p - 1 + psi(p)
    ok4 &= abs(mn - val) < 1e-6
results.append(("min over n>=0 matches 2p-1+Psi(p)", ok4))

# (P5) Hoffmann-Wielandt: ||A-B||^2 >= sum(p_i - n_i)^2  (Hermitian)
print("== (P5) Hoffmann-Wielandt ==")
ok5 = True
for n in (4, 8):
    A, B = herm_random(n), herm_random(n, 0.5)
    lhs = frob_sq(A - B)
    pa = np.sort(eigvals_h(A))[::-1]
    pb = np.sort(eigvals_h(B))[::-1]
    rhs = ((pa - pb) ** 2).sum()
    ok5 &= (lhs >= rhs - 1e-8)
    results.append((f"n={n}", lhs >= rhs - 1e-8, f"lhs={lhs:.4f} rhs={rhs:.4f}"))

# (P7) tr(P) <= r  and  tr(P) = sum_j ||col_j||^2
print("== (P7) trace bound ==")
ok7 = True
for (n, r) in ((5, 3), (8, 6), (10, 2)):
    V = rng.standard_normal((n, r)) + 1j * rng.standard_normal((n, r))
    V = V / np.maximum(np.linalg.norm(V, axis=0), 1e-12)
    P = V @ V.conj().T
    trP = trace_re(P)
    col_sums = sum(np.linalg.norm(V[:, j]) ** 2 for j in range(r))
    ok7 &= (trP <= r + 1e-9) and (abs(trP - col_sums) < 1e-8)
    results.append((f"n={n} r={r}: tr(P)={trP:.4f} <= r={r}", trP <= r + 1e-9))
results.append(("tr(P) = sum_j||col_j||^2", ok7))

def random_instance():
    n = int(rng.integers(2, 12)); r = int(rng.integers(1, min(n, 5) + 1))
    b = int(rng.integers(0, r + 1))          # b <= r always
    V = rng.standard_normal((n, r)) + 1j * rng.standard_normal((n, r))
    V = V / np.maximum(np.linalg.norm(V, axis=0), 1e-12)
    w = np.concatenate([rng.uniform(0.0, 1.5, b), rng.uniform(-1.5, -0.05, r - b),
                        np.zeros(max(n - r, 0))])
    U = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
    U, _ = np.linalg.qr(U)
    Q = (U * w) @ U.conj().T
    return n, r, b, V, Q

# THE MAIN INEQUALITY (2.1): ||P+Q||^2 >= 4·tr(P+Q) - 3r - 4b + tr Psi(M)
print("== (2.1) main inequality, random instances ==")
ok2 = True
for trial in range(400):
    n, r, b, V, Q = random_instance()
    Qp = pos_part(Q)
    P = V @ V.conj().T
    M = V.conj().T @ V
    lhs = frob_sq(P + Q)
    wM = np.linalg.eigvalsh((M + M.conj().T) / 2)
    trPsiM = psi(wM).sum()
    rhs = 4 * (trace_re(P) + trace_re(Q)) - 3 * r - 4 * b + trPsiM
    if lhs < rhs - 1e-6:
        ok2 = False
        results.append((f"trial {trial} n={n} r={r} b={b}", False,
                        f"lhs={lhs:.4f} rhs={rhs:.4f}"))
        break
results.append((f"400 random instances (b<=r): (2.1) holds", ok2))

# (P6) chain:  ||P-Q-||^2 + 4·tr(Q-) >= 2·tr(P) - r + tr Psi(M)
#   via Hoffmann-Wielandt + per-pair scalar identity (Q- = neg_part, PSD)
print("== (P6) chain + paper form ==")
ok6 = True
ok_paper = True
for trial in range(400):
    n, r, b, V, Q = random_instance()
    Qp = pos_part(Q); Qn = neg_part(Q)       # Q- PSD (proper)
    P = V @ V.conj().T; M = V.conj().T @ V
    wM = np.linalg.eigvalsh((M + M.conj().T) / 2)
    wP = np.linalg.eigvalsh(P); wN = np.linalg.eigvalsh(Qn)
    pdesc = np.sort(wP)[::-1]; ndesc = np.sort(wN)[::-1]
    hw_ok = frob_sq(P - Qn) >= ((pdesc - ndesc) ** 2).sum() - 1e-8
    pair_ok = ((pdesc - ndesc) ** 2 + 4 * ndesc).sum() >= (2 * pdesc - 1 + psi(pdesc)).sum() - 1e-8
    trPsiM = psi(wM).sum()
    comp6 = frob_sq(P - Qn) + 4 * trace_re(Qn) >= 2 * trace_re(P) - r + trPsiM - 1e-6
    ok6 &= (hw_ok and pair_ok and comp6)
    lhs = frob_sq(P + Q)
    rhs = 4 * trace_re(P + Q) - 3 * r - 4 * b + trPsiM
    ok_paper &= (lhs >= rhs - 1e-6)
results.append(("(P6) chain [HW + per-pair scalar + trPsiM] on 400", ok6))
results.append(("paper form (2.1) 4·tr(P+Q)-3r-4b+trPsiM on 400", ok_paper))

# Guardrail: the "sum-of-boxes" strong form is FALSE in general
print("== strong-form counterexample (guardrail) ==")
n, r, b = 4, 4, 0
V = np.eye(n, r)
w = np.array([-1.484, -1.189, -0.53, -0.24])
Q = (np.eye(n) * w) @ np.eye(n).conj().T
P = V @ V.conj().T; M = V.conj().T @ V
wM = np.linalg.eigvalsh((M + M.conj().T) / 2)
lhs = frob_sq(P + Q)
strong_rhs = (2 * trace_re(P) - r + psi(wM).sum()) + (4 * trace_re(pos_part(Q)) - 4 * b)
paper_rhs = (4 * trace_re(P) - 3 * r + psi(wM).sum()) + (4 * trace_re(pos_part(Q)) - 4 * b)
results.append(("strong form is FALSE here (guardrail)", lhs < strong_rhs,
                f"lhs={lhs:.4f} strong={strong_rhs:.4f} paper={paper_rhs:.4f}"))

# (P2) cross-term nonnegativity: tr(Q+(P-Q-)) >= 0
print("== (P2) cross term >= 0 ==")
ok2b = True
for trial in range(200):
    n = int(rng.integers(2, 10)); r = int(rng.integers(1, min(n, 4) + 1))
    V = rng.standard_normal((n, r)) + 1j * rng.standard_normal((n, r))
    V = V / np.maximum(np.linalg.norm(V, axis=0), 1e-12)
    Q = herm_random(n, 1.0)
    P = V @ V.conj().T
    ct = np.real(np.trace(pos_part(Q) @ (P - neg_part(Q))))
    ok2b &= (ct >= -1e-8)
results.append(("200 random: tr(Q+(P-Q-)) >= 0", ok2b))

# Psi properties
print("== Psi properties ==")
ts = np.linspace(0, 10, 20001)
results.append(("Psi >= 0 on [0,inf)", bool((psi(ts) >= -1e-12).all())))
results.append(("Psi continuous at 2", bool(abs(psi(2.0) - (2 * 2 - 3)) < 1e-12 and
                abs(psi(2.0) - (2 - 1) ** 2) < 1e-12)))

print()
allok = all(ok for _, ok, *_ in results)
print(f"TOTAL: {sum(1 for _, ok, *_ in results if ok)}/{len(results)} checks PASS")
print("VERDICT:", "ALL CHECKS PASS" if allok else "SOME CHECKS FAILED")
