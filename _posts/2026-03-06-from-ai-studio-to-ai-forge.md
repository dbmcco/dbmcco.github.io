---
layout: post
title: "From AI Studio to AI Forge"
date: 2026-03-06 09:00:00 -0500
categories: development ai workflow
tags: [ai, workflow, ai-studio, ai-forge, speedrift, lightforge-works]
mermaid: true
description: "Why the AI studio metaphor stopped being enough for me, and how I'm starting to think in terms of AI Forge, Speedrift, and a bounded dark factory."
---

<style>
  @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,500;8..60,600&family=Instrument+Sans:wght@400;500;600&display=swap');

  .post-header {
    display: none;
  }

  .page-content {
    background:
      radial-gradient(circle at top, rgba(193, 114, 61, 0.18), transparent 32%),
      linear-gradient(180deg, #f5ecdf 0%, #f8f2e8 30%, #fcf8f2 100%);
  }

  .page-content .wrapper {
    max-width: 980px !important;
    padding: 0 1.4rem !important;
  }

  .forge-progress {
    position: fixed;
    top: 0;
    left: 0;
    width: 0;
    height: 3px;
    background: linear-gradient(90deg, #8e4523 0%, #d98d53 100%);
    z-index: 9999;
    box-shadow: 0 0 18px rgba(217, 141, 83, 0.35);
  }

  .forge-essay {
    --forge-ink: #231a14;
    --forge-soft: #59493e;
    --forge-muted: #857160;
    --forge-rule: rgba(130, 92, 61, 0.28);
    --forge-accent: #8e4523;
    --forge-accent-soft: #d98d53;
    font-family: 'Source Serif 4', Georgia, serif;
    color: var(--forge-ink);
    counter-reset: forge-section;
    padding: 2.5rem 0 5rem;
  }

  .forge-essay a {
    color: var(--forge-accent);
    text-decoration-color: rgba(142, 69, 35, 0.35);
    text-underline-offset: 0.18em;
  }

  .forge-hero {
    text-align: center;
    padding: 1.5rem 0 2rem;
  }

  .forge-eyebrow,
  .forge-meta,
  .forge-essay h3,
  .forge-card h4 {
    font-family: 'Instrument Sans', sans-serif;
    letter-spacing: 0.22em;
    text-transform: uppercase;
  }

  .forge-eyebrow {
    font-size: 0.72rem;
    color: var(--forge-muted);
    margin: 0 0 1rem;
  }

  .forge-hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2.8rem, 8vw, 4.85rem);
    line-height: 0.98;
    font-weight: 500;
    letter-spacing: -0.02em;
    color: var(--forge-ink);
    max-width: 10ch;
    margin: 0 auto 1rem;
  }

  .forge-subtitle {
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-size: clamp(1.18rem, 3vw, 1.6rem);
    line-height: 1.45;
    color: var(--forge-soft);
    max-width: 34rem;
    margin: 0 auto 1.35rem;
  }

  .forge-meta {
    font-size: 0.74rem;
    color: var(--forge-muted);
    margin: 0;
  }

  .forge-rule {
    width: 92px;
    height: 1px;
    background: linear-gradient(90deg, transparent 0%, var(--forge-accent-soft) 50%, transparent 100%);
    margin: 1.75rem auto 0;
  }

  .forge-hero-image,
  .forge-pullquote,
  .forge-divider,
  .forge-diagram,
  .forge-diagram-caption,
  .forge-endgrid {
    opacity: 0;
    transform: translateY(14px);
    transition: opacity 0.8s ease, transform 0.8s ease;
  }

  .forge-visible {
    opacity: 1;
    transform: translateY(0);
  }

  .forge-hero-image {
    max-width: 860px;
    margin: 0 auto 3rem;
  }

  .forge-hero-image img {
    display: block;
    width: 100%;
    border-radius: 28px;
    border: 1px solid rgba(93, 63, 41, 0.16);
    box-shadow: 0 24px 60px rgba(54, 37, 24, 0.16);
  }

  .forge-hero-image p {
    max-width: none;
    margin: 1rem auto 0;
    text-align: center;
    font-family: 'Instrument Sans', sans-serif;
    font-size: 0.74rem;
    line-height: 1.6;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--forge-muted);
  }

  .forge-opening {
    max-width: 760px;
    margin: 0 auto 3rem;
  }

  .forge-opening p:first-child {
    font-size: 1.18rem;
  }

  .forge-opening p:last-child {
    margin-bottom: 0;
  }

  .forge-pullquote {
    max-width: 840px;
    margin: 0 auto 3.75rem;
    padding: 2rem 2rem 2.15rem;
    background: linear-gradient(135deg, rgba(201, 143, 100, 0.18), rgba(255, 255, 255, 0.58));
    border: 1px solid rgba(142, 69, 35, 0.14);
    border-radius: 24px;
    box-shadow: 0 18px 40px rgba(86, 57, 37, 0.08);
  }

  .forge-pullquote p {
    max-width: none;
    margin: 0;
    text-align: center;
    font-family: 'Playfair Display', serif;
    font-size: clamp(1.5rem, 3.8vw, 2.25rem);
    line-height: 1.34;
    color: var(--forge-ink);
  }

  .forge-essay h2 {
    counter-increment: forge-section;
    font-family: 'Playfair Display', serif;
    font-size: clamp(1.75rem, 4vw, 2.45rem);
    line-height: 1.08;
    font-weight: 500;
    letter-spacing: -0.02em;
    color: var(--forge-ink);
    text-align: center;
    max-width: 15ch;
    margin: 0 auto 2rem;
  }

  .forge-essay h2::before {
    content: counter(forge-section, upper-roman);
    display: block;
    margin: 0 0 0.85rem;
    font-family: 'Instrument Sans', sans-serif;
    font-size: 0.72rem;
    letter-spacing: 0.36em;
    text-transform: uppercase;
    color: var(--forge-accent-soft);
  }

  .forge-essay h2::after {
    content: "";
    display: block;
    width: 74px;
    height: 1px;
    margin: 1.15rem auto 0;
    background: var(--forge-rule);
  }

  .forge-divider {
    display: flex;
    align-items: center;
    gap: 0.9rem;
    max-width: 420px;
    margin: 3.75rem auto 3.2rem;
  }

  .forge-divider span:first-child,
  .forge-divider span:last-child {
    height: 1px;
    flex: 1;
    background: linear-gradient(90deg, transparent 0%, rgba(130, 92, 61, 0.22) 100%);
  }

  .forge-divider span:last-child {
    background: linear-gradient(90deg, rgba(130, 92, 61, 0.22) 0%, transparent 100%);
  }

  .forge-divider span:nth-child(2) {
    font-size: 1rem;
    color: var(--forge-accent-soft);
  }

  .forge-essay p,
  .forge-essay ul,
  .forge-essay ol,
  .forge-essay blockquote,
  .forge-essay pre {
    max-width: 740px;
    margin-left: auto;
    margin-right: auto;
  }

  .forge-essay p,
  .forge-essay li {
    font-size: 1.08rem;
    line-height: 1.88;
    color: var(--forge-soft);
  }

  .forge-essay p {
    margin-bottom: 1.2rem;
  }

  .forge-essay strong {
    color: var(--forge-ink);
  }

  .forge-essay ul,
  .forge-essay ol {
    margin-top: 1.2rem;
    margin-bottom: 1.5rem;
    padding-left: 1.35rem;
  }

  .forge-essay li {
    margin: 0.42rem 0;
    padding-left: 0.18rem;
  }

  .forge-essay code {
    font-size: 0.92em;
    background: rgba(81, 53, 35, 0.07);
    border-radius: 6px;
    padding: 0.1em 0.35em;
  }

  .forge-essay blockquote {
    padding: 1.1rem 1.2rem;
    border-left: 3px solid rgba(142, 69, 35, 0.38);
    background: rgba(255, 255, 255, 0.45);
    border-radius: 0 16px 16px 0;
  }

  .forge-diagram {
    max-width: 860px;
    margin: 1.8rem auto 2rem;
    padding: 1.1rem;
    background: rgba(255, 255, 255, 0.68);
    border: 1px solid rgba(103, 70, 45, 0.12);
    border-radius: 24px;
    box-shadow: 0 18px 36px rgba(86, 57, 37, 0.06);
  }

  .forge-diagram .mermaid {
    background: transparent !important;
  }

  .forge-diagram p {
    text-align: center;
    margin-top: 1rem;
    font-family: 'Instrument Sans', sans-serif;
    font-size: 0.82rem;
    line-height: 1.55;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--forge-muted);
  }

  .forge-diagram-caption {
    max-width: 740px;
    margin: 1rem auto 0;
    text-align: center;
    font-family: 'Instrument Sans', sans-serif;
    font-size: 0.82rem;
    line-height: 1.55;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--forge-muted);
  }

  .forge-essay h3 {
    max-width: 740px;
    font-size: 0.76rem;
    color: var(--forge-muted);
    margin: 0 0 1rem;
  }

  .forge-endgrid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1.35rem;
    max-width: 900px;
    margin: 4rem auto 0;
  }

  .forge-card {
    padding: 1.45rem 1.35rem 1.55rem;
    border-radius: 22px;
    background: rgba(255, 255, 255, 0.72);
    border: 1px solid rgba(104, 71, 46, 0.14);
    box-shadow: 0 16px 34px rgba(86, 57, 37, 0.06);
  }

  .forge-card h4 {
    font-size: 0.75rem;
    color: var(--forge-muted);
    margin: 0 0 0.9rem;
  }

  .forge-card p,
  .forge-card ul {
    max-width: none;
  }

  .forge-card ul {
    margin-bottom: 0;
  }

  @media (max-width: 720px) {
    .forge-essay {
      padding-top: 1.25rem;
    }

    .forge-opening p:first-child,
    .forge-essay p,
    .forge-essay li {
      font-size: 1rem;
    }

    .forge-pullquote {
      padding: 1.45rem 1.2rem 1.6rem;
      border-radius: 20px;
    }

    .forge-endgrid {
      grid-template-columns: 1fr;
    }
  }
