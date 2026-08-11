#!/usr/bin/env python3
"""Triangulation: in-house m3 values vs the Hejhal/RS triple-correlation kernel.

EXECUTIONER deliverable for the paper-hejhal94 note. Self-contained; does not touch
shared tools/. Run:

    cd /home/vstaln/riemann && uv run --quiet --with numpy --with mpmath python \
        research/notes/paper_hejhal94_crosscheck.py

Objects (all in mean-spacing units; the sine process, diagonal-1 Gram convention
G_ij = sinc(pi*lam*(x_i-x_j)) = sin(pi*lam*d)/(pi*lam*d)):
  S(x) = sin(pi x)/(pi x)                    (sine-kernel correlation density)
  K(x) = sin(pi lam x)/(pi lam x)            (Gram kernel at window lam)
  rho3(u,v) = det[ S ]_{3x3} = 1 - S(u)^2 - S(v)^2 - S(u+v)^2 + 2 S(u)S(v)S(u+v)
              (the Hejhal/RS triple-correlation density; CS2006 (1.2), det matrix)
  trace test function (CS coords u=x1-x2, v=x1-x3):  f(u,v) = K(u)K(v)K(u-v)
  A2(lam) = int_R K(u)^2 (1 - S(u)^2) du          (pair part)
  A3(lam) = int_int_R2 f(u,v) rho3(u,v) du dv     (connected part)
  m3(lam) = 1 + 3 A2(lam) + A3(lam)

In-house PROVEN closed forms (attack-twobandwidth.md, attack-thirdmoment.md):
  m2(lam) = 1/lam + lam/3 ;   m3(lam) = 3 + 3/lam + 1/lam^2 - lam - 6 J2(lam)(1+1/lam)
  J2(lam) = int_0^inf sinc(pi lam u)^2 sinc(pi u)^2 du
  values: m3(1/2)=5, m3(2/3)=13/4, m3(1)=2 ;  m2: 13/6, 31/18, 4/3.

Checks performed:
  (1) m2, m3 closed-form values at lam = 1/2, 2/3, 1  -> compare with 5, 13/4, 2.
  (2) A2 by direct 1D quadrature (decays u^-4) vs closed form.
  (3) A3 by direct 2D quadrature of the absolutely-convergent parts:
          A3 = D - 3B + 2C,  D = int_int f,  B = int_int f S(u)^2,  C = int_int f SSS
      with D = 1/lam^2 (Fourier identity), B = (2/lam) J2, C computed by direct 2D
      Gauss-Legendre (integrand ~ 1/(u^2 v^2 (u+v)^2), absolutely convergent).
  (4) Fourier support of f:  fhat(a,b) = (1/lam^3) L(a,b),
      L(a,b) = measure{t: |t|<lam/2, |a+t|<lam/2, |b-t|<lam/2},
      supported in {|a|<lam, |b|<lam, |a+b|<lam}  (checked at sample points vs the
      direct 2D quadrature of the FT).  For lam < 1 this lies strictly inside
      Hejhal's hexagon {|a|<=1,|b|<=1,|a+b|<=1} (CS2006)  => the Hejhal theorem
      (RH-conditional) covers the third trace for lam < 1.
  (5) Form factor: FT of the smooth part 2S(u)S(v)S(u+v) of the density rho3 at
      sample points, compared with 2G(a,b), G(a,b) = max((2-|a|-|b|-|a+b|)/2, 0)
      (Hejhal (11) / RS Thm 4.1 as quoted in Fazzari-Gerspach arXiv:2412.20099).
  (6) 0.85082 arithmetic (paper 7.5(g)): 1/2 + (2m2-m3)/18 + (4/9)(19/27), with the
      paper's window value 2m2-m3 = 0.68524...  and the flat value 2/3.
"""
import numpy as np
import mpmath as mp

mp.mp.dps = 40

def S(x):  # sin(pi x)/(pi x)
    return mp.sinc(mp.pi * x)

def K(x, lam):  # sin(pi lam x)/(pi lam x)
    return mp.sinc(mp.pi * lam * x)

# ---------------- J2, A2, closed forms ----------------
def J2_mp(lam):
    f = lambda u: K(u, lam) ** 2 * S(u) ** 2
    return mp.quad(f, [0, 1, mp.inf])

def A2_closed(lam): return 1 / lam - 2 * J2_mp(lam)

def m2_closed(lam): return 1 + A2_closed(lam)  # = 1/lam + lam/3

def A3_closed(lam):
    return 1 / lam ** 2 - (6 / lam) * J2_mp(lam) + 2 * (1 - lam / 2)

def m3_closed(lam): return 1 + 3 * A2_closed(lam) + A3_closed(lam)

