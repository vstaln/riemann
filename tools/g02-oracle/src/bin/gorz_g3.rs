// GORTTW Theorem 2.1(2) second-order verification on certified coefficients.
//
// GORTTW (arXiv 1910.01227) Thm 2.1(2): for gamma(n) = 8 n! b_n (their convention),
//   log(gamma(M-j)/gamma(M)) = -sum_{m>=1} G_m(M) Delta(M)^{2m-2} j^m
// with Delta(M) = sqrt( 1/2 * (1 - gamma(M-2)gamma(M)/gamma(M-1)^2) )  (their (2.3))
// and lim_{M->oo} G_m(M) = 2^{m-1}/(m(m-1))  (so G_3 -> 4/6 = 2/3).
//
// Extraction: fit the cubic in j from 4 consecutive log-ratios:
//   L_j := log(gamma(M-j)/gamma(M)) = -a1 j - a2 Delta^2 j^2 - a3 Delta^4 j^3 - ...
// so G_m = a_m. With Delta(M) ~ 1/sqrt(2M) -> 0, the cubic coefficient a3 ~ G3 Delta^4.
// Because Delta^4 is tiny, we instead verify the SCALED prediction:
//   a3 / Delta^4 -> 2/3   and   a2 / Delta^2 -> G2 -> 1  (G2(M) -> 1; their (2.5) gives G2 = 1 + O(Delta^2)).
//
// Work with ratios at 210 bits (f64-safe: b_k spans 1e-500..1e111).

use rug::Float;
use std::fs;

const PREC: u32 = 210;

