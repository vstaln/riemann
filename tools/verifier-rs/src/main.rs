//! Rust interval verifier for the coboundary floor inequality.
//! Port of tools/verify_coboundary_floor.py. Uses a rigorous interval type
//! (rug Float lo/hi pairs with directed rounding) instead of Arb balls.
//!
//! KNOWN GAP (2026-08-18): this port does NOT implement the convex-tangent
//! prune (Python verify_floor defaults use_tangent=True; tangent_lower uses
//! an exact arb LDL). Python's certified configs depend on it (ainta: 93,735
//! tangent prunes of 707,901 nodes; tawan: 18,182 of 209,236). Without it
//! this port certifies LESS than Python on every certified config — it is
//! NOT-FOR-CERTIFICATION until tangent_lower (second-derivative table +
//! LDL + tangent-plane bound) is ported. See research/notes/verifier-rs-fix-2026-08-18.md.
//!
//! ENCLOSURE CLAIM (corrected): sinc_iv (exact extrema via roots of x=tan x)
//! agrees with Arb's ball enclosure cell-by-cell; it is NOT meaningfully
//! tighter. The earlier header claim that it is "TIGHTER than python-flint's
//! arb ball enclosure" was unsubstantiated and is retracted.

use rug::float::Round;
use rug::ops::CompleteRound;
use rug::Float;
use std::collections::HashMap;

const PREC: u32 = 300;

// ---------------------------------------------------------------------------
// Interval type: (lo, hi) with lo <= hi, directed rounding everywhere
// ---------------------------------------------------------------------------

#[derive(Clone, Debug)]
struct Iv {
    lo: Float,
    hi: Float,
}

impl Iv {
    fn new(lo: Float, hi: Float) -> Iv {
        Iv { lo, hi }
    }
    fn point(x: f64) -> Iv {
        let lo = Float::with_val_round(PREC, x, Round::Down).0;
        let hi = Float::with_val_round(PREC, x, Round::Up).0;
        Iv { lo, hi }
    }
    fn add(&self, o: &Iv) -> Iv {
        let lo = (&self.lo + &o.lo).complete_round(PREC, Round::Down).0;
        let hi = (&self.hi + &o.hi).complete_round(PREC, Round::Up).0;
        Iv { lo, hi }
    }
    fn sub(&self, o: &Iv) -> Iv {
        let lo = (&self.lo - &o.hi).complete_round(PREC, Round::Down).0;
        let hi = (&self.hi - &o.lo).complete_round(PREC, Round::Up).0;
        Iv { lo, hi }
    }
    fn mul(&self, o: &Iv) -> Iv {
        let cands = [
            (&self.lo * &o.lo).complete_round(PREC, Round::Down).0,
            (&self.lo * &o.hi).complete_round(PREC, Round::Down).0,
            (&self.hi * &o.lo).complete_round(PREC, Round::Down).0,
            (&self.hi * &o.hi).complete_round(PREC, Round::Down).0,
        ];
        let mut lo = cands[0].clone();
        let mut hi = cands[0].clone();
        for c in &cands {
            if c < &lo { lo = c.clone(); }
            if c > &hi { hi = c.clone(); }
        }
        let cands = [
            (&self.lo * &o.lo).complete_round(PREC, Round::Up).0,
            (&self.lo * &o.hi).complete_round(PREC, Round::Up).0,
            (&self.hi * &o.lo).complete_round(PREC, Round::Up).0,
            (&self.hi * &o.hi).complete_round(PREC, Round::Up).0,
        ];
        for c in &cands {
            if c > &hi { hi = c.clone(); }
        }
        Iv { lo, hi }
    }
    fn div(&self, o: &Iv) -> Iv {
        // assumes o does not contain 0
        let cands = [
            (&self.lo / &o.lo).complete_round(PREC, Round::Down).0,
            (&self.lo / &o.hi).complete_round(PREC, Round::Down).0,
            (&self.hi / &o.lo).complete_round(PREC, Round::Down).0,
            (&self.hi / &o.hi).complete_round(PREC, Round::Down).0,
        ];
        let mut lo = cands[0].clone();
        let mut hi = cands[0].clone();
        for c in &cands {
            if c < &lo { lo = c.clone(); }
            if c > &hi { hi = c.clone(); }
        }
        let cands = [
            (&self.lo / &o.lo).complete_round(PREC, Round::Up).0,
            (&self.lo / &o.hi).complete_round(PREC, Round::Up).0,
            (&self.hi / &o.lo).complete_round(PREC, Round::Up).0,
            (&self.hi / &o.hi).complete_round(PREC, Round::Up).0,
        ];
        for c in &cands {
            if c > &hi { hi = c.clone(); }
        }
        Iv { lo, hi }
    }
    fn neg(&self) -> Iv {
        Iv { lo: Float::with_val_round(PREC, -&self.hi, Round::Down).0,
             hi: Float::with_val_round(PREC, -&self.lo, Round::Up).0 }
    }
    fn abs(&self) -> Iv {
        if self.lo >= Float::with_val(PREC, 0) {
            self.clone()
        } else if self.hi <= Float::with_val(PREC, 0) {
            self.neg()
        } else {
            let hi = Float::with_val_round(PREC, self.hi.clone().abs(), Round::Up).0;
            Iv { lo: Float::with_val(PREC, 0), hi }
        }
    }
    fn sqrt(&self) -> Iv {
        let lo = Float::with_val_round(PREC, self.lo.clone().sqrt(), Round::Down).0;
        let hi = Float::with_val_round(PREC, self.hi.clone().sqrt(), Round::Up).0;
        Iv { lo, hi }
    }
    fn lo_f64(&self) -> f64 { self.lo.to_f64_round(Round::Down) }
    fn hi_f64(&self) -> f64 { self.hi.to_f64_round(Round::Up) }
    fn contains_zero(&self) -> bool { self.lo <= Float::with_val(PREC, 0) && self.hi >= Float::with_val(PREC, 0) }
    fn strictly_positive(&self) -> bool { self.lo > Float::with_val(PREC, 0) }
}

