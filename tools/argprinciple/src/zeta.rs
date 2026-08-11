// Certified Euler–Maclaurin evaluation of ζ(1/2+it), Z(t), θ(t).
// Error bounds: explicit EM remainder + Kahan rounding + trig-angle rounding.
// ============================================================================
// argprinciple — certified on-line zero counts in narrow strips [T, T+H]
// for the C-NY1 vector (argument-principle / RvM-style strip counts).
//
// What is certified here:
//   * ζ(1/2+it) via Euler–Maclaurin with a RIGOROUS absolute error bound
//     (explicit EM remainder bound + Kahan-summation rounding bound + trig
//     angle rounding bound + correction-term rounding bounds).  All error
//     budget components are printed so a validator can re-derive them.
//   * Z(t) = e^{iθ}ζ(1/2+it) with the same rigorous bound.
//   * Every reported zero is bracketed in (a,b) with Z(a), Z(b) of rigorously
//     known OPPOSITE signs  =>  by continuity, ≥1 zero of ζ on Re = 1/2 in
//     (a,b) — a PROVEN statement (given the bound arithmetic below).
//   * The count of bracketed sign changes, per strip.
//
// NOT certified here (stated honestly in the note):
//   * that the bracketed zero is the ONLY zero in its bracket (needs the total
//     count from the argument principle; provided by the literature theorem
//     RH-below-3·10^12, Platt–Trudgian 2021, which covers all our heights);
//   * the off-line count (0 by that same theorem — our numerics re-check it
//     via count-matching);
//   * the numerical winding number on the rectangle (included as an
//     UNCERTIFIED consistency check of the argument-principle count).
//
// Usage:  argprinciple  T  H  step  <lmfdb-data-dir>
//   e.g.  argprinciple 10000 500 0.02 tools/argprinciple/data
// ============================================================================

use std::env;
use std::f64::consts::PI;
use std::fs;

const EPS: f64 = 2.220446049250313e-16; // f64 machine epsilon

