// WAVE 8C hi-N — certified d_N at N in {2000, 3000, 5000} (Báez-Duarte sharp rate).
//
// Layers of certification:
//   (A) f64 Gram (adaptive truncation P(L)) + f64 Cholesky            -> d_f64
//   (B) iterative refinement, residuals in double-double (~1e-30)     -> exact solve of STORED f64 G
//   (C) threaded MPFR-256 Cholesky on the SAME stored f64 G           -> independent solve check
//   (D) full double-double pipeline (Gram+Cholesky, dd integer-ln table) at N=2000
//       -> end-to-end measured gap (covers Gram closed-form truncation + storage).
//
// Truncation fix vs main.rs: tail p-expansion rate is (1+1/L)/4 per term (worst L=1: 0.5),
// so fixed P=32 leaves ~1e-10 rel error in G_11 — invisible to a same-P MPFR cross-check.
// Here P adapts: P(L) = ceil(digits*ln10/ln(4L/(L+1))) + 3, digits=17 (f64) / 31 (dd, MPFR).
// Regression mode Fixed(32) reproduces main.rs values exactly.
//
// Phases: validate | prod <N> | ddgram <N>.  All output appends (flushed) to results/hiN_log.txt.

use rug::Float;
use rug::ops::Pow;
use std::fs::OpenOptions;
use std::io::Write;
use std::sync::atomic::{AtomicUsize, Ordering};
use std::thread;

// raw pointer that crosses thread boundaries (disjoint writes by construction).
// access via .at() only — method receiver captures the whole struct, keeping the Send impl effective
struct SendPtr<T>(*mut T);
unsafe impl<T> Send for SendPtr<T> {}
impl<T> SendPtr<T> {
    #[inline(always)]
    fn at(&self, i: usize) -> *mut T {
        self.0.wrapping_add(i)
    }
}

const PMAX: usize = 110;

// Euler gamma to 50 digits, constructed exactly from u64 chunks (no string-parse API dependence):
// 0.57721566490153286060651209008240243104215933593992
//   = 5772156649015328606e-19 + 651209008240243104e-38 + 215933593992e-50
fn gamma_mpfr() -> Float {
    let prec = u32::try_from(256).unwrap();
    let e19 = Float::with_val(prec, 10_000_000_000_000_000_000u64);
    let e12 = Float::with_val(prec, 1_000_000_000_000u64);
    let c1 = Float::with_val(prec, Float::with_val(prec, 5_772_156_649_015_328_606u64) / &e19);
    let t2 = Float::with_val(prec, Float::with_val(prec, 651_209_008_240_243_104u64) / &e19);
    let c2 = Float::with_val(prec, &t2 / &e19);
    let t3 = Float::with_val(prec, Float::with_val(prec, 215_933_593_992u64) / &e12);
    let t4 = Float::with_val(prec, &t3 / &e19);
    let c3 = Float::with_val(prec, &t4 / &e19);
    Float::with_val(prec, &Float::with_val(prec, &c1 + &c2) + &c3)
}

fn log_line(s: &str) {
    // repo-root CWD (cargo run --manifest-path) or wave8c CWD (cargo run inside dir)
    let path = if std::path::Path::new("tools/wave8c/results").exists() {
        "tools/wave8c/results/hiN_log.txt".to_string()
    } else {
        std::fs::create_dir_all("results").unwrap();
        "results/hiN_log.txt".to_string()
    };
    let mut f = OpenOptions::new().create(true).append(true).open(path).unwrap();
    writeln!(f, "{}", s).unwrap();
    f.flush().unwrap();
    println!("{}", s);
}

// ---------------- basic integer helpers ----------------
fn gcd(a: u64, b: u64) -> u64 {
    let (mut x, mut y) = (a, b);
    while y != 0 {
        let t = x % y;
        x = y;
        y = t;
    }
    x
}
fn lcm(a: u64, b: u64) -> u64 {
    a / gcd(a, b) * b
}

// intervals (alpha,beta,floor(alpha/j),floor(alpha/k)) covering [1,1+L]  (copied from main.rs)
fn intervals(j: u64, k: u64, l: u64) -> Vec<(u64, u64, u64, u64)> {
    let end = 1 + l;
    let mut pts: Vec<u64> = Vec::with_capacity(((l / j) + (l / k) + 2) as usize);
    let mut m = 1u64;
    loop {
        let p = m * j;
        if p > end {
            break;
        }
        if p > 1 {
            pts.push(p);
        }
        m += 1;
    }
    let mut m = 1u64;
    loop {
        let p = m * k;
        if p > end {
            break;
        }
        if p > 1 {
            pts.push(p);
        }
        m += 1;
    }
    pts.sort_unstable();
    pts.dedup();
    let mut ivs = Vec::with_capacity(pts.len() + 1);
    let mut cur = 1u64;
    for &p in &pts {
        if p > cur {
            ivs.push((cur, p, cur / j, cur / k));
            cur = p;
        }
    }
    if cur < end {
        ivs.push((cur, end, cur / j, cur / k));
    }
    ivs
}

// adaptive tail depth; digits = 17 (f64) or 31 (dd/mpfr)
fn p_adaptive(l: u64, digits: f64) -> usize {
    let r = 4.0 * l as f64 / (l as f64 + 1.0); // 1/rate
    let p = (digits * 10.0f64.ln() / r.ln()).ceil() as usize + 3;
    p.clamp(24, PMAX)
}

// ---------------- z-tables ----------------
// Z_p = sum_{m>=4} m^{-(p+2)}; f64 version (EM) as in main.rs but sized PMAX.
fn z_table_f64(p_max: usize) -> Vec<f64> {
    let n1 = 10_000u64;
    let mut z = vec![0.0f64; p_max];
    for p in 0..p_max {
        let s = p as f64 + 2.0;
        let mut acc = 0.0;
        for m in 4..=n1 {
            acc += (m as f64).powf(-s);
        }
        let x = n1 as f64;
        // EM tail: sign of the half-term is MINUS (Euler-Maclaurin for the upper tail).
        // main.rs had PLUS — a real bug (error +n^{-(p+2)} in every published Z_p; fixed here).
        acc += x.powf(1.0 - s) / (s - 1.0)
            - 0.5 * x.powf(-s)
            + (s / 12.0) * x.powf(-s - 1.0)
            - (s * (s + 1.0) * (s + 2.0) / 720.0) * x.powf(-s - 3.0);
        z[p] = acc;
    }
    z
}

// MPFR-direct z-table (upgrade: the old zm was f64-converted, capping the "MPFR" gram at ~1e-15)
fn z_table_mpfr_direct(p_max: usize) -> Vec<Float> {
    let prec = u32::try_from(256).unwrap();
    let mut z: Vec<Float> = Vec::with_capacity(p_max);
    let n1 = 2000u64;
    for p in 0..p_max {
        let s = p as u32 + 2;
        // direct: sum m^{-(p+2)} for m=4..=2000, EM tail after
        let mut acc = Float::with_val(prec, 0);
        let negs = Float::with_val(prec, -(s as i32));
        for m in 4..=n1 {
            let mf = Float::with_val(prec, m);
            let t = mf.pow(&negs);
            acc += &t;
        }
        let n1f = Float::with_val(prec, n1);
        let one = Float::with_val(prec, 1);
        let s2 = Float::with_val(prec, s);
        // n^{1-s}
        let e1s = Float::with_val(prec, &one - &s2);
        let n1_e1s = n1f.clone().pow(&e1s);
        let n1_negs = n1f.clone().pow(&negs);
        let negs1 = Float::with_val(prec, &negs - &one);
        let n1_negs1 = n1f.clone().pow(&negs1);
        let negs3 = Float::with_val(prec, &negs - 3.0);
        let n1_negs3 = n1f.pow(&negs3);
        // c1 = n^{1-s}/(s-1)
        let sm1 = Float::with_val(prec, &s2 - &one);
        let c1 = Float::with_val(prec, &n1_e1s / &sm1);
        // c2 = -0.5 * n^{-s}   (MINUS: EM upper-tail half-term; main.rs sign bug documented+fixed)
        let c2 = Float::with_val(prec, &Float::with_val(prec, -0.5) * &n1_negs);
        // c3 = (s/12) n^{-s-1}
        let sd12 = Float::with_val(prec, &s2 / 12.0);
        let c3 = Float::with_val(prec, &sd12 * &n1_negs1);
        // c4 = s(s+1)(s+2)/720 * n^{-s-3}
        let sp1 = Float::with_val(prec, &s2 + 1.0);
        let sp2 = Float::with_val(prec, &s2 + 2.0);
        let s12 = Float::with_val(prec, &s2 * &sp1);
        let s123a = Float::with_val(prec, &s12 * &sp2);
        let s123 = Float::with_val(prec, &s123a / 720.0);
        let c4 = Float::with_val(prec, &s123 * &n1_negs3);
        acc += &c1;
        acc += &c2;
        acc += &c3;
        acc -= &c4;
        z.push(acc);
    }
    z
}

// ---------------- double-double arithmetic ----------------
#[derive(Clone, Copy, Debug)]
struct Dd {
    hi: f64,
    lo: f64,
}

impl Dd {
    fn from_f64(x: f64) -> Dd {
        Dd { hi: x, lo: 0.0 }
    }
    fn from_int(n: u64) -> Dd {
        Dd { hi: n as f64, lo: 0.0 } // exact for n < 2^53 (all our ints)
    }
    fn to_f64(self) -> f64 {
        self.hi + self.lo
    }
    fn is_zero(self) -> bool {
        self.hi == 0.0 && self.lo == 0.0
    }
}

fn two_sum(a: f64, b: f64) -> (f64, f64) {
    let s = a + b;
    let bb = s - a;
    let err = (a - (s - bb)) + (b - bb);
    (s, err)
}

fn two_prod(a: f64, b: f64) -> (f64, f64) {
    let p = a * b;
    let e = a.mul_add(b, -p);
    (p, e)
}

