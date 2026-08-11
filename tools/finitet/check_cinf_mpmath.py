"""Independent mpmath cross-checks for finitet-cinf numbers (attack-finitet-cinf.md).
Uses explicit Gauss-Legendre quadrature (method='gauss-legendre') for speed.
"""
from mpmath import mp, mpf, quad, cos, sin, sqrt, pi
mp.dps = 25

sq2 = sqrt(2)
GL = dict(method='gauss-legendre')

# --- 1. closed-form Psi(s) = FT of psi(u)=cos(sqrt2 u) 1_{|u|<=1/2} (e^{-2pi i} convention) ---
def psi_closed(s):
    s = mpf(s)
    return sin(mpf(1)/sq2 - pi*s)/(sq2 - 2*pi*s) + sin(mpf(1)/sq2 + pi*s)/(sq2 + 2*pi*s)
def psi_quad(s):
    s = mpf(s)
    return quad(lambda u: cos(sq2*u)*cos(2*pi*s*u), [-mpf(1)/2, mpf(1)/2], **GL)
print("== Psi(s): closed form vs mpmath GL ==")
for s in [0.0, 0.37, 1.9, 5.3, 12.7]:
    print(f"s={s}: cf={mp.nstr(psi_closed(s),15)}  gl={mp.nstr(psi_quad(s),15)}  d={mp.nstr(abs(psi_closed(s)-psi_quad(s)),3)}")

# --- 2. int psi^2 ---
print("\nint psi^2 (mpmath GL) =", mp.nstr(quad(lambda u: cos(sq2*u)**2, [-mpf(1)/2, mpf(1)/2], **GL), 15), " (rust: 0.849227999318304)")

# --- 3. Q functional for box window must be 4/3 ---
def box(u): return mpf(1) if abs(u) <= mpf(1)/2 else mpf(0)
a = quad(box, [-mpf(1)/2, mpf(1)/2], **GL)
b = quad(lambda u: box(u)**2, [-mpf(1)/2, mpf(1)/2], **GL)
J = quad(lambda w: w*quad(lambda u: box(u)*box(w-u), [-mpf(1)/2, mpf(1)/2], **GL), [0, 1], **GL)
print("\nQ(box) =", mp.nstr((b + 2*J)/a**2, 12), " (expect 4/3)")

# --- 4. Q functional for v = cos^2(sqrt2 u) 1 (round-1 idealized model HS constant) ---
def v(u):
    return cos(sq2*u)**2 if abs(u) <= mpf(1)/2 else mpf(0)
a = quad(v, [-mpf(1)/2, mpf(1)/2], **GL)
b = quad(lambda u: v(u)**2, [-mpf(1)/2, mpf(1)/2], **GL)
J = quad(lambda w: w*quad(lambda u: v(u)*v(w-u), [-mpf(1)/2, mpf(1)/2], **GL), [0, 1], **GL)
print("Q(cos^2 1) =", mp.nstr((b + 2*J)/a**2, 12), " (rust q_window: 1.332970409; paper cos-1 kernel: 1.327499296)")

# --- 5. smoothed-kernel Phi_hat (eps=0.1, k=8) vs mpmath GL ---
# sigma_8(t) explicit polynomial: (1/B(9,9)) sum_i (-1)^i C(8,i) t^{9+i}/(9+i)
def sig8(t):
    if t <= 0: return mpf(0)
    if t >= 1: return mpf(1)
    B = mpf(1)
    # B(9,9) = 8!8!/17!
    num = 1
    for i in range(1, 9): num *= i
    num2 = num
    den = 1
    for i in range(1, 18): den *= i
    B = mpf(num*num2)/mpf(den)
    tot = mpf(0)
    from mpmath import binomial
    for i in range(9):
        tot += (-1)**i * binomial(8, i) * t**(9+i) / (9+i)
    return tot / B
eps = mpf(1)/10
def chi(u): return sig8((u + mpf(1)/2)/eps)
def phi(u): return chi(u)*chi(-u)*cos(sq2*u)
print("\neps=0.1 smoothed-cos Phi_hat vs mpmath GL:")
for s in [0.0, 0.5, 2.0, 4.0]:
    val = quad(lambda u: phi(u)*cos(2*pi*s*u), [-mpf(1)/2, mpf(1)/2], **GL)
    print(f"  Phi_hat({s}) = {mp.nstr(val,10)}")

# --- 6. int phi^2 for eps=0.1 smoothed-cos ---
n2 = quad(lambda u: phi(u)**2, [-mpf(1)/2, mpf(1)/2], **GL)
print("\nint phi^2 eps=0.1 (mpmath GL) =", mp.nstr(n2, 12), " (rust Simpson: 0.779369217)")
