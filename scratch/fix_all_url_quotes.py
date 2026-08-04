import os
import re

base_dir = r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours"

fixed_files = 0
for root, dirs, files in os.walk(base_dir):
    if "scratch" in root or ".git" in root:
        continue
    for f in files:
        if f.endswith(".html"):
            filepath = os.path.join(root, f)
            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()
            
            # Replace url("/assets/...'); or url('/assets/..."); or url("assets/...') with url('/assets/...')
            new_content = re.sub(r'url\(["\']?/(assets/[^"\']+)["\']?\)', r"url('/\1')", content)
            
            # Also catch any remaining url("/assets/...
            new_content = re.sub(r'url\("(/assets/[^"\']+)\'\)', r"url('\1')", new_content)
            new_content = re.sub(r'url\(\'(/assets/[^"\']+)"\)', r"url('\1')", new_content)
            
            if new_content != content:
                with open(filepath, "w", encoding="utf-8") as file:
                    file.write(new_content)
                fixed_files += 1

print(f"Cleaned up background-image URL quotes in {fixed_files} files.")