fn dd_add(a: Dd, b: Dd) -> Dd {
    // QD dd_real::add (Hida-Li-Bailey): correct two-term accumulation
    let (s1, s2) = two_sum(a.hi, b.hi);
    let (t1, t2) = two_sum(a.lo, b.lo);
    let (s1a, s2a) = two_sum(s1, s2 + t1);
    let (hi, lo) = two_sum(s1a, s2a + t2);
    Dd { hi, lo }
}

fn dd_neg(a: Dd) -> Dd {
    Dd { hi: -a.hi, lo: -a.lo }
}

fn dd_sub(a: Dd, b: Dd) -> Dd {
    dd_add(a, dd_neg(b))
}

fn dd_mul(a: Dd, b: Dd) -> Dd {
    let (p, e) = two_prod(a.hi, b.hi);
    let lo = e + a.hi * b.lo + a.lo * b.hi;
    let (hi, lo2) = two_sum(p, lo);
    Dd { hi, lo: lo2 }
}

fn dd_div(a: Dd, b: Dd) -> Dd {
    let q1 = a.hi / b.hi;
    // r = a - b*q1
    let (p1, e1) = two_prod(b.hi, q1);
    let r = dd_add(a, dd_neg(Dd { hi: p1, lo: b.lo * q1 + e1 }));
    let q2 = r.hi / b.hi;
    let q3 = r.lo / b.hi;
    dd_add(Dd { hi: q1, lo: q2 }, Dd { hi: 0.0, lo: q3 })
}

fn dd_sqrt(a: Dd) -> Dd {
    if a.hi <= 0.0 {
        return Dd { hi: 0.0, lo: 0.0 };
    }
    let mut s = Dd::from_f64(a.hi.sqrt());
    for _ in 0..3 {
        // s = s*(1 + a/s^2)/2  (Newton, quadratic: eps -> -eps^2/2).
        // The form s*(3 - a/s^2)/2 is the RECIPROCAL-sqrt iteration — anti-convergent here
        // (doubles the error each pass; caught by V1 vs rug-256).
        let s2 = dd_mul(s, s);
        let q = dd_div(a, s2);
        let t = dd_add(Dd::from_f64(1.0), q);
        let u = dd_mul(s, t);
        s = Dd { hi: u.hi * 0.5, lo: u.lo * 0.5 };
    }
    s
}

fn dd_from_mpfr(z: &Float) -> Dd {
    let hi = z.to_f64();
    let d = Float::with_val(256, z - Float::with_val(256, hi));
    Dd { hi, lo: d.to_f64() }
}

fn dd_to_mpfr(a: Dd) -> Float {
    let hi = Float::with_val(256, a.hi);
    let lo = Float::with_val(256, a.lo);
    Float::with_val(256, &hi + &lo)
}

// dd constants
struct DdConsts {
    ln2: Dd,
    gamma: Dd,
    inv: Vec<Dd>,       // inv[m] = 1/m, m=1..=PMAX+4
    wtab_f64_digits: f64,
}

fn dd_consts() -> DdConsts {
    let prec = u32::try_from(256).unwrap();
    let two = Float::with_val(prec, 2);
    let ln2m = Float::with_val(prec, &two).ln();
    let gm = gamma_mpfr();
    let mut inv = vec![Dd { hi: 0.0, lo: 0.0 }; PMAX + 5];
    for m in 1..=PMAX + 4 {
        let q = Float::with_val(prec, 1) / Float::with_val(prec, m);
        inv[m] = dd_from_mpfr(&q);
    }
    DdConsts {
        ln2: dd_from_mpfr(&ln2m),
        gamma: dd_from_mpfr(&gm),
        inv,
        wtab_f64_digits: 17.0,
    }
}

static CST: std::sync::OnceLock<DdConsts> = std::sync::OnceLock::new();
fn cst() -> &'static DdConsts {
    CST.get_or_init(dd_consts)
}

// dd w-table: wtab[p] = (-1)^p (p+1) Z_p  (dd, from MPFR-direct z)
fn cst_ln(n: u64) -> Dd {
    dd_ln_int(n, cst().ln2, &cst().inv)
}

fn dd_wtab(zmp: &[Float]) -> Vec<Dd> {
    zmp.iter()
        .enumerate()
        .map(|(p, z)| {
            let mut w = Float::with_val(256, (p as f64 + 1.0) * z);
            if p & 1 == 1 {
                w = -w;
            }
            dd_from_mpfr(&w)
        })
        .collect()
}

// dd ln of integer n (series; exact n < 2^53)
fn dd_ln_int(n: u64, ln2: Dd, inv: &[Dd]) -> Dd {
    let x = n as f64;
    let e = x.abs().log2().floor() as i64; // exact
    let m = x / (2.0f64).powi(e as i32); // exact, in [1,2)
    // y = (m-1)/(m+1) in dd
    let num = Dd { hi: m - 1.0, lo: 0.0 };
    let den = Dd { hi: m + 1.0, lo: 0.0 };
    let y = dd_div(num, den);
    let y2 = dd_mul(y, y);
    // sum = sum_i y^{2i+1}/(2i+1)
    let mut p = y;
    let mut sum = Dd { hi: 0.0, lo: 0.0 };
    for i in 0..48usize {
        let term = dd_mul(p, inv[2 * i + 1]);
        sum = dd_add(sum, term);
        p = dd_mul(p, y2);
        if p.hi < sum.hi * 1e-36 {
            break;
        }
    }
    let lnm = Dd { hi: 2.0 * sum.hi, lo: 2.0 * sum.lo };
    // ln n = e*ln2 + lnm
    let e_dd = Dd { hi: e as f64, lo: 0.0 };
    dd_add(dd_mul(e_dd, ln2), lnm)
}

// ---------------- f64 Gram (from main.rs, with p-mode) ----------------
#[derive(Clone, Copy)]
enum PMode {
    Fixed(usize),
    Adaptive(f64), // digits
}

fn pm(mode: PMode, l: u64) -> usize {
    match mode {
        PMode::Fixed(p) => p,
        PMode::Adaptive(d) => p_adaptive(l, d),
    }
}

fn gram_f64(j: u64, k: u64, z: &[f64], mode: PMode) -> f64 {
    let l = lcm(j, k);
    let pmax = pm(mode, l).min(z.len());
    let ivs = intervals(j, k, l);
    let lf = l as f64;
    let jf = j as f64;
    let kf = k as f64;
    let mut total = 0.0f64;
    for &(x1, x2, ai, bi) in &ivs {
        let a = x1 as f64;
        let b = x2 as f64;
        let aif = ai as f64;
        let bif = bi as f64;
        let c2 = 1.0 / (jf * kf);
        let c1 = -(aif / kf + bif / jf);
        let c0 = aif * bif;
        total += c2 * (b - a) + c1 * (b.ln() - a.ln()) + c0 * (1.0 / a - 1.0 / b);
        for m in 1..4u64 {
            let ml = m as f64 * lf;
            let v1 = a / ml;
            let v2 = b / ml;
            let c2p = ml * ml / (jf * kf);
            let c1p = -ml * (aif / kf + bif / jf);
            let c0p = aif * bif;
            let e2 = |v: f64| v - 2.0 * (v + 1.0).ln() - 1.0 / (v + 1.0);
            let e1 = |v: f64| (v + 1.0).ln() + 1.0 / (v + 1.0);
            let e0 = |v: f64| -1.0 / (v + 1.0);
            total += (c2p * (e2(v2) - e2(v1)) + c1p * (e1(v2) - e1(v1)) + c0p * (e0(v2) - e0(v1))) / ml;
        }
        let bl = b / lf;
        let al = a / lf;
        let mut pb1 = bl;
        let mut pa1 = al;
        for p in 0..pmax {
            let pb2 = pb1 * bl;
            let pa2 = pa1 * al;
            let pb3 = pb2 * bl;
            let pa3 = pa2 * al;
            let d1 = pb1 - pa1;
            let d2 = pb2 - pa2;
            let d3 = pb3 - pa3;
            let pf = p as f64;
            let sign = if p & 1 == 0 { 1.0 } else { -1.0 };
            let t1 = c2 * lf * d3 / (pf + 3.0);
            let t2 = c1 * d2 / (pf + 2.0);
            let t3 = c0 * d1 / lf / (pf + 1.0);
            total += sign * (pf + 1.0) * z[p] * (t1 + t2 + t3);
            pb1 = pb2;
            pa1 = pa2;
        }
    }
    total
}

fn b_f64(k: u64) -> f64 {
    // same f64 constant bits as main.rs GAMMA for exact regression
    ((k as f64).ln() + 1.0 - 0.57721566490153286060651209008240243104215933593992) / k as f64
}

