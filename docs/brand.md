# Way Into AI

Brand, narrative and offer. Agreed 2026-09-25 (bead wayintoai-bnd). Full brief with mood board and visual directions: https://claude.ai/artifact/DLpmX593GvBX214vHLxCb9

## Narrative

> You can't make sense of AI without using it, and you can't use it well without making sense of it.

The site had three competing identities: a tutorial (how to use AI), an on-ramp (a way into AI for non-insiders), and a sensemaking project (what AI is doing to work, power and society). They are one practice: someone who uses these tools every day, watches the frontier closely, and reports back with an opinion. The site is the open notebook; the weekly email is the edit.

## Promise and offer

- **Promise:** What mattered in AI this week, and what to do about it.
- **Offer:** a free weekly email, sent on Tuesdays, our opinionated selection. The email signup is the primary call to action everywhere.
- **Each issue:** three to five developments with our take on why they matter; one thing to try (a tool, workflow, guide or reference for people using AI); the bigger picture (work, power, policy, safety); smaller finds from the log, one line each. Everything links back to the site.
- **Issue format:** sender `Way Into AI`, subject is the lead item's hook, preheader starts `Week N.` (ISO week of the Tuesday send date), site title `What mattered · week N`; one markdown file per issue in `weekly/` serves as both the site page and the email body. Drafted by the `weekly-roundup` skill (`.agents/skills/weekly-roundup/SKILL.md`).

## Audience

Capable generalists who use AI at work and care where it is going. Not insiders; not beginners.

## Voice

First person, opinionated, specific. Says "we think" and "we don't know yet". Concrete examples and honest uncertainty over hype, doom or jargon. No sponsored picks, no firehose, no AI-generated digest.

## Name

Site and email are both **Way Into AI**; the email is "Way Into AI Weekly". "AI Learned Today" (old Substack name and logo) is retired: "today" promises daily and "learned" covers only half the offer. Revisit after eight issues if the name still gets in the way. Final sign-off tracked in wayintoai-bnd.3.

## Structure

- **Use AI** (`/use`): guides, workflows, tools, agentic coding.
- **Understand AI** (`/understand`): capability, governance, work, power, safety, consequences.
- **Posts** and **Log** are the chronological record. The two routes are ways into the archive, below the email offer.

## Visual identity: "blue pencil"

Built on top of the Flowershow Monospace theme. Selection is the product, so the motif is the editor's blue pencil: things are marked, ticked, chosen.

- **Type:** IBM Plex Mono for structure (navigation, labels, lists, literal `#`/`##` heading markers); Newsreader serif for voice (headlines, titles, prose).
- **Colour:** paper `#fbfbf9`, ink `#1b1b1d`, muted `#5f5f66`, rule `#e2e2de`, one accent, editor's blue `#2140c4` (wash `#e8ecfd`). Dark: paper `#0e0e10`, ink `#e9e9e6`, blue `#93a6ff`.
- **Logo:** the text `A→]` in IBM Plex Mono semibold, white on editor's blue. The arrow is "a way into"; the bracket closes on AI. Files: `assets/logo.png` (512px), `assets/logo-160.png` (nav), `assets/favicon.png`.
- **Form:** hairline rules, no cards, no shadows, no rounded corners, no generic AI imagery.

Implementation notes live in `DESIGN.md`.
