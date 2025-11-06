---
layout: post
title: "My Development Setup: tmux, Tailscale, and Claude Agents"
date: 2025-09-03 08:00:00 -0500
categories: development ai workflow setup
tags: [ai, development, claude-code, workflow, setup, tmux, tailscale]
description: "A tour of the tmux, Tailscale, and Claude agent setup that keeps my remote development environment humming."
---

# My Development Setup: tmux, Tailscale, and Claude Agents

Five months ago I mentioned in ["The CLI LLM Agent Journey So Far"](https://dbmcco.github.io/2025/05/30/The-CLI-LLM-Agent-Journey-so-far/) that tmux felt "wildly daunting." Well, turns out I was wrong. tmux is now the backbone of my entire development workflow.

## The Multi-Agent Setup That Actually Works

Remember my original ["Vibe Coding"](https://dbmcco.github.io/2025/05/28/my-vibe-coding-process-atm/) approach with multiple Claude Code CLI instances? The manual markdown coordination was killing me. Now I run everything through tmux sessions.

Here's what I typically have running:

### Session Architecture
```bash
# Main coordination session
tmux new-session -d -s "coord" "claude-code"

# Specialized agent sessions  
tmux new-session -d -s "impl" "claude-code" # Implementer agent
tmux new-session -d -s "arch" "claude-code" # Architect agent  
tmux new-session -d -s "qual" "claude-code" # Quality agent
tmux new-session -d -s "test" "claude-code" # Testing focus
```

The beauty? I can switch between contexts instantly with `tmux attach -t impl` or monitor multiple agents simultaneously with tmux's split panes. No more copy-paste hell between CLI instances.

## Remote Development Revolution

This is where Tailscale changed everything. I can code from anywhere - my MacBook, my iPad with a keyboard, even my phone in a pinch (don't judge). All my development sessions persist on my main machine while I connect remotely.

### The Workflow
1. **Morning**: SSH into my development machine via Tailscale
2. **Resume sessions**: `tmux list-sessions` shows all my active work
3. **Context switching**: Jump between different projects/agents instantly
4. **Evening**: Detach and keep everything running

The psychological effect is huge. I'm not losing context when I switch locations or devices. My development "state" just persists.

## Agent Coordination That Actually Works

My previous approach had agents writing markdown messages to each other. Cute, but inefficient. Now I use:

### Shared Context Files
Each tmux session monitors shared files:
- `/project/status.md` - Overall project state
- `/project/coordination.md` - Inter-agent communication  
- `/project/todos.md` - Task tracking (TodoWrite integration)

### Real Communication Pattern
Instead of AI agents pretending to talk to each other, I orchestrate the handoffs:

1. **Architect agent** designs the system in `arch` session
2. I review, then switch to **Implementer agent** in `impl` session
3. **Quality agent** reviews implementation in `qual` session
4. **Testing agent** validates in `test` session

Human coordination, AI execution. Much cleaner.

## The LFW Business Context

This setup supports real client work now. My LFW business is at $2,500/month per application, and I need systems that scale. Can't afford context window disasters when clients are paying.

### Quality Gates Everywhere
Every session has the same quality standards:
- Pre-commit hooks must pass
- Tests must pass  
- TypeScript strict mode enforced
- >90% test coverage required

The tmux approach means I can monitor quality gates across multiple agents simultaneously. Game changer.

## Configuration That Matters

### tmux.conf Essentials
```bash
# Enable mouse support (controversial, I know)
set -g mouse on

# Better prefix key
unbind C-b
set-prefix C-a

# Session management
bind r source-file ~/.tmux.conf \; display "Reloaded!"
bind | split-window -h
bind - split-window -v
```

### Tailscale Setup
Pretty standard installation, but the magic is in the SSH config:
```bash
Host dev-machine
    HostName 100.x.x.x  # Your Tailscale IP
    User braydon
    Port 22
    ServerAliveInterval 60
```

## What I Got Wrong Before

In my earlier posts, I was fighting context window management manually. Turns out the solution isn't more sophisticated AI coordination - it's better human tooling.

The agents don't need to be smarter about communication. I need better tools to manage them efficiently.

## Current Challenges

### Session Management
Still figuring out optimal session organization. Do I create new sessions per project? Per agent type? Per client? Currently using a hybrid approach.

### Resource Usage  
Running 4-5 Claude Code instances simultaneously hits token limits faster. Working on better session lifecycle management.

### Context Bleeding
Sometimes agents in different sessions reference each other's work without explicit handoff. Need better isolation.

## What's Next

Exploring automation of the session creation itself. Maybe a script that:
1. Creates tmux sessions for a new project
2. Initializes each with appropriate agent context
3. Sets up shared coordination files
4. Connects to project's GitHub repo

Also considering GitHub Codespaces integration. Remote tmux + Claude agents + Codespaces could be interesting.

## Real Impact

This setup delivered three client applications in the past month. The coordination overhead that was killing my previous workflow is mostly gone. I can focus on architecture and requirements while the agents handle implementation.

Still experimental. Still learning. But finally feeling like I have sustainable tooling for AI-assisted development.

---

*This development setup continues evolving. Next post will dive into the actual processes and workflows that make this coordination effective.*

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>
