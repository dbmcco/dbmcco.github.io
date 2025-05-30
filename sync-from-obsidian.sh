#!/bin/bash

# Enhanced sync script to copy blog posts from Obsidian vault to Jekyll site
# Usage: ./sync-from-obsidian.sh [--auto-publish] [--verbose]

set -euo pipefail  # Exit on any error, undefined vars, pipe failures

OBSIDIAN_BLOG_DIR="/Users/braydon/Obsidian/bvault/blog"
JEKYLL_POSTS_DIR="/Users/braydon/projects/dbmcco.github.io/_posts"
LOG_FILE="/Users/braydon/projects/dbmcco.github.io/sync.log"
AUTO_PUBLISH=false
VERBOSE=false

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --auto-publish) AUTO_PUBLISH=true; shift ;;
        --verbose) VERBOSE=true; shift ;;
        *) echo "Unknown option: $1"; exit 1 ;;
    esac
done

# Logging function
log() {
    local timestamp=$(date "+%Y-%m-%d %H:%M:%S")
    echo "[$timestamp] $1" | tee -a "$LOG_FILE"
}

log_verbose() {
    if [[ "$VERBOSE" == true ]]; then
        log "VERBOSE: $1"
    fi
}

echo "🔄 Syncing blog posts from Obsidian to Jekyll..."
log "Sync started - Source: $OBSIDIAN_BLOG_DIR"

# Validation function for date consistency
validate_file() {
    local file="$1"
    local filename=$(basename "$file")
    
    log_verbose "Validating: $filename"
    
    # Check if file starts with Jekyll front matter
    if ! head -n 1 "$file" | grep -q "^---"; then
        echo "⏭️  Skipping (no front matter): $filename"
        log "SKIPPED: $filename (no front matter)"
        return 1
    fi
    
    # Extract date from filename (YYYY-MM-DD format)
    if [[ "$filename" =~ ^([0-9]{4}-[0-9]{2}-[0-9]{2})-(.+)\.md$ ]]; then
        local filename_date="${BASH_REMATCH[1]}"
        
        # Extract date from front matter
        local frontmatter_date=$(sed -n '/^date:/p' "$file" | head -1 | sed 's/date: *//g' | cut -d' ' -f1)
        
        # Check for date mismatch
        if [[ -n "$frontmatter_date" && "$filename_date" != "$frontmatter_date" ]]; then
            echo "❌ DATE MISMATCH: $filename (file:$filename_date vs front matter:$frontmatter_date)"
            log "ERROR: Date mismatch in $filename - filename=$filename_date, frontmatter=$frontmatter_date"
            return 2
        fi
        
        log_verbose "Date validation passed: $filename_date"
    else
        echo "⚠️  WARNING: Non-standard filename format: $filename"
        log "WARNING: $filename doesn't follow YYYY-MM-DD naming convention"
    fi
    
    return 0
}

# Check if Obsidian blog directory exists
if [ ! -d "$OBSIDIAN_BLOG_DIR" ]; then
    echo "❌ Error: Obsidian blog directory not found: $OBSIDIAN_BLOG_DIR"
    log "ERROR: Obsidian directory not found: $OBSIDIAN_BLOG_DIR"
    exit 1
fi

# Create posts directory if it doesn't exist
mkdir -p "$JEKYLL_POSTS_DIR"

# Track what we're doing
COPIED_COUNT=0
SKIPPED_COUNT=0
ERROR_COUNT=0

# Copy all markdown files from Obsidian blog to Jekyll posts
# Only copy files that have Jekyll front matter and pass validation
for file in "$OBSIDIAN_BLOG_DIR"/*.md; do
    if [ -f "$file" ]; then
        filename=$(basename "$file")
        
        # Validate file before copying
        if validate_file "$file"; then
            echo "✅ Copying: $filename"
            log "COPIED: $filename"
            cp "$file" "$JEKYLL_POSTS_DIR/"
            ((COPIED_COUNT++))
        else
            exit_code=$?
            if [[ $exit_code -eq 2 ]]; then
                # Date mismatch - critical error
                ((ERROR_COUNT++))
                echo "💀 CRITICAL: $filename has date inconsistency - manual review required"
            else
                # No front matter or other issues
                ((SKIPPED_COUNT++))
            fi
        fi
    fi
done

echo ""
echo "📊 Sync Summary:"
echo "   • Copied: $COPIED_COUNT posts"
echo "   • Skipped: $SKIPPED_COUNT files"
echo "   • Errors: $ERROR_COUNT files"
log "Sync completed - Copied: $COPIED_COUNT, Skipped: $SKIPPED_COUNT, Errors: $ERROR_COUNT"

# Stop if there are critical errors
if [ $ERROR_COUNT -gt 0 ]; then
    echo "💀 SYNC STOPPED: $ERROR_COUNT files have critical errors that must be fixed manually"
    log "ERROR: Sync stopped due to $ERROR_COUNT critical errors"
    echo "   Check the log file: $LOG_FILE"
    exit 1
fi

if [ $COPIED_COUNT -eq 0 ]; then
    echo "   • No posts to sync"
    log "No changes needed"
    exit 0
fi

if [ "$AUTO_PUBLISH" = true ]; then
    echo ""
    echo "🚀 Auto-publishing changes..."
    log "Starting auto-publish process"
    cd /Users/braydon/projects/dbmcco.github.io
    
    # Check if there are changes to commit
    if ! git diff --quiet || ! git diff --cached --quiet; then
        log "Changes detected, committing..."
        git add .
        git commit -m "Enhanced sync: $COPIED_COUNT posts updated

- Synced with validation and error checking
- Enhanced sync script with date validation
- Generated on $(date '+%Y-%m-%d %H:%M:%S')

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>"
        
        echo "📤 Pushing to GitHub..."
        log "Pushing to GitHub..."
        git push
        echo "✅ Blog updated! Check https://dbmcco.github.io in a few minutes."
        log "Successfully pushed to GitHub"
    else
        echo "   • No changes to publish"
        log "No git changes to publish"
    fi
else
    echo ""
    echo "📝 Next steps:"
    echo "   1. Review posts in $JEKYLL_POSTS_DIR"
    echo "   2. Run './sync-from-obsidian.sh --auto-publish' to auto-publish"
    echo "   3. Run with '--verbose' for detailed logging"
    echo "   4. Check sync.log for detailed operation history"
    echo "   5. Or manually: git add . && git commit && git push"
fi

log "Sync process completed successfully"