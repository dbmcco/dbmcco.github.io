# Braydon McCormick's Blog

This is my personal blog built with Jekyll and hosted on GitHub Pages.

## Workflow

1. **Write**: Create blog posts in Obsidian vault at `/Users/braydon/Obsidian/bvault/blog/`
2. **Sync**: Run `./sync-from-obsidian.sh` to copy posts to Jekyll
3. **Publish**: Commit and push to GitHub for automatic deployment

## Blog Post Format

Posts should include Jekyll front matter:

```yaml
---
layout: post
title: "Your Post Title"
date: YYYY-MM-DD HH:MM:SS -0500
categories: category1 category2
tags: [tag1, tag2, tag3]
---
```

## Local Development

```bash
bundle install
bundle exec jekyll serve
```

Visit `http://localhost:4000` to preview locally.

## Publishing

```bash
./sync-from-obsidian.sh
git add .
git commit -m "Add new blog post"
git push
```

The site will be automatically built and deployed to https://dbmcco.github.io