// ---------------------------------------------------------------------------
// sinc with rigorous enclosure over an interval
// ---------------------------------------------------------------------------

/// sinc(x)=sin(x)/x at a point, rigorous (lo, hi).
fn sinc_point(x: f64) -> (Float, Float) {
    if x == 0.0 {
        return (Float::with_val(PREC, 1), Float::with_val(PREC, 1));
    }
    let ax = Float::with_val_round(PREC, x.abs(), Round::Down).0;
    let ax_up = Float::with_val_round(PREC, x.abs(), Round::Up).0;
    let mut n_lo = Float::with_val(PREC, &ax);
    n_lo.sin_round(Round::Down);
    let mut n_hi = Float::with_val(PREC, &ax_up);
    n_hi.sin_round(Round::Up);
    let q_lo = Float::with_val_round(PREC, &n_lo / &ax_up, Round::Down).0;
    let q_hi = Float::with_val_round(PREC, &n_hi / &ax, Round::Up).0;
    (q_lo, q_hi)
}

/// k-th positive root of x = tan x (k >= 1). Bracket k*pi < r < k*pi + pi/2.
fn tan_root(k: u64) -> f64 {
    let pi = std::f64::consts::PI;
    let mut lo = k as f64 * pi;
    let mut hi = lo + pi / 2.0;
    for _ in 0..300 {
        let mid = (lo + hi) / 2.0;
        let f = mid - mid.tan();
        if f > 0.0 { lo = mid; } else { hi = mid; }
    }
    (lo + hi) / 2.0
}

/// Rigorous enclosure of sinc over [a, b].
fn sinc_iv(a: f64, b: f64) -> Iv {
    let mut glb = Float::with_val(PREC, f64::INFINITY);
    let mut lub = Float::with_val(PREC, f64::NEG_INFINITY);
    let mut fold = |x: f64, glb: &mut Float, lub: &mut Float| {
        let (l, u) = sinc_point(x);
        if &l < glb { *glb = l; }
        if &u > lub { *lub = u; }
    };
    fold(a, &mut glb, &mut lub);
    fold(b, &mut glb, &mut lub);
    let m = a.abs().max(b.abs());
    let lo_inner = a.abs().min(b.abs());
    let mut k: u64 = 1;
    loop {
        let r = tan_root(k);
        if r > m { break; }
        if r >= lo_inner {
            fold(r, &mut glb, &mut lub);
        }
        k += 1;
    }
    if a <= 0.0 && b >= 0.0 {
        if Float::with_val(PREC, 1) > lub { lub = Float::with_val(PREC, 1); }
    }
    Iv { lo: glb, hi: lub }
}

