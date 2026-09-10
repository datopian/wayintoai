---
created: 2026-09-10
author: Rufus Pollock
tags: [ai, mathematics, navier-stokes, pace-of-progress, scaling, superintelligence, takeoff, commentary, opinion]
---

# The real story isn't the proof — it's the pace

*A short comment, prompted by [[openai-navier-stokes-millennium-proof]]. Written up as a full post: [A Millennium Problem fell this week. The pace is the story.](/posts/2026-09-10-the-pace-is-the-story)*

On September 8, 2026, OpenAI announced a proof — Lean-formalized — that the Navier–Stokes equations can blow up in finite time. That would settle one of the seven Millennium Prize Problems: a genuine flagship of modern mathematics, open for roughly ninety years. There is a real controversy attached (priority, a rival NYU/Anthropic team, Codex drafts, intimidation allegations, Terence Tao's "strip-mining" lament) and it deserves attention. See the [[openai-navier-stokes-millennium-proof|main entry]] for all of that.

But the result is not what I find striking. **The pace is.**

## Look at the last eight weeks

- **July 2026:** a dozen decades-old problems fall in a fortnight — the Jacobian conjecture (87 years), the Maxwell conjecture (153 years), Dinitz–Garg–Goemans, Levit–Mandrescu, a clutch of Erdős problems — many solved by mathematicians just *asking a chatbot and insisting it keep going*. ([[ai-is-rewriting-mathematics]])
- **August 1, 2026:** OpenAI's Astra solves **10** major open problems across mathematics, quantum complexity and theoretical CS for under $2,000 of API spend. ([[ai-and-mathematics]])
- **September 5, 2026:** a swarm of ~10,000 agents resolves **Navier–Stokes** in 88 hours.

Each rung up that ladder is a bigger problem, solved faster, for less.

## The part that should stop you

The model that did Navier–Stokes **is not Astra**. It is an unreleased internal model that, by OpenAI's own statement, **has only been training since August 28** — thirteen days before the announcement, and *still training*. OpenAI's own chart (reproduced in the [[openai-navier-stokes-millennium-proof|main entry]]) shows it at roughly **two to three times Astra's pass rate** on a curated set of open math problems, at every compute budget on the sweep.

So: less than two weeks of training on a new model, and it is already well past the system that, a month earlier, had cleared ten flagship problems.

## Why I think this matters more than the proof

The interesting quantity here is not the *level* — it's the *derivative*, and the derivative of the derivative. In July the frontier was "AI helps a mathematician close a specific old problem." Six weeks later it is "a partially-trained model, running as a 10,000-agent swarm, closes a Millennium Problem over a weekend — and its makers say it's getting better daily."

If a new model can gain that much ground in thirteen days, the gap between "impressive research assistant" and "does frontier mathematics faster than the field can absorb it" is being crossed in *weeks*, not years. That is what a takeoff curve looks like from the inside. Tao's worry about the mathematical ecosystem being strip-mined assumes there is time to react; the pace here suggests there may not be.

I don't want to over-claim from a single announcement, especially a contested one. But if the "training since August 28" line is accurate, this is one of the clearer public signals so far that we are moving toward something that deserves the word **superintelligence** — and moving toward it quickly.

## See also

- [[openai-navier-stokes-millennium-proof]] — the result and the controversy in full
- [[ai-and-mathematics]] — the milestone timeline
- [[ai-is-rewriting-mathematics]] — the July–August run
- [[openai-research-acceleration-view-inside]] — OpenAI's own internal metrics: 3.1 agent-workdays per human workday, "automated research intern" declared shipped
- [[an-alien-mind-pachocki]] — OpenAI's Chief Scientist: the pace could sustain into RSI, and no lab has solved alignment/monitoring well enough to keep scaling at max speed
- [[anthropic-recursive-self-improvement]] — the feedback-loop framing
- [[elizabeth-barnes-we-are-not-on-top-of-it]] — "we are not on top of it," from the oversight side