</style>

<div class="forge-progress" aria-hidden="true"></div>

<div class="forge-essay" markdown="1">

<header class="forge-hero">
  <p class="forge-eyebrow">Essay • March 6, 2026</p>
  <h1>From AI Studio to AI Forge</h1>
  <p class="forge-subtitle">My process is moving from collaborating with models inside a room toward building the operating machinery behind the room.</p>
  <p class="forge-meta">Braydon McCormick · Means of Production</p>
  <div class="forge-rule"></div>
</header>

<div class="forge-hero-image" data-reveal markdown="1">

![](/assets/images/from-ai-studio-to-ai-forge-hero.png)
*Still figuring out the right visual language for this, but this gets close.*

</div>

<div class="forge-opening" markdown="1">

A while back I wrote about the idea of an AI studio. That was the right metaphor for that moment. It captured something important: I was no longer asking a chatbot for outputs; I was staging a room, directing work, managing loops, and using models more like specialists than vending machines.

But over the last few months I've realized the studio metaphor is starting to fall short.

The question I'm working on now isn't just, "How do I collaborate with models well?" It's more like: what would it look like if the room itself started to operate? Not in some magical fully autonomous sense. I don't mean "push a button and the company runs itself." I mean something much more bounded and much more practical: repos, workflows, checks, handoffs, and follow-up loops that keep moving, correcting, and recording with much less direct intervention from me.

