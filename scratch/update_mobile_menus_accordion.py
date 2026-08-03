import os
import re

base_dir = r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours"
tours_dir = os.path.join(base_dir, "tours")

root_mobile_menu_html = """    <!-- Mobile Menu -->
    <div class="mobile-menu">
        <div class="mobile-menu-header">
            <img src="assets/images/logo.png" alt="Logo" class="mobile-logo">
            <button class="close-menu-btn"><i class="fas fa-times"></i></button>
        </div>
        <ul class="mobile-nav-list">
            <li><a href="index.html">Home</a></li>
            <li><a href="marrakech-day-trips.html">Marrakech Day Trips</a></li>
            
            <li class="mobile-dropdown">
                <div class="mobile-dropdown-header">
                    <a href="trek-and-hike.html">Trek &amp; Hike</a>
                    <button type="button" class="mobile-dropdown-toggle" onclick="toggleMobileSubmenu(this)"><i class="fas fa-plus"></i></button>
                </div>
                <ul class="mobile-submenu">
                    <li><a href="climb-mount-toubkal.html">Climb Mount Toubkal</a></li>
                    <li><a href="berber-village-treks.html">Berber Village Treks</a></li>
                    <li><a href="combine-toubkal-and-villages.html">Combine Toubkal &amp; Villages</a></li>
                    <li><a href="biking-in-morocco.html">Biking in Morocco</a></li>
                </ul>
            </li>
            
            <li class="mobile-dropdown">
                <div class="mobile-dropdown-header">
                    <a href="combine-atlas-mountains-and-desert.html">Combine Atlas Mountains &amp; Desert</a>
                    <button type="button" class="mobile-dropdown-toggle" onclick="toggleMobileSubmenu(this)"><i class="fas fa-plus"></i></button>
                </div>
                <ul class="mobile-submenu">
                    <li><a href="combine-berber-villages-and-sahara.html">Combine Berber Villages &amp; Sahara</a></li>
                    <li><a href="combine-toubkal-and-sahara.html">Combine Toubkal &amp; Sahara</a></li>
                </ul>
            </li>

            <li class="mobile-dropdown">
                <div class="mobile-dropdown-header">
                    <a href="sahara-desert-tours.html">Sahara Desert Tours</a>
                    <button type="button" class="mobile-dropdown-toggle" onclick="toggleMobileSubmenu(this)"><i class="fas fa-plus"></i></button>
                </div>
                <ul class="mobile-submenu">
                    <li><a href="tours-from-marrakech.html">Tours from Marrakech</a></li>
                    <li><a href="tours-from-casablanca.html">Tours from Casablanca</a></li>
                    <li><a href="tours-from-fes.html">Tours from Fes</a></li>
                </ul>
            </li>

            <li><a href="morocco-tours.html">Morocco Tours</a></li>
        </ul>
        <a href="contact.html" class="btn btn-primary mobile-btn"><i class="fas fa-envelope"></i> Contact Us</a>
    </div>"""

tours_mobile_menu_html = """    <!-- Mobile Menu -->
    <div class="mobile-menu">
        <div class="mobile-menu-header">
            <img src="../assets/images/logo.png" alt="Logo" class="mobile-logo">
            <button class="close-menu-btn"><i class="fas fa-times"></i></button>
        </div>
        <ul class="mobile-nav-list">
            <li><a href="../index.html">Home</a></li>
            <li><a href="../marrakech-day-trips.html">Marrakech Day Trips</a></li>
            
            <li class="mobile-dropdown">
                <div class="mobile-dropdown-header">
                    <a href="../trek-and-hike.html">Trek &amp; Hike</a>
                    <button type="button" class="mobile-dropdown-toggle" onclick="toggleMobileSubmenu(this)"><i class="fas fa-plus"></i></button>
                </div>
                <ul class="mobile-submenu">
                    <li><a href="../climb-mount-toubkal.html">Climb Mount Toubkal</a></li>
                    <li><a href="../berber-village-treks.html">Berber Village Treks</a></li>
                    <li><a href="../combine-toubkal-and-villages.html">Combine Toubkal &amp; Villages</a></li>
                    <li><a href="../biking-in-morocco.html">Biking in Morocco</a></li>
                </ul>
            </li>
            
            <li class="mobile-dropdown">
                <div class="mobile-dropdown-header">
                    <a href="../combine-atlas-mountains-and-desert.html">Combine Atlas Mountains &amp; Desert</a>
                    <button type="button" class="mobile-dropdown-toggle" onclick="toggleMobileSubmenu(this)"><i class="fas fa-plus"></i></button>
                </div>
                <ul class="mobile-submenu">
                    <li><a href="../combine-berber-villages-and-sahara.html">Combine Berber Villages &amp; Sahara</a></li>
                    <li><a href="../combine-toubkal-and-sahara.html">Combine Toubkal &amp; Sahara</a></li>
                </ul>
            </li>

            <li class="mobile-dropdown">
                <div class="mobile-dropdown-header">
                    <a href="../sahara-desert-tours.html">Sahara Desert Tours</a>
                    <button type="button" class="mobile-dropdown-toggle" onclick="toggleMobileSubmenu(this)"><i class="fas fa-plus"></i></button>
                </div>
                <ul class="mobile-submenu">
                    <li><a href="../tours-from-marrakech.html">Tours from Marrakech</a></li>
                    <li><a href="../tours-from-casablanca.html">Tours from Casablanca</a></li>
                    <li><a href="../tours-from-fes.html">Tours from Fes</a></li>
                </ul>
            </li>

            <li><a href="../morocco-tours.html">Morocco Tours</a></li>
        </ul>
        <a href="../contact.html" class="btn btn-primary mobile-btn"><i class="fas fa-envelope"></i> Contact Us</a>
    </div>"""

pattern = r'<!-- Mobile Menu -->[\s\S]*?</div>\s*<!--'

print("=== UPDATING MOBILE MENU ACCORDION GROUPING ACROSS ALL HTML FILES ===")

# Update root HTML files
root_count = 0
for filename in os.listdir(base_dir):
    if not filename.endswith(".html"):
        continue

    filepath = os.path.join(base_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Find mobile menu block
    m = re.search(r'(<!-- Mobile Menu -->[\s\S]*?<a href="contact\.html" class="btn btn-primary mobile-btn">[\s\S]*?</div>)', content)
    if m:
        # Preserve active link state if present
        current_menu = root_mobile_menu_html
        if f'href="{filename}"' in current_menu:
            current_menu = current_menu.replace(f'href="{filename}"', f'href="{filename}" class="active"')
        content = content.replace(m.group(1), current_menu)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        root_count += 1
        print(f"Updated mobile menu in root file [{filename}]")

# Update tours/*.html files
tours_count = 0
for filename in os.listdir(tours_dir):
    if not filename.endswith(".html"):
        continue

    filepath = os.path.join(tours_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    m = re.search(r'(<!-- Mobile Menu -->[\s\S]*?<a href="\.\./contact\.html" class="btn btn-primary mobile-btn">[\s\S]*?</div>)', content)
    if m:
        content = content.replace(m.group(1), tours_mobile_menu_html)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        tours_count += 1
        print(f"Updated mobile menu in tours file [{filename}]")

print(f"\nDone! Updated mobile menu grouping with '+' accordion toggles across {root_count} root pages and {tours_count} tour pages.")
