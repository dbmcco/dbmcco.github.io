#!/usr/bin/env python3
"""
WordPress to Jekyll Migration Script
Converts WordPress XML export to Jekyll-compatible markdown files
"""

import xml.etree.ElementTree as ET
import html2text
import re
import os
from datetime import datetime
import argparse

class WordPressMigrator:
    def __init__(self, xml_file, output_dir):
        self.xml_file = xml_file
        self.output_dir = output_dir
        self.h = html2text.HTML2Text()
        self.h.ignore_links = False
        self.h.ignore_images = False
        self.h.body_width = 0
        self.h.unicode_snob = True
        
    def parse_wordpress_xml(self):
        """Parse WordPress XML export file"""
        try:
            tree = ET.parse(self.xml_file)
            root = tree.getroot()
            
            # Find the namespace
            ns = {'content': 'http://purl.org/rss/1.0/modules/content/',
                  'wp': 'http://wordpress.org/export/1.2/'}
            
            posts = []
            for item in root.findall('.//item'):
                post_type = item.find('.//wp:post_type', ns)
                post_status = item.find('.//wp:status', ns)
                
                # Only process published posts
                if (post_type is not None and post_type.text == 'post' and
                    post_status is not None and post_status.text == 'publish'):
                    
                    post_data = self.extract_post_data(item, ns)
                    if post_data:
                        posts.append(post_data)
            
            return posts
            
        except ET.ParseError as e:
            print(f"❌ Error parsing XML: {e}")
            return []
        except Exception as e:
            print(f"❌ Error: {e}")
            return []
    
    def extract_post_data(self, item, ns):
        """Extract post data from XML item"""
        try:
            title = item.find('title').text or "Untitled"
            
            # Get publication date
            pub_date_str = item.find('pubDate').text
            pub_date = datetime.strptime(pub_date_str, '%a, %d %b %Y %H:%M:%S %z')
            
            # Get content
            content_elem = item.find('.//content:encoded', ns)
            content = content_elem.text if content_elem is not None else ""
            
            # Get excerpt
            excerpt_elem = item.find('.//wp:post_excerpt', ns)
            excerpt = excerpt_elem.text if excerpt_elem is not None else ""
            
            # Get categories and tags
            categories = []
            tags = []
            
            for category in item.findall('category'):
                domain = category.get('domain')
                term = category.text
                if domain == 'category':
                    categories.append(term)
                elif domain == 'post_tag':
                    tags.append(term)
            
            # Get post slug
            slug_elem = item.find('.//wp:post_name', ns)
            slug = slug_elem.text if slug_elem is not None else ""
            
            return {
                'title': title,
                'date': pub_date,
                'content': content,
                'excerpt': excerpt,
                'categories': categories,
                'tags': tags,
                'slug': slug
            }
            
        except Exception as e:
            print(f"❌ Error extracting post data: {e}")
            return None
    
    def convert_to_markdown(self, html_content):
        """Convert HTML content to Markdown"""
        if not html_content:
            return ""
            
        # Clean up WordPress-specific shortcodes
        html_content = re.sub(r'\[caption[^\]]*\](.*?)\[/caption\]', r'\1', html_content, flags=re.DOTALL)
        html_content = re.sub(r'\[/?[a-zA-Z][^\]]*\]', '', html_content)
        
        # Convert to markdown
        markdown = self.h.handle(html_content)
        
        # Clean up markdown
        markdown = re.sub(r'\n\s*\n\s*\n', '\n\n', markdown)
        markdown = markdown.strip()
        
        return markdown
    
    def create_jekyll_post(self, post_data):
        """Create Jekyll-compatible markdown post"""
        # Generate filename
        date_str = post_data['date'].strftime('%Y-%m-%d')
        
        if post_data['slug']:
            title_slug = post_data['slug']
        else:
            title_slug = re.sub(r'[^\w\s-]', '', post_data['title'].lower())
            title_slug = re.sub(r'[-\s]+', '-', title_slug).strip('-')
        
        filename = f"{date_str}-{title_slug}.md"
        
        # Prepare categories and tags
        categories = ' '.join(post_data['categories']) if post_data['categories'] else 'wordpress-import'
        tags_list = post_data['tags'] + ['wordpress-import']
        
        # Create front matter
        front_matter = f"""---
layout: post
title: "{post_data['title']}"
date: {post_data['date'].strftime('%Y-%m-%d %H:%M:%S')} -0500
categories: {categories}
tags: {tags_list}
---

"""
        
        # Convert content to markdown
        markdown_content = self.convert_to_markdown(post_data['content'])
        
        # Add excerpt if available
        if post_data['excerpt']:
            excerpt_md = self.convert_to_markdown(post_data['excerpt'])
            if excerpt_md and excerpt_md != markdown_content[:len(excerpt_md)]:
                markdown_content = f"*{excerpt_md}*\n\n" + markdown_content
        
        # Add migration note
        migration_note = f"""

---

*Originally published on WordPress on {post_data['date'].strftime('%B %d, %Y')}. Migrated to this blog on {datetime.now().strftime('%B %d, %Y')}.*
"""
        
        full_content = front_matter + markdown_content + migration_note
        
        return filename, full_content
    
    def migrate_posts(self):
        """Main migration function"""
        print(f"🔄 Starting WordPress migration from {self.xml_file}")
        
        # Parse WordPress XML
        posts = self.parse_wordpress_xml()
        if not posts:
            print("❌ No posts found to migrate")
            return
        
        print(f"📄 Found {len(posts)} posts to migrate")
        
        # Create output directory
        os.makedirs(self.output_dir, exist_ok=True)
        
        migrated = 0
        for post_data in posts:
            try:
                filename, jekyll_content = self.create_jekyll_post(post_data)
                
                # Save to output directory
                output_path = os.path.join(self.output_dir, filename)
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(jekyll_content)
                
                print(f"✅ Migrated: {post_data['title']} → {filename}")
                migrated += 1
                
            except Exception as e:
                print(f"❌ Error migrating post '{post_data['title']}': {e}")
        
        print(f"\n🎉 Migration complete! Migrated {migrated} posts to {self.output_dir}")
        print(f"📝 Next steps:")
        print(f"   1. Review posts in Obsidian: {self.output_dir}")
        print(f"   2. Run: ./sync-from-obsidian.sh --auto-publish")
        print(f"   3. Check your blog: https://dbmcco.github.io")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Migrate WordPress XML export to Jekyll')
    parser.add_argument('xml_file', help='Path to WordPress XML export file')
    parser.add_argument('--output', '-o', default='/Users/braydon/Obsidian/bvault/blog',
                       help='Output directory for Jekyll posts')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.xml_file):
        print(f"❌ Error: XML file not found: {args.xml_file}")
        exit(1)
    
    migrator = WordPressMigrator(args.xml_file, args.output)
    migrator.migrate_posts()