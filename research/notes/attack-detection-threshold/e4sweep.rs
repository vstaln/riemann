// e4sweep: E4 — off-line detection-threshold sweep (idea-generator-ml-eco E4,
// extends attack-finitet.md §7 / attack-sandbox.md world (b)).
//
// Question: how much off-line structure could exist in the REAL data without the
// certificate noticing? I.e. the detection threshold — the realized-world slack in
// off-line pairs. Tells us how "loud" a hypothetical off-line signal must be.
//
// Machinery is a verbatim copy of the V7 sandbox (finitet-v7/src/sandbox.rs):
//   psi(u) = cos(sqrt2 u) 1_{|u|<=1/2};  psi2(s) = transform of psi^2;
//   int psi^2 = 0.849227999318304;  s_rho = (gamma - T)*N/T;
//   W_T = (1/int psi^2) V^T V;  certificates:
//     bound_rank/N = (2 tr - ||W||^2_HS)/N   (Lemma 3.4, rank >= 2tr - ||.||^2)
//     bound_s1/N   = (4 tr - ||W||^2_HS - 2N)/N  (Thm B / Lemma R c=2)
//   both -> 2 - c = 0.672500703679412 (c = 1.327499296320588).
//   Off-line pair at mean ordinate gamma0, members at gamma0 +- beta (beta in
//   ORDINATE units; s-space displacement imb = beta*N/T), pair matrix
//   M = vv^T + conj(v)conj(v)^T = 2(Re v Re v^T - Im v Im v^T), signature (1,1).
//
// Outputs:
//   A. REAL column T=100..700 (eig) + 900/1100/1300 (direct): tr/N, HS2/N,
//      bound_rank/N, bound_s1/N, n_- (three thresholds), min eig.  Confirms
//      n_- = 0 [idea-generator-chem F8] and computes the real-data noise band
//      [band_min, band_max] of bound_rank/N across T (the task's 0.704-0.719).
//   B. Sweep grid: T in {200,300,500}, beta in {0.05,0.1,0.2,0.3,0.5,1.0},
//      f in {0,0.005,0.01,0.02,0.04,0.08}, deterministic top-clustered injection
//      (N2 = round(f*N) pairs at the top of the window).  Certificate values;
//      eig (n_-) at T=300.
//   C. Pattern check: random-scattered injection (seed 7) at T=300, same grid.
//   D. Single-pair beta floor: one pair at the top of the window, beta sweep;
//      pair negative eigenvalue vs beta and n_- of the full W -> the beta at which
//      the direct detector n_- > 0 clears the numerical floor.
//   Thresholds (computed inside the program):
//     f_min_band(beta, T): smallest f with bound_rank/N < band_min (outside the
//       real-data noise band).
//     f_min_theory(beta, T): smallest f with bound_rank/N < 0.6725007037.
//     beta_floor(T): smallest beta with n_- >= 1 (direct detector).
use std::f64::consts::{FRAC_1_SQRT_2, PI, SQRT_2};
use std::time::Instant;

#[derive(Clone, Copy, Debug)]
struct C {
    re: f64,
    im: f64,
}
impl C {
    fn new(re: f64, im: f64) -> Self {
        C { re, im }
    }
    fn real(re: f64) -> Self {
        C { re, im: 0.0 }
    }
    fn scale(self, f: f64) -> C {
        C::new(self.re * f, self.im * f)
    }
    fn div(self, o: C) -> C {
        let d = o.re * o.re + o.im * o.im;
        C::new((self.re * o.re + self.im * o.im) / d, (self.im * o.re - self.re * o.im) / d)
    }
    fn conj(self) -> C {
        C::new(self.re, -self.im)
    }
    fn abs2(self) -> f64 {
        self.re * self.re + self.im * self.im
    }
    fn sin(self) -> C {
        C::new(self.re.sin() * self.im.cosh(), self.re.cos() * self.im.sinh())
    }
}

