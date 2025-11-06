---
layout: post
title: "My 'Vibe Coding' Process ATM"
date: 2025-05-28 10:00:00 -0500
categories: development ai workflow
tags: [substack-import, ai, development, claude-code, workflow]
description: "A walkthrough of my multi-agent vibe coding setup using Claude CLI roles, status rituals, and handoffs."
original_url: https://dbmcco.substack.com/p/my-vibe-coding-process-atm
---

# My "Vibe Coding" Process ATM

I've been experimenting with an approach I call "vibe coding" using multiple Claude Code CLI instances for complex projects. The goal is to create a more "repeatable, scalable and predictable" development process.

## Multi-Agent System

I use specialized agents with defined roles:

1. **Project Manager** - Coordination and planning
2. **Backend Developer** - Server-side implementation  
3. **Frontend Developer** - UI/UX development
4. **Data Service Developer** - Data layer and APIs
5. **Data Analyst** - Analysis and insights
6. **Business Analyst** - Requirements and strategy
7. **Tester** - Quality assurance and validation

## Communication Flow

The workflow follows a "Request-Response-Next" pattern:
- Manual coordination between agents
- Structured directory management  
- Emphasis on status tracking and todo management
- Clear handoffs between specialized roles

## Current Challenges

### Agent Coordination Issues
- Agents creating redundant scripts
- Inconsistent process following
- Context window management across sessions
- Asynchronous work coordination complexity

### Technical Limitations
- Managing state across multiple CLI instances
- Ensuring consistent project understanding
- Balancing autonomy with coordination

## Future Directions

I'm exploring several improvements:

### Orchestration Platforms
- **Microsoft AutoGen** for better agent orchestration
- **Headless Claude Code CLI** for programmatic control
- **Hybrid AI model approach** for specialized tasks

### Integration Enhancements
- Better pre-commit hooks integration
- Automated testing workflows
- Enhanced state management between agents

## Repository

The experimental setup is available at: https://github.com/dbmcco/claude-workspace

## Lessons Learned

This approach provides an in-depth look at AI-assisted software development, highlighting both current practices and areas for improvement. The key is finding the right balance between agent autonomy and coordinated execution.

The "vibe" aspect comes from letting the AI agents flow naturally while maintaining structure through defined roles and communication patterns.

---

*Originally published on [Substack](https://dbmcco.substack.com/p/my-vibe-coding-process-atm) on May 28, 2025. Migrated to this blog on May 29, 2025.*
