// em.rs — certified Euler–Maclaurin evaluation of Hurwitz zeta ζ(s,a) AND its
// derivative ζ'(s,a), a ∈ (0,1]; a = 1 gives ζ and ζ'.  Copied verbatim from
// tools/wave8b/src/em.rs (certified style: explicit EM remainder + Kahan rounding).
// ============================================================================
use std::f64::consts::PI;

pub const EPS: f64 = 2.220446049250313e-16;

// |B_{2k}|/(2k)! for k = 1..43 (from argprinciple/src/zeta.rs; inflated 1+1e-14)
pub const ABS_B_OVER_FACT: [f64; 43] = [
    0.083333333333333333333e0, 0.0013888888888888888889e0, 0.000033068783068783068783e0, 8.2671957671957671958e-7,
    2.0876756987868098979e-8, 5.2841901386874931848e-10, 1.3382536530684678833e-11, 3.3896802963225828668e-13,
    8.5860620562778445641e-15, 2.174868698558061873e-16, 5.5090028283602295152e-18, 1.3954464685812523341e-19,
    3.5347070396294674717e-21, 8.9535174270375468504e-23, 2.2679524523376830603e-24, 5.7447906688722024453e-26,
    1.4551724756148649019e-27, 3.6859949406653101782e-29, 9.336734257095044672e-31, 2.3650224157006299346e-32,
    5.9906717624821343047e-34, 1.5174548844682902617e-35, 3.8437581254541882322e-37, 9.7363530726466910353e-39,
    2.4662470442006809571e-40, 6.2470767418207436931e-42, 1.5824030244644914298e-43, 4.0082736859489359685e-45,
    1.0153075855569556312e-46, 2.5718041582418717499e-48, 6.5144560352338149316e-50, 1.6501309906896524555e-51,
    4.1798306285394758949e-53, 1.058763466770290877e-54, 2.6818791912607706661e-56, 6.7932793511074212095e-58,
    1.7207577616681404905e-59, 4.3587303293488938434e-61, 1.1040792903684666751e-62, 2.7966655133781345072e-64,
    7.0840365016794701985e-66, 1.7944074082892240666e-67, 4.5449264899414573e-69,
];
const COEF_INFL: f64 = 1.00000000000002;

pub fn abs_b_over_fact(k: usize) -> f64 {
    if k >= ABS_B_OVER_FACT.len() {
        return 2.0 * (1.0 + 2.0f64.powi(1 - 2 * k as i32)) / (2.0 * PI).powf(2.0 * k as f64);
    }
    ABS_B_OVER_FACT[k - 1] * COEF_INFL
}

#[derive(Clone, Copy)]
pub struct Em {
    pub re: f64,
    pub im: f64,
    pub err: f64,   // certified |error| bound on ζ(s,a)
    pub dre: f64,
    pub dim: f64,
    pub derr: f64,  // certified |error| bound on ζ'(s,a)
}

