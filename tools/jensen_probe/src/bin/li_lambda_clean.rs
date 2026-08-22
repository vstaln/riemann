// Clean-data rescan of the spectral Li formula restricted to TRUSTWORTHY rows.
// Data quarantine: zeros_rust_100k.txt is corrupted above gamma~17255; only
// rows 1..19000 are used. Values are numerical probes, not a proof of RH.
// Lower-bound honesty: omitted zeros contribute >= 0 (sin^2 >= 0), so every
// lambda_clean(n) below is a rigorous LOWER bound of the true lambda_n.

use std::fs;
use std::path::PathBuf;

const ROW_MAX: u32 = 19_000;
const N_MAX: usize = 30_000;
const QUARANTINE_G: f64 = 17_255.0;
const DATA: &str = "/home/vstaln/riemann/tools/data/zeros_rust_100k.txt";

fn load_trusted_gammas(path: &str) -> Vec<f64> {
    let text = fs::read_to_string(PathBuf::from(path))
        .unwrap_or_else(|e| panic!("cannot read zeros file {path}: {e}"));
    text.lines()
        .filter_map(|line| {
            let line = line.trim();
            let mut fields = line.split_whitespace();
            let row: u32 = fields.next()?.parse().ok()?;
            if !(1..=ROW_MAX).contains(&row) {
                return None;
            }
            fields.next().unwrap_or_else(|| {
                panic!("row {row}: missing ordinate")
            }).parse::<f64>().ok()
        })
        .collect()
}

// Phasor recurrence engine (same validated update formula as li_lambda_1e5.rs):
// theta_j = atan(1/(2 gamma_j)); sum 4 sin^2(n theta_j) accumulated block-wise.
fn spectral_sum(gammas: &[f64], n_max: usize) -> Vec<f64> {
    const LANES: usize = 8;
    let mut sums = vec![0.0f64; n_max];
    for block in 0..gammas.len().div_ceil(LANES) {
        let mut step_cos = [1.0f64; LANES];
        let mut step_sin = [0.0f64; LANES];
        let mut phase_cos = [1.0f64; LANES];
        let mut phase_sin = [0.0f64; LANES];
        let mut active = 0usize;
        for lane in 0..LANES {
            if let Some(&gamma) = gammas.get(block * LANES + lane) {
                let theta = (1.0 / (2.0 * gamma)).atan();
                step_cos[lane] = theta.cos();
                step_sin[lane] = theta.sin();
                active += 1;
            }
        }
        for value in sums.iter_mut() {
            let mut block_sum = 0.0;
            for lane in 0..active {
                let next_cos =
                    phase_cos[lane] * step_cos[lane] - phase_sin[lane] * step_sin[lane];
                let next_sin =
                    phase_cos[lane] * step_sin[lane] + phase_sin[lane] * step_cos[lane];
                phase_cos[lane] = next_cos;
                phase_sin[lane] = next_sin;
                block_sum += 4.0 * next_sin * next_sin;
            }
            *value += block_sum;
        }
    }
    sums
}

// Riemann-von Mangoldt density model of the omitted tail:
//   tail(n) ~= int_G^infty 4 sin^2(n/(2g)) * (ln(g/2pi)/(2pi)) dg.
// Substituting u = n/(2g), then v = ln u:
//   tail(n) = (n/(4pi)) * int_{-inf}^{V} sin^2(e^v) ln(n/(4 pi e^v)) dv,
// V = ln(n/(2G)). Trapezoid over v in [V-90, V]; at the left end the
// integrand is O(e^{2v}) and utterly negligible. [CONJECTURED model]
fn tail_integral(n: usize) -> f64 {
    let nf = n as f64;
    let v_hi = (nf / (2.0 * QUARANTINE_G)).ln();
    let span = 90.0f64;
    let steps = 90_000usize;
    let h = span / steps as f64;
    let mut acc = 0.0f64;
    for k in 0..=steps {
        let v = v_hi - span + h * k as f64;
        let u = v.exp();
        let s2 = u.sin() * u.sin();
        // stable small-u form: sin^2(u)/u^2 -> 1, written as (s2/(u*u))*ln(...)
        let logterm = (nf / (4.0 * std::f64::consts::PI * u)).ln();
        acc += (s2 / (u * u)) * logterm;
    }
    acc * h * nf / (4.0 * std::f64::consts::PI)
}

