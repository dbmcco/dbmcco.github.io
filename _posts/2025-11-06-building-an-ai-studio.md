---
layout: post
title: Building an AI Studio (Instead of Just Prompting)
date: 2025-11-06 09:15:00 -0500
categories: development ai workflow
tags: [ai-studio, workflow, practice, mindset]
---

![[ai studio.png]]

This week a teammate sent me a tidy agenda for “how Braydon uses LLMs.” It read like a step-by-step architecture review. I realized we weren’t talking about the same kind of work. The agenda imagined a straight line; I’m working in a flexible AI studio.

When I say “studio,” I’m thinking about those Renaissance workshops where a lead artist framed the piece, set the order of operations, and highly skilled collaborators executed parts with precision. That’s closer to what’s actually happening in my day-to-day flow. I’m not nudging a chatbot for code or text. I’m orchestrating a crew of capable (and occasionally temperamental) collaborators, each with a defined surface area and constraint set.

There’s a loud drumbeat right now that says “learn prompt engineering, paste the magic incantation into ChatGPT, watch the finished product fall out.” That framing treats the model like a vending machine: the more clever the words, the better the prize. The agenda I was handed shares the same base assumption even though it’s structured differently—it still expects the model to take instructions and go away. My studio mindset flips that: I build a space where we *work together*, loop fast, challenge each other, and keep the environment ready so the models can act like collaborators.

## The Mental Model Gap

That agenda assumed a long hallway: define the architecture, integrate the services, lay in the interface, test at the end. In my world the work happens in tight loops:

- **I coach the models like senior specialists.** Every session starts with context, friction points, and an explicit brief. “Here are the knobs you can touch; here are the ones you can’t.”  
- **We pressure-test ideas together.** I’ll ask for counter-arguments, anti-pattern hunts, or three sub-agents to disagree on the next step. It keeps me out of the “Claude, please fix” spiral and surfaces better answers.  
- **I keep the focus on information logistics.** The goal is always shrinking a 10-hour friction into a 10-minute loop. If I don’t love doing the work myself, I’d rather design the loop and let the studio run it.

Until you step into the director role, the models keep behaving like autocomplete engines. The friction everyone feels—the endless prompting, the brittle outputs, the “why isn’t this smarter?”—is usually a mental model mismatch. I see three versions playing out right now:

- **Prompt vending machine.** Outcome depends on clever wording. The model lives outside your operation; you hope it hands back something useful.  
- **Straight-line project planner.** Outcome depends on polished documents moving through stages. The model is an external contractor executing your prewritten plan.  
- **Studio director.** Outcome depends on the workroom you design: loops, tools, guardrails, and constant checkpoints. The model is a specialist inside your operation.

Most modern “prompt tricks” belong to the first two camps. The studio model demands more prep and more attention, but it pays off in leverage.

## What People Are Picking Up

In the last few weeks I’ve had more people ask, “Can you show me how you’re doing this?” Every time I demo the studio, the reaction is the same: “Oh, that’s totally different—and 10x faster.” I think what they’re sensing is:

- **I arrange the room, not just the words.** Before the model does anything, I’ve already staged the tools, the access, and the boundaries. They see the environment, not just the prompt.  
- **They can watch the feedback loops.** I narrate each pass, where the model pushes back, when I tighten the guardrails. It’s obvious there’s a conversation, not a one-shot request.  
- **The handoffs are visible.** The studio does work, pauses for review, adjusts, and keeps moving. The autonomy feels earned because they can see where I still own the call.  
- **Everything ties back to leverage.** I’m never chasing outputs for their own sake. I’m shrinking frictions, aligning with strategy, making space for the next problem. That framing resonates because they can map it to their own bottlenecks.

It’s not magic; it’s a different way of thinking about the tools. Once you see the studio in motion, the mindset shift clicks.

## Inside the AI Studio

Once you adopt the studio mindset, the first order of business is designing the room your collaborators will work in. Here’s what that looks like on a good day:

1. **Room setup (infrastructure first).**  
   - Keys ready: API tokens for the services I need, already trimmed to the smallest scope that works.  
   - Tools open: Claude Code (the command-line helper I lean on), Codex for extended context, Perplexity for research, browser devtools when they’re useful.  
   - Dashboards up: deployment logs, lightweight debug switches, a dedicated terminal pane per collaborator so the conversation stays organized.  
   The model doesn’t babysit my environment; it lives inside it.

2. **Crew assignments.**  
   - `PM` agent guards requirements, sequencing, and dependency calls.  
   - `Builder` agent handles the implementation slices (often switching between Claude and Codex).  
   - `Tester` agent runs the safety checks and watches the tests.  
   - `Analyst` agent keeps a running state-of-the-world log and sanity-checks decisions.  
   No one person (human or model) is allowed to carry the entire project in their head.

3. **Session choreography.**  
   - Start with the PM restating the brief and pulling outstanding blockers.  
   - Spin up the builder only when the PM signs off on the next task definition.  
   - Tester runs the guardrails before we save the work; failures kick back to the builder with notes on what broke.  
   - Analyst records context shifts in a shared notebook so I can drop into the conversation mid-stream.  
   This keeps the context windows clean and the work product auditable.

