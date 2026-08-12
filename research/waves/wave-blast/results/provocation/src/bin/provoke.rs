// provoke.rs — Provocation-engine anchors for the deliverable idea-provocation.md.
//
// Sections:
//   R0  Record arithmetic (PROVEN closed forms): reproduce the certified record
//       bound 0.6732628655343560 at (alpha=1.49, psum=1/220, m=133, eps=0.00806)
//       and the H-max anchor H(sqrt2) = 0.67250070367941164573 (Theorem-D const).
//       Also report the tau and B/m terms.
//   R1  "How absurd is each next milestone" map (provocation pricing): for targets
//       0.6733 / 0.6740 / 2/3 / 0.6750 / 0.6818, the certified eps that would be
//       needed at the record's (alpha=1.49, psum=1/220, m=133), solved by
//       bisection in eps. This prices each provocation's claim.
//   R2  "Curve, not line" phase-drift decomposition: dev(b) = theta(b)/pi + 1 - N
//       for the Gram-convention block starts (blocks_orig.txt). The +1 removes the
//       Riemann-von-Mangoldt offset so dev ~ S(T)/pi (the RvM remainder), which is
//       O(log T)-bounded, NOT a linear curve drift. Report mean/sd/slope and the
//       slope's significance against the residual sd (a "curve" would give a slope
//       >> sd/sqrt(n); the RvM remainder should give slope ~ 0).
//   R3  "Zeros form a drifted lattice mod 1": equidistribution discrepancy of
//       gamma_n/(2 pi) mod 1 over the first 11000 ordinates (zeros.txt). A lattice
//       + irrational drift fills [0,1) uniformly (discrepancy ~ 1/sqrt(N)); a
//       rational-period lattice would show a gap. Report D*(N) = max abs deviation
//       of the empirical CDF from uniform, and D*/sqrt(N).
//
// All outputs are produced by this script (CHECKED NUMERICALLY); the record value
// is additionally cross-checked against mpmath (scratch/paircorr/sqrt2_bound.py).

use std::f64::consts::PI;
use std::fs;

// theta(t) = Im log Gamma(1/4 + it/2) - (t/2) ln pi (Stirling, 1/(12s) term;
// error O(1/|s|^3) ~ 1e-13 at t ~ 5000).
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

// H(alpha) for the cosine window (I0/I2/J closed forms; matches
// scratch/paircorr/sqrt2_bound.py to ~1e-15).
fn h_cos(alpha: f64) -> f64 {
    let a = alpha;
    let i0 = 2.0 * (a / 2.0).sin() / a;
    let i2 = 0.5 + a.sin() / (2.0 * a);
    let cst = (a / 2.0).sin() / a + 2.0 * (a / 2.0).cos() / (a * a);
    let jv = -2.0 * i2 / (a * a) + cst * i0;
    let c = i0 * i0 / (i2 + jv);
    2.0 - 1.0 / c
}

fn phi_m(a: f64, m: f64) -> f64 {
    if a <= m / (m - 1.0) {
        a
    } else {
        2.0 * ((m - 1.0) * a / m).sqrt() - 1.0 + a / m
    }
}

fn joint_bound(h: f64, eps: f64, m: f64, psum: f64) -> (f64, f64, f64) {
    // tau = (m-6)/m * psum  (coboundary design, sum p_i = psum)
    let tau = (m - 6.0) / m * psum;
    let a = eps * (m - 6.0);
    let b = phi_m(a, m);
    ((h - tau) / (1.0 - b / m), tau, b / m)
}