That's the shift.

I think I'm moving from AI studio to AI forge.

I should note: "AI Forge" is not a finished product name or some grand theory I'm claiming to have completed. It's more like the least-wrong phrase I have right now for the direction my thinking is going. And, as usual with this stuff, I reserve the right to rename it again in six weeks.

If I'm honest, I think what I'm really driving toward is my own bounded dark factory. There, I said it. That phrase still sounds a little dramatic to me, but it is increasingly the direction I see in the work.

</div>

<aside class="forge-pullquote" data-reveal>
  <p>The unit is no longer just the prompt or the agent. It is the operating loop.</p>
</aside>

## The posts were checkpoints, not contradictions

If I look back over the last year or so, I can see a pretty clear progression in how I've been trying to name what I was doing.

- ["Vibe coding"](https://dbmcco.github.io/2025/05/28/my-vibe-coding-process-atm/) was really about discovering that I could build at all.
- The early [CLI journey](https://dbmcco.github.io/2025/05/30/The-CLI-LLM-Agent-Journey-so-far/) and [agentic model](https://dbmcco.github.io/2025/06/30/the-agentic-model-for-the-moment/) posts were about context control and process discipline.
- The [workflow and business acceleration post](https://dbmcco.github.io/2025/09/03/how-im-integrating-ai-into-my-workflow-for-business-acceleration/) was about tying the models into actual operating systems.
- The [AI studio post](https://dbmcco.github.io/2025/11/05/building-an-ai-studio/) was about the collaborative mental model.
- The [intuition post](https://dbmcco.github.io/2025/12/22/developing-intuition-for-cli-based-ai-coding/) was about how to smell when the models are going wrong.

All of those were right. None of them were enough.

What they were mostly describing, though, was my relationship to the models inside a session or a project. What they weren't fully naming was the next layer up: the operating fabric that sits above the individual session and keeps the whole thing from dissolving into chaos.

So what's the mental model gap now?

I think most people still think in one of three units:

1. The prompt
2. The agent
3. The collaborator

Those all matter. But the unit that increasingly matters to me is the loop.

Not the one-shot output. Not even the single agent. The loop: observe, decide, execute, verify, record, learn.

Once you start thinking that way, a lot of the conversation changes.

<div class="forge-divider" data-reveal><span></span><span>✦</span><span></span></div>

## The real shift in my head

The biggest change is that I'm no longer primarily asking, "Can the model do this task?"

I'm asking different questions now:

- What keeps this workflow healthy?
- Where does drift show up?
- What has to be verified?
- What is safe to automate?
- What needs a human decision versus a human glance?
- How does the system leave a trail so the next model, or the next human, can pick it up without losing the thread?

That's a different problem. It's less about prompting and more about governance, continuity, and return on expense.

To put it more bluntly: the value isn't "better AI answers." The value is lower friction in the operating system. Fewer broken handoffs. Fewer forgotten decisions. Earlier detection of stalls. Smaller costs when something breaks. Better continuity across repos, workflows, and business systems.

So the shift in my head looks something like this:

- From sessions to systems
- From output quality to workflow continuity
- From collaboration to orchestration
- From "what did the model say?" to "what does the loop do?"
- From clever prompting to model-mediated governance

That last phrase, model-mediated, is important to me, and I should probably define it more carefully than I usually do.

In the architecture work I've been doing, model-mediated does not mean the model directly owns side effects. It means the model owns judgment, intent, routing, timing, and interpretation. Deterministic systems own execution, evidence, and audit trails. Or more simply: the model decides what something means and what should happen next; code executes through a governed work surface and leaves artifacts behind.

That distinction matters because otherwise you get one of two bad outcomes: brittle rules pretending to be intelligence, or ungoverned model behavior pretending to be autonomy. Neither is very interesting. What I'm after is truthfulness-by-construction: if the system claims something happened, there should be work items, artifacts, or execution traces behind that claim.

<div class="forge-divider" data-reveal><span></span><span>✦</span><span></span></div>

## What I mean by AI Forge

"AI studio" described the room.

"AI Forge" is my current attempt to describe the machinery behind the room.

A forge is not just a place where an artisan thinks beautiful thoughts. It's heat, tools, sequence, repetition, discipline, shaping, reheating, reshaping, and quality control. Things move through it. They come out altered. There is craft in it, but there is also process.

That's closer to what I'm after now.

If I map it to the architecture docs, AI Forge is not one monolithic super-agent. It's closer to a stack:

- a model plane where judgment and interpretation happen
- an execution plane where deterministic systems run the side effects
- a memory plane where trajectory, identity, and working context are managed
- a governance plane where approvals, policy, and autonomy tiers live
- an integration plane where tools, MCPs, APIs, and external systems get touched

The reason I care about that split is that it keeps the roles clean. Models judge. Runners execute. Memory carries continuity. Governance defines what can happen without me. Observability tells me what actually happened.

When I say AI Forge, I mean a model-mediated operating layer that can:

- keep work moving across multiple repos and workflows
- surface drift, pressure, and dependency problems early
- emit bounded follow-up work
- preserve trail and context
- let a human stay at the level of policy, judgment, and strategic redirection more often than brute-force coordination

If the studio is where I collaborate with the models, the forge is where that collaboration starts becoming operational infrastructure.

<div class="forge-divider" data-reveal><span></span><span>✦</span><span></span></div>

## Why Speedrift matters so much to me

This is where the `speedrift` ecosystem comes in, and why I keep circling back to it.

Speedrift started, in my head and in practice, much closer to a repo-local drift checker. Useful, yes, but narrower. Over time it has evolved into something much more interesting: a multi-repo, model-mediated operations system with bounded autonomy. That matters because it forces the right questions.

Not:

- Can the agent finish this task?

But:

- Which repos are healthy?
- Which ones are stalled?
- Where are the dependency bottlenecks?
- What corrective work can be emitted safely?
- What should be logged, verified, or escalated?
- How does the system improve itself without becoming opaque?

The mental model shift in the Speedrift docs is actually the mental model shift in my own head:

- repo-local lane runner -> multi-repo operating fabric
- one-off checks -> continuous cycle
- scattered logs -> narrated dashboard and ledgers
- ad hoc intervention -> bounded corrective automation

That is very close to the core of what I mean by AI Forge.

Speedrift, to me, is not just a tool. It's one of the first real proving grounds for the dark-factory idea. Or maybe "crucible" is the better word, given the forge metaphor.

<div class="forge-divider" data-reveal><span></span><span>✦</span><span></span></div>

## So what do I mean by a "dark factory"?

Probably worth defining, since that phrase can sound either exciting or insane depending on your mood.

I should also say: I didn't invent the dark-factory metaphor. I'm borrowing it from the manufacturing idea of a lights-out or dark factory, where an automated plant can run in the dark because it doesn't need people on the floor all the time. I'm borrowing that metaphor for software and operational systems, but with a lot more caution and a lot more governance than the phrase can imply on first hearing.

I do **not** mean:

- no humans
- no oversight
- some magical AGI software company
- a black box making irreversible decisions while everybody sleeps

I mean something much more boring, which is exactly why I think it matters.

A dark factory, as I'm using the term, is a workflow environment that can keep itself operating, improving, coordinating, and recovering with low human intervention, while still staying inside clear policy and verification boundaries.

In other words:

- services restart when they should
- stalled work gets noticed
- broken dependency chains get surfaced
- corrective tasks get emitted
- verification gates still matter
- the system leaves a trail
- humans can step in at the right altitude

That last part is the real point. The human doesn't disappear. The human changes altitude.

Instead of manually pushing every wheel, the human is setting policy, reviewing exceptions, making strategic calls, and deciding when the system has earned more autonomy or needs less of it.

That is a much more interesting model than either "AI assistant" or "fully autonomous agent."

<div class="forge-divider" data-reveal><span></span><span>✦</span><span></span></div>

## Where Light Forge Works fits

One reason I think this way so much now is that Light Forge Works sits right at the edge between the visible and the invisible sides of this problem.

In the Light Forge world this is already starting to surface in a concrete way. ForgeWorks Core is explicitly being framed as a model-mediated operational backbone: chat as the human interface, deterministic work items for side effects, approvals for critical actions, and artifacts as the thing that backs the record. That feels important to me because it means AI Forge isn't just a blog metaphor. Pieces of it are already showing up in the architecture.

Light Forge Works is the outward-facing business. It's the promise to clients: we can take a messy workflow, de-risk it, and build a single-purpose application or system that actually improves the way work moves.

AI Forge, if the term sticks, is the inward-facing layer. It's the machinery I increasingly think needs to exist underneath that promise if a very small team is going to operate at a level that used to require many more people.

One way of putting it - maybe too neatly, but I think it's directionally right - is this:

- **Light Forge Works** is the visible forge: the work clients see, the workflow transformation, the applications, the service layer.
- **AI Forge** is the operating substrate behind it: the loops, ledgers, checks, context systems, control planes, and bounded automation that make the visible work possible.
- **The dark factory** is the operating condition I'm aiming toward: not perfection, not full autonomy, but a system that keeps a surprising amount of itself moving.

That distinction matters because otherwise people hear this stuff and think it's all just "Braydon likes AI tooling."

No. I like operating systems. I like reducing friction. I like structure from complexity. The models happen to be the new material.

<div class="forge-divider" data-reveal><span></span><span>✦</span><span></span></div>

## Visual: The shift I think I'm making

<div class="mermaid-container forge-diagram" data-reveal>
  <div class="mermaid">
flowchart TD
    Human["Human policy, judgment, strategy"]
    LFW["Light Forge Works<br/>client delivery + workflow transformation"]
    AIF["AI Forge<br/>model-mediated operating fabric"]
    S["Speedrift ecosystem<br/>proving ground / control plane"]

    O["Observe"]
    D["Decide"]
    E["Execute"]
    V["Verify"]
    R["Record"]
    L["Learn"]

    Human --> AIF
    AIF --> LFW
    S --> AIF

    O --> D
    D --> E
    E --> V
    V --> R
    R --> L
    L --> O

    AIF --> O
    AIF --> D
    AIF --> E
    AIF --> V
    AIF --> R
    AIF --> L
  </div>
</div>

<p class="forge-diagram-caption" data-reveal><em>The unit is no longer just the prompt or the agent. It's the operating loop.</em></p>

<div class="forge-divider" data-reveal><span></span><span>✦</span><span></span></div>

## Why I think this matters beyond coding

I don't actually think the long-term impact here is mainly about software development, even though that's where a lot of the sharpest experimentation is happening.

I think the deeper shift is that business operators - people who understand workflow, economics, customer reality, constraints, and governance - are going to be able to shape software and systems much more directly than before.

Not because code stops mattering. Code absolutely matters. Verification matters. Architecture matters. But the bottleneck begins to move.

The bottleneck becomes:

- clarity of workflow
- quality of governance
- ability to detect drift
- quality of context design
- discipline around verification
- knowing what not to automate

That is a very different landscape.

If AI Forge or things like it become real, I think the impact looks something like this:

- very small high-trust teams operating with much more leverage
- more business-native software because operators can shape it directly
- a tighter connection between strategy and implementation
- faster iteration on operational systems
- better return on expense for focused, governed automation

The part I keep coming back to is that the repo, the workflow, the CRM, the notes, the queue, the deployment surface, the logs - these increasingly start to feel like one connected operating surface rather than separate tools.

That's the future impact I can see, at least from where I'm standing.

<div class="forge-divider" data-reveal><span></span><span>✦</span><span></span></div>

## The honest part: I am not there yet

I should note: none of this is finished. Not even close.

There are still real problems everywhere:

- model drift is real
- context rot is real
- verification burden is still high
- UI/UX work is still painful
- broad autonomy still breaks in stupid ways
- model confidence is still a terrible proxy for correctness

And the more ambitious the loop, the more dangerous the failure mode if you don't have strong governance.

That is why I keep returning to the boring stuff:

- test gates
- hooks
- ledgers
- explicit policies
- bounded actions
- rollback paths
- clear trail and handoff context

Without those, this is a toy. Or worse, a chaos amplifier.

So I am not arguing for surrendering judgment to models. I am arguing for designing better systems in which models can do more useful work without putting the whole operation at risk.

<div class="forge-divider" data-reveal><span></span><span>✦</span><span></span></div>

## So what's the takeaway?

I think the studio metaphor got me to the right place for a while. It taught me to stop treating models like vending machines and start treating them like collaborators inside a designed room.

But now I'm trying to think one layer above that.

I'm trying to understand what it means to build the forge behind the studio.

That's where `speedrift` feels important to me. That's where the dark-factory language starts to feel useful. That's where Light Forge Works and this emerging idea of AI Forge begin to connect.

If the next year goes the way I think it might, the real change won't be that I got better at prompting or built a few more apps.

It will be that the operating loops themselves became more coherent, more visible, more bounded, and more capable of keeping work moving.

That, to me, is the real prize.

Whether "AI Forge" turns out to be the right name for it, I don't know yet. But it is the name that currently helps me see the shape of the thing.

And right now, that feels useful.

<div class="forge-endgrid" data-reveal">
  <div class="forge-card" markdown="1">

#### Process note

This draft was written with Codex helping me structure and tighten the argument while I pushed on the framing and the distinctions. It used my dossier as part of that process, which was itself derived from my writing style and my meeting transcripts, so the goal was not just to get the ideas down but to get them down in a voice that actually sounds like me. The hero image was generated with `grok-aurora-cli` because I wanted a visual that sat somewhere between workshop, control room, and operating metaphor.

  </div>
  <div class="forge-card" markdown="1">

#### Related posts / references

- [My 'Vibe Coding' Process ATM](https://dbmcco.github.io/2025/05/28/my-vibe-coding-process-atm/)
- [The CLI LLM Agent Journey So Far](https://dbmcco.github.io/2025/05/30/The-CLI-LLM-Agent-Journey-so-far/)
- [My agentic model at the end of June 2025](https://dbmcco.github.io/2025/06/30/the-agentic-model-for-the-moment/)
- [How I'm integrating AI into my workflow for business acceleration](https://dbmcco.github.io/2025/09/03/how-im-integrating-ai-into-my-workflow-for-business-acceleration/)
- [The Mindset Gap: How an AI Studio Changed My Workflow](https://dbmcco.github.io/2025/11/05/building-an-ai-studio/)
- [Developing intuition for CLI-based AI coding](https://dbmcco.github.io/2025/12/22/developing-intuition-for-cli-based-ai-coding/)
- [Speedrift Ecosystem](https://github.com/dbmcco/speedrift-ecosystem)

  </div>
</div>

</div>

<script>
  document.addEventListener("DOMContentLoaded", () => {
    const progress = document.querySelector(".forge-progress");
    const updateProgress = () => {
      const scrollTop = window.scrollY;
      const maxScroll = document.documentElement.scrollHeight - window.innerHeight;
      const pct = maxScroll > 0 ? (scrollTop / maxScroll) * 100 : 0;
      if (progress) progress.style.width = pct + "%";
    };

    const revealEls = document.querySelectorAll("[data-reveal]");
    const revealObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("forge-visible");
          revealObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });

    revealEls.forEach((el) => revealObserver.observe(el));
    updateProgress();
    document.addEventListener("scroll", updateProgress, { passive: true });
  });
</script>
