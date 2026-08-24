// ---------------------------------------------------------------------------
// Shared search context + threaded branch-and-bound
// ---------------------------------------------------------------------------

struct SearchCtx {
    kernel: CosineKernel,
    ranges: RangeMinimum,
    second_ranges: RangeMinimum,
    second_upper_ranges: RangeMaximum,
    first_ranges: RangeMinimum,
    first_upper_ranges: RangeMaximum,
    weights: HashMap<(usize, usize), f64>,
    pair_list: Vec<(usize, usize)>,
    grid: i64,
    q: usize,
    cap_scheme: String,
    pressure_coeffs: Option<Vec<f64>>,
    nearest_coeffs: Option<Vec<f64>>,
    pressure: f64,
    target_upper: f64,
    target_f: Float,
    cutoff_cells: i64,
}

impl SearchCtx {
    fn box_lower(&self, box_: &BBox) -> f64 {
        let q = self.q;
        let mut low_prefix = vec![0i64];
        let mut high_prefix = vec![0i64];
        for &(lo, hi) in &box_.coords {
            low_prefix.push(low_prefix.last().unwrap() + lo);
            high_prefix.push(high_prefix.last().unwrap() + hi);
        }
        let mut result = 0.0f64;
        if self.cap_scheme == "coboundary" {
            for i in 0..q {
                let p_i = self.pressure_coeffs.as_ref().unwrap()[i];
                result = next_down(result + next_down(p_i * (low_prefix[i+1] - low_prefix[i]) as f64 / self.grid as f64));
            }
            for i in 0..q {
                let q_i = self.nearest_coeffs.as_ref().unwrap()[i];
                let (lo, hi) = box_.coords[i];
                if hi < self.ranges.length as i64 {
                    result = next_down(result + next_down(q_i * self.ranges.query(lo as usize, hi as usize)));
                }
            }
            for &(i, j) in &self.pair_list {
                let span = (j - i) as i64;
                let left = low_prefix[j] - low_prefix[i];
                let right = high_prefix[j] - high_prefix[i] + span - 1;
                if right >= self.ranges.length as i64 { continue; }
                result = next_down(result + next_down(self.weights[&(i, j)] * self.ranges.query(left as usize, right as usize)));
            }
            result
        } else {
            result = next_down(next_down(self.pressure) * (*low_prefix.last().unwrap()) as f64 / self.grid as f64);
            for &(i, j) in &self.pair_list {
                let span = (j - i) as i64;
                let left = low_prefix[j] - low_prefix[i];
                let right = high_prefix[j] - high_prefix[i] + span - 1;
                if right >= self.ranges.length as i64 { continue; }
                result = next_down(result + next_down(self.weights[&(i, j)] * self.ranges.query(left as usize, right as usize)));
            }
            result
        }
    }
}

/// Python tangent_lower port: convex-tangent lower bound of F on the box.
/// None if convexity cannot be certified (PD LDL fails) or any component of
/// the second-derivative table is unavailable.
fn point_cell_range(x: &Iv, grid: i64, length: usize) -> Option<(usize, usize)> {
    if length == 0 { return None; }
    let lo = (x.lo.to_f64_round(Round::Down) * grid as f64).floor() as i64;
    let hi = (x.hi.to_f64_round(Round::Up) * grid as f64).floor() as i64;
    if hi < 0 || lo >= length as i64 { return None; }
    let left = lo.max(0) as usize;
    let right = hi.min(length as i64 - 1) as usize;
    if left > right { None } else { Some((left, right)) }
}

/// Conservative tangent inputs from precomputed cell enclosures. The value
/// uses only a cell lower bound; the derivative is an interval enclosing every
/// derivative in the midpoint's possible cells.
fn table_point_bounds(ctx: &SearchCtx, x: &Iv) -> Option<(f64, Iv)> {
    let (left, right) = point_cell_range(x, ctx.grid, ctx.ranges.length)?;
    let value_lower = ctx.ranges.query(left, right);
    let derivative = Iv {
        lo: mkd(ctx.first_ranges.query(left, right)),
        hi: mku(ctx.first_upper_ranges.query(left, right)),
    };
    if !value_lower.is_finite() || !derivative.lo.is_finite() || !derivative.hi.is_finite() {
        return None;
    }
    Some((value_lower, derivative))
}

