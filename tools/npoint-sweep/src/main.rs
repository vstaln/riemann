// npoint-sweep — n-point generalization of the rank-trace simple-zeros bound.
//
// Formula (research/ladder-f-family/threshold.py, trmdy proof, exact):
//   F_n(g) = p*sum g_i + sum_{i<j} a_ij w(y_j - y_i) >= eps   (all g >= 0)
//   a_ij = 2/(n - (j-i)),  q = n-1 gaps, span capacities exactly 2.
//
// TWO bound forms coexist in the repo:
//   (A) threshold.py / trmdy proof form (the task-mandated reference):
//       A = eps*(m-q),  R = A if A<=1 else 2*sqrt(A)-1,  eta = R/A,
//       B_p = q*p,  bound = (m*H - eta*B_p*(m-1)) / (m - R)
//   (B) certified record form (final_leader.py / bound-sweep, reproduces the
//       certified 0.6732628655343560 exactly):
//       A = eps*(m-q),  thr = m/(m-1),
//       B = A if A<=thr else 2*sqrt((m-1)*A/m)-1+A/m,
//       tau = psum*(m-q)/m,  bound = (H - tau)/(1 - B/m)
// (B) is the certified one.  Sweeps default to (B); pass formA for (A).
//
// H(alpha) (cosine window v(s)=cos(alpha s)):
//   I0 = 2 sin(alpha/2)/alpha,  I2 = 1/2 + sin(alpha)/(2 alpha),
//   J = -2 I2/alpha^2 + (sin(alpha/2)/alpha + 2 cos(alpha/2)/alpha^2)*I0,
//   c = I0^2/(I2+J),  H = 2 - 1/c.
//
// Record config (CERTIFIED): alpha=1.49, p=1/1320 (psum=1/220), eps=0.00806,
// m=133, H(1.49)=0.6724218860964 -> bound = 0.6732628655343560.
//
// Subcommands:
//   rec        — reproduce the certified record (sanity gate)
//   sweep      — max bound over (m, alpha, psum) per n, eps = kappa*p model
//   epsreq     — required eps to beat the record per n
//   kappareq   — required kappa = eps/p to beat the record per n
//   ffloor     — F_n infimum float estimate over gap configs (the decisive
//                check: does the n-point floor DROP below the 7-point one?)
#![allow(clippy::excessive_precision)]

use std::env;

const RECORD: f64 = 0.6732628655343560_f64;

// ---------------------------------------------------------------------------
// Window functional H(alpha)
// ---------------------------------------------------------------------------
fn h_window(alpha: f64) -> f64 {
    let a = alpha / 2.0;
    let i0 = 2.0 * a.sin() / alpha;
    let i2 = 0.5 + alpha.sin() / (2.0 * alpha);
    let constant = a.sin() / alpha + 2.0 * a.cos() / (alpha * alpha);
    let j = -2.0 * i2 / (alpha * alpha) + constant * i0;
    let c = i0 * i0 / (i2 + j);
    2.0 - 1.0 / c
}

// ---------------------------------------------------------------------------
// n-point bound, form A (threshold.py / trmdy): p is per-gap pressure
// ---------------------------------------------------------------------------
fn bound_a(n: usize, eps: f64, m: usize, alpha: f64, p: f64) -> f64 {
    let q = (n - 1) as f64;
    let h = h_window(alpha);
    let a = eps * (m as f64 - q);
    let r = if a <= 1.0 { a } else { 2.0 * a.sqrt() - 1.0 };
    let eta = r / a;
    let b_p = q * p;
    (m as f64 * h - eta * b_p * (m as f64 - 1.0)) / (m as f64 - r)
}

// ---------------------------------------------------------------------------
// n-point bound, form B (certified record form): psum is TOTAL block pressure
// ---------------------------------------------------------------------------
fn bound_b(n: usize, eps: f64, m: usize, alpha: f64, psum: f64) -> f64 {
    let q = (n - 1) as f64;
    let h = h_window(alpha);
    let a = eps * (m as f64 - q);
    let thr = m as f64 / (m as f64 - 1.0);
    let b = if a <= thr {
        a
    } else {
        2.0 * ((m as f64 - 1.0) * a / m as f64).sqrt() - 1.0 + a / m as f64
    };
    let tau = psum * (m as f64 - q) / m as f64;
    (h - tau) / (1.0 - b / m as f64)
}

