// quad.rs — Provocation: "Po: ζ(s) is a polynomial".
// What if ζ were a polynomial of degree N? Then Z(t) would be a real trigonometric
// polynomial and its zeros on the line would be quasi-periodic (almost-equally spaced
// for large zeros). Serious kernel to extract: how far is the *zero sequence* from
// any degree-N quasi-polynomial? Test via the 2nd/3rd/4th finite differences of the
// normalized ordinates x_n = theta(gamma_n)/pi (mean spacing 1). A polynomial-like
// sequence of "degree d" has |Δ^d x| ~ O(1) growth with N; a random (GUE) sequence
// has |Δ^d x| ~ sqrt(N) growth (random-walk scaling of order d). We measure the
// growth exponent of |Δ^d x| over blocks. Also the "zeta is a polynomial" idea
// suggests: Z(t) ~ trig-poly of degree ~ sqrt(t/2pi) — i.e. the number of sign
// changes up to T should be ~ (1/pi) theta(T) ~ T log T/2pi — a restatement of the
// Riemann-von-Mangoldt count. The test: the *normalized* Z-periods (Gram-lattice
// spacings) — the block-start data in data/blocks_mid.txt — should be ~1 in x-units;
// measured drift from 1 tells how far the "quasi-polynomial" picture is.

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

    // Q1: finite-difference magnitudes |Δ^d x_i| for d = 1,2,3,4 over the bulk.
    // Normalize by the mean gap (~1). Report mean |Δ^d x| and its growth with block
    // length (first half vs second half). Polynomial-like would be ~flat; random
    // walk-like grows as sqrt(block).
    for d in 1..=4usize {
        let mut diffs: Vec<f64> = Vec::new();
        for i in 0..n - d {
            // Δ^d x_i = sum_{k=0..d} (-1)^(d-k) C(d,k) x_{i+k}
            let mut v = 0.0f64;
            let mut c = 1i64; // binomial C(d, k) iteratively
            for k in 0..=d {
                let sign = if (d - k) % 2 == 0 { 1.0 } else { -1.0 };
                v += sign * (c as f64) * x[i + k];
                // update binomial: C(d, k+1) = C(d,k)*(d-k)/(k+1)
                c = c * ((d - k) as i64) / ((k + 1) as i64);
            }
            diffs.push(v);
        }
        let mean_abs: f64 = diffs.iter().map(|v| v.abs()).sum::<f64>() / diffs.len() as f64;
        // first-half vs second-half mean |Δ^d|
        let mid = diffs.len() / 2;
        let m1: f64 = diffs[..mid].iter().map(|v| v.abs()).sum::<f64>() / mid as f64;
        let m2: f64 = diffs[mid..].iter().map(|v| v.abs()).sum::<f64>() / (diffs.len() - mid) as f64;
        println!("Q1 d{} mean_abs {:.4} first_half {:.4} second_half {:.4} growth_ratio {:.3}", d, mean_abs, m1, m2, m2 / m1);
    }

    // Q2: quasi-polynomial "third difference" test (a degree-2 quasi-poly kills Δ^3).
    // Count |Δ^3 x_i| < 1e-2 and < 1e-1; compare with a random-walk null (scrambled gaps).
    let mut third_small_2 = 0usize;
    let mut third_small_1 = 0usize;
    for i in 0..n - 3 {
        let d3 = (x[i + 3] - x[i + 2]) - (x[i + 2] - x[i + 1]) - ((x[i + 2] - x[i + 1]) - (x[i + 1] - x[i]));
        // = x[i+3] - 3x[i+2] + 3x[i+1] - x[i]
        let d3b = x[i + 3] - 3.0 * x[i + 2] + 3.0 * x[i + 1] - x[i];
        if d3.abs() < 1e-1 || d3b.abs() < 1e-1 {
            third_small_1 += 1;
        }
        if d3.abs() < 1e-2 || d3b.abs() < 1e-2 {
            third_small_2 += 1;
        }
    }
    println!("Q2 third_diff_lt_1e-1 {} lt_1e-2 {} n {}", third_small_1, third_small_2, n - 3);

    // Q3: Gram-lattice drift. Use data/blocks_mid.txt: "<mid-index> <block start t>".
    // In x-units the block start should sit at ~ the mid-index (theta(b)/pi). Deviation
    // sd measures the "quasi-period" jitter. (wtest E1 already did this — report once.)
    let blk = fs::read_to_string("data/blocks_mid.txt").expect("blocks");
    let mut mids: Vec<f64> = Vec::new();
    let mut bstarts: Vec<f64> = Vec::new();
    for l in blk.lines() {
        let mut it = l.split_whitespace();
        if let (Some(m), Some(b)) = (it.next(), it.next()) {
            mids.push(m.parse().unwrap());
            bstarts.push(b.parse().unwrap());
        }
    }
    let mut dev_sum = 0.0f64;
    let mut dev_sq = 0.0f64;
    let mut dev_max = 0.0f64;
    let mut cnt = 0usize;
    for (&m, &b) in mids.iter().zip(bstarts.iter()) {
        let dev = theta(b) / PI - m;
        dev_sum += dev;
        dev_sq += dev * dev;
        cnt += 1;
        if dev.abs() > dev_max {
            dev_max = dev.abs();
        }
    }
    let mean = dev_sum / cnt as f64;
    let sd = (dev_sq / cnt as f64 - mean * mean).sqrt();
    println!("Q3 gram_blocks {} dev_mean {:.4} dev_sd {:.4} dev_max {:.4}", cnt, mean, sd, dev_max);

    println!("DONE");
}