fn main() {
    let txt = fs::read_to_string(
        "/home/vstaln/riemann/research/notes/g02-moments-oracle-2026-08-18.txt",
    )
    .expect("read table");
    let mut b: Vec<Float> = Vec::new();
    for line in txt.lines() {
        let line = line.trim();
        if line.is_empty() || line.starts_with('#') || line.starts_with("g0-2") {
            continue;
        }
        let cols: Vec<&str> = line.split('\t').collect();
        if cols.len() >= 3 {
            if let Ok(v) = Float::parse_radix(cols[2].trim(), 10) {
                b.push(Float::with_val(PREC, v));
            }
        }
    }
    println!("loaded b_k k=0..{}", b.len() - 1);

    // log gamma(n) = ln 8 + ln n! + ln b_n  (ln 8 cancels in ratios but keep for clarity)
    let mut lnfact = vec![0.0f64; 301];
    for i in 2..=300 {
        lnfact[i] = lnfact[i - 1] + (i as f64).ln();
    }
    let ln_b = |n: usize| -> f64 { b[n].clone().ln().to_f64() };
    let log_gamma = |n: usize| -> f64 { (8.0f64).ln() + lnfact[n] + ln_b(n) };

    // Delta(M)^2 = 1/2 (1 - gamma(M-2) gamma(M) / gamma(M-1)^2) via log-differences:
    // log[gamma(M-2)gamma(M)/gamma(M-1)^2] = lg(M-2) + lg(M) - 2 lg(M-1)
    let delta2 = |m: usize| -> f64 {
        let x = log_gamma(m - 2) + log_gamma(m) - 2.0 * log_gamma(m - 1);
        0.5 * (1.0 - x.exp())
    };

    // L_j = log gamma(M-j)/gamma(M); fit L_j = -a1 j - a2 D^2 j^2 - a3 D^4 j^3 for j=1..4
    // Solve the 4x4 Vandermonde-ish linear system exactly from the 4 values.
    let fit_cubic = |m: usize| -> (f64, f64, f64, f64) {
        let l = |j: usize| -> f64 { log_gamma(m - j) - log_gamma(m) };
        let l1 = l(1);
        let l2 = l(2);
        let l3 = l(3);
        let l4 = l(4);
        // L_j = -a1 j - a2 D^2 j^2 - a3 D^4 j^3. Let A1 = a1, A2 = a2 D^2, A3 = a3 D^4.
        // System (A1, A2, A3):
        //   l1 = -A1 - A2 - A3
        //   l2 = -2A1 - 4A2 - 8A3
        //   l3 = -3A1 - 9A2 - 27A3
        // Solve:
        // From l2 - 2*l1 = -2A2 - 6A3 ; l3 - 3*l1 = -6A2 - 24A3
        // Let B = l2 - 2l1, C = l3 - 3l1:
        //   B = -2A2 - 6A3 ; C = -6A2 - 24A3
        // 3B = -6A2 - 18A3 ; C - 3B = -6A3  =>  A3 = (3B - C)/6
        // A2 = (-B - 6A3)/2... from B = -2A2 - 6A3: A2 = -(B + 6A3)/2
        // A1 = -l1 - A2 - A3
        let b1 = l2 - 2.0 * l1;
        let c1 = l3 - 3.0 * l1;
        let a3 = (3.0 * b1 - c1) / 6.0;
        let a2 = -(b1 + 6.0 * a3) / 2.0;
        let a1 = -l1 - a2 - a3;
        // use l4 as a residual check: predicted l4' = -4A1 - 16A2 - 64A3
        let l4p = -4.0 * a1 - 16.0 * a2 - 64.0 * a3;
        (a1, a2, a3, (l4p - l4).abs())
    };

    println!(
        "\n{:>5} | {:>10} {:>12} {:>12} {:>12} {:>12} {:>10} | {:>10}",
        "M", "Delta", "G1=a1", "G2=a2/D^2", "G3=a3/D^4", "G3*Delta^4", "fit resid", "a4-cubic"
    );
    for &m in &[40usize, 60, 80, 100, 150, 200, 250, 299] {
        if m + 2 > 299 {
            continue;
        }
        let d2 = delta2(m);
        let d = d2.max(0.0).sqrt();
        let (a1, a2, a3, res) = fit_cubic(m);
        let g2 = a2 / d2;
        let g3 = a3 / (d2 * d2);
        // GORTTW (2.5): G2(M) = 1 + (1 - 3*G3(M))*Delta^2 + O(Delta^4). Cross-check:
        let g2_pred = 1.0 + (1.0 - 3.0 * g3) * d2;
        println!(
            "{:5} | {:10.5} {:12.6} {:12.6} {:12.6} {:12.3e} {:10.1e} | {:10.6} {:10.2e}",
            m, d, a1, g2, g3, a3, res, g2_pred, (g2 - g2_pred).abs()
        );
    }
    println!(
        "\n{:>5} | {:>10} {:>12} {:>12} {:>12} {:>12} {:>10} | {:>10} {:>10}",
        "M", "Delta", "G1=a1", "G2=a2/D^2", "G3=a3/D^4", "G3*Delta^4", "fit resid", "G2_pred(2.5)", "|G2-G2pred|"
    );
    println!(
        "\n(GORTTW Thm 2.1(2) predictions: G2(M) -> 1 (their (2.5): G2 = 1 + O(Delta^2));\n G3(M) -> 2^(3-1)/(3*2) = 2/3. The cubic-coefficient test a3/Delta^4 -> 2/3 is the\n second-order content. Caveat: Delta^4 ~ 1/(4M^2) is tiny; G3 extraction is numerically\n delicate at small M. fit residual = |predicted l4 - actual l4| tests the cubic model.)"
    );

    // ---- extend to large M via GORTTW (3.2) saddle-point formula ----------------
    // gamma(M) = e^{M-2} M^{M+1/2} L_{2M-2}^{2M-2} / (2^{2M-5} (2M-2)^{2M-3/2})
    //            * sqrt(2 pi / K_{2M-2}) * exp(L_{2M-2}/4 - (2M-2)/L_{2M-2} + 3/4)
    //            * (1 + O_eps(1/M^{1-eps}))
    // with L_M the unique positive solution of M = L_M (pi e^{L_M} + 3/4),
    // K_M = (L_M^{-1} + L_M^{-2}) M - 3/4.
    let lm = |m: f64| -> f64 {
        // solve m = L (pi e^L + 3/4) by Newton; init L = log(m/pi)
        let mut l = (m / std::f64::consts::PI).ln().max(1.0);
        for _ in 0..200 {
            let f = l * (std::f64::consts::PI * l.exp() + 0.75) - m;
            let fp = std::f64::consts::PI * l.exp() * (l + 1.0) + 0.75;
            let d = f / fp;
            l -= d;
            if d.abs() < 1e-15 {
                break;
            }
        }
        l
    };
    let log_gamma_saddle = |m: f64| -> f64 {
        let l = lm(2.0 * m - 2.0);
        let k = (1.0 / l + 1.0 / (l * l)) * (2.0 * m - 2.0) - 0.75;
        (m - 2.0) + (m + 0.5) * m.ln() + (2.0 * m - 2.0) * l.ln()
            - ((2.0 * m - 5.0) * (2.0f64).ln() + (2.0 * m - 1.5) * (2.0 * m - 2.0).ln())
            + 0.5 * (2.0 * std::f64::consts::PI / k).ln()
            + l / 4.0 - (2.0 * m - 2.0) / l + 0.75
    };
    let delta2_saddle = |m: usize| -> f64 {
        let mf = m as f64;
        let x = log_gamma_saddle(mf - 2.0) + log_gamma_saddle(mf) - 2.0 * log_gamma_saddle(mf - 1.0);
        0.5 * (1.0 - x.exp())
    };
    let fit_cubic_saddle = |m: usize| -> (f64, f64, f64, f64) {
        let l = |j: usize| -> f64 { log_gamma_saddle(m as f64 - j as f64) - log_gamma_saddle(m as f64) };
        let l1 = l(1);
        let l2 = l(2);
        let l3 = l(3);
        let l4 = l(4);
        let b1 = l2 - 2.0 * l1;
        let c1 = l3 - 3.0 * l1;
        let a3 = (3.0 * b1 - c1) / 6.0;
        let a2 = -(b1 + 6.0 * a3) / 2.0;
        let a1 = -l1 - a2 - a3;
        let l4p = -4.0 * a1 - 16.0 * a2 - 64.0 * a3;
        (a1, a2, a3, (l4p - l4).abs())
    };
    println!("\n=== Large-M check via GORTTW (3.2) saddle-point gamma (their own asymptotic) ===");
    println!("{:>8} | {:>10} {:>12} {:>12} {:>12} {:>10}", "M", "Delta", "G2=a2/D^2", "G3=a3/D^4", "G3-2/3", "fit resid");
    for &m in &[1000usize, 5000, 10000, 50000, 100000, 500000, 1000000] {
        let d2 = delta2_saddle(m);
        let (_, a2, a3, res) = fit_cubic_saddle(m);
        let g2 = a2 / d2;
        let g3 = a3 / (d2 * d2);
        println!(
            "{:8} | {:10.6} {:12.6} {:12.6} {:12.3e} {:10.1e}",
            m, d2.sqrt(), g2, g3, g3 - 2.0 / 3.0, res
        );
    }
    println!(
        "(Prediction: G3 -> 2/3 as M -> oo. Note (3.2) has a 1/M^(1-eps) error; this tests the\n limit prediction at large M using their own asymptotic formula for gamma.)"
    );
}
