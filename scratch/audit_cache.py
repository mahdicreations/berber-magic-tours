import os, re
from pathlib import Path

root = Path('.')
versioned_assets = []
unversioned_assets = []

# Check all HTML files for asset references
for html_file in sorted(root.rglob('*.html')):
    if '.git' in str(html_file) or 'scratch' in str(html_file):
        continue
    content = html_file.read_text(encoding='utf-8', errors='ignore')
    
    # Find JS and CSS references
    for m in re.finditer(r'(src|href)=["\']([^"\']+\.(js|css|woff2?|ttf|eot))["\']', content):
        url = m.group(2)
        if url.startswith('http') or url.startswith('//'):
            continue
        if '?' in url:
            versioned_assets.append((str(html_file), url))
        else:
            unversioned_assets.append((str(html_file), url))

print("=== VERSIONED ASSETS (have ?v= or ?hash=) ===")
for f, u in versioned_assets:
    print(f"  [{f}] {u}")

print("\n=== UNVERSIONED ASSETS (no query string) ===")
seen = set()
for f, u in unversioned_assets:
    if u not in seen:
        seen.add(u)
        print(f"  {u}")

# Check current asset sizes
print("\n=== LOCAL STATIC FILES ===")
for ext in ['.js', '.css']:
    for p in root.rglob(f'*{ext}'):
        if '.git' in str(p) or 'scratch' in str(p) or 'node_modules' in str(p):
            continue
        print(f"  {p} ({p.stat().st_size // 1024}KB)")
