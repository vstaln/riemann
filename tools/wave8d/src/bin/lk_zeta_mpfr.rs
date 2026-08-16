// lk_zeta_mpfr.rs — 8D L_k(t) at ~200/256-bit precision via rug (MPFR).
//
// Decisive re-run of the k=18/19/20 @ t=40 question that the f64 route
// (lk_zeta.rs route B) left INCONCLUSIVE (error >= signal: ~30-order Bell
// cancellation at f64 eps).  Full analytic-route port:
//   zeta^(0..m)(s)  certified Euler-Maclaurin (direct differentiation)
//   polygamma       shift + Stirling (corrected signs)
//   L_n = (d/ds)^n log zeta  (Bell-style recurrence, certified err recursion)
//   u^(n) = (d/dt)^n log Xi = Re[i^n A_n]   (reality self-check on Im)
//   B_k = complete Bell of u',   q = B_k^2 - B_{k-1}B_{k+1}
//   L_k = Xi(t)^2 * q
// Error: certified EM remainder + MPFR rounding budgets + term-based Stirling
// truncation, propagated through log-derivs -> u -> Bell -> q -> L.
//
// Controls (mpmath dps=60, pre-Rust-rule): L_3(40)=+1.657e-21, L_8(33.6)=+2.166e-17.
// Sanity: Xi(0)=0.497120778188314, |Xi|~0 at gamma_1..4, sign = (-1)^N(t).

#[path = "../em.rs"]
mod em;

use rug::float::Constant;
use rug::{Assign, Float, Integer};
use std::cell::RefCell;
use std::collections::HashMap;

const N_ZETA: usize = 600; // EM main-sum terms (certified remainder << 1e-90 here)
const SHIFT: usize = 40;   // polygamma Stirling shift
const KP: usize = 28;      // polygamma Stirling terms
const GAMMA_TERMS_MAX: usize = 300;
const COEF_INFL: f64 = 1.00000000000002; // conservative inflation for certified bounds

fn zf(prec: u32, v: f64) -> Float { Float::with_val(prec, v) }
fn pi(prec: u32) -> Float { Float::with_val(prec, Constant::Pi) }
fn eps_mpfr(prec: u32) -> Float { zf(prec, 1.0) >> (prec - 1) }
fn exp_(x: &Float) -> Float { Float::with_val(x.prec(), x.exp_ref()) }
fn ln_(x: &Float) -> Float { Float::with_val(x.prec(), x.ln_ref()) }
fn sqrt_(x: &Float) -> Float { Float::with_val(x.prec(), x.sqrt_ref()) }
fn abs_(x: &Float) -> Float { Float::with_val(x.prec(), x.abs_ref()) }
fn sincos_(x: &Float) -> (Float, Float) {
    let mut t: (Float, Float) = (Float::new(x.prec()), Float::new(x.prec()));
    t.assign(x.sin_cos_ref());
    t
}
fn atan2_(y: &Float, x: &Float) -> Float { Float::with_val(y.prec(), y.atan2_ref(x)) }
fn cos_(x: &Float) -> Float { Float::with_val(x.prec(), x.cos_ref()) }
fn sin_(x: &Float) -> Float { Float::with_val(x.prec(), x.sin_ref()) }

// explicit-completion arithmetic (rug reference ops are lazy)
fn add(a: &Float, b: &Float) -> Float { Float::with_val(a.prec(), a + b) }
fn sub(a: &Float, b: &Float) -> Float { Float::with_val(a.prec(), a - b) }
fn mul(a: &Float, b: &Float) -> Float { Float::with_val(a.prec(), a * b) }
fn div(a: &Float, b: &Float) -> Float { Float::with_val(a.prec(), a / b) }
fn neg(a: &Float) -> Float { Float::with_val(a.prec(), -a) }
fn hypot_(a: &Float, b: &Float) -> Float { sqrt_(&add(&mul(a, a), &mul(b, b))) }

fn ipow(base: &Float, mut e: usize) -> Float {
    let mut result = zf(base.prec(), 1.0);
    let mut b = base.clone();
    while e > 0 {
        if e & 1 == 1 {
            result *= &b;
        }
        e >>= 1;
        if e > 0 {
            b = Float::with_val(base.prec(), &b * &b);
        }
    }
    result
}

fn fact_mpfr(m: usize, prec: u32) -> Float {
    if m <= 1 {
        return zf(prec, 1.0);
    }
    let i = Integer::from(Integer::factorial(m as u32));
    Float::with_val(prec, &i)
}

fn binom_mpfr(n: usize, j: usize, prec: u32) -> Float {
    if j > n {
        return zf(prec, 0.0);
    }
    let num = Integer::from(Integer::factorial(n as u32));
    let den = Integer::from(Integer::factorial(j as u32)) * Integer::from(Integer::factorial((n - j) as u32));
    Float::with_val(prec, &num) / Float::with_val(prec, &den)
}

// zeta(2k): closed forms k<=6, direct sum m^{-2k} for k>=7 (tail < 2^{-(prec+20)})
fn zeta_even(k: usize, prec: u32) -> Float {
    let p = pi(prec);
    if k <= 6 {
        let (num, den): (f64, f64) = match k {
            1 => (1.0, 6.0),
            2 => (1.0, 90.0),
            3 => (1.0, 945.0),
            4 => (1.0, 9450.0),
            5 => (1.0, 93555.0),
            _ => (691.0, 638512875.0),
        };
        div(&mul(&ipow(&p, 2 * k), &zf(prec, num)), &zf(prec, den))
    } else {
        // M = ((2k-1) 2^{-(prec+20)})^{1/(1-2k)}  (tail after M terms < 2^{-(prec+20)})
        let c = mul(&(zf(prec, 1.0) >> (prec + 20)), &zf(prec, (2 * k - 1) as f64));
        let me = exp_(&div(&ln_(&c), &zf(prec, -((2 * k) as f64) + 1.0)));
        let m = me.to_f64().ceil() as u64 + 2;
        let mut sum = zf(prec, 1.0);
        for mi in 2..=m {
            sum += exp_(&mul(&zf(prec, -((2 * k) as f64)), &ln_(&zf(prec, mi as f64))));
        }
        sum
    }
}

