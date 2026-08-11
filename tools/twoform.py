#!/usr/bin/env python3
"""twoform.py — L8 exploratory numerics: the Weil form W and the CGG zeta'(rho)-moment
form C written on the SAME zero set (first 300 zeros), shared test-function frame.

Reconstruction notes (honest):
- The CGG98 / Bui-Heath-Brown13 form is NOT in the held papers (BHB 1302.5018 is a
  paper-hunt target; CGG98 appears only as [CGG98] in the held paper). We reconstruct
  the natural zero-set version from the paper's description (P §7.5(c): the CGG98 (1.2)
  integrality device = Prop 4.4 regrouping) and B25 §1 ("discrete, mollified moments of
  zeta'(rho)"), i.e. the frame-weighted quadratic form
      C = (1/int psi^2) * V^T diag(w) V,   w_rho = |zeta'(rho) M(rho)|^2,
  sharing the frame of the finite-T Weil form W = (1/int psi^2) V^T V (attack-finitet).
- On RH zeta'(rho) != 0 iff rho is simple, so rank C <= N_s unconditionally (M(rho)!=0).
- The CGG lower bound is Cauchy-Schwarz: N_s >= sup_a |a.u|^2 / (a^T C a), u = sum_j
  zeta'(rho_j) M(rho_j) v_j  (the "first discrete mollified moment" direction).
- The joint (direct-sum) rank-trace bound: on RH rank(W)+rank(C) <= N + N_s and
  rank >= (tr)^2/||.||^2 gives  N + N_s >= (trW+trC)^2 / (||W||^2 + ||C||^2).

Everything is f64 except the zeta'(rho) values (mpmath, 30 digits, converted to float).
"""
import math
import numpy as np
import mpmath as mp

mp.mp.dps = 30

# ---------------- frame (from attack-finitet / tools/finitet) ----------------
SQRT2 = math.sqrt(2.0)
FRAC_1_SQRT2 = 1.0 / SQRT2
PI = math.pi
TWO_PI = 2.0 * PI

INT_PSI2 = 0.5 + math.sin(SQRT2) / (2.0 * SQRT2)          # int psi^2 = 0.849227999318304
POLE = SQRT2 / TWO_PI                                      # 0.225079...

def psi(s):
    """Psi(s) = int_{-1/2}^{1/2} cos(sqrt2 u) e^{-2 pi i s u} du, real for real s.
    Removable poles at 2 pi s = +- sqrt2 with value 1/2 + sin(sqrt2)/(2 sqrt2) = INT_PSI2."""
    d1 = SQRT2 - TWO_PI * s
    d2 = SQRT2 + TWO_PI * s
    if abs(d1) < 1e-12:
        t1 = 0.5
    else:
        t1 = math.sin(FRAC_1_SQRT2 - PI * s) / d1
    if abs(d2) < 1e-12:
        t2 = 0.5
    else:
        t2 = math.sin(FRAC_1_SQRT2 + PI * s) / d2
    return t1 + t2

def psi2(s):
    """Psi2(s) = transform of psi^2 (Poisson kernel identity sum_k psi(s-k)psi(s'-k))."""
    ps = PI * s
    t1 = math.sin(ps) / (2.0 * ps) if abs(ps) > 1e-12 else 0.5
    a = SQRT2 - ps
    b = SQRT2 + ps
    t2 = math.sin(a) / a if abs(a) > 1e-12 else 1.0
    t3 = math.sin(b) / b if abs(b) > 1e-12 else 1.0
    return t1 + 0.25 * (t2 + t3)

# ---------------- data ----------------
gams = []
with open("/home/vstaln/riemann/tools/data/zeros_1_1000.txt") as f:
    for line in f:
        p = line.split()
        if len(p) >= 2:
            gams.append(float(p[1]))

N = 300
# finitet-style window: [T, 2T] containing exactly N zeros (scan; count jumps by 1 per zero)
def count_in(t):
    return sum(1 for g in gams if t <= g < 2.0 * t)

