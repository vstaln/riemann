// refereeB probe: (3a) minilp-infeasibility mechanism, (3b) floor monotonicity, (1b) p1-vs-P(m=1).
// Self-contained re-derivation of sinc_m3_cert math; verified output in refereeB note.
use std::f64::consts::PI;
const N: usize = 256;
const B: usize = 128;
const EPS: f64 = 0.44;
fn sinc(x: f64) -> f64 { if x.abs() < 1e-12 { 1.0 } else { x.sin() / x } }
fn khat_spectrum() -> Vec<f64> {
    let mut kh = vec![0.0f64; N];
    for m in 0..N { let mut s = 0.0;
        for i in 0..N { let x = i as f64 / N as f64;
            s += sinc(PI * B as f64 * x).powi(2) * (2.0 * PI * m as f64 * x).cos(); }
        kh[m] = s / N as f64; }
    kh
}
fn conv_circ(kh: &[f64]) -> Vec<f64> {
    let mut kk = vec![0.0f64; N];
    for k in 0..N { for m in 0..N { let j = (k + N - m) % N; kk[k] += kh[m] * kh[j]; } }
    kk
}
fn moments(p1: f64) -> (f64, f64, f64) {
    (2.0 / (1.0 + p1), (4.0 - 2.0 * p1) / (1.0 + p1), (8.0 - 6.0 * p1) / (1.0 + p1))
}
fn mu0sq(em: f64, em2: f64) -> f64 { em2 / N as f64 + (N as f64 - 1.0) / N as f64 * em * em }
fn m2(p1: f64, kk: &[f64], c: f64) -> f64 {
    let (em, em2, _) = moments(p1);
    let mut s = kk[0] * mu0sq(em, em2);
    for k in 1..N { s += kk[k] * (c * k as f64); }
    (N as f64 / em) * s
}
fn p3(p1: f64, kk: &[f64], c: f64) -> f64 {
    let (em, em2, em3) = moments(p1);
    let mut s = 0.0;
    for k in 0..N {
        let e = if k == 0 { em3 / N as f64 + (N as f64 - 1.0) / N as f64 * em2 * em }
            else { em3 / N as f64 + em2 * c * k as f64 / em - em2 * em2 / (N as f64 * em) };
        s += kk[k] * ((N as f64 * N as f64) * e - (N as f64) * em3);
    }
    3.0 * s / (N as f64 * em)
}
fn floor_s3(p1: f64, kk: &[f64], c: f64) -> f64 {
    let (em, _, em3) = moments(p1);
    (em3 / em + p3(p1, kk, c)).max(m2(p1, kk, c).powi(2))
}
fn main() {
    let kk = conv_circ(&khat_spectrum());
    let mut c = 0.01f64;
    for _ in 0..60 { c *= 2.22 / m2(1.0, &kk, c); }
    println!("c = {:.8}, m2(1) = {:.6}", c, m2(1.0, &kk, c));
    // (3b) floor monotonicity on 0.005 grid; branch D+P3(1)/m2^2(2)
    let mut prev = f64::NAN; let mut pb = 0; let mut nonmono = 0usize;
    let mut p = 0.0f64;
    while p <= 1.0001 {
        let (em, _, em3) = moments(p);
        let dp = em3 / em + p3(p, &kk, c);
        let ms = m2(p, &kk, c).powi(2);
        let fl = dp.max(ms);
        let b = if dp >= ms { 1 } else { 2 };
        if p > 0.0 && fl > prev + 1e-9 { nonmono += 1; }
        if pb == 1 && b == 2 { println!("branch switch 1->2 at p1~{:.3}", p); }
        prev = fl; pb = b; p += 0.005;
    }
    println!("non-monotone steps on grid: {} (tail only: m2^2 up 4.9260->4.9284 near p1=1)", nonmono);
    let f = |p: f64| floor_s3(p, &kk, c) - (5.0 + EPS);
    let (mut lo, mut hi_) = (0.0f64, 1.0f64);
    for _ in 0..80 { let mid = 0.5 * (lo + hi_); if f(mid) <= 0.0 { hi_ = mid; } else { lo = mid; } }
    let p1s = 0.5 * (lo + hi_);
    println!("p1s = {:.8}, floor = {:.8}", p1s, floor_s3(p1s, &kk, c));
    let h = 1e-4;
    let fdp = |p: f64| { let (_, _, em3) = moments(p); em3 / (2.0 / (1.0 + p)) + p3(p, &kk, c) };
    let d1 = (fdp(p1s + h) - fdp(p1s - h)) / (2.0 * h);
    let d2 = (m2(p1s + h, &kk, c).powi(2) - m2(p1s - h, &kk, c).powi(2)) / (2.0 * h);
    let (m0, f0) = (m2(p1s, &kk, c).powi(2), fdp(p1s));
    println!("d(D+P3)/dp1 = {:.4}, d(m2^2)/dp1 = {:.4}, gap m2^2-(D+P3) = {:.4}", d1, d2, m0 - f0);
    let (a1, a2, a3) = (5.0 - EPS - (f0 - d1 * p1s), 5.0 + EPS - (f0 - d1 * p1s),
        (m0 - f0) - (d2 - d1) * p1s);
    let mut feas = false; let mut q = 0.0f64;
    while q <= 1.0001 {
        let lo_t = ((a1 - d1 * q).max((d2 - d1) * q - a3)).max(0.0);
        if lo_t <= a2 - d1 * q + 1e-9 { feas = true; }
        q += 0.001;
    }
    println!("linearized LP feasible on p1 in [0,1]? {} (binary: Infeasible)", feas);
    for p1 in [0.6818287f64, 0.7488] {
        println!("p1 = {:.7} -> P(m=1) = {:.7}, P(m=2) = {:.7}, E[m] = {:.7}",
            p1, 2.0 * p1 / (1.0 + p1), (1.0 - p1) / (1.0 + p1), 2.0 / (1.0 + p1));
    }
}
