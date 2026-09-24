# Project Starter

这个仓库不是业务项目模板代码，而是一套用于 Codex 项目启动、体检、治理和持续开发的工作流模板。

它把职责分为三层：Global Rules 约束通用行为，`project-governance-bootstrap` Skill 管理可复用流程，每个项目自己的 `AGENTS.md` 与 `docs/` 记录项目事实。详见[架构说明](docs/architecture.md)。

## 新项目

```text
使用 project-governance-bootstrap 初始化当前新项目。
先完成立项和安全基线，不要开始业务开发。
```

Skill 会保护已有文件、建立最小 Git 与文档基线并验证结果；不会自动创建 remote、push 或 deploy。

## 已有项目

```text
使用 project-governance-bootstrap 对当前项目做一次只读体检。
只输出 Level A/B/C 和风险，不做整改。
```

体检结束后会停止。只有用户明确要求按体检结果治理，才进入整改流程。

## 日常开发

```text
按照当前项目 AGENTS.md 和项目开发执行循环完成这个任务。
完成后报告已验证 / 未验证 / Git 状态。
```

项目完成首次治理后，日常开发直接使用项目文件与精简执行循环，不必重复上传治理文档或每轮重新体检。

## 仓库内容

- [`skills/project-governance-bootstrap/`](skills/project-governance-bootstrap/)：Skill 入口与分模式流程
- [`templates/`](templates/)：可按项目事实填写的基础模板
- [`docs/usage.md`](docs/usage.md)：安装、更新与触发方式
- [`docs/examples.md`](docs/examples.md)：匿名化使用示例
- [`scripts/validate.py`](scripts/validate.py)：无第三方依赖的静态验证

## 维护验证

```bash
python3 scripts/validate.py
git diff --check
```

