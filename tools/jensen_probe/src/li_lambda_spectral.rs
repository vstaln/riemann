// li_lambda_spectral — exact stable Keiper-Li via the spectral phase identity
//
// On-line zero pair: 1 - 1/rho = exp(2*i*theta), theta = arctan(1/(2*gamma))
//   => pair contribution Phi_n(gamma) = 4*sin^2(n*theta)   (PROVEN, real >= 0)
// lambda_n = sum_{j} 4 sin^2(n*theta_j) + tail(n)          (on-line world)
// Planted off-line pair adds exactly: 2 - 2*Re(z^n), z = 1 - 1/(rho_p - 1)
//   |z| = |rho_p - 2| / |rho_p - 1| > 1  for beta0 > 1/2  => dips grow like |z|^n
//
// No binomial-cancellation: pure phasor recurrence, O(N) per n, f64-stable to n >= 10^4.
// Validation: must reproduce li_lambda_real / literature:
//   lambda_1 = 0.023096, lambda_2 = 0.092346, lambda_10 = 2.279340 (N=10k + tail)

use std::env;
use std::fs;
use std::path::PathBuf;

fn parse_arg(args: &[String], flag: &str) -> Option<String> {
    for i in 0..args.len() {
        if args[i] == flag && i + 1 < args.len() { return Some(args[i + 1].clone()); }
        if args[i].starts_with(&format!("{}=", flag)) { return Some(args[i][flag.len() + 1..].to_string()); }
    }
    None
}

