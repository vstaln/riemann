// 8D zeta-direct L_k check — settle whether the flagged negative L_k(t) values are real.
//
// L_k(t) = (Xi^(k))^2 - Xi^(k-1) Xi^(k+1),  Xi(t) = xi(1/2+it) real.
// L_k >= 0 for all (t,k) is a NECESSARY condition for RH (RH => xi in the
// Laguerre-Polya class => {xi^(k)} log-concave at every real t — classical).
// Positives are RH-consistent with ZERO evidential weight; a rigorous negative
// with |L_k| >> error would be an RH DISPROOF (escalate).
//
// TWO independent routes (Rust only):
//  (A) central differences on direct xi (em.rs zeta_em, n=600 — see N_ZETA) at
//      h, h/2, h/4 + Richardson extrapolation + error estimate. REQUIRED pass.
//      Known weakness: roundoff ~ eps/h^n swamps high k; reported honestly.
//  (B) ANALYTIC route (decisive at high k): zeta^(m)(1/2+it), m=0..21, directly
//      from the EM expansion (em::zeta_em_ders — certified, no differencing),
//      polygamma via Stirling with shift, then u^(n) = (d/dt)^n log Xi via
//      Bell composition, B_k = Bell(u'), L_k = Xi^2 (B_k^2 - B_{k-1} B_{k+1}).
//
// Controls (mpmath dps=60, pre-Rust-rule): L_3(56.5)=+8.9e-32, L_3(40)=+1.66e-21.
// Sanity of xi: Xi(0)=0.497120778188314, |Xi| ~ 0 at known zeros, sign flips.

#[path = "../em.rs"]
mod em;

use em::{binom_f, fact_f, zeta_em, zeta_em_ders1};

// EM main-sum terms: MUST be large enough for the certified remainder to be tiny
// at t ~ 56.5. em_n_for(t) (~0.25t) is FAR too small (EM unconverged at t>=35,
// terms ~1e41 at K=40 for N=12). N_ZETA=600 gives certified err < 1e-100 here.
const N_ZETA: usize = 600;
const SHIFT: usize = 40; // polygamma Stirling shift (|w| ~ 54..70)
const KP: usize = 10;    // polygamma Stirling terms

// ---- complex Gamma via Stirling (with 1/(12z) and -1/(360 z^3)) ------------
fn gamma_complex_stirling(re: f64, im: f64) -> (f64, f64) {
    let (lnz_r, lnz_i) = {
        let m = (re * re + im * im).sqrt();
        let th = im.atan2(re);
        (m.ln(), th)
    };
    let (a, b) = (re - 0.5, im);
    let (lr, li) = (a * lnz_r - b * lnz_i, a * lnz_i + b * lnz_r);
    let (lr, li) = (lr - re + 0.5 * (2.0 * std::f64::consts::PI).ln(), li - im);
    // + 1/(12z) - 1/(360 z^3)
    let z2 = re * re + im * im;
    let z3 = z2 * (re * re + im * im).sqrt();
    let (lr, li) = (lr + re / (12.0 * z2) - re / (360.0 * z3), li - im / (12.0 * z2) + im / (360.0 * z3));
    let m = lr.exp();
    (m * li.cos(), m * li.sin())
}

// xi(1/2+it) complex, s = 0.5 + i t
fn xi_complex(t: f64) -> (f64, f64) {
    let s_re = 0.5;
    let s_im = t;
    let lnpi = std::f64::consts::PI.ln();
    let ln_pow_re = -0.25 * lnpi;
    let ln_pow_im = -(t / 2.0) * lnpi;
    // NOTE: f64::sin_cos returns (sin, cos)!
    let (sn, cs) = ln_pow_im.sin_cos();
    let pi_pow = (cs * ln_pow_re.exp(), sn * ln_pow_re.exp());
    let ssm = (-(0.25 + t * t), 0.0);
    let b = t / 2.0;
    let (gr, gi) = gamma_complex_stirling(0.25, b);
    let z = zeta_em(s_re, s_im, N_ZETA);
    let re = 0.5 * ssm.0;
    let (pr, pi_) = (re * pi_pow.0, re * pi_pow.1);
    let (mr, mi) = (pr * gr - pi_ * gi, pr * gi + pi_ * gr);
    (mr * z.re - mi * z.im, mr * z.im + mi * z.re)
}

