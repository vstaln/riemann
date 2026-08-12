// rust-zeros v3 — HYBRID zero-finder, pure-std Rust, f64.
// Spec: task-rust-zeros-v3.md (FIXED design; no coefficient archaeology).
//   t <  200: Euler–Maclaurin zeta(1/2+it), N=40, hardcoded-via-recurrence B_2..B_40.
//   t >= 200: Riemann–Siegel g0-only.
// Z(t) = Re(e^{i theta(t)} zeta(1/2+it)); zeros of Z = zeros of zeta on the critical line.
// Scan step 0.2 from t=14, bisection x80; completeness vs N(T).
//
// Usage: zeros <count> [T_max_override]  > zeros_N.txt
// Every zero is flushed to stdout as found (crash-proof).
use std::env;
use std::io::{self, Write};

const PI: f64 = std::f64::consts::PI;
const TWO_PI: f64 = 2.0 * PI;

// --- theta(t) asymptotic (valid t>=14, error < 1e-9; t>=200 error < 1e-13) ---
fn theta(t: f64) -> f64 {
    let u = t / TWO_PI;
    let t3 = t * t * t;
    (t / 2.0) * u.ln() - t / 2.0 - PI / 8.0 + 1.0 / (48.0 * t) + 7.0 / (5760.0 * t3)
}

// Bernoulli numbers by recurrence: B_0 = 1, sum_{k=0}^{n} C(n+1,k) B_k = 0.
fn bernoulli(n: usize) -> f64 {
    let mut b = vec![0.0f64; n + 1];
    b[0] = 1.0;
    for m in 1..=n {
        let mut s = 0.0;
        let mut c: f64 = 1.0; // C(m+1, k)
        for k in 0..m {
            s += c * b[k];
            c *= (m + 1 - k) as f64 / (k + 1) as f64;
        }
        b[m] = -s / (m + 1) as f64;
    }
    b[n]
}

// --- Euler–Maclaurin zeta(1/2 + i t), N=40 terms, k=1..20 Bernoulli tail ---
fn zeta_half_it(t: f64) -> (f64, f64) {
    const N: usize = 40;
    const K: usize = 20;
    let lnN = (N as f64).ln();
    let (mut re, mut im) = (0.0f64, 0.0f64);

    // sum_{n=1}^{N-1} n^{-s}
    for n in 1..N {
        let nf = n as f64;
        let ang = -t * nf.ln();
        let mag = 1.0 / nf.sqrt();
        re += mag * ang.cos();
        im += mag * ang.sin();
    }
    // N^{1-s} / (s-1);  s = 0.5 + i t,  s-1 = -0.5 + i t
    let a = (N as f64).sqrt() * (t * lnN).cos();
    let b = -(N as f64).sqrt() * (t * lnN).sin(); // N^{0.5} e^{-i t lnN}
    let denom = 0.25 + t * t;
    re += (-0.5 * a + t * b) / denom;
    im += (-0.5 * b - t * a) / denom;
    // N^{-s}/2
    let c = (N as f64).powf(-0.5) * (t * lnN).cos() / 2.0;
    let d = -(N as f64).powf(-0.5) * (t * lnN).sin() / 2.0;
    re += c;
    im += d;
    // sum_{k=1}^{20} B_{2k}/(2k)! (s)_{2k-1} N^{-s-2k+1}
    for k in 1..=K {
        // (s)_{2k-1} = prod_{j=0}^{2k-2} (0.5 + j + i t)
        let mut pr = 1.0f64;
        let mut pi = 0.0f64;
        for j in 0..(2 * k - 1) {
            let xr = 0.5 + j as f64;
            let nr = pr * xr - pi * t;
            let ni = pr * t + pi * xr;
            pr = nr;
            pi = ni;
        }
        let bterm = bernoulli(2 * k);
        let fact = (2 * k) as f64;
        // (2k)! via loop
        let mut f = 1.0f64;
        for m in 2..=(2 * k) {
            f *= m as f64;
        }
        let coef = bterm / f * (N as f64).powf(-(2.0 * k as f64) + 0.5);
        let e = (t * lnN).cos();
        let f2 = -(t * lnN).sin(); // e^{-i t lnN}
        // term = coef * (pr + i pi) * (e + i f2)
        let tr = pr * e - pi * f2;
        let ti = pr * f2 + pi * e;
        re += coef * tr;
        im += coef * ti;
    }
    (re, im)
}

