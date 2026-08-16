// S2-PNT discriminator probe (v2) — the prime-counting side.
//
// ψ(x) − x via the classical explicit formula with the campaign's cached zeros
// (tools/data/zeros_rust_924k.txt: 924,715 zeros, γ ≤ 559999.733; 8A-certified on-line).
//
//   ψ(x) − x = −Σ_ρ x^ρ/ρ − log(2π) − ½·log(1 − x^{−2})      (x > 1, non-integer)
// pair-summed over positive γ (ρ = ½+iγ, ρ̄ = ½−iγ):
//   Σ_ρ x^ρ/ρ = 2√x · Σ_{γ>0} [ ½·cos(γt) + γ·sin(γt) ] / (γ² + ¼),   t = log x
//
// Planted-zero controls (8A pattern): remove the on-line pair at γ₁ = 14.134725…
// and plant (β, γ₁) and (1−β, γ₁) — conjugate + FE-symmetric fake ξ'.
//   off-line pair term: 2·x^β·[ β·cos(γt) + γ·sin(γt) ] / (β² + γ²)
//
// v2: grid extended to x = 3×10^11 (T = 5.6×10^5 suffices per the brief; truncation
// columns certify), three control strengths β ∈ {0.6, 0.65, 0.7}, and an effective
// growth exponent δ = d(ln E)/d(ln x) per case (discriminator signature).

use std::fs::File;
use std::io::{BufRead, BufReader};

fn load_zeros(path: &str) -> Vec<f64> {
    let f = File::open(path).expect("open zeros");
    BufReader::new(f)
        .lines()
        .map(|l| l.unwrap().trim().parse::<f64>().unwrap())
        .collect()
}

#[inline]
fn on_line(g: f64, t: f64, sqrtx: f64) -> f64 {
    let (s, c) = (g * t).sin_cos();
    2.0 * sqrtx * (0.5 * c + g * s) / (g * g + 0.25)
}

#[inline]
fn off_line(beta: f64, g: f64, t: f64, xb: f64) -> f64 {
    let (s, c) = (g * t).sin_cos();
    2.0 * xb * (beta * c + g * s) / (beta * beta + g * g)
}

const G1: f64 = 14.134725141735;

/// ψ(x) − x via the truncated explicit formula (first `n` positive zeros).
/// `control` = Some(β) plants (β,γ₁)+(1−β,γ₁) and removes the on-line γ₁ pair.
fn psi_minus_x(x: f64, zeros: &[f64], n: usize, control: Option<f64>) -> f64 {
    let t = x.ln();
    let sqrtx = x.sqrt();
    let mut s = 0.0f64;
    for &g in &zeros[..n] {
        if control.is_some() && (g - G1).abs() < 1e-6 {
            continue; // removed on-line pair
        }
        s += on_line(g, t, sqrtx);
    }
    if let Some(b) = control {
        s += off_line(b, G1, t, x.powf(b));
        s += off_line(1.0 - b, G1, t, x.powf(1.0 - b));
    }
    let log2pi = (2.0 * std::f64::consts::PI).ln();
    let small = 0.5 * (1.0 - 1.0 / (x * x)).ln();
    -s - log2pi - small
}

/// Direct sieve evaluation of ψ(x) = Σ_{n≤x} Λ(n) — independent validation.
fn psi_sieve(x: f64) -> f64 {
    let n = x as usize;
    let mut lam = vec![0.0f64; n + 1];
    let mut is_comp = vec![false; n + 1];
    for p in 2..=n {
        if !is_comp[p] {
            let lp = (p as f64).ln();
            let mut j = p;
            while j <= n {
                lam[j] += lp;
                if j > n / p {
                    break;
                }
                j *= p;
            }
        }
        let mut m = p * p;
        while m <= n {
            is_comp[m] = true;
            m += p;
        }
    }
    lam[2..=n].iter().sum()
}

/// slope of ln(E) vs ln(x) over slice [lo, hi) — effective growth exponent of the envelope.
fn slope_lnE_lnx(xs: &[f64], es: &[f64], lo: usize, hi: usize) -> f64 {
    let mut sx = 0.0;
    let mut sy = 0.0;
    let mut sxx = 0.0;
    let mut sxy = 0.0;
    let mut cnt = 0.0;
    for i in lo..hi {
        let u = xs[i].ln();
        let v = es[i].ln();
        sx += u;
        sy += v;
        sxx += u * u;
        sxy += u * v;
        cnt += 1.0;
    }
    (cnt * sxy - sx * sy) / (cnt * sxx - sx * sx)
}

