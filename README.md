# cth127.github.io

Personal academic homepage of Taehun Cha, built on [al-folio](https://github.com/alshedivat/al-folio) v1.x
(started from upstream commit `e0a684c`, 2026-11-02). Template docs are kept in [`docs/`](docs/).

## What lives where

| What | File |
| --- | --- |
| About page | `_pages/about.md` |
| Project cards | `_projects/*.md` (thumbnails in `assets/img/projects/`) |
| Publications | `_bibliography/papers.bib` (PDFs in `assets/pdf/<year>/`) |
| CV page | `assets/json/resume.json` (PDF: `assets/pdf/CV.pdf`) |
| Name, URL, scholar name highlighting | `_config.yml` |
| Email / social links | `_data/socials.yml` |

## Projects section (paper project pages)

Project pages are separate static sites hosted outside this repo. This site only links to them, in two places:

1. **Projects page** (`/projects/`): one full-width row per file in `_projects/`
   (thumbnail left, text and buttons right). Copy `_projects/weightgram.md` and edit:

   ```yaml
   ---
   title: Paper title
   venue: NeurIPS 2026                              # optional, shown in italics
   description: One-line summary.
   redirect: https://cth127.github.io/weightgram/   # "Project page" button (+ title/image link)
   paper: https://arxiv.org/abs/xxxx.xxxxx          # "Paper" button
   github: https://github.com/cth127/weightgram     # "Code" button
   img: assets/img/projects/weightgram.png          # optional thumbnail (any landscape ratio; never cropped)
   importance: 1                                    # smaller = shown first
   ---
   ```

   All link fields are optional; the title links to `redirect`, or to `paper` if there is no project page.
   The layout is plain markup in `_pages/projects.md` (no gem override).

2. **Publications page**: add a `website` field to the bib entry to get a "Website" button. Use `html` for the arXiv/publisher link:

   ```bibtex
     html    = "https://arxiv.org/abs/xxxx.xxxxx",    % "HTML" button
     website = "https://cth127.github.io/weightgram/", % "Website" button
   ```

Tip: a separate GitHub repo named e.g. `weightgram` with Pages enabled is served at
`https://cth127.github.io/weightgram/` automatically.

## Deploy

Pushing to `main` runs `.github/workflows/deploy.yml`, which builds the site and pushes `_site` to the
`gh-pages` branch. GitHub Pages must be set to deploy from the `gh-pages` branch.

## Updating al-folio later

al-folio v1 is a thin starter: layouts and features live in versioned `al_*` gems.
Updating is mostly bumping the pins in `Gemfile` (+ `bundle update`), see `docs/` and
`.agents/skills/al-folio-v1-migration/`.