// eps solving bound(eps) = target at (alpha, m, psum), by bisection.
fn eps_for(h: f64, m: f64, psum: f64, target: f64) -> f64 {
    let mut lo = 0.0f64;
    let mut hi = 0.02f64;
    for _ in 0..80 {
        let mid = 0.5 * (lo + hi);
        let (b, _, _) = joint_bound(h, mid, m, psum);
        if b > target {
            hi = mid; // bound increasing in eps: over-shot, come down
        } else {
            lo = mid; // under-shot, go up
        }
    }
    0.5 * (lo + hi)
}

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
    // ---------------- R0: record arithmetic ----------------
    let h149 = h_cos(1.49);
    let hs2 = h_cos(std::f64::consts::SQRT_2);
    let m = 133.0f64;
    let psum = 1.0 / 220.0;
    let (b_rec, tau, bm) = joint_bound(h149, 0.00806, m, psum);
    println!("R0 H(1.49) = {:.15}", h149);
    println!("R0 H(sqrt2) = {:.15}  (Theorem-D window constant 0.67250070367941164573)", hs2);
    println!("R0 record bound at (1.49, psum=1/220, m=133, eps=0.00806) = {:.15}", b_rec);
    println!("R0   tau = {:.12}  B/m = {:.12}", tau, bm);
    println!("R0   abs diff vs certified 0.6732628655343560 = {:.3e}", (b_rec - 0.6732628655343560).abs());
    // check H(sqrt2) vs the literature constant
    println!("R0   abs diff H(sqrt2) vs 0.67250070367941164573 = {:.3e}",
             (hs2 - 0.67250070367941164573).abs());

    // ---------------- R1: milestone pricing ----------------
    println!("\nR1 eps needed at (alpha=1.49, psum=1/220, m=133) to reach each target:");
    for &(name, tgt) in &[
        ("0.6733", 0.6733f64),
        ("0.6740", 0.6740f64),
        ("2/3    ", 2.0 / 3.0),
        ("0.6750", 0.6750f64),
        ("0.6818", 0.6818f64),
        ("1.0000", 1.0f64),
    ] {
        let e = eps_for(h149, m, psum, tgt);
        println!("R1 target {} -> eps needed {:.6}  (record eps = 0.00806, ratio {:.2}x)",
                 name, e, e / 0.00806);
    }
    // ... and at the H-max alpha = sqrt(2) (same eps certification burden assumed):
    println!("R1 (same map at alpha=sqrt(2), the H-max window):");
    for &(name, tgt) in &[("0.6733", 0.6733f64), ("2/3", 2.0 / 3.0), ("0.6740", 0.6740f64)] {
        let e = eps_for(hs2, m, psum, tgt);
        println!("R1 sqrt2 target {} -> eps needed {:.6}", name, e);
    }

    // ---------------- R2: curve phase-drift decomposition ----------------
    println!("\nR2 phase-drift decomposition (blocks_orig.txt, Gram convention):");
    let blk = fs::read_to_string("data/blocks_orig.txt").expect("blocks_orig");
    let mut idx: Vec<f64> = Vec::new();
    let mut bstart: Vec<f64> = Vec::new();
    for l in blk.lines() {
        let mut it = l.split_whitespace();
        if let (Some(a), Some(b)) = (it.next(), it.next()) {
            idx.push(a.parse().unwrap());
            bstart.push(b.parse().unwrap());
        }
    }
    let n = idx.len();
    // dev = theta(b)/pi + 1 - N   (RvM: N(T) ~ theta/pi + 1 + S(T))
    let dev: Vec<f64> = idx
        .iter()
        .zip(bstart.iter())
        .map(|(&nidx, &b)| theta(b) / PI + 1.0 - nidx)
        .collect();
    let mean = dev.iter().sum::<f64>() / n as f64;
    let sd = (dev.iter().map(|d| (d - mean) * (d - mean)).sum::<f64>() / (n - 1) as f64).sqrt();
    let i_mean = idx.iter().sum::<f64>() / n as f64;
    let mut num = 0.0f64;
    let mut den = 0.0f64;
    for (&i, &d) in idx.iter().zip(dev.iter()) {
        num += (i - i_mean) * (d - mean);
        den += (i - i_mean) * (i - i_mean);
    }
    let slope = num / den;
    let t_stat = slope * den.sqrt() / sd;
    // A "curve" would give |slope| >> sd/sqrt(n); the RvM remainder S(T) ~ O(log T)
    // should give slope consistent with 0.
    println!("R2 n_blocks {} mean_dev {:.6} sd {:.6}", n, mean, sd);
    println!("R2 slope {:.2e} t_stat {:.2}   (|t| >> 2 would be a curve signal)", slope, t_stat);
    println!("R2 sd/sqrt(n) = {:.2e} (noise floor for the slope)", sd / (n as f64).sqrt());
    // distributional check: is dev bounded like log T? max |dev| vs log(t_top)
    let t_top = bstart[n - 1];
    let max_abs = dev.iter().fold(0.0f64, |a, &d| a.max(d.abs()));
    println!("R2 max|dev| {:.4} vs log(t_top/2pi) {:.4} (ratio {:.3})",
             max_abs, (t_top / (2.0 * PI)).ln(), max_abs / (t_top / (2.0 * PI)).ln());

    // ---------------- R3: mod-1 equidistribution ----------------
    println!("\nR3 mod-1 equidistribution of gamma_n/(2pi) (zeros.txt, first 11000):");
    let ords = load_ords("data/zeros.txt");
    let nn = ords.len();
    let mut frac: Vec<f64> = ords.iter().map(|&t| (t / (2.0 * PI)).fract()).collect();
    frac.sort_by(|a, b| a.partial_cmp(b).unwrap());
    // Kolmogorov-style discrepancy: D* = max_k |F_k - k/N| over sorted fractions,
    // with the empirical CDF taken at the points.
    let mut dstar = 0.0f64;
    for (k, &f) in frac.iter().enumerate() {
        let cdf = (k as f64 + 1.0) / nn as f64;
        let dev = (cdf - f).abs();
        if dev > dstar {
            dstar = dev;
        }
    }
    println!("R3 N {} D* {:.5}  D*/sqrt(N) {:.2e}  (Kolmogorov 95% 1.22/sqrt(N) = {:.4}; ratio {:.2})",
             nn, dstar, dstar / (nn as f64).sqrt(), 1.22 / (nn as f64).sqrt(),
             dstar / (1.22 / (nn as f64).sqrt()));
    // Also the largest gap:
    let mut max_gap = frac[0] + (1.0 - frac[nn - 1]);
    for w in frac.windows(2) {
        let g = w[1] - w[0];
        if g > max_gap {
            max_gap = g;
        }
    }
    println!("R3 max_gap {:.5}  (uniform => ~ ln(N)/N = {:.4})",
             max_gap, (nn as f64).ln() / nn as f64);

    println!("DONE");
}
