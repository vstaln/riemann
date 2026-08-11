// Euler–Maclaurin evaluation of L(1/2+it, chi) via Hurwitz zeta, and the
// real function Z_chi(t) whose sign changes locate the zeros on the critical line.
// All f64. Verified internally against the functional equation and RvM counts.

use crate::characters::Character;
use std::f64::consts::PI;

pub fn bernoulli(n: usize) -> f64 {
    match n {
        2 => 1.0 / 6.0,
        4 => -1.0 / 30.0,
        6 => 1.0 / 42.0,
        8 => -1.0 / 30.0,
        10 => 5.0 / 66.0,
        12 => -691.0 / 2730.0,
        14 => 7.0 / 6.0,
        16 => -3617.0 / 510.0,
        18 => 43867.0 / 798.0,
        20 => -174611.0 / 330.0,
        22 => 854513.0 / 138.0,
        24 => -236364091.0 / 2730.0,
        26 => 8553103.0 / 6.0,
        28 => -23749461029.0 / 870.0,
        30 => 8615841276005.0 / 14322.0,
        _ => 0.0,
    }
}

/// Hurwitz zeta zeta(s, x) with s = re + i*im, x in (0,1]. Euler–Maclaurin.
/// N = main-sum cutoff (chosen ~2|t|/2pi), K = number of Bernoulli terms.
pub fn hurwitz_zeta(re: f64, im: f64, x: f64) -> (f64, f64) {
    let two_pi = std::f64::consts::TAU;
    let n = ((2.0 * im.abs() / two_pi).ceil() as usize).max(20) + 10;
    let k_max = 14;
    let mut sr = 0.0f64;
    let mut si = 0.0f64;
    // main sum: sum_{m=0}^{n-1} (m+x)^{-s}
    for m in 0..n {
        let a = m as f64 + x;
        let ln = a.ln();
        let mag = a.powf(-re);
        let (s, c) = (im * ln).sin_cos();
        // a^{-s} = a^{-re} e^{-i im ln a}
        sr += mag * c;
        si += -mag * s;
    }
    // (N+x)^{1-s}/(s-1)
    let a = n as f64 + x;
    let ln_a = a.ln();
    let m1 = a.powf(1.0 - re); // |(N+x)^{1-s}|
    let (s1, c1) = (im * ln_a).sin_cos();
    let num_re = m1 * c1;
    let num_im = -m1 * s1;
    let den_re = re - 1.0;
    let den_im = im;
    let d2 = den_re * den_re + den_im * den_im;
    sr += (num_re * den_re + num_im * den_im) / d2;
    si += (num_im * den_re - num_re * den_im) / d2;
    // (1/2)(N+x)^{-s}
    let m2 = 0.5 * a.powf(-re);
    sr += m2 * c1;
    si += -m2 * s1;
    // Bernoulli terms: sum_{k=1}^{K} B_{2k}/(2k)! (s)_{2k-1} (N+x)^{-s-2k+1}
    // (s)_{j} = prod_{l=0}^{j-1} (s+l); accumulate rising factorial incrementally.
    // (s)_{2k-1} for k = 1.. : multiply by (s+2k-3)(s+2k-2) each step from previous.
    let mut p_re = 1.0f64;
    let mut p_im = 0.0f64;
    for k in 1..=k_max {
        if k == 1 {
            p_re = re;
            p_im = im;
        } else {
            for jj in [2 * k - 3, 2 * k - 2] {
                let j = jj as f64;
                let nr = p_re * (re + j) - p_im * im;
                let ni = p_re * im + p_im * (re + j);
                p_re = nr;
                p_im = ni;
            }
        }
        let mut f = bernoulli(2 * k);
        for j in 1..=(2 * k) {
            f /= j as f64;
        }
        // (N+x)^{-s-2k+1} = a^{-(2k-1)-re} e^{-i im ln a}
        let exp_pow = -((2 * k) as f64) + 1.0 - re;
        let mag3 = a.powf(exp_pow);
        // (p_re + i p_im) * (c1 - i s1)
        let tr = p_re * c1 - p_im * (-s1);
        let ti = p_re * (-s1) + p_im * c1;
        sr += f * mag3 * tr;
        si += f * mag3 * ti;
    }
    (sr, si)
}