/// SOUND convexity certificate (Gershgorin/Weyl), mirroring current Python
/// `tangent_lower`. With H the true interval Hessian on the box,
///   lambda_min(H) >= min_i( H_ii^lo - sum_{j!=i} |H_ij|^up ) > 0
/// only licensees the tangent plane as a valid lower bound. H_ii^lo uses w''
/// LOWER bounds (all coefficients positive); |H_ij|^up uses max(|w''_lo|,|w''_up|)
/// over the covering spans. Returns true iff every diagonal dominance test
/// passes with a strictly positive margin. (NOT the entrywise-lower-bound LDL
/// of the old port, which Python proved INVALID: M >= 0 entrywise with M PD does
/// not imply the true Hessian is PD.)
fn hessian_pd_gershgorin(ctx: &SearchCtx, box_: &BBox) -> bool {
    let q = box_.coords.len();
    let mut low_prefix = vec![0i64];
    let mut high_prefix = vec![0i64];
    for &(lo, hi) in &box_.coords {
        low_prefix.push(low_prefix.last().unwrap() + lo);
        high_prefix.push(high_prefix.last().unwrap() + hi);
    }
    let mut diag_lo = vec![0.0f64; q];
    let mut off_abs = vec![vec![0.0f64; q]; q];
    for &(i, j) in &ctx.pair_list {
        let span = j - i;
        let left = low_prefix[j] - low_prefix[i];
        let right = high_prefix[j] - high_prefix[i] + span as i64 - 1;
        if right < 0 || right as usize >= ctx.second_ranges.length { return false; }
        let s_lo = ctx.second_ranges.query(left as usize, right as usize);
        if s_lo == f64::NEG_INFINITY { return false; }
        let s_up = ctx.second_upper_ranges.query(left as usize, right as usize);
        let s_abs = s_lo.abs().max(s_up.abs());
        let a_ij = ctx.weights[&(i, j)];
        let s_lo_scaled = next_down(a_ij * s_lo);
        let s_abs_scaled = next_up(a_ij * s_abs);
        for a in i..i + span {
            diag_lo[a] += s_lo_scaled;
            for b in i..i + span {
                if a != b { off_abs[a][b] += s_abs_scaled; }
            }
        }
    }
    if ctx.cap_scheme == "coboundary" {
        for i in 0..q {
            let (lo_i, hi_i) = box_.coords[i];
            if hi_i as usize >= ctx.second_ranges.length { return false; }
            let s_lo = ctx.second_ranges.query(lo_i as usize, hi_i as usize);
            if s_lo == f64::NEG_INFINITY { return false; }
            let qn = next_down(ctx.nearest_coeffs.as_ref().unwrap()[i]);
            diag_lo[i] += next_down(qn * s_lo);
        }
    }
    for i in 0..q {
        if diag_lo[i] - off_abs[i].iter().sum::<f64>() <= 0.0 { return false; }
    }
    true
}

fn tangent_lower_point(box_: &BBox, ctx: &SearchCtx) -> Option<Iv> {
    let q = box_.coords.len();
    let mut low_prefix = vec![0i64];
    let mut high_prefix = vec![0i64];
    for &(lo, hi) in &box_.coords {
        low_prefix.push(low_prefix.last().unwrap() + lo);
        high_prefix.push(high_prefix.last().unwrap() + hi);
    }
    if !hessian_pd_gershgorin(ctx, box_) { return None; }

    // tangent plane at midpoint
    let mut midpoints = Vec::with_capacity(q);
    let mut radii = Vec::with_capacity(q);
    for &(lo, hi) in &box_.coords {
        let m = Iv::point((lo + hi + 1) as f64).div(&Iv::point((2 * ctx.grid) as f64));
        let r = next_up((hi - lo + 1) as f64 / (2.0 * ctx.grid as f64));
        midpoints.push(m);
        radii.push(r);
    }
    let mut value = Iv::point(0.0);
    let mut gradient = vec![Iv::point(0.0); q];
    if ctx.cap_scheme == "coboundary" {
        for i in 0..q {
            let pc_i = next_down(ctx.pressure_coeffs.as_ref().unwrap()[i]);
            let term = Iv::point(pc_i).mul(&midpoints[i]);
            value = value.add(&term);
            gradient[i] = gradient[i].add(&Iv::point(pc_i));
        }
    } else {
        for i in 0..q {
            let p = next_down(ctx.pressure);
            let term = Iv::point(p).mul(&midpoints[i]);
            value = value.add(&term);
            gradient[i] = gradient[i].add(&Iv::point(p));
        }
    }
    for &(i, j) in &ctx.pair_list {
        let coeff = Iv::point(next_down(ctx.weights[&(i, j)]));
        let mut point = Iv::point(0.0);
        for kk in i..j { point = point.add(&midpoints[kk]); }
        let (pot, deriv) = ctx.kernel.squared_kernel_derivs_point(&point);
        value = value.add(&coeff.mul(&pot));
        for coordinate in i..j {
            gradient[coordinate] = gradient[coordinate].add(&coeff.mul(&deriv));
        }
    }
    if ctx.cap_scheme == "coboundary" {
        for i in 0..q {
            let qn_i = next_down(ctx.nearest_coeffs.as_ref().unwrap()[i]);
            let coeff = Iv::point(qn_i);
            let (pot, deriv) = ctx.kernel.squared_kernel_derivs_point(&midpoints[i]);
            value = value.add(&coeff.mul(&pot));
            gradient[i] = gradient[i].add(&coeff.mul(&deriv));
        }
    }
    let mut lower = value;
    for i in 0..q {
        let gabs = gradient[i].abs();
        let rad = Iv::point(radii[i]);
        let term = gabs.mul(&rad);
        lower = lower.sub(&term);
    }
    Some(lower)
}


