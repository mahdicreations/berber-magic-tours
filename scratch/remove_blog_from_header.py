import os
import re

base_dir = r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours"
tours_dir = os.path.join(base_dir, "tours")

def clean_header_nav(content, is_tour=False):
    # Regex to match <li><a href="..." ...>Blog</a></li> inside nav-list or mobile-nav-list
    # Pattern: <li><a href="(?:\.\./)?blog"[^>]*>Blog</a></li>
    
    # We want to remove it ONLY if it is inside <nav> or <div class="mobile-menu">, NOT inside <footer...
    
    # Split content into body/header part and footer part
    footer_idx = content.find('<footer')
    if footer_idx != -1:
        header_part = content[:footer_idx]
        footer_part = content[footer_idx:]
    else:
        header_part = content
        footer_part = ""

    # Remove blog link from header part
    blog_link_pattern = re.compile(r'\s*<li><a\s+href="(?:\.\./)?blog"\s*[^>]*>Blog</a></li>', re.IGNORECASE)
    cleaned_header = blog_link_pattern.sub('', header_part)

    return cleaned_header + footer_part

# Process root files
root_count = 0
for filename in os.listdir(base_dir):
    if filename.endswith(".html"):
        filepath = os.path.join(base_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        new_content = clean_header_nav(content, is_tour=False)
        if new_content != content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            root_count += 1

print(f"Removed Blog from header in {root_count} root files.")

# Process tour files
tour_count = 0
for filename in os.listdir(tours_dir):
    if filename.endswith(".html"):
        filepath = os.path.join(tours_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        new_content = clean_header_nav(content, is_tour=True)
        if new_content != content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            tour_count += 1

print(f"Removed Blog from header in {tour_count} tour files.")
