//! Rust interval verifier for the coboundary floor inequality.
//! Port of tools/verify_coboundary_floor.py (the sanctioned Python arb verifier).
//! Uses a rigorous interval type (rug Float lo/hi pairs with directed rounding).
//!
//! 2026-08-18 FIX: weights now span 7 points (indices 0..=6), matching Python
//! `{(i,j): 2.0/(7-(j-i)) for i in range(7) for j in range(i+1,7)}`. The old
//! `for i in 0..q { for j in (i+1)..q }` with q=6 only made pairs among 0..5.
//!
//! 2026-08-18 ADD: tangent prune ported (was the documented NOT-FOR-CERTIFICATION
//! gap). tangent_lower() mirrors Python's arb convex-tangent bound:
//!   * second-derivative table: rigorous per-cell lower bounds of
//!     w'' = ((K/K0)^2)'' via interval enclosures of K, K', K'' over each cell
//!     (sinc value by exact-extrema fold; sinc', sinc'' by closed forms with
//!     interval sine/cosine enclosures, Taylor branch for cells near |z|<0.02);
//!   * range-minimum over the second table;
//!   * Hessian minorant from weight * min-w'' per pair block (+ q_i diag terms
//!     in coboundary mode), certified positive-definite by an interval LDL with
//!     strictly-positive pivot bounds (mirror of Python _arb_ldl_positive);
//!   * F(midpoint) - sum |grad_i| * radius_i tangent-plane lower bound.
//!
//! All arithmetic is outward-rounded (sound); any step that cannot be certified
//! makes the prune return None (skip-and-subdivide), never an overclaim of True.

use rug::float::{Constant, Round};
use rug::ops::CompleteRound;
use rug::Float;
use std::collections::HashMap;

const PREC: u32 = 128;
const PI: f64 = std::f64::consts::PI;

// ---------------------------------------------------------------------------
// Interval type: (lo, hi) with lo <= hi, directed rounding everywhere
// ---------------------------------------------------------------------------

fn mk(v: f64) -> Float { Float::with_val(PREC, v) }
fn mkd(v: f64) -> Float { Float::with_val_round(PREC, v, Round::Down).0 }
fn mku(v: f64) -> Float { Float::with_val_round(PREC, v, Round::Up).0 }
fn dadd(a: &Float, b: &Float) -> Float { (a + b).complete_round(PREC, Round::Down).0 }
fn uadd(a: &Float, b: &Float) -> Float { (a + b).complete_round(PREC, Round::Up).0 }
fn dsub(a: &Float, b: &Float) -> Float { (a - b).complete_round(PREC, Round::Down).0 }
fn usub(a: &Float, b: &Float) -> Float { (a - b).complete_round(PREC, Round::Up).0 }
fn dmul(a: &Float, b: &Float) -> Float { (a * b).complete_round(PREC, Round::Down).0 }
fn umul(a: &Float, b: &Float) -> Float { (a * b).complete_round(PREC, Round::Up).0 }
fn ddiv(a: &Float, b: &Float) -> Float { (a / b).complete_round(PREC, Round::Down).0 }
fn udiv(a: &Float, b: &Float) -> Float { (a / b).complete_round(PREC, Round::Up).0 }
fn dneg(a: &Float) -> Float { (-a).complete_round(PREC, Round::Down).0 }
fn uneg(a: &Float) -> Float { (-a).complete_round(PREC, Round::Up).0 }

#[derive(Clone, Debug)]
struct Iv {
    lo: Float,
    hi: Float,
}

impl Iv {
    fn new(lo: Float, hi: Float) -> Iv { Iv { lo, hi } }
    fn point(x: f64) -> Iv { Iv { lo: mkd(x), hi: mku(x) } }
    fn add(&self, o: &Iv) -> Iv { Iv { lo: dadd(&self.lo, &o.lo), hi: uadd(&self.hi, &o.hi) } }
    fn sub(&self, o: &Iv) -> Iv { Iv { lo: dsub(&self.lo, &o.hi), hi: usub(&self.hi, &o.lo) } }
    fn mul(&self, o: &Iv) -> Iv {
        let c0 = dmul(&self.lo, &o.lo);
        let c1 = dmul(&self.lo, &o.hi);
        let c2 = dmul(&self.hi, &o.lo);
        let c3 = dmul(&self.hi, &o.hi);
        let mut lo = c0.clone();
        for c in [&c1, &c2, &c3] { if *c < lo { lo = c.clone(); } }
        let u0 = umul(&self.lo, &o.lo);
        let u1 = umul(&self.lo, &o.hi);
        let u2 = umul(&self.hi, &o.lo);
        let u3 = umul(&self.hi, &o.hi);
        let mut hi = u0.clone();
        for c in [&u1, &u2, &u3] { if *c > hi { hi = c.clone(); } }
        Iv { lo, hi }
    }
    fn div(&self, o: &Iv) -> Iv {
        // assumes o does not contain 0
        let c0 = ddiv(&self.lo, &o.lo);
        let c1 = ddiv(&self.lo, &o.hi);
        let c2 = ddiv(&self.hi, &o.lo);
        let c3 = ddiv(&self.hi, &o.hi);
        let mut lo = c0.clone();
        for c in [&c1, &c2, &c3] { if *c < lo { lo = c.clone(); } }
        let u0 = udiv(&self.lo, &o.lo);
        let u1 = udiv(&self.lo, &o.hi);
        let u2 = udiv(&self.hi, &o.lo);
        let u3 = udiv(&self.hi, &o.hi);
        let mut hi = u0.clone();
        for c in [&u1, &u2, &u3] { if *c > hi { hi = c.clone(); } }
        Iv { lo, hi }
    }
    fn neg(&self) -> Iv { Iv { lo: dneg(&self.hi), hi: uneg(&self.lo) } }
    fn abs(&self) -> Iv {
        if self.lo >= mk(0.0) {
            self.clone()
        } else if self.hi <= mk(0.0) {
            self.neg()
        } else {
            let loabs = self.lo.clone().abs();
            let hiabs = self.hi.clone().abs();
            let h = if hiabs > loabs { hiabs } else { loabs };
            Iv { lo: mk(0.0), hi: h }
        }
    }
    fn sqrt(&self) -> Iv {
        let mut l = self.lo.clone(); l.sqrt_round(Round::Down);
        let mut h = self.hi.clone(); h.sqrt_round(Round::Up);
        Iv { lo: l, hi: h }
    }
    fn lo_f64(&self) -> f64 { self.lo.to_f64_round(Round::Down) }
    fn hi_f64(&self) -> f64 { self.hi.to_f64_round(Round::Up) }
    fn strictly_positive(&self) -> bool { self.lo > mk(0.0) }
}

