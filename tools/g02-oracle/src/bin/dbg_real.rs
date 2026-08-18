// Debug: saddle log gamma at real arguments vs certified integer values
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
fn phi(u: &Float, prec: u32) -> Float {
    let pi = Float::with_val(prec, Constant::Pi);
    let two = zf(prec, 2.0);
    let e2u = Float::with_val(prec, zf(prec, 2.0) * u).exp();
    let e9 = Float::with_val(prec, zf(prec, 4.5) * u).exp();
    let e5 = Float::with_val(prec, zf(prec, 2.5) * u).exp();
    let pi2 = Float::with_val(prec, &pi * &pi);
    let npi = Float::with_val(prec, -&pi);
    let c2pi2 = Float::with_val(prec, &two * &pi2);
    let c3pi = Float::with_val(prec, zf(prec, 3.0) * &pi);
    let mut s = zf(prec, 0.0);
    for n in 1..=14u32 {
        let n2 = zf(prec, (n * n) as f64);
        let n4 = Float::with_val(prec, &n2 * &n2);
        let a1 = Float::with_val(prec, &npi * &n2);
        let a2 = Float::with_val(prec, &a1 * &e2u);
        let e = a2.exp();
        let c1a = Float::with_val(prec, &c2pi2 * &n4);
        let c1 = Float::with_val(prec, &c1a * &e9);
        let c2a = Float::with_val(prec, &c3pi * &n2);
        let c2 = Float::with_val(prec, &c2a * &e5);
        let d = Float::with_val(prec, &c1 - &c2);
        s += Float::with_val(prec, &d * &e);
    }
    Float::with_val(prec, &s * &two)
}
fn logfact_real(x: f64) -> Float { Float::with_val(PG, x + 1.0).ln_gamma() }
fn logb_saddle(k: f64, gl: &[(Float, Float)], prec: u32) -> Float {
    let pi = Float::with_val(prec, Constant::Pi);
    let lnk = zf(prec, k).ln();
    let lnlnk = Float::with_val(prec, &lnk).ln();
    let c = Float::with_val(prec, zf(prec, 2.0) / &pi).ln();
    let d1 = Float::with_val(prec, &lnk - &lnlnk);
    let d2 = Float::with_val(prec, &d1 + c);
    let u0 = Float::with_val(prec, &d2 / zf(prec, 2.0));
    let u0f: f64 = u0.to_f64();
    let sigma = u0f / (2.0 * k).sqrt();
    let half = (10.0 * sigma).max(1e-3);
    let lo = (u0f - half).max(1e-4);
    let hi = u0f + half;
    let npan: usize = 12;
    let h = (hi - lo) / npan as f64;
    let mut acc = zf(prec, 0.0);
    let two = zf(prec, 2.0);
    let ltwo = zf(prec, 2.0).ln();
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
            let p = Float::with_val(prec, phi(&u, prec).ln());
            let q = Float::with_val(prec, zf(prec, 2.0 * k) * &lu);
            let r = Float::with_val(prec, &ltwo + &p);
            let logf = Float::with_val(prec, &r + &q);
            let wf = Float::with_val(prec, w * logf.exp());
            acc += wf;
        }
    }
    let mk = Float::with_val(prec, &acc * zf(prec, h));
    let logmk = Float::with_val(prec, &mk).ln();
    let lfact = logfact_real(2.0 * k);
    Float::with_val(prec, &logmk - &lfact)
}
fn log_gamma_real(m: f64, gl: &[(Float, Float)]) -> Float {
    let l8 = zf(PG, 8.0).ln();
    let lf = logfact_real(m);
    let lb = logb_saddle(m, gl, PG);
    let s1 = Float::with_val(PG, &l8 + &lf);
    Float::with_val(PG, &s1 + &lb)
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
    println!("M | saddle log gamma | certified log gamma | diff | logb_saddle | logb_cert");
    for &m in &[100usize, 200, 300] {
        let lg_sad = log_gamma_real(m as f64, &gl_s);
        let l8 = zf(PG, 8.0).ln();
        let lf = logfact(m);
        let lb_cert = b[m].clone().ln();
        let lg_cert = Float::with_val(PG, Float::with_val(PG, &l8 + &lf) + &lb_cert);
        let lb_sad = logb_saddle(m as f64, &gl_s, PG);
        println!("{} | {:.12} | {:.12} | {:.2e} | {:.12} | {:.12}",
            m, lg_sad.to_f64(), lg_cert.to_f64(), (lg_sad - &lg_cert).to_f64().abs(),
            lb_sad.to_f64(), lb_cert.to_f64());
    }
    // also test the smoothness of log gamma at real args: differences should be ~-6 per unit
    println!("\nlog_gamma_real(1000) - log_gamma_real(999) should be ~ -6..-9 (log R_M(1) = a1, G1 = -a1):");
    for &m in &[500.0, 1000.0] {
        let d1 = log_gamma_real(m - 0.5, &gl_s) - log_gamma_real(m, &gl_s);
        println!("M={}: logR(0.5) = {:.6}", m, d1.to_f64());
    }
}
