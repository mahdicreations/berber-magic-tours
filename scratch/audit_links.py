import os
import re

base_dir = r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours"
index_path = os.path.join(base_dir, "index.html")

# Get list of all html files in root and in tours/
root_files = {f for f in os.listdir(base_dir) if f.endswith(".html")}
tour_files = {f for f in os.listdir(os.path.join(base_dir, "tours")) if f.endswith(".html")}

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

hrefs = re.findall(r'href=["\']([^"\'#]+)["\']', content)

print("--- AUDIT OF LINKS IN index.html ---")
broken_count = 0
for href in hrefs:
    if href.startswith("http") or href.startswith("mailto:") or href.startswith("tel:") or href.startswith("https://wa.me"):
        continue
    
    # Check resolution
    clean_href = href.split("?")[0]
    if not clean_href.endswith(".html"):
        clean_href_html = clean_href + ".html"
    else:
        clean_href_html = clean_href

    if clean_href_html.startswith("tours/"):
        target_name = clean_href_html[len("tours/"):]
        if target_name not in tour_files:
            print(f"BROKEN TOUR LINK in index.html: {href} (File 'tours/{target_name}' does NOT exist!)")
            broken_count += 1
    else:
        if clean_href_html not in root_files and clean_href != "/" and clean_href != "":
            print(f"BROKEN ROOT LINK in index.html: {href} (File '{clean_href_html}' does NOT exist!)")
            broken_count += 1

print(f"\nTotal broken links found in index.html: {broken_count}")
