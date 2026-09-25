# Redesign: brand narrative and email-first site (2026-09-25)

Epic: wayintoai-bnd. Brief, mood board and directions: https://claude.ai/artifact/DLpmX593GvBX214vHLxCb9. Canonical brand: `docs/brand.md`.

## Why

The earlier two-door homepage (wayintoai-89x, wayintoai-yig) split visitors between Use AI and Understand AI and put the email ask last. The site's identity was unclear (tutorial vs on-ramp vs sensemaking) and the thing we most want visitors to do, subscribe, was the least visible.

## Approach

1. Define the narrative and offer first (see brand doc), then design around the offer.
2. Mood board of seven references (Flowershow Monospace, Simon Willison, One Useful Thing, The Browser, Stratechery, Gwern, Maggie Appleton) and three directions: A pure Monospace, B "blue pencil" (Monospace structure plus serif voice plus one blue accent), C dark terminal. Chose **B**.
3. Ship the homepage first, email-first: promise, signup form and "in each issue" on the first screen; recently selected posts; the two routes; why this exists.
4. Roll the same system out to every page (posts, refs, logs, route pages) via `custom.css` on top of the current theme.
5. The weekly email routine is a separate epic (wayintoai-94n).

## Status

- Brief published; direction B agreed by Rufus.
- Homepage shipped (wayintoai-bnd.2).
- Site-wide rollout: wayintoai-cmw.
- Open: name sign-off (bnd.3), stale social share image (bnd.4), point the signup form at the new list system once the list moves off Substack (wayintoai-b7z).
