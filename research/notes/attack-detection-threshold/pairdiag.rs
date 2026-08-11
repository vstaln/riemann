// pairdiag: position dependence of a single off-line pair's negative eigenvalue.
// Reproduces the attack-finitet §7 anchor (pair at gwin[0], gamma ~= 201.265, beta=0.3
// -> isolated M eigenvalues {+1.817579, -0.151694}, W units {+2.1403, -0.1786}), then
// measures lambda_min of the full W_T with ONE pair at three positions (bottom = first
// zero, bulk = middle zero, top = last two zeros) as a function of beta.
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

fn main() {
    let int_psi2 = psi2(C::real(0.0)).re;
    println!("int psi^2 = {:.15}", int_psi2);
    let gams = load_zeros("/home/vstaln/riemann/tools/data/zeros_1_1000.txt");
    let t = 200.0_f64;
    let gwin = window(&gams, t);
    let n = gwin.len();
    println!("T={:.0} N={}  window [200,400): first gamma = {:.3}, last gammas = {:.3}, {:.3}", t, n, gwin[0], gwin[n - 2], gwin[n - 1]);

    // positions (s-coordinates) for a single pair
    let pos = [
        ("bottom(first)", 0.0f64, 0.0f64), // filled below
        ("bulk(mid)", 0.0, 0.0),
        ("top(last2)", 0.0, 0.0),
    ];
    let s_bottom = (gwin[0] - t) * (n as f64) / t;
    let s_bulk = (gwin[n / 2] - t) * (n as f64) / t;
    let s_top = (0.5 * (gwin[n - 2] + gwin[n - 1]) - t) * (n as f64) / t;
    println!("s positions: bottom {:.4}, bulk {:.4}, top {:.4}", s_bottom, s_bulk, s_top);

    // ---- §7 anchor reproduction: isolated pair matrix at bottom, beta=0.3 ----
    let beta0 = 0.3_f64;
    let imb0 = beta0 * (n as f64) / t;
    for (name, s) in [("bottom", s_bottom), ("bulk", s_bulk), ("top", s_top)] {
        let mut a = vec![0.0; n];
        let mut b = vec![0.0; n];
        for k in 0..n {
            let w = psi(C::new(s - k as f64, imb0));
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
            "[isolated pair beta={:.1} {}] nonzero eig M: {:+.6}, {:+.6}  (W units: {:+.4}, {:+.4})",
            beta0, name, nz[nz.len() - 2], nz[nz.len() - 1],
            nz[nz.len() - 2] / int_psi2, nz[nz.len() - 1] / int_psi2
        );
        // full W with one pair at this position
        let mut atoms: Vec<Atom> = Vec::new();
        for i in 0..n {
            if name == "bottom" && i == 0 {
                continue;
            }
            if name == "bulk" && i == n / 2 {
                continue;
            }
            if name == "top" && i >= n - 2 {
                continue;
            }
            atoms.push(Atom::OnLine { s: (gwin[i] - t) * (n as f64) / t });
        }
        atoms.push(Atom::Pair { s, imb: imb0 });
        let w = build_w(&atoms, n, int_psi2);
        let (eig, _) = jacobi_eig(&w);
        let lmax = eig.iter().cloned().fold(0.0_f64, f64::max);
        let eigmin = eig.iter().cloned().fold(f64::INFINITY, f64::min);
        let nneg = eig.iter().filter(|&&x| x < -1e-10 * lmax).count();
        println!(
            "    full W min eig = {:+.6e}  (lmax {:.4}, nneg_rel1e10 = {})",
            eigmin, lmax, nneg
        );
    }

    // ---- beta sweep of lambda_min(full W, one pair) at each position ----
    println!("\nbeta sweep: lambda_min of full W with one pair (position x beta)");
    println!("beta,imb,bottom_min,bottom_nneg,bulk_min,bulk_nneg,top_min,top_nneg");
    for &beta in &[0.02, 0.05, 0.1, 0.2, 0.3, 0.5, 1.0] {
        let imb = beta * (n as f64) / t;
        let mut row = String::new();
        for (name, s) in [("bottom", s_bottom), ("bulk", s_bulk), ("top", s_top)] {
            let mut atoms: Vec<Atom> = Vec::new();
            for i in 0..n {
                if name == "bottom" && i == 0 {
                    continue;
                }
                if name == "bulk" && i == n / 2 {
                    continue;
                }
                if name == "top" && i >= n - 2 {
                    continue;
                }
                atoms.push(Atom::OnLine { s: (gwin[i] - t) * (n as f64) / t });
            }
            atoms.push(Atom::Pair { s, imb });
            let w = build_w(&atoms, n, int_psi2);
            let (eig, _) = jacobi_eig(&w);
            let lmax = eig.iter().cloned().fold(0.0_f64, f64::max);
            let eigmin = eig.iter().cloned().fold(f64::INFINITY, f64::min);
            let nneg = eig.iter().filter(|&&x| x < -1e-10 * lmax).count();
            row.push_str(&format!("{:.6e},{},", eigmin, nneg));
        }
        println!("{:.2},{:.4},{}", beta, imb, row);
    }
}
