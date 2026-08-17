// tools/theta_semigroup/src/main.rs
// Bounded f64 probe for research/notes/direct-rh-theta-semigroup-2026-08-18.md
// Identity (★): xi(s) = 0.5*s*(s-1)*(T(s)+T(1-s)) + 0.5
//   T(s) = int_0^inf psi(e^v) e^{v s/2} dv,  psi(x)=sum_{n>=1} e^{-pi n^2 x}
// t1: (★) at s=1.5+2i (LHS via Euler-Maclaurin zeta), at s=2 (vs pi/6), at s=1/2
//     (vs xi(1/2)=0.49712077818831366); FE symmetry RHS(1-s)==RHS(s).
// t2: critical line: xi(1/2+it) = 1/2 - (t^2+1/4)*A(t), A=Re T; first zero t0.
// t3: theta-condition normalized gap rho=|K-target|*(1+t^2)/delta over a grid.
// STOPPING RULE: t1 relErr > 1e-6 => identity bug, stop. Otherwise report+stop.
use std::f64::consts::PI;

fn zeta_em(a: f64, b: f64) -> (f64, f64) {
    // Euler-Maclaurin, valid Re s > 1, |b| small.
    // zeta(s) = sum_{n<=N} n^-s + N^{1-s}/(s-1) + N^-s/2
    //           + sum_{k=1..K} B_{2k}/(2k)! * (s)_{2k-1} * N^{-s-2k+1}
    let n = 60.0f64;
    let ln_n = n.ln();
    let mut sr = 0.0f64;
    let mut si = 0.0f64;
    for j in 1..=60i32 {
        let lj = (j as f64).ln();
        let m = (-a * lj).exp();
        sr += m * (-b * lj).cos();
        si += m * (-b * lj).sin();
    }
    // N^{1-s} / (s-1)
    let m = ((1.0 - a) * ln_n).exp();
    let (nnr, nni) = (m * (-b * ln_n).cos(), m * (-b * ln_n).sin());
    let d = (a - 1.0) * (a - 1.0) + b * b;
    sr += (nnr * (a - 1.0) + nni * b) / d;
    si += (nni * (a - 1.0) - nnr * b) / d;
    // N^-s / 2
    let m2 = (-a * ln_n).exp();
    sr += 0.5 * m2 * (-b * ln_n).cos();
    si += 0.5 * m2 * (-b * ln_n).sin();
    // B_{2k}/(2k)! terms; (s)_{2k-1} = prod_{j=0..2k-2} (s+j)
    let berns: [f64; 6] = [1.0 / 6.0, -1.0 / 30.0, 1.0 / 42.0, -1.0 / 30.0, 5.0 / 66.0, -691.0 / 2730.0];
    let mut fact = 2.0f64; // 2!
    for kk in 1..=6usize {
        let m_ = 2 * kk - 1;
        let (mut pr, mut pi_) = (1.0f64, 0.0f64);
        for j in 0..m_ {
            let aa = a + j as f64;
            let (x, y) = (pr * aa - pi_ * b, pr * b + pi_ * aa);
            pr = x; pi_ = y;
        }
        let cf = berns[kk - 1] / fact;
        // N^{-s-2k+1} = N^{-a-2k+1} e^{-i b ln N}
        let mm = (-a - (2 * kk - 1) as f64).ln().max(1e-300);
        let _ = mm;
        let nre = (-(a + (2 * kk - 1) as f64) * ln_n).exp() * (-b * ln_n).cos();
        let nim = (-(a + (2 * kk - 1) as f64) * ln_n).exp() * (-b * ln_n).sin();
        let tr = cf * (pr * nre - pi_ * nim);
        let ti = cf * (pr * nim + pi_ * nre);
        sr += tr; si += ti;
        fact *= (2 * kk + 1) as f64 * (2 * kk + 2) as f64; // (2k+2)!
    }
    (sr, si)
}