## A Practical Run at It

If you want to try this without rebuilding my entire setup, here’s a compressed version you can execute in an afternoon:

1. **Pick a personal pain point.** Something that eats your hours—expense tracking, proposal version control, client note synthesis. The smaller and more annoying, the better.  
2. **Stage a tiny studio.** Create a fresh project folder with your tooling of choice, connect it to one data source or API, and pre-create the secrets file. Whatever you hand the model must already work.  
3. **Draft a two-column brief.** Column A: “Here’s what good looks like.” Column B: “Here’s what you are *not* allowed to do.” Give that to the PM agent.  
4. **Run a 90-minute loop.**  
   - 10 min: PM clarifies scope, breaks work into subtasks.  
   - 45 min: Builder executes in measured passes, pushing back when the brief is vague.  
   - 20 min: Tester enforces the guardrails and failing tests; Builder tightens.  
   - 15 min: Analyst documents decisions, surprises, and open loops.  
5. **Ship one artifact.** A working script, a dashboard, a report—something that closes the original pain point. By the end you should have a repeatable pattern, not just a one-off output.

Do this two or three times and you’ll feel what I’m chasing: you’re not “using an LLM,” you’re running a studio that happens to have silicon apprentices.

### Visual: The Studio Environment

```mermaid
flowchart LR
    subgraph Studio["Studio (Claude CLI · Codex)"]
    end
    Obsidian["Obsidian<br/>Strategy & Narrative"] --> Studio
    Studio --> GitHub["GitHub<br/>Repos & PRs"]
    Studio --> Vercel["Vercel<br/>Deployments & Logs"]
    Studio --> Todoist["Todoist<br/>Commitments"]
    Perplexity["Perplexity<br/>Research"] --> Studio
    Studio --> ReturnLoop["Updates & Briefs"]
```

*The studio sits in the middle. Each service is a surface the models can touch, with scoped permissions and clear responsibilities.*

## Why This Matters Right Now

- **Turnkey builders still collapse under real-world complexity.** In the transcript you can hear how often people wrestle with v0 UI prompts—we’ve all been there. The studio model keeps control of the infrastructure, so the work is portable and debuggable.  
- **Token budgets turn into resource budgets.** Once you treat models like teammates, you start managing capacity: which one gets the long memory, who handles research, where do we store shared context. That framing unlocks bigger missions.  
- **You reclaim your attention.** The studio’s real output isn’t code, it’s leverage. The more loops we automate, the more headroom we get for architecture, strategy, and the human decisions that still matter.

## Plugging the Studio Into My World

Once the studio is wired into my actual universe—Obsidian for strategy notes, GitHub repos for in-flight builds, Todoist for commitments, Perplexity for research—the model isn’t guessing in the dark. It’s inside my mental model.

- **Strategy stays coherent.** When Claude pulls an Obsidian note, it isn’t just copying text; it’s aligning implementation work with the priorities I’ve already set.  
- **Execution picks up speed.** Because the studio has real access to repos or deployment logs, I can hand off “make this change, run the tests, show me the result” without losing context.  
- **Decisions stay mine.** The model can surface options, contradictions, or risks faster than I can alone. But the call still runs through the way I think about quality, customers, process. The integrations supercharge my judgment—they don’t replace it.

That’s the quiet benefit. With the right wiring, the studio amplifies my thinking loops. Instead of asking, “What prompt gives me the answer?” the question becomes, “How do I give the studio the raw material to accelerate the way I already work?”

There’s also a big gap between passive and active use. Reading an AI-generated meeting recap is useful. Having the studio interrogate that recap—pull out the mental models in play, highlight conflicting assumptions, update my strategy notes, adjust my task list, and surface research prompts for a follow-up session—fundamentally changes my planning. The first is consumption. The second is collaboration.

### Visual: Passive vs. Active Follow-up

```mermaid
flowchart LR
    subgraph Passive["Passive Consumption"]
        P1("Read AI summary")
        P2("Maybe paste a snippet into notes")
        P3("Tell yourself you'll follow up")
        P4("Context fog builds by next meeting")
        P1 --> P2 --> P3 --> P4
    end
    subgraph Active["Active Studio Collaboration"]
        A1("Ask studio to map mental models")
        A2("Flag conflicting assumptions & gaps")
        A3("Update strategy notes & Todoist")
        A4("Generate research prompts & follow-up brief")
        A5("Walk into next session ready")
        A1 --> A2 --> A3 --> A4 --> A5
    end
```

### Visual: Shrinking the Friction

```mermaid
pie showData
    title Hours Spent on One Deliverable
    "Manual loop before the studio" : 10
    "After the studio builds the loop" : 2
```

*Once the loop exists, the studio runs it. The human work shifts to defining new problems, not repeating old ones.*

## Where I’m Pushing Next

I still don’t have a satisfying answer for front-end UX in the terminal. Complex state management blows up more often than I like. And I’m experimenting with a shared scratchpad so agents can hand off without me shuttling notes back and forth. Studios evolve—so will this one.

For now, the invitation is simple: stop prompting like a solo dev with a fancy autocomplete. Stand up your own AI studio. Give the models a room, a process, and a shared mission. Then direct the work like the piece is yours—because it is.
