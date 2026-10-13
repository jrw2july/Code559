# Instructions for coding agents (Code559)

The free lessons of the Code559 Front-End Developer Course: `blog/index.md` plus 14 module posts (`blog/module-00-*.md` to `blog/module-13-*.md`) and their pictures in `blog/images/`. The website (559solutions.com) and the paid packets are both built from these files.

## Owner rules (always)

- Do not commit, push, tag, open pull requests, or deploy. The owner reviews the diff and does those himself.
- Do not run `gh auth`, and do not read or print credentials or tokens.
- Keep each change to the task you were given.

## Writing rules

Follow `blog/STYLE-GUIDE.md` exactly. Its key points:

- Reading level grade 6 to 10: short sentences, second person, plain words. No profanity.
- Banned words: genuinely, honestly, straightforward.
- "Out loud" is used only for explaining code to yourself. The first one in each module carries the `[^recite]` footnote.
- Every core concept follows the IEIA badges (Introduce, Explain, Illustrate, Apply).
- Nothing unverified is published. Check each fact against a named source (MDN, GitHub Docs, git-scm.com) and add it, dated, to the post's "Sources checked" line.
- Pictures: real captures or renders, or drawn copies with a visible ILLUSTRATION label. Alt text on every picture. Never show a build path, a real student's name, or personal details.
- The "## Project (in the full packet)" section of each post is a public promise of what the paid packet contains. Do not change it without telling the owner, because the packet must still match it.

## Generated blocks: do not hand-edit

Text between `<!-- about:start -->` / `<!-- about:end -->` and `<!-- contents:start -->` / `<!-- contents:end -->` is generated. After any change to a post's headings, or to the summaries or tips, run:

```
pip install markdown-it-py
python tools/about_toc.py
```

It is safe to run more than once, and it keeps each file's line endings.

## After a lesson changes

1. Update the website copy: in `../559solutions.com`, run `pnpm sync:code559` then `pnpm validate`.
2. Tell the owner which modules changed. Their paid packets (PDF and EPUB) need a rebuild from the private packets folder (`../Code559-packets`, see its README). Do not put packet content in this repository; it is the paid product.
