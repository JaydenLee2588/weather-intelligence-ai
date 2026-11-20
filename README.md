# weather-intelligence-ai

这是一个练习项目：通过 API 获取不同气象数据，预测某一天最高温度达到某个值的概率。

## 开发环境

项目使用 [uv](https://docs.astral.sh/uv/) 管理 Python 环境和依赖：

```bash
uv sync --dev
```

配置项示例位于 `config/`，环境变量模板位于 `.env.example`。原始数据、处理过程数据和模型产物分别保存在 `data/` 与 `models/` 中；这些目录默认不提交数据文件。

## 项目结构

- `src/weather_ai/`：数据获取、特征工程、模型、预测及通用工具
- `notebooks/`：数据探索、特征分析和模型实验
- `scripts/`：数据获取、数据集构建及模型训练入口
- `tests/`：自动化测试
- `docs/`：架构、数据字典和实验记录

当前代码与配置文件是项目骨架，具体数据源、目标阈值和模型流程可在后续迭代中补充。
