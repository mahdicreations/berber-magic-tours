import os
from pathlib import Path
from PIL import Image
import re

workspace = Path('c:/Users/el mahdi/Desktop/mahdicreations/berber-magic-tours')
artifacts = Path('c:/Users/el mahdi/.gemini/antigravity-ide/brain/4adf8579-152b-4f17-9090-a04c435dc2de')

# 1. Convert and copy OG image
og_src = artifacts / 'og_social_1789012403158.jpg'
og_dest = workspace / 'assets/images/og-social.webp'

if og_src.exists():
    try:
        img = Image.open(og_src)
        img.save(og_dest, format='WEBP', quality=85)
        print("OG Image saved successfully.")
    except Exception as e:
        print(f"Error saving image: {e}")

# 2. Inject Social Metadata and Contextual Links
domain = "https://berber-magic-tours.com"
og_image_url = f"{domain}/assets/images/og-social.webp"

def get_page_meta(content, filename):
    # Try to extract title
    title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
    title = title_match.group(1).strip() if title_match else "Berber Magic Tours"
    
    # Try to extract description
    desc_match = re.search(r'<meta\s+name="description"\s+content="(.*?)"', content, re.IGNORECASE)
    desc = desc_match.group(1).strip() if desc_match else "Experience authentic tours in Morocco."
    
    return title, desc

updated_files = 0

for html_file in workspace.rglob('*.html'):
    if '.git' in str(html_file) or 'scratch' in str(html_file):
        continue
        
    try:
        content = html_file.read_text(encoding='utf-8', errors='ignore')
        original = content
        
        title, desc = get_page_meta(content, html_file.name)
        
        # Build new metadata block
        twitter_meta = f"""
    <!-- Twitter/X Card Data -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:site" content="@BerberMagicTours">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{desc}">
    <meta name="twitter:image" content="{og_image_url}">
"""
        # Remove old og:image
        content = re.sub(r'<meta property="og:image"[^>]*>', '', content)
        # Remove old twitter meta if any (clean up)
        content = re.sub(r'<meta name="twitter:[^>]*>', '', content)
        
        # Insert og:image and twitter meta before </head>
        new_og_image = f'<meta property="og:image" content="{og_image_url}">'
        head_end = content.find('</head>')
        if head_end != -1:
            content = content[:head_end] + f"    {new_og_image}\n{twitter_meta}\n" + content[head_end:]

        # Contextual Linking based on filename
        prefix = '../' if (html_file.parent.name in ['tours', 'blog']) else ''
        overview_match = re.search(r'<div class="tour-overview">', content)
        
        if overview_match and "Recommended Reading:" not in content:
            link = ""
            if 'toubkal' in html_file.name:
                link = f'<p><strong>Recommended Reading:</strong> Planning your ascent? Check out our <a href="{prefix}blog/ultimate-guide-trekking-mount-toubkal.html" class="text-primary">Ultimate Guide to Trekking Mount Toubkal</a> or read about a <a href="{prefix}blog/mount-toubkal-winter-ascent-guide.html" class="text-primary">Winter Ascent</a>.</p>'
            elif 'desert' in html_file.name or 'sahara' in html_file.name:
                link = f'<p><strong>Recommended Reading:</strong> Not sure which dunes to visit? Read our guide on <a href="{prefix}blog/sahara-desert-erg-chebbi-vs-chigaga.html" class="text-primary">Erg Chebbi vs Erg Chigaga</a>.</p>'
            elif 'valley' in html_file.name or 'berber' in html_file.name:
                link = f'<p><strong>Recommended Reading:</strong> Discover more about the region in our post on <a href="{prefix}blog/exploring-hidden-atlas-valleys.html" class="text-primary">Exploring Hidden Atlas Valleys</a>.</p>'
            
            if link:
                # Insert at the end of the overview div. We can just find the first closing </div> after tour-overview.
                # Actually, appending after the first paragraph in tour-overview is safer.
                p_match = re.search(r'<div class="tour-overview">.*?<p>.*?</p>', content, re.DOTALL)
                if p_match:
                    insert_pos = p_match.end()
                    content = content[:insert_pos] + "\n                    " + link + content[insert_pos:]
        
        if content != original:
            html_file.write_text(content, encoding='utf-8')
            updated_files += 1
            
    except Exception as e:
        print(f"Error on {html_file.name}: {e}")

print(f"Metadata and contextual links injected into {updated_files} HTML files.")
