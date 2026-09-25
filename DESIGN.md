# Design: Way Into AI

Brief and mood board: https://claude.ai/artifact/DLpmX593GvBX214vHLxCb9 (bead wayintoai-bnd).

The homepage is email-first. Its job is to sell one thing: the free weekly email, "what mattered in AI this week, and what to do about it". The first screen holds the promise, the signup form and what each issue contains; recent selected posts and the two routes (**Use AI**, **Understand AI**) sit below as ways into the archive.

Visual direction "blue pencil": built on top of the Flowershow Monospace theme. IBM Plex Mono carries structure (navigation, labels, lists, literal `##` heading markers); Newsreader serif carries the voice (headlines, titles, prose). Near-monochrome paper (`#fbfbf9`) and ink (`#1b1b1d`), hairline rules, no cards or shadows. One accent, editor's blue (`#2140c4`), marks selection: `[x]` ticks, heading markers, links, the emphasised half of the headline.

`index.md` uses Flowershow Markdown mode with standard HTML only; `custom.css` owns layout under the `.wai` scope. The signup form posts to the Substack subscribe page until the list moves (wayintoai-b7z). Carrying the same tokens to posts, refs and logs is the next slice (wayintoai-cmw). Avoid invented proof points, generic AI imagery and competing calls to action.
