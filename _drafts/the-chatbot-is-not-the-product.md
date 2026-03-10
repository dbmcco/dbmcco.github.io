---
layout: post
title: "You don't want another chatbot"
date: 2026-03-09 15:00:00 -0400
categories: development ai workflow
tags: [ai, capabilities, lightforge, workflow, judgment]
mermaid: true
description: "What most people call AI is often just a chat interface sitting on top of a much bigger capability problem."
---

<style>
  .model-product-post {
    --mop-ink: #241b14;
    --mop-soft: #59493d;
    --mop-muted: #7b6a5c;
    --mop-accent: #8b4a23;
    --mop-accent-soft: #d39a66;
    --mop-wash: rgba(255, 248, 240, 0.82);
    --mop-rule: rgba(139, 74, 35, 0.18);
    color: var(--mop-ink);
  }

  .model-product-post details summary,
  .model-product-post .diagram-label {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    text-transform: uppercase;
    letter-spacing: 0.16em;
  }

  .model-product-post p,
  .model-product-post ul,
  .model-product-post ol,
  .model-product-post blockquote,
  .model-product-post details,
  .model-product-post figure {
    max-width: 740px;
    margin-left: auto;
    margin-right: auto;
  }

  .model-product-post p,
  .model-product-post li {
    font-size: 1.08rem;
    line-height: 1.82;
    color: var(--mop-soft);
  }

  .model-product-post h2,
  .model-product-post h3 {
    max-width: 740px;
    margin-left: auto;
    margin-right: auto;
  }

  .model-product-post h2 {
    margin-top: 3.1rem;
    margin-bottom: 1.1rem;
    font-size: clamp(1.75rem, 3vw, 2.35rem);
    line-height: 1.08;
    letter-spacing: -0.02em;
    color: var(--mop-ink);
  }

  .model-product-post h3 {
    margin-top: 2rem;
    margin-bottom: 0.7rem;
    font-size: 1.18rem;
    color: var(--mop-ink);
  }

  .model-product-post ul,
  .model-product-post ol {
    margin-top: 1rem;
    margin-bottom: 1.4rem;
    padding-left: 1.35rem;
  }

  .model-product-post li {
    margin: 0.35rem 0;
  }

  .model-product-post blockquote {
    padding: 1rem 1.15rem;
    border-left: 3px solid rgba(139, 74, 35, 0.38);
    background: rgba(255, 251, 247, 0.82);
    border-radius: 0 16px 16px 0;
  }

  .model-product-post details {
    margin-top: 1.1rem;
    margin-bottom: 1.6rem;
    padding: 0.95rem 1rem 1rem;
    background: linear-gradient(135deg, rgba(244, 232, 220, 0.65), rgba(255, 255, 255, 0.9));
    border: 1px solid var(--mop-rule);
    border-radius: 16px;
    box-shadow: 0 10px 26px rgba(69, 38, 22, 0.05);
  }

  .model-product-post details summary {
    cursor: pointer;
    color: var(--mop-accent);
    font-size: 0.72rem;
    margin-bottom: 0.7rem;
    list-style: none;
  }

  .model-product-post details summary::-webkit-details-marker {
    display: none;
  }

  .model-product-post details p:last-child,
  .model-product-post details ul:last-child {
    margin-bottom: 0;
  }

  .model-product-post .diagram-shell {
    max-width: 860px;
    margin: 1.5rem auto 2rem;
    padding: 1rem 1rem 0.7rem;
    background: var(--mop-wash);
    border: 1px solid var(--mop-rule);
    border-radius: 22px;
    box-shadow: 0 14px 34px rgba(69, 38, 22, 0.06);
  }

  .model-product-post .diagram-shell .mermaid {
    background: transparent !important;
  }

  .model-product-post .diagram-label {
    margin: 0.7rem 0 0.2rem;
    text-align: center;
    font-size: 0.72rem;
    color: var(--mop-muted);
  }

  .model-product-post .concept-figure {
    margin-top: 1.6rem;
    margin-bottom: 2rem;
  }

  .model-product-post .concept-figure img {
    display: block;
    width: 100%;
    border-radius: 18px;
    box-shadow: 0 14px 34px rgba(69, 38, 22, 0.08);
  }

  .model-product-post .concept-figure figcaption {
    margin-top: 0.75rem;
    font-size: 0.94rem;
    line-height: 1.5;
    color: var(--mop-muted);
    text-align: center;
    font-style: italic;
  }

  .model-product-post .bridge-note {
    max-width: 740px;
    margin: 2rem auto 0;
    padding: 1rem 1.1rem;
    background: rgba(255, 248, 241, 0.72);
    border: 1px solid rgba(139, 74, 35, 0.12);
    border-radius: 14px;
  }

  @media (max-width: 720px) {
    .model-product-post p,
    .model-product-post li {
      font-size: 1rem;
    }
  }
