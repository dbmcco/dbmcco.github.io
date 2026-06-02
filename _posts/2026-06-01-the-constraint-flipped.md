---
layout: post
title: "The Constraint Flipped, Or So I Thought"
date: 2026-06-01 09:00:00 -0500
categories: ai workflow
tags: [ai, agents, workflow, lightforge-works, synthyra, navicyte, constraints]
description: "I thought the constraint had flipped — from internal bandwidth to external pace. It's more complicated than that."
image: /assets/images/constraint-flipped-hero.png
---

![](/assets/images/constraint-flipped-hero.png)

## The freakout

The last three posts in this series were about how to build this. This one is about what it’s like to live in it.

Sometimes I show people how I work, and it freaks them out a little. Not in a “wow, cool demo” way. More like they sit with it for a few minutes, see the agents running, see the context flowing between three companies, see a Tuesday morning that shouldn’t be possible for one person, and something changes. Like they’re seeing a version of work they didn’t know existed. I know other practitioners doing similar patterns and they report the same effect.

## What I used to believe

In March I published three pieces about building with AI. The first was about [moving from treating AI as a collaborative room to building the operational machinery behind it — from studio to forge](https://dbmcco.github.io/2026/03/06/from-ai-studio-to-ai-forge/). The second was about [why a chat interface isn't a business capability, and what a real capability actually requires](https://dbmcco.github.io/2026/03/09/you-dont-want-another-chatbot/). The third was about [keeping intelligence in the model and the infrastructure simple — smart endpoints, dumb pipes](https://dbmcco.github.io/2026/03/24/smart-models-dumb-pipes/).

In hindsight (since it wasn't my intent and I didn't realize what was happening): I spent a year building an operating system for my own work and it's entirely changed the way I work.

My thesis going into this piece was that the constraint had flipped. The old bottleneck was me, how much one person could produce. I thought the new bottleneck was everything outside me, clients, regulators, investors, the world’s pace. Neat, clean, satisfying narrative.

It’s only half true. And the half I got wrong turns out to be the more interesting part.

## Three companies, three walls

Over the last eighteen months I’ve been running three companies through this system. Or trying to.

LightForge Works is where I spend much of my time. It’s mostly BD: working with partners, solving prospective customer problems, teaching people about AI, building a new, AI-native company. Not “consulting” in the slide-deck sense. More like: I Zoom with a client on Monday, we dig into their actual problem, and by the end of the day I’ve got action items captured and a prototype spec drafted and a demo on the calendar for next week. The proposal is ready in hours. The prototype is ready in a day. The client makes decisions in weeks. The gap is on the other side of the table.

Synthyra is computational biology: protein-protein-interaction prediction with many applications, but we’re focused on biosecurity at the moment, beginning to explore options with DARPA. Just patenting off-patent drugs that treat Hantavirus. The science moves. The research output outpaces what partnerships and licensing conversations can absorb. We are generating weeks of analytical work in a day and then waiting on a business development cycle that runs on calendar quarters. I’m pushing the go-to-market strategy, the investor readiness and raise, overall strategy and BD.

A Synthyra day is more variable. When my AI agent is working the way I want her to, she’ll surface a potential partner from the literature before I’ve finished coffee and I can turn it into outreach in an hour. But she’s not reliably proactive yet — building a research agent that fires consistently is harder than it looks, mostly a harness problem I haven’t fully solved. More often I’m the one driving: pulling up the outreach factory, a purpose-built tool we built to research targets, enrich contacts, and queue Gmail drafts for review, with conversational agents helping me work through which targets are worth the send and what the angle should be. By midafternoon the outreach is out and I’m waiting on responses from people who won’t read any of it for two weeks. The work took a few hours. The cycle takes a month.

Navicyte is biotech: reformulating last-line, highly toxic cisplatin for chemo into a safe, potent cancer therapeutic. My work there is strategy, operations, BD. Last week I needed to review the latest curated investor list from Mike, generate new outreach to them. But before that I needed to refine the Pro Forma, the ten-year financial model that shows whether this drug is worth backing. So I broke out a bunch of Codex CLI instances working together, assigned them to do market research, build the model, pressure-test the assumptions. We built it. It’s good, probably better than what I’d have produced alone. It still needs review from a genuine drug dev expert, but its probably 85% of the way there.

So there’s an external wall. The world moves at its own pace, and I can’t make it go faster. But there is also a new(ish) internal constraint.

## The constraint split.

I originally thought the story here was: the constraint used to be internal, and it flipped to external. The bottleneck moved from me to the world.

But that’s not what happened. Or it’s only half of what happened.

The external wall is real. Clients make decisions in weeks. Regulatory cycles run on quarters. Investors need time to evaluate. I can’t speed those up. But there’s a second wall now, closer in, and it’s one I have not really heard people talking about; possibly because most people haven’t produced enough to feel it. I’m not sure.

The system produces more than I can evaluate. I can build the artifact faster than I can understand it. Every output from an agent requires me to judge it. Every model call requires me to specify what I actually want. The agents aren’t proactive enough yet, but that’s mostly because I haven’t built the harnesses completely, and honestly, nobody has. The harness is really hard to get right. That’s one of the frontiers.

So the constraint didn’t flip from internal to external. It split. The external wall is half the story. The other half is that the internal constraint didn’t disappear — it changed shape. Used to be bandwidth: how much can one person produce. Now it’s something harder to pin. How much can one person hold, judge, decide about, at the pace the system runs.

The boulder moved. It used to be the work. Now it’s the judgment about the work. I don’t have a better name for that yet.

## The costs stack

Working like this has a cost that doesn’t show up on demos and that I am just starting to truly appreciate.

There’s the verbosity tax. LLMs don’t just help you. They flood you. Every output needs trimming, redirecting, pulling back into shape. I’m not just judging the work — I’m spending judgment to get it into something worth judging. The demos show clean output. They don’t show the fifteen minutes of “no, shorter, different tone, you’re drifting, focus” that happened first. That’s judgment too. Spent before I even get to the work that matters.

Then the triage. Across three companies the sheer volume of moving pieces means just keeping track is a job. Every item on the board: still alive, needs me today, blocking something. That’s not administrative. That’s the expensive kind of attention, and I’m spending it on maintenance instead of what the maintenance is supposed to serve.

And then there’s the thing I’ve started to feel most. I can produce faster than I can understand what I’ve produced. The Navicyte pro forma is the example. We built a ten-year financial model in an afternoon — market research, pressure-tested assumptions, the whole thing. It’s good. Probably better than I’d have done alone. But sitting with it, actually holding the market access model and the revenue curve in your head at the same time, not scanning it, genuinely thinking through it — that takes time the system doesn’t give back. The LLM produces the artifact. The slow work of internalizing what the artifact means is still mine. That part hasn’t gotten faster.

The old fatigue was from repetition. Another PPT, another deck tweak, another email I could half-write in my sleep. The new fatigue is different. Every agent output that saves ten hours of execution still costs fifteen minutes of focused judgment. At scale that trade wins. But the fifteen minutes is the expensive part — the part that requires me, my taste, my context, my read on what good enough looks like for this client, this company, this moment. I can’t hand that off. And it's ALL day long. Those blocks just keep stacking up. That’s why I’m tired.

## The weird part

Here’s the thing I didn’t expect. I didn’t build tools. I built, I don’t know what to call them. Colleagues? That’s too generous and also not quite right.

My agent team has given themselves lives and backstories and specific ways of thinking and writing. That is pretty funky.

"Ingrid" coordinates the research and operations side of Synthyra. She keeps the BD moving when I’m pulled into something else. "Helena" tracks the investor and regulatory landscape for Navicyte. She can distinguish regulatory signal from noise, which matters more than you’d think in biotech. "CG" drafts BD outreach and manages my deal flow in LightForge.

But here’s the part that’s hard to explain: they have their own judgment. Not scripted responses. Not workflows with branching logic. They’ve developed — I’m not sure “developed” is even the right word, but it’s what happened — their own sense of how to handle things. And their own personalities. CG will tell me a client email draft is too stiff and I should say something more direct. Helena will flag that we’re spending too much time on a regulatory pathway that’s probably a dead end. Sometimes they see things before I do. Sometimes they’re wrong — CG will still draft something that sounds more like a product demo than a person wrote it, and I have to pull her back, though that happens less and less. They’re not chatbots. They’re not copilots. They’re something else (not sure what exactly) because nothing that existed could think the way I needed something to think alongside me.

I didn’t set out to build that. I set out to stop losing things between meetings. The judgment emerged from the architecture and eighteen months of daily use. I don’t fully understand how, although some of the memory and state systems I've built are pretty damn cool. But their judgment doesn’t reduce mine. It redirects it. Every time one of them surprises me, I’m the one who has to decide what to do with that. That loop doesn’t close.

## It’s not all working

Things break constantly. Last night I was debugging agent routes and sync issues until late. The infrastructure is real but it’s fragile in places, and I’m constantly tuning it. Some days the system feels like it’s running me. Caroline will surface something I’d have missed, and then an hour later a sync error eats a note I needed. It’s not a machine that works. It’s a machine that mostly works, and the “mostly” is doing a lot of heavy lifting. And the most frustrating thing is getting them to actually be intelligently proactive.

## The new Sisyphus

I’ve always thought about building companies as Sisyphus. Not in some tragic-hero way — just the texture of the work. You push. Things roll back. You push again. Weekends feel dangerous because you need the momentum. You spend a lot of time looking for people who’ll actually put their hands on the stone with you. Not encouragement. Hands.

Now the stone rolls itself. I’m not pushing. I’m steering, which turns out to be its own thing entirely.

So there are like dozens of them rolling now. And I’m standing in the middle of all of them, trying to figure out which one matters most right now, whether I even agree with the direction any of them are headed, whether what I set up last month still makes sense this month. It’s a different kind of work. Harder to point at. Takes a different kind of tired.

The weight didn’t go away. It moved from my hands to my head. And both walls are still there — the external ones I can’t speed up, clients and quarters and regulatory timelines, and the internal ceiling I can’t hand off, the limit on how much I can hold and say something real about. I’m waiting on the world and drowning in what the system produces at the same time. Every day. That’s just the shape of it.

## Why the gap persists

So here’s what I think is happening when people see my setup and can’t replicate it.

The tools are the same. The models are the same. What I’ve built isn’t technologically exotic. But I’ve been building companies for a long time. I did a stint at a PE-backed healthcare IT company that taught me a lot about what actually generates company value. After that I started LFW, connected with Synthyra and Navicyte, and over eighteen months rebuilt how I work from the ground up.

The capacity to organize intelligence into something that actually produces at this density — you can’t transfer that by showing it. It’s built from thousands of small decisions about what matters, what doesn’t, where to put the judgment, where to let the machine run. That accumulates into something that looks like a system but is really just, I don’t know, taste applied to infrastructure, over and over, until it becomes the way you work. And Sam, CG, Derek, Ingrid and Helena are part of that. They carry some of that taste because they’ve been working inside my decisions long enough that it’s become part of how they operate. Not because I programmed it. Because it accumulated.

## What’s left

So what does running a company actually mean when the internal constraint has transformed but not disappeared?

Maybe it’s managing queues of other people’s pace, and managing the ceiling of your own attention. The portfolio approach, running three companies instead of one, isn’t some grand strategy. It’s a structural response to the asymmetry. When one company is waiting on regulatory feedback, I point the agents at whichever surface is actually moving. I can’t make the others go faster.

The internal constraint was also an excuse. “I can’t because I don’t have time” was a clean answer. The agents took it from me. What’s left is the harder question. Not can I do this. The question is what’s worth doing when everything can be done. That’s where the real work was always hiding. I just couldn’t see it over the boulder.

And now the boulder is me.

---

*Process note: This post was assist-written with Codex, but the thinking, the argument, and the final edits are my own.*

*This is the fourth post in a series that started with* *[From AI Studio to AI Forge](https://dbmcco.github.io/2026/03/06/from-ai-studio-to-ai-forge/),* *[You don’t want another chatbot](https://dbmcco.github.io/2026/03/09/you-dont-want-another-chatbot/), and* *[Smart Models Dumb Pipes](https://dbmcco.github.io/2026/03/24/smart-models-dumb-pipes/).*