T = None
for t in np.arange(300.0, 900.0, 0.5):
    if count_in(t) == N:
        T = float(t)
        break
assert T is not None, "no window with exactly N zeros found"
gwin = [g for g in gams if T <= g < 2.0 * T]
assert len(gwin) == N
s_rho = [(g - T) * N / T for g in gwin]   # in (0, N)
gams = gwin                              # zeta'(rho) evaluated at the window zeros

print(f"window: T={T:.4f}, 2T={2*T:.4f}, N={N}, zero indices used: #{gams.index(gwin[0])+1}..#{gams.index(gwin[-1])+1} (ordinals in file)")
print(f"int psi^2 = {INT_PSI2:.15f}")

# ---------------- frame V (N x N) ----------------
V = np.empty((N, N))
for j in range(N):
    for k in range(N):
        V[j, k] = psi(s_rho[j] - k)

# ---------------- zeta'(rho_j) via mpmath ----------------
print("computing zeta'(rho_j), j=1..%d (mpmath, dps=30)..." % N)
zp = []
for g in gams:
    zp.append(complex(mp.zeta(mp.mpf('0.5') + 1j * mp.mpf(g), 1, 1)))
zp = np.array(zp)
print("  done. min|zeta'|={:.4e} max|zeta'|={:.4e} mean|zeta'|={:.4e}".format(
    np.abs(zp).min(), np.abs(zp).max(), np.abs(zp).mean()))

def mobius(y):
    mu = np.zeros(y + 1, dtype=int)
    mu[1] = 1
    for i in range(1, y + 1):
        if mu[i] != 0:
            for j in range(2 * i, y + 1, i):
                mu[j] -= mu[i]
    return mu

def mollified_weights(y=0):
    """w_j = |zeta'(rho_j) M(rho_j)|^2; y=0 means M=1."""
    if y == 0:
        return np.abs(zp) ** 2
    mu = mobius(y)
    Mvals = np.zeros(N, dtype=complex)
    for n in range(1, y + 1):
        if mu[n] != 0:
            c = mu[n] * n ** (-0.5)
            for j in range(N):
                Mvals[j] += c * np.exp(-1j * gams[j] * math.log(n))
    return np.abs(zp * Mvals) ** 2

print("\n================= results =================")
# ---------- Weil form ----------
VtV = V.T @ V
W = VtV / INT_PSI2
trW = np.trace(W)
hsW2 = np.sum(W * W)
print(f"\n[Weil form]  trW={trW:.6f}  trW/N={trW/N:.6f}  ||W||^2_HS={hsW2:.6f}  /N={hsW2/N:.6f}")
print(f"             Weil bound 2trW-||W||^2 = {2*trW-hsW2:.6f}  /N = {(2*trW-hsW2)/N:.6f}")
print(f"             Cauchy (trW)^2/||W||^2 = {(trW**2)/hsW2:.6f}  /N = {trW**2/hsW2/N:.6f}")

# ---------- CGG forms (M=1 and Mollified) ----------
def signed_M1(zp):
    return zp

def signed_M(y):
    mu = mobius(y)
    out = np.zeros(N, dtype=complex)
    for n in range(1, y + 1):
        if mu[n] != 0:
            c = mu[n] * n ** (-0.5)
            for j in range(N):
                out[j] += c * np.exp(-1j * gams[j] * math.log(n))
    return zp * out

