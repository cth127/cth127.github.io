---
layout: page
title: projects
permalink: /projects/
description:
nav: true
nav_order: 3
---

<!--
  One full-width row per project: thumbnail on the left, title / description / links on the right.
  Each row comes from a file in _projects/ (see README.md for the fields).
  Markup lives here (not in a gem include override) so al-folio updates are unaffected.
-->
<style>
  .project-list .card { margin-bottom: 1.5rem; overflow: hidden; }
  /* Small fixed-width thumbnail on the left, text takes the rest; stacks on narrow screens. */
  .project-list .project-row { display: flex; align-items: center; gap: 1rem; padding: 1rem; }
  .project-list .project-thumb { flex: 0 0 200px; } /* thumbnail width: change 200px to resize */
  .project-list .project-thumb img { display: block; width: 100%; height: auto; border-radius: 0.25rem; } /* never cropped */
  .project-list .project-text { flex: 1 1 auto; min-width: 0; }
  .project-list .project-text .card-title { margin-top: 0; }
  @media (max-width: 576px) {
    .project-list .project-row { flex-direction: column; align-items: stretch; }
    .project-list .project-thumb { flex-basis: auto; }
  }
  .project-list .card-title a { color: var(--global-text-color); text-decoration: none; }
  .project-list .card-title a:hover { color: var(--global-theme-color); }
  .project-list .project-links { margin-top: 0.75rem; }
  .project-list .project-links a {
    display: inline-block;
    margin: 0 0.4rem 0.4rem 0;
    padding: 0.2rem 0.9rem;
    font-size: 0.75rem;
    text-transform: uppercase;
    text-decoration: none;
    color: var(--global-text-color);
    border: 1px solid var(--global-text-color);
    border-radius: 0.125rem;
  }
  .project-list .project-links a:hover { color: var(--global-theme-color); border-color: var(--global-theme-color); }
</style>

<div class="project-list">
{% assign sorted_projects = site.projects | sort: "importance" %}
{% for project in sorted_projects %}
  <div class="card hoverable">
    <div class="project-row">
      {% if project.img %}
      <div class="project-thumb">
        <a href="{{ project.redirect | default: project.paper }}">
          <img src="{{ project.img | relative_url }}" alt="{{ project.title }} thumbnail" loading="lazy">
        </a>
      </div>
      {% endif %}
      <div class="project-text">
        <h3 class="card-title"><a href="{{ project.redirect | default: project.paper }}">{{ project.title }}</a></h3>
        {% if project.venue %}<p class="card-text"><em>{{ project.venue }}</em></p>{% endif %}
        <p class="card-text">{{ project.description }}</p>
        <div class="project-links">
          {% if project.redirect %}<a href="{{ project.redirect }}">Project page</a>{% endif %}
          {% if project.paper %}<a href="{{ project.paper }}">Paper</a>{% endif %}
          {% if project.github %}<a href="{{ project.github }}">Code</a>{% endif %}
        </div>
      </div>
    </div>
  </div>
{% endfor %}
</div>
