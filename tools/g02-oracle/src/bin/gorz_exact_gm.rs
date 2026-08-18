// TRUE GORTTW G_m via exact integral (3.1) for gamma at REAL arguments.
//
// gamma(M) = [M!/(2M)!] * [32*C(2M,2)*F(2M-2) - F(2M)] / 2^{2M-1},
// F(z) = int_0^inf u^z e^{u/4} (sum_k e^{-pi k^2 e^u}) du   (exact, no asymptotic error).
// Sample log R_M(j) = log gamma(M-j) - log gamma(M) at j = 0..0.6, interpolate exactly,
// read off Taylor coefficients a_m at j=0, then G_m = -a_m / Delta^{2m-2}.
use rug::float::Constant;
use rug::ops::Pow;
use rug::Float;
use std::f64::consts::PI;

const PG: u32 = 210;

fn zf(prec: u32, v: f64) -> Float { Float::with_val(prec, v) }

fn legendre(prec: u32, n: usize, x: &Float) -> (Float, Float) {
    let mut p0 = zf(prec, 1.0);
    if n == 0 { return (p0, zf(prec, 0.0)); }
    let mut p1 = x.clone();
    for k in 1..n {
        let kf = zf(prec, k as f64);
        let kp1 = zf(prec, (k + 1) as f64);
        let c = zf(prec, (2 * k + 1) as f64);
        let t1 = Float::with_val(prec, &c * x);
        let t2 = Float::with_val(prec, &t1 * &p1);
        let u1 = Float::with_val(prec, &kf * &p0);
        let v1 = Float::with_val(prec, &t2 - &u1);
        let p2 = Float::with_val(prec, &v1 / &kp1);
        p0 = p1; p1 = p2;
    }
    let x2 = Float::with_val(prec, x * x);
    let tp = Float::with_val(prec, x * &p1);
    let t = Float::with_val(prec, &tp - &p0);
    let num = Float::with_val(prec, zf(prec, n as f64) * &t);
    let den = Float::with_val(prec, &x2 - zf(prec, 1.0));
    (p1, Float::with_val(prec, &num / &den))
}

fn gl_nodes(prec: u32, order: usize) -> Vec<(Float, Float)> {
    let mut out = Vec::with_capacity(order);
    for j in 0..order {
        let init = (PI * (j as f64 + 0.75) / (order as f64 + 0.5)).cos();
        let mut x = zf(prec, init);
        for _ in 0..80 {
            let (p, dp) = legendre(prec, order, &x);
            let dx = Float::with_val(prec, &p / &dp);
            let nx = Float::with_val(prec, &x - &dx);
            x = nx;
            if dx.clone().abs() < zf(prec, 1e-75) { break; }
        }
        let (_, dp) = legendre(prec, order, &x);
        let x2 = Float::with_val(prec, &x * &x);
        let one_m = Float::with_val(prec, zf(prec, 1.0) - &x2);
        let dp2 = Float::with_val(prec, &dp * &dp);
        let den = Float::with_val(prec, &one_m * &dp2);
        let w = Float::with_val(prec, zf(prec, 2.0) / &den);
        out.push((x, w));
    }
    out
}

// theta-type sum S(u) = sum_{k>=1} e^{-pi k^2 e^u}, truncated when term < 2^{-230}
fn theta_sum(u: &Float, prec: u32) -> Float {
    let pi = Float::with_val(prec, Constant::Pi);
    let eu = Float::with_val(prec, u).exp();
    let pieu = Float::with_val(prec, &pi * &eu);
    let mut s = zf(prec, 0.0);
    let mut k = 1u32;
    loop {
        let k2 = zf(prec, (k * k) as f64);
        let prod = Float::with_val(prec, &pieu * &k2);
        let arg = Float::with_val(prec, -&prod);
        let term = arg.exp();
        if term < zf(prec, 1e-70) && k > 1 { break; }
        s += term;
        k += 1;
    }
    s
}

