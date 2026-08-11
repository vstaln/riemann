use std::env;
use std::f64::consts::PI;
use std::fs;

mod zeta;
use zeta::*;



#[derive(Clone, Copy)]
enum Sign {
    Pos,
    Neg,
    Indef,
}

fn sign_of(z: f64, err: f64) -> Sign {
    if z - err > 0.0 {
        Sign::Pos
    } else if z + err < 0.0 {
        Sign::Neg
    } else {
        Sign::Indef
    }
}

// ---------------------------------------------------------------------------
// Scan [T, T+H] for sign changes of Z, bracket each with certified bisection.
// Returns (brackets, total_evaluations, max_err_seen).
// ---------------------------------------------------------------------------
fn find_brackets(t0: f64, h: f64, step: f64) -> (Vec<(f64, f64)>, usize, f64) {
    let mut out = Vec::new();
    let mut evals = 0usize;
    let mut max_err = 0.0f64;
    let mut prev_t = t0;
    let (mut z_prev, e0, _) = z_cert(t0);
    evals += 1;
    max_err = max_err.max(e0);
    let mut prev_s = sign_of(z_prev, e0);
    let mut t = t0 + step;
    while t <= t0 + h + 1e-9 {
        let (z, e, _) = z_cert(t);
        evals += 1;
        max_err = max_err.max(e);
        let s = sign_of(z, e);
        if (matches!(prev_s, Sign::Pos) && matches!(s, Sign::Neg))
            || (matches!(prev_s, Sign::Neg) && matches!(s, Sign::Pos))
        {
            // certified sign change in (prev_t, t): bracket with bisection.
            // Invariant: Z(a) has the same definite sign as fa; Z(b) the opposite.
            let (mut a, mut b, mut fa) = (prev_t, t, z_prev);
            for _ in 0..80 {
                let mid = 0.5 * (a + b);
                let (zm, em, _) = z_cert(mid);
                evals += 1;
                max_err = max_err.max(em);
                // correct bisection: if sign(zm) == sign(fa), root in (mid, b): move a;
                // else root in (a, mid): move b.  Invariant: Z(a), Z(b) opposite.
                match sign_of(zm, em) {
                    Sign::Indef => break, // |Z(mid)| < err near the root; [a,b] still brackets
                    Sign::Pos => {
                        if matches!(sign_of(fa, 0.0), Sign::Pos) {
                            a = mid;
                            fa = zm;
                        } else {
                            b = mid;
                        }
                    }
                    Sign::Neg => {
                        if matches!(sign_of(fa, 0.0), Sign::Neg) {
                            a = mid;
                            fa = zm;
                        } else {
                            b = mid;
                        }
                    }
                }
                if b - a < 1e-9 {
                    break;
                }
            }
            out.push((a, b));
        }
        prev_t = t;
        z_prev = z;
        prev_s = s;
        t += step;
    }
    (out, evals, max_err)
}

// ---------------------------------------------------------------------------
// Numerical (UNCERTIFIED) winding number of ξ̃(s) = s(s-1)π^{-s/2}Γ(s/2)ζ(s)/2
// on the rectangle [0,1]×[T,T+H], counterclockwise.  Returns the winding and
// the max |Δarg| per sample step (must be << π for the unwrap to be sound).
// ---------------------------------------------------------------------------
fn ln_gamma_im(x: f64, y: f64) -> f64 {
    // Im ln Γ(x + iy), Stirling m=6, for x ≥ 0 (numerical, uncertified)
    let lz = (x * x + y * y).ln() / 2.0;
    let az = y.atan2(x);
    let mut th = (x - 0.5) * az + y * lz - y;
    // B_{2k}/(2k(2k-1)) · |z|^{1-2k} · sin((1-2k) az)
    let coefs: [(f64, usize); 6] = [
        (1.0 / 6.0, 2),
        (-1.0 / 30.0, 4),
        (1.0 / 42.0, 6),
        (-1.0 / 30.0, 8),
        (5.0 / 66.0, 10),
        (-691.0 / 2730.0, 12),
    ];
    let mag = (x * x + y * y).sqrt();
    for (b, k) in coefs {
        let coef = b / ((k * (k - 1)) as f64);
        let p = 1 - 2 * k as i32;
        th += coef * mag.powi(p) * ((p as f64) * az).sin();
    }
    th
}

fn arg_zeta(s_re: f64, s_im: f64, n: usize, lns: &[f64]) -> f64 {
    let (re, im, _) = zeta_em_cert(s_re, s_im, s_im, n, lns, 45);
    im.atan2(re)
}