// |B_{2k}|/(2k)! = 2 zeta(2k)/(2 pi)^{2k}  (cached per (k,prec); NOT inflated)
thread_local! {
    static ABF_CACHE: RefCell<HashMap<(usize, u32), Float>> = RefCell::new(HashMap::new());
}
fn abs_b_over_fact_mpfr(k: usize, prec: u32) -> Float {
    if let Some(v) = ABF_CACHE.with(|c| c.borrow().get(&(k, prec)).cloned()) {
        return v;
    }
    let z2k = zeta_even(k, prec);
    let twopi = mul(&zf(prec, 2.0), &pi(prec));
    let inv = exp_(&mul(&zf(prec, -(2.0 * k as f64)), &ln_(&twopi)));
    let v = mul(&mul(&zf(prec, 2.0), &z2k), &inv);
    ABF_CACHE.with(|c| c.borrow_mut().insert((k, prec), v.clone()));
    v
}

// B_{2k}/(2k(2k-1)) = (-1)^{k+1} |B_{2k}|/(2k)! * (2k-2)!   (log-Gamma Stirling coef)
fn b_over_2k_2kminus1_mpfr(k: usize, prec: u32) -> Float {
    let sign = if k % 2 == 1 { 1.0 } else { -1.0 };
    let abf = abs_b_over_fact_mpfr(k, prec);
    let f = Integer::from(Integer::factorial((2 * k - 2) as u32));
    mul(&mul(&zf(prec, sign), &abf), &Float::with_val(prec, &f))
}

fn bell_series_mpfr(lam_re: &[Float], lam_im: &[Float], m: usize, br: &mut [Float], bi: &mut [Float], prec: u32) {
    br[0] = zf(prec, 1.0);
    bi[0] = Float::new(prec);
    for j in 1..=m {
        let mut sr = Float::new(prec);
        let mut si = Float::new(prec);
        for r in 1..=j {
            let c = binom_mpfr(j - 1, r - 1, prec);
            let lr = &lam_re[r];
            let li = &lam_im[r];
            let bjr = &br[j - r];
            let bji = &bi[j - r];
            sr += mul(&c, &sub(&mul(lr, bjr), &mul(li, bji)));
            si += mul(&c, &add(&mul(lr, bji), &mul(li, bjr)));
        }
        br[j] = sr;
        bi[j] = si;
    }
}

struct EmDersM {
    re: Vec<Float>,
    im: Vec<Float>,
    err: Vec<Float>,
}

