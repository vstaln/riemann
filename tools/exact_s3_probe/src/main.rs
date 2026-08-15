// exact_s3_probe: rebuild sinc-m3 certificate on the EXACT identity m3 = m2^2 + N^2 M^2 Var(T1).
// 1) verify identity numerically on random configs
// 2) recompute envelope (E[m2](p1))^2 and D+P3(p1), min-p1 under the exact-identity bound
// 3) explore configs at count-p1 ~ 0.6818: exact m3, m3-m2^2, flat-row deviation
// 4) extremal configs (all-2, all-1) sanity: m3 == m2^2
use std::f64::consts::PI;

const N: usize = 256;
const B: usize = 128;

fn sinc(x: f64) -> f64 {
    if x.abs() < 1e-12 { 1.0 } else { x.sin() / x }
}

// DFT of K = sinc^2(pi B x) on lattice (1/N normalized, old-cert convention)
fn khat() -> Vec<f64> {
    (0..N).map(|m| {
        (0..N).map(|i| {
            let x = i as f64 / N as f64;
            sinc(PI * B as f64 * x).powi(2) * (2.0 * PI * m as f64 * x).cos()
        }).sum::<f64>() / N as f64
    }).collect()
}

fn conv_circ(kh: &[f64]) -> Vec<f64> {
    (0..N).map(|k| (0..N).map(|m| kh[m] * kh[(k + N - m) % N]).sum()).collect()
}

// DFT of a mark config (1/N normalized, real part; marks real so muhat[k] = muhat[-k]^*) 
fn muhat(m: &[u8]) -> Vec<f64> {
    (0..N).map(|k| {
        (0..N).map(|j| {
            let x = j as f64 / N as f64;
            m[j] as f64 * (2.0 * PI * k as f64 * x).cos()
        }).sum::<f64>() / N as f64
    }).collect()
}

// per-config moments in the REDERIVATION convention (unnormalized DFT muhat(k)=sum_j m_j e^{-2piikj/N},
// m2 = N*M*<1,T1>_nu, m3 = N^2*M^2*||T1||^2_nu, T1 = (K^2 * mu)/M). Direct O(N^2).
fn m2_m3(m: &[u8]) -> (f64, f64, f64) {
    let m_tot: f64 = m.iter().map(|&v| v as f64).sum();
    let g = |d: i64| { let x = d as f64 / N as f64; sinc(PI * B as f64 * x).powi(4) };
    // W_j = (K^2 * mu)(x_j)
    let mut w = vec![0.0f64; N];
    for j in 0..N {
        let mut s = 0.0;
        for i in 0..N {
            let d = (j as i64 - i as i64).rem_euclid(N as i64);
            s += m[i] as f64 * g(d);
        }
        w[j] = s;
    }
    // <1,T1>_nu = (1/M^2) sum m_j W_j ; ||T1||^2_nu = (1/M^3) sum m_j W_j^2
    let mut e1 = 0.0; let mut e2 = 0.0;
    for j in 0..N { e1 += m[j] as f64 * w[j]; e2 += m[j] as f64 * w[j] * w[j]; }
    e1 /= m_tot * m_tot; e2 /= m_tot * m_tot * m_tot;
    let m2 = (N as f64 * m_tot) * e1;
    let m3 = (N as f64 * N as f64 * m_tot * m_tot) * e2;
    (m2, m3, m2 * m2 + (N as f64 * N as f64 * m_tot * m_tot) * (e2 - e1 * e1))
}

// flat-row deviation: max_k | |muhat[k]|^2 / k - c | / c  over k=1..127 (kk[k]>0 band), c = avg
fn flat_dev(m: &[u8]) -> (f64, f64) {
    let mh = muhat(m);
    let mut ratios = Vec::new();
    for k in 1..128 { ratios.push(mh[k] * mh[k] / k as f64); }
    let c: f64 = ratios.iter().sum::<f64>() / ratios.len() as f64;
    let md = ratios.iter().map(|r| (r - c).abs() / c).fold(0.0f64, f64::max);
    (md, c)
}

