use rug::Float;
use std::fs;
fn main() {
    let txt = fs::read_to_string("/home/vstaln/riemann/research/notes/g02-moments-oracle-2026-08-18.txt").unwrap();
    let mut b: Vec<Float> = Vec::new();
    for line in txt.lines() {
        let line = line.trim();
        if line.is_empty() || line.starts_with('#') || line.starts_with("g0-2") { continue; }
        let cols: Vec<&str> = line.split('\t').collect();
        if cols.len() >= 3 {
            if let Ok(v) = Float::parse_radix(cols[2].trim(), 10) { b.push(Float::with_val(210, v)); }
        }
    }
    println!("b.len = {}", b.len());
    for n in [100usize, 250] {
        let l = b[n].clone().ln();
        let l1 = b[n+1].clone().ln();
        println!("n={} ln_b={} ln_b(n+1)={} diff={} r1(naive)=ln(b(n+1)/b(n))={}", n, l.to_f64(), l1.to_f64(), (l1-l).to_f64(), (b[n+1].clone()/&b[n]).ln().to_f64());
    }
    // r1 via ratio (no log of tiny): ln(b(n+1)/b(n)) + ln(n+1)
    for n in [10usize, 250] {
        let r = (b[n+1].clone()/&b[n]).ln().to_f64() + ((n+1) as f64).ln();
        let r2 = (b[n+2].clone()/&b[n+1]).ln().to_f64() + ((n+2) as f64).ln();
        let d2 = 0.5*(r-r2);
        let a = r + d2;
        println!("n={} r1={:.5} r2={:.5} delta2={:.5} A={:.5} eA={:.5}", n, r, r2, d2, a, a.exp());
    }
}
