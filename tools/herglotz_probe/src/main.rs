// herglotz_probe — H(t) = Xi'(t)/Xi(t) Herglotz probe (wave-20 g4-2).
// Xi(t) = xi(1/2+it); H(t) = d/dt log Xi(t) = i*A(s), s = 1/2+it, with
//   A(s) = d/ds log xi(s) = 1/s + 1/(s-1) - (1/2)ln(pi) + (1/2)psi(s/2) + zeta'(s)/zeta(s).
// Im H(t+iy) = Re A((0.5-y)+ix)  for t = x+iy.
// All-real zeros of Xi <=> H Herglotz (Im H >= 0 in UHP). Numerical probe only:
// finds a violation (RH-disproof signal) or is RH-consistent; never proves RH.
// Reuses wave8d em.rs (certified Euler-Maclaurin zeta and zeta', Kahan, explicit
// remainder) and the Stirling polygamma validated in lk_zeta.rs.

#[path = "../../wave8d/src/em.rs"]
mod em;

use em::{zeta_em, abs_b_over_fact, fact_f};

const N_ZETA: usize = 600; // EM main-sum terms (validated: certified err < 1e-100 at t~56.5, sigma=0.5)
const SHIFT: usize = 40;   // polygamma Stirling shift
const KP: usize = 10;      // polygamma Stirling terms

// ---- complex Gamma via Stirling (validated in lk_zeta.rs) -------------------
fn gamma_complex_stirling(re: f64, im: f64) -> (f64, f64) {
    let (lnz_r, lnz_i) = {
        let m = (re * re + im * im).sqrt();
        let th = im.atan2(re);
        (m.ln(), th)
    };
    let (a, b) = (re - 0.5, im);
    let (lr, li) = (a * lnz_r - b * lnz_i, a * lnz_i + b * lnz_r);
    let (lr, li) = (lr - re + 0.5 * (2.0 * std::f64::consts::PI).ln(), li - im);
    let z2 = re * re + im * im;
    let z3 = z2 * (re * re + im * im).sqrt();
    let (lr, li) = (lr + re / (12.0 * z2) - re / (360.0 * z3), li - im / (12.0 * z2) + im / (360.0 * z3));
    let m = lr.exp();
    (m * li.cos(), m * li.sin())
}

// ---- psi(z), z complex, via shift + Stirling (verbatim m=0 case of lk_zeta) --
fn polygamma0(z_re: f64, z_im: f64) -> (f64, f64) {
    let mut sr = 0.0;
    let mut si = 0.0;
    for l in 0..SHIFT {
        let (xr, xi) = (z_re + l as f64, z_im);
        let x2 = xr * xr + xi * xi;
        sr -= xr / x2;
        si += xi / x2;
    }
    let (wr, wi) = (z_re + SHIFT as f64, z_im);
    let w2 = wr * wr + wi * wi;
    let (inv_re, inv_im) = (wr / w2, -wi / w2);
    let ln_re = 0.5 * w2.ln();
    let ln_im = wi.atan2(wr);
    let (mut vr, mut vi) = (ln_re - 0.5 * inv_re, ln_im - 0.5 * inv_im);
    let maxp = 2 * KP + 1;
    let mut ip_re = vec![0.0f64; maxp + 1];
    let mut ip_im = vec![0.0f64; maxp + 1];
    ip_re[1] = inv_re;
    ip_im[1] = inv_im;
    for p in 2..=maxp {
        ip_re[p] = ip_re[p - 1] * inv_re - ip_im[p - 1] * inv_im;
        ip_im[p] = ip_re[p - 1] * inv_im + ip_im[p - 1] * inv_re;
    }
    for k in 1..=KP {
        let sgn = if k % 2 == 1 { 1.0 } else { -1.0 };
        let coef = sgn * abs_b_over_fact(k) * fact_f(2 * k) / (2.0 * k as f64);
        let p = 2 * k;
        // psi(w) = ln w - 1/(2w) - sum B_{2k}/(2k w^{2k}): SUBTRACT (lk_zeta.rs
        // polygamma m=0 branch adds — inherited sign slip, see probe note)
        vr -= coef * ip_re[p];
        vi -= coef * ip_im[p];
    }
    (sr + vr, si + vi)
}