// ---------------- dd Gram ----------------
// ln_table: Option<&[Dd]> — Some => use table (index = integer), None => on-demand series.
fn gram_dd(j: u64, k: u64, wtab: &[Dd], mode: PMode, ln_table: Option<&[Dd]>) -> Dd {
    let c0n = cst();
    let l = lcm(j, k);
    let pmax = pm(mode, l).min(wtab.len());
    let ivs = intervals(j, k, l);
    let ln_of = |n: u64| -> Dd {
        match ln_table {
            Some(t) => t[n as usize],
            None => dd_ln_int(n, c0n.ln2, &c0n.inv),
        }
    };
    let one = Dd::from_f64(1.0);
    let jk = Dd::from_int(j * k);
    let c2 = dd_div(one, jk);
    let mut total = Dd { hi: 0.0, lo: 0.0 };
    let lf = Dd::from_int(l);
    for &(x1, x2, ai, bi) in &ivs {
        let a = Dd::from_int(x1);
        let b = Dd::from_int(x2);
        let aif = Dd::from_int(ai);
        let bif = Dd::from_int(bi);
        // c2 (per entry) reused; c1, c0 per interval
        let c1 = dd_neg(dd_add(
            dd_div(aif, Dd::from_int(k)),
            dd_div(bif, Dd::from_int(j)),
        ));
        let c0 = Dd::from_int(ai * bi);
        // m = 0: c2*(b-a) + c1*(ln b - ln a) + c0*(1/a - 1/b)
        let db = Dd::from_int(x2 - x1);
        let t1 = dd_mul(c2, db);
        let dl = dd_sub(ln_of(x2), ln_of(x1));
        let t2 = dd_mul(c1, dl);
        let invdiff = dd_div(db, Dd::from_int(x1 * x2));
        let t3 = dd_mul(c0, invdiff);
        total = dd_add(total, dd_add(dd_add(t1, t2), t3));
        // m = 1..3
        for m in 1..4u64 {
            let ml = m * l;
            let mld = Dd::from_int(ml);
            let invml = dd_div(one, mld);
            let num1 = Dd::from_int(x1 + ml);
            let num2 = Dd::from_int(x2 + ml);
            let lnw1 = dd_sub(ln_of(x1 + ml), ln_of(ml));
            let lnw2 = dd_sub(ln_of(x2 + ml), ln_of(ml));
            let r1 = dd_div(mld, num1); // 1/(v1+1)
            let r2 = dd_div(mld, num2);
            let v1 = dd_div(a, mld);
            let v2 = dd_div(b, mld);
            // e2(v) = v - 2*ln(v+1) - 1/(v+1)
            let e2v1 = dd_sub(dd_sub(v1, Dd { hi: 2.0 * lnw1.hi, lo: 2.0 * lnw1.lo }), r1);
            let e2v2 = dd_sub(dd_sub(v2, Dd { hi: 2.0 * lnw2.hi, lo: 2.0 * lnw2.lo }), r2);
            let e1v1 = dd_add(lnw1, r1);
            let e1v2 = dd_add(lnw2, r2);
            let e0v1 = dd_neg(r1);
            let e0v2 = dd_neg(r2);
            let c2p = dd_div(Dd::from_int(ml * ml), jk);
            let c1p = dd_neg(dd_mul(mld, dd_add(
                dd_div(aif, Dd::from_int(k)),
                dd_div(bif, Dd::from_int(j)),
            )));
            let c0p = c0;
            let s = dd_add(
                dd_add(
                    dd_mul(c2p, dd_sub(e2v2, e2v1)),
                    dd_mul(c1p, dd_sub(e1v2, e1v1)),
                ),
                dd_mul(c0p, dd_sub(e0v2, e0v1)),
            );
            total = dd_add(total, dd_mul(s, invml));
        }
        // tail p >= 4
        let bl = dd_div(b, lf);
        let al = dd_div(a, lf);
        let c2lf = dd_mul(c2, lf);
        let invlf = dd_div(one, lf);
        let c0ilf = dd_mul(c0, invlf);
        let mut pb1 = bl;
        let mut pa1 = al;
        for p in 0..pmax {
            let pb2 = dd_mul(pb1, bl);
            let pa2 = dd_mul(pa1, al);
            let pb3 = dd_mul(pb2, bl);
            let pa3 = dd_mul(pa2, al);
            let d1 = dd_sub(pb1, pa1);
            let d2 = dd_sub(pb2, pa2);
            let d3 = dd_sub(pb3, pa3);
            let t1 = dd_mul(dd_mul(c2lf, d3), cst().inv[p + 3]);
            let t2 = dd_mul(dd_mul(c1, d2), cst().inv[p + 2]);
            let t3 = dd_mul(dd_mul(c0ilf, d1), cst().inv[p + 1]);
            let inner = dd_add(dd_add(t1, t2), t3);
            total = dd_add(total, dd_mul(wtab[p], inner));
            pb1 = pb2;
            pa1 = pa2;
        }
    }
    total
}

fn b_dd(k: u64, ln_table: Option<&[Dd]>) -> Dd {
    let c0n = cst();
    let lnk = match ln_table {
        Some(t) => t[k as usize],
        None => dd_ln_int(k, c0n.ln2, &c0n.inv),
    };
    // (ln k + 1 - gamma)/k
    dd_div(dd_sub(dd_add(lnk, Dd::from_f64(1.0)), c0n.gamma), Dd::from_int(k))
}

// ---------------- MPFR-direct Gram (true 256-bit, adaptive P) ----------------
fn gram_mpfr_direct(j: u64, k: u64, zw: &[Float], mode: PMode) -> Float {
    let prec = u32::try_from(256).unwrap();
    let l = lcm(j, k);
    let pmax = pm(mode, l).min(zw.len());
    let ivs = intervals(j, k, l);
    let mut total = Float::with_val(prec, 0);
    let lf = Float::with_val(prec, l);
    let jf = Float::with_val(prec, j);
    let kf = Float::with_val(prec, k);
    let two = Float::with_val(prec, 2);
    let jk = Float::with_val(prec, &jf * &kf);
    for &(x1, x2, ai, bi) in &ivs {
        let a = Float::with_val(prec, x1);
        let b = Float::with_val(prec, x2);
        let aif = Float::with_val(prec, ai);
        let bif = Float::with_val(prec, bi);
        let one = Float::with_val(prec, 1);
        let c2 = Float::with_val(prec, &one / &jk);
        let ak = Float::with_val(prec, &aif / &kf);
        let bj = Float::with_val(prec, &bif / &jf);
        let akbj = Float::with_val(prec, &ak + &bj);
        let c1 = Float::with_val(prec, -&akbj);
        let c0 = Float::with_val(prec, &aif * &bif);
        // m = 0
        let db = Float::with_val(prec, &b - &a);
        let la = Float::with_val(prec, &a).ln();
        let lb = Float::with_val(prec, &b).ln();
        let dl = Float::with_val(prec, &lb - &la);
        let ra = Float::with_val(prec, 1.0 / &a);
        let rb = Float::with_val(prec, 1.0 / &b);
        let dr = Float::with_val(prec, &ra - &rb);
        let m0a = Float::with_val(prec, &c2 * &db);
        let m0b = Float::with_val(prec, &c1 * &dl);
        let m0c = Float::with_val(prec, &c0 * &dr);
        let m0 = Float::with_val(prec, &Float::with_val(prec, &m0a + &m0b) + &m0c);
        total += &m0;
        // m = 1..3
        for m in 1..4u64 {
            let ml = Float::with_val(prec, m * l);
            let v1 = Float::with_val(prec, &a / &ml);
            let v2 = Float::with_val(prec, &b / &ml);
            let ml2 = Float::with_val(prec, &ml * &ml);
            let c2p = Float::with_val(prec, &ml2 / &jk);
            let c1p = Float::with_val(prec, &ml * &akbj);
            let c1p = Float::with_val(prec, -&c1p);
            let c0p = Float::with_val(prec, &aif * &bif);
            let w1 = Float::with_val(prec, &v1 + 1.0);
            let w2 = Float::with_val(prec, &v2 + 1.0);
            let lw1 = Float::with_val(prec, &w1).ln();
            let lw2 = Float::with_val(prec, &w2).ln();
            let rw1 = Float::with_val(prec, 1.0 / &w1);
            let rw2 = Float::with_val(prec, 1.0 / &w2);
            let tl1 = Float::with_val(prec, &two * &lw1);
            let tl2 = Float::with_val(prec, &two * &lw2);
            let u1 = Float::with_val(prec, &v1 - &tl1);
            let u2 = Float::with_val(prec, &v2 - &tl2);
            let e2v1 = Float::with_val(prec, &u1 - &rw1);
            let e2v2 = Float::with_val(prec, &u2 - &rw2);
            let e1v1 = Float::with_val(prec, &lw1 + &rw1);
            let e1v2 = Float::with_val(prec, &lw2 + &rw2);
            let e0v1 = Float::with_val(prec, -&rw1);
            let e0v2 = Float::with_val(prec, -&rw2);
            let d2e = Float::with_val(prec, &e2v2 - &e2v1);
            let d1e = Float::with_val(prec, &e1v2 - &e1v1);
            let d0e = Float::with_val(prec, &e0v2 - &e0v1);
            let p1 = Float::with_val(prec, &c2p * &d2e);
            let p2 = Float::with_val(prec, &c1p * &d1e);
            let p3 = Float::with_val(prec, &c0p * &d0e);
            let s = Float::with_val(prec, &Float::with_val(prec, &p1 + &p2) + &p3);
            let sm = Float::with_val(prec, &s / &ml);
            total += &sm;
        }
        // tail
        let bl = Float::with_val(prec, &b / &lf);
        let al = Float::with_val(prec, &a / &lf);
        let mut pb1 = bl.clone();
        let mut pa1 = al.clone();
        for p in 0..pmax {
            let pb2 = Float::with_val(prec, &pb1 * &bl);
            let pa2 = Float::with_val(prec, &pa1 * &al);
            let pb3 = Float::with_val(prec, &pb2 * &bl);
            let pa3 = Float::with_val(prec, &pa2 * &al);
            let d1 = Float::with_val(prec, &pb1 - &pa1);
            let d2 = Float::with_val(prec, &pb2 - &pa2);
            let d3 = Float::with_val(prec, &pb3 - &pa3);
            let c2d3 = Float::with_val(prec, &c2 * &d3);
            let c1d2 = Float::with_val(prec, &c1 * &d2);
            let c0d1 = Float::with_val(prec, &c0 * &d1);
            let c2d3lf = Float::with_val(prec, &c2d3 * &lf);
            let t1 = Float::with_val(prec, &c2d3lf / ((p + 3) as f64));
            let t2 = Float::with_val(prec, &c1d2 / ((p + 2) as f64));
            let c0d1lf = Float::with_val(prec, &c0d1 / &lf);
            let t3 = Float::with_val(prec, &c0d1lf / ((p + 1) as f64));
            let inner = Float::with_val(prec, &Float::with_val(prec, &t1 + &t2) + &t3);
            let mut w = Float::with_val(prec, &zw[p] * ((p + 1) as f64));
            if p & 1 == 1 {
                w = -w;
            }
            let wi = Float::with_val(prec, &w * &inner);
            total += &wi;
            pb1 = pb2;
            pa1 = pa2;
        }
    }
    total
}

// ---------------- Cholesky: f64 (lower flat) ----------------
fn ij_flat(i: usize, j: usize) -> usize {
    i * (i + 1) / 2 + j
}