// ---------------------------------------------------------------------------
// Cosine kernel
// ---------------------------------------------------------------------------

struct CosineKernel { alpha: f64, k0: f64, k0_sq: f64 }

impl CosineKernel {
    fn new(alpha: f64) -> CosineKernel {
        // K0 = sinc(alpha/2)
        let (l, u) = sinc_point(alpha / 2.0);
        let k0 = (l.to_f64_round(Round::Down) + u.to_f64_round(Round::Up)) / 2.0;
        CosineKernel { alpha, k0, k0_sq: k0 * k0 }
    }
    /// Enclosure of K on cell [i/grid, (i+1)/grid].
    fn k_on_cell(&self, index: i64, grid: i64) -> Iv {
        let pi = std::f64::consts::PI;
        let cl = index as f64 / grid as f64;
        let ch = (index as f64 + 1.0) / grid as f64;
        // a(x) = (alpha - 2 pi x)/2 decreasing; b(x) = (alpha + 2 pi x)/2 increasing
        let a_lo = (self.alpha - 2.0 * pi * ch) / 2.0;
        let a_hi = (self.alpha - 2.0 * pi * cl) / 2.0;
        let b_lo = (self.alpha + 2.0 * pi * cl) / 2.0;
        let b_hi = (self.alpha + 2.0 * pi * ch) / 2.0;
        let sa = sinc_iv(a_lo, a_hi);
        let sb = sinc_iv(b_lo, b_hi);
        let sum_lo = Float::with_val_round(PREC, &sa.lo + &sb.lo, Round::Down).0;
        let sum_hi = Float::with_val_round(PREC, &sa.hi + &sb.hi, Round::Up).0;
        let k_lo = Float::with_val_round(PREC, sum_lo / 2, Round::Down).0;
        let k_hi = Float::with_val_round(PREC, sum_hi / 2, Round::Up).0;
        Iv { lo: k_lo, hi: k_hi }
    }
    /// Rigorous lower bound of w = (K/K0)^2 on cell index, as f64 (nextafter down).
    fn w_lower_on_cell(&self, index: i64, grid: i64) -> f64 {
        let k = self.k_on_cell(index, grid);
        let k_abs = k.abs();
        let ratio_lo = Float::with_val_round(PREC, &k_abs.lo / self.k0, Round::Down).0;
        let w = Float::with_val_round(PREC, &ratio_lo * &ratio_lo, Round::Down).0;
        w.to_f64_round(Round::Down).next_down()
    }
}

// ---------------------------------------------------------------------------
// RangeMinimum sparse table
// ---------------------------------------------------------------------------

struct RangeMinimum {
    table: Vec<f64>,
    levels: Vec<Vec<f64>>,
    length: usize,
}

impl RangeMinimum {
    fn new(values: &[f64]) -> RangeMinimum {
        let length = values.len();
        let mut levels = vec![values.to_vec()];
        let mut k = 1;
        loop {
            let prev = &levels[k - 1];
            let width = 1 << k;
            if width > length { break; }
            let mut row = Vec::with_capacity(length - width + 1);
            for i in 0..(length - width + 1) {
                row.push(prev[i].min(prev[i + (width >> 1)]));
            }
            levels.push(row);
            k += 1;
        }
        RangeMinimum { table: values.to_vec(), levels, length }
    }
    fn query(&self, left: usize, right: usize) -> f64 {
        if right < left || right >= self.length { return f64::INFINITY; }
        let level = (right - left + 1).ilog2() as usize;
        let width = 1 << level;
        let row = &self.levels[level];
        row[left].min(row[right - width + 1])
    }
}

fn next_down(v: f64) -> f64 { v.next_down() }
fn next_up(v: f64) -> f64 { v.next_up() }

// ---------------------------------------------------------------------------
// Branch-and-bound verifier
// ---------------------------------------------------------------------------