fn psi(s: C) -> C {
    let s2 = C::real(SQRT_2);
    let d1 = s2.sub(s.scale(2.0 * PI));
    let d2 = s2.add(s.scale(2.0 * PI));
    let mut t1 = C::real(FRAC_1_SQRT_2).sub(s.scale(PI)).sin().div(d1);
    if d1.abs2() < 1e-18 {
        t1 = C::real(0.5);
    }
    let mut t2 = C::real(FRAC_1_SQRT_2).add(s.scale(PI)).sin().div(d2);
    if d2.abs2() < 1e-18 {
        t2 = C::real(0.5);
    }
    t1.add(t2)
}

fn psi2(s: C) -> C {
    let s2 = C::real(SQRT_2);
    let ps = s.scale(PI);
    let mut t1 = ps.sin().div(ps.scale(2.0));
    if ps.abs2() < 1e-18 {
        t1 = C::real(0.5);
    }
    let a = s2.sub(ps);
    let b = s2.add(ps);
    let mut t2 = a.sin().div(a);
    if a.abs2() < 1e-18 {
        t2 = C::real(1.0);
    }
    let mut t3 = b.sin().div(b);
    if b.abs2() < 1e-18 {
        t3 = C::real(1.0);
    }
    t1.add(t2.add(t3).scale(0.25))
}
impl C {
    fn add(self, o: C) -> C {
        C::new(self.re + o.re, self.im + o.im)
    }
    fn sub(self, o: C) -> C {
        C::new(self.re - o.re, self.im - o.im)
    }
}

fn jacobi_eig(a0: &[Vec<f64>]) -> (Vec<f64>, usize) {
    let n = a0.len();
    let mut a = a0.to_vec();
    let mut sweeps = 0;
    loop {
        sweeps += 1;
        let mut off = 0.0;
        for i in 0..n {
            for j in i + 1..n {
                off += a[i][j] * a[i][j];
            }
        }
        if off < 1e-28 || sweeps > 60 {
            break;
        }
        for p in 0..n {
            for q in p + 1..n {
                let apq = a[p][q];
                if apq.abs() < 1e-300 {
                    continue;
                }
                let app = a[p][p];
                let aqq = a[q][q];
                let theta = (aqq - app) / (2.0 * apq);
                let t = if theta >= 0.0 {
                    1.0 / (theta + (theta * theta + 1.0).sqrt())
                } else {
                    1.0 / (theta - (theta * theta + 1.0).sqrt())
                };
                let c = 1.0 / (t * t + 1.0).sqrt();
                let s = t * c;
                for k in 0..n {
                    if k != p && k != q {
                        let akp = a[k][p];
                        let akq = a[k][q];
                        a[k][p] = c * akp - s * akq;
                        a[p][k] = a[k][p];
                        a[k][q] = s * akp + c * akq;
                        a[q][k] = a[k][q];
                    }
                }
                a[p][p] = c * c * app - 2.0 * s * c * apq + s * s * aqq;
                a[q][q] = s * s * app + 2.0 * s * c * apq + c * c * aqq;
                a[p][q] = 0.0;
                a[q][p] = 0.0;
            }
        }
    }
    ((0..n).map(|i| a[i][i]).collect(), sweeps)
}

#[derive(Clone, Copy, Debug)]
enum Atom {
    OnLine { s: f64 },
    Pair { s: f64, imb: f64 },
}

fn build_w(atoms: &[Atom], n: usize, int_psi2: f64) -> Vec<Vec<f64>> {
    let mut g = vec![vec![0.0; n]; n];
    for &a in atoms {
        match a {
            Atom::OnLine { s } => {
                let v: Vec<f64> = (0..n).map(|k| psi(C::real(s - k as f64)).re).collect();
                for i in 0..n {
                    let vi = v[i];
                    let row = &mut g[i];
                    for j in 0..n {
                        row[j] += vi * v[j];
                    }
                }
            }
            Atom::Pair { s, imb } => {
                let mut a = vec![0.0; n];
                let mut b = vec![0.0; n];
                for k in 0..n {
                    let w = psi(C::new(s - k as f64, imb));
                    a[k] = w.re;
                    b[k] = w.im;
                }
                for i in 0..n {
                    let ai = a[i];
                    let bi = b[i];
                    let row = &mut g[i];
                    for j in 0..n {
                        row[j] += 2.0 * (ai * a[j] - bi * b[j]);
                    }
                }
            }
        }
    }
    g.iter().map(|row| row.iter().map(|&x| x / int_psi2).collect()).collect()
}

