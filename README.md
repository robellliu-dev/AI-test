# AI-test

一个最小可运行的 C++ 示例项目，包含：

- `src/main.cpp`：示例程序入口。
- `src/math_utils.*`：简单的加法函数。
- `tests/test_math.cpp`：基础测试。
- `.github/workflows/build.yaml`：PR/Push 自动构建与测试。

## 本地构建与测试

```bash
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build --config Release
ctest --test-dir build --output-on-failure
```