fn f_pi() -> Float { Float::with_val(PREC, Constant::Pi) }

// ---------------------------------------------------------------------------
// Point sin / cos with directed rounding
// ---------------------------------------------------------------------------

fn sin_pair(x: f64) -> (Float, Float) {
    let mut l = mk(x); l.sin_round(Round::Down);
    let mut u = mk(x); u.sin_round(Round::Up);
    (l, u)
}

fn cos_pair(x: f64) -> (Float, Float) {
    let mut l = mk(x); l.cos_round(Round::Down);
    let mut u = mk(x); u.cos_round(Round::Up);
    (l, u)
}

fn fold_pair(x: f64, sin: bool, glb: &mut Float, lub: &mut Float) {
    let (l, u) = if sin { sin_pair(x) } else { cos_pair(x) };
    if l < *glb { *glb = l; }
    if u > *lub { *lub = u; }
}

fn fold_one(v: f64, glb: &mut Float, lub: &mut Float) {
    let x = mk(v);
    if x < *glb { *glb = x.clone(); }
    if x > *lub { *lub = x; }
}

/// Rigorous enclosure of sin over [a, b]. Extrema at pi/2 + 2pi k (max 1) and
/// -pi/2 + 2pi k (min -1); fold with a 1e-12 f64 tolerance so the irrational
/// extremum positions can never be missed (spurious folds only widen, which is
/// sound for enclosures).
fn iv_sin(a: f64, b: f64) -> Iv {
    let mut glb = mk(f64::INFINITY);
    let mut lub = mk(f64::NEG_INFINITY);
    fold_pair(a, true, &mut glb, &mut lub);
    fold_pair(b, true, &mut glb, &mut lub);
    let two_pi = 2.0 * PI;
    let kmin = ((a / two_pi).floor() as i64) - 2;
    let kmax = ((b / two_pi).ceil() as i64) + 2;
    for k in kmin..=kmax {
        let p = PI / 2.0 + two_pi * (k as f64);
        if p >= a - 1e-12 && p <= b + 1e-12 { fold_one(1.0, &mut glb, &mut lub); }
        let q = -PI / 2.0 + two_pi * (k as f64);
        if q >= a - 1e-12 && q <= b + 1e-12 { fold_one(-1.0, &mut glb, &mut lub); }
    }
    Iv { lo: glb, hi: lub }
}

/// Rigorous enclosure of cos over [a, b]. Extrema at k*pi with value (-1)^k.
fn iv_cos(a: f64, b: f64) -> Iv {
    let mut glb = mk(f64::INFINITY);
    let mut lub = mk(f64::NEG_INFINITY);
    fold_pair(a, false, &mut glb, &mut lub);
    fold_pair(b, false, &mut glb, &mut lub);
    let kmin = ((a / PI).floor() as i64) - 2;
    let kmax = ((b / PI).ceil() as i64) + 2;
    for k in kmin..=kmax {
        let p = PI * (k as f64);
        if p >= a - 1e-12 && p <= b + 1e-12 {
            if k % 2 == 0 { fold_one(1.0, &mut glb, &mut lub); }
            else { fold_one(-1.0, &mut glb, &mut lub); }
        }
    }
    Iv { lo: glb, hi: lub }
}

// ---------------------------------------------------------------------------
// sinc and its derivatives at points (rigorous, directed rounding)
// ---------------------------------------------------------------------------

/// sinc(x)=sin(x)/x at a point, rigorous (lo, hi).
fn sinc_point(x: f64) -> (Float, Float) {
    if x == 0.0 { return (mk(1.0), mk(1.0)); }
    let ax = mkd(x.abs());
    let ax_up = mku(x.abs());
    let mut n_lo = ax.clone(); n_lo.sin_round(Round::Down);
    let mut n_hi = ax_up.clone(); n_hi.sin_round(Round::Up);
    let q_lo = ddiv(&n_lo, &ax_up);
    let q_hi = udiv(&n_hi, &ax);
    (q_lo, q_hi)
}

/// sinc'(x) = (x cos x - sin x)/x^2 at a point (lo, hi). Odd function.
fn sinc_d1_point(x: f64) -> (Float, Float) {
    if x == 0.0 { return (mk(0.0), mk(0.0)); }
    let ax = mk(x.abs());
    let (c_l, c_u) = cos_pair(x.abs());
    let (s_l, s_u) = sin_pair(x.abs());
    let p_lo = dmul(&ax, &c_l);
    let p_hi = umul(&ax, &c_u);
    let n_lo = dsub(&p_lo, &s_u);
    let n_hi = usub(&p_hi, &s_l);
    let d_lo = dmul(&ax, &ax);
    let d_hi = umul(&ax, &ax);
    let q_lo = ddiv(&n_lo, &d_hi);
    let q_hi = udiv(&n_hi, &d_lo);
    if x < 0.0 {
        (dneg(&q_hi), uneg(&q_lo))
    } else { (q_lo, q_hi) }
}

/// sinc''(x) = ((2-x^2) sin x - 2x cos x)/x^3 at a point (lo, hi). Even
/// function; limit -1/3 at 0.
fn sinc_d2_point(x: f64) -> (Float, Float) {
    if x == 0.0 { return (mkd(-1.0 / 3.0), mku(-1.0 / 3.0)); }
    let ax = mk(x.abs());
    let (c_l, c_u) = cos_pair(x.abs());
    let (s_l, s_u) = sin_pair(x.abs());
    let x2_lo = dmul(&ax, &ax);
    let x2_hi = umul(&ax, &ax);
    let two = mk(2.0);
    let two_minus_x2_lo = dsub(&two, &x2_hi);
    let two_minus_x2_hi = usub(&two, &x2_lo);
    let t1_lo = dmul(&two_minus_x2_lo, &s_l);
    let t1_hi = umul(&two_minus_x2_hi, &s_u);
    let ax2 = dadd(&ax, &ax);
    let t2_lo = dmul(&ax2, &c_l);
    let t2_hi = umul(&ax2, &c_u);
    let n_lo = dsub(&t1_lo, &t2_hi);
    let n_hi = usub(&t1_hi, &t2_lo);
    let x3_lo = dmul(&x2_lo, &ax);
    let x3_hi = umul(&x2_hi, &ax);
    let q_lo = ddiv(&n_lo, &x3_hi);
    let q_hi = udiv(&n_hi, &x3_lo);
    (q_lo, q_hi)
}