</style>

<div class="model-product-post" markdown="1">

Over the last week or so I have heard three different versions of the AI question.

One of the LightForge team told me about a prospect who wanted us to connect their Google Drive, email, and meeting notes and build a virtual me.

I also heard the quieter, very common version: I copied and pasted the document into Copilot and it just wasn't very good.

A friend told me he was using Grok to figure out whether a certain faucet would fit a code requirement, and whether that building code had been updated.

At first glance those sound like three different asks. I think they are actually three versions of a misunderstanding about where the power of AI really sits.

If I had to bucket them, the taxonomy is pretty simple:

1. AI as advanced retrieval and synthesis.
2. AI as a workbench assistant.
3. AI as a configured capability.

The faucet/building-code example lives mostly in the first bucket. The Copilot experience lives mostly in the second. The third is different. It is the system helping a bounded piece of work move correctly through a real workflow. The first two are real value. I use them constantly. But the actual business need usually lives one layer up, and, in my experience, people rarely know to ask for it directly. You more or less have to walk them to the idea before they can even see it.

So here is the mental model gap as I see it: people keep treating the model as though it is already the finished product. I do not think it is. I think it is much closer to raw cognitive horsepower. Useful, yes. Impressive, yes. Sometimes almost unsettlingly good. But not, by itself, the thing a business is actually buying.

Before going any further, I think it helps to see the two thought models side by side.

<figure class="post-figure concept-figure">
  <img src="{{ '/assets/images/the-chatbot-is-not-the-product-hero.png' | relative_url }}" alt="Editorial split illustration contrasting AI as a simple chatbot interaction with AI as a configured business capability">
  <figcaption>A Grok/Imagen sketch of the same contrast: on one side a chatbot sitting on top of a pile of work, on the other a more deliberate operating layer turning the work into decisions and next steps.</figcaption>
</figure>

_If you want the builder view, open the technical notes as you go. I tucked those throughout the post rather than turning the whole thing into a technical essay._

## The test most people are actually running

If you take a document, drop it into Copilot or ChatGPT, and ask a few good questions, you are running a pretty specific test. You are asking whether a general-purpose reasoning engine, with a thin interface around it, can produce a useful answer in a single interaction. Sometimes it can. Sometimes it really can. But that is not the same thing as asking whether AI can support a real business capability.

Those are different questions, and they fail in different ways.

If what you wanted was "turn this board memo into a crisp summary," "extract the open questions from this transcript," or "give me three good reactions to this draft," a thin interaction layer may be enough. But if what you really wanted was something more like "read this inbound RFP, compare it to our ICP, delivery capacity, pricing guardrails, redline history, and current pipeline, decide whether it is worth pursuing, surface the risks that actually matter, and hand the next step to the right person," then you have already moved into a different category of problem. That is no longer just a question-answering exercise. That is a stateful, policy-shaped, workflow-bound capability, whether you call it that or not.

I should note that this is one reason the current conversation around AI can feel slippery. People think they are evaluating the whole stack when they are often just evaluating a very thin slice of it.

## The model is the engine, not the vehicle

The easiest analogy I have found for this is still a mechanical one.

