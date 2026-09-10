import os, re
from pathlib import Path

root = Path('.')

# ============================================================
# 1. FIX "Other Tours" dead link href="#" in ALL HTML files
#    Change to href="morocco-tours" or href="../morocco-tours"
#    depending on whether the file is in /tours/ or root
# ============================================================

dead_pattern = re.compile(
    r'(<a\s[^>]*href=["\'])#(["\'][^>]*>Other Tours)',
    re.DOTALL
)

nav_fixed = 0
meta_fixed = []

for html_file in sorted(root.rglob('*.html')):
    if '.git' in str(html_file) or 'scratch' in str(html_file):
        continue

    content = html_file.read_text(encoding='utf-8', errors='ignore')
    original = content

    # Determine correct relative path
    in_tours_subdir = html_file.parent.name in ('tours', 'blog')
    in_blog = html_file.parent.name == 'blog'
    prefix = '../' if in_tours_subdir else ''

    # Replace href="#" for "Other Tours" with a real link
    content = dead_pattern.sub(
        rf'\g<1>{prefix}morocco-tours\g<2>',
        content
    )

    # -------------------------------------------------------
    # 2. FIX OUTLIER METADATA (surgical, file-by-file)
    # -------------------------------------------------------
    rel = str(html_file)

    # --- terms-conditions.html (179 chars → trim) ---
    if rel == 'terms-conditions.html':
        OLD = 'Read the Terms and Conditions of Berber Magic Tours. Information on booking procedures, payment policies, cancellations, travel insurance, and safety guidelines for Morocco trips.'
        NEW = 'Berber Magic Tours booking terms: payment, cancellations, travel insurance and safety guidelines for Morocco treks and desert tours.'
        if OLD in content:
            content = content.replace(OLD, NEW)
            meta_fixed.append((rel, 'description', len(OLD), len(NEW)))

    # --- about-us.html (167 chars → trim) ---
    if rel == 'about-us.html':
        OLD = 'Learn about Berber Magic Tours, a family-run Berber travel company in Morocco offering authentic Atlas mountain trekking, Sahara desert tours, and responsible tourism.'
        NEW = 'Berber Magic Tours is a family-run company offering authentic Atlas mountain trekking, Sahara desert tours and responsible travel in Morocco.'
        if OLD in content:
            content = content.replace(OLD, NEW)
            meta_fixed.append((rel, 'description', len(OLD), len(NEW)))

    # --- faq.html (163 chars → trim) ---
    if rel == 'faq.html':
        OLD = 'Find answers to common questions about trekking in the High Atlas, Mount Toubkal climbing, Sahara desert tours, packing lists, and booking with Berber Magic Tours.'
        NEW = 'Answers to common questions about High Atlas trekking, Mount Toubkal, Sahara desert tours, packing lists and booking with Berber Magic Tours.'
        if OLD in content:
            content = content.replace(OLD, NEW)
            meta_fixed.append((rel, 'description', len(OLD), len(NEW)))

    # --- 404.html (44 chars → too short) ---
    if rel == '404.html':
        OLD = 'The page you are looking for does not exist.'
        NEW = 'Page not found. Return to Berber Magic Tours and explore our Morocco treks, Sahara desert tours and Marrakech day trips.'
        if OLD in content:
            content = content.replace(OLD, NEW)
            meta_fixed.append((rel, 'description', len(OLD), len(NEW)))

    # --- tours/4days-in-four-valleys.html (truncated / 169 chars) ---
    if rel == r'tours\4days-in-four-valleys.html':
        OLD_T = '4days in four valleys | Berber Magic Tours'
        NEW_T = '4-Day Four Valleys Trek in Atlas Mountains | Berber Magic Tours'
        OLD_D_FRAG = 'Take a break from the hectic city scene and restore yourself with a brief walking tour through &quot;four valleys&quot; of the Atlas range. A refreshing timeout from the'
        NEW_D = '4-day guided trek through four Atlas Mountain valleys from Marrakech. Explore Berber villages, hidden waterfalls and mountain landscapes with local guides.'
        if OLD_T in content:
            content = content.replace(OLD_T, NEW_T)
            meta_fixed.append((rel, 'title', len(OLD_T), len(NEW_T)))
        if OLD_D_FRAG in content:
            content = content.replace(OLD_D_FRAG, NEW_D)
            meta_fixed.append((rel, 'description (truncated)', len(OLD_D_FRAG), len(NEW_D)))

    # --- tours/mount-toubkal-3days-trek-acclimatization.html (67 chars title) ---
    if rel == r'tours\mount-toubkal-3days-trek-acclimatization.html':
        OLD_T = 'Mount Toubkal 3 days trek | Acclimatize better | Berber Magic Tours'
        NEW_T = '3-Day Mount Toubkal Trek with Acclimatization | Berber Magic Tours'
        if OLD_T in content:
            content = content.replace(OLD_T, NEW_T)
            meta_fixed.append((rel, 'title', len(OLD_T), len(NEW_T)))

    # --- tours/3-days-atlas-mountains-trek-camel-ride.html (67 chars title, &amp; encoding issue) ---
    if rel == r'tours\3-days-atlas-mountains-trek-camel-ride.html':
        OLD_T = '3 days Atlas Mountain trek &amp; desert Agafay | Berber Magic Tours'
        NEW_T = '3-Day Atlas Mountain Trek &amp; Agafay Desert | Berber Magic Tours'
        if OLD_T in content:
            content = content.replace(OLD_T, NEW_T)
            meta_fixed.append((rel, 'title', len(OLD_T), len(NEW_T)))

    if content != original:
        html_file.write_text(content, encoding='utf-8')
        if dead_pattern.search(original):
            nav_fixed += 1

print(f"Navigation dead links fixed in {nav_fixed} files.")
print(f"\nMetadata changes:")
for item in meta_fixed:
    rel, field, old_len, new_len = item
    print(f"  {rel} -- {field}: {old_len} chars -> {new_len} chars")
