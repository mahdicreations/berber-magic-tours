with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
print("=== CSS FILES ===")
for m in re.finditer(r'<link[^>]+rel=["\']stylesheet["\'][^>]*>', html):
    print(m.group(0))

print("\n=== TOP BAR SOCIALS ===")
m_head = re.search(r'<div class="top-bar-socials">([\s\S]*?)</div>', html)
if m_head:
    print(m_head.group(0))

print("\n=== FOOTER SOCIALS ===")
m_foot = re.search(r'<div class="social-links[^"]*">([\s\S]*?)</div>', html)
if m_foot:
    print(m_foot.group(0))
