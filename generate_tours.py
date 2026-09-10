#!/usr/bin/env python3
"""
Tour HTML Generator Script for Berber Magic Tours.

This script scans tour directories in site/by-category/ (or by-category/),
parses tour-info.txt for each tour, fetches its images, and generates a fully
formatted HTML file using 2-days-azzaden-valley-trek.html as a master template.
The resulting HTML files are saved into an output_tours directory.
"""

import os
import sys
import glob
import re
import shutil
from html import escape

# Configuration
MASTER_TEMPLATE_PATH = "2-days-azzaden-valley-trek.html"
OUTPUT_DIRS = ["tours", "output_tours"]
SEARCH_PATHS = ["site/by-category", "by-category"]

def get_map_embed_url_and_title(tour_folder_name, title, categories, meta_location):
    """Determine exact Google Maps embed URL and location label for a tour."""
    title_lower = title.lower()
    cat_lower = categories.lower()
    folder_lower = tour_folder_name.lower()
    
    # 1. Mount Toubkal Treks
    if 'toubkal' in title_lower or 'toubkal' in folder_lower:
        if 'sahara' in title_lower or 'sahara' in folder_lower:
            return (
                'https://maps.google.com/maps?q=Mount+Toubkal+to+Merzouga+Desert,+Morocco&t=&z=8&ie=UTF8&iwloc=&output=embed',
                'Mount Toubkal & Sahara Desert, Morocco'
            )
        return (
            'https://maps.google.com/maps?q=Jebel+Toubkal,+Imlil,+Morocco&t=&z=11&ie=UTF8&iwloc=&output=embed',
            'Mount Toubkal (4,167m) & Imlil Valley, Morocco'
        )
    
    # 2. Azzaden Valley Treks
    if 'azzaden' in title_lower or 'azzaden' in folder_lower:
        return (
            'https://maps.google.com/maps?q=Azzaden+Valley,+High+Atlas,+Morocco&t=&z=11&ie=UTF8&iwloc=&output=embed',
            'Azzaden Valley, High Atlas Mountains, Morocco'
        )
        
    # 3. Ourika Valley & Setti Fatma
    if 'ourika' in title_lower or 'ourika' in folder_lower or 'setti' in title_lower or 'setti' in folder_lower:
        return (
            'https://maps.google.com/maps?q=Setti+Fatma,+Ourika+Valley,+Morocco&t=&z=11&ie=UTF8&iwloc=&output=embed',
            'Ourika Valley & Setti Fatma, Morocco'
        )

    # 4. Fes to Marrakech / Desert Tours from Fes
    if 'fes' in title_lower or 'fes' in folder_lower:
        return (
            'https://maps.google.com/maps?q=Fes+to+Merzouga+to+Marrakech,+Morocco&t=&z=7&ie=UTF8&iwloc=&output=embed',
            'Fes, Merzouga Desert & Marrakech, Morocco'
        )
        
    # 5. Casablanca Tours
    if 'casablanca' in title_lower or 'casablanca' in folder_lower:
        return (
            'https://maps.google.com/maps?q=Casablanca+to+Merzouga+Desert,+Morocco&t=&z=7&ie=UTF8&iwloc=&output=embed',
            'Casablanca, Sahara Desert & Imperial Cities, Morocco'
        )

    # 6. Combined Berber Villages & Sahara
    if ('berber' in folder_lower or 'berber' in title_lower) and ('sahara' in folder_lower or 'sahara' in title_lower):
        return (
            'https://maps.google.com/maps?q=Atlas+Mountains+to+Merzouga+Desert,+Morocco&t=&z=8&ie=UTF8&iwloc=&output=embed',
            'High Atlas Mountains & Sahara Desert, Morocco'
        )

    # 7. Sahara Desert / Merzouga Tours
    if 'desert' in title_lower or 'sahara' in title_lower or 'merzouga' in title_lower or 'desert' in folder_lower:
        return (
            'https://maps.google.com/maps?q=Merzouga+Sahara+Desert,+Morocco&t=&z=9&ie=UTF8&iwloc=&output=embed',
            'Erg Chebbi, Merzouga Sahara Desert, Morocco'
        )

    # 8. Atlas Mountains / Berber Villages / Day Trips / Biking
    if 'atlas' in title_lower or 'berber' in title_lower or 'berber' in folder_lower or 'valleys' in title_lower or 'hiking' in title_lower or 'cooking' in title_lower or 'bike' in title_lower or 'biking' in folder_lower or 'imlil' in folder_lower or 'day trip' in cat_lower:
        return (
            'https://maps.google.com/maps?q=Imlil+Valley,+High+Atlas+Mountains,+Morocco&t=&z=11&ie=UTF8&iwloc=&output=embed',
            'High Atlas Mountains & Berber Villages, Morocco'
        )
        
    # 9. Imperial Cities & Grand Morocco Tours
    if 'imperial' in title_lower or 'around morocco' in title_lower or 'holidays' in title_lower or 'imperial' in folder_lower:
        return (
            'https://maps.google.com/maps?q=Marrakech,+Fes,+Merzouga,+Morocco&t=&z=6&ie=UTF8&iwloc=&output=embed',
            'Imperial Cities & Highlights of Morocco'
        )

    # Default fallback: High Atlas
    return (
        'https://maps.google.com/maps?q=Imlil,+High+Atlas+Mountains,+Morocco&t=&z=11&ie=UTF8&iwloc=&output=embed',
        'Imlil Valley & High Atlas, Morocco'
    )

