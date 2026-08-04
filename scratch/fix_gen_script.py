import re

with open(r"scratch\generate_full_blog.py", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace('../assets/', '/assets/').replace('assets/', '/assets/').replace('//assets/', '/assets/')

with open(r"scratch\generate_full_blog.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated generate_full_blog.py paths.")
