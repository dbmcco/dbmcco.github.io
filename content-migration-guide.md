# Content Migration Guide

## Sources to Migrate

### 1. Substack (dbmcco.substack.com) ✅ Accessible
**Found 3 articles:**
- "Is LifeScience compliance ready for ChatGPT?" (2023-06-12)
- "Transforming MedComm with AI" (2023-06-14) 
- "Expanded LLMs in Life Science and Health" (2023-07-18)

### 2. WordPress (meansofproduction.wordpress.com) 🔒 Private
**Status:** Requires manual export

## Migration Strategy

### Substack Migration (Automated)
I'll create a script to:
1. Fetch public Substack posts
2. Convert HTML to Markdown
3. Add Jekyll front matter
4. Save to Obsidian blog directory

### WordPress Migration (Manual Export Required)
**Option A: WordPress.com Export**
1. Log into WordPress.com dashboard
2. Go to My Sites → Settings → Export
3. Download XML export file
4. Run conversion script

**Option B: WordPress Admin Export**
1. Access WP Admin (if available)
2. Tools → Export → All Content
3. Download XML file

## Next Steps
1. I'll fetch and convert Substack content automatically
2. You provide WordPress export file for conversion
3. Review all migrated content in Obsidian
4. Publish to GitHub blog