// ---- polygamma psi^(m)(z), m = 0..=20, z complex, via shift + Stirling ------
fn polygamma(m: usize, z_re: f64, z_im: f64) -> (f64, f64) {
    // shift: psi^(m)(z) = psi^(m)(z+M) - sum_{l=0}^{M-1} (-1)^m m! (z+l)^{-(m+1)}
    let mut sr = 0.0;
    let mut si = 0.0;
    let mfact = fact_f(m);
    for l in 0..SHIFT {
        let (xr, xi) = (z_re + l as f64, z_im);
        let x2 = xr * xr + xi * xi;
        // (z+l)^{-(m+1)}
        let (ir, ii) = (xr / x2, -xi / x2);
        // power m+1 by repeated squaring-style multiply
        let mut pr = 1.0;
        let mut pi = 0.0;
        for _ in 0..(m + 1) {
            let (nr, ni) = (pr * ir - pi * ii, pr * ii + pi * ir);
            pr = nr;
            pi = ni;
        }
        let sign = if m % 2 == 0 { -1.0 } else { 1.0 }; // -(-1)^m
        sr += sign * mfact * pr;
        si += sign * mfact * pi;
    }
    // Stirling at w = z + SHIFT
    let (wr, wi) = (z_re + SHIFT as f64, z_im);
    let w2 = wr * wr + wi * wi;
    let inv_re = wr / w2;
    let inv_im = -wi / w2;
    let maxp = m + 2 * KP + 1;
    let mut ip_re = vec![0.0f64; maxp + 1];
    let mut ip_im = vec![0.0f64; maxp + 1];
    ip_re[1] = inv_re;
    ip_im[1] = inv_im;
    for p in 2..=maxp {
        ip_re[p] = ip_re[p - 1] * inv_re - ip_im[p - 1] * inv_im;
        ip_im[p] = ip_re[p - 1] * inv_im + ip_im[p - 1] * inv_re;
    }
    let (mut vr, mut vi) = (0.0, 0.0);
    if m == 0 {
        // psi(w) = ln w - 1/(2w) - sum_{k>=1} B_{2k}/(2k w^{2k})
        let ln_re = 0.5 * w2.ln();
        let ln_im = wi.atan2(wr);
        vr = ln_re - 0.5 * inv_re;
        vi = ln_im - 0.5 * inv_im;
        for k in 1..=KP {
            // B_{2k}/(2k) = sign * |B_{2k}|/(2k)!, sign = (-1)^{k+1}
            let sgn = if k % 2 == 1 { 1.0 } else { -1.0 };
            let coef = sgn * em::abs_b_over_fact(k) * fact_f(2 * k) / (2.0 * k as f64);
            let p = 2 * k;
            vr += coef * ip_re[p];
            vi += coef * ip_im[p];
        }
    } else {
        // psi^(m)(w) = (-1)^{m-1}(m-1)! w^{-m} + (-1)^{m+1} m! w^{-(m+1)}/2
        //            + sum_{k>=1} (-1)^{m+1} B_{2k} (2k+m-1)!/(2k)! w^{-(2k+m)}
        let s1 = if (m - 1) % 2 == 0 { 1.0 } else { -1.0 };
        let s2 = if (m + 1) % 2 == 0 { 1.0 } else { -1.0 };
        vr += s1 * fact_f(m - 1) * ip_re[m];
        vi += s1 * fact_f(m - 1) * ip_im[m];
        vr += s2 * 0.5 * mfact * ip_re[m + 1];
        vi += s2 * 0.5 * mfact * ip_im[m + 1];
        for k in 1..=KP {
            let sgn = if k % 2 == 1 { 1.0 } else { -1.0 };
            // B_{2k} (2k+m-1)!/(2k)! = sgn * |B_{2k}|/(2k)! * (2k)!(2k+1)...(2k+m-1)
            //                            = sgn * abs_b_over_fact(k) * rising
            let mut rising = 1.0f64;
            for j in 1..m {
                rising *= (2 * k + j) as f64;
            }
            let coef = s2 * sgn * em::abs_b_over_fact(k) * rising;
            let p = 2 * k + m;
            vr += coef * ip_re[p];
            vi += coef * ip_im[p];
        }
    }
    (sr + vr, si + vi)
}

