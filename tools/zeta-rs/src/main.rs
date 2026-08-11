// zeta-rs — fast numerical verification toolkit for the 67.25% argument.
// Everything is f64. Subcommands:
//   constant   — verify 3/2-(1/sqrt2)cot(1/sqrt2) and the psi variational identity
//   zeros N    — compute the first N zeros of zeta on the critical line via
//                Euler-Maclaurin Z(t) + bracketing/Newton (independent of LMFDB)
//   bracket    — verify cached LMFDB zeros are bracketed sign changes of Z(t)
//   explicit   — verify the Guinand-Weil explicit formula on a Gaussian test fn
//   paircorr N — empirical Montgomery pair-correlation form factor from zeros
//   ranktrace  — brute-force Lemma 3.4 (rank-trace inequality) on random matrices
//   mv         — Montgomery-Vaughan / Hilbert inequality sanity check
//
// Data files: tools/data/zeros_<a>_<b>.txt ("n gamma" lines, 34 digits, LMFDB).
// Compute discipline: this is the ONLY heavy compute; results are cached in
// tools/data/ and reports go to research/notes/.

use std::env;
use std::fs;
use std::path::PathBuf;

mod checks;
mod zeta;

fn main() {
    let args: Vec<String> = env::args().collect();
    let cmd = args.get(1).map(|s| s.as_str()).unwrap_or("help");
    let data_dir = PathBuf::from(env::var("ZETA_DATA")
        .unwrap_or_else(|_| "../data".into()));
    match cmd {
        "constant" => checks::constant(),
        "zeros" => {
            let n: usize = args.get(2).and_then(|s| s.parse().ok()).unwrap_or(1000);
            let gs = zeta::find_zeros(n);
            let out = data_dir.join(format!("zeros_computed_{}.txt", n));
            let mut s = String::new();
            for (i, g) in gs.iter().enumerate() {
                s.push_str(&format!("{} {:.34}\n", i + 1, g));
            }
            fs::write(&out, s).expect("write zeros");
            println!("computed {} zeros -> {}", n, out.display());
            for (i, g) in gs.iter().enumerate().take(5) {
                println!("  gamma_{} = {:.15}", i + 1, g);
            }
            println!("  ... gamma_{} = {:.15}", n, gs[n - 1]);
        }
        "bracket" => {
            let n: usize = args.get(2).and_then(|s| s.parse().ok()).unwrap_or(1000);
            checks::bracket(&data_dir, n);
        }
        "explicit" => checks::explicit_formula(),
        "paircorr" => {
            let n: usize = args.get(2).and_then(|s| s.parse().ok()).unwrap_or(2000);
            checks::paircorr(n);
        }
        "ranktrace" => {
            let trials: usize = args.get(2).and_then(|s| s.parse().ok()).unwrap_or(5000);
            checks::ranktrace(trials);
        }
        "mv" => checks::montgomery_vaughan(),
        "debug" => {
            for &t in &[0.0, 10.0, 14.134725, 17.0, 21.022, 25.010, 30.425] {
                let (re, im) = zeta::zeta_half_it(t);
                println!("t={:8.3}  zeta(1/2+it) = {:+.6}{:+.6}i   Z(t)={:+.6}",
                         t, re, im, zeta::zeta_z(t));
            }
        }
        _ => {
            println!("zeta-rs subcommands: constant | zeros N | bracket N | explicit | paircorr N | ranktrace [trials] | mv");
        }
    }
}
