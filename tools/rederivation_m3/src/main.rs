// rederivation_m3: independent per-config check of m3 >= m2^2 for the marked
// zero-law on the 256-lattice. Kernel G = K^2, K(x)=sinc^2(pi*B*x), B=128.
// m2 = (N/M) sum_k kk[k] |muhat(k)|^2, m3 = (N^2/M) sum_i m_i (G*mu)(x_i)^2
// Theorem: m3 - m2^2 = N^2 M^2 ( ||T1||^2_nu - <1,T1>^2_nu ) >= 0 by Cauchy-Schwarz.
use std::f64::consts::PI;

const N: usize = 256;
const B: usize = 128;

fn sinc(x: f64) -> f64 {
    if x.abs() < 1e-12 { 1.0 } else { x.sin() / x }
}

fn khat_spectrum() -> Vec<f64> {
    let mut kh = vec![0.0f64; N];
    for m in 0..N {
        let mut s = 0.0;
        for i in 0..N {
            let x = i as f64 / N as f64;
            let k = sinc(PI * B as f64 * x).powi(2);
            s += k * (2.0 * PI * m as f64 * x).cos();
        }
        kh[m] = s / N as f64;
    }
    kh
}

fn conv_circ(kh: &[f64]) -> Vec<f64> {
    let mut kk = vec![0.0f64; N];
    for k in 0..N {
        let mut s = 0.0;
        for m in 0..N {
            let j = (k + N - m) % N;
            s += kh[m] * kh[j];
        }
        kk[k] = s;
    }
    kk
}

struct Rng(u64);
impl Rng {
    fn next(&mut self) -> f64 {
        self.0 ^= self.0 << 13; self.0 ^= self.0 >> 7; self.0 ^= self.0 << 17;
        (self.0 >> 11) as f64 / (1u64 << 53) as f64
    }
}

fn gen_marks(p1: f64, law_b: bool, rng: &mut Rng) -> Vec<f64> {
    let q = if law_b { 2.0 * p1 / (1.0 + p1) } else { p1 };
    (0..N).map(|_| if rng.next() < q { 1.0 } else { 2.0 }).collect()
}

// complex DFT (naive, N=256)
fn dft(m: &[f64]) -> (Vec<f64>, Vec<f64>) {
    let (mut re, mut im) = (vec![0.0f64; N], vec![0.0f64; N]);
    for k in 0..N {
        for j in 0..N {
            let a = 2.0 * PI * k as f64 * j as f64 / N as f64;
            re[k] += m[j] * a.cos(); im[k] -= m[j] * a.sin();
        }
    }
    (re, im)
}

// per-config moments via Fourier (lattice); returns (m2, m3, slack)
fn moments(m: &[f64], kk: &[f64]) -> (f64, f64, f64) {
    let msum: f64 = m.iter().sum();
    let (mre, mim) = dft(m);
    let mut t2 = 0.0;
    for k in 0..N { t2 += kk[k] * (mre[k] * mre[k] + mim[k] * mim[k]); }
    // gmu_i = sum_k kk[k] * muhat(k) * e^{2pi i k x_i}
    let mut gmu = vec![0.0f64; N];
    for i in 0..N {
        let mut s = 0.0;
        for k in 0..N {
            let a = 2.0 * PI * k as f64 * i as f64 / N as f64;
            s += kk[k] * (mre[k] * a.cos() - mim[k] * a.sin());
        }
        gmu[i] = s;
    }
    let t3: f64 = (0..N).map(|i| m[i] * gmu[i] * gmu[i]).sum();
    let m2 = (N as f64 / msum) * t2;
    let m3 = (N as f64 * N as f64 / msum) * t3;
    (m2, m3, m3 - m2 * m2)
}