// ---------------------------------------------------------------------------
// Bisect eps so bound == target; None if even eps->0 can't reach target.
// form=true: certified (B); form=false: threshold.py (A).
// ---------------------------------------------------------------------------
fn eps_for_target(n: usize, m: usize, alpha: f64, psum: f64, target: f64, form: bool) -> Option<f64> {
    // NOTE: bound_b can exceed H(alpha) because the denominator (1 - B/m)
    // is < 1 when B > 0.  So we must NOT early-return when H < target.
    let bfun = |eps: f64| {
        if form {
            bound_b(n, eps, m, alpha, psum)
        } else {
            bound_a(n, eps, m, alpha, psum / (n - 1) as f64)
        }
    };
    if bfun(0.0) >= target {
        // eps=0 already exceeds target: requirement is 0.
        return Some(0.0);
    }
    let mut lo = 0.0;
    let mut hi = 0.001;
    while bfun(hi) < target && hi < 1e6 {
        hi *= 2.0;
    }
    if bfun(hi) < target {
        return None;
    }
    for _ in 0..200 {
        let mid = 0.5 * (lo + hi);
        if bfun(mid) >= target {
            hi = mid;
        } else {
            lo = mid;
        }
    }
    Some(0.5 * (lo + hi))
}

// ---------------------------------------------------------------------------
// Sweep: max bound over (m, alpha, psum) with eps = kappa*p model
// (CONJECTURED frontier; record F6 kappa = 10.64).
// ---------------------------------------------------------------------------
fn sweep(ns: &[usize], kappa: f64, form: bool) {
    let which = if form { "B (certified record form)" } else { "A (threshold.py form)" };
    println!("=== constrained-ceiling sweep: eps = kappa*p, kappa={}, form={} ===", kappa, which);
    println!("{:>3} {:>18} {:>18} {:>10} {:>10} {:>10} {:>10} {:>12}", "n", "max_bound", "alpha", "psum", "p", "eps", "m", "vs record");
    for &n in ns {
        let mut best = -1.0f64;
        let mut best_cfg = (0.0f64, 0.0f64, 0.0f64, 0usize);
        let mut alpha = 1.30;
        while alpha <= 1.62 {
            let mut pden = 100;
            while pden <= 20000 {
                let psum = 1.0 / pden as f64;
                let p = psum / (n - 1) as f64;
                let eps = kappa * p;
                let mut m = n + 1;
                while m <= 3000 {
                    let b = if form {
                        bound_b(n, eps, m, alpha, psum)
                    } else {
                        bound_a(n, eps, m, alpha, p)
                    };
                    if b > best {
                        best = b;
                        best_cfg = (alpha, psum, eps, m);
                    }
                    m += 1;
                }
                pden = if pden < 2000 { (pden as f64 * 1.07).ceil() as usize } else { pden * 2 };
            }
            alpha += 0.005;
        }
        println!(
            "{:>3} {:>18.10} {:>18.4} {:>10.7} {:>10.7} {:>10.7} {:>10} {:>+12.2e}",
            n,
            best,
            best_cfg.0,
            best_cfg.1,
            best_cfg.1 / (n - 1) as f64,
            best_cfg.2,
            best_cfg.3,
            best - RECORD
        );
    }
}

// ---------------------------------------------------------------------------
// Required eps to beat the record.
// ---------------------------------------------------------------------------
fn eps_required(ns: &[usize], form: bool) {
    let which = if form { "B (record form)" } else { "A (threshold.py form)" };
    println!("=== eps* to beat record {} (bisect, alpha=1.49, form={}) ===", RECORD, which);
    for &n in ns {
        let alpha = 1.49;
        for (psum_label, psum) in [("1/220", 1.0 / 220.0), ("1/2200", 1.0 / 2200.0)] {
            let mut best_eps = f64::INFINITY;
            let mut best_m = 0;
            for m in (n + 1)..5000 {
                if let Some(e) = eps_for_target(n, m, alpha, psum, RECORD, form) {
                    if e < best_eps {
                        best_eps = e;
                        best_m = m;
                    }
                }
            }
            println!("n={:>2} psum={:>6}: min eps* = {:.8} at m={}", n, psum_label, best_eps, best_m);
        }
    }
}

// ---------------------------------------------------------------------------
// F_n evaluation and float infimum search
// ---------------------------------------------------------------------------

