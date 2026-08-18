// Full GORZ root-distribution check on certified coefficients.
//
// GORZ Theorem 3: if log(gamma(n+j)/gamma(n)) = A(n)*j - delta(n)^2*j^2 + o(delta(n)^d)
// then the normalized Jensen polynomial
//   Jhat^{d,n}(X) = J^{d,n}((delta*X - 1)/exp(A)) / (delta^d * gamma(n))
// converges to the Hermite polynomial H_d(X), with generating function
//   sum_d H_d(X) w^d/d! = exp(-w^2 + Xw)   (roots of H_2: +-sqrt(2), H_3: 0, +-sqrt(6), H_4: +-(3+-sqrt(6))... )
//
// We extract A(n), delta(n) from certified data:
//   R1 = log(gamma(n+1)/gamma(n)), R2 = log(gamma(n+2)/gamma(n+1))
//   delta^2 = (R1 - R2)/2,  A = R1 + delta^2
// then normalize the measured roots x_k of J^{d,n} (found from the ratio polynomial)
//   X_k = (1 + exp(A)*x_k)/delta
// and compare to the exact roots of H_d.  Deviation -> 0 as n -> oo is the full
// first-order GORZ asymptotics on certified coefficients.

use rug::Float;
use std::fs;

const PREC: u32 = 210;

