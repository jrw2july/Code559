# Code559 blog — style guide and post template

Source of truth: `code559-course-braindump-v2.md` (§2 template, §3A sequence, §3B gaps, §4 method, §6A credit line). This guide adapts the lesson packet for the blog: the free funnel. **The Exercise is published. The Project is held back** (a teaser only; the full brief, steps and finishing work are in the paid packet).

## File layout

- `blog/index.md` — landing page (module table, links).
- `blog/module-NN-slug.md` — one post per module, 0–13.
- `blog/images/mNN-name.png` — images for that module. Every image is referenced with a relative path `images/...`.

## Post structure (exact order)

```
---
title: "Module N: Title"
subtitle: "One line"
module: N
series: Code559 Front-End Developer Course
estimated_time: "about 90 minutes (estimate)"
---

# Module N — Title
*One-line subtitle.*

**Time:** about N minutes (estimate)

<!-- about:start --> collapsed <details> "About this module" (every module): What this module covers, Tips for the learner, The four badges <!-- about:end -->

<!-- contents:start --> **Contents**: a link to every ## section, with the Core concepts ### questions nested under it <!-- contents:end -->

**In this module you will learn:** bullet list (every concept introduced).

## Why this matters
2–3 short paragraphs.

## Before you start
Numbered steps; nothing installs inside the body. Ends with a **Checkpoint** block (blockquote).

## Core concepts
Each concept is a numbered `###` question, answered in short paragraphs that follow the IEIA stages: Introduce → Explain → Illustrate (snippet, image, or diagram with caption) → Apply (a one-line "try it" the reader does right now). There are no text labels; each stage paragraph starts with its badge (see "Badges and dividers" below).

## Exercise
Its own practice folder (`practice-NN`), numbered steps, "Type it, do not paste it," one deliberate break-it step. First line: *Your hands, about N minutes (estimate).*

