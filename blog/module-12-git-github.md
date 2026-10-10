---
title: "Module 12: Git, GitHub and Publishing"
subtitle: "Move from a memorized routine to a workflow you understand: diff, branches, merges, Issues, pull requests and releases."
module: 12
series: Code559 Front-End Developer Course
estimated_time: "about 2–3 hours (estimate)"
---

# Module 12 — Git, GitHub and Publishing

*Move from a memorized routine to a workflow you understand: diff, branches, merges, Issues, pull requests and releases.*

**In this module you will learn:**

- The Git mental model: working folder → staging area → commits → remote
- How to read `git status` and `git status --short`
- What `git add` and `git commit -m` really do, and why you make one change per commit
- How to check your work with `git diff`, `git diff --staged` and `git diff --stat` before every commit
- How to read history with `git log --oneline`
- How to make a branch with `git switch -c`, prove it is separate, merge it with `git merge` and delete it with `git branch -d`
- The checkout family: `git switch`, `git restore`, and `git checkout` as the older all-in-one
- How a `.gitignore` file keeps files out of Git, and how `git status` proves it
- How to write a `README.md` with four standard headings
- How the VS Code Source Control view does the same jobs as the terminal
- How GitHub Issues and pull requests connect through `Closes #1`, and how to leave line comments on your own pull request
- How to mark a version with `git tag v1.0`, and how a GitHub release is built on that tag
- What GitHub Desktop is (awareness only)
- What the `dubious ownership` message means and how to fix it

## Why this matters

Since Module 1 you have saved your site with five steps: `git status`, `git add .`, `git commit -m "…"`, `git push`, then a check of the live page. That routine works. But it treats Git like a black box. You type the words and hope.

This module opens the box. You will see where your changes sit at each step, check them before they become history, and try a new page on a branch without risking the working site. Then you will use the GitHub tools that teams use every day: an Issue that names the work, a pull request that proposes it, and a release that marks a finished version.

Employers read your GitHub profile. A history of small, clear commits, merged pull requests and a tagged v1.0 says "this person works the way we do." That is the goal of this module.

## Before you start

1. Your `my-site` folder from earlier modules is on GitHub, and the live page loads.
2. In VS Code, open a terminal. Type `git --version` and `gh auth status`. Both should answer without an error (you set them up in Module 0).
3. Decide on one short practice folder name for this module's Exercise, for example `git-practice`, inside your `code559` folder. **Not** inside `my-site`.

> **Checkpoint.** `git --version` prints a version, `gh auth status` says you are logged in, and you know where your practice folder will go.

A note on the pictures. Every terminal image in this post comes from a real run of Git 2.43.0 in a throwaway project on Linux, drawn in a Windows Terminal frame. The commit IDs (like `f7464f5`) are real for that run; yours will be different, because a commit ID depends on the time and the author too. GitHub.com, VS Code and GitHub Desktop pictures are drawings, because nothing in this post was pushed to GitHub.

## Core concepts

### 1. Where does your work live in Git?

*Introduce.* Git keeps your project in four places. Most confusion about Git comes from not knowing which place a change is in.

*Explain.* The **working folder** is the files you see and edit. The **staging area** is a list of changes you have chosen for the next commit. **Commits** are saved snapshots, stored in the hidden `.git` folder on your computer. The **remote** is the copy on GitHub. `git add` moves a change from the folder to staging. `git commit` turns staging into a snapshot. `git push` sends your commits to GitHub. Nothing reaches GitHub until you push.

*Illustrate.*

![Four boxes left to right: Working folder, Staging area, Commits, Remote (GitHub), joined by arrows labeled git add, git commit, git push. Brackets underneath show what git diff and git diff --staged compare.](images/m12-mental-model.png)
*Each arrow is one command. `git diff` compares the folder with staging; `git diff --staged` compares staging with the last commit. (illustration, not a screenshot)*

*Apply.* Say out loud which box a file is in right after you save it in VS Code. (Answer: only the working folder.)

