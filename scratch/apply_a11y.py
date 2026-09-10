import os
from pathlib import Path
import re

root = Path('.')

def process_html_file(file_path):
    try:
        content = file_path.read_text(encoding='utf-8', errors='ignore')
        original = content

        # 1. ARIA Labels for Buttons
        content = content.replace('<button class="mobile-menu-btn">', '<button class="mobile-menu-btn" aria-label="Open mobile menu" aria-expanded="false" aria-controls="mobile-nav">')
        content = content.replace('<button class="close-menu-btn">', '<button class="close-menu-btn" aria-label="Close mobile menu">')
        content = content.replace('<button class="slider-arrow prev">', '<button type="button" class="slider-arrow prev" aria-label="Previous slide">')
        content = content.replace('<button class="slider-arrow next">', '<button type="button" class="slider-arrow next" aria-label="Next slide">')
        
        # 2. Fix Dropdown Toggle (remove inline onclick, add ARIA)
        content = content.replace(
            '<button type="button" class="mobile-dropdown-toggle" onclick="toggleMobileSubmenu(this)">',
            '<button type="button" class="mobile-dropdown-toggle" aria-expanded="false" aria-label="Toggle submenu">'
        )
        # Handle cases where onclick might be missing or different
        content = re.sub(
            r'<button\s+type="button"\s+class="mobile-dropdown-toggle"\s*>',
            '<button type="button" class="mobile-dropdown-toggle" aria-expanded="false" aria-label="Toggle submenu">',
            content
        )
        
        # 3. Change Slider Dots to Buttons (for keyboard focus)
        content = re.sub(
            r'<span class="dot( active)?" data-index="(\d+)"></span>',
            r'<button type="button" class="dot\1" data-index="\2" aria-label="Go to slide \2"></button>',
            content
        )

        # 4. Heading Structure (index.html only)
        if file_path.name == 'index.html':
            content = content.replace('<h1 class="slide-title">', '<h2 class="slide-title">')
            content = content.replace('<h2 class="section-title">Experience Morocco Through Local Eyes</h2>', '<h1 class="section-title">Experience Morocco Through Local Eyes</h1>')

        # 5. Add Blog to Global Navigation (Desktop)
        # Look for the Contact Us list item to insert Blog before it, or after "Morocco Tours".
        # Let's insert after Morocco Tours: <li><a href="morocco-tours">Morocco Tours</a></li>
        if '<li><a href="blog" class="active">Blog</a></li>' not in content and '<li><a href="blog">Blog</a></li>' not in content and '<li><a href="../blog">Blog</a></li>' not in content:
            prefix = '../' if (file_path.parent.name in ['tours', 'blog']) else ''
            
            # Desktop Nav
            desktop_morocco = f'<li><a href="{prefix}morocco-tours">Morocco Tours</a></li>'
            desktop_morocco_active = f'<li><a href="{prefix}morocco-tours" class="active">Morocco Tours</a></li>'
            
            blog_desktop = f'<li><a href="{prefix}blog">Blog</a></li>'
            if file_path.name == 'blog.html':
                blog_desktop = f'<li><a href="{prefix}blog" class="active">Blog</a></li>'

            content = content.replace(desktop_morocco, f'{desktop_morocco}\n                        {blog_desktop}')
            content = content.replace(desktop_morocco_active, f'{desktop_morocco_active}\n                        {blog_desktop}')
            
            # Mobile Nav
            mobile_morocco = f'<li><a href="{prefix}morocco-tours">Morocco Tours</a></li>'
            blog_mobile = f'<li><a href="{prefix}blog">Blog</a></li>'
            if file_path.name == 'blog.html':
                blog_mobile = f'<li><a href="{prefix}blog" class="active">Blog</a></li>'
                
            # Mobile nav replacement requires careful regex or split, but since it's the same string, it might replace both if they are identical.
            # Actually, the strings are identical for desktop and mobile. The replacement above will hit both!

        # Write back if changed
        if content != original:
            file_path.write_text(content, encoding='utf-8')
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

updated_files = 0
for html_file in root.rglob('*.html'):
    if '.git' in str(html_file) or 'scratch' in str(html_file):
        continue
    if process_html_file(html_file):
        updated_files += 1

print(f"A11y ARIA and Blog links applied to {updated_files} HTML files.")
