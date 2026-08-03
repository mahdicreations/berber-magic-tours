import os
import re
from bs4 import BeautifulSoup

base_dir = r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours"
root_files = [f for f in os.listdir(base_dir) if f.endswith(".html")]

print("=== REMOVING DUPLICATE TOUR CARDS ACROSS ALL CATEGORY PAGES ===")
fixed_count = 0

for file_name in sorted(root_files):
    file_path = os.path.join(base_dir, file_name)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    soup = BeautifulSoup(content, "html.parser")
    grids = soup.find_all(class_=re.compile(r"tours-grid|tours-grid-container"))

    page_modified = False

    for grid in grids:
        cards = grid.find_all(class_=re.compile(r"tour-card|tour-card-premium"))
        seen_tours = set()
        cards_to_remove = []

        for card in cards:
            a = card.find("a", href=True)
            h3 = card.find(["h3", "h4", "h2"])
            href = a['href'].strip() if a else None
            title = h3.get_text(strip=True) if h3 else None

            # Key for deduplication
            key = href or title

            if key:
                if key in seen_tours:
                    cards_to_remove.append(card)
                else:
                    seen_tours.add(key)

        if cards_to_remove:
            print(f"File [{file_name}]: Removing {len(cards_to_remove)} duplicate tour card(s)...")
            for c in cards_to_remove:
                c.decompose()
            page_modified = True

    if page_modified:
        # Prettify / save HTML cleanly
        # Use str(soup) to preserve document structure
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(str(soup))
        fixed_count += 1

print(f"\nCompleted! Fixed duplicate cards on {fixed_count} page(s).")
