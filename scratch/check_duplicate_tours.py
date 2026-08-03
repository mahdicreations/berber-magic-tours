import os
import re
from collections import Counter

base_dir = r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours"
root_files = [f for f in os.listdir(base_dir) if f.endswith(".html")]

print("=== CHECKING FOR DUPLICATE TOURS IN CATEGORY PAGES ===")
total_duplicates_found = 0

for file_name in sorted(root_files):
    file_path = os.path.join(base_dir, file_name)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find all tour links in the page
    tour_links = re.findall(r'href=["\'](tours/[^"\'#]+)["\']', content)
    
    # Count occurrences
    link_counts = Counter(tour_links)
    duplicates = {link: count for link, count in link_counts.items() if count > 1}

    # Note: Cards usually have 2 links to the same tour (e.g. title link and "View Tour" button link).
    # We want to check if there are duplicate CARDS (i.e. tour links appearing in more than 2 places or duplicate card blocks).
    card_occurrences = {}
    for link, count in link_counts.items():
        # count / 2 is approximate card count
        card_count = count // 2 if count >= 2 else 1
        if count > 2:
            card_occurrences[link] = count

    if card_occurrences:
        print(f"\nPage [{file_name}] has DUPLICATE TOUR CARDS:")
        for link, count in card_occurrences.items():
            print(f"  - Tour link '{link}' appears {count} times (likely duplicate tour cards!)")
            total_duplicates_found += 1

print(f"\nAudit complete. Found duplicate issues in {total_duplicates_found} tour instances.")