fn winding(t0: f64, h: f64, ds: f64) -> (f64, f64, f64, f64, f64, f64, f64, f64, f64, f64, f64, f64) {
    // rectangle [0,1] x [t0, t0+h], CCW: bottom (σ 0→1), right (t ↑), top (σ 1→0), left (t ↓)
    let n = ((1.6 * (t0 + h) / (2.0 * PI)).ceil().max(10.0)) as usize;
    let lns: Vec<f64> = (0..n).map(|j| if j == 0 { 0.0 } else { (j as f64).ln() }).collect();
    let mut total = 0.0f64;
    let mut max_d = 0.0f64;
    let max_dz = std::cell::Cell::new(0.0f64);
    let max_dg = std::cell::Cell::new(0.0f64);
    let n_big = std::cell::Cell::new(0usize);
    // we track the arg of each factor separately (product rule) and sum deltas
    let mut prev_s: Option<f64> = None;
    let mut prev_g: Option<f64> = None;
    let mut prev_z: Option<f64> = None;
    let mut prev_p: Option<f64> = None;
    let mut total_g = 0.0f64;
    let mut total_z = 0.0f64;
    let mut total_s = 0.0f64;
    let mut total_p = 0.0f64;
    let mut edge_z = [0.0f64; 4];
    let mut edge_i = 0usize;
    let mut unwrap = |cur: f64, prev: &mut Option<f64>| -> f64 {
        let d = match *prev {
            Some(p) => {
                let mut dd = cur - p;
                while dd > PI {
                    dd -= 2.0 * PI;
                }
                while dd <= -PI {
                    dd += 2.0 * PI;
                }
                dd
            }
            None => 0.0,
        };
        *prev = Some(cur);
        d
    };

    let mut unwrap_cur = 0.0f64;
    let mut eval = |s_re: f64, s_im: f64,
                    total_s: &mut f64,
                    total_g: &mut f64,
                    total_z: &mut f64,
                    total_p: &mut f64,
                    prev_s: &mut Option<f64>,
                    prev_g: &mut Option<f64>,
                    prev_z: &mut Option<f64>,
                    prev_p: &mut Option<f64>,
                    max_d: &mut f64| {
        // arg(s(s-1)/2)
        let a1 = s_im.atan2(s_re);
        let a2 = s_im.atan2(s_re - 1.0);
        let a_s = a1 + a2; // continuous-ish; unwrap composite
        // arg π^{-s/2} = -(t/2) ln π
        let a_p = -0.5 * s_im * PI.ln();
        // arg Γ(s/2)
        let a_g = ln_gamma_im(s_re / 2.0, s_im / 2.0);
        // arg ζ(s)
        let a_z = arg_zeta(s_re, s_im, n, &lns);
        let d_s = unwrap(a_s, prev_s);
        let d_g = unwrap(a_g, prev_g);
        let d_z = unwrap(a_z, prev_z);
        let d_p = unwrap(a_p, prev_p);
        unwrap_cur = d_z;
        *total_s += d_s;
        *total_g += d_g;
        *total_z += d_z;
        *total_p += d_p;
        *max_d = (*max_d).max(d_z.abs()).max(d_s.abs()).max(d_g.abs());
        max_dz.set(max_dz.get().max(d_z.abs()));
        max_dg.set(max_dg.get().max(d_g.abs()));
        if d_z.abs() > 0.8 * PI {
            n_big.set(n_big.get() + 1);
        }
    };

    // bottom: σ 0→1 at t=t0
    let mut sigma = 0.0;
    edge_i = 0;
    while sigma <= 1.0 + 1e-9 {
        eval(sigma, t0, &mut total_s, &mut total_g, &mut total_z, &mut total_p, &mut prev_s, &mut prev_g, &mut prev_z, &mut prev_p, &mut max_d);
        edge_z[edge_i] += unwrap_cur;
        sigma += ds;
    }
    // right: t t0→t0+h at σ=1
    let mut tt = t0 + ds;
    edge_i = 1;
    while tt <= t0 + h + 1e-9 {
        eval(1.0, tt, &mut total_s, &mut total_g, &mut total_z, &mut total_p, &mut prev_s, &mut prev_g, &mut prev_z, &mut prev_p, &mut max_d);
        edge_z[edge_i] += unwrap_cur;
        tt += ds;
    }
    // top: σ 1→0 at t=t0+h
    let mut sigma = 1.0 - ds;
    edge_i = 2;
    while sigma >= -1e-9 {
        eval(sigma, t0 + h, &mut total_s, &mut total_g, &mut total_z, &mut total_p, &mut prev_s, &mut prev_g, &mut prev_z, &mut prev_p, &mut max_d);
        edge_z[edge_i] += unwrap_cur;
        sigma -= ds;
    }
    // left: t t0+h→t0 at σ=0
    let mut tt = t0 + h - ds;
    edge_i = 3;
    while tt >= t0 - 1e-9 {
        eval(0.0, tt, &mut total_s, &mut total_g, &mut total_z, &mut total_p, &mut prev_s, &mut prev_g, &mut prev_z, &mut prev_p, &mut max_d);
        edge_z[edge_i] += unwrap_cur;
        tt -= ds;
    }
    total = total_s + total_g + total_z + total_p;
    (total / (2.0 * PI), max_d, max_dz.get().max(max_dg.get()), n_big.get() as f64,
     total_z, total_g, total_s, total_p, edge_z[0], edge_z[1], edge_z[2], edge_z[3])
}

