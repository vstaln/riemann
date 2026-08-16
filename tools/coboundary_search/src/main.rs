//! coboundary_search: Rust port of the coboundary-redistribution max-min LP and
//! global float-floor search (Python originals: tools/coboundary-reopt/).
//!
//! F_B(g; l, c) = F0(g) + sum_k l_k (g_{k+1}-g_k) + sum_k c_k (w(g_{k+1})-w(g_k))
//! F0 = P0 sum g_j + Q0 sum w(g_j) + S(y),  P0=1/1920, Q0=1/3,
//! S(y) = sum_{0<=a<b<=6} (2/(7-(b-a))) w(y_b-y_a), y_0=0, y_k = g_1+..+g_k.
//!
//! Two LPs (HiGHS, same solver as scipy):
//!   - full:  vars (l1..l5, c1..c5, v) over the 1089-config family
//!   - sym:   vars (a1,a2,b1,b2,v), l=(a1,a2,0,-a2,-a1), c=(b1,b2,0,-b2,-b1)
//!            over the 578-config family
//! huge-gap rows: kappa_i = P0 + l_{i-1} - l_i >= 0  (l_0 = l_6 = 0).
//!
//! Global float floor: pure-Rust differential evolution (best/1/bin + Nelder-Mead
//! polish) over [0.4,3.5]^6 plus a huge-gap scan g_i in [5,21].
//!
//! SEARCH HEURISTIC ONLY. It certifies nothing; the interval verifier
//! (tools/verify_coboundary_floor.py) is the ground truth for certification.

use std::time::Instant;

const P0: f64 = 1.0 / 1920.0;
const Q0: f64 = 1.0 / 3.0;
const L_BOUND: f64 = 0.0012;

fn sinc(z: f64) -> f64 {
    if z.abs() < 1e-12 {
        1.0 - z * z / 6.0
    } else {
        z.sin() / z
    }
}

/// k_alpha from the Python: 0.5*(sinc(z1/pi)+sinc(z2/pi))/sinc(a/pi),
/// z1 = pi x - a, z2 = pi x + a, a = alpha/2; sinc(t)=sin(pi t)/(pi t).
fn k_alpha(x: f64, alpha: f64) -> f64 {
    let a = alpha / 2.0;
    let z1 = std::f64::consts::PI * x - a;
    let z2 = std::f64::consts::PI * x + a;
    0.5 * (sinc(z1) + sinc(z2)) / sinc(a)
}

fn w_alpha(x: f64, alpha: f64) -> f64 {
    let k = k_alpha(x, alpha);
    k * k
}

fn f0(g: &[f64; 6], alpha: f64) -> f64 {
    let mut y = [0.0f64; 7];
    for i in 0..6 {
        y[i + 1] = y[i] + g[i];
    }
    let mut total = P0 * g.iter().sum::<f64>()
        + Q0 * g.iter().map(|&x| w_alpha(x, alpha)).sum::<f64>();
    for i in 0..7 {
        for j in (i + 1)..7 {
            total += (2.0 / (7.0 - (j - i) as f64)) * w_alpha(y[j] - y[i], alpha);
        }
    }
    total
}

/// (L_k, C_k) for k=0..4: L_k = g_{k+1} - g_k, C_k = w(g_{k+1}) - w(g_k)
fn lin_coeffs(g: &[f64; 6], alpha: f64) -> ([f64; 5], [f64; 5]) {
    // g0 = [0, g_1..g_6, 0]
    let mut g0 = [0.0f64; 8];
    for i in 0..6 {
        g0[i + 1] = g[i];
    }
    let mut l = [0.0f64; 5];
    let mut c = [0.0f64; 5];
    for k in 0..5 {
        l[k] = g0[k + 2] - g0[k + 1];
        c[k] = w_alpha(g0[k + 2], alpha) - w_alpha(g0[k + 1], alpha);
    }
    (l, c)
}

fn f_b(g: &[f64; 6], alpha: f64, l: &[f64; 5], c: &[f64; 5]) -> f64 {
    let (l_, c_) = lin_coeffs(g, alpha);
    f0(g, alpha) + dot(&l_, l) + dot(&c_, c)
}

fn dot(a: &[f64; 5], b: &[f64; 5]) -> f64 {
    a.iter().zip(b.iter()).map(|(x, y)| x * y).sum()
}

