---
layout: post
title: "Herding Kittens with Jet Packs"
date: 2026-07-16 09:00:00 -0400
categories: ai management
tags: [ai, agents, management, ai-tropes, lightforge-works, rube-goldberg, orchestration]
description: "Everyone's got a jet pack now and productivity still hasn't moved. This is about the fast, fragile little machines people are building with them, none of it composed, nobody steering, and what to do next."
image: /assets/images/kittens-with-jetpacks.png
---

![Kittens with jet packs](/assets/images/kittens-with-jetpacks.png)
*Everyone gets a jet pack. Watch the kittens fly!*

> **TL;DR** — Everyone's got a jet pack now and productivity still hasn't moved. This is about the fast, fragile little machines people are building with them, none of them connected to anything, nobody steering any of it (ours included, for a while), and what to do about it.
{: .tldr }

We keep hearing the same thing from clients and prospects: *we're giving everyone Claude so they can build it themselves, software is cheap now.* And they think that's the whole job. Get the tools in people's hands. Done. The rest takes care of itself.

And look, it works. The person who's had a request stuck in an IT queue for a year can build the thing herself by Tuesday. I do it myself; a motivated person with a capable model is more powerful than the same person without one. Just try taking that superpower away and wait for the wrath. Everyone can have a jet pack now. It's super fun and awesome.

So this isn't an argument against handing out jet packs. But a [paper out of NBER](https://www.nber.org/papers/w34836) this year surveyed nearly six thousand senior executives and found that nine in ten say AI has had no impact on their firm's employment or productivity over the last three years. Everyone has Claude (well, an increasing share do), and productivity hasn't moved. The part that complicates the jet-pack story: those same executives are using AI about **1.5 hours a week**. So it's not that the tools are broken and it's not (yet) that they're transforming anything. They're just on the desk, used lightly.

You can read that two ways, and I think the reading matters. One: it's early, give it time, the gains are coming. Two: the tools work, but the work the tools make possible isn't getting composed into anything, it's piling up in competing directions. I'm in the second camp, and the rest of this is why.

## Many beautiful, fragile, isolated machines

An org's AI journey usually starts with one or two people eager to get into things, the lateral integration thinkers who just want stuff done. Every office has a spreadsheet whisperer. She discovers she can build a little tool: a form that routes intake emails, a dashboard that pulls from the CRM and makes it legible. She built it in an afternoon in Claude desktop. It's pretty good and she's amazed and proud. A year ago that tool would have cost a six-week IT project and a Jira board with its own ecosystem of tickets, and would never have been prioritized. Not anymore (sorry, IT, your support role is about to get a modification).

That invention is a shiny, cool Rube Goldberg machine: a chain of clever steps that does a real task, and works beautifully right up until somebody bumps the table.

![A hand-drawn Rube Goldberg machine from 1966](/assets/images/teschmacher-rube-goldberg-1966.jpg)
*My uncle Guy Teschmacher's Rube Goldberg machine, drawn in 1966. He also has a clock in MoMA that has its face hidden. Too funny.*

<details markdown="1">
<summary><strong>What one of these actually looks like (click to expand)</strong></summary>

A clever person, one afternoon, has the model write her this:

```python
# intake_router.py — built Tuesday, works on Tuesday
import requests

FORM_ID = "1aB...cD9"
SHEET_TOKEN = "ya29.A0..."        # her personal OAuth token, in plaintext
SLACK_WEBHOOK = "https://hooks.slack.com/services/T0.../B0..."

def main():
    rows = requests.get(
        f"https://sheets.googleapis.com/v4/spreadsheets/{FORM_ID}/values/A:Z",
        headers={"Authorization": f"Bearer {SHEET_TOKEN}"},
    ).json()["values"]
    for r in rows:
        requests.post(SLACK_WEBHOOK, json={"text": f"New lead: {r[1]}"})  # r[1] = Name
```

It runs pretty well and she is, legitimately, a hero.

