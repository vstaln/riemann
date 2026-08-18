// GORTTW Thm 2.1 G_m extraction, CLEAN protocol, on the certified 210-bit table.
//
//   log(gamma(M-j)/gamma(M)) = sum_{m>=1} G_m(M) Delta(M)^{2m-2} j^m
//   Delta(M)^2 = 1/2 (1 - gamma(M-2) gamma(M) / gamma(M-1)^2)
//   lim G_m = 2^{m-1}/(m(m-1))   =>  G2 -> 1, G3 -> 2/3, G4 -> 2/3.
//
// Clean protocol: fit the degree-6 polynomial through the EXACT certified
// log-ratios at integer j = 0..6 (includes j=0, so we read the true Taylor
// coefficients at 0; previous fits through j=1..4 were shifted/windowed and
// contaminated).  Certified values are exact 210-bit; do the whole fit in
// Float at 210 bits since c4 ~ Delta^6 is 14 orders below the values.
//
// No quadrature anywhere: gamma at integer n comes straight from the table.

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

    // log gamma(n) = ln 8 + ln n! + ln b_n   (ln 8 cancels in ratios)
    let mut lnfact = vec![Float::with_val(PREC, 0); 301];
    for i in 2..=300 {
        let fi = Float::with_val(PREC, i as f64);
        lnfact[i] = Float::with_val(PREC, &lnfact[i - 1] + fi.ln());
    }
    let ln8 = Float::with_val(PREC, 8.0f64).ln();
    let lg = |n: usize| -> Float {
        let a = Float::with_val(PREC, &ln8 + &lnfact[n]);
        Float::with_val(PREC, a + b[n].clone().ln())
    };

    // Delta(M)^2 via certified values
    let delta2 = |m: usize| -> Float {
        // log[gamma(M-2)gamma(M)/gamma(M-1)^2] = lg(M-2)+lg(M)-2 lg(M-1)
        let s = Float::with_val(PREC, &lg(m - 2) + &lg(m));
        let x = Float::with_val(PREC, s - 2.0 * Float::with_val(PREC, &lg(m - 1)));
        Float::with_val(PREC, (Float::with_val(PREC, 1) - x.exp()) / 2)
    };

    // Degree-6 Newton (forward difference) interpolation through (j, L_j),
    // j = 0..6 (equispaced nodes, h = 1), converted to monomial coefficients
    // c_m:  L_j = c1 j + c2 j^2 + ... + c6 j^6.  L_0 = 0 by definition.
    // Same proven routine as gorz_true_gm.rs (verified exact on test polys).
    let interpolate = |ys: &[Float]| -> Vec<Float> {
        let n = ys.len();
        let mut diff: Vec<Vec<Float>> = vec![ys.to_vec()];
        for k in 1..n {
            let mut row = Vec::new();
            for i in 0..n - k {
                let d = Float::with_val(PREC, &diff[k - 1][i + 1] - &diff[k - 1][i]);
                row.push(d);
            }
            diff.push(row);
        }
        // Horner for Newton basis P(x) = sum_k c_k prod_{i<k}(x - x_i), x_i = i*h (h=1):
        //   mon = c_{n-1};  for k = n-2 .. 0: mon = mon * (x - x_k) + c_k
        let h = 1.0f64;
        let mut mon = vec![Float::with_val(PREC, 0); n];
        for k in (0..n).rev() {
            let mut fact = 1.0;
            for j in 2..=k {
                fact *= j as f64;
            }
            let ck = Float::with_val(PREC, &diff[k][0] / Float::with_val(PREC, fact * h.powi(k as i32)));
            if k < n - 1 {
                let xk = k as f64 * h;
                let mut shifted = vec![Float::with_val(PREC, 0); n];
                for i in 0..n - 1 {
                    shifted[i + 1] += mon[i].clone();
                }
                for i in 0..n {
                    let t = Float::with_val(PREC, &mon[i] * Float::with_val(PREC, xk));
                    shifted[i] = Float::with_val(PREC, &shifted[i] - &t);
                }
                mon = shifted;
            }
            mon[0] = Float::with_val(PREC, &mon[0] + &ck);
        }
        mon
    };
    let fit6 = |m: usize| -> [Float; 7] {
        let n = 7usize;
        let mut ys = Vec::new();
        for j in 0..n {
            ys.push(Float::with_val(PREC, &lg(m - j) - &lg(m)));
        }
        let mon = interpolate(&ys);
        [
            mon[0].clone(), mon[1].clone(), mon[2].clone(), mon[3].clone(),
            mon[4].clone(), mon[5].clone(), mon[6].clone(),
        ]
    };

    println!(
        "{:>6} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12}",
        "M", "Delta^2", "G2", "G3", "G4", "G5", "G6", "c0", "c1"
    );
    for &m in &[60usize, 80, 100, 120, 150, 180, 210, 240, 270, 290] {
        let d2 = delta2(m);
        let d2f = d2.to_f64();
        let c = fit6(m);
        // G_m = c_m / Delta^{2m-2}
        let d_pow = |e: i32| -> Float {
            let mut p = Float::with_val(PREC, 1);
            for _ in 0..e {
                p *= &d2;
            }
            p
        };
        let g2 = Float::with_val(PREC, &c[2] / d_pow(1));
        let g3 = Float::with_val(PREC, &c[3] / d_pow(2));
        let g4 = Float::with_val(PREC, &c[4] / d_pow(3));
        let g5 = Float::with_val(PREC, &c[5] / d_pow(4));
        let g6 = Float::with_val(PREC, &c[6] / d_pow(5));
        println!(
            "{:>6} {:>12.3e} {:>12.7} {:>12.7} {:>12.7} {:>12.7} {:>12.7} {:>12.3e} {:>12.7}",
            m,
            d2f,
            g2.to_f64(),
            g3.to_f64(),
            g4.to_f64(),
            g5.to_f64(),
            g6.to_f64(),
            c[0].to_f64(),
            c[1].to_f64(),
        );
    }
}
