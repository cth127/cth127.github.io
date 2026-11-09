# cth127.github.io

Personal academic homepage of Taehun Cha, built on [al-folio](https://github.com/alshedivat/al-folio) v1.x
(started from upstream commit `e0a684c`, 2026-11-02). Template docs are kept in [`docs/`](docs/).

## What lives where

| What | File |
| --- | --- |
| About page | `_pages/about.md` |
| Publications | `_bibliography/papers.bib` (PDFs in `assets/pdf/<year>/`) |
| CV page | `assets/json/resume.json` (PDF: `assets/pdf/CV.pdf`) |
| Name, URL, scholar name highlighting | `_config.yml` |
| Email / social links | `_data/socials.yml` |

## Paper project pages

Project pages are hosted as separate static sites (not inside this repo).
Link them from the bib entry, e.g.

```bibtex
  html    = "https://arxiv.org/abs/xxxx.xxxxx",   % shown as an "HTML" button
  website = "https://cth127.github.io/<paper>/", % shown as a "Website" button
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