fn sinc(z: f64) -> f64 {
    if z == 0.0 {
        1.0
    } else {
        z.sin() / z
    }
}

// Cosine kernel K(x) = (sinc(pi x - alpha/2) + sinc(pi x + alpha/2))/2,
// w(x) = (K(x)/K(0))^2.
struct Ker {
    alpha: f64,
    k0: f64,
    // scale: true = w = (k/k0)^2 (theory, w(0)=1)
    //        false = w = k^2/k0^2 (verifier's double-normalized kernel, w(0)=1/k0^2)
    // The verifier's build_tables/squared_kernel_derivs computes w = k^2/k0^2
    // (see verify_cos7.py: w = k*k/k0sq) — the certified 0.00806 is for THIS.
    scale: bool,
}

impl Ker {
    fn new(alpha: f64) -> Self {
        let k0 = 2.0 * (alpha / 2.0).sin() / alpha;
        Ker { alpha, k0, scale: true }
    }
    fn new_verifier(alpha: f64) -> Self {
        let k0 = 2.0 * (alpha / 2.0).sin() / alpha;
        Ker { alpha, k0, scale: false }
    }
    fn w(&self, x: f64) -> f64 {
        let a = self.alpha;
        let z1 = std::f64::consts::PI * x - a / 2.0;
        let z2 = std::f64::consts::PI * x + a / 2.0;
        let k = 0.5 * (sinc(z1) + sinc(z2));
        let k0sq = self.k0 * self.k0;
        if self.scale {
            let r = k / self.k0;
            r * r
        } else {
            k * k / k0sq
        }
    }
}

// F_n(g) = p*sum g_i + sum_{i<j} a_ij w(y_j - y_i), a_ij = 2/(n-(j-i))
fn f_n(ker: &Ker, n: usize, p: f64, gaps: &[f64]) -> f64 {
    let mut total = 0.0;
    for &g in gaps {
        total += p * g;
    }
    let mut y = vec![0.0; n];
    for i in 1..n {
        y[i] = y[i - 1] + gaps[i - 1];
    }
    for i in 0..n {
        for j in (i + 1)..n {
            let aij = 2.0 / (n as f64 - (j - i) as f64);
            total += aij * ker.w(y[j] - y[i]);
        }
    }
    total
}

// F_n infimum float estimate via random-restart coordinate descent plus
// a coarse grid scan for global coverage.  Float estimate (CONJECTURED) —
// the interval verifier is the ground truth.  Mirrors the approach of
// cert_floor_scan.py (Nelder-Mead + many restarts) that finds F6 ~ 0.0081.
// verifier_kernel=false: theory kernel w=(k/k0)^2 (w(0)=1)
// verifier_kernel=true:  double-normalized w=k^2/k0^2 (as verify_cos7 computes)
fn f_floor_mode(alpha: f64, n: usize, p: f64, restarts: usize, seed: u64, verifier_kernel: bool) -> (f64, Vec<f64>) {
    let q = n - 1;
    let ker = if verifier_kernel { Ker::new_verifier(alpha) } else { Ker::new(alpha) };
    let mut rng_state = seed.wrapping_mul(0x9E3779B97F4A7C15).wrapping_add(0x1234567);
    let mut rnd = move || {
        rng_state ^= rng_state << 13;
        rng_state ^= rng_state >> 7;
        rng_state ^= rng_state << 17;
        (rng_state >> 11) as f64 / (1u64 << 53) as f64
    };

    let mut best = f64::INFINITY;
    let mut best_g = vec![0.0; q];

    // structured seeds (mirror the Python probe)
    let mut seeds: Vec<Vec<f64>> = Vec::new();
    for base in [0.8, 1.0, 1.03, 1.2, 1.98, 2.0, 2.6, 3.0] {
        seeds.push(vec![base; q]);
    }
    for (a, b) in [(0.5, 1.5), (0.7, 1.3), (1.03, 1.98), (0.3, 1.7)] {
        let mut s = Vec::with_capacity(q);
        for k in 0..q {
            s.push(if k % 2 == 0 { a } else { b });
        }
        seeds.push(s);
    }
    // theorist F6 argmin pattern (known good)
    if q >= 6 {
        let t6 = [1.04, 1.03, 1.95, 1.03, 1.02, 1.03];
        let mut s = Vec::with_capacity(q);
        for k in 0..q {
            s.push(t6[k % 6]);
        }
        seeds.push(s);
        let t6b = [1.046, 1.979, 1.042, 1.986, 1.991, 1.047];
        let mut s = Vec::with_capacity(q);
        for k in 0..q {
            s.push(t6b[k % 6]);
        }
        seeds.push(s);
    }
    for _ in 0..restarts {
        let mut s = Vec::with_capacity(q);
        for _ in 0..q {
            s.push(0.3 + rnd() * 2.7);
        }
        seeds.push(s);
    }

    // evaluate each seed with coordinate descent
    for (si, seed_g) in seeds.iter().enumerate() {
        let mut g = seed_g.clone();
        let mut val = f_n(&ker, n, p, &g);
        let iters = 8000 + (si % 5) * 2000;
        let mut step0 = 0.15;
        let mut step = step0;
        for _ in 0..iters {
            let k = (rnd() * q as f64) as usize;
            let delta = (rnd() * 2.0 - 1.0) * step;
            let newv = g[k] + delta;
            if newv < 0.0 {
                continue;
            }
            let old = g[k];
            g[k] = newv;
            let nv = f_n(&ker, n, p, &g);
            if nv < val {
                val = nv;
                step = step0;
            } else {
                g[k] = old;
                step *= 0.9995;
                if step < 1e-4 {
                    step = step0;
                }
            }
        }
        if val < best {
            best = val;
            best_g = g;
        }
    }
    (best, best_g)
}

