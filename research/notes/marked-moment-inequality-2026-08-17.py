#!/usr/bin/env python3
"""
L2 wall-breaker: does a PROVEN moment inequality on the marked Gram matrix supply
the missing T-bound (connected part) for the marked-m3 certificate?

THEOREM UNDER TEST (per configuration, any PSD kernel matrix G, marks M=diag(m),
A = M^{1/2} G M^{1/2} PSD; marked moments m_k = tr((MG)^k)/tr(M) = tr(A^k)/tr(A)):
  Cauchy-Schwarz on (lambda_i^{3/2}), (lambda_i^{1/2})  =>  m3 >= m2^2.
  Hence for a law:  S3(law) = E[m3] >= E[m2^2] >= (E[m2])^2   (Jensen).
So if E[m2] is pinned by the certificate's read rows + p1 + marks, then
S3(law) >= (E[m2])^2 is a PROVEN lower bound on the marked third moment —
bypassing the T-decomposition entirely.

Two conventions:
  (A) TORUS projection kernel (the certificate's formal setting, attack-law-s3):
      periodic kernel c_j = 1/B (|j| <= M, B=2M+1), d = circular conv c*c.
      Exact identity (D2, machine-verified in attack_law_s3.py):
        m2(config) = (1/256) sum_m d_m |mu_hat(m)|^2
      => with the certificate's read rows E|mu_hat(m)|^2 = m (m=1..255), mu_hat(0)=256:
        E[m2] = (1/256)[d_0*65536 + sum_{m=1..255} d_m*m]   (p1-INDEPENDENT)
        and  E[m2] = u(lam) + (2-p1)  with u = attack-law-s3's u.
  (B) CONTINUUM sinc kernel (the empirical/measurement convention): measured on
      GUE blocks, marks {1,2} at q, both no-rescale and mass-density-1.

Command:  cd /home/vstaln/riemann && uv run --quiet --with numpy python3 \
          research/notes/marked-moment-inequality-2026-08-17.py
"""
import math, glob
import numpy as np

p0 = 10909258999421303588095230195816054408197 / 16000000000000000000000000000000000000000
N = 256
q = (1.0 - p0) / (1.0 + p0)
print("=" * 78)
print("PROVEN moment inequality m3 >= m2^2 on the marked Gram matrix: does it supply")
print("the missing T-bound for the marked-m3 certificate?  (2026-08-17, L2)")
print("=" * 78)
print(f"p0 = {p0:.12f},  q = {q:.6f}")

# ---------------------------------------------------------------------------
# 1. THEOREM verification on random 256-periodic marked configurations
#    (certificate's own torus kernel), plus u() reproduction.
# ---------------------------------------------------------------------------
def per_kernel_coeffs(lam):
    M = int(math.floor(128 * lam)); B = 2 * M + 1
    c = np.zeros(N)
    for j in range(-M, M + 1):
        c[j % N] = 1.0 / B
    return c, M, B

def torus_moments(x, m, lam):
    """Marked m2, m3 of a 256-periodic config with the projection kernel.
       m2 = (1/256) sum_{i,j} m_i m_j K_ij^2 = (1/256) sum_m d_m |mu_hat(m)|^2
       m3 = (1/256) tr((MG)^3)."""
    c, M, B = per_kernel_coeffs(lam)
    d = np.fft.ifft(np.fft.fft(c) ** 2).real
    E = np.abs(np.array([np.sum(m * np.exp(2j * np.pi * j * x / N)) for j in range(N)])) ** 2
    m2 = np.sum(d * E) / 256.0
    K = per_kernel_values(x, lam)
    MG = K * m[None, :]
    m3 = np.trace(np.linalg.matrix_power(MG, 3)).real / np.sum(m)
    return m2, m3, d

def per_kernel_values(x, lam):
    c, M, B = per_kernel_coeffs(lam)
    n = len(x)
    dd = (x[:, None] - x[None, :]) % N
    K = np.zeros((n, n), dtype=complex)
    for j, cj in enumerate(c):
        if cj != 0:
            K += cj * np.exp(2j * np.pi * j * dd / N)
    return K.real

