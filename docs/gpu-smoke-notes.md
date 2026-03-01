# GPU 冒烟测试与 Token 可行性说明

## 结论

- **GitHub 官方免费托管 Runner（`ubuntu-latest`）不提供 NVIDIA GPU**，因此无法直接在免费 Runner 上执行 Triton 的真实 GPU kernel 冒烟。
- **GitHub 本身没有“免费 GPU API Token”可直接领取并启用 GPU 算力**。
- NVIDIA 生态（如 NGC/NVIDIA Cloud）通常是独立的云资源与计费体系，**不存在通用“免费 API token + GitHub Action 就能长期跑 GPU CI”** 的官方模式。

## 可用方案

1. 使用 **self-hosted GPU runner**（本仓库 `triton-ci.yaml` 已预留 `gpu-smoke-optional` 作业）。
2. 接入第三方 GPU CI 服务（通常需要服务商 token/付费额度）。
3. PR/CI 默认跑 CPU fallback smoke，GPU smoke 作为可选门禁。

## 当前仓库实现

- `triton-pr.yaml`：PR 上保证“生成 -> 编译检查 -> UT -> CPU 冒烟”通过。
- `triton-ci.yaml`：Push/手动触发同样流程；若仓库变量 `ENABLE_GPU_SMOKE=true` 且 runner 标签可用，则执行可选 GPU 冒烟。