fn z_low(t: f64) -> f64 {
    let (re, im) = zeta_half_it(t);
    let th = theta(t);
    // Z = Re(e^{i th} zeta) = re*cos(th) - im*sin(th)
    re * th.cos() - im * th.sin()
}

// --- Riemann–Siegel g0-only (t >= 200) ---
fn z_high(t: f64) -> f64 {
    let x = t / TWO_PI;
    let sq = x.sqrt();
    let n = sq.floor() as usize;
    let a = sq - n as f64;
    let th = theta(t);
    let mut s = 0.0f64;
    for k in 1..=n {
        s += (th - t * (k as f64).ln()).cos() / (k as f64).sqrt();
    }
    let sign = if n % 2 == 0 { -1.0 } else { 1.0 }; // (-1)^{n-1}
    let g0 = (TWO_PI * (a * a - a - 1.0 / 16.0)).cos() / (TWO_PI * a).cos();
    s = 2.0 * s + sign * x.powf(-0.25) * g0;
    s
}

fn z(t: f64) -> f64 {
    if t < 200.0 {
        z_low(t)
    } else {
        z_high(t)
    }
}

// N(T) = (T/2pi) ln(T/2pi) - T/2pi + 7/8
fn n_count(t: f64) -> f64 {
    let u = t / TWO_PI;
    u * u.ln() - u + 7.0 / 8.0
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let count: usize = args
        .get(1)
        .expect("usage: zeros <count> [T_max]")
        .parse()
        .expect("count");
    let t_max: f64 = args
        .get(2)
        .map(|s| s.parse().unwrap())
        .unwrap_or(if count > 0 { -1.0 } else { 0.0 });

    // sanity checks on Bernoulli
    assert!((bernoulli(2) - 1.0 / 6.0).abs() < 1e-15, "B2");
    assert!((bernoulli(4) + 1.0 / 30.0).abs() < 1e-14, "B4");
    assert!((bernoulli(6) - 1.0 / 42.0).abs() < 1e-14, "B6");

    let mut out = io::stdout().lock();
    let t0 = 14.0;
    let step = args.get(3).and_then(|s| s.parse().ok()).unwrap_or(0.2);
    let _ = writeln!(out, "# rust-zeros v3 hybrid: EM(t<200) + RS-g0(t>=200), step {step}, bisect x80");

    let mut zeros: Vec<f64> = Vec::with_capacity(count);
    let mut t = t0;
    let mut zprev = z(t0);
    let mut t_hi = t_max;
    let mut found = 0usize;

    while found < count {
        let t_next = t + step;
        if t_max > 0.0 && t_next > t_max {
            break;
        }
        let znext = z(t_next);
        if zprev.is_finite() && znext.is_finite() && zprev * znext < 0.0 {
            // bisection x80
            let (mut lo, mut hi) = (t, t_next);
            let mut zlo = zprev;
            for _ in 0..80 {
                let mid = 0.5 * (lo + hi);
                let zm = z(mid);
                if zlo * zm < 0.0 {
                    hi = mid;
                } else {
                    lo = mid;
                    zlo = zm;
                }
            }
            let g = 0.5 * (lo + hi);
            let _ = writeln!(out, "{} {:.12}", found + 1, g);
            let _ = out.flush();
            zeros.push(g);
            found += 1;
            if found >= count {
                t_hi = g;
                break;
            }
        }
        t = t_next;
        zprev = znext;
    }

    // completeness: N(T) at t_hi
    let nc = n_count(t_hi);
    let _ = writeln!(
        out,
        "# done: found={} t_last={:.3} N(T_last)={:.2} diff={:+.2} T_max_used={:.3}",
        found,
        t_hi,
        nc,
        found as f64 - nc,
        t_hi
    );
    let _ = out.flush();
    eprintln!("rust-zeros: found={} t_last={:.3} N(T)={:.2} diff={:+.2}", found, t_hi, nc, found as f64 - nc);
}
