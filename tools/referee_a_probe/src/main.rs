// referee_a_probe: hostile blind referee attack on the sinc-m3 marked-law model.
// Attacks: (A) mass vs count normalization; (B) proven floor (E[T] free) vs code floor
// (E[T]>=0); (C) 256-law control in both conventions; (D) PSD 3x3 counterexample T<0.
// Pure std (no deps). Build: cargo build --release --target x86_64-unknown-linux-musl

use std::f64::consts::PI;

const N: usize = 256;
const B: usize = 128;
const P0: f64 = 0.6818286874638; // 256-law count simple-point fraction (Lean)

fn sinc(x: f64) -> f64 {
    if x.abs() < 1e-12 { 1.0 } else { x.sin() / x }
}

fn khat_spectrum() -> Vec<f64> {
    let mut kh = vec![0.0f64; N];
    for m in 0..N {
        let mut s = 0.0;
        for i in 0..N {
            let x = i as f64 / N as f64;
            let k = sinc(PI * B as f64 * x).powi(2);
            s += k * (2.0 * PI * m as f64 * x).cos();
        }
        kh[m] = s / N as f64;
    }
    kh
}

fn conv_circ(kh: &[f64]) -> Vec<f64> {
    let mut kk = vec![0.0f64; N];
    for k in 0..N {
        let mut s = 0.0;
        for m in 0..N {
            let j = (k + N - m) % N;
            s += kh[m] * kh[j];
        }
        kk[k] = s;
    }
    kk
}

// two conventions: mass (code: P(m=1)=2p1/(1+p1)) vs count (marks on zeros: P(m=1)=p1)
fn moments_mass(p1: f64) -> (f64, f64, f64) {
    (2.0 / (1.0 + p1), (4.0 - 2.0 * p1) / (1.0 + p1), (8.0 - 6.0 * p1) / (1.0 + p1))
}
fn moments_count(p1: f64) -> (f64, f64, f64) {
    (2.0 - p1, 4.0 - 3.0 * p1, 8.0 - 7.0 * p1)
}

fn mu0sq(em: f64, em2: f64) -> f64 {
    em2 / N as f64 + (N as f64 - 1.0) / N as f64 * em * em
}

fn m2_of(p1: f64, kk: &[f64], c: f64, mom: fn(f64) -> (f64, f64, f64)) -> f64 {
    let (em, em2, _) = mom(p1);
    let mut s = kk[0] * mu0sq(em, em2);
    for k in 1..N {
        s += kk[k] * (c * k as f64);
    }
    (N as f64 / em) * s
}

fn p3_of(p1: f64, kk: &[f64], c: f64, mom: fn(f64) -> (f64, f64, f64)) -> f64 {
    let (em, em2, em3) = mom(p1);
    let mut s = 0.0;
    for k in 0..N {
        let e_mu2mu = if k == 0 {
            em3 / N as f64 + (N as f64 - 1.0) / N as f64 * em2 * em
        } else {
            em3 / N as f64 + em2 * c * k as f64 / em - em2 * em2 / (N as f64 * em)
        };
        let ef = (N as f64 * N as f64) * e_mu2mu - (N as f64) * em3;
        s += kk[k] * ef;
    }
    3.0 * s / (N as f64 * em)
}

fn floor_full(p1: f64, kk: &[f64], c: f64, mom: fn(f64) -> (f64, f64, f64)) -> f64 {
    let (em, _, em3) = mom(p1);
    let d = em3 / em;
    let m2v = m2_of(p1, kk, c, mom);
    (d + p3_of(p1, kk, c, mom)).max(m2v * m2v)
}

fn floor_proven(p1: f64, kk: &[f64], c: f64, mom: fn(f64) -> (f64, f64, f64)) -> f64 {
    let m2v = m2_of(p1, kk, c, mom);
    m2v * m2v
}

// smallest p1 in [0,1] with floor(p1) <= hi, assuming decreasing (checked); None if floor(1)>hi
fn min_p1(kk: &[f64], c: f64, eps: f64, fl: fn(f64, &[f64], f64, fn(f64) -> (f64, f64, f64)) -> f64,
          mom: fn(f64) -> (f64, f64, f64)) -> Option<(f64, f64)> {
    let hi = 5.0 + eps;
    let f = |p: f64| fl(p, kk, c, mom) - hi;
    if f(1.0) > 0.0 { return None; }
    if f(0.0) <= 0.0 { return Some((0.0, fl(0.0, kk, c, mom))); }
    let (mut lo, mut h) = (0.0f64, 1.0f64);
    for _ in 0..80 {
        let mid = 0.5 * (lo + h);
        if f(mid) <= 0.0 { h = mid; } else { lo = mid; }
    }
    let p = 0.5 * (lo + h);
    Some((p, fl(p, kk, c, mom)))
}

