---
layout: post
title: "The Mindset Gap: How an AI Studio Changed My Workflow"
date: 2025-11-05 09:15:00 -0500
categories: development ai workflow
tags: [ai-studio, workflow, practice, mindset]
mermaid: true
---

<figure class="post-figure">
  <img src="{{ '/assets/images/ai-studio.png' | relative_url }}" alt="AI studio environment sketch">
  <figcaption>Nano banana is so fun!</figcaption>
</figure>

This week a teammate sent me an agenda to learn “how Braydon uses LLMs.” These requests are becoming more frequent, which is encouraging, but what struck me this time is that the agenda read like a flat instruction set—almost the way you’d stage assembling an IKEA dresser. It made something really clear: we were thinking about LLMs in entirely different ways. The agenda imagined a straight line; I’m operating an AI studio.

When I say “studio,” I’m thinking about those Renaissance workshops where a lead artist framed the piece (I’m no Renaissance master, but I admire the structure), set the order of operations, and highly skilled collaborators executed the parts with precision. That’s closer to my day-to-day reality. I’m not nudging a chatbot for code or copy. I’m orchestrating a crew of capable (and occasionally temperamental) collaborators, each with a defined surface area and constraint set.

There’s still a loud drumbeat in LLM-land that says “master prompt engineering, paste the magic incantation into ChatGPT, and the finished product will fall out.” That framing treats the model like a vending machine: clever words in, prize out. The agenda I saw shared that assumption—it still expected the model to take instructions and disappear until the job was done. My studio mindset flips that: I build a space where we *work together*, loop fast, challenge each other, and keep the environment ready so the models can act like collaborators.

## The Mental Model Gap

That linear agenda assumed a long hallway: define the architecture, integrate the services, lay in the interface, test at the end. In my world the work happens in tight loops:

- **I coach the models like senior specialists.** Every session starts with context, friction points, and an explicit brief. “Here are the knobs you can touch; here are the ones you can’t.”  
- **We pressure-test ideas together.** I’ll ask for counter-arguments, anti-pattern hunts, or three sub-agents to disagree on the next step. It keeps me out of the “Claude, please fix” spiral and surfaces better answers.  
- **I keep the focus on information logistics.** The goal is always shrinking a 10-hour friction into a 10-minute loop. If I don’t love doing the work myself, I’d rather design the loop and let the studio run it.

Until you step into the director role, the models keep behaving like autocomplete engines. The friction everyone feels—the endless prompting, the brittle outputs, the “why isn’t this smarter?”—is usually a mental model mismatch. I see three versions playing out right now:

- **Prompt vending machine.** Outcome depends on clever wording. The model lives outside your operation; you hope it hands back something useful.  
- **Straight-line project planner.** Outcome depends on polished documents moving through stages. The model is an external contractor executing your prewritten plan.  
- **Studio director.** Outcome depends on the workroom you design: loops, tools, guardrails, and constant checkpoints. The model is a specialist inside your operation.

Most modern “prompt tricks” belong to the first two camps. The studio model demands more prep and more attention, but it pays off in leverage.

## What People Are Picking Up

In the last few weeks more people have asked, “Can you show me how you’re doing this?” Every time I demo the studio, the reaction is the same: “Oh, that’s totally different—and 10x faster.” I think what they’re sensing is:

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

## Visual: The Studio Environment

{% raw %}
<div class="mermaid-container">
  <div class="mermaid">
