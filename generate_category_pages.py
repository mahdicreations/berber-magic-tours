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

# Mapping of categories to curated high-res background images in /assets/images/
HERO_IMAGES = {
    "marrakech-day-trips": "/assets/images/tour1.png",
    "trek-and-hike": "/assets/images/trek1.jpg",
    "climb-mount-toubkal": "/assets/images/blog-toubkal.jpg",
    "berber-village-treks": "/assets/images/blog-valleys.jpg",
    "combine-toubkal-and-villages": "/assets/images/trek5.jpg",
    "biking-in-morocco": "/assets/images/trek6.jpg",
    "combine-atlas-mountains-and-desert": "/assets/images/combine1.jpg",
    "combine-berber-villages-and-sahara": "/assets/images/combine2.jpg",
    "combine-toubkal-and-sahara": "/assets/images/combine3.jpg",
    "sahara-desert-tours": "/assets/images/blog-sahara.jpg",
    "tours-from-marrakech": "/assets/images/tour2.png",
    "tours-from-casablanca": "/assets/images/morocco1.jpg",
    "tours-from-fes": "/assets/images/morocco2.jpg",
    "morocco-tours": "/assets/images/morocco3.jpg"
}

# Category Metadata
CATEGORIES = [
    {
        "slug": "marrakech-day-trips",
        "title": "Marrakech Day Trips",
        "subtitle": "Unforgettable Excursions from Marrakech",
        "description": "Explore scenic valleys, waterfalls, authentic Berber villages, and Atlas foothills on our curated day trips from Marrakech.",
        "search_pattern": "marrakech-day-trips"
    },
    {
        "slug": "trek-and-hike",
        "title": "Trek & Hike in the Atlas Mountains",
        "subtitle": "Immersive Mountain Adventures & Alpine Passes",
        "description": "Discover our full range of trekking tours in the High Atlas Mountains—from short day walks to multi-day summits and valley loops.",
        "search_pattern": "trek"
    },
    {
        "slug": "climb-mount-toubkal",
        "title": "Climb Mount Toubkal",
        "subtitle": "North Africa's Highest Peak (4,167m)",
        "description": "Summit Jebel Toubkal with certified local Berber guides. Summer treks, winter mountaineering, and acclimatization routes available.",
        "search_pattern": "toubkal"
    },
    {
        "slug": "berber-village-treks",
        "title": "Berber Village Treks",
        "subtitle": "Culture, Hospitality & Stone Villages",
        "description": "Walk between ancient clay hamlets, meet welcoming local families, and experience authentic mountain life in High Atlas valleys.",
        "search_pattern": "village"
    },
    {
        "slug": "combine-toubkal-and-villages",
        "title": "Combine Toubkal & Berber Villages",
        "subtitle": "The Complete High Atlas Experience",
        "description": "Combine the thrill of climbing Mount Toubkal with peaceful village hiking through terraced walnut orchards and alpine valleys.",
        "search_pattern": "combine"
    },
    {
        "slug": "biking-in-morocco",
        "title": "Biking & Cycling in Morocco",
        "subtitle": "Mountain Biking across Atlas Trails & Deserts",
        "description": "Ride through rugged mountain passes, Berber dirt trails, and panoramic desert landscapes with professional support.",
        "search_pattern": "bik"
    },
    {
        "slug": "combine-atlas-mountains-and-desert",
        "title": "Combine Atlas Mountains & Sahara Desert",
        "subtitle": "From Snow Peaks to Golden Dunes",
        "description": "Experience Morocco's two greatest landscapes—the majestic High Atlas Mountains and the golden dunes of the Sahara Desert.",
        "search_pattern": "desert"
    },
    {
        "slug": "combine-berber-villages-and-sahara",
        "title": "Combine Berber Villages & Sahara Desert",
        "subtitle": "Cultural Valleys & Desert Glamping",
        "description": "Immerse yourself in mountain village traditions before embarking on a camel safari to private luxury Sahara camps.",
        "search_pattern": "sahara"
    },
    {
        "slug": "combine-toubkal-and-sahara",
        "title": "Combine Toubkal & Sahara Desert",
        "subtitle": "High Altitude Summit to Desert Oasis",
        "description": "The ultimate adventure itinerary: climb North Africa's highest summit then relax under the starry Sahara night skies.",
        "search_pattern": "toubkal"
    },
    {
        "slug": "sahara-desert-tours",
        "title": "Sahara Desert Tours",
        "subtitle": "Merzouga, Zagora & Erg Chebbi Glamping",
        "description": "Ride camels over golden sand dunes, stay in luxury desert camps, and watch unforgettable desert sunrises and sunsets.",
        "search_pattern": "desert"
    },
    {
        "slug": "tours-from-marrakech",
        "title": "Sahara Tours from Marrakech",
        "subtitle": "Classic Desert Routes via Ait Ben Haddou",
        "description": "Traverse the High Atlas Tizi n'Tichka pass to Ait Ben Haddou Kasbah and onward to the Merzouga or Zagora dunes.",
        "search_pattern": "marrakech"
    },
    {
        "slug": "tours-from-casablanca",
        "title": "Morocco Tours from Casablanca",
        "subtitle": "Imperial Cities, Coastlines & Deserts",
        "description": "Start your Moroccan journey from Casablanca Hassan II Mosque and travel through Rabat, Fes, Marrakech, and the Sahara.",
        "search_pattern": "casablanca"
    },
    {
        "slug": "tours-from-fes",
        "title": "Desert Tours from Fes",
        "subtitle": "Through Cedar Forests & Middle Atlas to Dunes",
        "description": "Journey south from Fes through Ifrane cedar forests and Ziz Valley palm groves to the magnificent Erg Chebbi dunes.",
        "search_pattern": "fes"
    },
    {
        "slug": "morocco-tours",
        "title": "Grand Morocco Imperial Tours",
        "subtitle": "Custom Tailored Morocco Itineraries",
        "description": "Comprehensive private tours covering Morocco's imperial cities, High Atlas mountains, Sahara desert, and Atlantic coast.",
        "search_pattern": "morocco"
    }
]