// ---- xi(1/2 + i t), t complex: s = 0.5 + it = (0.5 - t_im) + i t_re ----------
fn xi_c(t_re: f64, t_im: f64) -> (f64, f64) {
    let s_re = 0.5 - t_im;
    let s_im = t_re;
    let lnpi = std::f64::consts::PI.ln();
    // pi^{-s/2} = exp(-(s/2) ln pi)
    let lp_re = -(s_re / 2.0) * lnpi;
    let lp_im = -(s_im / 2.0) * lnpi;
    let (sn, cs) = lp_im.sin_cos();
    let (pp_re, pp_im) = (cs * lp_re.exp(), sn * lp_re.exp());
    // s(s-1)
    let (ss_re, ss_im) = (s_re * (s_re - 1.0) - s_im * s_im, s_im * (2.0 * s_re - 1.0));
    let (gr, gi) = gamma_complex_stirling(s_re / 2.0, s_im / 2.0);
    let z = zeta_em(s_re, s_im, N_ZETA);
    let (a_re, a_im) = (0.5 * ss_re, 0.5 * ss_im);
    let (b_re, b_im) = (a_re * pp_re - a_im * pp_im, a_re * pp_im + a_im * pp_re);
    let (c_re, c_im) = (b_re * gr - b_im * gi, b_re * gi + b_im * gr);
    (c_re * z.re - c_im * z.im, c_re * z.im + c_im * z.re)
}

// ---- A(s) = d/ds log xi(s) at complex s = (s_re, s_im) ----------------------
// returns (Re A, Im A). H(t) = i*A(1/2+it), so Im H(t) = Re A.
fn logxi_deriv_s(s_re: f64, s_im: f64) -> (f64, f64) {
    let lnpi = std::f64::consts::PI.ln();
    let s2 = s_re * s_re + s_im * s_im;
    let (i1_re, i1_im) = (s_re / s2, -s_im / s2); // 1/s
    let dm = s_re - 1.0;
    let d2 = dm * dm + s_im * s_im;
    let (i2_re, i2_im) = (dm / d2, -s_im / d2); // 1/(s-1)
    let (ps_re, ps_im) = polygamma0(s_re / 2.0, s_im / 2.0);
    let z = zeta_em(s_re, s_im, N_ZETA);
    let z2 = z.re * z.re + z.im * z.im;
    let (ld_re, ld_im) = ((z.dre * z.re + z.dim * z.im) / z2, (z.dim * z.re - z.dre * z.im) / z2);
    (
        i1_re + i2_re - 0.5 * lnpi + 0.5 * ps_re + ld_re,
        i1_im + i2_im + 0.5 * ps_im + ld_im,
    )
}

// ---- Phi(u), wave8d-corrected, for the structural positivity spot-check ------
fn phi(u: f64) -> f64 {
    let pi = std::f64::consts::PI;
    let mut s = 0.0;
    for n in 1..=60usize {
        let nf = n as f64;
        let t1 = 2.0 * pi * pi * nf.powi(4) * (9.0 * u / 2.0).exp();
        let t2 = 3.0 * pi * nf * nf * (5.0 * u / 2.0).exp();
        s += (t1 - t2) * (-pi * nf * nf * (2.0 * u).exp()).exp();
    }
    2.0 * s
}

