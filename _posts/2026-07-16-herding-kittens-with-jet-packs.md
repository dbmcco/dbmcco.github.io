---
layout: post
title: "Herding Kittens with Jet Packs"
date: 2026-07-16 09:00:00 -0400
categories: ai management
tags: [ai, agents, management, ai-tropes, lightforge-works, rube-goldberg]
description: "At LightForge Works, we keep noticing a trend across clients and prospects — it says more about systems than tools."
image: /assets/images/kittens-with-jetpacks.png
---

![Kittens with jet packs](/assets/images/kittens-with-jetpacks.png)
*Everyone gets a jet pack. Watch the kittens fly!*

At [LightForge Works](https://www.lightforgeworks.com) we are noticing a trend across clients and prospects that is interesting. When we begin assessing a workflow challenge, we are often hearing some version of “*we're giving everyone Claude so they can build it themselves. Software is cheap now.”*

This is pretty good. Giving people Claude/ChatGPT works. Cursor works. Whatever lands on the desk next quarter will work too. The person stuck for a year in an IT queue can build the thing herself by Tuesday. I do it myself, and a motivated person with a capable model is more powerful/accelerated than the same person without one. Just try taking that new superpower away and wait for the wrath. Everyone can have a jet pack now. And it's super fun and awesome.

So this isn't an argument against handing out jet packs. However... a [paper out of NBER](https://www.nber.org/papers/w34836) this year surveyed nearly six thousand senior executives and found that nine in ten of them say AI has had no impact on their firm's employment or productivity over the last three years. Everyone has Claude (or well, an increasing % do), but productivity levels are the same (and at an all time high - maybe an AI Hawthorne effect; I wonder). We can argue that it’s still too early in the Single-player-AI-revolution to see real gains but I think there is a different aspect of this that is important to contemplate and points to a downstream effect that the orgs we are talking to do not seem to be thinking about.

## Many beautiful, fragile, isolated machines

An org's AI journey may start with one or two people eager to get into things; lateral integration thinkers who want to get stuff done. Think of the office's unofficial spreadsheet whisperer; every office has one. She discovers she can build a little tool. A form that routes intake emails. A dashboard that pulls from the CRM and makes it legible. She built it in an afternoon in Claude desktop. It’s pretty good and she’s amazed and proud. A year ago that tool would have cost a six-week IT project and a Jira board with its own little ecosystem of tickets; and would never have been prioritized or built. Not any more (sorry IT, you’re about to have a modification to your support role).

That invention is a shiny, cool Rube Goldberg machine: a chain of clever steps that does a real task, and works beautifully right up until somebody bumps the table.

![A hand-drawn Rube Goldberg machine from 1966](/assets/images/teschmacher-rube-goldberg-1966.jpg)
*My uncle Guy Teschmacher’s Rube Goldberg machine, drawn in 1966. He also has a clock in Moma that has it's face hidden. Too funny.*

<details>
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

It runs petty well and she is, legitimately, a hero.

The downside: in a single player environment, the token is hers; the morning she leaves the company, it dies, and nobody knows why. Or it breaks the day the form adds a "Company" field and the columns shift, because nobody told the agent to update the script or that the columns might move. The CRM has never heard of any of this. The lead exists in Slack and nowhere else. And she is the only person who knows the script exists. She is going on vacation Thursday. Etc.

That is a Rube Goldberg machine. Clever, fragile, and don't mess with it.

</details>

Then it fans out (the proverbial hitting the fan action). The whole team gets their own jet pack, gets super excited, and each person builds their own version of the thing they always wanted but couldn't have. Marketing automates its reporting. Operations builds a scheduling widget. Finance stands up a reconciliation script. Each one, on its own, is impressive and valuable And each one has the same defect a Rube Goldberg machine has.

We actually experience this ourselves and are building systems to mitigate it, but here is my real example. I generate a twelve-week LinkedIn campaign on Monday, and by Tuesday morning somebody else's agents have overwritten it. A third person's agents don't know where to pick it up, so they start over. We put the work in GitHub, the way you're supposed to, and it doesn't help, and GitHub was never built for the sheer volume of stuff a team of agents generates and overwrites in a day. Then on top of that, if merges are not handled correctly, the agents get confused over what is currently the gold copy and start using the wrong language when we move to automation.

It's a compounding mess. We build these systems for other people for a living, and our own integrations were a disaster.

We are, collectively, herding kittens with jet packs.

I really do love this image and feel like it captures things pretty well. Tiny jet packs strapped to furry bodies, little contrails arcing across the office. One just knocked a lamp off the desk and didn't notice. Another is on top of the refrigerator, refusing to come down, generating a campaign brief nobody asked for. A third is midair, headed for the curtains. Each kitten, individually, is magnificent, faster and more capable than any kitten has ever been. And you're standing in the middle of the room with a clipboard, watching the furniture get destroyed, trying to remember why you thought the clipboard would help.

Among what is missing is the structure underneath: no shared state, nothing that says which kitten goes where and which curtain is off-limits. (Why there's no structure, and what to build instead, is the next essay. This one is about what it does to you while you wait.)

## Human momentum and human+agent momentum are different time scales

The coordination is part of the problem and the other is timing. Or, to quote The Police (courtesy of Jung), the whole thing is synchronicity.

In human time, do weekly check-ins, monthly reviews, quarterly planning.  All necessary and good, even if we've always are annoyed; it's the the tax you pay for coordination. It was keeping a clock the whole time to keep people in sync. Weekly meetings worked because everyone in the room moved at roughly the same speed. Nobody had moved so far since last Friday that an hour couldn't catch them up.

But kittens with jet packs is different. People are moving multiples faster and broader than they used to, and each one is generating an avalanche of artifacts along the way, because that's what humans+agents do: they produce. Reports, dashboards, scripts, drafts, follow-ups. The old Friday meeting can't re-synchronize any of it, because the gap between last Friday and this Friday has opened into a canyon. The artifacts pile up unreviewed and humans fall further behind the thing they're supposed to be overseeing, until they're not overseeing it at all. The attention tax of driving jet packs causes fatigue but the momentum remains.

And all along, nobody did anything wrong. Every individual made a sensible decision. The system still came apart, because it wasn't designed as a system, let alone for coordinated effort or a team focused idea, it got improvised, at high speed, by people told to go fast and given no way to stay fast together.

## What it does to trust

A friend told me the other day he says to people now: *if you send me a deck longer than three slides, I'm not reading it.* The other thing I've heard said more than once from other people, and I feel the same way: *if I catch one AI-ism in an article, I stop trusting the author.*

It's everywhere now: plausible, confident, mostly-fine material that nobody had time to check, and the rational response is to avoid it. The artifacts piled up faster than the humans could validate them, so the audience taught itself to flinch at the whole category. Hand everyone a jet pack and you also hand them a reason to trust the next deck a little less.

Note - I am handwriting this - emdashes and all - although I certainly had a lot of AI help from my memory system and golden voice pack. Just being transparent here. Hope you've read this far and didn't get too annoyed. I've tried to stamp out AI'isms, Really. 

## Herding kittens with jet packs

So you've got a room full of fast, empowered people, each generating a small mountain of output, none of it composed, most of it unvalidated, and the old meeting cadence can't keep up. Managing that is its own problem, and most of what's out there stops at "call a vendor when you're ready for the next level," which isn't really helpful, except to the vendor's sales funnel.

Herding kittens was hard when the kittens were slow. Herding kittens with jet packs is a different sport. The old management questions — what did you do this week, are you on track — don't catch the real failure mode, because the real failure mode isn't underperformance. It's overproduction in a bunch of competing directions. Things that don't compose, that nobody validates, that pile up unread. The person looks busy and productive and is, in fact, generating the problem. You can't spot that by asking whether they hit their hours. The kitten was technically productive. It visited the ceiling six times.

Here's what I'd ask, as a starting point for a new style of human+agent management:

**How did you limit the output to the core effort?** The default behavior of an agent team is to produce everything it can. A good operator's job, now, is mostly subtraction — deciding what not to generate, what to cut, what to refuse to ship. If someone can't tell you how they limited the output, they didn't. 

**What's your intentional work this week, and how are you steering your agent team toward it?** Intentional work is the small set of things a person means to accomplish, separate from the avalanche the agents produced along the way. The question is whether they can name it — and whether the team is pointed at it, or just pointed. Most people, asked this for the first time, will struggle. I ask myself this one every Monday (and increasingly every day), and I don't always like the answer. That struggle is the diagnostic. If the agent team has no relationship to the intentional work, the agent team is driving and the person is along for the ride. I am trying different agent language to keep me on track: "North Star" is pretty good at the moment. Until the next model release anyway.

These are decent at the individual level, but they are exponentially important at the team level.

Anyway...

You can't take the jet packs back, and you shouldn't want to. But you can stop measuring kitten motion and start managing intent. 

*(Next: the structure the kittens need — what a smart kitchen is, and why your team needs one to really cook.)*
