// prime.rs — prime-indexed subsampling probes.
//
// Reads data/zeros.txt (11000 LMFDB ordinates) and data/zeros2.txt (10000 computed).
// Tests the provocations:
//   P1  "zeros are organized by the primes": count 4-term APs (equal gaps to 1e-3)
//       among prime-indexed zero differences; compare vs composite-indexed and
//       vs random-indexed baselines.
//   P2  "zeros are a prime lattice": mean gap of prime-indexed zeros vs composite-
//       indexed vs all (density distortion test).
//   P3  "zeros forget their index": autocorrelation of gap sequence at lags 1..20,
//       plus a runs statistic (up/down runs of consecutive gaps).
//   P4  "zeros are an operator spectrum": nearest-neighbor IPR-like share,
//       and the E10-style nn_share computed on a window.

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

fn is_prime(k: usize) -> bool {
    if k < 2 {
        return false;
    }
    let mut d = 2usize;
    while d * d <= k {
        if k % d == 0 {
            return false;
        }
        d += 1;
    }
    true
}

fn main() {
    let ords = load_ords("data/zeros.txt");
    let n = ords.len();

    // P1: 4-term APs among prime-indexed zero differences (indices 1-based).
    // gaps at prime indices: (t_p - t_{p-1}); look for 4-term APs in the *values*
    // of consecutive prime-indexed gaps (i.e., g_{p_i} == g_{p_{i+1}} == g_{p_{i+2}}).
    let primes: Vec<usize> = (2..=n).filter(|&k| is_prime(k)).collect();
    let mut pgaps: Vec<f64> = Vec::new();
    for &p in primes.iter() {
        if p >= n {
            continue;
        }
        pgaps.push(ords[p] - ords[p - 1]);
    }
    let mut ap4p = 0usize;
    for i in 2..pgaps.len() {
        if (pgaps[i] - pgaps[i - 1]).abs() < 1e-3 && (pgaps[i] - pgaps[i - 2]).abs() < 1e-3 {
            ap4p += 1;
        }
    }
    // composite-indexed gaps
    let comps: Vec<usize> = (4..=n).filter(|&k| !is_prime(k)).collect();
    let mut cgaps: Vec<f64> = Vec::new();
    for &c in comps.iter() {
        if c >= n {
            continue;
        }
        cgaps.push(ords[c] - ords[c - 1]);
    }
    let mut ap4c = 0usize;
    for i in 2..cgaps.len() {
        if (cgaps[i] - cgaps[i - 1]).abs() < 1e-3 && (cgaps[i] - cgaps[i - 2]).abs() < 1e-3 {
            ap4c += 1;
        }
    }
    // random baseline: random subsets of indices of the same size
    let mut rng_state = 0x9E3779B97F4A7C15u64;
    let mut rng = move || {
        rng_state ^= rng_state << 13;
        rng_state ^= rng_state >> 7;
        rng_state ^= rng_state << 17;
        rng_state
    };
    let mut rand_gaps: Vec<f64> = Vec::new();
    let mut trials = 200usize;
    let mut ap4r = 0usize;
    for _ in 0..trials {
        rand_gaps.clear();
        for _ in 0..pgaps.len() {
            let idx = (rng() % (n as u64)) as usize + 1;
            if idx < n {
                rand_gaps.push(ords[idx] - ords[idx - 1]);
            }
        }
        for i in 2..rand_gaps.len() {
            if (rand_gaps[i] - rand_gaps[i - 1]).abs() < 1e-3
                && (rand_gaps[i] - rand_gaps[i - 2]).abs() < 1e-3
            {
                ap4r += 1;
            }
        }
    }
    println!(
        "P1 ap4_prime {} ap4_composite {} ap4_random_avg {} (trials {}) prime_gaps {}",
        ap4p,
        ap4c,
        ap4r as f64 / trials as f64,
        trials,
        pgaps.len()
    );

    // P2: mean gap of prime-indexed vs composite vs all (x-units via theta)
    let x: Vec<f64> = ords.iter().map(|&t| theta(t) / PI).collect();
    let mut pg_mean = 0.0f64;
    for &p in primes.iter() {
        if p < n {
            pg_mean += x[p] - x[p - 1];
        }
    }
    pg_mean /= pgaps.len() as f64;
    let mut cg_mean = 0.0f64;
    for &c in comps.iter() {
        if c < n {
            cg_mean += x[c] - x[c - 1];
        }
    }
    cg_mean /= cgaps.len() as f64;
    let all_mean = (x[n - 1] - x[0]) / (n - 1) as f64;
    println!(
        "P2 mean_gap_prime {:.5} mean_gap_composite {:.5} mean_gap_all {:.5}",
        pg_mean, cg_mean, all_mean
    );

    // P3: gap autocorrelation lags 1..20 + up/down runs.
    let g: Vec<f64> = x.windows(2).map(|w| w[1] - w[0]).collect();
    let gm = g.iter().sum::<f64>() / g.len() as f64;
    let mut var = 0.0f64;
    for &v in g.iter() {
        var += (v - gm) * (v - gm);
    }
    var /= g.len() as f64;
    println!("P3 gap_mean {:.5} gap_var {:.5}", gm, var);
    for lag in 1..=20usize {
        let mut num = 0.0f64;
        let mut den = 0.0f64;
        for i in 0..g.len() - lag {
            num += (g[i] - gm) * (g[i + lag] - gm);
        }
        for i in 0..g.len() {
            den += (g[i] - gm) * (g[i] - gm);
        }
        println!("P3 ac_lag_{} {:.5}", lag, num / den);
    }
    // up/down runs
    let mut runs: Vec<usize> = Vec::new();
    let mut cur = 0usize;
    let mut cur_dir = 0i32;
    for i in 1..g.len() {
        let d = if g[i] > g[i - 1] {
            1
        } else if g[i] < g[i - 1] {
            -1
        } else {
            0
        };
        if d == 0 {
            continue;
        }
        if d == cur_dir {
            cur += 1;
        } else {
            if cur > 0 {
                runs.push(cur);
            }
            cur = 1;
            cur_dir = d;
        }
    }
    if cur > 0 {
        runs.push(cur);
    }
    let mean_run = runs.iter().sum::<usize>() as f64 / runs.len().max(1) as f64;
    println!("P3 runs {} mean_run {:.3}", runs.len(), mean_run);

    // P4: nn_share (nearest-neighbor share of the 1/d pair sum, window R=10) — from twowin E10 but cheap here.
    let r_cut = 10.0f64;
    let mut total = 0.0f64;
    let mut nn = 0.0f64;
    for i in 0..n {
        let xi = x[i];
        let mut dmin = f64::MAX;
        let mut s = 0.0f64;
        for j in 0..n {
            if j == i {
                continue;
            }
            let d = (x[j] - xi).abs();
            if d < dmin {
                dmin = d;
            }
            if d < r_cut && d > 1e-12 {
                s += 1.0 / d;
            }
        }
        total += s;
        nn += if dmin < r_cut && dmin > 1e-12 { 1.0 / dmin } else { 0.0 };
    }
    println!("P4 nn_share {:.6} total_pairsum {:.6}", nn / total, total);

    println!("DONE");
}
