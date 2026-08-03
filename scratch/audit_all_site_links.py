import os
import re

base_dir = r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours"
tour_dir = os.path.join(base_dir, "tours")

root_files = {f for f in os.listdir(base_dir) if f.endswith(".html")}
tour_files = {f for f in os.listdir(tour_dir) if f.endswith(".html")}

print("--- AUDITING ALL PAGES ON THE SITE ---")
total_broken = 0

all_html_paths = [os.path.join(base_dir, f) for f in root_files]

for page_path in sorted(all_html_paths):
    page_name = os.path.basename(page_path)
    with open(page_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    hrefs = re.findall(r'href=["\']([^"\'#]+)["\']', content)
    page_broken = []
    
    for href in hrefs:
        if href.startswith("http") or href.startswith("mailto:") or href.startswith("tel:") or href.startswith("https://wa.me") or href.startswith("assets/") or href.startswith("#"):
            continue
        
        clean_href = href.split("?")[0]
        if clean_href.startswith("tours/"):
            target_name = clean_href[len("tours/"):]
            if not target_name.endswith(".html"):
                target_name += ".html"
            if target_name not in tour_files:
                page_broken.append((href, f"tours/{target_name}"))
        else:
            target_name = clean_href
            if not target_name.endswith(".html"):
                target_name += ".html"
            if target_name not in root_files and target_name != ".html":
                page_broken.append((href, target_name))
    
    if page_broken:
        print(f"\nPage [{page_name}] has {len(page_broken)} broken link(s):")
        for orig, target in page_broken:
            print(f"  - {orig} (Target '{target}' missing)")
            total_broken += 1

print(f"\nAudit complete. Total broken links across all category & root pages: {total_broken}")
