// Zero-side Hilbert–Schmidt computation for a single character: builds the matrix
// G_{kl} = sum_rho phihat(gamma_rho - tau_k) phihat(gamma_rho - tau_l)  (paper (2.20))
// from the zeros, with the paper's tapered window (ramp profile rho(x)=x-sin(2pix)/(2pi),
// width w = eta L/2), and reports tr G, tr G^2, kappa = ||bG||^2_F/tr bG and
// C = (tr bG)^2/tr bG^2, bG = G/(a L^2), as in the paper's Sections 4-5 and 8.

use crate::em;
use crate::em::im_log_gamma;
use std::f64::consts::PI;

pub struct Window {
    pub l: f64,      // ell_{1,chi} = ln(qT/2pi) + 2ln2 - 1 (mean-spacing scale)
    pub lw: f64,     // ln(qT/2pi)
    pub lambda: f64, // bandwidth: L = lambda * l
    pub L: f64,      // window length
    pub w: f64,      // ramp width
    pub eta: f64,    // w = eta L/2
    pub a: f64,      // (1/L) int phi^2
    pub b: f64,      // (1/L) int phi^4
    pub h: f64,      // 2pi/L
    pub d: usize,    // number of Gabor channels
    pub x: f64,      // X = e^L
}

pub fn rho(x: f64) -> f64 {
    x - (2.0 * PI * x).sin() / (2.0 * PI)
}

/// phi(u) on [0, L/2]: 1 on [0, L/2-w], rho((L/2-u)/w) on [L/2-w, L/2]; even in u.
pub fn phi(u: f64, l: f64, w: f64) -> f64 {
    let u = u.abs();
    let half = l / 2.0;
    if u > half {
        return 0.0;
    }
    if u <= half - w {
        1.0
    } else {
        rho((half - u) / w)
    }
}

/// Fourier transform of the window, closed form. phihat(r) = 2 int_0^{L/2} phi(u) cos(ru) du.
pub fn phihat(r: f64, l: f64, w: f64) -> f64 {
    if r.abs() < 1e-9 {
        return l - w; // int phi = L - w
    }
    let half = l / 2.0;
    // first piece: [0, L/2 - w] constant 1
    let t1 = 2.0 * (r * (half - w)).sin() / r;
    // second piece: [L/2-w, L/2] with rho
    let a = r * half;
    let b = r * w;
    let b2 = b * b;
    let fourpi2 = 4.0 * PI * PI;
    // I1 = int_0^1 rho(x) cos(bx) dx, I2 = int_0^1 rho(x) sin(bx) dx
    let i1 = if b2 < 1e-9 {
        // limit: int x - x = 1/2 - 0
        0.5
    } else {
        (b * b.sin() + b.cos() - 1.0) / b2 - (1.0 - b.cos()) / (fourpi2 - b2)
    };
    let i2 = if b2 < 1e-9 {
        0.0
    } else {
        (b.sin() - b * b.cos()) / b2 + b.sin() / (fourpi2 - b2)
    };
    t1 + 2.0 * w * (a.cos() * i1 + a.sin() * i2)
}

/// int_0^1 rho(x)^k dx by Gauss–Legendre (32 pts) — smooth, exact to 1e-14.
fn rho_moment(k: u32) -> f64 {
    // Gauss-Legendre nodes/weights for n=16 on [-1,1]
    const X: [f64; 16] = [
        -0.9894009349916499, -0.9445750230732326, -0.8656312023878318, -0.7554044083550030,
        -0.6178762444026438, -0.4580167776572274, -0.2816035507792589, -0.09501250983763744,
        0.09501250983763744, 0.2816035507792589, 0.4580167776572274, 0.6178762444026438,
        0.7554044083550030, 0.8656312023878318, 0.9445750230732326, 0.9894009349916499,
    ];
    const W: [f64; 16] = [
        0.027152459411754095, 0.06225352393864789, 0.09515851168249278, 0.12462897125553387,
        0.14959598881657673, 0.16915651939500254, 0.18260341504492359, 0.18945061045506850,
        0.18945061045506850, 0.18260341504492359, 0.16915651939500254, 0.14959598881657673,
        0.12462897125553387, 0.09515851168249278, 0.06225352393864789, 0.027152459411754095,
    ];
    let mut s = 0.0;
    for i in 0..16 {
        let x = 0.5 * (X[i] + 1.0);
        let v = rho(x).powi(k as i32);
        s += W[i] * v;
    }
    0.5 * s
}

