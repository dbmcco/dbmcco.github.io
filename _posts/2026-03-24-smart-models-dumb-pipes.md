---
id: 3a7c8d91-2e4f-4b5a-9c1d-8f6e2b0a3c5d
layout: post
title: "Smart Models, Dumb Pipes"
date: 2026-03-24 09:00:00 -0500
categories: development ai architecture
tags: [ai, architecture, model-mediated, multi-agent, lfw, draftforge]
mermaid: true
description: "Most people are using LLMs as question-answering machines. That's not wrong, it's just not the interesting part."
---
<style>
  @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,500;8..60,600&family=Instrument+Sans:wght@400;500;600&display=swap');

  .post-header { display: none; }

  .site-header {
    position: relative;
    overflow: hidden;
    background:
      radial-gradient(circle at 50% 120%, rgba(245, 236, 223, 0.92) 0%, rgba(245, 236, 223, 0) 42%),
      linear-gradient(135deg, #5c281d 0%, #8e4523 48%, #d98d53 100%) !important;
    border-bottom: 1px solid rgba(92, 40, 29, 0.14) !important;
    box-shadow: inset 0 -1px 0 rgba(255, 247, 239, 0.18), 0 14px 34px rgba(70, 39, 25, 0.12) !important;
    margin-bottom: 0 !important;
    padding: 2rem 0 1.25rem !important;
  }

  .site-header .wrapper { max-width: 980px !important; gap: 1.1rem !important; }
  .site-header .site-title { color: #fff7ef !important; text-shadow: 0 1px 2px rgba(44, 21, 12, 0.24) !important; }
  .site-header .site-nav { background: rgba(255, 247, 239, 0.14) !important; border: 1px solid rgba(255, 247, 239, 0.22) !important; backdrop-filter: blur(10px); }

  .page-content {
    background:
      radial-gradient(circle at top, rgba(193, 114, 61, 0.18), transparent 32%),
      linear-gradient(180deg, #f5ecdf 0%, #f8f2e8 30%, #fcf8f2 100%);
  }

  .page-content .wrapper { max-width: 980px !important; padding: 0 1.4rem !important; }

  .forge-progress {
    position: fixed; top: 0; left: 0; width: 0; height: 3px;
    background: linear-gradient(90deg, #8e4523 0%, #d98d53 100%);
    z-index: 9999; box-shadow: 0 0 18px rgba(217, 141, 83, 0.35);
  }

  .forge-essay {
    --forge-ink: #231a14; --forge-soft: #59493e; --forge-muted: #857160;
    --forge-rule: rgba(130, 92, 61, 0.28); --forge-accent: #8e4523; --forge-accent-soft: #d98d53;
    font-family: 'Source Serif 4', Georgia, serif;
    color: var(--forge-ink);
    padding: 2.5rem 0 5rem;
  }

  .forge-essay a { color: var(--forge-accent); text-decoration-color: rgba(142, 69, 35, 0.35); text-underline-offset: 0.18em; }

  .forge-hero { text-align: center; padding: 1.5rem 0 2rem; }

  .forge-eyebrow, .forge-meta, .forge-essay h3 {
    font-family: 'Instrument Sans', sans-serif;
    letter-spacing: 0.22em; text-transform: uppercase;
  }

  .forge-eyebrow { font-size: 0.72rem; color: var(--forge-muted); margin: 0 0 1rem; }

  .forge-hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2.8rem, 8vw, 4.85rem);
    line-height: 0.98; font-weight: 500; letter-spacing: -0.02em;
    color: var(--forge-ink); max-width: 12ch; margin: 0 auto 1rem;
  }

  .forge-subtitle {
    font-family: 'Playfair Display', serif; font-style: italic;
    font-size: clamp(1.18rem, 3vw, 1.6rem); color: var(--forge-soft);
    max-width: 52ch; margin: 0 auto 1.2rem; line-height: 1.45;
  }

  .forge-meta { font-size: 0.72rem; color: var(--forge-muted); margin: 0; }
  .forge-rule { width: 2.5rem; height: 1px; background: var(--forge-rule); margin: 1.4rem auto 0; }

  .forge-opening p, .forge-essay > p, .forge-essay > ul, .forge-essay > ol {
    font-size: clamp(1.05rem, 2vw, 1.2rem); line-height: 1.75;
    max-width: 68ch; margin: 0 auto 1.4rem;
  }

  .forge-opening p:first-child::first-letter {
    font-family: 'Playfair Display', serif; font-size: 3.4em; font-weight: 500;
    float: left; line-height: 0.82; margin: 0.07em 0.06em 0 0; color: var(--forge-accent);
  }

  .forge-essay h2 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(1.5rem, 3.5vw, 2rem); font-weight: 500; letter-spacing: -0.01em;
    color: var(--forge-ink); max-width: 68ch; margin: 3rem auto 1rem; line-height: 1.2;
  }

  .forge-essay h3 { max-width: 740px; font-size: 0.76rem; color: var(--forge-muted); margin: 0 0 1rem; }

  .forge-pullquote {
    background: rgba(255, 248, 240, 0.9); border-left: 3px solid var(--forge-accent-soft);
    padding: 1.6rem 1.8rem 1.7rem; border-radius: 0 18px 18px 0;
    max-width: 64ch; margin: 2.2rem auto;
  }

  .forge-pullquote p {
    font-family: 'Playfair Display', serif; font-style: italic;
    font-size: clamp(1.1rem, 2vw, 1.3rem); line-height: 1.5;
    color: var(--forge-soft); margin: 0 !important; max-width: none !important;
  }

  .forge-divider {
    display: flex; align-items: center; gap: 0.75rem;
    max-width: 68ch; margin: 2.5rem auto; color: var(--forge-muted); font-size: 0.8rem;
  }

  .forge-divider span:first-child, .forge-divider span:last-child {
    flex: 1; height: 1px; background: var(--forge-rule);
  }

  .forge-callout {
    background: rgba(255, 255, 255, 0.72); border: 1px solid rgba(104, 71, 46, 0.16);
    border-radius: 18px; padding: 1.4rem 1.6rem 1.5rem; max-width: 68ch; margin: 2rem auto;
    box-shadow: 0 8px 24px rgba(86, 57, 37, 0.06);
  }

  .forge-callout h4 {
    font-family: 'Instrument Sans', sans-serif; font-size: 0.7rem;
    letter-spacing: 0.22em; text-transform: uppercase; color: var(--forge-muted); margin: 0 0 0.75rem;
  }

  .forge-callout p, .forge-callout ul {
    font-size: 1rem; line-height: 1.65; color: var(--forge-soft); margin: 0 0 0.75rem;
  }

  .forge-callout ul { padding-left: 1.2rem; }
  .forge-callout p:last-child, .forge-callout ul:last-child { margin-bottom: 0; }

  .forge-essay ul, .forge-essay ol { padding-left: 1.4rem; }

  .forge-essay li {
    font-size: clamp(1.05rem, 2vw, 1.2rem); line-height: 1.7; margin-bottom: 0.4rem; max-width: 64ch;
  }

  .forge-process {
    border-top: 1px solid var(--forge-rule); padding-top: 2rem; margin-top: 3.5rem;
    max-width: 68ch; margin-left: auto; margin-right: auto;
  }

  .forge-process p, .forge-process ul {
    font-size: 0.95rem; color: var(--forge-muted); line-height: 1.65; margin-bottom: 0.75rem;
  }

  .forge-process h3 { margin-bottom: 0.75rem !important; }

  .forge-hero-image {
    width: 100%; max-width: 980px; margin: 0 auto 2.5rem;
    border-radius: 12px; overflow: hidden;
    box-shadow: 0 18px 48px rgba(70, 39, 25, 0.18);
  }

  .forge-hero-image img {
    width: 100%; height: auto; display: block;
    object-fit: cover;
  }

  .forge-hero-image figcaption {
    font-family: 'Instrument Sans', sans-serif;
    font-size: 0.7rem; letter-spacing: 0.12em; text-transform: uppercase;
    color: var(--forge-muted); text-align: center;
    padding: 0.6rem 1rem; background: rgba(245, 236, 223, 0.6);
  }
</style>

<div class="forge-progress" aria-hidden="true"></div>

<div class="forge-essay" markdown="1">

<header class="forge-hero">
  <p class="forge-eyebrow">Essay · March 24, 2026</p>
  <h1>Smart Models, Dumb Pipes</h1>
  <p class="forge-subtitle">Most people are using LLMs as question-answering machines. That's not wrong, it's just not the interesting part.</p>
  <p class="forge-meta">Braydon McCormick · Means of Production</p>
  <div class="forge-rule"></div>
</header>

<figure class="forge-hero-image" data-reveal>
  <img src="/assets/images/smart-models-friction-hero.jpg" alt="A lone knowledge worker at a desk, golden streams of information converging from all directions, pooling in amber around them, a few threads racing away as cool blue light." />
  <figcaption>Where human judgment creates drag and exposure, that's where the interesting work is.</figcaption>
</figure>

<div class="forge-opening" markdown="1">

I keep saying "smart models, dumb pipes" in conversations and then moving on like I've explained something. I haven't, really. So here's my actual attempt to unpack it.

The phrase borrows from an old argument in network architecture, one I think got settled the right way and hasn't gotten enough credit for the lesson it contains.

</div>

<aside class="forge-pullquote" data-reveal>
  <p>When you put the intelligence in the pipe, the pipe becomes the bottleneck. Every new use case requires changing the infrastructure.</p>
</aside>

## Where the phrase comes from

In the early internet era, there was a real debate about whether network intelligence should live in the network itself or at the edges. The traditional telephone network was what people called an intelligent network: switching logic, routing decisions, and service features were all baked into the infrastructure. The internet took the other side: dumb pipes. The network just moves packets. It doesn't know, and doesn't need to know, what's in them. The intelligence lives at the endpoints.

That design won, decisively. And I think the reason it won is worth holding onto: when you put the intelligence in the pipe, the pipe becomes the bottleneck. Every new use case requires changing the infrastructure. When the pipe is dumb and the endpoints are smart, the system stays flexible. New things become possible without rebuilding what's underneath.

I keep thinking about how directly that maps to AI. Kind of uncomfortably so.

<div class="forge-divider" data-reveal><span></span><span>✦</span><span></span></div>

## What most people's mental model actually is

Most people's mental model of an LLM comes from the chat box. You type something in, it responds. That's how I started with these things too, and there's real value in it, I'm not arguing against it.

But I think the chat box trains you toward a particular framing: LLM as question-answering machine. Ask something, get something back. Better prompt, better answer. Optimize the input, improve the output.

That's fine as a framing for a tool, though. It's not a useful framing for a system.

The cost is subtle. Once you're in the Q&A frame, you start optimizing for the wrong variable. You get "AI strategy" that's really prompt strategy. You get enterprise products that are basically search with a chat front end. You get the question of how to get AI to answer employees' questions faster, which is a real question, but it's the narrow version of what's actually available.

The return on expense question for AI, as I think about it, isn't "are the answers better?" It's "where does judgment belong in the workflow, and what does it cost when that judgment is wrong?"

Those are very different questions.

<div class="mermaid-container forge-diagram" data-reveal>
  <div class="mermaid">
flowchart LR
    subgraph qa ["The Q&A Frame"]
        direction LR
        q1["Prompt"] --> q2["Model"] --> q3["Answer"]
    end
    subgraph jl ["The Judgment Layer"]
        direction TB
        j1["Context + Task"] --> j2["Model\nJudges what should happen"]
        j2 -->|routing call| j3["Dumb Pipe\ncarries it faithfully"]
        j3 -->|governed execution| j4["Side Effects\n+ Audit Trail"]
    end
  </div>
</div>

<p class="forge-diagram-caption" data-reveal><em>The Q&A frame optimizes for the answer. The judgment layer asks what should happen and who should do it.</em></p>

<div class="forge-divider" data-reveal><span></span><span>✦</span><span></span></div>

## What I think these things actually are

Not a search engine with better grammar. Search retrieves. A model reasons. Those aren't different in degree, they're different in kind.

Not a chatbot that got promoted. A chatbot routes inputs to predefined outputs. A model interprets context and decides what the output should be.

What I keep coming back to: an LLM is a **judgment machine**. Something that can hold a problem, reason over a space of possibilities, weigh competing options, and produce a decision about what should happen next.

Not retrieval. Judgment.

There, I said it.

I should note: that judgment doesn't come ready-made. Models don't have inherent opinions. They don't arrive with a default point of view on your domain or workflow. Humans have to force the judgment function onto them, through focused, narrow system and user prompts that define what kind of reasoning is expected and from what angle. The "smart" in smart models isn't a product of the model in the abstract. It's the model given a specific thing to be smart about. A poorly scoped prompt into a capable model produces capable-sounding noise. That distinction matters more than most people realize when they're designing a system around this.

Once you start thinking about it that way, the question changes. It's no longer "what should I ask this?" It becomes: where does judgment belong in this system, and what should I route through it?

<div class="forge-divider" data-reveal><span></span><span>✦</span><span></span></div>

## The architecture that follows

If models are judgment machines, the design principle that follows is, I think, pretty straightforward.

**Smart models** own the judgment work: what should happen, why, when, in what order, which agents or processes are appropriate. The model decides what something means and what to do because of it.

**Dumb pipes** own the mechanical work: execution, delivery, storage, record-keeping, audit trails. The pipe moves data. It doesn't need to understand what it's carrying. It just needs to carry it faithfully and leave a trace.

I should note: model-mediated does not mean the model directly owns side effects. It means the model owns the judgment call, what should happen and why, and deterministic systems own the execution and the record.

Or more simply: the model decides; the infrastructure runs it.

That distinction matters because otherwise you get one of two failure modes I see constantly:

- Brittle rules pretending to be intelligence. Complex conditional logic someone built to simulate judgment, which breaks the moment the real world doesn't match the assumptions baked into the code.
- Ungoverned model behavior pretending to be an operating system. Outputs that aren't verified, logged, or traceable. "The model said so" as a source of truth. That's not a system. That's exposure.

Neither works. The clean separation is what makes it work.

<div class="forge-callout" markdown="1">

#### For the more technical reader

In a **deterministic orchestration** system, routing logic is hardcoded, if X then Y. Predictable, but brittle. It can only handle what the designer anticipated.

In a **model-mediated** system, the model makes routing calls dynamically based on context, task requirements, and available options. The pipe infrastructure is identical either way. What changes is who decides what goes into it, and whether that decision can be reasoned about and audited afterward.

This is, pretty directly, the dumb network argument applied to agents.

</div>

<div class="mermaid-container forge-diagram" data-reveal>
  <div class="mermaid">
flowchart TD
    SM["Smart Model\n──────────────\nJudgment · Routing · Intent\nInterpretation · Persona\nWhat should happen next?"]
    DP["Dumb Pipe\n──────────────\nCarries data faithfully\nDoesn't need to understand it\nLeaves a trace"]
    DE["Deterministic Execution\n──────────────\nSide effects · Storage\nAudit trail · Record"]

    SM -->|"judgment call"| DP
    DP -->|"execution instruction"| DE
    DE -.->|"artifacts + trail"| SM
  </div>
</div>

<p class="forge-diagram-caption" data-reveal><em>Models own judgment. Pipes carry it. Deterministic systems execute and record. The roles stay clean.</em></p>

<div class="forge-divider" data-reveal><span></span><span>✦</span><span></span></div>

## Three things I've built around this

**The expert panel simulator** is [public on GitHub](https://github.com/dbmcco/expert-panel-simulator), MIT licensed, so you can actually look at it. It's a Python tool that creates a virtual panel of domain experts to review any topic sequentially.

What it does: the model assembles the panel for the task. Economist, futurist, anthropologist, contrarian, others depending on what the problem needs. Each agent responds in character, reads what the previous agent said, and builds on it, qualifies it, or disagrees with it. The contrarian is always included. Not as a nice-to-have. It's structural; without it the panel tends toward false consensus.

The data flowing between agents is structured data moving through a pipe. The pipe doesn't know it's carrying a disagreement. That's the whole point. The model's job was deciding who's in the room. The pipe's job was moving the work between turns.

It's a demonstration more than a production system, but the pattern is real.

**DraftForge**, private. This applies the same principle inside a production content system. The model selects the right combination of agents for a task: what diversity of perspective is needed, what kind of challenge will sharpen rather than just validate. Agents work sequentially and contradict each other by design.

If I'm honest, the output is genuinely different from what a single prompt to a single model produces. You get something closer to deliberation than generation. That only works because the model owns the judgment layer. The pipes just carry the turns.

**Lodestar / Meridian**, also private. This one adds something the others don't: model tiering. Different model capabilities matched to different judgment functions in the same system.

Lodestar is a situation intelligence platform for scenario planning and decision de-risking. The interesting part here is how the model assignments work:

- **Haiku** runs intel classification in the background, automatically. Fast, cheap, and right-sized. It doesn't need to reason about geopolitical scenarios. It needs to classify whether a news signal is relevant and route it correctly.
- **Sonnet and Opus** handle the actual scenario reasoning and specialist analysis, the work that requires judgment.
- A three-tier **Factory Brain** (Haiku → Sonnet → Opus) watches the system infrastructure itself, restarts stalled processes, and escalates when something persists past what a lower tier can resolve.

<div class="mermaid-container forge-diagram" data-reveal>
  <div class="mermaid">
flowchart LR
    t1["Intel Classification\nfast · high-volume"] --> H["Haiku"]
    t2["System Supervision\nheartbeats · restarts"] --> H
    t3["Scenario Reasoning\nspecialist analysis"] --> S["Sonnet"]
    t4["Escalation\ncomplex judgment"] --> O["Opus"]

    H --> Inf["Model-Agnostic\nInfrastructure\nsame data structure\nregardless of tier"]
    S --> Inf
    O --> Inf
    Inf --> Out["Execution\n+ Record"]
  </div>
</div>

<p class="forge-diagram-caption" data-reveal><em>Right model for the right judgment function. The pipes don't know or care which tier ran.</em></p>

The infrastructure carries the same data structure regardless of which model tier produced the output. The pipes don't know, and don't need to know, whether Haiku or Opus ran. They just move it.

So it's not just smart models and dumb pipes. It's the *right* model matched to the *right* judgment function, all running through the same model-agnostic infrastructure. That's what the principle looks like when it's fully developed.

<div class="forge-divider" data-reveal><span></span><span>✦</span><span></span></div>

## The question I think matters more

Once you start seeing LLMs as judgment layers rather than answer machines, a lot of the "AI strategy" conversation starts to look like it's optimizing for the wrong thing.

There's a lot of work on how to get better answers. Not enough work on where judgment belongs in a workflow, who owns the execution, and what the pipe should actually carry.

The question I find more useful, and I think it's the question that leads somewhere, isn't "how do we add AI to this?"

It's: *where does judgment belong in this system, and what should the infrastructure just move?*

That second question is harder. It requires actually mapping the workflow, identifying the decision points, and being honest about what you want the model to own versus what should be governed by deterministic code with a proper audit trail.

One way I've found to get at it concretely: look for where human friction exists in a workflow, and what risk that friction carries. Slow judgment calls. Inconsistent ones. Decisions that are expensive when they're wrong, or that accumulate risk quietly over time. Those are the interesting places, not "where can AI answer questions?" but "where is human judgment creating drag or exposure?" That reframe tends to surface the actually valuable interventions. And it tends to surface them in places that aren't obvious from a high-level "let's add AI" conversation.

But it's the right question.

The chat box is a fine interface for exploration. It is not a system design.

The models happen to be the new material. The architecture is the old argument, finally applied somewhere it really fits.

<div class="forge-process" markdown="1">

### Process note

Part of a running series on how my thinking about AI development has evolved: [vibe coding](https://dbmcco.github.io/2025/05/28/my-vibe-coding-process-atm/), [CLI journey](https://dbmcco.github.io/2025/05/30/The-CLI-LLM-Agent-Journey-so-far/), [agentic model](https://dbmcco.github.io/2025/06/30/the-agentic-model-for-the-moment/), [workflow integration](https://dbmcco.github.io/2025/09/03/how-im-integrating-ai-into-my-workflow-for-business-acceleration/), [AI studio](https://dbmcco.github.io/2025/11/05/building-an-ai-studio/), [developing intuition](https://dbmcco.github.io/2025/12/22/developing-intuition-for-cli-based-ai-coding/), [AI forge](https://dbmcco.github.io/2026/03/06/from-ai-studio-to-ai-forge/).

Written with Claude Code assistance using my own voice dossier as the style anchor.

### Resources

- [expert-panel-simulator](https://github.com/dbmcco/expert-panel-simulator), public, MIT licensed
- DraftForge and Lodestar/Meridian (private); reach out if you want to talk architecture

</div>

</div>

<script>
  (function() {
    var prog = document.querySelector('.forge-progress');
    if (!prog) return;
    function update() {
      var s = document.documentElement;
      var pct = (s.scrollTop || document.body.scrollTop) / ((s.scrollHeight || document.body.scrollHeight) - s.clientHeight) * 100;
      prog.style.width = Math.min(pct, 100) + '%';
    }
    window.addEventListener('scroll', update, { passive: true });
  })();
</script>