fn tangent_lower_cell(box_: &BBox, ctx: &SearchCtx) -> Option<Iv> {
    let q = box_.coords.len();
    let mut low_prefix = vec![0i64];
    let mut high_prefix = vec![0i64];
    for &(lo, hi) in &box_.coords {
        low_prefix.push(low_prefix.last().unwrap() + lo);
        high_prefix.push(high_prefix.last().unwrap() + hi);
    }
    if !hessian_pd_gershgorin(ctx, box_) { return None; }

    // Tangent plane at the midpoint, using rigorous precomputed cell bounds.
    // The scalar value_lo is a lower bound; gradient remains an interval.
    let mut midpoints = Vec::with_capacity(q);
    let mut radii = Vec::with_capacity(q);
    for &(lo, hi) in &box_.coords {
        let m = Iv::point((lo + hi + 1) as f64).div(&Iv::point((2 * ctx.grid) as f64));
        let r = next_up((hi - lo + 1) as f64 / (2.0 * ctx.grid as f64));
        midpoints.push(m);
        radii.push(r);
    }
    let mut value_lo = 0.0f64;
    let mut gradient = vec![Iv::point(0.0); q];
    if ctx.cap_scheme == "coboundary" {
        for i in 0..q {
            let pc_i = next_down(ctx.pressure_coeffs.as_ref().unwrap()[i]);
            let coeff = Iv::point(pc_i);
            let term = coeff.mul(&midpoints[i]);
            value_lo = next_down(value_lo + term.lo.to_f64_round(Round::Down));
            gradient[i] = gradient[i].add(&coeff);
        }
    } else {
        for i in 0..q {
            let p = next_down(ctx.pressure);
            let coeff = Iv::point(p);
            let term = coeff.mul(&midpoints[i]);
            value_lo = next_down(value_lo + term.lo.to_f64_round(Round::Down));
            gradient[i] = gradient[i].add(&coeff);
        }
    }
    for &(i, j) in &ctx.pair_list {
        let mut point = Iv::point(0.0);
        for kk in i..j { point = point.add(&midpoints[kk]); }
        let (wlo, deriv) = table_point_bounds(ctx, &point)?;
        let coeff_f = next_down(ctx.weights[&(i, j)]);
        value_lo = next_down(value_lo + next_down(coeff_f * wlo));
        let coeff = Iv::point(coeff_f);
        for coordinate in i..j {
            gradient[coordinate] = gradient[coordinate].add(&coeff.mul(&deriv));
        }
    }
    if ctx.cap_scheme == "coboundary" {
        for i in 0..q {
            let qn_i = next_down(ctx.nearest_coeffs.as_ref().unwrap()[i]);
            let coeff = Iv::point(qn_i);
            let (wlo, deriv) = table_point_bounds(ctx, &midpoints[i])?;
            value_lo = next_down(value_lo + next_down(qn_i * wlo));
            gradient[i] = gradient[i].add(&coeff.mul(&deriv));
        }
    }
    let mut lower = Iv::point(value_lo);
    for i in 0..q {
        let gabs = gradient[i].abs();
        let rad = Iv::point(radii[i]);
        let term = gabs.mul(&rad);
        lower = lower.sub(&term);
    }
    Some(lower)
}