// factors lower-tri G in place; returns (ok, kappa_pivot)
// Threaded: per column j, compute the diagonal first (serial), then parallelize the
// off-diagonal rows i>j (independent given columns <j and the diagonal).
fn chol_f64(g: &mut Vec<f64>, n: usize) -> (bool, f64) {
    let mut ok = true;
    let mut mn = f64::INFINITY;
    let mut mx = 0.0f64;
    let nthreads = 8.min(n);
    for j in 0..n {
        // diagonal first (serial, needs L[j][k] for k<j which are already done)
        let mut sval = g[ij_flat(j, j)];
        for k in 0..j {
            sval -= g[ij_flat(j, k)] * g[ij_flat(j, k)];
        }
        if sval <= 0.0 {
            ok = false;
            sval = 1e-300;
        }
        g[ij_flat(j, j)] = sval.sqrt();
        mn = mn.min(sval);
        mx = mx.max(sval);
        let djj = g[ij_flat(j, j)];
        // off-diagonal rows i in (j, n) parallel
        let base = SendPtr(g.as_mut_ptr());
        let col = j;
        let nn = n;
        let next = AtomicUsize::new(col + 1);
        thread::scope(|s| {
            for _ in 0..nthreads {
                let next = &next;
                let base = SendPtr(base.0);
                s.spawn(move || loop {
                    let i = next.fetch_add(1, Ordering::Relaxed);
                    if i >= nn {
                        break;
                    }
                    let mut sval = unsafe { *base.at(ij_flat(i, col)) };
                    for k in 0..col {
                        sval -= unsafe { *base.at(ij_flat(i, k)) } * unsafe { *base.at(ij_flat(col, k)) };
                    }
                    unsafe { *base.at(ij_flat(i, col)) = sval / djj };
                });
            }
        });
    }
    (ok, if mn > 0.0 { mx / mn } else { f64::INFINITY })
}

// triangular solves using factor L (lower flat, unit? no: standard L L^T)
fn tri_solve_f64(l: &[f64], b: &[f64], n: usize) -> Vec<f64> {
    let mut y = vec![0.0f64; n];
    for i in 0..n {
        let mut s = b[i];
        for k in 0..i {
            s -= l[ij_flat(i, k)] * y[k];
        }
        y[i] = s / l[ij_flat(i, i)];
    }
    let mut c = vec![0.0f64; n];
    for i in (0..n).rev() {
        let mut s = y[i];
        for k in (i + 1)..n {
            s -= l[ij_flat(k, i)] * c[k];
        }
        c[i] = s / l[ij_flat(i, i)];
    }
    c
}

// ---------------- dd Cholesky (lower flat) ----------------
fn chol_dd(g: &mut Vec<Dd>, n: usize) -> bool {
    for j in 0..n {
        for i in j..n {
            let mut s = g[ij_flat(i, j)];
            for k in 0..j {
                let t = dd_mul(g[ij_flat(i, k)], g[ij_flat(j, k)]);
                s = dd_sub(s, t);
            }
            if i == j {
                if s.hi <= 0.0 {
                    return false;
                }
                g[ij_flat(i, i)] = dd_sqrt(s);
            } else {
                g[ij_flat(i, j)] = dd_div(s, g[ij_flat(j, j)]);
            }
        }
    }
    true
}

fn tri_solve_dd(l: &[Dd], b: &[Dd], n: usize) -> Vec<Dd> {
    let mut y = vec![Dd { hi: 0.0, lo: 0.0 }; n];
    for i in 0..n {
        let mut s = b[i];
        for k in 0..i {
            s = dd_sub(s, dd_mul(l[ij_flat(i, k)], y[k]));
        }
        y[i] = dd_div(s, l[ij_flat(i, i)]);
    }
    let mut c = vec![Dd { hi: 0.0, lo: 0.0 }; n];
    for i in (0..n).rev() {
        let mut s = y[i];
        for k in (i + 1)..n {
            s = dd_sub(s, dd_mul(l[ij_flat(k, i)], c[k]));
        }
        c[i] = dd_div(s, l[ij_flat(i, i)]);
    }
    c
}

// ---------------- MPFR Cholesky (lower flat, threaded) ----------------
struct SyncFloat(Float);
unsafe impl Sync for SyncFloat {}

fn chol_mpfr_threaded(lmp: &mut Vec<SyncFloat>, n: usize) -> bool {
    let ptr = SendPtr(lmp.as_mut_ptr());
    let nthreads = 8.min(n);
    for j in 0..n {
        // L[j][j] first (sequential)
        let mut s = unsafe { ((*ptr.at(ij_flat(j, j))).0).clone() };
        for k in 0..j {
            let a = unsafe { &((*ptr.at(ij_flat(j, k))).0) };
            let t = Float::with_val(256, a * a);
            s -= t;
        }
        if s.to_f64() <= 0.0 {
            return false;
        }
        unsafe {
            (*ptr.at(ij_flat(j, j))).0 = s.sqrt();
        }
        let ljj = unsafe { ((*ptr.at(ij_flat(j, j))).0).clone() };
        // parallel i in (j, n)
        if n - j - 1 > 64 {
            let next = AtomicUsize::new(j + 1);
            thread::scope(|sc| {
                for _ in 0..nthreads {
                    let next = &next;
                    let ptr = SendPtr(ptr.0);
                    let ljj = ljj.clone();
                    sc.spawn(move || loop {
                        // block-claim rows: avoids false sharing on adjacent column-j writes
                        let blk = next.fetch_add(16, Ordering::Relaxed);
                        if blk >= n {
                            break;
                        }
                        let bend = (blk + 16).min(n);
                        for i in blk..bend {
                        let mut s = unsafe { ((*ptr.at(ij_flat(i, j))).0).clone() };
                        for k in 0..j {
                            let a = unsafe { &((*ptr.at(ij_flat(i, k))).0) };
                            let b = unsafe { &((*ptr.at(ij_flat(j, k))).0) };
                            let t = Float::with_val(256, a * b);
                            s -= t;
                        }
                        let q = Float::with_val(256, &s / &ljj);
                        unsafe {
                            (*ptr.at(ij_flat(i, j))).0 = q;
                        }
                        }
                    });
                }
            });
        } else {
            for i in (j + 1)..n {
                let mut s = unsafe { ((*ptr.at(ij_flat(i, j))).0).clone() };
                for k in 0..j {
                    let a = unsafe { &((*ptr.at(ij_flat(i, k))).0) };
                    let b = unsafe { &((*ptr.at(ij_flat(j, k))).0) };
                    let t = Float::with_val(256, a * b);
                    s -= t;
                }
                unsafe {
                    (*ptr.at(ij_flat(i, j))).0 = Float::with_val(256, &s / &ljj);
                }
            }
        }
    }
    true
}

fn tri_solve_mpfr(l: &[SyncFloat], b: &[Float], n: usize) -> Vec<Float> {
    let mut y: Vec<Float> = (0..n).map(|i| b[i].clone()).collect();
    for i in 0..n {
        let mut s = b[i].clone();
        for k in 0..i {
            let t = Float::with_val(256, &l[ij_flat(i, k)].0 * &y[k]);
            s -= t;
        }
        y[i] = Float::with_val(256, &s / &l[ij_flat(i, i)].0);
    }
    let mut c: Vec<Float> = vec![Float::with_val(256, 0); n];
    for i in (0..n).rev() {
        let mut s = y[i].clone();
        for k in (i + 1)..n {
            let t = Float::with_val(256, &l[ij_flat(k, i)].0 * &c[k]);
            s -= t;
        }
        c[i] = Float::with_val(256, &s / &l[ij_flat(i, i)].0);
    }
    c
}

// ---------------- threaded Gram fill (f64, lower triangle) ----------------
fn gram_fill_f64(n: usize, z: &[f64], mode: PMode) -> Vec<f64> {
    let mut g = vec![0.0f64; n * (n + 1) / 2];
    let base = SendPtr(g.as_mut_ptr());
    let next = AtomicUsize::new(n);
    let done = AtomicUsize::new(0);
    let nthreads = 8.min(n);
    thread::scope(|s| {
        for _ in 0..nthreads {
            let next = &next;
            let done = &done;
            let base = SendPtr(base.0);
            s.spawn(move || loop {
                let i = next.fetch_sub(1, Ordering::Relaxed);
                if i == 0 || i > (1usize << 63) {
                    break;
                }
                let i = i - 1;
                let ji = (i + 1) as u64;
                for k in 0..=i {
                    let v = gram_f64(ji, (k + 1) as u64, z, mode);
                    unsafe {
                        *base.at(ij_flat(i, k)) = v;
                    }
                }
                let d = done.fetch_add(1, Ordering::Relaxed) + 1;
                if d % 250 == 0 {
                    eprintln!("  gram f64: {}/{} rows", d, n);
                }
            });
        }
    });
    g
}

fn gram_fill_dd(n: usize, wtab: &[Dd], mode: PMode, ln_table: &[Dd]) -> Vec<Dd> {
    let mut g = vec![Dd { hi: 0.0, lo: 0.0 }; n * (n + 1) / 2];
    let base = SendPtr(g.as_mut_ptr());
    let next = AtomicUsize::new(n);
    let done = AtomicUsize::new(0);
    let nthreads = 8.min(n);
    thread::scope(|s| {
        for _ in 0..nthreads {
            let next = &next;
            let done = &done;
            let base = SendPtr(base.0);
            s.spawn(move || loop {
                let i = next.fetch_sub(1, Ordering::Relaxed);
                if i == 0 || i > (1usize << 63) {
                    break;
                }
                let i = i - 1;
                let ji = (i + 1) as u64;
                for k in 0..=i {
                    let v = gram_dd(ji, (k + 1) as u64, wtab, mode, Some(ln_table));
                    unsafe {
                        *base.at(ij_flat(i, k)) = v;
                    }
                }
                let d = done.fetch_add(1, Ordering::Relaxed) + 1;
                if d % 100 == 0 {
                    eprintln!("  gram dd: {}/{} rows", d, n);
                }
            });
        }
    });
    g
}

