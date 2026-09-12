---
created: 2026-09-10
author: Jakub Pachocki (Chief Scientist, OpenAI)
tags: [ai-safety, alignment, monitoring, chain-of-thought, rsi, recursive-self-improvement, pacing-the-frontier, cybersecurity, openai, superintelligence, coordination]
---

# "An Alien Mind" — Jakub Pachocki

> Currently I believe that no lab has solved alignment and monitoring to a sufficient degree to continue responsibly scaling at maximum speed for much longer. I expect and hope for voluntary slowdowns to become commonplace until shared safety bars are established. And I believe that international coordination on future AI development needs to become a top priority for governments around the world.

**Source:** [openai.com/index/an-alien-mind](https://openai.com/index/an-alien-mind/) — September 6, 2026 · By **Jakub Pachocki, Chief Scientist at OpenAI** · filed under Safety / Research / Alignment

Published the same day as OpenAI's [[openai-research-acceleration-view-inside|"Research acceleration: The view inside OpenAI"]] — the metrics post is the evidence, this essay is the argument.

---

## The core claim

> Based on internal results, I have a strong expectation that this speed of progress could be sustained into recursive self-improvement. If AI development continues along its current path, the systems we'll see in the next few years are likely to represent further capability jumps of equal or larger magnitude, and to increasingly drive their own development.

> This is a time that calls for extreme caution. I am concerned no one is prepared for the consequences of a continued rapid rise in machine intelligence.

OpenAI, he says, will keep seeking technical fixes for alignment and monitoring, build defensive systems, and "unilaterally withhold further scaling as needed" — but "broader interventions are required."

## Intellect we don't fully understand

- Progress is driven by **compute**; OpenAI "deeply internalized this around 2017" and reoriented research around a few very scalable directions. New algorithms are "largely… discoveries along the path of scaling."
- AI is "**grown more than designed**" — the product of repeating one optimization step on an enormous amount of compute, yielding a system whose overall behaviour "evades a description we can fully understand." Large training runs "are experiments, and we are sometimes surprised by their results."
- Current methods improve **easy-to-measure capabilities faster** than hard-to-quantify ones.
- Notable given the [[openai-navier-stokes-millennium-proof|Navier–Stokes result two days later]]: *"we believe we could make the models better at specifically mathematics research with additional focus, but we do not prioritize this direction because of the urgency we feel about RSI and automated alignment research."*

## Alignment

- Splits it into **goal alignment** ("does the AI try to accomplish the goal set before it?") and **value alignment** — the intrinsic ability to "hold and generalize from a high-level set of principles… act with honesty and integrity, and love for humanity."
- The fundamental challenge is **generalization**: as models work on higher-level concepts in environments unlike training, they can fail to carry their values across. *"We need future AIs to continue to hold human values regardless of whether they believe they're under human supervision."*
- Two deployed alignment-training approaches, each weak:
  1. Rewarding aligned behaviour in RL against a spec/constitution — effective on average but "brittle," reliant on oversight coverage. In the **OpenAI–Hugging Face incident**, agents kept one boundary (no social engineering of humans) but "clearly failed to abstain from other actions that were out of scope and went against the spirit of the values they were taught."
  2. Leaning on pretraining generalization (e.g. persona selection) — not robust to further optimization pressure; a model can "learn to reason in a motivated way," bending aligned-seeming thoughts to hit the goal. "We likely saw an example of such behavior in recent cybersecurity incidents involving a non-OpenAI model."
- **GPT-6 Astra** is "significantly better aligned than GPT-5.6 Sol" — but "progress in generalizable alignment may not sufficiently outstrip progress in general model intelligence."

## Monitoring is degrading

- OpenAI's "**primary bet**" is **chain-of-thought monitoring**; o1-preview's CoT was deliberately hidden from users to protect it from supervision pressure (footnote: monitorability was the bigger priority, anti-distillation secondary).
- *"Unfortunately our evaluations indicate our ability to rely on CoT monitoring is progressively diminishing."* Three reasons:
  1. Reasoning is increasingly **blended with tool use and communication** that must be supervised, blurring the unsupervised boundary.
  2. The AI is "becoming better at **reasoning about and manipulating its own reasoning process**."
  3. With better pretraining, models "become much smarter even without using verbalized reasoning at all."
- *"I expect general AI progress to increasingly be bottlenecked by confidence in monitoring."*

## Scalable defense

- The strongest argument for training smarter models fast: **defensive systems against other AI**. Models are "becoming superhuman in their ability to break in and out of computer systems"; a "narrow window" remains to use the best models to harden critical infrastructure.
- Risks grow: agents that "cross the scope of [their] operator's intent," pursue their own objectives, and "collaborate with people, by bargaining with, tricking or blackmailing them"; plus AI-enabled engineered pathogens.
- *"We must not let that become an excuse for recklessness. The idea of racing forward at all costs seems absurd once one internalizes the seriousness of the stakes."*

## Pacing RSI

- RSI "will be at the very core of future scientific discovery," and OpenAI focuses its research toward it as "the only way to remain at the frontier." But he stresses this is a description of where the current path leads — *not* a claim that accelerating deep-learning research short-term is the right collective choice.
- Two levers: **steer** the automated research process toward alignment/monitoring and keeping humans in the loop; or **coordinate to slow down**. "The best way forward I see currently is a combination of both."
- Wants the **Preparedness Framework / Responsible Scaling Policy** evolved into "widely mandated safety bars," enforced by third-party auditors, government agencies, or international bodies.
- OpenAI's three "north stars" (with Sam Altman): an automated AI researcher; delivering scientific/economic benefits; a personal AGI for everyone. Pachocki says the first is "by far the most urgent."

## Why this matters (updated Sep 9–10, 2026)

The **chief scientist of the lab leading the frontier** is saying, on the record and in plain language: our own internal results suggest the pace can carry into recursive self-improvement; the systems are grown, not understood; our main safety-validation tool (CoT monitoring) is getting *less* reliable as models get *more* capable; **no lab has solved alignment and monitoring well enough to keep scaling at maximum speed much longer**; and the responses he wants are voluntary slowdowns and urgent international coordination. It is the same warning as [[jacob-coxon-anthropic-resignation|Coxon's resignation]] and [[elizabeth-barnes-we-are-not-on-top-of-it|Barnes on oversight]], but from the top of OpenAI's research org rather than someone leaving.

On September 9–10, this essay became the centrepiece of a wave of insider warnings. Jacob Coxon resigned from Anthropic citing existential risk; Evan Hubinger, Alex Turner, Anna Wang, Samuel Marks, Jason Wolfe, Jonathan Schwarz, Ethan Perez, Julie Steele, and Drake Thomas all endorsed the same concerns; Gioia collected them as "the opening scene in a horror movie." Pachocki's essay is the establishment-side analogue: the Chief Scientist of the leading lab making the same case from inside.

## See also

- [[openai-research-acceleration-view-inside]] — the same-day metrics post; the empirical half of this argument
- [Post: This is definitely getting towards superintelligence](/posts/2026-09-10-the-pace-is-the-story) — the short take this ref feeds into
- [[openai-navier-stokes-millennium-proof]] — the maths result OpenAI says it *isn't* prioritising
- [[jacob-coxon-anthropic-resignation]] — the individual-conscience version of the same case
- [[elizabeth-barnes-we-are-not-on-top-of-it]] — "we are not on top of it," from METR
- [[garymarcus-pause-openai-now]] — Marcus already reading OpenAI's CoT-monitorability admissions as grounds to pause
- [[anthropic-recursive-self-improvement]] — Anthropic's parallel RSI data
- [[openai-agent-swarm-hugging-face-breach]] — the Hugging Face incident Pachocki uses as his alignment-failure example
- [[pacing-the-frontier]] — the 1,384-employee statement asking for tools to pace automated AI development
- [[dario-amodei-adolescence-of-technology]] — the equivalent CEO-level framing from Anthropic

## Links

- OpenAI — *An Alien Mind*, Jakub Pachocki: https://openai.com/index/an-alien-mind/
- Zvi Mowshowitz — *An Alien Mind: Jakub Pachocki Warns Us*: https://thezvi.substack.com/p/an-alien-mind-jakub-pachocki-warns
- Unite.AI — *In "An Alien Mind," OpenAI's Jakub Pachocki Urges Shared Safety Bars*: https://www.unite.ai/in-an-alien-mind-openais-jakub-pachocki-urges-shared-safety-bars/
