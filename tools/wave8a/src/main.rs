// Wave 8A: Li's criterion, lambda_n = sum_rho [1 - (1-1/rho)^n]  (RH <=> lambda_n >= 0 for all n)
//
// Route: direct conjugate-pair sum over cached zeros (the computable route; the brief's
// "Taylor coefficients of log xi" route is exercised on the MODEL where everything is finite).
//   On-line zero (sigma=1/2): |1-1/rho| = |rho-1|/|rho| = 1  =>  (1-1/rho)^n = e^{i n phi(gamma)},
//     phi(gamma) = arg((rho-1)/rho) = atan2(g,-1/2) - atan2(g,1/2) = 1/gamma + O(1/gamma^3),
//     pair term = 2 - 2 Re(e^{i n phi}) = 2(1 - cos(n phi)) >= 0.   (f64: ~1e-16 error per pair)
//   Off-line (sigma<1/2): |1-1/rho| > 1 => pair term -> -inf: the control's signature.
// Main term (Lagarias): M(n) = (n/2)(log n - log 2pi + gamma_EM - 1).
// Fluctuation probe: lambda_n vs lambda^sm_n where the zeros are replaced by their
// Riemann-von Mangoldt smooth positions (Newton on N(t)); fluct = lambda - lambda^sm
// isolates the actual-zero-position signal, dominated by the low zeros.
//
// rug (MPFR) used only for the model self-check: high-order Taylor coefficients of
// log xi_hat at s=1 suffer f64 cancellation; MPFR removes the doubt. (one-line reason)
use rug::Float;
use std::env;
use std::fs;

const LOG_2PI: f64 = 1.8378770664093453;
const GAMMA_EM: f64 = 0.5772156649015329;

fn read_gammas(path: &str) -> Vec<f64> {
    let s = fs::read_to_string(path).expect("read zeros file");
    s.lines()
        .filter(|l| !l.trim().is_empty() && !l.trim_start().starts_with('#'))
        .filter_map(|l| {
            l.split_whitespace()
                .last()
                .and_then(|tok| tok.parse::<f64>().ok())
        })
        .collect()
}

// arg((rho-1)/rho), rho = 1/2 + i*gamma   (= 1/gamma to O(gamma^-3))
fn phi(g: f64) -> f64 {
    g.atan2(-0.5) - g.atan2(0.5)
}

fn lambda_from_phis(phis: &[f64], n: usize, skip: usize) -> f64 {
    let nf = n as f64;
    let mut s = 0.0;
    let mut i = skip.min(phis.len());
    while i < phis.len() {
        s += 2.0 * (1.0 - (nf * phis[i]).cos());
        i += 1;
    }
    s
}

// complex helpers (f64) for the planted off-line zeros
fn cmul(a: (f64, f64), b: (f64, f64)) -> (f64, f64) {
    (a.0 * b.0 - a.1 * b.1, a.0 * b.1 + a.1 * b.0)
}
fn cpow(z: (f64, f64), n: usize) -> (f64, f64) {
    let mut r = (1.0, 0.0);
    let mut b = z;
    let mut k = n;
    while k > 0 {
        if k & 1 == 1 {
            r = cmul(r, b);
        }
        b = cmul(b, b);
        k >>= 1;
    }
    r
}

// planted-zero control: remove pair at gamma1, add rho = sigma0 +- i*gamma1, (1-sigma0) +- i*gamma1
fn lambda_control(phis: &[f64], n: usize, gamma1: f64, sigma0: f64) -> f64 {
    let nf = n as f64;
    let base = lambda_from_phis(phis, n, 0)
        - 2.0 * (1.0 - (nf * phi(gamma1)).cos()); // remove the real pair at gamma1
    let mut s = 0.0;
    for &sig in &[sigma0, 1.0 - sigma0] {
        for &sgn in &[1.0f64, -1.0f64] {
            let rho = (sig, sgn * gamma1); // (re, im)
            // 1 - 1/rho = (rho-1)/rho ;  1/rho = conj(rho)/|rho|^2 = (sig, -gamma)/|rho|^2
            let den = rho.0 * rho.0 + rho.1 * rho.1;
            let t = cmul((rho.0 - 1.0, rho.1), (rho.0 / den, -rho.1 / den));
            let tn = cpow(t, n);
            s += 1.0 - tn.0;
        }
    }
    base + s
}

