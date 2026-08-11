// Euler–Maclaurin evaluation of ζ(1/2 + it), the Riemann–Siegel theta, Z(t),
// and zero finding on the critical line. All f64. Error budget ~1e-10 for
// t <= 1e5 (K = 10 Bernoulli terms, N = ceil(1.6 t/2pi) main-sum terms).

/// Riemann–Siegel theta via the standard asymptotic expansion:
/// θ(t) = (t/2)(ln(t/2π) − 1) − π/8 + 1/(48t) + 7/(5760 t³) + 31/(80640 t⁵) + ...
/// Good to ~t^{-9}; for t >= 20 the error is < 1e-12.
pub fn theta(t: f64) -> f64 {
    const TWO_PI: f64 = 6.283185307179586;
    if t < 20.0 {
        // For tiny t use a direct Stirling evaluation of Im ln Γ(1/4 + it/2) - (t/2) ln π.
        return theta_small(t);
    }
    let x = t / TWO_PI;
    let inv = 1.0 / t;
    let inv3 = inv * inv * inv;
    let inv5 = inv3 * inv * inv;
    let inv7 = inv5 * inv * inv;
    (t / 2.0) * (x.ln() - 1.0) - std::f64::consts::FRAC_PI_8
        + inv / 48.0
        + 7.0 * inv3 / 5760.0
        + 31.0 * inv5 / 80640.0
        + 127.0 * inv7 / 430080.0
}

fn theta_small(t: f64) -> f64 {
    // θ(t) = Im ln Γ(1/4 + it/2) − (t/2) ln π, via Stirling on z = 1/4 + it/2.
    // ln Γ(z) ≈ (z − 1/2) ln z − z + (1/2) ln(2π) + Σ B_{2k}/(2k(2k−1)) z^{1−2k}
    let re = 0.25;
    let im = t / 2.0;
    let lz = (re * re + im * im).ln() / 2.0;
    let az = im.atan2(re); // arg z
    // (z - 1/2) ln z - z + 1/2 ln(2π): imaginary part
    let mut th = (re - 0.5) * az + im * lz - im;
    // Bernoulli corrections z^{1-2k}: arg = (1-2k) az, |z|^{1-2k}
    let mag = (re * re + im * im).sqrt();
    for k in 1..=6 {
        let b = bernoulli(2 * k);
        let coef = b / ((2.0 * k as f64) * (2.0 * k as f64 - 1.0));
        th += coef * mag.powi(1 - 2 * k as i32) * ((1 - 2 * k as i32) as f64 * az).sin();
    }
    th - (t / 2.0) * std::f64::consts::PI.ln()
}

pub fn bernoulli(n: usize) -> f64 {
    // B_2k for k = 1..=10
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
        _ => 0.0,
    }
}

