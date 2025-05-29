# Obsidian to Jekyll Blog Workflow

## 🎯 Quick Start

**Write a new post:**
1. Create a new `.md` file in `/Users/braydon/Obsidian/bvault/blog/`
2. Start with Jekyll front matter
3. Write your content
4. Sync and publish

**Publish posts:**
```bash
cd /Users/braydon/projects/dbmcco.github.io
./sync-from-obsidian.sh --auto-publish
```

## 📝 Writing Posts in Obsidian

### File Naming Convention
Use Jekyll's standard naming: `YYYY-MM-DD-post-title.md`

Examples:
- `2025-05-27-my-thoughts-on-ai.md`
- `2025-05-28-building-better-workflows.md`

### Front Matter Template
Every post must start with Jekyll front matter:

```yaml
---
layout: post
title: "Your Post Title"
date: 2025-05-27 10:00:00 -0500
categories: technology business
tags: [ai, productivity, workflows]
---
```

**Important:** Use dates in the past or present, never future dates.

### Draft Posts
Files without front matter won't be synced:
- `draft-ideas.md` ← Won't be published
- `research-notes.md` ← Won't be published

## 🔄 Sync Options

### Manual Review (Recommended)
```bash
./sync-from-obsidian.sh
# Review changes, then:
git add .
git commit -m "Add new blog post"
git push
```

### Auto-Publish (Fast)
```bash
./sync-from-obsidian.sh --auto-publish
```

## 📊 What Gets Synced

✅ **Synced to Blog:**
- `.md` files with Jekyll front matter
- Properly dated posts
- Published content

⏭️ **Skipped:**
- Files without front matter (drafts)
- Non-markdown files
- Files starting with `draft-`

## 🚀 Publishing Timeline

1. **Sync** → Copies files to Jekyll `_posts/`
2. **Commit** → Saves changes to Git
3. **Push** → Triggers GitHub Pages build
4. **Live** → Available at https://dbmcco.github.io (1-2 minutes)

## 💡 Tips

**Productive Writing:**
- Use Obsidian's linking `[[page]]` for internal references
- Leverage tags for organization
- Keep drafts without front matter until ready

**Quick Publishing:**
- Set up an Obsidian hotkey to run the sync script
- Use consistent naming conventions
- Date posts accurately to avoid timezone issues

**Content Organization:**
- Use categories for broad topics: `technology`, `business`, `personal`
- Use tags for specific themes: `ai`, `workflows`, `productivity`

## 🔍 Troubleshooting

**Posts not appearing?**
- Check that dates are in the past
- Verify front matter format
- Ensure file names match dates

**Sync not working?**
- Verify Obsidian vault path: `/Users/braydon/Obsidian/bvault/blog/`
- Check file permissions
- Run sync script with verbose output