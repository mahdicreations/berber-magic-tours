import os
import re

base_dir = r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours"
target_files = [
    "berber-village-treks.html", "biking-in-morocco.html", "climb-mount-toubkal.html",
    "combine-atlas-mountains-and-desert.html", "combine-berber-villages-and-sahara.html",
    "combine-toubkal-and-sahara.html", "combine-toubkal-and-villages.html",
    "marrakech-day-trips.html", "morocco-tours.html", "sahara-desert-tours.html",
    "tours-from-casablanca.html", "tours-from-fes.html", "tours-from-marrakech.html",
    "trek-and-hike.html"
]

print("=== EXACT DEDUPLICATION OF CARDS WITHOUT ALTERING HTML/CSS/TEXT ===")

total_removed = 0

for file_name in target_files:
    file_path = os.path.join(base_dir, file_name)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    pos = 0
    cards_found = []
    
    while True:
        m = re.search(r'(?:<!-- Tour Card:[^\n]*-->\s*)?<div class="tour-card(?:-premium)?"', content[pos:])
        if not m:
            break
        
        card_start = pos + m.start()
        div_start = card_start + m.group(0).rfind('<div class="tour-card')
        
        idx = div_start
        div_depth = 0
        card_end = -1
        
        while idx < len(content):
            if content[idx:idx+4] == '<div':
                div_depth += 1
                idx += 4
            elif content[idx:idx+6] == '</div>':
                div_depth -= 1
                idx += 6
                if div_depth == 0:
                    card_end = idx
                    break
            else:
                idx += 1
        
        if card_end != -1:
            card_code = content[card_start:card_end]
            href_m = re.search(r'href=["\'](tours/[^"\'#]+)["\']', card_code)
            href = href_m.group(1) if href_m else None
            cards_found.append((card_start, card_end, href, card_code))
            pos = card_end
        else:
            pos += 4

    seen_hrefs = set()
    ranges_to_remove = []
    
    for start, end, href, code in cards_found:
        if href:
            if href in seen_hrefs:
                ranges_to_remove.append((start, end))
            else:
                seen_hrefs.add(href)
    
    if ranges_to_remove:
        print(f"[FILE: {file_name}] Removing {len(ranges_to_remove)} duplicate card(s)...")
        total_removed += len(ranges_to_remove)
        
        new_content = list(content)
        for start, end in reversed(ranges_to_remove):
            del new_content[start:end]
        
        final_html = "".join(new_content)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(final_html)

print(f"\nDeduplication complete! Total {total_removed} duplicate cards removed. Zero HTML structure, text, or design alterations made.")