#[derive(Default)]
struct Counters {
    nodes: std::sync::atomic::AtomicU64,
    splits: std::sync::atomic::AtomicU64,
    pruned_interval: std::sync::atomic::AtomicU64,
    pruned_pressure: std::sync::atomic::AtomicU64,
    pruned_tangent: std::sync::atomic::AtomicU64,
}

use std::sync::atomic::{AtomicBool, AtomicU64, Ordering};
use std::sync::Mutex;

const BATCH: usize = 512;

fn worker(ctx: &SearchCtx, shared: &Mutex<Vec<BBox>>, stop: &AtomicBool,
          term: &Mutex<Option<String>>, cnt: &Counters,
          progress_every: u64, last_report: &AtomicU64,
          max_nodes: Option<u64>) {
    let mut local: Vec<BBox> = Vec::new();
    loop {
        if stop.load(Ordering::Relaxed) { return; }
        if local.is_empty() {
            let mut g = shared.lock().unwrap();
            if g.is_empty() { return; }
            let take = g.len().min(BATCH);
            let split_at = g.len() - take;
            let tail: Vec<BBox> = g.drain(split_at..).collect();
            local.extend(tail);
        }
        let box_ = local.pop().unwrap();
        let n = cnt.nodes.fetch_add(1, Ordering::Relaxed) + 1;
        if progress_every > 0 {
            let last = last_report.load(Ordering::Relaxed);
            if n >= last + progress_every
                && last_report.compare_exchange(last, n, Ordering::Relaxed, Ordering::Relaxed).is_ok() {
                println!("  nodes={n} splits={} pruned_i={} pruned_p={} pruned_t={}",
                         cnt.splits.load(Ordering::Relaxed),
                         cnt.pruned_interval.load(Ordering::Relaxed),
                         cnt.pruned_pressure.load(Ordering::Relaxed),
                         cnt.pruned_tangent.load(Ordering::Relaxed));
            }
        }
        if let Some(mn) = max_nodes {
            if n > mn {
                *term.lock().unwrap() = Some(format!("node-limit {mn} hit"));
                stop.store(true, Ordering::Relaxed);
                return;
            }
        }
        if sum_firsts(&box_) >= ctx.cutoff_cells {
            cnt.pruned_pressure.fetch_add(1, Ordering::Relaxed);
            continue;
        }
        let low = ctx.box_lower(&box_);
        if low >= ctx.target_upper {
            cnt.pruned_interval.fetch_add(1, Ordering::Relaxed);
            continue;
        }
        let cell_tangent = tangent_lower_cell(&box_, ctx);
        let cell_proves = cell_tangent.as_ref().is_some_and(|tl| tl.lo >= ctx.target_f);
        // Cell intervals are cheap but wider. On unresolved boxes, retry with
        // the tighter outward-rounded point tangent; this is a fallback only.
        let point_proves = if cell_proves {
            false
        } else {
            tangent_lower_point(&box_, ctx)
                .as_ref().is_some_and(|tl| tl.lo >= ctx.target_f)
        };
        if cell_proves || point_proves {
            cnt.pruned_tangent.fetch_add(1, Ordering::Relaxed);
            continue;
        }
        let widths: Vec<i64> = box_.coords.iter().map(|&(l, r)| r - l).collect();
        if widths.iter().all(|&w| w == 0) {
            *term.lock().unwrap() = Some(format!("terminal-cell cell={:?} low={low}", box_.coords));
            stop.store(true, Ordering::Relaxed);
            return;
        }
        cnt.splits.fetch_add(1, Ordering::Relaxed);
        let coord = (0..ctx.q).max_by_key(|&i| widths[i]).unwrap();
        let (left, right) = box_.coords[coord];
        let mid = (left + right) / 2;
        let mut lo_box = box_.clone(); lo_box.coords[coord] = (left, mid);
        local.push(lo_box);
        let mut hi_box = box_.clone(); hi_box.coords[coord] = (mid + 1, right);
        local.push(hi_box);
    }
}