fn main() {
    let txt = fs::read_to_string(
        "/home/vstaln/riemann/research/notes/g02-moments-oracle-2026-08-18.txt",
    )
    .expect("read table");
    // tab-separated: k, M_k, b_k, gamma(k)
    let mut b: Vec<Float> = Vec::new();
    for line in txt.lines() {
        let line = line.trim();
        if line.is_empty() || line.starts_with('#') || line.starts_with("g0-2") {
            continue;
        }
        let cols: Vec<&str> = line.split('\t').collect();
        if cols.len() >= 3 {
            if let Ok(v) = Float::parse_radix(cols[2].trim(), 10) {
                b.push(Float::with_val(PREC, v));
            }
        }
    }
    let nk = b.len();
    println!("loaded b_k k=0..{}", nk - 1);

    // Hermite H_d roots (generating fn exp(-w^2 + Xw)).
    // H_2 = X^2 - 2          roots +-sqrt(2)
    // H_3 = X^3 - 6X         roots 0, +-sqrt(6)
    // H_4 = X^4 - 12X^2 + 12 roots +-(3+-sqrt(6))^...  (4 real roots: +-a, +-b, a^2+b^2=12, ab=2sqrt(3))
    // Exact roots computed below numerically via root-finding on H_d directly.
    let hermite = |d: usize, x: f64| -> f64 {
        // H_d via recurrence for generating fn exp(-w^2+Xw):
        // H_{k+1} = X*H_k - 2k*H_{k-1}  (gives H_2 = X^2-2, H_3 = X^3-6X — checked below).
        let mut h0 = 1.0f64;
        let mut h1 = x;
        for k in 1..d {
            let h2 = x * h1 - 2.0 * (k as f64) * h0;
            h0 = h1;
            h1 = h2;
        }
        if d == 0 {
            1.0
        } else {
            h1
        }
    };
    // Sanity: H_2 = x^2 - 2?
    {
        let c2 = hermite(2, 1.0);
        let c3 = hermite(3, 1.0);
        println!(
            "[sanity] H_2(1)={:.6} (want -1), H_3(1)={:.6} (want -5)",
            c2, c3
        );
    }
    // roots of H_d by scanning
    let hroots = |d: usize| -> Vec<f64> {
        let mut roots = Vec::new();
        let step = 0.001;
        let mut x = -10.0;
        let mut prev = hermite(d, x);
        while x < 10.0 {
            let nx = x + step;
            let nv = hermite(d, nx);
            if prev * nv <= 0.0 {
                // bisect
                let (mut lo, mut hi) = (x, nx);
                for _ in 0..60 {
                    let mid = 0.5 * (lo + hi);
                    let mv = hermite(d, mid);
                    if mv * hermite(d, lo) <= 0.0 {
                        hi = mid;
                    } else {
                        lo = mid;
                    }
                }
                roots.push(0.5 * (lo + hi));
            }
            prev = nv;
            x = nx;
        }
        roots
    };

    // gamma(n) = 8 * n! * b_n. Compute the log directly to avoid huge intermediates:
    // log gamma(n) = ln(8) + sum_{i=1..n} ln(i) + ln b_n, then ratio logs are differences.
    // Precompute log-factorials in f64 (ln(300!) ~ 1500, no overflow) and log b_n at 210 bits.
    let mut lnfact = vec![0.0f64; 301];
    for i in 2..=300 {
        lnfact[i] = lnfact[i - 1] + (i as f64).ln();
    }
    let ln8 = (8.0f64).ln();
    let ln_b = |n: usize| -> f64 { b[n].clone().ln().to_f64() };
    let log_gamma = |n: usize| -> f64 { ln8 + lnfact[n] + ln_b(n) };
    let ratio_log = |n: usize, j: usize| -> f64 { log_gamma(n + j) - log_gamma(n) };

    for &n in &[10usize, 20, 40, 60, 100, 150, 200, 250] {
        let r1 = ratio_log(n, 1);
        let r2 = ratio_log(n, 2);
        // r1 = log(g(n+1)/g(n)) = A - d^2 (j=1), r2 = log(g(n+2)/g(n)) = 2A - 4d^2 (j=2)
        // => d^2 = r1 - r2/2, A = r1 + d^2
        let delta2 = r1 - r2 / 2.0;
        let delta = delta2.max(0.0).sqrt();
        let a = r1 + delta2;
        let eA = a.exp();
        print!(
            "n={:3} A={:10.5} delta={:10.6} eA={:10.3} |",
            n, a, delta, eA
        );
        // ratio polynomial coefficients c_j = C(d,j) * gamma(n+j)/gamma(n)  (roots unchanged by scale)
        for &d in &[2usize, 3, 4] {
            let mut coef: Vec<f64> = Vec::new();
            for j in 0..=d {
                // C(d,j) * gamma(n+j)/gamma(n)
                let mut comb = 1.0f64;
                for i in 1..=j {
                    comb *= (d - i + 1) as f64 / i as f64;
                }
                let r = ratio_log(n, j).exp();
                coef.push(comb * r);
            }
            // find roots of sum coef[j] X^j  (sign convention: constant term c0, so roots near -eA)
            let poly = |x: f64| -> f64 {
                let mut s = 0.0;
                let mut p = 1.0;
                for j in 0..=d {
                    s += coef[j] * p;
                    p *= x;
                }
                s
            };
            let mut roots: Vec<f64> = Vec::new();
            // roots cluster at -exp(-A); spread ~ exp(-A)*delta*H_d-root-diameter
            let center = -(-a).exp();
            let half = (-a).exp() * delta * 30.0 + 1.0;
            let step = (2.0 * half) / 200000.0;
            let (x0, x1) = (center - half, center + half);
            let mut prev = poly(x0);
            let mut x = x0;
            while x < x1 {
                let nx = x + step;
                let nv = poly(nx);
                if prev * nv <= 0.0 {
                    let (mut lo, mut hi) = (x, nx);
                    for _ in 0..60 {
                        let mid = 0.5 * (lo + hi);
                        let mv = poly(mid);
                        if mv * poly(lo) <= 0.0 {
                            hi = mid;
                        } else {
                            lo = mid;
                        }
                    }
                    roots.push(0.5 * (lo + hi));
                }
                prev = nv;
                x = nx;
            }
            roots.sort_by(|a, b| a.partial_cmp(b).unwrap());
            let hr = hroots(d);
            if roots.len() != hr.len() {
                print!(" d={} nroots={}!= {} SKIP |", d, roots.len(), hr.len());
                continue;
            }
            // normalize each root (sort both ascending): X_k = (1 + eA*x_k)/delta
            let mut maxdev = 0.0f64;
            for k in 0..roots.len() {
                let xk = (1.0 + eA * roots[k]) / delta;
                let dev = (xk - hr[k]).abs();
                if dev > maxdev {
                    maxdev = dev;
                }
            }
            print!(" d={} maxdev={:8.5} |", d, maxdev);
        }
        println!();
    }
    println!(
        "\n(GORZ full-content check: normalized roots X_k=(1+e^A x)/delta vs exact H_d roots.\n maxdev -> 0 as n -> oo confirms the complete first-order asymptotics on certified coefficients.)"
    );
}
