// em.rs — certified Euler–Maclaurin evaluation of Hurwitz zeta ζ(s,a) AND its
// derivative ζ'(s,a), a ∈ (0,1]; a = 1 gives ζ and ζ'.  Same certified style as
// tools/argprinciple/src/zeta.rs (explicit EM remainder + Kahan rounding + trig
// angle rounding).  The derivative's remainder is bounded by the Cauchy estimate
// on a disk of radius δ = 0.1:  |R_K'(s)| ≤ (1/δ)·sup_{|w−s|=δ}|R_K(w)|.
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

// ζ(s,a) = Σ_{k≥0}(k+a)^{-s}  and its s-derivative, a ∈ (0,1].
// Main sum k = 0..n−1; tail base N = n + a.  K = 40 EM corrections.
// Valid for σ + 2K − 1 > 0 (all our σ ≥ 0.001).
// Derivative remainder: Cauchy estimate with radius δ = 0.1.
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

    // ---- main sums (ζ and ζ'), Kahan + bounds ----------------------------
    let mut re = 0.0; let mut im = 0.0;
    let mut dre = 0.0; let mut dim = 0.0;
    let mut rc = 0.0; let mut ic = 0.0;
    let mut drc = 0.0; let mut dic = 0.0;
    let mut sum_mag = 0.0;      // Σ (k+a)^{-σ}
    let mut dsum_mag = 0.0;     // Σ ln(k+a)·(k+a)^{-σ}
    let mut angle_err = 0.0;
    let mut dangle_err = 0.0;
    for k in 0..n {
        let x = k as f64 + a;
        let lnx = x.ln();
        let mag = x.powf(-s_re);
        let tln = s_im * lnx;
        let (sx, cx) = tln.sin_cos();
        let tr = mag * cx;   // Re n^{-s}
        let ti = -mag * sx;  // Im n^{-s}
        // ζ Kahan
        let yr = tr - rc; let trn = re + yr; rc = (trn - re) - yr; re = trn;
        let yi = ti - ic; let tin = im + yi; ic = (tin - im) - yi; im = tin;
        // ζ' = Σ -lnx·(k+a)^{-s}
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

    // ---- N^{1-s}/(s-1) and its derivative ---------------------------------
    // ζ-term: N^{1-s}/(s-1); ζ'-term: N^{1-s}(-(s-1)ln N - 1)/(s-1)^2
    let den_re = s_re - 1.0;
    let den_im = s_im;
    let d2 = den_re * den_re + den_im * den_im;
    // q = N^{1-s}/(s-1)
    let q_re = (n_pow * e_re * den_re + n_pow * e_im * den_im) / d2;
    let q_im = (n_pow * e_im * den_re - n_pow * e_re * den_im) / d2;
    re += q_re; im += q_im;
    let term2_mag = n_pow / d2.sqrt();
    // u = -(s-1)ln N - 1 ;  num = N^{1-s}·u ;  q' = num/(s-1)^2
    let u_re = -den_re * ln_n - 1.0;
    let u_im = -den_im * ln_n;
    let num_re = n_pow * (e_re * u_re - e_im * u_im);
    let num_im = n_pow * (e_re * u_im + e_im * u_re);
    // q' = num/(s-1)^2 : divide by (s-1) twice
    let t1_re = (num_re * den_re + num_im * den_im) / d2;
    let t1_im = (num_im * den_re - num_re * den_im) / d2;
    let dq_re = (t1_re * den_re + t1_im * den_im) / d2;
    let dq_im = (t1_im * den_re - t1_re * den_im) / d2;
    dre += dq_re; dim += dq_im;
    let dterm2_mag = n_pow * (u_re * u_re + u_im * u_im).sqrt() / d2;

    // ---- N^{-s}/2 and derivative ------------------------------------------
    let h = 0.5 * n_neg_sig;
    re += h * e_re; im += h * e_im;
    let term3_mag = h;
    let dh = -0.5 * ln_n * n_neg_sig;
    dre += dh * e_re; dim += dh * e_im;
    let dterm3_mag = dh.abs();

    // ---- Bernoulli corrections and derivatives ----------------------------
    // C_k = B_{2k}/(2k)! · (s)_{2k-1}·N^{-s-2k+1}
    // C'_k = C_k·(Σ_{j=0}^{2k-2} 1/(s+j) − ln N)
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
        // derivative: C_k·(hsum − ln N)
        let h_re = hsum_re - ln_n;
        let h_im = hsum_im;
        let dcr = cr * h_re - ci * h_im;
        let dci = cr * h_im + ci * h_re;
        dre += dcr; dim += dci;
        let dcmag = cmag * (h_re * h_re + h_im * h_im).sqrt();
        dcorr_round += (3 * k + 20) as f64 * EPS * dcmag * 1.02;
    }

    // ---- remainder bounds --------------------------------------------------
    // |R_K| ≤ 2|B_{2K}|/(2K)! · ∏_{j=0}^{2K-1}|s+j|/N · N^{1-σ}/(σ+2K-1)
    let mut rprod = prod_mag;
    {
        let jf = (2 * k_max as i64 - 1) as f64;
        let a_re = (s_re + jf) / n_base;
        let a_im = s_im / n_base;
        rprod *= (a_re * a_re + a_im * a_im).sqrt();
    }
    let rem = 2.0 * abs_b_over_fact(k_max) * rprod * n_pow / (s_re + 2.0 * k_max as f64 - 1.0);
    // derivative remainder (Cauchy, radius δ): factors |s+j|→|s+j|+δ, N^{1-σ}→N^{1-(σ-δ)}
    // derivative remainder: every factor j=0..2K-1 inflated by δ (Cauchy radius)
    let mut drprod = 1.0;
    for jj in 0..(2 * k_max as i64) {
        let jf = jj as f64;
        let a_re = (s_re + jf) / n_base;
        let a_im = s_im / n_base;
        drprod *= (a_re * a_re + a_im * a_im).sqrt() + delta / n_base;
    }
    let drem = (1.0 / delta) * 2.0 * abs_b_over_fact(k_max) * drprod
        * n_base.powf(1.0 - (s_re - delta)) / (s_re - delta + 2.0 * k_max as f64 - 1.0);

    // ---- assemble ---------------------------------------------------------
    let value_round = main_round + 4.0 * EPS * (term2_mag + term3_mag) + corr_round + 4.0 * EPS * (re.abs() + im.abs());
    let err = value_round + rem;
    let dvalue_round = dmain_round + 4.0 * EPS * (dterm2_mag + dterm3_mag) + dcorr_round + 4.0 * EPS * (dre.abs() + dim.abs());
    let derr = dvalue_round + drem;
    Em { re, im, err, dre, dim, derr }
}