fn f_floor(alpha: f64, n: usize, p: f64, restarts: usize, seed: u64) -> (f64, Vec<f64>) {
    f_floor_mode(alpha, n, p, restarts, seed, false)
}

// Full deterministic coarse grid over [0,3]^q (used as an independent
// cross-check to the descent; q<=8 to keep the count sane).
fn f_floor_grid(alpha: f64, n: usize, p: f64, grid_pts: usize) -> (f64, Vec<f64>) {
    let q = n - 1;
    let ker = Ker::new(alpha);
    let gmax = 3.0;
    let mut best = f64::INFINITY;
    let mut best_g = vec![0.0; q];
    let mut g = vec![0.0; q];
    let mut idx: Vec<usize> = vec![0; q];
    let total_pts = grid_pts.pow(q as u32) as usize;
    for _ in 0..total_pts {
        for k in 0..q {
            g[k] = idx[k] as f64 / (grid_pts - 1) as f64 * gmax;
        }
        let v = f_n(&ker, n, p, &g);
        if v < best {
            best = v;
            best_g = g.clone();
        }
        let mut carry = 1;
        for k in 0..q {
            idx[k] += carry;
            if idx[k] >= grid_pts {
                idx[k] = 0;
                carry = 1;
            } else {
                carry = 0;
                break;
            }
        }
        if carry == 1 {
            break;
        }
    }
    (best, best_g)
}

fn ffloor(ns: &[usize], alphas: &[f64], p: f64) {
    println!("=== F_n infimum float estimates (cosine kernel, per-gap pressure p={}) ===", p);
    println!("  [kernel=theory: w=(k/k0)^2, w(0)=1]");
    println!("{:>3} {:>10} {:>14} {:>14} {:>10} {:>10}", "n", "alpha", "F_inf~", "per_point", "H", "kappa=F/p");
    for &n in ns {
        for &alpha in alphas {
            let (b, g) = f_floor(alpha, n, p, 120, 1000 + n as u64 * 7);
            println!(
                "{:>3} {:>10.2} {:>14.8} {:>14.8} {:>10.8} {:>10.2}",
                n,
                alpha,
                b,
                b / n as f64,
                h_window(alpha),
                b / p
            );
            println!(
                "      argmin gaps: {:?}",
                g.iter().map(|x| (x * 100.0).round() / 100.0).collect::<Vec<_>>()
            );
        }
    }
}

// Same, but with the verifier's double-normalized kernel w=k^2/k0^2 (the
// kernel whose floor the certification 0.00806 is actually about).
fn ffloor_v(ns: &[usize], alphas: &[f64], p: f64) {
    println!("=== F_n infimum (VERIFIER kernel w=k^2/k0^2, per-gap pressure p={}) ===", p);
    println!("{:>3} {:>10} {:>14} {:>14} {:>10}", "n", "alpha", "F_inf~", "per_point", "kappa=F/p");
    for &n in ns {
        for &alpha in alphas {
            let (b, g) = f_floor_mode(alpha, n, p, 120, 1000 + n as u64 * 7, true);
            println!(
                "{:>3} {:>10.2} {:>14.8} {:>14.8} {:>10.2}",
                n,
                alpha,
                b,
                b / n as f64,
                b / p
            );
            println!(
                "      argmin gaps: {:?}",
                g.iter().map(|x| (x * 100.0).round() / 100.0).collect::<Vec<_>>()
            );
        }
    }
}

