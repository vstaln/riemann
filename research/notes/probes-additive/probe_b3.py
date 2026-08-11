import numpy as np, time

# (1) I1 = ∫∫∫ K(u)K(v)K(w)K(u+v+w) dudvdw, K=sinc(pi la u); analytic = 2/3 (Irwin-Hall volume).
# direct 3D quadrature on [-R,R]^3, tail trend logR/R (twobandwidth note), should -> 2/3
def gl(n):
    x, w = np.polynomial.legendre.leggauss(n)
    return x, w

def I1_quad(R, n=40):
    x, w = gl(n)
    xs = R*x; ws = R*w
    uu, vv, ww = np.meshgrid(xs, xs, xs, indexing='ij')
    K = np.sinc(uu)*np.sinc(vv)*np.sinc(ww)*np.sinc(uu+vv+ww)
    return float(np.sum(K * np.einsum('i,j,k->ijk', ws, ws, ws)))

print("I1 = integral of '1'-term of rho4 (analytic 2/3):")
for R in (30, 60, 120):
    print(f"  R={R}: {I1_quad(R):.5f}")

# Irwin-Hall: P(sum of 3 U[0,1] > 2) = 1/6 (this is what gives the 2/3 volume)
from scipy.integrate import quad
f3 = lambda x: (3-x)**2/2          # density of sum of 3 uniforms on [0,1], x in [2,3]
p, _ = quad(f3, 2, 3)
print(f"Irwin-Hall P(S3>2) = {p:.6f}  (1/6 = {1/6:.6f}); cube vol 8*(1-2p) = {8*(1-2*p):.6f} = 16/3 -> I1 = 2/3") 

# (2) small finite-GUE ballpark for m3, m4 at lambda = 1 and 1/2 (slow BLAS: N=300 eigvalsh ~ 26s)
def gue_moments(N, M, lam):
    rng = np.random.default_rng(3)
    A = (rng.standard_normal((N, N)) + 1j*rng.standard_normal((N, N))) / np.sqrt(2*N)
    A = (A + A.conj().T)/2
    np.fill_diagonal(A, rng.standard_normal(N)/np.sqrt(N))
    x = np.linalg.eigvalsh(A)
    y = x*N/np.pi
    lo = (N-M)//2
    yc = y[lo:lo+M]
    d = yc[:,None]-yc[None,:]
    G = np.sinc(lam*d)
    ev = np.linalg.eigvalsh(G)
    return (ev**2).mean(), (ev**3).mean(), (ev**4).mean(), yc[0], yc[-1]

for lam in (1.0, 0.5):
    t0=time.time()
    m2, m3, m4, ylo, yhi = gue_moments(300, 60, lam)
    print(f"lam={lam} N=300 M=60: m2={m2:.3f} (ref {1/lam+lam/3:.3f})  m3={m3:.3f} (ref {5.0 if lam==0.5 else 2.0})  m4={m4:.3f}  [{time.time()-t0:.0f}s]")
print("paper targets: m4(1)=13/4=3.25; finite-M corrections ~ M/N = 20% expected")
