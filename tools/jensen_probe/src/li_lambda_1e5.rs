// Bounded f64 scan of the spectral Li formula through n=100000.
// Values are numerical probes, not a proof of Li positivity or RH.

use std::fs;
use std::path::PathBuf;
use std::sync::Arc;
use std::thread;
use std::time::Instant;

const N_MAX: usize = 100_000;
const LANES: usize = 8;

fn load_all_gammas(path: &str) -> Vec<f64> {
    let text = fs::read_to_string(PathBuf::from(path))
        .unwrap_or_else(|e| panic!("cannot read zeros file {path}: {e}"));
    text.lines()
        .filter_map(|line| {
            let line = line.trim();
            if !line.chars().next().is_some_and(|c| c.is_ascii_digit()) {
                return None;
            }
            let mut fields = line.split_whitespace();
            let first = fields.next()?;
            fields.next().unwrap_or(first).parse::<f64>().ok()
        })
        .collect()
}

// Eight independent complex phasor recurrences expose enough instruction-level
// parallelism for this bounded O(N*J) scan and use the validated engine's
// update formula exactly.
fn spectral_sum(gammas: &[f64], n_max: usize) -> Vec<f64> {
    let workers = thread::available_parallelism()
        .map_or(1, usize::from)
        .min(16);
    let blocks = gammas.len().div_ceil(LANES);
    let blocks_per_worker = blocks.div_ceil(workers);
    let gammas = Arc::new(gammas.to_vec());
    let mut handles = Vec::new();

    for worker in 0..workers {
        let first_block = worker * blocks_per_worker;
        let end_block = ((worker + 1) * blocks_per_worker).min(blocks);
        if first_block >= end_block {
            continue;
        }
        let gammas = Arc::clone(&gammas);
        handles.push(thread::spawn(move || {
            let mut sums = vec![0.0f64; n_max];
            for block in first_block..end_block {
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
        }));
    }

    let mut total = vec![0.0f64; n_max];
    for handle in handles {
        let partial = handle.join().expect("spectral worker panicked");
        for (total_n, partial_n) in total.iter_mut().zip(partial) {
            *total_n += partial_n;
        }
    }
    total
}

fn main() {
    let path = "/home/vstaln/riemann/tools/data/zeros_rust_100k.txt";
    let gammas = load_all_gammas(path);
    assert!(!gammas.is_empty(), "zero data must not be empty");
    let cutoff = *gammas.last().unwrap();
    let started = Instant::now();
    let mut lambda = spectral_sum(&gammas, N_MAX);

    // Riemann-von Mangoldt-density tail model used by li_lambda_spectral.
    // It is also n^2 times the asymptotic estimate of
    // sum_{gamma>T} 4/(4 gamma^2+1).
    let crude_kernel_bound = ((cutoff / (2.0 * std::f64::consts::PI)).ln() + 1.0)
        / (2.0 * std::f64::consts::PI * cutoff);
    for (index, value) in lambda.iter_mut().enumerate() {
        let n = (index + 1) as f64;
        *value += n * n * crude_kernel_bound;
    }

    let (min_index, min_value) = lambda
        .iter()
        .enumerate()
        .min_by(|a, b| a.1.total_cmp(b.1))
        .unwrap();
    let first_negative = lambda.iter().position(|&x| x < 0.0).map(|i| i + 1);

    println!(
        "li_lambda_1e5 n_max={N_MAX} J={} gamma_cutoff={cutoff:.12}",
        gammas.len()
    );
    println!("data note: the supplied file ends near {cutoff:.1}, not 500000; all loaded zeros were used");
    println!(
        "real global_min n={} lambda={:.12}",
        min_index + 1,
        min_value
    );
    println!(
        "real first_negative={}",
        first_negative.map_or_else(|| "NONE".into(), |n| n.to_string())
    );
    for n in [1000usize, 5000, 5155, 5156, 10000, 100000] {
        println!("real anchor n={n} lambda={:.12}", lambda[n - 1]);
    }

    // Functional-equation quadruplet generated by rho=beta+i*gamma:
    // z1=1-1/rho and z3=1/z1. Its exact contribution is
    // 4 - 2 Re(z1^n) - 2 Re(z3^n).
    let beta = 0.85f64;
    let gamma = 14.13472514f64;
    let denominator = beta * beta + gamma * gamma;
    let z1 = (
        ((beta - 1.0) * beta + gamma * gamma) / denominator,
        gamma / denominator,
    );
    let z1_norm2 = z1.0 * z1.0 + z1.1 * z1.1;
    let z3 = (z1.0 / z1_norm2, -z1.1 / z1_norm2);
    let mut p1 = (1.0f64, 0.0f64);
    let mut p3 = (1.0f64, 0.0f64);
    let mut first_plant_negative = None;
    let mut last_plant_nonnegative = None;
    let mut plant_anchors = Vec::new();
    for n in 1..=N_MAX {
        p1 = (p1.0 * z1.0 - p1.1 * z1.1, p1.0 * z1.1 + p1.1 * z1.0);
        p3 = (p3.0 * z3.0 - p3.1 * z3.1, p3.0 * z3.1 + p3.1 * z3.0);
        let planted = lambda[n - 1] + 4.0 - 2.0 * p1.0 - 2.0 * p3.0;
        if planted < 0.0 && first_plant_negative.is_none() {
            first_plant_negative = Some(n);
        }
        if planted >= 0.0 {
            last_plant_nonnegative = Some(n);
        }
        if matches!(n, 5155 | 5156 | 100000) {
            plant_anchors.push((n, planted));
        }
    }
    println!(
        "plant beta={beta} gamma={gamma} |z_growing|={:.12}",
        z3.0.hypot(z3.1)
    );
    println!(
        "plant first_negative={}",
        first_plant_negative.map_or_else(|| "NONE".into(), |n| n.to_string())
    );
    for (n, value) in plant_anchors {
        println!("plant anchor n={n} lambda={value:.12}");
    }
    match last_plant_nonnegative {
        Some(N_MAX) => println!(
            "plant permanently_negative_suffix=NONE (value is nonnegative again at n={N_MAX})"
        ),
        Some(n) => println!(
            "plant permanently_negative_suffix_through_scan={} (finite-range statement only)",
            n + 1
        ),
        None => println!(
            "plant permanently_negative_suffix_through_scan=1 (finite-range statement only)"
        ),
    }

    println!("omitted_zero_count=INFINITE (the data set is finite; exact ordinates beyond cutoff are not loaded)");
    println!("[CONJECTURED] Riemann-von Mangoldt-density estimate sum_{{gamma>T}} 4/(4gamma^2+1) ~= {crude_kernel_bound:.12e}");
    println!("[CONJECTURED] using |sin(n theta)| <= n|sin(theta)| gives omitted on-line tail magnitude <= n^2 times that estimate; at n={N_MAX}: {:.12}", (N_MAX as f64).powi(2) * crude_kernel_bound);
    println!("CHECKED NUMERICALLY: finite f64 scan only; no claim that lambda_n >= 0 globally and no RH proof.");
    println!("elapsed_seconds={:.3}", started.elapsed().as_secs_f64());
}
