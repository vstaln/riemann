// lambda-sweep driver — bounded, resumable Rust orchestration for the dilation
// family. It invokes only the sanctioned arb verifier; this driver contains no
// numeric certification logic.
//
// Unlike the old driver, verifier stdout is streamed live. The old
// wait_with_output() hid all progress, which made a correct long run look hung.
//
// Usage: lambda-sweep <alpha> <p1..p6 comma> <q1..q6 comma>
//   [--pressure NUMERATOR_OVER_3000] [--grid N] [--nodes N]
//   [--progress N] [--timeout-sec N] <lam:eps> ...
use std::io::{BufRead, BufReader};
use std::process::{Command, Stdio};
use std::path::Path;
use std::sync::mpsc;
use std::thread;
use std::time::{Duration, Instant};

fn parse_result(line: &str, verified: &mut String, n_nodes: &mut String,
                status: &mut String, reason: &mut String) {
    if let Some(rest) = line.strip_prefix("VERIFY_RESULT ") {
        if let Ok(v) = serde_json::from_str::<serde_json::Value>(rest) {
            *verified = v["verified"].as_bool().unwrap_or(false).to_string();
            *n_nodes = v["nodes"].as_i64().unwrap_or(-1).to_string();
            *status = v["status"].as_str().unwrap_or("?").to_string();
            *reason = v["reason"].as_str().unwrap_or("").to_string();
        }
    }
}

fn run_target(alpha: &str, p_raw: &[f64], q_raw: &[f64], pressure: f64,
              grid: i64, nodes: u64, progress: u64, timeout_sec: u64,
              lam: f64, eps: f64) -> (String, String, String, String) {
    let started = Instant::now();
    println!("START lam={lam:.6} eps={eps:.7} timeout={}s nodes={} progress={}",
             timeout_sec, nodes, progress);

    let mut cmd = Command::new("uv");
    let repo_root = Path::new(env!("CARGO_MANIFEST_DIR"))
        .parent().and_then(Path::parent).expect("repository root");
    cmd.current_dir(repo_root);
    // -u is essential: without unbuffered Python stdout, a streaming Rust
    // parent still sees nothing until the verifier exits.
    cmd.args(["run", "--quiet", "--with", "mpmath", "--with", "python-flint",
              "python", "-u", "tools/verify_coboundary_floor.py"]);
    cmd.env("VERIFY_ALPHA", alpha);
    cmd.env("VERIFY_TARGET", format!("{eps:.17}"));
    cmd.env("VERIFY_PRESSURE", format!("{pressure:.17}"));
    cmd.env("VERIFY_LAMBDA", format!("{lam:.17}"));
    cmd.env("VERIFY_GRID", format!("{grid}"));
    cmd.env("VERIFY_MAX_NODES", format!("{nodes}"));
    cmd.env("VERIFY_PROGRESS_EVERY", format!("{progress}"));
    for (k, c) in p_raw.iter().enumerate() {
        cmd.env(format!("VERIFY_P{}", k + 1), format!("{c:.17}"));
    }
    for (k, c) in q_raw.iter().enumerate() {
        cmd.env(format!("VERIFY_Q{}", k + 1), format!("{c:.17}"));
    }
    cmd.stdout(Stdio::piped()).stderr(Stdio::inherit());

    let mut child = match cmd.spawn() {
        Ok(c) => c,
        Err(e) => return ("false".into(), "-1".into(), "spawn-error".into(), e.to_string()),
    };
    let stdout = child.stdout.take().expect("piped stdout");
    let (tx, rx) = mpsc::channel::<String>();
    thread::spawn(move || {
        for line in BufReader::new(stdout).lines() {
            if let Ok(line) = line {
                if tx.send(line).is_err() { break; }
            }
        }
    });

    let mut verified = "?".to_string();
    let mut n_nodes = "?".to_string();
    let mut status = "running".to_string();
    let mut reason = String::new();
    let mut last_heartbeat = Instant::now();
    loop {
        while let Ok(line) = rx.try_recv() {
            println!("  [{:.1}s] {line}", started.elapsed().as_secs_f64());
            parse_result(&line, &mut verified, &mut n_nodes, &mut status, &mut reason);
        }
        match child.try_wait() {
            Ok(Some(exit)) => {
                while let Ok(line) = rx.try_recv() {
                    println!("  [{:.1}s] {line}", started.elapsed().as_secs_f64());
                    parse_result(&line, &mut verified, &mut n_nodes, &mut status, &mut reason);
                }
                if verified == "?" {
                    status = format!("exit-{}", exit.code()
                        .map_or_else(|| "signal".to_string(), |c| c.to_string()));
                }
                break;
            }
            Ok(None) => {}
            Err(e) => {
                status = "wait-error".into();
                reason = e.to_string();
                break;
            }
        }
        if started.elapsed() >= Duration::from_secs(timeout_sec) {
            let _ = child.kill();
            let _ = child.wait();
            verified = "false".into();
            status = "timeout".into();
            reason = format!("wall timeout {}s", timeout_sec);
            println!("  [{:.1}s] TIMEOUT: killed verifier", started.elapsed().as_secs_f64());
            break;
        }
        if last_heartbeat.elapsed() >= Duration::from_secs(10) {
            println!("  [{:.1}s] HEARTBEAT: verifier still running",
                     started.elapsed().as_secs_f64());
            last_heartbeat = Instant::now();
        }
        thread::sleep(Duration::from_millis(100));
    }
    (verified, n_nodes, status, reason)
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    if args.len() < 6 {
        eprintln!("usage: {} <alpha> <p1..p6 comma> <q1..q6 comma> [opts] <lam:eps> ...", args[0]);
        std::process::exit(1);
    }
    let alpha = &args[1];
    let p_raw: Vec<f64> = args[2].split(',').map(|s| s.parse().unwrap()).collect();
    let q_raw: Vec<f64> = args[3].split(',').map(|s| s.parse().unwrap()).collect();
    assert_eq!(p_raw.len(), 6);
    assert_eq!(q_raw.len(), 6);

    let mut i = 4;
    let mut pressure = 1.0f64;
    let mut grid = 4000i64;
    let mut nodes = 8_000_000u64;
    let mut progress = 100_000u64;
    let mut timeout_sec = 300u64;
    let mut targets: Vec<(f64, f64)> = Vec::new();
    while i < args.len() {
        match args[i].as_str() {
            "--pressure" => { i += 1; pressure = args[i].parse().unwrap(); }
            "--grid" => { i += 1; grid = args[i].parse().unwrap(); }
            "--nodes" => { i += 1; nodes = args[i].parse().unwrap(); }
            "--progress" => { i += 1; progress = args[i].parse().unwrap(); }
            "--timeout-sec" => { i += 1; timeout_sec = args[i].parse().unwrap(); }
            tok => {
                let (lam, eps) = tok.split_once(':').unwrap();
                targets.push((lam.parse().unwrap(), eps.parse().unwrap()));
            }
        }
        i += 1;
    }

    println!("alpha={} pressure_arg={}/3000 grid={} max_nodes={} timeout={}s",
             alpha, pressure, grid, nodes, timeout_sec);
    println!("{:<6} {:<11} {:<8} {:<12} {}", "lam", "eps", "verified", "nodes", "status");
    for (lam, eps) in targets {
        let (verified, n_nodes, status, reason) = run_target(
            alpha, &p_raw, &q_raw, pressure, grid, nodes, progress, timeout_sec, lam, eps);
        println!("{:<6} {:<11} {:<8} {:<12} {} {}", lam, format!("{eps:.7}"),
                 verified, n_nodes, status, reason);
    }
}