// ---------------------------------------------------------------------------
// sinc', sinc'' enclosures over an interval (for the second-derivative table)
// ---------------------------------------------------------------------------

const DELTA: f64 = 0.02;

/// Taylor enclosures for |x| <= DELTA (rigorous, alternating series with tiny
/// tails; error bound 1e-24 is a very safe overestimate of the tail).
/// sinc'(x) = -x/3 + x^3/30 - x^5/840 + x^7/45360 - x^9/3991680 + ...
fn taylor_d1(x: f64) -> (Float, Float) {
    let err = 1e-24;
    let x2f = mk(x * x);
    let c3 = mkd(1.0 / 45360.0);
    let c2 = mkd(-1.0 / 840.0);
    let c1 = mkd(1.0 / 30.0);
    let c0 = mkd(-1.0 / 3.0);
    let c3u = mku(1.0 / 45360.0);
    let c2u = mku(-1.0 / 840.0);
    let c1u = mku(1.0 / 30.0);
    let c0u = mku(-1.0 / 3.0);
    let xf = mk(x);
    // lo: Horner with downward rounding
    let mut r = mkd(-1.0 / 3991680.0);
    r = dadd(&dmul(&r, &x2f), &c3);
    r = dadd(&dmul(&r, &x2f), &c2);
    r = dadd(&dmul(&r, &x2f), &c1);
    r = dadd(&dmul(&r, &x2f), &c0);
    let lo = dsub(&dmul(&r, &xf), &mk(err));
    // hi: Horner with upward rounding
    let mut r = mku(-1.0 / 3991680.0);
    r = uadd(&umul(&r, &x2f), &c3u);
    r = uadd(&umul(&r, &x2f), &c2u);
    r = uadd(&umul(&r, &x2f), &c1u);
    r = uadd(&umul(&r, &x2f), &c0u);
    let hi = uadd(&umul(&r, &xf), &mk(err));
    (lo, hi)
}

/// sinc''(x) = -1/3 + x^2/10 - x^4/168 + x^6/6480 - x^8/443520 + ... (even)
fn taylor_d2(x: f64) -> (Float, Float) {
    let err = 1e-24;
    let x2f = mk(x * x);
    let c3 = mkd(1.0 / 6480.0);
    let c2 = mkd(-1.0 / 168.0);
    let c1 = mkd(1.0 / 10.0);
    let c0 = mkd(-1.0 / 3.0);
    let c3u = mku(1.0 / 6480.0);
    let c2u = mku(-1.0 / 168.0);
    let c1u = mku(1.0 / 10.0);
    let c0u = mku(-1.0 / 3.0);
    let mut r = mkd(-1.0 / 443520.0);
    r = dadd(&dmul(&r, &x2f), &c3);
    r = dadd(&dmul(&r, &x2f), &c2);
    r = dadd(&dmul(&r, &x2f), &c1);
    let lo = dsub(&dadd(&dmul(&r, &x2f), &c0), &mk(err));
    let mut r = mku(-1.0 / 443520.0);
    r = uadd(&umul(&r, &x2f), &c3u);
    r = uadd(&umul(&r, &x2f), &c2u);
    r = uadd(&umul(&r, &x2f), &c1u);
    let hi = uadd(&uadd(&umul(&r, &x2f), &c0u), &mk(err));
    (lo, hi)
}

/// Enclosure of sinc' over [a, b] (a <= b). Taylor branch near 0, otherwise
/// closed form (z cos z - sin z)/z^2 in interval arithmetic.
fn sinc_d1_iv(a: f64, b: f64) -> Iv {
    if a >= -DELTA && b <= DELTA {
        let (la, ha) = if a.abs() <= DELTA { taylor_d1(a) } else { sinc_d1_point(a) };
        let (lb, hb) = if b.abs() <= DELTA { taylor_d1(b) } else { sinc_d1_point(b) };
        let mut glb = la; let mut lub = ha;
        if lb < glb { glb = lb; }
        if hb > lub { lub = hb; }
        if a <= 0.0 && b >= 0.0 { fold_one(0.0, &mut glb, &mut lub); }
        return Iv { lo: glb, hi: lub };
    }
    let z = Iv { lo: mkd(a), hi: mku(b) };
    let cos = iv_cos(a, b);
    let sin = iv_sin(a, b);
    num_div_den(&z.mul(&cos).sub(&sin), &z.mul(&z))
}

/// Enclosure of sinc'' over [a, b], Taylor branch near 0, otherwise closed
/// form ((2-z^2) sin z - 2 z cos z)/z^3.
fn sinc_d2_iv(a: f64, b: f64) -> Iv {
    if a >= -DELTA && b <= DELTA {
        let (la, ha) = taylor_d2(a);
        let (lb, hb) = taylor_d2(b);
        let mut glb = la; let mut lub = ha;
        if lb < glb { glb = lb; }
        if hb > lub { lub = hb; }
        if a <= 0.0 && b >= 0.0 {
            let (l0, h0) = sinc_d2_point(0.0);
            if l0 < glb { glb = l0; }
            if h0 > lub { lub = h0; }
        }
        return Iv { lo: glb, hi: lub };
    }
    let z = Iv { lo: mkd(a), hi: mku(b) };
    let sin = iv_sin(a, b);
    let cos = iv_cos(a, b);
    let two = Iv::point(2.0);
    let z2 = z.mul(&z);
    let t1 = two.sub(&z2).mul(&sin);
    let t2 = z.mul(&cos).mul(&two);
    num_div_den(&t1.sub(&t2), &z2.mul(&z))
}

