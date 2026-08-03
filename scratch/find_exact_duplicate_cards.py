import os
import re
from bs4 import BeautifulSoup

base_dir = r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours"
root_files = [f for f in os.listdir(base_dir) if f.endswith(".html")]

print("=== CHECKING FOR TRUE DUPLICATE CARDS (MULTIPLE CARDS FOR SAME TOUR) ===")
total_duplicate_cards = 0

for file_name in sorted(root_files):
    file_path = os.path.join(base_dir, file_name)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    soup = BeautifulSoup(content, "html.parser")
    grids = soup.find_all(class_=re.compile(r"tours-grid|tours-grid-container"))

    for g in grids:
        cards = g.find_all(class_=re.compile(r"tour-card|tour-card-premium"))
        seen_tours = set()
        duplicates_in_page = []

        for c in cards:
            a = c.find("a", href=True)
            if a:
                href = a['href'].strip()
                if href in seen_tours:
                    duplicates_in_page.append(href)
                else:
                    seen_tours.add(href)

        if duplicates_in_page:
            print(f"\nPage [{file_name}] has {len(duplicates_in_page)} duplicate card(s):")
            for dup in duplicates_in_page:
                print(f"  - Duplicate card pointing to: {dup}")
            total_duplicate_cards += len(duplicates_in_page)

print(f"\nVerification finished. Total true duplicate cards across all pages: {total_duplicate_cards}")
