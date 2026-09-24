# Usage

## Skill 源目录

本仓库中的可安装 Skill 位于：

```text
skills/project-governance-bootstrap
```

## 安装

将该目录完整复制或连接到当前 Codex 支持的个人 Skill 目录。常见的个人安装位置是 `$CODEX_HOME/skills/project-governance-bootstrap`；如果未设置 `CODEX_HOME`，Codex 通常使用 `~/.codex/skills/project-governance-bootstrap`。应以当前 Codex 版本实际支持的 Skill 安装方式为准。

安装时保留以下相对结构：

```text
project-governance-bootstrap/
├── SKILL.md
└── references/
```

安装不会授权 Skill 自动创建 remote、push、deploy、发布或执行破坏性操作。

## 更新

1. 拉取或下载本仓库的新版本。
2. 用新的 `skills/project-governance-bootstrap` 目录更新已安装副本。
3. 不要覆盖目标业务项目自己的 `AGENTS.md` 和 `docs/`。
4. 重新运行 Skill 校验，并在新的 Codex 会话中确认它已被发现。

## 验证已识别

如果当前安装包含 Codex 的 `quick_validate.py`，可运行：

```bash
python3 /path/to/quick_validate.py /path/to/project-governance-bootstrap
```

随后在一个测试项目中明确调用：

```text
使用 project-governance-bootstrap 对当前项目做一次只读体检。
```

确认 Codex 进入 `AUDIT` 模式，只输出报告而不修改文件。路径示例需要替换为当前环境的实际路径，不应复制进项目模板。

## 首次触发

新项目：

```text
使用 project-governance-bootstrap 初始化当前新项目。
先完成立项和安全基线，不要开始业务开发。
```

已有项目：

```text
使用 project-governance-bootstrap 对当前项目做一次只读体检。
只输出 Level A/B/C 和风险，不做整改。
```

## 后续开发

首次立项或治理会把稳定的项目事实写入目标项目的 `AGENTS.md`、`README.md` 与 `docs/`。之后 Codex 直接读取这些项目文件，再按 Skill 的开发执行循环工作。因此无需在每次对话中重复上传四份流程文档，也无需每轮重新做完整体检。

