// curve.rs — Provocation: "Po: all zeros lie on a curve, not a line."
// The functional equation forces symmetry about Re(s) = 1/2 but does NOT force the
// zeros to be ON the line: an off-line pair (rho, 1-rho-bar) is symmetric about 1/2.
// "On a curve" = the zeros' real parts form a non-trivial function of the ordinate.
// Serious kernel: the vertical (real-part) structure is what RH asserts is degenerate.
// A "curve" would manifest as a systematic phase drift of the Z-function (arg Z is
// pinned to 0 mod pi at on-line zeros). Two honest tests:
//   C1  deviation of the actual zeros from the EXACT Gram lattice:
//       x_n = theta(gamma_n)/pi should equal n if gamma_n were the Gram lattice.
//       Report mean |x_n - n|, max, and the growth first-half vs second-half.
//       A drifted lattice would grow ~ n (linear); a random (GUE) sequence grows
//       ~ sqrt(n); both are "not a lattice" but with different signatures.
//   C2  unit-cell occupancy of x-space: partition into cells [k, k+1). A rigid
//       lattice has exactly 1 zero per cell (var 0). Report mean, var, multi rate,
//       empty rate — the honest "how far from a lattice" in the occupancy direction.
//   C3  theoretical conversion (no data): an off-line pair with real-part offset
//       beta at height t twists the phase of xi(1/2+it) by ~ beta * ln(t/2pi) in
//       winding units; at the detection threshold beta ~ 0.02 the twist per zero
//       is ~ 0.02*14.3 ~ 0.3 radians at t ~ 10^4 — below the numerical floor.
//       (This is the scaling law motivating the detection-threshold verdict;
//       printed for reference, CHECKED as a formula, not a numerical measurement.)

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
    // C1: deviation from the exact Gram lattice in x-units (mean spacing = 1).
    let x: Vec<f64> = ords.iter().map(|&t| theta(t) / PI).collect();
    let dev: Vec<f64> = x.iter().enumerate().map(|(i, &v)| v - (i as f64 + 1.0)).collect();
    let mean_abs: f64 = dev.iter().map(|d| d.abs()).sum::<f64>() / n as f64;
    let max_dev = dev.iter().map(|d| d.abs()).fold(0.0f64, f64::max);
    let mid = n / 2;
    let m1: f64 = dev[..mid].iter().map(|d| d.abs()).sum::<f64>() / mid as f64;
    let m2: f64 = dev[mid..].iter().map(|d| d.abs()).sum::<f64>() / (n - mid) as f64;
    println!("C1 n {} mean_abs_dev {:.4} max_dev {:.4} first_half {:.4} second_half {:.4} growth_ratio {:.3}",
             n, mean_abs, max_dev, m1, m2, m2 / m1);
    println!("C1 note: drifted lattice ~ linear growth (ratio >> 1); random walk ~ sqrt growth (ratio ~ sqrt(2) ~ 1.41); here ratio {:.3}",
             m2 / m1);

    // C2: unit-cell occupancy in x-space. Cells [k, k+1) for k = floor(min)..floor(max).
    let lo = x[0].floor() as i64;
    let hi = x[n - 1].ceil() as i64;
    let ncells = (hi - lo) as usize;
    let mut occ = vec![0usize; ncells];
    for &v in x.iter() {
        let k = (v.floor() as i64 - lo) as usize;
        if k < ncells {
            occ[k] += 1;
        }
    }
    let mut sum = 0usize;
    let mut sum2 = 0.0f64;
    let mut multi = 0usize;
    let mut empty = 0usize;
    for &c in occ.iter() {
        sum += c;
        sum2 += (c as f64) * (c as f64);
        if c >= 2 {
            multi += 1;
        }
        if c == 0 {
            empty += 1;
        }
    }
    let mean_occ = sum as f64 / ncells as f64;
    let var_occ = sum2 / ncells as f64 - mean_occ * mean_occ;
    println!("C2 cells {} mean_occ {:.4} var_occ {:.4} (lattice var 0) multi_rate {:.6} empty_rate {:.6}",
             ncells, mean_occ, var_occ, multi as f64 / ncells as f64, empty as f64 / ncells as f64);

    // C3: theoretical phase conversion (formula, no data).
    let ln_t = (ords[n - 1] / (2.0 * PI)).ln();
    println!("C3 ln_t_top {:.3}  (off-line beta=0.02 pair twists phase ~ {:.3} rad/zero at top)",
             ln_t, 0.02 * ln_t);
    println!("C3 note: phase twist per zero ~ beta*ln(t/2pi); below numerical floor for beta < ~0.02 (detection-threshold verdict, attack-detection-threshold.md)");

    println!("DONE");
}