// smooth (RvM) zero position solving N(t) = k, N(t) = (t/2pi)(log(t/2pi)-1) + 7/8
fn gamma_smooth(k: f64) -> f64 {
    let two_pi = 2.0 * std::f64::consts::PI;
    let mut t = two_pi * (k + 1.0) / (k + 1.0).ln().max(1.0);
    for _ in 0..60 {
        let n = (t / two_pi) * ((t / two_pi).ln() - 1.0) + 0.875;
        let dn = (t / two_pi).ln() / two_pi;
        let step = (n - k) / dn;
        t -= step;
        if step.abs() < 1e-12 * t {
            break;
        }
    }
    t
}

fn lambda_smooth(n: usize, count: usize) -> f64 {
    let nf = n as f64;
    let mut s = 0.0;
    for k in 1..=count {
        s += 2.0 * (1.0 - (nf * phi(gamma_smooth(k as f64))).cos());
    }
    s
}

fn main_term(n: usize) -> f64 {
    let nf = n as f64;
    (nf / 2.0) * (nf.ln() - LOG_2PI + GAMMA_EM - 1.0)
}

// ---------------- model self-check (rug) ----------------
// xi_hat(s) = prod over 8 conjugate pairs (1 - s/rho)(1 - s/conj(rho)); real polynomial, deg 16.
// Route A (direct product-sum):  lambda = sum_pairs 2(1-cos(n phi(gamma)))
// Route B (xi-derivative / Taylor coefficients of log xi_hat):  lambda = n * [x^n] (1+x)^{n-1} log xi_hat(1+x)
fn model_check(prec: u32) {
    let model_g: [f64; 8] = [
        14.134725141735, 21.022039638772, 25.010857580146, 30.424876125859, 32.935061587739,
        100.0, 200.0, 300.0,
    ];
    // polynomial coeffs in s: c[0..=16], c[0]=1
    let mut c: Vec<Float> = vec![Float::with_val(prec, 1)];
    for &g in &model_g {
        let den = 0.25 + g * g;
        // multiply by (1 - (1/rho + 1/conj) s + s^2/|rho|^2) = (1 - s/den s + s^2/den) since 2*sigma=1
        // 1/rho + 1/conj(rho) = 2*Re(1/rho) = 2*(1/2)/den = 1/den ; 1/|rho|^2 = 1/den
        // => factor = 1 - (1/den) s + (1/den) s^2
        let inv = Float::with_val(prec, 1.0 / den);
        let deg = c.len() - 1;
        let mut nc: Vec<Float> = vec![Float::with_val(prec, 0); deg + 3];
        for (j, cj) in c.iter().enumerate() {
            nc[j] += cj.clone();
            nc[j + 1] -= &inv * cj;
            nc[j + 2] += &inv * cj;
        }
        c = nc;
    }
    assert_eq!(c.len(), 17);
    // shift to x = s-1: P(x) = xi_hat(1+x); coefficients p[0..=16] in x
    // build by Horner: start from leading coeff, multiply by (1+x) repeatedly
    let mut p: Vec<Float> = vec![Float::with_val(prec, 0); 17];
    let mut acc: Vec<Float> = vec![Float::with_val(prec, 0); 17];
    acc[0] = c[16].clone();
    for j in (0..16).rev() {
        // acc *= (1+x), then add c[j]
        let mut na: Vec<Float> = vec![Float::with_val(prec, 0); 17];
        for i in 0..17 {
            if i < 16 {
                na[i + 1] += &acc[i];
            }
            na[i] += &acc[i];
        }
        na[0] += &c[j];
        acc = na;
    }
    p = acc;
    // log P(x) = log P(0) + log(1 + Q(x)); Q = (P - P0)/P0, Q(0)=0
    let p0 = p[0].clone();
    let mut q: Vec<Float> = Vec::new();
    for j in 1..17 {
        q.push(Float::with_val(prec, &p[j] / &p0));
    }
    // log(1+Q) = sum_{m>=1} (-1)^{m+1} Q^m / m ; series coeffs up to degree 80
    let nmax = 80usize;
    let mut lc = vec![Float::with_val(prec, 0); nmax + 1]; // lc[m] = [x^m] log P
    let mut qpow: Vec<Float> = vec![Float::with_val(prec, 0); nmax + 1];
    qpow[0] = Float::with_val(prec, 1); // Q^0 = 1
    for m in 1..=nmax {
        // qpow = qpow * Q
        let mut nq: Vec<Float> = vec![Float::with_val(prec, 0); nmax + 1];
        for i in 0..nmax {
            if qpow[i] != 0.0 {
                for (j, qj) in q.iter().enumerate() {
                    if i + j + 1 <= nmax {
                        nq[i + j + 1] += &qpow[i] * qj;
                    }
                }
            }
        }
        qpow = nq;
        let sign = if m % 2 == 1 { 1.0 } else { -1.0 };
        let mm = Float::with_val(prec, m as f64);
        for i in 1..=nmax {
            lc[i] += Float::with_val(prec, sign) * &qpow[i] / &mm;
        }
    }
    // compare routes for n = 1..=40
    let mut maxdiff = Float::with_val(prec, 0);
    for n in 1..=40usize {
        // route B: n * sum_{m=1..n} C(n-1, n-m) lc[m]
        let mut binom = Float::with_val(prec, 1); // C(n-1, 0)
        let mut acc2 = Float::with_val(prec, 0);
        // sum over m: coefficient of x^n in (1+x)^{n-1} log P
        for m in 1..=n {
            // C(n-1, n-m) = C(n-1, m-1)
            if m > 1 {
                let k = (m - 1) as f64;
                let nn1 = (n - 1) as f64;
                binom *= Float::with_val(prec, (nn1 - k + 1.0) / k);
            }
            acc2 += &binom * &lc[m];
        }
        let route_b = Float::with_val(prec, n as f64) * acc2;
        // route A: direct pair sum
        let mut route_a = Float::with_val(prec, 0);
        let nf = n as f64;
        for &g in &model_g {
            route_a += Float::with_val(prec, 2.0 * (1.0 - (nf * phi(g)).cos()));
        }
        let d = Float::with_val(prec, &route_a - &route_b).abs();
        if d > maxdiff {
            maxdiff = d.clone();
        }
        if n <= 12 {
            println!("  n={:>2}  direct={:+.12}  series={:+.12}  diff={:+.3e}", n, route_a.to_f64(), route_b.to_f64(), d.to_f64());
        }
    }
    println!("  MODEL CHECK max |direct - series| over n=1..40 = {:.3e} (prec {} bits)", maxdiff.to_f64(), prec);
}