#[derive(Clone)]
struct BBox { coords: Vec<(i64, i64)> }

fn verify_floor(alpha: f64, weights: &HashMap<(usize, usize), f64>, pressure: f64,
                q: usize, target: f64, grid: i64, cap_scheme: &str,
                pressure_coeffs: Option<&[f64]>, nearest_coeffs: Option<&[f64]>,
                max_nodes: Option<u64>, use_tangent: bool) -> String {
    let kernel = CosineKernel::new(alpha);
    let cutoff_units = target / pressure;
    let cutoff_cells = (next_up(cutoff_units) * grid as f64).ceil() as i64 + 1;
    let cell_count = cutoff_cells + 8;
    println!("  grid={grid} cutoff_cells={cutoff_cells} cell_count={cell_count}");

    let table: Vec<f64> = (0..cell_count).map(|i| kernel.w_lower_on_cell(i, grid)).collect();
    let ranges = RangeMinimum::new(&table);
    // second-derivative table: skip for now (tangent bound needs it); use -inf -> no tangent
    let target_upper = next_up(target);
    let pressure_lower = next_down(pressure);

    let one_body = |i: usize, gcell: i64| -> f64 {
        let (p_i, q_i) = if cap_scheme == "coboundary" {
            (pressure_coeffs.unwrap()[i], nearest_coeffs.unwrap()[i])
        } else {
            (pressure, weights.get(&(i, i + 1)).copied().unwrap_or(0.0))
        };
        let mut val = next_down(p_i * gcell as f64 / grid as f64);
        let wl = if gcell < table.len() as i64 { table[gcell as usize] } else { 0.0 };
        val = next_down(val + next_down(q_i * wl));
        val
    };

    let mut components: Vec<Vec<(i64, i64)>> = Vec::new();
    for i in 0..q {
        let mut surviving = Vec::new();
        for index in 0..cutoff_cells {
            if one_body(i, index) < target_upper { surviving.push(index); }
        }
        let mut comps: Vec<(i64, i64)> = Vec::new();
        for &idx in &surviving {
            if let Some(last) = comps.last_mut() {
                if idx == last.1 + 1 { last.1 = idx; continue; }
            }
            comps.push((idx, idx));
        }
        components.push(comps);
        println!("  coord {i}: {} components: {:?}...", components[i].len(),
                 &components[i].iter().take(3).cloned().collect::<Vec<_>>());
    }

    // initial boxes = cartesian product
    let mut initial: Vec<BBox> = vec![BBox { coords: vec![] }];
    for comp in &components {
        let mut next = Vec::new();
        for b in &initial {
            for &(a, c) in comp {
                let mut nb = b.clone();
                nb.coords.push((a, c));
                next.push(nb);
            }
        }
        initial = next;
    }
    println!("  initial boxes: {}", initial.len());

    let box_lower = |box_: &BBox| -> f64 {
        let mut low_prefix = vec![0i64];
        let mut high_prefix = vec![0i64];
        for &(lo, hi) in &box_.coords {
            low_prefix.push(low_prefix.last().unwrap() + lo);
            high_prefix.push(high_prefix.last().unwrap() + hi);
        }
        let mut result = 0.0f64;
        if cap_scheme == "coboundary" {
            for i in 0..q {
                let p_i = pressure_coeffs.unwrap()[i];
                result = next_down(result + next_down(p_i * (low_prefix[i+1] - low_prefix[i]) as f64 / grid as f64));
            }
            for i in 0..q {
                let q_i = nearest_coeffs.unwrap()[i];
                let (lo, hi) = box_.coords[i];
                if hi < ranges.length as i64 {
                    result = next_down(result + next_down(q_i * ranges.query(lo as usize, hi as usize)));
                }
            }
            let mut pair_list: Vec<(usize, usize)> = weights.keys().cloned().collect();
            pair_list.sort();
            for &(i, j) in &pair_list {
                let span = (j - i) as i64;
                let left = low_prefix[j] - low_prefix[i];
                let right = high_prefix[j] - high_prefix[i] + span - 1;
                if right >= ranges.length as i64 { continue; }
                result = next_down(result + next_down(weights[&(i, j)] * ranges.query(left as usize, right as usize)));
            }
            result
        } else {
            result = next_down(pressure_lower * (*low_prefix.last().unwrap()) as f64 / grid as f64);
            let mut pair_list: Vec<(usize, usize)> = weights.keys().cloned().collect();
            pair_list.sort();
            for &(i, j) in &pair_list {
                let span = (j - i) as i64;
                let left = low_prefix[j] - low_prefix[i];
                let right = high_prefix[j] - high_prefix[i] + span - 1;
                if right >= ranges.length as i64 { continue; }
                result = next_down(result + next_down(weights[&(i, j)] * ranges.query(left as usize, right as usize)));
            }
            result
        }
    };

    let mut stack = initial;
    let mut nodes: u64 = 0;
    let mut pruned_interval: u64 = 0;
    let mut pruned_pressure: u64 = 0;
    let mut splits: u64 = 0;
    while let Some(box_) = stack.pop() {
        nodes += 1;
        if let Some(mn) = max_nodes { if nodes > mn {
            return format!("{{'verified': False, 'nodes': {nodes}, 'status': 'node-limit'}}");
        }}
        if sum_firsts(&box_) >= cutoff_cells {
            pruned_pressure += 1;
            continue;
        }
        let low = box_lower(&box_);
        if low >= target_upper {
            pruned_interval += 1;
            continue;
        }
        let widths: Vec<i64> = box_.coords.iter().map(|&(l, r)| r - l).collect();
        if widths.iter().all(|&w| w == 0) {
            return format!("{{'verified': False, 'nodes': {nodes}, 'status': 'terminal-cell', 'reason': 'cell {:?} low={low}'}}", box_.coords);
        }
        splits += 1;
        let coord = (0..q).max_by_key(|&i| widths[i]).unwrap();
        let (left, right) = box_.coords[coord];
        let mid = (left + right) / 2;
        let mut lo_box = box_.clone(); lo_box.coords[coord] = (left, mid);
        let mut hi_box = box_.clone(); hi_box.coords[coord] = (mid + 1, right);
        stack.push(lo_box);
        stack.push(hi_box);
    }
    format!("{{'verified': True, 'nodes': {nodes}, 'splits': {splits}, 'pruned_interval': {pruned_interval}, 'pruned_pressure': {pruned_pressure}}}")
}