// Certified Euler-Maclaurin: zeta^(0..m_max)(s), a in (0,1]; a=1 gives zeta.
fn zeta_em_ders_mpfr(s_re: &Float, s_im: &Float, a: &Float, n: usize, k_max: usize, m_max: usize) -> EmDersM {
    let prec = s_re.prec();
    let delta = zf(prec, 0.1);
    let eps = eps_mpfr(prec);
    let mm = m_max + 1;
    let n_base = add(&zf(prec, n as f64), a);
    let ln_n = ln_(&n_base);
    let n_neg_sig = exp_(&mul(&neg(s_re), &ln_n)); // N^{-sigma}
    let n_pow = exp_(&mul(&sub(&zf(prec, 1.0), s_re), &ln_n)); // N^{1-sigma}
    let (s_ln, c_ln) = sincos_(&mul(s_im, &ln_n));
    let e_re = c_ln; // Re N^{-it}
    let e_im = neg(&s_ln); // Im N^{-it}

    let mut re = vec![Float::new(prec); mm];
    let mut im = vec![Float::new(prec); mm];
    let mut rc = vec![Float::new(prec); mm];
    let mut ic = vec![Float::new(prec); mm];
    let mut sum_mag = vec![Float::new(prec); mm];
    let mut angle_err = vec![Float::new(prec); mm];

    // main sums: sum_k (-ln(k+a))^m (k+a)^{-s}, Kahan per order
    for k in 0..n {
        let x = add(&zf(prec, k as f64), a);
        let lnx = ln_(&x);
        let mag = exp_(&mul(&neg(s_re), &lnx));
        let (sx, cx) = sincos_(&mul(s_im, &lnx));
        let tr = mul(&mag, &cx);
        let ti = mul(&neg(&mag), &sx);
        let ang = add(&mul(&abs_(&mul(s_im, &lnx)), &eps), &eps);
        let mut p = zf(prec, 1.0);
        for m in 0..=m_max {
            let v = mul(&p, &tr);
            let w = mul(&p, &ti);
            let yr = sub(&v, &rc[m]);
            let tn = add(&re[m], &yr);
            rc[m] = sub(&sub(&tn, &re[m]), &yr);
            re[m] = tn;
            let yi = sub(&w, &ic[m]);
            let tn2 = add(&im[m], &yi);
            ic[m] = sub(&sub(&tn2, &im[m]), &yi);
            im[m] = tn2;
            sum_mag[m] += mul(&abs_(&p), &mag);
            angle_err[m] += mul(&mul(&ang, &abs_(&p)), &mag);
            p = mul(&neg(&p), &lnx);
        }
    }

    // tail terms in closed form
    let b_re = mul(&n_pow, &e_re); // N^{1-s}
    let b_im = mul(&n_pow, &e_im);
    let ns_re = mul(&n_neg_sig, &e_re); // N^{-s}
    let ns_im = mul(&n_neg_sig, &e_im);
    let d_re = sub(s_re, &zf(prec, 1.0));
    let d_im = s_im.clone();
    let d2 = add(&mul(&d_re, &d_re), &mul(&d_im, &d_im));
    let w1_re = div(&d_re, &d2);
    let w1_im = div(&neg(&d_im), &d2);
    let mut wp_re = vec![Float::new(prec); m_max + 2];
    let mut wp_im = vec![Float::new(prec); m_max + 2];
    wp_re[1] = w1_re.clone();
    wp_im[1] = w1_im.clone();
    for p in 2..=m_max + 1 {
        wp_re[p] = sub(&mul(&wp_re[p - 1], &w1_re), &mul(&wp_im[p - 1], &w1_im));
        wp_im[p] = add(&mul(&wp_re[p - 1], &w1_im), &mul(&wp_im[p - 1], &w1_re));
    }
    let mag_b = hypot_(&b_re, &b_im);
    let mut tail_round = vec![Float::new(prec); mm];
    for m in 0..=m_max {
        let mut tr = Float::new(prec);
        let mut ti = Float::new(prec);
        let mut tmag = Float::new(prec);
        for j in 0..=m {
            let c = binom_mpfr(m, j, prec);
            let lj = ipow(&neg(&ln_n), j);
            let sign = if (m - j) % 2 == 0 { 1.0 } else { -1.0 };
            let cf = mul(&mul(&mul(&zf(prec, sign), &fact_mpfr(m - j, prec)), &c), &lj);
            let p = m - j + 1;
            let vr = sub(&mul(&b_re, &wp_re[p]), &mul(&b_im, &wp_im[p]));
            let vi = add(&mul(&b_re, &wp_im[p]), &mul(&b_im, &wp_re[p]));
            tr += mul(&cf, &vr);
            ti += mul(&cf, &vi);
            tmag += mul(&mul(&abs_(&cf), &mag_b), &hypot_(&wp_re[p], &wp_im[p]));
        }
        let um = mul(&zf(prec, 0.5), &ipow(&neg(&ln_n), m));
        let ur = mul(&um, &ns_re);
        let ui = mul(&um, &ns_im);
        re[m] += add(&tr, &ur);
        im[m] += add(&ti, &ui);
        tail_round[m] = mul(&mul(&zf(prec, 4.0), &eps), &add(&tmag, &mul(&abs_(&um), &n_neg_sig)));
    }

    // Bernoulli corrections with Bell of Pochhammer log-derivatives
    let mut corr_round = vec![Float::new(prec); mm];
    let mut lam_re = vec![Float::new(prec); m_max + 2];
    let mut lam_im = vec![Float::new(prec); m_max + 2];
    let mut bell_re = vec![Float::new(prec); m_max + 2];
    let mut bell_im = vec![Float::new(prec); m_max + 2];
    let mut pwr_re = vec![Float::new(prec); m_max + 2];
    let mut pwr_im = vec![Float::new(prec); m_max + 2];
    let mut pr_re = vec![Float::new(prec); m_max + 2];
    let mut pr_im = vec![Float::new(prec); m_max + 2];
    let mut rem_prod = zf(prec, 1.0);
    for k in 1..=k_max {
        let mfac = 2 * k - 1;
        let mut p_re = zf(prec, 1.0);
        let mut p_im = Float::new(prec);
        for r in 1..=m_max {
            pr_re[r] = Float::new(prec);
            pr_im[r] = Float::new(prec);
        }
        for l in 0..mfac {
            let xr = add(s_re, &zf(prec, l as f64));
            let xi = s_im.clone();
            let x2 = add(&mul(&xr, &xr), &mul(&xi, &xi));
            let ir = div(&xr, &x2);
            let ii = div(&neg(&xi), &x2);
            pwr_re[1] = ir.clone();
            pwr_im[1] = ii.clone();
            for r in 2..=m_max {
                pwr_re[r] = sub(&mul(&pwr_re[r - 1], &ir), &mul(&pwr_im[r - 1], &ii));
                pwr_im[r] = add(&mul(&pwr_re[r - 1], &ii), &mul(&pwr_im[r - 1], &ir));
            }
            for r in 1..=m_max {
                pr_re[r] += &pwr_re[r];
                pr_im[r] += &pwr_im[r];
            }
            let nr = sub(&mul(&p_re, &xr), &mul(&p_im, &xi));
            let ni = add(&mul(&p_re, &xi), &mul(&p_im, &xr));
            p_re = nr;
            p_im = ni;
            let infl = add(&hypot_(&xr, &xi), &delta);
            rem_prod *= div(&infl, &n_base);
        }
        for r in 1..=m_max {
            let sign = if (r - 1) % 2 == 0 { 1.0 } else { -1.0 };
            let cf = mul(&zf(prec, sign), &fact_mpfr(r - 1, prec));
            lam_re[r] = mul(&cf, &pr_re[r]);
            lam_im[r] = mul(&cf, &pr_im[r]);
        }
        bell_series_mpfr(&lam_re, &lam_im, m_max, &mut bell_re, &mut bell_im, prec);
        let coef = abs_b_over_fact_mpfr(k, prec);
        let sign = if k % 2 == 1 { 1.0 } else { -1.0 };
        let nfac = exp_(&mul(&zf(prec, (2 * k - 1) as f64), &neg(&ln_n))); // N^{-(2k-1)}
        let nsf_re = mul(&mul(&n_neg_sig, &nfac), &e_re);
        let nsf_im = mul(&mul(&n_neg_sig, &nfac), &e_im);
        let nsf_mag = mul(&n_neg_sig, &nfac);
        for m in 0..=m_max {
            let mut cr = Float::new(prec);
            let mut ci = Float::new(prec);
            let mut cmag = Float::new(prec);
            for j in 0..=m {
                let c = binom_mpfr(m, j, prec);
                let lj = ipow(&neg(&ln_n), m - j);
                let dr_ = sub(&mul(&p_re, &bell_re[j]), &mul(&p_im, &bell_im[j]));
                let di_ = add(&mul(&p_re, &bell_im[j]), &mul(&p_im, &bell_re[j]));
                let vr = sub(&mul(&dr_, &nsf_re), &mul(&di_, &nsf_im));
                let vi = add(&mul(&dr_, &nsf_im), &mul(&di_, &nsf_re));
                cr += mul(&mul(&c, &lj), &vr);
                ci += mul(&mul(&c, &lj), &vi);
                cmag += mul(&mul(&mul(&c, &abs_(&lj)), &hypot_(&dr_, &di_)), &nsf_mag);
            }
            let sc = mul(&zf(prec, sign), &coef);
            re[m] += mul(&sc, &cr);
            im[m] += mul(&sc, &ci);
            corr_round[m] += mul(&mul(&mul(&mul(&zf(prec, (3 * k + 20) as f64), &eps), &coef), &cmag), &zf(prec, 1.02));
        }
    }

    // certified remainder: |R_K^(m)(s)| <= m!/delta^m * 2|B_2K|/(2K)! * prod * N^{1-(sigma-delta)} / denom
    let last = (2 * k_max as i64 - 1) as f64;
    let lr_ = add(s_re, &zf(prec, last));
    let last_mag = hypot_(&lr_, s_im);
    let infl = add(&last_mag, &delta);
    let base_rem = mul(&mul(&zf(prec, 2.0), &abs_b_over_fact_mpfr(k_max, prec)), &zf(prec, COEF_INFL));
    let n_pow_infl = exp_(&mul(&sub(&zf(prec, 1.0), &sub(s_re, &delta)), &ln_n));
    let denom = add(&sub(s_re, &delta), &zf(prec, ((2 * k_max) as f64) - 1.0));
    let mut err = vec![Float::new(prec); mm];
    for m in 0..=m_max {
        let mfac_b = div(&fact_mpfr(m, prec), &ipow(&delta, m));
        let rem = div(
            &mul(&mul(&mul(&mul(&mfac_b, &base_rem), &rem_prod), &div(&infl, &n_base)), &n_pow_infl),
            &denom,
        );
        let value_round = add(
            &add(&add(&add(&mul(&mul(&zf(prec, 4.0), &eps), &sum_mag[m]), &angle_err[m]), &tail_round[m]), &corr_round[m]),
            &mul(&mul(&zf(prec, 4.0), &eps), &add(&abs_(&re[m]), &abs_(&im[m]))),
        );
        err[m] = add(&value_round, &rem);
    }
    EmDersM { re, im, err }
}