### 2. What is `git status` telling you?

*Introduce.* `git status` is the question "where is everything right now?" Run it before and after every other Git command.

*Explain.* In a brand-new project, Git lists your files as **untracked**: it sees them, but it is not keeping their history yet. `git status --short` gives the same facts in one line per file. The two characters at the start are two columns. The **left** column is the staging area; the **right** column is the working folder. `??` means untracked. `A` on the left means added to staging. `M` means modified: on the left it is staged, on the right it is not staged yet.

*Illustrate.*

![A terminal running git init, then git status listing index.html and style.css as untracked, then git status --short showing two lines beginning with question marks.](images/m12-init-status.png)
*The long form explains; the short form is faster once you can read it. `??` means "untracked." (real output, rendered; captured on Linux with Git 2.43.0. On Windows the `git init` line shows your own folder path.)*

*Apply.* In your `my-site` folder, run `git status --short` now. An empty answer means nothing has changed since your last commit.

### 3. What do `git add` and `git commit` actually do?

*Introduce.* `git add` chooses. `git commit` saves. They are separate so that you decide exactly what goes into each snapshot.

*Explain.* You have used `git add .`, which stages everything. Naming one file, `git add index.html`, stages only that file. Then `git commit -m "message"` saves what is staged, and only that. This lets you follow the most useful habit in Git: **one change per commit**. A good message finishes the sentence "This commit will…": *Add home page structure*, *Add base styles*. Short, starts with a verb, says what changed. "stuff" and "fixes" tell your future self nothing.

*Illustrate.*

![A terminal: git add index.html, git status --short showing A index.html and ?? style.css, a commit, then git add style.css and a second commit, then git status saying working tree clean.](images/m12-add-commit.png)
*After `git add index.html`, only that file has an `A`. Two files, two commits, two clear messages. "working tree clean" means the folder matches the last commit. (real output, rendered; captured on Linux with Git 2.43.0)*

*Apply.* Look at your own `my-site` history with `git log --oneline` (Concept 5). Find one message that does not finish "This commit will…". You will write better ones from now on.

### 4. How do you check your work before you commit?

*Introduce.* `git diff` shows exactly which lines changed. Reading it before every commit is how you catch a stray edit before it becomes history.

*Explain.* `git diff --stat` gives a summary: which files changed and how many lines. `git diff` shows the lines. A line starting with `+` was added; `-` was removed; the lines with no sign are context so you can find your place. Once you stage a file, plain `git diff` stops showing it, because it compares the folder with staging. To see what you are about to commit, use `git diff --staged`.

In the story below, two different changes are waiting: a new tagline in `index.html` and a darker heading color in `style.css`. That is two changes, so it should be two commits.

*Illustrate.*

![A terminal: git diff --stat showing two files changed, then git diff showing a plus line adding a paragraph to index.html and a minus and plus pair changing a color in style.css.](images/m12-diff.png)
*`--stat` first for the big picture, then the full diff. The color change shows as one `-` line and one `+` line. (real output, rendered; captured on Linux with Git 2.43.0)*

![A terminal: git add index.html, git diff --staged showing only the tagline change, then two commits, one per file.](images/m12-diff-staged.png)
*`git diff --staged` shows only what the next commit will contain, so each commit holds one change. (real output, rendered; captured on Linux with Git 2.43.0)*

*Apply.* Before your next commit on `my-site`, run `git diff --staged` and read every `+` and `-` line. If a line surprises you, do not commit yet.

### 5. How do you read history, and what is a branch?

*Introduce.* `git log --oneline` lists your commits, newest first, one line each. A **branch** is a separate line of commits, so you can try something without touching `main`.

*Explain.* `git switch -c add-about-page` creates a branch and moves you onto it. Commits you make there belong to that branch only. To prove it, list the files Git is tracking with `git ls-files`, switch back with `git switch main`, and list them again. The new page is gone from `main`; it is safe on its branch. `git branch` lists your branches and puts a `*` beside the one you are on. The git-scm.com manual describes `-c` as "Create a new branch named *<new-branch>* … before switching to the branch" (*git-switch*).

