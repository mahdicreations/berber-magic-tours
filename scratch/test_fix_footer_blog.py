import os
import re

base_dir = r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours"

files_to_fix = []

for root, dirs, files in os.walk(base_dir):
    if "scratch" in root or ".git" in root:
        continue
    for f in files:
        if f.endswith(".html"):
            filepath = os.path.join(root, f)
            with open(filepath, "r", encoding="utf-8", errors="ignore") as fh:
                content = fh.read()
            
            # Match footer
            footer_match = re.search(r'<footer.*?</footer>', content, re.DOTALL)
            if not footer_match:
                continue
            footer = footer_match.group(0)
            
            # Check for duplicated blog in footer
            # Pattern 1: href="blog" followed by href="/blog"
            p1 = re.search(r'([ \t]*<li>\s*<a\s+href=["\']blog["\']>Blog</a>\s*</li>\r?\n)([ \t]*<li>\s*<a\s+href=["\']/blog["\']>Blog</a>\s*</li>\r?\n?)', footer)
            # Pattern 2: href="../blog" followed by href="/blog"
            p2 = re.search(r'([ \t]*<li>\s*<a\s+href=["\']\.\./blog["\']>Blog</a>\s*</li>\r?\n)([ \t]*<li>\s*<a\s+href=["\']/blog["\']>Blog</a>\s*</li>\r?\n?)', footer)
            # Pattern 3: any duplicate blog link
            all_blogs = re.findall(r'[ \t]*<li>\s*<a\s+href=["\'][^"\']*blog[^"\']*["\'][^>]*>Blog</a>\s*</li>', footer)
            
            rel_path = os.path.relpath(filepath, base_dir)
            if p1:
                files_to_fix.append((filepath, rel_path, "root_dup", p1.group(0), p1.group(1)))
            elif p2:
                files_to_fix.append((filepath, rel_path, "tour_dup", p2.group(0), p2.group(1)))
            elif len(all_blogs) > 1:
                files_to_fix.append((filepath, rel_path, "other_dup", None, None))

print(f"Total files detected for fix: {len(files_to_fix)}")
types = {}
for item in files_to_fix:
    types[item[2]] = types.get(item[2], 0) + 1
print(f"By type: {types}")
