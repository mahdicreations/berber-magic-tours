import os
import re

base_dir = r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours"
category_files = [
    "berber-village-treks.html", "biking-in-morocco.html", "climb-mount-toubkal.html",
    "combine-atlas-mountains-and-desert.html", "combine-berber-villages-and-sahara.html",
    "combine-toubkal-and-sahara.html", "combine-toubkal-and-villages.html",
    "marrakech-day-trips.html", "morocco-tours.html", "sahara-desert-tours.html",
    "tours-from-casablanca.html", "tours-from-fes.html", "tours-from-marrakech.html",
    "trek-and-hike.html"
]

print("=== CLEANING DUPLICATE TOUR CARDS SAFELY VIA REGEX STRING MATCHING ===")

for file_name in category_files:
    file_path = os.path.join(base_dir, file_name)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the main tours grid block
    # Tour cards are inside <div class="tours-grid..."> ... </div>
    # Pattern to match individual card blocks:
    # (<!-- Tour Card:.*?-->)?\s*<div class="tour-card(?:-premium)?">.*?</div>\s*</div>
    
    # We locate cards inside the grid
    # Let's split content or extract card blocks matching <div class="tour-card...
    
    pattern = r'((?:<!-- Tour Card:.*?-->\s*)?<div class="tour-card(?:-premium)?">[\s\S]*?</div>\s*</div>)'
    
    cards = re.findall(pattern, content)
    seen_hrefs = set()
    cards_to_remove = []
    
    for card_str in cards:
        # Find href inside this card block
        href_match = re.search(r'href=["\'](tours/[^"\'#]+)["\']', card_str)
        if href_match:
            href = href_match.group(1).strip()
            if href in seen_hrefs:
                cards_to_remove.append(card_str)
            else:
                seen_hrefs.add(href)

    if cards_to_remove:
        print(f"File [{file_name}]: Removing {len(cards_to_remove)} duplicate card block(s)...")
        for card_str in cards_to_remove:
            # Remove exact string occurrence of duplicate card
            content = content.replace(card_str, "", 1)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

print("Safely cleaned all duplicate tour cards without touching any HTML/CSS design!")
