// pf_planted_high: firewall resolution vs zero INDEX.
// The de Bruijn-Newman picture says an RH-false world would first manifest at large height
// (large gamma_k). Displacing zero #k by delta_k changes b_tilde = b * c^{(k)} where
//   R_k(z) = (1 - z^2/l_k^2)(1 - z^2/lbar_k^2) / (1 - z^2/gamma_k^2)^2,  l_k = gamma_k + i*delta_k.
// For fixed delta, a HIGH zero (large gamma_k) contributes a smaller correction to the first
// coefficients (r1 ~ 1/gamma_k^2), so detection should be harder. This probe measures, for
// k in {1, 10, 100}, the smallest delta detected at each PF order — quantifying how blind the
// finite tests are exactly where a realistic disproof would live.
use rug::{ops::Pow, Float};
use std::fs;

const PG: u32 = 210;

fn main() {
    // certified b_k = M_k/(2k)!
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
    // zeros gamma_1..gamma_120 from LMFDB cache (30+ digit precision)
    let ztxt = fs::read_to_string("/home/vstaln/riemann/tools/data/zeros_1_1000.txt").expect("zeros");
    let mut g: Vec<Float> = Vec::new();
    for line in ztxt.lines().take(120) {
        let v: f64 = line.split_whitespace().nth(1).unwrap().parse().unwrap();
        g.push(Float::with_val(PG, v));
    }
    println!("loaded b_k k=0..{}, zeros 1..120 (gamma_100 = {:.6})", b.len() - 1, g[99].to_f64());

    let eps_f = Float::with_val(PG, 1) >> 205;
    let factor_f = |r: usize| -> Float {
        let mut base: Float = Float::with_val(PG, 1) + &eps_f;
        base = base.pow(r as u32);
        base - 1
    };

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
        (det, sum_abs * factor_f(r))
    };

    // build planted world displacing zero index kk (1-based) by delta
    let planted = |kk: usize, delta: f64| -> Vec<Float> {
        let gk = &g[kk - 1];
        let g2 = Float::with_val(PG, gk * gk);
        let d = Float::with_val(PG, delta);
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
        for k in 3..24 {
            c.push(Float::with_val(PG, 2.0) * &b1 * &c[k - 1] - &b1sq * &c[k - 2]);
        }
        let mut bt: Vec<Float> = Vec::with_capacity(24);
        for k in 0..24 {
            let mut s = Float::with_val(PG, 0);
            for j in 0..=k { s += &b[j] * &c[k - j]; }
            bt.push(s);
        }
        bt
    };

    // smallest delta detected at each PF order, for k in {1, 10, 100}
    println!("\nDetection threshold: smallest delta at which a certified-negative minor appears,");
    println!("for planted displacement of zero #k (gamma_k = 14.13 / 49.77 / 236.5):");
    println!("  {:<4} {:<10} {:<10} {:<10} {:<10} {:<10}", "k", "PF2", "PF3", "PF4", "PF6", "PF8");
    // relative grid: delta = gamma_k * 10^-j, ascending so the first found is the SMALLEST
    let mut rels: Vec<f64> = (1..=10).map(|e| 10f64.powi(-e)).collect();
    rels.reverse(); // 1e-10 .. 1e-1
    rels.push(0.5); rels.push(1.0); rels.push(2.0); rels.push(5.0); rels.push(10.0);
    for &kk in &[1usize, 10, 100] {
        let gkf = g[kk - 1].to_f64();
        let mut row = format!("  {:<4} ({:>6.1})", kk, gkf);
        for &r in &[2usize, 3, 4, 6, 8] {
            let mut thresh: Option<f64> = None;
            for &re in &rels {
                let dl = gkf * re; // absolute displacement = gamma_k * 10^-j
                let bt = planted(kk, dl);
                let win: usize = 18;
                let lim = win.saturating_sub(r);
                let mut found = false;
                'inner: for s in 0..=lim {
                    for c0 in 0..=lim {
                        let rows: Vec<usize> = (s + 1..=s + r).collect();
                        let cols: Vec<usize> = (c0..c0 + r).collect();
                        let (dv, ev) = det_cert(&bt, &rows, &cols);
                        let negev = Float::with_val(PG, -&ev);
                        if dv < negev { found = true; break 'inner; }
                    }
                }
                if found { thresh = Some(dl); break; }
            }
            match thresh {
                Some(t) => row.push_str(&format!(" {:<10}", format!("{:.0e}", t / gkf))),
                None => row.push_str(&format!(" {:<10}", ">10")),
            }
        }
        println!("{}", row);
    }
    println!("  (thresholds shown as relative delta/gamma_k; absolute = gamma_k * value)");
    println!("\nInterpretation: the detection threshold is the SMALLEST displacement detected at that");
    println!("order. If it rises with gamma_k, the finite tests are blind exactly where an RH-false");
    println!("world would live (large height, per de Bruijn-Newman).");
}
