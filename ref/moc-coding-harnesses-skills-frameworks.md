---
created: 2026-09-26
tags: [moc, coding-agents, harness, skills, frameworks, claude-code, codex, cursor, context-engineering]
---

# MOC: Coding Harnesses, Skills & Frameworks

Map of Content for the layers around a coding model: the **harness** it runs in, the **skills** that teach it, and the **frameworks** that impose a workflow (plan, execute, verify, review) on top.

## Harnesses (the agent runtime)

- [[pi.dev]] — minimal, terminal-first, deeply extensible.
- [[harness-engineering-openai]] — OpenAI's account of shipping a product with Codex and no hand-written code; how to shape the environment.
- [[symphony-openai]] — turns a Linear board into isolated autonomous runs.
- [[moc-agent-workbenches]] — environments that run and coordinate agents ([[bb]], [[paperclip]], [[dmux]]).

## Skills (packaged know-how)

- [[anthropic-skills-guide]] — Anthropic's guide to building skills.
- [[skill-vs-agents-vs-claude-md]] — where each kind of instruction belongs.
- [[moc-best-ai-skills]] — shortlist of skills worth adopting.
- [[company-skills-library]] · [[skills-managers]] · [[openskills]] — sharing and distributing skills.

## Frameworks (workflow on top)

- [[pstack]] — Cursor plugin: 23 skills, 21 principles, 22 playbooks; `/poteto-mode` routes work, verification and multi-model review built in. Skills are `SKILL.md`, so portable (unofficial Claude Code port: pstack-claude). Review: [[pstack-review-flavio-copes]].
- [[gsd-core]] — spec-driven loop (discuss, plan, execute, verify, ship) using fresh-context subagents.
- [[moc-loop-engineering]] — loops that prompt agents on a schedule.
- [[moc-planning-work]] — planning before delegating.

## Pattern

`SKILL.md` is becoming the common packaging format across Claude Code, Codex and Cursor, so frameworks increasingly ship as portable skill folders rather than tool-specific plugins. What differs is the harness features they lean on (per-role model assignment, subagents, hooks).

---

*Grows as harnesses, skills and frameworks earn a place.*
