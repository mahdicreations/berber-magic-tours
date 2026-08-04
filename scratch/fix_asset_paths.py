import os
import re

base_dir = r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours"

def fix_content_assets(content):
    # Replace href="../assets/" or href="assets/" with href="/assets/"
    content = re.sub(r'href=["\'](?:\.\./)?assets/', 'href="/assets/', content)
    # Replace src="../assets/" or src="assets/" with src="/assets/"
    content = re.sub(r'src=["\'](?:\.\./)?assets/', 'src="/assets/', content)
    # Replace url('../assets/') or url('assets/') or url(../assets/) or url(assets/)
    content = re.sub(r'url\(["\']?(?:\.\./)?assets/', 'url("/assets/', content)
    return content

files_fixed = 0

for root, dirs, files in os.walk(base_dir):
    # Skip scratch and git folders
    if "scratch" in root or ".git" in root:
        continue
    for f in files:
        if f.endswith(".html"):
            filepath = os.path.join(root, f)
            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()
            
            new_content = fix_content_assets(content)
            if new_content != content:
                with open(filepath, "w", encoding="utf-8") as file:
                    file.write(new_content)
                files_fixed += 1

print(f"Fixed asset paths in {files_fixed} HTML files.")