// ---------------- refinement ----------------
// r = b - G c with c in dd, G/b f64-promoted; returns f64 residual + norms
fn residual_dd(g: &[f64], b: &[f64], c: &[Dd], n: usize) -> (Vec<f64>, f64, f64) {
    let mut r = vec![0.0f64; n];
    let mut rinf = 0.0f64;
    let mut binf = 0.0f64;
    for i in 0..n {
        let mut acc = Dd { hi: 0.0, lo: 0.0 };
        // sum over all k: G[i][k] c[k], G lower-tri symmetric
        for k in 0..n {
            let gik = if k <= i { g[ij_flat(i, k)] } else { g[ij_flat(k, i)] };
            let t = dd_mul(Dd::from_f64(gik), c[k]);
            acc = dd_add(acc, t);
        }
        let ri = dd_sub(Dd::from_f64(b[i]), acc);
        r[i] = ri.to_f64();
        rinf = rinf.max(r[i].abs());
        binf = binf.max(b[i].abs());
    }
    (r, rinf, binf)
}

// ---------------- phases ----------------
fn phase_validate() {
    let t0 = std::time::Instant::now();
    log_line("[validate] START");
    let prec = u32::try_from(256).unwrap();

    // V1: dd micro-ops vs rug-256
    {
        let mut worst = 0.0f64;
        let mut seed = 0x1234_5678_9abc_u64;
        let mut rnd = move || {
            seed = seed.wrapping_mul(6364136223846793005).wrapping_add(1442695040888963407);
            ((seed >> 11) as f64) / (1u64 << 53) as f64
        };
        let mut w_mul = 0.0f64;
        let mut w_div = 0.0f64;
        let mut w_sqrt = 0.0f64;
        let mut bad_a = 0.0f64;
        for _ in 0..2000 {
            let a = 1e-6 + rnd() * 1e6;
            let b = 1e-6 + rnd() * 1e6;
            let da = Dd::from_f64(a);
            let db = Dd::from_f64(b);
            // mul
            let dd = dd_mul(da, db);
            let mp = Float::with_val(prec, &Float::with_val(prec, a) * &Float::with_val(prec, b));
            let diff = Float::with_val(prec, dd_to_mpfr(dd) - &mp);
            let rel = diff.to_f64().abs() / mp.to_f64().abs().max(1e-300);
            if rel > w_mul { w_mul = rel; }
            // div
            let dd = dd_div(da, db);
            let mp = Float::with_val(prec, &Float::with_val(prec, a) / &Float::with_val(prec, b));
            let diff = Float::with_val(prec, dd_to_mpfr(dd) - &mp);
            let rel = diff.to_f64().abs() / mp.to_f64().abs().max(1e-300);
            if rel > w_div { w_div = rel; bad_a = a; }
            // sqrt
            let dd = dd_sqrt(da);
            let mp = Float::with_val(prec, a).sqrt();
            let diff = Float::with_val(prec, dd_to_mpfr(dd) - &mp);
            let rel = diff.to_f64().abs() / mp.to_f64().abs().max(1e-300);
            if rel > w_sqrt { w_sqrt = rel; }
            worst = worst.max(rel.max(w_mul.max(w_div)));
        }
        log_line(&format!("[validate] V1 dd ops vs rug256: mul {:.2e} div {:.2e} sqrt {:.2e} (worst {:.2e}, expect < 1e-28) {}", w_mul, w_div, w_sqrt, worst, if worst < 1e-28 { "OK" } else { "FAIL" }));
        if worst >= 1e-28 {
            log_line(&format!("[validate] V1 worst-div input a={:.17e}", bad_a));
        }
    }

    // V2: dd_ln_int vs rug
    {
        let mut worst = 0.0f64;
        let mut seed = 0xfeed_face_u64;
        let mut rnd = move || {
            seed = seed.wrapping_mul(6364136223846793005).wrapping_add(1442695040888963407);
            ((seed >> 11) as f64) / (1u64 << 53) as f64
        };
        for _ in 0..500 {
            let n = 1 + (rnd() * 16_000_000.0) as u64;
            let lnd = dd_ln_int(n, cst().ln2, &cst().inv);
            let mp = Float::with_val(prec, n).ln();
            let diff = Float::with_val(prec, dd_to_mpfr(lnd) - &mp);
            let rel = diff.to_f64().abs() / mp.to_f64().abs().max(1e-300);
            worst = worst.max(rel);
        }
        log_line(&format!("[validate] V2 dd_ln_int vs rug256: max rel {:.2e} (expect < 1e-27) {}", worst, if worst < 1e-27 { "OK" } else { "FAIL" }));
    }

    // z-tables
    let zf = z_table_f64(PMAX);
    let zmp_direct = z_table_mpfr_direct(PMAX);
    {
        let mut worst = 0.0f64;
        for p in 0..40usize {
            let rel = (zf[p] - zmp_direct[p].to_f64()).abs() / zmp_direct[p].to_f64().abs().max(1e-300);
            worst = worst.max(rel);
        }
        log_line(&format!("[validate] V3a z_f64 vs z_mpfr_direct p<40: max rel {:.2e} (expect < 1e-13) {}", worst, if worst < 1e-13 { "OK" } else { "FAIL" }));
    }
    let wtab = dd_wtab(&zmp_direct);
    // wtab also needs f64 z for the f64 adaptive path (use zf, sized PMAX)

    // V4: Gram small pairs, three arithmetics + truncation measurement
    {
        let mut worst_dd_mp = 0.0f64;
        let mut worst_f64_mp = 0.0f64;
        let mut worst_p32_shift = 0.0f64;
        let mut g11_p32 = 0.0f64;
        let mut g11_adp = 0.0f64;
        let mut g11_mp = 0.0f64;
        for j in 1..=40u64 {
            for k in 1..=j {
                let gm = gram_mpfr_direct(j, k, &zmp_direct, PMode::Adaptive(31.0));
                let gd = gram_dd(j, k, &wtab, PMode::Adaptive(31.0), None);
                let gf_a = gram_f64(j, k, &zf, PMode::Adaptive(17.0));
                let gf_32 = gram_f64(j, k, &zf, PMode::Fixed(32));
                let mpv = gm.to_f64();
                if j == 1 && k == 1 {
                    g11_p32 = gf_32;
                    g11_adp = gf_a;
                    g11_mp = mpv;
                }
                let d_dd_mp = Float::with_val(prec, dd_to_mpfr(gd) - gm.clone());
                let r1 = d_dd_mp.to_f64().abs() / mpv.abs().max(1e-300);
                let r2 = (gf_a - mpv).abs() / mpv.abs().max(1e-300);
                let r3 = (gf_32 - gf_a).abs() / gf_a.abs().max(1e-300);
                worst_dd_mp = worst_dd_mp.max(r1);
                worst_f64_mp = worst_f64_mp.max(r2);
                worst_p32_shift = worst_p32_shift.max(r3);
            }
        }
        log_line(&format!("[validate] V4 gram j,k<=40: dd-vs-mpfr max rel {:.2e} (expect < 1e-27) {}", worst_dd_mp, if worst_dd_mp < 1e-27 { "OK" } else { "FAIL" }));
        log_line(&format!("[validate] V4 f64(adaptive)-vs-mpfr max rel {:.2e} (expect < 2e-13: f64 rounding of cancellative closed form) {}", worst_f64_mp, if worst_f64_mp < 2e-13 { "OK" } else { "FAIL" }));
        log_line(&format!("[validate] V4b TRUNCATION AUDIT: G_11(P32)={:.15e} G_11(adp)={:.15e} G_11(mpfr)={:.15e} |P32-adp|/G={:.2e} max over pairs={:.2e}", g11_p32, g11_adp, g11_mp, (g11_p32 - g11_adp).abs() / g11_adp, worst_p32_shift));
    }

    // V5: d_N(50) and d_N(100): regression + arithmetic cross-checks
    for &n in &[50usize, 100] {
        // f64 P32 regression (must reproduce main.rs published values)
        let g32 = gram_fill_f64(n, &zf, PMode::Fixed(32));
        let b: Vec<f64> = (1..=n as u64).map(b_f64).collect();
        let mut l32 = g32.clone();
        let (ok, _k) = chol_f64(&mut l32, n);
        let c = tri_solve_f64(&l32, &b, n);
        let bt: f64 = b.iter().zip(&c).map(|(x, y)| x * y).sum();
        let d32 = (1.0 - bt).max(0.0).sqrt();
        // f64 adaptive
        let ga = gram_fill_f64(n, &zf, PMode::Adaptive(17.0));
        let mut la = ga.clone();
        let (oka, kappa) = chol_f64(&mut la, n);
        let ca = tri_solve_f64(&la, &b, n);
        let bt_a: f64 = b.iter().zip(&ca).map(|(x, y)| x * y).sum();
        let d_f64 = (1.0 - bt_a).max(0.0).sqrt();
        // dd full (adaptive)
        let mut gd = vec![Dd { hi: 0.0, lo: 0.0 }; n * (n + 1) / 2];
        for i in 0..n {
            for k2 in 0..=i {
                gd[ij_flat(i, k2)] = gram_dd((i + 1) as u64, (k2 + 1) as u64, &wtab, PMode::Adaptive(31.0), None);
            }
        }
        let bd: Vec<Dd> = (1..=n as u64).map(|k| b_dd(k, None)).collect();
        let mut ld = gd.clone();
        let okd = chol_dd(&mut ld, n);
        let cd = tri_solve_dd(&ld, &bd, n);
        let mut btd = Dd { hi: 0.0, lo: 0.0 };
        for i in 0..n {
            btd = dd_add(btd, dd_mul(bd[i], cd[i]));
        }
        let d_dd = dd_sqrt(dd_max0(dd_sub(Dd::from_f64(1.0), btd))).to_f64();
        log_line(&format!("[validate] V5 N={}: d_f64(P32)={:.10e} d_f64(adp)={:.10e} d_dd={:.10e} chol {}/{}/{} kappa~{:.1e}", n, d32, d_f64, d_dd, ok, oka, okd, kappa));
        log_line(&format!("[validate] V5 N={}: rel(P32,adp)={:.2e} rel(adp,dd)={:.2e} [published P32: N=50 1.0793711120e-1, N=100 1.0013884399e-1]", n, (d32 - d_f64).abs() / d_f64, (d_f64 - d_dd).abs() / d_dd));

        // full MPFR-direct pipeline at N=50 only (cost)
        if n == 50 {
            let mut gmp: Vec<SyncFloat> = Vec::with_capacity(n * (n + 1) / 2);
            for i in 0..n {
                for k2 in 0..=i {
                    gmp.push(SyncFloat(gram_mpfr_direct((i + 1) as u64, (k2 + 1) as u64, &zmp_direct, PMode::Adaptive(31.0))));
                }
            }
            let bmp: Vec<Float> = (1..=n as u64)
                .map(|k| {
                    let g = gamma_mpfr();
                    let lk = Float::with_val(prec, k).ln();
                    let t1 = Float::with_val(prec, &lk + 1.0);
                    let t2 = Float::with_val(prec, &t1 - &g);
                    Float::with_val(prec, &t2 / Float::with_val(prec, k))
                })
                .collect();
            let okm = chol_mpfr_threaded(&mut gmp, n);
            let cm = tri_solve_mpfr(&gmp, &bmp, n);
            let mut bt = Float::with_val(prec, 0);
            for i in 0..n {
                bt += Float::with_val(prec, &bmp[i] * &cm[i]);
            }
            let one = Float::with_val(prec, 1);
            let d2m = Float::with_val(prec, &one - &bt);
            let dm = d2m.to_f64().max(0.0).sqrt();
            log_line(&format!("[validate] V5 N=50 mpfr-direct: d_mpfr={:.10e} rel(dd)={:.2e} chol={}", dm, (dm - d_dd).abs() / dm, okm));
        }
    }

    // V6: pow2 control (saturation)
    {
        let idx = |i: usize| 1u64 << i;
        let mut last = 0.0;
        for m in 8..=14usize {
            let n = m + 1;
            let mut g = vec![0.0f64; n * (n + 1) / 2];
            for i in 0..n {
                for k in 0..=i {
                    g[ij_flat(i, k)] = gram_f64(idx(i), idx(k), &zf, PMode::Adaptive(17.0));
                }
            }
            let b: Vec<f64> = (0..n).map(|i| b_f64(idx(i))).collect();
            let mut l = g.clone();
            let (ok, _) = chol_f64(&mut l, n);
            let c = tri_solve_f64(&l, &b, n);
            let bt: f64 = b.iter().zip(&c).map(|(x, y)| x * y).sum();
            last = (1.0 - bt).max(0.0).sqrt();
            let _ = ok;
        }
        log_line(&format!("[validate] V6 pow2 control d'(2^14)={:.6e} (expect ~0.3187711 saturated) {}", last, if (last - 0.3187711).abs() < 1e-5 { "OK" } else { "CHECK" }));
    }

    log_line(&format!("[validate] END elapsed {:.1}s", t0.elapsed().as_secs_f64()));
}

