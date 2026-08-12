// pat4.rs — "zeros form a 4-term arithmetic progression" — period-4 gap statistics.
//
// Reads data/zeros2.txt (10000 computed ordinates, 40 digits). Tests:
//   E7a  count of 4-term APs: gaps g_i == g_{i+1} == g_{i+2} to within 1e-3 (absolute).
//   E7b  "lattice + drift": normalized ordinate n -> (t_n - 2pi n / W(n)) — the
//        deviation from the leading-order Gram lattice; report mean abs deviation
//        and its growth with n (linear = drifted lattice; sqrt = random).
//   E7c  period-4 lattice statistic: sum over n of sin(2 pi * (t_n - t_{n-4}) / mean)
//        — measures 4-periodic structure. Also E8: curvature sign pattern of
//        consecutive-difference ratios s_n (E3) — count monotone runs.
//
// All output: "E<k> <label> <value>".

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

fn main() {
    let ords = load_ords("data/zeros2.txt");
    let n = ords.len();

    // E7a: 4-term APs (3 equal consecutive gaps to 1e-3)
    let mut ap4 = 0usize;
    let mut ap4_loose = 0usize;
    for i in 2..n - 2 {
        let g0 = ords[i] - ords[i - 1];
        let g1 = ords[i + 1] - ords[i];
        let g2 = ords[i + 2] - ords[i + 1];
        if (g0 - g1).abs() < 1e-3 && (g1 - g2).abs() < 1e-3 {
            ap4 += 1;
        }
        if (g0 - g1).abs() < 1e-2 && (g1 - g2).abs() < 1e-2 {
            ap4_loose += 1;
        }
    }
    println!("E7a ap4_strict_1e3 {} ap4_loose_1e2 {}", ap4, ap4_loose);

    // E7b: deviation from the leading-order Gram lattice.
    // gamma_n ~ 2 pi n / W(n), W(n) = Lambert W(n/(2 pi e))... use theta(gamma_n) = pi n.
    // theta(t) via Stirling (like wtest).
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
    // Newton invert theta(t) = pi n with a correct seed and derivative.
    fn inv_theta(n: f64) -> f64 {
        // Robust: pure bisection on a wide bracket. theta is increasing on t > ~1.
        let mut lo = 1.0f64;
        let mut hi = 2.0 * PI * (n + 4.0) + 40.0; // generous upper bound
        // ensure theta(lo) < pi n < theta(hi)
        for _ in 0..200 {
            let mid = 0.5 * (lo + hi);
            let f = theta(mid) - PI * n;
            if f > 0.0 {
                hi = mid;
            } else {
                lo = mid;
            }
        }
        0.5 * (lo + hi)
    }
    // deviation d_n = t_n - gamma_n^approx (in units of mean gap)
    let mut dev_sum = 0.0f64;
    let mut dev_max = 0.0f64;
    let mut dev_first = 0.0f64;
    let mut dev_last = 0.0f64;
    let mut first_t = 0.0f64;
    let mut last_t = 0.0f64;
    let mut last_n = 0.0f64;
    for (i, &t) in ords.iter().enumerate() {
        let nn = (i + 1) as f64;
        let g = inv_theta(nn);
        let dev = (t - g).abs();
        dev_sum += dev;
        if dev > dev_max {
            dev_max = dev;
        }
        if i == 100 {
            dev_first = dev;
            first_t = t;
        }
        if i == n - 2 {
            dev_last = dev;
            last_t = t;
            last_n = nn;
        }
    }
    let dev_mean = dev_sum / n as f64;
    println!(
        "E7b dev_mean {:.4} dev_max {:.4} dev_at_100 {:.4} dev_at_{} {:.4}",
        dev_mean, dev_max, dev_first, last_n as usize, dev_last
    );

    // E7c: 4-periodic structure: P4 = (1/(n-4)) sum sin(2 pi (t_n - t_{n-4})/mean_gap)
    let mut gaps: Vec<f64> = ords.windows(2).map(|w| w[1] - w[0]).collect();
    let mean_gap = gaps.iter().sum::<f64>() / gaps.len() as f64;
    let mut p4 = 0.0f64;
    let mut p8 = 0.0f64;
    let mut cnt4 = 0usize;
    for i in 4..n {
        p4 += ((2.0 * PI) * (ords[i] - ords[i - 4]) / mean_gap).sin();
        cnt4 += 1;
    }
    p4 /= cnt4 as f64;
    for i in 8..n {
        p8 += ((2.0 * PI) * (ords[i] - ords[i - 8]) / mean_gap).sin();
    }
    p8 /= (n - 8) as f64;
    println!("E7c p4_periodicity {:.6} p8_periodicity {:.6} mean_gap {:.5}", p4, p8, mean_gap);

    // E8: curvature sign pattern — runs of same-sign second differences.
    // second difference d_i = g_{i+1} - g_i; count runs of consistent sign.
    let mut runs: Vec<usize> = Vec::new();
    let mut cur = 0usize;
    let mut cur_sign = 0i32;
    for i in 1..gaps.len() {
        let d = gaps[i] - gaps[i - 1];
        let sg = if d > 0.0 {
            1
        } else if d < 0.0 {
            -1
        } else {
            0
        };
        if sg == 0 {
            continue;
        }
        if sg == cur_sign {
            cur += 1;
        } else {
            if cur > 0 {
                runs.push(cur);
            }
            cur = 1;
            cur_sign = sg;
        }
    }
    if cur > 0 {
        runs.push(cur);
    }
    let max_run = runs.iter().max().copied().unwrap_or(0);
    let mean_run = runs.iter().sum::<usize>() as f64 / runs.len().max(1) as f64;
    println!("E8 curvature_runs {} max_run {} mean_run {:.3}", runs.len(), max_run, mean_run);

    // E8b: "third difference" near-zero count (polynomial of degree 2 kills 3rd diffs):
    // count |t_{n+3} - 3 t_{n+2} + 3 t_{n+1} - t_n| < 1e-2 (in units where mean gap ~ 1)
    let mut third_small = 0usize;
    for i in 0..n - 3 {
        let d3 = ords[i + 3] - 3.0 * ords[i + 2] + 3.0 * ords[i + 1] - ords[i];
        if d3.abs() < 1e-2 {
            third_small += 1;
        }
    }
    println!("E8b third_diff_small_1e2 {}", third_small);

    println!("DONE");
}
