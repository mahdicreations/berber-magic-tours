import os
import re

base_dir = r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours"
duplicates = []
all_footer_blog_files = []

for root, dirs, files in os.walk(base_dir):
    if "scratch" in root or ".git" in root:
        continue
    for f in files:
        if f.endswith(".html"):
            filepath = os.path.join(root, f)
            with open(filepath, "r", encoding="utf-8", errors="ignore") as fh:
                content = fh.read()
            footer_match = re.search(r"<footer.*?</footer>", content, re.DOTALL)
            if footer_match:
                footer = footer_match.group(0)
                # find all blog links inside footer
                blog_links = re.findall(r"<li>\s*<a\s+href=[\"'][^\"']*blog[^\"']*[\"']>Blog</a>\s*</li>", footer, re.IGNORECASE)
                rel_path = os.path.relpath(filepath, base_dir)
                all_footer_blog_files.append((rel_path, len(blog_links), blog_links))
                if len(blog_links) > 1:
                    duplicates.append((rel_path, len(blog_links), blog_links))

print(f"Total HTML files checked: {len(all_footer_blog_files)}")
print(f"Total files with duplicated footer blog link: {len(duplicates)}")
print("\nFiles with duplicates:")
for path, count, links in duplicates:
    print(f"  {path}: {count} occurrences: {links}")
