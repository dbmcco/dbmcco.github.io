---
layout: post
title: "CLI AI Coding: A Vault of Valuable Things"
date: 2025-12-07 09:30:00 -0500
categories: development ai workflow
tags: [ai, claude-code, cli, tools, resources]
description: "A curated list of repos, configs, and practices for CLI-based AI coding—road-tested by people doing real work."
unlisted: true
---

*This is a companion post to [Developing intuition for CLI-based AI coding]({{ '/2025/12/07/developing-intuition-for-cli-based-ai-coding/' | relative_url }}) — that post is about the understanding; this one is about the tools.*

---

## What this is

A curated list of repos, configs, and practices that have emerged from a group of people thinking hard about CLI-based AI coding. Not everything here will be right for you, but it's all been road-tested by people doing real work.

---

## Skills and Workflow Systems

| Tool | What it does | Link |
|------|--------------|------|
| **superpowers** | Installable skills for Claude Code—TDD, debugging, planning, pressure tests | [repo](https://github.com/obra/superpowers) / [blog](https://blog.fsck.com/2025/10/09/superpowers/) |
| **2389 Research skills** | fresh-eyes-review, scenario-testing from Harper's team | [repo](https://github.com/2389-research/claude-plugins) |
| **claude-commands** | UserPromptSubmit hook for multi-step workflows | [repo](https://github.com/jleechanorg/claude-commands) |

**Installing superpowers:**
```
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
```

---

## Memory and Context

| Tool | What it does | Link |
|------|--------------|------|
| **episodic-memory** | Cross-session recall for Claude | [repo](https://github.com/obra/episodic-memory) |
| **private-journal-mcp** | Persistent journals with vector search | [repo](https://github.com/obra/private-journal-mcp) |

### File-based planning pattern

Not a repo—a pattern. Externalize state because context window is unreliable; files aren't.

```
project/
├── prompt_plan.md      # Current plan, model reads but human controls
├── TODO.md             # Task list, can be auto-updated via hooks
├── .scratch/           # Disposable working space
└── CLAUDE.md           # Project-specific instructions
```

---

## CLAUDE.md and Configuration

### Example configs

| Source | Notes | Link |
|--------|-------|------|
| obra/dotfiles | Well-structured with testing section | [CLAUDE.md](https://github.com/obra/dotfiles/blob/main/.claude/CLAUDE.md) |
| harperreed/dotfiles | Thorough git/pre-commit guidance | [CLAUDE.md](https://github.com/harperreed/dotfiles/blob/master/.claude/CLAUDE.md) |
| dbmcco/claude-workspace | Modular memory system with imports | [repo](https://github.com/dbmcco/claude-workspace) |
| glimpser | AGENTS.md pattern | [example](https://github.com/KristopherKubicki/glimpser/blob/main/AGENTS.md) / [template](https://github.com/KristopherKubicki/glimpser/blob/main/AGENTS.template.md) |

### Settings and hooks

| Source | What's there | Link |
|--------|--------------|------|
| Ryan's dotfiles | ntfy.sh notifications setup | [settings.json](https://github.com/ryankanno/dotfiles/blob/main/dot_claude%2Bsettings.json) |
| Harper's dotfiles | Commands and agents | [commands](https://github.com/harperreed/dotfiles/tree/master/.claude/commands) / [agents](https://github.com/harperreed/dotfiles/tree/master/.claude/agents) |
| Dylan's dotfiles | Commands collection | [commands](https://github.com/detour1999/dotfiles/tree/main/.config/claude/commands) |

---

## Git and Parallel Work

### Worktrees

Built into git—multiple checkouts from one clone. Essential for running multiple Claude instances.

| Resource | Link |
|----------|------|
| Spawn script | [gist](https://gist.github.com/obra/bc7168431bc44451bec856672e690186) |
| Graphite rules | [rules doc](https://github.com/outfitter-dev/blz/blob/main/.agents/rules/GRAPHITE.md) |

```bash
git worktree add ../feature-branch feature-branch
git worktree list
git worktree remove ../feature-branch
```

---

## Hooks and Guardrails

### Pre-commit hooks (last line of defense)

| Tool | Language | Link |
|------|----------|------|
| pre-commit-hooks | General | [repo](https://github.com/pre-commit/pre-commit-hooks) |
| pre-commit-rust | Rust | [repo](https://github.com/doublify/pre-commit-rust) |
| ruff-pre-commit | Python linting | [repo](https://github.com/charliermarsh/ruff-pre-commit) |
| Test script example | — | [gist](https://gist.github.com/fredbenenson/2458dab98169040d5cc603caca0c9fa9) |

**Claude Code hooks:** [docs](https://docs.anthropic.com/en/docs/claude-code/hooks) — shell commands on events like tool calls or session starts.

---

## MCP Servers

| MCP | What it does | Link |
|-----|--------------|------|
| mcp-obsidian | Obsidian vault access | [repo](https://github.com/MarkusPfundstein/mcp-obsidian) |
| obsidian-mcp | Alternative Obsidian MCP | [repo](https://github.com/dbmcco/obsidian-mcp) |
| vocalize-mcp | Voice integration | [repo](https://github.com/2389-research/vocalize-mcp) |
| StageWhisper | Voice to text via accessibility APIs | [repo](https://github.com/obra/StageWhisper) |
| zen-mcp-server | Multi-model access | [repo](https://github.com/BeehiveInnovations/zen-mcp-server) |
| playwright-mcp | Browser testing | [repo](https://github.com/microsoft/playwright-mcp) |
| mcp-language-server | LSP to MCP adapter | [repo](https://github.com/isaacphi/mcp-language-server) |
| ht-mcp | Terminal/screen control | [repo](https://github.com/memextech/ht-mcp) |

---

## Agent Orchestration

| Tool | What it does | Link |
|------|--------------|------|
| **claude-squad** | Multiple Claude instances coordination | [repo](https://github.com/smtg-ai/claude-squad) |
| **claude-swarm** | Swarm-style agent coordination | [repo](https://github.com/parruda/claude-swarm) |
| **lace** | Custom agentic coding tool, more hookable than CC | [repo](https://github.com/obra/lace) / [prompts](https://github.com/obra/lace/tree/main/src/config/prompts) |
| **issue-cards** | Agent-friendly issue tracker with PM/dev roles | [repo](https://github.com/obra/issue-cards) |
| **botboard / 2389** | Agent journaling, "social tokens" | [site](https://2389.ai) / [research](https://2389.ai/posts/agents-discover-subtweeting-solve-problems-faster/) |

---

## Monitoring and Debugging

| Tool | What it does | Link |
|------|--------------|------|
| **cc-log-viewer** | Web viewer for Claude Code logs | [repo](https://github.com/2389-research/cc-log-viewer) |
| **ClaudeStatus** | Terminal status line (prompt, todos, git) | [repo](https://github.com/amac0/ClaudeStatus) |
| **ccstatusline** | Alternative status line | [repo](https://github.com/sirmalloc/ccstatusline) |
| **node-traffic-logger** | HTTP logging for transcript reconstruction | [repo](https://github.com/obra/node-traffic-logger) |
| **ScreenshotForChat** | Screenshot to clipboard in one key | [repo](https://github.com/obra/ScreenshotForChat) |

---

## GitHub Actions and CI

| Tool | What it does | Link |
|------|--------------|------|
| **claude-code-action** | Trigger Claude from GitHub issues/PRs | [repo](https://github.com/anthropics/claude-code-action) / [example](https://github.com/anthropics/claude-code-action/blob/main/examples/claude.yml) |
| **github-tdd-template** | TDD-focused GitHub template | [repo](https://github.com/dbmcco/github-tdd-template) |
| **Codex setup script** | Tool shims, uv, codebase hints | [gist](https://gist.github.com/KristopherKubicki/7197bc9e0eab51d2a9bbe7b0ef369101) |

---

## Model Routing and Proxies

| Tool | What it does | Link |
|------|--------------|------|
| **claude-code-router** | Route through OpenRouter for other models | [repo](https://github.com/musistudio/claude-code-router) |
| **claude-code-proxy** | Multi-model with judge voting | [repo](https://github.com/1rgs/claude-code-proxy) |

---

## Alternative Interfaces

| Tool | What it does | Link |
|------|--------------|------|
| **claude-code-webui** | Web UI for Claude Code | [repo](https://github.com/sugyan/claude-code-webui) |
| **claude-code.nvim** | Neovim integration | [repo](https://github.com/greggh/claude-code.nvim) |
| **Ghostty setup** | AppleScript for Ghostty + neovim | [gist](https://gist.github.com/paulsmith/e24438daca4e6907f342f4abd25f2309) |

---

## Mobile and Remote

**The stack:** tmux (persistence) + mosh (handles network changes) + [Tailscale](https://tailscale.com) (VPN) + Termux (Android)

| Voice Tool | What it does | Link |
|------------|--------------|------|
| loq | Voice input | [repo](https://github.com/LoqLab/loq) |
| whisper-to-input | API-based voice input | [repo](https://github.com/j3soon/whisper-to-input) |
| dsnote | Local voice transcription | [repo](https://github.com/mkiol/dsnote) |

---

## Interesting Projects Built with These Tools

| Project | What it is | Link |
|---------|------------|------|
| pgsqlite | Postgres wrapper on SQLite | [repo](https://github.com/erans/pgsqlite) |
| gruboros | RNN training project | [repo](https://github.com/ekg/gruboros) |
| hyprmon | Hyprland monitor management TUI | [repo](https://github.com/erans/hyprmon) |
| tiny-agent | Minimal agentic loop (~1KB) | [repo](https://github.com/obra/tiny-agent) |
| smallest-agent | Even smaller agent example | [repo](https://github.com/obra/smallest-agent) |

---

## Methodology Posts

| Post | Link |
|------|------|
| Jesse's methodology (June 2025) | [blog](https://blog.fsck.com/2025/06/24/my-agentic-coding-methodology-of-june-2025/) |
| System prompts comparison | [blog](https://blog.fsck.com/2025/06/26/system-prompts-for-cli-coding-agents/) |
| Anthropic's internal usage | [PDF](https://www-cdn.anthropic.com/58284b19e702b49db9302d5b6f135ad8871e7658.pdf) |

---

## House Rules

Patterns that aren't tools but are worth codifying:

| Rule | Why |
|------|-----|
| Plans in files, not in context | Context window forgets. Files don't. |
| Shorter sessions, more often | Context rot is real. Clear early and often. |
| Guardrails in code, not in prompts | Instructions decay. Pre-commit hooks don't. |
| Verify, don't trust | Model speaks with same confidence right or wrong. |
| Expect shortcuts | Model will find the easy path. Design around it. |
| No mocks in tests | Or at least separate `TestsWithMocks/` and `TestsWithoutMocks/` |
| Give Claude access to the MCP while developing it | Makes dev go 5x faster. |

---

*Last updated: December 2025*