/// kappa_i = P0 + l_{i-1} - l_i, i=1..6 (l_0 = l_6 = 0)
fn kappa(l: &[f64; 5]) -> [f64; 6] {
    let mut out = [0.0f64; 6];
    for i in 0..6 {
        let li = if i == 0 { 0.0 } else { l[i - 1] };
        let li1 = if i == 5 { 0.0 } else { l[i] };
        out[i] = P0 + li - li1;
    }
    out
}

fn read_cfgs(path: &str) -> Vec<[f64; 6]> {
    let txt = std::fs::read_to_string(path).expect("read cfg file");
    let mut out = Vec::new();
    for line in txt.lines() {
        let s = line.trim();
        if s.is_empty() {
            continue;
        }
        let mut v = [0.0f64; 6];
        for (i, tok) in s.split_whitespace().enumerate() {
            v[i] = tok.parse().expect("parse f64");
        }
        out.push(v);
    }
    out
}

// ---------------------------------------------------------------------------
// LP solvers (self-contained bounded-variable simplex, pure Rust)
// ---------------------------------------------------------------------------

/// Solve: minimize c.x  s.t.  A.x <= b,  lo <= x <= hi.
/// Standard-form two-phase simplex: shift x = lo + t (t >= 0), add explicit
/// upper-bound rows t_j <= hi_j - lo_j, start from the all-slack basis
/// (t = 0 is feasible), pivot with Dantzig's rule. x = 0 always feasible so no
/// artificials are needed. Validated against scipy/HiGHS reference values.
fn bounded_simplex(a: &[Vec<f64>], b: &[f64], lo: &[f64], hi: &[f64], c: &[f64]) -> Option<Vec<f64>> {
    let n = c.len();
    let m = a.len();
    assert_eq!(m, b.len());
    // b' = b - A.lo  (constraints on t);  u_j = hi_j - lo_j
    let mut b2 = Vec::with_capacity(m + n);
    for i in 0..m {
        let mut bi = b[i];
        for j in 0..n {
            bi -= a[i][j] * lo[j];
        }
        b2.push(bi);
    }
    let m2 = m + n;
    let cols = n + m2 + 1; // vars + slacks + rhs
    let mut t = vec![vec![0.0f64; cols]; m2 + 1];
    // row 0: objective (reduced costs; initially c since c_B = 0)
    for j in 0..n {
        t[0][j] = c[j];
    }
    for i in 0..m {
        for j in 0..n {
            t[i + 1][j] = a[i][j];
        }
        t[i + 1][n + i] = 1.0; // slack column
        t[i + 1][cols - 1] = b2[i];
        if b2[i] < 0.0 {
            for j in 0..cols {
                t[i + 1][j] = -t[i + 1][j];
            }
        }
    }
    for j in 0..n {
        let i = m + j;
        t[i + 1][j] = 1.0;
        t[i + 1][n + i] = 1.0;
        t[i + 1][cols - 1] = hi[j] - lo[j];
    }
    let mut basis: Vec<usize> = (0..m2).map(|i| n + i).collect();
    let eps = 1e-12;
    for _ in 0..20_000 {
        // entering column: most negative reduced cost
        let mut enter = None;
        let mut best = -1e-9;
        for col in 0..(n + m2) {
            if t[0][col] < best {
                best = t[0][col];
                enter = Some(col);
            }
        }
        let Some(enter) = enter else { break }; // optimal
        // leaving row: min ratio test
        let mut leave = None;
        let mut bestr = f64::INFINITY;
        for i in 1..=m2 {
            let aij = t[i][enter];
            if aij > eps {
                let ratio = t[i][cols - 1] / aij;
                if ratio < bestr {
                    bestr = ratio;
                    leave = Some(i);
                }
            }
        }
        let leave = leave?; // unbounded: cannot happen (all vars bounded)
        let p = t[leave][enter];
        for col in 0..cols {
            t[leave][col] /= p;
        }
        for i in 0..=m2 {
            if i != leave {
                let f = t[i][enter];
                if f != 0.0 {
                    for col in 0..cols {
                        t[i][col] -= f * t[leave][col];
                    }
                }
            }
        }
        basis[leave - 1] = enter;
    }
    let mut x = vec![0.0f64; n];
    for i in 0..m2 {
        let col = basis[i];
        if col < n {
            x[col] = t[i + 1][cols - 1];
        }
    }
    for j in 0..n {
        x[j] += lo[j];
    }
    Some(x)
}