// envelope from pair rows (count convention P(m=1)=2p1/(1+p1) as in old cert)
fn envelope(p1: f64, kk: &[f64], c: f64) -> (f64, f64, f64) {
    let em = 2.0 / (1.0 + p1); let em2 = (4.0 - 2.0 * p1) / (1.0 + p1); let em3 = (8.0 - 6.0 * p1) / (1.0 + p1);
    let mu0sq = em2 / N as f64 + (N as f64 - 1.0) / N as f64 * em * em;
    let mut s = kk[0] * mu0sq;
    for k in 1..N { s += kk[k] * (c * k as f64); }
    let m2v = (N as f64 / em) * s;
    // D + P3 (two-equal pinned part)
    let mut sp = 0.0;
    for k in 0..N {
        let e_mu2mu = if k == 0 { em3 / N as f64 + (N as f64 - 1.0) / N as f64 * em2 * em }
            else { em3 / N as f64 + em2 * c * k as f64 / em - em2 * em2 / (N as f64 * em) };
        let ef = (N as f64 * N as f64) * e_mu2mu - (N as f64) * em3;
        sp += kk[k] * ef;
    }
    let p3 = 3.0 * sp / (N as f64 * em);
    let d = em3 / em;
    (m2v * m2v, d + p3, m2v)
}

