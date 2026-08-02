#!/usr/bin/env python3
"""
Category Pages Generator for Berber Magic Tours.

Generates category overview pages with responsive tour grids for every category
defined in the navigation menu hierarchy.
"""

import os
import sys
import glob
import re
from html import escape

# Search path for tours
BASE_DIR = "by-category"

# Navigation Header HTML generator (relative_prefix = "" for root, "../" for tours/)
def build_header_html(active_cat="", relative_prefix=""):
    home_link = f"{relative_prefix}index.html" if relative_prefix else "index.html"
    
    cats = {
        "marrakech-day-trips": f"{relative_prefix}marrakech-day-trips.html",
        "trek-and-hike": f"{relative_prefix}trek-and-hike.html",
        "climb-mount-toubkal": f"{relative_prefix}climb-mount-toubkal.html",
        "berber-village-treks": f"{relative_prefix}berber-village-treks.html",
        "combine-toubkal-and-villages": f"{relative_prefix}combine-toubkal-and-villages.html",
        "biking-in-morocco": f"{relative_prefix}biking-in-morocco.html",
        "combine-atlas-mountains-and-desert": f"{relative_prefix}combine-atlas-mountains-and-desert.html",
        "combine-berber-villages-and-sahara": f"{relative_prefix}combine-berber-villages-and-sahara.html",
        "combine-toubkal-and-sahara": f"{relative_prefix}combine-toubkal-and-sahara.html",
        "sahara-desert-tours": f"{relative_prefix}sahara-desert-tours.html",
        "tours-from-marrakech": f"{relative_prefix}tours-from-marrakech.html",
        "tours-from-casablanca": f"{relative_prefix}tours-from-casablanca.html",
        "tours-from-fes": f"{relative_prefix}tours-from-fes.html",
        "morocco-tours": f"{relative_prefix}morocco-tours.html",
    }
    
    logo_src = f"{relative_prefix}assets/images/logo.png"

    return f"""<header id="header" class="header">
        <div class="top-bar">
            <div class="container top-bar-container">
                <div class="top-bar-left">
                    <a href="https://wa.me/212653274190" target="_blank"><i class="fab fa-whatsapp"></i> +212 653 274 190</a>
                    <a href="mailto:contact@berber-magic-tours.com"><i class="far fa-envelope"></i> contact@berber-magic-tours.com</a>
                </div>
                <div class="top-bar-right">
                    <span><i class="fas fa-map-marker-alt"></i> Douar Imlil, Marrakech</span>
                    <div class="top-bar-socials">
                        <a href="#" target="_blank"><i class="fab fa-facebook-f"></i></a>
                        <a href="#" target="_blank"><i class="fab fa-instagram"></i></a>
                        <a href="#" target="_blank"><i class="fab fa-tripadvisor"></i></a>
                    </div>
                </div>
            </div>
        </div>

        <div class="container header-container">
            <div class="logo">
                <a href="{home_link}"><img src="{logo_src}" alt="Berber Magic Tours"></a>
            </div>
            
            <nav class="nav">
                <ul class="nav-list">
                    <li><a href="{home_link}">Home</a></li>
                    <li><a href="{cats['marrakech-day-trips']}" class="{'active' if active_cat=='marrakech-day-trips' else ''}">Marrakech Day Trips</a></li>
                    
                    <li class="dropdown">
                        <a href="{cats['trek-and-hike']}" class="{'active' if active_cat in ['trek-and-hike','climb-mount-toubkal','berber-village-treks','combine-toubkal-and-villages','biking-in-morocco'] else ''}">Trek & Hike <i class="fas fa-chevron-down"></i></a>
                        <ul class="dropdown-menu">
                            <li><a href="{cats['climb-mount-toubkal']}">Climb Mount Toubkal</a></li>
                            <li><a href="{cats['berber-village-treks']}">Berber Village Treks</a></li>
                            <li><a href="{cats['combine-toubkal-and-villages']}">Combine Toubkal & Villages</a></li>
                            <li><a href="{cats['biking-in-morocco']}">Biking in Morocco</a></li>
                        </ul>
                    </li>
                    
                    <li class="dropdown">
                        <a href="{cats['combine-atlas-mountains-and-desert']}" class="{'active' if active_cat in ['combine-atlas-mountains-and-desert','combine-berber-villages-and-sahara','combine-toubkal-and-sahara'] else ''}">Combine Atlas Mountains & Desert <i class="fas fa-chevron-down"></i></a>
                        <ul class="dropdown-menu">
                            <li><a href="{cats['combine-berber-villages-and-sahara']}">Combine Berber Villages & Sahara</a></li>
                            <li><a href="{cats['combine-toubkal-and-sahara']}">Combine Toubkal & Sahara</a></li>
                        </ul>
                    </li>
                    
                    <li class="dropdown">
                        <a href="#" class="{'active' if active_cat in ['sahara-desert-tours','tours-from-marrakech','tours-from-casablanca','tours-from-fes','morocco-tours'] else ''}">Other Tours <i class="fas fa-chevron-down"></i></a>
                        <ul class="dropdown-menu">
                            <li class="dropdown-submenu">
                                <a href="{cats['sahara-desert-tours']}">Sahara Desert Tours <i class="fas fa-chevron-right"></i></a>
                                <ul class="dropdown-menu">
                                    <li><a href="{cats['tours-from-marrakech']}">Tours from Marrakech</a></li>
                                    <li><a href="{cats['tours-from-casablanca']}">Tours from Casablanca</a></li>
                                    <li><a href="{cats['tours-from-fes']}">Tours from Fes</a></li>
                                </ul>
                            </li>
                            <li><a href="{cats['morocco-tours']}">Morocco Tours</a></li>
                        </ul>
                    </li>
                </ul>
            </nav>
            
            <div class="header-actions">
                <div class="header-flags">
                    <span class="fi fi-gb"></span>
                    <span class="fi fi-fr"></span>
                    <span class="fi fi-es"></span>
                </div>
                <a href="https://wa.me/212653274190" class="btn btn-whatsapp"><i class="fab fa-whatsapp"></i> Book Now</a>
                <button class="mobile-menu-btn"><i class="fas fa-bars"></i></button>
            </div>
        </div>
    </header>

    <!-- Mobile Menu -->
    <div class="mobile-menu">
        <div class="mobile-menu-header">
            <img src="{logo_src}" alt="Logo" class="mobile-logo">
            <button class="close-menu-btn"><i class="fas fa-times"></i></button>
        </div>
        <ul class="mobile-nav-list">
            <li><a href="{home_link}">Home</a></li>
            <li><a href="{cats['marrakech-day-trips']}">Marrakech Day Trips</a></li>
            <li><a href="{cats['trek-and-hike']}">Trek & Hike</a></li>
            <li><a href="{cats['climb-mount-toubkal']}">- Climb Mount Toubkal</a></li>
            <li><a href="{cats['berber-village-treks']}">- Berber Village Treks</a></li>
            <li><a href="{cats['combine-toubkal-and-villages']}">- Combine Toubkal & Villages</a></li>
            <li><a href="{cats['biking-in-morocco']}">- Biking in Morocco</a></li>
            <li><a href="{cats['combine-atlas-mountains-and-desert']}">Combine Atlas Mountains & Desert</a></li>
            <li><a href="{cats['combine-berber-villages-and-sahara']}">- Combine Berber Villages & Sahara</a></li>
            <li><a href="{cats['combine-toubkal-and-sahara']}">- Combine Toubkal & Sahara</a></li>
            <li><a href="{cats['sahara-desert-tours']}">Sahara Desert Tours</a></li>
            <li><a href="{cats['tours-from-marrakech']}">-- Tours from Marrakech</a></li>
            <li><a href="{cats['tours-from-casablanca']}">-- Tours from Casablanca</a></li>
            <li><a href="{cats['tours-from-fes']}">-- Tours from Fes</a></li>
            <li><a href="{cats['morocco-tours']}">Morocco Tours</a></li>
        </ul>
        <a href="https://wa.me/212653274190" class="btn btn-whatsapp mobile-btn"><i class="fab fa-whatsapp"></i> Book Now</a>
    </div>"""