#[derive(Clone, Copy, Debug)]
struct Cert {
    n: usize,
    trn: f64,
    hsn: f64,
    b_rank: f64,
    b_s1: f64,
}

// direct certificate (no eig): tr/N, HS2/N, bound_rank/N, bound_s1/N
fn measure_cert(atoms: &[Atom], n: usize, int_psi2: f64) -> Cert {
    let w = build_w(atoms, n, int_psi2);
    let mut tr = 0.0;
    let mut hs2 = 0.0;
    for i in 0..n {
        tr += w[i][i];
        for j in 0..n {
            hs2 += w[i][j] * w[i][j];
        }
    }
    let trn = tr / n as f64;
    let hsn = hs2 / n as f64;
    Cert {
        n,
        trn,
        hsn,
        b_rank: 2.0 * tr - hs2,
        b_s1: 4.0 * tr - hs2 - 2.0 * n as f64,
    }
}

// eig-based extra: rank thresholds, n_+/n_- (3 thresholds), min eig, lambda_max
struct EigStats {
    rank1e6: usize,
    nneg_rel1e9: usize,
    nneg_rel1e10: usize,
    nneg_abs1e12: usize,
    eigmin: f64,
    lmax: f64,
}
fn eig_stats(w: &[Vec<f64>]) -> EigStats {
    let (eig, _) = jacobi_eig(w);
    let lmax = eig.iter().cloned().fold(0.0_f64, f64::max);
    let r1e6 = eig.iter().filter(|&&x| x > 1e-6 * lmax).count();
    let nneg_rel1e9 = eig.iter().filter(|&&x| x < -1e-9 * lmax).count();
    let nneg_rel1e10 = eig.iter().filter(|&&x| x < -1e-10 * lmax).count();
    let nneg_abs1e12 = eig.iter().filter(|&&x| x < -1e-12).count();
    let eigmin = eig.iter().cloned().fold(f64::INFINITY, f64::min);
    EigStats {
        rank1e6: r1e6,
        nneg_rel1e9,
        nneg_rel1e10,
        nneg_abs1e12,
        eigmin,
        lmax,
    }
}

fn load_zeros(path: &str) -> Vec<f64> {
    let mut g = Vec::new();
    for line in std::fs::read_to_string(path).expect("zeros file").lines() {
        let p: Vec<&str> = line.split_whitespace().collect();
        if p.len() >= 2 {
            g.push(p[1].parse().unwrap());
        }
    }
    g
}

fn window(gams: &[f64], t: f64) -> Vec<f64> {
    gams.iter().copied().filter(|&g| g >= t && g < 2.0 * t).collect()
}

fn world_real(gwin: &[f64], t: f64) -> Vec<Atom> {
    let n = gwin.len();
    gwin.iter().map(|&g| Atom::OnLine { s: (g - t) * (n as f64) / t }).collect()
}

// deterministic: lowest N1 = N - 2N2 ordinates on-line, top 2N2 form N2 pairs at
// the top of the window (mean ordinate per pair, split +-beta)
fn world_offline(gwin: &[f64], t: f64, f: f64, beta: f64) -> (Vec<Atom>, f64) {
    let n = gwin.len();
    let n2 = (f * n as f64).round() as usize;
    let n1 = n - 2 * n2;
    let mut atoms = Vec::with_capacity(n);
    let imb = beta * (n as f64) / t;
    for &g in &gwin[..n1] {
        atoms.push(Atom::OnLine { s: (g - t) * (n as f64) / t });
    }
    let mut k = n1;
    while k + 1 < n {
        let gm = 0.5 * (gwin[k] + gwin[k + 1]);
        let s = (gm - t) * (n as f64) / t;
        atoms.push(Atom::Pair { s, imb });
        k += 2;
    }
    (atoms, n1 as f64 / n as f64)
}

