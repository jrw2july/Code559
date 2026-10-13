"""Insert (or refresh) the collapsed "About this module" block (Modules 1-13) and the Contents list (all modules) under each post's Time line.
Idempotent: the inserted parts sit between <!-- about:start/end --> and <!-- contents:start/end --> markers.
Usage (from the Code559 folder):  python tools/about_toc.py            (or pass a blog folder path)
Needs: pip install markdown-it-py
Run it after any change to a post's headings, or to the summaries and tips below. Never hand-edit between the markers."""
import re, glob, os, sys
from markdown_it import MarkdownIt

BLOG = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "blog")

SUMMARIES = {
0: "You set up file extensions, VS Code (with its AI features off), Git, the GitHub CLI and Node.js, and prove each one works with a single command. It's what keeps the rest of the course moving: every later module assumes these tools are ready, so no lesson ever stops for an install.",
1: "You learn how the web delivers a page, how to write HTML by hand, how to link pages together, and how to publish your first page on GitHub Pages. This is foundational: every website, framework and page builder ends up as an HTML file a browser reads. You also finish the first week with something live on the web.",
2: "You learn to link a stylesheet, write rules for color, type and spacing, predict which rule wins, and build a navigation bar with Flexbox. It saves you hours: when a rule \"does nothing,\" the cause is almost always one of the three problems this module teaches on purpose.",
3: "You learn the box model, mobile-first media queries, CSS Grid and responsive images, and how to test a page at different widths. It's essential because more visitors will see your site on a phone than on a laptop, and one HTML file with one stylesheet can serve them all.",
4: "You learn to build forms with real controls, labels and radio groups, and to test them with the keyboard and style their states. It matters to every visitor: a missing label or name can leave a screen reader user guessing, or lose what a visitor typed. The browser already gives you most of the fix if you use the right elements.",
5: "You learn what a program is, where JavaScript runs, how to see a value and how to read an error message. You also start the Predict → Run → Modify → Create → Debug habit. It's the habit every later module depends on: run it, change it, break it, and read what the computer tells you.",
6: "You learn values and types, `const` and `let`, operators, comparisons, and `if`/`else`. These are the moves behind every interactive feature: store a value, compare it, decide. They are also where most early bugs come from, so you cause each one on purpose to learn to recognize it.",
7: "You learn to define, call, test and return values from functions, including how to write one from a one-sentence description. It's how working developers check their code: a function that hands back a value can be tested with made-up inputs before any web page exists.",
8: "You learn to keep lists in arrays, visit every item with a loop, and give each item named facts with objects. It's the toolkit for any page built from data: twenty projects or milestones don't fit in twenty separate variables.",
9: "You learn to find elements on a page, change them, and react to clicks and keys, organizing every script in the same three blocks. This is where everything you've learned becomes visible: the language from Modules 5–8 finally changes what a visitor sees.",
10: "You learn to catch a form before it sends, check what was typed, show accessible error messages, and confirm success. It's a kindness to your visitors: a clear message in the right place saves them from guessing. You'll also learn why these checks are about the visitor's experience, not security.",
11: "You learn to read errors, track down bugs with the Console, test with the keyboard, and write Action / Expected / Actual test plans. It turns fixing into a method, not luck: guess-and-edit stops working once a page has real JavaScript, and a written test can be checked again after every change.",
12: "You learn what your save routine actually does: staging, diffs, history, branches, merges, and Issues and pull requests connected with `Closes #1`. You also learn to tag a v1.0 release. It's what employers look for: a history of small, clear commits and merged pull requests shows you work the way a team does.",
13: "You learn to turn a written requirement into tasks, and to finish each feature with the nine-step completion standard. Then you check the whole site and audit your portfolio. It's the skill real work asks for: building from a short list with no step-by-step guide, and knowing when you are actually done.",
}

TIPS = """**Tips for the learner**

Some prompts ask you to explain code to yourself, out loud. Others ask you to write something down. Each habit does a different job.

**Recite to understand.** When a prompt says "out loud," explain the code in your own words, as if you were teaching it. Saying it aloud makes a deeper impression than reading silently. It helps you picture how the pieces of code fit together. And it shows you right away which line you cannot explain yet. That line is the one to review.

**Write it down to check yourself.** When a prompt says "write down," it is usually a prediction, a choice, or a guess about a bug. A written answer can't change after you see the result, so the comparison is fair and you learn from the difference. Writing also keeps your attention on the lesson and helps you pick out the main points.

**Keep one notebook for this course.** Use it for your predictions, key terms, steps, mistakes, and questions to come back to. Date each entry and write the module number, so you can find it later. Before you start a new module, read your last few entries and recite one or two of them out loud."""