// ---- L_n = (d/ds)^n log zeta(s), n = 1..=m_max, at complex s ----------------
fn zeta_logderivs(s_re: f64, s_im: f64, m_max: usize) -> (Vec<f64>, Vec<f64>) {
    let d = zeta_em_ders1(s_re, s_im, N_ZETA, m_max);
    let z2 = d.re[0] * d.re[0] + d.im[0] * d.im[0];
    let mut lr = vec![0.0f64; m_max + 1];
    let mut li = vec![0.0f64; m_max + 1];
    lr[1] = (d.re[1] * d.re[0] + d.im[1] * d.im[0]) / z2;
    li[1] = (d.im[1] * d.re[0] - d.re[1] * d.im[0]) / z2;
    for n in 2..=m_max {
        let mut sr = d.re[n];
        let mut si = d.im[n];
        for j in 1..n {
            let c = binom_f(n - 1, j - 1);
            let (a, b) = (d.re[n - j], d.im[n - j]);
            let (cr, ci) = (a * lr[j] - b * li[j], a * li[j] + b * lr[j]);
            sr -= c * cr;
            si -= c * ci;
        }
        lr[n] = (sr * d.re[0] + si * d.im[0]) / z2;
        li[n] = (si * d.re[0] - sr * d.im[0]) / z2;
    }
    (lr, li)
}

// ---- u^(n)(t) = (d/dt)^n log Xi(t) = Re[i^n A_n], A_n = (d/ds)^n log xi ----
// returns (u, max_imag) where max_imag = max |Im[i^n A_n]| (reality self-check)
fn logxi_derivs(t: f64, m_max: usize) -> (Vec<f64>, f64) {
    let s_re = 0.5;
    let s_im = t;
    let (lr, li) = zeta_logderivs(s_re, s_im, m_max);
    let lnpi = std::f64::consts::PI.ln();
    // powers of 1/s and 1/(s-1)
    let s2 = s_re * s_re + s_im * s_im;
    let (inv_re, inv_im) = (s_re / s2, -s_im / s2);
    let dm = s_re - 1.0;
    let d2 = dm * dm + s_im * s_im;
    let (inv1_re, inv1_im) = (dm / d2, -s_im / d2);
    let mut ip_re = vec![0.0f64; m_max + 2];
    let mut ip_im = vec![0.0f64; m_max + 2];
    let mut ip1_re = vec![0.0f64; m_max + 2];
    let mut ip1_im = vec![0.0f64; m_max + 2];
    ip_re[1] = inv_re;
    ip_im[1] = inv_im;
    ip1_re[1] = inv1_re;
    ip1_im[1] = inv1_im;
    for p in 2..=m_max + 1 {
        ip_re[p] = ip_re[p - 1] * inv_re - ip_im[p - 1] * inv_im;
        ip_im[p] = ip_re[p - 1] * inv_im + ip_im[p - 1] * inv_re;
        ip1_re[p] = ip1_re[p - 1] * inv1_re - ip1_im[p - 1] * inv1_im;
        ip1_im[p] = ip1_re[p - 1] * inv1_im + ip1_im[p - 1] * inv1_re;
    }
    // polygamma values psi^(m)(s/2), m = 0..=m_max-1
    let mut ps_re = vec![0.0f64; m_max];
    let mut ps_im = vec![0.0f64; m_max];
    for m in 0..m_max {
        let (pr, pi) = polygamma(m, s_re / 2.0, s_im / 2.0);
        ps_re[m] = pr;
        ps_im[m] = pi;
    }
    let mut u = vec![0.0f64; m_max + 1];
    let mut max_imag = 0.0f64;
    for n in 1..=m_max {
        // A_n = (d/ds)^n log xi
        let (ar, ai);
        if n == 1 {
            ar = ip_re[1] + ip1_re[1] - 0.5 * lnpi + 0.5 * ps_re[0] + lr[1];
            ai = ip_im[1] + ip1_im[1] + 0.5 * ps_im[0] + li[1];
        } else {
            let sgn = if (n - 1) % 2 == 0 { 1.0 } else { -1.0 };
            let cf = sgn * fact_f(n - 1);
            ar = cf * (ip_re[n] + ip1_re[n]) + (1.0 / (1u64 << n) as f64) * ps_re[n - 1] + lr[n];
            ai = cf * (ip_im[n] + ip1_im[n]) + (1.0 / (1u64 << n) as f64) * ps_im[n - 1] + li[n];
        }
        // u^(n) = i^n A_n; rotate by n mod 4
        let (ur, ui) = match n % 4 {
            0 => (ar, ai),
            1 => (-ai, ar),
            2 => (-ar, -ai),
            _ => (ai, -ar),
        };
        max_imag = max_imag.max(ui.abs());
        u[n] = ur;
    }
    (u, max_imag)
}