fn load_gammas(path: &str, n: usize) -> Vec<f64> {
    let txt = fs::read_to_string(PathBuf::from(path)).unwrap_or_else(|_| {
        for cand in ["tools/data/zeros_rust_100k.txt", "../data/zeros_rust_100k.txt"] {
            if let Ok(t) = fs::read_to_string(cand) { return t; }
        }
        panic!("no zeros file at {}", path);
    });
    let mut out = Vec::with_capacity(n);
    for line in txt.lines() {
        let t = line.trim();
        if t.is_empty() || t.starts_with('#') || !t.chars().next().map_or(false, |c| c.is_ascii_digit()) { continue; }
        let parts: Vec<&str> = t.split_whitespace().collect();
        let g_str = if parts.len() >= 2 { parts[1] } else { parts[0] };
        if let Ok(g) = g_str.parse::<f64>() { out.push(g); if out.len() >= n { break; } }
    }
    out
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let n_max: usize = parse_arg(&args, "--n-max").and_then(|v| v.parse().ok()).unwrap_or(4000);
    let n_zeros: usize = parse_arg(&args, "--zeros-n").and_then(|v| v.parse().ok()).unwrap_or(10000);
    let pb: f64 = parse_arg(&args, "--planted-beta").and_then(|v| v.parse().ok()).unwrap_or(0.85);
    let pg: f64 = parse_arg(&args, "--planted-gamma").and_then(|v| v.parse().ok()).unwrap_or(14.13472514);
    let with_plant = args.iter().any(|a| a == "--planted-beta" || a == "--plant");
    let zpath = parse_arg(&args, "--zeros-file")
        .unwrap_or_else(|| "/home/vstaln/riemann/tools/data/zeros_rust_100k.txt".to_string());

    let gammas = load_gammas(&zpath, n_zeros);
    let g_max = gammas.last().copied().unwrap_or(1.0);
    // spectral phases theta_j = arctan(1/(2 gamma_j))  (PROVEN identity)
    let thetas: Vec<f64> = gammas.iter().map(|&g| (1.0 / (2.0 * g)).atan()).collect();
    // tail: Riemann-von Mangoldt density integral beyond gamma_N
    let tail = |n: usize| (n as f64).powi(2) / (2.0 * std::f64::consts::PI * g_max) * ((g_max / (2.0 * std::f64::consts::PI)).ln() + 1.0);

    // planted phasor z = 1 - 1/(rho_p - 1)
    let (zr, zi) = if with_plant {
        let w_re = pb - 1.0; let w_im = pg; // rho_p - 1
        let d = w_re * w_re + w_im * w_im;
        (1.0 - w_re / d, w_im / d) // 1 - conj(w)/|w|^2 ... 1/w = conj(w)/|w|^2; z = 1 - 1/w
    } else { (0.0, 0.0) };
    let zmod = (zr * zr + zi * zi).sqrt();

    println!("li_lambda_spectral n_max={} zeros={} gamma_max={:.1} plant={} |z|={:.6}",
             n_max, gammas.len(), g_max,
             if with_plant { format!("{}+{}i", pb, pg) } else { "none".into() }, zmod);

    // iterate phasors: e_j^{i n theta_j} via recurrence; z^n via recurrence
    let mut cos_nt: Vec<f64> = vec![1.0; thetas.len()];
    let mut sin_nt: Vec<f64> = vec![0.0; thetas.len()];
    let (mut zc, mut zs) = (1.0f64, 0.0f64);
    let lit: [(usize, f64); 4] = [(1, 0.023096), (2, 0.092346), (3, 0.207639), (10, 2.279340)];
    let mut first_neg = 0usize;
    let mut max_dip = 0.0f64;
    for n in 1..=n_max {
        let nf = n as f64;
        // advance all phasors one step
        let mut lam = 0.0f64;
        for j in 0..thetas.len() {
            let c = cos_nt[j] * thetas[j].cos() - sin_nt[j] * thetas[j].sin();
            let s = cos_nt[j] * thetas[j].sin() + sin_nt[j] * thetas[j].cos();
            cos_nt[j] = c; sin_nt[j] = s;
            lam += 4.0 * s * s; // 4 sin^2(n theta_j)
        }
        lam += tail(n);
        let mut lam_p = lam;
        if with_plant {
            let zc_n = zc; // capture before update
            let zs_n = zs;
            let zc1 = zc * zr - zs * zi;
            let zs1 = zc * zi + zs * zr;
            zc = zc1; zs = zs1;
            let plant_pair = 2.0 - 2.0 * zc_n; // 2 - 2 Re(z^n)
            lam_p = lam + plant_pair;
            if plant_pair < 0.0 && (plant_pair).abs() > max_dip { max_dip = plant_pair.abs(); }
            if lam_p < 0.0 && first_neg == 0 { first_neg = n; }
        }
        if n <= 10 || n == 20 || n == 50 || n == 100 || n % 250 == 0 || (first_neg > 0 && (n - first_neg) < 4) || (lam_p < 0.0) {
            let lit_str = lit.iter().find(|(k, _)| *k == n).map(|(_, v)| format!("{:.6}", v)).unwrap_or("-".into());
            println!("{:>5}  lam={:>14.6}  lit={}  plant_delta={:>14.6}  lam_planted={:>14.6}",
                     n, lam, lit_str,
                     if with_plant { format!("{:.6}", lam_p - lam) } else { "-".into() },
                     if with_plant { format!("{:.6}", lam_p) } else { "-".into() });
        }
    }
    println!("VALIDATION: lambda_1/2/3/10 above must match lit (6dp) => spectral engine {}",
             if !with_plant { "check by eye vs lit column" } else { "(plant run: compare no-plant run)" });
    if with_plant {
        println!("CONTROL: first n with lambda_n(planted) < 0 : {} {}",
                 if first_neg > 0 { format!("n={}", first_neg) } else { "NONE in range".into() },
                 if first_neg > 0 { "=> LI CONTROL FIRES (RH-false world detected)" } else { "(extend range or increase |z| via beta0)" });
        println!("max plant dip magnitude in range: {:.3}", max_dip);
    }
    println!("LABEL: values CHECKED NUMERICALLY; positivity for ALL n remains NOT proven (Li criterion iff RH).");
}