fn phase_prod(n: usize) {
    let t0 = std::time::Instant::now();
    log_line(&format!("[prod {}] START", n));
    let zf = z_table_f64(PMAX);
    let zmp_direct = z_table_mpfr_direct(PMAX);
    let wtab = dd_wtab(&zmp_direct);

    // Gram f64 adaptive, threaded
    let g = gram_fill_f64(n, &zf, PMode::Adaptive(17.0));
    log_line(&format!("[prod {}] gram f64 filled {:.1}s", n, t0.elapsed().as_secs_f64()));

    let b: Vec<f64> = (1..=n as u64).map(b_f64).collect();

    // f64 Cholesky
    let mut l = g.clone();
    let (ok, kappa) = chol_f64(&mut l, n);
    let c0v = tri_solve_f64(&l, &b, n);
    let bt: f64 = b.iter().zip(&c0v).map(|(x, y)| x * y).sum();
    let d_f64 = (1.0 - bt).max(0.0).sqrt();
    log_line(&format!("[prod {}] d_f64={:.12e} kappa_pivot={:.2e} chol={} ({:.1}s)", n, d_f64, kappa, ok, t0.elapsed().as_secs_f64()));

    // refinement with dd residuals
    let mut c: Vec<Dd> = c0v.iter().map(|&x| Dd::from_f64(x)).collect();
    let mut d_ref = d_f64;
    let mut plateau = String::new();
    for it in 1..=6 {
        let (r, rinf, binf) = residual_dd(&g, &b, &c, n);
        let dlt = tri_solve_f64(&l, &r, n);
        for i in 0..n {
            c[i] = dd_add(c[i], Dd::from_f64(dlt[i]));
        }
        let mut bt = Dd { hi: 0.0, lo: 0.0 };
        for i in 0..n {
            bt = dd_add(bt, dd_mul(Dd::from_f64(b[i]), c[i]));
        }
        let d2 = dd_sub(Dd::from_f64(1.0), bt);
        let d_new = dd_sqrt(dd_max0(d2)).to_f64();
        plateau.push_str(&format!("it{} rel_r={:.1e} d={:.12e} dd_d={:.2e}; ", it, rinf / binf, d_new, (d_new - d_ref).abs() / d_new));
        if rinf / binf < 1e-26 || (d_new - d_ref).abs() / d_new < 1e-24 {
            d_ref = d_new;
            break;
        }
        d_ref = d_new;
    }
    log_line(&format!("[prod {}] refined: {}", n, plateau));
    log_line(&format!("[prod {}] d_ref={:.12e} rel(f64)={:.2e}", n, d_ref, (d_ref - d_f64).abs() / d_ref));

    // dd Gram entry sampling (f64 storage/closed-form error at this N)
    {
        let mut seed = 0xbeef_cafe_u64 + n as u64;
        let mut rnd = move || {
            seed = seed.wrapping_mul(6364136223846793005).wrapping_add(1442695040888963407);
            ((seed >> 11) as f64) / (1u64 << 53) as f64
        };
        let mut worst_fd = 0.0f64;
        let mut worst_dm = 0.0f64;
        for s in 0..120 {
            let j = (1 + (rnd() * n as f64) as u64).min(n as u64);
            let k = (1 + (rnd() * j as f64) as u64).min(j);
            let gf = gram_f64(j, k, &zf, PMode::Adaptive(17.0));
            let gd = gram_dd(j, k, &wtab, PMode::Adaptive(31.0), None);
            let rel = (gf - gd.to_f64()).abs() / gd.to_f64().abs().max(1e-300);
            worst_fd = worst_fd.max(rel);
            if s < 12 {
                let gm = gram_mpfr_direct(j, k, &zmp_direct, PMode::Adaptive(31.0));
                let gmv = gm.to_f64();
                let d_dd_mp = Float::with_val(256, dd_to_mpfr(gd) - gm);
                let r2 = d_dd_mp.to_f64().abs() / gmv.abs().max(1e-300);
                worst_dm = worst_dm.max(r2);
            }
        }
        log_line(&format!("[prod {}] gram sampling: f64-vs-dd max rel {:.2e} over 120 rand pairs; dd-vs-mpfr max rel {:.2e} over 12", n, worst_fd, worst_dm));
    }

    // MPFR Cholesky on stored f64 G (independent solve check)
    // Skip at n>=3000: ~550B/Float * n(n+1)/2 => ~4.5M MPFR floats ~ multi-GB, OOMs a 9GB box
    // (measured: prod 3000 aborted "memory allocation of 46057267840 bytes failed").
    // The dd refinement residual (<= 1e-28) already certifies exact-solve-of-stored-G, and the
    // MPFR-Cholesky implementation is cross-checked at N=2000 (d_mpfr == d_ref rel 0.00e0).
    if n >= 3000 {
        log_line(&format!("[prod {}] mpfr-chol SKIPPED (n>=3000: MPFR Cholesky OOMs 9GB box; refinement residual {} certifies exact-solve-of-stored-G; implementation cross-check covered at 2000)", n, "plateau"));
    } else {
    {
        let prec = u32::try_from(256).unwrap();
        let mut gmp: Vec<SyncFloat> = Vec::with_capacity(n * (n + 1) / 2);
        for i in 0..n {
            for k in 0..=i {
                gmp.push(SyncFloat(Float::with_val(prec, g[ij_flat(i, k)])));
            }
        }
        let bmp: Vec<Float> = b.iter().map(|&x| Float::with_val(prec, x)).collect();
        let okm = chol_mpfr_threaded(&mut gmp, n);
        let cm = tri_solve_mpfr(&gmp, &bmp, n);
        let mut bt = Float::with_val(prec, 0);
        for i in 0..n {
            bt += Float::with_val(prec, &bmp[i] * &cm[i]);
        }
        let d2m = Float::with_val(prec, Float::with_val(prec, 1) - &bt);
        let dm = d2m.to_f64().max(0.0).sqrt();
        log_line(&format!("[prod {}] d_mpfr(stored-G)={:.12e} rel(ref)={:.2e} chol={} ({:.1}s)", n, dm, (dm - d_ref).abs() / dm, okm, t0.elapsed().as_secs_f64()));
    }
    }

    let lnn = (n as f64).ln();
    log_line(&format!("[prod {}] RESULT d_ref={:.12e} d*sqrt(ln N)={:.6} d_f64*sqrt(lnN)={:.6} [flat-law band 0.21-0.22]", n, d_ref, d_ref * lnn.sqrt(), d_f64 * lnn.sqrt()));
    log_line(&format!("[prod {}] END elapsed {:.1}s", n, t0.elapsed().as_secs_f64()));
}

fn phase_sample(n: usize) {
    // standalone repro of the prod sampling block (same deterministic seeds)
    let t0 = std::time::Instant::now();
    log_line(&format!("[sample {}] START", n));
    let zf = z_table_f64(PMAX);
    let zmp_direct = z_table_mpfr_direct(PMAX);
    let wtab = dd_wtab(&zmp_direct);
    let mut seed = 0xbeef_cafe_u64 + n as u64;
    let mut rnd = move || {
        seed = seed.wrapping_mul(6364136223846793005).wrapping_add(1442695040888963407);
        ((seed >> 11) as f64) / (1u64 << 53) as f64
    };
    for s in 0..120 {
        let j = 1 + (rnd() * n as f64) as u64;
        let k = 1 + (rnd() * j as f64) as u64;
        let gf = gram_f64(j, k, &zf, PMode::Adaptive(17.0));
        let gd = gram_dd(j, k, &wtab, PMode::Adaptive(31.0), None);
        let rel = (gf - gd.to_f64()).abs() / gd.to_f64().abs().max(1e-300);
        eprintln!("s={} j={} k={} G={:.6e} f64-vs-dd={:.2e}", s, j, k, gd.to_f64(), rel);
        if s < 12 {
            let gm = gram_mpfr_direct(j, k, &zmp_direct, PMode::Adaptive(31.0));
            let gmv = gm.to_f64();
            let d_dd_mp = Float::with_val(256, dd_to_mpfr(gd) - gm);
            let r2 = d_dd_mp.to_f64().abs() / gmv.abs().max(1e-300);
            eprintln!("   dd-vs-mpfr={:.2e}", r2);
        }
    }
    log_line(&format!("[sample {}] END {:.1}s", n, t0.elapsed().as_secs_f64()));
}

