// Debug: raw logR values and forward differences at M=2000 to see why G3 extraction fails
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
fn f_exact(z: f64, gl: &[(Float, Float)], prec: u32) -> Float {
    let mut u0 = ((z / PI).ln()).max(1.0);
    for _ in 0..200 {
        let u1 = ((z / u0 + 0.25) / PI).ln();
        if (u1 - u0).abs() < 1e-15 { u0 = u1; break; }
        u0 = u1;
    }
    let curv = (z / (u0 * u0) + PI * u0.exp()).abs();
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
fn log_gamma_real(m: f64, gl: &[(Float, Float)]) -> Float {
    let lf = Float::with_val(PG, m + 1.0).ln_gamma();
    let lf2 = Float::with_val(PG, 2.0 * m + 1.0).ln_gamma();
    let f1 = f_exact(2.0 * m - 2.0, gl, PG);
    let f2 = f_exact(2.0 * m, gl, PG);
    let c32 = Float::with_val(PG, 16.0 * (2.0 * m) * (2.0 * m - 1.0));
    let t1 = Float::with_val(PG, &c32 * &f1);
    let num = Float::with_val(PG, &t1 - &f2);
    let den = Float::with_val(PG, zf(PG, 2.0).pow(2.0 * m - 1.0));
    let lg = Float::with_val(PG, &num / &den);
    let s1 = Float::with_val(PG, &lf - &lf2);
    let s2 = Float::with_val(PG, &s1 + lg.ln());
    s2
}
fn main() {
    let gl_s = gl_nodes(PG, 64);
    for &m in &[1000f64, 2000.0, 5000.0] {
        println!("M = {}", m);
        let lg_m = log_gamma_real(m, &gl_s);
        let mut ys = Vec::new();
        for i in 0..7 {
            let j = i as f64 * 0.1;
            let lg_mj = log_gamma_real(m - j, &gl_s);
            let r = Float::with_val(PG, &lg_mj - &lg_m);
            ys.push(r.clone());
            println!("  logR({:.1}) = {:.15}", j, r.to_f64());
        }
        // forward differences
        let mut d = ys.clone();
        for k in 1..7 {
            let mut nd = Vec::new();
            for i in 0..d.len() - 1 {
                nd.push(Float::with_val(PG, &d[i + 1] - &d[i]));
            }
            d = nd;
            println!("  D^{}(y0) = {:.6e}", k, d[0].to_f64());
        }
        // predicted a3 from G3~2/3: a3 = -G3*D^4 ~ -0.667*D^4; check D^3 y0 ~ 6*a3*h^3
        println!();
    }
}