# ---------------- direct 1D A2 (numpy Gauss-Legendre, tail bounded) ----------------
def gl1(f, a, b, n=2000):
    x, w = np.polynomial.legendre.leggauss(n)
    xs = 0.5 * (b - a) * x + 0.5 * (b + a)
    return 0.5 * (b - a) * np.dot(w, f(xs))

def A2_direct(lam, R=80.0, n=4000):
    # int_R K(u)^2 (1 - S(u)^2) du = 1/lam - int_R K(u)^2 S(u)^2 du
    g = lambda u: np.sinc(lam * u) ** 2 * np.sinc(u) ** 2
    val = gl1(g, -R, R, n)                 # ~ 2 * int_0^R K^2 S^2
    tail = 2.0 / (3 * np.pi ** 4 * lam ** 2 * R ** 3)   # int_{|u|>R} g
    return 1.0 / lam - (val + tail)

# ---------------- direct C part (absolutely convergent 2D) ----------------
def C_direct(lam, R=35.0, n=220):
    x, w = np.polynomial.legendre.leggauss(n)
    xs = R * x; ws = R * w
    U, V = np.meshgrid(xs, xs, indexing='ij')
    W = U + V
    Ku = np.sinc(lam * U); Kv = np.sinc(lam * V); Kw = np.sinc(lam * W)
    Su = np.sinc(U); Sv = np.sinc(V); Sw = np.sinc(W)
    integ = Ku * Kv * Kw * Su * Sv * Sw
    return np.sum(integ * np.outer(ws, ws))

# ---------------- fhat: analytic L-formula and direct FT ----------------
def L_formula(a, b, lam):
    """length{t: |t|<lam/2, |a+t|<lam/2, |b-t|<lam/2}."""
    lo = max(-lam / 2, -a - lam / 2, b - lam / 2)
    hi = min(lam / 2, -a + lam / 2, b + lam / 2)
    return max(0.0, hi - lo)

def fhat_analytic(a, b, lam):
    return L_formula(a, b, lam) / lam ** 3

def fhat_direct(a, b, lam, R=40.0, n=300):
    """FT of f(u,v)=K(u)K(v)K(u-v): int_int K(u)K(v)K(u-v) e^{-2pi i (au+bv)} dudv."""
    x, w = np.polynomial.legendre.leggauss(n)
    xs = R * x; ws = R * w
    U, V = np.meshgrid(xs, xs, indexing='ij')
    W = U - V
    integ = np.sinc(lam * U) * np.sinc(lam * V) * np.sinc(lam * W) \
            * np.exp(-2j * np.pi * (a * U + b * V))
    return np.sum(integ * np.outer(ws, ws))

# ---------------- FT of the smooth part of the density rho3 ----------------
def rho3_smooth_fhat(a, b, R=30.0, n=260):
    """FT[2 S(u)S(v)S(u+v)] at (a,b) by direct 2D GL (absolutely convergent)."""
    x, w = np.polynomial.legendre.leggauss(n)
    xs = R * x; ws = R * w
    U, V = np.meshgrid(xs, xs, indexing='ij')
    W = U + V
    integ = 2.0 * np.sinc(U) * np.sinc(V) * np.sinc(W) \
            * np.exp(-2j * np.pi * (a * U + b * V))
    return np.sum(integ * np.outer(ws, ws))

def G(a, b):
    return max((2.0 - abs(a) - abs(b) - abs(a + b)) / 2.0, 0.0)

# ---------------- A3 by direct 2D quadrature of the fast parts ----------------
def A3_direct_parts(lam, R=35.0, n=220):
    Cv = C_direct(lam, R, n)
    Bv = (2.0 / lam) * float(J2_mp(lam))
    Dv = 1.0 / lam ** 2
    return Dv - 3 * Bv + 2 * Cv, Dv, Bv, Cv

