#!/bin/bash

# Sync script to copy blog posts from Obsidian vault to Jekyll site
# Usage: ./sync-from-obsidian.sh

OBSIDIAN_BLOG_DIR="/Users/braydon/Obsidian/bvault/blog"
JEKYLL_POSTS_DIR="/Users/braydon/projects/dbmcco.github.io/_posts"

echo "Syncing blog posts from Obsidian to Jekyll..."

# Check if Obsidian blog directory exists
if [ ! -d "$OBSIDIAN_BLOG_DIR" ]; then
    echo "Error: Obsidian blog directory not found: $OBSIDIAN_BLOG_DIR"
    exit 1
fi

# Create posts directory if it doesn't exist
mkdir -p "$JEKYLL_POSTS_DIR"

# Copy all markdown files from Obsidian blog to Jekyll posts
# Only copy files that have Jekyll front matter (start with ---)
for file in "$OBSIDIAN_BLOG_DIR"/*.md; do
    if [ -f "$file" ]; then
        # Check if file starts with Jekyll front matter
        if head -n 1 "$file" | grep -q "^---"; then
            filename=$(basename "$file")
            echo "Copying: $filename"
            cp "$file" "$JEKYLL_POSTS_DIR/"
        else
            echo "Skipping (no front matter): $(basename "$file")"
        fi
    fi
done

echo "Sync complete!"
echo "Next steps:"
echo "1. Review posts in $JEKYLL_POSTS_DIR"
echo "2. Run 'git add .' to stage changes"
echo "3. Run 'git commit -m \"Update blog posts\"' to commit"
echo "4. Run 'git push' to publish to GitHub Pages"