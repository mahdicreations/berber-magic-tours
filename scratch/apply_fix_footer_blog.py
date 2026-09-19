import os
import re

base_dir = r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours"

updated_count = 0

for root, dirs, files in os.walk(base_dir):
    if "scratch" in root or ".git" in root:
        continue
    for f in files:
        if f.endswith(".html"):
            filepath = os.path.join(root, f)
            with open(filepath, "r", encoding="utf-8") as fh:
                content = fh.read()
            
            # Match footer
            footer_match = re.search(r'<footer.*?</footer>', content, re.DOTALL)
            if not footer_match:
                continue
            
            orig_footer = footer_match.group(0)
            new_footer = orig_footer
            
            # Pattern 1: root duplicates
            # <li><a href="blog">Blog</a></li> followed by <li><a href="/blog">Blog</a></li>
            p1 = re.search(r'([ \t]*<li>\s*<a\s+href=["\']blog["\']>Blog</a>\s*</li>\r?\n)[ \t]*<li>\s*<a\s+href=["\']/blog["\']>Blog</a>\s*</li>\r?\n?', new_footer)
            if p1:
                new_footer = new_footer[:p1.start()] + p1.group(1) + new_footer[p1.end():]
                
            # Pattern 2: tour duplicates
            # <li><a href="../blog">Blog</a></li> followed by <li><a href="/blog">Blog</a></li>
            p2 = re.search(r'([ \t]*<li>\s*<a\s+href=["\']\.\./blog["\']>Blog</a>\s*</li>\r?\n)[ \t]*<li>\s*<a\s+href=["\']/blog["\']>Blog</a>\s*</li>\r?\n?', new_footer)
            if p2:
                new_footer = new_footer[:p2.start()] + p2.group(1) + new_footer[p2.end():]
                
            if new_footer != orig_footer:
                new_content = content[:footer_match.start()] + new_footer + content[footer_match.end():]
                with open(filepath, "w", encoding="utf-8") as fh:
                    fh.write(new_content)
                updated_count += 1

print(f"Successfully cleaned footer in {updated_count} HTML files.")
