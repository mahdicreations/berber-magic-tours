import os
import re

scripts = set()
styles = set()
fonts = set()
iframes = set()
images = set()

for root, _, files in os.walk('.'):
    if 'node_modules' in root or '.git' in root or 'scratch' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                content = f.read()
                for m in re.finditer(r'<script[^>]+src=["\']([^"\']+)["\']', content):
                    src = m.group(1)
                    if src.startswith('http') or src.startswith('//'):
                        scripts.add(src)
                for m in re.finditer(r'<link[^>]+href=["\']([^"\']+)["\'][^>]*rel=["\']stylesheet["\']', content):
                    href = m.group(1)
                    if href.startswith('http') or href.startswith('//'):
                        styles.add(href)
                for m in re.finditer(r'<link[^>]+href=["\']([^"\']+)["\'][^>]*rel=["\']preconnect["\']', content):
                    href = m.group(1)
                    if href.startswith('http') or href.startswith('//'):
                        fonts.add(href)
                for m in re.finditer(r'<iframe[^>]+src=["\']([^"\']+)["\']', content):
                    src = m.group(1)
                    if src.startswith('http') or src.startswith('//'):
                        iframes.add(src)
                for m in re.finditer(r'<img[^>]+src=["\']([^"\']+)["\']', content):
                    src = m.group(1)
                    if src.startswith('http') or src.startswith('//'):
                        images.add(src)

print('Scripts:', scripts)
print('Styles:', styles)
print('Preconnect/Fonts:', fonts)
print('Iframes:', iframes)
print('External Images:', images)