def main():
    print("=" * 78)
    print("PAPER-HEJHAL94 CROSS-CHECK: in-house m3 values vs Hejhal/RS kernel")
    print("=" * 78)
    lams = [mp.mpf(1) / 2, mp.mpf(2) / 3, mp.mpf(1)]
    ref_m2 = {"1/2": mp.mpf(13) / 6, "2/3": mp.mpf(31) / 18, "1": mp.mpf(4) / 3}
    ref_m3 = {"1/2": mp.mpf(5), "2/3": mp.mpf(13) / 4, "1": mp.mpf(2)}
    names = ["1/2", "2/3", "1"]

    print("\n--- (1) closed-form m2, m3 at lam = 1/2, 2/3, 1 ---")
    print(f"{'lam':>5} {'m2_closed':>14} {'m2_ref':>10} {'m3_closed':>14} {'m3_ref':>10} {'2m2-m3':>10}")
    for name, lam in zip(names, lams):
        m2c = m2_closed(lam); m3c = m3_closed(lam)
        print(f"{name:>5} {mp.nstr(m2c, 12):>14} {mp.nstr(ref_m2[name], 10):>10} "
              f"{mp.nstr(m3c, 14):>14} {mp.nstr(ref_m3[name], 10):>10} {mp.nstr(2*m2c-m3c, 10):>10}")

    print("\n--- (2) A2 direct 1D quadrature vs closed form ---")
    for name, lam in zip(names, lams):
        a2d = A2_direct(float(lam)); a2c = float(A2_closed(lam))
        print(f"lam={name}: A2_direct={a2d:.6f}  A2_closed={a2c:.6f}  diff={a2d-a2c:+.2e}")

    print("\n--- (3) A3: D - 3B + 2C decomposition (C by direct 2D GL) ---")
    print(f"{'lam':>5} {'D=1/lam^2':>10} {'B=(2/lam)J2':>12} {'C_direct':>10} {'2(1-lam/2)':>10} {'A3_parts':>12} {'A3_closed':>12}")
    for name, lam in zip(names, lams):
        a3p, Dv, Bv, Cv = A3_direct_parts(float(lam))
        a3c = float(A3_closed(lam))
        print(f"{name:>5} {Dv:>10.6f} {Bv:>12.6f} {Cv:>10.6f} {2*(1-float(lam)/2):>10.6f} {a3p:>12.6f} {a3c:>12.6f}")

    print("\n--- (3b) m3 assembled from the kernel parts (1+3A2+D-3B+2C) ---")
    for name, lam in zip(names, lams):
        a2c = float(A2_closed(lam)); a3p, *_ = A3_direct_parts(float(lam))
        m3k = 1 + 3 * a2c + a3p
        ok = "AGREE" if abs(m3k - float(ref_m3[name])) < 1e-5 else "MISMATCH"
        print(f"lam={name}: m3_kernel={m3k:.6f}  in-house={float(ref_m3[name]):.6f}  -> {ok}")

    print("\n--- (4) Fourier support of the trace test function f(u,v)=K(u)K(v)K(u-v) ---")
    print("    analytic fhat(a,b)=(1/lam^3)L(a,b), support {|a|<lam,|b|<lam,|a+b|<lam}")
    for lam in (0.5, 1.0):
        print(f"  lam={lam}:")
        pts = [(0.9*lam, 0.0, "|a|<lam, b=0    (in) "),
               (0.9*lam, 0.9*lam, "|a+b|=1.8lam  (out)"),
               (0.5*lam, 0.5*lam, "|a+b|=1.0lam  (out)"),
               (0.4*lam, 0.4*lam, "|a+b|=0.8lam  (in) ")]
        for (a, b, lbl) in pts:
            fa = fhat_analytic(a, b, lam)
            fd = fhat_direct(a, b, lam)
            print(f"    ({a:.2f},{b:.2f}) {lbl}: analytic={fa:.5f}  direct={fd.real:.5f}  match={abs(fa-fd.real)<2e-3}")
    print("    Hejhal hexagon (CS2006): {|a|<=1, |b|<=1, |a+b|<=1}; support strictly inside iff lam<1.")

    print("\n--- (5) Form factor: FT[2 S(u)S(v)S(u+v)] (smooth part) vs 2G(a,b) ---")
    print("    G(a,b) = max((2-|a|-|b|-|a+b|)/2,0)  [Hejhal (11)/RS Thm 4.1 via fg2412.20099]")
    for (a, b) in [(0.2, 0.2), (0.5, 0.2), (0.6, 0.4), (0.9, 0.1), (0.5, 0.9), (1.2, 0.2)]:
        ff = rho3_smooth_fhat(a, b).real
        g2 = 2 * G(a, b)
        print(f"    (a,b)=({a:.1f},{b:.1f}): FT[2SSS]={ff:.5f}  2G={g2:.5f}  diff={ff-g2:+.5f}")

    print("\n--- (6) 0.85082 arithmetic (paper 7.5(g)) ---")
    for tag, t in [("paper window cos(8s/5): 2m2-m3 = 0.68524", 0.68524),
                   ("flat window: 2m2-m3 = 2/3", 2.0 / 3.0)]:
        Nd = 0.5 + t / 18 + (4.0 / 9.0) * (19.0 / 27.0)
        print(f"  1/2 + ({t:.5f})/18 + (4/9)(19/27) = {Nd:.5f}   [{tag}]")
    print("  components: (4/9)(19/27)=76/243=0.312757..., 1/2=0.5")

    print("\n--- (7) sanity: J2 reference values (attack-twobandwidth: 5/12, 7/18, 1/3) ---")
    ref_j2 = {"1/2": mp.mpf(5) / 12, "2/3": mp.mpf(7) / 18, "1": mp.mpf(1) / 3}
    for name, lam in zip(names, lams):
        j2 = J2_mp(lam)
        print(f"  J2({name}) = {mp.nstr(j2, 18)}   (ref {mp.nstr(ref_j2[name], 12)})")

if __name__ == "__main__":
    main()