/// Build the window constants for the given q, T, lambda, eta.
pub fn window(q: u32, t: f64, lambda: f64, eta: f64) -> Window {
    let lw = (q as f64 * t / std::f64::consts::TAU).ln();
    let l = lw + 2.0 * (2.0f64).ln() - 1.0;
    let l_win = lambda * l;
    let w = eta * l_win / 2.0;
    let a = 1.0 - 2.0 * w / l_win + 2.0 * w / l_win * rho_moment(2);
    let b = 1.0 - 2.0 * w / l_win + 2.0 * w / l_win * rho_moment(4);
    let h = std::f64::consts::TAU / l_win;
    let d = (l_win * t / std::f64::consts::TAU).floor() as usize;
    Window {
        l,
        lw,
        lambda,
        L: l_win,
        w,
        eta,
        a,
        b,
        h,
        d,
        x: l_win.exp(),
    }
}

/// g(y) = int phi^2(u) phi^2(u+y) du, for y in [0, L]. Composite Simpson on the
/// overlap domain [-L/2, L/2 - y], subdivided at the ramp breakpoints.
pub fn g_of(y: f64, win: &Window) -> f64 {
    let l = win.L;
    let w = win.w;
    if y < 0.0 || y > l {
        return 0.0;
    }
    // breakpoints of u where phi^2 or phi^2(u+y) changes analytic piece:
    // phi^2(u): -L/2, -L/2+w, L/2-w, L/2 ; phi^2(u+y): -L/2-y, -L/2-y+w, L/2-w-y, L/2-y
    let mut pts = vec![
        -l / 2.0,
        -l / 2.0 + w,
        l / 2.0 - w,
        l / 2.0 - y,
        -l / 2.0 - y + w,
        l / 2.0 - y - w,
    ];
    pts.push(-l / 2.0);
    pts.push(l / 2.0 - y);
    pts.retain(|&u| u >= -l / 2.0 - 1e-12 && u <= l / 2.0 - y + 1e-12);
    pts.sort_by(|a, b| a.partial_cmp(b).unwrap());
    let mut total = 0.0;
    for i in 0..pts.len() - 1 {
        let (u0, u1) = (pts[i], pts[i + 1]);
        if u1 - u0 < 1e-12 {
            continue;
        }
        // Simpson with n=64 per piece
        let n = 64usize;
        let du = (u1 - u0) / n as f64;
        let f = |u: f64| phi(u, l, w).powi(2) * phi(u + y, l, w).powi(2);
        let mut s = f(u0) + f(u1);
        for j in 1..n {
            let u = u0 + j as f64 * du;
            s += if j % 2 == 0 { 2.0 } else { 4.0 } * f(u);
        }
        total += s * du / 3.0;
    }
    total
}

/// J_T = (2/L^3) sum_{n<=X, (n,q)=1} Lambda(n)^2/n * g(log n), the finite second-moment
/// constant (paper Remark 5.9; -> 1/3).
pub fn j_t(win: &Window, q: u32) -> f64 {
    let x = win.x;
    let mut sum = 0.0f64;
    // sieve primes up to X
    let lim = x.ceil() as usize;
    let mut is_prime = vec![true; lim + 1];
    if lim >= 0 {
        is_prime[0] = false;
    }
    if lim >= 1 {
        is_prime[1] = false;
    }
    let mut p = 2usize;
    while p * p <= lim {
        if is_prime[p] {
            let mut m = p * p;
            while m <= lim {
                is_prime[m] = false;
                m += p;
            }
        }
        p += 1;
    }
    // prime powers n = p^k <= X
    for p in 2..=lim {
        if !is_prime[p] {
            continue;
        }
        if (p as u32) % q == 0 {
            continue;
        }
        let lp = (p as f64).ln();
        let mut pk = p as f64;
        let mut k = 1u32;
        while pk <= x {
            // Lambda(n) = ln p ; n = pk
            let ln_n = pk.ln();
            sum += lp * lp / pk * g_of(ln_n, win);
            k += 1;
            pk *= p as f64;
            if pk > x {
                break;
            }
        }
    }
    2.0 / (win.L * win.L * win.L) * sum
}

