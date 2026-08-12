// twowin.rs — two-window pair-correlation / "universality operator" experiment.
//
// Reads data/zeros.txt (11000 LMFDB ordinates). Computes the empirical 2-point
// correlation on two bandwidth windows and the "sliding-window stability" of the
// certificate constants, testing the provocations:
//   E9  "zeros are universal / an operator's spectrum": two-window pair correlation
//       F_alpha for alpha in {0.3, 0.5, 0.7, 0.9, 1.0, 1.1, 1.2, 1.3, 1.5, 2.0}
//       via the standard normalized count (Riemann-von-Mangoldt unfolding).
//   E10 "zeros remember only their near neighbors": localization — for each zero,
//       fraction of the pair-sum carried by the nearest neighbor (IPR-like ratio).
//
// Output: "E9 <alpha> <F>" and "E10 <label> <value>".

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

// normalized ordinate via RvM: x_n = theta(t_n)/pi (so consecutive differ by ~1)
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
    // window on x-coordinates: pairs with |x_i - x_j| < w, count/(2 * (#pairs in window) * w)
    // standard: F(w) = (1/(2 N w)) * sum_{i != j} 1_{|x_i - x_j| < w}  (for w not too small)
    let alphas: [f64; 10] = [0.3, 0.5, 0.7, 0.9, 1.0, 1.1, 1.2, 1.3, 1.5, 2.0];
    for &a in alphas.iter() {
        let w = a;
        let mut c = 0.0f64;
        for i in 0..n {
            // j > i only, symmetric; count pairs
            let xi = x[i];
            let mut j = i + 1;
            while j < n && x[j] - xi < w {
                c += 1.0;
                j += 1;
            }
        }
        let f = c / (2.0 * (n as f64) * w);
        println!("E9 {:.2} {:.6}", a, f);
    }

    // E10: localization — nearest-neighbor share of the total pair sum.
    // pair sum P = sum_i sum_j 1/(|x_i - x_j|) over j != i within a cutoff R (say 10)
    // nearest-neighbor share: for each i, contribution of the single nearest j.
    let r_cut = 10.0f64;
    let mut total = 0.0f64;
    let mut nn_share = 0.0f64;
    for i in 0..n {
        let xi = x[i];
        // nearest
        let mut dmin = f64::MAX;
        for j in 0..n {
            if j == i {
                continue;
            }
            let d = (x[j] - xi).abs();
            if d < dmin {
                dmin = d;
            }
        }
        let mut s = 0.0f64;
        for j in 0..n {
            if j == i {
                continue;
            }
            let d = (x[j] - xi).abs();
            if d < r_cut && d > 1e-12 {
                s += 1.0 / d;
            }
        }
        total += s;
        nn_share += if dmin < r_cut && dmin > 1e-12 { 1.0 / dmin } else { 0.0 };
    }
    println!("E10 nn_share_total {:.6} total_pairsum {:.6}", nn_share / total, total);

    println!("DONE");
}