The downside: in a single-player environment, the token is hers; the morning she leaves the company, it dies, and nobody knows why. Or it breaks the day the form adds a "Company" field and the columns shift, because nobody told the agent to update the script or that the columns might move. The CRM has never heard of any of this. The lead exists in Slack and nowhere else. And she's the only person who knows the script exists. She's going on vacation Thursday. Etc.

That is a Rube Goldberg machine. Clever, fragile, and don't mess with it.

</details>

Then it fans out. The whole team gets the same superpower, gets excited, and each person builds their own version of the thing they always wanted but couldn't have. Marketing automates its reporting. Operations builds a scheduling widget. Finance stands up a reconciliation script. Each one, on its own, is impressive and valuable. And each one has the same defect a Rube Goldberg machine has. Nobody reads what the others built, because everyone's heads-down in their own.

We live this ourselves. I generate a twelve-week LinkedIn campaign on Monday, and by Tuesday morning somebody else's agents have overwritten it. A third person's agents don't know where to pick it up, so they start over. We put the work in GitHub, the way you're supposed to, and it doesn't help. GitHub was never built for the sheer volume of stuff a team of agents generates and overwrites in a day. Then on top of that, if merges aren't handled correctly, the agents get confused over what is currently the gold copy and start using the wrong language when we move to automation.

It's a compounding mess. We build these systems for other people for a living, and our own integrations were a disaster.

We are, collectively, herding kittens with jet packs.

Tiny jet packs strapped to furry bodies, little contrails arcing across the office. One just knocked a lamp off the desk and didn't notice. Another is on top of the refrigerator, refusing to come down, generating a campaign brief nobody asked for. A third is midair, headed for the curtains. Each kitten, individually, is magnificent, faster and more capable than any kitten has ever been. And you're standing in the middle of the room with a clipboard, watching the furniture get destroyed, trying to remember why you thought the clipboard would help.

What's missing is the structure underneath: no shared state, nothing that says which goes where and which curtain is off-limits. We'll come back to that. First, the part people skip.

## A different clock

Coordination is part of the problem. The other part is timing. Or, to quote The Police (courtesy of Jung), the whole thing is synchronicity.

In human time, you do weekly check-ins, monthly reviews, quarterly planning. All necessary and good, even if we've always been annoyed by them, it's the tax you pay for coordination. It was keeping a clock the whole time, to keep people in sync. Weekly meetings worked because everyone in the room moved at roughly the same speed. Nobody had moved so far since last Friday that an hour couldn't catch them up.

But this runs on a different clock. People are moving faster and broader than they used to, and each one is generating an avalanche of artifacts along the way, because that's what humans-plus-agents do, they produce. Reports, dashboards, scripts, drafts, follow-ups. The old Friday meeting can't re-synchronize any of it, because the gap between last Friday and this Friday has opened into a canyon. The artifacts pile up unreviewed and the humans fall further behind the thing they're supposed to be overseeing, until they're not overseeing it at all. Piloting one of these things is fatiguing, but the momentum isn't.

And all along, nobody did anything wrong. Every individual made a sensible decision. The system still came apart, because it wasn't designed as a system, let alone for coordinated effort, or a team-focused idea. It got improvised, at high speed, by people told to go fast and given no way to stay fast together.

## What it does to trust

There's a downstream consequence. A friend told me the other day he now says to people: *if you send me a deck longer than three slides, I'm not reading it.* And I've heard this more than once, and feel it myself: *if I catch one AI-ism in an article, I stop trusting the author.*

This is the overproduction problem hitting the audience. The artifacts piled up faster than the humans could validate them, so the audience taught itself to flinch at the whole category. Hand everyone a jet pack and you also hand them a reason to trust the next deck a little less. The kittens aren't just wrecking your office, they're wrecking the room you deliver the work into.

## Herding kittens with jet packs

So you've got a room full of fast, empowered people, each generating a small mountain of output, none of it composed, most of it unvalidated, and the old meeting cadence can't keep up. Managing that is its own problem, and most of what's out there stops at "call a vendor when you're ready for the next level," which isn't really helpful, except to the vendor's sales funnel.