/// Full LP: maximize v over (l1..l5, c1..c5, v), F_B(g) >= v on cfgs,
/// kappa_i >= 0, |l_k| <= L_BOUND, |c_k| <= c_bound.
fn solve_full_lp(alpha: f64, cfgs: &[[f64; 6]], c_bound: f64) -> Option<([f64; 5], [f64; 5], f64)> {
    let n = 11;
    let mut a: Vec<Vec<f64>> = Vec::new();
    let mut b: Vec<f64> = Vec::new();
    for g in cfgs {
        let (l_, c_) = lin_coeffs(g, alpha);
        let f0v = f0(g, alpha);
        let mut row = vec![0.0f64; n];
        for k in 0..5 {
            row[k] = -l_[k];
            row[5 + k] = -c_[k];
        }
        row[10] = 1.0; // +v <= f0
        a.push(row);
        b.push(f0v);
    }
    // kappa_i = P0 + l_{i-1} - l_i >= 0  <=>  -l_{i-1} + l_i <= P0
    for i in 1..=6 {
        let mut row = vec![0.0f64; n];
        if i >= 2 {
            row[i - 2] = -1.0;
        }
        if i <= 5 {
            row[i - 1] = 1.0;
        }
        a.push(row);
        b.push(P0);
    }
    let mut lo = vec![0.0f64; n];
    let mut hi = vec![0.0f64; n];
    for k in 0..5 {
        lo[k] = -L_BOUND;
        hi[k] = L_BOUND;
        lo[5 + k] = -c_bound;
        hi[5 + k] = c_bound;
    }
    lo[10] = -1.0;
    hi[10] = 20.0; // safe: v* in [0, ~0.01] for these families
    let mut c = vec![0.0f64; n];
    c[10] = -1.0; // maximize v
    let x = bounded_simplex(&a, &b, &lo, &hi, &c)?;
    let l: [f64; 5] = std::array::from_fn(|k| x[k]);
    let cv: [f64; 5] = std::array::from_fn(|k| x[5 + k]);
    Some((l, cv, x[10]))
}

/// Symmetric-subspace LP: maximize v over (a1,a2,b1,b2,v),
/// l=(a1,a2,0,-a2,-a1), c=(b1,b2,0,-b2,-b1).
fn solve_sym_lp(alpha: f64, cfgs: &[[f64; 6]], c_bound: f64) -> Option<([f64; 5], [f64; 5], f64)> {
    let mut a: Vec<Vec<f64>> = Vec::new();
    let mut b: Vec<f64> = Vec::new();
    for g in cfgs {
        let (l_, c_) = lin_coeffs(g, alpha);
        let f0v = f0(g, alpha);
        // F_B = f0 + (L0-L4) a1 + (L1-L3) a2 + (C0-C4) b1 + (C1-C3) b2
        a.push(vec![
            -(l_[0] - l_[4]),
            -(l_[1] - l_[3]),
            -(c_[0] - c_[4]),
            -(c_[1] - c_[3]),
            1.0,
        ]);
        b.push(f0v);
    }
    // huge-gap in the symmetric subspace: a1 <= P0, a2-a1 <= P0, -a2 <= P0
    a.push(vec![1.0, 0.0, 0.0, 0.0, 0.0]);
    b.push(P0);
    a.push(vec![-1.0, 1.0, 0.0, 0.0, 0.0]);
    b.push(P0);
    a.push(vec![0.0, -1.0, 0.0, 0.0, 0.0]);
    b.push(P0);
    let lo = vec![-L_BOUND, -L_BOUND, -c_bound, -c_bound, -1.0];
    let hi = vec![L_BOUND, L_BOUND, c_bound, c_bound, 20.0];
    let c = vec![0.0, 0.0, 0.0, 0.0, -1.0];
    let x = bounded_simplex(&a, &b, &lo, &hi, &c)?;
    let (a1v, a2v, b1v, b2v, v) = (x[0], x[1], x[2], x[3], x[4]);
    let l = [a1v, a2v, 0.0, -a2v, -a1v];
    let cv = [b1v, b2v, 0.0, -b2v, -b1v];
    Some((l, cv, v))
}

