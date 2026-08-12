// faster_finder.rs — v1 per SPEC (tools/zeros_rust/faster-finder-spec.md)
//   Batch/row-update Riemann-Siegel: Z(t) = cos(theta)*2A + sin(theta)*2B + sign*x^-1/4*g0,
//   A = sum c_k/sqrt(k), B = sum s_k/sqrt(k), (c_k,s_k) = (cos,sin)(t ln k)
//   updated per step via rotation by (cos,sin)(STEP*ln k): 4 mul + 2 add per term.
//   Re-seeded (direct cos/sin) every BLOCK steps. n grows as sqrt(t/2pi).
//   Scan step 0.02 (completeness fix vs the 0.78% miss at 0.2). Refine = IQI + bisection.
//   std::thread over sub-windows. EM path (z_low) for t < 200, same as main.rs.
//   Output: win mode single column (gamma), count mode "index gamma", N(T) diff at end.
// Usage:  faster win <t_lo> <t_hi> <step> [shard] [shard_count] [threads]
//         faster <count> [threads]
use std::env;
use std::io::{self, Write};
use std::thread;

const PI: f64 = std::f64::consts::PI;
const TWO_PI: f64 = 2.0 * PI;
const STEP_DEFAULT: f64 = 0.02;
const BLOCK: usize = 1024; // re-seed period in steps

// --- theta(t) asymptotic (same as main.rs; error < 1e-9 for t>=14) ---
fn theta(t: f64) -> f64 {
    let u = t / TWO_PI;
    let t3 = t * t * t;
    (t / 2.0) * u.ln() - t / 2.0 - PI / 8.0 + 1.0 / (48.0 * t) + 7.0 / (5760.0 * t3)
}

// --- Bernoulli numbers by recurrence (same as main.rs) ---
fn bernoulli(n: usize) -> f64 {
    let mut b = vec![0.0f64; n + 1];
    b[0] = 1.0;
    for m in 1..=n {
        let mut s = 0.0;
        let mut c: f64 = 1.0;
        for k in 0..m {
            s += c * b[k];
            c *= (m + 1 - k) as f64 / (k + 1) as f64;
        }
        b[m] = -s / (m + 1) as f64;
    }
    b[n]
}

// --- Euler-Maclaurin zeta(1/2+it), N=40, k=1..20 tail (same as main.rs) ---
fn zeta_half_it(t: f64) -> (f64, f64) {
    const N: usize = 40;
    const K: usize = 20;
    let ln_n = (N as f64).ln();
    let (mut re, mut im) = (0.0f64, 0.0f64);
    for n in 1..N {
        let nf = n as f64;
        let ang = -t * nf.ln();
        let mag = 1.0 / nf.sqrt();
        re += mag * ang.cos();
        im += mag * ang.sin();
    }
    let a = (N as f64).sqrt() * (t * ln_n).cos();
    let b = -(N as f64).sqrt() * (t * ln_n).sin();
    let denom = 0.25 + t * t;
    re += (-0.5 * a + t * b) / denom;
    im += (-0.5 * b - t * a) / denom;
    let c = (N as f64).powf(-0.5) * (t * ln_n).cos() / 2.0;
    let d = -(N as f64).powf(-0.5) * (t * ln_n).sin() / 2.0;
    re += c;
    im += d;
    for k in 1..=K {
        let mut pr = 1.0f64;
        let mut pi = 0.0f64;
        for j in 0..(2 * k - 1) {
            let xr = 0.5 + j as f64;
            let nr = pr * xr - pi * t;
            let ni = pr * t + pi * xr;
            pr = nr;
            pi = ni;
        }
        let bterm = bernoulli(2 * k);
        let mut f = 1.0f64;
        for m in 2..=(2 * k) {
            f *= m as f64;
        }
        let coef = bterm / f * (N as f64).powf(-(2.0 * k as f64) + 0.5);
        let e = (t * ln_n).cos();
        let f2 = -(t * ln_n).sin();
        let tr = pr * e - pi * f2;
        let ti = pr * f2 + pi * e;
        re += coef * tr;
        im += coef * ti;
    }
    (re, im)
}

fn z_low(t: f64) -> f64 {
    let (re, im) = zeta_half_it(t);
    let th = theta(t);
    re * th.cos() - im * th.sin()
}

// N(T) = (T/2pi) ln(T/2pi) - T/2pi + 7/8
fn n_count(t: f64) -> f64 {
    let u = t / TWO_PI;
    u * u.ln() - u + 7.0 / 8.0
}