Herding kittens was hard when the kittens were slow. Herding kittens with jet packs is a different sport. The old management questions, what did you do this week, are you on track, don't catch the real failure mode, because the real failure mode isn't underperformance. It's overproduction in a bunch of competing directions. Things that don't compose, that nobody validates, that pile up unread. The person looks busy and productive and is, in fact, generating the problem. You can't spot that by asking whether they hit their hours.

> The real failure mode isn't underperformance. It's overproduction in a bunch of competing directions, things that don't compose, that nobody validates, that pile up unread.
{: .callout }

There's a trap in here that catches the people who feel the most capable. The tool makes production frictionless, so you produce more than you ever have, and the volume feels like competence. It isn't. Using AI well doesn't make you an expert in the thing you're producing; it makes you a fast first-draft factory for a thing you still have to know how to judge. I've watched smart people ship dashboards they couldn't actually defend, campaigns they couldn't tie to an outcome, reconciliations that were confidently wrong in the last row. They felt like experts because the output was fluent. The fluency was the model's; the judgment was still theirs, and it hadn't grown to match the throughput. Overproduction under a false sense of expertise is worse than plain overproduction, because the person generating it doesn't know they're the problem.

So the first move isn't structural. It's managerial, and it's mostly subtraction. Two questions, aimed less at motion and more at intent:

> **How did you limit the output to the core effort?** The default behavior of an agent team is to produce everything it can. A good operator's job, now, is mostly subtraction, deciding what not to generate, what to cut, what to refuse to ship. If someone can't tell you how they limited the output, they didn't.
>
> **What's your intentional work this week, and how are you steering your agent team toward it?** Intentional work is the small set of things a person means to accomplish, separate from the avalanche the agents produced along the way. The question is whether they can name it, and whether the team is pointed at it, or just pointed. If the agent team has no relationship to the intentional work, the agent team is driving and the person is along for the ride.
{: .callout }

I ask myself that second one every Monday (and increasingly every day), and I don't always like the answer. That struggle is the diagnostic.

At the team level these get exponentially harder, and I suspect they turn into a role: someone whose entire job is subtraction, taking the ten near-identical jobs the team just generated and folding them into one, killing the duplicates, keeping the shared state clean. A dedup PM, basically. We're starting to see the shape of it.

That's the managerial floor. It's what you do on Monday to keep the overproduction from burying you while you figure out the bigger piece.

## The bigger piece

The two questions are a stopgap. They're how you manage the problem before the real fix exists, because the real fix isn't a management practice, it's structure.

And the objection: *but the labs are fixing this*. Yes, partly, and it hasn't gotten far. Anthropic and OpenAI are both racing to add the connective tissue: Claude's shared agents and scheduled tasks on Team and Enterprise plans, ChatGPT's scheduled tasks and workspace agents for business, plus a whole crop of orchestration startups, CrewAI, LangGraph, n8n (which I use myself), all selling the "AI brain" that coordinates the rest. Here's the thing, though. So far, in our experience, almost all of it bolts onto the individual jet packs. It coordinates them. It doesn't yet sit underneath them as shared structure, the part that says what state is true, what work is intentional, and what's just noise the kittens made on the way to the ceiling. (We build that kind of underlying structure for clients at LightForge, so read this as the hypothesis we're betting on, not an idle observation. And it's a falsifiable one: if a firm builds the coordination layer and productivity still doesn't move, the frame is wrong, not the implementation, and we'll have said so.)

This isn't a new shape of problem, by the way. It's the old one, what Charles Perrow called *normal accidents*: systems fail not because any single part is broken but because the parts interact in ways nobody designed for. And it rhymes with Solow's productivity paradox, the one about computers showing up everywhere except in the productivity statistics. The kittens-with-jet-packs version is the same pattern at a new clock speed.

> The fix is the same shape it's always been: stop bolting coordination onto the parts, and put structure underneath them instead.
{: .callout }

Anyway. You can't take the jet packs back, and you shouldn't want to. But you can stop measuring kitten motion and start managing intent on Monday, and start building the kitchen the kittens are flying around in.

*(Next: what a smart kitchen is, and why your team needs one to really cook.)*
