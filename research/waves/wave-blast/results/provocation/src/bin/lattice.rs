// lattice.rs — Provocation: "Po: the zeros form a lattice."
// The sandbox proved the certificate reads ≈ 0.977 on a *rigid lattice* world
// (Parseval ceiling 2 - 1.0231 = 0.9769) — i.e. if the zeros WERE a lattice, RH-style
// certificates would certify nearly 100%, not 67%. The real zeros certify 0.6725.
// So "zeros are a lattice" is decisively FALSE at the certificate level. The serious
// kernel to extract: how far is the real set from a lattice, in the *only* direction
// that matters to the certificate (the second-moment/pair-correlation direction)?
//   L1  distance from a lattice in the pair-correlation sense: the certificate
//       constant C = tr + off-diag = 1.3275 (measured 1.265→1.287 finite-T, approaching
//       1.3275). The lattice world gives HS²/N → 1.0231; zeta gives 1.3275. Report the
//       finite-T HS²/N of the real zeros in x-units and the implied "lattice-ness"
//       = how far the realized value is from the lattice 1.0231 vs the GUE value 1.3275.
//   L2  "lattice" test via block starts: a lattice has exactly 1 zero per cell; the
//       Gram-interval occupancy variance (multi/empty rates) measures deviation from
//       lattice-ness. (curve C2 already does this — cross-reference.)
//   L3  jittered-lattice benchmark: if the zeros were a jittered lattice with jitter
//       sigma, the certificate constant would interpolate 1.0231 -> 1.3275. Estimate
//       the effective jitter sigma that reproduces the measured HS²/N (an inverse
//       problem); report sigma in units of mean spacing. (The sandbox's jittered
//       lattice gave 0.89-0.90 certificate at its sigma — cross-check.)
//   L4  "lattice with a defect": one missing zero (a gap of 2) — the two-point
//       correlation F(1) drops by ~ 2/N; the certificate constant by ~ 1/N. Report
//       the *sensitivity* of the certificate to a single missing zero (the "defect
//       detectability" of the detection-threshold verdict).

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

fn kern_norm(x: f64) -> f64 {
    let s2 = std::f64::consts::SQRT_2;
    let h = s2 / 2.0;
    let t1 = (h - PI * x).sin() / (s2 - 2.0 * PI * x);
    let t2 = (h + PI * x).sin() / (s2 + 2.0 * PI * x);
    let k0 = 0.5 + (std::f64::consts::SQRT_2).sin() / (2.0 * std::f64::consts::SQRT_2);
    (0.5 * (t1 + t2)) / k0
}

