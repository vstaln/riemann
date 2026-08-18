// Correct protocol for GORTTW G_m: they are the Taylor coefficients of log R_M(j) at j=0,
// log R_M(j) = -sum_m G_m(M) Delta^{2m-2} j^m,  R_M(j) = gamma(M-j)/gamma(M).
//
// The paper defines G_m via -a_m = G_m * Delta^{2m-2} where a_m are the Taylor coefficients
// of log R_M(j) at j=0.  (This differs from polynomial interpolation through j=1..4, which
// mixes in higher a_m: earlier cubic/quartic fits measured *interpolation* coefficients, and
// the striking resid/D^4 -> 4/3 was PROVEN to be an interpolation artifact -- the cubic
// reproduces log(1-2D^2) exactly at j=1,2, forcing 4/3 identically, with NO G4 content.)
//
// Here: evaluate log gamma at REAL arguments via the saddle quadrature (gamma extends to
// real M), sample log R_M(j) at j = 0, 0.1, ..., 0.6 (7 points, small range, well-conditioned),
// interpolate exactly with a degree-6 polynomial, read off Taylor coefficients a_1..a_6.
// Then G_m = -a_m / Delta^{2m-2}.
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

fn logfact_real(x: f64) -> Float {
    Float::with_val(PG, x + 1.0).ln_gamma()
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

// exact interpolation through n equally spaced points x_i = i*h (h>0), x0 = 0.
// returns monomial coefficients [c0, c1, ..., c_{n-1}] of the interpolating polynomial.
// (Newton forward differences converted to monomial form)
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
    // Horner for Newton basis P(x) = sum_k c_k prod_{i<k}(x - x_i), x_i = i*h:
    //   mon = c_{n-1};  for k = n-2 .. 0: mon = mon * (x - x_k) + c_k
    let mut mon = vec![zf(PG, 0.0); n];
    for k in (0..n).rev() {
        let mut fact = 1.0;
        for j in 2..=k { fact *= j as f64; }
        let ck = Float::with_val(PG, &diff[k][0] / zf(PG, fact * h.powi(k as i32)));
        if k < n - 1 {
            let xk = k as f64 * h;
            let mut shifted = vec![zf(PG, 0.0); n];
            for i in 0..n - 1 {
                shifted[i + 1] += mon[i].clone();
            }
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
    println!("TRUE G_m via Taylor coeffs of log R_M(j) at j=0 (saddle gamma at real args, {} GL nodes, deg-6 interp on j in [0,0.6]):", ngl);
    println!("{:>6} | {:>10} {:>12} {:>12} {:>12} {:>12} {:>12} | G3-2/3 | G4-2/3", "M", "D", "G1", "G2", "G3", "G4", "G5");
    for &m in &[300f64, 500.0, 1000.0, 2000.0, 5000.0, 10000.0] {
        let n = 7; // j = 0 .. 0.6 step 0.1
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
        let a5 = mon[5].clone();
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
        let d8 = Float::with_val(PG, &d6 * &d2);
        let na1 = Float::with_val(PG, -&a1);
        let na2 = Float::with_val(PG, -&a2);
        let na3 = Float::with_val(PG, -&a3);
        let na4 = Float::with_val(PG, -&a4);
        let na5 = Float::with_val(PG, -&a5);
        let g1 = na1.clone();
        let g2 = Float::with_val(PG, &na2 / &d2);
        let g3 = Float::with_val(PG, &na3 / &d4);
        let g4 = Float::with_val(PG, &na4 / &d6);
        let g5 = Float::with_val(PG, &na5 / &d8);
        let twoth = zf(PG, 2.0 / 3.0);
        println!(
            "{:6.0} | {:10.5} {:12.4} {:12.6} {:12.6} {:12.6} {:12.4} | {:+.3e} | {:+.3e}",
            m, d.to_f64(), g1.to_f64(), g2.to_f64(), g3.to_f64(), g4.to_f64(), g5.to_f64(),
            (g3 - &twoth).to_f64(), (g4 - &twoth).to_f64()
        );
    }
    println!("\nExpected limits: G2 -> 1, G3 -> 2/3, G4 -> 2/3 (paper Thm 2.1(2)).");
}
