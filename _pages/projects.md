---
layout: page
title: projects
permalink: /projects/
description:
nav: true
nav_order: 3
horizontal: true # true: wide cards (thumbnail left, text right), false: 3-column grid
---

<!-- Each card comes from a file in _projects/ and links to the external project page given by `redirect:`. -->
<div class="projects">
{% assign sorted_projects = site.projects | sort: "importance" %}
{% if page.horizontal %}
  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for project in sorted_projects %}
      {% include projects_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
{% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
{% endif %}
</div>
