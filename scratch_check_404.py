with open('404.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
print("=== 404.html TOP BAR SOCIALS ===")
m_head = re.search(r'<div class="top-bar-socials">([\s\S]*?)</div>', html)
if m_head:
    print(m_head.group(0))
else:
    print("No top-bar-socials in 404.html!")

print("\n=== 404.html FOOTER SOCIALS ===")
m_foot = re.search(r'<div class="social-links[^"]*">([\s\S]*?)</div>', html)
if m_foot:
    print(m_foot.group(0))
else:
    print("No footer socials in 404.html!")
