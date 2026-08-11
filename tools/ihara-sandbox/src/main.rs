// ihara-sandbox: G1 — run the two-moment (Weil-form) certificate pipeline on the
// Ihara zeta of small regular graphs, where RH is PROVEN (zeros on |u| = 1/sqrt q
// iff the graph is Ramanujan) and everything is finite and exact.
//
// Pipeline port (exactly the tools/finitet pipeline, verified to reproduce it):
//   zeros of Z_G(u): nontrivial roots of det(I - A u + q u^2), q = d-1 (d = degree),
//   one conjugate pair per nontrivial eigenvalue lambda:  u = (lambda +- i sqrt(4q - lambda^2))/(2q),
//   angle theta = arccos(lambda/(2 sqrt q)) in (0, pi)  [pair -> one angle]
//   unit-density rescaling:  s_i = theta_i * N / pi   (N = # nontrivial eigenvalues)
//   V[i][k] = psi(s_i - k),  k = 0..N-1;   W = V^T V / int_psi2
//   tr W/N, ||W||^2_HS/N, rank, certificate = (2 tr - HS^2)/N
// The exact number of zeros on the circle is s1 = N (all graphs below are Ramanujan),
// so the certificate is a valid lower bound iff certificate <= 1 (checked).
//
// Same kernel as finitet: psi(u) = cos(sqrt2 u) 1_{|u|<=1/2},
//   Psi(s) = sin(1/sqrt2 - pi s)/(sqrt2 - 2 pi s) + sin(1/sqrt2 + pi s)/(sqrt2 + 2 pi s)
//   Psi2(s) = sin(pi s)/(2 pi s) + 1/4[ sin(sqrt2 - pi s)/(sqrt2 - pi s) + sin(sqrt2 + pi s)/(sqrt2 + pi s) ]
//   int psi^2 = 1/2 + sin(sqrt2)/(2 sqrt2) = 0.849227999318304
// Reference constants: c_hs = 1/2 + (1/sqrt2)cot(1/sqrt2) = 1.327499296320588;
//   bound const = 3/2 - (1/sqrt2)cot(1/sqrt2) = 0.672500703679412 (Thm D / Lemma 3.4);
//   ceiling p0 = 0.6818286874638 (attack-ceiling.md, the near-CUE law simple-point fraction).

use std::f64::consts::{FRAC_1_SQRT_2, PI, SQRT_2};

// ---------- kernel (identical to tools/finitet; verified to reproduce its numbers) ----------
fn psi(s: f64) -> f64 {
    let d1 = SQRT_2 - 2.0 * PI * s;
    let d2 = SQRT_2 + 2.0 * PI * s;
    let mut t1 = (FRAC_1_SQRT_2 - PI * s).sin() / d1;
    if d1.abs() < 1e-12 {
        t1 = 0.5;
    }
    let mut t2 = (FRAC_1_SQRT_2 + PI * s).sin() / d2;
    if d2.abs() < 1e-12 {
        t2 = 0.5;
    }
    t1 + t2
}

fn psi2(s: f64) -> f64 {
    let ps = PI * s;
    let mut t1 = ps.sin() / (2.0 * ps);
    if ps.abs() < 1e-12 {
        t1 = 0.5;
    }
    let a = SQRT_2 - ps;
    let b = SQRT_2 + ps;
    let mut t2 = a.sin() / a;
    if a.abs() < 1e-12 {
        t2 = 1.0;
    }
    let mut t3 = b.sin() / b;
    if b.abs() < 1e-12 {
        t3 = 1.0;
    }
    t1 + 0.25 * (t2 + t3)
}

fn int_psi2() -> f64 {
    0.5 + SQRT_2.sin() / (2.0 * SQRT_2)
}

// ---------- Jacobi eigenvalues (copy of the finitet routine) ----------
fn jacobi_eig(a0: &[Vec<f64>]) -> Vec<f64> {
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
    (0..n).map(|i| a[i][i]).collect()
}

// ---------- graph builders ----------
fn complete(n: usize) -> Vec<Vec<f64>> {
    let mut a = vec![vec![0.0; n]; n];
    for i in 0..n {
        for j in 0..n {
            if i != j {
                a[i][j] = 1.0;
            }
        }
    }
    a
}

