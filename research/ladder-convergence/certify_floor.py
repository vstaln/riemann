#!/usr/bin/env python3
"""RIGOROUS interval certification of the pure block floor

    tr Psi(G_n(u)) / n  >=  eps_cert

over u_i > 0, sum u_i <= 4, G_ij = k(y_j - y_i), y_j = u_1+..+u_j.

Strategy: exhaustive branch-and-bound on the (n-1)-dimensional simplex,
  * per-cell rigorous lower bounds on k(x) via Arb balls (interval midpoint
    + radius, monotone enclosure of the sinc form),
  * a rigorous lower bound for tr Psi(G) from a ball enclosure of the
    Gram matrix: for the symmetric G with entries ball_ij, take the exact
    lower-eigenvalue bound   lambda_min(G) >= m_center - r_F  where
    m_center = min eigenvalue of the center matrix (computed in Arb as a
    lower bound) and r_F = Frobenius-radius of the ball matrix.  Then
    tr Psi(G) >= n*Psi((m_center - r_F)_+) + (n-1)*Psi( (tr_upper - (m_center-r_F))_+ )
    ... this is crude; a sharper route is Weyl:  tr Psi(G) >= sum_k Psi(m_k - r_F)
    with m_k the eigenvalues of the center.  We use the latter (valid because
    Psi is nondecreasing on [0,oo) and Psi(|lam - shift| ...) -- need care:
    eigenvalue perturbation |lam_k(G) - m_k| <= ||G - center||_2 <= r_F,
    and Psi is 1-Lipschitz on [0,2] and nondecreasing, so
    sum Psi(lam_k) >= sum Psi(m_k - r_F).  Since m_k >= 0 and Psi >= -1/4
    can be negative, we clamp the argument at 0: Psi(t) >= Psi(max(0,t))
    for t in [0,2]?  NO: Psi decreases on [0,1].  Use instead
    sum Psi(lam_k) >= sum (Psi(m_k - r_F) clamped below by Psi(0)=1? ...
    -- see below; we implement the safe lower bound and VALIDATE it against
    exact eigh on random cells.)
  * splitting: pick the widest coordinate; terminate when cell width < 1e-3
    (or when lower >= target).

Labels: this certifies eps_cert (a rational lower bound), NOT the true floor.
The certificate's eps_cert must be <= the numerically-estimated floor.

Run: cd .../ladder-convergence
     uv run --quiet --with python-flint --with numpy --with scipy python certify_floor.py
"""
import itertools
import math
import time

from flint import arb, fmpq, ctx

ctx.prec = 128

SQ2 = arb(2).sqrt()
PI = arb.pi()
K0 = SQ2 * (1 / SQ2).sin()          # K(0) = sqrt(2) sin(1/sqrt2)
GRID = 2000
SPAN = 4

def kern_ball(x: arb) -> arb:
    """Ball enclosure of k(x) = K(x)/K0, K(x)=int cos(sqrt2 t) cos(2pi x t)dt."""
    f = 2 * PI * x
    left = ((SQ2 - f) / 2).sinc()
    right = ((SQ2 + f) / 2).sinc()
    return ((left + right) / 2) / K0

def ball_mid_rad(x: float, rad: float):
    """Enclosure of k over [x-rad, x+rad] via interval evaluation."""
    mid = arb(x)
    r = arb(rad)
    lo = kern_ball(mid - r)
    hi = kern_ball(mid + r)
    # interval enclosure: take union of the two point values (crude but valid
    # if k is monotone on the cell -- it is NOT in general; instead use the
    # standard midpoint-radius interval arithmetic of Arb: build a ball and
    # evaluate).
    # Arb's arb() with a radius gives a ball; function evaluation is rigorous.
    b = arb(x, rad)
    v = kern_ball(b)
    return float(v.lower()), float(v.upper())

def psi_ball(t_low: float) -> float:
    """Lower bound of Psi(t) for t >= t_low (t_low may be < 0)."""
    if t_low <= 0.0:
        # Psi(t) for t in [0,2]: min at t=1 is 0; for t<0 no meaning (eigs >=0)
        return 0.0 if t_low <= 0.0 else (t_low - 1.0)**2
    if t_low <= 2.0:
        # Psi decreasing on [0,1], increasing on [1,2]: min on [t_low, inf)
        # is at t=max(t_low,1) -> Psi = (max(t_low,1)-1)^2
        return (max(t_low, 1.0) - 1.0) ** 2
    return 2.0 * t_low - 3.0

def tr_psi_lower_from_center(center_eigs, radius):
    """Rigorous lower bound for tr Psi(G) from eigenvalue-ball radius.

    |lam_k(G) - m_k| <= ||G - C||_2 <= r_F (Frobenius radius).  Psi is
    1-Lipschitz on [0,2] and nondecreasing on [1,inf); Psi decreases on [0,1].
    Lower bound: lam_k >= m_k - r_F, so Psi(lam_k) >= Psi( (m_k - r_F)_+ )
    because Psi is nondecreasing on [0, inf)?  Psi is NOT monotone on [0,1].
    Correct approach: Psi(t) >= min over [max(0,m_k-r_F), m_k+r_F] of Psi,
    which is at t0 = clamp(1, m_k-r_F, m_k+r_F): Psi(t0).  Use that.
    """
    total = 0.0
    for mk in center_eigs:
        lo = max(0.0, mk - radius)
        hi = mk + radius
        # min of Psi on [lo,hi]: if 1 in [lo,hi], min=0; else at nearest end
        if lo <= 1.0 <= hi:
            total += 0.0
        else:
            if hi < 1.0:
                t = hi
            else:
                t = lo
            total += psi_ball(t)
    return total

def eigvals_lower_center(M):
    """Lower bounds for eigenvalues of the (float) center matrix via Arb."""
    # We need RIGOROUS lower bounds: do an Arb Jacobi/eigendecomposition.
    # flint exposes mp_... ?  Use the fact: eigenvalues of symmetric M are
    # >=  center value - residual.  We'll compute a certified interval for
    # each eigenvalue by Gershgorin-free approach: use Arb's built-in
    # eigensolver via matrix operations is not exposed.  Instead, we can
    # certify with a simple: bound each eigenvalue from below by
    # min_{||x||=1} x^T C x  >=  (1/n) tr C - ((n-1)/n) * sqrt(sum (C_ij)^2)?? 
    # Simplest VALID rigorous route: use the Courant-Fischer + rational
    # shift-invert: for a candidate shift s, test definiteness of (C - sI)
    # via Arb LDL.  Do a binary search per eigenvalue.
    return None  # replaced below

if __name__ == "__main__":
    print("certify_floor.py: scaffold — see notes for the rigorous strategy.")