fn num_div_den(n: &Iv, d: &Iv) -> Iv { n.div(d) }

// ---------------------------------------------------------------------------
// sinc with rigorous enclosure over an interval (value only)
// ---------------------------------------------------------------------------

/// k-th positive root of x = tan x (k >= 1). Bracket k*pi < r < k*pi + pi/2.
fn tan_root(k: u64) -> f64 {
    let mut lo = k as f64 * PI;
    let mut hi = lo + PI / 2.0;
    for _ in 0..300 {
        let mid = (lo + hi) / 2.0;
        let f = mid - mid.tan();
        if f > 0.0 { lo = mid; } else { hi = mid; }
    }
    (lo + hi) / 2.0
}

/// Rigorous enclosure of sinc over [a, b]. Endpoints plus interior extrema at
/// the roots of x = tan x, which bracket the local extrema of sinc.
fn sinc_iv(a: f64, b: f64) -> Iv {
    let mut glb = mk(f64::INFINITY);
    let mut lub = mk(f64::NEG_INFINITY);
    let (la, ha) = sinc_point(a); let (lb, hb) = sinc_point(b);
    if la < glb { glb = la; } if ha > lub { lub = ha; }
    if lb < glb { glb = lb; } if hb > lub { lub = hb; }
    let m = a.abs().max(b.abs());
    let lo_inner = a.abs().min(b.abs());
    let mut k: u64 = 1;
    loop {
        let r = tan_root(k);
        if r > m { break; }
        if r >= lo_inner {
            let (lr, hr) = sinc_point(r);
            if lr < glb { glb = lr; }
            if hr > lub { lub = hr; }
        }
        k += 1;
    }
    if a <= 0.0 && b >= 0.0 {
        if mk(1.0) > lub { lub = mk(1.0); }
    }
    Iv { lo: glb, hi: lub }
}

// ---------------------------------------------------------------------------
// Cosine kernel
// ---------------------------------------------------------------------------

#[derive(Clone)]
struct CosineKernel {
    alpha: f64,
    alpha_iv: Iv,
    k0: f64,
    k0_iv: Iv,
    k0sq_iv: Iv,
    pi_iv: Iv,
    two_pi: Iv,
    half: Iv,
    half_pi: Iv,
    two: Iv,
}

struct CellBounds {
    w_lower: f64,
    first_lower: f64,
    first_upper: f64,
    second_lower: f64,
    second_upper: f64,
}

struct KernelDerivsCell {
    k: Iv,
    k1: Iv,
    k2: Iv,
}

