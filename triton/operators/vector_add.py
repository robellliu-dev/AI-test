"""Auto-generated Triton operator sample."""

from __future__ import annotations

from typing import Sequence

HAS_TRITON = False
try:
    import triton  # type: ignore
    import triton.language as tl  # type: ignore

    HAS_TRITON = hasattr(triton, "jit")
except Exception:
    HAS_TRITON = False


if HAS_TRITON:
    @triton.jit
    def vector_add_kernel(x_ptr, y_ptr, output_ptr, n_elements, BLOCK_SIZE: tl.constexpr):
        pid = tl.program_id(axis=0)
        block_start = pid * BLOCK_SIZE
        offsets = block_start + tl.arange(0, BLOCK_SIZE)
        mask = offsets < n_elements
        x = tl.load(x_ptr + offsets, mask=mask)
        y = tl.load(y_ptr + offsets, mask=mask)
        tl.store(output_ptr + offsets, x + y, mask=mask)


def cpu_add(x: Sequence[float], y: Sequence[float]) -> list[float]:
    if len(x) != len(y):
        raise ValueError("Input lengths must match")
    return [a + b for a, b in zip(x, y)]
