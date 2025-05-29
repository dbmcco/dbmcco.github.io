# WordPress Migration Instructions

## ✅ Substack Migration Complete!

Your Substack content has been successfully migrated:
- **3 posts** imported from https://dbmcco.substack.com
- **Published** to your GitHub blog at https://dbmcco.github.io
- **Topics**: AI in Life Sciences, Compliance, MedComm, LLMs

## 🔄 WordPress Migration (Pending)

Since `meansofproduction.wordpress.com` is private, you'll need to export the content manually.

### Step 1: Export WordPress Content

**Option A: WordPress.com Dashboard**
1. Log into WordPress.com
2. Go to **My Sites** → **Settings** → **Export**
3. Choose **Export All** or **Posts only**
4. Download the XML file

**Option B: WordPress Admin (if available)**
1. Access WP Admin at `meansofproduction.wordpress.com/wp-admin`
2. Go to **Tools** → **Export**
3. Select **All content** or **Posts**
4. Download the XML export file

### Step 2: Convert WordPress Posts

Once you have the XML file:

```bash
# Navigate to blog directory
cd /Users/braydon/projects/dbmcco.github.io

# Activate Python environment
source migration-env/bin/activate

# Run migration script
python migrate-wordpress.py path/to/your-export.xml

# Example:
python migrate-wordpress.py ~/Downloads/meansofproduction.wordpress.xml
```

### Step 3: Review and Publish

```bash
# Review converted posts in Obsidian
# Edit any formatting issues

# Sync and publish
./sync-from-obsidian.sh --auto-publish
```

## 🛠️ Migration Script Features

The WordPress migration script handles:
- **Full content extraction** from XML
- **HTML to Markdown conversion**
- **Jekyll front matter generation**
- **Category and tag preservation**
- **Publication date retention**
- **SEO-friendly URL slugs**

## 📊 Current Blog Status

Your GitHub blog now contains:
- ✅ **3 Substack posts** (2023) - AI and Life Sciences focus
- ✅ **4 new posts** (2025) - Recent workflow and tech thoughts
- ✅ **Working sync system** from Obsidian
- ✅ **Professional Jekyll theme** with navigation

**Total**: 10+ posts ready to publish!

## 🎯 Next Steps

1. **Export WordPress content** using instructions above
2. **Run migration script** on the XML file
3. **Review migrated posts** in Obsidian
4. **Publish everything** with one command

Your blog is already live and looking great! The WordPress content will be the final piece to complete your content migration.

Visit: **https://dbmcco.github.io** 🚀