// GORTTW G3 -> 2/3 at large M via saddle-quadrature log b_k (oracle's logb_saddle).
//
// The certified table stops at k=300; the crude GORTTW (3.2) asymptotic has O(1/M)
// error that swamps Delta^4 ~ 1/(4M^2). The oracle's saddle GL quadrature of
//   log b_k = log(2 int Phi(u) u^{2k} du) - log((2k)!)
// is accurate at large k (saddle-concentrated integrand), so it can test the
// GORTTW limit prediction G3 -> 2/3 at M up to ~1e5.
//
// Plan:
//   1. Cross-validate saddle log b_k vs the certified table at M = 100..299.
//   2. Extract G2, G3 from 5 consecutive log gamma values (fit cubic in j),
//      same scheme as gorz_g3.rs.
//   3. Report G2 -> 1, G3 -> 2/3 at large M.

use rug::float::Constant;
use rug::ops::Pow;
use rug::Float;
use std::fs;

const PG: u32 = 210;

fn zf(prec: u32, v: f64) -> Float {
    Float::with_val(prec, v)
}

fn legendre(prec: u32, n: usize, x: &Float) -> (Float, Float) {
    let mut p0 = zf(prec, 1.0);
    if n == 0 {
        return (p0, zf(prec, 0.0));
    }
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
        p0 = p1;
        p1 = p2;
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
            if dx.clone().abs() < zf(prec, 1e-75) {
                break;
            }
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

// Phi(u) = 2 sum_n (2 pi^2 n^4 e^{9u/2} - 3 pi n^2 e^{5u/2}) e^{-pi n^2 e^{2u}}
// (verbatim structure from oracle main.rs)
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
    for j in 2..=n {
        s += zf(prec, j as f64).ln();
    }
    s
}

// log b_k via saddle GL quadrature (copied from oracle main.rs)
fn logb_saddle(k: f64, gl: &[(Float, Float)], prec: u32) -> Float {
    let pi = Float::with_val(prec, Constant::Pi);
    let lnk = zf(prec, k).ln();
    let lnlnk = Float::with_val(prec, &lnk).ln();
    let c = Float::with_val(prec, zf(prec, 2.0) / &pi).ln();
    let d1 = Float::with_val(prec, &lnk - &lnlnk);
    let d2 = Float::with_val(prec, &d1 + c);
    let u0 = Float::with_val(prec, &d2 / zf(prec, 2.0));
    let u0f: f64 = u0.to_f64();
    // Gaussian saddle width: -f'' ~ 2k/u0^2  =>  sigma = u0/sqrt(2k).
    // Window scaled to the saddle concentrates the quadrature where the
    // integrand lives; resolution IMPROVES as k grows (fixed panel count,
    // shrinking panel width) instead of degrading like the fixed [u0/2,3u0/2]
    // window did (peak spanned only ~2 nodes at k=5e4).
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
    // log gamma(M) = log(8 M! b_M)
    let l8 = zf(PG, 8.0).ln();
    let lf = logfact(m, PG);
    let lb = logb_saddle(m as f64, gl, PG);
    let s1 = Float::with_val(PG, &l8 + &lf);
    Float::with_val(PG, &s1 + &lb)
}

// fit cubic at 210-bit precision: L_j = log gamma(M-j)/gamma(M) = -a1 j - a2 j^2 - a3 j^3, j=1..4
// (the f64 version lost a3 ~ G3*D^4 ~ 6e-11 in the rounding of log gamma ~ 3.6e5:
//  f64 abs error there is ~4e-11, exactly the observed noise floor)
fn fit_cubic(lg: &[Float]) -> (Float, Float, Float, Float) {
    let z = zf(PG, 0.0);
    let l = |j: usize| -> Float { Float::with_val(PG, &lg[j] - &lg[0]) };
    let l1 = l(1);
    let l2 = l(2);
    let l3 = l(3);
    let l4 = l(4);
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
    let ngl = std::env::args()
        .nth(1)
        .and_then(|s| s.parse().ok())
        .unwrap_or(64usize);
    let gl_s = gl_nodes(PG, ngl);
    // ---- 1. cross-validate saddle log b_k vs certified table at k=100..299 ----
    let txt = fs::read_to_string(
        "/home/vstaln/riemann/research/notes/g02-moments-oracle-2026-08-18.txt",
    )
    .expect("read table");
    let mut b: Vec<Float> = Vec::new();
    for line in txt.lines() {
        let line = line.trim();
        if line.is_empty() || line.starts_with('#') || line.starts_with("g0-2") {
            continue;
        }
        let cols: Vec<&str> = line.split('\t').collect();
        if cols.len() >= 3 {
            if let Ok(v) = Float::parse_radix(cols[2].trim(), 10) {
                b.push(Float::with_val(PG, v));
            }
        }
    }
    println!("cross-validating saddle log b_k vs certified table (k = 100..299):");
    let mut worst = 0.0f64;
    for k in (100..=299).step_by(40) {
        let lb_cert = b[k].clone().ln();
        let lb_sad = logb_saddle(k as f64, &gl_s, PG);
        let diff = (lb_sad - &lb_cert).to_f64().abs();
        worst = worst.max(diff);
        println!("  k={:3}  |saddle - cert| = {:.3e}", k, diff);
    }
    println!("  worst |diff| = {:.2e}  (saddle quadrature trusted if ~1e-20 or better)", worst);
    println!();

    // ---- 2. G2, G3 at large M via saddle log gamma ----
    println!("G2 -> 1, G3 -> 2/3 at large M (saddle-quadrature log gamma):");
    println!("{:>10} | {:>10} {:>12} {:>12} {:>12} {:>10}", "M", "Delta", "G2", "G3", "G3-2/3", "fit res");
    for &m in &[300usize, 400, 500, 800, 1000, 2000, 5000, 10000, 20000, 50000, 100000] {
        let mut lg = vec![zf(PG, 0.0); 5];
        for j in 0..5 {
            lg[j] = log_gamma_saddle(m - j, &gl_s);
        }
        // Delta^2 = 1/2 (1 - gamma(M-2)gamma(M)/gamma(M-1)^2) from logs:
        // log[..] = lg[2] + lg[0] - 2 lg[1]   (lg[j] = log gamma(M-j))
        let t1 = Float::with_val(PG, &lg[2] + &lg[0]);
        let t2 = Float::with_val(PG, zf(PG, 2.0) * &lg[1]);
        let x = Float::with_val(PG, &t1 - &t2);
        let d2 = Float::with_val(PG, 0.5 * (zf(PG, 1.0) - x.exp()));
        let (_, a2, a3, res) = fit_cubic(&lg);
        let g2 = Float::with_val(PG, &a2 / &d2);
        let d22 = Float::with_val(PG, &d2 * &d2);
        let g3 = Float::with_val(PG, &a3 / &d22);
        let d2f = d2.to_f64().sqrt();
        let g2f = g2.to_f64();
        let g3f = g3.to_f64();
        let resf = res.to_f64();
        println!(
            "{:10} | {:10.5} {:12.6} {:12.6} {:12.3e} {:10.1e}",
            m,
            d2f,
            g2f,
            g3f,
            g3f - 2.0 / 3.0,
            resf
        );
    }
    println!(
        "\n(If G3 -> 2/3, this confirms GORTTW Thm 2.1(2)'s limit prediction at M beyond the\n certified table — a second-order asymptotic check on the full saddle structure.\n Caveat: this uses the oracle's own saddle quadrature of M_k, not a theorem; the\n cross-validation above quantifies its accuracy at k <= 299.)"
    );
}
