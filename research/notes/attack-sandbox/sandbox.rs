// sandbox: V7 method sandbox — certificate value (bound/N) on three worlds.
// (a) REAL all-on-line (LMFDB zeros / computed zeros), (b) FORCED OFF-LINE (inject
// a few % of pairs, finitet synthetic-pair machinery §7 of attack-finitet.md),
// (c) SYNTHETIC all-on-line worlds (rigid lattice, jittered lattice, Poisson).
//
// Same pipeline as finitet main.rs (hard-cutoff psi = cos(sqrt2 u) 1_{|u|<=1/2},
// W_T = V^T V / int psi^2), plus the two certificates compared against 0.6725:
//   bound_rank/N = 2 tr/N - ||W||^2_HS/N          (Lemma 3.4, rank >= 2tr - ||.||^2)
//   bound_s1/N   = 4 tr/N - ||W||^2_HS/N - 2      (Thm B / Lemma R c=2, s1 >= 4tr - ||.||^2 - 2N)
// both -> 2 - c = 0.672500703679412 asymptotically in the all-on-line world
// (c = 1/2 + (1/sqrt2)cot(1/sqrt2) = 1.327499296320588, HS constant of Lemma 3.3).
// In a world with N2 off-line pairs and N1 = N - 2N2 on-line zeros, the truth is
// s1/N = N1/N and the s1-certificate must satisfy bound_s1 <= s1 (validity check).
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

// psi2(s) = transform of psi^2 at rescaled argument (int psi^2 = psi2(0) = 1/2 + sin(sqrt2)/(2 sqrt2))
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

// jacobi eigenvalues of a real symmetric matrix (diagonal entries at end)
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

// ---------- atoms ----------
#[derive(Clone, Copy, Debug)]
enum Atom {
    OnLine { s: f64 },               // real s-coordinate (zero on the line)
    Pair { s: f64, imb: f64 },       // off-line pair, members at s +- i*imb
}

// build G = sum_rho v_rho v_rho^T (real symmetric; pairs contribute v v^T + conj(v) conj(v)^T
// = 2(Re v Re v^T - Im v Im v^T)); W = G / int_psi2
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
                // v = psi(s - k + i*imb); pair form 2(a a^T - b b^T), a=Re v, b=Im v
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

fn measure(tag: &str, atoms: &[Atom], n: usize, int_psi2: f64, truth_s1: Option<f64>, do_eig: bool) {
    let t0 = Instant::now();
    let w = build_w(atoms, n, int_psi2);
    let build_t = t0.elapsed().as_secs_f64();

    // direct tr and HS^2 (exact, O(n^2) after build)
    let mut tr = 0.0;
    let mut hs2 = 0.0;
    let mut diag = 0.0;
    let mut offdiag = 0.0;
    for i in 0..n {
        tr += w[i][i];
        for j in 0..n {
            let x = w[i][j];
            hs2 += x * x;
            if i == j {
                diag += x * x;
            } else {
                offdiag += x * x;
            }
        }
    }
    let c_bound = 1.5 - FRAC_1_SQRT_2 * (FRAC_1_SQRT_2.tan().recip());
    let trn = tr / n as f64;
    let hsn = hs2 / n as f64;
    let b_rank = 2.0 * tr - hs2;
    let b_s1 = 4.0 * tr - hs2 - 2.0 * n as f64;

    if do_eig {
        let (eig, sweeps) = jacobi_eig(&w);
        let eig_sum: f64 = eig.iter().sum();
        let lmax = eig.iter().cloned().fold(0.0_f64, f64::max);
        let r1e6 = eig.iter().filter(|&&x| x > 1e-6 * lmax).count();
        let r1e8 = eig.iter().filter(|&&x| x > 1e-8 * lmax).count();
        let npos = eig.iter().filter(|&&x| x > 1e-10 * lmax).count();
        let nneg = eig.iter().filter(|&&x| x < -1e-10 * lmax).count();
        let mut esort = eig.clone();
        esort.sort_by(|a, b| a.partial_cmp(b).unwrap());
        let hs2_chk: f64 = eig.iter().map(|x| x * x).sum();
        println!(
            "{} N={} | tr/N={:.6} HS2/N={:.6} (diag {:.4} + offdiag {:.4}) | bound_rank/N={:.6} bound_s1/N={:.6} | Delta_rank={:+.6} Delta_s1={:+.6} | rank(1e-6)={} (1e-8)={} n+/n-={}/{} sweeps={} | tr-chk={:.1e} HS2-chk={:.1e} | eigmin/lamax={:.2e} | t={:.1}s",
            tag, n, trn, hsn, diag / n as f64, offdiag / n as f64,
            b_rank / n as f64, b_s1 / n as f64,
            b_rank / n as f64 - c_bound, b_s1 / n as f64 - c_bound,
            r1e6, r1e8, npos, nneg, sweeps,
            (tr - eig_sum).abs(), (hs2 - hs2_chk).abs(),
            esort[0] / lmax, build_t
        );
    } else {
        println!(
            "{} N={} | tr/N={:.6} HS2/N={:.6} (diag {:.4} + offdiag {:.4}) | bound_rank/N={:.6} bound_s1/N={:.6} | Delta_rank={:+.6} Delta_s1={:+.6} | rank=(eig skipped) | t={:.1}s",
            tag, n, trn, hsn, diag / n as f64, offdiag / n as f64,
            b_rank / n as f64, b_s1 / n as f64,
            b_rank / n as f64 - c_bound, b_s1 / n as f64 - c_bound, build_t
        );
    }
    if let Some(s1) = truth_s1 {
        // validity: the s1-certificate must not exceed the true number of on-line zeros
        let cert = b_s1 / n as f64;
        let flag = if cert <= s1 + 1e-9 { "OK" } else { "VIOLATION" };
        println!(
            "    truth s1/N = {:.6} (off-line fraction {:.4});  bound_s1/N = {:.6}  ->  {flag}",
            s1, 1.0 - s1, cert
        );
    }
}

