# CLAUDE.md

Personal academic site built on al-folio v1.x (thin Jekyll starter; runtime lives in `al_*` gems).
See `AGENTS.md` for the upstream rules (gem-owned paths, Gemfile/_config.yml plugin lists must agree).

Site-specific differences from upstream:

- `baseurl` is blank (site is served at the root of https://cth127.github.io), NOT `/al-folio`.
- Only pages: about, publications, cv, 404. Blog/news/projects/books/teachings content was removed.
- Disabled plugins (removed from `_config.yml` `plugins:` only; still in `Gemfile` so `Gemfile.lock` stays valid):
  `al_analytics`, `al_ext_posts`, `al_search`. Responsive images (imagemagick) are off.
- CV uses `cv_format: jsonresume` → `assets/json/resume.json`.
- Only workflow is `.github/workflows/deploy.yml` (no tests/lint workflows).
- Paper project pages are external sites, linked via `website`/`html` fields in `_bibliography/papers.bib`.
