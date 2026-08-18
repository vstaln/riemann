// pf_planted: firewall-resolution measurement for the PF audit.
//
// RH-false planted world: split the first zero pair of Xi into a symmetric off-line
// cluster. In z-space the true world has simple zeros at z = +-gamma_1 (factor
// 1 - z^2/gamma_1^2). The planted world replaces this by the four zeros +-(gamma_1+-i*delta),
// i.e. multiplies Xi by
//   R(z) = (1 - z^2/l^2)(1 - z^2/lbar^2) / (1 - z^2/gamma_1^2)^2,   l = gamma_1 + i*delta.
// At delta = 0 this is identically 1 (the planted world IS the true world); for delta > 0
// the xi-zeros sit at rho = 1/2 +- delta +- i*gamma_1, off the critical line (honest RH-false).
//
// In w = z^2 coordinates with true coefficients b_k (certified 210-bit table),
//   planted b = b * c  (convolution),  R(w) = A(w)/B(w) = sum c_k w^k,
//   A(w) = 1 - 2 r1 w + r2 w^2,  r1 = (g^2 - d^2)/(g^2 + d^2)^2,  r2 = 1/(g^2+d^2)^2
//   B(w) = (1 - w/g^2)^2
//   c_0 = 1; c_1 = -2 r1 + 2/g^2; c_2 = r2 + (2/g^2) c_1 - 1/g^4;
//   c_k = (2/g^2) c_{k-1} - (1/g^4) c_{k-2}  (k >= 3).
//
// For each delta we run the same certified PF audit (orders 2..8) and record the first
// order at which a certified-negative minor appears. This measures how deep the audit must
// go to detect an RH-false world of displacement delta (the firewall's resolution).
use rug::{ops::Pow, Float};
use std::fs;

const PG: u32 = 210;