flowchart LR
    Studio((Studio<br/>Claude CLI &amp; Codex))
    Obsidian["Obsidian<br/>Strategy &amp; Narrative"]
    GitHub["GitHub<br/>Repos &amp; PRs"]
    Vercel["Vercel<br/>Deployments &amp; Logs"]
    Todoist["Todoist<br/>Commitments"]
    Reminders["Apple Reminders<br/>Custom MCP"]
    Attio["Attio<br/>Skills + API"]
    SendGrid["SendGrid<br/>Skills + API"]
    Perplexity["Perplexity<br/>Research"]
    Local["Local Files<br/>Transcripts &amp; Docs"]
    Drive["Google Drive<br/>Skills access"]
    ReturnLoop["Updates &amp; Briefs"]

    Studio <-->|Custom MCP| Obsidian
    Studio <-->|CLI| GitHub
    Studio <-->|Claude/Codex Skill + API| Vercel
    Studio <-->|Custom MCP| Todoist
    Studio <-->|Custom MCP| Reminders
    Studio <-->|Claude/Codex Skill + API| Attio
    Studio <-->|Claude/Codex Skill + API| SendGrid
    Studio <-->|Claude/Codex Skill + API| Perplexity
    Studio <-->|CLI| Local
    Studio <-->|Claude/Codex Skill + Service Account| Drive
    Studio --> ReturnLoop
    ReturnLoop --> Obsidian
  </div>
</div>
{% endraw %}

*The studio sits in the middle. Each service is a surface the models can touch, with scoped permissions and clear responsibilities. (CLI = direct shell tools, Custom MCP = bespoke connector, Claude/Codex Skill = scripted agent skill with API bindings.)*

## What Keeps Breaking for People

- **Turnkey builders still collapse under real-world complexity.** I hear about v0 prompting struggles almost every week. The moment a project needs real integrations or deeper testing, the “one prompt” dream falls apart.  
- **Token budgets get wasted without a plan.** Treat the model as a teammate, hand it a clear brief, and suddenly the context window works like a real resource instead of a black hole.  
- **Attention is the scarcest asset.** The studio’s output isn’t “more features,” it’s reclaimed headspace. The loops we automate give me time back for architecture, strategy, and the human decisions that still matter.

<div class="bar-chart">
  <div class="bar-row">
    <div class="bar-label">Manual loop before the studio</div>
    <div class="bar-track">
      <div class="bar-fill bar-long">10 hrs</div>
    </div>
  </div>
  <div class="bar-row">
    <div class="bar-label">After the studio builds the loop</div>
    <div class="bar-track">
      <div class="bar-fill bar-short">45 min</div>
    </div>
  </div>
</div>

*Once the loop exists, the studio runs it. The human work shifts to defining new problems, not repeating old ones. That kind of leverage unlocks an entirely different way of working—more on that soon.*

There’s also a big gap between passive and active use. Reading an AI-generated meeting recap is useful. Having the studio interrogate that recap—pull out the mental models in play, highlight conflicting assumptions, update my strategy notes, adjust my task list, and surface research prompts for a follow-up session—fundamentally changes my planning. The first is consumption. The second is collaboration.

### Visual: Passive vs. Active Follow-up

<div class="comparison-grid">
  <div>
    <h4>Passive consumption</h4>
    <ul>
      <li>Read the AI-generated summary.</li>
      <li>Maybe copy a highlight into notes.</li>
      <li>Tell yourself you’ll follow up later.</li>
      <li>Walk into the next meeting with fuzzy context.</li>
    </ul>
  </div>
  <div>
    <h4>Active studio collaboration</h4>
    <ul>
      <li>Ask the studio to map the mental models in the room.</li>
      <li>Flag conflicting assumptions and missing data.</li>
      <li>Update strategy notes, adjust Todoist, open research prompts.</li>
      <li>Show up with a brief, open questions, and a plan to close gaps.</li>
    </ul>
  </div>
</div>

## Where I’m Pushing Next

I still don’t have a satisfying answer for front-end UX in the terminal. Complex state management blows up more often than I like. And I’m experimenting with a shared scratchpad so agents can hand off without me shuttling notes back and forth. Studios evolve—so will this one.

For now, the invitation is simple: stop prompting like a solo dev with a fancy autocomplete. Stand up your own AI studio. Give the models a room, a process, and a shared mission. Then direct the work like the piece is yours—because it is.

---

*Process note: I drafted this with Codex inside the studio. I defined the goals, prompts, and guardrails; Codex executed the heavy lift on prose and diagrams. Human direction, machine acceleration—including that silly sounding phrase.*