def clean_text(text):
    if not text:
        return ""
    text = text.replace('\ufffd', "'")
    text = text.replace('â€™', "'").replace('â€"', "-").replace('â€œ', '"').replace('â€\x9d', '"')
    replacements = [('\u2019', "'"), ('\u2018', "'"), ('`', "'"), ('´', "'"), ('\u201c', '"'), ('\u201d', '"'), ('\u2013', '-'), ('\u2014', '-')]
    for old, new in replacements:
        text = text.replace(old, new)
    return text.strip()

def parse_tour_info(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        raw_content = f.read()
    content = clean_text(raw_content)

    title_m = re.search(r'^TOUR:\s*(.+)$', content, re.MULTILINE)
    title = title_m.group(1).strip() if title_m else ""

    cat_m = re.search(r'^Categories:\s*(.+)$', content, re.MULTILINE)
    categories = cat_m.group(1).strip() if cat_m else ""

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

    desc_match = re.search(r'DESCRIPTION:\s*\n(.*?)(?=\nITINERARY:|\nTOUR META:|\nIMAGES|\Z)', content, re.DOTALL)
    description = desc_match.group(1).strip() if desc_match else ""

    if not description or "(not available on the website)" in description.lower():
        dur_str = f"for {meta.get('duration')}" if meta.get('duration') else ""
        loc_str = meta.get('location', 'the High Atlas Mountains')
        description = (
            f"Embark on an unforgettable adventure {dur_str} with Berber Magic Tours. "
            f"Discover authentic Berber villages, stunning mountain landscapes, and rich local culture in {loc_str}."
        )

    return {
        'title': title,
        'categories': categories,
        'meta': meta,
        'description': description
    }

def get_tour_first_image(tour_folder_path, tour_folder_name):
    img_dir = None
    for name in ['images', 'image', 'IMAGE', 'IMAGES']:
        candidate = os.path.join(tour_folder_path, name)
        if os.path.isdir(candidate):
            img_dir = candidate
            break

    if not img_dir:
        return "assets/images/trek1.jpg"

    valid_extensions = ('.jpg', '.jpeg', '.png', '.webp', '.gif')
    for f in sorted(os.listdir(img_dir)):
        if f.lower() in ['curbe-bottom.png', 'thumb.jpg', 'logo.png']:
            continue
        if f.lower().endswith(valid_extensions):
            return f"tours/images/{tour_folder_name}/{f}"
            
    return "assets/images/trek1.jpg"

# Category Definitions
CATEGORIES_CONFIG = [
    {
        'slug': 'marrakech-day-trips',
        'title': 'Marrakech Day Trips',
        'subtitle': 'Unforgettable Excursions from Marrakech',
        'description': 'Explore scenic valleys, waterfalls, authentic Berber villages, and Atlas foothills on our curated day trips from Marrakech.',
        'folders': ['marrakech-day-trips']
    },
    {
        'slug': 'trek-and-hike',
        'title': 'Trek & Hike',
        'subtitle': 'Atlas Mountains Hiking & Summit Treks',
        'description': 'Discover our complete selection of mountain treks, valley hikes, and Toubkal ascents guided by local Berber experts.',
        'folders': ['climb-mount-toubkal', 'berber-village-treks', 'combine-atlas-and-sahara', 'trek-and-hike']
    },
    {
        'slug': 'climb-mount-toubkal',
        'title': 'Climb Mount Toubkal',
        'subtitle': 'Summit the Highest Peak in North Africa (4,167m)',
        'description': 'Challenge yourself with guided 2-day to 5-day climbs of Mount Toubkal with experienced local Berber guides and mule support.',
        'folders': ['climb-mount-toubkal']
    },
    {
        'slug': 'berber-village-treks',
        'title': 'Berber Village Treks',
        'subtitle': 'Authentic Cultural Treks in the High Atlas',
        'description': 'Walk through terraced valleys, walnut groves, and historic clay villages while staying in local Berber guesthouses.',
        'folders': ['berber-village-treks']
    },
    {
        'slug': 'combine-toubkal-and-villages',
        'title': 'Combine Toubkal & Villages',
        'subtitle': 'Mount Toubkal Ascent & Valley Exploration',
        'description': 'Experience the best of both worlds: scenic acclimatization walks through Berber villages followed by the Toubkal summit climb.',
        'folders': ['combine-toubkal-and-villages']
    },
    {
        'slug': 'biking-in-morocco',
        'title': 'Biking in Morocco',
        'subtitle': 'Mountain Biking Adventures in the Atlas Mountains',
        'description': 'Exhilarating mountain bike tours through rugged Atlas trails, mountain passes, and scenic Berber village valleys.',
        'folders': ['biking-in-morocco']
    },
    {
        'slug': 'combine-atlas-mountains-and-desert',
        'title': 'Combine Atlas Mountains & Desert',
        'subtitle': 'From High Peaks to Sahara Sand Dunes',
        'description': 'Combine mountain trekking in the High Atlas with camel rides and starry night luxury desert camps in Erg Chebbi, Merzouga.',
        'folders': ['combine-atlas-and-sahara', 'combine-atlas-mountains-and-desert', 'combine-berber-villages-and-sahara', 'combine-toubkal-and-sahara']
    },
    {
        'slug': 'combine-berber-villages-and-sahara',
        'title': 'Combine Berber Villages & Sahara',
        'subtitle': 'Berber Cultural Treks & Sahara Desert Expeditions',
        'description': 'Immerse yourself in mountain village life before traveling across the Dades and Todra gorges to the golden Sahara dunes.',
        'folders': ['combine-berber-villages-and-sahara']
    },
    {
        'slug': 'combine-toubkal-and-sahara',
        'title': 'Combine Toubkal & Sahara',
        'subtitle': 'Mount Toubkal Summit & Sahara Desert Tour',
        'description': 'Conquer Jebel Toubkal (4,167m) and reward your efforts with a scenic journey into the heart of the Erg Chebbi dunes.',
        'folders': ['combine-toubkal-and-sahara']
    },
    {
        'slug': 'sahara-desert-tours',
        'title': 'Sahara Desert Tours',
        'subtitle': 'Magical Journeys into the Dunes of Merzouga',
        'description': 'Experience camel treks, 4x4 desert drives, Berber music around campfires, and luxury desert camping in the Moroccan Sahara.',
        'folders': ['sahara-desert-tours', 'tours-from-marrakech', 'tours-from-casablanca', 'tours-from-fes']
    },
    {
        'slug': 'tours-from-marrakech',
        'title': 'Tours from Marrakech',
        'subtitle': 'Desert & Mountain Expeditions Departing from Marrakech',
        'description': 'Seamless private tours starting from Marrakech to the Sahara Desert, Ait Benhaddou, and High Atlas mountain passes.',
        'folders': ['tours-from-marrakech']
    },
    {
        'slug': 'tours-from-casablanca',
        'title': 'Tours from Casablanca',
        'subtitle': 'Morocco & Sahara Tours Starting in Casablanca',
        'description': 'Comprehensive Morocco itineraries departing from Casablanca, visiting Rabat, Chefchaouen, Fes, Merzouga, and Marrakech.',
        'folders': ['tours-from-casablanca']
    },
    {
        'slug': 'tours-from-fes',
        'title': 'Tours from Fes',
        'subtitle': 'Desert Tours Departing from Fes to Marrakech',
        'description': 'Travel through the Middle Atlas, Cedar Forests, Ziz Valley, Erg Chebbi dunes, and Dades Valley from Fes to Marrakech.',
        'folders': ['tours-from-fes']
    },
    {
        'slug': 'morocco-tours',
        'title': 'Morocco Tours',
        'subtitle': 'Grand Tours & Imperial City Circuit Highlights',
        'description': 'Discover the rich history, vibrant souks, ancient medinas, and diverse landscapes of Morocco on our signature grand tours.',
        'folders': ['morocco-tours']
    }
]

def load_tours_for_category(cat_config):
    matched_tours = []
    seen_paths = set()

    for root, dirs, files in os.walk(BASE_DIR):
        if "tour-info.txt" in files:
            category_folder = os.path.basename(os.path.dirname(root))
            tour_folder_name = os.path.basename(root)

            match = False
            if cat_config['slug'] == 'combine-toubkal-and-villages':
                if 'toubkal' in tour_folder_name and ('villages' in tour_folder_name or 'berber' in tour_folder_name):
                    match = True
            elif category_folder in cat_config['folders']:
                match = True
            elif cat_config['slug'] == 'trek-and-hike' and category_folder in ['climb-mount-toubkal', 'berber-village-treks', 'combine-atlas-and-sahara', 'combine-atlas-mountains-and-desert']:
                match = True

            if match and root not in seen_paths:
                seen_paths.add(root)
                info = parse_tour_info(os.path.join(root, "tour-info.txt"))
                cover_img = get_tour_first_image(root, tour_folder_name)
                matched_tours.append({
                    'folder_name': tour_folder_name,
                    'title': info['title'] or tour_folder_name.replace('-', ' ').title(),
                    'categories': info['categories'] or cat_config['title'],
                    'duration': info['meta'].get('duration', 'Custom Duration'),
                    'location': info['meta'].get('location', 'High Atlas, Morocco'),
                    'description': info['description'],
                    'cover_image': cover_img,
                    'link': f"tours/{tour_folder_name}.html"
                })

    return matched_tours

def generate_category_html(cat_config, tours):
    title = cat_config['title']
    subtitle = cat_config['subtitle']
    description = cat_config['description']
    slug = cat_config['slug']

    header_html = build_header_html(active_cat=slug, relative_prefix="")

    tour_cards_html = []
    for tour in tours:
        short_desc = tour['description'][:140].replace('\n', ' ') + "..." if len(tour['description']) > 140 else tour['description']
        first_cat = tour['categories'].split(',')[0].strip()
        tour_cards_html.append(f"""
                <!-- Tour Card: {escape(tour['title'])} -->
                <div class="tour-card-premium">
                    <div class="tour-card-image" style="background-image: url('{escape(tour['cover_image'])}');">
                        <div class="tour-card-overlay"></div>
                        <div class="tour-cat-badge">{escape(first_cat)}</div>
                    </div>
                    <div class="tour-card-body">
                        <div class="tour-card-meta mb-2">
                            <span><i class="fas fa-map-marker-alt text-primary"></i> {escape(tour['location'])}</span>
                            <span class="duration-pill"><i class="far fa-clock"></i> {escape(tour['duration'])}</span>
                        </div>
                        <h3 class="tour-card-title mb-3">{escape(tour['title'])}</h3>
                        <p class="tour-card-text mb-4">{escape(short_desc)}</p>
                        <div class="tour-card-footer">
                            <div class="tour-price-tag"><i class="fas fa-shield-alt text-primary"></i> Guided Trek</div>
                            <a href="{escape(tour['link'])}" class="btn-card-explore">Explore Tour <i class="fas fa-arrow-right"></i></a>
                        </div>
                    </div>
                </div>""")

    grid_content = "\n".join(tour_cards_html) if tour_cards_html else "<p class='lead-text text-center'>Tours coming soon for this category.</p>"

    hero_bg = tours[0]['cover_image'] if tours else "assets/images/slide1.png"

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{escape(title)} | Berber Magic Tours</title>
    <meta name="description" content="{escape(description)}">
    <link rel="stylesheet" href="assets/css/style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Style+Script&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/lipis/flag-icons@7.0.0/css/flag-icons.min.css" />
    <style>
        /* Force white header for category page header */
        #header.header {{
            background: white !important;
            background-image: none !important;
            padding: 10px 0 !important;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05) !important;
        }}
        #header.header .top-bar {{ 
            border-bottom: 1px solid rgba(0, 0, 0, 0.1) !important; 
        }}
        #header.header .top-bar-left a, 
        #header.header .top-bar-right span,
        #header.header .top-bar-socials a {{
            color: var(--secondary) !important;
        }}
        #header.header .top-bar-left a:hover,
        #header.header .top-bar-socials a:hover {{
            color: var(--primary) !important;
        }}
        #header.header .nav-list > li > a {{ color: var(--secondary) !important; }}
        #header.header .nav-list > li > a:hover, #header.header .nav-list > li > a.active {{ color: var(--primary) !important; }}
        #header.header .header-flags {{ border-right: 1px solid rgba(0, 0, 0, 0.1) !important; }}
        #header.header .mobile-menu-btn {{ color: var(--secondary) !important; }}

        .category-hero {{
            background-image: url('{escape(hero_bg)}');
            background-size: cover;
            background-position: center;
            position: relative;
            padding: 120px 0 80px;
            color: white;
            text-align: center;
        }}
        .category-hero-overlay {{
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            background: linear-gradient(180deg, rgba(0,0,0,0.6) 0%, rgba(0,0,0,0.85) 100%);
        }}
        .tours-grid-container {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
            gap: 30px;
            margin-top: 40px;
        }}
        .tour-card {{
            background: #ffffff;
            border-radius: 16px;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(0,0,0,0.08);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            display: flex;
            flex-direction: column;
            border: 1px solid rgba(0,0,0,0.05);
        }}
        .tour-card:hover {{
            transform: translateY(-8px);
            box-shadow: 0 15px 35px rgba(0,0,0,0.15);
        }}
        .tour-card-image {{
            height: 220px;
            background-size: cover;
            background-position: center;
            position: relative;
        }}
        .tour-card-badge {{
            position: absolute;
            bottom: 12px;
            right: 12px;
            background: rgba(0,0,0,0.75);
            color: #ffffff;
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 500;
            backdrop-filter: blur(4px);
        }}
        .tour-card-body {{
            padding: 24px;
            display: flex;
            flex-direction: column;
            flex-grow: 1;
        }}
        .tour-card-meta {{
            display: flex;
            gap: 15px;
            font-size: 0.88rem;
            color: #666;
        }}
        .tour-card-title {{
            font-size: 1.35rem;
            color: var(--secondary);
            font-family: var(--font-heading);
            line-height: 1.3;
        }}
        .tour-card-text {{
            font-size: 0.95rem;
            color: #555;
            flex-grow: 1;
            line-height: 1.6;
        }}
        .btn-sm {{
            padding: 10px 22px;
            font-size: 0.9rem;
        }}
    </style>