rng = np.random.default_rng(0)
print("\n--- 1. THEOREM m3 >= m2^2 on random 256-periodic marked configs (torus kernel)")
viol = {lam: 0 for lam in (0.5, 2.0/3.0)}
worstgap = {lam: 1e9 for lam in (0.5, 2.0/3.0)}
for lam in (0.5, 2.0/3.0):
    for trial in range(20):
        npos = int(rng.integers(150, 210))
        x = rng.permutation(np.arange(N))[0:npos].astype(float)
        m = np.ones(npos)
        nd = int(rng.integers(0, 40))
        if nd > 0:
            m[rng.choice(npos, size=nd, replace=False)] = 2.0
        m2, m3, _ = torus_moments(x, m, lam)
        if m3 + 1e-12 < m2 * m2:
            viol[lam] += 1
        worstgap[lam] = min(worstgap[lam], m3 - m2 * m2)
    print(f"  lam={lam:.4f}: m3 >= m2^2 held on all 20 draws: {viol[lam]==0}"
          f"  (min gap m3-m2^2 = {worstgap[lam]:+.6f})")

# ---------------------------------------------------------------------------
# 2. Reproduction of attack-law-s3 u(), and the row-pinned E[m2] (torus convention)
# ---------------------------------------------------------------------------
print("\n--- 2. Row-pinned E[m2] in the certificate's torus convention")
rows = np.arange(N, dtype=float)          # E|mu_hat(m)|^2 = m for m=1..255
rows[0] = N * N                           # E|mu_hat(0)|^2 = 65536
for lam in (0.5, 2.0/3.0):
    c, M, B = per_kernel_coeffs(lam)
    d = np.fft.ifft(np.fft.fft(c) ** 2).real
    u_p0 = np.sum(d * (rows - 256.0 * (2.0 - p0))) / 256.0
    Em2_rows = np.sum(d * rows) / 256.0
    print(f"  lam={lam:.4f} (M={M}, B={B}):  u(p0) = {u_p0:.6f}   (attack-law-s3: "
          f"{1.162449 if abs(lam-0.5)<1e-9 else 0.675981})")
    print(f"    row-pinned E[m2] = {Em2_rows:.6f}   | E[m2] - (u(p0)+2-p0) | = "
          f"{abs(Em2_rows - (u_p0 + 2.0 - p0)):.2e}")
    # p1-independence of E[m2] (rows are flat; marks only change the row *read*, not m2's value)
    vals = {p1: np.sum(d * rows) / 256.0 for p1 in (0.5, 0.6, p0, 0.75, 0.9, 1.0)}
    spread = max(vals.values()) - min(vals.values())
    print(f"    E[m2] at p1 in {{0.5,0.6,p0,0.75,0.9,1.0}}: identical {spread:.1e}  "
          f"=> E[m2]^2 = {Em2_rows**2:.6f}")
    print(f"    => theorem S3(law) >= (E[m2])^2 = {Em2_rows**2:.6f}   (pinned bottom "
          f"D+3u = {4-3*p0+3*u_p0:.6f}; read window 5+eps, eps=0.44 -> 5.4400)")

# ---------------------------------------------------------------------------
# 3. GUE synthetic family: marked m2, m3, per-config inequality, both conventions
# ---------------------------------------------------------------------------
def gue_blocks(n, K, seed):
    rr = np.random.default_rng(seed)
    out = []
    for _ in range(K):
        A = (rr.standard_normal((n, n)) + 1j * rr.standard_normal((n, n))) / math.sqrt(2.0 * n)
        out.append(np.linalg.eigvalsh((A + A.conj().T) / 2.0))
    return out

def per_block_spacing(w):
    wi = w[np.abs(w) < 1.9]
    lo, hi = np.percentile(wi, 5), np.percentile(wi, 95)
    return (hi - lo) / len(wi)

def marks_for(n, p1, rr):
    nd = int(round(n * (1.0 - p1)))
    m = np.ones(n)
    if nd > 0:
        m[rr.choice(n, size=nd, replace=False)] = 2.0
    return m

def m2m3(xb, lam, m=None):
    n = len(xb)
    G = np.sinc(lam * np.subtract.outer(xb, xb))
    if m is not None:
        MG = m[:, None] * G
        m2 = np.trace(MG @ MG) / m.sum()
        m3 = np.trace(np.linalg.matrix_power(MG, 3)).real / m.sum()
        return m2, m3
    m2 = np.trace(G @ G) / n
    m3 = np.trace(np.linalg.matrix_power(G, 3)).real / n
    return m2, m3