// central difference of order n via direct binomial stencil (n+1 evals)
fn dxi_stencil(t: f64, n: usize, h: f64) -> f64 {
    if n == 0 {
        return xi_complex(t).0;
    }
    let mut sum = 0.0f64;
    for j in 0..=n {
        let c = binom_f(n, j);
        let sgn = if j % 2 == 0 { 1.0 } else { -1.0 };
        let x = t + ((n as i64 - 2 * j as i64) as f64) * h;
        sum += sgn * c * xi_complex(x).0;
    }
    sum / (2.0 * h).powi(n as i32)
}

fn lk_cd(t: f64, k: usize, h: f64) -> f64 {
    let dk = dxi_stencil(t, k, h);
    let dkm = dxi_stencil(t, k - 1, h);
    let dkp = dxi_stencil(t, k + 1, h);
    dk * dk - dkm * dkp
}

// analytic-route L_k; returns (L_k, err_est, bracket, bell_scale)
fn lk_analytic(t: f64, k: usize) -> (f64, f64, f64, f64) {
    let m_max = k + 1;
    let (u, _mi) = logxi_derivs(t, m_max);
    // Bell: B[0]=1, B[j] = sum_{m=0..j-1} C(j-1,m) u[m+1] B[j-1-m]
    let mut b = vec![0.0f64; m_max + 1];
    let mut scale = vec![0.0f64; m_max + 1]; // sum of |terms| at each level
    b[0] = 1.0;
    scale[0] = 1.0;
    for j in 1..=m_max {
        let mut s = 0.0;
        let mut sc = 0.0;
        for m in 0..j {
            let c = binom_f(j - 1, m);
            let term = c * u[m + 1] * b[j - 1 - m];
            s += term;
            sc += c * u[m + 1].abs() * b[j - 1 - m].abs();
        }
        b[j] = s;
        scale[j] = sc;
    }
    let xi = xi_complex(t).0;
    let xi2 = xi * xi;
    let q = b[k] * b[k] - b[k - 1] * b[k + 1];
    // estimated rounding of Q: dQ ~ eps*(2|B_k| S_k + S_{k-1}|B_{k+1}| + |B_{k-1}| S_{k+1})
    let err_q = 2.220446049250313e-16
        * (2.0 * b[k].abs() * scale[k] + scale[k - 1] * b[k + 1].abs() + b[k - 1].abs() * scale[k + 1]);
    (xi2 * q, xi2 * err_q, q, scale[k])
}