// ---------- world constructors ----------
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

// window ordinates in [T, 2T)
fn window(gams: &[f64], t: f64) -> Vec<f64> {
    gams.iter().copied().filter(|&g| g >= t && g < 2.0 * t).collect()
}

// (a) real world: all on-line, s = (gamma - T) N/T
fn world_real(gwin: &[f64], t: f64) -> Vec<Atom> {
    let n = gwin.len();
    gwin.iter().map(|&g| Atom::OnLine { s: (g - t) * (n as f64) / t }).collect()
}

// (b) forced off-line: keep the lowest N1 = N - 2N2 ordinates on-line; group the top
//     2N2 into N2 consecutive pairs at mean ordinate, split +-beta off the line
fn world_offline(gwin: &[f64], t: f64, f: f64, beta: f64) -> (Vec<Atom>, f64) {
    let n = gwin.len();
    let n2 = (f * n as f64).round() as usize;
    let n1 = n - 2 * n2;
    let mut atoms = Vec::with_capacity(n);
    let imb = beta * (n as f64) / t; // off-line displacement in s-units
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

// (b) forced off-line, RANDOM subset, REPLACE world (N1 + 2*N2 = N):
//     pick 2*N2 random distinct zero indices, sort them, group into N2 consecutive
//     pairs at mean ordinate (split +-beta); the other N - 2*N2 stay on-line
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

// (c1) rigid lattice: N midpoints of the window, s = k + 1/2
fn world_lattice(t: f64) -> Vec<Atom> {
    // N = window count at T; we use the exact count N(T) implied by spacing T/N.
    // We fix N by the RvM-style count below (same as real window size), then place
    // N points at s = k + 1/2.
    let n_est = rvm_count(t);
    (0..n_est).map(|k| Atom::OnLine { s: k as f64 + 0.5 }).collect()
}

fn rvm_count(t: f64) -> usize {
    let n2 = (2.0 * t / (2.0 * PI)) * ((2.0 * t / (2.0 * PI)).ln() - 1.0) + 7.0 / 8.0;
    let n1 = (t / (2.0 * PI)) * ((t / (2.0 * PI)).ln() - 1.0) + 7.0 / 8.0;
    (n2 - n1).round().max(1.0) as usize
}

// (c2) Poisson: N uniform points in [0, N) in s-space (same density 1)
fn world_poisson(t: f64, seed: u64) -> Vec<Atom> {
    let n = rvm_count(t);
    let mut rng = SplitMix64::new(seed);
    (0..n).map(|_| Atom::OnLine { s: rng.next_f64() * n as f64 }).collect()
}

// (c3) jittered lattice: s = k + 1/2 + U(-amp, amp)
fn world_jitter(t: f64, amp: f64, seed: u64) -> Vec<Atom> {
    let n = rvm_count(t);
    let mut rng = SplitMix64::new(seed);
    (0..n).map(|k| Atom::OnLine { s: k as f64 + 0.5 + (2.0 * rng.next_f64() - 1.0) * amp }).collect()
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

// isolated-pair spectral check (reproduces finitet main.rs §7: {+1.817579, -0.151694})
fn pair_check(int_psi2: f64) {
    let t = 200.0_f64;
    let gams = load_zeros("/home/vstaln/riemann/tools/data/zeros_1_1000.txt");
    let gwin = window(&gams, t);
    let n = gwin.len();
    let beta = 0.3_f64;
    let imb = -beta * (n as f64) / t;
    let s = (gwin[0] - t) * (n as f64) / t;
    let mut a = vec![0.0; n];
    let mut b = vec![0.0; n];
    for k in 0..n {
        let w = psi(C::new(s - k as f64, imb));
        a[k] = w.re;
        b[k] = w.im;
    }
    let mut m = vec![vec![0.0; n]; n];
    for i in 0..n {
        for j in 0..n {
            m[i][j] = 2.0 * (a[i] * a[j] - b[i] * b[j]);
        }
    }
    let (meig, _) = jacobi_eig(&m);
    let mut nz: Vec<f64> = meig.iter().copied().filter(|&x| x.abs() > 1e-10).collect();
    nz.sort_by(|x, y| x.abs().partial_cmp(&y.abs()).unwrap());
    println!(
        "[pair-check T=200 beta=0.3] nonzero eig of M: {:+.6}, {:+.6} (expect +1.817579, -0.151694); in W units (x/int psi^2): {:+.4}, {:+.4}",
        nz[nz.len() - 2], nz[nz.len() - 1], nz[nz.len() - 2] / int_psi2, nz[nz.len() - 1] / int_psi2
    );
}

fn main() {
    let int_psi2 = psi2(C::real(0.0)).re;
    println!("int psi^2 = {:.15}", int_psi2);
    println!("c (HS) = 1.327499296320588  bound const 2 - c = 0.672500703679412\n");

    pair_check(int_psi2);
    println!();

    let gams1k = load_zeros("/home/vstaln/riemann/tools/data/zeros_1_1000.txt");
    let gams10k = load_zeros("/home/vstaln/riemann/tools/data/zeros_computed_10000.txt");

    println!("===== WORLD (a): REAL, all on-line (zeros_1_1000.txt) =====");
    for &t in &[100.0, 200.0, 300.0, 400.0, 500.0, 600.0, 700.0] {
        let gwin = window(&gams1k, t);
        let n = gwin.len();
        let atoms = world_real(&gwin, t);
        measure(&format!("real T={t:4.0}"), &atoms, n, int_psi2, None, true);
    }

    println!("\n===== WORLD (a'): REAL, all on-line, larger T (zeros_computed_10000.txt) =====");
    for &t in &[900.0, 1100.0, 1300.0] {
        let gwin = window(&gams10k, t);
        let n = gwin.len();
        let atoms = world_real(&gwin, t);
        measure(&format!("real T={t:4.0}"), &atoms, n, int_psi2, None, false);
    }

    println!("\n===== WORLD (b): FORCED OFF-LINE (pairs at beta, fractions f of N) =====");
    for &t in &[200.0, 500.0] {
        for &beta in &[0.1, 0.3] {
            for &f in &[0.01, 0.02, 0.05] {
                let gwin = window(&gams1k, t);
                let n = gwin.len();
                let (atoms, s1) = world_offline(&gwin, t, f, beta);
                measure(
                    &format!("offline T={t:4.0} f={f:.2} beta={beta:.1}"),
                    &atoms,
                    n,
                    int_psi2,
                    Some(s1),
                    true,
                );
            }
        }
    }
    // random-subset injection (pattern-robustness) at T=500
    for &beta in &[0.3] {
        for &f in &[0.02, 0.05] {
            let gwin = window(&gams1k, 500.0);
            let n = gwin.len();
            let (atoms, s1) = world_offline_random(&gwin, 500.0, f, beta, 7);
            measure(
                &format!("offline-rnd T=500 f={f:.2} beta={beta:.1} s=7"),
                &atoms,
                n,
                int_psi2,
                Some(s1),
                true,
            );
        }
    }
    // beta-sweep at the crossing (T=500, f=0.02): how deep must off-line zeros be to break 0.6725?
    for &beta in &[0.05, 0.1, 0.2, 0.3, 0.5] {
        let gwin = window(&gams1k, 500.0);
        let n = gwin.len();
        let (atoms, s1) = world_offline(&gwin, 500.0, 0.02, beta);
        measure(
            &format!("offline T=500 f=0.02 beta={beta:.2}"),
            &atoms,
            n,
            int_psi2,
            Some(s1),
            true,
        );
    }

    println!("\n===== WORLD (c): SYNTHETIC all-on-line =====");
    for &t in &[200.0, 500.0] {
        let atoms = world_lattice(t);
        measure(&format!("lattice  T={t:4.0}"), &atoms, atoms.len(), int_psi2, None, true);
    }
    for &t in &[200.0, 500.0] {
        let atoms = world_jitter(t, 0.2, 42);
        measure(&format!("jitter   T={t:4.0}"), &atoms, atoms.len(), int_psi2, None, true);
    }
    for &(t, seed) in &[(200.0, 1u64), (500.0, 1u64), (500.0, 2u64)] {
        let atoms = world_poisson(t, seed);
        measure(&format!("poisson  T={t:4.0} s={seed}"), &atoms, atoms.len(), int_psi2, None, true);
    }
    // asymptotic checks at larger T (direct only)
    for &t in &[1100.0] {
        let atoms = world_lattice(t);
        measure(&format!("lattice  T={t:4.0}"), &atoms, atoms.len(), int_psi2, None, false);
    }
    for &(t, seed) in &[(1100.0, 1u64)] {
        let atoms = world_poisson(t, seed);
        measure(&format!("poisson  T={t:4.0} s={seed}"), &atoms, atoms.len(), int_psi2, None, false);
    }
}