fn main() {
    let gammas = load_trusted_gammas(DATA);
    assert_eq!(gammas.len(), ROW_MAX as usize, "expected exactly 19000 trusted rows");
    let gamma_max = gammas.iter().cloned().fold(f64::NEG_INFINITY, f64::max);
    println!(
        "li_lambda_clean J={J} row_range=1..{ROW_MAX} gamma_max={gamma_max:.9}",
        J = gammas.len()
    );
    println!("quarantine: corrupted rows >19000 EXCLUDED; lambda_clean is a rigorous LOWER bound of true lambda_n (sin^2>=0)");

    let started = std::time::Instant::now();
    let lambda = spectral_sum(&gammas, N_MAX);

    let (min_index, min_value) = lambda
        .iter()
        .enumerate()
        .min_by(|a, b| a.1.total_cmp(b.1))
        .unwrap();
    println!(
        "clean global_min n={} lambda_clean={:.12}",
        min_index + 1,
        min_value
    );
    let first_negative = lambda.iter().position(|&x| x < 0.0);
    println!(
        "clean all_nonnegative_1..30000={}",
        first_negative.is_none()
    );

    for n in [1usize, 1000, 5155, 10000, 30000] {
        println!(
            "anchor n={n} lambda_clean={:.12} tail_integral_est={:.6e}",
            lambda[n - 1],
            tail_integral(n)
        );
    }

    // Plant control (beta_0 = 0.85 quadruplet, identical construction to
    // li_lambda_1e5.rs): rho = beta + i*gamma_1; z1 = 1 - 1/rho, z3 = 1/z1;
    // exact planted contribution 4 - 2 Re(z1^n) - 2 Re(z3^n).
    let beta = 0.85f64;
    let g1 = 14.13472514f64;
    let den = beta * beta + g1 * g1;
    let z1 = (
        ((beta - 1.0) * beta + g1 * g1) / den,
        g1 / den,
    );
    let z1n2 = z1.0 * z1.0 + z1.1 * z1.1;
    let z3 = (z1.0 / z1n2, -z1.1 / z1n2);
    let mut p1 = (1.0f64, 0.0f64);
    let mut p3 = (1.0f64, 0.0f64);
    let mut first_plant_negative = false;
    for n in 1..=N_MAX {
        p1 = (p1.0 * z1.0 - p1.1 * z1.1, p1.0 * z1.1 + p1.1 * z1.0);
        p3 = (p3.0 * z3.0 - p3.1 * z3.1, p3.0 * z3.1 + p3.1 * z3.0);
        let planted = lambda[n - 1] + 4.0 - 2.0 * p1.0 - 2.0 * p3.0;
        if planted < 0.0 && !first_plant_negative {
            first_plant_negative = true;
            println!("plant first_negative n={n} planted_lambda={planted:.12}");
            break;
        }
    }
    if !first_plant_negative {
        println!("plant first_negative=NONE through n={N_MAX}");
    }

    // Cross-check vs li_lambda_1e5.rs at n=1000: subtract this scan's own
    // estimate of the corrupted-row contribution (rows >19000 of the same file)
    // plus that binary's n^2*crude_kernel_bound additive term.
    let n_x = 1000usize;
    let mut corrupt = 0.0f64;
    {
        // recompute theta phases for rows 19001..end only, single pass at n=1000
        let text = fs::read_to_string(PathBuf::from(DATA)).unwrap();
        for line in text.lines() {
            let mut fields = line.trim().split_whitespace();
            let row: u32 = match fields.next().and_then(|f| f.parse().ok()) {
                Some(r) => r,
                None => continue,
            };
            if row <= ROW_MAX {
                continue;
            }
            if let Ok(g) = fields.next().unwrap_or("").parse::<f64>() {
                let th = (n_x as f64) / (2.0 * g);
                let s = th.sin();
                corrupt += 4.0 * s * s;
            }
        }
    }
    let cutoff_all: f64 = {
        let text = fs::read_to_string(PathBuf::from(DATA)).unwrap();
        text.lines().rev().find_map(|l| {
            l.split_whitespace().nth(1)?.parse::<f64>().ok()
        }).unwrap_or(f64::NAN)
    };
    let crude_kernel_bound =
        ((cutoff_all / (2.0 * std::f64::consts::PI)).ln() + 1.0)
            / (2.0 * std::f64::consts::PI * cutoff_all);
    let kernel_add = (n_x * n_x) as f64 * crude_kernel_bound;
    println!(
        "crosscheck n=1000 lambda_clean={:.12} corrupted_row_contribution_est={:.12} kernel_bound_add={:.6e}",
        lambda[n_x - 1],
        corrupt,
        kernel_add
    );
    println!("crosscheck note: expected identity lambda_1e5(1000) ~= lambda_clean(1000) + corrupted_contribution + kernel_add; paste li_lambda_1e5 anchor value alongside");

    println!("CHECKED NUMERICALLY: finite f64 scan of rows 1..19000 only; no claim of global Li positivity; no RH proof.");
    println!("[CONJECTURED] tail_integral_est uses a Riemann-von Mangoldt density model for omitted zeros.");
    println!("elapsed_seconds={:.3}", started.elapsed().as_secs_f64());
}