// ---------------------------------------------------------------------------
// Global float floor: DE + Nelder-Mead polish + huge-gap scan
// ---------------------------------------------------------------------------

/// SplitMix64 — deterministic stand-in for numpy's PRNG (stochastic heuristic;
/// exact RNG replication is not required at the ~1e-3 acceptance tolerance).
struct Rng(u64);
impl Rng {
    fn next(&mut self) -> u64 {
        self.0 = self.0.wrapping_add(0x9E3779B97F4A7C15);
        let mut z = self.0;
        z = (z ^ (z >> 30)).wrapping_mul(0xBF58476D1CE4E5B9);
        z = (z ^ (z >> 27)).wrapping_mul(0x94D049BB133111EB);
        z ^ (z >> 31)
    }
    fn unit(&mut self) -> f64 {
        (self.next() >> 11) as f64 * (1.0 / 9007199254740992.0)
    }
    fn normal(&mut self) -> f64 {
        // Box-Muller
        let u1 = (self.unit() + 1e-300).max(1e-300);
        let u2 = self.unit();
        (-2.0 * u1.ln()).sqrt() * (2.0 * std::f64::consts::PI * u2).cos()
    }
}

fn nelder_mead(
    x0: &[f64; 6],
    alpha: f64,
    l: &[f64; 5],
    c: &[f64; 5],
    maxiter: usize,
    xatol: f64,
    fatol: f64,
    lo: f64,
    hi: f64,
) -> ([f64; 6], f64) {
    const N: usize = 6;
    let clamp = |p: &mut [f64; 6]| {
        for k in 0..6 {
            p[k] = p[k].clamp(lo, hi);
        }
    };
    let mut simplex = vec![[0.0f64; N]; N + 1];
    let mut fv = vec![0.0f64; N + 1];
    simplex[0] = *x0;
    clamp(&mut simplex[0]);
    fv[0] = f_b(&simplex[0], alpha, l, c);
    for i in 0..N {
        let mut p = *x0;
        p[i] *= 1.05;
        if p[i] == 0.0 {
            p[i] = 1e-6;
        }
        clamp(&mut p);
        simplex[i + 1] = p;
        fv[i + 1] = f_b(&simplex[i + 1], alpha, l, c);
    }
    for _ in 0..maxiter {
        // order
        for i in 1..simplex.len() {
            let mut j = i;
            while j > 0 && fv[j - 1] > fv[j] {
                fv.swap(j - 1, j);
                simplex.swap(j - 1, j);
                j -= 1;
            }
        }
        let mut centroid = [0.0f64; N];
        for i in 0..N {
            for k in 0..N {
                centroid[k] += simplex[i][k];
            }
        }
        for k in 0..N {
            centroid[k] /= N as f64;
        }
        let xr = reflect(&centroid, &simplex[N], 1.0);
        let xr = {
            let mut t = xr;
            clamp(&mut t);
            t
        };
        let fr = f_b(&xr, alpha, l, c);
        if fr < fv[0] {
            let xe = reflect(&centroid, &simplex[N], 2.0);
            let xe = {
                let mut t = xe;
                clamp(&mut t);
                t
            };
            let fe = f_b(&xe, alpha, l, c);
            if fe < fr {
                simplex[N] = xe;
                fv[N] = fe;
            } else {
                simplex[N] = xr;
                fv[N] = fr;
            }
        } else if fr < fv[N - 1] {
            simplex[N] = xr;
            fv[N] = fr;
        } else {
            // contraction / shrink
            if fr < fv[N] {
                let xc = reflect(&centroid, &simplex[N], 0.5);
                let xc = {
                    let mut t = xc;
                    clamp(&mut t);
                    t
                };
                let fc = f_b(&xc, alpha, l, c);
                if fc <= fr {
                    simplex[N] = xc;
                    fv[N] = fc;
                } else {
                    shrink(&mut simplex, &mut fv, alpha, l, c, lo, hi);
                }
            } else {
                let xc = reflect(&centroid, &simplex[N], 0.5);
                let xc = {
                    let mut t = xc;
                    clamp(&mut t);
                    t
                };
                let fc = f_b(&xc, alpha, l, c);
                if fc < fv[N] {
                    simplex[N] = xc;
                    fv[N] = fc;
                } else {
                    shrink(&mut simplex, &mut fv, alpha, l, c, lo, hi);
                }
            }
        }
        if fv[N] - fv[0] <= fatol
            && (0..N).all(|k| (simplex[N][k] - simplex[0][k]).abs() <= xatol)
        {
            break;
        }
    }
    let mut best = simplex[0];
    let mut bestf = fv[0];
    for i in 1..simplex.len() {
        if fv[i] < bestf {
            bestf = fv[i];
            best = simplex[i];
        }
    }
    (best, bestf)
}

