import os

tours_dir = r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours\tours"

updated_count = 0

for f in os.listdir(tours_dir):
    if f.endswith(".html"):
        filepath = os.path.join(tours_dir, f)
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
            
        # Check if Blog link is missing in footer
        if 'class="footer-links"' in content and '/blog' not in content and '../blog' not in content:
            # Replace Contact Us with Blog + Contact Us in footer menu
            if '<li><a href="../contact">Contact Us</a></li>' in content:
                content = content.replace(
                    '<li><a href="../contact">Contact Us</a></li>',
                    '<li><a href="/blog">Blog</a></li>\n                        <li><a href="../contact">Contact Us</a></li>'
                )
                updated_count += 1
            elif '<li><a href="/contact">Contact Us</a></li>' in content:
                content = content.replace(
                    '<li><a href="/contact">Contact Us</a></li>',
                    '<li><a href="/blog">Blog</a></li>\n                        <li><a href="/contact">Contact Us</a></li>'
                )
                updated_count += 1
            elif '<li><a href="contact">Contact Us</a></li>' in content:
                content = content.replace(
                    '<li><a href="contact">Contact Us</a></li>',
                    '<li><a href="/blog">Blog</a></li>\n                        <li><a href="/contact">Contact Us</a></li>'
                )
                updated_count += 1
                
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(content)

print(f"Added Blog link to footer in {updated_count} tour HTML files in tours/ directory.")