// ---------------------------------------------------------------------------
// RvM main term and the explicit Trudgian bound on |S(t)|
// ---------------------------------------------------------------------------
fn rvm_main(t: f64) -> f64 {
    let x = t / (2.0 * PI);
    (t / (2.0 * PI)) * (x.ln() - 1.0) + 7.0 / 8.0
}

fn trudgian_s_bound(t: f64) -> f64 {
    // Trudgian 2014: |S(t)| ≤ 0.112 log t + 0.278 log log t + 2.510, t ≥ 3
    0.112 * t.ln() + 0.278 * t.ln().ln().max(0.0) + 2.510
}

// ---------------------------------------------------------------------------
fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 4 {
        eprintln!("usage: argprinciple T H step [lmfdb-data-dir]");
        std::process::exit(1);
    }
    let t0: f64 = args[1].parse().unwrap();
    let h: f64 = args[2].parse().unwrap();
    let step: f64 = args[3].parse().unwrap();
    let datadir = if args.len() > 4 { args[4].clone() } else { String::new() };

    // ---- error-budget spot check at the top of the strip ------------------
    let (z0, e0, n0) = z_cert(t0);
    let (z1, e1, n1) = z_cert(t0 + h);
    let n0u = n0 as usize;
    let n1u = n1 as usize;
    let lns0: Vec<f64> = (0..n0u).map(|j| if j == 0 { 0.0 } else { (j as f64).ln() }).collect();
    let lns1: Vec<f64> = (0..n1u).map(|j| if j == 0 { 0.0 } else { (j as f64).ln() }).collect();
    let (_r0, _i0, _e0, b0) = zeta_em_cert_budget(0.5, t0, t0, n0u, &lns0, 40);
    let (_r1, _i1, _e1, b1) = zeta_em_cert_budget(0.5, t0 + h, t0 + h, n1u, &lns1, 40);
    println!("== error budget @ T={} (K=40 EM terms) ==", t0);
    println!("  Z({}) = {:.6e}  certified err = {:.3e}", t0, z0, e0);
    println!("  Z({}) = {:.6e}  certified err = {:.3e}", t0 + h, z1, e1);
    println!("  @T:    main-sum round {:.2e}  corr round {:.2e}  EM remainder {:.2e}", b0.main_round, b0.corr_round, b0.rem);
    println!("  @T+H:  main-sum round {:.2e}  corr round {:.2e}  EM remainder {:.2e}", b1.main_round, b1.corr_round, b1.rem);
    println!("  N (EM main-sum length) = {} / {}", n0u, n1u);

    // ---- certified sign changes ------------------------------------------
    let (brackets, evals, max_err) = find_brackets(t0, h, step);
    println!("== certified scan ==");
    println!("  evaluations: {}", evals);
    println!("  max certified |Z| error: {:.3e}", max_err);
    println!("  bracketed sign changes (on-line zeros): {}", brackets.len());
    println!("  brackets: (a, b), width, mid");
    for (a, b) in &brackets {
        println!("    [{:.12e}, {:.12e}]  width={:.2e}  mid={:.12e}", a, b, b - a, 0.5 * (a + b));
    }

    // ---- cross-check with LMFDB ordinates --------------------------------
    let mut lmfdb: Vec<f64> = Vec::new();
    if !datadir.is_empty() {
        if let Ok(entries) = fs::read_dir(&datadir) {
            for e in entries.flatten() {
                let p = e.path();
                if p.extension().map(|x| x == "txt").unwrap_or(false) {
                    let name = p.file_name().unwrap().to_string_lossy().to_string();
                    if name.starts_with("lmfdb_zeros_") {
                        if let Ok(txt) = fs::read_to_string(&p) {
                            for line in txt.lines() {
                                let mut it = line.split_whitespace();
                                let _idx = it.next();
                                if let Some(v) = it.next() {
                                    if let Ok(x) = v.parse::<f64>() {
                                        lmfdb.push(x);
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    lmfdb.sort_by(|a, b| a.partial_cmp(b).unwrap());
    let in_strip: Vec<f64> = lmfdb.iter().copied().filter(|&g| g > t0 && g < t0 + h).collect();
    let n_leq_t0 = lmfdb.iter().filter(|&&g| g <= t0).count();
    let n_leq_th = lmfdb.iter().filter(|&&g| g <= t0 + h).count();
    println!("== LMFDB cross-check (fetched ordinates) ==");
    println!("  ordinates in fetched data: {}; in strip (T, T+H): {}", lmfdb.len(), in_strip.len());
    println!("  N(T) from data = {}, N(T+H) from data = {},  N(T+H)-N(T) = {}",
             n_leq_t0, n_leq_th, n_leq_th - n_leq_t0);
    if !in_strip.is_empty() {
        // every LMFDB ordinate inside exactly one bracket
        let mut miss = 0;
        let mut multi = 0;
        let mut max_dev = 0.0f64;
        for g in &in_strip {
            let mut count = 0;
            for (a, b) in &brackets {
                if *a < *g && *g < *b {
                    count += 1;
                    let mid = 0.5 * (a + b);
                    max_dev = max_dev.max((mid - g).abs());
                }
            }
            if count == 0 {
                miss += 1;
            }
            if count > 1 {
                multi += 1;
            }
        }
        // brackets with no LMFDB ordinate
        let mut no_lm = 0;
        for (a, b) in &brackets {
            if !in_strip.iter().any(|&g| *a < g && g < *b) {
                no_lm += 1;
            }
        }
        println!("  LMFDB ordinates NOT inside any bracket: {}", miss);
        println!("  LMFDB ordinates inside >1 bracket: {}", multi);
        println!("  brackets containing no LMFDB ordinate: {}", no_lm);
        println!("  max |bracket mid − LMFDB ordinate|: {:.3e}", max_dev);
        let ok = miss == 0 && multi == 0 && no_lm == 0
            && in_strip.len() == brackets.len()
            && in_strip.len() == n_leq_th - n_leq_t0;
        println!("  count-match (brackets == LMFDB count): {}", ok);
    }

    // ---- RvM --------------------------------------------------------------
    let main_diff = rvm_main(t0 + h) - rvm_main(t0);
    println!("== Riemann–von Mangoldt ==");
    println!("  main term N(T+H)-N(T) = {:.6}", main_diff);
    let sb = trudgian_s_bound(t0 + h) + trudgian_s_bound(t0);
    println!("  Trudgian |S(T+H)|+|S(T)| ≤ {:.3}  =>  rigorous RvM bracket on N(T+H)-N(T): [{:.3}, {:.3}]",
             sb, main_diff - sb, main_diff + sb);
    if n_leq_th - n_leq_t0 > 0 {
        let s_t0 = n_leq_t0 as f64 - rvm_main(t0);
        let s_th = n_leq_th as f64 - rvm_main(t0 + h);
        println!("  S(T) = N(T) − main = {:.6},  S(T+H) = {:.6}", s_t0, s_th);
    }

    // ---- numerical winding (uncertified) ----------------------------------
    let (w, maxd, maxdg, nbig, tz, tg, ts, tp, ez0, ez1, ez2, ez3) = winding(t0, h, 0.02);
    println!("== numerical argument-principle winding on [0,1]×[T,T+H] ==");
    println!("  winding number: {:.6}   max |Δarg| per step: {:.3} rad (zeta/other)", w, maxd);
    println!("  max |Δarg| for the zeta and Gamma factors: {:.3} rad; steps with |Δarg zeta|>0.8π: {}", maxdg, nbig as usize);
    println!("  Δarg zeta = {:.4} rad (2π·{:.6}), Δarg Gamma = {:.4}, Δarg s(s-1)/2 = {:.4}, Δarg π = {:.4}",
             tz, tz / (2.0 * PI), tg, ts, tp);
    println!("  Δarg zeta per edge: bottom={:.4} right={:.4} top={:.4} left={:.4}", ez0, ez1, ez2, ez3);
    println!("  (UNCERTIFIED — demonstration of the contour count)");

    // ---- p1-type summary --------------------------------------------------
    let c_2_3 = 2.0 / 3.0;
    let c_6725 = 0.6725007036794116; // 3/2 − (1/√2)cot(1/√2), verification-001
    let p0 = 0.6818286874638315; // 256-law simple fraction, attack-lpdual
    let p0_e = p0 + 2.5431315104e-6; // p0 + |E(1)|
    println!("== implied simple-on-line fraction (p1-type) ==");
    let total = n_leq_th - n_leq_t0;
    if total > 0 {
        let frac = brackets.len() as f64 / total as f64;
        println!("  bracketed on-line simple zeros / total zeros in strip = {} / {} = {:.10}", brackets.len(), total, frac);
        println!("  vs 2/3 = {:.10}, 0.6725007036794116 = {:.10}, p0 = {:.10}, p0+|E(1)| = {:.10}",
                 c_2_3, c_6725, p0, p0_e);
        println!("  measured fraction ABOVE all in-class constants: {}", frac > p0_e);
    } else {
        println!("  (no LMFDB data for this strip — fraction unavailable)");
    }
}
