"""Verify attack-nevanlinna and attack-qi-sweep algebraic/numeric claims."""
import numpy as np
import cmath

print("=== nevanlinna ===")
# identity m2 = 2 - p1 for marks in {1,2}, sum marks = N
for N in (6, 256, 1000):
    for s in range(0, N + 1, max(1, N // 7)):
        if s > N: break
        d = (N - s) // 2
        if 2 * d + s != N: continue
        p1 = s / N
        m2 = (s + 4 * d) / N
        assert abs(m2 - (2 - p1)) < 1e-12
print("identity m2 = 2 - p1 holds for all tested (s,d)  [PROVEN algebra]")

# P- and P+ canonical measures: moments (1,1,4/3)
for name, atoms, masses in [("P-", [1 - 1 / np.sqrt(3), 1 + 1 / np.sqrt(3)], [0.5, 0.5]),
                            ("P+", [0, 4 / 3], [0.25, 0.75])]:
    moms = [sum(m * a ** k for m, a in zip(masses, atoms)) for k in range(5)]
    print("%s moments (m0..m4) = %s  (m1=1 m2=4/3 expected)" % (name, ["%.6f" % x for x in moms]))

# Nevanlinna parametrization: w(z) = ((3z-1)phi + (z-1)) / ((3z^2-4z)phi + (z^2 - 2z + 2/3))
# verify phi=0 -> P-, phi=inf -> P+ (w ~ (3z-1)/(3z^2-4z) and (z-1)/(z^2-2z+2/3))
def wP(z):  # P- Stieltjes: int dsigma/(z-x)
    return 0.5 / (z - (1 - 1 / np.sqrt(3))) + 0.5 / (z - (1 + 1 / np.sqrt(3)))
def wPp(z):
    return 0.25 / (z - 0) + 0.75 / (z - 4 / 3)
for z in (2.0, 2.5 + 0.3j, 1.7):
    zi = complex(z)
    a = (3 * zi - 1) / (3 * zi * zi - 4 * zi)
    b = (zi - 1) / (zi * zi - 2 * zi + 2 / 3)
    print("z=%s: phi=0 w=%s vs w(P-)=%s ; phi=inf w=%s vs w(P+)=%s" %
          (z, a, wP(zi), b, wPp(zi)))
# moments from Laurent expansion of phi=0 branch: w(z) ~ (3z)/(3z^2) * ... = 1/z + m1/z^2 + m2/z^3...
# (3z-1)/(3z^2-4z) = (3z-1)/(z(3z-4)) -> 1/z + (1/3)/z^2 + (4/9)/z^3 + (16/27)/z^4 ...
# m0=1, m1=1/3?? that would be wrong. Check directly: series of (3z-1)/(3z^2-4z):
# = (3z-1)/(3z^2) * 1/(1 - 4/(3z)) = (1/z - 1/(3z^2))(1 + 4/(3z) + 16/(9z^2) + ...)
# = 1/z + [4/3 - 1/3]/z^2 + [16/9 - 4/9]/z^3 + ... = 1/z + 1/z^2 + 4/3/z^3 + ...
print("phi=0 Laurent: m0=1 m1=1 m2=4/3 (from (3z-1)/(3z^2-4z) expansion)")

# test phi = 1, -2, z, z/(z^2+1): Laurent coefficients
def laurent(w, z0=3.0, n=6):
    # w(z) ~ sum_{k>=0} c_k / (z-z0')... use expansion in 1/z at large |z|: compute
    # coefficients by evaluating w at large z: w(z) ~ m0/z + m1/z^2 + ... via numerical
    # differentiation-free fit on a circle |z|=R
    R = 1000.0
    M = 10
    coeffs = []
    for k in range(M):
        # c_k = (1/2pi i) int w(z) z^{k-1} dz around |z|=R; c_0 = m0 etc. Use:
        # w(z) = sum_{k>=1} m_{k-1} / z^k  =>  m_{k-1} = (1/2pi i) int w(z) z^{k-1} dz
        th = np.linspace(0, 2 * np.pi, 4000, endpoint=False)
        zs = R * np.exp(1j * th)
        vals = np.array([complex(w(zi)) for zi in zs])
        integ = np.sum(vals * zs ** (k - 1)) * (2 * np.pi * 1j * R) / 4000
        coeffs.append((integ / (2 * np.pi * 1j)).real)
    return coeffs

def W(phi):
    def f(z):
        p = complex(phi(z))
        a = (3 * z - 1) * p + (z - 1)
        b = (3 * z * z - 4 * z) * p + (z * z - 2 * z + 2 / 3)
        return a / b
    return f

for name, phi in [("1", lambda z: 1 + 0j), ("-2", lambda z: -2 + 0j), ("z", lambda z: z),
                  ("z/(z^2+1)", lambda z: z / (z * z + 1)), ("1e40 z", lambda z: 1e40 * z)]:
    c = laurent(W(phi))
    print("phi=%s Laurent (m0,m1,m2,m3) = %s" % (name, ["%.4f" % x for x in c[:4]]))
    # Im w < 0 on upper half plane:
    z = 1.0 + 1.0j
    w = W(phi)(z)
    print("   Im w(1+i) = %.4f  (should be < 0 for a positive measure)" % w.imag)

print()
print("=== qi-sweep ===")
# identity (1): for Q = m(vv^T + conj(v)conj(v)^T), eigenvalues {+m a, -m b}:
# ||Q||_F^2 = (tr Q)^2 + 2 (m a)(m b) = (tr Q)^2 + 2|det Q|
rng = np.random.default_rng(7)
worst = 0
for _ in range(20):
    n = 12
    v = rng.standard_normal(n) + 1j * rng.standard_normal(n)
    m = 1.0
    M = m * (np.outer(v, v) + np.outer(v.conj(), v.conj()))
    ev = np.linalg.eigvalsh(M)
    tr = ev.sum(); det = np.prod(ev)
    lhs = np.sum(ev ** 2)
    rhs = tr ** 2 + 2 * np.abs(det)
    worst = max(worst, abs(lhs - rhs))
print("identity ||Q||^2 = (trQ)^2 + 2|detQ|: max err over 20 random v = %.2e" % worst)

# sharp config: A = diag(1..1, 2..2) with s1 ones, b twos: ||A||^2 = 4 trA - 3 s1 - 4 b
for s1, b in [(67, 16), (6725, 1638)]:
    A = np.diag([1.0] * s1 + [2.0] * b)
    tr = A.trace(); hs = np.sum(A * A)
    pred = 4 * tr - 3 * s1 - 4 * b
    print("sharp diag(%d ones, %d twos): ||A||^2=%.6f  4tr-3s1-4b=%.6f  err=%.2e" % (s1, b, hs, pred, abs(hs - pred)))

# (L') gap: (tr Q+ - 2b)^2/b  at sharp config (tr Q+ = 2b exactly)
b = 16
trQplus = 2 * b
print("sharp config: (trQ+ - 2b)^2/b =", (trQplus - 2 * b) ** 2 / b, " (=0)")

# random indefinite Q: ||Q||^2 >= (tr Q+)^2/b
worstgap = 1e9
for _ in range(400):
    n = 10
    Aq = rng.standard_normal((n, n)); Q = (Aq + Aq.T) / 2
    ev = np.linalg.eigvalsh(Q)
    b_ = sum(ev > 1e-12)
    if b_ == 0: continue
    trQp = sum(x for x in ev if x > 0)
    gap = (trQp ** 2 / b_) - (4 * np.sum(ev) - 4 * b_)
    worstgap = min(worstgap, gap)
print("min over 400 random Q of [(trQ+)^2/b - (4trQ - 4b)] = %.4f (all >= 0?)" % worstgap)

# f1curve structural: Parseval p1 >= 1/2 + 1/(2N) and bandwidth-2 wall
N = 256
# Sigma_{j=1}^{255} j = 32640; sum m^2 = 383.5 forced; p1 = s/256, s = 512 - 383.5 -> 128.5/256
print("f1curve Parseval: sum m^2 = 383.5 -> p1 >= 1/2 + 1/(2N) =", 0.5 + 1 / (2 * N))
print("bandwidth-2 wall: floor(A*N)(floor(A*N)+1) <= 261632 -> floor(AN) <= %d, A <= %.6f"
      % (int(np.floor(np.sqrt(261632 + 0.25) - 0.5)), 511 / 256))
print("second-period sum j=256..511 =", sum(range(256, 512)), " (= 98176 = total twisted Parseval)")
