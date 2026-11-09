# CLAUDE.md

Personal academic site built on al-folio v1.x (thin Jekyll starter; runtime lives in `al_*` gems).
See `AGENTS.md` for the upstream rules (gem-owned paths, Gemfile/_config.yml plugin lists must agree).

Site-specific differences from upstream:

- `baseurl` is blank (site is served at the root of https://cth127.github.io), NOT `/al-folio`.
- Only pages: about, publications, projects, cv, 404. Blog/news/books/teachings content was removed.
- Disabled plugins (removed from `_config.yml` `plugins:` only; still in `Gemfile` so `Gemfile.lock` stays valid):
  `al_analytics`, `al_ext_posts`, `al_search`. Responsive images (imagemagick) are off.
- CV uses `cv_format: jsonresume` → `assets/json/resume.json`.
- Only workflow is `.github/workflows/deploy.yml` (no tests/lint workflows).
- Paper project pages are external sites. Listed on `/projects/` from `_projects/*.md` (fields: redirect, paper,
  github, img, venue) with custom markup + inline <style> in `_pages/projects.md` (deliberately no gem overrides).
  Collection has `output: false`; no per-project pages are generated.
- Policy: do not shadow gem-owned files (layouts/includes/sass/main.scss) so al-folio updates stay simple.
- Known issue: CV lists show bullets (al_folio_cv 1.0.2 bug, fixed upstream in 1.0.3 but not yet on rubygems as of
  2026-11-09). Fix = bump `al_folio_cv` to 1.0.3 in Gemfile + Gemfile.lock (incl. CHECKSUMS) once released.
