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

**In this module you will learn:** bullet list (every concept introduced).

## Why this matters
2–3 short paragraphs.

## Before you start
Numbered steps; nothing installs inside the body. Ends with a **Checkpoint** block (blockquote).

## Core concepts
Each concept is a numbered bold question, answered in one or two short paragraphs, labeled with the IEIA stage in italics:
  *Introduce* → *Explain* → *Illustrate* (snippet, image, or diagram with caption) → *Apply* (a one-line "try it" the reader does right now).

## Exercise
Isolated, throwaway folder, numbered steps, "Type it, do not paste it," one deliberate break-it step. Labeled *Apply — your hands, about N minutes (estimate)*.

## Project (in the full packet)
Teaser only: one paragraph describing the finished thing and what the visitor can do, plus the sentence:
"The full brief, the step-by-step build, and the finishing work in Git are in the Module N packet. [Get the packet →](PACKET_LINK_MODULE_N)"

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
Real resources only: MDN (search term or page title), GitHub Docs article titles, matching freeCodeCamp module. Affiliate slots as plain placeholders: `[W3Schools HTML Tutorial](AFFILIATE_W3SCHOOLS)` with the line "*Affiliate link: Code559 may earn a commission at no extra cost to you.*" Never invent video titles or runtimes.

## What to keep
What the reader should have at the end, plus "Which step would be hardest to repeat without this post, and why?"

---
*Code559 is a 559 Solutions project. Portions adapted from Visual Studio Code documentation (CC BY 3.0 US), GitHub Docs (CC BY 4.0), and GitHub Skills (MIT). Screenshots used with permission from Microsoft.*
```

## Style rules (from the braindump)

- Plain, direct, adult, a little informal. Short sentences. One idea per sentence. 6th–10th grade readability. No opening fluff. No profanity.
- Second person. "After this module you can…"
- Prose in paragraphs, not one sentence per line.
- Generic snippets the reader adapts (`"image-one.jpg"`, "a folder you choose, short name, no spaces"). Never the pilot student's name, email, username, site, drive letter or folder names.
- Windows 11 and Edge or Chrome assumed. VS Code with AI features off (Module 0).
- One new concept per layer per module. Do not introduce higher-order functions, recursion, modules or frameworks.
- Avoid the "test scores" theme in examples.
- Modules 2–11 end with the simple Git routine (status → add → commit → push → verify) as a reminder line in "Before next module"; full Git is Module 12.

## Honesty rules (non-negotiable)

- Every command and every output shown was run for real in the build environment. Terminal images are rendered from real captured output.
- **Image captions say what the reader should notice AND whether the image is real or drawn.** Use exactly one of these tags at the end of every caption:
  - `(real: rendered in Chromium)` — a lesson page captured by Chromium.
  - `(real output, rendered)` — terminal or console text captured from a real run, drawn into a terminal-styled frame. If captured on Linux, say so and say what differs on Windows.
  - `(illustration, not a screenshot)` — a drawn facsimile of VS Code, GitHub.com, Windows, DevTools, or a diagram.
- Numbers are measured, not estimated, and say so; time estimates say "(estimate)".
- Anything not verified is flagged inline: **[unverified: …]**.
- Sources named by page title (MDN page titles, GitHub Docs article titles, git-scm.com docs, GitHub CLI manual).

## Image helpers

`build/imgkit.py` provides:
- `render_page(html_path, out_png, width, height=None, full_page=True, actions=None)` — real Chromium render of a lesson page. `actions` is a list of (kind, arg) such as ("click", "#faq-1"), ("press", "Tab"), ("fill", ("#name","Ada")).
- `render_terminal(cmd_blocks, out_png, title="Windows Terminal — PowerShell")` — draws a light-theme terminal frame; `cmd_blocks` is a list of (prompt, command, output). **Output must come from a real run** (use `run(cmd, cwd)` which executes and returns stdout+stderr).
- `render_console(entries, out_png)` — DevTools-Console-styled frame; entries are (kind, text) with kind in `log|error|result|input`. Values must come from a real run (`node_eval(js)` or `browser_eval(html, js)` return real results).
- `render_svg(svg_text, out_png, width)` — rasterizes a drawn illustration or diagram.
- `browser_frame(html_path, out_png, url_text, width)` — real page render inside a drawn browser chrome (address bar). Caption as `(page real: rendered in Chromium; browser frame drawn)`.
