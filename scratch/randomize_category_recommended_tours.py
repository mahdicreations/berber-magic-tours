import os
import re
import random

base_dir = r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours"
tours_dir = os.path.join(base_dir, "tours")

# Category mappings for all 45 tours
tour_categories = {
    # Climb Mount Toubkal
    "2-days-mount-toubkal.html": ("Climb Mount Toubkal", "2 Days"),
    "3-days-mount-toubkal.html": ("Climb Mount Toubkal", "3 Days"),
    "4-days-toubkal-peaks.html": ("Climb Mount Toubkal", "4 Days"),
    "mount-toubkal-3days-trek-acclimatization.html": ("Climb Mount Toubkal", "3 Days"),
    "toubkal-winter-climb.html": ("Climb Mount Toubkal", "5 Days"),
    "toubkal-summit-via-lake-ifni-6-days.html": ("Climb Mount Toubkal", "6 Days"),

    # Berber Village Treks
    "2days-atlas-mountains-valleys.html": ("Berber Village Treks", "2 Days"),
    "2days-azzaden-valley.html": ("Berber Village Treks", "2 Days"),
    "3-day-hiking-atlas-mountains.html": ("Berber Village Treks", "3 Days"),
    "3-days-atlas-mountains-trek-camel-ride.html": ("Berber Village Treks", "3 Days"),
    "3days-in-three-valleys.html": ("Berber Village Treks", "3 Days"),
    "3days-to-setti-fattma.html": ("Berber Village Treks", "3 Days"),
    "4days-in-four-valleys.html": ("Berber Village Treks", "4 Days"),
    "5-days-atlas-mountain-trek.html": ("Berber Village Treks", "5 Days"),
    "overnight-in-atlas-mountains.html": ("Berber Village Treks", "2 Days"),

    # Combine Toubkal & Villages
    "4days-berber-villages-toubkal.html": ("Combine Toubkal & Villages", "4 Days"),
    "5days-berber-villages-toubkal.html": ("Combine Toubkal & Villages", "5 Days"),
    "6-days-berber-villages-toubkal.html": ("Combine Toubkal & Villages", "6 Days"),

    # Combine Atlas & Sahara
    "5days-berber-villagessahara.html": ("Combine Atlas & Sahara", "5 Days"),
    "5days-toubkal-sahara.html": ("Combine Atlas & Sahara", "5 Days"),
    "6days-berber-villagessahara.html": ("Combine Atlas & Sahara", "6 Days"),
    "6days-berber-villagessahara-opt-2.html": ("Combine Atlas & Sahara", "6 Days"),
    "6days-toubkal-sahara.html": ("Combine Atlas & Sahara", "6 Days"),
    "6days-toubkal-sahara-opt-2.html": ("Combine Atlas & Sahara", "6 Days"),
    "7days-berber-villagessahara.html": ("Combine Atlas & Sahara", "7 Days"),

    # Sahara Desert Tours
    "3-day-desert-tour-casablanca-marrakech.html": ("Sahara Desert Tours", "3 Days"),
    "3days-fes-to-marrakech-desert-tour.html": ("Sahara Desert Tours", "3 Days"),
    "3days-merzouga-desert.html": ("Sahara Desert Tours", "3 Days"),
    "4-day-desert-tour-from-fes-to-marrakech.html": ("Sahara Desert Tours", "4 Days"),
    "4-days-sahara-desert-marrakech-to-fes.html": ("Sahara Desert Tours", "4 Days"),
    "4days-sahara-desert.html": ("Sahara Desert Tours", "4 Days"),
    "5-day-desert-tour-from-fes-to-marrakech.html": ("Sahara Desert Tours", "5 Days"),
    "5-days-desert-tour-from-casablanca.html": ("Sahara Desert Tours", "5 Days"),
    "6-days-desert-tour-from-casablanca.html": ("Sahara Desert Tours", "6 Days"),
    "6-days-desert-tour-from-fes-to-marrakech.html": ("Sahara Desert Tours", "6 Days"),

    # Marrakech Day Trips
    "cooking-class-in-high-atlas.html": ("Marrakech Day Trips", "1 Day"),
    "day-trip-to-ourika-valley.html": ("Marrakech Day Trips", "1 Day"),
    "imlil-valley-day-trip.html": ("Marrakech Day Trips", "1 Day"),
    "mountain-bike-day-trip.html": ("Marrakech Day Trips", "1 Day"),

    # Biking in Morocco
    "4-days-biking-in-morocco.html": ("Biking in Morocco", "4 Days"),
    "5-days-morocco-biking.html": ("Biking in Morocco", "5 Days"),

    # Imperial Cities & Morocco Tours
    "5-days-imperial-cities.html": ("Morocco Tours", "5 Days"),
    "6days-imperial-cities-desert.html": ("Morocco Tours", "6 Days"),
    "7-days-around-morocco.html": ("Morocco Tours", "7 Days"),
    "best-of-morocco-holidays.html": ("Morocco Tours", "10 Days")
}

# Collect metadata for each tour
tour_meta = {}

