from pathlib import Path

from scripts.generate_triton_sample import generate


def test_generate_file(tmp_path: Path) -> None:
    output = tmp_path / "triton" / "operators" / "vector_add.py"
    generate(output)

    assert output.exists()
    content = output.read_text(encoding="utf-8")
    assert "cpu_add" in content
    assert "vector_add_kernel" in content