/// Zero-side HS computation for one character. zeros: ordinates in the window range
/// (sorted). Returns (tr G, tr G^2, kappa, C).
pub fn hs_from_zeros(
    zeros: &[f64],
    win: &Window,
    t: f64,
    rv: f64,  // reach for V entries: |gamma - tau_k| <= rv*L
    rp: f64,  // pair reach: |gamma - gamma'| <= rp*L
) -> (f64, f64, f64, f64) {
    let l = win.L;
    let h = win.h;
    let d = win.d;
    if d == 0 {
        return (0.0, 0.0, 0.0, 0.0);
    }
    // For each zero, the list of (k, V) with |gamma - tau_k| <= rv*L
    let nz = zeros.len();
    // precompute channel index range
    let kmin_for = |g: f64| -> isize {
        ((g - rv * l - t) / h).floor() as isize
    };
    let kmax_for = |g: f64| -> isize {
        ((g + rv * l - t) / h).ceil() as isize
    };
    let mut tr_g = 0.0f64;
    let mut tr2_g = 0.0f64;
    // diagonal W_rho,rho = sum_k V^2
    let mut diag = vec![0.0f64; nz];
    // W_rho,rho' for pairs within rp*L
    // iterate rho' = j in increasing order; for each rho < j with |g_j - g_rho| <= rp*L
    for j in 0..nz {
        let gj = zeros[j];
        let (k0, k1) = (kmin_for(gj), kmax_for(gj));
        // k indices restricted to [0, d)
        let k0 = k0.max(0);
        let k1 = k1.min(d as isize - 1);
        if k0 > k1 {
            continue;
        }
        // diagonal
        let mut dsum = 0.0;
        for k in k0..=k1 {
            let v = phihat(gj - (t + k as f64 * h), l, win.w);
            dsum += v * v;
        }
        diag[j] = dsum;
        tr_g += dsum;
        // pairs with earlier zeros within rp*L
        let g0 = gj - rp * l;
        let mut i = j;
        while i > 0 && zeros[i - 1] >= g0 {
            i -= 1;
            let gi = zeros[i];
            let (i0, i1) = (kmin_for(gi).max(0), kmax_for(gi).min(d as isize - 1));
            let kk0 = k0.max(i0);
            let kk1 = k1.min(i1);
            if kk0 <= kk1 {
                let mut w = 0.0;
                for k in kk0..=kk1 {
                    let v1 = phihat(gi - (t + k as f64 * h), l, win.w);
                    let v2 = phihat(gj - (t + k as f64 * h), l, win.w);
                    w += v1 * v2;
                }
                tr2_g += 2.0 * w * w; // symmetric pair counted twice
            }
        }
    }
    // add diagonal squares
    for j in 0..nz {
        tr2_g += diag[j] * diag[j];
    }
    // bG = G/(a L^2)
    let norm = win.a * l * l;
    let tr_bg = tr_g / norm;
    let tr2_bg = tr2_g / (norm * norm);
    let kappa = tr2_bg / tr_bg;
    let c = tr_bg * tr_bg / tr2_bg;
    (tr_g, tr2_g, kappa, c)
}

/// The paper's finite-window prediction (Remark 5.9 / Theorem 5.8 taper factor):
/// kappa_pred = (b + lambda^2 J_T)/(a^2 lambda),  C_pred/N = lambda a^2/(b + lambda^2 J_T).
pub fn prediction(win: &Window, q: u32) -> (f64, f64) {
    let j = j_t(win, q);
    let lam = win.lambda;
    let kappa = (win.b + lam * lam * j) / (win.a * win.a * lam);
    let c_n = lam * win.a * win.a / (win.b + lam * lam * j);
    (kappa, c_n)
}

/// Riemann–von Mangoldt count for N_chi(T1, T2): the phase-function formula
/// (T/2pi) ln(q/pi) + (1/pi) Im ln Gamma(1/4 + iT/2), differenced, + O(log qT).
pub fn rvm_main(q: u32, t1: f64, t2: f64) -> f64 {
    let f = |t: f64| -> f64 {
        t * (q as f64 / PI).ln() / std::f64::consts::TAU + im_log_gamma(0.25, t / 2.0) / PI
    };
    f(t2) - f(t1)
}
