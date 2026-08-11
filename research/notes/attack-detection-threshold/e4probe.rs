// e4probe: fine-grid probe below f = 0.5% to pin the exact certificate detection
// threshold for the random-scattered pattern, and to bisect the 1%-2% crossing for
// the top-clustered pattern.  Also records which zero indices a scattered run paired.
// Direct (no eig) except one n_- readout per scattered row at T=300.
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

fn main() {
    let int_psi2 = psi2(C::real(0.0)).re;
    let gams1k = load_zeros("/home/vstaln/riemann/tools/data/zeros_1_1000.txt");
    // band from the full run (computed there; hardcode with provenance in note)
    let band_min = 0.704966_f64;

    println!("===== PROBE 1: random-scattered (seed 7), T=300, fine f grid =====");
    println!("beta,f,N2,pos_idx,tr/N,HS2/N,bound_rank/N,bound_s1/N,in_band,nneg_rel1e10");
    let t = 300.0;
    let gwin = window(&gams1k, t);
    let n = gwin.len();
    let fs: [f64; 7] = [0.001, 0.002, 0.003, 0.004, 0.005, 0.01, 0.02];
    let betas: [f64; 4] = [0.05, 0.1, 0.3, 0.5];
    for &beta in &betas {
        for &f in &fs {
            let n2 = (f * n as f64).round() as usize;
            let removed = 2 * n2;
            let imb = beta * (n as f64) / t;
            let mut rng = SplitMix64::new(7);
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
            let mut atoms: Vec<Atom> = Vec::with_capacity(n);
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
            let w = build_w(&atoms, n, int_psi2);
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
            let br = (2.0 * tr - hs2) / n as f64;
            let bs1 = (4.0 * tr - hs2 - 2.0 * n as f64) / n as f64;
            let (eig, _) = jacobi_eig(&w);
            let lmax = eig.iter().cloned().fold(0.0_f64, f64::max);
            let nneg = eig.iter().filter(|&&x| x < -1e-10 * lmax).count();
            let pos = if n2 >= 1 {
                format!("({},{})", pick[0], pick[1])
            } else {
                "none".to_string()
            };
            println!(
                "{:.2},{:.4},{},{},{:.6},{:.6},{:.6},{:.6},{},{}",
                beta, f, n2, pos, trn, hsn, br, bs1, br >= band_min, nneg
            );
        }
    }

    println!("\n===== PROBE 2: top-clustered, T=300, bisect 1%-2% =====");
    println!("beta,f,N2,tr/N,HS2/N,bound_rank/N,bound_s1/N,in_band");
    for &beta in &[0.05, 0.1, 0.2, 0.3] {
        for &f in &[0.015, 0.025] {
            let n2 = (f * n as f64).round() as usize;
            let n1 = n - 2 * n2;
            let imb = beta * (n as f64) / t;
            let mut atoms: Vec<Atom> = Vec::with_capacity(n);
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
            let w = build_w(&atoms, n, int_psi2);
            let mut tr = 0.0;
            let mut hs2 = 0.0;
            for i in 0..n {
                tr += w[i][i];
                for j in 0..n {
                    hs2 += w[i][j] * w[i][j];
                }
            }
            let br = (2.0 * tr - hs2) / n as f64;
            let bs1 = (4.0 * tr - hs2 - 2.0 * n as f64) / n as f64;
            println!(
                "{:.2},{:.4},{},{:.6},{:.6},{:.6},{:.6},{}",
                beta, f, n2, tr / n as f64, hs2 / n as f64, br, bs1, br >= band_min
            );
        }
    }

    println!("\n===== PROBE 3: random-scattered (seed 7), T=500, coarse =====");
    let t500 = 500.0;
    let gwin5 = window(&gams1k, t500);
    let n5 = gwin5.len();
    println!("beta,f,N2,tr/N,HS2/N,bound_rank/N,bound_s1/N,in_band");
    for &beta in &[0.05, 0.3] {
        for &f in &[0.002, 0.005, 0.01] {
            let n2 = (f * n5 as f64).round() as usize;
            let removed = 2 * n2;
            let imb = beta * (n5 as f64) / t500;
            let mut rng = SplitMix64::new(7);
            let mut idx: Vec<usize> = (0..n5).collect();
            let mut pick = Vec::with_capacity(removed);
            for k in 0..removed {
                let j = k + (rng.next_u64() as usize) % (n5 - k);
                idx.swap(k, j);
                pick.push(idx[k]);
            }
            pick.sort_unstable();
            let mut is_pair = vec![false; n5];
            for k in 0..n2 {
                is_pair[pick[2 * k]] = true;
                is_pair[pick[2 * k + 1]] = true;
            }
            let mut atoms: Vec<Atom> = Vec::with_capacity(n5);
            let mut k = 0;
            while k + 1 < removed {
                let i0 = pick[k];
                let i1 = pick[k + 1];
                let gm = 0.5 * (gwin5[i0] + gwin5[i1]);
                let s = (gm - t500) * (n5 as f64) / t500;
                atoms.push(Atom::Pair { s, imb });
                k += 2;
            }
            for i in 0..n5 {
                if !is_pair[i] {
                    atoms.push(Atom::OnLine { s: (gwin5[i] - t500) * (n5 as f64) / t500 });
                }
            }
            let w = build_w(&atoms, n5, int_psi2);
            let mut tr = 0.0;
            let mut hs2 = 0.0;
            for i in 0..n5 {
                tr += w[i][i];
                for j in 0..n5 {
                    hs2 += w[i][j] * w[i][j];
                }
            }
            let br = (2.0 * tr - hs2) / n5 as f64;
            let bs1 = (4.0 * tr - hs2 - 2.0 * n5 as f64) / n5 as f64;
            println!(
                "{:.2},{:.4},{},{:.6},{:.6},{:.6},{:.6},{}",
                beta, f, n2, tr / n5 as f64, hs2 / n5 as f64, br, bs1, br >= band_min
            );
        }
    }
}
