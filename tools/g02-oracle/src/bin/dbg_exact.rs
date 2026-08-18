// Cross-validate exact integral (3.1) log gamma at INTEGER M against certified 210-bit table
use rug::float::Constant;
use rug::ops::Pow;
use rug::Float;
use std::fs;
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
    let mut u0 = (z.ln() - PI.ln()).max(1.0);
    for _ in 0..200 {
        let eu = u0.exp();
        let g = z / u0 + 0.25 - PI * eu;
        let gp = -z / (u0 * u0) - PI * eu;
        let du = -g / gp;
        u0 += du;
        if du.abs() < 1e-14 { break; }
    }
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
    let txt = fs::read_to_string("/home/vstaln/riemann/research/notes/g02-moments-oracle-2026-08-18.txt").expect("read");
    let mut b: Vec<Float> = Vec::new();
    for line in txt.lines() {
        let line = line.trim();
        if line.is_empty() || line.starts_with('#') || line.starts_with("g0-2") { continue; }
        let cols: Vec<&str> = line.split('\t').collect();
        if cols.len() >= 3 {
            if let Ok(v) = Float::parse_radix(cols[2].trim(), 10) { b.push(Float::with_val(PG, v)); }
        }
    }
    let logfact = |n: usize| -> Float {
        let mut s = zf(PG, 0.0);
        for j in 2..=n { s += zf(PG, j as f64).ln(); }
        s
    };
    println!("M | exact-integral log gamma | certified | |diff|");
    for &m in &[40usize, 100, 200, 300] {
        let lg_ex = log_gamma_real(m as f64, &gl_s);
        let l8 = zf(PG, 8.0).ln();
        let lf = logfact(m);
        let lb_cert = b[m].clone().ln();
        let lg_cert = Float::with_val(PG, Float::with_val(PG, &l8 + &lf) + &lb_cert);
        println!("{} | {:.12} | {:.12} | {:.2e}",
            m, lg_ex.to_f64(), lg_cert.to_f64(), (lg_ex - &lg_cert).to_f64().abs());
    }
}