// ζ(s) and ζ'(s), s = σ+it.  n = number of main-sum terms (tail base n+1).
pub fn zeta_em(s_re: f64, s_im: f64, n: usize) -> Em {
    hurwitz_em(s_re, s_im, 1.0, n, 40)
}

pub fn em_n_for(t: f64) -> usize {
    ((1.6 * t / (2.0 * PI)).ceil().max(10.0)) as usize
}

// ============================================================================
// ζ^(m)(s) for m = 0..=m_max — DIRECT analytic differentiation of the EM
// expansion (no finite differencing, so no roundoff amplification). Same
// certified style: Kahan rounding budgets per order + Cauchy remainder bound
// |R_K^(m)(s)| ≤ (m!/δ^m)·sup_{|w−s|=δ}|R_K(w)|, inflating every |s+j|→|s+j|+δ
// and σ→σ−δ in the standard remainder bound.
// ============================================================================

pub fn binom_f(m: usize, j: usize) -> f64 {
    if j > m {
        return 0.0;
    }
    let mut c = 1.0f64;
    for i in 1..=j {
        c = c * (m - i + 1) as f64 / i as f64;
    }
    c
}

pub fn fact_f(m: usize) -> f64 {
    let mut f = 1.0f64;
    for i in 2..=m {
        f *= i as f64;
    }
    f
}

// complete Bell polynomials B_0..=B_m of complex λ (B_j = Σ_{r=1..j} C(j−1,r−1) λ_r B_{j−r})
fn bell_series(lam_re: &[f64], lam_im: &[f64], m: usize, br: &mut [f64], bi: &mut [f64]) {
    br[0] = 1.0;
    bi[0] = 0.0;
    for j in 1..=m {
        let mut sr = 0.0;
        let mut si = 0.0;
        for r in 1..=j {
            let c = binom_f(j - 1, r - 1);
            let (lr, li) = (lam_re[r], lam_im[r]);
            let (bjr, bji) = (br[j - r], bi[j - r]);
            sr += c * (lr * bjr - li * bji);
            si += c * (lr * bji + li * bjr);
        }
        br[j] = sr;
        bi[j] = si;
    }
}

pub struct EmDers {
    pub re: Vec<f64>,
    pub im: Vec<f64>,
    pub err: Vec<f64>, // |error| bound per derivative order m = 0..=m_max
}