// random-scattered (seed), replace-world
fn world_offline_random(gwin: &[f64], t: f64, f: f64, beta: f64, seed: u64) -> (Vec<Atom>, f64) {
    let n = gwin.len();
    let n2 = (f * n as f64).round() as usize;
    let removed = 2 * n2;
    let n1 = n - removed;
    let imb = beta * (n as f64) / t;
    let mut rng = SplitMix64::new(seed);
    let mut idx: Vec<usize> = (0..n).collect();
    let mut pick = Vec::with_capacity(removed);
    for k in 0..removed {
        let j = k + (rng.next_u64() as usize) % (n - k);
        idx.swap(k, j);
        pick.push(idx[k]);
    }
    pick.sort_unstable();
    let mut is_pair = vec![false; n];
    for k in 0..n2 {
        let i0 = pick[2 * k];
        let i1 = pick[2 * k + 1];
        is_pair[i0] = true;
        is_pair[i1] = true;
    }
    let mut atoms = Vec::with_capacity(n);
    let mut k = 0;
    while k + 1 < removed {
        let i0 = pick[k];
        let i1 = pick[k + 1];
        let gm = 0.5 * (gwin[i0] + gwin[i1]);
        let s = (gm - t) * (n as f64) / t;
        atoms.push(Atom::Pair { s, imb });
        k += 2;
    }
    for i in 0..n {
        if !is_pair[i] {
            atoms.push(Atom::OnLine { s: (gwin[i] - t) * (n as f64) / t });
        }
    }
    (atoms, n1 as f64 / n as f64)
}

// single pair at the top of the window (last two ordinates), exactly one pair
fn world_one_pair_top(gwin: &[f64], t: f64, beta: f64) -> Vec<Atom> {
    let n = gwin.len();
    let imb = beta * (n as f64) / t;
    let gm = 0.5 * (gwin[n - 2] + gwin[n - 1]);
    let s = (gm - t) * (n as f64) / t;
    let mut atoms: Vec<Atom> = gwin[..n - 2]
        .iter()
        .map(|&g| Atom::OnLine { s: (g - t) * (n as f64) / t })
        .collect();
    atoms.push(Atom::Pair { s, imb });
    atoms
}

struct SplitMix64(u64);
impl SplitMix64 {
    fn new(seed: u64) -> Self {
        SplitMix64(seed)
    }
    fn next_u64(&mut self) -> u64 {
        self.0 = self.0.wrapping_add(0x9E3779B97F4A7C15);
        let mut z = self.0;
        z = (z ^ (z >> 30)).wrapping_mul(0xBF58476D1CE4E5B9);
        z = (z ^ (z >> 27)).wrapping_mul(0x94D049BB133111EB);
        z ^ (z >> 31)
    }
    fn next_f64(&mut self) -> f64 {
        (self.next_u64() >> 11) as f64 / (1u64 << 53) as f64
    }
}