*Illustrate.*

![A terminal: git log --oneline with four commits, git switch -c add-about-page, a commit adding about.html, git ls-files listing three files, git switch main, git ls-files listing two files, git branch showing two branches with a star on main.](images/m12-branch.png)
*On the branch, `about.html` exists. Back on `main`, it does not. Same folder, different branch, different files. (real output, rendered; captured on Linux with Git 2.43.0)*

*Apply.* Predict: if you open the folder in File Explorer while on `main`, will you see `about.html`? (No. Git removes it from the folder when you switch, and puts it back when you switch to the branch.)

### 6. How does a merge bring the branch back?

*Introduce.* When the branch is ready, you stand on `main` and run `git merge` with the branch name.

*Explain.* If `main` has not changed since you made the branch, Git does not need a new commit. It simply moves `main` forward to the branch's last commit. The manual calls this a **fast-forward**: "only update the branch pointer to match the merged branch; do not create a merge commit" (*git-merge*). After the merge, the branch has done its job; `git branch -d` deletes the name. Your commits stay. Git refuses to delete a branch whose work is not merged yet; in a test it printed "error: the branch 'y' is not fully merged."

*Illustrate.*

![A terminal: git merge add-about-page printing Updating, Fast-forward and about.html 12 plus signs, then git ls-files now listing about.html on main, git log --oneline with five commits, and git branch -d deleting the branch.](images/m12-merge.png)
*"Fast-forward" means `main` just moved ahead; the log shows no extra merge commit. (real output, rendered; captured on Linux with Git 2.43.0)*

*Apply.* Explain in one sentence why the log after the merge has exactly five lines, not six.

### 7. What are `switch`, `restore` and `checkout`?

*Introduce.* These three commands overlap, and you will see all three in tutorials.

*Explain.* `git switch` changes branches. `git restore` puts a file back. `git restore index.html` throws away the changes you have not committed and returns the file to its last committed version. `git restore --staged style.css` takes a file out of staging but keeps your edit in the folder. `git checkout` is the older command that does both jobs; its manual title is "Switch branches or restore working tree files" (*git-checkout*). `git checkout -b name` is the older way to write `git switch -c name`. You will meet it in older tutorials; this course uses `switch` and `restore` because each does one job. One more word you may hear is "check-in." That is not a Git command.

*Illustrate.*

![A terminal: git status --short shows index.html modified, git restore index.html, status is empty; then style.css staged with M in the left column, git restore --staged moves the M to the right column, git restore style.css, and git status says working tree clean.](images/m12-restore.png)
*Watch the `M` move from the left column (staged) to the right column (not staged) after `git restore --staged`. (real output, rendered; captured on Linux with Git 2.43.0)*

*Apply.* Be careful: `git restore` on a file throws away your edits to it. There is no undo for edits you never committed. Run `git diff` on the file first.

### 8. How do you keep files out of Git?

*Introduce.* Some files in your folder should never be committed: editor settings, system files, logs.

*Explain.* A file named `.gitignore`, in the top of your project, lists patterns Git should ignore. Use this starter:

```
.vscode/
Thumbs.db
*.log
```

`.vscode/` (with the slash) matches a folder; the manual says a pattern ending in a slash "will only match directories." `Thumbs.db` is a file Windows can create to store picture thumbnails. `*.log` matches every file ending in `.log`, because "an asterisk `*` matches anything except a slash" (*gitignore*). One catch: "Files already tracked by Git are not affected" (*gitignore*). Add the `.gitignore` before you commit those files, not after.

*Illustrate.*

![A terminal: git status --short lists .vscode/, Thumbs.db and debug.log as untracked; after .gitignore is created, git status --short lists only .gitignore; then it is committed and status is clean.](images/m12-gitignore.png)
*The proof: three untracked entries disappear the moment `.gitignore` exists. The files are still in the folder; Git just stops reporting them. (real output, rendered; captured on Linux with Git 2.43.0)*