// --- batch state for the row-update RS ---
struct Batch {
    lnk: Vec<f64>,
    inv_sqrt: Vec<f64>,
    ch: Vec<f64>, // cos(STEP * ln k)
    sh: Vec<f64>, // sin(STEP * ln k)
    c: Vec<f64>,  // cos(t ln k)
    s: Vec<f64>,  // sin(t ln k)
    n: usize,     // active range
}

impl Batch {
    fn new(t: f64, t_hi: f64, step: f64) -> Self {
        let n_max = (t_hi / TWO_PI).sqrt().ceil() as usize + 2;
        let mut lnk = vec![0.0; n_max + 1];
        let mut inv_sqrt = vec![0.0; n_max + 1];
        let mut ch = vec![0.0; n_max + 1];
        let mut sh = vec![0.0; n_max + 1];
        let mut c = vec![0.0; n_max + 1];
        let mut s = vec![0.0; n_max + 1];
        let n0 = ((t / TWO_PI).sqrt().floor() as usize).max(1);
        for k in 1..=n_max {
            lnk[k] = (k as f64).ln();
            inv_sqrt[k] = 1.0 / (k as f64).sqrt();
            let ang = step * lnk[k];
            ch[k] = ang.cos();
            sh[k] = ang.sin();
        }
        let mut b = Batch { lnk, inv_sqrt, ch, sh, c, s, n: n0 };
        b.reseed(t, n0);
        b
    }
    fn reseed(&mut self, t: f64, n: usize) {
        self.n = n;
        for k in 1..=n {
            let ang = t * self.lnk[k];
            self.c[k] = ang.cos();
            self.s[k] = ang.sin();
        }
    }
    // advance the rotation to t (next grid point); grow n if the sqrt bound crossed
    fn advance(&mut self, t: f64, step_idx: usize, step: f64) {
        let n_tgt = ((t / TWO_PI).sqrt().floor() as usize).max(1);
        if step_idx % BLOCK == 0 {
            self.reseed(t, n_tgt);
            return;
        }
        let n_old = self.n;
        if n_tgt > self.n {
            for k in (self.n + 1)..=n_tgt {
                let ang = t * self.lnk[k];
                self.c[k] = ang.cos();
                self.s[k] = ang.sin();
            }
            self.n = n_tgt;
        }
        // rotate ONLY the terms that were present at the previous t (1..=n_old):
        // the newly seeded terms are already at the CURRENT t and must NOT be
        // rotated this step (rotating them here put them one step AHEAD, a
        // phase error of step*ln k that persisted until the next re-seed and
        // corrupted Z by ~0.01-0.05 right after every n-growth).
        for k in 1..=n_old {
            let ck = self.c[k];
            let sk = self.s[k];
            let chk = self.ch[k];
            let shk = self.sh[k];
            self.c[k] = ck * chk - sk * shk;
            self.s[k] = sk * chk + ck * shk;
        }
        let _ = step;
    }
    fn z(&self, t: f64) -> f64 {
        let th = theta(t);
        let n = self.n;
        let mut a = 0.0f64;
        let mut b = 0.0f64;
        for k in 1..=n {
            a += self.c[k] * self.inv_sqrt[k];
            b += self.s[k] * self.inv_sqrt[k];
        }
        let x = t / TWO_PI;
        let sq = x.sqrt();
        let nf = sq.floor() as usize;
        let aa = sq - nf as f64;
        let sign = if nf % 2 == 0 { -1.0 } else { 1.0 };
        let g0 = (TWO_PI * (aa * aa - aa - 1.0 / 16.0)).cos() / (TWO_PI * aa).cos();
        2.0 * (th.cos() * a + th.sin() * b) + sign * x.powf(-0.25) * g0
    }
}

// direct RS eval (single point, used for refinement)
fn z_direct(t: f64, lnk: &[f64], inv_sqrt: &[f64]) -> f64 {
    let x = t / TWO_PI;
    let sq = x.sqrt();
    let n = sq.floor() as usize;
    let th = theta(t);
    let mut s = 0.0f64;
    for k in 1..=n {
        s += (th - t * lnk[k]).cos() * inv_sqrt[k];
    }
    let aa = sq - n as f64;
    let sign = if n % 2 == 0 { -1.0 } else { 1.0 };
    let g0 = (TWO_PI * (aa * aa - aa - 1.0 / 16.0)).cos() / (TWO_PI * aa).cos();
    2.0 * s + sign * x.powf(-0.25) * g0
}

