import os
import re

base_dir = r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours"
index_path = os.path.join(base_dir, "index.html")

tour_dir = os.path.join(base_dir, "tours")
all_tours = set(os.listdir(tour_dir))
all_roots = set(os.listdir(base_dir))

print("Available tour files in tours/:")
for t in sorted(all_tours):
    print("  ", t)

print("\nAvailable root files:")
for r in sorted(all_roots):
    if r.endswith(".html"):
        print("  ", r)

# Precise Mapping dictionary based on actual available files
mapping = {
    "tours/2-days-azzaden-valley-trek.html": "tours/2days-azzaden-valley.html",
    "tours/2-days-mount-toubkal-trek.html": "tours/2-days-mount-toubkal.html",
    "tours/2days-overnight-in-atlas-mountains.html": "tours/overnight-in-atlas-mountains.html",
    "tours/3-days-mount-toubkal-trek-acclimatize-better.html": "tours/mount-toubkal-3days-trek-acclimatization.html",
    "tours/3-days-atlas-mountain-trek-desert-agafay.html": "tours/3-days-atlas-mountains-trek-camel-ride.html",
    "tours/5-days-atlas-mountain-trek-camel-ride.html": "tours/5-days-atlas-mountain-trek.html",
    "tours/3-days-desert-tour-from-marrakech.html": "tours/3days-merzouga-desert.html",
    "tours/4-day-desert-tour-from-marrakech2marrakech.html": "tours/4days-sahara-desert.html",
    "tours/4-days-sahara-desert-from-marrakech-to-fes.html": "tours/4-days-sahara-desert-marrakech-to-fes.html",
    "morocco-tours-and-holidays.html": "morocco-tours.html"
}

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Verify all replacement targets exist before replacing
for orig, target in mapping.items():
    target_path = os.path.join(base_dir, target.replace("/", os.sep))
    if os.path.exists(target_path):
        print(f"Mapping VALIDATED: {orig} -> {target}")
        content = content.replace(f'href="{orig}"', f'href="{target}"')
        content = content.replace(f"href='{orig}'", f"href='{target}'")
    else:
        print(f"WARNING Target DOES NOT EXIST: {target_path}")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

print("\nUpdated index.html successfully!")
