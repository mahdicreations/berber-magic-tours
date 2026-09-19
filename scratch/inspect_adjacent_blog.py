import os
import re

base_dir = r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours"
files_to_check = []

for root, dirs, files in os.walk(base_dir):
    if "scratch" in root or ".git" in root:
        continue
    for f in files:
        if f.endswith(".html"):
            filepath = os.path.join(root, f)
            with open(filepath, "r", encoding="utf-8", errors="ignore") as fh:
                content = fh.read()
            
            # Look for adjacent blog links
            matches = re.findall(r'((?:[^\n]*blog[^\n]*\n){2,4})', content, re.IGNORECASE)
            if matches:
                files_to_check.append((os.path.relpath(filepath, base_dir), matches))

print(f"Files with adjacent blog links: {len(files_to_check)}")
for path, m in files_to_check[:10]:
    print(f"--- {path} ---")
    for block in m:
        print(block.strip())