fn main() {
    println!("=== 8D zeta-direct L_k check (flagged points) ===");
    println!("L_k = (Xi^(k))^2 - Xi^(k-1) Xi^(k+1);  Xi(t)=xi(1/2+it). n_em = {}", N_ZETA);
    println!("L_k >= 0 is NECESSARY for RH (LP-class log-concavity). Positives: RH-consistent only.\n");

    // ---- 0. certified zeta error at the flagged points ----------------------
    let pts: &[(f64, usize)] = &[(56.5, 3), (40.0, 18), (40.0, 19), (40.0, 20), (33.6, 8), (35.5, 4)];
    println!("-- certified zeta error at each point (n={}) --", N_ZETA);
    for &(t, _k) in pts {
        let d = zeta_em_ders1(0.5, t, N_ZETA, 21);
        println!("t={:6.1}: zeta err={:.2e}  zeta' err={:.2e}  zeta^(21) err={:.2e}", t, d.err[0], d.err[1], d.err[21]);
    }

    // ---- 1. xi sanity -------------------------------------------------------
    println!("\n-- xi sanity (sign pattern + zeros) --");
    // ---- component debug (phase diagnosis) ----
    println!("-- phase components --");
    let lnpi = std::f64::consts::PI.ln();
    for &t in &[0.0, 7.6, 17.6, 31.7, 40.0, 56.5] {
        let z = zeta_em(0.5, t, N_ZETA);
        let (gr, gi) = gamma_complex_stirling(0.25, t / 2.0);
        let argz = z.im.atan2(z.re);
        let argg = gi.atan2(gr);
        let theta = argg - (t / 2.0) * lnpi;
        let argp = std::f64::consts::PI + theta;
        let phase = argp + argz;
        let c = phase.cos();
        println!("t={:5.1}: zeta=({:+.6e},{:+.6e}) err={:.1e} gamma=({:+.6e},{:+.6e}) argzeta={:+.4} argGamma={:+.4} theta={:+.4} phaseTot={:+.4} cos={:+.4}", t, z.re, z.im, z.err, gr, gi, argz, argg, theta, phase, c);
        let (xc_r, xc_i) = xi_complex(t);
        println!("   xi_complex({:4.1}) = ({:+.6e}, {:+.6e})", t, xc_r, xc_i);
    }
    let xi0 = xi_complex(0.0).0;
    println!("Xi(0) = {:.15}  (expect 0.497120778188314)", xi0);
    let zeros = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062, 37.586178,
                 40.918719, 43.327073, 48.005150, 49.773832, 52.970321, 56.446248];
    for (i, &g) in zeros.iter().enumerate() {
        let (r, im_) = xi_complex(g);
        println!("|Xi(gamma_{:2})| at t={:9.6} = {:.3e}  (Re={:+.3e} Im={:+.3e})", i + 1, g, r.hypot(im_), r, im_);
    }
    // sign pattern: sign on (gamma_m, gamma_{m+1}) = (-1)^m  (gamma_0 = 0)
    let mid = [7.6, 17.6, 23.05, 27.7, 31.7, 34.7, 39.2, 42.1, 45.7, 48.9, 51.4, 54.7, 57.9, 62.1, 66.1];
    let exp_sign: Vec<i32> = (0..mid.len()).map(|m| if m % 2 == 0 { 1 } else { -1 }).collect();
    let mut ok = true;
    for (i, &t) in mid.iter().enumerate() {
        let r = xi_complex(t).0;
        let s = if r >= 0.0 { 1 } else { -1 };
        let good = s == exp_sign[i];
        ok &= good;
        println!("Xi({:5.1}) = {:+.4e}  sign {:>+2} expect {:>+2}  {}", t, r, s, exp_sign[i], if good { "OK" } else { "MISMATCH" });
    }
    for &(t, _) in pts {
        let r = xi_complex(t).0;
        let s = if r >= 0.0 { 1 } else { -1 };
        println!("Xi({:5.1}) (flagged) = {:+.4e}  sign {:>+2}", t, r, s);
    }
    println!("sign pattern: {}", if ok { "ALL OK" } else { "FAILED — Stirling phase broken, STOP" });

    // ---- 2. REQUIRED error-bound pass: CD at h, h/2, h/4 + Richardson --------
    println!("\n-- route A: central differences + Richardson (h, h/2, h/4) --");
    let h0 = |k: usize| if k <= 4 { 1e-3 } else if k <= 7 { 1e-2 } else if k <= 12 { 3e-2 } else { 5e-2 };
    let mut all: Vec<(f64, usize)> = pts.to_vec();
    all.push((40.0, 3)); // mpmath control L_3(40)
    for &(t, k) in &all {
        let h = h0(k);
        let l1 = lk_cd(t, k, h);
        let l2 = lk_cd(t, k, h / 2.0);
        let l4 = lk_cd(t, k, h / 4.0);
        // Richardson order-2 and order-4
        let r2 = (4.0 * l2 - l1) / 3.0;
        let r4 = (16.0 * l4 - l2) / 15.0;
        let err = (r4 - r2).abs().max((l4 - l2).abs() / 3.0);
        let verdict = if l4.abs() < err { "INCONCLUSIVE" } else if l4 > 0.0 { "POSITIVE" } else { "NEGATIVE!" };
        println!("t={:6.1} k={:2}: L(h={:.0e})={:+.3e} L(h/2)={:+.3e} L(h/4)={:+.3e}  R2={:+.3e} R4={:+.3e}  err~{:+.1e}  -> {}", t, k, h, l1, l2, l4, r2, r4, err, verdict);
    }

    // ---- 3. analytic route (decisive) ---------------------------------------
    println!("\n-- route B: analytic EM differentiation (zeta^(0..21), Stirling polygamma, Bell) --");
    for &(t, k) in &all {
        let (lk, err, q, sc) = lk_analytic(t, k);
        let (u, mi) = logxi_derivs(t, k + 1);
        println!("t={:6.1} k={:2}: L_k = {:+.6e}  err_est~{:+.1e}  (bracket={:+.4e}, Bk_scale={:.1e}, max|Im u'..u^({})|={:.1e})", t, k, lk, err, q, sc, k + 1, mi);
        if k == 3 {
            println!("    u-derivatives: {}", (1..=4).map(|m| format!("u^{}={:+.3e}", m, u[m])).collect::<Vec<_>>().join(" "));
        }
        let verdict = if lk.abs() < err { "INCONCLUSIVE" } else if lk > 0.0 { "POSITIVE (RH-consistent)" } else { "NEGATIVE -> CHECK/ESCALATE" };
        println!("    -> {}", verdict);
    }
    println!("\n=== done. ===");
}