// Gamma via Stirling: lnGamma(z) = (z-1/2)ln z - z + ln(2pi)/2 + sum_k B_{2k}/(2k(2k-1)) z^{1-2k}.
// Terms are added while they decrease; truncation error ~ last added term.
fn gamma_complex_stirling_mpfr(re: &Float, im: &Float) -> (Float, Float, Float) {
    let prec = re.prec();
    let eps = eps_mpfr(prec);
    let z2 = add(&mul(re, re), &mul(im, im));
    let zmag = sqrt_(&z2);
    let lnz_r = ln_(&zmag);
    let lnz_i = atan2_(im, re);
    let a = sub(re, &zf(prec, 0.5));
    let b = im.clone();
    let mut lr = sub(&mul(&a, &lnz_r), &mul(&b, &lnz_i));
    let mut li = add(&mul(&a, &lnz_i), &mul(&b, &lnz_r));
    lr += add(&neg(re), &mul(&zf(prec, 0.5), &ln_(&mul(&zf(prec, 2.0), &pi(prec)))));
    li += neg(im);
    let inv_re = div(re, &z2);
    let inv_im = div(&neg(im), &z2);
    let mut p_re = inv_re.clone();
    let mut p_im = inv_im.clone();
    let mut prev_mag = Float::new(prec);
    let mut trunc = Float::new(prec);
    let mut terms_scale = Float::new(prec);
    let mut k_used: usize = 0;
    for k in 1..=GAMMA_TERMS_MAX {
        let coef = b_over_2k_2kminus1_mpfr(k, prec);
        let tr = mul(&coef, &p_re);
        let ti = mul(&coef, &p_im);
        let tmag = hypot_(&tr, &ti);
        terms_scale += &tmag;
        if k > 1 && &tmag > &prev_mag {
            trunc = prev_mag.clone();
            break;
        }
        lr += tr;
        li += ti;
        prev_mag = tmag;
        k_used = k;
        let nr = sub(&mul(&p_re, &inv_re), &mul(&p_im, &inv_im));
        let ni = add(&mul(&p_re, &inv_im), &mul(&p_im, &inv_re));
        p_re = nr;
        p_im = ni;
    }
    if k_used == GAMMA_TERMS_MAX {
        trunc = prev_mag;
    }
    let m = exp_(&lr);
    let gr = mul(&m, &cos_(&li));
    let gi = mul(&m, &sin_(&li));
    let err = mul(&m, &add(&add(&trunc, &mul(&eps, &terms_scale)), &eps));
    (gr, gi, err)
}

// psi^(m)(z), z complex: shift sum + Stirling. Returns (re, im, err).
fn polygamma_mpfr(m: usize, z_re: &Float, z_im: &Float, prec: u32) -> (Float, Float, Float) {
    let eps = eps_mpfr(prec);
    let mfact = fact_mpfr(m, prec);
    let mut sr = Float::new(prec);
    let mut si = Float::new(prec);
    let mut shift_scale = Float::new(prec);
    for l in 0..SHIFT {
        let xr = add(z_re, &zf(prec, l as f64));
        let xi = z_im.clone();
        let x2 = add(&mul(&xr, &xr), &mul(&xi, &xi));
        let ir = div(&xr, &x2);
        let ii = div(&neg(&xi), &x2);
        let mut pr = zf(prec, 1.0);
        let mut pi = Float::new(prec);
        for _ in 0..(m + 1) {
            let nr = sub(&mul(&pr, &ir), &mul(&pi, &ii));
            let ni = add(&mul(&pr, &ii), &mul(&pi, &ir));
            pr = nr;
            pi = ni;
        }
        let sign = if m % 2 == 0 { -1.0 } else { 1.0 };
        let sc = mul(&zf(prec, sign), &mfact);
        sr += mul(&sc, &pr);
        si += mul(&sc, &pi);
        shift_scale += hypot_(&mul(&sc, &pr), &mul(&sc, &pi));
    }
    let wr = add(z_re, &zf(prec, SHIFT as f64));
    let wi = z_im.clone();
    let w2 = add(&mul(&wr, &wr), &mul(&wi, &wi));
    let inv_re = div(&wr, &w2);
    let inv_im = div(&neg(&wi), &w2);
    let maxp = m + 2 * KP + 1;
    let mut ip_re = vec![Float::new(prec); maxp + 1];
    let mut ip_im = vec![Float::new(prec); maxp + 1];
    ip_re[1] = inv_re.clone();
    ip_im[1] = inv_im.clone();
    for p in 2..=maxp {
        ip_re[p] = sub(&mul(&ip_re[p - 1], &inv_re), &mul(&ip_im[p - 1], &inv_im));
        ip_im[p] = add(&mul(&ip_re[p - 1], &inv_im), &mul(&ip_im[p - 1], &inv_re));
    }
    let (mut vr, mut vi) = (Float::new(prec), Float::new(prec));
    let mut stir_scale = Float::new(prec);
    let mut trunc = Float::new(prec);
    if m == 0 {
        // psi(w) = ln w - 1/(2w) + sum_k (-1)^k |B_{2k}|/(2k) w^{-2k}
        let ln_re = mul(&zf(prec, 0.5), &ln_(&w2));
        let ln_im = atan2_(&wi, &wr);
        vr = sub(&ln_re, &mul(&zf(prec, 0.5), &inv_re));
        vi = sub(&ln_im, &mul(&zf(prec, 0.5), &inv_im));
        stir_scale = add(&abs_(&vr), &abs_(&vi));
        let mut prev = Float::new(prec);
        let mut broken = false;
        for k in 1..=KP {
            let coef = mul(
                &mul(&zf(prec, if k % 2 == 0 { 1.0 } else { -1.0 }), &abs_b_over_fact_mpfr(k, prec)),
                &fact_mpfr(2 * k - 1, prec),
            );
            let p = 2 * k;
            let tr = mul(&coef, &ip_re[p]);
            let ti = mul(&coef, &ip_im[p]);
            let tmag = hypot_(&tr, &ti);
            stir_scale += &tmag;
            if k > 1 && &tmag > &prev {
                trunc = prev.clone();
                broken = true;
                break;
            }
            vr += tr;
            vi += ti;
            prev = tmag;
        }
        if !broken {
            trunc = prev;
        }
    } else {
        // psi^(m)(w) = (-1)^{m-1}(m-1)! w^{-m} + (-1)^{m+1} m! w^{-(m+1)}/2
        //            + sum_k (-1)^{m+k} |B_{2k}| (2k+m-1)!/(2k)! w^{-(2k+m)}
        let s1 = if (m - 1) % 2 == 0 { 1.0 } else { -1.0 };
        let s2 = if (m + 1) % 2 == 0 { 1.0 } else { -1.0 };
        vr += mul(&mul(&zf(prec, s1), &fact_mpfr(m - 1, prec)), &ip_re[m]);
        vi += mul(&mul(&zf(prec, s1), &fact_mpfr(m - 1, prec)), &ip_im[m]);
        vr += mul(&mul(&mul(&zf(prec, s2), &zf(prec, 0.5)), &mfact), &ip_re[m + 1]);
        vi += mul(&mul(&mul(&zf(prec, s2), &zf(prec, 0.5)), &mfact), &ip_im[m + 1]);
        stir_scale = add(&abs_(&vr), &abs_(&vi));
        let mut prev = Float::new(prec);
        let mut broken = false;
        for k in 1..=KP {
            let sgn_k = if k % 2 == 1 { 1.0 } else { -1.0 };
            let mut rising = zf(prec, 1.0);
            for j in 1..m {
                rising *= zf(prec, (2 * k + j) as f64);
            }
            let coef = mul(
                &mul(&mul(&mul(&zf(prec, s2), &zf(prec, sgn_k)), &abs_b_over_fact_mpfr(k, prec)), &fact_mpfr(2 * k, prec)),
                &rising,
            );
            let p = 2 * k + m;
            let tr = mul(&coef, &ip_re[p]);
            let ti = mul(&coef, &ip_im[p]);
            let tmag = hypot_(&tr, &ti);
            stir_scale += &tmag;
            if k > 1 && &tmag > &prev {
                trunc = prev.clone();
                broken = true;
                break;
            }
            vr += tr;
            vi += ti;
            prev = tmag;
        }
        if !broken {
            trunc = prev;
        }
    }
    let err = add(&mul(&eps, &add(&shift_scale, &stir_scale)), &trunc);
    (add(&sr, &vr), add(&si, &vi), err)
}

