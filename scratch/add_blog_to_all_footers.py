import os

base_dir = r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours"

updated_count = 0

for root, dirs, files in os.walk(base_dir):
    if "scratch" in root or ".git" in root:
        continue
    for f in files:
        if f.endswith(".html"):
            filepath = os.path.join(root, f)
            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()
            
            # Check if blog link is missing in footer
            if 'class="footer-links"' in content and 'href="/blog"' not in content and 'href="blog"' not in content:
                # Insert Blog link before Contact Us link in footer
                if '<li><a href="/contact">Contact Us</a></li>' in content:
                    content = content.replace(
                        '<li><a href="/contact">Contact Us</a></li>',
                        '<li><a href="/blog">Blog</a></li>\n                        <li><a href="/contact">Contact Us</a></li>'
                    )
                    updated_count += 1
                elif '<li><a href="contact">Contact Us</a></li>' in content:
                    content = content.replace(
                        '<li><a href="contact">Contact Us</a></li>',
                        '<li><a href="/blog">Blog</a></li>\n                        <li><a href="contact">Contact Us</a></li>'
                    )
                    updated_count += 1
                
                with open(filepath, "w", encoding="utf-8") as file:
                    file.write(content)

print(f"Added Blog link to footer in {updated_count} HTML files.")