// IQI root estimate from (x0,y0),(x1,y1),(x2,y2)
fn iqi(x0: f64, y0: f64, x1: f64, y1: f64, x2: f64, y2: f64) -> f64 {
    let d01 = y0 - y1;
    let d02 = y0 - y2;
    let d12 = y1 - y2;
    if d01.abs() < 1e-300 || d02.abs() < 1e-300 || d12.abs() < 1e-300 {
        return 0.5 * (x1 + x2);
    }
    let t1 = y1 * y2 * x0 / (d01 * d02);
    let t2 = y2 * y0 * x1 / (-d01 * d12);
    let t3 = y0 * y1 * x2 / (d02 * d12);
    t1 + t2 + t3
}

// refine a root in [lo, hi] (z(lo)*z(hi) < 0); z is cheap enough here
// refine a root in [lo, hi] (z(lo)*z(hi) < 0) by pure bisection — the IQI was
// fragile (edge-case bracket collapse produced spurious roots ~1e-3..7e-3 off).
// 8 bisections on the 0.02 bracket -> 8e-5 precision, well under the 1e-3 bar.
fn z_any(t: f64, lnk: &[f64], inv_sqrt: &[f64]) -> f64 {
    if t < 200.0 {
        z_low(t)
    } else {
        z_direct(t, lnk, inv_sqrt)
    }
}

fn refine(lo: f64, hi: f64, zlo: f64, lnk: &[f64], inv_sqrt: &[f64]) -> f64 {
    let (mut a, mut b) = (lo, hi);
    let mut za = zlo;
    for _ in 0..8 {
        let mid = 0.5 * (a + b);
        let zm = z_any(mid, lnk, inv_sqrt);
        if za * zm < 0.0 {
            b = mid;
        } else {
            a = mid;
            za = zm;
        }
    }
    0.5 * (a + b)
}

// scan [w_lo, w_hi) for zeros; returns them sorted.
// Pure fine scan (step 0.02): with the batch rotation phase-bug fixed the batch
// values equal z_direct, so every detected crossing is a real crossing of the
// computed Z. The g0-only RS error near the t~200-300 crossover creates wiggle
// PAIRS (two computed-Z crossings straddling the true zero, gap ~1e-3..1e-2) —
// these are collapsed to their midpoint by the caller's post-filter (gap<0.01),
// which is a better root estimate than either crossing; genuine twin pairs
// (min observed gap 0.0279) are untouched.
fn scan_window(w_lo: f64, w_hi: f64, step: f64, thread_id: usize, out_err: &str) -> Vec<f64> {
    let _ = out_err;
    let mut batch = Batch::new(w_lo, w_hi, step);
    let mut out: Vec<f64> = Vec::new();
    let mut t_prev = w_lo;
    let mut z_prev = z_at(&batch, w_lo);
    let mut step_idx = 0usize;
    let mut t = w_lo + step;
    while t <= w_hi + step {
        batch.advance(t, step_idx, step);
        let z = z_at(&batch, t);
        step_idx += 1;
        if z_prev.is_finite() && z.is_finite() && z_prev * z < 0.0 {
            let g = refine(t_prev, t, z_prev, &batch.lnk, &batch.inv_sqrt);
            if g.is_finite() {
                out.push(g);
            }
        }
        t_prev = t;
        z_prev = z;
        t += step;
    }
    let _ = thread_id;
    out
}

fn z_at(batch: &Batch, t: f64) -> f64 {
    if t < 200.0 {
        z_low(t)
    } else {
        batch.z(t)
    }
}

