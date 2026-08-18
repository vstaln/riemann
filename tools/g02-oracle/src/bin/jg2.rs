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
    let mut gam: Vec<Float> = Vec::with_capacity(b.len());
    let mut fact = Float::with_val(PG, 1);
    for (n, bn) in b.iter().enumerate() {
        if n > 0 { fact *= n as f64; }
        gam.push(Float::with_val(PG, 8) * &fact * bn);
    }
    let jval = |d: usize, n: usize, x: f64| -> f64 {
        let mut s = 0.0f64;
        for j in (0..=d).rev() {
            let mut binom = 1.0f64;
            for i in 0..j { binom *= (d - i) as f64 / (i + 1) as f64; }
            s = s * x + binom * gam[n + j].to_f64();
        }
        s
    };
    for &(d, n) in &[(2usize, 10usize), (2, 200), (3, 10), (3, 200)] {
        for x in [-1000.0, -500.0, -200.0, -100.0, -50.0, -10.0, 0.0, 10.0, 100.0] {
            println!("d={} n={} J({}) = {:.4e}", d, n, x, jval(d, n, x));
        }
        println!();
    }
}