TIPS_M0 = """**Tips for the learner**

This module is mostly installing, so its prompts ask you to write things down. In later modules, some prompts will also ask you to explain code to yourself, out loud. Each habit does a different job.

**Write it down to check yourself.** Here that means your answers in Concept 1, and what each version command prints. A written answer can't change after you see the result, so the comparison is fair and you learn from the difference. If a tool stops working in a later module, your notes show what was working before.

**Recite to understand.** From the later modules on, when a prompt says "out loud," explain the code in your own words, as if you were teaching it. Saying it aloud makes a deeper impression than reading silently, and it shows you right away which line you cannot explain yet.

**Start one notebook for this course, today.** Use it for your predictions, key terms, steps, mistakes, and questions to come back to. Date each entry and write the module number. Your first entries come from this module: the four version numbers (Git, GitHub CLI, Node, npm) and the folder path of `my-site`."""

BADGE = '<img src="images/brand/marker-{n}.svg" alt="" width="24" height="24" style="vertical-align:-0.35em;">'
LEGEND = f"""**The four badges**

Every core concept moves through the same four steps, called IEIA. Each step is marked with its badge.

{BADGE.format(n="introduce")} - **Introduce** (a lightbulb: a new idea) - You meet the concept: its name, and why it matters to you, in a sentence or two.

{BADGE.format(n="explain")} - **Explain** (a speech bubble: the idea in words) - How it works, one idea at a time, in plain words.

{BADGE.format(n="illustrate")} - **Illustrate** (an eye: see it) - A small example you can look at: a code snippet, a real screenshot or a diagram. Its caption, which starts with this badge, tells you what to notice.

{BADGE.format(n="apply")} - **Apply** (a keyboard: your turn) - A short task to do right now, before you read on. Often you type or predict something; sometimes you write it down, sketch it, or explain code to yourself out loud."""

def about_block(n):
    return ("<!-- about:start -->\n<details>\n<summary><strong>About this module</strong></summary>\n\n"
            f"**What this module covers**\n\n{SUMMARIES[n]}\n\n{TIPS_M0 if n == 0 else TIPS}\n\n{LEGEND}\n\n</details>\n<!-- about:end -->")

def gh_slug(text):
    """GitHub-style heading id: lowercase, drop punctuation (keep letters, digits, _, -, spaces), spaces to hyphens."""
    s = text.strip().lower()
    s = re.sub(r"[^\w\- ]", "", s)
    return s.replace(" ", "-")

def headings(src):
    md = MarkdownIt("commonmark", {"html": True}).enable("table")
    src = re.sub(r"\A---\n.*?\n---\n", "", src, flags=re.S)
    toks = md.parse(src)
    out, seen = [], {}
    for i, t in enumerate(toks):
        if t.type != "heading_open":
            continue
        inline = toks[i + 1]
        plain = "".join(c.content for c in inline.children if c.type in ("text", "code_inline"))
        base = gh_slug(plain); k = seen.get(base, 0); seen[base] = k + 1
        out.append((t.tag, inline.content, base if k == 0 else f"{base}-{k}"))
    return out

def contents_block(src):
    lines, in_core = ["<!-- contents:start -->", "", "**Contents**", ""], False
    for tag, text, slug in headings(src):
        if tag == "h2":
            in_core = text == "Core concepts"
            lines.append(f"- [{text}](#{slug})")
        elif tag == "h3" and in_core:
            lines.append(f"  - [{text}](#{slug})")
    lines += ["", "<!-- contents:end -->"]
    return "\n".join(lines)

def process(path):
    raw = open(path, "rb").read()
    crlf = b"\r\n" in raw                      # keep the file's own line endings (Windows checkouts use CRLF)
    s = raw.decode("utf-8").replace("\r\n", "\n")
    n = int(re.search(r"^module:\s*(\d+)", s, re.M).group(1))
    s = re.sub(r"\n*<!-- about:start -->.*?<!-- about:end -->\n*", "\n\n", s, flags=re.S)
    s = re.sub(r"\n*<!-- contents:start -->.*?<!-- contents:end -->\n*", "\n\n", s, flags=re.S)
    m = re.search(r"^\*\*Time:\*\*[^\n]*\n", s, re.M)
    assert m, path
    head, rest = s[:m.end()], s[m.end():].lstrip("\n")
    parts = [about_block(n), contents_block(s)]
    s = head + "\n" + "\n\n".join(parts) + "\n\n" + rest
    if crlf:
        s = s.replace("\n", "\r\n")
    open(path, "w", encoding="utf-8", newline="").write(s)
    return n

if __name__ == "__main__":
    for f in sorted(glob.glob(os.path.join(BLOG, "module-*.md"))):
        print(process(f), os.path.basename(f))