fn sum_firsts(b: &BBox) -> i64 { b.coords.iter().map(|&(l, _)| l).sum() }

fn main() {
    let grid = 4000i64;
    let q = 6usize;
    let mut weights = HashMap::new();
    for i in 0..q {
        for j in (i+1)..q {
            weights.insert((i, j), 2.0 / (7.0 - (j - i) as f64));
        }
    }
    let p_coeff: Vec<f64> = vec![946.0, 1177.0, 877.0, 877.0, 1177.0, 946.0].iter()
        .map(|c| c / 1_920_000.0).collect();
    let q_coeff: Vec<f64> = vec![31343.0/100000.0, 1.0/3.0, 105971.0/300000.0,
                                 105971.0/300000.0, 1.0/3.0, 31343.0/100000.0];
    // acceptance config 3: ainta sanity (MT kernel, uniform, p=1/3000, 19/5000)
    let ainta_alpha = std::f64::consts::SQRT_2;
    let r = verify_floor(ainta_alpha, &weights, 1.0/3000.0, q, 19.0/5000.0, grid,
                         "h", None, None, Some(5_000_000), false);
    println!("AINTA RESULT: {r}");
    // acceptance config 4: tawan baseline (cosine 1.47, coboundary, 577/1e5)
    let r = verify_floor(1.47, &weights, 1.0/3000.0, q, 577.0/100000.0, grid,
                         "coboundary", Some(&p_coeff), Some(&q_coeff),
                         Some(5_000_000), false);
    println!("TAWAN RESULT: {r}");
    for eps in [0.00620f64, 0.00621f64] {
        println!("=== eps={eps} ===");
        let r = verify_floor(1.464, &weights, 1.0/3000.0, q, eps, grid,
                             "coboundary", Some(&p_coeff), Some(&q_coeff),
                             Some(5_000_000), false);
        println!("RESULT: {r}");
    }
}