impl CosineKernel {
    fn new(alpha: f64) -> CosineKernel {
        let (l, u) = sinc_point(alpha / 2.0);
        let k0 = (l.to_f64_round(Round::Down) + u.to_f64_round(Round::Up)) / 2.0;
        let k0_iv = Iv { lo: l, hi: u };
        let k0sq_iv = k0_iv.mul(&k0_iv);
        // Kernel-invariant constants, built once; bit-identical to the
        // per-call constructions they replace.
        let pi_iv = Iv { lo: Float::with_val_round(PREC, Constant::Pi, Round::Down).0,
                         hi: Float::with_val_round(PREC, Constant::Pi, Round::Up).0 };
        let two_pi = Iv { lo: mkd(2.0 * PI), hi: mku(2.0 * PI) };
        let half = Iv::point(0.5);
        let half_pi = pi_iv.mul(&half);
        let two = Iv::point(2.0);
        CosineKernel { alpha, alpha_iv: Iv { lo: mkd(alpha), hi: mku(alpha) },
                       k0, k0_iv, k0sq_iv, pi_iv, two_pi, half, half_pi, two }
    }
    /// Enclosure of K on cell [i/grid, (i+1)/grid].
    fn k_on_cell(&self, index: i64, grid: i64) -> Iv {
        let cl = index as f64 / grid as f64;
        let ch = (index as f64 + 1.0) / grid as f64;
        // a(x) = (alpha - 2 pi x)/2 decreasing; b(x) = (alpha + 2 pi x)/2 increasing
        let a_lo = (self.alpha - 2.0 * PI * ch) / 2.0;
        let a_hi = (self.alpha - 2.0 * PI * cl) / 2.0;
        let b_lo = (self.alpha + 2.0 * PI * cl) / 2.0;
        let b_hi = (self.alpha + 2.0 * PI * ch) / 2.0;
        let sa = sinc_iv(a_lo.min(a_hi), a_lo.max(a_hi));
        let sb = sinc_iv(b_lo.min(b_hi), b_lo.max(b_hi));
        let half = &mk(0.5);
        Iv {
            lo: dmul(&dadd(&sa.lo, &sb.lo), half),
            hi: umul(&uadd(&sa.hi, &sb.hi), half),
        }
    }
    /// (K, K', K'') enclosures over a cell (single cosine coefficient).
    fn k_derivs_on_cell(&self, index: i64, grid: i64) -> KernelDerivsCell {
        let cl = index as f64 / grid as f64;
        let ch = (index as f64 + 1.0) / grid as f64;
        let pi_iv = &self.pi_iv;
        let a_lo = (self.alpha - 2.0 * PI * ch) / 2.0;
        let a_hi = (self.alpha - 2.0 * PI * cl) / 2.0;
        let b_lo = (self.alpha + 2.0 * PI * cl) / 2.0;
        let b_hi = (self.alpha + 2.0 * PI * ch) / 2.0;
        let (zmlo, zmhi) = (a_lo.min(a_hi), a_lo.max(a_hi));
        let (zplo, zphi) = (b_lo.min(b_hi), b_lo.max(b_hi));
        let sa = sinc_iv(zmlo, zmhi);
        let sb = sinc_iv(zplo, zphi);
        let half = &mk(0.5);
        let k = Iv {
            lo: dmul(&dadd(&sa.lo, &sb.lo), half),
            hi: umul(&uadd(&sa.hi, &sb.hi), half),
        };
        let d1m = sinc_d1_iv(zmlo, zmhi);
        let d1p = sinc_d1_iv(zplo, zphi);
        let d2m = sinc_d2_iv(zmlo, zmhi);
        let d2p = sinc_d2_iv(zplo, zphi);
        // k1 = pi/2 * (d1(z+) - d1(z-)); k2 = pi^2/2 * (d2(z-) + d2(z+))
        let half_pi = pi_iv.mul(&Iv::point(0.5));
        let k1 = d1p.sub(&d1m).mul(&half_pi);
        let pi2 = pi_iv.mul(&pi_iv);
        let k2 = d2m.add(&d2p).mul(&pi2).mul(&Iv::point(0.5));
        KernelDerivsCell { k, k1, k2 }
    }
    /// Rigorous lower bound of w = (K/K0)^2 on cell index, as f64 (nextafter down).
    fn w_lower_on_cell(&self, index: i64, grid: i64) -> f64 {
        let k = self.k_on_cell(index, grid);
        let k_abs = k.abs();
        let ratio_lo = ddiv(&k_abs.lo, &mk(self.k0));
        let w = dmul(&ratio_lo, &ratio_lo);
        w.to_f64_round(Round::Down).next_down()
    }
    /// Rigorous lower bound of w'' = ((K/K0)^2)'' on cell index.
    /// w'' = 2*(k1^2 + k*k2)/k0^2, all in interval arithmetic.
    fn w_second_lower_on_cell(&self, index: i64, grid: i64) -> f64 {
        let d = self.k_derivs_on_cell(index, grid);
        let k1sq = d.k1.mul(&d.k1);
        let kk2 = d.k.mul(&d.k2);
        let num = k1sq.add(&kk2);
        let num2 = num.mul(&Iv::point(2.0));
        let ratio = num2.div(&self.k0sq_iv);
        let lo = ratio.lo_f64();
        if !lo.is_finite() { return f64::NEG_INFINITY; }
        lo.next_down()
    }
    /// Rigorous cell bounds for w, w', and w''. All returned f64 values have
    /// already been rounded outward in the direction needed by the caller.
    fn cell_bounds(&self, index: i64, grid: i64) -> CellBounds {
        let d = self.k_derivs_on_cell(index, grid);
        let k_abs = d.k.abs();
        let ratio_lo = ddiv(&k_abs.lo, &mk(self.k0));
        let w = dmul(&ratio_lo, &ratio_lo);
        let first = d.k.mul(&d.k1).mul(&self.two).div(&self.k0sq_iv);
        let second = d.k1.mul(&d.k1).add(&d.k.mul(&d.k2))
            .mul(&self.two).div(&self.k0sq_iv);
        CellBounds {
            w_lower: w.to_f64_round(Round::Down).next_down(),
            first_lower: first.lo.to_f64_round(Round::Down).next_down(),
            first_upper: first.hi.to_f64_round(Round::Up).next_up(),
            second_lower: second.lo.to_f64_round(Round::Down).next_down(),
            second_upper: second.hi.to_f64_round(Round::Up).next_up(),
        }
    }
    /// Rigorous value/first derivative of w = (K/K0)^2 at a POINT x. Returns
    /// (potential, first_deriv) enclosures. No caller uses the second
    /// derivative (tangent_lower destructures the third element as `_`), so it
    /// is not computed; the returned values are produced by exactly the same
    /// outward-rounded expressions as before.
    fn squared_kernel_derivs_point(&self, x: &Iv) -> (Iv, Iv) {
        let two_pi_x = x.mul(&self.two_pi);
        let zm = self.alpha_iv.sub(&two_pi_x).mul(&self.half);
        let zp = self.alpha_iv.add(&two_pi_x).mul(&self.half);
        // Point evaluations of sinc, sinc' at the (near-point) z's.
        // The z's are obtained from f64 projections, so the true point sits
        // within ~2^-52 of zc; |d/dz| of sinc/sinc' on |z|<=60 is bounded by
        // ~3e3, so a widening of 1e-8 is a very safe Lipschitz correction
        // that keeps the enclosure valid.
        let widen = 1e-8;
        let point_ivs = |z: &Iv| -> (Iv, Iv) {
            let zlo = z.lo_f64(); let zhi = z.hi_f64();
            let zc = (zlo + zhi) / 2.0;
            let (vl, vh) = sinc_point(zc);
            let (d1l, d1h) = sinc_d1_point(zc);
            (Iv { lo: dadd(&vl, &mk(-widen)), hi: uadd(&vh, &mk(widen)) },
             Iv { lo: dadd(&d1l, &mk(-widen)), hi: uadd(&d1h, &mk(widen)) })
        };
        let (vm, d1m) = point_ivs(&zm);
        let (vp, d1p) = point_ivs(&zp);
        let k = Iv {
            lo: dmul(&dadd(&vm.lo, &vp.lo), &self.half.lo),
            hi: umul(&uadd(&vm.hi, &vp.hi), &self.half.hi),
        };
        let k1 = d1p.sub(&d1m).mul(&self.half_pi);
        let k0sq = &self.k0sq_iv;
        let pot = k.mul(&k).div(k0sq);
        let first = k.mul(&k1).mul(&self.two).div(k0sq);
        (pot, first)
    }
}

// ---------------------------------------------------------------------------
// RangeMinimum sparse table
// ---------------------------------------------------------------------------

struct RangeMinimum {
    levels: Vec<Vec<f64>>,
    length: usize,
}

impl RangeMinimum {
    fn new(values: &[f64]) -> RangeMinimum {
        let length = values.len();
        let mut levels = vec![values.to_vec()];
        let mut k = 1;
        loop {
            let prev = &levels[k - 1];
            let width = 1 << k;
            if width > length { break; }
            let mut row = Vec::with_capacity(length - width + 1);
            for i in 0..(length - width + 1) {
                row.push(prev[i].min(prev[i + (width >> 1)]));
            }
            levels.push(row);
            k += 1;
        }
        RangeMinimum { levels, length }
    }
    fn query(&self, left: usize, right: usize) -> f64 {
        if right < left || right >= self.length { return f64::INFINITY; }
        let level = (right - left + 1).ilog2() as usize;
        let width = 1 << level;
        let row = &self.levels[level];
        row[left].min(row[right - width + 1])
    }
}

struct RangeMaximum {
    levels: Vec<Vec<f64>>,
    length: usize,
}