fn build_derivative_tables_parallel(kernel: &CosineKernel, cell_count: i64, grid: i64)
    -> (Vec<f64>, Vec<f64>, Vec<f64>, Vec<f64>) {
    let requested = std::env::var("VRS_TABLE_THREADS").ok()
        .and_then(|s| s.parse::<usize>().ok()).unwrap_or_else(|| {
            std::thread::available_parallelism().map(|n| n.get()).unwrap_or(1)
        });
    let nthreads = requested.min(cell_count.max(1) as usize).min(16);
    let chunk = (cell_count as usize + nthreads - 1) / nthreads;
    let mut slots: Vec<Option<Vec<CellBounds>>> = (0..nthreads).map(|_| None).collect();
    std::thread::scope(|scope| {
        let mut handles = Vec::new();
        for part in 0..nthreads {
            let start = (part * chunk) as i64;
            let end = ((part + 1) * chunk).min(cell_count as usize) as i64;
            if start >= end { continue; }
            let local_kernel = kernel.clone();
            handles.push(scope.spawn(move || {
                let mut values = Vec::with_capacity((end - start) as usize);
                for i in start..end { values.push(local_kernel.cell_bounds(i, grid)); }
                (part, values)
            }));
        }
        for handle in handles {
            let (part, values) = handle.join().expect("derivative table worker panicked");
            slots[part] = Some(values);
        }
    });
    let bounds: Vec<CellBounds> = slots.into_iter().flatten().flatten().collect();
    let second = bounds.iter().map(|b| b.second_lower).collect();
    let second_upper = bounds.iter().map(|b| b.second_upper).collect();
    let first_lower = bounds.iter().map(|b| b.first_lower).collect();
    let first_upper = bounds.iter().map(|b| b.first_upper).collect();
    (second, second_upper, first_lower, first_upper)
}

