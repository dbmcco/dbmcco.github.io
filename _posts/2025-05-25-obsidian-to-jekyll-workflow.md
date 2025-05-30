---
layout: post
title: "Building an Obsidian to Jekyll Workflow"
date: 2025-05-25 14:30:00 -0500
categories: productivity workflow
tags: [obsidian, jekyll, automation, blogging]
---


After years of trying different note-taking and blogging systems, I've finally found a setup that works: **Obsidian for writing, Jekyll for publishing**.

## Why This Combination Works

**Obsidian Benefits:**
- Excellent writing environment with vim keybindings
- Powerful linking and graph features
- Local files in plain markdown
- Extensible with plugins

**Jekyll Benefits:**
- Static site generation
- GitHub Pages integration
- Flexible theming
- Great performance

## The Sync Process

My workflow is straightforward:

1. **Write** in Obsidian at `bvault/blog/`
2. **Sync** with a simple script that copies posts with front matter
3. **Publish** via git push to GitHub Pages

The magic is in the front matter - only files that start with Jekyll front matter get synced:

```yaml
---
layout: post
title: "Your Title"
date: 2025-05-25 10:00:00 -0500
categories: your categories
tags: [tag1, tag2]
---
```

## Next Improvements

I'm planning to enhance this with:
- Automatic image optimization
- Tag-based organization
- Draft management
- Automated publishing schedules

The goal is to make publishing as frictionless as possible while maintaining full control over the content.