import os
import re

tag_code = """    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-CTF6X8R87Z"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'G-CTF6X8R87Z');
    </script>"""

count = 0
skipped = 0
no_head = 0

for root, dirs, files in os.walk('.'):
    if '.git' in root or 'node_modules' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            if 'G-CTF6X8R87Z' in content:
                skipped += 1
                continue
            
            if '<head>' in content:
                new_content = content.replace('<head>', '<head>\n' + tag_code, 1)
            elif re.search(r'<head[^>]*>', content, re.IGNORECASE):
                new_content = re.sub(r'(<head[^>]*>)', r'\1\n' + tag_code, content, count=1, flags=re.IGNORECASE)
            else:
                print(f"WARNING: No <head> tag found in {filepath}")
                no_head += 1
                continue
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1

print(f"Update summary: Updated {count} files, Skipped {skipped} files, Missing head {no_head} files.")