// F(z) = int_0^inf u^z e^{u/4} S(u) du via GL over a sigma-scaled window around the saddle.
// log integrand L(u) = z ln u + u/4 + ln S(u).  Saddle: z/u + 1/4 + S'/S = 0.
// S(u) ~ e^{-pi e^u} (k=1), ln S ~ -pi e^u, d/du ~ -pi e^u.  Solve iteratively in f64.
fn f_exact(z: f64, gl: &[(Float, Float)], prec: u32) -> Float {
    // saddle of L(u) = z ln u + u/4 + ln S(u):  z/u + 1/4 + S'/S = 0,  S'/S -> -pi e^u (k=1).
    // Solve z/u + 1/4 = pi e^u by fixed-point iteration u = ln((z/u + 1/4)/pi).
    // (Newton with the k=1-only approximation was found to oscillate and converge to a
    //  WRONG root for large z, placing the quadrature window off the integrand -> F ~ 0.)
    let mut u0 = ((z / PI).ln()).max(1.0);
    for _ in 0..200 {
        let u1 = ((z / u0 + 0.25) / PI).ln();
        if (u1 - u0).abs() < 1e-15 { u0 = u1; break; }
        u0 = u1;
    }
    // refine with exact S'/S via central difference? approximate fine: window covers it.
    // curvature: L'' = -z/u^2 - pi e^u
    let curv = (-z / (u0 * u0) - PI * u0.exp()).abs();
    let sigma = 1.0 / curv.sqrt();
    let half = (12.0 * sigma).max(1e-2);
    let lo = (u0 - half).max(1e-6);
    let hi = u0 + half;
    let npan: usize = 16;
    let h = (hi - lo) / npan as f64;
    let mut acc = zf(prec, 0.0);
    for p in 0..npan {
        let a = zf(prec, lo + h * p as f64);
        let b = zf(prec, lo + h * (p + 1) as f64);
        let ab = Float::with_val(prec, &a + &b);
        let ba = Float::with_val(prec, &b - &a);
        let mid = Float::with_val(prec, &ab / zf(prec, 2.0));
        let hh = Float::with_val(prec, &ba / zf(prec, 2.0));
        for (x, w) in gl {
            let hx = Float::with_val(prec, &hh * x);
            let u = Float::with_val(prec, &mid + &hx);
            let lu = Float::with_val(prec, &u).ln();
            let uz = Float::with_val(prec, zf(prec, z) * &lu);
            let uq = Float::with_val(prec, &u / zf(prec, 4.0));
            let l1 = Float::with_val(prec, &uz + &uq);
            let l2 = Float::with_val(prec, theta_sum(&u, prec).ln());
            let logf = Float::with_val(prec, &l1 + &l2);
            let wf = Float::with_val(prec, w * logf.exp());
            acc += wf;
        }
    }
    Float::with_val(prec, &acc * zf(prec, h))
}

// gamma(M) exact for real M via (3.1)
fn log_gamma_real(m: f64, gl: &[(Float, Float)]) -> Float {
    let lf = Float::with_val(PG, m + 1.0).ln_gamma();       // log M!
    let lf2 = Float::with_val(PG, 2.0 * m + 1.0).ln_gamma(); // log (2M)!
    let f1 = f_exact(2.0 * m - 2.0, gl, PG); // F(2M-2)
    let f2 = f_exact(2.0 * m, gl, PG);       // F(2M)
    // 32*C(2M,2) = 32 * (2M)(2M-1)/2 = 16 (2M)(2M-1)
    let c32 = Float::with_val(PG, 16.0 * (2.0 * m) * (2.0 * m - 1.0));
    let t1 = Float::with_val(PG, &c32 * &f1);
    let num = Float::with_val(PG, &t1 - &f2);
    let den = Float::with_val(PG, zf(PG, 2.0).pow(2.0 * m - 1.0));
    let lg = Float::with_val(PG, &num / &den);
    // gamma(M) = M!/(2M)! * lg  => log gamma = log M! - log(2M)! + log lg
    let s1 = Float::with_val(PG, &lf - &lf2);
    let s2 = Float::with_val(PG, &s1 + lg.ln());
    s2
}