fn build_table_parallel(kernel: &CosineKernel, cell_count: i64, grid: i64, second: bool) -> Vec<f64> {
    let requested = std::env::var("VRS_TABLE_THREADS").ok()
        .and_then(|s| s.parse::<usize>().ok()).unwrap_or_else(|| {
            std::thread::available_parallelism().map(|n| n.get()).unwrap_or(1)
        });
    let nthreads = requested.min(cell_count.max(1) as usize).min(16);
    let chunk = (cell_count as usize + nthreads - 1) / nthreads;
    let mut slots: Vec<Option<Vec<f64>>> = (0..nthreads).map(|_| None).collect();
    std::thread::scope(|scope| {
        let mut handles = Vec::new();
        for part in 0..nthreads {
            let start = (part * chunk) as i64;
            let end = ((part + 1) * chunk).min(cell_count as usize) as i64;
            if start >= end { continue; }
            let local_kernel = kernel.clone();
            handles.push(scope.spawn(move || {
                let mut values = Vec::with_capacity((end - start) as usize);
                for i in start..end {
                    values.push(if second {
                        local_kernel.w_second_lower_on_cell(i, grid)
                    } else {
                        local_kernel.w_lower_on_cell(i, grid)
                    });
                }
                (part, values)
            }));
        }
        for handle in handles {
            let (part, values) = handle.join().expect("table worker panicked");
            slots[part] = Some(values);
        }
    });
    slots.into_iter().flatten().flatten().collect()
}
fn verify_floor(alpha: f64, weights: &HashMap<(usize, usize), f64>, pressure: f64,
                q: usize, target: f64, grid: i64, cap_scheme: &str,
                pressure_coeffs: Option<&[f64]>, nearest_coeffs: Option<&[f64]>,
                max_nodes: Option<u64>, use_tangent: bool) -> String {
    let kernel = CosineKernel::new(alpha);
    let cutoff_units = target / pressure;
    let cutoff_cells = (next_up(cutoff_units) * grid as f64).ceil() as i64 + 1;
    let cell_count = cutoff_cells + 8;
    println!("  grid={grid} cutoff_cells={cutoff_cells} cell_count={cell_count}");

    let t_table = std::time::Instant::now();
    let table: Vec<f64> = build_table_parallel(&kernel, cell_count, grid, false);
    println!("  kernel table built in {:.1}s", t_table.elapsed().as_secs_f64());
    let ranges = RangeMinimum::new(&table);
    let t_second = std::time::Instant::now();
    let (second_table, second_upper_table, first_lower_table, first_upper_table) =
        build_derivative_tables_parallel(&kernel, cell_count, grid);
    println!("  derivative tables built in {:.1}s", t_second.elapsed().as_secs_f64());
    if std::env::var("VRS_DEBUG").is_ok() {
        let nneg = second_table.iter().filter(|v| **v == f64::NEG_INFINITY).count();
        println!("  DEBUG: second_table len={} (-inf count={}) first6={:?} last3={:?}",
                 second_table.len(), nneg, &second_table[0..6.min(second_table.len())],
                 &second_table[second_table.len().saturating_sub(3)..]);
        println!("  DEBUG: second_upper first6={:?} last3={:?}",
                 &second_upper_table[0..6.min(second_upper_table.len())],
                 &second_upper_table[second_upper_table.len().saturating_sub(3)..]);
        for probe in [3701usize, 5000, 6874, 8000, 49434] {
            if probe < second_table.len() {
                println!("  DEBUG: cell[{probe}] w''_lo={} w''_up={}",
                         second_table[probe], second_upper_table[probe]);
            }
        }
        // sample the second-derivative w''_lo over a 1000-col window near the band
        let wlo_min = second_table[4000..9000].iter().cloned().fold(f64::INFINITY, f64::min);
        let wlo_max = second_table[4000..9000].iter().cloned().fold(f64::NEG_INFINITY, f64::max);
        println!("  DEBUG: band cells[4000..9000] w''_lo in [{wlo_min}, {wlo_max}]");
    }
    let second_ranges = RangeMinimum::new(&second_table);
    let second_upper_ranges = RangeMaximum::new(&second_upper_table);
    let first_ranges = RangeMinimum::new(&first_lower_table);
    let first_upper_ranges = RangeMaximum::new(&first_upper_table);
    let target_upper = next_up(target);
    let target_f = mk(target);

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

    let mut pair_list: Vec<(usize, usize)> = weights.keys().cloned().collect();
    pair_list.sort();
    let ctx = SearchCtx {
        kernel,
        ranges,
        second_ranges,
        second_upper_ranges,
        first_ranges,
        first_upper_ranges,
        weights: weights.clone(),
        pair_list,
        grid,
        q,
        cap_scheme: cap_scheme.to_string(),
        pressure_coeffs: pressure_coeffs.map(|v| v.to_vec()),
        nearest_coeffs: nearest_coeffs.map(|v| v.to_vec()),
        pressure,
        target_upper,
        target_f,
        cutoff_cells,
    };

    if !use_tangent {
        // very small kernels: skip tangent entirely (unused in acceptance cases)
        // placeholder to keep use_tangent meaningful
    }

    let shared = Mutex::new(initial);
    let stop = AtomicBool::new(false);
    let term: Mutex<Option<String>> = Mutex::new(None);
    let cnt = Counters::default();
    let progress_every = std::env::var("VRS_PROGRESS").ok()
        .and_then(|s| s.parse::<u64>().ok()).unwrap_or(0);
    let last_report = AtomicU64::new(0);
    let nthreads = std::env::var("VRS_THREADS").ok()
        .and_then(|s| s.parse::<usize>().ok())
        .unwrap_or_else(|| std::thread::available_parallelism().map(|n| n.get()).unwrap_or(1))
        .min(16);

    std::thread::scope(|s| {
        for _ in 0..nthreads {
            s.spawn(|| worker(&ctx, &shared, &stop, &term, &cnt, progress_every, &last_report, max_nodes));
        }
    });

    let nodes = cnt.nodes.load(Ordering::Relaxed);
    let splits = cnt.splits.load(Ordering::Relaxed);
    let pi = cnt.pruned_interval.load(Ordering::Relaxed);
    let pp = cnt.pruned_pressure.load(Ordering::Relaxed);
    let pt = cnt.pruned_tangent.load(Ordering::Relaxed);
    if let Some(reason) = term.lock().unwrap().clone() {
        return format!("{{\"verified\": False, \"nodes\": {nodes}, \"status\": \"{reason}\"}}");
    }
    format!("{{\"verified\": True, \"nodes\": {nodes}, \"splits\": {splits}, \"pruned_interval\": {pi}, \"pruned_pressure\": {pp}, \"pruned_tangent\": {pt}, \"threads\": {nthreads}}}")
}