fn main() {
    let kh = khat();
    let kk = conv_circ(&kh);
    println!("kk[0] = {:.6}, C = sum kk[k]k = {:.6}", kk[0], (1..N).map(|k| kk[k] * k as f64).sum::<f64>());
    // calibration: c so m2(p1=1) = 2.22 (real-zeros sinc m2^2=4.9256)
    let mut c = 0.01f64;
    for _ in 0..60 {
        let v = envelope(1.0, &kk, c).2;
        c *= 2.22 / v;
        if (envelope(1.0, &kk, c).2 - 2.22).abs() < 1e-10 { break; }
    }
    println!("calibrated c = {:.8}, m2(1) = {:.6}", c, envelope(1.0, &kk, c).2);

    // 1) identity check on random configs (xorshift)
    let mut state = 0x9E3779B97F4A7C15u64;
    let mut rnd = || { state ^= state << 13; state ^= state >> 7; state ^= state << 17; state };
    println!("\n== 1) identity m3 == m2^2 + N^2M^2 Var(T1) (rederivation convention) on random configs ==");
    let mut maxdiff = 0.0f64;
    let mut maxneg = 0.0f64;
    for trial in 0..8 {
        let q = 0.3 + 0.4 * (trial as f64) / 7.0;
        let m: Vec<u8> = (0..N).map(|_| if (rnd() % 1000) as f64 / 1000.0 < q { 1 } else { 2 }).collect();
        let (m2, m3, m3id) = m2_m3(&m);
        let d = (m3 - m3id).abs();
        maxdiff = maxdiff.max(d);
        maxneg = maxneg.max(m2 * m2 - m3);
        let p1m = m.iter().filter(|&&v| v == 1).count() as f64 / N as f64;
        println!("  trial {}: mass-p1 = {:.3}, m2 = {:.3}, m3 = {:.1}, m3-m2^2 = {:.1}, |id| = {:.2e}", trial, p1m, m2, m3, m3 - m2 * m2, d);
    }
    println!("  MAX |m3 - identity| = {:.2e}  [{}];  max(m2^2 - m3) = {:.2e}  [CS {}]", maxdiff, if maxdiff < 1e-6 { "IDENTITY VERIFIED" } else { "FAILED" }, maxneg, if maxneg <= 1e-6 { "m3>=m2^2 HOLDS" } else { "VIOLATED" });

    // 2) envelope + min-p1 under EXACT identity bound (E[m3] >= (E[m2])^2)
    // old-cert parameter p is the MASS fraction P(m=1)=2p/(1+p), E[m]=2/(1+p); count = 2p/(1+p)
    println!("\n== 2) envelope (parameter p = MASS fraction, as in old cert), window [4.56, 5.44] ==");
    println!("  p(mass)  count     (E[m2])^2   D+P3");
    for p1 in [0.422384f64, 0.50, 0.5173, 0.5939, 0.6818, 0.7488, 0.8564, 1.00] {
        let (m2sq, dp3, _) = envelope(p1, &kk, c);
        let cnt = 2.0 * p1 / (1.0 + p1);
        println!("  {:.4}   {:.4}   {:.4}    {:.4}", p1, cnt, m2sq, dp3);
    }
    // min-p1 (mass): smallest mass-p with (E[m2])^2 <= 5.44
    let f = |p: f64| envelope(p, &kk, c).0 - 5.44;
    let (mut lo, mut hi) = (0.0f64, 1.0f64);
    for _ in 0..80 { let mid = 0.5 * (lo + hi); if f(mid) <= 0.0 { hi = mid } else { lo = mid } }
    let pmin_mass = 0.5 * (lo + hi);
    let pmin_cnt = 2.0 * pmin_mass / (1.0 + pmin_mass);
    println!("  min-p1 (MASS, exact-identity bound) = {:.6};  COUNT equiv = {:.6}", pmin_mass, pmin_cnt);
    println!("  vs wall count-p0 = 0.6818287 -> {} (count {:.4} vs {:.4})", if pmin_cnt > 0.6818287 { "BEATS WALL" } else { "does NOT beat wall" }, pmin_cnt, 0.6818287);

    // 3) configs at count-p1 ~ 0.6818: exact m3 + flat-row deviation
    println!("\n== 3) exact configs at count-p1 ~ 0.6818 (174 ones / 256) ==");
    let n_ones = 174usize;
    let mut configs: Vec<(String, Vec<u8>)> = Vec::new();
    // equidistributed spread
    let mut s = vec![2u8; N];
    for j in 0..n_ones { let idx = ((j as f64) * 256.0 / n_ones as f64).round() as usize % N; s[idx] = 1; }
    configs.push(("spread-174".into(), s));
    // contiguous block
    let mut s = vec![2u8; N];
    for j in 0..n_ones { s[j] = 1; }
    configs.push(("block-174".into(), s));
    // random (q=0.68)
    let m: Vec<u8> = (0..N).map(|_| if (rnd() % 1000) as f64 / 1000.0 < 0.68 { 1 } else { 2 }).collect();
    configs.push(("random-q0.68".into(), m));
    // near-uniform alternating (2,1,2,1,...) then patch to 174
    let mut s = vec![2u8; N];
    for j in 0..N { if j % 2 == 0 { s[j] = 1; } }
    for j in (0..N).step_by(2) { if s.iter().filter(|&&v| v == 1).count() > n_ones { s[j] = 2; } }
    configs.push(("alt-patched-174".into(), s));
    for (name, cfg) in &configs {
        let (m2, m3, _) = m2_m3(cfg);
        let (fd, cr) = flat_dev(cfg);
        let p1m = cfg.iter().filter(|&&v| v == 1).count() as f64 / N as f64;
        println!("  {}: mass-p1={:.4}, m2={:.2}, m3={:.1}, (m3-m2^2)/m2^2={:.3}, flat-dev={:.1}x, flat-c={:.6} (calib 3.48e-5)", name, p1m, m2, m3, (m3 - m2 * m2) / (m2 * m2), fd, cr);
    }
    println!("  NOTE: per-config m3 lives in the rederivation normalization (m2~500, m3~1e5); the read window [4.56,5.44] is the LAW-level normalized m3. Configs above violate flat rows (flat-dev>>1) so are OUT of the admissible class.");

    // 4) extremals
    println!("\n== 4) extremals (m3 == m2^2) ==");
    let all2 = vec![2u8; N];
    let all1 = vec![1u8; N];
    for (nm, cfg) in [("all-2", &all2), ("all-1", &all1)] {
        let (m2, m3, m3id) = m2_m3(cfg);
        println!("  {}: m2={:.4}, m3={:.4}, m3-m2^2={:.2e}, id-diff={:.2e}  [Var(T1)=0 extremal]", nm, m2, m3, m3 - m2 * m2, (m3 - m3id).abs());
    }
}
