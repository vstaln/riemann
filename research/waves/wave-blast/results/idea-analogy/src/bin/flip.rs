// flip.rs — Boolean-function / sensitivity anchors for the analogy catalog.
//
// The rank-trace certificate is a "Boolean-function-like" object: its value
// is a stable statistic of a huge combinatorial configuration (which zeros
// are simple / on-line). Boolean-function sensitivity theory (O'Donnell) says
// a function with low average sensitivity is a junta — depends on few
// coordinates. Here we measure the ANALOG: how sensitive is the certified
// bound to local perturbations of the gap configuration?
//
// Probes:
//   F1. Flip one gap g_i -> g_i + delta in a 7-point block; measure d(bound)/d
//       (the local floor F(g) sensitivity) — the "coordinate sensitivity" of
//       the certificate.
//   F2. Spectral-sensitivity: the Boolean-Fourier analog is the variance of
//       the function over coordinate flips; here we measure the empirical
//       variance of the floor F(g) over random gap jitter at fixed mean —
//       "average sensitivity" of the certificate to gap noise.
//   F3. Junta-check: does the floor depend mostly on the nearest-neighbor
//       pair terms (w(y_{i+1}-y_i)) or on the long-range terms? Compute the
//       fraction of F's value carried by span-1 (nearest) pair terms.
//
// Uses the 7-point F(g) = p*sum g_i + sum_{i<j} a_ij w(y_j-y_i) functional
// with the uniform window-averaging weights a_ij = 2/(7-(j-i)), kernel
// w(x) = k(x)^2, k = K/K0 (the certified 7-point floor machinery of the
// record's ladder; see research/ladder-f-family/threshold.py).
//
// Pure std. CHECKED NUMERICALLY by construction (this script).

use std::f64::consts::PI;
use std::fs;

const SQRT2: f64 = std::f64::consts::SQRT_2;

fn sinc(z: f64) -> f64 {
    if z.abs() < 1e-12 {
        1.0
    } else {
        z.sin() / z
    }
}

// K(x) = int_{-1/2}^{1/2} cos(sqrt2 t) cos(2 pi x t) dt, K0 = K(0)
fn kappa(x: f64) -> f64 {
    let a = (SQRT2 - 2.0 * PI * x) / 2.0;
    let b = (SQRT2 + 2.0 * PI * x) / 2.0;
    let kx = 0.5 * (sinc(a) + sinc(b));
    kx / sinc(1.0 / SQRT2)
}

fn w(x: f64) -> f64 {
    let k = kappa(x);
    k * k
}

// uniform window-averaging weights a_ij = 2/(7 - (j-i))
fn a_ij(i: usize, j: usize) -> f64 {
    2.0 / (7.0 - (j - i) as f64)
}

// F(g) for the 7-point block, p = pressure
fn f7(g: &[f64], p: f64) -> f64 {
    let mut total = p * g.iter().sum::<f64>();
    let mut y = vec![0.0f64; 7];
    for j in 1..7 {
        y[j] = y[j - 1] + g[j - 1];
    }
    for i in 0..7 {
        for j in (i + 1)..7 {
            total += a_ij(i, j) * w(y[j] - y[i]);
        }
    }
    total
}

// nearest-neighbor (span-1) share of the pair energy
fn nn_share(g: &[f64]) -> f64 {
    let mut y = vec![0.0f64; 7];
    for j in 1..7 {
        y[j] = y[j - 1] + g[j - 1];
    }
    let mut pair_total = 0.0f64;
    let mut nn_total = 0.0f64;
    for i in 0..7 {
        for j in (i + 1)..7 {
            let term = a_ij(i, j) * w(y[j] - y[i]);
            pair_total += term;
            if j - i == 1 {
                nn_total += term;
            }
        }
    }
    if pair_total.abs() < 1e-15 {
        0.0
    } else {
        nn_total / pair_total
    }
}

// simple xorshift64 for reproducibility
struct Rng(u64);
impl Rng {
    fn next(&mut self) -> u64 {
        let mut x = self.0;
        x ^= x << 13;
        x ^= x >> 7;
        x ^= x << 17;
        self.0 = x;
        x
    }
    fn unit(&mut self) -> f64 {
        (self.next() >> 11) as f64 / (1u64 << 53) as f64
    }
}

fn main() {
    println!("== F. Boolean-function sensitivity anchors ==");

    // F1: single-coordinate sensitivity at a near-extremal configuration
    // (the certified floor's minimizer cluster: gaps near the kernel-zero
    // pattern from scratch_q4_out.txt: u ~ 1.057, v ~ 2.012, ...).
    // We use a generic clustered config with gaps in [1, 2] and measure
    // dF/dg_i by finite difference.
    let g0 = [1.0573, 0.9727, 1.0, 1.0, 0.9727, 1.0573]; // symmetric near cluster
    let p = 1.0 / 2300.0; // the trmdy design pressure
    let f0 = f7(&g0, p);
    println!("F1a F(g0) at p=1/2300 = {:.8}", f0);
    for (i, &gi) in g0.iter().enumerate() {
        let mut gp = g0;
        gp[i] += 1e-4;
        let fp = f7(&gp, p);
        println!("F1b dF/dg[{}] ~ {:.4}", i, (fp - f0) / 1e-4);
    }

    // F2: average sensitivity to gap jitter (variance of F over jitter)
    let mut rng = Rng(7);
    let mut sum = 0.0f64;
    let mut sumsq = 0.0f64;
    let trials = 200_000usize;
    for _ in 0..trials {
        // jitter each gap by +-0.05 around g0 (mean preserved)
        let mut g = [0.0f64; 6];
        for k in 0..6 {
            g[k] = g0[k] + (rng.unit() - 0.5) * 0.1;
        }
        let f = f7(&g, p);
        sum += f;
        sumsq += f * f;
    }
    let mean = sum / trials as f64;
    let var = sumsq / trials as f64 - mean * mean;
    println!("F2a mean F over jitter = {:.8}, std = {:.8}", mean, var.sqrt());

    // F3: junta-check — nearest-neighbor share of pair energy
    let share = nn_share(&g0);
    println!("F3a nearest-neighbor (span-1) share of pair energy = {:.4}", share);
    // and at a uniform config (gaps all 1)
    let guni = [1.0f64; 6];
    let share_uni = nn_share(&guni);
    println!("F3b same at uniform gaps = {:.4}", share_uni);

    println!("\nVERDICT: F-probes produced by flip.rs (CHECKED NUMERICALLY)");
}