## Project (in the full packet)
Teaser only: one paragraph describing the finished thing and what the visitor can do, plus the sentence:
"The full brief, the step-by-step build, and the finishing work in Git are in the Module N packet. [Get the packet →](https://code559.gumroad.com/l/module-NN-slug)" (the product address is the post's file name without `.md`; decided 2026-10-12)

## Common misconception
> *"quoted wrong belief"*
What would you say? Hint.

## Summary
One paragraph, one sentence per concept.

## Check your understanding
Three questions; one is a standing question (rotate: Why does it work? / What value does this variable hold? / What happens if this changes? / What causes this function to run? / What would you test?).

## Before next module
- [ ] checkboxes

## Go further
Real resources only: MDN (search term or page title), GitHub Docs article titles, and freeCodeCamp. Modules 5–11 use the standard freeCodeCamp line (see "Standard wording"). No affiliate links for now (decided 2026-10-12; the W3Schools slots were removed until a program is chosen). Never invent video titles or runtimes.

## What to keep
What the reader should have at the end, plus "Which step would be hardest to repeat without this post, and why?"

---
*Code559 is a 559 Solutions project. Portions adapted from Visual Studio Code documentation (CC BY 3.0 US), GitHub Docs (CC BY 4.0), and GitHub Skills (MIT). Screenshots used with permission from Microsoft.*
```

## About block and Contents (decided 2026-10-12)

- Both blocks are generated, never edited by hand: `about_toc.py` (kept outside this repository, with the image scripts) inserts them under the **Time:** line between the marker comments, and rerunning it refreshes them. Run it again after adding, renaming or reordering any `##` or `###` heading.
- **What this module covers** (one per module, approved by the owner): the scope of the module, then why it matters, with the "why" chosen to fit that module (foundational, saves you hours, essential, and so on). The badge legend is the same in every module. The tips are the same in Modules 1–13; Module 0 has its own version (decided 2026-10-12), written for a module that is mostly installing.
- Contents links use GitHub-style heading ids (lowercase, punctuation dropped, spaces to hyphens). The static page build must give headings the same ids.
- The paid packets build an "About this module" page right after the cover from the same block, then a Contents page with page numbers and links (every module, Module 0 included).

## Style rules (from the braindump)

- Plain, direct, adult, a little informal. Short sentences. One idea per sentence. 6th–10th grade readability. No opening fluff. No profanity.
- Second person. "After this module you can…"
- Prose in paragraphs, not one sentence per line.
- Generic snippets the reader adapts (`"image-one.jpg"`, "a folder you choose, short name, no spaces"). Never the pilot student's name, email, username, site, drive letter or folder names.
- Windows 11 and Edge or Chrome assumed. VS Code with AI features off (Module 0).
- One new concept per layer per module. Do not introduce higher-order functions, recursion, modules or frameworks. Explain anything new the first time it is used, even in a code sample.
- Avoid the "test scores" theme in examples.
- Never use the words "genuinely", "honestly" or "straightforward".
- **"Out loud" is only for explaining code to yourself** ("explain each line to yourself, out loud"). Other prompts vary the action: write it down, sketch it on paper, point at it, or "Think this through:" followed by a question. The first "out loud" prompt in a post (not counting the tips in the About block) carries the footnote marker `[^recite]`, and the post ends with the standard footnote (see "Standard wording"). Later uses in the same post have no marker.
- Modules 2–11 end with the standard Git checklist line in "Before next module" (see "Standard wording"); full Git is Module 12.

## Course decisions (owner, 2026-10-11)

1. **Free path.** Module 1 ends with free readers publishing a first page of `my-site` to GitHub Pages. From Module 2 on, each Exercise uses its own practice folder; building out `my-site` is the paid packet's Project. Text for free readers must not assume `my-site` has more than that first page.
2. **Viewing pages.** Learners open pages directly in Edge or Chrome and press **F5** after each save. **F12** (or **Ctrl+Shift+J**) opens DevTools. Live Preview is optional and explained only in Module 0. Never send a learner to the Console from Live Preview, and never rely on a local server address.
3. **Names, everywhere.**
   - Stylesheet: `styles.css`.
   - Practice folders: `practice-NN` inside the course folder (`practice-01` … `practice-13`). Sub-folders are fine (`practice-13\goal-counter`).
   - The Module 4 card is the **rating card**. Its HTML and CSS are Module 4; its JavaScript is Module 10.
   - The personal site folder and repository: `my-site`. Live address: `https://your-username.github.io/my-site/`.
   - The course folder in examples: `C:\Users\you\Documents\code559`.
4. **Reader notes, not flags.** Nothing unverified is published. A claim is either checked and stated plainly with its source, or written as a plain reader note that says what to expect or do (for example *"Your screen may look slightly different; the button names are what matter."*). No bracketed "[unverified]" notes.

## Standard wording (use exactly, adapting only the bracketed part)

- **Opening a page and the Console** (first time per module where needed): "Open `[file]` in Edge or Chrome (double-click it in File Explorer, or drag it onto a browser window). After each save, press **F5** to reload. Press **F12** (or **Ctrl+Shift+J**) to open DevTools, then click the **Console** tab." When there is no file to open, use "Open Edge or Chrome." and the last sentence. When nothing is saved in the module, the F5 sentence may be left out.
- **Git checklist line, Modules 2–11** ("Before next module"):
  `- [ ] If you did this module's packet project in my-site, saved it with the routine: git status → git add . → git commit -m "…" → git push → check the live page. (Your practice folder is not saved to GitHub.)`
- **DOM code typed before Module 9** (Modules 3–4): introduce each Console line with "Type this line exactly as shown. You will learn how it works in Module 9; for now, read the answer it gives."
- **Code shown only in a Console picture:** put the exact lines in a `js` block above the picture, starting with "Typed into the Console for the picture below, in this order:". A Console picture that only shows how a result was checked, and that the reader is not meant to repeat, needs no block; its caption says "You do not need to type…".
- **"Out loud" footnote** (last line of the post, after "Sources checked"; add the dated source entry to that line):
  `[^recite]: **Why out loud?** Most people have recited something to learn it by heart: a phone number, a poem, lines for a play. Words you say aloud stick better than words you read silently; memory researchers call this the production effect (Ozubko and MacLeod, 2010). Explaining code to yourself out loud uses the same idea. It also shows you the line you cannot explain yet, and that line is the one to study next.`
- **freeCodeCamp line, Modules 5–11** (Go further): `- freeCodeCamp: the free [JavaScript Certification](https://www.freecodecamp.org/learn/javascript-v9/) (checked YYYY-MM-DD) has practice on this topic.` No module names.

## Accessibility standard

- Focus rings and other interface outlines: **`#b45309`** (dark orange, 5.0:1 on white). MDN *Color contrast* asks for at least 3:1 for interface parts.
- On a dark background the ring must change: the navy bar `#1d3557` gets **`#fdba74`** (light orange, 7.3:1 on that navy), set with `outline-color`. Check every ring against what is behind it.
- Body text meets 4.5:1. Alt text and captions name the ring color in words ("dark orange ring", "light orange ring").

## Honesty rules (non-negotiable)

- Every command and every output shown was run for real in the build environment. Terminal images are rendered from real captured output.
- **Image captions say what the reader should notice, and real images say they are real.** Three kinds of image:
  - **Real** (a page captured by Chromium, or terminal/Console text from a real run drawn into a frame). The caption ends with a tag such as `(real: rendered in Chromium at 600 px)` or `(real output, rendered)`. When the run happened in another folder or on Linux, use exactly: `(real output, rendered; captured on Linux, with the folder path changed to the course folder)`. Only the folder path may be changed; every other character is real. Git paths in Git's own messages use forward slashes (`C:/Users/you/…`), as Git for Windows prints them; prompts use backslashes. Capture Git through a pseudo-terminal so `git log` shows its labels (`(HEAD -> main)`) as a real terminal does.
  - **Drawn screen copies** (VS Code, GitHub.com, GitHub Desktop, DevTools, File Explorer). The yellow ILLUSTRATION tag is drawn into the image. The caption has no tag.
  - **Diagrams.** No ILLUSTRATION tag and no caption tag.
- No image or text ever shows a build path (`/home/...`, `/tmp/...`) or a real person's name, username or folder.
- Numbers are measured, not estimated, and say so; time estimates say "(estimate)".
- Nothing unverified is published (see decision 4).
- Sources named by page title (MDN page titles, GitHub Docs article titles, git-scm.com docs, GitHub CLI manual). Each post ends with a "Sources checked" line; add a dated entry when you check new pages.

## Badges and dividers

- Each Core concept paragraph starts with its stage badge, an inline image:
  `<img src="images/brand/marker-introduce.svg" alt="Introduce" width="24" height="24" style="vertical-align:-0.35em;"> ` (also `marker-explain.svg`, `marker-illustrate.svg`, `marker-apply.svg`, with matching alt text). Plain notes have no badge.
- A floor-plan divider (wall, window, wall, door) sits on its own line before each Illustrate picture, and before the "Typed into the Console…" block when the picture has one. The Illustrate badge then goes at the start of the caption under the picture:
  `<div role="separator" style="display:flex;align-items:flex-end;margin:1.5em 0;"><img src="images/brand/divider-wall.svg" alt="" style="flex:1;min-width:0;height:34px;"><img src="images/brand/divider-window.svg" alt="" style="width:70px;height:34px;"><img src="images/brand/divider-wall.svg" alt="" style="flex:3;min-width:0;height:34px;"><img src="images/brand/divider-door.svg" alt="" style="width:46px;height:34px;"></div>`
- Badge and divider files are in `images/brand/` (icons from Lucide; see `LICENSE-lucide.txt`).

## Image helpers

The image build scripts are kept outside this repository. `build/imgkit.py` provides:
- `render_page(html_path, out_png, width, height=None, full_page=True, actions=None)` — real Chromium render of a lesson page. `actions` is a list of (kind, arg) such as ("click", "#faq-1"), ("press", "Tab"), ("fill", ("#name","Ada")).
- `render_terminal(cmd_blocks, out_png, title="Windows Terminal — PowerShell")` — draws a light-theme terminal frame; `cmd_blocks` is a list of (prompt, command, output). **Output must come from a real run** (use `run(cmd, cwd)` which executes and returns stdout+stderr).
- `render_console(entries, out_png)` — DevTools-Console-styled frame; entries are (kind, text) with kind in `log|error|result|input`. Values must come from a real run (`node_eval(js)` or `browser_eval(html, js)` return real results).
- `render_svg(svg_text, out_png, width)` — rasterizes a drawn illustration or diagram.
- `browser_frame(html_path, out_png, url_text, width)` — real page render inside a drawn browser chrome (address bar). Caption as `(page real: rendered in Chromium; browser frame drawn)`. Its frame cannot load `file://` pages; for a page opened from disk, render the real page and draw the frame around it in a separate step.
- Never re-run an old module build script over the images folder: the scripts may hold older names and colors than the posts. Copy a script, render only the image you need, look at it, then copy that one image in.
