import os
import re
from bs4 import BeautifulSoup

base_dir = r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours"
root_files = [f for f in os.listdir(base_dir) if f.endswith(".html")]

print("=== DEEP AUDIT FOR DUPLICATE TOUR CARDS ON ALL CATEGORY PAGES ===")
total_pages_with_dups = 0

for file_name in sorted(root_files):
    file_path = os.path.join(base_dir, file_name)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    soup = BeautifulSoup(content, "html.parser")
    tour_cards = soup.find_all(class_=re.compile(r"tour-card|card|package-card"))

    titles = []
    links = []

    for card in tour_cards:
        # Find title
        h3 = card.find(["h3", "h4", "h2"])
        title = h3.get_text(strip=True) if h3 else "NO TITLE"
        
        # Find tour href
        a = card.find("a", href=True)
        href = a['href'] if a else "NO HREF"

        titles.append(title)
        links.append(href)

    # Check duplicate titles or links
    seen_titles = set()
    dup_titles = set()
    for t in titles:
        if t in seen_titles:
            dup_titles.add(t)
        seen_titles.add(t)

    seen_links = set()
    dup_links = set()
    for l in links:
        if l in seen_links and l != "NO HREF" and not l.startswith("#"):
            dup_links.add(l)
        seen_links.add(l)

    if dup_titles or dup_links:
        print(f"\n[PAGE: {file_name}]")
        if dup_titles:
            print("  DUPLICATE CARD TITLES:")
            for dt in dup_titles:
                print(f"    - '{dt}'")
        if dup_links:
            print("  DUPLICATE CARD LINKS:")
            for dl in dup_links:
                print(f"    - '{dl}'")
        total_pages_with_dups += 1

print(f"\nAudit finished. Total pages with duplicate tour cards: {total_pages_with_dups}")
