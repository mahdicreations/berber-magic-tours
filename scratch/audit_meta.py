import os, re
from pathlib import Path

root = Path('.')
results = []

for html_file in sorted(root.rglob('*.html')):
    if '.git' in str(html_file) or 'scratch' in str(html_file) or 'node_modules' in str(html_file):
        continue
    
    content = html_file.read_text(encoding='utf-8', errors='ignore')
    
    # Title
    m = re.search(r'<title>(.*?)</title>', content, re.DOTALL)
    title = m.group(1).strip() if m else ''
    
    # Meta description
    m = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', content, re.DOTALL)
    desc = m.group(1).strip() if m else ''
    
    # H1
    m = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.DOTALL)
    h1_raw = m.group(1).strip() if m else ''
    h1 = re.sub(r'<[^>]+>', '', h1_raw).strip()
    
    # Canonical
    m = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\'](.*?)["\']', content)
    canonical = m.group(1).strip() if m else ''
    
    # Check for "Other Tours" pointing to #
    has_dead_link = bool(re.search(r'href=["\']#["\'][^>]*>Other Tours', content))
    
    results.append({
        'file': str(html_file),
        'title': title,
        'title_len': len(title),
        'desc': desc,
        'desc_len': len(desc),
        'h1': h1,
        'canonical': canonical,
        'dead_nav': has_dead_link,
    })

print(f"{'FILE':<55} {'TITLE LEN':>9} {'DESC LEN':>8} {'H1?':>4} {'DEAD?':>5}")
print("-" * 90)
for r in results:
    flag_t = '!' if r['title_len'] > 60 else ' '
    flag_d = '!' if r['desc_len'] > 160 or r['desc_len'] < 50 else ' '
    flag_h = 'Y' if r['h1'] else 'N'
    flag_n = 'X' if r['dead_nav'] else ' '
    print(f"{r['file']:<55} {flag_t}{r['title_len']:>8} {flag_d}{r['desc_len']:>7} {flag_h:>4} {flag_n:>5}")

print("\n=== TITLES > 60 chars ===")
for r in results:
    if r['title_len'] > 60:
        print(f"  [{r['title_len']}] {r['file']}")
        print(f"       {r['title']}")

print("\n=== DESCRIPTIONS > 160 or < 50 chars ===")
for r in results:
    if r['desc_len'] > 160 or (r['desc_len'] < 50 and r['desc_len'] > 0):
        print(f"  [{r['desc_len']}] {r['file']}")
        print(f"       {r['desc']}")

print("\n=== DEAD NAVIGATION (href='#') ===")
for r in results:
    if r['dead_nav']:
        print(f"  {r['file']}")
