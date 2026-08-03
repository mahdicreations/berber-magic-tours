import os
import re

base_dir = r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours"
tours_dir = os.path.join(base_dir, "tours")

fixed_recommended_html = """    <!-- Recommended Tours Section -->
    <section class="recommended-tours-section" style="padding: 70px 0; background: #F8FAFC; border-top: 1px solid #E2E8F0;">
        <div class="container">
            <div class="section-header text-center" style="margin-bottom: 40px; text-align: center;">
                <span class="subtitle" style="color: var(--primary); font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; font-size: 0.85rem; display: block; margin-bottom: 6px;">Explore More Journeys</span>
                <h2 class="section-title" style="font-family: var(--font-heading); font-size: 2.1rem; color: var(--secondary); margin: 0;">Recommended Tours</h2>
                <div style="width: 50px; height: 3px; background: var(--primary); margin: 12px auto 0; border-radius: 2px;"></div>
            </div>

            <div class="tours-grid-container" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(290px, 1fr)); gap: 28px;">
                
                <!-- Recommended Tour 1 -->
                <div class="tour-card-premium" style="background: #ffffff; border-radius: 16px; overflow: hidden; box-shadow: 0 10px 25px rgba(0,0,0,0.05); border: 1px solid #E2E8F0; display: flex; flex-direction: column; transition: transform 0.3s ease, box-shadow 0.3s ease;">
                    <div class="tour-card-image" style="height: 210px; background-image: url('images/2-days-mount-toubkal/Toubkal-ascent.jpg'); background-size: cover; background-position: center; position: relative;">
                        <div class="tour-card-overlay" style="position: absolute; top:0; left:0; right:0; bottom:0; background: linear-gradient(180deg, rgba(0,0,0,0) 50%, rgba(0,0,0,0.6) 100%);"></div>
                        <div class="tour-cat-badge" style="position: absolute; bottom: 12px; right: 12px; background: rgba(0,0,0,0.75); color: #ffffff; padding: 5px 12px; border-radius: 20px; font-size: 0.78rem; font-weight: 600; backdrop-filter: blur(4px);">Climb Mount Toubkal</div>
                    </div>
                    <div class="tour-card-body" style="padding: 22px; display: flex; flex-direction: column; flex-grow: 1;">
                        <div class="tour-card-meta" style="font-size: 0.85rem; color: #64748B; display: flex; gap: 14px; margin-bottom: 10px;">
                            <span><i class="fas fa-map-marker-alt" style="color: var(--primary);"></i> High Atlas</span>
                            <span><i class="far fa-clock" style="color: var(--primary);"></i> 2 Days</span>
                        </div>
                        <h3 class="tour-card-title" style="font-size: 1.18rem; color: var(--secondary); font-family: var(--font-heading); margin-bottom: 10px; line-height: 1.35;"><a href="2-days-mount-toubkal.html" style="color: inherit; text-decoration: none;">2 days Mount Toubkal trek</a></h3>
                        <p class="tour-card-text" style="font-size: 0.9rem; color: #475569; line-height: 1.6; flex-grow: 1; margin-bottom: 18px;">Ascend North Africa's highest peak (4,167m) over 2 days with experienced mountain guides and traditional Berber meals.</p>
                        <div class="tour-card-footer" style="display: flex; align-items: center; justify-content: space-between; margin-top: auto; padding-top: 15px; border-top: 1px solid #F1F5F9;">
                            <div class="tour-price-tag" style="font-size: 0.85rem; color: #64748B;"><i class="fas fa-shield-alt" style="color: var(--primary);"></i> Guided Trek</div>
                            <a href="2-days-mount-toubkal.html" class="btn-card-explore" style="display: inline-flex; align-items: center; gap: 6px; background: var(--primary); color: #ffffff; padding: 8px 18px; border-radius: 25px; font-weight: 600; font-size: 0.88rem; text-decoration: none; transition: background 0.2s ease;">Explore Tour <i class="fas fa-arrow-right"></i></a>
                        </div>
                    </div>
                </div>

                <!-- Recommended Tour 2 -->
                <div class="tour-card-premium" style="background: #ffffff; border-radius: 16px; overflow: hidden; box-shadow: 0 10px 25px rgba(0,0,0,0.05); border: 1px solid #E2E8F0; display: flex; flex-direction: column; transition: transform 0.3s ease, box-shadow 0.3s ease;">
                    <div class="tour-card-image" style="height: 210px; background-image: url('images/3days-merzouga-desert/merzougadesertmarrakech-570x400.jpg'); background-size: cover; background-position: center; position: relative;">
                        <div class="tour-card-overlay" style="position: absolute; top:0; left:0; right:0; bottom:0; background: linear-gradient(180deg, rgba(0,0,0,0) 50%, rgba(0,0,0,0.6) 100%);"></div>
                        <div class="tour-cat-badge" style="position: absolute; bottom: 12px; right: 12px; background: rgba(0,0,0,0.75); color: #ffffff; padding: 5px 12px; border-radius: 20px; font-size: 0.78rem; font-weight: 600; backdrop-filter: blur(4px);">Sahara Desert Tours</div>
                    </div>
                    <div class="tour-card-body" style="padding: 22px; display: flex; flex-direction: column; flex-grow: 1;">
                        <div class="tour-card-meta" style="font-size: 0.85rem; color: #64748B; display: flex; gap: 14px; margin-bottom: 10px;">
                            <span><i class="fas fa-map-marker-alt" style="color: var(--primary);"></i> Merzouga</span>
                            <span><i class="far fa-clock" style="color: var(--primary);"></i> 3 Days</span>
                        </div>
                        <h3 class="tour-card-title" style="font-size: 1.18rem; color: var(--secondary); font-family: var(--font-heading); margin-bottom: 10px; line-height: 1.35;"><a href="3days-merzouga-desert.html" style="color: inherit; text-decoration: none;">3 days desert tour from Marrakech</a></h3>
                        <p class="tour-card-text" style="font-size: 0.9rem; color: #475569; line-height: 1.6; flex-grow: 1; margin-bottom: 18px;">Experience the magic of Merzouga dunes with sunset camel treks, authentic Berber music around campfire, and stargazing.</p>
                        <div class="tour-card-footer" style="display: flex; align-items: center; justify-content: space-between; margin-top: auto; padding-top: 15px; border-top: 1px solid #F1F5F9;">
                            <div class="tour-price-tag" style="font-size: 0.85rem; color: #64748B;"><i class="fas fa-shield-alt" style="color: var(--primary);"></i> Guided Tour</div>
                            <a href="3days-merzouga-desert.html" class="btn-card-explore" style="display: inline-flex; align-items: center; gap: 6px; background: var(--primary); color: #ffffff; padding: 8px 18px; border-radius: 25px; font-weight: 600; font-size: 0.88rem; text-decoration: none; transition: background 0.2s ease;">Explore Tour <i class="fas fa-arrow-right"></i></a>
                        </div>
                    </div>
                </div>

                <!-- Recommended Tour 3 -->
                <div class="tour-card-premium" style="background: #ffffff; border-radius: 16px; overflow: hidden; box-shadow: 0 10px 25px rgba(0,0,0,0.05); border: 1px solid #E2E8F0; display: flex; flex-direction: column; transition: transform 0.3s ease, box-shadow 0.3s ease;">
                    <div class="tour-card-image" style="height: 210px; background-image: url('images/2days-azzaden-valley/Atlas-mountains-valleys-1.jpg'); background-size: cover; background-position: center; position: relative;">
                        <div class="tour-card-overlay" style="position: absolute; top:0; left:0; right:0; bottom:0; background: linear-gradient(180deg, rgba(0,0,0,0) 50%, rgba(0,0,0,0.6) 100%);"></div>
                        <div class="tour-cat-badge" style="position: absolute; bottom: 12px; right: 12px; background: rgba(0,0,0,0.75); color: #ffffff; padding: 5px 12px; border-radius: 20px; font-size: 0.78rem; font-weight: 600; backdrop-filter: blur(4px);">Berber Village Treks</div>
                    </div>
                    <div class="tour-card-body" style="padding: 22px; display: flex; flex-direction: column; flex-grow: 1;">
                        <div class="tour-card-meta" style="font-size: 0.85rem; color: #64748B; display: flex; gap: 14px; margin-bottom: 10px;">
                            <span><i class="fas fa-map-marker-alt" style="color: var(--primary);"></i> Atlas Valleys</span>
                            <span><i class="far fa-clock" style="color: var(--primary);"></i> 2 Days</span>
                        </div>
                        <h3 class="tour-card-title" style="font-size: 1.18rem; color: var(--secondary); font-family: var(--font-heading); margin-bottom: 10px; line-height: 1.35;"><a href="2days-azzaden-valley.html" style="color: inherit; text-decoration: none;">2 days Azzaden valley trek</a></h3>
                        <p class="tour-card-text" style="font-size: 0.9rem; color: #475569; line-height: 1.6; flex-grow: 1; margin-bottom: 18px;">Hike through the colorful red clay villages of Azzaden Valley, majestic juniper forests, and mountain streams with local Berber hospitality.</p>
                        <div class="tour-card-footer" style="display: flex; align-items: center; justify-content: space-between; margin-top: auto; padding-top: 15px; border-top: 1px solid #F1F5F9;">
                            <div class="tour-price-tag" style="font-size: 0.85rem; color: #64748B;"><i class="fas fa-shield-alt" style="color: var(--primary);"></i> Guided Trek</div>
                            <a href="2days-azzaden-valley.html" class="btn-card-explore" style="display: inline-flex; align-items: center; gap: 6px; background: var(--primary); color: #ffffff; padding: 8px 18px; border-radius: 25px; font-weight: 600; font-size: 0.88rem; text-decoration: none; transition: background 0.2s ease;">Explore Tour <i class="fas fa-arrow-right"></i></a>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </section>"""

print("=== FIXING RECOMMENDED TOURS DESIGN ACROSS ALL SINGLE TOUR PAGES ===")
total_updated = 0

for file_name in sorted(os.listdir(tours_dir)):
    if not file_name.endswith(".html"):
        continue

    file_path = os.path.join(tours_dir, file_name)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find and replace existing Recommended Tours section
    pattern = r'<!-- Recommended Tours Section -->[\s\S]*?</section>'
    if re.search(pattern, content):
        content = re.sub(pattern, fixed_recommended_html, content)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        total_updated += 1
        print(f"Fixed Recommended Tours design in [{file_name}]")

print(f"\nDone! Fixed Recommended Tours design across {total_updated} tour pages.")