fn calibrate(kk: &[f64], mom: fn(f64) -> (f64, f64, f64)) -> f64 {
    let tgt = 2.22f64;
    let mut c = 0.01f64;
    for _ in 0..60 {
        let v = m2_of(1.0, kk, c, mom);
        c *= tgt / v;
        if (m2_of(1.0, kk, c, mom) - tgt).abs() < 1e-10 { break; }
    }
    c
}

fn counterexample() {
    // G = [[1,a,a],[a,1,a],[a,a,1]], a = -0.2: PSD (ev 0.6, 1.2, 1.2), all marks 1.
    let a = -0.2f64;
    let g = [[1.0, a, a], [a, 1.0, a], [a, a, 1.0]];
    let mut g2 = [[0.0f64; 3]; 3];
    for i in 0..3 { for j in 0..3 { for k in 0..3 { g2[i][j] += g[i][k] * g[k][j]; } } }
    let mut g3 = [[0.0f64; 3]; 3];
    for i in 0..3 { for j in 0..3 { for k in 0..3 { g3[i][j] += g2[i][k] * g[k][j]; } } }
    let tr3: f64 = (0..3).map(|i| g3[i][i]).sum();
    let tr2: f64 = (0..3).map(|i| g2[i][i]).sum();
    let m3 = tr3 / 3.0;
    let m2 = tr2 / 3.0;
    let d = 1.0; // G_ii = 1
    let p2: f64 = (0..3).flat_map(|i| (0..3).filter(move |&j| j != i).map(move |j| g[i][j] * g[i][j])).sum();
    let t = m3 - d - p2;
    println!("  3x3 PSD, a=-0.2: m3={:.4} m2^2={:.4} D=1 P2={:.4} T=m3-D-P2={:.4}  -> theorem m3>=m2^2 {}; T>=0 {}",
        m3, m2 * m2, p2, t, if m3 >= m2 * m2 { "HOLDS" } else { "FAILS" },
        if t >= 0.0 { "HOLDS" } else { "FALSE (S3 can dip below D+P3)" });
}

