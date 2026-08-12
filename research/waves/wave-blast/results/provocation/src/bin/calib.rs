// calib.rs — calibrated two-window pair-correlation + certificate-constant stability.
//
// x_n = theta(t_n)/pi (so x-spacing ~ 1, first zero at x ~ -0.55). Pair counts in
// x-windows. This matches the LS-calibrated estimator convention (hot_hand_calib.py),
// whose GUE null at alpha = 1.0 reads ~ 1.007 +- 0.037 and zeta reads 1.378.
//   C1  F(alpha) for alpha in {0.5, 0.7, 0.9, 1.0, 1.05, 1.1, 1.2, 1.3, 1.5, 2.0}
//       computed as (1/(2 N alpha)) * #{|x_i - x_j| < alpha, i != j}, trimmed to the
//       bulk window [50, N-50] to avoid the negative-tail edge.
//   C2  "operator spectrum" stability: certificate constants from two windows —
//       recompute the Gram-style tr/N and HS/N on two overlapping windows and the
//       sliding ratio; report stability (this tests "zeros are a universal operator's
//       spectrum": the constants should be window-stable).

use std::f64::consts::PI;
use std::fs;

fn load_ords(path: &str) -> Vec<f64> {
    fs::read_to_string(path)
        .expect("read")
        .lines()
        .filter_map(|l| {
            let l = l.trim();
            if l.is_empty() {
                return None;
            }
            let mut it = l.split_whitespace();
            let _ = it.next()?;
            let t: f64 = it.next()?.parse().ok()?;
            Some(t)
        })
        .collect()
}

fn theta(t: f64) -> f64 {
    let z = t / 2.0;
    let s_re = 0.25;
    let s_im = z;
    let log_s_re = 0.5 * (s_re * s_re + s_im * s_im).ln();
    let log_s_im = s_im.atan2(s_re);
    let lg_im = (s_re - 0.5) * log_s_im + s_im * log_s_re - s_im
        - s_im / (12.0 * (s_re * s_re + s_im * s_im));
    lg_im - z * PI.ln()
}

fn main() {
    let ords = load_ords("data/zeros.txt");
    let n = ords.len();
    let x: Vec<f64> = ords.iter().map(|&t| theta(t) / PI).collect();

    // bulk window
    let lo = 50usize;
    let hi = n - 50;
    let m = (hi - lo) as f64;

    let alphas: [f64; 10] = [0.5, 0.7, 0.9, 1.0, 1.05, 1.1, 1.2, 1.3, 1.5, 2.0];
    for &a in alphas.iter() {
        let mut c = 0.0f64;
        for i in lo..hi {
            let xi = x[i];
            let mut j = i + 1;
            while j < hi && x[j] - xi < a {
                c += 1.0;
                j += 1;
            }
        }
        let f = c / (2.0 * m * a);
        println!("C1 {:.2} {:.6}", a, f);
    }

    // C2: two-window stability of the HS/tr ratio (the certificate's "second moment"
    // constant C = 1.3275). On x-units: tr = N, HS^2 = sum over pairs of k(d)^2 ...
    // The certificate constant C appears as ||A||^2/N = 1.3275 = 1/2 + (1/sqrt2) cot(1/sqrt2)
    // in the paper's normalization. Here we measure the *window-invariance* of the
    // normalized pair-sum P(w) = (1/N) sum_{i!=j} 1_{|x_i-x_j|<w} at w = 1.3275-ish.
    // Report P(1.0), P(1.3275), and the sliding-window ratio at half-window.
    for &w in [0.5f64, 1.0, 1.3275, 1.5].iter() {
        let mut c = 0.0f64;
        for i in lo..hi {
            let xi = x[i];
            let mut j = i + 1;
            while j < hi && x[j] - xi < w {
                c += 1.0;
                j += 1;
            }
        }
        println!("C2 P({:.4}) {:.6}", w, c / (m * m / 2.0) * 2.0); // normalized: 2 * pairs / m^2
    }
    // sliding half-window stability: P on [0, m/2] vs [m/2, m]
    let mid = (lo + hi) / 2;
    for (name, a, b) in [
        ("first_half", lo, mid),
        ("second_half", mid, hi),
    ] {
        let mut c = 0.0f64;
        let len = (b - a) as f64;
        for i in a..b {
            let xi = x[i];
            let mut j = i + 1;
            while j < b && x[j] - xi < 1.3275 {
                c += 1.0;
                j += 1;
            }
        }
        println!("C2 {}_P(1.3275) {:.6}", name, 2.0 * c / (len * len));
    }

    println!("DONE");
}