print("\n--- 3. GUE synthetic marked family (n=300 K=40 seed=99; seed=7 robustness)")
n, K = 300, 40
results = {}
for seed in (99, 7):
    blocks = gue_blocks(n, K, seed)
    sp = [per_block_spacing(w) for w in blocks]
    xs = [(w[np.abs(w) < 1.9]) / sp[i] for i, w in enumerate(blocks)]
    xs = [x for x in xs if len(x) > 10]
    rr = np.random.default_rng(11)
    row = {}
    for p1 in (0.5, 0.6, p0, 0.75, 0.9, 1.0):
        for conv in ("point-density", "mass-density-1"):
            m2s, m3s, gaps = [], [], []
            for xb in xs:
                m = marks_for(len(xb), p1, rr)
                x2 = xb
                if conv == "mass-density-1":
                    L = xb.max() - xb.min()
                    x2 = xb * (m.sum() / L)
                m2, m3 = m2m3(x2, 0.5, m)
                m2s.append(m2); m3s.append(m3); gaps.append(m3 - m2 * m2)
            m2s = np.array(m2s); m3s = np.array(m3s); gaps = np.array(gaps)
            row[(p1, conv)] = (m2s.mean(), m3s.mean(), (m2s.mean())**2, gaps.min())
    results[seed] = row

for conv in ("point-density", "mass-density-1"):
    print(f"\n  [{conv} convention, lam=1/2]")
    print(f"  {'p1':>8} | {'Em2':>8} {'Em3':>8} {'Em2^2':>8} {'min gap m3-m2^2':>16} | bound>5.44?")
    for p1 in (0.5, 0.6, p0, 0.75, 0.9, 1.0):
        m2, m3, sq, gap = results[99][(p1, conv)]
        m2b, m3b, sqb, gapb = results[7][(p1, conv)]
        print(f"  {p1:8.4f} | {m2:8.4f} {m3:8.4f} {sq:8.4f} {gap:16.6f} | "
              f"{'YES' if sq > 5.44 else 'no'}   (seed7: Em2={m2b:.4f} Em3={m3b:.4f})")
    print("  (theorem: per-config m3 >= m2^2; law: S3 >= (E[m2])^2; window 5+eps=5.44)")

# ---------------------------------------------------------------------------
# 4. Real zeros: all marks 1, m2/m3 at lam=1/2, inequality check
# ---------------------------------------------------------------------------
print("\n--- 4. Real zeros (LMFDB, all marks 1, windowed blocks B=2000, lam=1/2)")
def load_lmfdb_zeros():
    gammas = []
    for f in sorted(glob.glob('/home/vstaln/riemann/tools/argprinciple/data/lmfdb_zeros_*.txt')):
        for line in open(f):
            p = line.split()
            if len(p) >= 2:
                try:
                    gammas.append(float(p[1]))
                except ValueError:
                    pass
    return np.array(sorted(gammas))

def density1_normalize(g):
    return (g / (2 * np.pi)) * np.log(g / (2 * np.pi)) - g / (2 * np.pi) + 7.0 / 8.0

g = load_lmfdb_zeros()
xs = density1_normalize(g)
B = 2000
m2s, m3s = [], []
for start in range(0, len(xs) - B, B):
    xb = xs[start:start+B]
    xb = xb - xb[0]
    m2, m3 = m2m3(xb, 0.5)
    m2s.append(m2); m3s.append(m3)
m2s = np.array(m2s); m3s = np.array(m3s)
print(f"  {len(g)} zeros, {len(m2s)} blocks:  m2 = {m2s.mean():.4f} +/- {m2s.std()/math.sqrt(len(m2s)):.4f}"
      f"  (theory 13/6 = 2.1667),  m3 = {m3s.mean():.4f} +/- {m3s.std()/math.sqrt(len(m3s)):.4f} (sine 5)")
print(f"  m3 >= m2^2 : {m3s.mean():.4f} >= {m2s.mean()**2:.4f}  (gap {m3s.mean()-m2s.mean()**2:+.4f})")

# ---------------------------------------------------------------------------
# 5. Verdict
# ---------------------------------------------------------------------------
print("\n--- 5. VERDICT ------------------------------------------------------------")
lam = 0.5
c, M, B = per_kernel_coeffs(lam)
d = np.fft.ifft(np.fft.fft(c) ** 2).real
u_p0 = np.sum(d * (rows - 256.0 * (2.0 - p0))) / 256.0
Em2_rows = np.sum(d * rows) / 256.0
print(f"  Certificate's torus convention (read rows flat): E[m2] = {Em2_rows:.6f} (p1-indep),")
print(f"    theorem bound S3(law) >= (E[m2])^2 = {Em2_rows**2:.6f}")
print(f"    vs read window 5+0.44 = 5.4400: excluded by theorem, margin "
      f"{Em2_rows**2 - 5.44:+.4f}" if Em2_rows**2 > 5.44 else "    (below window)")
print(f"    vs pinned bottom D+3u = {4-3*p0+3*u_p0:.4f}: theorem is "
      f"{'stronger' if Em2_rows**2 > 4-3*p0+3*u_p0 else 'weaker'} by "
      f"{Em2_rows**2 - (4-3*p0+3*u_p0):+.4f}")
