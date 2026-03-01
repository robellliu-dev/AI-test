#!/usr/bin/env python3
"""Smoke test for generated Triton sample."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


MODULE_PATH = Path("triton/operators/vector_add.py")


def load_module(path: Path):
    spec = importlib.util.spec_from_file_location("vector_add", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load module from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    if not MODULE_PATH.exists():
        raise FileNotFoundError(f"{MODULE_PATH} not found. Run generator first.")

    mod = load_module(MODULE_PATH)
    result = mod.cpu_add([1.0, 2.5, -3.0], [2.0, 0.5, 3.0])
    assert result == [3.0, 3.0, 0.0], f"Unexpected cpu_add result: {result}"

    if getattr(mod, "HAS_TRITON", False):
        print("Triton detected. CPU smoke path passed; GPU kernel declaration is available.")
    else:
        print("Triton/GPU not available. CPU fallback smoke passed.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