*Apply.* Run `git status --short` in `my-site`. If you see `.vscode/` or a `.log` file listed, that is your sign to add a `.gitignore`.

### 9. What goes in a README?

*Introduce.* `README.md` is the first thing a visitor sees on your repository page. GitHub shows it below the file list.

*Explain.* The `.md` means Markdown: `#` makes a heading, `##` a smaller one. This course uses four headings for every project: **What it does**, **Built with**, **What I learned**, **Live site**. Keep each to a sentence or two. "What I learned" is the one employers read.

*Illustrate.* This is the README committed in the story (the commit appears in Concept 10):

```
# My Portfolio

## What it does
A small personal website with a Home page and an About page.

## Built with
HTML and CSS.

## What I learned
How to keep a project's history with Git: one change per commit,
branches for new pages, and a .gitignore for files that do not belong.

## Live site
https://your-username.github.io/portfolio/
```

*Apply.* Draft the "What I learned" section for your own `my-site` in two sentences. You will use it in the Project.

### 10. How do you mark a finished version?

*Introduce.* A **tag** is a name stuck to one commit, such as `v1.0`. A GitHub **release** is a page built on a tag.

*Explain.* `git tag v1.0` puts the name on the commit you are on. `git tag` lists your tags. `git log --oneline --decorate` shows the tag next to the commit. GitHub Docs explains the link: "Releases are based on Git tags, which mark a specific point in your repository's history" (*About releases*). Tags are not sent by a plain `git push`; you send one with `git push origin v1.0`, or let GitHub create the tag when you draft the release on the website. **[unverified in this build: no push was run, so the push of a tag and the GitHub release form were not tested here.]**

*Illustrate.*

![A terminal: README.md committed, git tag v1.0, git tag printing v1.0, and git log --oneline --decorate showing HEAD -> main, tag: v1.0 beside the newest commit.](images/m12-tag.png)
*`tag: v1.0` now sits on the README commit. That exact snapshot can always be found again by name. (real output, rendered; captured on Linux with Git 2.43.0)*

![A GitHub release page for Portfolio v1.0 with a Latest badge, tag v1.0 on main, release notes and source code downloads.](images/m12-release.png)
*What a release looks like on GitHub: a title, notes and downloads, all pointing at the tagged commit. (illustration, not a screenshot)*

*Apply.* Run `git tag` in `my-site`. You probably have none yet. You will add `v1.0` in the Project.

### 11. Can VS Code do all of this with buttons?

*Introduce.* Yes. The Source Control view in VS Code runs the same Git commands behind its buttons.

*Explain.* In a folder with no repository, the view shows **Initialize Repository** (the same as `git init`). When you have changes, each file has a **+** button, **Stage Changes**, which is `git add`. You type a message in the box and select **Commit**. To put a brand-new repository on GitHub you open the Command Palette (Ctrl+Shift+P) and run **Publish to GitHub**. After that, **Sync Changes** sends and receives commits; VS Code's documentation says it "pulls remote changes before pushing your commits" (*Quickstart: use source control in VS Code*). The terminal is still the main tool in this course, because its messages teach you what happened. Use the buttons once you can say which command each one runs.

*Illustrate.*

![Three Source Control panels: one with an Initialize Repository button; one with a commit message box, a Commit button, a staged index.html and an unstaged style.css with a plus button; one with Publish to GitHub and Sync Changes buttons.](images/m12-vscode-source-control.png)
*Each button is a Git command you already know. (illustration, not a screenshot)*

*Apply.* Open the Source Control view in `my-site` and match each file it lists to a line of `git status --short`.

### 12. How do Issues and pull requests work together?

*Introduce.* An **Issue** is a note on GitHub that names a piece of work. A **pull request** (PR) proposes the commits that do that work. GitHub Docs puts it plainly: "Pull requests are proposals to merge code changes into a project" (*Pull requests*).