/// Complex log-gamma via Lanczos (GSL g=7 coefficients, mpmath-compatible),
/// with reflection for Re z < 0.5. Accurate to ~1e-13 for Re z > 0.
pub fn ln_gamma_complex(re: f64, im: f64) -> (f64, f64) {
    const P: [f64; 9] = [
        0.99999999999980993,
        676.5203681218851,
        -1259.1392167224028,
        771.32342877765313,
        -176.61502916214059,
        12.507343278686905,
        -0.13857109526572012,
        9.9843695780195716e-6,
        1.5056327351493116e-7,
    ];
    if re < 0.5 {
        // reflection: ln Gamma(z) = ln pi - ln Gamma(1-z) - ln sin(pi z)
        let (gr, gi) = ln_gamma_complex(1.0 - re, -im);
        // sin(pi (re+im i)) = sin(pi re)cosh(pi im) + i cos(pi re)sinh(pi im)
        let (sr, si) = ((PI * re).sin() * (PI * im).cosh(), (PI * re).cos() * (PI * im).sinh());
        let lmag = (sr * sr + si * si).ln() / 2.0;
        let larg = si.atan2(sr);
        return (PI.ln() - gr - lmag, -gi - larg);
    }
    // x = z - 1 ; r = sum P[i]/(x+i) ; t = x + 7.5
    let x = re - 1.0;
    let y = im;
    let mut r_re = P[0];
    let mut r_im = 0.0f64;
    for i in 1..9 {
        let den = (x + i as f64) * (x + i as f64) + y * y;
        r_re += P[i] * (x + i as f64) / den;
        r_im += P[i] * (-y) / den;
    }
    let t_re = x + 7.5;
    let t_im = y;
    let lt = (t_re * t_re + t_im * t_im).ln() / 2.0;
    let at = t_im.atan2(t_re);
    let lr = (r_re * r_re + r_im * r_im).ln() / 2.0;
    let ar = r_im.atan2(r_re);
    // ln Gamma = 1/2 ln(2pi) + (x+1/2) ln t - t + ln r   with (x+1/2) = (re-1+1/2) = re-1/2
    let a_re = re - 0.5;
    let a_im = im;
    let re_out = 0.5 * (2.0 * PI).ln() + a_re * lt - a_im * at - t_re + lr;
    let im_out = a_re * at + a_im * lt - t_im + ar;
    (re_out, im_out)
}

/// Im ln Gamma(re + i*im) via Lanczos (accurate for all re > 0, small and large |z|).
pub fn im_log_gamma(re: f64, im: f64) -> f64 {
    ln_gamma_complex(re, im).1
}

/// L(1/2 + i t, chi) via q^{-s} sum_a chi(a) zeta(s, a/q).
pub fn l_half_it(t: f64, chi: &Character) -> (f64, f64) {
    let q = chi.q as f64;
    let s_re = 0.5;
    let s_im = t;
    let mut re = 0.0f64;
    let mut im = 0.0f64;
    for a in 1..chi.q {
        let (cr, ci) = chi.value(a as u64);
        if cr == 0.0 && ci == 0.0 {
            continue;
        }
        let (hr, hi) = hurwitz_zeta(s_re, s_im, a as f64 / q);
        // chi(a) * zeta(s, a/q)
        re += cr * hr - ci * hi;
        im += cr * hi + ci * hr;
    }
    // q^{-s} = q^{-1/2} e^{-i t ln q}
    let mag = q.powf(-s_re);
    let (s, c) = (t * q.ln()).sin_cos();
    (mag * (re * c - im * (-s)), mag * (re * (-s) + im * c))
}

/// arg(tau(chi))/2 for the Z-function phase.
fn half_arg_gauss(chi: &Character) -> f64 {
    let (gr, gi) = chi.gauss_sum;
    gi.atan2(gr) / 2.0
}