pub fn zeta_em_ders(s_re: f64, s_im: f64, a: f64, n: usize, k_max: usize, m_max: usize) -> EmDers {
    let delta = 0.1f64;
    let mm = m_max + 1;
    let n_base = n as f64 + a;
    let ln_n = n_base.ln();
    let n_neg_sig = n_base.powf(-s_re);
    let n_pow = n_base.powf(1.0 - s_re);
    let (s_ln, c_ln) = (s_im * ln_n).sin_cos();
    let e_re = c_ln;  // Re N^{-it}
    let e_im = -s_ln; // Im N^{-it}

    let mut re = vec![0.0f64; mm];
    let mut im = vec![0.0f64; mm];
    let mut rc = vec![0.0f64; mm];
    let mut ic = vec![0.0f64; mm];
    let mut sum_mag = vec![0.0f64; mm];
    let mut angle_err = vec![0.0f64; mm];

    // ---- main sums Σ (−ln(k+a))^m (k+a)^{-s}, Kahan per order -----------------
    for k in 0..n {
        let x = k as f64 + a;
        let lnx = x.ln();
        let mag = x.powf(-s_re);
        let tln = s_im * lnx;
        let (sx, cx) = tln.sin_cos();
        let tr = mag * cx;
        let ti = -mag * sx;
        let ang = tln.abs() * 2.0f64.powi(-52) + 1e-15;
        let mut p = 1.0f64; // (−ln x)^m
        for m in 0..=m_max {
            let v = p * tr;
            let w = p * ti;
            let yr = v - rc[m];
            let tn = re[m] + yr;
            rc[m] = (tn - re[m]) - yr;
            re[m] = tn;
            let yi = w - ic[m];
            let tn2 = im[m] + yi;
            ic[m] = (tn2 - im[m]) - yi;
            im[m] = tn2;
            sum_mag[m] += p.abs() * mag;
            angle_err[m] += ang * p.abs() * mag;
            p *= -lnx;
        }
    }

    // ---- tail terms, derivatives in closed form --------------------------------
    let b_re = n_pow * e_re;   // N^{1−s}
    let b_im = n_pow * e_im;
    let ns_re = n_neg_sig * e_re; // N^{−s}
    let ns_im = n_neg_sig * e_im;
    let d_re = s_re - 1.0;
    let d_im = s_im;
    let d2 = d_re * d_re + d_im * d_im;
    let w1_re = d_re / d2; // 1/(s−1)
    let w1_im = -d_im / d2;
    let mut wp_re = vec![0.0f64; m_max + 2];
    let mut wp_im = vec![0.0f64; m_max + 2];
    wp_re[1] = w1_re;
    wp_im[1] = w1_im;
    for p in 2..=m_max + 1 {
        wp_re[p] = wp_re[p - 1] * w1_re - wp_im[p - 1] * w1_im;
        wp_im[p] = wp_re[p - 1] * w1_im + wp_im[p - 1] * w1_re;
    }
    let mag_b = (b_re * b_re + b_im * b_im).sqrt();
    let mut tail_round = vec![0.0f64; mm];
    for m in 0..=m_max {
        // T_m = Σ_j C(m,j) (−lnN)^j N^{1−s} (−1)^{m−j}(m−j)! (s−1)^{−(m−j+1)}
        let mut tr = 0.0;
        let mut ti_ = 0.0;
        let mut tmag = 0.0;
        for j in 0..=m {
            let c = binom_f(m, j);
            let lj = (-ln_n).powi(j as i32);
            let sign = if (m - j) % 2 == 0 { 1.0 } else { -1.0 };
            let cf = sign * fact_f(m - j) * c * lj;
            let p = m - j + 1;
            let (wre, wim) = (wp_re[p], wp_im[p]);
            let (vr, vi) = (b_re * wre - b_im * wim, b_re * wim + b_im * wre);
            tr += cf * vr;
            ti_ += cf * vi;
            tmag += cf.abs() * mag_b * (wre * wre + wim * wim).sqrt();
        }
        // U_m = (−lnN)^m N^{−s}/2
        let um = (-ln_n).powi(m as i32) * 0.5;
        let ur = um * ns_re;
        let ui = um * ns_im;
        re[m] += tr + ur;
        im[m] += ti_ + ui;
        tail_round[m] = 4.0 * EPS * (tmag + um.abs() * n_neg_sig);
    }

    // ---- Bernoulli corrections with derivatives (Bell of Pochhammer log-derivs) -
    let mut corr_round = vec![0.0f64; mm];
    let mut lam_re = vec![0.0f64; m_max + 1];
    let mut lam_im = vec![0.0f64; m_max + 1];
    let mut bell_re = vec![0.0f64; m_max + 1];
    let mut bell_im = vec![0.0f64; m_max + 1];
    let mut pwr_re = vec![0.0f64; m_max + 1];
    let mut pwr_im = vec![0.0f64; m_max + 1];
    let mut pr_re = vec![0.0f64; m_max + 1];
    let mut pr_im = vec![0.0f64; m_max + 1];
    let mut rem_prod = 1.0f64; // ∏_{j=0..2K−2} ((|s+j|+δ)/N), built incrementally
    for k in 1..=k_max {
        let mfac = 2 * k - 1; // (s)_{2k−1}
        let mut p_re = 1.0;
        let mut p_im = 0.0;
        let mut p_mag = 1.0;
        for r in 1..=m_max {
            pr_re[r] = 0.0;
            pr_im[r] = 0.0;
        }
        for l in 0..mfac {
            let lf = l as f64;
            let (xr, xi) = (s_re + lf, s_im);
            let x2 = xr * xr + xi * xi;
            let ir = xr / x2;
            let ii = -xi / x2;
            pwr_re[1] = ir;
            pwr_im[1] = ii;
            for r in 2..=m_max {
                pwr_re[r] = pwr_re[r - 1] * ir - pwr_im[r - 1] * ii;
                pwr_im[r] = pwr_re[r - 1] * ii + pwr_im[r - 1] * ir;
            }
            for r in 1..=m_max {
                pr_re[r] += pwr_re[r];
                pr_im[r] += pwr_im[r];
            }
            let (nr, ni) = (p_re * xr - p_im * xi, p_re * xi + p_im * xr);
            p_re = nr;
            p_im = ni;
            p_mag *= (xr * xr + xi * xi).sqrt();
            rem_prod *= ((xr * xr + xi * xi).sqrt() + delta) / n_base;
        }
        // λ_r = (−1)^{r−1}(r−1)! P_r
        for r in 1..=m_max {
            let sign = if (r - 1) % 2 == 0 { 1.0 } else { -1.0 };
            let cf = sign * fact_f(r - 1);
            lam_re[r] = cf * pr_re[r];
            lam_im[r] = cf * pr_im[r];
        }
        bell_series(&lam_re, &lam_im, m_max, &mut bell_re, &mut bell_im);
        let coef = abs_b_over_fact(k);
        let sign = if k % 2 == 1 { 1.0 } else { -1.0 };
        let nfac = n_base.powf(-(2.0 * k as f64 - 1.0)); // N^{−(2k−1)}
        let nsf_re = n_neg_sig * nfac * e_re; // N^{−s−(2k−1)}
        let nsf_im = n_neg_sig * nfac * e_im;
        let nsf_mag = n_neg_sig * nfac;
        for m in 0..=m_max {
            let mut cr = 0.0;
            let mut ci = 0.0;
            let mut cmag = 0.0;
            for j in 0..=m {
                let c = binom_f(m, j);
                let lj = (-ln_n).powi((m - j) as i32);
                // D_j = (s)_M · Bell_j
                let (dr_, di_) = (
                    p_re * bell_re[j] - p_im * bell_im[j],
                    p_re * bell_im[j] + p_im * bell_re[j],
                );
                let (vr, vi) = (dr_ * nsf_re - di_ * nsf_im, dr_ * nsf_im + di_ * nsf_re);
                cr += c * lj * vr;
                ci += c * lj * vi;
                cmag += c * lj.abs() * (dr_ * dr_ + di_ * di_).sqrt() * nsf_mag;
            }
            let sc = sign * coef;
            re[m] += sc * cr;
            im[m] += sc * ci;
            corr_round[m] += (3 * k + 20) as f64 * EPS * (coef * cmag) * 1.02;
        }
    }

    // ---- remainder bounds (Cauchy, radius δ) ------------------------------------
    let mut err = vec![0.0f64; mm];
    let last = (2 * k_max as i64 - 1) as f64;
    let lr = s_re + last;
    let last_mag = (lr * lr + s_im * s_im).sqrt();
    let infl = last_mag + delta;
    let base_rem = 2.0 * abs_b_over_fact(k_max);
    let n_pow_infl = n_base.powf(1.0 - (s_re - delta));
    let denom = s_re - delta + 2.0 * k_max as f64 - 1.0;
    for m in 0..=m_max {
        let mfac_b = fact_f(m) / delta.powi(m as i32);
        let rem = mfac_b * base_rem * rem_prod * (infl / n_base) * n_pow_infl / denom;
        let value_round = 4.0 * EPS * sum_mag[m] + angle_err[m] + tail_round[m] + corr_round[m]
            + 4.0 * EPS * (re[m].abs() + im[m].abs());
        err[m] = value_round + rem;
    }
    EmDers { re, im, err }
}

// ζ^(0..m_max)(s) for s = σ+it, a = 1
pub fn zeta_em_ders1(s_re: f64, s_im: f64, n: usize, m_max: usize) -> EmDers {
    zeta_em_ders(s_re, s_im, 1.0, n, 40, m_max)
}
