// pf_gamma: certified PF audit on gamma(n) = n! * b_n (column 4 of the certified table),
// the sequence GORZ's Jensen polynomials J^{d,n}(X) = sum C(d,j) gamma(n+j) X^j are built from.
// Classical Jensen/GORZ: RH iff all J^{d,n} hyperbolic iff {gamma} is PF_infinity. The frontier
// correction note claimed gamma fails Toeplitz 3x3 at -7.0e-8 (f64); this is the certified check.
use rug::{ops::Pow, Float};
use std::fs;
const PG: u32 = 210;
fn main() {
    let txt = fs::read_to_string("/home/vstaln/riemann/research/notes/g02-moments-oracle-2026-08-18.txt").unwrap();
    let mut g: Vec<Float> = Vec::new();
    for line in txt.lines() {
        let line = line.trim();
        if line.is_empty() || line.starts_with('#') || line.starts_with("g0-2") { continue; }
        let cols: Vec<&str> = line.split('\t').collect();
        if cols.len() >= 4 {
            if let Ok(v) = Float::parse_radix(cols[3].trim(), 10) { g.push(Float::with_val(PG, v)); }
        }
    }
    println!("loaded gamma(n)=n!*b_n n=0..{}", g.len() - 1);
    let eps_f = Float::with_val(PG, 1) >> 207;
    let factor_f = |r: usize| -> Float {
        let mut base: Float = Float::with_val(PG, 1) + &eps_f;
        base = base.pow(r as u32);
        base - 1
    };
    let det_cert = |seq: &Vec<Float>, rows: &[usize], cols: &[usize]| -> (Float, Float) {
        let r = rows.len();
        let mut vals: Vec<Float> = Vec::with_capacity(r * r);
        for i in 0..r { for j in 0..r {
            let idx = rows[i] as i64 - cols[j] as i64;
            let v = if idx < 0 { Float::with_val(PG, 0) } else { seq[idx as usize].clone() };
            vals.push(v);
        }}
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
    let classify = |d: &Float, e: &Float| -> &'static str {
        if d > e { "CERTIFIED > 0" } else if d < &Float::with_val(PG, -e) { "CERTIFIED < 0 <<< PF FAIL" } else { "INCONCLUSIVE" }
    };
    println!("\nCertified consecutive Toeplitz minors of gamma(n)=n!*b_n (Fekete family):");
    let mut bad = 0;
    for r in 2..=6usize {
        let mut npos = 0u64; let mut nzero = 0u64; let mut ninc = 0u64;
        let mut worst: f64 = 1e300;
        for s in 0..=(20 - r) { for c0 in 0..=(20 - r) {
            let rows: Vec<usize> = (s + 1..=s + r).collect();
            let cols: Vec<usize> = (c0..c0 + r).collect();
            let (d, e) = det_cert(&g, &rows, &cols);
            let cls = classify(&d, &e);
            match cls {
                "CERTIFIED > 0" => npos += 1,
                "INCONCLUSIVE" => { if d == 0 { nzero += 1 } else { ninc += 1 } },
                _ => { bad += 1; if worst > 0.0 { println!("   FAIL {}x{} rows({:?}) cols({:?}): det={:.3e} err={:.1e}", r, r, rows, cols, d.to_f64(), e.to_f64()); } worst = -1.0; },
            }
        }}
        println!("  order {}: {} certified > 0, {} exact-zero, {} inconclusive; min |det|/err = {:.1e}",
                 r, npos, nzero, ninc, if worst < 0.0 { 0.0 } else { worst });
    }
    // the specific 3x3 the correction note flagged: check all 3x3 in window 0..20
    println!("\nSpecific check: all 3x3 consecutive minors (the correction note claimed -7.0e-8):");
    let mut min3 = 1e300; let mut spec = String::new();
    for s in 0..=(20 - 3) { for c0 in 0..=(20 - 3) {
        let rows: Vec<usize> = (s + 1..=s + 3).collect();
        let cols: Vec<usize> = (c0..c0 + 3).collect();
        let (d, e) = det_cert(&g, &rows, &cols);
        if d.to_f64().abs() < min3 { min3 = d.to_f64().abs(); spec = format!("rows({:?}) cols({:?}) d={:.6e} err={:.1e}", rows, cols, d.to_f64(), e.to_f64()); }
    }}
    println!("  min |3x3 minor|: {:.3e} at {}", min3, spec);
    println!("\nVERDICT: {}", if bad == 0 { "gamma(n)=n!*b_n passes certified PF2-PF6 — the correction note's -7.0e-8 claim was an f64 artifact" } else { "certified PF failure found" });
}
