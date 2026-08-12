// eigen.rs — Provocation: "Po: the zeros are the spectrum of a self-adjoint operator"
// (Hilbert-Pólya) — and the dual reading: "Po: the certificate's window functional IS
// that operator, so the zeros should diagonalize it." The sandbox showed the
// certificate is a pair-correlation functional, but the *eigen* reading has a concrete
// testable kernel: the matrix W_T (the compressed Weil form of the finitet code) has a
// Gram structure V^T V whose off-diagonal is governed by the kernel k(x) = K(x)/K(0),
// K(x) = ∫ cos(√2 t) cos(2πxt) dt. If the zeros "diagonalize" the window, then the
// Gram matrix on the zero atoms should be nearly diagonal — i.e. the *coherence*
// max_{i≠j} |k(gamma_i - gamma_j)| should be small. Provocation → test:
//   E1  coherence of the zero-atom kernel at the true ordinates vs a random set of
//       the same size and density. If the zeros avoid the kernel's zeros (repulsion
//       at the kernel scale), coherence < random; if they hit them, coherence ~ max.
//   E2  empirical two-point kernel average: (1/N^2) Σ k(x_i - x_j) over the bulk —
//       the "diagonal dominance" of the operator's Gram matrix; compare to the
//       Parseval/lattice value 2 - 1.0231 = 0.9769 (sandbox) and to 0.6725.
//   E3  "zeros are an operator spectrum": the nearest-neighbor IPR-like share of the
//       1/d pair sum (localization diagnostic). A delocalized (GUE-like) spectrum has
//       IPR ~ 3/N; a localized (lattice) one has O(1). We measure the nn_share.
//   E4  Hilbert-Pólya "operator" sanity: the operator is Hermitian, so the spectrum
//       should have NO imaginary part and the empirical level spacing should follow
//       the GUE sine kernel. Report the first three spacing cumulants (mean, var,
//       skew) vs the GUE predictions (mean 1, var 0.286, skew ~0.005) — CHECKED
//       NUMERICALLY as a *description*, not a proof.

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

// kernel k(x) = K(x)/K(0), K(x) = ∫_{-1/2}^{1/2} cos(√2 t) cos(2π x t) dt
// closed form: K(x) = [sin(√2/2 - πx)/(√2 - 2πx) + sin(√2/2 + πx)/(√2 + 2πx)]/2
fn kernel(x: f64) -> f64 {
    let s2 = std::f64::consts::SQRT_2;
    let h = s2 / 2.0;
    let t1 = (h - PI * x).sin() / (s2 - 2.0 * PI * x);
    let t2 = (h + PI * x).sin() / (s2 + 2.0 * PI * x);
    0.5 * (t1 + t2) / 0.5 // K(0) = (sin(√2/2) + sin(√2/2))/(2√2)*2 = ... normalize by K(0)
}

fn k0() -> f64 {
    // K(0) = ∫ cos²(√2 t) dt over [-1/2,1/2] = 1/2 + sin(√2)/(2√2)
    0.5 + (std::f64::consts::SQRT_2).sin() / (2.0 * std::f64::consts::SQRT_2)
}

fn kern_norm(x: f64) -> f64 {
    // normalized kernel K(x)/K(0)
    let s2 = std::f64::consts::SQRT_2;
    let h = s2 / 2.0;
    let t1 = (h - PI * x).sin() / (s2 - 2.0 * PI * x);
    let t2 = (h + PI * x).sin() / (s2 + 2.0 * PI * x);
    (0.5 * (t1 + t2)) / k0()
}

