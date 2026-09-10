---
title: A Millennium Problem fell this week. The pace is the story.
description: OpenAI says an internal model resolved Navier–Stokes. The striking part isn't the proof — it's that the model has only been training since August 28.
date: 2026-09-10
---

On September 8, OpenAI [announced](https://openai.com/index/navier-stokes-solution/) a Lean-formalised proof that the Navier–Stokes equations can blow up in finite time. If it holds up under review, that settles one of the seven Clay [Millennium Prize Problems](https://www.claymath.org/millennium-problems/) — a genuine flagship of modern mathematics, open in its modern form since the 1930s.

It's a big result. It also comes with a real controversy: a rival NYU/Anthropic team says OpenAI scooped an approach they'd already verified, there are questions about whether draft work sitting in Codex was safe, and Terence Tao has warned about "strip-mining" open problems. I've written that up [separately](/ref/openai-navier-stokes-millennium-proof). It matters, and it's not settled.

But the proof isn't what I keep thinking about. **The pace is.**

## Eight weeks

- **July 2026:** roughly a dozen decades-old problems fall in two weeks — the Jacobian conjecture (87 years), the Maxwell conjecture (153 years), a run of Erdős problems. Several were closed by a mathematician literally asking a chatbot for a counterexample and telling it to keep going. ([timeline](/ref/ai-is-rewriting-mathematics))
- **August 1:** OpenAI's Astra model [clears 10 major open problems](/ref/ai-and-mathematics) across maths, quantum complexity and theoretical CS — for under $2,000 of API spend.
- **September 5:** a swarm of about 10,000 agents resolves Navier–Stokes in 88 hours.

Every rung up that ladder is a bigger problem, solved faster, for less.

## Thirteen days

Here's the line in OpenAI's announcement that should stop you:

> Since August 28 we have been training a new internal model that has exhibited unprecedented performance in our benchmarks, including mathematics. This model's training is ongoing and its performance continues to improve.

The model that did Navier–Stokes is **not Astra**. It's an unreleased model that had been training for **thirteen days** when the proof landed — and is still training. OpenAI's own chart puts it at roughly two to three times Astra's pass rate on a curated set of open maths problems, at every compute budget they tested.

![OpenAI's chart: the new internal model (training since Aug 28) against GPT-6 Astra on open maths problems — roughly 2–3× the pass rate at every compute level](/assets/openai-new-model-since-aug-28-2026-09-10.jpg)

So: under two weeks of training on a new model, and it's already well past the system that, a month earlier, had cleared ten flagship problems.

## The derivative, not the level

The interesting quantity here isn't how good the model is. It's how fast that number is moving — and whether the rate itself is increasing.

In July the frontier was "AI helps a mathematician close a specific old problem." Six weeks later it's "a half-trained model, run as a 10,000-agent swarm, closes a Millennium Problem over a weekend, and its makers say it's improving day by day." If a fresh model can gain that much ground in thirteen days, the distance between "impressive research assistant" and "does frontier mathematics faster than the field can absorb it" is being crossed in *weeks*.

That's what a takeoff curve looks like from the inside.

## It's not just the maths

The same week, OpenAI published [two other things](/ref/openai-research-acceleration-view-inside) that point the same direction:

- A [metrics report](/ref/openai-research-acceleration-view-inside) on its own research org: as of mid-August it runs **3.1 agent-workdays of effort for every human workday**, the median researcher spends over $600/day on internal coding agents, and OpenAI says it has hit its "automated research intern" milestone — with an "automated AI researcher" pencilled in for March 2028.
- An [essay by chief scientist Jakub Pachocki](/ref/an-alien-mind-pachocki), "An Alien Mind," saying plainly that internal results give him "a strong expectation that this speed of progress could be sustained into recursive self-improvement," that chain-of-thought monitoring is getting *less* reliable as models get more capable, and that "no lab has solved alignment and monitoring" well enough to keep scaling at maximum speed much longer.

The thing that's accelerating isn't just problem-solving. It's the process that builds the models.

## Saying it plainly

I don't want to over-claim from a single announcement, especially a contested one that still needs to survive peer review. Any one of these results could be softer than the headline.

But the trend across eight weeks doesn't depend on any single result. Decades-old problems in July; ten of them at once on August 1; a Millennium Problem this week, by a model that didn't exist a fortnight ago — while the lab that built it talks openly about recursive self-improvement and asks governments to coordinate.

I think we are now watching the approach to superintelligence, and it is happening faster than almost anyone budgeted for.
