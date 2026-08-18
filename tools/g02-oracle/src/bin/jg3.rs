use rug::Float;
use std::fs;
const PG: u32 = 210;
fn main() {
    let txt = fs::read_to_string("/home/vstaln/riemann/research/notes/g02-moments-oracle-2026-08-18.txt").unwrap();
    let mut b: Vec<Float> = Vec::new();
    for line in txt.lines() {
        let line = line.trim();
        if line.is_empty() || line.starts_with('#') || line.starts_with("g0-2") { continue; }
        let cols: Vec<&str> = line.split('\t').collect();
        if cols.len() >= 2 {
            if let Ok(v) = Float::parse_radix(cols[2].trim(), 10) { b.push(Float::with_val(PG, v)); }
        }
    }
    let mkpoly = |d: usize, n: usize| -> Vec<f64> {
        let gn = &b[n];
        let mut r: Vec<f64> = Vec::with_capacity(d + 1);
        let mut prod = Float::with_val(PG, 1);
        for j in 0..=d {
            if j > 0 { prod *= (n + j) as f64; }
            let num = Float::with_val(PG, &prod * &b[n + j]);
            let ratio = Float::with_val(PG, num / gn);
            let mut binom = 1.0f64;
            for i in 0..j { binom *= (d - i) as f64 / (i + 1) as f64; }
            r.push(binom * ratio.to_f64());
        }
        r
    };
    for &(d, n) in &[(2usize, 10usize), (3, 10), (2, 250)] {
        let c = mkpoly(d, n);
        println!("d={} n={} coeffs: {:?}", d, n, c);
        for x in [-10000.0, -1000.0, -500.0, -283.0, -250.0, -200.0, -100.0, -50.0, 0.0, 50.0, 100.0] {
            let v = c.iter().rev().fold(0.0, |s, &a| s * x + a);
            println!("   P({}) = {:.4e}", x, v);
        }
        println!();
    }
}