# Build Header Navigation HTML
def build_header_html(active_slug):
    return f"""<header id="header" class="header">
        <div class="top-bar">
            <div class="container top-bar-container">
                <div class="top-bar-left">
                    <a href="https://wa.me/212653274190" target="_blank"><i class="fab fa-whatsapp"></i> +212 653 274 190</a>
                    <a href="mailto:info@berber-magic-tours.com"><i class="far fa-envelope"></i> info@berber-magic-tours.com</a>
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
                <a href="/"><img src="/assets/images/logo.png" alt="Berber Magic Tours"></a>
            </div>
            
            <nav class="nav">
                <ul class="nav-list">
                    <li><a href="/">Home</a></li>
                    <li><a href="/marrakech-day-trips" class="{'active' if active_slug=='marrakech-day-trips' else ''}">Marrakech Day Trips</a></li>
                    
                    <li class="dropdown">
                        <a href="/trek-and-hike" class="{'active' if active_slug in ['trek-and-hike','climb-mount-toubkal','berber-village-treks','combine-toubkal-and-villages','biking-in-morocco'] else ''}">Trek &amp; Hike <i class="fas fa-chevron-down"></i></a>
                        <ul class="dropdown-menu">
                            <li><a href="/climb-mount-toubkal">Climb Mount Toubkal</a></li>
                            <li><a href="/berber-village-treks">Berber Village Treks</a></li>
                            <li><a href="/combine-toubkal-and-villages">Combine Toubkal &amp; Villages</a></li>
                            <li><a href="/biking-in-morocco">Biking in Morocco</a></li>
                        </ul>
                    </li>
                    
                    <li class="dropdown">
                        <a href="/combine-atlas-mountains-and-desert" class="{'active' if active_slug in ['combine-atlas-mountains-and-desert','combine-berber-villages-and-sahara','combine-toubkal-and-sahara'] else ''}">Combine Atlas Mountains &amp; Desert <i class="fas fa-chevron-down"></i></a>
                        <ul class="dropdown-menu">
                            <li><a href="/combine-berber-villages-and-sahara">Combine Berber Villages &amp; Sahara</a></li>
                            <li><a href="/combine-toubkal-and-sahara">Combine Toubkal &amp; Sahara</a></li>
                        </ul>
                    </li>
                    
                    <li class="dropdown">
                        <a href="#" class="{'active' if active_slug in ['sahara-desert-tours','tours-from-marrakech','tours-from-casablanca','tours-from-fes','morocco-tours'] else ''}">Other Tours <i class="fas fa-chevron-down"></i></a>
                        <ul class="dropdown-menu">
                            <li class="dropdown-submenu">
                                <a href="/sahara-desert-tours">Sahara Desert Tours <i class="fas fa-chevron-right"></i></a>
                                <ul class="dropdown-menu">
                                    <li><a href="/tours-from-marrakech">Tours from Marrakech</a></li>
                                    <li><a href="/tours-from-casablanca">Tours from Casablanca</a></li>
                                    <li><a href="/tours-from-fes">Tours from Fes</a></li>
                                </ul>
                            </li>
                            <li><a href="/morocco-tours">Morocco Tours</a></li>
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
                <a href="/contact" class="btn btn-primary"><i class="fas fa-envelope"></i> Contact Us</a>
                <button class="mobile-menu-btn"><i class="fas fa-bars"></i></button>
            </div>
        </div>
    </header>"""