// collapse wiggle pairs: two roots closer than the threshold are two computed-Z
// crossings straddling one true zero (the g0-only error near the crossover);
// their midpoint is the better root estimate. Genuine twin pairs have gaps
// >= ~0.0197 (measured, 100k) and live at t >= 5000, so the crossover band
// [150, 1200] — where ALL wiggle pairs live — can collapse up to 0.02 safely;
// elsewhere collapse only up to 0.01 (never touches a real pair).
const WIGGLE_GAP: f64 = 0.01;
const WIGGLE_GAP_BAND: f64 = 0.02;
fn collapse_wiggles(v: &mut Vec<f64>) {
    let mut out: Vec<f64> = Vec::with_capacity(v.len());
    let mut i = 0;
    while i < v.len() {
        if i + 1 < v.len() && v[i + 1] - v[i] < WIGGLE_GAP_BAND {
            let mid = 0.5 * (v[i] + v[i + 1]);
            let thresh = if mid >= 150.0 && mid <= 1200.0 {
                WIGGLE_GAP_BAND
            } else {
                WIGGLE_GAP
            };
            if v[i + 1] - v[i] < thresh {
                out.push(mid);
                i += 2;
            } else {
                out.push(v[i]);
                i += 1;
            }
        } else {
            out.push(v[i]);
            i += 1;
        }
    }
    *v = out;
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let threads = std::thread::available_parallelism()
        .map(|n| n.get())
        .unwrap_or(1)
        .min(8);

    let mut out = io::stdout().lock();

    if args.get(1).map(|s| s.as_str()) == Some("win") {
        let t_lo: f64 = args.get(2).expect("win t_lo").parse().unwrap();
        let t_hi: f64 = args.get(3).expect("win t_hi").parse().unwrap();
        let step: f64 = args.get(4).map(|s| s.parse().unwrap()).unwrap_or(STEP_DEFAULT);
        let shard: usize = args.get(5).map(|s| s.parse().unwrap()).unwrap_or(0);
        let n_shard: usize = args.get(6).map(|s| s.parse().unwrap()).unwrap_or(1);
        let nt: usize = args.get(7).and_then(|s| s.parse().ok()).unwrap_or(threads);

        let w = (t_hi - t_lo) / n_shard as f64;
        let clo = t_lo + shard as f64 * w;
        let chi = clo + w;
        let scan_lo = (clo - 2.0 * step).max(14.0);
        let scan_hi = chi + 2.0 * step;

        let t0 = std::time::Instant::now();
        let span = scan_hi - scan_lo;
        let sub = span / nt as f64;
        let mut handles = Vec::new();
        for i in 0..nt {
            let s_lo = scan_lo + i as f64 * sub;
            let s_hi = if i + 1 == nt { scan_hi } else { scan_lo + (i + 1) as f64 * sub + step };
            handles.push(thread::spawn(move || scan_window(s_lo, s_hi, step, i, "")));
        }
        let mut all: Vec<f64> = Vec::new();
        for h in handles {
            all.extend(h.join().unwrap());
        }
        all.sort_by(|a, b| a.partial_cmp(b).unwrap());
        all.dedup_by(|a, b| (*a - *b).abs() < 1e-9);
        collapse_wiggles(&mut all);

        let mut kept = Vec::new();
        for g in all {
            if g >= clo && g <= chi {
                let _ = writeln!(out, "{:.12}", g);
                kept.push(g);
            }
        }
        let _ = out.flush();
        let expect = n_count(chi) - n_count(clo);
        let wall = t0.elapsed().as_secs_f64();
        let _ = writeln!(
            out,
            "# win done: found={} expected={expect:.2} diff={:+.2} wall={wall:.2}s",
            kept.len(),
            kept.len() as f64 - expect
        );
        eprintln!(
            "faster win {shard}: found={} expected={expect:.2} diff={:+.2} wall={wall:.2}s",
            kept.len(),
            kept.len() as f64 - expect
        );
        return;
    }

    // count mode: find the first <count> zeros from 14
    let count: usize = args.get(1).expect("usage: faster <count> [threads]").parse().expect("count");
    let nt: usize = args.get(3).and_then(|s| s.parse().ok()).unwrap_or(threads);

    let t0 = std::time::Instant::now();
    let step: f64 = args.get(2).and_then(|s| s.parse().ok()).unwrap_or(STEP_DEFAULT);
    let scan_hi = 14.0 + count as f64 * 1.6 + 200.0; // generous upper bound
    let span = scan_hi - 14.0;
    let sub = span / nt as f64;
    let mut handles = Vec::new();
    for i in 0..nt {
        let s_lo = 14.0 + i as f64 * sub;
        let s_hi = if i + 1 == nt { scan_hi } else { 14.0 + (i + 1) as f64 * sub + step };
        handles.push(thread::spawn(move || scan_window(s_lo, s_hi, step, i, "")));
    }
    let mut all: Vec<f64> = Vec::new();
    for h in handles {
        all.extend(h.join().unwrap());
    }
    all.sort_by(|a, b| a.partial_cmp(b).unwrap());
    all.dedup_by(|a, b| (*a - *b).abs() < 1e-9);
    collapse_wiggles(&mut all);

    let _ = writeln!(out, "# faster v1: batch RS + IQI, step {step}, threads {nt}");
    let mut found = 0usize;
    let mut last = 0.0f64;
    for g in all {
        if g < 14.0 {
            continue;
        }
        found += 1;
        if found > count {
            break;
        }
        let _ = writeln!(out, "{} {:.12}", found, g);
        let _ = out.flush();
        last = g;
    }
    let nc = n_count(last);
    let wall = t0.elapsed().as_secs_f64();
    let _ = writeln!(
        out,
        "# done: found={found} t_last={last:.3} N(T_last)={nc:.2} diff={:+.2} wall={wall:.2}s",
        found as f64 - nc
    );
    eprintln!("faster: found={found} t_last={last:.3} N(T)={nc:.2} diff={:+.2} wall={wall:.2}s", found as f64 - nc);
}