fn main() {
    // certified b_k = M_k/(2k)!, k = 0..300
    let txt = fs::read_to_string("/home/vstaln/riemann/research/notes/g02-moments-oracle-2026-08-18.txt")
        .expect("oracle table");
    let mut b: Vec<Float> = Vec::new();
    for line in txt.lines() {
        let line = line.trim();
        if line.is_empty() || line.starts_with('#') || line.starts_with("g0-2") { continue; }
        let cols: Vec<&str> = line.split('\t').collect();
        if cols.len() >= 3 {
            if let Ok(v) = Float::parse_radix(cols[2].trim(), 10) {
                b.push(Float::with_val(PG, v));
            }
        }
    }
    // first zero gamma_1 from the LMFDB cache
    let ztxt = fs::read_to_string("/home/vstaln/riemann/tools/data/zeros_1_1000.txt").expect("zeros");
    let g1: f64 = ztxt.lines().next().unwrap()
        .split_whitespace().nth(1).unwrap().parse().unwrap();
    let g1 = Float::with_val(PG, g1);
    println!("loaded b_k k=0..{}, gamma_1 = {:.12}", b.len() - 1, g1.to_f64());

    // error factor for planted entries: table error (2^-207) + convolution arithmetic (~2^-205)
    let eps_f = Float::with_val(PG, 1) >> 205;
    let factor_f = |r: usize| -> Float {
        let mut base: Float = Float::with_val(PG, 1) + &eps_f;
        base = base.pow(r as u32);
        base - 1
    };

    // certified determinant (same machinery as pf_certified)
    let det_cert = |seq: &Vec<Float>, rows: &[usize], cols: &[usize]| -> (Float, Float) {
        let r = rows.len();
        let mut vals: Vec<Float> = Vec::with_capacity(r * r);
        for i in 0..r {
            for j in 0..r {
                let idx = rows[i] as i64 - cols[j] as i64;
                let v = if idx < 0 { Float::with_val(PG, 0) } else { seq[idx as usize].clone() };
                vals.push(v);
            }
        }
        let mut perm: Vec<usize> = (0..r).collect();
        let mut det = Float::with_val(PG, 0);
        let mut sum_abs = Float::with_val(PG, 0);
        let mut expect = 1u128;
        for i in 1..=r { expect *= i as u128; }
        let mut count = 0u64;
        loop {
            let mut sign = 1i64;
            let mut inv = 0;
            for a in 0..r { for c in a + 1..r { if perm[a] > perm[c] { inv += 1; } } }
            if inv % 2 == 1 { sign = -1; }
            let mut term = Float::with_val(PG, 1);
            for i in 0..r { term *= &vals[i * r + perm[i]]; }
            sum_abs += term.clone().abs();
            if sign > 0 { det += term; } else { det -= term; }
            count += 1;
            let mut k = r - 1;
            while k > 0 && perm[k - 1] >= perm[k] { k -= 1; }
            if k == 0 { break; }
            let mut l = r - 1;
            while perm[l] <= perm[k - 1] { l -= 1; }
            perm.swap(k - 1, l);
            perm[k..].reverse();
        }
        assert_eq!(count as u128, expect, "perm count r={}", r);
        let err = sum_abs * factor_f(r);
        (det, err)
    };

    // For each delta: build planted b (first 24 coefficients), run certified PF 2..8,
    // report the first failing order and the most negative certified minor.
    println!("\n{:<10} | {} | {} | {}",
             "delta", "first fail", "worst minor", "notes");
    println!("{:-<10}-+-{:-<50}-+-{:-<12}-+-{:-<40}", "", "", "", "");
    for delta in [1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 0.0] {
        let d = Float::with_val(PG, delta);
        let g2 = Float::with_val(PG, &g1 * &g1);          // gamma_1^2
        let d2 = Float::with_val(PG, &d * &d);
        let gd2 = Float::with_val(PG, &g2 + &d2);         // g^2 + d^2
        let gd4 = Float::with_val(PG, &gd2 * &gd2);
        let r1 = Float::with_val(PG, &g2 - &d2) / &gd4;
        let r2 = Float::with_val(PG, 1) / &gd4;
        let b1 = Float::with_val(PG, 1) / &g2;            // 1/g^2
        let b1sq = Float::with_val(PG, &b1 * &b1);
        // correction series c_0..c_23
        let mut c: Vec<Float> = Vec::with_capacity(24);
        c.push(Float::with_val(PG, 1));
        c.push(Float::with_val(PG, -2.0) * &r1 + Float::with_val(PG, 2.0) * &b1);
        c.push(&r2 + Float::with_val(PG, 2.0) * &b1 * &c[1] - &b1sq);
        for k in 3..24 {
            let v = Float::with_val(PG, 2.0) * &b1 * &c[k - 1] - &b1sq * &c[k - 2];
            c.push(v);
        }
        // planted b_tilde_k = sum_{j=0}^{k} b_j c_{k-j}, k = 0..23
        let mut btilde: Vec<Float> = Vec::with_capacity(24);
        for k in 0..24 {
            let mut s = Float::with_val(PG, 0);
            for j in 0..=k {
                s += &b[j] * &c[k - j];
            }
            btilde.push(s);
        }
        // certified PF audit orders 2..8 on the planted world
        let mut first_fail: Option<usize> = None;
        let mut worst: f64 = 0.0;
        let mut worst_spec = String::new();
        'outer: for r in 2..=8usize {
            let win = if r <= 6 { 16 } else { 10 };
            for s in 0..=(win - r) {
                for c0 in 0..=(win - r) {
                    let rows: Vec<usize> = (s + 1..=s + r).collect();
                    let cols: Vec<usize> = (c0..c0 + r).collect();
                    let (dv, ev) = det_cert(&btilde, &rows, &cols);
                    let negev = Float::with_val(PG, -&ev);
                    if dv < negev {
                        if first_fail.is_none() { first_fail = Some(r); }
                        if dv.to_f64() < worst {
                            worst = dv.to_f64();
                            worst_spec = format!("{}x{} rows({:?}) cols({:?})", r, r, rows, cols);
                        }
                        if r >= 3 { break 'outer; } // enough evidence; record only lowest order
                    }
                }
            }
        }
        let ff = match first_fail {
            Some(r) => format!("PF{}", r),
            None => "none (<=8)".to_string(),
        };
        let note = if delta == 0.0 { "control: true world (delta=0, must pass)" } else { "" };
        println!("{:<10} | {:<50} | {:<12.3e} | {}", format!("{:.0e}", delta), ff, worst, note);
    }

    // Also run a finer sweep recording the failure order vs delta explicitly
    println!("\nFailure order vs delta (first certified-negative PF order):");
    println!("  delta        first failing order");
    for delta in [5e-2, 2e-2, 1e-2, 5e-3, 2e-3, 1e-3, 5e-4, 2e-4, 1e-4, 5e-5, 1e-5] {
        let d = Float::with_val(PG, delta);
        let g2 = Float::with_val(PG, &g1 * &g1);
        let d2 = Float::with_val(PG, &d * &d);
        let gd2 = Float::with_val(PG, &g2 + &d2);
        let gd4 = Float::with_val(PG, &gd2 * &gd2);
        let r1 = Float::with_val(PG, &g2 - &d2) / &gd4;
        let r2 = Float::with_val(PG, 1) / &gd4;
        let b1 = Float::with_val(PG, 1) / &g2;
        let b1sq = Float::with_val(PG, &b1 * &b1);
        let mut c: Vec<Float> = Vec::with_capacity(24);
        c.push(Float::with_val(PG, 1));
        c.push(Float::with_val(PG, -2.0) * &r1 + Float::with_val(PG, 2.0) * &b1);
        c.push(&r2 + Float::with_val(PG, 2.0) * &b1 * &c[1] - &b1sq);
        for k in 3..24 { c.push(Float::with_val(PG, 2.0) * &b1 * &c[k - 1] - &b1sq * &c[k - 2]); }
        let mut btilde: Vec<Float> = Vec::with_capacity(24);
        for k in 0..24 {
            let mut s = Float::with_val(PG, 0);
            for j in 0..=k { s += &b[j] * &c[k - j]; }
            btilde.push(s);
        }
        let mut first_fail: Option<usize> = None;
        let mut worst: f64 = 0.0;
        'outer: for r in 2..=8usize {
            let win = if r <= 6 { 16 } else { 10 };
            for s in 0..=(win - r) {
                for c0 in 0..=(win - r) {
                    let rows: Vec<usize> = (s + 1..=s + r).collect();
                    let cols: Vec<usize> = (c0..c0 + r).collect();
                    let (dv, ev) = det_cert(&btilde, &rows, &cols);
                    let negev = Float::with_val(PG, -&ev);
                    if dv < negev {
                        if first_fail.is_none() {
                            first_fail = Some(r);
                            worst = dv.to_f64();
                        }
                        if r >= 3 { break 'outer; }
                    }
                }
            }
        }
        match first_fail {
            Some(r) => println!("  {:>9.0e}   PF{}  (worst minor {:.2e})", delta, r, worst),
            None => println!("  {:>9.0e}   none up to PF8", delta),
        }
    }
    println!("\nInterpretation: the smallest certified-detected displacement and the depth needed");
    println!("quantify the firewall — for any fixed audit depth there are RH-false worlds that pass.");
}