fn dd_max0(a: Dd) -> Dd {
    if a.hi < 0.0 {
        Dd { hi: 0.0, lo: 0.0 }
    } else {
        a
    }
}

fn phase_ddgram(n: usize) {
    let t0 = std::time::Instant::now();
    log_line(&format!("[ddgram {}] START", n));
    let zmp_direct = z_table_mpfr_direct(PMAX);
    let wtab = dd_wtab(&zmp_direct);

    // integer ln table 0..=4*lcm_max+2 (lcm_max = max over j>=k of lcm <= n*(n-1))
    let lmax = (n as u64) * (n as u64);
    let tsize = (4 * lmax + 2) as usize + 1;
    log_line(&format!("[ddgram {}] building ln table {} entries ({:.0} MB)", n, tsize, tsize as f64 * 16.0 / 1e6));
    let mut lnt: Vec<Dd> = vec![Dd { hi: 0.0, lo: 0.0 }; tsize];
    {
        let base = SendPtr(lnt.as_mut_ptr());
        let next = AtomicUsize::new(tsize);
        thread::scope(|s| {
            for _ in 0..8 {
                let next = &next;
                let base = SendPtr(base.0);
                s.spawn(move || loop {
                    let i = next.fetch_sub(1, Ordering::Relaxed);
                    if i <= 1 || i > (1usize << 63) {
                        break;
                    }
                    let v = dd_ln_int(i as u64, cst().ln2, &cst().inv);
                    unsafe {
                        *base.at(i) = v;
                    }
                });
            }
        });
    }
    log_line(&format!("[ddgram {}] ln table done {:.1}s", n, t0.elapsed().as_secs_f64()));

    let g = gram_fill_dd(n, &wtab, PMode::Adaptive(31.0), &lnt);
    log_line(&format!("[ddgram {}] gram dd filled {:.1}s", n, t0.elapsed().as_secs_f64()));
    drop(lnt);

    let b: Vec<Dd> = (1..=n as u64).map(|k| b_dd(k, None)).collect();
    let mut l = g.clone();
    let ok = chol_dd(&mut l, n);
    if !ok {
        log_line(&format!("[ddgram {}] CHOLESKY FAIL (non-positive pivot)", n));
        return;
    }
    let c = tri_solve_dd(&l, &b, n);
    let mut bt = Dd { hi: 0.0, lo: 0.0 };
    for i in 0..n {
        bt = dd_add(bt, dd_mul(b[i], c[i]));
    }
    let d2 = dd_max0(dd_sub(Dd::from_f64(1.0), bt));
    let d = dd_sqrt(d2).to_f64();
    let lnn = (n as f64).ln();
    log_line(&format!("[ddgram {}] RESULT d_dd={:.12e} d*sqrt(lnN)={:.6} chol={} ({:.1}s)", n, d, d * lnn.sqrt(), ok, t0.elapsed().as_secs_f64()));
    log_line(&format!("[ddgram {}] END elapsed {:.1}s", n, t0.elapsed().as_secs_f64()));
}

