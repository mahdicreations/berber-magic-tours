import os
from pathlib import Path
import re
from PIL import Image

workspace = Path('c:/Users/el mahdi/Desktop/mahdicreations/berber-magic-tours')
image_dir = workspace / 'assets' / 'images'
tour_image_dir = workspace / 'tours' / 'images'

def get_image_dimensions(src, html_file):
    # resolve src path relative to workspace or html_file
    if src.startswith('/'):
        file_path = workspace / src.lstrip('/')
    elif src.startswith('images/'):
        file_path = html_file.parent / src
    elif src.startswith('../assets/'):
        file_path = workspace / src[3:]
    else:
        file_path = html_file.parent / src
        
    if file_path.exists():
        try:
            with Image.open(file_path) as img:
                return img.width, img.height
        except Exception:
            pass
    return None, None

img_regex = re.compile(r'<img\s+([^>]+)>', re.IGNORECASE)
iframe_regex = re.compile(r'<iframe\s+([^>]+)>', re.IGNORECASE)

stats = {
    'total_imgs': 0,
    'already_lazy': 0,
    'missing_lazy_below_fold': 0,
    'has_width_height': 0,
    'needs_width_height': 0,
    'iframes_missing_lazy': 0
}

for html_file in workspace.rglob('*.html'):
    if '.git' in str(html_file) or 'scratch' in str(html_file):
        continue
        
    content = html_file.read_text(encoding='utf-8', errors='ignore')
    
    # Analyze iframes
    for match in iframe_regex.finditer(content):
        attrs = match.group(1)
        if 'loading="lazy"' not in attrs.lower() and 'loading=\'lazy\'' not in attrs.lower():
            stats['iframes_missing_lazy'] += 1
            
    # Analyze images
    for match in img_regex.finditer(content):
        attrs = match.group(1)
        stats['total_imgs'] += 1
        
        # Determine if above or below fold based on class or src (e.g. logo, mobile-logo are above fold)
        src_match = re.search(r'src=["\']([^"\']+)["\']', attrs, re.IGNORECASE)
        src = src_match.group(1) if src_match else ""
        
        is_above_fold = False
        if 'logo' in src.lower() or 'mobile-logo' in attrs or 'hero' in attrs:
            is_above_fold = True
            
        is_lazy = 'loading="lazy"' in attrs.lower() or "loading='lazy'" in attrs.lower()
        
        if is_lazy:
            stats['already_lazy'] += 1
        elif not is_above_fold:
            stats['missing_lazy_below_fold'] += 1
            
        has_dims = 'width=' in attrs.lower() and 'height=' in attrs.lower()
        if has_dims:
            stats['has_width_height'] += 1
        elif src:
            w, h = get_image_dimensions(src, html_file)
            if w and h:
                stats['needs_width_height'] += 1

print(stats)