fn main() {
    let int_psi2 = psi2(C::real(0.0)).re;
    let c_bound = 1.5 - FRAC_1_SQRT_2 * (FRAC_1_SQRT_2.tan().recip());
    println!("int psi^2 = {:.15}", int_psi2);
    println!("c (HS) = 1.327499296320588  2 - c = 0.672500703679412  (c_bound computed {:.15})", c_bound);

    let gams1k = load_zeros("/home/vstaln/riemann/tools/data/zeros_1_1000.txt");
    let gams10k = load_zeros("/home/vstaln/riemann/tools/data/zeros_computed_10000.txt");

    // ---------- A. REAL column + noise band ----------
    println!("\n===== A. REAL world (all on-line): certificate + n_- =====");
    println!("T,N,tr/N,HS2/N,bound_rank/N,bound_s1/N,rank1e6,nneg_rel1e9,nneg_rel1e10,nneg_abs1e12,eigmin");
    let mut band: Vec<f64> = Vec::new();
    let mut real_at_t: Vec<(f64, f64, f64)> = Vec::new(); // (T, b_rank/N, b_s1/N)
    for &t in &[100.0, 200.0, 300.0, 400.0, 500.0, 600.0, 700.0] {
        let gwin = window(&gams1k, t);
        let n = gwin.len();
        let atoms = world_real(&gwin, t);
        let c = measure_cert(&atoms, n, int_psi2);
        let w = build_w(&atoms, n, int_psi2);
        let e = eig_stats(&w);
        band.push(c.b_rank / n as f64);
        real_at_t.push((t, c.b_rank / n as f64, c.b_s1 / n as f64));
        println!(
            "{:.0},{},{:.6},{:.6},{:.6},{:.6},{},{},{},{},{:.3e}",
            t, n, c.trn, c.hsn, c.b_rank / n as f64, c.b_s1 / n as f64,
            e.rank1e6, e.nneg_rel1e9, e.nneg_rel1e10, e.nneg_abs1e12, e.eigmin
        );
    }
    for &t in &[900.0, 1100.0, 1300.0] {
        let gwin = window(&gams10k, t);
        let n = gwin.len();
        let atoms = world_real(&gwin, t);
        let c = measure_cert(&atoms, n, int_psi2);
        band.push(c.b_rank / n as f64);
        real_at_t.push((t, c.b_rank / n as f64, c.b_s1 / n as f64));
        println!(
            "{:.0},{},{:.6},{:.6},{:.6},{:.6},(eig skipped)",
            t, n, c.trn, c.hsn, c.b_rank / n as f64, c.b_s1 / n as f64
        );
    }
    let band_min = band.iter().cloned().fold(f64::INFINITY, f64::min);
    let band_max = band.iter().cloned().fold(f64::NEG_INFINITY, f64::max);
    println!("NOISE-BAND bound_rank/N over T=100..1300: [{:.6}, {:.6}]  (width {:.6})", band_min, band_max, band_max - band_min);
    // also the s1 band for reference
    let s1_vals: Vec<f64> = real_at_t.iter().map(|&(_, _, s)| s).collect();
    let s1_min = s1_vals.iter().cloned().fold(f64::INFINITY, f64::min);
    let s1_max = s1_vals.iter().cloned().fold(f64::NEG_INFINITY, f64::max);
    println!("NOISE-BAND bound_s1/N  over T=100..1300: [{:.6}, {:.6}]", s1_min, s1_max);

    // ---------- B. SWEEP grid ----------
    let betas = [0.05, 0.1, 0.2, 0.3, 0.5, 1.0];
    let fs = [0.0, 0.005, 0.01, 0.02, 0.04, 0.08];
    println!("\n===== B. SWEEP (deterministic top-clustered): certificate vs f, beta, T =====");
    println!("T,beta,f,N2,tr/N,HS2/N,bound_rank/N,bound_s1/N,in_band,below_theory");
    for &t in &[200.0, 300.0, 500.0] {
        let gwin = window(&gams1k, t);
        let n = gwin.len();
        for &beta in &betas {
            for &f in &fs {
                let (atoms, _s1) = world_offline(&gwin, t, f, beta);
                let n2 = (f * n as f64).round() as usize;
                let c = measure_cert(&atoms, n, int_psi2);
                let br = c.b_rank / n as f64;
                let bs1 = c.b_s1 / n as f64;
                let in_band = br >= band_min && br <= band_max;
                let below_theory = br < c_bound;
                println!(
                    "{:.0},{:.2},{:.4},{},{:.6},{:.6},{:.6},{:.6},{},{:}",
                    t, beta, f, n2, c.trn, c.hsn, br, bs1, in_band, below_theory
                );
            }
        }
    }

    // ---------- C. random-scattered pattern at T=300 ----------
    println!("\n===== C. SWEEP (random-scattered seed=7, T=300): certificate + n_- =====");
    println!("beta,f,N2,tr/N,HS2/N,bound_rank/N,bound_s1/N,in_band,nneg_rel1e10");
    let gwin300 = window(&gams1k, 300.0);
    let n300 = gwin300.len();
    for &beta in &betas {
        for &f in &fs {
            let (atoms, _s1) = world_offline_random(&gwin300, 300.0, f, beta, 7);
            let n2 = (f * n300 as f64).round() as usize;
            let c = measure_cert(&atoms, n300, int_psi2);
            let br = c.b_rank / n300 as f64;
            let w = build_w(&atoms, n300, int_psi2);
            let e = eig_stats(&w);
            println!(
                "{:.2},{:.4},{},{:.6},{:.6},{:.6},{:.6},{},{}",
                beta, f, n2, c.trn, c.hsn, br, c.b_s1 / n300 as f64,
                br >= band_min && br <= band_max, e.nneg_rel1e10
            );
        }
    }

    // ---------- D. single-pair beta floor (direct detector n_-) ----------
    println!("\n===== D. Single-pair beta floor: n_- of full W with exactly one pair at the top =====");
    for &t in &[200.0, 300.0] {
        let gwin = window(&gams1k, t);
        let n = gwin.len();
        println!("T={:.0} N={}  imb=beta*N/T={:.4}*beta", t, n, n as f64 / t);
        println!("beta,imb,lambdamin_W,nneg_rel1e9,nneg_rel1e10,nneg_abs1e12,eigmin_paired");
        for &beta in &[0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.3, 0.5, 1.0] {
            let atoms = world_one_pair_top(&gwin, t, beta);
            let w = build_w(&atoms, n, int_psi2);
            let e = eig_stats(&w);
            let imb = beta * (n as f64) / t;
            println!(
                "{:.3},{:.4},{:.6e},{},{},{},{:.3e}",
                beta, imb, e.eigmin, e.nneg_rel1e9, e.nneg_rel1e10, e.nneg_abs1e12, e.eigmin
            );
        }
    }

    // ---------- thresholds ----------
    println!("\n===== THRESHOLDS =====");
    println!("band_min = {:.6}  (lower edge of real-data noise band, bound_rank/N)", band_min);
    println!("theory 0.6725007 = {:.10}", c_bound);
    for &t in &[200.0, 300.0, 500.0] {
        let gwin = window(&gams1k, t);
        let n = gwin.len();
        let real_t = real_at_t.iter().find(|&&(tt, _, _)| (tt - t).abs() < 0.5).unwrap();
        println!(
            "T={:.0}: real bound_rank/N = {:.6} (within band: {}); real bound_s1/N = {:.6}",
            t, real_t.1, real_t.1 >= band_min && real_t.1 <= band_max, real_t.2
        );
        for &beta in &betas {
            let mut fmin_band = f64::INFINITY;
            let mut fmin_theory = f64::INFINITY;
            let mut fmin_band_val = 0.0;
            let mut fmin_theory_val = 0.0;
            for &f in &fs {
                if f == 0.0 {
                    continue;
                }
                let (atoms, _s1) = world_offline(&gwin, t, f, beta);
                let c = measure_cert(&atoms, n, int_psi2);
                let br = c.b_rank / n as f64;
                if br < band_min && f < fmin_band {
                    fmin_band = f;
                    fmin_band_val = br;
                }
                if br < c_bound && f < fmin_theory {
                    fmin_theory = f;
                    fmin_theory_val = br;
                }
            }
            println!(
                "T={:.0} beta={:.2}: f_min_band={:.3} (cert {:.6})   f_min_theory(0.6725)={:.3} (cert {:.6})",
                t, beta, fmin_band, fmin_band_val, fmin_theory, fmin_theory_val
            );
        }
    }

    // n- floor: smallest beta with a resolvable negative from a single pair (T=300)
    {
        let t = 300.0;
        let gwin = window(&gams1k, t);
        let n = gwin.len();
        let mut beta_floor = f64::INFINITY;
        for &beta in &[0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.3, 0.5, 1.0] {
            let atoms = world_one_pair_top(&gwin, t, beta);
            let w = build_w(&atoms, n, int_psi2);
            let e = eig_stats(&w);
            if e.nneg_rel1e10 > 0 && beta < beta_floor {
                beta_floor = beta;
            }
        }
        println!("T=300: smallest beta with n_- (rel 1e-10) >= 1 from a single pair: beta = {:.3}", beta_floor);
    }

    let _ = Instant::now();
}