for filename in sorted(os.listdir(tours_dir)):
    if not filename.endswith(".html"):
        continue

    filepath = os.path.join(tours_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract title
    title_m = re.search(r'<h1[^>]*class=["\'][^"\'\n]*page-title[^"\'\n]*["\'][^>]*>([\s\S]*?)</h1>', content, re.IGNORECASE)
    if not title_m:
        title_m = re.search(r'<title>([\s\S]*?)\|', content, re.IGNORECASE)
    title = re.sub(r'<[^>]+>', '', title_m.group(1)).strip() if title_m else filename.replace(".html", "").replace("-", " ").capitalize()

    # Extract hero/first image
    img_m = re.search(r'background-image:\s*url\(["\']?(images/[^"\'\)\s]+)["\']?\)', content)
    if not img_m:
        img_m = re.search(r'<img[^>]+src=["\'](images/[^"\'\s]+)["\']', content)
    img_src = img_m.group(1) if img_m else "images/2-days-mount-toubkal/Toubkal-ascent.jpg"

    # Extract excerpt from lead text or overview
    lead_m = re.search(r'<p[^>]*class=["\'][^"\'\n]*lead-text[^"\'\n]*["\'][^>]*>([\s\S]*?)</p>', content, re.IGNORECASE)
    if lead_m:
        excerpt = re.sub(r'<[^>]+>', '', lead_m.group(1)).strip()
    else:
        meta_desc = re.search(r'<meta\s+name=["\']description["\']\s+content=["\']([^"\'\n]+)["\']', content, re.IGNORECASE)
        excerpt = meta_desc.group(1).strip() if meta_desc else "Embark on an authentic Moroccan journey with Berber Magic Tours."

    if len(excerpt) > 130:
        excerpt = excerpt[:125].rstrip() + "..."

    cat_info = tour_categories.get(filename, ("Morocco Tours", "Guided Tour"))

    tour_meta[filename] = {
        "title": title,
        "image": img_src,
        "excerpt": excerpt,
        "category": cat_info[0],
        "duration": cat_info[1]
    }

# Group tours by category
category_to_tours = {}
for filename, meta in tour_meta.items():
    cat = meta["category"]
    category_to_tours.setdefault(cat, []).append(filename)

print("=== RANDOMIZING CATEGORY-BASED RECOMMENDED TOURS FOR EACH PAGE ===")
updated_count = 0

for filename, meta in tour_meta.items():
    curr_cat = meta["category"]
    
    # Use deterministic seed based on filename so recommendations are static per page, but unique across pages
    seed_val = int.from_bytes(filename.encode('utf-8'), 'big') % 1000000
    rng = random.Random(seed_val)

    same_cat_tours = [t for t in category_to_tours[curr_cat] if t != filename]
    
    # Shuffle same category tours uniquely for this page
    rng.shuffle(same_cat_tours)

    pool = same_cat_tours[:]

    # If category pool has fewer than 3, append shuffled tours from other categories
    if len(pool) < 3:
        other_tours = [t for t in tour_meta.keys() if t != filename and t not in pool]
        rng.shuffle(other_tours)
        pool.extend(other_tours)

    # Pick 3 unique tours for this page
    selected_3 = pool[:3]

    cards_html = ""
    for rel_file in selected_3:
        rm = tour_meta[rel_file]
        cards_html += f"""                <!-- Related Tour Card -->
                <div style="background: #ffffff; border-radius: 12px; border: 1px solid #E2E8F0; overflow: hidden; display: flex; flex-direction: column;">
                    <a href="{rel_file}" style="display: block; overflow: hidden;">
                        <img src="{rm['image']}" alt="{rm['title']}" style="width: 100%; height: 180px; object-fit: cover; display: block;">
                    </a>
                    <div style="padding: 18px; display: flex; flex-direction: column; flex-grow: 1;">
                        <div style="font-size: 0.78rem; font-weight: 700; color: var(--primary); text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 4px;">{rm['category']}</div>
                        <h3 style="font-size: 1.08rem; font-weight: 700; color: var(--secondary); margin: 0 0 8px 0; line-height: 1.35;">
                            <a href="{rel_file}" style="color: inherit; text-decoration: none;">{rm['title']}</a>
                        </h3>
                        <p style="font-size: 0.88rem; color: #64748B; line-height: 1.55; margin: 0 0 16px 0; flex-grow: 1;">{rm['excerpt']}</p>
                        <div style="margin-top: auto; padding-top: 12px; border-top: 1px solid #F1F5F9; display: flex; align-items: center; justify-content: space-between;">
                            <span style="font-size: 0.82rem; color: #64748B;"><i class="far fa-clock"></i> {rm['duration']}</span>
                            <a href="{rel_file}" style="color: var(--primary); font-weight: 700; font-size: 0.85rem; text-decoration: none;">View Tour <i class="fas fa-arrow-right" style="font-size: 0.75rem;"></i></a>
                        </div>
                    </div>
                </div>\n"""

    rec_section_code = f"""    <!-- Recommended Tours Section -->
    <section class="recommended-tours-section" style="padding: 50px 0; background: #FAFAFA; border-top: 1px solid #E2E8F0;">
        <div class="container">
            <div style="margin-bottom: 30px; text-align: center;">
                <h2 style="font-family: var(--font-heading); font-size: 1.8rem; color: var(--secondary); margin: 0 0 6px 0;">Recommended Tours</h2>
                <p style="color: #64748B; font-size: 0.92rem; margin: 0;">Explore handpicked adventures and popular itineraries in Morocco crafted by Berber Magic Tours.</p>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px;">
{cards_html}
            </div>
        </div>
    </section>"""

    # Apply to tour page
    filepath = os.path.join(tours_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        file_content = f.read()

    pattern = r'<!-- Recommended Tours Section -->[\s\S]*?</section>'
    if re.search(pattern, file_content):
        file_content = re.sub(pattern, rec_section_code, file_content)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(file_content)
        updated_count += 1
        print(f"Randomized unique recommended selection for [{filename}] -> {selected_3}")

print(f"\nCompleted! Randomized unique category-based Recommended Tours across all {updated_count} tour pages.")
