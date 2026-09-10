import os
from pathlib import Path
import re
from PIL import Image

workspace = Path('c:/Users/el mahdi/Desktop/mahdicreations/berber-magic-tours')

def get_file_path(src, html_file):
    if src.startswith('/'):
        return workspace / src.lstrip('/')
    elif src.startswith('images/'):
        return html_file.parent / src
    elif src.startswith('../assets/'):
        return workspace / src[3:]
    else:
        return html_file.parent / src

def has_webp_variant(img_path):
    # Check if a .webp version exists
    if img_path.suffix.lower() in ['.jpg', '.jpeg', '.png']:
        webp_path = img_path.with_suffix('.webp')
        if webp_path.exists():
            return webp_path
    return None

stats = {
    'updated_files': 0,
    'lazy_added': 0,
    'dims_added': 0,
    'pictures_added': 0
}

def process_html_file(html_file):
    try:
        content = html_file.read_text(encoding='utf-8', errors='ignore')
        original = content
        
        def replace_img(match):
            img_tag = match.group(0)
            attrs = match.group(1)
            
            src_match = re.search(r'src=["\']([^"\']+)["\']', attrs, re.IGNORECASE)
            if not src_match:
                return img_tag
            
            src = src_match.group(1)
            
            # Check for above fold
            is_above_fold = False
            if 'logo' in src.lower() or 'hero' in attrs.lower():
                is_above_fold = True
                
            # Add loading="lazy" if needed
            new_attrs = attrs
            if not is_above_fold and 'loading=' not in new_attrs.lower():
                new_attrs += ' loading="lazy"'
                stats['lazy_added'] += 1
                
            # Add dimensions if needed
            if 'width=' not in new_attrs.lower() and 'height=' not in new_attrs.lower():
                img_path = get_file_path(src, html_file)
                if img_path and img_path.exists():
                    try:
                        with Image.open(img_path) as img:
                            w, h = img.width, img.height
                            new_attrs += f' width="{w}" height="{h}"'
                            stats['dims_added'] += 1
                    except Exception:
                        pass
                        
            # Reconstruct img tag
            # Just replacing the inner attrs is safer
            new_img = f'<img {new_attrs}>'
            # fix double spaces if any
            new_img = re.sub(r'\s+', ' ', new_img)
            new_img = new_img.replace(' >', '>')
            
            # Check for webp to wrap in <picture>
            # ONLY if it's not already inside a picture. This is tricky with regex.
            # We'll rely on a second pass or just check the context.
            # Actually, doing it here is risky if it's already in a picture. 
            return new_img
            
        # First, process raw img tags to add lazy and dimensions
        content = re.sub(r'<img\s+([^>]+)>', replace_img, content, flags=re.IGNORECASE)
        
        # Now, look for img tags NOT inside <picture> and wrap them if webp exists
        def wrap_picture(match):
            full_match = match.group(0)
            img_tag = match.group(1)
            
            if '<picture>' in full_match.lower():
                return full_match # Already inside a picture
                
            # Not inside a picture, let's check webp
            src_match = re.search(r'src=["\']([^"\']+)["\']', img_tag, re.IGNORECASE)
            if src_match:
                src = src_match.group(1)
                img_path = get_file_path(src, html_file)
                if img_path and img_path.exists():
                    webp_path = has_webp_variant(img_path)
                    if webp_path:
                        # Create webp src relative to the original src
                        base, ext = os.path.splitext(src)
                        webp_src = f"{base}.webp"
                        
                        # Wrap
                        new_block = f'<picture><source srcset="{webp_src}" type="image/webp">{img_tag}</picture>'
                        stats['pictures_added'] += 1
                        return new_block
            
            return full_match # no change
            
        # Regex to find img tags, capturing any preceding <picture> context loosely.
        # A better approach: find all img tags, then check surrounding text, but it's simpler to just replace all and ignore if `<picture>` is right before it.
        # We can split the file by `<picture>` and `</picture>`, then only process text outside these blocks.
        
        parts = re.split(r'(?i)(<picture>.*?</picture>)', content, flags=re.DOTALL)
        for i in range(0, len(parts), 2): # Evens are outside <picture>
            parts[i] = re.sub(r'(<img\s+[^>]+>)', lambda m: wrap_picture(re.match(r'()(<img\s+[^>]+>)', m.group(1))), parts[i], flags=re.IGNORECASE)
            # The lambda is a bit hacky above, let's rewrite the logic inside the loop cleanly
        
        new_content = ""
        for i, part in enumerate(parts):
            if i % 2 == 1:
                # Inside picture
                new_content += part
            else:
                # Outside picture
                def process_outside_img(m):
                    img_tag = m.group(0)
                    src_match = re.search(r'src=["\']([^"\']+)["\']', img_tag, re.IGNORECASE)
                    if src_match:
                        src = src_match.group(1)
                        img_path = get_file_path(src, html_file)
                        if img_path and img_path.exists():
                            webp_path = has_webp_variant(img_path)
                            if webp_path:
                                base, ext = os.path.splitext(src)
                                webp_src = f"{base}.webp"
                                stats['pictures_added'] += 1
                                return f'<picture><source srcset="{webp_src}" type="image/webp">{img_tag}</picture>'
                    return img_tag
                new_content += re.sub(r'<img\s+[^>]+>', process_outside_img, part, flags=re.IGNORECASE)
                
        content = new_content
        
        if content != original:
            html_file.write_text(content, encoding='utf-8')
            stats['updated_files'] += 1
            
    except Exception as e:
        print(f"Error on {html_file.name}: {e}")

for html_file in workspace.rglob('*.html'):
    if '.git' in str(html_file) or 'scratch' in str(html_file):
        continue
    process_html_file(html_file)

print(stats)