def clean_text(text):
    """Clean up corrupted text encoding characters."""
    if not text:
        return ""
    text = text.replace('\ufffd', "'")
    text = text.replace('’', "'").replace('–', "-").replace('“', '"').replace('”', '"')
    
    replacements = [
        ('\u2019', "'"),
        ('\u2018', "'"),
        ('`', "'"),
        ('´', "'"),
        ('\u201c', '"'),
        ('\u201d', '"'),
        ('\u2013', '-'),
        ('\u2014', '-'),
    ]
    for old, new in replacements:
        text = text.replace(old, new)
        
    return text.strip()

def parse_tour_info(filepath):
    """Parse structured tour-info.txt into a dictionary."""
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        raw_content = f.read()

    content = clean_text(raw_content)

    # 1. Title
    title_m = re.search(r'^TOUR:\s*(.+)$', content, re.MULTILINE)
    title = title_m.group(1).strip() if title_m else ""

    # 2. Categories
    cat_m = re.search(r'^Categories:\s*(.+)$', content, re.MULTILINE)
    categories = cat_m.group(1).strip() if cat_m else ""

    # 3. Meta details
    meta = {}
    duration_m = re.search(r'Duration:\s*(.+)', content)
    if duration_m:
        meta['duration'] = duration_m.group(1).strip()
    price_m = re.search(r'Price start from:\s*(.+)', content)
    if price_m:
        meta['price'] = price_m.group(1).strip()
    loc_m = re.search(r'Location:\s*(.+)', content)
    if loc_m:
        meta['location'] = loc_m.group(1).strip()

    # 4. Description
    desc_match = re.search(r'DESCRIPTION:\s*\n(.*?)(?=\nITINERARY:|\nTOUR META:|\nIMAGES|\Z)', content, re.DOTALL)
    description = desc_match.group(1).strip() if desc_match else ""

    # Check if description is missing / placeholder
    if not description or "(not available on the website)" in description.lower():
        dur_str = f"for {meta.get('duration')}" if meta.get('duration') else ""
        loc_str = meta.get('location', 'the High Atlas Mountains')
        description = (
            f"Embark on an unforgettable adventure {dur_str} with Berber Magic Tours. "
            f"Discover authentic Berber villages, stunning mountain landscapes, and rich local culture in {loc_str}. "
            f"Our experienced local guides will ensure a safe, scenic, and immersive journey tailored for all nature and culture lovers."
        )

    # 5. Itinerary
    itin_match = re.search(r'ITINERARY:\s*\n(.*?)(?=\nIMAGES|\Z)', content, re.DOTALL)
    itin_raw = itin_match.group(1).strip() if itin_match else ""

    if itin_raw:
        # Strip trailing inclusions / packing list sections from itinerary text
        itin_raw = re.split(r'\n(?=What is included|What\'s included|Included:|Includes:|Things you need to bring|What is not included)', itin_raw, flags=re.IGNORECASE)[0].strip()

    days = []
    if itin_raw:
        raw_days = re.split(r'(?=\n?DAY\s*\d+[\s,:\*\-])', itin_raw, flags=re.IGNORECASE)
        for rd in raw_days:
            rd = rd.strip()
            if not rd or rd.upper().startswith('PLEASE NOTE'):
                continue
            
            lines = [l.strip() for l in rd.split('\n') if l.strip()]
            if not lines:
                continue
            
            header_line = lines[0]
            body_lines = lines[1:]
            
            day_match = re.match(r'^DAY\s*(\d+)[\s,:\*\-]*(.*)', header_line, re.IGNORECASE)
            if day_match:
                day_num = day_match.group(1).strip()
                day_title = day_match.group(2).strip()
                day_title = re.sub(r'^[\s,:\*]+', '', day_title)
                day_title = day_title.replace('*', '-').strip()
                if not day_title:
                    day_title = f"{title} - Day {day_num}"
                
                days.append({
                    'day': f"Day {day_num}",
                    'title': day_title,
                    'body': '\n\n'.join(body_lines) if body_lines else header_line
                })
            else:
                if days:
                    days[-1]['body'] += '\n\n' + rd
                else:
                    days.append({
                        'day': "Day 1",
                        'title': "Day Trip Itinerary",
                        'body': rd
                    })

    # Fallback if no itinerary days parsed but description contains itinerary info (e.g. day trips)
    if not days:
        days.append({
            'day': "Day 1",
            'title': title or "Tour Itinerary",
            'body': description
        })

    return {
        'title': title,
        'categories': categories,
        'meta': meta,
        'description': description,
        'days': days
    }