fn main() {
    let zeros = load_zeros("tools/data/zeros_rust_924k.txt");
    let nfull = zeros.len();
    let n462k = 462_000;
    let n100k = 100_000;
    println!("zeros loaded: {} (max γ {:.3})", nfull, zeros[nfull - 1]);

    // ---- Validation anchors: explicit formula vs direct sieve ----
    println!("\n# anchor x | explicit ψ | sieve ψ | |diff|");
    for &x in &[10.0f64, 100.0, 1000.0, 10000.0, 100000.0] {
        let ef = psi_minus_x(x, &zeros, nfull, None) + x;
        let sv = psi_sieve(x);
        println!(
            "anchor x={:.0}  explicit_psi={:.6}  sieve_psi={:.6}  diff={:.2e}",
            x, ef, sv, (ef - sv).abs()
        );
    }

    // ---- Grid: 72 log-spaced points, x ∈ [10^3, 3×10^11] ----
    let npts = 72;
    let lo = 3.0f64;
    let hi = 11.4771f64; // log10(3e11)
    let mut xs: Vec<f64> = Vec::with_capacity(npts);
    for i in 0..npts {
        let lx = lo + (hi - lo) * i as f64 / (npts - 1) as f64;
        xs.push(10f64.powf(lx));
    }

    let betas = [0.6f64, 0.65, 0.7];

    let mut env_real = vec![0.0f64; npts];
    let mut r_full = vec![0.0f64; npts];
    let mut trunc_462 = vec![0.0f64; npts];
    let mut trunc_100 = vec![0.0f64; npts];
    let mut env_ctrl: Vec<Vec<f64>> = vec![vec![0.0f64; npts]; betas.len()];
    let mut c_full: Vec<Vec<f64>> = vec![vec![0.0f64; npts]; betas.len()];

    let mut er = 0.0f64;
    let mut ec = vec![0.0f64; betas.len()];
    for (i, &x) in xs.iter().enumerate() {
        let rf = psi_minus_x(x, &zeros, nfull, None);
        let r4 = psi_minus_x(x, &zeros, n462k, None);
        let r1 = psi_minus_x(x, &zeros, n100k, None);
        r_full[i] = rf;
        trunc_462[i] = (rf - r4).abs();
        trunc_100[i] = (rf - r1).abs();
        er = er.max(rf.abs() / x.sqrt());
        env_real[i] = er;
        for (k, &b) in betas.iter().enumerate() {
            let cf = psi_minus_x(x, &zeros, nfull, Some(b));
            c_full[k][i] = cf;
            ec[k] = ec[k].max(cf.abs() / x.sqrt());
            env_ctrl[k][i] = ec[k];
        }
    }

    // ---- Output: real table ----
    println!("\n# REAL: x  psi-x  |psi-x|/sqrtx  env  logx  sqrtlogx  env/logx  env/sqrtlogx  trunc462  trunc100");
    for i in 0..npts {
        let x = xs[i];
        let lx = x.ln();
        let s = lx.sqrt();
        println!(
            "{:.6e}  {:.6e}  {:.6e}  {:.6e}  {:.4}  {:.4}  {:.6e}  {:.6e}  {:.2e}  {:.2e}",
            x, r_full[i], r_full[i].abs() / x.sqrt(), env_real[i], lx, s,
            env_real[i] / lx, env_real[i] / s, trunc_462[i], trunc_100[i]
        );
    }

    // ---- Output: control tables ----
    for (k, &b) in betas.iter().enumerate() {
        println!(
            "\n# CONTROL β={}: x  psi-x  |psi-x|/sqrtx  env  env/logx  env/sqrtlogx",
            b
        );
        for i in 0..npts {
            let x = xs[i];
            let lx = x.ln();
            let s = lx.sqrt();
            println!(
                "{:.6e}  {:.6e}  {:.6e}  {:.6e}  {:.6e}  {:.6e}",
                x, c_full[k][i], c_full[k][i].abs() / x.sqrt(), env_ctrl[k][i],
                env_ctrl[k][i] / lx, env_ctrl[k][i] / s
            );
        }
    }

    // ---- Effective growth exponent δ = d(ln E)/d(ln x) over the top half ----
    let lo_fit = npts / 2;
    let d_real = slope_lnE_lnx(&xs, &env_real, lo_fit, npts);
    println!("\n# effective growth exponent δ = slope of ln(E) vs ln(x), points {}..{}", lo_fit, npts);
    println!("REAL   δ = {:.4}", d_real);
    for (k, &b) in betas.iter().enumerate() {
        let d = slope_lnE_lnx(&xs, &env_ctrl[k], lo_fit, npts);
        println!("CTRL β={}  δ = {:.4}   (expected β−1/2 = {:.2})", b, d, b - 0.5);
    }

    // ---- Band verdicts ----
    println!("\n# verdicts (band sqrtx-log^(1/2) fires when env/sqrtlogx > 1; band sqrtx-log when env/logx > 1)");
    let mut max_r_half = 0.0f64;
    let mut max_r_one = 0.0f64;
    for i in 0..npts {
        let lx = xs[i].ln();
        max_r_half = max_r_half.max(env_real[i] / lx.sqrt());
        max_r_one = max_r_one.max(env_real[i] / lx);
    }
    println!(
        "REAL: max env/√(log x) = {:.4} (must be < 1 for the √x(log x)^(1/2) band)  |  max env/log x = {:.4} (√x log x band)",
        max_r_half, max_r_one
    );
    for (k, &b) in betas.iter().enumerate() {
        let mut mx = 0.0f64;
        let mut fire_x = -1.0f64;
        for i in 0..npts {
            let r = env_ctrl[k][i] / xs[i].ln().sqrt();
            mx = mx.max(r);
            if r > 1.0 && fire_x < 0.0 {
                fire_x = xs[i];
            }
        }
        println!(
            "CTRL β={}: max env/√(log x) = {:.4} | first x where env exceeds √x(log x)^(1/2) band: {}",
            b,
            mx,
            if fire_x > 0.0 { format!("{:.3e}", fire_x) } else { "NEVER (in range)".to_string() }
        );
    }

    // ---- Truncation summary ----
    let (mut m462, mut m100) = (0.0f64, 0.0f64);
    let (mut ix462, mut ix100) = (0usize, 0usize);
    for i in 0..npts {
        if trunc_462[i] > m462 {
            m462 = trunc_462[i];
            ix462 = i;
        }
        if trunc_100[i] > m100 {
            m100 = trunc_100[i];
            ix100 = i;
        }
    }
    println!(
        "\n# truncation: max |full − 462k| = {:.3e} at x = {:.3e} (E-units {:.3e})",
        m462, xs[ix462], m462 / xs[ix462].sqrt()
    );
    println!(
        "# truncation: max |full − 100k| = {:.3e} at x = {:.3e} (E-units {:.3e})",
        m100, xs[ix100], m100 / xs[ix100].sqrt()
    );
}
