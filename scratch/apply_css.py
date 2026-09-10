import os
import re

css_path = 'c:/Users/el mahdi/Desktop/mahdicreations/berber-magic-tours/assets/css/style.css'
content = open(css_path, 'r', encoding='utf-8').read()
original = content

# 1. Add --primary-dark to :root
if '--primary-dark' not in content:
    content = content.replace('--primary: #D36135;', '--primary: #D36135;\n    --primary-dark: #B84A22;')

# 2. Replace text color usages
content = re.sub(r'color:\s*var\(--primary\)', 'color: var(--primary-dark)', content)
# Ensure we don't break borders and backgrounds which might use color? No, color only affects text, borders use border-color. 
# But wait, what if SVG fill uses color via currentColor? That's fine, SVG can be darker too.

if content != original:
    open(css_path, 'w', encoding='utf-8').write(content)
    print("CSS updated successfully.")
else:
    print("No CSS updates required.")
