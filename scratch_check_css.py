with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

print("File length:", len(css))
lines = [line for line in css.splitlines() if 'social' in line.lower() or 'tripadvisor' in line.lower()]
print(f"Found {len(lines)} lines with social or tripadvisor:")
for l in lines[:20]:
    print("  ", l)
