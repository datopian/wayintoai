---
created: 2026-09-26
author: Flavio Copes
tags: [cursor, pstack, skills, review, coding-agents, engineering-workflow]
---

# A Deep Dive into pstack (Flavio Copes)

Flavio Copes's walkthrough of [[pstack]], Lauren Tan's Cursor plugin for rigorous AI-assisted engineering. Published 2026-08-21.

![Article](https://screenshotit.app/https://flaviocopes.com/pstack/)

## Links

- **Article**: https://flaviocopes.com/pstack/
- **Subject**: [[pstack]]

## Key points

> AI coding agents can write a lot of code, but engineering also means understanding the existing system, choosing a good design, verifying the result, reviewing the diff, and shipping it without breaking something else.
>
> pstack is a Cursor plugin built around that problem. […] The stated goal is not more code. It is less code, higher quality, and enough verification that several agents can work in parallel without turning the repository into a mess.
>
> It currently contains 23 workflow skills, 21 engineering principles, 22 task playbooks, 2 specialized subagents, helper programs, and an optional automation pack.

On portability:

> Does pstack work outside Cursor? Yes. The official package is a Cursor plugin. The skills themselves are SKILL.md files. That is the same format Claude Code, Codex, and other coding agents already load. You can copy the skill folders into that tool's skills directory. If you want a ready-made Claude Code port, use pstack-claude. It is not the official package. It translates Cursor-specific pieces to Claude Code equivalents, and it also ships a Codex plugin.

## Takeaways

- `/poteto-mode` is the single front door: picks a playbook, makes a task list, delegates by model, demands evidence.
- Verification is treated as a repo capability, not a one-off.
- `/interrogate` triages multi-model review findings into actionable / considered / noted / dismissed.
- Verdict: worth it for migrations, performance work and auditable autonomous runs; overkill for routine small changes.