fn main() {
    let ords = load_ords("data/zeros.txt");
    let n = ords.len();
    let x: Vec<f64> = ords.iter().map(|&t| theta(t) / PI).collect();

    // L1: HS²/N reading of the real zeros (finite-T, x-units).
    // The certificate's HS²/N = 1 + (1/N) Σ_{i≠j} k(x_i - x_j) (window kernel).
    let lo = 50usize;
    let hi = n - 50;
    let m = (hi - lo) as f64;
    let mut off = 0.0f64;
    for i in lo..hi {
        let xi = x[i];
        let mut j = i + 1;
        while j < hi && x[j] - xi < 2.0 {
            off += kern_norm(x[j] - xi);
            j += 1;
        }
    }
    let hs2_n = 1.0 + 2.0 * off / m;
    println!("L1 HS2_over_N {:.4}  (lattice 1.0231, GUE/theory 1.3275, zeta finite-T 1.265..1.287)", hs2_n);

    // L2: lattice cell occupancy — 1 zero per cell would be a lattice.
    let blk = fs::read_to_string("data/blocks_mid.txt").expect("blocks");
    let mut bstarts: Vec<f64> = Vec::new();
    for l in blk.lines() {
        let mut it = l.split_whitespace();
        if let (Some(_m), Some(b)) = (it.next(), it.next()) {
            bstarts.push(b.parse().unwrap());
        }
    }
    let mut multi = 0usize;
    let mut empty = 0usize;
    let mut occ = 0usize;
    let mut var_occ = 0.0f64;
    let mut cnt = 0usize;
    for w in bstarts.windows(2) {
        let lo2 = w[0];
        let hi2 = w[1];
        let mut c = 0usize;
        for &t in ords.iter() {
            if t > lo2 && t < hi2 {
                c += 1;
            }
        }
        occ += c;
        var_occ += (c as f64) * (c as f64);
        cnt += 1;
        if c >= 2 {
            multi += 1;
        }
        if c == 0 {
            empty += 1;
        }
    }
    let mean_occ = occ as f64 / cnt as f64;
    let var_occ = var_occ / cnt as f64 - mean_occ * mean_occ;
    println!("L2 cells {} mean_occ {:.4} var_occ {:.4} (lattice would be var 0) multi {} empty {}", cnt, mean_occ, var_occ, multi, empty);

    // L3: effective jitter sigma reproducing HS²/N.
    // Model: jittered lattice x_i = i + sigma * epsilon_i (epsilon ~ N(0,1)). The
    // pair-sum E[k(x_i - x_j)] for |i-j| = d: E[k(d + sigma(eps_i - eps_j))] ~ k(d) +
    // sigma² k''(d). Numerically solve for sigma matching the measured off-diag mean.
    // We use the empirical pair-avg (L1/E2) and the kernel second difference.
    let mut off_sum = 0.0f64;
    let mut off_cnt = 0.0f64;
    for i in lo..hi {
        let xi = x[i];
        let mut j = i + 1;
        while j < hi && x[j] - xi < 2.0 {
            off_sum += kern_norm(x[j] - xi);
            off_cnt += 1.0;
            j += 1;
        }
    }
    let pair_avg = off_sum / off_cnt;
    // theoretical lattice pair-avg: sum_{d>=1} k(d) ~ integrate: use the mean over the
    // same window (the lattice would put pairs at integer d).
    let mut lat_sum = 0.0f64;
    let mut lat_cnt = 0.0f64;
    for d in 1..20 {
        lat_sum += kern_norm(d as f64);
        lat_cnt += 1.0;
    }
    let lat_avg = lat_sum / lat_cnt;
    // crude sigma estimate: sigma ~ sqrt((pair_avg - lat_avg) / |k''|_scale), k'' ~ -pi²
    let kpp = -PI * PI; // rough scale
    let sigma_est = ((pair_avg - lat_avg) / kpp.abs()).sqrt().max(0.0);
    println!("L3 pair_avg {:.4} lattice_pair_avg {:.4} effective_jitter_sigma_est {:.3} (units of mean spacing)", pair_avg, lat_avg, sigma_est);

    // L4: single-defect sensitivity — remove one zero in the bulk, recompute F(1).
    let w = 1.0f64;
    let mut c_full = 0.0f64;
    for i in lo..hi {
        let xi = x[i];
        let mut j = i + 1;
        while j < hi && x[j] - xi < w {
            c_full += 1.0;
            j += 1;
        }
    }
    let f_full = c_full / (2.0 * m * w);
    // remove zero at index mid
    let rm = (lo + hi) / 2;
    let mut c_rm = 0.0f64;
    for i in lo..hi {
        if i == rm {
            continue;
        }
        let xi = x[i];
        let mut j = i + 1;
        while j < hi && x[j] - xi < w {
            if j == rm {
                j += 1;
                continue;
            }
            c_rm += 1.0;
            j += 1;
        }
    }
    let f_rm = c_rm / (2.0 * (m - 1.0) * w);
    println!("L4 F1_full {:.6} F1_minus_one_zero {:.6} delta {:.6} (detection threshold ~ 0.7% band width)", f_full, f_rm, f_rm - f_full);

    println!("DONE");
}
