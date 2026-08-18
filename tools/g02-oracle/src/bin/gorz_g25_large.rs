// Verify GORTTW (2.5): G2 = 1 + (1-3*G3)*Delta^2 + O(Delta^4) at large M,
// using the same saddle log-gamma extraction as gorz_g3_large (210-bit fit).
use rug::float::Constant;
use rug::ops::Pow;
use rug::Float;
use std::fs;

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
        let init = (std::f64::consts::PI * (j as f64 + 0.75) / (order as f64 + 0.5)).cos();
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

fn logfact(n: usize, prec: u32) -> Float {
    let mut s = zf(prec, 0.0);
    for j in 2..=n { s += zf(prec, j as f64).ln(); }
    s
}

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
    let lfact = logfact(2 * k as usize, prec);
    Float::with_val(prec, &logmk - &lfact)
}

fn log_gamma_saddle(m: usize, gl: &[(Float, Float)]) -> Float {
    let l8 = zf(PG, 8.0).ln();
    let lf = logfact(m, PG);
    let lb = logb_saddle(m as f64, gl, PG);
    let s1 = Float::with_val(PG, &l8 + &lf);
    Float::with_val(PG, &s1 + &lb)
}

fn fit_cubic(lg: &[Float]) -> (Float, Float, Float, Float) {
    let l = |j: usize| -> Float { Float::with_val(PG, &lg[j] - &lg[0]) };
    let l1 = l(1); let l2 = l(2); let l3 = l(3); let l4 = l(4);
    let b1 = Float::with_val(PG, &l2 - Float::with_val(PG, &zf(PG, 2.0) * &l1));
    let c1 = Float::with_val(PG, &l3 - Float::with_val(PG, &zf(PG, 3.0) * &l1));
    let a3 = Float::with_val(PG, (Float::with_val(PG, &zf(PG, 3.0) * &b1) - &c1) / zf(PG, 6.0));
    let t1 = Float::with_val(PG, &b1 + Float::with_val(PG, &zf(PG, 6.0) * &a3));
    let nt1 = Float::with_val(PG, -&t1);
    let a2 = Float::with_val(PG, &nt1 / zf(PG, 2.0));
    let t2 = Float::with_val(PG, &a2 + &a3);
    let nl1 = Float::with_val(PG, -&l1);
    let a1 = Float::with_val(PG, &nl1 - &t2);
    let t3 = Float::with_val(PG, &zf(PG, 64.0) * &a3);
    let t4 = Float::with_val(PG, &zf(PG, 16.0) * &a2);
    let t5 = Float::with_val(PG, &zf(PG, 4.0) * &a1);
    let l4p = Float::with_val(PG, &t5 + &t4);
    let l4p = Float::with_val(PG, &l4p + &t3);
    let nl4p = Float::with_val(PG, -&l4p);
    (a1, a2, a3, Float::with_val(PG, &nl4p - &l4).abs())
}

fn main() {
    let ngl = std::env::args().nth(1).and_then(|s| s.parse().ok()).unwrap_or(64usize);
    let gl_s = gl_nodes(PG, ngl);
    println!("GORTTW (2.5) at large M: G2 = 1 + (1-3*G3)*D^2 + O(D^4); residual = |G2 - pred| / D^4");
    println!("{:>10} | {:>10} {:>10} {:>12} {:>12} {:>10}", "M", "G2", "G3", "G2_pred", "|resid|", "resid/D^4");
    for &m in &[1000usize, 2000, 5000, 10000, 20000, 50000] {
        let mut lg = vec![zf(PG, 0.0); 5];
        for j in 0..5 { lg[j] = log_gamma_saddle(m - j, &gl_s); }
        let t1 = Float::with_val(PG, &lg[2] + &lg[0]);
        let t2 = Float::with_val(PG, zf(PG, 2.0) * &lg[1]);
        let x = Float::with_val(PG, &t1 - &t2);
        let d2 = Float::with_val(PG, 0.5 * (zf(PG, 1.0) - x.exp()));
        let (_, a2, a3, _) = fit_cubic(&lg);
        let g2 = Float::with_val(PG, &a2 / &d2);
        let d22 = Float::with_val(PG, &d2 * &d2);
        let g3 = Float::with_val(PG, &a3 / &d22);
        // pred = 1 + (1 - 3 G3) D^2
        let three_g3 = Float::with_val(PG, zf(PG, 3.0) * &g3);
        let one_m = Float::with_val(PG, zf(PG, 1.0) - &three_g3);
        let g2p = Float::with_val(PG, zf(PG, 1.0) + Float::with_val(PG, &one_m * &d2));
        let resid = Float::with_val(PG, &g2 - &g2p).abs();
        let d4 = d22.clone(); // d22 = D^2 * D^2 = D^4 (was mistakenly D^8)
        let rat = Float::with_val(PG, &resid / &d4);
        println!(
            "{:10} | {:12.9} {:12.9} {:14.9} {:13.4e} {:14.9}",
            m, g2.to_f64(), g3.to_f64(), g2p.to_f64(), resid.to_f64(), rat.to_f64()
        );
    }
    println!("\n(If resid/D^4 stays O(1), (2.5) holds to O(D^4) at large M — internal consistency of the saddle extraction.)");
}
