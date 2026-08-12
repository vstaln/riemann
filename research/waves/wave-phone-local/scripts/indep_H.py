#!/usr/bin/env python3
# INDEPENDENT H(alpha) computation for the record claim.
# Spec (from paper main.tex sec "The window functional"):
#   v(s) = cos(alpha s) on [-1/2, 1/2]
#   I0 = int v^2 = 2 sin(alpha/2)/alpha
#   I2 = 1/2 + sin(alpha)/(2 alpha)
#   J  = intint |s-t| v(s) v(t) ds dt   (kink at s=t)
#   c  = I0^2/(I2 + J),  H(alpha) = 2 - 1/c
# Analytic J: J = -2 I2/alpha^2 + (I0/2 + 2 cos(alpha/2)/alpha^2) I0
# Independent checks:
#   (a) analytic formula at 120 digits
#   (b) kink-split quadrature (exact split at s=t): J = 2 * int_{s=0}^{1/2} int_{t=-1/2}^{s} (s-t) v(s) v(t) dt ds
#   (c) naive mp.quad of the raw double integral (documented to FAIL at the kink)
import mpmath as mp
mp.mp.dps = 120

alpha = mp.mpf('1.49')

def analytic(alpha):
    a = alpha
    I0 = 2*mp.sin(a/2)/a
    I2 = mp.mpf('0.5') + mp.sin(a)/(2*a)
    J  = -2*I2/(a*a) + (I0/2 + 2*mp.cos(a/2)/(a*a))*I0
    c  = I0*I0/(I2+J)
    H  = 2 - 1/c
    return I0, I2, J, c, H

def split_quad(alpha, dps=100):
    mp.mp.dps = dps
    a = alpha
    v = lambda s: mp.cos(a*s)
    # J = int_{-1/2}^{1/2} int_{-1/2}^{1/2} |s-t| v(s)v(t) dt ds
    # split into s in [-1/2,0] and [0,1/2] by symmetry J = 2 * J_+ where
    # J_+ = int_0^{1/2} [ int_{-1/2}^{s} (s-t) v(t) dt + int_{s}^{1/2} (t-s) v(t) dt ] v(s) ds
    def inner(s):
        # int_{-1/2}^{s} (s-t) v(t) dt
        a1 = mp.quad(lambda t: (s-t)*v(t), [mp.mpf('-0.5'), s])
        # int_{s}^{1/2} (t-s) v(t) dt
        a2 = mp.quad(lambda t: (t-s)*v(t), [s, mp.mpf('0.5')])
        return (a1+a2)*v(s)
    J = 2*mp.quad(inner, [mp.mpf('0'), mp.mpf('0.5')])
    return J

def naive_quad(alpha, dps=80):
    mp.mp.dps = dps
    a = alpha
    v = lambda s: mp.cos(a*s)
    J = mp.quad(lambda s, t: mp.fabs(s-t)*v(s)*v(t),
                [mp.mpf('-0.5'), mp.mpf('0.5')],
                [mp.mpf('-0.5'), mp.mpf('0.5')])
    return J

I0, I2, J, c, H = analytic(alpha)
print("alpha        =", mp.nstr(alpha, 60))
print("I0 (analytic)= 2 sin(a/2)/a =", mp.nstr(I0, 60))
print("I2 (analytic)= 1/2 + sin a/(2a) =", mp.nstr(I2, 60))
print("J  (analytic)=", mp.nstr(J, 60))
print("c  = I0^2/(I2+J) =", mp.nstr(c, 60))
print("H  = 2 - 1/c =", mp.nstr(H, 60))
print()
print("CLAIMED H(1.49) = 0.6724218860964")

# kink-split quadrature
mp.mp.dps = 100
Js = split_quad(alpha, 100)
I0s = 2*mp.sin(alpha/2)/alpha
I2s = mp.mpf('0.5') + mp.sin(alpha)/(2*alpha)
cs  = I0s*I0s/(I2s+Js)
Hs  = 2 - 1/cs
print()
print("kink-split quadrature J =", mp.nstr(Js, 60))
print("kink-split quadrature H =", mp.nstr(Hs, 60))
print("|J_analytic - J_split|  =", mp.nstr(abs(J-Js), 30))
print("|H_analytic - H_split|  =", mp.nstr(abs(H-Hs), 30))

# naive quadrature (expected to fail at the kink)
Jnaive = naive_quad(alpha, 80)
cnaive = I0s*I0s/(I2s+Jnaive)
Hnaive = 2 - 1/cnaive
print()
print("NAIVE mp.quad J =", mp.nstr(Jnaive, 40))
print("NAIVE H        =", mp.nstr(Hnaive, 40))
print("|H_analytic - H_naive| =", mp.nstr(abs(H-Hnaive), 25))

# Cross-check alpha = sqrt(2) (paper: H0 = 3/2 - (1/sqrt2) cot(1/sqrt2) = 0.6725007036794116)
a2 = mp.sqrt(2)
I0b, I2b, Jb, cb, Hb = analytic(a2)
H0 = mp.mpf('1.5') - (1/a2)*mp.cot(1/a2)
print()
print("CHECK alpha=sqrt2: analytic H =", mp.nstr(Hb, 40))
print("CHECK H0 paper   =", mp.nstr(H0, 40))
print("diff =", mp.nstr(abs(Hb-H0), 25))

# The tawanerguo alpha=1.47 value: H = 0.6724587094007293
I0c, I2c, Jc, cc, Hc = analytic(mp.mpf('1.47'))
print()
print("CHECK alpha=1.47: H =", mp.nstr(Hc, 40), " (tawanerguo: 0.6724587094007293)")