fn cube_q3() -> Vec<Vec<f64>> {
    // vertices {0,1}^3, edge iff Hamming distance 1
    let n = 8;
    let mut a = vec![vec![0.0; n]; n];
    for x in 0..n {
        for y in 0..n {
            if (x ^ y).count_ones() == 1 {
                a[x][y] = 1.0;
            }
        }
    }
    a
}

fn cube_q4() -> Vec<Vec<f64>> {
    // vertices {0,1}^4, edge iff Hamming distance 1
    let n = 16;
    let mut a = vec![vec![0.0; n]; n];
    for x in 0..n {
        for y in 0..n {
            if (x ^ y).count_ones() == 1 {
                a[x][y] = 1.0;
            }
        }
    }
    a
}

fn petersen() -> Vec<Vec<f64>> {
    // vertices = 2-subsets of {1..5}; edge iff disjoint
    let mut sets: Vec<(u32, u32)> = Vec::new();
    for i in 0..5u32 {
        for j in (i + 1)..5 {
            sets.push((i, j));
        }
    }
    let n = sets.len();
    let mut a = vec![vec![0.0; n]; n];
    for x in 0..n {
        for y in 0..n {
            if sets[x].0 != sets[y].0
                && sets[x].0 != sets[y].1
                && sets[x].1 != sets[y].0
                && sets[x].1 != sets[y].1
            {
                a[x][y] = 1.0;
            }
        }
    }
    a
}

fn clebsch() -> Vec<Vec<f64>> {
    // vertices = F_2^4; edge iff x^y has popcount 1 or 4
    let n = 16;
    let mut a = vec![vec![0.0; n]; n];
    for x in 0..n {
        for y in 0..n {
            let d = (x ^ y).count_ones();
            if d == 1 || d == 4 {
                a[x][y] = 1.0;
            }
        }
    }
    a
}

fn icosahedron() -> Vec<Vec<f64>> {
    // pentagonal antiprism + two poles
    // 0..4 ring A, 5..9 ring B, 10 = P, 11 = Q
    let n = 12;
    let mut a = vec![vec![0.0; n]; n];
    let mut add = |i: usize, j: usize, a: &mut Vec<Vec<f64>>| {
        a[i][j] = 1.0;
        a[j][i] = 1.0;
    };
    for i in 0..5 {
        add(i, (i + 1) % 5, &mut a); // A ring
        add(5 + i, 5 + ((i + 1) % 5), &mut a); // B ring
        add(i, 5 + i, &mut a); // antiprism A_i - B_i
        add(i, 5 + ((i + 4) % 5), &mut a); // antiprism A_i - B_{i-1}
        add(10, i, &mut a); // pole P - all A
        add(11, 5 + i, &mut a); // pole Q - all B
    }
    a
}

fn hoffman_singleton() -> Vec<Vec<f64>> {
    // vertices (i,j,t): i in Z5, j in Z5, t in {0,1}; index = t*25 + i*5 + j
    // t=0 layer: (i,j) ~ (i, j+-1); t=1 layer: (i,j) ~ (i, j+-2)
    // cross: (i,j,0) ~ (k,l,1) iff l = j + i*k (mod 5)   [variant B]
    let n = 50;
    let idx = |t: usize, i: usize, j: usize| t * 25 + i * 5 + j;
    let mut a = vec![vec![0.0; n]; n];
    let mut add = |i: usize, j: usize, a: &mut Vec<Vec<f64>>| {
        if i != j {
            a[i][j] = 1.0;
            a[j][i] = 1.0;
        }
    };
    for i in 0..5 {
        for j in 0..5 {
            add(idx(0, i, j), idx(0, i, (j + 1) % 5), &mut a);
            add(idx(0, i, j), idx(0, i, (j + 4) % 5), &mut a);
            add(idx(1, i, j), idx(1, i, (j + 2) % 5), &mut a);
            add(idx(1, i, j), idx(1, i, (j + 3) % 5), &mut a);
            for k in 0..5 {
                let l = (j + i * k) % 5;
                add(idx(0, i, j), idx(1, k, l), &mut a);
            }
        }
    }
    a
}

