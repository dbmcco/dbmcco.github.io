#!/usr/bin/env python3
"""
Substack to Jekyll Migration Script
Fetches public Substack posts and converts them to Jekyll-compatible markdown
"""

import requests
import re
import html2text
import os
from datetime import datetime
from urllib.parse import urljoin, urlparse
import json

class SubstackMigrator:
    def __init__(self, substack_url, output_dir):
        self.substack_url = substack_url.rstrip('/')
        self.output_dir = output_dir
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })
        
    def fetch_post_content(self, post_url):
        """Fetch full content of a Substack post"""
        try:
            response = self.session.get(post_url)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"❌ Error fetching {post_url}: {e}")
            return None
    
    def extract_post_data(self, html_content, post_url):
        """Extract post data from HTML"""
        # Extract title
        title_match = re.search(r'<title>(.*?)</title>', html_content, re.IGNORECASE)
        title = title_match.group(1).strip() if title_match else "Untitled"
        title = title.replace(' - by Braydon McCormick', '').strip()
        
        # Extract publication date
        date_match = re.search(r'"datePublished":"([^"]+)"', html_content)
        if date_match:
            pub_date = datetime.fromisoformat(date_match.group(1).replace('Z', '+00:00'))
        else:
            pub_date = datetime.now()
        
        # Extract main content
        content_pattern = r'<div[^>]*class="[^"]*available-content[^"]*"[^>]*>(.*?)</div>(?=\s*<div[^>]*class="[^"]*subscription-widget)'
        content_match = re.search(content_pattern, html_content, re.DOTALL | re.IGNORECASE)
        
        if not content_match:
            # Fallback pattern
            content_pattern = r'<div[^>]*class="[^"]*post-content[^"]*"[^>]*>(.*?)</div>'
            content_match = re.search(content_pattern, html_content, re.DOTALL | re.IGNORECASE)
        
        content = content_match.group(1) if content_match else ""
        
        # Extract categories/tags from content
        categories = ["substack", "ai", "life-sciences"]
        if "ChatGPT" in title or "ChatGPT" in content:
            categories.append("chatgpt")
        if "compliance" in title.lower() or "compliance" in content.lower():
            categories.append("compliance")
        if "MedComm" in content:
            categories.append("medcomm")
            
        return {
            'title': title,
            'date': pub_date,
            'content': content,
            'categories': categories,
            'url': post_url
        }
    
    def convert_to_markdown(self, html_content):
        """Convert HTML content to Markdown"""
        # Configure html2text
        h = html2text.HTML2Text()
        h.ignore_links = False
        h.ignore_images = False
        h.ignore_emphasis = False
        h.body_width = 0  # Don't wrap lines
        h.unicode_snob = True
        
        # Clean up HTML before conversion
        html_content = re.sub(r'<div[^>]*class="[^"]*captioned-image[^"]*"[^>]*>.*?</div>', '', html_content, flags=re.DOTALL)
        html_content = re.sub(r'<div[^>]*class="[^"]*subscription-widget[^"]*"[^>]*>.*?</div>', '', html_content, flags=re.DOTALL)
        
        markdown = h.handle(html_content)
        
        # Clean up markdown
        markdown = re.sub(r'\n\s*\n\s*\n', '\n\n', markdown)  # Remove excessive newlines
        markdown = markdown.strip()
        
        return markdown
    
    def create_jekyll_post(self, post_data):
        """Create Jekyll-compatible markdown post"""
        # Generate filename
        date_str = post_data['date'].strftime('%Y-%m-%d')
        title_slug = re.sub(r'[^\w\s-]', '', post_data['title'].lower())
        title_slug = re.sub(r'[-\s]+', '-', title_slug).strip('-')
        filename = f"{date_str}-{title_slug}.md"
        
        # Create front matter
        front_matter = f"""---
layout: post
title: "{post_data['title']}"
date: {post_data['date'].strftime('%Y-%m-%d %H:%M:%S')} -0500
categories: {' '.join(post_data['categories'])}
tags: [substack-import, ai, life-sciences]
original_url: {post_data['url']}
---

"""
        
        # Convert content to markdown
        markdown_content = self.convert_to_markdown(post_data['content'])
        
        # Add migration note
        migration_note = f"""
---

*Originally published on [Substack]({post_data['url']}) on {post_data['date'].strftime('%B %d, %Y')}. Migrated to this blog on {datetime.now().strftime('%B %d, %Y')}.*
"""
        
        full_content = front_matter + markdown_content + migration_note
        
        return filename, full_content
    
    def migrate_posts(self):
        """Main migration function"""
        print(f"🔄 Starting Substack migration from {self.substack_url}")
        
        # Known posts from the Substack (since we can see them)
        posts = [
            {
                'url': f"{self.substack_url}/p/is-lifescience-compliance-ready-for",
                'date': '2023-06-12'
            },
            {
                'url': f"{self.substack_url}/p/transforming-medcomm-with-ai", 
                'date': '2023-06-14'
            },
            {
                'url': f"{self.substack_url}/p/expanded-llms-in-life-science-and",
                'date': '2023-07-18'
            }
        ]
        
        migrated = 0
        os.makedirs(self.output_dir, exist_ok=True)
        
        for post_info in posts:
            print(f"\n📄 Processing: {post_info['url']}")
            
            html_content = self.fetch_post_content(post_info['url'])
            if not html_content:
                continue
                
            post_data = self.extract_post_data(html_content, post_info['url'])
            filename, jekyll_content = self.create_jekyll_post(post_data)
            
            # Save to Obsidian blog directory
            output_path = os.path.join(self.output_dir, filename)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(jekyll_content)
            
            print(f"✅ Saved: {filename}")
            migrated += 1
        
        print(f"\n🎉 Migration complete! Migrated {migrated} posts to {self.output_dir}")
        print(f"📝 Next steps:")
        print(f"   1. Review posts in Obsidian: {self.output_dir}")
        print(f"   2. Run: ./sync-from-obsidian.sh --auto-publish")
        print(f"   3. Check your blog: https://dbmcco.github.io")

if __name__ == "__main__":
    # Configuration
    SUBSTACK_URL = "https://dbmcco.substack.com"
    OUTPUT_DIR = "/Users/braydon/Obsidian/bvault/blog"
    
    # Run migration
    migrator = SubstackMigrator(SUBSTACK_URL, OUTPUT_DIR)
    migrator.migrate_posts()