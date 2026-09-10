---
layout: post
title: "Using AI to Predict Clinical Trial Patient Populations in the Future"
date: 2026-09-10 09:00:00 -0500
categories: ai biotech
tags: [ai, agents, navicyte, clinical-trials, population-prediction, adversarial-review]
description: "The field's tools forecast whether a trial will enroll. Almost nobody asks whether the population is real. A multi-panel adversarial run killed our lead population assumption in a day."
image: /assets/images/patient-population-monitor.png
---

At [Navicyte](https://navicytebiotech.com) we were talking with one of our senior advisors. She made the point that a lot of high-potential drug candidates don't die from bad science. They run out of money during clinical trials because the competition for patients is too dense. The trial can't enroll, the program burns cash waiting, and the drug dies.

That put the question in front of us years before the first dose: will there be enough patients for a Phase 1a or 1b trial, given the competing trials that will be recruiting when we expect to start ours?

## What I built

We're early-stage, and we run the company as an AI-native org. So I didn't buy the vendor version of this answer. I built a process.

I broke the population question into parts: total addressable pool, competitive trial landscape, residual feasibility, biology fit. Then I ran a multi-panel analysis against it. The architecture descends from the expert-panel simulator I open-sourced in ["Smart Models, Dumb Pipes"](https://dbmcco.github.io/2026/03/24/smart-models-dumb-pipes/): structured decomposition, parallel expert agents working the sub-questions independently, adversarial seats that challenge the core assumptions, and preserved dissent that keeps the minority position in the final deliverable. The adversarial seats were pointed at the framing itself: the population definitions and the plan's own assumptions. The whole thing ran in roughly a day for about fifty dollars in tokens. The comparable [IQVIA StudyOptimizer](https://www.iqvia.com/solutions/technologies/orchestrated-clinical-trials/planning-suite/studyoptimizer) engagement takes months and costs a fortune.

Then I pointed it at the population our development plan was built on.

![The population monitor: inputs, parallel expert panels, and the feasibility verdict](/assets/images/patient-population-monitor.png)

## What it found

The documented lead was a "cisplatin-ineligible" slice of a relapsed blood-cancer population, an operational target we expected to enroll. The process found that population doesn't exist as a recognized clinical stratum. The salvage regimen the framing assumed uses carboplatin, not cisplatin (the dominant salvage standard in relapsed disease), so "cisplatin-ineligible" sorts patients by their tolerance of a drug they were never going to get. The 20–40% citation supporting it was unverifiable. The patients it claimed overlap with the CAR-T- and bispecific-eligible pool: the cell and antibody therapies competing for the same relapsed patients. The operational prediction was precise and wrong. The error didn't come from the model. It came from the framing we brought to it: the planning documents, the KOL interviews, the narrative that said there was a population to enroll.

The second failure was the pool itself. On the run's count, that population alone carried 89 US trials competing for roughly 5,638 patients in the 2028 window, with a graduation class (golcadomide, soquelitinib, valemetostat, next-wave CD19×CD3 bispecifics) coming through Phase 2 readouts and about to consume more of the relapsed pool. Even if the cisplatin-ineligible slice had been a real stratum, the competitive density was eating it before our sites could open.

You're actually predicting three things, and the field builds tools for one and a half of them. Who will enroll is operational: which sites, how fast, do you hit your number. Who should enroll is scientific: is this the right population. And will the pool still be there when you get there is competitive density. The tools that exist forecast your enrollment as if nothing else is running.

When I looked at what the field had built, it's almost all the first one. The operational tier is saturated: [Medidata](https://www.medidata.com/en/study-experience/clinical-trial-analytics/), [IQVIA](https://www.iqvia.com/solutions/technologies/orchestrated-clinical-trials/planning-suite/studyoptimizer), [Lokavant](https://www.lokavant.com/). A second tier ([BEKhealth](https://www.bekhealth.com/platform/), [Carta Healthcare](https://www.carta.healthcare/research/), [NIH TrialGPT](https://www.ncbi.nlm.nih.gov/research/trialgpt/)) matches patients in EHR systems to trial criteria but never asks the validity question. Two products edge toward the should side: [QuantHealth](https://quanthealth.ai/) evaluates protocols and populations through simulation, and [PhaseV](https://www.phasevtrials.com/solutions) models protocol trade-offs before lock. But neither frames it as which population the trial is actually asking about, and neither runs anything adversarial against the answer. Competitive density is barely touched.

The same process found where the premise holds: recurrent, cisplatin-refractory head and neck cancer, where cisplatin is still the backbone, the toxicity is the actual reason for discontinuation, "cisplatin-unsuitable" is a published concept, and most competing trials use cisplatin rather than competing for the patients who can't finish it. The lead died in analysis instead of in the clinic.

## What's left

I applied adversarial multi-panel review to clinical trial population validity, and it produced a real redirect. The integration doesn't appear as a commercial product anywhere I looked. The closest comparable is [TRIAGE](https://openreview.net/attachment?id=YYmB6Zi088&name=pdf), an academic prototype that uses a generative agent to propose biological targets, adversarial agents to falsify them, and an output agent to synthesize. Same structural pattern, applied to target validation, not population prediction, and never deployed. Survey methodology solved the frame-validation problem in the 1930s. The [Literary Digest poll](https://en.wikipedia.org/wiki/The_Literary_Digest) drew 2.4 million responses and predicted the wrong outcome because the frame was wrong. Nobody has ported that toolkit to clinical trial population assessment.

So can a small team catch a wrong-population prediction before the money runs out? The Navicyte run says yes. A day, fifty dollars, a redirect. The candidate that would have died the way our advisor described is still in development.

---

## Links & sources

**My prior writing:**
- [Smart Models, Dumb Pipes](https://dbmcco.github.io/2026/03/24/smart-models-dumb-pipes/) — the architectural ancestor (the open-sourced expert-panel simulator). The Navicyte harness applet described here is a production-grade descendant; we're not open-sourcing that version.
- [The Constraint Flipped](https://dbmcco.github.io/2026/06/01/the-constraint-flipped/) — the production-vs-understanding tension this piece extends

**The work this piece describes:**
- [Navicyte](https://navicytebiotech.com) — the population & competitive-landscape monitor described here is a private production tool, not the open-sourced simulator.

**The will / should tool landscape:**
- [Medidata Study Feasibility](https://www.medidata.com/en/study-experience/clinical-trial-analytics/)
- [IQVIA StudyOptimizer](https://www.iqvia.com/solutions/technologies/orchestrated-clinical-trials/planning-suite/studyoptimizer)
- [Lokavant Spectrum](https://www.lokavant.com/)
- [Phesi Trial Accelerator](https://www.phesi.com/trial-accelerator/)
- [Confyde](https://www.confyde.ai/)
- [PSI SYNETIC](https://psi-cro.com/psi-synetic-clinical-trial-site-intelligence-selection/)
- [PhaseV Enrollment Lab](https://www.phasevtrials.com/solutions)
- [BEKhealth](https://www.bekhealth.com/platform/) — patient matching
- [Carta Healthcare](https://www.carta.healthcare/research/) — patient matching
- [NIH TrialGPT](https://www.ncbi.nlm.nih.gov/research/trialgpt/) — patient matching
- [QuantHealth](https://quanthealth.ai/) — protocol/population simulation (closest to "should")

**The closest comparable (the honest novelty test):**
- [TRIAGE: An AI Scientist for Adversarial Target Falsification](https://openreview.net/attachment?id=YYmB6Zi088&name=pdf) — same structural pattern, applied to biological target validation, not population prediction; academic prototype, never deployed

**The frame-validation precedent:**
- [The Literary Digest (Wikipedia)](https://en.wikipedia.org/wiki/The_Literary_Digest) — the 1936 straw poll that drew 2.4 million responses and predicted the wrong outcome because the frame was wrong

*Process note: this post was assist-written with an agent, but the thinking, the argument, and the final edits are my own.*