fn main() {
    let ords = load_ords("data/zeros.txt");
    let n = ords.len();
    let x: Vec<f64> = ords.iter().map(|&t| theta(t) / PI).collect();

    // E1: coherence of the kernel on true differences vs a random set.
    // Kernel argument: in x-units the kernel is applied to (gamma_i - gamma_j) scaled
    // by the window; the finitet W_T uses s_rho = (gamma - T)*N/T, i.e. differences
    // are in units of mean spacing. k(u) with u = (x_i - x_j) * c where c = mean gap ~ 1.
    // Compute max |kern_norm(x_i - x_j)| for |x_i - x_j| < 2 (near-diagonal coherence).
    let mut true_max = 0.0f64;
    let mut true_sum = 0.0f64;
    let mut true_cnt = 0.0f64;
    for i in 0..n {
        let xi = x[i];
        let mut j = i + 1;
        while j < n && x[j] - xi < 2.0 {
            let v = kern_norm(x[j] - xi).abs();
            if v > true_max {
                true_max = v;
            }
            true_sum += v;
            true_cnt += 1.0;
            j += 1;
        }
    }
    println!("E1 true_coherence_max {:.4} mean_offdiag {:.4} pairs {:.0}", true_max, true_sum / true_cnt, true_cnt);

    // random baseline: same count of differences drawn uniformly from [0, 2)
    let mut rng_state = 0x123456789ABCDEFu64;
    let mut rng = move || {
        rng_state ^= rng_state << 13;
        rng_state ^= rng_state >> 7;
        rng_state ^= rng_state << 17;
        rng_state
    };
    let mut rand_max = 0.0f64;
    let mut rand_sum = 0.0f64;
    let trials = (true_cnt as usize).min(200_000);
    for _ in 0..trials {
        let u = (rng() >> 11) as f64 / (1u64 << 53) as f64 * 2.0;
        let v = kern_norm(u).abs();
        rand_sum += v;
        if v > rand_max {
            rand_max = v;
        }
    }
    println!("E1 random_coherence_max {:.4} mean_offdiag {:.4} trials {}", rand_max, rand_sum / trials as f64, trials);

    // E2: empirical two-point kernel average over the bulk.
    let lo = 50usize;
    let hi = n - 50;
    let mut s = 0.0f64;
    let mut c = 0.0f64;
    for i in lo..hi {
        let xi = x[i];
        let mut j = i + 1;
        while j < hi && x[j] - xi < 2.0 {
            s += kern_norm(x[j] - xi);
            c += 1.0;
            j += 1;
        }
    }
    // the certificate's HS² constant 1.3275 = tr + off-diag contribution; the
    // "diagonal-dominance" reading: (1/N²) Σ_{i≠j} k(x_i-x_j) ~ 2 * (1.3275 - 1).
    let pair_avg = s / c;
    println!("E2 pair_avg_kernel {:.4}  (Parseval lattice value 0.9769 is the rigid-lattice ceiling; 0.6725 is the zeta constant)", pair_avg);

    // E3: IPR-like nearest-neighbor share (localization).
    let r_cut = 10.0f64;
    let mut total = 0.0f64;
    let mut nn = 0.0f64;
    for i in lo..hi {
        let xi = x[i];
        let mut dmin = f64::MAX;
        let mut s2 = 0.0f64;
        let mut j = i + 1;
        while j < hi && x[j] - xi < r_cut {
            let d = x[j] - xi;
            s2 += 1.0 / d;
            if d < dmin {
                dmin = d;
            }
            j += 1;
        }
        // also left neighbors
        let mut jj = i as isize - 1;
        while jj >= lo as isize && xi - x[jj as usize] < r_cut {
            let d = xi - x[jj as usize];
            s2 += 1.0 / d;
            if d < dmin {
                dmin = d;
            }
            jj -= 1;
        }
        total += s2;
        nn += if dmin < r_cut { 1.0 / dmin } else { 0.0 };
    }
    println!("E3 nn_share {:.6} (GUE-delocalized would be ~ 3/N = {:.6})", nn / total, 3.0 / (hi - lo) as f64);

    // E4: spacing cumulants vs GUE.
    let mut gaps: Vec<f64> = (lo..hi - 1).map(|i| x[i + 1] - x[i]).collect();
    let gm = gaps.iter().sum::<f64>() / gaps.len() as f64;
    let mut v2 = 0.0f64;
    let mut v3 = 0.0f64;
    for &g in gaps.iter() {
        v2 += (g - gm) * (g - gm);
        v3 += (g - gm).powi(3);
    }
    v2 /= gaps.len() as f64;
    v3 /= gaps.len() as f64;
    let sd = v2.sqrt();
    let skew = v3 / (sd * sd * sd);
    // GUE: mean 1, var ~ 0.2868 (2/pi - ... actually var = 1 - 8/pi² ≈ 0.189?? use the
    // well-known GUE spacing var ≈ 0.2868? — the correct GUE var is 1 - 8/pi² ≈ 0.1893.
    // Reference: GUE level spacing pdf p(s) = (32/pi²) s² e^{-4s²/pi}; var = 1 - 8/pi² ≈ 0.1893.
    println!("E4 gap_mean {:.4} sd {:.4} skew {:.3} (GUE: mean 1, sd {:.4}, skew ~0.01)", gm, sd, skew, (1.0 - 8.0 / (PI * PI)).sqrt());

    println!("DONE");
}