fn lgamma_re_im(zr: f64, zi: f64) -> (f64, f64) {
    // log Gamma(z), Re z > 0, via Lanczos (g=7, 9 coeffs)
    let c = [0.99999999999980993, 676.5203681218851, -1259.1392167224028,
             771.32342877765313, -176.61502916214059, 12.507343278686905,
             -0.13857109526572012, 9.9843695780195716e-6, 1.5056327351493116e-7];
    let x = zr - 1.0;
    let (mut ar, mut ai) = (c[0], 0.0f64);
    for i in 1..9 {
        let d = x + i as f64;
        let den = d * d + zi * zi;
        ar += c[i] * d / den;
        ai -= c[i] * zi / den;
    }
    // log Gamma(z) = (z - 1/2) ln(T) - T + ln(2pi)/2 + ln(S),  T = x + g + 1/2,
    // Re part (|Gamma| = e^Re): Re[z ln T] = (x+1/2) ln|T| - zi arg(T); -Re T = -T0.
    let t0 = x + 7.5;
    let abs_t = (t0 * t0 + zi * zi).sqrt();
    let arg_t = (zi / t0).atan();
    let re = (x + 0.5) * abs_t.ln() - zi * arg_t - t0
        + 0.5 * (2.0 * std::f64::consts::PI).ln() + 0.5 * (ar * ar + ai * ai).ln();
    let im = (x + 0.5) * arg_t + zi * abs_t.ln() - zi + (ai / ar).atan();
    (re, im)
}

fn xi_classical(a: f64, b: f64) -> (f64, f64) {
    // xi(s) = 0.5 s(s-1) pi^{-s/2} Gamma(s/2) zeta(s)
    let (zr, zi) = zeta_em(a, b);
    let (gr, gi) = lgamma_re_im(a / 2.0, b / 2.0);
    let (gmag, gang) = (gr.exp() * gi.cos(), gr.exp() * gi.sin());
    // pi^{-s/2}
    let lnp = PI.ln();
    let pr = (-a / 2.0 * lnp).exp() * (-b / 2.0 * lnp).cos();
    let pi_ = (-a / 2.0 * lnp).exp() * (-b / 2.0 * lnp).sin();
    // s(s-1)
    let (s1, s2) = (a * (a - 1.0) - b * b, b * (a - 1.0) + a * b);
    // 0.5 * s(s-1) * pi^{-s/2} * Gamma * zeta
    let mut ar = 0.5 * s1 * pr - 0.5 * s2 * pi_;
    let mut ai = 0.5 * s1 * pi_ + 0.5 * s2 * pr;
    // * Gamma (real gmag; imag ignored — Gamma(s/2) imag small; document: using |Gamma|)
    let (gmag, gang) = (gr.exp() * gi.cos(), gr.exp() * gi.sin());
    // * Gamma (complex rotation by gang)
    let (xr, xi_) = (ar * gmag - ai * gang, ar * gang + ai * gmag);
    ar = xr; ai = xi_;
    // * zeta
    let (x, y) = (ar, ai);
    ar = x * zr - y * zi; ai = x * zi + y * zr;
    (ar, ai)
}

fn psi_e(v: f64, tol: f64) -> f64 {
    // psi(exp(v)) = sum_{n>=1} e^{-pi n^2 e^v}; caller passes the LOG variable v.
    let base = v.exp() * PI;
    let nmax = (((-tol.ln() / base).sqrt()) as usize).max(1) + 1;
    let mut s = 0.0;
    for n in 1..=nmax {
        let t = (-base * (n * n) as f64).exp();
        if t < tol { break; }
        s += t;
    }
    s
}

fn t_val(a: f64, b: f64) -> (f64, f64) {
    // T(s=a+ib) = int_0^inf psi(e^v) e^{v s/2} dv, composite Simpson
    let h = 0.02f64;
    let vmax = 30.0f64;
    let tol = 1e-18f64;
    let n = (vmax / h) as usize;
    let mut sr = 0.0f64; let mut si = 0.0f64;
    for i in 0..=n {
        let v = i as f64 * h;
        let wgt = if i == 0 || i == n { 1.0 } else if i % 2 == 1 { 4.0 } else { 2.0 };
        let p = psi_e(v, tol);
        if p == 0.0 { continue; }
        let mag = p * (v * a / 2.0).exp();
        sr += wgt * mag * (v * b / 2.0).cos();
        si += wgt * mag * (v * b / 2.0).sin();
    }
    (sr * h / 3.0, si * h / 3.0)
}

