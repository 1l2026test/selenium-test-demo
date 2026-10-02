# 软件测试练习项目

一个用 Python 写的软件测试入门 demo，覆盖黑盒测试、接口测试、Linux 环境检查。

## 项目结构

```
software-testing-demo/
├── src/
│   └── calculator.py          # 被测函数（成绩等级计算、除法）
├── tests/
│   ├── test_calculator.py      # 黑盒用例：等价类划分 + 边界值分析
│   └── test_api.py             # 接口测试：requests + pytest 测 httpbin.org
├── postman/
│   └── demo-api-tests.postman_collection.json   # Postman 手动接口用例
├── scripts/
│   └── check_env.sh            # Linux 测试环境检查脚本
└── notes/
    └── testing-basics.md       # 测试理论笔记（黑盒/白盒、等价类、边界值、Bug 生命周期）
```

## 已掌握技能对照

| 岗位要求 | 对应内容 |
|---|---|
| 测试理论（黑盒/白盒、等价类、边界值） | `tests/test_calculator.py` + `notes/testing-basics.md` |
| Python 自动化测试脚本 | 全部 `tests/` 目录，基于 pytest |
| Linux 基本操作 | `scripts/check_env.sh`（文件查看、进程、日志、磁盘） |
| Postman / Python 接口测试 | `tests/test_api.py` + `postman/` |
| Git | 本项目即 Git 仓库 |

## 运行方式

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 跑单元测试（不需要联网）
pytest tests/test_calculator.py -v

# 3. 跑接口测试（需要联网访问 httpbin.org）
pytest tests/test_api.py -v

# 4. 跑 Linux 环境检查脚本
bash scripts/check_env.sh
```

## 设计思路

`src/calculator.py` 里的 `get_grade(score)` 是一个简单函数：输入 0-100 分数，返回 A/B/C/F 等级。

测试用例按**等价类划分**分有效/无效输入，按**边界值分析**在每个分数段边界取值：
- 有效边界：0, 59, 60, 79, 80, 89, 90, 100
- 无效边界：-1, 101, 非数字

接口测试用 `requests` 测公开测试服务 httpbin.org，断言状态码和返回字段。