fn main() {
    println!("=== referee A probe: sinc-m3 marked-law model ===");
    let kh = khat_spectrum();
    let kk = conv_circ(&kh);
    let c_mass = calibrate(&kk, moments_mass);
    let c_count = calibrate(&kk, moments_count);
    println!("calibration c (mass) = {:.8}, (count) = {:.8}  (both hit m2(1)=2.22; m2(1)^2={:.4})",
        c_mass, c_count, m2_of(1.0, &kk, c_mass, moments_mass).powi(2));

    // monotonicity check of both floors, both conventions
    type Mom = fn(f64) -> (f64, f64, f64);
    let ff: fn(f64, &[f64], f64, Mom) -> f64 = floor_full;
    let fp: fn(f64, &[f64], f64, Mom) -> f64 = floor_proven;
    let mm: Mom = moments_mass;
    let mc: Mom = moments_count;
    for (name, fl, mom) in [("full/mass", ff, mm), ("full/count", ff, mc),
                            ("prov/mass", fp, mm), ("prov/count", fp, mc)] {
        let mut mx = 0.0f64;
        let mut prev = fl(0.0, &kk, c_mass, mom);
        for i in 1..=1000 {
            let p = i as f64 / 1000.0;
            let v = fl(p, &kk, c_mass, mom);
            if v - prev > mx { mx = v - prev; }
            prev = v;
        }
        println!("  monotonicity {}: max increase over [0,1] = {:.2e} ({})", name, mx,
            if mx < 1e-6 { "decreasing OK" } else { "NOT decreasing" });
    }

    println!("\n=== scan: D+P3, m2^2, floor(full), floor(proven) ===");
    println!("  p1        D+P3(mass) m2^2(mass) fl(mass) flP(mass)  D+P3(cnt) m2^2(cnt) fl(cnt) flP(cnt)");
    for p1 in [0.40f64, 0.50, 0.60, 0.6818, 0.70, 0.75, 0.80, 0.90, 1.00] {
        let (em, _, em3) = moments_mass(p1);
        let (ec, _, ec3) = moments_count(p1);
        println!("  {:.4}   {:.4}  {:.4}  {:.4}  {:.4}   {:.4}  {:.4}  {:.4}  {:.4}",
            p1,
            em3 / em + p3_of(p1, &kk, c_mass, moments_mass),
            m2_of(p1, &kk, c_mass, moments_mass).powi(2),
            floor_full(p1, &kk, c_mass, moments_mass),
            floor_proven(p1, &kk, c_mass, moments_mass),
            ec3 / ec + p3_of(p1, &kk, c_count, moments_count),
            m2_of(p1, &kk, c_count, moments_count).powi(2),
            floor_full(p1, &kk, c_count, moments_count),
            floor_proven(p1, &kk, c_count, moments_count));
    }

    println!("\n=== min-p1 (eps=0.44), code floor (E[T]>=0) vs proven floor (E[T] free) ===");
    for (name, fl, c, mom) in [("full/mass ", ff, c_mass, mm),
                               ("prov/mass ", fp, c_mass, mm),
                               ("full/count", ff, c_count, mc),
                               ("prov/count", fp, c_count, mc)] {
        match min_p1(&kk, c, 0.44, fl, mom) {
            Some((p, f)) => {
                let lo = 4.56;
                let inw = f >= lo - 1e-9 && f <= 5.44 + 1e-9;
                println!("  {}: min-p1 = {:.6}, floor = {:.6}, kappa = {:.6}  in-window: {}  {}",
                    name, p, f, p + 1.0 / (6.0 * 256.0 * 256.0), inw,
                    if p + 1.0 / (6.0 * 256.0 * 256.0) > 0.6818 { "> 0.6818" } else { "<= 0.6818" });
            }
            None => println!("  {}: EMPTY", name),
        }
    }

    println!("\n=== CONTROL: 256-law ===");
    let p_mass = P0 / (2.0 - P0); // count 0.6818 -> mass
    println!("  256-law: count p1 = {:.6}, equivalent mass p1 = {:.6}", P0, p_mass);
    let (em, _, em3) = moments_mass(p_mass);
    let dp_mass = em3 / em + p3_of(p_mass, &kk, c_mass, moments_mass);
    let m2sq_mass = m2_of(p_mass, &kk, c_mass, moments_mass).powi(2);
    println!("  mass conv @ p1={:.4}: D+P3={:.4}, m2^2={:.4}, floor(full)={:.4} (in [4.56,5.44]? {}), floor(proven)={:.4} (in? {})",
        p_mass, dp_mass, m2sq_mass, dp_mass.max(m2sq_mass), dp_mass.max(m2sq_mass) >= 4.56 && dp_mass.max(m2sq_mass) <= 5.44,
        m2sq_mass, m2sq_mass >= 4.56 && m2sq_mass <= 5.44);
    let (ec, _, ec3) = moments_count(P0);
    let dp_cnt = ec3 / ec + p3_of(P0, &kk, c_count, moments_count);
    let m2sq_cnt = m2_of(P0, &kk, c_count, moments_count).powi(2);
    println!("  count conv @ p1={:.4}: D+P3={:.4}, m2^2={:.4}, floor(full)={:.4} (in? {}), floor(proven)={:.4} (in? {})",
        P0, dp_cnt, m2sq_cnt, dp_cnt.max(m2sq_cnt), dp_cnt.max(m2sq_cnt) >= 4.56 && dp_cnt.max(m2sq_cnt) <= 5.44,
        m2sq_cnt, m2sq_cnt >= 4.56 && m2sq_cnt <= 5.44);

    println!("\n=== calibration sensitivity (count convention, eps=0.44) ===");
    for tgt in [2.0f64, 2.11, 2.22, 2.33, 2.44] {
        let mut cc = 0.01f64;
        for _ in 0..60 {
            let v = m2_of(1.0, &kk, cc, moments_count);
            cc *= tgt / v;
        }
        match min_p1(&kk, cc, 0.44, floor_full, moments_count) {
            Some((p, _)) => println!("  m2(1)={:.2}: c={:.6}, min-p1={:.5}, kappa={:.5} {}",
                tgt, cc, p, p + 1.0 / (6.0 * 256.0 * 256.0),
                if p + 1.0 / (6.0 * 256.0 * 256.0) > 0.6818 { "> 0.6818" } else { "<= 0.6818" }),
            None => println!("  m2(1)={:.2}: EMPTY", tgt),
        }
    }

    counterexample();
}
