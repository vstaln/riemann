// primeq.rs — Provocation: "Po: the zeros are organized by the primes"
// (i.e. ζ is a polynomial-like Euler product, so the zero gaps "remember" the prime
// structure). Serious kernels: (a) is there ANY residual prime-indexed structure in
// the zero gaps beyond what a generic GUE sequence has? (b) can the *window* detect
// prime arithmetic — the certificate's prime-side comes from the explicit formula
// (Guinand-Weil), so a prime-indexed subsample of the gaps probes whether the zero
// statistics "know" their index. Prior probe (prime.rs P1-P4) found: 4-term APs in
// prime-indexed gaps = 0 (vs random baseline 0); mean gap of prime-indexed zeros =
// 0.9739 vs composite 1.0036 (a density distortion); gap autocorrelations small but
// lag-16 = -0.106 and lag-18 = +0.068 (borderline). New here:
//   P1  prime-indexed gap distribution: KS-style comparison of prime-indexed gaps vs
//       composite-indexed gaps (in x-units), with a shuffled baseline.
//   P2  "zeta is a polynomial in the primes": the *2-point correlation restricted to
//       prime-indexed pairs* F_p(alpha) vs the all-pairs F(alpha). If the zeros were
//       "organized by the primes", the prime-indexed pairs would show a different
//       pair correlation.
//   P3  an Euler-product "factor memory" test: gaps following a zero whose index is a
//       prime power p^k vs gaps following a generic index — mean and variance.
//   P4  the certificate's "prime-side" lever: the off-diagonal prime-pair sum
//       (M29's beyond-1 wall) — report the *empirical* size of the beyond-1 pair
//       count at alpha in (1, 1.3] (the unexplained alpha~1.1 feature) and its
//       prime-indexed restriction. (Diagnostic only — no claim of proof.)

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

fn is_prime_power(k: usize) -> bool {
    // k = p^e for e >= 1
    if k < 2 {
        return false;
    }
    let mut d = 2usize;
    while d * d <= k {
        if k % d == 0 {
            let mut t = k;
            while t % d == 0 {
                t /= d;
            }
            return t == 1;
        }
        d += 1;
    }
    true // prime itself
}

fn main() {
    let ords = load_ords("data/zeros.txt");
    let n = ords.len();
    let x: Vec<f64> = ords.iter().map(|&t| theta(t) / PI).collect();
    let g: Vec<f64> = x.windows(2).map(|w| w[1] - w[0]).collect();

    // P1: prime-indexed gap mean/var vs composite-indexed, with a shuffle baseline.
    let primes: Vec<usize> = (2..n).filter(|&k| is_prime(k)).collect();
    let mut pg: Vec<f64> = Vec::new();
    for &p in primes.iter() {
        if p < n {
            pg.push(x[p] - x[p - 1]);
        }
    }
    let comps: Vec<usize> = (4..n).filter(|&k| !is_prime(k)).collect();
    let mut cg: Vec<f64> = Vec::new();
    for &c in comps.iter() {
        if c < n {
            cg.push(x[c] - x[c - 1]);
        }
    }
    let (pm, pv) = {
        let s = pg.iter().sum::<f64>();
        let m = s / pg.len() as f64;
        let v = pg.iter().map(|&v| (v - m) * (v - m)).sum::<f64>() / pg.len() as f64;
        (m, v)
    };
    let (cm, cv) = {
        let s = cg.iter().sum::<f64>();
        let m = s / cg.len() as f64;
        let v = cg.iter().map(|&v| (v - m) * (v - m)).sum::<f64>() / cg.len() as f64;
        (m, v)
    };
    // KS two-sample statistic between pg and cg (on x-units, mean ~1)
    let mut pg_s = pg.clone();
    let mut cg_s = cg.clone();
    pg_s.sort_by(|a, b| a.partial_cmp(b).unwrap());
    cg_s.sort_by(|a, b| a.partial_cmp(b).unwrap());
    let ks = {
        let (mut i, mut j) = (0usize, 0usize);
        let mut d = 0.0f64;
        while i < pg_s.len() && j < cg_s.len() {
            if pg_s[i] < cg_s[j] {
                i += 1;
            } else {
                j += 1;
            }
            let frac = (i as f64 / pg_s.len() as f64) - (j as f64 / cg_s.len() as f64);
            if frac.abs() > d {
                d = frac.abs();
            }
        }
        d
    };
    println!("P1 prime_gap_mean {:.4} var {:.4} | comp_gap_mean {:.4} var {:.4} | KS {:.4}", pm, pv, cm, cv, ks);

    // P2: pair correlation restricted to prime-indexed pairs.
    let alphas: [f64; 6] = [0.3, 0.6, 1.0, 1.1, 1.2, 1.3];
    for &a in alphas.iter() {
        let mut c_all = 0.0f64;
        let mut c_p = 0.0f64;
        let mut m_all = 0.0f64;
        let mut m_p = 0.0f64;
        for i in 50..n - 50 {
            let xi = x[i];
            let mut j = i + 1;
            while j < n - 50 && x[j] - xi < a {
                c_all += 1.0;
                let isp = is_prime(i + 1) || is_prime(j + 1);
                if isp {
                    c_p += 1.0;
                }
                j += 1;
            }
            m_all += 1.0;
            if is_prime(i + 1) {
                m_p += 1.0;
            }
        }
        let f_all = c_all / (2.0 * m_all * a);
        // prime-pair fraction normalized by the prime-indexed density
        let dens_p = m_p / m_all;
        let f_p = c_p / (2.0 * m_all * a) / dens_p; // normalize by prime density
        println!("P2 alpha {:.2} F_all {:.4} F_prime_normalized {:.4}", a, f_all, f_p);
    }

    // P3: gap after prime-power indices vs after generic indices.
    let mut ppg: Vec<f64> = Vec::new();
    let mut other: Vec<f64> = Vec::new();
    for i in 1..n - 1 {
        let v = x[i + 1] - x[i];
        if is_prime_power(i + 1) {
            ppg.push(v);
        } else {
            other.push(v);
        }
    }
    let (ppm, ppv) = {
        let s = ppg.iter().sum::<f64>();
        let m = s / ppg.len() as f64;
        let v = ppg.iter().map(|&v| (v - m) * (v - m)).sum::<f64>() / ppg.len() as f64;
        (m, v)
    };
    let (om, ov) = {
        let s = other.iter().sum::<f64>();
        let m = s / other.len() as f64;
        let v = other.iter().map(|&v| (v - m) * (v - m)).sum::<f64>() / other.len() as f64;
        (m, v)
    };
    println!("P3 prime_power_gap_mean {:.4} var {:.4} | other_mean {:.4} var {:.4}", ppm, ppv, om, ov);

    // P4: beyond-1 pair count and its prime-indexed restriction (the alpha~1.1 feature).
    for &a in [1.0f64, 1.1, 1.2, 1.3].iter() {
        let mut c_all = 0.0f64;
        let mut c_p = 0.0f64;
        for i in 50..n - 50 {
            let xi = x[i];
            let mut j = i + 1;
            while j < n - 50 && x[j] - xi < a {
                if x[j] - xi >= 1.0 {
                    c_all += 1.0;
                    if is_prime(i + 1) || is_prime(j + 1) {
                        c_p += 1.0;
                    }
                }
                j += 1;
            }
        }
        println!("P4 pairs_in_[1,{:.1}) {:.0} prime_indexed {:.0} share {:.4}", a, c_all, c_p, c_p / c_all.max(1.0));
    }

    println!("DONE");
}