/// theta_chi(t) = (t/2) ln(q/pi) + Im ln Gamma(1/4 + it/2) - arg(tau(chi))/2  (even chi).
pub fn theta_chi(t: f64, chi: &Character) -> f64 {
    let q = chi.q as f64;
    (t / 2.0) * (q / PI).ln() + im_log_gamma(0.25, t / 2.0) - half_arg_gauss(chi)
}

/// Z_chi(t) = Re[e^{i theta} L(1/2+it, chi)] — real-valued for even chi.
/// Also returns the imaginary part for a self-check of the phase convention.
pub fn z_chi(t: f64, chi: &Character) -> (f64, f64) {
    let (lr, li) = l_half_it(t, chi);
    let th = theta_chi(t, chi);
    let (s, c) = th.sin_cos();
    // e^{i th} L = (c + i s)(lr + i li)
    let re = c * lr - s * li;
    let im = c * li + s * lr;
    (re, im)
}

/// Find zeros (ordinates) of L(s,chi) on the critical line in (t0, t1].
/// Scans sign changes of Z_chi and refines by bisection. Returns sorted ordinates.
pub fn find_zeros(t0: f64, t1: f64, chi: &Character) -> Vec<f64> {
    // parallel: split into subranges (overlapping by one step), merge, dedup
    let n_sub = 8usize;
    let chunk = (t1 - t0) / n_sub as f64;
    let mut all = std::thread::scope(|s| {
        let handles: Vec<_> = (0..n_sub)
            .map(|i| {
                let a = t0 + i as f64 * chunk;
                let mut b = t0 + (i + 1) as f64 * chunk;
                // overlap by one scan step at the boundary
                b = (b + step_size(b.max(1.0), chi)).min(t1);
                s.spawn(move || scan_range(a, b, chi))
            })
            .collect();
        let mut out: Vec<f64> = Vec::new();
        for h in handles {
            out.extend(h.join().unwrap());
        }
        out
    });
    all.sort_by(|a, b| a.partial_cmp(b).unwrap());
    let mut dedup: Vec<f64> = Vec::new();
    for z in all {
        if let Some(&last) = dedup.last() {
            if z - last < 1e-7 {
                continue;
            }
        }
        dedup.push(z);
    }
    dedup
}

fn step_size(t: f64, chi: &Character) -> f64 {
    let l = (chi.q as f64 * t / std::f64::consts::TAU).ln().max(1.0);
    (std::f64::consts::TAU / l / 8.0).clamp(0.01, 0.3)
}

fn scan_range(t0: f64, t1: f64, chi: &Character) -> Vec<f64> {
    let mut out = Vec::new();
    let mut t = t0;
    let mut z_prev = z_chi(t, chi).0;
    while t < t1 {
        let st = step_size(t, chi);
        let t2 = (t + st).min(t1);
        if t2 <= t {
            break;
        }
        let z = z_chi(t2, chi).0;
        if (z_prev > 0.0 && z < 0.0) || (z_prev < 0.0 && z > 0.0) {
            // sign change in [t, t2]
            let (mut a, mut b) = (t, t2);
            let mut fa = z_prev;
            // bisect to width ~1e-8 (plenty: phi-hat is smooth on scale 1/L ~ 0.1)
            for _ in 0..24 {
                let m = 0.5 * (a + b);
                let fm = z_chi(m, chi).0;
                if (fa > 0.0) == (fm > 0.0) {
                    a = m;
                    fa = fm;
                } else {
                    b = m;
                }
                if b - a < 1e-8 {
                    break;
                }
            }
            out.push(0.5 * (a + b));
        }
        t = t2;
        z_prev = z;
    }
    out
}

/// Check the functional equation L(1/2+it,chi) vs eps * conj(L(1/2-it,chi_bar) form):
/// verify that Z_chi is (numerically) real. Returns max |Im| / |L| over sample points.
pub fn phase_selfcheck(chi: &Character, tmax: f64) -> f64 {
    let mut worst = 0.0f64;
    let mut t = 2.0;
    while t <= tmax {
        let (re, im) = z_chi(t, chi);
        let mag = (re * re + im * im).sqrt();
        if mag > 1e-30 {
            worst = worst.max(im.abs() / mag);
        }
        t *= 1.7;
    }
    worst
}