// L_n = (d/ds)^n log zeta(s), n=1..m_max, with certified error recursion dl.
fn zeta_logderivs_mpfr(s_re: &Float, s_im: &Float, m_max: usize, prec: u32, n_em: usize) -> (Vec<Float>, Vec<Float>, Vec<Float>) {
    let d = zeta_em_ders_mpfr(s_re, s_im, &zf(prec, 1.0), n_em, 40, m_max);
    let eps = eps_mpfr(prec);
    let z2 = add(&mul(&d.re[0], &d.re[0]), &mul(&d.im[0], &d.im[0]));
    let zmag = sqrt_(&z2);
    let mut lr = vec![Float::new(prec); m_max + 1];
    let mut li = vec![Float::new(prec); m_max + 1];
    let mut dl = vec![Float::new(prec); m_max + 1];
    lr[1] = div(&add(&mul(&d.re[1], &d.re[0]), &mul(&d.im[1], &d.im[0])), &z2);
    li[1] = div(&sub(&mul(&d.im[1], &d.re[0]), &mul(&d.re[1], &d.im[0])), &z2);
    dl[1] = div(&add(&mul(&d.err[1], &zmag), &mul(&hypot_(&d.re[1], &d.im[1]), &d.err[0])), &z2);
    for n in 2..=m_max {
        let mut sr = d.re[n].clone();
        let mut si = d.im[n].clone();
        let mut dnum = d.err[n].clone();
        for j in 1..n {
            let c = binom_mpfr(n - 1, j - 1, prec);
            let cr = sub(&mul(&d.re[n - j], &lr[j]), &mul(&d.im[n - j], &li[j]));
            let ci = add(&mul(&d.re[n - j], &li[j]), &mul(&d.im[n - j], &lr[j]));
            sr -= mul(&c, &cr);
            si -= mul(&c, &ci);
            let zmj = hypot_(&d.re[n - j], &d.im[n - j]);
            let lj_mag = hypot_(&lr[j], &li[j]);
            dnum += mul(&c, &add(&mul(&d.err[n - j], &lj_mag), &mul(&zmj, &dl[j])));
        }
        lr[n] = div(&add(&mul(&sr, &d.re[0]), &mul(&si, &d.im[0])), &z2);
        li[n] = div(&sub(&mul(&si, &d.re[0]), &mul(&sr, &d.im[0])), &z2);
        let ln_mag = hypot_(&lr[n], &li[n]);
        dl[n] = add(&div(&add(&dnum, &mul(&ln_mag, &d.err[0])), &zmag), &mul(&eps, &ln_mag));
    }
    (lr, li, dl)
}