Part of that is probably just how my own head works. I love cars. I named one of my repos [`Speedrift`](https://github.com/dbmcco/speedrift-ecosystem) for a reason. I also have a private, curated, multi-tiered research engine that I use to stay on top of key topics and make decisions for myself. So when I reach for the word engine here, I do not mean "fast thing." I mean a system that turns raw power into directed, reliable motion. Intake matters. Tuning matters. Instrumentation matters. Transmission matters. What the engine is connected to matters.

If you hand someone a powerful engine, they do not yet have a delivery van, or a forklift, or a race car, or a tractor. They have a powerful component that can become one of those things if it is put into the right frame, connected to the right controls, and aimed at a specific job. The engine matters. It matters a lot. But no one confuses the engine with the finished vehicle unless they are being careless, or unless the technology is new enough that people are still dazzled by raw power.

I think frontier AI models are in that phase.

The model is the engine.

The finished business capability is the vehicle.

And I think a lot of present-day AI disappointment comes from confusing those two things. When someone says, "I tried Copilot and it wasn't very good," what I often hear is: "I put a powerful engine on the floor, sat on it, and it did not drive like a truck." That does not mean the engine is useless. It means there is more between raw power and useful work than people first assume.

<figure class="post-figure concept-figure">
  <img src="{{ '/assets/images/the-chatbot-is-not-the-product-engine-vs-vehicle.png' | relative_url }}" alt="Editorial illustration showing a raw engine on one side and a finished drivable vehicle system on the other">
  <figcaption>Another Grok/Imagen sketch of the same argument: raw power on its own is not yet the useful instrument.</figcaption>
</figure>

<details>
<summary>Tech note: I am not claiming foundation models do not matter</summary>

For a developer, model choice shows up in very concrete ways: schema adherence, function-call reliability, long-context degradation, tool-selection accuracy, latency variance, token economics, and how often the system needs retries or repair prompts. A stronger substrate reduces how much defensive scaffolding you need around the model.

But even with a frontier model, the application behavior you care about usually is not determined at the model boundary. The moment you need durable state, typed interfaces, constrained writes, multi-step control flow, evaluator passes, or escalation rules, you are already in application design. In practice, that is where a lot of the product differentiation lives. The model sets the ceiling on some classes of performance. It does not, by itself, define the operating behavior of the system.

</details>

## A capability is a different kind of thing

This is the core distinction I have been trying to sharpen for myself.

A model can generate text, summarize, classify, extract, answer, code, and generally behave in ways that look quite intelligent. Those are useful functions. But a business capability is something else. A business capability is a bounded, repeatable ability to get some important piece of work done.

That is why I think it helps to be much more precise about the unit of value.

"Retrieve the email" is a function. "Pull fields from the attachment" is a function. "Draft the reply" is a function. "Correctly handle inbound RFP requests and move them to the next step" is a capability.

Businesses do not really buy AI for its own sake. They buy improvements in how work gets done. They buy fewer dropped balls, fewer manual handoffs, fewer missed details, faster throughput, lower cost, lower friction, better decisions in workflows that actually matter. In other words, they buy a capability that changes the economics of a piece of work.

That is why I keep coming back to the same phrase: the model is not the product. The configured capability is the product.

<details>
<summary>Tech note: what I mean by "configured capability"</summary>

Think something closer to a typed service boundary than a clever prompt. A real capability usually has a state model, a context assembly layer, explicit tool contracts, a control loop, validators, evaluators, and rules about when writes are allowed. The system should know what object it is operating on, what state that object is in, what tools it is allowed to call, what success looks like, and what conditions require escalation.

In implementation terms, that often means structured inputs, schema-constrained outputs, idempotent tool calls, durable memory separated from transient context, and some kind of planner-orchestrator-evaluator pattern. Prompt text still matters. But prompt text without typed state, control flow, and observable failure handling is not a capability. It is an improvisation layer.

</details>

## Why the average chatbot interaction disappoints

I do not think the problem is mainly that the model is dumb. The problem is that a lot of the things people really want from AI are sitting one or two layers above what a basic chat interaction is designed to do.

The first missing layer is definition of what "good" actually means. A chatbot can often tell you what is in a document. It can sometimes tell you what seems important in a general sense. But that is not the same thing as knowing what matters in your organization, in this workflow, right now. Which customer is politically sensitive? Which delay is noise and which one is dangerous? Which recommendation sounds good in theory but would create chaos in practice? That kind of judgment is often not written down anywhere. It lives in people, habits, consequences, and memory.

The second missing layer is workflow. A chatbot gives you an answer. A capability has to fit into a real process. It has to know what starts the work, what comes next, who owns the next step, what system needs to be updated, what counts as done, and when to stop and ask for help. If you do not define those things, then even a smart answer may simply become one more output a human has to interpret and manually route.

The third missing layer is the ability to ignore the wrong things. This matters more than many people think. A lot of business judgment is not just about seeing what is present; it is about knowing what does not matter yet. If three vendors say an order may be delayed, should the system trigger a full remediation workflow? Maybe. Or maybe the right move is to flag it, wait a day, and see whether the signal hardens into something real. A thin chat interaction usually does not know that difference, because why would it?

The fourth missing layer is shaped context. People often say, "well, I gave it the file." Sure. But a file is not the same thing as usable operating context. Useful context is usually shaped. It has the right facts in the right structure with the right relationships attached to the right decisions inside the right boundary. That is different from "we uploaded a bunch of stuff."

I think about this the same way I think about my own research systems. The value is not that I can dump more articles into a feed. The value is that the feed is curated, tiered, and oriented around decisions. It has structure. It has priorities. It has different lanes for weak signals, developing stories, and things that actually deserve action. Raw information is abundant. Decision-grade context is designed.

And the fifth missing layer is repeatability. A good answer is nice. A repeatable business ability is better. A real capability has to work more than once, stay inside scope, fit into a workflow, expose mistakes, and operate with some consistency over time. That is a much higher bar than "this answer felt impressive."

<details>
<summary>Tech note: retrieval is not the same thing as representation</summary>

Retrieval answers a similarity question: what text chunks look most relevant to this query? Representation answers a state question: what objects exist in the system, what state are they in, and how are they related? Those are not the same operation.

A vector store can help recover useful evidence. It is a poor substitute for an addressable model of the world. If the system needs to know that a deal is in procurement, legal already approved fallback clause B, the client has a history of late approvals, and the margin floor is 32 percent, those should not be rediscovered from semantically adjacent chunks on every turn. They should exist as typed state or computable facts. When teams blur retrieval and representation together, they get systems that sound informed but behave inconsistently because the same underlying reality is being re-inferred from text each time instead of being referenced directly.

</details>

## So what does a real capability require?

Once I started thinking about AI this way, the architecture started to matter a lot more than the interface.

At a very practical level, I think a real AI capability usually requires six things. It needs a bounded job. It needs a reasonably clear definition of what good looks like. It needs the right structure underneath the work so it is not improvising its own schema as it goes. It needs some orchestration, because not every meaningful problem should be solved in one shot. It needs human judgment in the places where human judgment actually matters. And it needs boundaries, because a capability without edges tends to become a blob.

That last one is especially important. A useful capability should be able to answer both of these questions: what do I do, and what do I not do? If you skip the second question, the system tends to sprawl in exactly the way software usually sprawls: costs go up, expectations get fuzzy, and reliability starts to bend under the weight of ambiguity.

This is also why "make an AI version of me" is harder than it sounds. The naive version of that idea is: connect my inbox, connect my docs, connect my meetings, and now the system knows me. But that is not usually where the real expertise lives. Real expertise often includes what the person notices quickly, what they routinely discount, what they worry about before others do, what they treat as noise, what they escalate immediately, and what tradeoffs they make under pressure. That is not simply a document problem. It is partly a cognition problem and partly a workflow problem, which means that if you want the system to reproduce some bounded slice of expert behavior, you usually need to design for it deliberately. You are not just giving it more content. You are shaping a capability.

<details>
<summary>Tech note: the thin-layer failure modes I expect most</summary>

The most common failure mode is context entanglement: planning, execution, critique, and decision all happen in one giant prompt, so the system loses separation of concerns and starts optimizing for local plausibility instead of process integrity. Closely related is evaluator collapse, where the same model instance both generates and grades without a genuinely distinct pass, so obvious defects slide through because nothing independent is checking them.

After that, the usual culprits are retrieval collisions, where semantically similar but operationally irrelevant chunks outrank authoritative facts; hidden state drift across turns; prompt accretion that creates brittle behavior nobody can reason about; and tool optimism, where the model narrates an action as though it happened even though the underlying tool returned a partial or failed result. I would also worry about non-idempotent retries, no clean boundary between read paths and write paths, and no observability around why the system took a given branch. Those are not model parlor tricks. They are systems problems.

</details>

For builders, I do think the implementation layers matter a lot. I keep coming back to representation, perspective separation, orchestration, evaluation, and boundary design. But those feel like supporting mechanics for the larger point, not a separate essay, so I have tucked the more technical picture below instead of letting it take over the main flow.

## Two more pictures that help

At some point diagrams are more honest than more prose, so here are two more that help.

### Picture one: the first test people run

<div class="diagram-shell">
  <div class="mermaid">
flowchart LR
  subgraph A["What people do"]
    A1["Paste in a document"]
    A2["Ask a few questions"]
    A3["Get a mixed result"]
  end

  subgraph B["What they often conclude"]
    B1["AI is not very useful here"]
  end

  subgraph C["What that mostly tested"]
    C1["One chatbot interaction"]
    C2["How the question was asked"]
    C3["Whatever the tool could pull in"]
  end

  A3 --> B1
  A3 -. really measured .-> C1
  A3 -. sometimes measured .-> C2
  A3 -. maybe measured .-> C3
  </div>

<p class="diagram-label">a first chatbot test is real, but it is still a very narrow test</p>
</div>

### Picture two: a pile of information versus working context

<div class="diagram-shell">
  <div class="mermaid">
flowchart LR
  subgraph Left["A pile of information"]
    L1["Documents"]
    L2["Emails"]
    L3["Meeting notes"]
    L4["Chats"]
  end

  subgraph Right["Working context"]
    R1["What matters now"]
    R2["What can wait"]
    R3["Who owns next"]
    R4["What needs escalation"]
  end
  </div>

<p class="diagram-label">more information is not the same thing as usable operating context</p>
</div>

<details>
<summary>Tech diagram: one concrete way to think about the capability layer</summary>

<div class="diagram-shell">
  <div class="mermaid">
flowchart TD
  A["Event or request"] --> B["Load typed state"]
  B --> C["Assemble context"]
  C --> D["Plan next step"]
  D --> E["Call tools through contracts"]
  E --> F["Evaluate result"]
  F --> G{"Act or escalate?"}
  G -->|Act| H["Write state and create next task"]
  G -->|Escalate| I["Human review"]
  </div>

<p class="diagram-label">a more technical view: the capability layer is control flow plus state, tools, and evaluation</p>
</div>

</details>

## The questions I would ask instead

If I were evaluating an AI product or vendor for business use, I do not think I would start with which model are you using, can it read our documents, or can it sound like our team. Those are not irrelevant questions, but they are secondary.

I would want to know what specific capability is being improved, where it fits in the workflow, how the system knows what good looks like, what it explicitly does not do, and what happens when it is wrong. Those questions get you much closer to whether you are buying something real.

That, to me, is the more interesting shift now underway in the market. A lot of current AI tooling is still sold at the level of interface and impression: chat with your data, ask better questions, generate insights, automate work. Some of that is useful. Some of it is real. But it is also easy to stop one layer too early and mistake a clever demo for a durable business instrument.

I think the more interesting companies over the next few years will be the ones that move one layer up, from model access to capability design. That is where things start becoming economically meaningful. It is also where disappointment tends to go down, because you are no longer asking the system to magically become useful. You are defining the job, the boundary, the context, the review, and the measure of success.

In other words, you are shaping the vehicle, not just admiring the engine.

<p class="bridge-note"><strong>I should note:</strong> none of this means the first Copilot or ChatGPT test was stupid. It was a perfectly reasonable first experiment. I just think a lot of people are drawing a much broader conclusion from a much narrower test than they realize.</p>

## So what is the takeaway?

If you pasted a document into Copilot, asked a few questions, and the result was not very good, that does not necessarily mean AI is weak. It may just mean you tested the wrong layer.

You tested whether a raw reasoning engine could give you a useful answer in a single interaction. That is a perfectly reasonable first test. But it is not the same thing as testing whether AI can support or improve a real business capability.

And once you see that distinction, I think the conversation gets a lot more honest. You stop asking which model should we use and start asking what capability are we trying to improve, what does good actually look like, what context does the system really need, where does human judgment belong, and how do we make this repeatable.

That feels like a much better conversation to me.

</div>
