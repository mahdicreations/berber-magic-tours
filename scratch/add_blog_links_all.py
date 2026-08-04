import os
import re

base_dir = r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours"
tours_dir = os.path.join(base_dir, "tours")

# 1. Update Root HTML Files
root_files_updated = 0
for filename in os.listdir(base_dir):
    if filename.endswith(".html"):
        filepath = os.path.join(base_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        changed = False

        # Header Nav update (add Blog if not present)
        # Search for: <li><a href="morocco-tours">Morocco Tours</a></li>\n                        </ul>\n                    </li>
        if 'href="blog"' not in content:
            # Insert Blog in Header nav list right after Other Tours dropdown closes or inside nav-list
            target_nav = '<li><a href="morocco-tours">Morocco Tours</a></li>\n                        </ul>\n                    </li>'
            replacement_nav = '<li><a href="morocco-tours">Morocco Tours</a></li>\n                        </ul>\n                    </li>\n                    <li><a href="blog">Blog</a></li>'
            
            if target_nav in content:
                content = content.replace(target_nav, replacement_nav)
                changed = True

            # Insert Blog in Mobile Nav list
            target_mobile = '<li><a href="morocco-tours">Morocco Tours</a></li>'
            replacement_mobile = '<li><a href="morocco-tours">Morocco Tours</a></li>\n            <li><a href="blog">Blog</a></li>'
            if target_mobile in content and '<li><a href="blog">Blog</a></li>' not in content:
                content = content.replace(target_mobile, replacement_mobile)
                changed = True

            # Insert Blog in Footer Menu links
            target_footer = '<li><a href="morocco-tours">Morocco Tours</a></li>'
            replacement_footer = '<li><a href="morocco-tours">Morocco Tours</a></li>\n                        <li><a href="blog">Blog</a></li>'
            if target_footer in content and '<li><a href="blog">Blog</a></li>' not in content:
                content = content.replace(target_footer, replacement_footer)
                changed = True

        if changed:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            root_files_updated += 1

print(f"Updated {root_files_updated} root HTML files with Blog links.")

# 2. Update Tours Subdirectory HTML Files
tour_files_updated = 0
for filename in os.listdir(tours_dir):
    if filename.endswith(".html"):
        filepath = os.path.join(tours_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        changed = False

        if 'href="../blog"' not in content and 'href="blog"' not in content:
            # Header Nav insertion
            target_nav = '<li><a href="../morocco-tours">Morocco Tours</a></li>\n                        </ul>\n                    </li>'
            replacement_nav = '<li><a href="../morocco-tours">Morocco Tours</a></li>\n                        </ul>\n                    </li>\n                    <li><a href="../blog">Blog</a></li>'
            
            if target_nav in content:
                content = content.replace(target_nav, replacement_nav)
                changed = True

            # Mobile Nav insertion
            target_mobile = '<li><a href="../morocco-tours">Morocco Tours</a></li>'
            replacement_mobile = '<li><a href="../morocco-tours">Morocco Tours</a></li>\n            <li><a href="../blog">Blog</a></li>'
            if target_mobile in content and '<li><a href="../blog">Blog</a></li>' not in content:
                content = content.replace(target_mobile, replacement_mobile)
                changed = True

            # Footer links insertion
            target_footer = '<li><a href="../morocco-tours">Morocco Tours</a></li>'
            replacement_footer = '<li><a href="../morocco-tours">Morocco Tours</a></li>\n                        <li><a href="../blog">Blog</a></li>'
            if target_footer in content and '<li><a href="../blog">Blog</a></li>' not in content:
                content = content.replace(target_footer, replacement_footer)
                changed = True

        if changed:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            tour_files_updated += 1

print(f"Updated {tour_files_updated} tour HTML files with Blog links.")