// u^(n)(t) = (d/dt)^n log Xi(t), n=1..m_max. Returns (u, max|Im|, du).
fn logxi_derivs_mpfr(t: &Float, m_max: usize, prec: u32, n_em: usize) -> (Vec<Float>, Float, Vec<Float>) {
    let s_re = zf(prec, 0.5);
    let s_im = t.clone();
    let (lr, li, dl) = zeta_logderivs_mpfr(&s_re, &s_im, m_max, prec, n_em);
    let eps = eps_mpfr(prec);
    let lnpi = ln_(&pi(prec));
    let s2 = add(&mul(&s_re, &s_re), &mul(&s_im, &s_im));
    let inv_re = div(&s_re, &s2);
    let inv_im = div(&neg(&s_im), &s2);
    let dm = sub(&s_re, &zf(prec, 1.0));
    let d2 = add(&mul(&dm, &dm), &mul(&s_im, &s_im));
    let inv1_re = div(&dm, &d2);
    let inv1_im = div(&neg(&s_im), &d2);
    let mut ip_re = vec![Float::new(prec); m_max + 2];
    let mut ip_im = vec![Float::new(prec); m_max + 2];
    let mut ip1_re = vec![Float::new(prec); m_max + 2];
    let mut ip1_im = vec![Float::new(prec); m_max + 2];
    ip_re[1] = inv_re.clone();
    ip_im[1] = inv_im.clone();
    ip1_re[1] = inv1_re.clone();
    ip1_im[1] = inv1_im.clone();
    for p in 2..=m_max + 1 {
        ip_re[p] = sub(&mul(&ip_re[p - 1], &inv_re), &mul(&ip_im[p - 1], &inv_im));
        ip_im[p] = add(&mul(&ip_re[p - 1], &inv_im), &mul(&ip_im[p - 1], &inv_re));
        ip1_re[p] = sub(&mul(&ip1_re[p - 1], &inv1_re), &mul(&ip1_im[p - 1], &inv1_im));
        ip1_im[p] = add(&mul(&ip1_re[p - 1], &inv1_im), &mul(&ip1_im[p - 1], &inv1_re));
    }
    let half_t = mul(&s_im, &zf(prec, 0.5));
    let mut ps_re = vec![Float::new(prec); m_max];
    let mut ps_im = vec![Float::new(prec); m_max];
    let mut dps = vec![Float::new(prec); m_max];
    for m in 0..m_max {
        let (pr, pi, e) = polygamma_mpfr(m, &zf(prec, 0.25), &half_t, prec);
        ps_re[m] = pr;
        ps_im[m] = pi;
        dps[m] = e;
    }
    let mut u = vec![Float::new(prec); m_max + 1];
    let mut du = vec![Float::new(prec); m_max + 1];
    let mut max_imag = Float::new(prec);
    for n in 1..=m_max {
        let (ar, ai): (Float, Float);
        let da: Float;
        if n == 1 {
            ar = add(
                &add(&sub(&add(&ip_re[1], &ip1_re[1]), &mul(&zf(prec, 0.5), &lnpi)), &mul(&zf(prec, 0.5), &ps_re[0])),
                &lr[1],
            );
            ai = add(&add(&ip_im[1], &ip1_im[1]), &add(&mul(&zf(prec, 0.5), &ps_im[0]), &li[1]));
            da = add(&add(&dl[1], &mul(&zf(prec, 0.5), &dps[0])), &mul(&eps, &add(&abs_(&ar), &abs_(&ai))));
        } else {
            let sgn = if (n - 1) % 2 == 0 { 1.0 } else { -1.0 };
            let cf = mul(&zf(prec, sgn), &fact_mpfr(n - 1, prec));
            let halfn = div(&zf(prec, 1.0), &zf(prec, (1u64 << n) as f64));
            ar = add(&add(&mul(&cf, &add(&ip_re[n], &ip1_re[n])), &mul(&halfn, &ps_re[n - 1])), &lr[n]);
            ai = add(&add(&mul(&cf, &add(&ip_im[n], &ip1_im[n])), &mul(&halfn, &ps_im[n - 1])), &li[n]);
            da = add(&add(&dl[n], &mul(&halfn, &dps[n - 1])), &mul(&eps, &add(&abs_(&ar), &abs_(&ai))));
        }
        let (ur, ui) = match n % 4 {
            0 => (ar, ai),
            1 => (neg(&ai), ar),
            2 => (neg(&ar), neg(&ai)),
            _ => (ai, neg(&ar)),
        };
        let ui_abs = abs_(&ui);
        if ui_abs > max_imag {
            max_imag = ui_abs;
        }
        u[n] = ur;
        du[n] = da;
    }
    (u, max_imag, du)
}

// xi(1/2+it) = 0.5*s(s-1) * pi^{-s/2} * Gamma(1/4+it/2) * zeta(s). Returns (re, im, err).
fn xi_complex_mpfr(t: &Float) -> (Float, Float, Float) {
    let prec = t.prec();
    let s_re = zf(prec, 0.5);
    let s_im = t.clone();
    let lnpi = ln_(&pi(prec));
    let ln_pow_re = exp_(&mul(&zf(prec, -0.25), &lnpi));
    let arg = mul(&mul(&neg(&s_im), &zf(prec, 0.5)), &lnpi);
    let (sn, cs) = sincos_(&arg);
    let pi_pow_re = mul(&ln_pow_re, &cs);
    let pi_pow_im = mul(&ln_pow_re, &sn);
    let ssm = sub(&zf(prec, -0.25), &mul(t, t));
    let b = mul(t, &zf(prec, 0.5));
    let (gr, gi, dg) = gamma_complex_stirling_mpfr(&zf(prec, 0.25), &b);
    let z = zeta_em_ders_mpfr(&s_re, &s_im, &zf(prec, 1.0), N_ZETA, 40, 0);
    let re_f = mul(&zf(prec, 0.5), &ssm);
    let a_re = mul(&re_f, &pi_pow_re);
    let a_im = mul(&re_f, &pi_pow_im);
    let m_re = sub(&mul(&a_re, &gr), &mul(&a_im, &gi));
    let m_im = add(&mul(&a_re, &gi), &mul(&a_im, &gr));
    let xi_re = sub(&mul(&m_re, &z.re[0]), &mul(&m_im, &z.im[0]));
    let xi_im = add(&mul(&m_re, &z.im[0]), &mul(&m_im, &z.re[0]));
    let a_mag = mul(&abs_(&re_f), &ln_pow_re);
    let g_mag = hypot_(&gr, &gi);
    let z_mag = hypot_(&z.re[0], &z.im[0]);
    let eps = eps_mpfr(prec);
    let dxi = add(&mul(&a_mag, &add(&mul(&g_mag, &z.err[0]), &mul(&z_mag, &dg))), &mul(&eps, &hypot_(&xi_re, &xi_im)));
    (xi_re, xi_im, dxi)
}