// exact interpolation through n equally spaced points x_i = i*h -> monomial coeffs
fn interpolate(h: f64, ys: &[Float]) -> Vec<Float> {
    let n = ys.len();
    let mut diff: Vec<Vec<Float>> = vec![ys.to_vec()];
    for k in 1..n {
        let mut row = Vec::new();
        for i in 0..n - k {
            let d = Float::with_val(PG, &diff[k - 1][i + 1] - &diff[k - 1][i]);
            row.push(d);
        }
        diff.push(row);
    }
    let mut mon = vec![zf(PG, 0.0); n];
    for k in (0..n).rev() {
        let mut fact = 1.0;
        for j in 2..=k { fact *= j as f64; }
        let ck = Float::with_val(PG, &diff[k][0] / zf(PG, fact * h.powi(k as i32)));
        if k < n - 1 {
            let xk = k as f64 * h;
            let mut shifted = vec![zf(PG, 0.0); n];
            for i in 0..n - 1 { shifted[i + 1] += mon[i].clone(); }
            for i in 0..n {
                let t = Float::with_val(PG, &mon[i] * zf(PG, xk));
                shifted[i] = Float::with_val(PG, &shifted[i] - &t);
            }
            mon = shifted;
        }
        mon[0] = Float::with_val(PG, &mon[0] + &ck);
    }
    mon
}

fn main() {
    let ngl = std::env::args().nth(1).and_then(|s| s.parse().ok()).unwrap_or(64usize);
    let gl_s = gl_nodes(PG, ngl);
    println!("TRUE G_m via EXACT integral (3.1), deg-6 interp on j in [0,0.6], {} GL nodes:", ngl);
    println!("{:>6} | {:>10} {:>12} {:>12} {:>12} {:>12} | G2-1 | G3-2/3 | G4-2/3", "M", "D", "G1", "G2", "G3", "G4");
    for &m in &[40f64, 100.0, 200.0, 300.0, 500.0, 1000.0, 2000.0, 5000.0, 10000.0] {
        let n = 7;
        let h = 0.1;
        let mut ys = Vec::new();
        let lg_m = log_gamma_real(m, &gl_s);
        for i in 0..n {
            let j = i as f64 * h;
            let lg_mj = log_gamma_real(m - j, &gl_s);
            ys.push(Float::with_val(PG, &lg_mj - &lg_m));
        }
        let mon = interpolate(h, &ys);
        let a1 = mon[1].clone();
        let a2 = mon[2].clone();
        let a3 = mon[3].clone();
        let a4 = mon[4].clone();
        let lg0 = log_gamma_real(m, &gl_s);
        let lg1 = log_gamma_real(m - 1.0, &gl_s);
        let lg2 = log_gamma_real(m - 2.0, &gl_s);
        let t1 = Float::with_val(PG, &lg2 + &lg0);
        let t2 = Float::with_val(PG, zf(PG, 2.0) * &lg1);
        let x = Float::with_val(PG, &t1 - &t2);
        let d2 = Float::with_val(PG, 0.5 * (zf(PG, 1.0) - x.exp()));
        let d = d2.clone().sqrt();
        let d4 = Float::with_val(PG, &d2 * &d2);
        let d6 = Float::with_val(PG, &d4 * &d2);
        let na1 = Float::with_val(PG, -&a1);
        let na2 = Float::with_val(PG, -&a2);
        let na3 = Float::with_val(PG, -&a3);
        let na4 = Float::with_val(PG, -&a4);
        let g1 = na1.clone();
        let g2 = Float::with_val(PG, &na2 / &d2);
        let g3 = Float::with_val(PG, &na3 / &d4);
        let g4 = Float::with_val(PG, &na4 / &d6);
        let one = zf(PG, 1.0);
        let twoth = zf(PG, 2.0 / 3.0);
        println!(
            "{:6.0} | {:10.5} {:12.4} {:12.6} {:12.6} {:12.6} | {:+.2e} | {:+.2e} | {:+.2e}",
            m, d.to_f64(), g1.to_f64(), g2.to_f64(), g3.to_f64(), g4.to_f64(),
            (g2 - &one).to_f64(), (g3 - &twoth).to_f64(), (g4 - &twoth).to_f64()
        );
    }
    println!("\nExpected limits (paper Thm 2.1(2)): G2 -> 1, G3 -> 2/3, G4 -> 2/3.");
}