impl RangeMaximum {
    fn new(values: &[f64]) -> RangeMaximum {
        let length = values.len();
        let mut levels = vec![values.to_vec()];
        let mut k = 1;
        loop {
            let prev = &levels[k - 1];
            let width = 1 << k;
            if width > length { break; }
            let mut row = Vec::with_capacity(length - width + 1);
            for i in 0..(length - width + 1) {
                row.push(prev[i].max(prev[i + (width >> 1)]));
            }
            levels.push(row);
            k += 1;
        }
        RangeMaximum { levels, length }
    }
    fn query(&self, left: usize, right: usize) -> f64 {
        if right < left || right >= self.length { return f64::NEG_INFINITY; }
        let level = (right - left + 1).ilog2() as usize;
        let width = 1 << level;
        let row = &self.levels[level];
        row[left].max(row[right - width + 1])
    }
}

fn next_down(v: f64) -> f64 { v.next_down() }
fn next_up(v: f64) -> f64 { v.next_up() }

// ---------------------------------------------------------------------------
// Branch-and-bound verifier
// ---------------------------------------------------------------------------

#[derive(Clone)]
struct BBox { coords: Vec<(i64, i64)> }

fn sum_firsts(b: &BBox) -> i64 { b.coords.iter().map(|&(l, _)| l).sum() }

/// Interval LDL (mirror of Python _arb_ldl_positive). Returns true iff all
/// pivots are certified strictly positive. Matrix entries are point intervals
/// built from the (lower-bound) scalars; every operation is outward-rounded,
/// so a true return certifies positive-definiteness of the minorant matrix.
/// Interval LDL (mirror of Python _arb_ldl_positive). Returned for possible
/// reuse; NOTE it is NOT a sound PD certificate (see hessian_pd_gershgorin in
/// block.rs — Python proved the entrywise-lower-bound LDL can be PD while the
/// true Hessian is indefinite), so it must not be used to license a tangent
/// prune. Retained only as dead reference; remove if it rots.
#[allow(dead_code)]
fn ldl_positive(matrix: &[Vec<Iv>], q: usize) -> bool {
    let mut lower = vec![vec![Iv::point(0.0); q]; q];
    let mut diagonal = vec![Iv::point(0.0); q];
    for column in 0..q {
        lower[column][column] = Iv::point(1.0);
        let mut pivot = matrix[column][column].clone();
        for prev in 0..column {
            let lcp = lower[column][prev].clone();
            let term = lcp.mul(&lcp).mul(&diagonal[prev]);
            pivot = pivot.sub(&term);
        }
        if !pivot.strictly_positive() { return false; }
        diagonal[column] = pivot.clone();
        for row in (column + 1)..q {
            let mut value = matrix[row][column].clone();
            for prev in 0..column {
                let lrp = lower[row][prev].clone();
                let lcp = lower[column][prev].clone();
                let term = lrp.mul(&lcp).mul(&diagonal[prev]);
                value = value.sub(&term);
            }
            lower[row][column] = value.div(&pivot);
        }
    }
    true
}

include!("block.rs");

fn run_case(name: &str, alpha: f64, pressure: f64, target: f64, lambda: f64,
            p_raw: &[f64], q_raw: &[f64], use_tangent: bool) {
    let mut weights = HashMap::new();
    // 7 points, indices 0..=6 inclusive (FIX: was 0..q / 0..q in old code)
    for i in 0..7i64 {
        for j in (i + 1)..7i64 {
            weights.insert((i as usize, j as usize), 2.0 / (7.0 - (j - i) as f64));
        }
    }
    let p_coeff: Vec<f64> = p_raw.iter().map(|c| lambda * c / 1_920_000.0).collect();
    let q_coeff: Vec<f64> = q_raw.iter().map(|c| lambda * c).collect();
    let r = verify_floor(alpha, &weights, pressure, 6, target, 4000,
                         "coboundary", Some(&p_coeff), Some(&q_coeff),
                         Some(std::env::var("VRS_MAX_NODES").ok().and_then(|s| s.parse().ok()).unwrap_or(8_000_000)), use_tangent);
    println!("CASE {name}: {r}");
    let line = format!("CASE {name}: {r}\n");
    std::fs::OpenOptions::new().create(true).append(true)
        .open("/tmp/verifier-rs-status.md")
        .and_then(|mut f| { use std::io::Write; f.write_all(line.as_bytes()) })
        .ok();
}

/// Microbenchmark for the tangent hot path: rigorous (pot, first) point
/// evaluation of w=(K/K0)^2. Gated behind VRS_BENCH_POINT; never runs in
/// certification mode.
fn bench_point_eval() {
    let kernel = CosineKernel::new(1.464);
    let iters: u64 = std::env::var("VRS_BENCH_ITERS").ok()
        .and_then(|s| s.parse().ok()).unwrap_or(200_000);
    // representative midpoint-sum points |x| in [0.13, 0.92], like sums of
    // 1..6 consecutive board midpoints in the active band
    let mut acc: u64 = 0;
    let t0 = std::time::Instant::now();
    for i in 0..iters {
        let xv = 0.13 + 0.79 * ((i % 61) as f64) / 60.0;
        let x = Iv::point(xv);
        let (pot, first) = kernel.squared_kernel_derivs_point(&x);
        acc = acc.wrapping_add(pot.lo_f64() as i64 as u64);
        acc = acc.wrapping_add(first.hi_f64() as i64 as u64);
    }
    let dt = t0.elapsed().as_secs_f64();
    println!("BENCH point_eval: {iters} iters in {dt:.4}s = {:.2} ns/op (acc={acc})",
             dt * 1e9 / iters as f64);
}

fn build_weights(span1_mode: &str) -> HashMap<(usize, usize), f64> {
    let mut w = HashMap::new();
    for i in 0..7i64 {
        for j in (i + 1)..7i64 {
            let span = j - i;
            if span1_mode == "replaced" && span == 1 { continue; }
            w.insert((i as usize, j as usize), 2.0 / (7.0 - span as f64));
        }
    }
    w
}