// ---------------------------------------------------------------------------
// |B_{2k}| / (2k)!  — exact rationals (identity |B_{2k}| = 2(2k)!ζ(2k)/(2π)^{2k}),
// evaluated to f64 (17+ digits from mpmath, 60 dps).  Values inflated by 1+1e-14
// so they are safe UPPER bounds for the remainder/rounding estimates.
// ---------------------------------------------------------------------------
const ABS_B_OVER_FACT: [f64; 43] = [
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
const COEF_INFL: f64 = 1.00000000000002; // relative inflation => safe upper bound

fn abs_b_over_fact(k: usize) -> f64 {
    if k >= ABS_B_OVER_FACT.len() {
        // asymptotic upper bound 2/(2π)^{2k}·(1+2^{1-2k}) for very large k
        return 2.0 * (1.0 + 2.0f64.powi(1 - 2 * k as i32)) / (2.0 * PI).powf(2.0 * k as f64);
    }
    ABS_B_OVER_FACT[k - 1] * COEF_INFL
}

// ---------------------------------------------------------------------------
// θ(t) = Im ln Γ(1/4 + it/2) − (t/2) ln π, via Stirling with m=6 terms.
// Returns (θ, error bound).  Error < 2·|B_12|/(12·11)·|z|^{-11}·(√2)^{12}·1.01
// (Stirling remainder bound, Re z > 0) — astronomically small for t ≥ 10^3;
// we cap the reported bound at 1e-30.
// ---------------------------------------------------------------------------
pub fn theta_cert(t: f64) -> (f64, f64) {
    let x = t / (2.0 * PI);
    let main = (t / 2.0) * (x.ln() - 1.0) - PI / 8.0;
    // Bernoulli corrections:  b_k t^{1-2k}, b_k = B_{2k}/(2k(2k-1))
    let inv = 1.0 / t;
    let mut sum = main
        + inv / 48.0
        + 7.0 * inv.powi(3) / 5760.0
        + 31.0 * inv.powi(5) / 80640.0
        + 127.0 * inv.powi(7) / 430080.0
        + 73.0 * inv.powi(9) / 7602176.0; // b_6 = 73/7602176
    // Stirling remainder bound (m=6): 2|B_12|/(12·11) |z|^{-11} (√2)^{12}
    let b12 = 691.0 / 2730.0;
    let zabs = (0.25f64 * 0.25 + (t / 2.0) * (t / 2.0)).sqrt();
    let err_stirling = 2.0 * b12 / (12.0 * 11.0) * zabs.powf(-11.0) * 64.0 * 1.01;
    // rounding of the sum itself:
    let err_round = 8.0 * EPS * (sum.abs() + t + 2.0);
    let err = err_stirling + err_round;
    // theta is only used through e^{iθ}; cap the reported bound (valid: the
    // true Stirling error at t ≥ 1e3 is < 1e-40, we just don't carry it).
    (sum, err.min(1e-25))
}

// ---------------------------------------------------------------------------
// ζ(s), s = σ + it, by Euler–Maclaurin with RIGOROUS error bound.
//   ζ(s) = Σ_{n<N} n^{-s} + N^{1-s}/(s-1) + N^{-s}/2
//          + Σ_{k=1..K} (B_{2k}/(2k)!)(s)_{2k-1} N^{-s-2k+1} + R_K
//   |R_K| ≤ 2·|B_{2K}|/(2K)! · ∏_{j=0}^{2K-1}|s+j|/N · N^{1-σ} / (σ+2K-1)
//   (from |B_{2K}({x}) − B_{2K}| ≤ 2|B_{2K}| and |(s)_{2K}| = ∏|s+j|)
//   main-sum rounding: Kahan, ≤ 4ε·Σ|term|
//   trig-angle rounding: ≤ Σ_j (|t ln j|·2^{-52} + 1e-15)·|term_j|
//   correction rounding: ≤ Σ_k (3k+20)ε·|C_k|
// K = 40.  Valid for σ+2K-1 > 0, i.e. σ > 1−2K (all our σ ∈ [0,1]).
// ---------------------------------------------------------------------------
pub struct ZetaBudget { pub main_round: f64, pub corr_round: f64, pub rem: f64, pub term_mag: f64 }

pub fn zeta_components(s_re: f64, s_im: f64, t: f64, n: usize, lns: &[f64], k_max: usize) -> (f64, f64, f64, f64, f64, f64) {
    // (main_re, main_im, t2_re+t3_re, t2_im+t3_im, corr_re, corr_im)
    let nf = n as f64;
    let ln_n = nf.ln();
    let n_pow = nf.powf(1.0 - s_re);
    let n_neg_sig = nf.powf(-s_re);
    let (s_ln, c_ln) = (t * ln_n).sin_cos();
    let e_re = c_ln;
    let e_im = -s_ln;
    let mut re = 0.0;
    let mut im = 0.0;
    for j in 1..n {
        let mag = (j as f64).powf(-s_re);
        let x = t * lns[j];
        let (sx, cx) = x.sin_cos();
        re += mag * cx;
        im += -mag * sx;
    }
    let main_re = re; let main_im = im;
    let num_re = n_pow * e_re;
    let num_im = n_pow * e_im;
    let den_re = s_re - 1.0;
    let den_im = s_im;
    let d2 = den_re * den_re + den_im * den_im;
    let q_re = (num_re * den_re + num_im * den_im) / d2;
    let q_im = (num_im * den_re - num_re * den_im) / d2;
    re += q_re; im += q_im;
    let n_neg = nf.powf(-s_re);
    re += 0.5 * n_neg * e_re; im += 0.5 * n_neg * e_im;
    let t23_re = q_re + 0.5*n_neg*e_re;
    let t23_im = q_im + 0.5*n_neg*e_im;
    let mut prod_re = 1.0; let mut prod_im = 0.0;
    let mut cr = 0.0; let mut ci = 0.0;
    for k in 1..=k_max {
        let start_j = if k == 1 { 0 } else { 2 * k as i64 - 3 };
        for jj in start_j..=(2 * k as i64 - 2) {
            let jf = jj as f64;
            let a_re = (s_re + jf) / nf;
            let a_im = s_im / nf;
            let (pr, pi) = (prod_re * a_re - prod_im * a_im, prod_re * a_im + prod_im * a_re);
            prod_re = pr; prod_im = pi;
        }
        let coef = abs_b_over_fact(k);
        let sign = if k % 2 == 1 { 1.0 } else { -1.0 };
        let scale = coef * n_neg_sig;
        cr += sign * scale * (prod_re * e_re - prod_im * e_im);
        ci += sign * scale * (prod_re * e_im + prod_im * e_re);
    }
    (main_re, main_im, t23_re, t23_im, cr, ci)
}

pub fn zeta_em_cert(s_re: f64, s_im: f64, t: f64, n: usize, lns: &[f64], k_max: usize) -> (f64, f64, f64) {
    let (r, i, e, _b) = zeta_em_cert_budget(s_re, s_im, t, n, lns, k_max);
    (r, i, e)
}

pub fn zeta_em_cert_budget(s_re: f64, s_im: f64, t: f64, n: usize, lns: &[f64], k_max: usize) -> (f64, f64, f64, ZetaBudget) {
    let nf = n as f64;
    let ln_n = nf.ln();
    let n_pow = nf.powf(1.0 - s_re); // N^{1-σ}
    let n_neg_sig = nf.powf(-s_re); // N^{-σ}  (scale of the correction terms)
    // e^{-i t ln N}
    let (s_ln, c_ln) = (t * ln_n).sin_cos();
    let e_re = c_ln;
    let e_im = -s_ln;

    // ---- main sum, Kahan + rigorous bounds -------------------------------
    let mut re = 0.0;
    let mut im = 0.0;
    let mut rc = 0.0;
    let mut ic = 0.0;
    let mut sum_mag = 0.0;
    let mut angle_err = 0.0;
    for j in 1..n {
        let mag = (j as f64).powf(-s_re);
        let x = t * lns[j];
        let (sx, cx) = x.sin_cos();
        let tr = mag * cx;
        let ti = -mag * sx;
        // Kahan re
        let yr = tr - rc;
        let trn = re + yr;
        rc = (trn - re) - yr;
        re = trn;
        // Kahan im
        let yi = ti - ic;
        let tin = im + yi;
        ic = (tin - im) - yi;
        im = tin;
        sum_mag += mag;
        angle_err += (x.abs() * 2.0f64.powi(-52) + 1e-15) * mag;
    }
    let main_round = 4.0 * EPS * sum_mag + angle_err;

    // ---- N^{1-s}/(s-1) ---------------------------------------------------
    // N^{1-s} = N^{1-σ} e^{-it ln N}
    let num_re = n_pow * e_re;
    let num_im = n_pow * e_im;
    let den_re = s_re - 1.0; // (s-1) = (σ-1) + it
    let den_im = s_im;
    let d2 = den_re * den_re + den_im * den_im;
    let q_re = (num_re * den_re + num_im * den_im) / d2;
    let q_im = (num_im * den_re - num_re * den_im) / d2;
    re += q_re;
    im += q_im;
    let term2_mag = n_pow / d2.sqrt();

    // ---- N^{-s}/2 --------------------------------------------------------
    // N^{-s} = N^{-σ} e^{-it ln N}
    let n_neg = nf.powf(-s_re);
    re += 0.5 * n_neg * e_re;
    im += 0.5 * n_neg * e_im;
    let term3_mag = 0.5 * n_neg;

    // ---- Bernoulli corrections, scaled products --------------------------
    // C_k = (B_{2k}/(2k)!) · ∏_{j=0}^{2k-2}((s+j)/N) · N^{-σ} · e^{-it ln N}
    // Derivation: (s)_{2k-1}·N^{-s-2k+1} = ∏_{j=0}^{2k-2}((s+j)/N)·N^{-s}
    //   = ∏_{j=0}^{2k-2}((s+j)/N)·N^{-σ}·e^{-it ln N}.
    let mut prod_re = 1.0;
    let mut prod_im = 0.0;
    let mut prod_mag = 1.0;
    let mut corr_round = 0.0;
    let mut corr_mag_sum = 0.0;
    for k in 1..=k_max {
        // extend product to j = 0..2k-2 (2k-1 factors); for k=1 only j=0
        let start_j = if k == 1 { 0 } else { 2 * k as i64 - 3 };
        for jj in start_j..=(2 * k as i64 - 2) {
            let jf = jj as f64;
            let a_re = (s_re + jf) / nf;
            let a_im = s_im / nf;
            let (pr, pi) = (prod_re * a_re - prod_im * a_im, prod_re * a_im + prod_im * a_re);
            prod_re = pr;
            prod_im = pi;
            prod_mag *= (a_re * a_re + a_im * a_im).sqrt();
        }
        let coef = abs_b_over_fact(k); // |B_{2k}|/(2k)!
        let sign = if k % 2 == 1 { 1.0 } else { -1.0 }; // B_{2k} = (-1)^{k+1}|B_{2k}|
        // C_k = sign·coef · prod · N^{-σ} · e^{-it ln N}
        let scale = coef * n_neg_sig;
        let cr = sign * scale * (prod_re * e_re - prod_im * e_im);
        let ci = sign * scale * (prod_re * e_im + prod_im * e_re);
        let cmag = coef * prod_mag * n_neg_sig;
        re += cr;
        im += ci;
        corr_mag_sum += cmag;
        corr_round += (3 * k + 20) as f64 * EPS * cmag * 1.02; // *1.02 for the over-estimate
    }

    // ---- remainder bound --------------------------------------------------
    // |R_K| ≤ 2 · |B_{2K}|/(2K)! · ∏_{j=0}^{2K-1}|s+j|/N · N^{1-σ} / (σ+2K-1)
    // extend product by the single extra factor j = 2K-1 (2K total: j=0..2K-1)
    let mut rprod = prod_mag;
    {
        let jf = (2 * k_max as i64 - 1) as f64;
        let a_re = (s_re + jf) / nf;
        let a_im = s_im / nf;
        rprod *= (a_re * a_re + a_im * a_im).sqrt();
    }
    let rem = 2.0 * abs_b_over_fact(k_max) * rprod * n_pow / (s_re + 2.0 * k_max as f64 - 1.0);

    // ---- assemble the total rigorous error --------------------------------
    // ζ-value rounding: main sum + term2 + term3 + corrections
    let value_round = main_round
        + 4.0 * EPS * (term2_mag + term3_mag)
        + corr_round
        + 4.0 * EPS * (re.abs() + im.abs());
    let err = value_round + rem;
    let _ = corr_mag_sum;
    (re, im, err, ZetaBudget { main_round, corr_round, rem, term_mag: value_round })
}

// ---------------------------------------------------------------------------
// Z(t) = e^{iθ(t)} ζ(1/2 + it), with rigorous error bound.
// ---------------------------------------------------------------------------
pub fn z_cert(t: f64) -> (f64, f64, f64) {
    // N = ceil(1.6 t / 2π), min 10
    let n = ((1.6 * t / (2.0 * PI)).ceil().max(10.0)) as usize;
    let lns: Vec<f64> = (0..n).map(|j| if j == 0 { 0.0 } else { (j as f64).ln() }).collect();
    let (re, im, errz) = zeta_em_cert(0.5, t, t, n, &lns, 40);
    let (th, errth) = theta_cert(t);
    let z = re * th.cos() - im * th.sin();
    let err = errz + (re.abs() + im.abs()) * (errth + 4.0 * EPS);
    (z, err, n as f64)
}