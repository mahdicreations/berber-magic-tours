import os
import re

base_dir = r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours"
tours_dir = os.path.join(base_dir, "tours")

root_footer_menu_html = """                <!-- Col 2: Menu -->
                <div class="footer-col links-col">
                    <h3 class="footer-title">Menu</h3>
                    <ul class="footer-links">
                        <li><a href="index.html">Home</a></li>
                        <li><a href="about-us.html">About Us</a></li>
                        <li><a href="faq.html">FAQ</a></li>
                        <li><a href="marrakech-day-trips.html">Marrakech Day Trips</a></li>
                        <li><a href="trek-and-hike.html">Trek &amp; Hike</a></li>
                        <li><a href="sahara-desert-tours.html">Sahara Desert Tours</a></li>
                        <li><a href="morocco-tours.html">Morocco Tours</a></li>
                        <li><a href="contact.html">Contact Us</a></li>
                    </ul>
                </div>"""

tours_footer_menu_html = """                <!-- Col 2: Menu -->
                <div class="footer-col links-col">
                    <h3 class="footer-title">Menu</h3>
                    <ul class="footer-links">
                        <li><a href="../index.html">Home</a></li>
                        <li><a href="../about-us.html">About Us</a></li>
                        <li><a href="../faq.html">FAQ</a></li>
                        <li><a href="../marrakech-day-trips.html">Marrakech Day Trips</a></li>
                        <li><a href="../trek-and-hike.html">Trek &amp; Hike</a></li>
                        <li><a href="../sahara-desert-tours.html">Sahara Desert Tours</a></li>
                        <li><a href="../morocco-tours.html">Morocco Tours</a></li>
                        <li><a href="../contact.html">Contact Us</a></li>
                    </ul>
                </div>"""

pattern = r'<!-- Col 2: Menu -->[\s\S]*?</div>'

print("=== UPDATING FOOTER MENU LINKS WITH ABOUT US & FAQ ===")

# Root pages
root_updated = 0
for filename in os.listdir(base_dir):
    if not filename.endswith(".html"):
        continue

    filepath = os.path.join(base_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if re.search(pattern, content):
        content = re.sub(pattern, root_footer_menu_html, content)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        root_updated += 1
        print(f"Updated footer links in root page [{filename}]")

# Tours pages
tours_updated = 0
for filename in os.listdir(tours_dir):
    if not filename.endswith(".html"):
        continue

    filepath = os.path.join(tours_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if re.search(pattern, content):
        content = re.sub(pattern, tours_footer_menu_html, content)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        tours_updated += 1
        print(f"Updated footer links in tour page [{filename}]")

print(f"\nDone! Updated footer menu links across {root_updated} root pages and {tours_updated} tour pages.")