fn main() {
    println!("=== t1: identity (★) xi(s) = 0.5 s(s-1)(T(s)+T(1-s)) + 0.5 ===");
    // s = 1.5 + 2i
    let (a, b) = (1.5f64, 2.0f64);
    let (tr, ti) = t_val(a, b);
    let (t2r, t2i) = t_val(1.0 - a, -b); // T(1-s) = T(1-a - ib)
    let s1 = a * (a - 1.0) - b * b; let s2 = b * (a - 1.0) + a * b;
    let sumr = tr + t2r; let sumi = ti + t2i;
    let rhs_r = 0.5 * (s1 * sumr - s2 * sumi) + 0.5;
    let rhs_i = 0.5 * (s1 * sumi + s2 * sumr);
    let lhs = xi_classical(a, b);
    let err = ((rhs_r - lhs.0).powi(2) + (rhs_i - lhs.1).powi(2)).sqrt();
    let rel = err / ((lhs.0 * lhs.0 + lhs.1 * lhs.1).sqrt() + 1e-30);
    println!("s=1.5+2i LHS=({:.9e},{:.9e}) RHS=({:.9e},{:.9e}) absErr={:.3e} relErr={:.3e}",
        lhs.0, lhs.1, rhs_r, rhs_i, err, rel);

    let (t2v, _) = t_val(2.0, 0.0);
    let (tm1v, _) = t_val(-1.0, 0.0);
    let rhs2 = 0.5 * 2.0 * (t2v + tm1v) + 0.5;
    println!("s=2  xi(2)=pi/6={:.12} RHS={:.12} absErr={:.3e}", PI / 6.0, rhs2, (rhs2 - PI / 6.0).abs());

    let (t05, _) = t_val(0.5, 0.0);
    let rhs05 = 0.5 * (0.5 * -0.5) * (2.0 * t05) + 0.5;
    let xi05 = 0.49712077818831366_f64;
    println!("s=1/2 xi(1/2)={:.12} RHS={:.12} absErr={:.3e}", xi05, rhs05, (rhs05 - xi05).abs());

    // FE symmetry of RHS
    let (a3, b3) = (-0.5f64, -2.0f64);
    let (t3r, t3i) = t_val(a3, b3);
    let (t33r, t33i) = t_val(1.0 - a3, -b3);
    let s1_ = a3 * (a3 - 1.0) - b3 * b3; let s2_ = b3 * (a3 - 1.0) + a3 * b3;
    let sr_ = t3r + t33r; let si_ = t3i + t33i;
    let r3 = 0.5 * (s1_ * sr_ - s2_ * si_) + 0.5;
    let i3 = 0.5 * (s1_ * si_ + s2_ * sr_);
    let dfe = ((r3 - rhs_r).powi(2) + (i3 - rhs_i).powi(2)).sqrt();
    println!("FE check: RHS(1-s=(-0.5-2i)) vs RHS(1.5+2i): dist={:.3e}", dfe);

    println!("=== t2: critical line xi(1/2+it) = 1/2 - (t^2+1/4) A(t), A=Re T ===");
    for (tt, want_zero) in [(14.13472514173469379f64, true), (10.0, false)] {
        let (tr, ti) = t_val(0.5, tt);
        let rex = 0.5 - (tt * tt + 0.25) * tr;
        let imx = -(tt * tt + 0.25) * ti;
        println!("t={:.6} Re xi={:.6e} Im xi={:.6e} |xi|={:.3e}  (want_zero={})",
            tt, rex, imx, (rex * rex + imx * imx).sqrt(), want_zero);
    }

    println!("=== t3: normalized gap rho = |K-target|*(1+t^2)/delta ===");
    let mut min_rho = f64::MAX;
    for &d in &[0.01f64, 0.05, 0.1, 0.2] {
        for &t in &[3.0f64, 10.0, 30.0, 100.0] {
            let sig = 0.5 + d;
            let (tr, ti) = t_val(sig, t);
            let (tr2, ti2) = t_val(1.0 - sig, -t); // T(1-s)
            let kr = tr + tr2; let ki = ti + ti2;
            let asq = sig * sig + t * t;
            let bsq = (sig - 1.0).powi(2) + t * t;
            let den = asq * bsq;
            let tgt_r = (0.25 + t * t - d * d) / den;
            let tgt_i = 2.0 * d * t / den;
            let gap = ((kr - tgt_r).powi(2) + (ki - tgt_i).powi(2)).sqrt();
            let rho = gap * (1.0 + t * t) / d;
            if rho < min_rho { min_rho = rho; }
            println!("d={:.2} t={:6.1} K=({:+.4e},{:+.4e}) target=({:+.4e},{:+.4e}) gap={:.3e} rho={:.3e}",
                d, t, kr, ki, tgt_r, tgt_i, gap, rho);
        }
    }
    println!("min rho over grid (observed kappa candidate) = {:.6e}", min_rho);
    println!("STOPPING RULE: t1 relErr(1.5+2i) must be < 1e-6; see value above.");
}