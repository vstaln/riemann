// rep.rs — repulsion/order probes for the provocation wave.
//
// All in x-units (x_n = theta(t_n)/pi, mean spacing 1).
//   R1  close-pair exponent: #pairs with |x_i - x_j| < delta vs delta (log-log slope).
//       GUE predicts slope 3 (rho2 ~ (pi x)^2/3); Poisson predicts 1; lattice ~ 0 below
//       the lattice constant. Data: zeros.txt (11000 LMFDB ordinates).
//   R2  running min gap vs N: min gap among the first k zeros (repulsion => slow decrease,
//       super-linear suppression).
//   R3  gap palindrome (reflection symmetry of the SET): |g_i - g_{n-2-i}| mean.
//   R4  theta self-check against mpmath (calibration lines).
//   R5  close-pair count at small delta in absolute terms (pairs < 0.05, < 0.1).

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

    // R4 calibration: print theta/pi at the first zero and near the 10000th.
    println!("R4 theta_pi_14_1347 {:.8}", theta(14.1347251417346937904572519835625) / PI);
    println!("R4 theta_pi_9877_78 {:.8}", theta(9877.782655) / PI);
    println!("R4 x_first {:.6} x_last {:.6} n {}", x[0], x[n - 1], n);

    // R1: close-pair counts at logarithmic delta grid.
    let deltas: [f64; 14] = [
        0.004, 0.006, 0.01, 0.015, 0.02, 0.03, 0.05, 0.07, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5,
    ];
    println!("R1 pairs_vs_delta");
    let mut prev = (0.0f64, 0.0f64);
    let mut prev_count = 0.0f64;
    for &d in deltas.iter() {
        let mut c = 0.0f64;
        for i in 0..n {
            let xi = x[i];
            let mut j = i + 1;
            while j < n && x[j] - xi < d {
                c += 1.0;
                j += 1;
            }
        }
        // pairs are unordered; expected #pairs = N * integral of rho2, N ~ n
        println!("R1 {:.3} {:.1}", d, c);
        if prev.0 != 0.0 {
            let slope = (c / prev_count).ln() / (d / prev.0).ln();
            println!("R1 slope {:.3} {:.3}", d, slope);
        }
        prev = (d, c);
        prev_count = c;
    }

    // R5: absolute close-pair counts.
    let mut c005 = 0.0f64;
    let mut c01 = 0.0f64;
    for i in 0..n {
        let xi = x[i];
        let mut j = i + 1;
        while j < n && x[j] - xi < 0.1 {
            let d = x[j] - xi;
            if d < 0.05 {
                c005 += 1.0;
            }
            c01 += 1.0;
            j += 1;
        }
    }
    println!("R5 pairs_lt_0.05 {:.0} pairs_lt_0.1 {:.0}", c005, c01);

    // R2: running min gap vs k (in x units).
    let ks: [usize; 6] = [100, 500, 1000, 3000, 6000, n - 1];
    let mut run_min = f64::MAX;
    for &k in ks.iter() {
        for i in 0..k.min(n) {
            let d = (x[i + 1] - x[i]).abs();
            if d < run_min {
                run_min = d;
            }
        }
        println!("R2 min_gap_first_{} {:.6}", k, run_min);
    }

    // R3: gap palindrome.
    let mut g: Vec<f64> = x.windows(2).map(|w| w[1] - w[0]).collect();
    let m = g.len();
    let mut pal = 0.0f64;
    for i in 0..m / 2 {
        pal += (g[i] - g[m - 1 - i]).abs();
    }
    pal /= (m / 2) as f64;
    println!("R3 gap_palindrome_mean {:.6}", pal);

    println!("DONE");
}
