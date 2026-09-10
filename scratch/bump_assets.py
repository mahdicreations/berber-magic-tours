import os
from pathlib import Path
import re
import hashlib

workspace = Path('c:/Users/el mahdi/Desktop/mahdicreations/berber-magic-tours')

def get_hash(filepath):
    h = hashlib.md5()
    h.update(filepath.read_bytes())
    return h.hexdigest()[:8]

css_hash = get_hash(workspace / 'assets/css/style.css')
js_hash = get_hash(workspace / 'assets/js/main.js')

updated = 0
for html_file in workspace.rglob('*.html'):
    if '.git' in str(html_file) or 'scratch' in str(html_file):
        continue
        
    try:
        content = html_file.read_text(encoding='utf-8', errors='ignore')
        original = content
        
        # Replace CSS version
        content = re.sub(r'style\.css\?v=[a-z0-9]+', f'style.css?v={css_hash}', content)
        # Replace JS version
        content = re.sub(r'main\.js\?v=[a-z0-9]+', f'main.js?v={js_hash}', content)
        
        if content != original:
            html_file.write_text(content, encoding='utf-8')
            updated += 1
            
    except Exception as e:
        print(e)

print(f"Asset versions bumped in {updated} files.")