</head>
<body>

    {header_html}

    <!-- Category Hero Section -->
    <section class="category-hero">
        <div class="category-hero-overlay"></div>
        <div class="container relative z-10">
            <h1 class="section-title text-white">{escape(title)}</h1>
            <p class="subtitle text-white mb-3" style="color: var(--primary);">{escape(subtitle)}</p>
            <div class="breadcrumb text-white justify-content-center">
                <a href="index.html" class="text-white">Home</a> <span>/</span> {escape(title)}
            </div>
        </div>
    </section>

    <!-- Tour Grid Section -->
    <section class="section bg-light">
        <div class="container">
            <div class="section-header text-center" style="max-width: 780px; margin: 0 auto 40px;">
                <p class="lead-text">{escape(description)}</p>
                <div class="card-header-accent" style="margin: 20px auto 0; width: 60px;"></div>
            </div>

            <div class="tours-grid-container">
                {grid_content}
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer bg-secondary text-white">
        <div class="container footer-container">
            <div class="footer-col">
                <img src="assets/images/logo.png" alt="Berber Magic Tours" class="footer-logo mb-3" style="height: 50px;">
                <p>Authentic, immersive, and unforgettable trekking and tour experiences across the Atlas Mountains and Sahara Desert in Morocco.</p>
            </div>
            <div class="footer-col">
                <h3>Quick Links</h3>
                <ul class="footer-links">
                    <li><a href="index.html">Home</a></li>
                    <li><a href="marrakech-day-trips.html">Marrakech Day Trips</a></li>
                    <li><a href="trek-and-hike.html">Trek & Hike</a></li>
                    <li><a href="sahara-desert-tours.html">Sahara Desert Tours</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h3>Contact Us</h3>
                <p><i class="fas fa-map-marker-alt text-primary"></i> Douar Imlil, High Atlas, Morocco</p>
                <p><i class="fab fa-whatsapp text-primary"></i> +212 653 274 190</p>
                <p><i class="far fa-envelope text-primary"></i> contact@berber-magic-tours.com</p>
            </div>
        </div>
        <div class="footer-bottom text-center py-3" style="border-top: 1px solid rgba(255,255,255,0.1);">
            <div class="container">
                <p>&copy; 2026 Berber Magic Tours. All Rights Reserved.</p>
            </div>
        </div>
    </footer>

    <script src="assets/js/main.js"></script>
</body>
</html>"""
    return html

def main():
    print("Generating Category Pages...")
    for cat_config in CATEGORIES_CONFIG:
        slug = cat_config['slug']
        filename = f"{slug}.html"
        
        tours = load_tours_for_category(cat_config)
        print(f"\nCategory: {cat_config['title']} ({len(tours)} tour(s) found)")
        
        cat_html = generate_category_html(cat_config, tours)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(cat_html)
        print(f"  Created root category page: {filename}")
        
    print("\nAll Category Pages Generated Successfully!")

if __name__ == "__main__":
    main()