/// HARD mass conditions (ledger 2026-08-24 final): |sum q - 2| < 1e-9 AND every
/// present span keeps its design mass (2). Refuses to run otherwise — makes the
/// launcher-encoding bug class unrepresentable (a mangled P/Q vector or a bad
/// span1_mode flips at least one of these before any node is spent).
fn assert_mass_conditions(q_coeff: &[f64], span1_mode: &str) -> Result<(), String> {
    let sum_q: f64 = q_coeff.iter().sum();
    if (sum_q - 2.0).abs() > 1e-9 {
        return Err(format!(
            "MASS-FAIL: |sum q - 2| = {:.3e} > 1e-9 (sum q = {:.17}); refusing to run",
            (sum_q - 2.0).abs(), sum_q));
    }
    let w = build_weights(span1_mode);
    for span in 1..=6i64 {
        let design: f64 = if span1_mode == "replaced" && span == 1 { 0.0 } else { 2.0 };
        let mass: f64 = w.iter().filter(|((i, j), _)| (*j - *i) as i64 == span)
            .map(|(_, v)| *v).sum();
        if (mass - design).abs() > 1e-9 {
            return Err(format!(
                "MASS-FAIL: span {span} mass {mass} != design {design} (mode={span1_mode}); refusing to run"));
        }
    }
    Ok(())
}

fn print_params(alpha: f64, target: f64, grid: i64, max_nodes: u64, span1_mode: &str,
                lam: f64, p_raw: &[f64], q_raw: &[f64], p_coeff: &[f64], q_coeff: &[f64]) {
    println!("--- verifier-rs candidate (self-describing) ---");
    println!("alpha      = {:.17}", alpha);
    println!("target     = {:.17}", target);
    println!("grid       = {grid}");
    println!("max_nodes  = {max_nodes}");
    println!("span1_mode = {span1_mode}   (added = F_V, replaced = F_T)");
    println!("lambda     = {:.17}", lam);
    for i in 0..q_raw.len() {
        println!("p_raw[{i}] = {:.17}", p_raw[i]);
    }
    for i in 0..q_raw.len() {
        println!("q_raw[{i}] = {:.17}", q_raw[i]);
    }
    for i in 0..p_coeff.len() {
        println!("p_coeff[{i}] = {:.17}", p_coeff[i]);
    }
    for i in 0..q_coeff.len() {
        println!("q_coeff[{i}] = {:.17}", q_coeff[i]);
    }
    let sum_p: f64 = p_coeff.iter().sum();
    let sum_q: f64 = q_coeff.iter().sum();
    println!("sum p = {:.17}   sum q = {:.17}", sum_p, sum_q);
    println!("--- end candidate ---");
}

/// Verify one coboundary candidate. Runs self-describing echo, mass assertions,
/// then the B&B; returns the raw status line "{"verified": ...}".
fn verify_one(alpha: f64, target: f64, grid: i64, max_nodes: u64, span1_mode: &str,
              lam: f64, p_raw: &[f64], q_raw: &[f64],
              p_coeff: &[f64], q_coeff: &[f64], use_tangent: bool) -> String {
    if let Err(e) = assert_mass_conditions(q_coeff, span1_mode) {
        eprintln!("{e}");
        std::process::exit(2);
    }
    print_params(alpha, target, grid, max_nodes, span1_mode, lam, p_raw, q_raw, p_coeff, q_coeff);
    let weights = build_weights(span1_mode);
    verify_floor(alpha, &weights, 1.0 / 3000.0, 6, target, grid, "coboundary",
                 Some(p_coeff), Some(q_coeff), Some(max_nodes), use_tangent)
}

/// Record-chain bound, port of cert-floor-rs::joint_bound/record_chain
/// (tawanerguo chain: bound = (H(alpha) - tau)/(1 - B/m), q=6). Returns
/// (best_bound, argmax_m) over m in [m0, m1]. Honesty: f64 FLOAT-PROBE of the
/// chain only; the floor certification lives in verify_one above.
fn record_chain_bound(alpha: f64, eps: f64, psum: f64, m0: f64, m1: f64) -> (f64, f64) {
    let a = alpha;
    let i0 = 2.0 * (a / 2.0).sin() / a;
    let i2 = 0.5 + a.sin() / (2.0 * a);
    let c_const = (a / 2.0).sin() / a + 2.0 * (a / 2.0).cos() / (a * a);
    let jv = -2.0 * i2 / (a * a) + c_const * i0;
    let c = i0 * i0 / (i2 + jv);
    let h = 2.0 - 1.0 / c;
    let phi_m = |am: f64, mm: f64| -> f64 {
        if am <= mm / (mm - 1.0) { am }
        else { 2.0 * ((mm - 1.0) * am / mm).sqrt() - 1.0 + am / mm }
    };
    let mut best = (f64::NEG_INFINITY, 0.0f64);
    let mut m = m0;
    while m <= m1 + 1e-9 {
        let bm = phi_m(eps * (m - 6.0), m);
        let tau = psum * (m - 6.0) / m;
        let bound = (h - tau) / (1.0 - bm / m);
        if bound > best.0 { best = (bound, m); }
        m += 1.0;
    }
    (best.0, best.1)
}