# Parse existing tours HTML files to extract title, duration, image, link
def parse_tour_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Extract title
        title_m = re.search(r'<title>(.*?)(?:\||-)</title>', content, re.IGNORECASE)
        title = title_m.group(1).strip() if title_m else os.path.basename(filepath).replace(".html", "").replace("-", " ").title()
        
        # Extract meta description
        desc_m = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', content, re.IGNORECASE)
        desc = desc_m.group(1).strip() if desc_m else "Experience an authentic guided tour in Morocco with local Berber experts."
        
        # Extract image
        img_m = re.search(r'background-image:\s*url\(["\']?([^"\']+)["\']?\)', content)
        img = img_m.group(1).strip() if img_m else "/assets/images/tour1.png"
        if not img.startswith("/assets/"):
            img = "/assets/images/tour1.png"

        # Determine relative link
        rel_link = "/" + os.path.basename(filepath).replace(".html", "")
        if filepath.startswith("tours/") or "\\tours\\" in filepath:
            rel_link = "/tours/" + os.path.basename(filepath).replace(".html", "")
            
        return {
            "title": title,
            "description": desc,
            "image": img,
            "link": rel_link
        }
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return None

# Generate Category Page HTML
def generate_category_page(cat):
    slug = cat["slug"]
    title = cat["title"]
    subtitle = cat["subtitle"]
    description = cat["description"]
    hero_bg = HERO_IMAGES.get(slug, "/assets/images/tour1.png")
    
    header_html = build_header_html(slug)
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-CTF6X8R87Z"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'G-CTF6X8R87Z');
    </script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{escape(title)} | Berber Magic Tours</title>
    <meta name="description" content="{escape(description)}">
    <link rel="canonical" href="https://berber-magic-tours.com/{slug}" />
    <meta property="og:title" content="{escape(title)} | Berber Magic Tours">
    <meta property="og:description" content="{escape(description)}">
    <meta property="og:image" content="https://berber-magic-tours.com{hero_bg}">
    <meta property="og:url" content="https://berber-magic-tours.com/{slug}">
    <meta property="og:type" content="website">
    <link rel="stylesheet" href="/assets/css/style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Style+Script&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/lipis/flag-icons@7.0.0/css/flag-icons.min.css" />
    <style>
        /* Force white header for category header */
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

        /* Category Hero Styles with High Contrast White Title */
        .category-hero {{
            background: linear-gradient(180deg, rgba(15, 23, 42, 0.7) 0%, rgba(15, 23, 42, 0.88) 100%), url('{hero_bg}') center/cover no-repeat;
            position: relative;
            padding: 110px 0 70px 0;
            color: #ffffff !important;
            text-align: center;
        }}
        .category-hero h1,
        .category-hero .section-title {{
            font-family: var(--font-heading);
            font-size: 2.8rem;
            font-weight: 700;
            color: #ffffff !important;
            margin-bottom: 12px;
            text-shadow: 0 2px 12px rgba(0,0,0,0.6);
        }}
        .category-hero .subtitle {{
            font-size: 1.15rem;
            color: var(--primary) !important;
            margin-bottom: 16px;
            font-weight: 600;
            text-shadow: 0 1px 6px rgba(0,0,0,0.5);
        }}
        .category-hero .breadcrumb {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            font-size: 0.92rem;
            color: rgba(255,255,255,0.9) !important;
            text-shadow: 0 1px 4px rgba(0,0,0,0.5);
        }}
        .category-hero .breadcrumb a {{
            color: #ffffff !important;
            text-decoration: underline;
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
        .tour-card-body {{
            padding: 24px;
            display: flex;
            flex-direction: column;
            flex-grow: 1;
        }}
        .tour-card-title {{
            font-size: 1.3rem;
            color: var(--secondary);
            font-family: var(--font-heading);
            line-height: 1.3;
            margin-bottom: 10px;
        }}
        .tour-card-text {{
            font-size: 0.95rem;
            color: #555;
            flex-grow: 1;
            line-height: 1.6;
            margin-bottom: 20px;
        }}
        .btn-sm {{
            padding: 10px 22px;
            font-size: 0.9rem;
        }}
    </style>
</head>
<body>

    {header_html}

    <!-- Mobile Menu -->
    <div class="mobile-menu">
        <div class="mobile-menu-header">
            <img src="/assets/images/logo.png" alt="Berber Magic Tours" class="mobile-logo">
            <button class="mobile-menu-close"><i class="fas fa-times"></i></button>
        </div>
        <ul class="mobile-nav-list">
            <li><a href="/">Home</a></li>
            <li><a href="/about-us">About Us</a></li>
            <li><a href="/faq">FAQ</a></li>
            <li><a href="/marrakech-day-trips">Marrakech Day Trips</a></li>
            <li><a href="/trek-and-hike">Trek &amp; Hike</a></li>
            <li><a href="/sahara-desert-tours">Sahara Desert Tours</a></li>
            <li><a href="/morocco-tours">Morocco Tours</a></li>
            <li><a href="/contact">Contact Us</a></li>
        </ul>
    </div>
    <div class="mobile-overlay"></div>

    <!-- Category Hero Section -->
    <section class="category-hero">
        <div class="container relative z-10">
            <h1 class="section-title">{escape(title)}</h1>
            <p class="subtitle">{escape(subtitle)}</p>
            <div class="breadcrumb">
                <a href="/">Home</a> <span>/</span> <span>{escape(title)}</span>
            </div>
        </div>
    </section>

    <!-- Tour Grid Section -->
    <section class="section bg-light">
        <div class="container">
            <div class="section-header text-center" style="max-width: 780px; margin: 0 auto 40px;">
                <p class="lead-text" style="font-size: 1.1rem; color: #475569; line-height: 1.7;">{escape(description)}</p>
                <div style="margin: 20px auto 0; width: 60px; height: 3px; background: var(--primary); border-radius: 2px;"></div>
            </div>

            <div class="tours-grid-container">
                <!-- Tour cards dynamically rendered -->
                <div class="tour-card">
                    <div class="tour-card-image" style="background-image: url('/assets/images/tour1.png');"></div>
                    <div class="tour-card-body">
                        <h3 class="tour-card-title">{escape(title)} Featured Experience</h3>
                        <p class="tour-card-text">{escape(description)}</p>
                        <div>
                            <a href="/contact" class="btn btn-primary btn-sm">Book This Tour <i class="fas fa-arrow-right"></i></a>
                        </div>
                    </div>
                </div>
                <div class="tour-card">
                    <div class="tour-card-image" style="background-image: url('/assets/images/tour2.png');"></div>
                    <div class="tour-card-body">
                        <h3 class="tour-card-title">Custom Private Experience</h3>
                        <p class="tour-card-text">Tailored private itinerary guided by native Berber mountain and desert guides.</p>
                        <div>
                            <a href="/contact" class="btn btn-primary btn-sm">Enquire Now <i class="fas fa-arrow-right"></i></a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container footer-container">
            <div class="footer-grid">
                <!-- Col 1: About -->
                <div class="footer-col about-col">
                    <img src="/assets/images/logo.png" alt="Berber Magic Tours" class="footer-logo">
                    <p class="footer-desc">Experience the magic of Morocco through the eyes of Locals. Let us help you find a journey of a lifetime.</p>
                    <ul class="footer-contact-list">
                        <li><i class="fas fa-map-marker-alt"></i> <span>Douar Imlil Poste Asni 42152 Marrakech</span></li>
                        <li><i class="fab fa-whatsapp"></i> <span>+212 653 274 190</span></li>
                        <li><i class="fas fa-envelope"></i> <a href="mailto:info@berber-magic-tours.com">info@berber-magic-tours.com</a></li>
                    </ul>
                    <div class="social-links mt-4">
                        <a href="#" target="_blank" title="Facebook"><i class="fab fa-facebook-f"></i></a>
                        <a href="#" target="_blank" title="Instagram"><i class="fab fa-instagram"></i></a>
                        <a href="#" target="_blank" title="LinkedIn"><i class="fab fa-linkedin-in"></i></a>
                    </div>
                </div>
                
                <!-- Col 2: Menu -->
                <div class="footer-col links-col">
                    <h3 class="footer-title">Menu</h3>
                    <ul class="footer-links">
                        <li><a href="/">Home</a></li>
                        <li><a href="/about-us">About Us</a></li>
                        <li><a href="/faq">FAQ</a></li>
                        <li><a href="/marrakech-day-trips">Marrakech Day Trips</a></li>
                        <li><a href="/trek-and-hike">Trek &amp; Hike</a></li>
                        <li><a href="/sahara-desert-tours">Sahara Desert Tours</a></li>
                        <li><a href="/morocco-tours">Morocco Tours</a></li>
                        <li><a href="/blog">Blog</a></li>
                        <li><a href="/contact">Contact Us</a></li>
                    </ul>
                </div>
                
                <!-- Col 3: Popular Morocco -->
                <div class="footer-col popular-col">
                    <h3 class="footer-title">Popular Morocco</h3>
                    <ul class="footer-links">
                        <li><a href="/#trek-hike">Exploring Berber villages &amp; valleys</a></li>
                        <li><a href="/#trek-hike">Climbing Mount Toubkal</a></li>
                        <li><a href="/#tours">Day trips from Marrakech</a></li>
                        <li><a href="/#desert-tours">Desert Tours</a></li>
                        <li><a href="/#morocco-tours">Morocco Trips</a></li>
                        <li><a href="/#combine-tours">Combine Atlas mountains &amp; Desert</a></li>
                    </ul>
                </div>
                
                <!-- Col 4: TripAdvisor -->
                <div class="footer-col tripadvisor-col">
                    <h3 class="footer-title">Recommended</h3>
                    <div class="tripadvisor-widget-dark">
                        <div class="tripadvisor-logo-wrapper">
                            <i class="fab fa-tripadvisor"></i>
                            <span>Tripadvisor</span>
                        </div>
                        <div class="tripadvisor-rating">
                            <span class="bubble"></span>
                            <span class="bubble"></span>
                            <span class="bubble"></span>
                            <span class="bubble"></span>
                            <span class="bubble"></span>
                        </div>
                        <p>Recommended by travelers</p>
                        <a href="#" class="btn btn-tripadvisor" target="_blank">View Reviews</a>
                    </div>
                </div>
            </div>
            
            <div class="footer-bottom">
                <p>&copy; 2026 Berber Magic Tours. All Rights Reserved.</p>
                <div class="footer-legal-links">
                    <a href="/privacy-policy">Privacy Policy</a> | <a href="/terms-conditions">Terms &amp; Conditions</a>
                </div>
                <p class="footer-signature mt-2" style="font-size: 0.85rem; color: #94A3B8;">Designed with <i class="fas fa-heart" style="color: #D95D39;"></i> by <a href="https://mahdicreations.dev" target="_blank" rel="noopener" style="color: #ffffff; text-decoration: underline;">mahdicreations.dev</a></p>
            </div>
        </div>
    </footer>

    <script src="/assets/js/main.js?v=1.1"></script>
</body>
</html>"""
    
    filepath = os.path.join(r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours", f"{slug}.html")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated category page: {slug}.html")

for cat in CATEGORIES:
    generate_category_page(cat)

print("All category pages generated with visible white titles and background images successfully.")
