// e4nminus: n_- columns for the deterministic (top-clustered) sweep grid at
// T=200/300/500, so the deliverable table has (f, beta, certificate, n_-).
// Also repeats the key scattered rows.  Thresholds: rel 1e-9, rel 1e-10, abs 1e-12.
use std::f64::consts::{FRAC_1_SQRT_2, PI, SQRT_2};

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
}

fn measure(atoms: &[Atom], n: usize, int_psi2: f64) -> (f64, f64, usize, usize, usize, f64) {
    let w = build_w(atoms, n, int_psi2);
    let mut tr = 0.0;
    let mut hs2 = 0.0;
    for i in 0..n {
        tr += w[i][i];
        for j in 0..n {
            hs2 += w[i][j] * w[i][j];
        }
    }
    let (eig, _) = jacobi_eig(&w);
    let lmax = eig.iter().cloned().fold(0.0_f64, f64::max);
    let n9 = eig.iter().filter(|&&x| x < -1e-9 * lmax).count();
    let n10 = eig.iter().filter(|&&x| x < -1e-10 * lmax).count();
    let n12 = eig.iter().filter(|&&x| x < -1e-12).count();
    let eigmin = eig.iter().cloned().fold(f64::INFINITY, f64::min);
    (
        (2.0 * tr - hs2) / n as f64,
        (4.0 * tr - hs2 - 2.0 * n as f64) / n as f64,
        n9,
        n10,
        n12,
        eigmin,
    )
}

fn top_clustered(gwin: &[f64], t: f64, f: f64, beta: f64) -> Vec<Atom> {
    let n = gwin.len();
    let n2 = (f * n as f64).round() as usize;
    let n1 = n - 2 * n2;
    let imb = beta * (n as f64) / t;
    let mut atoms = Vec::with_capacity(n);
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
    atoms
}

fn scattered(gwin: &[f64], t: f64, f: f64, beta: f64, seed: u64) -> Vec<Atom> {
    let n = gwin.len();
    let n2 = (f * n as f64).round() as usize;
    let removed = 2 * n2;
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
        is_pair[pick[2 * k]] = true;
        is_pair[pick[2 * k + 1]] = true;
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
    atoms
}

fn main() {
    let int_psi2 = psi2(C::real(0.0)).re;
    let gams1k = load_zeros("/home/vstaln/riemann/tools/data/zeros_1_1000.txt");

    println!("===== n_- grid: deterministic top-clustered =====");
    println!("T,beta,f,N2,bound_rank/N,bound_s1/N,nneg1e9,nneg1e10,nneg1e12,eigmin");
    for &t in &[200.0, 300.0, 500.0] {
        let gwin = window(&gams1k, t);
        let n = gwin.len();
        for &beta in &[0.05, 0.1, 0.3, 0.5] {
            for &f in &[0.0, 0.005, 0.02, 0.08] {
                let n2 = (f * n as f64).round() as usize;
                let atoms = if f == 0.0 {
                    (0..n).map(|i| Atom::OnLine { s: (gwin[i] - t) * (n as f64) / t }).collect()
                } else {
                    top_clustered(&gwin, t, f, beta)
                };
                let (br, bs1, n9, n10, n12, emin) = measure(&atoms, n, int_psi2);
                println!("{:.0},{:.2},{:.4},{},{:.6},{:.6},{},{},{},{:.3e}", t, beta, f, n2, br, bs1, n9, n10, n12, emin);
            }
        }
    }

    println!("\n===== n_- grid: random-scattered (seed 7) =====");
    println!("T,beta,f,N2,bound_rank/N,bound_s1/N,nneg1e9,nneg1e10,nneg1e12,eigmin");
    for &t in &[300.0, 500.0] {
        let gwin = window(&gams1k, t);
        let n = gwin.len();
        for &beta in &[0.05, 0.1, 0.3, 0.5] {
            for &f in &[0.0, 0.005, 0.02, 0.08] {
                let n2 = (f * n as f64).round() as usize;
                let atoms = if f == 0.0 {
                    (0..n).map(|i| Atom::OnLine { s: (gwin[i] - t) * (n as f64) / t }).collect()
                } else {
                    scattered(&gwin, t, f, beta, 7)
                };
                let (br, bs1, n9, n10, n12, emin) = measure(&atoms, n, int_psi2);
                println!("{:.0},{:.2},{:.4},{},{:.6},{:.6},{},{},{},{:.3e}", t, beta, f, n2, br, bs1, n9, n10, n12, emin);
            }
        }
    }
}