// L_k = Xi^2 (B_k^2 - B_{k-1} B_{k+1}) with certified error. Returns (L, err, q, scale).
fn lk_analytic_mpfr(t: &Float, k: usize, prec: u32, n_em: usize) -> (Float, Float, Float, Float) {
    let m_max = k + 1;
    let (u, _mi, du) = logxi_derivs_mpfr(t, m_max, prec, n_em);
    let eps = eps_mpfr(prec);
    let mut b = vec![Float::new(prec); m_max + 1];
    let mut db = vec![Float::new(prec); m_max + 1];
    let mut scale = vec![Float::new(prec); m_max + 1];
    b[0] = zf(prec, 1.0);
    scale[0] = zf(prec, 1.0);
    for j in 1..=m_max {
        let mut s = Float::new(prec);
        let mut sc = Float::new(prec);
        let mut ds = Float::new(prec);
        for m in 0..j {
            let c = binom_mpfr(j - 1, m, prec);
            let term = mul(&mul(&c, &u[m + 1]), &b[j - 1 - m]);
            s += &term;
            sc += mul(&mul(&c, &abs_(&u[m + 1])), &abs_(&b[j - 1 - m]));
            ds += mul(&c, &add(&mul(&du[m + 1], &abs_(&b[j - 1 - m])), &mul(&abs_(&u[m + 1]), &db[j - 1 - m])));
        }
        b[j] = s;
        scale[j] = sc.clone();
        db[j] = add(&ds, &mul(&eps, &sc));
    }
    let q = sub(&mul(&b[k], &b[k]), &mul(&b[k - 1], &b[k + 1]));
    let dq = add(
        &add(
            &add(&mul(&mul(&zf(prec, 2.0), &abs_(&b[k])), &db[k]), &mul(&abs_(&b[k - 1]), &db[k + 1])),
            &mul(&abs_(&b[k + 1]), &db[k - 1]),
        ),
        &mul(
            &eps,
            &add(
                &add(&mul(&mul(&zf(prec, 2.0), &abs_(&b[k])), &scale[k]), &mul(&scale[k - 1], &abs_(&b[k + 1]))),
                &mul(&abs_(&b[k - 1]), &scale[k + 1]),
            ),
        ),
    );
    let (xi, _xi_im, dxi) = xi_complex_mpfr(t);
    let xi2 = mul(&xi, &xi);
    let dxi2 = add(&mul(&mul(&zf(prec, 2.0), &abs_(&xi)), &dxi), &mul(&eps, &xi2));
    let l = mul(&xi2, &q);
    let err = add(&add(&mul(&xi2, &dq), &mul(&abs_(&q), &dxi2)), &mul(&eps, &abs_(&l)));
    (l, err, q, scale[k].clone())
}

fn fmt_sci(f: &Float, digits: usize) -> String {
    if f.is_zero() {
        return "0".to_string();
    }
    let prec = f.prec();
    let ln10 = ln_(&zf(prec, 10.0));
    let mut e = (div(&ln_(&abs_(f)), &ln10)).floor().to_f64();
    let scale = exp_(&mul(&zf(prec, -e), &ln10));
    let mut m = mul(f, &scale);
    let mut s = m.to_string_radix(10, Some(digits));
    if s.starts_with("10") {
        e += 1.0;
        m = mul(f, &exp_(&mul(&zf(prec, -e), &ln10)));
        s = m.to_string_radix(10, Some(digits));
    }
    format!("{}e{:+.0}", s, e as i64)
}

fn print_result(t: f64, k: usize, l: &Float, err: &Float, q: &Float, sc: &Float, tag: &str) {
    let lf = l.to_f64();
    let ef = err.to_f64();
    let verdict = if lf.abs() < ef {
        "INCONCLUSIVE"
    } else if lf > 0.0 {
        "POSITIVE (RH-consistent)"
    } else {
        "NEGATIVE -> ESCALATE"
    };
    println!(
        "t={:5.1} k={:2} [{}]: L_k = {:+.6e}  err<{:+.1e}  bracket q={:+.6e}  Bk_scale={:.1e}  -> {}",
        t, k, tag, lf, ef, q.to_f64(), sc.to_f64(), verdict
    );
    println!("      L_k (36 digits) = {}", fmt_sci(l, 36));
}