fn floor_pipeline(args: &[String]) {
    // floor-pipeline <alpha> <target> <p1 p2 p3 p4 p5 p6> <q1 q2 q3 q4 q5 q6>
    //              [--spans added|replaced] [--grid N] [--max-nodes N] [--chain-m0 N] [--chain-m1 N]
    if args.len() < 14 {
        eprintln!("usage: verifier-rs floor-pipeline <alpha> <target> <p1..p6> <q1..q6> [--spans added|replaced] [--grid N] [--max-nodes N] [--chain-m0 N] [--chain-m1 N]");
        std::process::exit(2);
    }
    let alpha: f64 = args[0].parse().expect("alpha");
    let target: f64 = args[1].parse().expect("target");
    let p_raw: Vec<f64> = args[2..8].iter().map(|s| s.parse().expect("p")).collect();
    let q_raw: Vec<f64> = args[8..14].iter().map(|s| s.parse().expect("q")).collect();
    let mut span1_mode = "added";
    let mut grid: i64 = 4000;
    let mut max_nodes: u64 = 8_000_000;
    let mut m0 = 40.0;
    let mut m1 = 600.0;
    let mut i = 14;
    while i < args.len() {
        match args[i].as_str() {
            "--spans" => { span1_mode = &args[i + 1]; i += 2; }
            "--grid" => { grid = args[i + 1].parse().expect("grid"); i += 2; }
            "--max-nodes" => { max_nodes = args[i + 1].parse().expect("max-nodes"); i += 2; }
            "--chain-m0" => { m0 = args[i + 1].parse().expect("m0"); i += 2; }
            "--chain-m1" => { m1 = args[i + 1].parse().expect("m1"); i += 2; }
            _ => { eprintln!("unknown flag {}", args[i]); std::process::exit(2); }
        }
    }
    let lam = 1.0; // floor-pipeline takes final (lambda-applied) p/q by design
    let p_coeff: Vec<f64> = p_raw.iter().map(|c| lam * c / 1_920_000.0).collect();
    let q_coeff: Vec<f64> = q_raw.iter().map(|c| lam * c).collect();
    let use_tangent = std::env::var("VRS_NO_TANGENT").is_err();
    let r = verify_one(alpha, target, grid, max_nodes, span1_mode, lam,
                       &p_raw, &q_raw, &p_coeff, &q_coeff, use_tangent);
    println!("VERIFY_RESULT {r}");
    let verified = r.contains("\"verified\": True");
    let psum: f64 = p_coeff.iter().sum(); // = sum P_raw / 1920000 (tau through tau)
    let (bound, best_m) = record_chain_bound(alpha, target, psum, m0, m1);
    println!("CHAIN_BOUND {bound:.17} (argmax m = {best_m:.0}, psum = {psum:.17}, H(alpha) chain)");
    println!("PIPELINE_VERDICT: {}   (verify={} bound={:.17})",
             if verified { "PASS" } else { "FAIL" }, if verified { "true" } else { "false" }, bound);
}

fn main() {
    if std::env::var("VRS_BENCH_POINT").is_ok() {
        bench_point_eval();
        return;
    }
    let args: Vec<String> = std::env::args().collect();
    // floor-pipeline subcommand: candidate -> verify -> chain bound -> verdict
    if args.len() >= 2 && args[1] == "floor-pipeline" {
        floor_pipeline(&args[2..]);
        return;
    }
    let use_tangent = std::env::var("VRS_NO_TANGENT").is_err();
    println!("use_tangent={use_tangent}");

    // Env-parameterized mode (python-verifier-compatible driver): VERIFY_ALPHA +
    // VERIFY_TARGET + optional VERIFY_LAMBDA/VERIFY_GRID/VERIFY_MAX_NODES/
    // VERIFY_SPAN1_MODE/VERIFY_P1..P6/VERIFY_Q1..Q6.
    if std::env::var("VERIFY_TARGET").is_ok() && std::env::var("VERIFY_ALPHA").is_ok() {
        let alpha: f64 = std::env::var("VERIFY_ALPHA").unwrap().parse().expect("VERIFY_ALPHA");
        let target: f64 = std::env::var("VERIFY_TARGET").unwrap().parse().expect("VERIFY_TARGET");
        let grid: i64 = std::env::var("VERIFY_GRID").ok().and_then(|s| s.parse().ok()).unwrap_or(4000);
        let max_nodes: u64 = std::env::var("VERIFY_MAX_NODES").ok().and_then(|s| s.parse().ok()).unwrap_or(8_000_000);
        let lam: f64 = std::env::var("VERIFY_LAMBDA").ok().and_then(|s| s.parse().ok()).unwrap_or(1.0);
        let span1_mode = std::env::var("VERIFY_SPAN1_MODE").unwrap_or_else(|_| "added".to_string());
        let p_raw: Vec<f64> = (1..=6).map(|i| std::env::var(format!("VERIFY_P{i}")).ok()
            .map(|s| s.parse().unwrap_or(0.0)).unwrap_or(0.0)).collect();
        let q_raw: Vec<f64> = (1..=6).map(|i| std::env::var(format!("VERIFY_Q{i}")).ok()
            .map(|s| s.parse().unwrap_or(0.0)).unwrap_or(0.0)).collect();
        let p_coeff: Vec<f64> = p_raw.iter().map(|c| lam * c / 1_920_000.0).collect();
        let q_coeff: Vec<f64> = q_raw.iter().map(|c| lam * c).collect();
        let r = verify_one(alpha, target, grid, max_nodes, &span1_mode, lam,
                           &p_raw, &q_raw, &p_coeff, &q_coeff, use_tangent);
        let psum: f64 = p_coeff.iter().sum();
        let (bound, best_m) = record_chain_bound(alpha, target, psum, 40.0, 600.0);
        println!("VERIFY_RESULT {r}");
        println!("CHAIN_BOUND {bound:.17} (argmax m = {best_m:.0}, psum = {psum:.17})");
        return;
    }

    // Legacy builtin acceptance cases (F_V, span1=added, matches prior behavior).
    if let Some(s) = std::env::var("VRS_SELF_DESCRIBE").ok() {
        if s == "1" { println!("note: legacy cases use span1_mode=added (F_V)"); }
    }
    let p_raw: [f64; 6] = [946.0, 1177.0, 877.0, 877.0, 1177.0, 946.0];
    let q_raw: [f64; 6] = [31343.0 / 100000.0, 1.0 / 3.0, 105971.0 / 300000.0,
                           105971.0 / 300000.0, 1.0 / 3.0, 31343.0 / 100000.0];
    let selected = std::env::var("VRS_CASE").ok();
    if selected.as_deref().map_or(true, |s| s == "A") { run_case("A", 1.464, 1.0 / 3000.0, 0.0062, 1.0, &p_raw, &q_raw, use_tangent); }
    if selected.as_deref().map_or(true, |s| s == "B") { run_case("B", 1.464, 1.0 / 3000.0, 0.0063, 1.0, &p_raw, &q_raw, use_tangent); }
    if selected.as_deref().map_or(true, |s| s == "C") { run_case("C", 1.464, 1.10 / 3000.0, 0.0066774, 1.10, &p_raw, &q_raw, use_tangent); }
    if selected.as_deref().map_or(true, |s| s == "D") { run_case("D", 1.464, 1.0 / 3000.0, 0.00698, 1.15, &p_raw, &q_raw, use_tangent); }
}
