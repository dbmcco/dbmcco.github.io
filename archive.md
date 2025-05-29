---
layout: page
title: Archive
permalink: /archive/
---

# Complete Post Archive

*{{ site.posts.size }} posts spanning 2007-2025*

<div class="archive-summary">
  <p>This archive contains my complete blog history from startup journey to AI insights:</p>
  <ul>
    <li><strong>2007-2009:</strong> rVibe startup journey, music industry insights, VC funding</li>
    <li><strong>2023:</strong> AI in Life Sciences, medical communications, compliance</li>
    <li><strong>2025:</strong> Modern development workflows and technical innovation</li>
  </ul>
</div>

<div class="archive">
  {% assign postsByYear = site.posts | group_by_exp:"post", "post.date | date: '%Y'" %}
  {% for year in postsByYear %}
    <h2>{{ year.name }} <span class="year-count">({{ year.items.size }} posts)</span></h2>
    <ul>
      {% for post in year.items %}
        <li>
          <span class="post-date">{{ post.date | date: "%b %-d" }}</span>
          <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
          {% if post.categories.size > 0 %}
            <span class="post-categories">
              {% for category in post.categories limit: 3 %}
                <span class="category">{{ category }}</span>
              {% endfor %}
            </span>
          {% endif %}
        </li>
      {% endfor %}
    </ul>
  {% endfor %}
</div>

<style>
.archive-summary {
  background: #f8f9fa;
  padding: 1.5rem;
  border-radius: 8px;
  margin-bottom: 2rem;
}

.archive-summary ul {
  margin: 1rem 0 0 0;
}

.year-count {
  color: #666;
  font-size: 0.8rem;
  font-weight: normal;
}

.archive ul {
  list-style: none;
  padding-left: 0;
}

.archive li {
  margin-bottom: 0.5rem;
  padding: 0.5rem 0;
  border-bottom: 1px solid #eee;
}

.archive li:last-child {
  border-bottom: none;
}

.post-date {
  color: #666;
  font-size: 0.9rem;
  margin-right: 1rem;
  min-width: 4rem;
  display: inline-block;
}

.post-categories {
  margin-left: 1rem;
}

.category {
  background: #f0f0f0;
  padding: 0.2rem 0.5rem;
  border-radius: 3px;
  font-size: 0.8rem;
  margin-right: 0.3rem;
  color: #666;
}

.archive h2 {
  border-bottom: 2px solid #eee;
  padding-bottom: 0.5rem;
  margin-top: 2rem;
}

.archive h2:first-of-type {
  margin-top: 0;
}
</style>