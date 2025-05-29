# WordPress to Jekyll Migration Guide

## Step 1: Export WordPress Content

Since your WordPress blog is private, you'll need to export the content:

### Option A: WordPress Admin Export
1. Log into your WordPress admin at `https://meansofproduction.wordpress.com/wp-admin`
2. Go to **Tools > Export**
3. Choose **All content** or **Posts** 
4. Download the XML file

### Option B: WordPress.com Export  
1. Go to your WordPress.com dashboard
2. Navigate to **My Sites > Settings > Export**
3. Choose **Export All** or **Posts**
4. Download the export file

## Step 2: Convert to Markdown

I'll create a Python script to convert your WordPress XML export to Jekyll-compatible markdown files.

## Step 3: Organize in Obsidian

The script will place converted posts in your `bvault/blog/` directory with proper:
- Jekyll front matter
- Converted HTML to Markdown
- Preserved publication dates
- Category and tag mapping

## Step 4: Sync and Publish

Use your existing sync workflow:
```bash
./sync-from-obsidian.sh
git add .
git commit -m "Import WordPress posts"
git push
```

## Next Steps

1. Export your WordPress content using one of the methods above
2. Place the XML file in this directory
3. Run the conversion script I'll create
4. Review converted posts in Obsidian
5. Sync to your blog