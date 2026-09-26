---
title: "How do you handle the \"pre-work\" phase without gunking up your repository?"
description: "Where to dump the early design experiments and research that go into a project or a major new feature? Do I put it in a branch, or just pull the trigger on a separate repo?"
date: 2026-01-12
---

I’ve been thinking about a pattern I keep running into at the very start of AI development.

Before the “real” coding begins, I’m usually deep in experimentation—trying to nail a landing page or a specific look and feel. Or I’m doing heavy marketing and product research and suddenly have a whole bunch of materials.


The problem is: **where do I store this stuff?** I want a place to keep it all together, but I really don’t want to pollute the main part of the repo. I’ve been weighing two paths:

- **The Branch Strategy:** Keeping it in a separate branch within the main project.

- **The Prefix Strategy:** Creating a completely separate repo with a prefix like `design-project-name`

I’m leaning toward the separate repo. There’s something about keeping the core codebase “pure” while letting the preliminary chaos live elsewhere. But I wonder if that’s just creating more silos.

How are you all handling the “pre-work” phase?