*Explain.* The flow is: open an Issue (say, #1 "Add a Contact page"); make a branch; commit on it; push the branch; open a pull request from the branch into `main`. In the PR description, write **`Closes #1`**. When the PR is merged, GitHub closes Issue #1 for you. The keywords that work are close, closes, closed, fix, fixes, fixed, resolve, resolves and resolved, and GitHub only reads them "when the pull request targets the repository's *default* branch" (*Linking a pull request to an issue*). For you, that is `main`.

Working alone, you can still review your own work. In the PR, open **Files changed**, hover a line number, and click the blue comment icon. Type a note, then choose **Comment** for one note or **Start a review** for several (*Commenting on a pull request*). Reading your own diff on GitHub, slowly, catches mistakes you skipped past in the terminal.

*Illustrate.*

![A GitHub page showing Issue #1 Add a Contact page beside Pull request #2 Add Contact page, whose description ends with Closes #1, and a note that merging closes the issue.](images/m12-issue-pr.png)
*`Closes #1` in the description links the two. Merge into `main`, and the Issue closes. (illustration, not a screenshot)*

![A GitHub Files changed view of contact.html with a blue plus icon beside line 11 and a comment box with Start a review and Comment buttons.](images/m12-line-comment.png)
*A line comment on your own pull request: a note pinned to the exact line it is about. (illustration, not a screenshot)*

*Apply.* Write, on paper, the title of an Issue for the next change you want on `my-site`. Keep it to a few words that start with a verb.

### 13. What is GitHub Desktop?

*Introduce.* GitHub Desktop is "a free, open source application that helps you to work with files hosted on GitHub" (*About GitHub Desktop*). It runs on Windows and macOS.

*Explain.* It shows the same ideas you now know: a Changes list (status and diff), a History list (log), a commit box, and buttons to talk to GitHub. In this course it is **awareness only**. You do not need to install it. If a future job uses it, you will recognize every part.

*Illustrate.*

![A GitHub Desktop window with Current repository portfolio, Current branch main, a Changes tab listing index.html, a diff with one added line, and a commit button.](images/m12-github-desktop.png)
*Different screen, same model: changes, staging, commit, history. (illustration, not a screenshot)*

*Apply.* Name the terminal command that matches the History tab. (`git log`.)

### 14. What does "dubious ownership" mean?

*Introduce.* One day Git may refuse to work in a folder and print `fatal: detected dubious ownership in repository`.

*Explain.* Git checks that the folder belongs to the user account running Git. If it does not, Git stops, so that a repository someone else controls cannot run settings on your account. On Windows this tends to happen with folders on an external or network drive, or folders copied from another account. Your work is fine. Git prints the fix itself: one `git config --global --add safe.directory …` command with your folder's path. Copy it exactly as Git prints it, run it, and run `git status` again.

*Illustrate.*

![A terminal: git status fails with fatal: detected dubious ownership and prints a git config --global --add safe.directory command; that command is run, and git status then works.](images/m12-dubious.png)
*Git names the exact command to run. After it, `git status` works. (real output, rendered; captured on Linux by giving a copy of the project to a different user account. The paths are Linux paths; on Windows Git prints your Windows folder path.)* **[unverified: the exact path format Git prints on Windows, and which Windows drive setups trigger it on your computer.]**

*Apply.* If you ever see this message, read the last line first. That is the fix.

## Exercise

*Apply — your hands, about 45 minutes (estimate).* Type every command. Do not paste. This is a throwaway folder: you will not push it.

1. **Make the practice folder.** In File Explorer, create `git-practice` inside your `code559` folder (beside `my-site`, not inside it). Open it in VS Code with **File → Open Folder…**, then **Terminal → New Terminal**. Check that the prompt ends in `git-practice>`.
2. **Start a repository.** Type `git init`. Create a file `notes.txt` with one line, `Favorite color: blue` (use your own color). Save it. Then:

   ```
   git status --short
   git add notes.txt
   git commit -m "Add notes"
   ```

   *Predict* before you press Enter on the first line: what two characters will start the line? (`??`.)
3. **Make a branch.** `git switch -c add-hobby`. Add a second line to `notes.txt`, for example `Hobby: drawing`. Save. Then check before you commit:

   ```
   git diff
   git add notes.txt
   git diff --staged
   git commit -m "Add hobby line"
   ```

   Both diffs should show one `+` line.
4. **Prove the branch is separate.** `git switch main`. Look at `notes.txt` in VS Code (or type `cat notes.txt`). The hobby line is gone.
5. **Merge it.** Still on `main`: `git merge add-hobby`. Look for the word `Fast-forward`. Then `git branch -d add-hobby` and `git log --oneline`. You should see two commits.
6. **Break it on purpose: a merge conflict.** You will change the same line two different ways on two branches.

   ```
   git switch -c change-color
   ```

   Change `blue` to `green` in `notes.txt`, save, then `git add notes.txt` and `git commit -m "Change color to green"`. Now `git switch main`, change `blue` to `orange`, save, `git add notes.txt`, `git commit -m "Change color to orange"`. Finally:

   ```
   git merge change-color
   ```

   Read the whole message.

   ![A terminal: git merge change-color prints CONFLICT (content): Merge conflict in notes.txt; git status --short shows UU notes.txt; the file contains HEAD and change-color sections separated by equals signs, with the hobby line untouched below.](images/m12-conflict.png)
   *Git merged what it could (the hobby line) and stopped at the line both branches changed. `UU` means "both changed it." Between `<<<<<<< HEAD` and `=======` is your side (`main`); below it, the branch. (real output, rendered; captured on Linux with Git 2.43.0. On Windows, `cat` in PowerShell shows the same file lines.)*

7. **Fix it.** Open `notes.txt` in VS Code. Delete the three marker lines (`<<<<<<<`, `=======`, `>>>>>>>`) and the color you do not want, so one `Favorite color` line is left. Save. Then:

   ```
   git add notes.txt
   git commit -m "Merge change-color, keep green"
   git log --oneline --graph
   git branch -d change-color
   ```

   ![A terminal: the merge commit is made, and git log --oneline --graph draws two lines splitting after Add hobby line and joining again at the merge commit, then the branch is deleted.](images/m12-conflict-fixed.png)
   *This time the log shows a real merge commit with two parents: the graph splits and joins. Compare it with the straight line after the fast-forward in step 5. (real output, rendered; captured on Linux with Git 2.43.0)*

8. **Tag it.** `git tag v0.1`, then `git log --oneline --decorate -1`. The newest commit should show `tag: v0.1`.
9. **Modify.** Make one more branch of your own, change one line, and merge it. Before you merge, say whether it will be a fast-forward, and why.

## Project (in the full packet)

You put your real `my-site` through the full team workflow, start to finish. You add a `.gitignore` and a `README.md` with the four headings, open a GitHub Issue for one real improvement, do the work on a branch, push the branch, open a pull request whose description says `Closes #n`, leave line comments on your own diff, merge it, and watch the Issue close by itself. Then you tag the result `v1.0` and publish it as your site's first GitHub release. A visitor to your repository sees a clear README, a tidy history of small commits, a closed Issue linked to a merged pull request, and a v1.0 release. The full brief, the step-by-step build, and the finishing work in Git are in the Module 12 packet. [Get the packet →](PACKET_LINK_MODULE_12)

## Common misconception

> *"When I commit, my work is saved on GitHub."*

What would you say? Hint: look at the mental-model picture in Concept 1 and count the arrows between the Commits box and GitHub.

## Summary

Git keeps your work in four places, and `git add`, `git commit` and `git push` move it from the working folder to staging, to commits, to GitHub. `git status --short` tells you where each file is, with the left column for staging and the right column for the folder. One change per commit, with a message that finishes "This commit will…", makes your history readable. `git diff`, `git diff --staged` and `git diff --stat` let you check every line before it becomes history, and `git log --oneline` reads that history back. A branch made with `git switch -c` keeps new work separate until `git merge` brings it in, often as a fast-forward, and `git branch -d` tidies up. `git switch` changes branches and `git restore` puts files back; `git checkout` is the older command that does both. A `.gitignore` keeps editor, system and log files out, and `git status` proves it. A README with four headings tells visitors what the project is. A tag names a version, and a GitHub release is built on it. VS Code's Source Control view and GitHub Desktop do the same jobs with buttons. Issues name the work, pull requests propose it, `Closes #n` links them, and line comments let you review yourself. "Dubious ownership" is a safety check, and Git prints its own fix.

## Check your understanding

1. `git status --short` shows `M  style.css` on one line and ` M index.html` on another. Which file is ready to commit, and how can you tell?
2. In the Exercise, why did step 5 say `Fast-forward` while step 6 stopped with a conflict?
3. **What would you test** to prove that your `.gitignore` is working?

## Before next module

This module is the full workflow, so instead of the short routine, check off the whole thing:

- [ ] I can draw the four places (folder, staging, commits, remote) and name the command between each
- [ ] I run `git status` (or `--short`) before and after other Git commands, and can read the two columns
- [ ] I run `git diff --stat`, `git diff` and `git diff --staged` before every commit
- [ ] Each commit holds one change, with a message that finishes "This commit will…"
- [ ] I can make a branch with `git switch -c`, prove it is separate, merge it, and delete it
- [ ] I can fix a merge conflict by removing the markers, then `git add` and `git commit`
- [ ] `my-site` has a `.gitignore` (`.vscode/`, `Thumbs.db`, `*.log`) and a `README.md` with the four headings
- [ ] I have opened an Issue, a pull request with `Closes #n`, and left a line comment on my own PR
- [ ] `my-site` has a `v1.0` tag and a GitHub release
- [ ] I can still do the short routine: `git status` → `git add` → `git commit -m "…"` → `git push` → check the live page

## Go further

- git-scm.com manual pages: *git-switch*, *git-merge* (the "Fast-forward merge" and "How conflicts are presented" sections), *gitignore*, *git-restore*, *git-checkout*
- GitHub Docs: *Pull requests*, *Linking a pull request to an issue*, *Commenting on a pull request*, *About issues*, *About releases*, *About GitHub Desktop*
- VS Code Docs: *Quickstart: use source control in VS Code* and *Source control in VS Code*
- GitHub Skills, free practice exercises that run inside a repository of your own:
  - *Communicate using Markdown* (`skills/communicate-using-markdown`) for your README
  - *Review pull requests* (`skills/review-pull-requests`)
  - *Resolve Merge Conflicts* (`skills/resolve-merge-conflicts`)
  - *Create a release based workflow* (`skills/release-based-workflow`)
- [W3Schools Git Tutorial](AFFILIATE_W3SCHOOLS_GIT)

*Affiliate link: Code559 may earn a commission at no extra cost to you.*

## What to keep

Keep your `git-practice` folder until you finish the Project; its `git log --oneline --graph` is a picture of both kinds of merge. Keep your Issue title and your "What I learned" draft. Then answer for yourself: **which step would be hardest to repeat without this post, and why?**

---

*Code559 is a 559 Solutions project. Portions adapted from Visual Studio Code documentation (CC BY 3.0 US), GitHub Docs (CC BY 4.0), and GitHub Skills (MIT). Screenshots used with permission from Microsoft.*

*Sources checked 2026-10-09: git-scm.com "git-switch", "git-merge", "gitignore", "git-restore", "git-checkout"; GitHub Docs "Pull requests" (the page at the about-pull-requests address), "Linking a pull request to an issue", "Commenting on a pull request", "About issues", "About releases", "About GitHub Desktop"; VS Code Docs "Quickstart: use source control in VS Code" and "Source control in VS Code"; GitHub repositories skills/communicate-using-markdown, skills/review-pull-requests, skills/resolve-merge-conflicts, skills/release-based-workflow.*
