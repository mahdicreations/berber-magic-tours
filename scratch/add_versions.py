import os, re, hashlib
from pathlib import Path

root = Path('.')

def file_hash(path, length=8):
    h = hashlib.sha256(path.read_bytes()).hexdigest()
    return h[:length]

css_hash = file_hash(root / 'assets/css/style.css')
js_hash  = file_hash(root / 'assets/js/main.js')

print(f"Adding ?v={css_hash} to style.css and ?v={js_hash} to main.js")

html_files = sorted(root.rglob('*.html'))
updated = 0
for html_file in html_files:
    if '.git' in str(html_file) or 'scratch' in str(html_file):
        continue
    content = html_file.read_text(encoding='utf-8', errors='ignore')
    original = content

    # Replace /assets/css/style.css (with or without existing ?v=...)
    content = re.sub(
        r'(/assets/css/style\.css)(\?v=[^"\']*)?',
        f'/assets/css/style.css?v={css_hash}',
        content
    )
    # Replace /assets/js/main.js (with or without existing ?v=...)
    content = re.sub(
        r'(/assets/js/main\.js)(\?v=[^"\']*)?',
        f'/assets/js/main.js?v={js_hash}',
        content
    )

    if content != original:
        html_file.write_text(content, encoding='utf-8')
        updated += 1

print(f"Updated {updated} HTML files with versioned asset references.")
