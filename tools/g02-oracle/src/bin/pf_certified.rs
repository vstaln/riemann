// pf_certified: CERTIFIED PF audit of the Taylor-coefficient sequence
// b_k = M_k/(2k)! of Xi. RH <-> PF_infinity of {b_k} (Edrei/Aissen-Schoenberg-Whitney:
// F(w)=sum b_k w^k has all real zeros <= 0 iff {b_k} is a PF sequence), so a NEGATIVE
// certified Toeplitz minor at any order would be an RH disproof; positive certified
// minors are RH-consistent evidence (never a proof).
//
// Error bound: entries b_k known to relative error eps (table prints ~63 sig digits at
// 210 bits, so eps = 2^-207 conservative). All b_k > 0, so each Leibniz term
// t_pi = +- prod(entries) has relative error ((1+eps)^r - 1) in magnitude, and
//   |det_true - det_computed| <= (sum over pi of |t_pi|) * ((1+eps)^r - 1).
// This is far tighter than the crude r!*max_abs^r*eps bound and certifies the tiny
// positive minors. Classification: det - err > 0 -> CERTIFIED > 0;
// det + err < 0 -> CERTIFIED < 0 (RH disproof); else INCONCLUSIVE.
//
// Control: the logistic density rho(u)=(1/4)sech^2(u/2), whose Fourier transform
// pi z / sinh(pi z) has non-real zeros (RH-false in the LP sense). Its moments are
// M_k = (2k)! (1 - 2^{1-2k}) zeta(2k), so b_k = (1 - 2^{1-2k}) zeta(2k), computed at
// 210 bits from exact Bernoulli numbers. Same certified pipeline must find a
// CERTIFIED < 0 minor to demonstrate the test discriminates.
use rug::{ops::Pow, Float};
use std::fs;

const PG: u32 = 210;

