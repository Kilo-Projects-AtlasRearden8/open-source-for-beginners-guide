# STATUS

## What was built

A beginner manual for using and contributing to open-source software, focused on
GitHub, written in plain English, with a printable checklist. Created by Asdale
Dynamics, LLC.

Files:

- `README.md` — project overview; credits Asdale Dynamics, LLC
- `LICENSE` — MIT License; copyright line exactly
  `Copyright (c) 2026 Asdale Dynamics, LLC`
- `docs/intro.md` — what open source is and what the guide covers
- `docs/finding-projects.md` — finding projects on GitHub
- `docs/installing.md` — installing via releases or from source
- `docs/reporting-issues.md` — reporting issues on GitHub
- `docs/first-pull-request.md` — making your first pull request (web UI only)
- `docs/checklist.md` — printable checklist (Markdown)
- `static/index.html` — static HTML version of the manual
- `static/checklist.html` — static HTML printable checklist
- `static/style.css` — shared styles, including print stylesheet

## How to run it

Open any file directly in a web browser:

- `static/index.html` — full manual
- `static/checklist.html` — printable checklist (use Ctrl+P / Cmd+P to print)

Markdown files in `docs/` can be read in any text editor or Markdown viewer.

No build step, no dependencies, no server required.

## Verification results

- HTML files parse without errors (`html.parser` check passed)
- `LICENSE` contains the exact line `Copyright (c) 2026 Asdale Dynamics, LLC`
- `README.md`, both HTML pages, and `LICENSE` credit Asdale Dynamics, LLC
- No `.github/workflows` directory present
- No secrets, API keys, or personal data found in committed files
- Git initialized locally; one commit created; no remote configured; nothing pushed

## Known gaps

- No automated test suite (static content only; nothing to test beyond HTML parsing)
- The manual is GitHub-focused and does not cover GitLab, Bitbucket, or self-hosted forges
- Install section covers common Python/Node patterns only; other ecosystems point to the project README
- Pull-request section uses GitHub's web UI only; command-line Git is not covered
