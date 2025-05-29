#!/bin/bash

# Enhanced sync script to copy blog posts from Obsidian vault to Jekyll site
# Usage: ./sync-from-obsidian.sh [--auto-publish]

OBSIDIAN_BLOG_DIR="/Users/braydon/Obsidian/bvault/blog"
JEKYLL_POSTS_DIR="/Users/braydon/projects/dbmcco.github.io/_posts"
AUTO_PUBLISH=false

# Check for auto-publish flag
if [ "$1" = "--auto-publish" ]; then
    AUTO_PUBLISH=true
fi

echo "🔄 Syncing blog posts from Obsidian to Jekyll..."

# Check if Obsidian blog directory exists
if [ ! -d "$OBSIDIAN_BLOG_DIR" ]; then
    echo "❌ Error: Obsidian blog directory not found: $OBSIDIAN_BLOG_DIR"
    exit 1
fi

# Create posts directory if it doesn't exist
mkdir -p "$JEKYLL_POSTS_DIR"

# Track what we're doing
COPIED_COUNT=0
SKIPPED_COUNT=0

# Copy all markdown files from Obsidian blog to Jekyll posts
# Only copy files that have Jekyll front matter (start with ---)
for file in "$OBSIDIAN_BLOG_DIR"/*.md; do
    if [ -f "$file" ]; then
        filename=$(basename "$file")
        
        # Check if file starts with Jekyll front matter
        if head -n 1 "$file" | grep -q "^---"; then
            echo "✅ Copying: $filename"
            cp "$file" "$JEKYLL_POSTS_DIR/"
            ((COPIED_COUNT++))
        else
            echo "⏭️  Skipping (no front matter): $filename"
            ((SKIPPED_COUNT++))
        fi
    fi
done

echo ""
echo "📊 Sync Summary:"
echo "   • Copied: $COPIED_COUNT posts"
echo "   • Skipped: $SKIPPED_COUNT files"

if [ $COPIED_COUNT -eq 0 ]; then
    echo "   • No posts to sync"
    exit 0
fi

if [ "$AUTO_PUBLISH" = true ]; then
    echo ""
    echo "🚀 Auto-publishing changes..."
    cd /Users/braydon/projects/dbmcco.github.io
    
    # Check if there are changes to commit
    if ! git diff --quiet || ! git diff --cached --quiet; then
        git add .
        git commit -m "Auto-sync blog posts from Obsidian

- Synced $COPIED_COUNT posts from bvault/blog/
- Generated automatically by sync script

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>"
        
        echo "📤 Pushing to GitHub..."
        git push
        echo "✅ Blog updated! Check https://dbmcco.github.io in a few minutes."
    else
        echo "   • No changes to publish"
    fi
else
    echo ""
    echo "📝 Next steps:"
    echo "   1. Review posts in $JEKYLL_POSTS_DIR"
    echo "   2. Run './sync-from-obsidian.sh --auto-publish' to auto-publish"
    echo "   3. Or manually: git add . && git commit && git push"
fi