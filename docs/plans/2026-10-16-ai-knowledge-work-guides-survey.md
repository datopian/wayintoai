---
title: Survey — existing guides on AI for knowledge work, and what ours adds
created: 2026-10-16
status: research note (AI-gathered; not yet reviewed by Rufus)
beads: pl-4pep (rufuspollock/planning)
---

# Survey: guides on using AI for knowledge work

Purpose: before we publish the "AI for Knowledge Work" section of Way Into AI, see what already exists for beginners and the intermediate non-coder, and be clear what ours adds. Our v1 is two pieces: "Post-its and filing cabinets" (how to organise shared work, concepts-first) and a manifesto / "how to use AI" intro (thesis: the AI is the interface, apps are storage). Prior research on the practitioner end is in `life-itself/planning/docs/plans/2026-10-10-ai-practice-research.md` and is reused, not repeated, here.

Verification key: **[opened]** I read the page myself in this session. **[snippet]** only search-result summaries or third-party write-ups, so treat details as unconfirmed. **[prior]** from the 2026-10-10 research note. Dates and prices in this area change fast.

## 1. The landscape in one paragraph

Nearly everything for beginners falls into four types. (a) **Vendor "getting started" guides** (Anthropic, OpenAI, Google, Microsoft): tool-specific, prompt- and use-case-led, mostly assume one person with one task. (b) **Mindset and skills frameworks** (Mollick, Anthropic's AI Fluency): how to think about delegating to and judging AI, with no treatment of where work is kept. (c) **Courses** (Andrew Ng, Every, Forte Labs): paid or time-heavy, aimed at either understanding the technology or building a personal system. (d) **Practitioner posts** (Lenny, Torres, Citrix and others): personal setups using agents on local files, strong on practice but written for the already-converted, and individual rather than shared. Almost nothing explains *how a team's documents and tasks should be organised* so that AI can work in them, and almost nothing starts from "the AI is the interface".

## 2. Comparable guides

### Frameworks and mindset

**1. Ethan Mollick, "A Guide to Which AI to Use in the Agentic Era"** — One Useful Thing, 18 Feb 2026. https://www.oneusefulthing.org/p/a-guide-to-which-ai-to-use-in-the **[opened]**
- Audience: general knowledge workers using or considering AI for real work, including people comfortable with chatbots who want agentic tools.
- Covers: model vs app vs harness; pay about $20/month and pick the strongest model manually; chatbots for casual use, agentic apps (Claude Code, Cowork, Excel/PowerPoint integrations, NotebookLM) for substantial work; test on real tasks; manage rather than prompt.
- Differs from ours: it is a *buyer's guide* to tools and ages quickly. It says nothing about how work is stored or organised. It is the best "which tool" link to give beginners, which we do not want to duplicate.

**2. Ethan Mollick, "Management as AI superpower"** — One Useful Thing, 27 Jan 2026. https://www.oneusefulthing.org/p/management-as-ai-superpower **[opened]**
- Audience: managers and professionals. Practical, accessible tone.
- Covers: delegating to agents is a management skill. Whether to delegate depends on human time, probability of acceptable output, and review cost. "What's scarce is knowing what to ask for."
- Differs: same spirit as our principle 8 ("you still think and steer") and gives it a sharper, citable rationale. Does not touch organising files or shared work.

**3. Ethan Mollick, "Claude Code and What Comes Next"** — 7 Jan 2026. https://www.oneusefulthing.org/p/claude-code-and-what-comes-next **[opened]**
- Audience: programmers mainly, but explicitly "programming-adjacent" people and knowledge workers.
- Covers: why agent harnesses (compaction, skills, subagents, MCP) matter; risks of giving an AI file and browser access; suggests non-coders try research reports and spreadsheet analysis; predicts harnesses for other knowledge work.
- Differs: the "why this is different now" argument. We assume it and go straight to the consequence (organise your work for it). Useful link for readers who ask why.

**4. Ethan Mollick, *Co-Intelligence* (2024) and *Co-Existence* (due 20 Oct 2026)** — books. Publisher listing only **[snippet]**.
- Audience: general readers and managers. A playbook for working with the latest AI (Co-Existence).
- Differs: book-length, general mindset. Neither is a practice for shared documents and tasks. Worth linking from "further reading" once Co-Existence is out and we have read it.

**5. Anthropic, "AI Fluency: Framework & Foundations" course** — Anthropic with Rick Dakan and Joseph Feller; announced 15 Jun 2025. https://www.anthropic.com/ai-fluency/overview (via https://www.theneuron.ai/explainer-articles/inside-anthropics-ai-fluency-masterclass-on-human-ai-collaboration) **[opened, secondary page]**
- Audience: anyone working with AI; tool-agnostic. Free, 12 video lessons, about 3–4 hours, certificate. Framework is CC BY-NC-SA 4.0 **[snippet]**.
- Covers: the 4Ds (Delegation, Description, Discernment, Diligence) and three interaction modes (automation, augmentation, agency).
- Differs: skills of the individual in conversation. Nothing on storage, shared work, or where the AI gets its context. Complementary: the 4Ds map onto our "you still think and steer" and "talk to it". Link, do not rebuild.

### Vendor guides

**6. Anthropic, "Best practices for getting started with Claude Cowork"** — Austin Lau, 3 Jun 2026. https://claude.com/blog/best-practices-for-getting-started-with-claude-cowork **[opened]**
- Audience: non-technical knowledge workers (email, decks, spreadsheets, documents).
- Covers: chat for quick answers vs Cowork for multi-step deliverables; how to tell if a task fits; start with a task you know well; context matters more than prompt wording; ask Claude to restate and clarify first; schedule recurring work.
- Differs: closest vendor guide to our audience, but task-led and tool-specific. Mentions pointing it at a folder and connecting Drive/Slack/Gmail, but does not explain how to organise files, shared team workspaces or storage concepts. This is exactly the gap our concepts piece fills.

**7. OpenAI, "Identifying and scaling AI use cases"** — OpenAI business guide, 2025. https://openai.com/business/guides-and-resources/identifying-and-scaling-ai-use-cases/ **[snippet; page returned 403 to my fetch]**
- Audience: enterprise leaders and teams rolling out ChatGPT.
- Covers: finding use cases in repetitive tasks, skill bottlenecks and ambiguity; six "primitives" (content creation, research, automation, coding, data analysis, ideation/strategy); leadership should lead; start simple.
- Differs: organisational adoption playbook for leaders, not a how-to for a person or small team. Use-case-led, not storage-led.

**8. Google, "Gemini for Google Workspace: Prompting Guide 101"** — Google, April 2024, updated Oct 2024 edition. https://services.google.com/fh/files/misc/gemini-for-google-workspace-prompting-guide-101.pdf **[snippet; the PDF link returned 404 to my fetch]**
- Audience: Workspace users; role-specific tips. Free, about 68 pages.
- Covers: prompt = persona + task + context + format; examples by role.
- Differs: prompting craft inside Google's apps, i.e. the "apps are the interface" model we argue against. Dated.

**9. Microsoft, Work Trend Index 2025 and 2026 ("Frontier Firm")** — WorkLab. 2025 post: https://www.microsoft.com/en-us/microsoft-365/blog/2025/06/26/how-microsoft-365-copilot-and-agents-help-tackle-the-infinite-workday/ **[snippet]**; 2026 figures only via third-party summaries (mer.vin) **[snippet, unreliable]**.
- Audience: leaders and managers; survey-based reports.
- Covers: Frontier Firms, human-agent teams, collaboration patterns (Author, Editor, Director, Orchestrator), culture and manager support mattering about twice as much as individual mindset (per a secondary summary).
- Differs: research and strategy, not a how-to. Useful as evidence that organisational practice matters more than individual skill, which supports a *team* guide. Check the original before citing numbers.

**10. Zapier, AI Playbook** — Zapier, 2025–26. Only via a consultancy summary (gend.co) **[snippet]**.
- Audience: companies adopting AI across non-technical teams.
- Covers: sequence of urgency, safe guidelines, "fluency sprints", process design, then automation with Zaps and agents.
- Differs: adoption and automation, written by an automation vendor. Overlaps with our "develop processes for you and your AI", but at company rollout level.

### Courses

**11. Andrew Ng / DeepLearning.AI, "AI for Everyone" and "Generative AI for Everyone"** — Coursera. https://www.deeplearning.ai/courses/ai-for-everyone and https://www.deeplearning.ai/short-courses/generative-ai-for-everyone/ **[snippet]**
- Audience: non-technical professionals; about 6–7 hours each; beginner.
- Covers: what AI and generative AI are, how they work, what they can and cannot do, spotting opportunities in an organisation.
- Differs: "understand the technology", not "change how you work". Good foundation link for the very newest beginner; we should not try to cover the technology explainer.

**12. Every, "Claude Code for Beginners" / claude101.every.to** — Dan Shipper and Every. https://every.to/events/claude-code-101 and https://claude101.every.to **[snippet]**
- Audience: curious non-developers and developers intimidated by the terminal; one-day live workshop (Nov 2025 cohort closed), plus a self-serve site.
- Covers: install, assign tasks, ship a project in a day.
- Differs: hands-on tool onboarding and building. Not about organising shared work. The workshop format is a reminder that beginners want a guided first win.

**13. Forte Labs, "AI Second Brain"** — Tiago Forte. https://help.fortelabs.com/hc/en-us/articles/44591754695821-What-is-the-AI-Second-Brain **[snippet]**
- Audience: individual knowledge workers, existing BASB audience. Paid three-week live programme (first cohort Apr–May 2026, second planned autumn 2026).
- Covers: "Personal Context Management": give the AI your notes and files in the right form. Extends PARA.
- Differs: closest in spirit to our "storage is what matters" and the cabinet/folder metaphor (PARA is itself a filing scheme). But it is personal, paid, and cohort-based. Ours is shared/team work, free and concept-first. The nearest overlap risk, but not a free public guide.

### Practitioner posts (already in the prior research; headlines only)

**14. Lenny Rachitsky, "Everyone should be using Claude Code more"** — 14 Oct 2025. https://www.lennysnewsletter.com/p/everyone-should-be-using-claude-code **[prior, partial paywall]**. Agent on local files for non-coding work. Examples, not concepts; individual.

**15. Teresa Torres on `/today` with Claude Code and Obsidian** — via ChatPRD / How I AI, Jan 2026. https://www.chatprd.ai/how-i-ai/teresa-torres-claude-code-obsdian-task-management **[prior]**. Closest practice match to our "what's on today". Individual setup, not explained for beginners.

**16. Citrix, "Workers' second brains..." / "The 7 stage roadmap for human-AI collaboration, 2026 edition"** — Citrix blog, Feb and Jun 2026. https://www.citrix.com/blogs/2026/06/10/the-7-stage-roadmap-for-human-ai-collaboration-2026-edition/ **[snippet]**. Describes the "second brain" as plain-text files both person and AI read and write, the same architecture as ours, framed for a security and IT audience. Notes it is still a small minority practice. Confirms the idea is spreading, but not as a beginner guide.

(The prior note also covers Steve Yegge on Beads, Anthropic's harness and context-engineering posts, and Jamin Ball / Steven Lin on systems of record. Those support our thesis but are written for developers and builders, not beginners.)

## 3. Gap analysis

### Where ours is distinctive

1. **Organising shared work is the unaddressed topic.** None of the beginner guides above explains how a *team's* documents and tasks should be laid out so AI can work in them. Vendor guides stop at "point it at a folder"; Mollick and Anthropic Fluency are about the individual's conversation with the AI; Forte is personal. The cabinet / post-it / pointer model (including the "overview problem" and why a pointer beats a copy) appears to be original and is the strongest asset.
2. **Concepts first, tool second.** Most guides are tool-led and date quickly (model names, plan names). A tool-neutral office metaphor that maps to Drive *and* text-plus-git will age better.
3. **"AI is the interface; apps are storage" as the organising thesis.** The idea is in the air (Ball, Lin, Webb, Citrix) but nobody has put it in front of beginners as a plain statement with a practice attached ("what's on today?", "land the plane"). The vendor guides implicitly keep apps as the interface.
4. **Honest about the limits.** Principle 8 plus the research on workslop, METR and cognitive debt gives a "you still think" caveat that vendor guides under-emphasise.
5. **The pointer idea, "land the plane", and "AGENTS.md as the note inside the cabinet door"** turn infrastructure into something a non-programmer can picture.

### What to borrow or link to

- **Link out for "which AI should I use / how do I start":** Mollick's Feb 2026 guide, and Anthropic's Cowork best-practices post. Do not write our own tool buyer's guide.
- **Link out for individual skills:** Anthropic's AI Fluency (free, CC BY-NC-SA, so quotable with attribution but non-commercial and share-alike, so check before copying anything into Way Into AI). Map our principles onto the 4Ds in one line.
- **Link out for "what is generative AI":** Ng's *Generative AI for Everyone*, for readers needing the technology basics.
- **Borrow Mollick's delegation test** (human time, probability of success, review cost) as the evidence behind "you still think and steer".
- **Borrow the "start with a real task you know well" framing** (Anthropic, Mollick) for a first-win exercise at the end of each piece. Our concepts piece currently has none.
- **Borrow Microsoft's four patterns (Author, Editor, Director, Orchestrator)** only if we need a vocabulary for degrees of delegation. Verify against the original first.
- Reuse the prior note's borrowable patterns: "land the plane", `/today`, two-tier memory, "what did we learn?".

### Risk of duplicating something better

- **Low:** the filing-cabinet concepts piece. No equivalent found. (Caveat: this is a web-search survey, not exhaustive; Forte Labs and Citrix are the nearest, and I could not read Forte's materials.)
- **Not a concern (Rufus, 2026-10-16):** the manifesto's thesis. "Work in the AI, not in apps" overlaps with Mollick's agentic-era writing, Karpathy, and the systems-of-record posts, and that is welcome: convergence is evidence. Link to them, and keep the practice (the four everyday situations) as what we add. The thesis also gets its own blog post with a growing "others saying this" section (wayintoai-z1c).
- **Medium, tool-picking content:** anything in our intro that recommends specific tools or plans should be dropped or replaced by a link to Mollick, who updates his guide and has more authority.
- **Watch:** Anthropic and others are moving fast into this space (Cowork, Skills, projects, connectors). Within months vendors may publish "organise your files for Cowork" guidance. A concepts-first piece is more defensible than a tool-specific one, but we should publish soon and avoid tool-specific claims.

### Suggested v1 adjustments

1. Add a short "Where to start" box on the section index linking Mollick (which AI), Anthropic Fluency (skills) and Ng (basics), so readers do not expect us to cover them.
2. Add one first-win exercise to each piece: "ask your AI what's in this folder", "write a pointer for one project".
3. Add a footnote for each principle that has outside backing (Mollick for steering; METR and the workslop study for the caveats). The prior note has the links.
4. Before publishing, read the Forte Labs AI Second Brain materials and Citrix piece in full, and re-check items marked [snippet].

## 4. Not found / gaps in this survey

- No Notion, Asana or Atlassian beginner "AI at work" guide turned up in search. Not checked on their own sites.
- Google's "AI Essentials" course (Grow with Google) returned nothing; unverified whether it exists in current form.
- OpenAI's guide and Google's PDF could not be opened (403 and 404), so their entries rest on summaries.
- Non-English and academic-library guides were not searched.