def run(label, signed):
    w = np.abs(signed) ** 2
    C = (V.T @ (w[:, None] * V)) / INT_PSI2
    Craw = V.T @ (w[:, None] * V)          # raw second-moment form (no 1/int psi^2)
    trC = np.trace(C)
    hsC2 = np.sum(C * C)
    diagC2 = np.sum(np.diag(C) ** 2)
    offC2 = hsC2 - diagC2
    # ---- CGG certificate: sup_a |a.u|^2 / (a^T Craw a) = u^T Craw^+ u ----
    # (raw Craw: the certificate must use sum_j w_j |a.v_j|^2, no 1/int psi^2 factor)
    u = (signed * V.T).sum(axis=1)          # complex N-vector
    lam, Q = np.linalg.eigh(Craw)
    lmax = lam[-1]
    thr = 1e-10 * lmax
    qt = Q.T @ u
    sup = sum(abs(qt[i]) ** 2 / lam[i] for i in range(N) if lam[i] > thr)
    ceiling = np.sum(w > 0)                 # = #{j : zeta'(rho_j) M(rho_j) != 0} <= N_s
    # real-a certificate: lambda_max of 2x2 pencil on Re u, Im u w.r.t. Craw^+
    def cp(v):
        vq = Q.T @ v
        return Q @ (vq / np.where(lam > thr, lam, 1.0))
    Rv, Iv = u.real, u.imag
    a2 = Rv @ cp(Rv); b2 = Rv @ cp(Iv); c2 = Iv @ cp(Iv)
    sup_real = np.linalg.eigvalsh(np.array([[a2, b2], [b2, c2]]))[-1]
    # ---- joint direct-sum bound ----
    joint = (trW + trC) ** 2 / (hsW2 + hsC2)
    # ---- rank of C (fact: rank C <= N_s = #simple, since zeta'(rho)=0 iff multiple) ----
    lmaxC = lam[-1]
    rankC = int(np.sum(lam > 1e-8 * lmaxC))
    # ---- per-zero weight stats ----
    print(f"\n[{label}]  trC={trC:.6f}  (mean w = {w.mean():.6f}; trW/N={trW/N:.4f})")
    print(f"           ||C||^2_HS={hsC2:.6f}  diag={diagC2:.6f}  offdiag={offC2:.6f}")
    print(f"           w: min={w.min():.4e}  p10={np.percentile(w,10):.4e}  med={np.median(w):.4e}  p90={np.percentile(w,90):.4e}  max={w.max():.4e}")
    print(f"           rank C = {rankC}  (<= N_s = #simple in window; all {N} window zeros are simple per LMFDB)")
    print(f"           CGG cert N_s >= u^T Craw^+ u = {sup:.3f}  (ceiling #(zeta'M!=0) = {ceiling} <= N_s; real-a: {sup_real:.3f})")
    print(f"           joint direct-sum (trW+trC)^2/(||W||^2+||C||^2) = {joint:.3f}  -> implied N_s >= {joint-N:.3f}")
    print(f"           Cauchy on C: (trC)^2/||C||^2 = {(trC**2)/hsC2:.3f}")
    # near-multiple detectors (both-forms-small count): |zeta'M| small
    nsmall = [np.sum(w < eps * w.mean()) for eps in (0.01, 0.1, 0.25)]
    print(f"           #zeros with |zeta'M|^2 < eps*mean, eps=0.01/0.1/0.25: {nsmall}")
    order = np.argsort(w)
    print(f"           ordinates of the 5 smallest w: {[round(gams[i],3) for i in order[:5]]}")
    # correlation of log w with ||v_j||^2 (joint smallness check)
    vn = np.sum(V * V, axis=1) / INT_PSI2
    r = np.corrcoef(np.log(w), vn)[0, 1]
    print(f"           corr(log w_j, ||v_j||^2) = {r:+.4f}  (||v||^2 range: {vn.min():.4f}..{vn.max():.4f})")
    return sup, joint

print("\n-- M = 1 (unmollified zeta'-moment form) --")
run("M=1", signed_M1(zp))
print("\n-- M = Mobius mollifier, y=10 (exploratory: NOT the CGG98-optimal mollifier) --")
run("M=Mob(y=10)", signed_M(10))
print("\n-- M = Mobius mollifier, y=30 --")
run("M=Mob(y=30)", signed_M(30))