def get_tour_images(tour_folder_path):
    """Find images in image/ or images/ subfolder, excluding non-photo assets."""
    img_dir = None
    for name in ['images', 'image', 'IMAGE', 'IMAGES']:
        candidate = os.path.join(tour_folder_path, name)
        if os.path.isdir(candidate):
            img_dir = candidate
            break

    if not img_dir:
        return []

    valid_extensions = ('.jpg', '.jpeg', '.png', '.webp', '.gif')
    images = []
    for f in sorted(os.listdir(img_dir)):
        # Exclude old theme graphics like curbe-bottom.png
        if f.lower() in ['curbe-bottom.png', 'thumb.jpg', 'logo.png']:
            continue
        if f.lower().endswith(valid_extensions):
            images.append((f, os.path.join(img_dir, f)))
            
    return images

def find_tour_folders():
    """Find all tour directories across search paths."""
    base_dir = None
    for sp in SEARCH_PATHS:
        if os.path.exists(sp):
            base_dir = sp
            break

    if not base_dir:
        print(f"Error: Neither 'site/by-category' nor 'by-category' found.")
        sys.exit(1)

    tours = []
    for root, dirs, files in os.walk(base_dir):
        if "tour-info.txt" in files:
            category_name = os.path.basename(os.path.dirname(root))
            tour_folder_name = os.path.basename(root)
            tours.append({
                'category_folder': category_name,
                'tour_folder': tour_folder_name,
                'path': root,
                'info_txt': os.path.join(root, "tour-info.txt")
            })
    return tours

