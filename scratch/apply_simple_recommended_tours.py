import os
import re

base_dir = r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours"
tours_dir = os.path.join(base_dir, "tours")

simple_recommended_html = """    <!-- Recommended Tours Section -->
    <section class="recommended-tours-section" style="padding: 50px 0; background: #FAFAFA; border-top: 1px solid #E2E8F0;">
        <div class="container">
            <div style="margin-bottom: 30px; text-align: center;">
                <h2 style="font-family: var(--font-heading); font-size: 1.8rem; color: var(--secondary); margin: 0 0 6px 0;">Recommended Tours</h2>
                <p style="color: #64748B; font-size: 0.92rem; margin: 0;">Explore other popular itineraries crafted by Berber Magic Tours.</p>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px;">
                
                <!-- Recommended Tour 1 -->
                <div style="background: #ffffff; border-radius: 12px; border: 1px solid #E2E8F0; overflow: hidden; display: flex; flex-direction: column;">
                    <a href="2-days-mount-toubkal.html" style="display: block; overflow: hidden;">
                        <img src="images/2-days-mount-toubkal/Toubkal-ascent.jpg" alt="2 days Mount Toubkal trek" style="width: 100%; height: 180px; object-fit: cover; display: block;">
                    </a>
                    <div style="padding: 18px; display: flex; flex-direction: column; flex-grow: 1;">
                        <div style="font-size: 0.78rem; font-weight: 700; color: var(--primary); text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 4px;">Climb Mount Toubkal</div>
                        <h3 style="font-size: 1.08rem; font-weight: 700; color: var(--secondary); margin: 0 0 8px 0; line-height: 1.35;">
                            <a href="2-days-mount-toubkal.html" style="color: inherit; text-decoration: none;">2 days Mount Toubkal trek</a>
                        </h3>
                        <p style="font-size: 0.88rem; color: #64748B; line-height: 1.55; margin: 0 0 16px 0; flex-grow: 1;">Ascend North Africa's highest peak (4,167m) over 2 days with experienced mountain guides.</p>
                        <div style="margin-top: auto; padding-top: 12px; border-top: 1px solid #F1F5F9; display: flex; align-items: center; justify-content: space-between;">
                            <span style="font-size: 0.82rem; color: #64748B;"><i class="far fa-clock"></i> 2 Days</span>
                            <a href="2-days-mount-toubkal.html" style="color: var(--primary); font-weight: 700; font-size: 0.85rem; text-decoration: none;">View Tour <i class="fas fa-arrow-right" style="font-size: 0.75rem;"></i></a>
                        </div>
                    </div>
                </div>

                <!-- Recommended Tour 2 -->
                <div style="background: #ffffff; border-radius: 12px; border: 1px solid #E2E8F0; overflow: hidden; display: flex; flex-direction: column;">
                    <a href="3days-merzouga-desert.html" style="display: block; overflow: hidden;">
                        <img src="images/3days-merzouga-desert/merzougadesertmarrakech-570x400.jpg" alt="3 days desert tour from Marrakech" style="width: 100%; height: 180px; object-fit: cover; display: block;">
                    </a>
                    <div style="padding: 18px; display: flex; flex-direction: column; flex-grow: 1;">
                        <div style="font-size: 0.78rem; font-weight: 700; color: var(--primary); text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 4px;">Sahara Desert Tours</div>
                        <h3 style="font-size: 1.08rem; font-weight: 700; color: var(--secondary); margin: 0 0 8px 0; line-height: 1.35;">
                            <a href="3days-merzouga-desert.html" style="color: inherit; text-decoration: none;">3 days desert tour from Marrakech</a>
                        </h3>
                        <p style="font-size: 0.88rem; color: #64748B; line-height: 1.55; margin: 0 0 16px 0; flex-grow: 1;">Experience the magic of Merzouga dunes with sunset camel treks, Berber music, and stargazing.</p>
                        <div style="margin-top: auto; padding-top: 12px; border-top: 1px solid #F1F5F9; display: flex; align-items: center; justify-content: space-between;">
                            <span style="font-size: 0.82rem; color: #64748B;"><i class="far fa-clock"></i> 3 Days</span>
                            <a href="3days-merzouga-desert.html" style="color: var(--primary); font-weight: 700; font-size: 0.85rem; text-decoration: none;">View Tour <i class="fas fa-arrow-right" style="font-size: 0.75rem;"></i></a>
                        </div>
                    </div>
                </div>

                <!-- Recommended Tour 3 -->
                <div style="background: #ffffff; border-radius: 12px; border: 1px solid #E2E8F0; overflow: hidden; display: flex; flex-direction: column;">
                    <a href="2days-azzaden-valley.html" style="display: block; overflow: hidden;">
                        <img src="images/2days-azzaden-valley/Atlas-mountains-valleys-1.jpg" alt="2 days Azzaden valley trek" style="width: 100%; height: 180px; object-fit: cover; display: block;">
                    </a>
                    <div style="padding: 18px; display: flex; flex-direction: column; flex-grow: 1;">
                        <div style="font-size: 0.78rem; font-weight: 700; color: var(--primary); text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 4px;">Berber Village Treks</div>
                        <h3 style="font-size: 1.08rem; font-weight: 700; color: var(--secondary); margin: 0 0 8px 0; line-height: 1.35;">
                            <a href="2days-azzaden-valley.html" style="color: inherit; text-decoration: none;">2 days Azzaden valley trek</a>
                        </h3>
                        <p style="font-size: 0.88rem; color: #64748B; line-height: 1.55; margin: 0 0 16px 0; flex-grow: 1;">Hike through the colorful red clay villages of Azzaden Valley and juniper forests with local guides.</p>
                        <div style="margin-top: auto; padding-top: 12px; border-top: 1px solid #F1F5F9; display: flex; align-items: center; justify-content: space-between;">
                            <span style="font-size: 0.82rem; color: #64748B;"><i class="far fa-clock"></i> 2 Days</span>
                            <a href="2days-azzaden-valley.html" style="color: var(--primary); font-weight: 700; font-size: 0.85rem; text-decoration: none;">View Tour <i class="fas fa-arrow-right" style="font-size: 0.75rem;"></i></a>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </section>"""

print("=== APPLYING SIMPLE & MINIMALIST RECOMMENDED TOURS DESIGN ===")
total_updated = 0

for file_name in sorted(os.listdir(tours_dir)):
    if not file_name.endswith(".html"):
        continue

    file_path = os.path.join(tours_dir, file_name)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = r'<!-- Recommended Tours Section -->[\s\S]*?</section>'
    if re.search(pattern, content):
        content = re.sub(pattern, simple_recommended_html, content)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        total_updated += 1
        print(f"Updated Recommended Tours design in [{file_name}]")

print(f"\nDone! Updated simple Recommended Tours design across {total_updated} tour pages.")
