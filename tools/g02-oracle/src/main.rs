// g0-2 certified-moment oracle for Xi Taylor coefficients.
//   M_k = 2 int_0^inf Phi(u) u^{2k} du ;  b_k = M_k/(2k)! ;  gamma(k) = k! b_k
//   Phi(u) = 2 sum_{n>=1} (2 pi^2 n^4 e^{9u/2} - 3 pi n^2 e^{5u/2}) e^{-pi n^2 e^{2u}}
// Also: theta-derivative identity  Phi(u) = 2 e^{u/2}(2x^2 th''(x)+3x th'(x)), x=e^{2u}.
// Also: S1-saddle deficit: t_k = 1 - b_{k-1}b_{k+1}/b_k^2, D(k)=(2-k*t_k)*log k,
//       extended to large k via saddle quadrature of log M_k.
use rug::float::Constant;
use rug::ops::Pow;
use rug::Float;
use std::io::Write;

const PG: u32 = 210; // working precision (~63 digits)
const NSUM: usize = 14;
const UMAX: f64 = 4.0;
const NPAN: usize = 40;
const NGL: usize = 48;
const KMAX: usize = 300;

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
    for n in 1..=NSUM {
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
fn phi_theta(u: &Float, prec: u32) -> Float {
    let pi = Float::with_val(prec, Constant::Pi);
    let x = Float::with_val(prec, zf(prec, 2.0) * u).exp();
    let x2 = Float::with_val(prec, &x * &x);
    let mut thp = zf(prec, 0.0);
    let mut thpp = zf(prec, 0.0);
    let pi2 = Float::with_val(prec, &pi * &pi);
    let npi = Float::with_val(prec, -&pi);
    let two_x2 = Float::with_val(prec, zf(prec, 2.0) * &x2);
    let three_x = Float::with_val(prec, zf(prec, 3.0) * &x);
    for n in 1..=NSUM {
        let n2 = zf(prec, (n * n) as f64);
        let a1 = Float::with_val(prec, &npi * &n2);
        let a2 = Float::with_val(prec, &a1 * &x);
        let e = a2.exp();
        let ta = Float::with_val(prec, &pi * &n2);
        let t = Float::with_val(prec, &ta * &e);
        thp = Float::with_val(prec, &thp - &t);
        let n2sq = Float::with_val(prec, &n2 * &n2);
        let t2a = Float::with_val(prec, &pi2 * &n2sq);
        let t2 = Float::with_val(prec, &t2a * &e);
        thpp = Float::with_val(prec, &thpp + &t2);
    }
    let a = Float::with_val(prec, &two_x2 * &thpp);
    let b = Float::with_val(prec, &three_x * &thp);
    let inner = Float::with_val(prec, &a + &b);
    let eu = Float::with_val(prec, u / zf(prec, 2.0)).exp();
    Float::with_val(prec, zf(prec, 2.0) * &eu * &inner)
}

fn moment(k: usize, gl: &[(Float, Float)], prec: u32) -> Float {
    let mut s = zf(prec, 0.0);
    for p in 0..NPAN {
        let a = Float::with_val(prec, 4.0 * p as f64) / zf(prec, 40.0);
        let b = Float::with_val(prec, 4.0 * (p + 1) as f64) / zf(prec, 40.0);
        let ab = Float::with_val(prec, &a + &b);
        let ba = Float::with_val(prec, &b - &a);
        let mid = Float::with_val(prec, &ab / zf(prec, 2.0));
        let half = Float::with_val(prec, &ba / zf(prec, 2.0));
        for (x, w) in gl {
            let hx = Float::with_val(prec, &half * x);
            let u = Float::with_val(prec, &mid + &hx);
            let f = phi(&u, prec);
            let uk = Float::with_val(prec, u.pow(2 * k as u32));
            let wf = Float::with_val(prec, w * &f);
            s += Float::with_val(prec, &wf * &uk);
        }
    }
    Float::with_val(prec, &s * zf(prec, 4.0) / zf(prec, 40.0)) // M_k = h*s
}
fn gamma_k(k: usize, mk: &Float, prec: u32) -> Float {
    let mut d = zf(prec, 1.0);
    for j in (k + 1)..=(2 * k) { d *= zf(prec, j as f64); }
    Float::with_val(prec, mk / &d)
}
fn b_k(k: usize, mk: &Float, prec: u32) -> Float {
    let mut d = zf(prec, 1.0);
    for j in 2..=(2 * k) { d *= zf(prec, j as f64); }
    Float::with_val(prec, mk / &d)
}
fn logfact(n: usize, prec: u32) -> Float {
    let mut s = zf(prec, 0.0);
    for j in 2..=n { s += zf(prec, j as f64).ln(); }
    s
}
fn logb_saddle(k: f64, gl: &[(Float, Float)], prec: u32) -> Float {
    // log b_k = log M_k - log((2k)!) ; M_k = 2 int Phi(u) u^{2k} du via saddle GL.
    let pi = Float::with_val(prec, Constant::Pi);
    let lnk = zf(prec, k).ln();
    let lnlnk = Float::with_val(prec, &lnk).ln();
    let c = Float::with_val(prec, zf(prec, 2.0) / &pi).ln();
    let d1 = Float::with_val(prec, &lnk - &lnlnk);
    let d2 = Float::with_val(prec, &d1 + c);
    let u0 = Float::with_val(prec, &d2 / zf(prec, 2.0));
    let u0f: f64 = u0.to_f64();
    let half = u0f * 0.5;
    let lo = u0f - half;
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
fn t_from_logb(lprev: &Float, lk: &Float, lnext: &Float, prec: u32) -> Float {
    let two_lk = Float::with_val(prec, zf(prec, 2.0) * lk);
    let s1 = Float::with_val(prec, lprev + lnext);
    let ex = Float::with_val(prec, &s1 - &two_lk);
    Float::with_val(prec, zf(prec, 1.0) - ex.exp())
}

fn main() {
    let t0 = std::time::Instant::now();
    let gl = gl_nodes(PG, NGL);
    println!("Phi(0) = {:.8} (anchor 0.8933938)", phi0());
    let gl_s = gl_nodes(PG, 64);

    let mut out = String::new();
    out.push_str(&format!("# g0-2 moment oracle. k, M_k, b_k, gamma(k) ~{} bits\n", PG));
    let mut gammas: Vec<Float> = Vec::new();
    let mut bs: Vec<Float> = Vec::new();
    for k in 0..=KMAX {
        let mk = moment(k, &gl, PG);
        let g = gamma_k(k, &mk, PG);
        let b = b_k(k, &mk, PG);
        gammas.push(g.clone());
        bs.push(b.clone());
        out.push_str(&format!("{}\t{}\t{}\t{}\n", k, mk, b, g));
    }
    let _ = std::fs::write("research/notes/g02-moments-oracle-2026-08-18.txt", &out);
    println!("[t={:?}] moments 0..{} computed", t0.elapsed(), KMAX);

    let table: [&str; 9] = [
        "0.4971207781883141", "0.0114859721575727188", "0.000246904036140636",
        "4.99413288831316e-6", "9.58134372322593e-8", "1.75392309121332e-9",
        "3.07766883278653e-11", "5.19605157184748e-13", "8.46627186645890e-15",
    ];
    println!("validation gamma(0..8) vs 60-digit table:");
    for i in 0..9 {
        let got = gammas[i].clone();
        let expct: f64 = table[i].parse().unwrap();
        let rel = ((got.to_f64() - expct) / expct).abs();
        println!("  gamma({})={}  relerr={:.2e}", i, got, rel);
    }

    println!("theta identity  Phi_direct vs 2e^{{u/2}}(2x^2 th''+3x th'):");
    for u in [0.0f64, 0.5, 1.0, 2.0] {
        let uu = zf(PG, u);
        let a = phi(&uu, PG);
        let b = phi_theta(&uu, PG);
        let diff = Float::with_val(PG, &a - &b).abs().to_f64();
        println!("  u={}: |diff|={:.3e}  phi={:.20}", u, diff, a);
    }

    println!("deficit from ORACLE (exact moments):");
    for &k in &[1usize, 2, 5, 10, 30, 50, 100, 150, 200, 250, 290, 299] {
        if k + 1 > KMAX { continue; }
        let lp = Float::with_val(PG, &bs[k - 1]).ln();
        let lk = Float::with_val(PG, &bs[k]).ln();
        let ln = Float::with_val(PG, &bs[k + 1]).ln();
        let t = t_from_logb(&lp, &lk, &ln, PG);
        let kt = Float::with_val(PG, zf(PG, k as f64) * &t);
        let d = Float::with_val(PG, (zf(PG, 2.0) - &kt) * zf(PG, k as f64).ln());
        println!("  k={}: k*t_k={:.9}  (2-kt)*lnk={:.6}", k, kt, d);
    }

    println!("deficit from SADDLE (large k):");
    for &k in &[1_000.0f64, 10_000.0, 100_000.0, 1_000_000.0] {
        let lprev = logb_saddle(k - 1.0, &gl_s, PG);
        let lk = logb_saddle(k, &gl_s, PG);
        let lnext = logb_saddle(k + 1.0, &gl_s, PG);
        let t = t_from_logb(&lprev, &lk, &lnext, PG);
        let kt = Float::with_val(PG, zf(PG, k) * &t);
        let d = Float::with_val(PG, (zf(PG, 2.0) - &kt) * zf(PG, k).ln());
        println!("  k={}: k*t_k={:.9}  (2-kt)*lnk={:.6}  logb_k={:.9}", k, kt, d, lk);
    }
    println!("[t={:?}] done", t0.elapsed());
}

fn phi0() -> f64 {
    let p = 210u32;
    let pi = Float::with_val(p, Constant::Pi);
    let two = zf(p, 2.0);
    let pi2 = Float::with_val(p, &pi * &pi);
    let npi = Float::with_val(p, -&pi);
    let c2pi2 = Float::with_val(p, &two * &pi2);
    let c3pi = Float::with_val(p, zf(p, 3.0) * &pi);
    let mut s = zf(p, 0.0);
    for n in 1..=NSUM {
        let n2 = zf(p, (n * n) as f64);
        let n4 = Float::with_val(p, &n2 * &n2);
        let a1 = Float::with_val(p, &npi * &n2);
        let e = a1.exp();
        let c1 = Float::with_val(p, &c2pi2 * &n4);
        let c2 = Float::with_val(p, &c3pi * &n2);
        let d = Float::with_val(p, &c1 - &c2);
        s += Float::with_val(p, &d * &e);
    }
    Float::with_val(p, &s * &two).to_f64()
}
