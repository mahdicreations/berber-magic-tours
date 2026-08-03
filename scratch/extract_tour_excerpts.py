import os
import re

base_dir = r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours"
tours_dir = os.path.join(base_dir, "tours")

tour_excerpts = {}

for f in sorted(os.listdir(tours_dir)):
    if not f.endswith(".html"):
        continue
    
    tour_path = os.path.join(tours_dir, f)
    with open(tour_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Look for meta description or first paragraph in overview/description
    meta_desc = re.search(r'<meta\s+name=["\']description["\']\s+content=["\']([^"\'\n]+)["\']', content, re.IGNORECASE)
    
    # Or find first <p> in overview section
    overview_p = re.search(r'<(?:p|div)[^>]*class=["\'][^"\'\n]*overview[^"\'\n]*["\'][^>]*>[\s\S]*?<p[^>]*>([\s\S]*?)</p>', content, re.IGNORECASE)
    if not overview_p:
        overview_p = re.search(r'<p[^>]*class=["\'][^"\'\n]*lead[^"\'\n]*["\'][^>]*>([\s\S]*?)</p>', content, re.IGNORECASE)
    
    text = ""
    if overview_p:
        # Clean html tags
        text = re.sub(r'<[^>]+>', '', overview_p.group(1)).strip()
    elif meta_desc:
        text = meta_desc.group(1).strip()
    else:
        # Fallback: search for first paragraph with length > 40
        all_ps = re.findall(r'<p[^>]*>([\s\S]*?)</p>', content, re.IGNORECASE)
        for p in all_ps:
            clean_p = re.sub(r'<[^>]+>', '', p).strip()
            if len(clean_p) > 40 and not clean_p.startswith("Copyright") and not clean_p.startswith("At Berber"):
                text = clean_p
                break
    
    # Trim to ~140 chars for card excerpt
    if text:
        # Remove extra whitespace
        text = " ".join(text.split())
        if len(text) > 150:
            text = text[:145].rstrip() + "..."
        tour_excerpts[f] = text
        print(f"[{f}]: {text}\n")
    else:
        print(f"[{f}]: NO EXCERPT FOUND\n")

print(f"Extracted unique excerpts for {len(tour_excerpts)} tours.")
