---
layout: page
title: Archive
permalink: /archive/
---

# Post Archive

<div class="archive">
  {% assign postsByYear = site.posts | group_by_exp:"post", "post.date | date: '%Y'" %}
  {% for year in postsByYear %}
    <h2>{{ year.name }}</h2>
    <ul>
      {% for post in year.items %}
        <li>
          <span class="post-date">{{ post.date | date: "%b %-d" }}</span>
          <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
          {% if post.categories.size > 0 %}
            <span class="post-categories">
              {% for category in post.categories %}
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
.archive ul {
  list-style: none;
  padding-left: 0;
}

.archive li {
  margin-bottom: 0.5rem;
  padding: 0.5rem 0;
  border-bottom: 1px solid #eee;
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
}
</style>