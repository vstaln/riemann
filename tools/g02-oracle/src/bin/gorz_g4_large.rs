// Measure G4(M) at large M via saddle log-gamma (quartic fit), to decide:
// paper limit G4 -> 2/3  vs  data suggesting G4 -> 0 (which would explain resid/D^4 -> 4/3).
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

// solve quartic through j=1..4 (invert Vandermonde), residual at j=5
fn fit_quartic(lg: &[Float]) -> (Float, Float, Float, Float, Float) {
    let l = |j: usize| -> Float { Float::with_val(PG, &lg[j] - &lg[0]) };
    let mut a: Vec<Vec<Float>> = Vec::new();
    let mut b: Vec<Float> = Vec::new();
    for i in 0..4 {
        let jj = (i + 1) as f64;
        let mut row = Vec::new();
        for k in 0..4 {
            row.push(Float::with_val(PG, jj.powi(k as i32 + 1)));
        }
        a.push(row);
        b.push(l(i + 1));
    }
    let mut x = vec![zf(PG, 0.0); 4];
    for col in 0..4 {
        let mut piv = col;
        for r in col + 1..4 {
            if a[r][col].clone().abs() > a[piv][col].clone().abs() { piv = r; }
        }
        a.swap(col, piv); b.swap(col, piv);
        let pv = a[col][col].clone();
        for r in col + 1..4 {
            let f = Float::with_val(PG, &a[r][col] / &pv);
            for c in col..4 {
                let t = Float::with_val(PG, &f * &a[col][c]);
                let v = Float::with_val(PG, &a[r][c] - &t);
                a[r][c] = v;
            }
            let t = Float::with_val(PG, &f * &b[col]);
            let v = Float::with_val(PG, &b[r] - &t);
            b[r] = v;
        }
    }
    for col in (0..4).rev() {
        let mut s = b[col].clone();
        for c in col + 1..4 {
            let t = Float::with_val(PG, &a[col][c] * &x[c]);
            s = Float::with_val(PG, &s - &t);
        }
        x[col] = Float::with_val(PG, &s / &a[col][col]);
    }
    let mut pred = zf(PG, 0.0);
    for k in 0..4 {
        let j5 = Float::with_val(PG, 5.0f64.powi(k as i32 + 1));
        pred = Float::with_val(PG, &pred + Float::with_val(PG, &x[k] * &j5));
    }
    let res = Float::with_val(PG, &pred - &l(5)).abs();
    (x[0].clone(), x[1].clone(), x[2].clone(), x[3].clone(), res)
}

fn main() {
    let ngl = std::env::args().nth(1).and_then(|s| s.parse().ok()).unwrap_or(64usize);
    let gl_s = gl_nodes(PG, ngl);
    println!("{:>6} | {:>10} {:>12} {:>12} {:>12} {:>12} {:>10}", "M", "D", "G2", "G3", "G4", "G4-2/3", "fit res");
    for &m in &[300usize, 500, 1000, 2000, 5000, 10000, 20000, 50000] {
        let mut lg = vec![zf(PG, 0.0); 6];
        for j in 0..6 { lg[j] = log_gamma_saddle(m - j, &gl_s); }
        let (_, c2, c3, c4, res) = fit_quartic(&lg);
        let t1 = Float::with_val(PG, &lg[2] + &lg[0]);
        let t2 = Float::with_val(PG, zf(PG, 2.0) * &lg[1]);
        let x = Float::with_val(PG, &t1 - &t2);
        let d2 = Float::with_val(PG, 0.5 * (zf(PG, 1.0) - x.exp()));
        let d = d2.clone().sqrt();
        let d4 = Float::with_val(PG, &d2 * &d2);
        let d6 = Float::with_val(PG, &d4 * &d2);
        // NOTE: log R_M(j) = -sum G_m D^{2m-2} j^m  => c2 = -G2 D^2, c3 = -G3 D^4, c4 = -G4 D^6
        let nc2 = Float::with_val(PG, -&c2);
        let nc3 = Float::with_val(PG, -&c3);
        let nc4 = Float::with_val(PG, -&c4);
        let g2 = Float::with_val(PG, &nc2 / &d2);
        let g3 = Float::with_val(PG, &nc3 / &d4);
        let g4 = Float::with_val(PG, &nc4 / &d6);
        let twoth = zf(PG, 2.0 / 3.0);
        println!(
            "{:6} | {:10.5} {:12.6} {:12.6} {:12.6} {:12.4e} {:10.1e}",
            m, d.to_f64(), g2.to_f64(), g3.to_f64(), g4.to_f64(), (g4 - &twoth).to_f64(), res.to_f64()
        );
    }
    println!("\nIf G4 -> 0: resid/D^4 -> 4/3 (measured). If G4 -> 2/3 (paper): resid/D^4 -> 10/3.");
}
