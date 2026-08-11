$ErrorActionPreference = 'Stop'
$repo = [IO.Path]::GetFullPath((Split-Path -Parent $PSScriptRoot)).TrimEnd([IO.Path]::DirectorySeparatorChar)
$tmp = Join-Path $repo ".tmp_test_zeta_verify_$PID"
$resolvedTmp = [IO.Path]::GetFullPath($tmp)
if ((Split-Path -Parent $resolvedTmp) -ne $repo -or
    (Split-Path -Leaf $resolvedTmp) -notmatch '^\.tmp_test_zeta_verify_\d+$') {
    throw "refusing unsafe temporary path: $resolvedTmp"
}
if (Test-Path -LiteralPath $tmp) { throw "temporary path unexpectedly exists: $tmp" }
New-Item -ItemType Directory -Path $tmp | Out-Null
$workers = if ($env:ZETA_VERIFY_WORKERS) { [int]$env:ZETA_VERIFY_WORKERS } else { 8 }
if ($workers -lt 1) { throw 'ZETA_VERIFY_WORKERS must be positive' }

function Assert-EqualBytes([string]$left, [string]$right, [string]$label) {
    $a = [IO.File]::ReadAllBytes($left); $b = [IO.File]::ReadAllBytes($right)
    if (-not [Linq.Enumerable]::SequenceEqual($a, $b)) { throw "$label byte comparison failed" }
}

try {
    Push-Location $repo
    $bound = (& python tools/compute_joint_bound.py | Out-String)
    $bound | Write-Output
    if ($bound -notmatch 'new_bound=0\.673192911473142253') {
        throw 'compute_joint_bound.py did not reproduce the Bellman bound'
    }
    $directed = (& python tools/evaluate_coboundary_bound.py | Out-String)
    $directed | Write-Output
    foreach ($needle in @('precision_bits=256','bound_lower=0.6731929114731422',
            'bound_upper=0.67319291147314231')) {
        if ($directed -notmatch [regex]::Escape($needle)) { throw "directed evaluator missing $needle" }
    }
    if ($directed -notmatch 'mpfr_version=4\.2\.') { throw 'directed evaluator requires MPFR 4.2.x' }

    $kernelTmp = Join-Path $tmp 'cos147-kernel.bin'
    & python tools/run_generate_joint_kernel_table.py --output $kernelTmp --progress-every 0
    Assert-EqualBytes $kernelTmp (Join-Path $repo 'data\cos147-kernel.bin') 'kernel table'
    $derivativeTmp = Join-Path $tmp 'cos147-derivatives.bin'
    & python tools/generate_coboundary_derivative_table.py --output $derivativeTmp --workers $workers
    Assert-EqualBytes $derivativeTmp (Join-Path $repo 'data\cos147-derivatives.bin') 'derivative table'

    $gxx = (Get-Command g++ -ErrorAction Stop).Source
    $verifyExe = Join-Path $tmp 'verify_coboundary.exe'
    $compileArgs = @('-O2','-std=c++20','-frounding-math','-ffp-contract=off',
        '-Wall','-Wextra','-Wpedantic')
    $inc = 'C:\Strawberry\c\include'; $lib = 'C:\Strawberry\c\lib'
    if (Test-Path -LiteralPath (Join-Path $inc 'gmp.h')) { $compileArgs += "-I$inc" }
    $compileArgs += @('tools/verify_coboundary.cpp')
    if (Test-Path -LiteralPath $lib) { $compileArgs += "-L$lib" }
    $compileArgs += @('-lgmp','-o',$verifyExe)
    & $gxx @compileArgs
    if ($LASTEXITCODE -ne 0) { throw 'GMP verifier compilation failed' }

    $rows = @()
    for ($box = 0; $box -lt 64; $box++) {
        $oldErrorAction = $ErrorActionPreference
        $ErrorActionPreference = 'Continue'
        $line = (& $verifyExe (Join-Path $repo 'data\cos147-kernel.bin') $derivativeTmp $box 2>&1 | Out-String).Trim()
        $exitCode = $LASTEXITCODE
        $ErrorActionPreference = $oldErrorAction
        $line | Write-Output
        if ($exitCode -ne 0 -or $line -notmatch 'verified=true') { throw "certificate box $box failed" }
        $rows += $line
    }
    $expected = @{ coarse_nodes = 1126636; coarse_splits = 563286; coarse_pressure = 3477; coarse_interval = 318922; coarse_tangent = 240951 }
    foreach ($key in $expected.Keys) {
        $sum = 0
        foreach ($line in $rows) { $m = [regex]::Match($line, "$key=(\d+)"); if (-not $m.Success) { throw "missing $key" }; $sum += [int64]$m.Groups[1].Value }
        if ($sum -ne $expected[$key]) { throw "$key total $sum != $($expected[$key])" }
    }
    $depth = ($rows | ForEach-Object { [int]([regex]::Match($_, 'coarse_depth=(\d+)').Groups[1].Value) } | Measure-Object -Maximum).Maximum
    if ($depth -ne 55) { throw "maximum depth $depth != 55" }
    if (1126636 - 563286 - 3477 - 318922 - 240951 -ne 0) { throw 'tree identity failed' }
    'verification=passed (Bellman rerun; external peer review pending)'
} finally {
    Pop-Location
    if (Test-Path -LiteralPath $tmp) { Remove-Item -LiteralPath $tmp -Recurse -Force }
}
