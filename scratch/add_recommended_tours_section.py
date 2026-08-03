import os

base_dir = r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours"
tours_dir = os.path.join(base_dir, "tours")

recommended_section_html = """
    <!-- Recommended Tours Section -->
    <section class="recommended-tours-section" style="padding: 70px 0; background: #FFFFFF; border-top: 1px solid #E2E8F0;">
        <div class="container">
            <div class="section-header text-center" style="margin-bottom: 45px; text-align: center;">
                <span class="subtitle" style="color: var(--primary); font-weight: 700; text-transform: uppercase; letter-spacing: 1px; font-size: 0.88rem; display: block;">Explore More Journeys</span>
                <h2 class="section-title" style="font-family: var(--font-heading); font-size: 2.2rem; color: var(--secondary); margin-top: 6px;">Recommended Tours</h2>
                <p style="color: #64748B; font-size: 0.98rem; max-width: 600px; margin: 10px auto 0; line-height: 1.6;">Discover other handpicked adventures and popular itineraries in Morocco crafted by Berber Magic Tours.</p>
            </div>

            <div class="tours-grid-container" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px;">
                
                <!-- Recommended Tour 1 -->
                <div class="tour-card-premium" style="background: #ffffff; border-radius: 16px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.06); border: 1px solid #E2E8F0; display: flex; flex-direction: column;">
                    <div class="tour-card-image" style="height: 210px; background-image: url('../assets/images/trek2.jpg'); background-size: cover; background-position: center; position: relative;">
                        <div class="tour-cat-badge" style="position: absolute; bottom: 12px; right: 12px; background: rgba(0,0,0,0.75); color: #fff; padding: 5px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: 600;">Climb Mount Toubkal</div>
                    </div>
                    <div class="tour-card-body" style="padding: 22px; display: flex; flex-direction: column; flex-grow: 1;">
                        <div class="tour-card-meta mb-2" style="font-size: 0.85rem; color: #64748B; display: flex; gap: 12px; margin-bottom: 10px;">
                            <span><i class="fas fa-map-marker-alt text-primary"></i> High Atlas</span>
                            <span><i class="far fa-clock"></i> 2 Days</span>
                        </div>
                        <h3 class="tour-card-title mb-3" style="font-size: 1.2rem; color: var(--secondary); font-family: var(--font-heading); margin-bottom: 10px;"><a href="2-days-mount-toubkal.html" style="color: inherit; text-decoration: none;">2 days Mount Toubkal trek</a></h3>
                        <p class="tour-card-text mb-4" style="font-size: 0.9rem; color: #475569; line-height: 1.6; flex-grow: 1; margin-bottom: 16px;">Ascend North Africa's highest peak (4,167m) over 2 days with experienced mountain guides and traditional Berber meals.</p>
                        <div class="tour-card-footer" style="display: flex; align-items: center; justify-content: space-between; margin-top: auto; padding-top: 15px; border-top: 1px solid #F1F5F9;">
                            <div class="tour-price-tag" style="font-size: 0.85rem; color: #64748B;"><i class="fas fa-shield-alt text-primary"></i> Guided Trek</div>
                            <a href="2-days-mount-toubkal.html" class="btn-card-explore" style="display: inline-flex; align-items: center; gap: 6px; background: var(--primary); color: #fff; padding: 8px 18px; border-radius: 25px; font-weight: 600; font-size: 0.88rem; text-decoration: none;">Explore Tour <i class="fas fa-arrow-right"></i></a>
                        </div>
                    </div>
                </div>

                <!-- Recommended Tour 2 -->
                <div class="tour-card-premium" style="background: #ffffff; border-radius: 16px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.06); border: 1px solid #E2E8F0; display: flex; flex-direction: column;">
                    <div class="tour-card-image" style="height: 210px; background-image: url('../assets/images/slide1.png'); background-size: cover; background-position: center; position: relative;">
                        <div class="tour-cat-badge" style="position: absolute; bottom: 12px; right: 12px; background: rgba(0,0,0,0.75); color: #fff; padding: 5px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: 600;">Sahara Desert Tours</div>
                    </div>
                    <div class="tour-card-body" style="padding: 22px; display: flex; flex-direction: column; flex-grow: 1;">
                        <div class="tour-card-meta mb-2" style="font-size: 0.85rem; color: #64748B; display: flex; gap: 12px; margin-bottom: 10px;">
                            <span><i class="fas fa-map-marker-alt text-primary"></i> Merzouga</span>
                            <span><i class="far fa-clock"></i> 3 Days</span>
                        </div>
                        <h3 class="tour-card-title mb-3" style="font-size: 1.2rem; color: var(--secondary); font-family: var(--font-heading); margin-bottom: 10px;"><a href="3days-merzouga-desert.html" style="color: inherit; text-decoration: none;">3 days desert tour from Marrakech</a></h3>
                        <p class="tour-card-text mb-4" style="font-size: 0.9rem; color: #475569; line-height: 1.6; flex-grow: 1; margin-bottom: 16px;">Experience the magic of Merzouga dunes with sunset camel treks, authentic Berber music around campfire, and stargazing.</p>
                        <div class="tour-card-footer" style="display: flex; align-items: center; justify-content: space-between; margin-top: auto; padding-top: 15px; border-top: 1px solid #F1F5F9;">
                            <div class="tour-price-tag" style="font-size: 0.85rem; color: #64748B;"><i class="fas fa-shield-alt text-primary"></i> Guided Tour</div>
                            <a href="3days-merzouga-desert.html" class="btn-card-explore" style="display: inline-flex; align-items: center; gap: 6px; background: var(--primary); color: #fff; padding: 8px 18px; border-radius: 25px; font-weight: 600; font-size: 0.88rem; text-decoration: none;">Explore Tour <i class="fas fa-arrow-right"></i></a>
                        </div>
                    </div>
                </div>

                <!-- Recommended Tour 3 -->
                <div class="tour-card-premium" style="background: #ffffff; border-radius: 16px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.06); border: 1px solid #E2E8F0; display: flex; flex-direction: column;">
                    <div class="tour-card-image" style="height: 210px; background-image: url('../assets/images/trek1.jpg'); background-size: cover; background-position: center; position: relative;">
                        <div class="tour-cat-badge" style="position: absolute; bottom: 12px; right: 12px; background: rgba(0,0,0,0.75); color: #fff; padding: 5px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: 600;">Berber Village Treks</div>
                    </div>
                    <div class="tour-card-body" style="padding: 22px; display: flex; flex-direction: column; flex-grow: 1;">
                        <div class="tour-card-meta mb-2" style="font-size: 0.85rem; color: #64748B; display: flex; gap: 12px; margin-bottom: 10px;">
                            <span><i class="fas fa-map-marker-alt text-primary"></i> Atlas Valleys</span>
                            <span><i class="far fa-clock"></i> 2 Days</span>
                        </div>
                        <h3 class="tour-card-title mb-3" style="font-size: 1.2rem; color: var(--secondary); font-family: var(--font-heading); margin-bottom: 10px;"><a href="2days-azzaden-valley.html" style="color: inherit; text-decoration: none;">2 days Azzaden valley trek</a></h3>
                        <p class="tour-card-text mb-4" style="font-size: 0.9rem; color: #475569; line-height: 1.6; flex-grow: 1; margin-bottom: 16px;">Hike through the colorful red clay villages of Azzaden Valley, majestic juniper forests, and mountain streams with local Berber hospitality.</p>
                        <div class="tour-card-footer" style="display: flex; align-items: center; justify-content: space-between; margin-top: auto; padding-top: 15px; border-top: 1px solid #F1F5F9;">
                            <div class="tour-price-tag" style="font-size: 0.85rem; color: #64748B;"><i class="fas fa-shield-alt text-primary"></i> Guided Trek</div>
                            <a href="2days-azzaden-valley.html" class="btn-card-explore" style="display: inline-flex; align-items: center; gap: 6px; background: var(--primary); color: #fff; padding: 8px 18px; border-radius: 25px; font-weight: 600; font-size: 0.88rem; text-decoration: none;">Explore Tour <i class="fas fa-arrow-right"></i></a>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </section>
"""

print("=== ADDING RECOMMENDED TOURS SECTION TO ALL SINGLE TOUR PAGES ===")
total_updated = 0

for file_name in sorted(os.listdir(tours_dir)):
    if not file_name.endswith(".html"):
        continue

    file_path = os.path.join(tours_dir, file_name)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Skip if Recommended Tours section is already present
    if "Recommended Tours" in content:
        continue

    # Insert right before <!-- Footer -->
    target_str = "<!-- Footer -->"
    if target_str in content:
        content = content.replace(target_str, recommended_section_html + "\n\n        " + target_str, 1)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        total_updated += 1
        print(f"Added Recommended Tours section to [{file_name}]")

print(f"\nDone! Added Recommended Tours section across {total_updated} tour pages.")