/// ζ(1/2 + it) by Euler–Maclaurin.
/// ζ(s) = Σ_{n<N} n^{-s} + N^{1-s}/(s-1) + N^{-s}/2 + Σ_{k=1..K} (B_{2k}/(2k)!)(s)_{2k-1} N^{-s-2k+1}
/// Returns (re, im).
pub fn zeta_half_it(t: f64) -> (f64, f64) {
    const TWO_PI: f64 = 6.283185307179586;
    let n = (1.6 * t / TWO_PI).ceil().max(10.0) as usize;
    let s_re = 0.5;
    let s_im = t;
    let mut re = 0.0;
    let mut im = 0.0;
    // main sum n^{-s} = n^{-1/2} e^{-it ln n} = n^{-1/2}(cos(t ln n) - i sin(t ln n))
    for n_ in 1..n {
        let ln = (n_ as f64).ln();
        let mag = 1.0 / (n_ as f64).sqrt();
        // NOTE: f64::sin_cos returns (sin, cos)
        let (s, c) = (t * ln).sin_cos();
        re += mag * c;
        im += -mag * s;
    }
    // N^{1-s}/(s-1): N^{1-s} = N^{1/2} e^{-it ln N}; divide by (s-1) = -1/2 + it
    let ln_n = (n as f64).ln();
    let m1 = (n as f64).sqrt();
    let (s1, c1) = (t * ln_n).sin_cos(); // e^{-it ln N} = c1 - i s1
    let num_re = m1 * c1;
    let num_im = -m1 * s1;
    let den_re = -0.5;
    let den_im = t;
    let d2 = den_re * den_re + den_im * den_im;
    let (q_re, q_im) = ((num_re * den_re + num_im * den_im) / d2,
                        (num_im * den_re - num_re * den_im) / d2);
    re += q_re;
    im += q_im;
    // (1/2) N^{-s}
    let m2 = 0.5 / (n as f64).sqrt();
    re += m2 * c1;
    im += -m2 * s1;
    // Bernoulli terms: (B_{2k}/(2k)!) (s)_{2k-1} N^{-s-2k+1}
    // (s)_{2k-1} = prod_{j=0}^{2k-2} (s + j); N^{-s-2k+1} = N^{-2k+1/2} e^{-it ln N}
    let mut p_re = 1.0;
    let mut p_im = 0.0;
    for k in 1..=10 {
        // extend (s)_{2k-3} -> (s)_{2k-1}: multiply by (s + 2k-3)(s + 2k-2)
        if k == 1 {
            p_re = s_re;
            p_im = s_im;
        } else {
            for jj in [2 * k - 3, 2 * k - 2] {
                let j = jj as f64;
                let (a_re, a_im) = (p_re * (s_re + j) - p_im * s_im,
                                    p_re * s_im + p_im * (s_re + j));
                p_re = a_re;
                p_im = a_im;
            }
        }
        // B_{2k}/(2k)!
        let mut f = bernoulli(2 * k);
        for j in 1..=(2 * k) {
            f /= j as f64;
        }
        // N^{-2k+1/2} e^{-it ln N}
        let exp_pow = -(2.0 * k as f64) + 0.5;
        let mag3 = (n as f64).powf(exp_pow);
        let term_re = f * mag3 * (p_re * c1 - p_im * (-s1));
        let term_im = f * mag3 * (p_re * (-s1) + p_im * c1);
        re += term_re;
        im += term_im;
    }
    (re, im)
}

/// The real function Z(t) = e^{iθ(t)} ζ(1/2 + it).
pub fn zeta_z(t: f64) -> f64 {
    let (re, im) = zeta_half_it(t);
    let th = theta(t);
    re * th.cos() - im * th.sin()
}

/// Find the first `count` zeros of ζ on the critical line (ordinates, ascending),
/// by scanning Z(t) for sign changes and bisecting. Independent of any database.
pub fn find_zeros(count: usize) -> Vec<f64> {
    let mut out = Vec::with_capacity(count);
    let mut t = 10.0; // first zero is at 14.134...
    let mut z_prev = zeta_z(t);
    // step = spacing/4 approx; spacing ~ 2π/ln(t/2π)
    let mut step = 0.5;
    while out.len() < count {
        let z = zeta_z(t + step);
        if z_prev == 0.0 || (z_prev > 0.0 && z < 0.0) || (z_prev < 0.0 && z > 0.0) {
            // sign change in [t, t+step] -> bisect
            let (mut a, mut b) = (t, t + step);
            let (mut fa, _) = (z_prev, 0.0);
            for _ in 0..80 {
                let m = 0.5 * (a + b);
                let fm = zeta_z(m);
                if (fa > 0.0) == (fm > 0.0) {
                    a = m;
                    fa = fm;
                } else {
                    b = m;
                }
                if b - a < 1e-13 {
                    break;
                }
            }
            let root = 0.5 * (a + b);
            out.push(root);
            if out.len() >= count {
                break;
            }
            // step = spacing/16: close pairs (gaps as small as ~0.16 at t~1000) must
            // not be skipped. spacing ~ 2π/ln(t/2π) -> step = π/(8·ln(t/2π)).
            step = (std::f64::consts::PI / (8.0 * (root / 6.283185307179586).ln())).clamp(0.02, 0.5);
            // continue scanning from just past the root
            t = root + 1e-6;
            z_prev = zeta_z(t);
        } else {
            t += step;
            z_prev = z;
        }
        if t > 1e7 {
            panic!("scan escaped: only found {} zeros", out.len());
        }
    }
    out
}