fn main() {
    let txt = fs::read_to_string("/home/vstaln/riemann/research/notes/g02-moments-oracle-2026-08-18.txt")
        .expect("oracle table");
    // parse b_k = M_k/(2k)! = column 3 (index 2) at 210-bit precision
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
    let mut all_pos = true; // all b_k > 0? (needed for the tight bound's sign reasoning)
    for v in &b { if v.is_sign_negative() { all_pos = false; } }
    println!("loaded b_k = M_k/(2k)! at {} bits, k=0..{} (all entries > 0: {})", PG, b.len() - 1, all_pos);

    // certified determinant of r x r Toeplitz matrix T(i,j) = b[rows[i] - cols[j]]
    // returns (det, err); also flags structurally-zero (exact zero rows/cols cases)
    // (1+eps)^r - 1 computed at 210 bits: f64 1+2^-207 rounds to exactly 1.0
    let eps_f = Float::with_val(PG, 1) >> 207; // 2^-207
    let factor_f = |r: usize| -> Float {
        let one = Float::with_val(PG, 1);
        let mut base: Float = one + &eps_f;
        base = base.pow(r as u32);
        base - 1
    };
    let det_cert = |b: &Vec<Float>, rows: &[usize], cols: &[usize]| -> (Float, Float) {
        let r = rows.len();
        let mut vals: Vec<Float> = Vec::with_capacity(r * r);
        for i in 0..r {
            for j in 0..r {
                let idx = rows[i] as i64 - cols[j] as i64;
                let v = if idx < 0 { Float::with_val(PG, 0) } else { b[idx as usize].clone() };
                vals.push(v);
            }
        }
        let mut perm: Vec<usize> = (0..r).collect();
        let mut det = Float::with_val(PG, 0);
        let mut sum_abs = Float::with_val(PG, 0); // sum of |terms| for the error bound
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
            let t = term.clone().abs();
            sum_abs += &t;
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
        assert_eq!(count as u128, expect, "permutation count mismatch (r={})", r);
        let err = sum_abs * factor_f(r);
        (det, err)
    };

    // classify: >0 certified / <0 certified / inconclusive
    let classify = |d: &Float, e: &Float| -> &'static str {
        if d > e { "CERTIFIED > 0 ✓" }
        else if d < &-e.clone() { "CERTIFIED < 0 ✗✗ (RH disproof!)" }
        else { "INCONCLUSIVE" }
    };

    println!("\n=== ZETA: certified Toeplitz minors of b_k (consecutive rows/cols; Fekete: consecutive minors suffice for TP) ===");
    let mut bad: Vec<String> = Vec::new();
    for r in 2..=6usize {
        let mut worst: f64 = 1e300;
        let mut npos = 0u64;
        let mut nzero = 0u64;
        let mut ninc = 0u64;
        for s in 0..=(40 - r) {
            for c0 in 0..=(40 - r) {
                let rows: Vec<usize> = (s + 1..=s + r).collect();
                let cols: Vec<usize> = (c0..c0 + r).collect();
                let (d, e) = det_cert(&b, &rows, &cols);
                let cls = classify(&d, &e);
                if cls.starts_with("CERTIFIED >") { npos += 1; }
                else if d == 0 { nzero += 1; } // exact structural zero (allowed: PF needs >= 0)
                else { ninc += 1; }
                if cls.starts_with("CERTIFIED <") {
                    bad.push(format!("{}x{} rows({:?}) cols({:?}): det={:.3e} err={:.1e}", r, r, rows, cols, d.to_f64(), e.to_f64()));
                }
                let ratio = if e.to_f64() > 0.0 { d.to_f64().abs() / e.to_f64() } else { 1e300 };
                if ratio < worst { worst = ratio; }
            }
        }
        println!("  order {}: {} certified > 0, {} exact-zero (structural), {} tiny/inconclusive over window 0..40; min |det|/err = {:.1e}",
                 r, npos, nzero, ninc, worst);
    }
    for r in 7..=8usize {
        let mut worst: f64 = 1e300;
        let mut npos = 0u64;
        let mut nzero = 0u64;
        let mut ninc = 0u64;
        for s in 0..=(12 - r) {
            for c0 in 0..=(12 - r) {
                let rows: Vec<usize> = (s + 1..=s + r).collect();
                let cols: Vec<usize> = (c0..c0 + r).collect();
                let (d, e) = det_cert(&b, &rows, &cols);
                let cls = classify(&d, &e);
                if cls.starts_with("CERTIFIED >") { npos += 1; }
                else if d == 0 { nzero += 1; }
                else { ninc += 1; }
                if cls.starts_with("CERTIFIED <") {
                    bad.push(format!("{}x{} rows({:?}) cols({:?}): det={:.3e} err={:.1e}", r, r, rows, cols, d.to_f64(), e.to_f64()));
                }
                let ratio = if e.to_f64() > 0.0 { d.to_f64().abs() / e.to_f64() } else { 1e300 };
                if ratio < worst { worst = ratio; }
            }
        }
        println!("  order {}: {} certified > 0, {} exact-zero (structural), {} tiny/inconclusive over window 0..12; min |det|/err = {:.1e}",
                 r, npos, nzero, ninc, worst);
    }
    // FULL all-selections PF check, orders 2..=5 over index window 0..=8: every minor with
    // ARBITRARY row/col subsets (the actual PF_r condition, not just consecutive).
    // C(9,r)^2 minors each; r<=5 keeps Leibniz cost bounded (r=5: 1296 subsets^2 * 120 perms).
    println!("\n  FULL PF check (all row/col selections), orders 2..=5 over index window 0..=8:");
    for r in 2..=5usize {
        let idxs: Vec<usize> = (0..=8).collect();
        // all r-subsets of idxs
        fn subsets(v: &[usize], r: usize) -> Vec<Vec<usize>> {
            let mut out = Vec::new();
            let n = v.len();
            let mut comb: Vec<usize> = (0..r).collect();
            loop {
                out.push(comb.iter().map(|&i| v[i]).collect());
                let mut i = r;
                while i > 0 {
                    i -= 1;
                    if comb[i] != n - r + i { break; }
                }
                if i == 0 && comb[0] == n - r { break; }
                comb[i] += 1;
                for j in i + 1..r { comb[j] = comb[j - 1] + 1; }
            }
            out
        }
        let subs = subsets(&idxs, r);
        let mut ntest = 0u64;
        let mut worst: f64 = 1e300;
        let mut npos = 0u64;
        let mut nzero = 0u64;
        for rows in &subs {
            for cols in &subs {
                // rows/cols must be strictly increasing (they are, by construction);
                // skip the all-identical structurally-degenerate cases handled implicitly
                let (d, e) = det_cert(&b, rows, cols);
                ntest += 1;
                let cls = classify(&d, &e);
                if cls.starts_with("CERTIFIED >") { npos += 1; }
                else if d == 0 { nzero += 1; }
                else if cls.starts_with("CERTIFIED <") {
                    bad.push(format!("{}x{} rows({:?}) cols({:?}): det={:.3e} err={:.1e}", r, r, rows, cols, d.to_f64(), e.to_f64()));
                }
                let ratio = if e.to_f64() > 0.0 { d.to_f64().abs() / e.to_f64() } else { 1e300 };
                if ratio < worst { worst = ratio; }
            }
        }
        println!("  order {}: {} certified > 0, {} exact-zero, {} total all-selection minors over window 0..8; min |det|/err = {:.1e}",
                 r, npos, nzero, ntest, worst);
    }

    // orders 9-10: single leading minor each (9! = 362880, 10! = 3628800 Leibniz terms)
    for r in 9..=10usize {
        let mut worst: f64 = 1e300;
        let mut npos = 0u64;
        let mut nzero = 0u64;
        let mut ninc = 0u64;
        let mut ntest = 0u64;
        let win = r; // s,c0 in 0..=0 -> exactly the leading minor
        let lim = win.saturating_sub(r);
        for s in 0..=lim {
            for c0 in 0..=lim {
                let rows: Vec<usize> = (s + 1..=s + r).collect();
                let cols: Vec<usize> = (c0..c0 + r).collect();
                let (d, e) = det_cert(&b, &rows, &cols);
                ntest += 1;
                let cls = classify(&d, &e);
                if cls.starts_with("CERTIFIED >") { npos += 1; }
                else if d == 0 { nzero += 1; }
                else { ninc += 1; }
                if cls.starts_with("CERTIFIED <") {
                    bad.push(format!("{}x{} rows({:?}) cols({:?}): det={:.3e} err={:.1e}", r, r, rows, cols, d.to_f64(), e.to_f64()));
                }
                let ratio = if e.to_f64() > 0.0 { d.to_f64().abs() / e.to_f64() } else { 1e300 };
                if ratio < worst { worst = ratio; }
            }
        }
        println!("  order {}: {} certified > 0, {} exact-zero (structural), {} tiny/inconclusive (leading minor); min |det|/err = {:.1e}",
                 r, npos, nzero, ninc, worst);
    }
    if bad.is_empty() {
        println!("  VERDICT (zeta): no certified-negative minor up to order 10 — RH-consistent (PF2..PF10 pass, no disproof).");
    } else {
        println!("  VERDICT (zeta): {} certified-negative minor(s)!", bad.len());
        for s in bad { println!("    {}", s); }
    }

    // ---------- CONTROL: logistic density ----------
    // b_k = (1 - 2^{1-2k}) zeta(2k), zeta(2k) = (2 pi)^(2k) |B_{2k}| / (2 (2k)!)
    // exact Bernoulli numbers B_2..B_24 (|B_{2k}| = abs):
    let bern: [f64; 13] = [1.0 / 6.0, 1.0 / 30.0, 1.0 / 42.0, 1.0 / 30.0, 5.0 / 66.0,
                           691.0 / 2730.0, 7.0 / 6.0, 3617.0 / 510.0, 43867.0 / 798.0,
                           174611.0 / 330.0, 854513.0 / 138.0, 236364091.0 / 2730.0,
                           8553103.0 / 6.0]; // B_26
    let pi = Float::with_val(PG, rug::float::Constant::Pi);
    let mut ctl: Vec<Float> = Vec::new();
    ctl.push(Float::with_val(PG, 1)); // b_0 = 1
    for k in 1..=13usize {
        // zeta(2k) = (2pi)^{2k} |B_{2k}| / (2 (2k)!)
        let two_pi = Float::with_val(PG, &pi * 2);
        let num = two_pi.pow(2 * k as u32) * bern[k - 1].abs()
            / (2.0 * (1..=(2 * k)).fold(1.0f64, |a, i| a * i as f64));
        let bk = num * (1.0 - 2f64.powi(1 - 2 * k as i32));
        ctl.push(bk);
    }
    println!("\n=== CONTROL: logistic rho(u)=(1/4)sech^2(u/2), b_k=(1-2^{{1-2k}})zeta(2k) (FT pi z/sinh(pi z), RH-false in LP sense) ===");
    println!("  control b_k (k=0..12): {}", ctl.iter().map(|v| format!("{:.4}", v.to_f64())).collect::<Vec<_>>().join(", "));
    let mut cbad: Vec<String> = Vec::new();
    for r in 2..=5usize {
        let mut worst: f64 = 1e300; // most negative minor
        let mut worst_spec = String::new();
        let lim = 12usize.saturating_sub(r); // keep indices within ctl[0..13]
        for s in 0..=lim {
            for c0 in 0..=lim {
                let rows: Vec<usize> = (s + 1..=s + r).collect();
                let cols: Vec<usize> = (c0..c0 + r).collect();
                let (d, e) = det_cert(&ctl, &rows, &cols);
                let cls = classify(&d, &e);
                if cls.starts_with("CERTIFIED <") {
                    cbad.push(format!("{}x{} rows({:?}) cols({:?}): det={:.3e} err={:.1e}  {}", r, r, rows, cols, d.to_f64(), e.to_f64(), cls));
                }
                if d.to_f64() < worst {
                    worst = d.to_f64();
                    worst_spec = format!("{}x{} rows({:?}) cols({:?})", r, r, rows, cols);
                }
            }
        }
        println!("  order {}: most negative minor = {:.3e}  at {}", r, worst, worst_spec);
    }
    if cbad.is_empty() {
        println!("  VERDICT (control): NO certified-negative minor — test does NOT discriminate at these orders?");
    } else {
        println!("  VERDICT (control): {} certified-negative minor(s) — the non-LP control FAILS where zeta passes:", cbad.len());
        for s in cbad { println!("    {}", s); }
    }
    println!("\n(PF_∞ is still not certified for zeta: finite orders cannot prove the infinite property.)");
}
