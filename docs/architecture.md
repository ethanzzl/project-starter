# Architecture

本仓库采用三层治理结构：

```text
Global Rules
    ↓
project-governance-bootstrap Skill
    ↓
Project AGENTS.md + docs
```

## Global Rules

Global Rules 只管理跨项目通用的工作方式：

- 回答与协作风格
- 项目隔离
- 最小修改
- 验证原则
- Git 安全
- 高风险操作边界

它不保存单个项目的产品事实，也不替代项目内文档。

## Skill

`project-governance-bootstrap` 只管理可复用流程：

- 新项目立项
- 已有项目只读体检
- 体检后的治理顺序
- 日常开发执行循环
- 本地验证与平台真实验证的边界

Skill 通过仓库事实选择模式，不依赖额外数据库或强制状态文件。各模式的详细规则按需从 `references/` 加载。

## Project Files

目标项目中的文件只记录该项目自己的事实与规则：

- `AGENTS.md`：AI / Codex 在当前项目如何工作
- `README.md`：人如何进入和使用项目
- `docs/project.md`：项目当前事实与状态
- `docs/decisions.md`：长期决策及原因
- `docs/assets.md`：不可重建或重要素材的恢复策略，仅在需要时创建

这三层不能互相混写。通用行为留在 Global Rules，可复用流程留在 Skill，易变化的项目事实留在项目文件。

## Lifecycle

Skill 使用以下概念状态帮助判断下一步：

```text
NEW → AUDITED → GOVERNED → DEVELOPMENT → PLATFORM_VALIDATION → RELEASE
```

状态以 Git baseline、项目文档、风险、实现目录和验证证据等现有事实判断。项目可选择在 `docs/project.md` 记录当前阶段，但不要求维护额外状态系统。

