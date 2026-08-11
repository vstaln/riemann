#!/usr/bin/env python3
"""Portable entry point for the bundled MPFR kernel-table generator.

The original generator intentionally keeps the Linux soname ``libmpfr.so.6``
in its source so that its certificate hash is stable. On Windows this small
launcher points ctypes at an installed MPFR DLL and executes that unchanged
generator.
"""
from __future__ import annotations

import ctypes.util
import os
import runpy
import sys
from pathlib import Path


def _windows_mpfr() -> str | None:
    candidates = []
    configured = os.environ.get("ZETA_MPFR_DLL")
    if configured:
        candidates.append(configured)
    candidates.extend(
        [
            r"C:\Strawberry\c\bin\libmpfr-6.dll",
            r"C:\msys64\mingw64\bin\libmpfr-6.dll",
        ]
    )
    for candidate in candidates:
        if Path(candidate).is_file():
            return candidate
    return None


if os.name == "nt":
    dll = _windows_mpfr()
    if dll is None:
        raise SystemExit(
            "MPFR DLL not found; set ZETA_MPFR_DLL to libmpfr-6.dll "
            "(or install Strawberry/MSYS2 MPFR)"
        )
    ctypes.util.find_library = lambda _name: dll

generator = Path(__file__).with_name("generate_joint_kernel_table.py")
sys.argv[0] = str(generator)
runpy.run_path(str(generator), run_name="__main__")