fn main() {
    let data_dir = env::var("W8A_DATA").unwrap_or_else(|_| "../data".into());
    let small = format!("{}/zeros_rust_100k.txt", data_dir);
    let big = format!("{}/zeros_rust_924k.txt", data_dir);
    let gs100 = read_gammas(&small);
    let gs924 = read_gammas(&big);
    // precompute phi once (the per-n cost is then cos-only)
    let ph100: Vec<f64> = gs100.iter().map(|&g| phi(g)).collect();
    let ph924: Vec<f64> = gs924.iter().map(|&g| phi(g)).collect();
    let ph_sm: Vec<f64> = (1..=gs924.len()).map(|k| phi(gamma_smooth(k as f64))).collect();
    println!("zeros: 100k={} 924k={}", gs100.len(), gs924.len());
    println!("gamma_1={:.9} gamma_2={:.9} gamma_100k={:.3} gamma_last={:.3}", gs924[0], gs924[1], gs100[gs100.len() - 1], gs924[gs924.len() - 1]);

    // 0) model self-check (rug)
    println!("== MODEL SELF-CHECK (finite xi_hat, 8 pairs) ==");
    model_check(192);

    // 1) closed-form anchor lambda_1 = 1 + gamma/2 - log(pi)/2 - log(2)
    let lam1_closed = 1.0 + GAMMA_EM / 2.0 - std::f64::consts::PI.ln() / 2.0 - 2.0f64.ln();
    let lam1_924 = lambda_from_phis(&ph924, 1, 0);
    let lam1_100 = lambda_from_phis(&ph100, 1, 0);
    println!("== ANCHORS ==");
    println!("lambda_1 closed form = {:.12}  (PROVEN: xi'(1)/xi(1) = 1 + gamma/2 - log(4pi)/2)", lam1_closed);
    println!("lambda_1 from 100k zeros = {:.12}  (tail missing ~ {:.3e})", lam1_100, lam1_closed - lam1_100);
    println!("lambda_1 from 924k zeros = {:.12}  (tail missing ~ {:.3e})", lam1_924, lam1_closed - lam1_924);
    let lam2 = lambda_from_phis(&ph924, 2, 0);
    let lam3 = lambda_from_phis(&ph924, 3, 0);
    let lam4 = lambda_from_phis(&ph924, 4, 0);
    let lam5 = lambda_from_phis(&ph924, 5, 0);
    println!("lambda_2..5 (924k) = {:.8} {:.8} {:.8} {:.8}   (Keiper: 0.09234586 0.20763936 0.36825319 0.57332746)", lam2, lam3, lam4, lam5);

    // 2) convergence: 100k vs 924k at n=1000
    let n1000_100 = lambda_from_phis(&ph100, 1000, 0);
    let n1000_924 = lambda_from_phis(&ph924, 1000, 0);
    println!("== CONVERGENCE ==");
    println!("lambda_1000: 100k zeros={:.6}  924k zeros={:.6}  diff={:.4} (predicted tail ~ (n^2/2pi)(log(G/2pi e)+1)/G, G=7.49e4: ~ {:.2})", n1000_100, n1000_924, n1000_924 - n1000_100, 1e6 / 6.2832 * (10.3 + 1.0) / 74920.0);

    // 3) CONTROL first: planted zero at gamma1 (brief's prescription: rho=0.6+-14.13i, 0.4-+14.13i)
    let g1 = gs924[0];
    println!("== CONTROL (planted rho = 0.6 +- {}i, 0.4 +- {}i; real pair removed) ==", g1, g1);
    // the sigma=0.4 member has |1-1/rho| > 1 -> term ~ -2|t|^n cos(n phi'); dips grow exponentially at
    // resonances n ~ 2 pi m / phi' ~ 2 pi m gamma1. Sample those + a scan for the first negative.
    let mut first_neg: Option<usize> = None;
    let mut dip_report: Vec<(usize, f64)> = Vec::new();
    let mut m = 1usize;
    loop {
        let nres = ((2.0 * std::f64::consts::PI * m as f64 * g1).round()) as usize;
        if nres > 60000 {
            break;
        }
        let lc = lambda_control(&ph924, nres, g1, 0.6);
        if lc < 0.0 && first_neg.is_none() {
            first_neg = Some(nres);
        }
        if m <= 12 {
            dip_report.push((nres, lc));
        }
        m += 1;
    }
    for &(nr, lc) in &dip_report {
        println!("  n={:>5} (resonance m={})  lambda'_n = {:+.6e}", nr, (nr as f64 / (2.0 * std::f64::consts::PI * g1)).round() as usize, lc);
    }
    // coarse scan 1..=5000 step 7 for completeness
    let mut n = 1usize;
    while n <= 5000 {
        let lc = lambda_control(&ph924, n, g1, 0.6);
        if lc < 0.0 && first_neg.is_none() {
            first_neg = Some(n);
        }
        n += 7;
    }
    match first_neg {
        Some(n) => {
            println!("  CONTROL ANOMALY: lambda'_n < 0 first at n = {}", n);
            let lc = lambda_control(&ph924, n, g1, 0.6);
            println!("  lambda'_{} = {:.6e}  (main term there = {:.1})", n, lc, main_term(n));
        }
        None => println!("  CONTROL: no negative lambda' found (BAD - discriminator failed)"),
    }
    // envelope growth of the planted dip: dip depth d = main - lambda' at resonances
    // vs the planted |t|^n envelope (|t| = e^{0.00050 n} for sigma=0.4, gamma=14.13)
    if dip_report.len() >= 2 {
        let (d0, dn_last) = (dip_report[0], dip_report[dip_report.len() - 1]);
        let dip0 = main_term(d0.0) - d0.1;
        let dipl = main_term(dn_last.0) - dn_last.1;
        let rate = (dipl.abs().max(1e-12).ln() - dip0.abs().max(1e-12).ln()) / (dn_last.0 - d0.0) as f64;
        println!("  control dip depth at n=89: {:.3e}, at n=1066: {:.3e}; log-growth {:.6}/n (planted envelope: e^(0.00050 n))", dip0.max(0.0), dipl.max(0.0), rate);
    }

    // 4) REAL CASE: lambda_n, main term, residual, smoothed fluctuation, periodogram
    let n_samples: Vec<usize> = (1..=1000).collect();
    let mut out = String::new();
    out.push_str("# n lambda_n main residual fluct(actual-smoothed) main_over_n\n");
    let mut fluct: Vec<f64> = Vec::new();
    let mut res: Vec<f64> = Vec::new();
    let mut nn: Vec<usize> = Vec::new();
    for &n in &n_samples {
        let l = lambda_from_phis(&ph924, n, 0);
        let m = main_term(n);
        let ls = lambda_from_phis(&ph_sm, n, 0);
        let f = l - ls;
        fluct.push(f);
        res.push(l - m);
        nn.push(n);
        if n <= 60 || n % 100 == 0 {
            out.push_str(&format!("{} {:.10} {:.10} {:.6e} {:.6e} {:.6}\n", n, l, m, l - m, f, m / n as f64));
        }
    }
    fs::write("lambda_table.txt", &out).expect("write table");
    println!("== REAL CASE ==");
    println!("lambda_1..10: {:?}", (1..=10).map(|n| lambda_from_phis(&ph924, n, 0)).collect::<Vec<f64>>());
    println!("main_term/n = (1/2)(log n - log 2pi + gamma - 1);  table -> lambda_table.txt");

    // empirical constant: (lambda_n - (n/2) log n)/(n/2) -> C_emp, compare -log 2pi + gamma - 1
    let mut csum = 0.0;
    let mut cnt = 0.0;
    for &n in &[500usize, 600, 700, 800, 900, 1000] {
        let l = lambda_from_phis(&ph924, n, 0);
        let c = (l - (n as f64) / 2.0 * (n as f64).ln()) / ((n as f64) / 2.0);
        csum += c;
        cnt += 1.0;
    }
    println!("empirical C = {:.6}  vs  -log(2pi) + gamma - 1 = {:.6}", csum / cnt, -LOG_2PI + GAMMA_EM - 1.0);

    // residual envelope fit: |r_n| ~ A n^alpha (least squares in log-log over sampled n)
    let idxr: Vec<usize> = (0..nn.len()).filter(|&i| nn[i] % 25 == 0 && nn[i] > 50).collect();
    let mut sx = 0.0;
    let mut sy = 0.0;
    let mut sxx = 0.0;
    let mut sxy = 0.0;
    let mut cnt2 = 0.0;
    for &i in &idxr {
        let x = (nn[i] as f64).ln();
        let y = res[i].abs().max(1e-12).ln();
        sx += x;
        sy += y;
        sxx += x * x;
        sxy += x * y;
        cnt2 += 1.0;
    }
    let alpha_r = (cnt2 * sxy - sx * sy) / (cnt2 * sxx - sx * sx);
    let beta_r = (sy - alpha_r * sx) / cnt2;
    println!("residual envelope fit: |r_n| ~ {:.3e} * n^{:.4}", beta_r.exp(), alpha_r);

    // fluct envelope fit (secondary; dominated by low-zero positional deviations from RvM)
    sx = 0.0; sy = 0.0; sxx = 0.0; sxy = 0.0; cnt2 = 0.0;
    for &i in &idxr {
        let x = (nn[i] as f64).ln();
        let y = fluct[i].abs().max(1e-12).ln();
        sx += x; sy += y; sxx += x * x; sxy += x * y; cnt2 += 1.0;
    }
    let alpha_f = (cnt2 * sxy - sx * sy) / (cnt2 * sxx - sx * sx);
    let beta_f = (sy - alpha_f * sx) / cnt2;
    println!("fluct envelope fit: |fluct_n| ~ {:.3e} * n^{:.4}   (note: RvM smooth is poor at low gamma -> low-zero deviations give ~linear envelope; not an RH signal)", beta_f.exp(), alpha_f);

    // periodogram of the RESIDUAL r_n: exact power at low-zero frequencies + scan
    let f1 = phi(gs924[0]);
    let f2 = phi(gs924[1]);
    let f3 = phi(gs924[2]);
    let nf = nn.len();
    let pow_at = |om: f64| -> f64 {
        let (mut cr, mut ci) = (0.0, 0.0);
        for i in 0..nf {
            let a = om * nn[i] as f64;
            cr += res[i] * a.cos();
            ci -= res[i] * a.sin();
        }
        cr * cr + ci * ci
    };
    println!("residual periodogram exact powers: phi(g1)=0.070718 -> {:.3e}   phi(g2)=0.047560 -> {:.3e}   phi(g3)=0.039981 -> {:.3e}", pow_at(f1), pow_at(f2), pow_at(f3));
    let mut scan: Vec<(f64, f64)> = Vec::new();
    let mut om = 0.01;
    while om < 0.25 {
        scan.push((om, pow_at(om)));
        om += 0.0005;
    }
    scan.sort_by(|a, b| b.1.partial_cmp(&a.1).unwrap());
    println!("residual periodogram top-6 freqs: {:?}", &scan[..6]);
    println!("predicted low-zero freqs: phi(gamma_1={:.6})={:.6}  phi(gamma_2={:.6})={:.6}  phi(gamma_3={:.6})={:.6}", gs924[0], f1, gs924[1], f2, gs924[2], f3);

    // largest residual
    let (mut mx, mut mxi) = (0.0f64, 0usize);
    let (mut mn, mut mni) = (f64::MAX, 0usize);
    for i in 0..nf {
        if fluct[i].abs() > mx {
            mx = fluct[i].abs();
            mxi = nn[i];
        }
        if res[i] < mn {
            mn = res[i];
            mni = nn[i];
        }
    }
    println!("max |fluct| = {:.4} at n = {} (main term there ~ {:.1})", mx, mxi, main_term(mxi));
    println!("min residual = {:.4} at n = {} (lambda_n > 0 for all n<=1000 termwise: on-line zeros give 2(1-cos)>=0)", mn, mni);

    // 5) large n samples up to 10^4 with analytic tail correction
    // tail beyond Gamma=5.6e5: (n^2/2pi)(log(Gamma/2pi e)+1)/Gamma  [pair term ~ (n/gamma)^2 for gamma >> n]
    let gamma_tail = gs924[gs924.len() - 1];
    let tail_coeff = ((gamma_tail / (2.0 * std::f64::consts::PI * std::f64::consts::E)).ln() + 1.0) / (2.0 * std::f64::consts::PI * gamma_tail);
    println!("== LARGE n (tail-corrected) ==");
    for &n in &[2000usize, 3000, 5000, 10000] {
        let l = lambda_from_phis(&ph924, n, 0);
        let tail = (n as f64) * (n as f64) * tail_coeff;
        let lc = l + tail;
        let m = main_term(n);
        println!("  n={:>5}  lambda_n={:>10.3}  +tail({:>6.1}) = {:>10.3}   main={:>10.3}   residual={:>9.3} ({:.3}% of main)", n, l, tail, lc, m, lc - m, 100.0 * (lc - m).abs() / m);
    }
}