def sanitize_for_json(text):
    """Strip control characters (except tab/LF/CR) and collapse whitespace for safe JSON embedding."""
    result = []
    for ch in text:
        cp = ord(ch)
        if cp < 0x20 and ch not in ('\t', '\n', '\r'):
            result.append(' ')
        else:
            result.append(ch)
    import re as _re
    return _re.sub(r'[ \t\r\n]+', ' ', ''.join(result)).strip()


def generate_jsonld_block(title, description, canonical_url, image_web_src, duration_text, map_label):
    """
    Build a schema.org JSON-LD array (TouristTrip + BreadcrumbList) for a tour page.
    Only uses data verifiably present on the page; no prices or ratings are added.
    Returns a <script> tag string ready for injection into <head>.
    """
    import json as _json
    import re as _re

    BASE_URL = 'https://berber-magic-tours.com'
    ORGANIZER_ID = f'{BASE_URL}/#organization'

    # Derive absolute image URL
    if image_web_src.startswith('http'):
        abs_image = image_web_src
    elif image_web_src.startswith('/'):
        abs_image = BASE_URL + image_web_src
    else:
        abs_image = f'{BASE_URL}/tours/{image_web_src}'

    # Parse ISO 8601 duration from e.g. '2 days/ 1 night'
    duration_iso = None
    if duration_text:
        day_m = _re.search(r'(\d+)\s*day', duration_text, _re.IGNORECASE)
        if day_m:
            duration_iso = f'P{day_m.group(1)}D'

    safe_name  = sanitize_for_json(title)
    safe_desc  = sanitize_for_json(description)
    safe_dep   = sanitize_for_json(map_label) if map_label else 'Marrakech, Morocco'

    tour_block = {
        '@context': 'https://schema.org',
        '@type': 'TouristTrip',
        '@id': f'{canonical_url}#trip',
        'name': safe_name,
        'description': safe_desc,
        'url': canonical_url,
        'image': abs_image,
        'organizer': {'@type': 'TravelAgency', '@id': ORGANIZER_ID},
        'touristType': 'Adventure tourists',
        'provider': {'@type': 'TravelAgency', '@id': ORGANIZER_ID},
    }
    if duration_iso:
        tour_block['duration'] = duration_iso
    if safe_dep:
        tour_block['departureLocation'] = {'@type': 'Place', 'name': safe_dep}

    breadcrumb_block = {
        '@context': 'https://schema.org',
        '@type': 'BreadcrumbList',
        'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': f'{BASE_URL}/'},
            {'@type': 'ListItem', 'position': 2, 'name': safe_name, 'item': canonical_url},
        ]
    }

    json_str = _json.dumps([tour_block, breadcrumb_block], ensure_ascii=False, indent=2)
    return (
        '    <script type="application/ld+json">\n'
        f'    {json_str}\n'
        '    </script>\n'
    )