fn main() {
    println!("=== herglotz probe: H(t)=Xi'(t)/Xi(t); Im H >= 0 in UHP <=> RH ===");
    println!("H(t) = i*A(1/2+it);  Im H(x+iy) = Re A((0.5-y)+ix);  n_em = {}", N_ZETA);

    // polygamma sanity (known values): psi(0.25) = -4.227453534, psi(1) = -0.577215665
    let (p25r, p25i) = polygamma0(0.25, 0.0);
    let (p1r, _p1i) = polygamma0(1.0, 0.0);
    println!("psi(0.25) = {:+.9} (expect -4.227453534)   psi(1) = {:+.9} (expect -0.577215665)", p25r, p1r);

    // gate 1: H(0) = i*A(0.5) must be 0 (Xi even)
    let (ar0, ai0) = logxi_deriv_s(0.5, 0.0);
    println!("\n[gate1] |H(0)| = |A(0.5)| = {:.3e}  (expect < 1e-12)", ar0.hypot(ai0));

    // gate 2: H real on the real axis  (Im H = Re A(0.5+ix) ~ 0)
    let mut max_imh = 0.0f64;
    for i in 0..=12 {
        let x = 10.0 * i as f64;
        let (ar, _ai) = logxi_deriv_s(0.5, x);
        max_imh = max_imh.max(ar.abs());
    }
    println!("[gate2] max |Im H(t)| for real t in [0,120] = {:.3e}  (expect ~1e-13)", max_imh);

    // gate 3: residue +1 at known zeros of Xi  (validates zeta AND zeta' at the poles)
    let zeros = [
        14.134725, 21.022040, 25.010858, 30.424876, 32.935062, 37.586178, 40.918719,
        43.327073, 48.005150, 49.773832, 52.970321, 56.446248,
    ];
    let delta = 1e-4;
    for (j, &g) in zeros.iter().take(4).enumerate() {
        let t = g + delta;
        let (ar, ai) = logxi_deriv_s(0.5, t);
        let h = (-ai, ar); // H(t) = i*A
        let (pr, pi) = (h.0 * delta, h.1 * delta);
        println!(
            "[gate3] gamma_{}: (t-g)H(t) = ({:+.6e}, {:+.6e})  |·-1| = {:.2e}",
            j + 1, pr, pi, (pr - 1.0).hypot(pi)
        );
    }

    // gate 4: cross-check H vs central-difference of log Xi (direct xi_c)
    let t0 = 9.7;
    let eps = 1e-5;
    let (x1r, x1i) = xi_c(t0 + eps, 0.0);
    let (x2r, x2i) = xi_c(t0 - eps, 0.0);
    let (m1, a1) = (x1r.hypot(x1i), x1i.atan2(x1r));
    let (m2, a2) = (x2r.hypot(x2i), x2i.atan2(x2r));
    let hfd = ((m1 / m2).ln() / (2.0 * eps), (a1 - a2) / (2.0 * eps));
    let (ar, ai) = logxi_deriv_s(0.5, t0);
    let h = (-ai, ar);
    println!(
        "[gate4] H({}) analytic = ({:+.9e}, {:+.9e}); FD log-Xi = ({:+.9e}, {:+.9e}); |diff| = {:.2e}",
        t0, h.0, h.1, hfd.0, hfd.1, (h.0 - hfd.0).hypot(h.1 - hfd.1)
    );

    // Phi positivity spot-check (structural analysis support)
    let mut phi_min = f64::INFINITY;
    let mut phi_min_u = 0.0;
    for i in -6..=20i32 {
        let u = 0.1 * i as f64;
        let v = phi(u);
        if v < phi_min {
            phi_min = v;
            phi_min_u = u;
        }
        if i % 5 == 0 {
            println!("Phi({:+.1}) = {:+.6e}", u, v);
        }
    }
    println!("Phi min over u in [-0.6, 2.0] = {:+.6e} at u = {:+.1}", phi_min, phi_min_u);

    // ---- grid probe --------------------------------------------------------
    println!("\n-- grid probe: min Im H(x+iy) over x (Herglotz requires >= 0) --");
    let ys = [0.1, 0.5, 1.0, 2.0, 5.0];
    for &y in &ys {
        let s_re = 0.5 - y;
        let mut mn = f64::INFINITY;
        let mut mn_x = 0.0;
        let mut mn_err = 0.0;
        let mut worst = 0.0f64; // certified zeta error bound seen on this row
        let mut check = |x: f64, s_re: f64, mn: &mut f64, mn_x: &mut f64, mn_err: &mut f64, worst: &mut f64| {
            let z = zeta_em(s_re, x, N_ZETA);
            let (ar, _ai) = logxi_deriv_s(s_re, x);
            let imh = ar;
            *worst = worst.max(z.err.max(z.derr));
            if imh < *mn {
                *mn = imh;
                *mn_x = x;
                *mn_err = z.err.max(z.derr);
            }
        };
        for i in 0..=30 {
            check(2.0 * i as f64, s_re, &mut mn, &mut mn_x, &mut mn_err, &mut worst);
        }
        for j in 0..zeros.len() - 1 {
            check(0.5 * (zeros[j] + zeros[j + 1]), s_re, &mut mn, &mut mn_x, &mut mn_err, &mut worst);
        }
        check(0.0, s_re, &mut mn, &mut mn_x, &mut mn_err, &mut worst);
        // near-pole point x = gamma_1: Im H ~ 1/y (pole dominance)
        let (ar1, _) = logxi_deriv_s(s_re, zeros[0]);
        let verdict = if mn > 10.0 * mn_err { "POSITIVE (RH-consistent)" } else if mn < -10.0 * mn_err { "NEGATIVE -> ESCALATE" } else { "INCONCLUSIVE" };
        println!(
            "y={:4.1}: min Im H = {:+.9e} at x = {:6.2}   (cert. zeta err there = {:.1e}; row max err = {:.1e})   Im H(x=gamma1) = {:+.6e} (expect ~{:.4})  -> {}",
            y, mn, mn_x, mn_err, worst, ar1, 1.0 / y, verdict
        );
    }

    // detailed table for y = 0.1 and y = 2.0 (most informative rows)
    for &y in &[0.1, 2.0] {
        let s_re = 0.5 - y;
        println!("\n-- Im H(x+iy) table, y = {} --", y);
        for i in 0..=30 {
            let x = 2.0 * i as f64;
            let (ar, _ai) = logxi_deriv_s(s_re, x);
            let (z, _) = { let z = zeta_em(s_re, x, N_ZETA); (z, ()) };
            println!("  x = {:5.1}: Im H = {:+.9e}   (zeta err = {:.1e})", x, ar, z.err.max(z.derr));
        }
    }
    println!("\n=== done. ===");
}
