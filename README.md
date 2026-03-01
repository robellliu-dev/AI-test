# AI-test

一个最小可运行的 C++ + Triton 示例项目，包含：

- `src/main.cpp`：C++ 示例程序入口。
- `src/math_utils.*`：简单的加法函数。
- `tests/test_math.cpp`：C++ 基础测试。
- `scripts/generate_triton_sample.py`：自动生成 Triton 算子样例文件。
- `triton/operators/vector_add.py`：自动生成的 Triton 向量加法算子样例（含 CPU fallback）。
- `triton/run_smoke.py`：Triton 冒烟脚本（无 GPU 时走 CPU fallback）。
- `tests_triton/test_generate_triton_sample.py`：Triton 生成器 UT。

## CI / PR 流水线

- `.github/workflows/build.yaml`：C++ 在 PR/Push 自动构建与测试。
- `.github/workflows/triton-pr.yaml`：Triton 在 PR 自动执行「生成 -> 编译检查 -> UT -> 冒烟」。
- `.github/workflows/triton-ci.yaml`：Triton 在 Push/手动触发同样流程，并可选触发 GPU 冒烟。
- `.github/workflows/pre-commit.yaml`：pre-commit 检查。
- `.github/workflows/codeql.yaml`：CodeQL 安全扫描。
- `.github/workflows/scorecard.yaml`：OpenSSF Scorecard 分析。
- `.github/workflows/slsa.yaml`：SLSA provenance 生成（tag/workflow_dispatch）。

## 本地构建与测试

### C++

```bash
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build --config Release
ctest --test-dir build --output-on-failure
```

### Triton（生成 / UT / 冒烟）

```bash
python3 scripts/generate_triton_sample.py
python3 -m py_compile triton/operators/vector_add.py
python3 -m pytest -q tests_triton
python3 triton/run_smoke.py
```

## GPU 能力说明

关于 GitHub 免费 Runner / NVIDIA token 可行性说明见：

- `docs/gpu-smoke-notes.md`