fn main() {
    let prec = 200u32;
    let prec_x = 256u32;
    println!("=== 8D L_k — MPFR (rug) zeta-direct, k=18/19/20 @ t=40, {} bits ===", prec);
    println!("L_k(t) = (Xi^(k))^2 - Xi^(k-1) Xi^(k+1), Xi(t) = xi(1/2+it).");
    println!("L_k >= 0 for all (t,k) is NECESSARY for RH (LP-class log-concavity). Positive = RH-consistent only.\n");

    // 0. |B_2k|/(2k)! cross-check: MPFR vs f64 table
    println!("-- |B_2k|/(2k)!: MPFR vs f64 table --");
    for k in 1..=12 {
        let mp = div(&abs_b_over_fact_mpfr(k, prec), &zf(prec, COEF_INFL));
        let f64v = em::abs_b_over_fact(k) / COEF_INFL;
        let rel = (mp.to_f64() - f64v).abs() / f64v.abs();
        println!("k={:2}: mpfr={:.17e}  f64={:.17e}  rel={:.1e}", k, mp.to_f64(), f64v, rel);
    }

    // 0b. polygamma real-axis sanity vs known constants
    println!("\n-- polygamma sanity (real axis, vs hardcoded constants) --");
    let c0 = Float::with_val(prec, Float::parse("-1.9635100260214234794409763329987555671931596046604373773475969").unwrap());
    let c1 = Float::with_val(prec, Float::parse("-0.5772156649015328606065120900824024310421593359399235988057672").unwrap());
    let c2 = Float::with_val(prec, Float::parse("4.9348022005446793094172454999380755676568497036203953132066743").unwrap());
    let (p0, _, e0) = polygamma_mpfr(0, &zf(prec, 0.5), &zf(prec, 0.0), prec);
    let (p1, _, e1) = polygamma_mpfr(0, &zf(prec, 1.0), &zf(prec, 0.0), prec);
    let (p2, _, e2) = polygamma_mpfr(1, &zf(prec, 0.5), &zf(prec, 0.0), prec);
    println!("psi(1/2) = {}  |dev|={:.1e}", fmt_sci(&p0, 24), abs_(&sub(&p0, &c0)).to_f64());
    println!("psi(1)   = {}  |dev|={:.1e}", fmt_sci(&p1, 24), abs_(&sub(&p1, &c1)).to_f64());
    println!("psi'(1/2)= {}  |dev|={:.1e}", fmt_sci(&p2, 24), abs_(&sub(&p2, &c2)).to_f64());
    // psi(1/4) = -gamma - pi/2 - 3 ln 2 = -4.2274535333762654080895301460966835773672444387... (the point where the f64 m=0 sign bug showed err ~1e-4)
    let c_quarter = Float::with_val(prec, Float::parse("-4.2274535333762654080895301460966835773672444387082422716552869").unwrap());
    let (p3, _, e3) = polygamma_mpfr(0, &zf(prec, 0.25), &zf(prec, 0.0), prec);
    println!("psi(1/4) = {}  |dev|={:.1e}", fmt_sci(&p3, 24), abs_(&sub(&p3, &c_quarter)).to_f64());

    // 1. certified zeta error at decision/control points
    println!("\n-- certified zeta error (n={}) --", N_ZETA);
    for &(t, mm) in &[(40.0f64, 21usize), (33.6, 9), (56.5, 4)] {
        let d = zeta_em_ders_mpfr(&zf(prec, 0.5), &zf(prec, t), &zf(prec, 1.0), N_ZETA, 40, mm);
        println!(
            "t={:5.1}: err(zeta)={:.2e} err(zeta')={:.2e} err(zeta^({}))={:.2e}  zeta={:+.6e}{:+.6e}i",
            t, d.err[0].to_f64(), d.err[1].to_f64(), mm, d.err[mm].to_f64(), d.re[0].to_f64(), d.im[0].to_f64()
        );
    }

    // 2. xi sanity
    println!("\n-- xi sanity --");
    let g14 = Float::with_val(prec, Float::parse("3.6256099082219083119306851558676720029951676828800654674333779995699192435387").unwrap());
    let z05 = zeta_em_ders_mpfr(&zf(prec, 0.5), &zf(prec, 0.0), &zf(prec, 1.0), N_ZETA, 40, 0);
    let lnpi = ln_(&pi(prec));
    let pi_pow = exp_(&mul(&zf(prec, -0.25), &lnpi));
    let xi0 = mul(&mul(&mul(&zf(prec, -0.125), &pi_pow), &g14), &z05.re[0]);
    println!("Xi(0) = {}  (true 0.497120778188314...; zeta(1/2)={:.17e} err={:.1e})", fmt_sci(&xi0, 20), z05.re[0].to_f64(), z05.err[0].to_f64());
    let zeros = [
        "14.134725141734693790457251983562470270784",
        "21.022039638771554992628479593896902777334",
        "25.010857580145688763213790992562821818660",
        "30.424876125859513210311897530584091320182",
    ];
    for (i, gs) in zeros.iter().enumerate() {
        let g = Float::with_val(prec, Float::parse(gs).unwrap());
        let (r, im_, _) = xi_complex_mpfr(&g);
        println!("|Xi(gamma_{})| at t={} = {:.3e}  (Re={:+.3e} Im={:+.3e})", i + 1, gs, hypot_(&r, &im_).to_f64(), r.to_f64(), im_.to_f64());
    }
    let mid = [7.6f64, 17.6, 23.05, 27.7, 31.7, 34.7, 39.2, 42.1, 45.7, 48.9, 51.4, 54.7, 57.9, 62.1, 66.1];
    let exp_sign: Vec<i32> = (0..mid.len()).map(|m| if m % 2 == 0 { 1 } else { -1 }).collect();
    let mut ok = true;
    for (i, &t) in mid.iter().enumerate() {
        let r = xi_complex_mpfr(&zf(prec, t)).0;
        let s = if r >= 0.0 { 1 } else { -1 };
        let good = s == exp_sign[i];
        ok &= good;
        println!("Xi({:5.1}) = {:+.4e}  sign {:>+2} expect {:>+2}  {}", t, r.to_f64(), s, exp_sign[i], if good { "OK" } else { "MISMATCH" });
    }
    for &t in &[33.6f64, 35.5, 40.0, 56.5] {
        let r = xi_complex_mpfr(&zf(prec, t)).0;
        println!("Xi({:5.1}) (flagged) = {:+.4e}  sign {:>+2}", t, r.to_f64(), if r >= 0.0 { 1 } else { -1 });
    }
    println!("sign pattern: {}", if ok { "ALL OK" } else { "FAILED" });

    // 3. controls + main points
    println!("\n-- L_k (analytic EM route, MPFR, n={}) --", N_ZETA);
    for &(t, k) in &[(40.0f64, 3usize), (33.6, 8), (56.5, 3), (35.5, 4)] {
        let (l, err, q, sc) = lk_analytic_mpfr(&zf(prec, t), k, prec, N_ZETA);
        print_result(t, k, &l, &err, &q, &sc, "control");
    }
    for &(t, k) in &[(40.0f64, 18usize), (40.0, 19), (40.0, 20)] {
        let (l, err, q, sc) = lk_analytic_mpfr(&zf(prec, t), k, prec, N_ZETA);
        print_result(t, k, &l, &err, &q, &sc, "main");
        let (u, mi, _du) = logxi_derivs_mpfr(&zf(prec, t), k + 1, prec, N_ZETA);
        println!(
            "      u^({:2})..u^({:3}): {}  (max|Im u|={:.1e})",
            k - 2,
            k + 1,
            (k - 2..=k + 1).map(|n| format!("u^{}={:+.3e}", n, u[n].to_f64())).collect::<Vec<_>>().join(" "),
            mi.to_f64()
        );
    }

    // 4. cross-checks
    println!("\n-- cross-checks (rounding: 200 vs 256 bit; EM truncation: n=600 vs 900) --");
    let l200 = lk_analytic_mpfr(&zf(prec, 40.0), 20, prec, N_ZETA).0;
    let l256 = lk_analytic_mpfr(&zf(prec_x, 40.0), 20, prec_x, N_ZETA).0;
    println!("k=20 t=40: L(200bit)={}  L(256bit)={}  |diff|={:.2e}", fmt_sci(&l200, 36), fmt_sci(&l256, 36), abs_(&sub(&l256, &l200)).to_f64());
    let l900 = lk_analytic_mpfr(&zf(prec, 40.0), 20, prec, 900).0;
    println!("k=20 t=40: L(n=600)={}  L(n=900)={}  |diff|={:.2e}", fmt_sci(&l200, 36), fmt_sci(&l900, 36), abs_(&sub(&l900, &l200)).to_f64());
    println!("\n=== done. ===");
}
