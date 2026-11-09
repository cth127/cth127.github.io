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

1. **Projects page** (`/projects/`): one card per file in `_projects/`. Copy `_projects/weightgram.md` and edit:

   ```yaml
   ---
   title: Weight Gram Matrix
   description: One-line summary shown on the card.
   redirect: https://cth127.github.io/weightgram/   # where the card links
   img: assets/img/projects/weightgram.png          # optional thumbnail
   github: https://github.com/cth127/weightgram     # optional code icon
   importance: 1                                    # smaller = shown first
   ---
   ```

   `redirect` is required. Projects don't get their own page on this site (`output: false`), so a card with no `redirect` leads to a 404.

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