pub fn hurwitz_em(s_re: f64, s_im: f64, a: f64, n: usize, k_max: usize) -> Em {
    let delta = 0.1f64; // Cauchy radius for the derivative remainder
    let nf = n as f64;
    let n_base = nf + a; // tail base N = n + a
    let ln_n = n_base.ln();
    let n_pow = n_base.powf(1.0 - s_re); // N^{1-σ}
    let n_neg_sig = n_base.powf(-s_re);  // N^{-σ}
    let (s_ln, c_ln) = (s_im * ln_n).sin_cos();
    let e_re = c_ln;
    let e_im = -s_ln;

    let mut re = 0.0; let mut im = 0.0;
    let mut dre = 0.0; let mut dim = 0.0;
    let mut rc = 0.0; let mut ic = 0.0;
    let mut drc = 0.0; let mut dic = 0.0;
    let mut sum_mag = 0.0;
    let mut dsum_mag = 0.0;
    let mut angle_err = 0.0;
    let mut dangle_err = 0.0;
    for k in 0..n {
        let x = k as f64 + a;
        let lnx = x.ln();
        let mag = x.powf(-s_re);
        let tln = s_im * lnx;
        let (sx, cx) = tln.sin_cos();
        let tr = mag * cx;
        let ti = -mag * sx;
        let yr = tr - rc; let trn = re + yr; rc = (trn - re) - yr; re = trn;
        let yi = ti - ic; let tin = im + yi; ic = (tin - im) - yi; im = tin;
        let dtr = -lnx * tr;
        let dti = -lnx * ti;
        let dyr = dtr - drc; let dtrn = dre + dyr; drc = (dtrn - dre) - dyr; dre = dtrn;
        let dyi = dti - dic; let dtin = dim + dyi; dic = (dtin - dim) - dyi; dim = dtin;
        sum_mag += mag;
        dsum_mag += lnx * mag;
        let ang = tln.abs() * 2.0f64.powi(-52) + 1e-15;
        angle_err += ang * mag;
        dangle_err += ang * lnx * mag;
    }
    let main_round = 4.0 * EPS * sum_mag + angle_err;
    let dmain_round = 4.0 * EPS * dsum_mag + dangle_err;

    let den_re = s_re - 1.0;
    let den_im = s_im;
    let d2 = den_re * den_re + den_im * den_im;
    let q_re = (n_pow * e_re * den_re + n_pow * e_im * den_im) / d2;
    let q_im = (n_pow * e_im * den_re - n_pow * e_re * den_im) / d2;
    re += q_re; im += q_im;
    let term2_mag = n_pow / d2.sqrt();
    let u_re = -den_re * ln_n - 1.0;
    let u_im = -den_im * ln_n;
    let num_re = n_pow * (e_re * u_re - e_im * u_im);
    let num_im = n_pow * (e_re * u_im + e_im * u_re);
    let t1_re = (num_re * den_re + num_im * den_im) / d2;
    let t1_im = (num_im * den_re - num_re * den_im) / d2;
    let dq_re = (t1_re * den_re + t1_im * den_im) / d2;
    let dq_im = (t1_im * den_re - t1_re * den_im) / d2;
    dre += dq_re; dim += dq_im;
    let dterm2_mag = n_pow * (u_re * u_re + u_im * u_im).sqrt() / d2;

    let h = 0.5 * n_neg_sig;
    re += h * e_re; im += h * e_im;
    let term3_mag = h;
    let dh = -0.5 * ln_n * n_neg_sig;
    dre += dh * e_re; dim += dh * e_im;
    let dterm3_mag = dh.abs();

    let mut prod_re = 1.0; let mut prod_im = 0.0; let mut prod_mag = 1.0;
    let mut hsum_re = 0.0; let mut hsum_im = 0.0;
    let mut corr_round = 0.0;
    let mut dcorr_round = 0.0;
    for k in 1..=k_max {
        let start_j = if k == 1 { 0 } else { 2 * k as i64 - 3 };
        for jj in start_j..=(2 * k as i64 - 2) {
            let jf = jj as f64;
            let a_re = (s_re + jf) / n_base;
            let a_im = s_im / n_base;
            let (pr, pi) = (prod_re * a_re - prod_im * a_im, prod_re * a_im + prod_im * a_re);
            prod_re = pr; prod_im = pi;
            prod_mag *= (a_re * a_re + a_im * a_im).sqrt();
            let den = (s_re + jf) * (s_re + jf) + s_im * s_im;
            hsum_re += (s_re + jf) / den;
            hsum_im -= s_im / den;
        }
        let coef = abs_b_over_fact(k);
        let sign = if k % 2 == 1 { 1.0 } else { -1.0 };
        let scale = coef * n_neg_sig;
        let cr = sign * scale * (prod_re * e_re - prod_im * e_im);
        let ci = sign * scale * (prod_re * e_im + prod_im * e_re);
        re += cr; im += ci;
        let cmag = coef * prod_mag * n_neg_sig;
        corr_round += (3 * k + 20) as f64 * EPS * cmag * 1.02;
        let h_re = hsum_re - ln_n;
        let h_im = hsum_im;
        let dcr = cr * h_re - ci * h_im;
        let dci = cr * h_im + ci * h_re;
        dre += dcr; dim += dci;
        let dcmag = cmag * (h_re * h_re + h_im * h_im).sqrt();
        dcorr_round += (3 * k + 20) as f64 * EPS * dcmag * 1.02;
    }

    let mut rprod = prod_mag;
    {
        let jf = (2 * k_max as i64 - 1) as f64;
        let a_re = (s_re + jf) / n_base;
        let a_im = s_im / n_base;
        rprod *= (a_re * a_re + a_im * a_im).sqrt();
    }
    let rem = 2.0 * abs_b_over_fact(k_max) * rprod * n_pow / (s_re + 2.0 * k_max as f64 - 1.0);
    let mut drprod = 1.0;
    for jj in 0..(2 * k_max as i64) {
        let jf = jj as f64;
        let a_re = (s_re + jf) / n_base;
        let a_im = s_im / n_base;
        drprod *= (a_re * a_re + a_im * a_im).sqrt() + delta / n_base;
    }
    let drem = (1.0 / delta) * 2.0 * abs_b_over_fact(k_max) * drprod
        * n_base.powf(1.0 - (s_re - delta)) / (s_re - delta + 2.0 * k_max as f64 - 1.0);

    let value_round = main_round + 4.0 * EPS * (term2_mag + term3_mag) + corr_round + 4.0 * EPS * (re.abs() + im.abs());
    let err = value_round + rem;
    let dvalue_round = dmain_round + 4.0 * EPS * (dterm2_mag + dterm3_mag) + dcorr_round + 4.0 * EPS * (dre.abs() + dim.abs());
    let derr = dvalue_round + drem;
    Em { re, im, err, dre, dim, derr }
}

pub fn zeta_em(s_re: f64, s_im: f64, n: usize) -> Em {
    hurwitz_em(s_re, s_im, 1.0, n, 40)
}

pub fn em_n_for(t: f64) -> usize {
    ((1.6 * t / (2.0 * PI)).ceil().max(10.0)) as usize
}
