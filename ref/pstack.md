---
created: 2026-09-26
author: Lauren Tan (@poteto)
tags: [cursor, coding-agents, skills, engineering-workflow, verification, parallel-agents, plugin, framework]
---

# pstack

Cursor plugin of engineering workflows, principles and playbooks: less code, higher quality, and enough verification that several agents can work in parallel.

![pstack](https://screenshotit.app/https://github.com/cursor/plugins/tree/main/pstack)

## Links

- **GitHub**: https://github.com/cursor/plugins/tree/main/pstack
- **Review**: [[pstack-review-flavio-copes]] (https://flaviocopes.com/pstack/)
- **Claude Code port (unofficial)**: https://github.com/michael-denyer/pstack-claude
- **Install (Cursor)**: `/add-plugin pstack`, then `/setup-pstack`
- **License**: MIT

## Overview

Built by Lauren Tan (@poteto; previously Meta, Netflix, React core team) inside Cursor's plugins repo. Its premise: "throughput without quality is not a goal." AI agents write a lot of code; engineering also means understanding the existing system, choosing a design, verifying the result, reviewing the diff and shipping without breakage. pstack packages that discipline.

It is much bigger than a prompt pack: 23 workflow skills, 21 engineering principles, 22 task playbooks, 2 specialised subagents, helper programs and an optional automation pack (including issue triage).

The main entry point is `/poteto-mode`: describe the task, it picks a playbook (bug fix, performance, feature, refactor, overnight run…), builds a task list, delegates to suitable models and demands evidence before reporting success.

## Notable skills

- `/how`, `/why`, `/teach`, `/recall` — understand the current system, past decisions, and previous work.
- `/architect` — design starting from caller usage.
- `/arena` — competing attempts, synthesised.
- `/swarm` — parallel agents.
- `/interrogate` — send a diff to several models and triage findings.
- Verification skills — "verify it" becomes a repo capability, not ad-hoc testing.

## Works outside Cursor?

Yes, in part (per [[pstack-review-flavio-copes]]). The official package is a Cursor plugin, but the skills are `SKILL.md` files, the format Claude Code, Codex and others load; copy the skill folders into that tool's skills directory. `pstack-claude` is a ready-made, non-official Claude Code port (also ships a Codex plugin). Cursor remains the best fit since pstack assigns different models per role.

## Why interesting

A full engineering-process framework shipped as skills, with verification and multi-model review as first-class steps. Compare [[gsd-core]] (spec-driven loop) and the [[moc-loop-engineering]] primitives. Heavyweight for small changes.

See [[moc-coding-harnesses-skills-frameworks]].
