import os
import re

base_dir = r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours"

files_with_dup_links = {}

for root, dirs, files in os.walk(base_dir):
    if "scratch" in root or ".git" in root:
        continue
    for f in files:
        if f.endswith(".html"):
            filepath = os.path.join(root, f)
            with open(filepath, "r", encoding="utf-8", errors="ignore") as fh:
                content = fh.read()
            
            footer_match = re.search(r'<footer.*?</footer>', content, re.DOTALL)
            if not footer_match:
                continue
            footer = footer_match.group(0)
            
            # Find footer-links lists
            menu_matches = re.findall(r'<ul class=["\']footer-links["\']>(.*?)</ul>', footer, re.DOTALL)
            for m in menu_matches:
                items = re.findall(r'<li>\s*<a\s+[^>]*href=["\']([^"\']*)["\'][^>]*>(.*?)</a>\s*</li>', m, re.DOTALL)
                seen = set()
                dups = []
                for href, text in items:
                    clean_text = text.strip()
                    if clean_text in seen:
                        dups.append((clean_text, href))
                    else:
                        seen.add(clean_text)
                if dups:
                    rel_path = os.path.relpath(filepath, base_dir)
                    if rel_path not in files_with_dup_links:
                        files_with_dup_links[rel_path] = []
                    files_with_dup_links[rel_path].extend(dups)

print(f"Files with ANY duplicated link in footer menu: {len(files_with_dup_links)}")
for path, dups in files_with_dup_links.items():
    print(f"{path}: {dups}")