// ---------------------------------------------------------------------------
// Required kappa = eps/p to beat the record.
// ---------------------------------------------------------------------------
fn kappareq(ns: &[usize], form: bool) {
    let which = if form { "B (record form)" } else { "A (threshold.py form)" };
    println!("=== required kappa = eps/p to beat record (alpha=1.49, psum=1/220, form={}) ===", which);
    for &n in ns {
        let alpha = 1.49;
        let psum = 1.0 / 220.0;
        let p = psum / (n - 1) as f64;
        let mut best_eps = f64::INFINITY;
        for m in (n + 1)..5000 {
            if let Some(e) = eps_for_target(n, m, alpha, psum, RECORD, form) {
                if e < best_eps {
                    best_eps = e;
                }
            }
        }
        println!(
            "n={:>2}: required eps*={:.8}, kappa*={:.4} (record F6 kappa=10.64)",
            n,
            best_eps,
            best_eps / p
        );
    }
}

// ---------------------------------------------------------------------------
// Sanity gate: reproduce the certified record.
// ---------------------------------------------------------------------------
fn rec_check() {
    let h = h_window(1.49);
    let b = bound_b(7, 0.00806, 133, 1.49, 1.0 / 220.0);
    println!("H(1.49)     = {:.16}", h);
    println!("bound_b(n=7)= {:.16}", b);
    println!("record      = 0.6732628655343560");
    println!("diff        = {:.3e}", (b - RECORD).abs());
    let ba = bound_a(7, 0.00806, 133, 1.49, 1.0 / 1320.0);
    println!("bound_a(n=7)= {:.16} (threshold.py form, not the record)", ba);
}

fn eval_cfg(alpha: f64, n: usize, p: f64, gaps: &[f64]) {
    let ker = Ker::new(alpha);
    println!("F_n(alpha={}, n={}, p={}, gaps={:?}) = {:.10}", alpha, n, p, gaps, f_n(&ker, n, p, gaps));
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let cmd = args.get(1).map(|s| s.as_str()).unwrap_or("sweep");
    let ns: Vec<usize> = vec![7, 8, 9, 11, 13, 15];
    let form = !args.iter().any(|a| a == "formA");
    match cmd {
        "rec" => rec_check(),
        "eval" => {
            let alpha: f64 = args.get(2).and_then(|s| s.parse().ok()).unwrap_or(1.49);
            let n: usize = args.get(3).and_then(|s| s.parse().ok()).unwrap_or(7);
            let p: f64 = args.get(4).and_then(|s| s.parse().ok()).unwrap_or(1.0 / 1320.0);
            let gaps: Vec<f64> = args[5..].iter().filter_map(|s| s.parse().ok()).collect();
            eval_cfg(alpha, n, p, &gaps);
        }
        "sweep" => {
            let kappa: f64 = args.get(2).and_then(|s| s.parse().ok()).unwrap_or(10.7);
            sweep(&ns, kappa, form);
        }
        "epsreq" => eps_required(&ns, form),
        "ffloor" => {
            let ns_arg: Vec<usize> = args
                .get(2)
                .map(|s| s.split(',').filter_map(|x| x.parse().ok()).collect())
                .unwrap_or(vec![7, 9, 11]);
            let p: f64 = args.get(3).and_then(|s| s.parse().ok()).unwrap_or(1.0 / 1320.0);
            let alphas: Vec<f64> = args
                .get(4)
                .map(|s| s.split(',').filter_map(|x| x.parse().ok()).collect())
                .unwrap_or(vec![1.49]);
            if args.iter().any(|a| a == "v") {
                ffloor_v(&ns_arg, &alphas, p);
            } else {
                ffloor(&ns_arg, &alphas, p);
            }
        }
        "kappareq" => kappareq(&ns, form),
        _ => {
            eprintln!("usage: npoint-sweep <rec|sweep|epsreq|ffloor|kappareq> [args] [formA|formB]");
            std::process::exit(2);
        }
    }
}
