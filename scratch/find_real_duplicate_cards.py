import os
import re
from bs4 import BeautifulSoup

base_dir = r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours"
root_files = [f for f in os.listdir(base_dir) if f.endswith(".html")]

print("=== CHECKING ACCURATE DUPLICATE CARDS (ONLY TOP LEVEL CARDS) ===")
total_pages = 0

for file_name in sorted(root_files):
    file_path = os.path.join(base_dir, file_name)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    soup = BeautifulSoup(content, "html.parser")
    grids = soup.find_all(class_=re.compile(r"tours-grid|tours-grid-container"))

    for g in grids:
        # Match only exact top-level cards
        cards = g.find_all(lambda tag: tag.name == "div" and ("tour-card" in tag.get("class", []) or "tour-card-premium" in tag.get("class", [])))
        
        seen_tours = set()
        duplicate_urls = []

        for c in cards:
            a = c.find("a", href=True)
            if a:
                href = a['href'].strip()
                if href in seen_tours:
                    duplicate_urls.append(href)
                else:
                    seen_tours.add(href)

        if duplicate_urls:
            print(f"\n[PAGE: {file_name}] Has {len(duplicate_urls)} DUPLICATE CARD(S):")
            for d in duplicate_urls:
                print(f"  - Duplicate card pointing to '{d}'")
            total_pages += len(duplicate_urls)

print(f"\nAudit complete. Total duplicate cards across all category pages: {total_pages}")
