import os
import re

root_dir = r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours"

category_files = [
    "marrakech-day-trips.html",
    "trek-and-hike.html",
    "climb-mount-toubkal.html",
    "berber-village-treks.html",
    "combine-toubkal-and-villages.html",
    "biking-in-morocco.html",
    "combine-atlas-mountains-and-desert.html",
    "combine-berber-villages-and-sahara.html",
    "combine-toubkal-and-sahara.html",
    "sahara-desert-tours.html",
    "tours-from-marrakech.html",
    "tours-from-casablanca.html",
    "tours-from-fes.html",
    "morocco-tours.html"
]

updated_count = 0

for fname in category_files:
    filepath = os.path.join(root_dir, fname)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    # 1. Convert relative asset paths to root-relative /assets/
    content = re.sub(r'(href|src)=["\']assets/', r'\1="/assets/', content)
    content = re.sub(r'url\(["\']?assets/', r'url("/assets/', content)
    
    # 2. Fix tour images and tour links to be root-relative /tours/
    content = re.sub(r'url\(["\']?tours/images/', r'url("/tours/images/', content)
    content = re.sub(r'href=["\']tours/', r'href="/tours/', content)
    
    # 3. Ensure white hero title CSS styling
    if '.category-hero h1' not in content:
        hero_style_fix = """
        /* High Contrast White Title for Category Hero */
        .category-hero h1, .category-hero .section-title, .page-header h1 {
            color: #ffffff !important;
            text-shadow: 0 2px 12px rgba(0, 0, 0, 0.7) !important;
        }
        .category-hero .subtitle {
            color: var(--primary) !important;
            text-shadow: 0 1px 6px rgba(0, 0, 0, 0.6) !important;
        }
        .category-hero .breadcrumb, .category-hero .breadcrumb a {
            color: #ffffff !important;
            text-shadow: 0 1px 4px rgba(0, 0, 0, 0.5) !important;
        }
        """
        content = content.replace("</style>", hero_style_fix + "\n    </style>")

    # 4. Remove Blog link from header nav list if present
    content = re.sub(r'<li><a href="[^"]*blog[^"]*"[^>]*>Blog</a></li>\s*', '', content)
    
    # 5. Add Blog link to footer links if missing
    if 'href="/blog"' not in content and 'href="blog"' not in content:
        if '<li><a href="contact">Contact Us</a></li>' in content:
            content = content.replace('<li><a href="contact">Contact Us</a></li>', '<li><a href="/blog">Blog</a></li>\n                        <li><a href="/contact">Contact Us</a></li>')
        elif '<li><a href="/contact">Contact Us</a></li>' in content:
            content = content.replace('<li><a href="/contact">Contact Us</a></li>', '<li><a href="/blog">Blog</a></li>\n                        <li><a href="/contact">Contact Us</a></li>')

    # 6. Ensure footer signature is present and updated
    if 'mahdicreations.dev' in content:
        content = re.sub(
            r'Designed with <i class="fas fa-heart"[^>]*></i> by <a href="https://mahdicreations.dev"[^>]*>mahdicreations.dev</a>',
            'Designed with <i class="fas fa-heart" style="color: #D95D39;"></i> by <a href="https://mahdicreations.dev" target="_blank" rel="noopener" style="color: #ffffff; text-decoration: underline;">mahdicreations.dev</a>',
            content
        )

    # 7. Use cache-busted JS main script
    content = content.replace('src="/assets/js/main.js"', 'src="/assets/js/main.js?v=1.1"')
    content = content.replace('src="assets/js/main.js"', 'src="/assets/js/main.js?v=1.1"')

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
        
    updated_count += 1
    print(f"Updated restored category file: {fname}")

print(f"Successfully processed {updated_count} restored category pages.")
