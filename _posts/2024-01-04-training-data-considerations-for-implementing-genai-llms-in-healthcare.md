---
layout: post
title: "The healthcare AI training data problem (and why your old EMR data is actually gold)"
date: 2024-01-04
categories: ai healthcare data
tags:
  - AI
  - healthcare
  - training-data
  - EMR
---

I've been working with healthcare organizations on AI implementation for the past year, and there's this one problem that keeps coming up in every conversation: training data.

Everyone wants to build AI systems that understand their specific patient populations, clinical workflows, and organizational context. But when they look at the available training datasets, they're all generic, often outdated, and definitely not representative of their actual patient base.

And then someone in the room always says, "But we have decades of our own clinical data sitting in our EMR system. Can't we use that?"

That's when things get interesting.

## The problem with public healthcare datasets

Most healthcare AI systems are trained on datasets like MIMIC-III, eICU, or various clinical trial datasets. These are great for research, but they have some pretty significant limitations when you're trying to build AI that works in real healthcare settings:

**They're not representative** - MIMIC-III is mostly data from Beth Israel Deaconess Medical Center. If you're a rural health system in Texas, your patient population probably looks very different.

**They're old** - A lot of these datasets are from 5-10 years ago. Healthcare changes fast, especially post-COVID. Treatment protocols, medication options, and patient care pathways have evolved significantly.

**They're limited in scope** - Most public datasets focus on specific conditions or care settings. But healthcare AI needs to understand the full complexity of patient care across multiple conditions and touchpoints.

I was working with a health system last year that tried to implement a sepsis prediction model trained on one of these public datasets. The model performed great in testing, but when they deployed it in their ICU, the false positive rate was astronomical. 

Turns out their patient population had different risk factors, their clinical documentation patterns were different, and their lab timing protocols didn't match what the model had been trained on.

## Why your archived data is actually perfect (and why you're not using it)

Here's what I keep explaining to healthcare CIOs: You already have the best possible training dataset for your organization. It's sitting in your EMR system right now.

You have years (sometimes decades) of clinical notes, lab results, diagnostic imaging reports, medication records, and outcome data. All specific to your patient population, your clinical workflows, and your documentation practices.

Nobody's using it for AI training;

**"It's messy"** - Real clinical data is messy. But that's actually a feature, not a bug. AI systems trained on messy, real-world data perform better in messy, real-world environments than systems trained on clean research datasets.

**"We don't have the technical expertise"** - This one's more legitimate. Most healthcare organizations don't have teams that know how to process clinical data for AI training. But this is a solvable problem.

**"Compliance and privacy concerns"** - Also legitimate, but there are established frameworks for using internal clinical data for AI development while maintaining HIPAA compliance.

## What I'm seeing work in practice

The healthcare organizations that are getting good results from AI are the ones that figured out how to use their own data effectively.

One health system I'm working with built a clinical decision support tool using 8 years of their own EMR data. The model can predict which patients are likely to need additional care coordination, which medications are most likely to cause adverse reactions in their specific patient population, and which discharge plans are most likely to lead to readmissions.

The key insight? They didn't try to build a general-purpose AI system. They built AI that understands their specific environment, patient base, and clinical workflows.

Another organization used their archived radiology reports to train a model that can flag imaging studies that might need expedited review. Not because the AI is making diagnostic decisions, but because it learned to recognize patterns in their radiologists' language that indicate urgency.

## The technical approach that's working

Here's the process that seems to be most effective:

**Start with a specific use case** - Don't try to build general-purpose medical AI. Pick one workflow or decision point where you have good data and clear success metrics.

**Use your EMR archive systematically** - Most EMR systems have been collecting structured and unstructured data for years. That's your training corpus.

**Focus on your organization's specific patterns** - The goal isn't to build AI that works everywhere. It's to build AI that works really well in your environment.

**Maintain human oversight** - These AI systems should augment clinical decision-making, not replace it. The models work best when they're designed to help clinicians be more effective rather than make autonomous decisions.

The health system with the sepsis prediction model? They eventually rebuilt it using their own EMR data. The new version has a much lower false positive rate and actually gets used by their clinical teams because it understands their specific patient population and care patterns.

## Why this matters now

Healthcare organizations are under massive pressure to improve efficiency and outcomes while controlling costs. AI can help with all of that, but only if it's trained on data that reflects the actual environment where it's going to be deployed.

The organizations that figure out how to leverage their archived clinical data effectively are going to have a significant advantage. Not because their AI is smarter, but because it's trained on data that actually represents their real-world challenges and patient populations.

And the ones that keep waiting for perfect public datasets or off-the-shelf solutions? They're going to keep struggling with AI systems that work great in research papers but don't translate to their actual clinical environment.

## The implementation reality

This isn't easy work. You need people who understand both clinical workflows and AI development. You need robust data governance processes. And you need leadership that's willing to invest in building internal AI capabilities rather than just buying vendor solutions.

But the organizations that are making this investment are seeing real results. Better clinical outcomes, more efficient workflows, and AI systems that actually get adopted by clinical teams because they're designed around real-world data and workflows.

Your EMR archive isn't just historical data - it's the foundation for AI systems that can actually improve patient care in your specific environment. The question is whether you're going to use it or keep waiting for someone else to solve this problem for you.