fn random_regular(v: usize, d: usize, seed: u64) -> Vec<Vec<f64>> {
    // configuration model with rejection (simple graph required)
    let mut rng = SplitMix64::new(seed);
    loop {
        // stubs: vertex v appears d times; shuffle positions
        let mut stubs: Vec<usize> = Vec::with_capacity(v * d);
        for i in 0..v {
            for _ in 0..d {
                stubs.push(i);
            }
        }
        // Fisher-Yates
        for k in (1..stubs.len()).rev() {
            let j = (rng.next_u64() as usize) % (k + 1);
            stubs.swap(k, j);
        }
        let mut a = vec![vec![0.0; v]; v];
        let mut ok = true;
        let mut pairs = 0;
        for k in (0..stubs.len()).step_by(2) {
            let (x, y) = (stubs[k], stubs[k + 1]);
            if x == y {
                ok = false;
                break;
            }
            if a[x][y] != 0.0 {
                ok = false;
                break;
            }
            a[x][y] = 1.0;
            a[y][x] = 1.0;
            pairs += 1;
        }
        if ok && pairs * 2 == stubs.len() {
            return a;
        }
    }
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

// ---------- spectrum verification ----------
// returns (eigenvalues sorted desc, ok) after checking against `expected` (sorted desc)
fn spectrum(a: &[Vec<f64>], expected: &[f64]) -> (Vec<f64>, bool) {
    let mut eig = jacobi_eig(a);
    eig.sort_by(|x, y| y.partial_cmp(x).unwrap());
    let ok = expected
        .iter()
        .zip(eig.iter())
        .all(|(e, g)| (e - g).abs() < 1e-7);
    (eig, ok)
}

fn n_components(a: &[Vec<f64>]) -> usize {
    let n = a.len();
    let mut seen = vec![false; n];
    let mut comps = 0;
    for start in 0..n {
        if seen[start] {
            continue;
        }
        comps += 1;
        let mut stack = vec![start];
        seen[start] = true;
        while let Some(u) = stack.pop() {
            for v in 0..n {
                if a[u][v] != 0.0 && !seen[v] {
                    seen[v] = true;
                    stack.push(v);
                }
            }
        }
    }
    comps
}

// ---------- the two-moment pipeline ----------
fn measure(tag: &str, s: &[f64], truth_s1: Option<f64>, int2: f64) {
    let n = s.len();
    if n == 0 {
        println!("{tag}: N=0 (skip)");
        return;
    }
    // V[i][k] = psi(s_i - k)
    let mut v = vec![vec![0.0; n]; n];
    for i in 0..n {
        for k in 0..n {
            v[i][k] = psi(s[i] - k as f64);
        }
    }
    // W = V^T V / int2
    let mut w = vec![vec![0.0; n]; n];
    for k in 0..n {
        for k2 in 0..n {
            let mut x = 0.0;
            for i in 0..n {
                x += v[i][k] * v[i][k2];
            }
            w[k][k2] = x / int2;
        }
    }
    let tr: f64 = (0..n).map(|k| w[k][k]).sum();
    let hs2: f64 = w.iter().map(|row| row.iter().map(|x| x * x).sum::<f64>()).sum();
    // analytic prediction of the off-diagonal part (continuum; full Psi2, no grid truncation)
    let mut off_an = 0.0_f64;
    for i in 0..n {
        for j in 0..n {
            if i != j {
                let x = psi2(s[i] - s[j]) / int2;
                off_an += x * x;
            }
        }
    }
    let hs2_an = (n as f64 + off_an) / n as f64;
    // rank via Jacobi
    let eig = jacobi_eig(&w);
    let lmax = eig.iter().cloned().fold(0.0_f64, f64::max);
    let rank = eig.iter().filter(|&&x| x > 1e-6 * lmax).count();
    let npos = eig.iter().filter(|&&x| x > 1e-10 * lmax).count();
    let nneg = eig.iter().filter(|&&x| x < -1e-10 * lmax).count();
    let bound = 2.0 * tr - hs2;
    let trn = tr / n as f64;
    let hsn = hs2 / n as f64;
    let boundn = bound / n as f64;
    let s1 = truth_s1.unwrap_or(1.0);
    let valid = if boundn <= s1 + 1e-9 { "OK" } else { "VIOLATION" };
    println!(
        "{tag:>28} | N={n:3} | tr/N={trn:.6} | HS2/N={hsn:.6} | HS2_an/N={hs2_an:.6} | bound/N={boundn:+.6} | d_0.6725={:+.6} d_0.6818={:+.6} | rank={rank:3} n+/n-={npos}/{nneg} | truth s1/N={s1:.4} {valid}",
        boundn - 0.672500703679412,
        boundn - 0.6818286874638
    );
}

// ---------- theory curve: pair-correlation-law predictions of the certificate ----------
fn theory(int2: f64) {
    // c(g) = 1 + (1/int2)^2 * int_0^inf g(u) Psi2(u)^2 du  (even integrand -> 2*int_0^inf)
    // g_GUE = 1 - sinc^2(pi u); g_pois = 1; g_lat = sum_{m != 0} delta(u - m)
    let a = 0.0_f64;
    let b = 400.0_f64;
    let m = 800_000usize; // step 5e-4
    let h = (b - a) / m as f64;
    let mut igue = 0.0_f64;
    let mut ipois = 0.0_f64;
    for k in 0..=m {
        let u = a + h * k as f64;
        let w = if k == 0 || k == m { 1.0 } else if k % 2 == 1 { 4.0 } else { 2.0 };
        let p2 = psi2(u);
        let p2s = p2 * p2;
        let ggue = if u < 1e-12 { 0.0 } else { 1.0 - (PI * u).sin().powi(2) / (PI * u).powi(2) };
        igue += w * p2s * ggue;
        ipois += w * p2s;
    }
    igue *= h / 3.0;
    ipois *= h / 3.0;
    // lattice sum over integers
    let mut slat = 0.0_f64;
    for m1 in 1..2000i64 {
        let x = psi2(m1 as f64) / int2;
        slat += x * x;
    }
    let cgue = 1.0 + 2.0 * igue / (int2 * int2);
    let cpois = 1.0 + 2.0 * ipois / (int2 * int2);
    let clat = 1.0 + 2.0 * slat;
    println!("theory: c_GUE = {:.9} -> cert 2-c = {:.6}", cgue, 2.0 - cgue);
    println!("theory: c_pois = {:.9} -> cert 2-c = {:.6}", cpois, 2.0 - cpois);
    println!("theory: c_lat  = {:.9} -> cert 2-c = {:.6}", clat, 2.0 - clat);
    println!("paper:  c_hs = 1.327499296320588 -> cert 0.672500703679412");
    println!("ceiling p0 = 0.6818286874638");
}

fn main() {
    let int2 = int_psi2();
    println!("int psi^2 = {int2:.15}");
    println!("c_hs = 1.327499296320588 | bound const = 0.672500703679412 | ceiling p0 = 0.6818286874638");
    println!("");

    // ---------- 0. fidelity: reproduce finitet on the zeta worlds ----------
    println!("===== 0. FIDELITY (must reproduce finitet / attack-sandbox numbers) =====");
    let gams: Vec<f64> = std::fs::read_to_string("/home/vstaln/riemann/tools/data/zeros_1_1000.txt")
        .expect("zeros file")
        .lines()
        .filter_map(|l| {
            let p: Vec<&str> = l.split_whitespace().collect();
            if p.len() >= 2 {
                p[1].parse().ok()
            } else {
                None
            }
        })
        .collect();
    for &t in &[200.0_f64, 500.0] {
        let gwin: Vec<f64> = gams.iter().copied().filter(|&g| g >= t && g < 2.0 * t).collect();
        let n = gwin.len();
        let s: Vec<f64> = gwin.iter().map(|&g| (g - t) * (n as f64) / t).collect();
        measure(&format!("zeta-real T={t:.0}"), &s, Some(1.0), int2);
    }
    for &n in &[122usize, 379] {
        let s: Vec<f64> = (0..n).map(|k| k as f64 + 0.5).collect();
        measure(&format!("lattice N={n}"), &s, Some(1.0), int2);
    }
    for &n in &[122usize, 379] {
        let mut rng = SplitMix64::new(1);
        let s: Vec<f64> = (0..n).map(|_| rng.next_f64() * n as f64).collect();
        measure(&format!("poisson N={n}"), &s, Some(1.0), int2);
    }
    for &n in &[122usize, 379] {
        let mut rng = SplitMix64::new(42);
        let s: Vec<f64> = (0..n)
            .map(|k| k as f64 + 0.5 + (2.0 * rng.next_f64() - 1.0) * 0.2)
            .collect();
        measure(&format!("jitter N={n}"), &s, Some(1.0), int2);
    }
    println!("");

    // ---------- theory curve ----------
    println!("===== 1. THEORY: what the certificate predicts per pair-correlation law =====");
    theory(int2);
    println!("");

    // ---------- 2. Ihara graphs ----------
    println!("===== 2. IHARA ZEROS of Ramanujan graphs (RH PROVEN; zeros on |u|=1/sqrt q) =====");
    struct G {
        name: &'static str,
        d: usize,       // degree
        expected: Vec<f64>,
    }
    let graphs = [
        G { name: "K4", d: 3, expected: vec![3.0, -1.0, -1.0, -1.0] },
        G { name: "K5", d: 4, expected: vec![4.0, -1.0, -1.0, -1.0, -1.0] },
        G { name: "K8", d: 7, expected: vec![7.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0] },
        G { name: "Petersen", d: 3, expected: vec![3.0, 1.0, 1.0, 1.0, 1.0, 1.0, -2.0, -2.0, -2.0, -2.0] },
        G { name: "CubeQ3", d: 3, expected: vec![3.0, 1.0, 1.0, 1.0, -1.0, -1.0, -1.0, -3.0] },
        G { name: "Clebsch", d: 5, expected: {
            let mut e = vec![5.0];
            e.extend(std::iter::repeat(1.0).take(10));
            e.extend(std::iter::repeat(-3.0).take(5));
            e
        } },
        G { name: "Icosa", d: 5, expected: {
            let s5 = 5.0_f64.sqrt();
            let mut e = vec![5.0];
            e.extend(std::iter::repeat(s5).take(3));
            e.extend(std::iter::repeat(-1.0).take(5));
            e.extend(std::iter::repeat(-s5).take(3));
            e
        } },
        G { name: "Q4", d: 4, expected: {
            let mut e = vec![4.0];
            e.extend(std::iter::repeat(2.0).take(4));
            e.extend(std::iter::repeat(0.0).take(6));
            e.extend(std::iter::repeat(-2.0).take(4));
            e.push(-4.0);
            e
        } },
        G { name: "Hoffman-Singleton", d: 7, expected: {
            let mut e = vec![7.0];
            e.extend(std::iter::repeat(2.0).take(28));
            e.extend(std::iter::repeat(-3.0).take(21));
            e
        } },
    ];
    let builders: Vec<Box<dyn Fn() -> Vec<Vec<f64>>>> = vec![
        Box::new(|| complete(4)),
        Box::new(|| complete(5)),
        Box::new(|| complete(8)),
        Box::new(petersen),
        Box::new(cube_q3),
        Box::new(clebsch),
        Box::new(icosahedron),
        Box::new(cube_q4),
        Box::new(hoffman_singleton),
    ];
    for (g, b) in graphs.iter().zip(builders.iter()) {
        let a = b();
        let (eig, ok) = spectrum(&a, &g.expected);
        let q = (g.d - 1) as f64;
        // Ramanujan check: |lambda| <= 2 sqrt(d-1) for all non-Perron, non-bipartite-trivial
        let nontriv: Vec<f64> = eig
            .iter()
            .copied()
            .filter(|&l| (l - g.d as f64).abs() > 1e-9 && (l + g.d as f64).abs() > 1e-9)
            .collect();
        let ram_max = nontriv.iter().map(|&l| l.abs()).fold(f64::MIN, f64::max);
        let bound_ab = 2.0 * ((g.d - 1) as f64).sqrt();
        let ram_ok = ram_max <= bound_ab + 1e-9;
        // angles
        let theta: Vec<f64> = nontriv.iter().map(|&l| (l / (2.0 * q.sqrt())).acos()).collect();
        let n = theta.len();
        let s: Vec<f64> = theta.iter().map(|&t| t * (n as f64) / PI).collect();
        // verify Ihara-RH: the two roots u of q u^2 - lambda u + 1 = 0 satisfy |u| = 1/sqrt q
        let mut max_err = 0.0_f64;
        for &l in &nontriv {
            let disc = 4.0 * q - l * l;
            let re = l / (2.0 * q);
            let im = if disc >= 0.0 { disc.sqrt() / (2.0 * q) } else { 0.0 };
            let r2 = re * re + im * im;
            max_err = max_err.max((r2 - 1.0 / q).abs());
        }
        println!(
            "graph {:<18} d={} V={} | spectrum verified: {} | Ramanujan (|lambda|<=2sqrt(d-1)={:.3}): max|nontriv|={:.3} {} | #angles N={} | Ihara-RH |u|=1/sqrt q err={:.1e}",
            g.name,
            g.d,
            a.len(),
            if ok { "YES" } else { "NO" },
            bound_ab,
            ram_max,
            if ram_ok { "YES" } else { "NO" },
            n,
            max_err
        );
        if !ok {
            let e: Vec<String> = eig.iter().map(|x| format!("{:.4}", x)).collect();
            println!("    actual spectrum: {}", e.join(" "));
            let cc = n_components(&a);
            println!("    connected components: {cc}");
        }
        measure(g.name, &s, Some(1.0), int2);
    }
    println!("");

    // ---------- 3. generic random regular graph (Alon-Boppana-saturated end) ----------
    println!("===== 3. RANDOM REGULAR graph (near-Ramanujan; a few zeros slightly off the circle) =====");
    for &(v, d, seed) in &[(200usize, 4usize, 7u64), (120, 5, 11)] {
        let a = random_regular(v, d, seed);
        let comps = n_components(&a);
        let mut eig = jacobi_eig(&a);
        eig.sort_by(|x, y| y.partial_cmp(x).unwrap());
        let q = (d - 1) as f64;
        let circ = 2.0 * q.sqrt();
        let deg: usize = (0..v).map(|i| a[0][i] as usize).sum();
        let nontriv: Vec<f64> = eig
            .iter()
            .copied()
            .filter(|&l| (l - d as f64).abs() > 1e-9 && (l + d as f64).abs() > 1e-9)
            .collect();
        let on_circ: Vec<f64> = nontriv.iter().copied().filter(|&l| l.abs() <= circ + 1e-9).collect();
        let off_circ = nontriv.len() - on_circ.len();
        let theta: Vec<f64> = on_circ.iter().map(|&l| (l / (2.0 * q.sqrt())).acos()).collect();
        let n = theta.len();
        let s: Vec<f64> = theta.iter().map(|&t| t * (n as f64) / PI).collect();
        let mut dmin = f64::MAX;
        let mut near = 0usize;
        for i in 0..n {
            for j in (i + 1)..n {
                let dd = (s[i] - s[j]).abs();
                if dd < dmin {
                    dmin = dd;
                }
                if dd < 0.5 {
                    near += 1;
                }
            }
        }
        let edge = s.iter().filter(|&&x| x < 1.0 || x > n as f64 - 1.0).count();
        // histogram of s-values in 10 bins + min eigenvalue gap
        let mut hist = [0usize; 10];
        for &x in &s {
            let b = ((x / n as f64) * 10.0) as usize;
            hist[b.min(9)] += 1;
        }
        let mut mingap = f64::MAX;
        for w in nontriv.windows(2) {
            let gap = (w[0] - w[1]).abs();
            if gap > 1e-9 && gap < mingap {
                mingap = gap;
            }
        }
        println!(
            "random {}-regular V={} seed={} | components={} deg check: {} | V'={} nontriv, {} on-circle, {} off-circle | lambda2={:.4} (2 sqrt q = {:.4}) | min s-sep={:.4} pairs<0.5={} edge-s={} min-lambda-gap={:.6} | s-hist: {:?}",
            d, v, seed, comps, deg == d, nontriv.len(), on_circ.len(), off_circ, eig[1], circ, dmin, near, edge, mingap, hist
        );
        let truth = on_circ.len() as f64 / (nontriv.len() as f64);
        measure(&format!("rand d={d} V={v}"), &s, Some(truth), int2);
    }
}