fn reflect(c: &[f64; 6], worst: &[f64; 6], rho: f64) -> [f64; 6] {
    let mut out = [0.0f64; 6];
    for k in 0..6 {
        out[k] = c[k] + rho * (c[k] - worst[k]);
    }
    out
}

fn shrink(
    simplex: &mut Vec<[f64; 6]>,
    fv: &mut Vec<f64>,
    alpha: f64,
    l: &[f64; 5],
    c: &[f64; 5],
    lo: f64,
    hi: f64,
) {
    for i in 1..simplex.len() {
        for k in 0..6 {
            simplex[i][k] = (0.5 * (simplex[i][k] + simplex[0][k])).clamp(lo, hi);
        }
        fv[i] = f_b(&simplex[i], alpha, l, c);
    }
}

/// Differential evolution (best/1/bin), popsize=20*6=120, maxiter=400, then
/// Nelder-Mead polish on the best. Bounds [lo, hi]^6.
fn de_global(alpha: f64, l: &[f64; 5], c: &[f64; 5], lo: f64, hi: f64) -> (f64, [f64; 6]) {
    let dim = 6;
    let npop = 20 * dim;
    let mut rng = Rng(3);
    let mut pop = vec![[0.0f64; 6]; npop];
    let mut fit = vec![0.0f64; npop];
    for i in 0..npop {
        for k in 0..dim {
            pop[i][k] = lo + (hi - lo) * rng.unit();
        }
        fit[i] = f_b(&pop[i], alpha, l, c);
    }
    let mut best = pop[0];
    let mut bestf = fit[0];
    for i in 0..npop {
        if fit[i] < bestf {
            bestf = fit[i];
            best = pop[i];
        }
    }
    let mut stalled = 0;
    for _gen in 0..400 {
        let mut newbest = bestf;
        for i in 0..npop {
            // pick 3 distinct indices != i
            let mut r = [0usize; 3];
            for slot in 0..3 {
                loop {
                    let x = (rng.next() as usize) % npop;
                    if x != i && !r[..slot].contains(&x) {
                        r[slot] = x;
                        break;
                    }
                }
            }
            let f = 0.5 + 0.5 * rng.unit(); // dither in (0.5, 1)
            let cr = 0.7;
            let jrand = (rng.next() as usize) % dim;
            let mut trial = [0.0f64; 6];
            for k in 0..dim {
                trial[k] = if rng.unit() < cr || k == jrand {
                    let m = best[k] + f * (pop[r[0]][k] - pop[r[1]][k]);
                    m.clamp(lo, hi) // scipy DE clamps mutants to bounds
                } else {
                    pop[i][k]
                };
            }
            let ft = f_b(&trial, alpha, l, c);
            if ft < fit[i] {
                fit[i] = ft;
                pop[i] = trial;
                if ft < newbest {
                    newbest = ft;
                    best = trial;
                }
            }
        }
        if (bestf - newbest).abs() < 1e-13 {
            stalled += 1;
        } else {
            stalled = 0;
        }
        bestf = newbest;
        if stalled > 40 {
            break;
        }
    }
    // polish best with Nelder-Mead (bounded to the verifier's active domain)
    let (_, pf) = nelder_mead(&best, alpha, l, c, 1500, 1e-9, 1e-12, lo, hi);
    (pf.min(bestf), best)
}