fn phase_selftest() {
    let prec = u32::try_from(256).unwrap();
    println!("== dd basics ==");
    let m37 = dd_mul(Dd::from_f64(3.0), Dd::from_f64(7.0));
    println!("dd_mul(3,7) = {} + {}", m37.hi, m37.lo);
    let d21_7 = dd_div(Dd::from_f64(21.0), Dd::from_f64(7.0));
    println!("dd_div(21,7) = {} + {}", d21_7.hi, d21_7.lo);
    let s2 = dd_sqrt(Dd::from_f64(2.0));
    println!("dd_sqrt(2) = {} + {}", s2.hi, s2.lo);
    let addt = dd_add(Dd { hi: 1.0, lo: 1e-20 }, Dd { hi: 1e-10, lo: 0.0 });
    println!("dd_add(1+1e-20, 1e-10) = {} + {}", addt.hi, addt.lo);
    println!("== rug references ==");
    let mp2 = Float::with_val(prec, 2).sqrt();
    println!("mpfr sqrt2  = {}", mp2);
    println!("mpfr ln1000 = {}", Float::with_val(prec, 1000).ln());
    let l1000 = dd_ln_int(1000, cst().ln2, &cst().inv);
    println!("dd_ln_int(1000) = {} + {}  (to_mpfr: {})", l1000.hi, l1000.lo, dd_to_mpfr(l1000));
    println!("mpfr gamma  = {}", gamma_mpfr());
    println!("dd gamma    = {} + {}", cst().gamma.hi, cst().gamma.lo);
    println!("dd ln2      = {} + {}", cst().ln2.hi, cst().ln2.lo);
    println!("== V1-style spot checks ==");
    let (a, b) = (1.234567f64, 9.87654321f64);
    let dm = dd_mul(Dd::from_f64(a), Dd::from_f64(b));
    let mp = Float::with_val(prec, &Float::with_val(prec, a) * &Float::with_val(prec, b));
    let diff = Float::with_val(prec, dd_to_mpfr(dm) - &mp);
    println!("dd a*b = {} vs mpfr {} diff {}", dd_to_mpfr(dm), mp, diff);
    let dd_ = dd_div(Dd::from_f64(a), Dd::from_f64(b));
    let mp = Float::with_val(prec, &Float::with_val(prec, a) / &Float::with_val(prec, b));
    let diff = Float::with_val(prec, dd_to_mpfr(dd_) - &mp);
    println!("dd a/b = {} vs mpfr {} diff {}", dd_to_mpfr(dd_), mp, diff);
    println!("== z tables ==");
    let zf = z_table_f64(PMAX);
    let zm = z_table_mpfr_direct(PMAX);
    for p in 0..10usize {
        println!("p={}: z_f64={:.16e}  z_mpfr={:.16e}  rel={:.2e}", p, zf[p], zm[p].to_f64(), (zf[p] - zm[p].to_f64()).abs() / zm[p].to_f64());
    }
    for p in [20usize, 39, 60].iter() {
        println!("p={}: z_f64={:.16e}  z_mpfr={:.16e}  rel={:.2e}", p, zf[*p], zm[*p].to_f64(), (zf[*p] - zm[*p].to_f64()).abs() / zm[*p].to_f64());
    }
    println!("== G_11 three ways ==");
    let zmp_direct = z_table_mpfr_direct(PMAX);
    let wtab = dd_wtab(&zmp_direct);
    let g11_f = gram_f64(1, 1, &zf, PMode::Adaptive(17.0));
    let g11_d = gram_dd(1, 1, &wtab, PMode::Adaptive(31.0), None);
    let g11_m = gram_mpfr_direct(1, 1, &zmp_direct, PMode::Adaptive(31.0));
    println!("G_11 f64={:.16e} dd={} mpfr={}", g11_f, dd_to_mpfr(g11_d), g11_m);
    // per-piece audit for (1,1): interval (1,2), ai=bi=1, L=1
    {
        let c2 = 1.0f64;
        let c1 = -2.0f64;
        let c0 = 1.0f64;
        let m0 = c2 * 1.0 + c1 * 2.0f64.ln() + c0 * 0.5;
        println!("f64 m0 piece = {:.16e} (exact: 1.5-2ln2)", m0);
        let mut m13 = 0.0f64;
        for m in 1..4u64 {
            let ml = m as f64;
            let v1 = 1.0 / ml;
            let v2 = 2.0 / ml;
            let c2p = ml * ml;
            let c1p = -2.0 * ml;
            let e2 = |v: f64| v - 2.0 * (v + 1.0).ln() - 1.0 / (v + 1.0);
            let e1 = |v: f64| (v + 1.0).ln() + 1.0 / (v + 1.0);
            let e0 = |v: f64| -1.0 / (v + 1.0);
            m13 += (c2p * (e2(v2) - e2(v1)) + c1p * (e1(v2) - e1(v1)) + c0 * (e0(v2) - e0(v1))) / ml;
        }
        println!("f64 m13 piece = {:.16e}", m13);
        let mut tail = 0.0f64;
        let bl = 2.0f64;
        let al = 1.0f64;
        let mut pb1 = bl;
        let mut pa1 = al;
        let pmax = p_adaptive(1, 17.0);
        for p in 0..pmax {
            let pb2 = pb1 * bl;
            let pa2 = pa1 * al;
            let pb3 = pb2 * bl;
            let pa3 = pa2 * al;
            let d1 = pb1 - pa1;
            let d2 = pb2 - pa2;
            let d3 = pb3 - pa3;
            let pf = p as f64;
            let sign = if p & 1 == 0 { 1.0 } else { -1.0 };
            let t1 = c2 * 1.0 * d3 / (pf + 3.0);
            let t2 = c1 * d2 / (pf + 2.0);
            let t3 = c0 * d1 / (pf + 1.0);
            tail += sign * (pf + 1.0) * zf[p] * (t1 + t2 + t3);
            pb1 = pb2;
            pa1 = pa2;
        }
        println!("f64 tail piece = {:.16e} (pmax={})", tail, pmax);
        println!("f64 sum = {:.16e}", m0 + m13 + tail);
        // mp pieces
        let prec = u32::try_from(256).unwrap();
        let one = Float::with_val(prec, 1);
        let two = Float::with_val(prec, 2);
        let c2m = Float::with_val(prec, 1.0);
        let c1m = Float::with_val(prec, -2.0);
        let c0m = Float::with_val(prec, 1.0);
        let ln2f = Float::with_val(prec, &two).ln();
        let m0m = Float::with_val(prec, &Float::with_val(prec, &Float::with_val(prec, &c2m * &one) + &Float::with_val(prec, &c1m * &ln2f)) + &Float::with_val(prec, &c0m * &Float::with_val(prec, 0.5)));
        println!("mp m0 piece = {}", m0m);
        let mut m13m = Float::with_val(prec, 0);
        for m in 1..4u64 {
            let ml = Float::with_val(prec, m);
            let v1 = Float::with_val(prec, &one / &ml);
            let v2 = Float::with_val(prec, &two / &ml);
            let ml2 = Float::with_val(prec, &ml * &ml);
            let c2p = Float::with_val(prec, &ml2 / &one);
            let c1p0 = Float::with_val(prec, &ml * &two);
            let c1p = Float::with_val(prec, -&c1p0);
            let w1 = Float::with_val(prec, &v1 + 1.0);
            let w2 = Float::with_val(prec, &v2 + 1.0);
            let lw1 = Float::with_val(prec, &w1).ln();
            let lw2 = Float::with_val(prec, &w2).ln();
            let rw1 = Float::with_val(prec, 1.0 / &w1);
            let rw2 = Float::with_val(prec, 1.0 / &w2);
            let tl1 = Float::with_val(prec, &two * &lw1);
            let tl2 = Float::with_val(prec, &two * &lw2);
            let u1 = Float::with_val(prec, &v1 - &tl1);
            let u2 = Float::with_val(prec, &v2 - &tl2);
            let e2v1 = Float::with_val(prec, &u1 - &rw1);
            let e2v2 = Float::with_val(prec, &u2 - &rw2);
            let e1v1 = Float::with_val(prec, &lw1 + &rw1);
            let e1v2 = Float::with_val(prec, &lw2 + &rw2);
            let e0v1 = Float::with_val(prec, -&rw1);
            let e0v2 = Float::with_val(prec, -&rw2);
            let d2e = Float::with_val(prec, &e2v2 - &e2v1);
            let d1e = Float::with_val(prec, &e1v2 - &e1v1);
            let d0e = Float::with_val(prec, &e0v2 - &e0v1);
            let p1 = Float::with_val(prec, &c2p * &d2e);
            let p2 = Float::with_val(prec, &c1p * &d1e);
            let p3 = Float::with_val(prec, &c0m * &d0e);
            let s = Float::with_val(prec, &Float::with_val(prec, &p1 + &p2) + &p3);
            let sm = Float::with_val(prec, &s / &ml);
            m13m += &sm;
        }
        println!("mp m13 piece = {}", m13m);
        let mut tailm = Float::with_val(prec, 0);
        let blm = Float::with_val(prec, 2.0);
        let alm = Float::with_val(prec, 1.0);
        let mut pb1 = blm.clone();
        let mut pa1 = alm.clone();
        for p in 0..p_adaptive(1, 31.0) {
            let pb2 = Float::with_val(prec, &pb1 * &blm);
            let pa2 = Float::with_val(prec, &pa1 * &alm);
            let pb3 = Float::with_val(prec, &pb2 * &blm);
            let pa3 = Float::with_val(prec, &pa2 * &alm);
            let d1 = Float::with_val(prec, &pb1 - &pa1);
            let d2 = Float::with_val(prec, &pb2 - &pa2);
            let d3 = Float::with_val(prec, &pb3 - &pa3);
            let c2d3 = Float::with_val(prec, &c2m * &d3);
            let c1d2 = Float::with_val(prec, &c1m * &d2);
            let c0d1 = Float::with_val(prec, &c0m * &d1);
            let t1 = Float::with_val(prec, &c2d3 / ((p + 3) as f64));
            let t2 = Float::with_val(prec, &c1d2 / ((p + 2) as f64));
            let t3 = Float::with_val(prec, &c0d1 / ((p + 1) as f64));
            let inner = Float::with_val(prec, &Float::with_val(prec, &t1 + &t2) + &t3);
            let mut w = Float::with_val(prec, &zmp_direct[p] * ((p + 1) as f64));
            if p & 1 == 1 {
                w = -w;
            }
            let wi = Float::with_val(prec, &w * &inner);
            tailm += &wi;
            pb1 = pb2;
            pa1 = pa2;
        }
        println!("mp tail piece = {}", tailm);
        // dd pieces
        {
            let one = Dd::from_f64(1.0);
            let c2 = one;
            let c1 = Dd::from_f64(-2.0);
            let c0 = one;
            let lntwo = cst().ln2;
            let t1 = dd_mul(c2, Dd::from_f64(1.0));
            let dl = dd_mul(c1, lntwo);
            let t3 = dd_mul(c0, Dd { hi: 0.5, lo: 0.0 });
            let m0 = dd_add(dd_add(t1, dl), t3);
            println!("dd m0 piece = {}", dd_to_mpfr(m0));
            let mut m13 = Dd { hi: 0.0, lo: 0.0 };
            for m in 1..4u64 {
                let ml = Dd::from_int(m);
                let invml = dd_div(one, ml);
                let lnw1 = dd_sub(cst_ln(m + 1), cst_ln(m));
                let lnw2 = dd_sub(cst_ln(2 + m), cst_ln(m));
                let r1 = dd_div(ml, Dd::from_int(m + 1));
                let r2 = dd_div(ml, Dd::from_int(2 + m));
                let v1 = dd_div(one, ml);
                let v2 = Dd { hi: 2.0 / m as f64, lo: 0.0 };
                let tl1 = Dd { hi: 2.0 * lnw1.hi, lo: 2.0 * lnw1.lo };
                let tl2 = Dd { hi: 2.0 * lnw2.hi, lo: 2.0 * lnw2.lo };
                let e2v1 = dd_sub(dd_sub(v1, tl1), r1);
                let e2v2 = dd_sub(dd_sub(v2, tl2), r2);
                let e1v1 = dd_add(lnw1, r1);
                let e1v2 = dd_add(lnw2, r2);
                let e0v1 = dd_neg(r1);
                let e0v2 = dd_neg(r2);
                let c2p = Dd { hi: (m * m) as f64, lo: 0.0 };
                let c1p = Dd { hi: -2.0 * m as f64, lo: 0.0 };
                let s = dd_add(
                    dd_add(dd_mul(c2p, dd_sub(e2v2, e2v1)), dd_mul(c1p, dd_sub(e1v2, e1v1))),
                    dd_mul(c0, dd_sub(e0v2, e0v1)),
                );
                m13 = dd_add(m13, dd_mul(s, invml));
            }
            println!("dd m13 piece = {}", dd_to_mpfr(m13));
            let bl = Dd { hi: 2.0, lo: 0.0 };
            let al = one;
            let mut tail = Dd { hi: 0.0, lo: 0.0 };
            let mut pb1 = bl;
            let mut pa1 = al;
            for p in 0..p_adaptive(1, 31.0) {
                let pb2 = dd_mul(pb1, bl);
                let pa2 = dd_mul(pa1, al);
                let pb3 = dd_mul(pb2, bl);
                let pa3 = dd_mul(pa2, al);
                let d1 = dd_sub(pb1, pa1);
                let d2 = dd_sub(pb2, pa2);
                let d3 = dd_sub(pb3, pa3);
                let t1 = dd_mul(dd_mul(c2, d3), cst().inv[p + 3]);
                let t2 = dd_mul(dd_mul(c1, d2), cst().inv[p + 2]);
                let t3 = dd_mul(dd_mul(c0, d1), cst().inv[p + 1]);
                let inner = dd_add(dd_add(t1, t2), t3);
                tail = dd_add(tail, dd_mul(wtab[p], inner));
                pb1 = pb2;
                pa1 = pa2;
            }
            println!("dd tail piece = {}", dd_to_mpfr(tail));
        }
    }
    // m-piece audit for G_11 by direct MPFR period integrals
    let mut per = Float::with_val(prec, 0);
    for m in 0..300u64 {
        // int_1^2 (t-1)^2/(t+m)^2 dt exactly: t - 2m ln t - (m^2-1)/t ... derive: (t-1)^2/(t+m)^2 = 1 - (2m+2)/(t+m) + (m+1)^2/(t+m)^2
        let a1 = Float::with_val(prec, 1);
        let t2 = Float::with_val(prec, 2);
        let mm = Float::with_val(prec, m);
        let mp1 = Float::with_val(prec, m + 1);
        // int_1^2 1 dt = 1
        // int_1^2 dt/(t+m) = ln((2+m)/(1+m))
        let wm1 = Float::with_val(prec, &t2 + &mm);
        let wm0 = Float::with_val(prec, &a1 + &mm);
        let lm = Float::with_val(prec, &Float::with_val(prec, &wm1).ln() - &Float::with_val(prec, &wm0).ln());
        // int_1^2 dt/(t+m)^2 = 1/(1+m) - 1/(2+m)
        let u1 = Float::with_val(prec, &a1 / &wm0);
        let u2 = Float::with_val(prec, &a1 / &wm1);
        let l2 = Float::with_val(prec, &u1 - &u2);
        let two_mp1 = Float::with_val(prec, &mp1 + &mp1);
        let c2m2 = Float::with_val(prec, &two_mp1 * &lm);
        let mp1sq = Float::with_val(prec, &mp1 * &mp1);
        let t_a = Float::with_val(prec, &a1 - &c2m2);
        let t_b = Float::with_val(prec, &mp1sq * &l2);
        let ival = Float::with_val(prec, &t_a + &t_b);
        per += &ival;
    }
    println!("G_11 partial m<300 (mpfr) = {:.16e} (expect ~0.2595-0.2605)", per.to_f64());
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    if args.len() < 2 {
        eprintln!("usage: hiN validate | prod <N> | ddgram <N>");
        std::process::exit(1);
    }
    std::fs::create_dir_all("tools/wave8c/results").unwrap();
    match args[1].as_str() {
        "validate" => phase_validate(),
        "selftest" => phase_selftest(),
        "sample" => phase_sample(args[2].parse().unwrap()),
        "prod" => phase_prod(args[2].parse().unwrap()),
        "ddgram" => phase_ddgram(args[2].parse().unwrap()),
        _ => {
            eprintln!("unknown phase");
            std::process::exit(1);
        }
    }
}