def generate_html(tour_info, tour_images, template_content, tour_folder_name):
    """Inject tour data into the master HTML template."""
    title = tour_info['title'] or tour_folder_name.replace('-', ' ').title()
    categories = tour_info['categories'] or "Morocco Tours"
    duration = tour_info['meta'].get('duration', 'Custom Duration')
    location = tour_info['meta'].get('location', 'High Atlas, Morocco')
    description = tour_info['description']

    # 1. Image handling - Copy images to each directory in OUTPUT_DIRS
    out_img_rel_dir = os.path.join("images", tour_folder_name)
    copied_images = []
    for fname, fpath in tour_images:
        for out_dir in OUTPUT_DIRS:
            out_img_abs_dir = os.path.join(out_dir, out_img_rel_dir)
            os.makedirs(out_img_abs_dir, exist_ok=True)
            dest_path = os.path.join(out_img_abs_dir, fname)
            shutil.copy2(fpath, dest_path)
        # Web relative path from output HTML
        web_src = f"images/{tour_folder_name}/{fname}"
        copied_images.append((fname, web_src))

    # Fallback images if no tour images found
    if not copied_images:
        fallback_srcs = [
            "../assets/images/trek1.jpg",
            "../assets/images/trek2.jpg",
            "../assets/images/trek3.jpg",
            "../assets/images/trek4.jpg"
        ]
        copied_images = [(f"fallback_{i}", src) for i, src in enumerate(fallback_srcs)]

    hero_bg_src = copied_images[0][1]

    # 2. Adjust relative asset and page links for output files in tours/
    html = template_content
    html = re.sub(r'href=["\']assets/', 'href="../assets/', html)
    html = re.sub(r'src=["\']assets/', 'src="../assets/', html)
    html = re.sub(r'href=["\']index\.html', 'href="../index.html', html)
    # Rewrite root category page links (e.g. href="climb-mount-toubkal.html" -> href="../climb-mount-toubkal.html")
    cat_pages = [
        "marrakech-day-trips.html", "trek-and-hike.html", "climb-mount-toubkal.html",
        "berber-village-treks.html", "combine-toubkal-and-villages.html", "biking-in-morocco.html",
        "combine-atlas-mountains-and-desert.html", "combine-berber-villages-and-sahara.html",
        "combine-toubkal-and-sahara.html", "sahara-desert-tours.html", "tours-from-marrakech.html",
        "tours-from-casablanca.html", "tours-from-fes.html", "morocco-tours.html"
    ]
    for cp in cat_pages:
        html = html.replace(f'href="{cp}"', f'href="../{cp}"')

    # 3. Update Title & Meta description
    html = re.sub(r'<title>.*?</title>', f'<title>{escape(title)} | Berber Magic Tours</title>', html, flags=re.DOTALL)
    
    clean_meta_desc = escape(description[:160].replace('\n', ' ').strip())
    html = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{clean_meta_desc}">', html, flags=re.DOTALL)

    # 4. Update Header Hero Title & Breadcrumb
    html = re.sub(
        r'<section class="page-header".*?>',
        f'<section class="page-header" style="background-image: url(\'{hero_bg_src}\');">',
        html
    )
    html = re.sub(
        r'<h1 class="page-title text-white">.*?</h1>',
        f'<h1 class="page-title text-white">{escape(title)}</h1>',
        html,
        flags=re.DOTALL
    )

    first_cat = categories.split(",")[0].strip() if categories else "Tours"
    breadcrumb_html = (
        f'<div class="breadcrumb text-white">\n'
        f'                <a href="../index.html" class="text-white">Home</a> <span>/</span> '
        f'<a href="../index.html#tours" class="text-white">{escape(first_cat)}</a> <span>/</span> '
        f'{escape(title)}\n'
        f'            </div>'
    )
    html = re.sub(r'<div class="breadcrumb text-white">.*?</div>', breadcrumb_html, html, flags=re.DOTALL)

    # 5. Build Photo Strip Gallery HTML
    photo_strip_items = []
    for idx, (fname, web_src) in enumerate(copied_images):
        webp_src = web_src.rsplit('.', 1)[0] + '.webp'
        photo_strip_items.append(
            f'                    <a href="{web_src}" class="photo-strip-item gallery-trigger" data-index="{idx}">\n'
            f'                        <picture><source srcset="{webp_src}" type="image/webp"><img src="{web_src}" alt="{escape(title)} Photo {idx + 1}" loading="lazy"></picture>\n'
            f'                        <div class="photo-strip-overlay"><i class="fas fa-expand-arrows-alt"></i></div>\n'
            f'                    </a>'
        )
    
    new_photo_strip_wrapper = (
        f'<div class="photo-strip-wrapper mb-5">\n'
        f'                <div class="photo-strip-scroll">\n'
        + '\n'.join(photo_strip_items) + '\n'
        f'                </div>\n'
        f'                <p class="photo-strip-hint"><i class="fas fa-hand-point-right"></i> Swipe to explore photos</p>\n'
        f'            </div>'
    )
    html = re.sub(
        r'<div class="photo-strip-wrapper mb-5">.*?<p class="photo-strip-hint"><i class="fas fa-hand-point-right"></i> Swipe to explore photos</p>\s*</div>',
        new_photo_strip_wrapper,
        html,
        flags=re.DOTALL
    )

    # 6. Update Lightbox JS galleryImages Array
    js_images = []
    for idx, (fname, web_src) in enumerate(copied_images):
        js_images.append(f"            {{ src: '{web_src}', alt: '{escape(title)} Photo {idx + 1}' }}")
    js_gallery_code = "const galleryImages = [\n" + ",\n".join(js_images) + "\n        ];"
    html = re.sub(r'const galleryImages = \[.*?\];', js_gallery_code, html, flags=re.DOTALL)

    # 7. Update Tour Overview / Description Section
    desc_paragraphs = [p.strip() for p in description.split('\n\n') if p.strip()]
    if not desc_paragraphs:
        desc_paragraphs = [description]
    
    desc_html_blocks = []
    for i, p_text in enumerate(desc_paragraphs):
        if i == 0:
            desc_html_blocks.append(f'<p class="lead-text">{escape(p_text)}</p>')
        else:
            desc_html_blocks.append(f'<p>{escape(p_text)}</p>')

    overview_block_html = (
        f'<div class="tour-content-block premium-card">\n'
        f'                        <div class="card-header-accent"></div>\n'
        f'                        <h2 class="mb-3"><i class="fas fa-map-marked-alt text-primary"></i> Tour Overview</h2>\n'
        f'                        ' + '\n                        '.join(desc_html_blocks) + '\n'
        f'                    </div>'
    )

    html = re.sub(
        r'<div class="tour-content-block premium-card">\s*<div class="card-header-accent"></div>\s*<h2 class="mb-3">.*?Tour Overview</h2>.*?</div>\s*(?=<div class="tour-content-block premium-card mt-5">)',
        overview_block_html + '\n\n                    ',
        html,
        flags=re.DOTALL
    )

    # 8. Build Detailed Itinerary HTML Section
    itinerary_items_html = []
    for day in tour_info['days']:
        day_badge = day['day']
        day_title = day['title']
        body_text = day['body']

        paragraphs = [p.strip() for p in body_text.split('\n\n') if p.strip()]
        p_html = "".join([f'<p>{escape(p)}</p>' for p in paragraphs]) if paragraphs else f'<p>{escape(body_text)}</p>'

        itinerary_items_html.append(
            f'                            <!-- {day_badge} -->\n'
            f'                            <div class="timeline-item">\n'
            f'                                <div class="timeline-marker"></div>\n'
            f'                                <div class="timeline-content">\n'
            f'                                    <div class="day-badge">{escape(day_badge)}</div>\n'
            f'                                    <h3>{escape(day_title)}</h3>\n'
            f'                                    {p_html}\n'
            f'                                </div>\n'
            f'                            </div>'
        )

    itinerary_block_html = (
        f'<div class="tour-content-block premium-card mt-5">\n'
        f'                        <div class="card-header-accent"></div>\n'
        f'                        <h2 class="mb-4"><i class="fas fa-route text-primary"></i> Detailed Itinerary</h2>\n'
        f'                        <div class="itinerary-timeline-premium">\n'
        + '\n'.join(itinerary_items_html) + '\n'
        f'                        </div>\n'
        f'                    </div>'
    )

    html = re.sub(
        r'<div class="tour-content-block premium-card mt-5">\s*<div class="card-header-accent"></div>\s*<h2 class="mb-4">.*?Detailed Itinerary</h2>.*?</div>\s*</div>\s*(?=<!-- Included / Not Included -->)',
        itinerary_block_html + '\n\n                    ',
        html,
        flags=re.DOTALL
    )

    # 9. Update Booking Widget details
    html = html.replace('value="2 Days Azzaden Valley Trek"', f'value="{escape(title)}"')
    html = re.sub(
        r'<p class="widget-subtitle mb-4">.*?</p>',
        f'<p class="widget-subtitle mb-4">Reserve your {escape(title)} today.</p>',
        html
    )

    # 10. Update Custom Map Section & Map Info Strip
    map_url, map_label = get_map_embed_url_and_title(tour_folder_name, title, categories, location)
    
    map_section_html = (
        f'<div class="tour-map-section mt-5">\n'
        f'                        <h3 class="mb-3"><i class="fas fa-map-marker-alt text-primary"></i> Trek Location</h3>\n'
        f'                        <div class="tour-map-wrapper">\n'
        f'                            <iframe\n'
        f'                                src="{escape(map_url)}"\n'
        f'                                width="100%"\n'
        f'                                height="380"\n'
        f'                                style="border:0; border-radius: 14px; display: block;"\n'
        f'                                allowfullscreen=""\n'
        f'                                loading="lazy"\n'
        f'                                referrerpolicy="no-referrer-when-downgrade"\n'
        f'                                title="{escape(title)} Location - {escape(map_label)}">\n'
        f'                            </iframe>\n'
        f'                        </div>\n'
        f'                        <div class="map-info-strip">\n'
        f'                            <span><i class="fas fa-map-pin"></i> {escape(map_label)}</span>\n'
        f'                            <span><i class="fas fa-mountain"></i> {escape(categories)}</span>\n'
        f'                            <span><i class="fas fa-road"></i> Duration: {escape(duration)}</span>\n'
        f'                        </div>\n'
        f'                    </div>'
    )
    html = re.sub(r'<div class="tour-map-section mt-5">.*?</div>\s*</div>\s*(?=\n\s*<!-- Sidebar Content)', map_section_html + '\n\n                </div>', html, flags=re.DOTALL)

    # 11. Inject schema.org JSON-LD (TouristTrip + BreadcrumbList) before </head>
    #     Only inject if not already present (prevents duplicates on re-runs).
    if 'application/ld+json' not in html:
        slug = tour_folder_name
        canonical_url = f'https://berber-magic-tours.com/tours/{slug}'
        first_image_src = copied_images[0][1] if copied_images else '/assets/images/logo.png'
        jsonld_script = generate_jsonld_block(
            title=title,
            description=description,
            canonical_url=canonical_url,
            image_web_src=first_image_src,
            duration_text=duration,
            map_label=map_label
        )
        html = re.sub(r'(</head>)', jsonld_script + r'\1', html, count=1, flags=re.IGNORECASE)

    return html