/// Huge-gap scan: g_pos = H in [5,21], others around the crystal base, with
/// Nelder-Mead refinement; plus all-1.1 background with one big gap.
fn huge_gap_floor(alpha: f64, l: &[f64; 5], c: &[f64; 5]) -> f64 {
    let mut rng = Rng(9);
    let mut best = f64::INFINITY;
    let base = [1.05, 1.98, 1.05, 1.98, 1.05, 1.98];
    for pos in 0..6 {
        for h in 0..9 {
            let hval = 5.0 + (21.0 - 5.0) * h as f64 / 8.0; // linspace(5,21,9)
            let mut g = base;
            g[pos] = hval;
            // 6 Nelder-Mead restarts from g + N(0,0.3), clamped >= 0.4
            for _ in 0..6 {
                let mut x0 = g;
                for k in 0..6 {
                    x0[k] = (g[k] + 0.3 * rng.normal()).max(0.4);
                }
                let (_, f) = nelder_mead(&x0, alpha, l, c, 1500, 1e-9, 1e-12, 0.4, 21.0);
                if f < best {
                    best = f;
                }
            }
            // all-1.1 background, one big gap
            let mut g2 = [1.1f64; 6];
            g2[pos] = hval;
            let f2 = f_b(&g2, alpha, l, c);
            if f2 < best {
                best = f2;
            }
        }
    }
    best
}

fn floor_over_family(alpha: f64, l: &[f64; 5], c: &[f64; 5], cfgs: &[[f64; 6]]) -> f64 {
    cfgs.iter().map(|g| f_b(g, alpha, l, c)).fold(f64::INFINITY, f64::min)
}

// ---------------------------------------------------------------------------

fn main() {
    let args: Vec<String> = std::env::args().collect();
    let mut alpha = 1.464f64;
    let mut mode = "sym".to_string();
    let mut c_bound = 0.06f64;
    let mut i = 1;
    while i < args.len() {
        match args[i].as_str() {
            "--alpha" => {
                i += 1;
                alpha = args[i].parse().expect("alpha");
            }
            "--mode" => {
                i += 1;
                mode = args[i].clone();
            }
            "--c-bound" => {
                i += 1;
                c_bound = args[i].parse().expect("c_bound");
            }
            other => panic!("unknown arg {other}"),
        }
        i += 1;
    }
    let data_dir = concat!(env!("CARGO_MANIFEST_DIR"), "/data");
    type LpFn = fn(f64, &[[f64; 6]], f64) -> Option<([f64; 5], [f64; 5], f64)>;
    let (cfgs_path, solve): (String, LpFn) = if mode == "sym" {
        (format!("{data_dir}/family_578.txt"), solve_sym_lp)
    } else {
        (format!("{data_dir}/family_1089.txt"), solve_full_lp)
    };
    let cfgs = read_cfgs(&cfgs_path);
    println!("mode={mode} alpha={alpha} c_bound={c_bound} family={} cfgs", cfgs.len());

    let t0 = Instant::now();
    let (l, c, v) = solve(alpha, &cfgs, c_bound).expect("LP infeasible/unbounded");
    let t_lp = t0.elapsed();
    let kap = kappa(&l);
    let p: Vec<f64> = (0..5)
        .map(|k| P0 + (if k == 0 { 0.0 } else { l[k - 1] }) - l[k])
        .collect();
    let p6 = P0 + l[4];
    let fl_fam = floor_over_family(alpha, &l, &c, &cfgs);
    println!("LP v* = {v:.9}   (LP wall {:.2?})", t_lp);
    println!("  l = {l:?}");
    println!("  c = {c:?}");
    println!("  kappa = {kap:?}");
    println!("  p = {p:?} p6={p6:.7} sum_p={:.9}", p.iter().sum::<f64>() + p6);
    println!("  floor over LP family = {fl_fam:.9}");

    let t1 = Instant::now();
    let (de_f, _) = de_global(alpha, &l, &c, 0.4, 3.5);
    let t_de = t1.elapsed();
    let t2 = Instant::now();
    let hg = huge_gap_floor(alpha, &l, &c);
    let t_hg = t2.elapsed();
    let gf = de_f.min(hg);
    println!("DE floor (bounded box) = {de_f:.9}  ({:.2?})", t_de);
    println!("huge-gap floor = {hg:.9}  ({:.2?})", t_hg);
    println!("GLOBAL float floor = {gf:.9}   (total DE+hugegap {:.2?})", t0.elapsed());
}