fn main() {
    let kk = conv_circ(&khat_spectrum());
    let mut rng = Rng(0x9E3779B97F4A7C15);
    println!("=== rederivation_m3: per-config m3 >= m2^2 (256-lattice, G=sinc^4, B=128) ===");
    println!("law  p1      worst m3-m2^2 (6 configs)   verdict");
    let mut all_pass = true;
    for (law_b, tag) in [(false, "A"), (true, "B")] {
        for p1 in [0.10f64, 0.40, 0.6818287, 0.90] {
            let mut worst = f64::INFINITY;
            let mut last = (0.0f64, 0.0f64, 0.0f64);
            for _ in 0..6 {
                let m = gen_marks(p1, law_b, &mut rng);
                last = moments(&m, &kk);
                if last.2 < worst { worst = last.2; }
            }
            let ok = worst >= -1e-9;
            all_pass &= ok;
            println!("{}   {:.4}   {:+.3e} (m2={:.4}, m3={:.4})   {}", tag, p1, worst, last.0, last.1,
                if ok { "PASS" } else { "FAIL" });
        }
    }
    // extremal: uniform marks => nu uniform => T1 constant => equality m3 = m2^2
    let m: Vec<f64> = vec![2.0; N];
    let (m2, m3, sl) = moments(&m, &kk);
    println!("\nuniform marks (m_j=2): m2={:.6}, m3={:.6}, m3-m2^2={:+.2e}  [{}]", m2, m3, sl,
        if sl.abs() < 1e-6 { "EQUALITY (extremal case)" } else { "not equality" });

    // control: RAW mark moments fail; mean-1 Y holds (both laws)
    println!("\n=== control: raw mark moments vs mean-1 mark variable ===");
    for (law_b, tag) in [(false, "A"), (true, "B")] {
        for p1 in [0.10f64, 0.50, 0.6818287] {
            let (em, em2, em3) = if law_b {
                (2.0 / (1.0 + p1), (4.0 - 2.0 * p1) / (1.0 + p1), (8.0 - 6.0 * p1) / (1.0 + p1))
            } else {
                (2.0 - p1, 4.0 - 3.0 * p1, 8.0 - 7.0 * p1)
            };
            let raw = em3 - em2 * em2;
            let ey2 = em2 / (em * em); let ey3 = em3 / (em * em * em);
            let y = ey3 - ey2 * ey2;
            println!("  law {} p1={:.4}: raw m3-(m2)^2 = {:+.4} [{}] | mean-1 Y: {:+.4e} [{}]",
                tag, p1, raw, if raw < 0.0 { "FAIL as expected" } else { "UNEXPECTED" },
                y, if y >= -1e-12 { "HOLDS" } else { "FAILS" });
        }
    }

    // RH-inert control: random positions (not the lattice) — same inequality
    let m: Vec<f64> = gen_marks(0.5, true, &mut rng);
    let msum: f64 = m.iter().sum();
    let mut worst = f64::INFINITY;
    for _ in 0..4 {
        let pos: Vec<f64> = (0..N).map(|_| rng.next()).collect();
        let mut gmu = vec![0.0f64; N];
        let mut t2 = 0.0;
        for i in 0..N { for j in 0..N {
            let d = (pos[i] - pos[j]).abs().min(1.0 - (pos[i] - pos[j]).abs());
            let g = sinc(PI * B as f64 * d).powi(4);
            gmu[i] += g * m[j]; t2 += m[i] * m[j] * g;
        }}
        let t3: f64 = (0..N).map(|i| m[i] * gmu[i] * gmu[i]).sum();
        let m2 = (N as f64 / msum) * t2;
        let m3 = (N as f64 * N as f64 / msum) * t3;
        if m3 - m2 * m2 < worst { worst = m3 - m2 * m2; }
    }
    println!("\nrandom-position control (positions arbitrary, marks law B): worst m3-m2^2 = {:+.2e} [{}]",
        worst, if worst >= -1e-9 { "PASS — theorem position-blind (RH-inert)" } else { "FAIL" });
    println!("\nOVERALL: {}", if all_pass { "ALL CONFIGS PASS: m3 >= m2^2 CONFIRMED" } else { "SOME CONFIG FAILED" });
}