def main():
    if not os.path.exists(MASTER_TEMPLATE_PATH):
        print(f"Error: Master template '{MASTER_TEMPLATE_PATH}' not found in current directory.")
        sys.exit(1)

    with open(MASTER_TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        template_content = f.read()

    for out_dir in OUTPUT_DIRS:
        os.makedirs(out_dir, exist_ok=True)
    tours = find_tour_folders()

    print(f"Found {len(tours)} tour folder(s). Processing...")

    for tour in tours:
        tour_folder_name = tour['tour_folder']
        info_txt_path = tour['info_txt']
        
        print(f"\nProcessing tour: {tour_folder_name}")
        tour_info = parse_tour_info(info_txt_path)
        tour_images = get_tour_images(tour['path'])
        
        print(f"  Title: {tour_info['title']}")
        print(f"  Categories: {tour_info['categories']}")
        print(f"  Meta: {tour_info['meta']}")
        print(f"  Days parsed: {len(tour_info['days'])}")
        print(f"  Images found: {len(tour_images)}")

        generated_html = generate_html(tour_info, tour_images, template_content, tour_folder_name)

        output_filename = f"{tour_folder_name}.html"
        for out_dir in OUTPUT_DIRS:
            output_filepath = os.path.join(out_dir, output_filename)
            with open(output_filepath, 'w', encoding='utf-8') as f:
                f.write(generated_html)
            print(f"  Successfully generated: {output_filepath}")

    print(f"\nAll tours processed! Output HTML files saved in {OUTPUT_DIRS}.")

if __name__ == "__main__":
    main()
