import os, re, hashlib
from pathlib import Path

root = Path('.')

def file_hash(path, length=8):
    """Compute first N chars of SHA-256 hex hash of a file's contents."""
    h = hashlib.sha256(path.read_bytes()).hexdigest()
    return h[:length]

css_hash = file_hash(root / 'assets/css/style.css')
js_hash = file_hash(root / 'assets/js/main.js')

print(f"style.css hash: {css_hash}")
print(f"main.js hash:   {js_hash}")

# Find all HTML files that reference unversioned /assets/css/style.css or /assets/js/main.js
html_files = sorted(root.rglob('*.html'))
for html_file in html_files:
    if '.git' in str(html_file) or 'scratch' in str(html_file):
        continue
    content = html_file.read_text(encoding='utf-8', errors='ignore')
    found_css = re.search(r'href=["\'][^"\']*style\.css["\']', content)
    found_js = re.search(r'src=["\'][^"\']*main\.js["\']', content)
    if found_css or found_js:
        print(f"  {html_file}: css={bool(found_css)}, js={bool(found_js)}")
