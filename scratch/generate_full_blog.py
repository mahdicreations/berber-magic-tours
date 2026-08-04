import os

root_dir = r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours"
blog_dir = os.path.join(root_dir, "blog")
os.makedirs(blog_dir, exist_ok=True)

# Common white header CSS to force non-transparent header on blog and article pages
white_header_style = """
    <style>
        /* Solid white header like tour pages */
        #header.header {
            background: white !important;
            background-image: none !important;
            padding: 10px 0 !important;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05) !important;
        }
        #header.header .top-bar { 
            border-bottom: 1px solid rgba(0, 0, 0, 0.1) !important; 
        }
        #header.header .top-bar-left a, 
        #header.header .top-bar-right span,
        #header.header .top-bar-socials a {
            color: var(--secondary) !important;
        }
        #header.header .top-bar-left a:hover,
        #header.header .top-bar-socials a:hover {
            color: var(--primary) !important;
        }
        #header.header .nav-list a { color: var(--secondary) !important; }
        #header.header .nav-list a:hover, #header.header .nav-list a.active { color: var(--primary) !important; }
        #header.header .header-flags { border-right: 1px solid rgba(0, 0, 0, 0.1) !important; }
        #header.header .mobile-menu-btn { color: var(--secondary) !important; }
    </style>
"""

# Articles Definition
articles = [
    {
        "slug": "ultimate-guide-trekking-mount-toubkal",
        "title": "The Ultimate Guide to Trekking Mount Toubkal | High Atlas Morocco",
        "seo_title": "The Ultimate Guide to Trekking Mount Toubkal | High Atlas Morocco",
        "seo_desc": "Everything you need to know about climbing Mount Toubkal (4,167m) in Morocco. Essential gear, acclimatization routes, best seasons, and local Berber guide advice.",
        "keywords": "Mount Toubkal trek, Mount Toubkal guide, Imlil trekking, climb Mount Toubkal, High Atlas Mountains Morocco, Toubkal acclimatization",
        "category": "Trekking Guide",
        "category_bg": "#D95D39",
        "date": "August 2026",
        "read_time": "8 min read",
        "image": "/assets/images/blog-toubkal.jpg",
        "tour_cta_title": "Ready to Summit Mount Toubkal?",
        "tour_cta_desc": "Join our certified local Berber guides for a safe, unforgettable 3-day or 4-day trek to North Africa's highest peak.",
        "tour_cta_link": "/tours/3-days-mount-toubkal",
        "tour_cta_btn": "View 3-Day Toubkal Trek",
        "content_html": """
            <div class="article-lead">
                <p>Standing tall at <strong>4,167 meters (13,671 feet)</strong>, Mount Toubkal (Jebel Toubkal) is the highest peak in North Africa and the Arabian World. Nestled in the dramatic High Atlas Mountains just 60 kilometers south of Marrakech, climbing Toubkal is one of Africa's most rewarding alpine trekking adventures.</p>
            </div>

            <div class="article-toc">
                <h4><i class="fas fa-list-ul"></i> Article Outline</h4>
                <ul>
                    <li><a href="#section-1">1. Why Climb Mount Toubkal?</a></li>
                    <li><a href="#section-2">2. Choosing Your Trek Itinerary (2, 3, or 4 Days)</a></li>
                    <li><a href="#section-3">3. Best Seasons to Trek Mount Toubkal</a></li>
                    <li><a href="#section-4">4. Essential Packing & Gear Checklist</a></li>
                    <li><a href="#section-5">5. Altitude & Safety: The Berber Guide Advantage</a></li>
                </ul>
            </div>

            <h2 id="section-1">1. Why Climb Mount Toubkal?</h2>
            <p>Mount Toubkal is widely considered one of the most accessible 4,000-meter peaks in the world. Unlike high peaks in the Himalayas or Andes, Toubkal requires no technical rock climbing skills during the summer season. What makes the trek truly unique is the blend of striking mountain geography and the rich culture of the native <strong>Amazigh (Berber) people</strong>.</p>
            <p>As you hike through terraced walnut groves and stone-built villages like Imlil and Aroumd, you're welcomed into ancient traditions, fresh mint tea ceremonies, and warm mountain hospitalities.</p>

            <blockquote class="article-quote">
                <i class="fas fa-quote-left"></i>
                <p>"Climbing Toubkal isn't just about reaching the summit marker; it's about sharing footsteps with local mountain families who have navigated these passes for centuries."</p>
            </blockquote>

            <h2 id="section-2">2. Choosing Your Trek Itinerary (2, 3, or 4 Days)</h2>
            <p>While some fit hikers opt for a rapid 2-day summit push, taking 3 or 4 days dramatically improves your acclimatization and overall enjoyment:</p>
            <ul>
                <li><strong>2-Day Toubkal Express:</strong> Day 1 hike from Imlil (1,740m) to Toubkal Refuge (3,207m). Day 2 early morning summit climb (4,167m) and complete descent back to Imlil. Best for experienced hikers with limited time.</li>
                <li><strong>3-Day Toubkal & Acclimatization Trek (Recommended):</strong> Includes an extra day exploring neighboring valleys (like Tizi Mzik pass) before heading to the refuge, allowing your body to adapt naturally to altitude.</li>
                <li><strong>4-Day Toubkal & Azzaden Valley Loop:</strong> Combines the dramatic red clay villages of Azzaden Valley with the Toubkal summit, offering the ultimate Atlas wilderness experience.</li>
            </ul>

            <h2 id="section-3">3. Best Seasons to Trek Mount Toubkal</h2>
            <p>Toubkal is a year-round trekking destination, but each season presents a distinct atmosphere:</p>
            <ul>
                <li><strong>Spring (April to June):</strong> Clear skies, blossoming wildflowers, mild temperatures, and melting snowfields. Perfect weather for trekking.</li>
                <li><strong>Summer (July to August):</strong> Warm daytime temperatures in lower valleys, though cool at the refuge. Summit climbs start early at 4:30 AM to beat the mid-day heat.</li>
                <li><strong>Autumn (September to November):</strong> Golden autumn light, pleasant hiking climate, and clear blue mountain views.</li>
                <li><strong>Winter (December to March):</strong> Transforms Toubkal into an alpine wonderland requiring crampons and ice axes.</li>
            </ul>

            <h2 id="section-4">4. Essential Packing & Gear Checklist</h2>
            <p>Equipping yourself properly ensures comfort across fluctuating mountain microclimates:</p>
            <div class="key-takeaways-box">
                <h4><i class="fas fa-check-circle"></i> Mandatory Gear Checklist</h4>
                <ul>
                    <li>Sturdy, well-broken-in hiking boots with good ankle support.</li>
                    <li>Layered clothing: thermal base layer, fleece mid-layer, and waterproof/windproof outer shell.</li>
                    <li>Warm beanie hat, light gloves, and UV protection sunglasses.</li>
                    <li>Hydration bladder (at least 2 liters) and water purification tablets.</li>
                    <li>Trekking poles (highly recommended for descending scree slopes).</li>
                    <li>Headlamp with spare batteries for early summit morning.</li>
                </ul>
            </div>

            <h2 id="section-5">5. Altitude & Safety: The Berber Guide Advantage</h2>
            <p>Official Moroccan regulations require all trekkers on Mount Toubkal to be accompanied by a licensed mountain guide. Beyond legal compliance, hiring a local Berber guide from Berber Magic Tours guarantees safety, proper pacing, refuge reservations, and mule support for your heavy luggage.</p>
            <p>Our guides are born and raised in the High Atlas, trained in wilderness first aid, and deeply passionate about sharing their mountain heritage with guests from all over the world.</p>
        """
    },
    {
        "slug": "sahara-desert-erg-chebbi-vs-chigaga",
        "title": "Sahara Desert Guide: Erg Chebbi vs Erg Chigaga | Morocco",
        "seo_title": "Sahara Desert Guide: Erg Chebbi vs Erg Chigaga | Berber Magic Tours",
        "seo_desc": "Which Sahara desert dunes are right for your Morocco trip? Compare dune heights, luxury glamping camps, camel treks, and stargazing in Merzouga vs Zagora.",
        "keywords": "Sahara desert tours, Merzouga desert camp, Erg Chebbi sand dunes, Erg Chigaga 4x4, Morocco desert trip",
        "category": "Sahara Desert",
        "category_bg": "#0284C7",
        "date": "July 2026",
        "read_time": "6 min read",
        "image": "/assets/images/blog-sahara.jpg",
        "tour_cta_title": "Experience the Magic of the Sahara Desert",
        "tour_cta_desc": "Book an unforgettable 3-day or 4-day desert tour from Marrakech to Merzouga with luxury camp stays and camel sunset rides.",
        "tour_cta_link": "/tours/3days-merzouga-desert",
        "tour_cta_btn": "View 3-Day Merzouga Desert Tour",
        "content_html": """
            <div class="article-lead">
                <p>Few travel experiences on Earth match spending a night under the starry sky of the <strong>Sahara Desert in Morocco</strong>. Riding camels across undulating golden sand dunes, enjoying traditional Gnawa drum music around a flickering bonfire, and watching sunrise over the horizon are unforgettable highlights.</p>
            </div>

            <div class="article-toc">
                <h4><i class="fas fa-list-ul"></i> Article Outline</h4>
                <ul>
                    <li><a href="#section-1">1. Erg Chebbi (Merzouga): The Iconic Golden Dunes</a></li>
                    <li><a href="#section-2">2. Erg Chigaga (Zagora): Wild & Off-the-Beaten-Path</a></li>
                    <li><a href="#section-3">3. Comparing Erg Chebbi vs Erg Chigaga</a></li>
                    <li><a href="#section-4">4. What to Pack for Your Sahara Trip</a></li>
                </ul>
            </div>

            <h2 id="section-1">1. Erg Chebbi (Merzouga): The Iconic Golden Dunes</h2>
            <p>Located near the village of Merzouga in southeastern Morocco, <strong>Erg Chebbi</strong> features towering dunes that rise up to 150 meters (500 feet). The sand possesses a brilliant orange-gold hue that shifts color dramatically during sunrise and sunset.</p>
            <ul>
                <li><strong>Accessibility:</strong> Paved roads lead directly to the edge of the dunes, making Merzouga easily accessible for 3-day tours from Marrakech or Fes.</li>
                <li><strong>Luxury Glamping:</strong> Erg Chebbi hosts world-class luxury desert camps featuring king-size beds, hand-woven Berber carpets, en-suite bathrooms with hot showers, and gourmet Moroccan dinners.</li>
                <li><strong>Activities:</strong> Camel trekking, quad biking, sandboarding, 4x4 dune bashing, and stargazing.</li>
            </ul>

            <h2 id="section-2">2. Erg Chigaga (Zagora): Wild & Off-the-Beaten-Path</h2>
            <p>Stretching across 40 kilometers of rugged wilderness near M'Hamid, <strong>Erg Chigaga</strong> is Morocco's largest and most remote dune field. Reaching Chigaga requires 2 to 3 hours of thrilling 4x4 off-road driving across hamada (stone desert).</p>
            <ul>
                <li><strong>Vibe:</strong> Remote, quiet, and wild. Ideal for travelers wanting pure silence and solitude away from crowds.</li>
                <li><strong>Best For:</strong> Off-road enthusiasts and travelers taking 4 to 5 days for a deep desert safari.</li>
            </ul>

            <h2 id="section-3">3. Comparing Erg Chebbi vs Erg Chigaga</h2>
            <div class="key-takeaways-box">
                <h4><i class="fas fa-balance-scale"></i> Quick Comparison Guide</h4>
                <ul>
                    <li><strong>Dune Height:</strong> Erg Chebbi (150m) > Erg Chigaga (60m).</li>
                    <li><strong>Luxury & Comfort:</strong> Erg Chebbi offers higher-end glamping infrastructure.</li>
                    <li><strong>Drive Access:</strong> Erg Chebbi is accessible by standard road; Erg Chigaga requires 4x4 off-road transfer.</li>
                    <li><strong>Best Choice:</strong> For 3-day tours from Marrakech, <strong>Erg Chebbi (Merzouga)</strong> is the top recommended destination.</li>
                </ul>
            </div>

            <h2 id="section-4">4. What to Pack for Your Sahara Trip</h2>
            <p>Desert temperatures fluctuate widely—hot daytime sun followed by cool desert night breeze:</p>
            <ul>
                <li>Lightweight breathable cotton clothing for daytime.</li>
                <li>Warm fleece or jacket for nighttime around the campfire.</li>
                <li>Chech (traditional Berber turban scarf) to protect against desert wind and sun.</li>
                <li>Sunglasses, sunscreen, and lip balm.</li>
                <li>Camera with protective dust pouch.</li>
            </ul>
        """
    },
    {
        "slug": "exploring-hidden-atlas-valleys",
        "title": "Exploring Hidden Atlas Valleys: Imlil, Ourika & Azzaden",
        "seo_title": "Exploring Hidden Atlas Valleys: Imlil, Ourika & Azzaden | Morocco",
        "seo_desc": "Discover the pristine High Atlas river valleys of Morocco. Explore traditional stone Berber villages, walnut groves, waterfalls, and authentic mountain life.",
        "keywords": "Berber villages trek, Imlil valley hike, Azzaden valley trekking, High Atlas valleys, Morocco day trips",
        "category": "Cultural Treks",
        "category_bg": "#16A34A",
        "date": "July 2026",
        "read_time": "6 min read",
        "image": "/assets/images/blog-valleys.jpg",
        "tour_cta_title": "Hike the Enchanting Berber Valleys",
        "tour_cta_desc": "Explore authentic stone villages, terraced farms, and alpine passes on our 2-day or 3-day Atlas Mountain valley treks.",
        "tour_cta_link": "/tours/3days-in-three-valleys",
        "tour_cta_btn": "Explore 3 Valleys Trek",
        "content_html": """
            <div class="article-lead">
                <p>Just one hour from the bustling souks of Marrakech lie the peaceful, green sanctuaries of the <strong>High Atlas Mountains</strong>. Here, ancient river valleys wind beneath towering granite peaks, sheltering stone and mudbrick Berber villages unchanged for generations.</p>
            </div>

            <h2>1. Imlil Valley: The Heart of the High Atlas</h2>
            <p>Sitting at 1,740 meters altitude, <strong>Imlil Valley</strong> is the vibrant beating heart of Atlas mountain tourism. Surrounded by walnut orchards, apple trees, and terraced barley fields, Imlil serves as the scenic basecamp for trekkers venturing toward Toubkal.</p>
            <p>Hiking between mountain hamlets such as Aroumd, Tamatert, and Targa Imoula lets you observe daily mountain life—children heading to school, elders tending terraced gardens, and mules transporting harvest yields.</p>

            <h2>2. Azzaden Valley: The Hidden Gem</h2>
            <p>Known as the "Red Valley" due to its rich terra-cotta clay soil and traditional red homes, <strong>Azzaden Valley</strong> remains blissfully serene and secluded. Accessing Azzaden requires hiking over scenic mountain passes like Tizi n'Test or Tizi Mzik.</p>
            <p>Walking along the Azzaden River beneath giant juniper trees provides a peaceful retreat from modern city life.</p>

            <h2>3. Ourika Valley: Waterfalls & Cool Waters</h2>
            <p>Famous for its rushing mountain river and seven cascades at Setti Fatma, <strong>Ourika Valley</strong> is a beloved day trip destination. Visitors enjoy sipping fresh orange juice or mint tea at riverside wooden tables set right in the cool water currents during warm summer afternoons.</p>

            <div class="key-takeaways-box">
                <h4><i class="fas fa-heart"></i> Why Trek Valley Villages with Local Guides?</h4>
                <ul>
                    <li>Dine on authentic home-cooked Berber tagines inside local family guesthouses.</li>
                    <li>Support sustainable local village economies through responsible tourism.</li>
                    <li>Cross scenic high-altitude passes with muleteers carrying your luggage safely.</li>
                </ul>
            </div>
        """
    },
    {
        "slug": "first-time-morocco-travel-tips",
        "title": "First Time in Morocco? 10 Essential Cultural & Travel Tips",
        "seo_title": "10 Essential Morocco Travel & Culture Tips for First-Timers",
        "seo_desc": "First visit to Morocco? Learn essential tips on souk bargaining, mint tea etiquette, currency Dirhams, dress codes, and local Berber customs.",
        "keywords": "Morocco travel tips, Moroccan culture etiquette, souk bargaining Marrakech, mint tea Morocco, currency Dirham",
        "category": "Travel Tips",
        "category_bg": "#8B5CF6",
        "date": "June 2026",
        "read_time": "7 min read",
        "image": "/assets/images/blog-morocco.jpg",
        "tour_cta_title": "Plan Your Dream Morocco Journey",
        "tour_cta_desc": "Let our local Berber travel experts craft your tailored private tour around Marrakech, the Atlas Mountains, and the Sahara.",
        "tour_cta_link": "/contact",
        "tour_cta_btn": "Contact Our Travel Experts",
        "content_html": """
            <div class="article-lead">
                <p>Morocco is a captivating land where ancient medina alleys, majestic snow-capped peaks, and endless golden dunes come together. To help first-time visitors travel smoothly and respectfully, here are 10 expert cultural and practical tips from our local team.</p>
            </div>

            <h2>1. Moroccan Mint Tea ("Berber Whiskey")</h2>
            <p>Fresh mint tea is the heart of Moroccan hospitality. Poured from high above to create a frothy foam crown, accepting a glass when offered by shopkeepers or hosts is a universal gesture of friendship and warmth.</p>

            <h2>2. Cash is King (Moroccan Dirham - MAD)</h2>
            <p>While major credit cards are accepted in high-end hotels and restaurants in Marrakech and Casablanca, cash is essential in rural villages, souks, mountain guesthouses, and taxis. Always keep small bank notes (20, 50 MAD) handy.</p>

            <h2>3. Master the Art of Souk Haggling</h2>
            <p>Bargaining in Marrakech or Fes souks is expected and meant to be a friendly conversation. Smile, remain polite, and start negotiations around 40-50% of the initial quoted price until both sides agree happily.</p>

            <h2>4. Respectful Attire in Public</h2>
            <p>Morocco is a welcoming yet culturally conservative country. Wearing clothing that covers shoulders and knees when exploring medinas, markets, and mountain villages shows cultural respect and ensures comfortable interactions.</p>

            <h2>5. Tipping Customs (Baksheesh)</h2>
            <p>Tipping is customary in Morocco. Leaving 10% in cafes and restaurants is standard practice. For private drivers and mountain trekking guides, tipping at the end of your tour acknowledges their personal care and dedication.</p>

            <div class="key-takeaways-box">
                <h4><i class="fas fa-lightbulb"></i> Extra First-Timer Quick Tips</h4>
                <ul>
                    <li>Always ask permission before taking photos of street vendors or locals.</li>
                    <li>Drink bottled or filtered water during your stay.</li>
                    <li>Greetings: Placing your hand on your heart after shaking hands expresses sincere warmth.</li>
                </ul>
            </div>
        """
    },
    {
        "slug": "mount-toubkal-winter-ascent-guide",
        "title": "Mount Toubkal Winter Ascent: Preparation, Gear & Safety",
        "seo_title": "Mount Toubkal Winter Ascent: Gear, Safety & Preparation | Morocco",
        "seo_desc": "Guide to climbing Mount Toubkal in winter. Snow conditions, crampon and ice axe gear requirements, refuge stays, and alpine safety tips.",
        "keywords": "Toubkal winter climb, winter mountaineering Morocco, crampons Toubkal, Toubkal refuge winter, winter trek Imlil",
        "category": "Winter Treks",
        "category_bg": "#0284C7",
        "date": "June 2026",
        "read_time": "6 min read",
        "image": "/assets/images/blog-winter-toubkal.jpg",
        "tour_cta_title": "Challenge Yourself on a Winter Summit Climb",
        "tour_cta_desc": "Conquer snow-capped Mount Toubkal with our experienced alpine Berber guides and technical gear support.",
        "tour_cta_link": "/tours/toubkal-winter-climb",
        "tour_cta_btn": "View Winter Toubkal Climb",
        "content_html": """
            <div class="article-lead">
                <p>From December through April, the High Atlas Mountains transform into a striking alpine arena. Ascending Mount Toubkal in winter snow conditions offers experienced hikers a thrilling winter mountaineering challenge.</p>
            </div>

            <h2>1. Winter Snow & Weather Conditions</h2>
            <p>Snow blankets the peaks above 2,500 meters altitude. Temperatures at the Toubkal Refuge (3,207m) drop below freezing (-5°C to -15°C at pre-dawn summit start). Blue sunny skies are frequent, but alpine weather can shift quickly.</p>

            <h2>2. Technical Gear Essentials</h2>
            <p>Unlike trekking in summer, winter climbs require technical equipment for safety:</p>
            <ul>
                <li><strong>Crampons & Ice Axe:</strong> Required for ascending the icy snow couloirs on the South Ikhibi summit route. Our team fits technical equipment in Imlil before ascending.</li>
                <li><strong>Mountaineering Boots:</strong> Stiff, insulated boots compatible with crampon bindings.</li>
                <li><strong>Thermal Layering & Goggles:</strong> Heavy down jacket, thermal underwear, windproof hardshell, ski goggles, and insulated gloves.</li>
            </ul>

            <h2>3. Alpine Safety & Refuge Comfort</h2>
            <p>Our winter expeditions base at the heated Les Mouflons / CAF Toubkal Refuge, featuring warm communal meals, hot showers, and indoor dining lounge. Certified mountain guides monitor avalanche safety daily to ensure a secure summit push.</p>

            <div class="key-takeaways-box">
                <h4><i class="fas fa-snowflake"></i> Winter Climb Key Takeaways</h4>
                <ul>
                    <li>Pre-dawn summit start at 5:00 AM to take advantage of firm snow conditions.</li>
                    <li>Technical crampon training provided by guides prior to summit morning.</li>
                    <li>Full luggage transport by winter mules up to the snowline.</li>
                </ul>
            </div>
        """
    },
    {
        "slug": "moroccan-gastronomy-culinary-guide",
        "title": "Moroccan Gastronomy & Culinary Secrets: From Tagine to Pastilla",
        "seo_title": "Moroccan Gastronomy & Food Guide: Tagine, Pastilla & Spices",
        "seo_desc": "Explore the rich world of Moroccan gastronomy. Slow-cooked clay tagines, sweet and savory pastilla pastry, Friday couscous, and Imlil cooking classes.",
        "keywords": "Moroccan gastronomy, traditional Berber tagine, Moroccan food guide, cooking class Imlil, Marrakech spices",
        "category": "Gastronomy",
        "category_bg": "#D97706",
        "date": "May 2026",
        "read_time": "5 min read",
        "image": "/assets/images/blog-moroccan-food.jpg",
        "tour_cta_title": "Join Our Authentic Berber Cooking Class",
        "tour_cta_desc": "Visit local spice markets and cook traditional Moroccan tagines with a Berber family in the Atlas Mountains.",
        "tour_cta_link": "/tours/cooking-class-in-high-atlas",
        "tour_cta_btn": "Book High Atlas Cooking Class",
        "content_html": """
            <div class="article-lead">
                <p>Moroccan cuisine is world-renowned for its sublime harmony of sweet and savory notes, fragrant spices, and slow-cooked Berber tagine traditions. Dining in Morocco is a celebration of family, culture, and ancient culinary history.</p>
            </div>

            <h2>1. The Art of Slow-Cooked Berber Tagines</h2>
            <p>Named after the conical terracotta pot in which it simmers over glowing embers, the tagine locks in moisture and infuses delicate flavors. Tender lamb with caramelized prunes and toasted almonds, or chicken with preserved lemons and green olives, are iconic classics.</p>

            <h2>2. Pastilla: The Royal Sweet & Savory Pastry</h2>
            <p>Pastilla is a culinary masterpiece featuring paper-thin warka pastry layers stuffed with spiced shredded chicken or pigeon, layered with toasted crushed almonds, and finished with a delicate dusting of powdered sugar and cinnamon.</p>

            <h2>3. Friday Couscous Tradition</h2>
            <p>In Moroccan culture, Fridays are dedicated to family gatherings around a large clay platter of hand-rolled, fluffy steamed couscous heaped with seven tender vegetables and rich savory broth.</p>

            <h2>4. Essential Moroccan Spices</h2>
            <div class="key-takeaways-box">
                <h4><i class="fas fa-pepper-hot"></i> Key Moroccan Spices</h4>
                <ul>
                    <li><strong>Saffron:</strong> Harvested by hand in Taliouine, giving golden color and earthy aroma.</li>
                    <li><strong>Cumin:</strong> Freshly ground for tagines, grilled meats, and salads.</li>
                    <li><strong>Ras el Hanout:</strong> The "head of the shop" master spice blend containing up to 30 aromatic spices.</li>
                    <li><strong>Cinnamon & Ginger:</strong> Essential for balancing sweet and savory meat glazes.</li>
                </ul>
            </div>
        """
    }
]

# Generate Individual Blog Post HTML Files (without author info & with white header CSS)
for art in articles:
    post_filename = os.path.join(blog_dir, f"{art['slug']}.html")
    
    page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{art['seo_title']}</title>
    <meta name="description" content="{art['seo_desc']}">
    <meta name="keywords" content="{art['keywords']}">
    <link rel="canonical" href="https://berber-magic-tours.com/blog/{art['slug']}" />
    <meta property="og:title" content="{art['seo_title']}">
    <meta property="og:description" content="{art['seo_desc']}">
    <meta property="og:image" content="https://berber-magic-tours.com{art['image']}">
    <meta property="og:url" content="https://berber-magic-tours.com/blog/{art['slug']}">
    <meta property="og:type" content="article">
    <link rel="stylesheet" href="/assets/css/style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Style+Script&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/lipis/flag-icons@7.0.0/css/flag-icons.min.css" />
    {white_header_style}
    <style>
        /* Blog Post Dedicated Styles */
        .article-hero {{
            background: #F8FAFC;
            padding: 50px 0 30px 0;
            border-bottom: 1px solid #E2E8F0;
        }}
        .breadcrumb {{
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 0.88rem;
            color: #64748B;
            margin-bottom: 20px;
        }}
        .breadcrumb a {{
            color: var(--secondary);
            text-decoration: none;
            font-weight: 500;
        }}
        .breadcrumb a:hover {{
            color: var(--primary);
        }}
        .article-category-badge {{
            display: inline-block;
            background: {art['category_bg']};
            color: #ffffff;
            font-size: 0.78rem;
            font-weight: 700;
            padding: 4px 14px;
            border-radius: 50px;
            text-transform: uppercase;
            letter-spacing: 0.6px;
            margin-bottom: 15px;
        }}
        .article-main-title {{
            font-family: var(--font-heading);
            font-size: 2.6rem;
            color: var(--secondary);
            line-height: 1.28;
            margin-bottom: 20px;
        }}
        .article-meta-bar {{
            display: flex;
            align-items: center;
            gap: 20px;
            font-size: 0.88rem;
            color: #64748B;
            padding-bottom: 10px;
            flex-wrap: wrap;
        }}
        .article-meta-bar span {{
            display: flex;
            align-items: center;
            gap: 6px;
        }}
        .article-meta-bar i {{
            color: var(--primary);
        }}
        .article-cover-wrapper {{
            margin: 35px 0 45px 0;
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 12px 35px rgba(0,0,0,0.08);
            max-height: 480px;
        }}
        .article-cover-wrapper img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
        }}
        .article-container {{
            max-width: 860px;
            margin: 0 auto;
            padding: 0 20px 70px 20px;
        }}
        .article-body-text {{
            font-size: 1.05rem;
            color: #334155;
            line-height: 1.85;
        }}
        .article-body-text p {{
            margin-bottom: 22px;
            text-align: justify;
        }}
        .article-body-text h2 {{
            font-family: var(--font-heading);
            font-size: 1.75rem;
            color: var(--secondary);
            margin: 36px 0 16px 0;
            padding-bottom: 8px;
            border-bottom: 2px solid #F1F5F9;
        }}
        .article-body-text h3 {{
            font-family: var(--font-heading);
            font-size: 1.3rem;
            color: var(--secondary);
            margin: 26px 0 12px 0;
        }}
        .article-body-text ul {{
            margin-bottom: 24px;
            padding-left: 22px;
        }}
        .article-body-text li {{
            margin-bottom: 10px;
            color: #334155;
        }}
        .article-lead {{
            font-size: 1.15rem;
            font-weight: 500;
            color: #1E293B;
            line-height: 1.8;
            background: #F1F5F9;
            padding: 22px 28px;
            border-left: 4px solid var(--primary);
            border-radius: 0 12px 12px 0;
            margin-bottom: 30px;
        }}
        .article-toc {{
            background: #FFF7F2;
            border: 1px solid #FFEDD5;
            padding: 22px 28px;
            border-radius: 14px;
            margin-bottom: 35px;
        }}
        .article-toc h4 {{
            font-size: 1.05rem;
            color: var(--primary-dark);
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .article-toc ul {{
            margin: 0;
            padding-left: 18px;
        }}
        .article-toc li {{
            margin-bottom: 6px;
        }}
        .article-toc a {{
            color: #475569;
            text-decoration: none;
            font-weight: 600;
            font-size: 0.94rem;
        }}
        .article-toc a:hover {{
            color: var(--primary);
        }}
        .article-quote {{
            background: #F8FAFC;
            border-left: 4px solid var(--secondary);
            padding: 24px 30px;
            border-radius: 0 14px 14px 0;
            margin: 35px 0;
            position: relative;
        }}
        .article-quote i {{
            font-size: 1.8rem;
            color: #CBD5E1;
            margin-bottom: 10px;
            display: block;
        }}
        .article-quote p {{
            font-family: var(--font-heading);
            font-size: 1.2rem;
            font-style: italic;
            color: var(--secondary);
            margin-bottom: 0;
        }}
        .key-takeaways-box {{
            background: #F0FDF4;
            border: 1px solid #BBF7D0;
            padding: 24px 28px;
            border-radius: 14px;
            margin: 30px 0;
        }}
        .key-takeaways-box h4 {{
            color: #15803D;
            font-size: 1.1rem;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .key-takeaways-box ul {{
            margin: 0;
            padding-left: 20px;
        }}
        .key-takeaways-box li {{
            color: #166534;
        }}
        .article-tour-cta {{
            background: linear-gradient(135deg, var(--secondary) 0%, #0F172A 100%);
            color: #ffffff;
            border-radius: 18px;
            padding: 35px;
            margin: 50px 0;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 25px;
            box-shadow: 0 12px 30px rgba(0,0,0,0.15);
        }}
        .article-tour-cta h3 {{
            font-family: var(--font-heading);
            font-size: 1.5rem;
            color: #ffffff;
            margin-bottom: 8px;
        }}
        .article-tour-cta p {{
            color: #94A3B8;
            font-size: 0.95rem;
            margin: 0;
            text-align: left;
        }}
        .article-tour-cta .btn {{
            white-space: nowrap;
            padding: 12px 24px;
        }}
        @media (max-width: 768px) {{
            .article-main-title {{ font-size: 2rem; }}
            .article-container {{ padding: 0 15px 50px 15px; }}
            .article-tour-cta {{ flex-direction: column; text-align: center; text-align-last: center; }}
            .article-tour-cta p {{ text-align: center; }}
        }}
    </style>
</head>
<body>
    <!-- Header -->
    <header id="header" class="header">
        <div class="top-bar">
            <div class="container top-bar-container">
                <div class="top-bar-left">
                    <a href="https://wa.me/212653274190" target="_blank"><i class="fab fa-whatsapp"></i> +212 653 274 190</a>
                    <a href="mailto:info@berber-magic-tours.com"><i class="far fa-envelope"></i> info@berber-magic-tours.com</a>
                </div>
                <div class="top-bar-right">
                    <span><i class="fas fa-map-marker-alt"></i> Douar Imlil, Marrakech</span>
                    <div class="top-bar-socials">
                        <a href="YOUR_LINK_HERE" target="_blank"><i class="fab fa-facebook-f"></i></a>
                        <a href="YOUR_LINK_HERE" target="_blank"><i class="fab fa-instagram"></i></a>
                        <a href="YOUR_LINK_HERE" target="_blank"><i class="fab fa-tripadvisor"></i></a>
                    </div>
                </div>
            </div>
        </div>

        <div class="container header-container">
            <div class="logo">
                <a href="/"><img src="/assets/images/logo.png" alt="Berber Magic Tours"></a>
            </div>
            
            <nav class="nav">
                <ul class="nav-list">
                    <li><a href="/">Home</a></li>
                    <li><a href="/marrakech-day-trips">Marrakech Day Trips</a></li>
                    
                    <li class="dropdown">
                        <a href="/trek-and-hike">Trek &amp; Hike <i class="fas fa-chevron-down"></i></a>
                        <ul class="dropdown-menu">
                            <li><a href="/climb-mount-toubkal">Climb Mount Toubkal</a></li>
                            <li><a href="/berber-village-treks">Berber Village Treks</a></li>
                            <li><a href="/combine-toubkal-and-villages">Combine Toubkal &amp; Villages</a></li>
                            <li><a href="/biking-in-morocco">Biking in Morocco</a></li>
                        </ul>
                    </li>
                    
                    <li class="dropdown">
                        <a href="/combine-atlas-mountains-and-desert">Combine Atlas Mountains &amp; Desert <i class="fas fa-chevron-down"></i></a>
                        <ul class="dropdown-menu">
                            <li><a href="/combine-berber-villages-and-sahara">Combine Berber Villages &amp; Sahara</a></li>
                            <li><a href="/combine-toubkal-and-sahara">Combine Toubkal &amp; Sahara</a></li>
                        </ul>
                    </li>
                    
                    <li class="dropdown">
                        <a href="#">Other Tours <i class="fas fa-chevron-down"></i></a>
                        <ul class="dropdown-menu">
                            <li class="dropdown-submenu">
                                <a href="/sahara-desert-tours">Sahara Desert Tours <i class="fas fa-chevron-right"></i></a>
                                <ul class="dropdown-menu">
                                    <li><a href="/tours-from-marrakech">Tours from Marrakech</a></li>
                                    <li><a href="/tours-from-casablanca">Tours from Casablanca</a></li>
                                    <li><a href="/tours-from-fes">Tours from Fes</a></li>
                                </ul>
                            </li>
                            <li><a href="/morocco-tours">Morocco Tours</a></li>
                        </ul>
                    </li>
                </ul>
            </nav>
            
            <div class="header-actions">
                <div class="header-flags">
                    <span class="fi fi-gb"></span>
                    <span class="fi fi-fr"></span>
                    <span class="fi fi-es"></span>
                </div>
                <a href="/contact" class="btn btn-primary"><i class="fas fa-envelope"></i> Contact Us</a>
                <button class="mobile-menu-btn"><i class="fas fa-bars"></i></button>
            </div>
        </div>
    </header>

    <!-- Mobile Menu -->
    <div class="mobile-menu">
        <div class="mobile-menu-header">
            <img src="/assets/images/logo.png" alt="Berber Magic Tours" class="mobile-logo">
            <button class="mobile-menu-close"><i class="fas fa-times"></i></button>
        </div>
        <ul class="mobile-nav-list">
            <li><a href="/">Home</a></li>
            <li><a href="/about-us">About Us</a></li>
            <li><a href="/faq">FAQ</a></li>
            <li><a href="/marrakech-day-trips">Marrakech Day Trips</a></li>
            <li><a href="/trek-and-hike">Trek &amp; Hike</a></li>
            <li><a href="/sahara-desert-tours">Sahara Desert Tours</a></li>
            <li><a href="/morocco-tours">Morocco Tours</a></li>
            <li><a href="/contact">Contact Us</a></li>
        </ul>
    </div>
    <div class="mobile-overlay"></div>

    <!-- Article Hero Header -->
    <section class="article-hero">
        <div class="container" style="max-width: 860px;">
            <div class="breadcrumb">
                <a href="/">Home</a> <i class="fas fa-chevron-right" style="font-size: 0.7rem;"></i>
                <a href="/blog">Blog</a> <i class="fas fa-chevron-right" style="font-size: 0.7rem;"></i>
                <span>{art['category']}</span>
            </div>
            
            <span class="article-category-badge">{art['category']}</span>
            <h1 class="article-main-title">{art['title']}</h1>

            <div class="article-meta-bar">
                <span><i class="far fa-calendar-alt"></i> {art['date']}</span>
                <span><i class="far fa-clock"></i> {art['read_time']}</span>
            </div>
        </div>
    </section>

    <!-- Main Article Body -->
    <article class="article-container">
        <div class="article-cover-wrapper">
            <img src="{art['image']}" alt="{art['title']}">
        </div>

        <div class="article-body-text">
            {art['content_html']}
        </div>

        <!-- Related Tour Banner CTA -->
        <div class="article-tour-cta">
            <div>
                <h3>{art['tour_cta_title']}</h3>
                <p>{art['tour_cta_desc']}</p>
            </div>
            <a href="{art['tour_cta_link']}" class="btn btn-primary">{art['tour_cta_btn']} <i class="fas fa-arrow-right"></i></a>
        </div>
    </article>

    <!-- Footer -->
    <footer class="footer">
        <div class="container footer-container">
            <div class="footer-grid">
                <!-- Col 1: About -->
                <div class="footer-col about-col">
                    <img src="/assets/images/logo.png" alt="Berber Magic Tours" class="footer-logo">
                    <p class="footer-desc">Experience the magic of Morocco through the eyes of Locals. Let us help you find a journey of a lifetime.</p>
                    <ul class="footer-contact-list">
                        <li><i class="fas fa-map-marker-alt"></i> <span>Douar Imlil Poste Asni 42152 Marrakech</span></li>
                        <li><i class="fab fa-whatsapp"></i> <span>+212 653 274 190</span></li>
                        <li><i class="fas fa-envelope"></i> <a href="mailto:info@berber-magic-tours.com">info@berber-magic-tours.com</a></li>
                    </ul>
                    <div class="social-links mt-4">
                        <a href="YOUR_LINK_HERE" target="_blank" title="Facebook"><i class="fab fa-facebook-f"></i></a>
                        <a href="YOUR_LINK_HERE" target="_blank" title="Instagram"><i class="fab fa-instagram"></i></a>
                        <a href="YOUR_LINK_HERE" target="_blank" title="LinkedIn"><i class="fab fa-linkedin-in"></i></a>
                    </div>
                </div>
                
                <!-- Col 2: Menu -->
                <div class="footer-col links-col">
                    <h3 class="footer-title">Menu</h3>
                    <ul class="footer-links">
                        <li><a href="/">Home</a></li>
                        <li><a href="/about-us">About Us</a></li>
                        <li><a href="/faq">FAQ</a></li>
                        <li><a href="/marrakech-day-trips">Marrakech Day Trips</a></li>
                        <li><a href="/trek-and-hike">Trek &amp; Hike</a></li>
                        <li><a href="/sahara-desert-tours">Sahara Desert Tours</a></li>
                        <li><a href="/morocco-tours">Morocco Tours</a></li>
                        <li><a href="/blog">Blog</a></li>
                        <li><a href="/contact">Contact Us</a></li>
                    </ul>
                </div>
                
                <!-- Col 3: Popular Morocco -->
                <div class="footer-col popular-col">
                    <h3 class="footer-title">Popular Morocco</h3>
                    <ul class="footer-links">
                        <li><a href="/#trek-hike">Exploring Berber villages &amp; valleys</a></li>
                        <li><a href="/#trek-hike">Climbing Mount Toubkal</a></li>
                        <li><a href="/#tours">Day trips from Marrakech</a></li>
                        <li><a href="/#desert-tours">Desert Tours</a></li>
                        <li><a href="/#morocco-tours">Morocco Trips</a></li>
                        <li><a href="/#combine-tours">Combine Atlas mountains &amp; Desert</a></li>
                    </ul>
                </div>
                
                <!-- Col 4: TripAdvisor -->
                <div class="footer-col tripadvisor-col">
                    <h3 class="footer-title">Recommended</h3>
                    <div class="tripadvisor-widget-dark">
                        <div class="tripadvisor-logo-wrapper">
                            <i class="fab fa-tripadvisor"></i>
                            <span>Tripadvisor</span>
                        </div>
                        <div class="tripadvisor-rating">
                            <span class="bubble"></span>
                            <span class="bubble"></span>
                            <span class="bubble"></span>
                            <span class="bubble"></span>
                            <span class="bubble"></span>
                        </div>
                        <p>Recommended by travelers</p>
                        <a href="YOUR_LINK_HERE" class="btn btn-tripadvisor" target="_blank">View Reviews</a>
                    </div>
                </div>
            </div>
            
            <div class="footer-bottom">
                <p>&copy; 2026 Berber Magic Tours. All Rights Reserved.</p>
                <div class="footer-legal-links">
                    <a href="/privacy-policy">Privacy Policy</a> | <a href="/terms-conditions">Terms &amp; Conditions</a>
                </div>
                <p class="footer-signature mt-2" style="font-size: 0.85rem; color: #94A3B8;">Designed with <i class="fas fa-heart" style="color: #D95D39;"></i> by <a href="https://mahdicreations.dev" target="_blank" rel="noopener" style="color: #ffffff; text-decoration: underline;">mahdicreations.dev</a></p>
            </div>
        </div>
    </footer>

    <script src="/assets/js/main.js?v=1.1"></script>
</body>
</html>"""

    with open(post_filename, "w", encoding="utf-8") as pf:
        pf.write(page_html)

    print(f"Generated blog post page: blog/{art['slug']}.html")

# Generate blog/index.html & root blog.html (with white header CSS)
cards_html = ""
for art in articles:
    cards_html += f"""
                <!-- Article Card -->
                <div class="blog-card">
                    <div class="blog-card-img">
                        <img src="{art['image']}" alt="{art['title']}">
                        <span class="blog-card-tag" style="background: {art['category_bg']};">{art['category']}</span>
                    </div>
                    <div class="blog-card-body">
                        <div class="blog-meta">
                            <span><i class="far fa-calendar-alt"></i> {art['date']}</span>
                            <span><i class="far fa-clock"></i> {art['read_time']}</span>
                        </div>
                        <h3 class="blog-card-title">{art['title']}</h3>
                        <p class="blog-excerpt">{art['seo_desc']}</p>
                        <a href="/blog/{art['slug']}" class="blog-read-btn">
                            Read Full Article <i class="fas fa-arrow-right"></i>
                        </a>
                    </div>
                </div>
"""

blog_index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Morocco Travel & Trekking Blog | Berber Magic Tours</title>
    <meta name="description" content="Discover expert Morocco travel advice, Mount Toubkal trekking guides, Sahara desert tips, winter mountaineering, and authentic Berber cultural insights.">
    <link rel="canonical" href="https://berber-magic-tours.com/blog" />
    <meta property="og:title" content="Morocco Travel & Trekking Blog | Berber Magic Tours">
    <meta property="og:description" content="Discover expert Morocco travel advice, Mount Toubkal trekking guides, Sahara desert tips, winter mountaineering, and authentic Berber cultural insights.">
    <meta property="og:image" content="https://berber-magic-tours.com/assets/images/blog-toubkal.jpg">
    <meta property="og:url" content="https://berber-magic-tours.com/blog">
    <meta property="og:type" content="website">
    <link rel="stylesheet" href="/assets/css/style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Style+Script&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/lipis/flag-icons@7.0.0/css/flag-icons.min.css" />
    {white_header_style}
    <style>
        .blog-hero {{
            background: linear-gradient(135deg, rgba(15, 23, 42, 0.88), rgba(30, 41, 59, 0.82)), url('/assets/images/blog-toubkal.jpg') center/cover no-repeat;
            padding: 90px 0 60px 0;
            color: #ffffff;
            text-align: center;
            position: relative;
        }}
        .blog-hero h1 {{
            font-family: var(--font-heading);
            font-size: 3rem;
            font-weight: 700;
            margin-bottom: 16px;
            color: #ffffff;
        }}
        .blog-hero p {{
            font-size: 1.12rem;
            color: #CBD5E1;
            max-width: 680px;
            margin: 0 auto 20px auto;
            line-height: 1.6;
        }}
        .blog-badge {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: rgba(217, 93, 57, 0.25);
            color: var(--primary);
            border: 1px solid rgba(217, 93, 57, 0.4);
            padding: 6px 16px;
            border-radius: 50px;
            font-size: 0.85rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            margin-bottom: 15px;
        }}
        .blog-section {{
            padding: 70px 0;
            background: #F8FAFC;
        }}
        .blog-grid-3 {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 32px;
        }}
        .blog-card {{
            background: #ffffff;
            border-radius: 16px;
            overflow: hidden;
            border: 1px solid #E2E8F0;
            box-shadow: 0 6px 20px rgba(0,0,0,0.03);
            display: flex;
            flex-direction: column;
            transition: all 0.3s ease;
        }}
        .blog-card:hover {{
            transform: translateY(-7px);
            box-shadow: 0 16px 38px rgba(0,0,0,0.08);
            border-color: var(--primary);
        }}
        .blog-card-img {{
            height: 230px;
            overflow: hidden;
            position: relative;
        }}
        .blog-card-img img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.5s ease;
        }}
        .blog-card:hover .blog-card-img img {{
            transform: scale(1.06);
        }}
        .blog-card-tag {{
            position: absolute;
            top: 14px;
            left: 14px;
            background: var(--secondary);
            color: #ffffff;
            padding: 4px 14px;
            border-radius: 50px;
            font-size: 0.75rem;
            font-weight: 700;
            letter-spacing: 0.5px;
        }}
        .blog-card-body {{
            padding: 26px 24px;
            display: flex;
            flex-direction: column;
            flex-grow: 1;
        }}
        .blog-meta {{
            display: flex;
            align-items: center;
            gap: 14px;
            font-size: 0.82rem;
            color: #64748B;
            margin-bottom: 12px;
        }}
        .blog-meta span {{
            display: flex;
            align-items: center;
            gap: 5px;
        }}
        .blog-meta i {{
            color: var(--primary);
        }}
        .blog-card-title {{
            font-family: var(--font-heading);
            font-size: 1.25rem;
            font-weight: 700;
            color: var(--secondary);
            line-height: 1.38;
            margin-bottom: 12px;
        }}
        .blog-excerpt {{
            color: #475569;
            font-size: 0.92rem;
            line-height: 1.65;
            margin-bottom: 20px;
            flex-grow: 1;
        }}
        .blog-read-btn {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            color: var(--primary);
            font-weight: 700;
            font-size: 0.92rem;
            text-decoration: none;
            transition: gap 0.2s ease;
            margin-top: auto;
        }}
        .blog-read-btn:hover {{
            gap: 12px;
            color: var(--primary-dark);
        }}
        @media (max-width: 992px) {{
            .blog-grid-3 {{ grid-template-columns: repeat(2, 1fr); }}
        }}
        @media (max-width: 640px) {{
            .blog-grid-3 {{ grid-template-columns: 1fr; }}
            .blog-hero h1 {{ font-size: 2.1rem; }}
        }}
    </style>
</head>
<body>
    <!-- Header -->
    <header id="header" class="header">
        <div class="top-bar">
            <div class="container top-bar-container">
                <div class="top-bar-left">
                    <a href="https://wa.me/212653274190" target="_blank"><i class="fab fa-whatsapp"></i> +212 653 274 190</a>
                    <a href="mailto:info@berber-magic-tours.com"><i class="far fa-envelope"></i> info@berber-magic-tours.com</a>
                </div>
                <div class="top-bar-right">
                    <span><i class="fas fa-map-marker-alt"></i> Douar Imlil, Marrakech</span>
                    <div class="top-bar-socials">
                        <a href="YOUR_LINK_HERE" target="_blank"><i class="fab fa-facebook-f"></i></a>
                        <a href="YOUR_LINK_HERE" target="_blank"><i class="fab fa-instagram"></i></a>
                        <a href="YOUR_LINK_HERE" target="_blank"><i class="fab fa-tripadvisor"></i></a>
                    </div>
                </div>
            </div>
        </div>

        <div class="container header-container">
            <div class="logo">
                <a href="/"><img src="/assets/images/logo.png" alt="Berber Magic Tours"></a>
            </div>
            
            <nav class="nav">
                <ul class="nav-list">
                    <li><a href="/">Home</a></li>
                    <li><a href="/marrakech-day-trips">Marrakech Day Trips</a></li>
                    
                    <li class="dropdown">
                        <a href="/trek-and-hike">Trek &amp; Hike <i class="fas fa-chevron-down"></i></a>
                        <ul class="dropdown-menu">
                            <li><a href="/climb-mount-toubkal">Climb Mount Toubkal</a></li>
                            <li><a href="/berber-village-treks">Berber Village Treks</a></li>
                            <li><a href="/combine-toubkal-and-villages">Combine Toubkal &amp; Villages</a></li>
                            <li><a href="/biking-in-morocco">Biking in Morocco</a></li>
                        </ul>
                    </li>
                    
                    <li class="dropdown">
                        <a href="/combine-atlas-mountains-and-desert">Combine Atlas Mountains &amp; Desert <i class="fas fa-chevron-down"></i></a>
                        <ul class="dropdown-menu">
                            <li><a href="/combine-berber-villages-and-sahara">Combine Berber Villages &amp; Sahara</a></li>
                            <li><a href="/combine-toubkal-and-sahara">Combine Toubkal &amp; Sahara</a></li>
                        </ul>
                    </li>
                    
                    <li class="dropdown">
                        <a href="#">Other Tours <i class="fas fa-chevron-down"></i></a>
                        <ul class="dropdown-menu">
                            <li class="dropdown-submenu">
                                <a href="/sahara-desert-tours">Sahara Desert Tours <i class="fas fa-chevron-right"></i></a>
                                <ul class="dropdown-menu">
                                    <li><a href="/tours-from-marrakech">Tours from Marrakech</a></li>
                                    <li><a href="/tours-from-casablanca">Tours from Casablanca</a></li>
                                    <li><a href="/tours-from-fes">Tours from Fes</a></li>
                                </ul>
                            </li>
                            <li><a href="/morocco-tours">Morocco Tours</a></li>
                        </ul>
                    </li>
                </ul>
            </nav>
            
            <div class="header-actions">
                <div class="header-flags">
                    <span class="fi fi-gb"></span>
                    <span class="fi fi-fr"></span>
                    <span class="fi fi-es"></span>
                </div>
                <a href="/contact" class="btn btn-primary"><i class="fas fa-envelope"></i> Contact Us</a>
                <button class="mobile-menu-btn"><i class="fas fa-bars"></i></button>
            </div>
        </div>
    </header>

    <!-- Mobile Menu -->
    <div class="mobile-menu">
        <div class="mobile-menu-header">
            <img src="/assets/images/logo.png" alt="Berber Magic Tours" class="mobile-logo">
            <button class="mobile-menu-close"><i class="fas fa-times"></i></button>
        </div>
        <ul class="mobile-nav-list">
            <li><a href="/">Home</a></li>
            <li><a href="/about-us">About Us</a></li>
            <li><a href="/faq">FAQ</a></li>
            <li><a href="/marrakech-day-trips">Marrakech Day Trips</a></li>
            <li><a href="/trek-and-hike">Trek &amp; Hike</a></li>
            <li><a href="/sahara-desert-tours">Sahara Desert Tours</a></li>
            <li><a href="/morocco-tours">Morocco Tours</a></li>
            <li><a href="/contact">Contact Us</a></li>
        </ul>
    </div>
    <div class="mobile-overlay"></div>

    <!-- Blog Hero -->
    <section class="blog-hero">
        <div class="container">
            <span class="blog-badge"><i class="fas fa-compass"></i> Berber Magic Journal</span>
            <h1>Morocco Travel &amp; Trekking Journal</h1>
            <p>Expert local advice, trekking guides, culture tips, and desert insights for your journey across Morocco.</p>
        </div>
    </section>

    <!-- Main Blog Section (3 Columns Grid - 6 Articles total) -->
    <section class="blog-section">
        <div class="container">
            
            <div class="blog-grid-3">
                {cards_html}
            </div>

        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container footer-container">
            <div class="footer-grid">
                <!-- Col 1: About -->
                <div class="footer-col about-col">
                    <img src="/assets/images/logo.png" alt="Berber Magic Tours" class="footer-logo">
                    <p class="footer-desc">Experience the magic of Morocco through the eyes of Locals. Let us help you find a journey of a lifetime.</p>
                    <ul class="footer-contact-list">
                        <li><i class="fas fa-map-marker-alt"></i> <span>Douar Imlil Poste Asni 42152 Marrakech</span></li>
                        <li><i class="fab fa-whatsapp"></i> <span>+212 653 274 190</span></li>
                        <li><i class="fas fa-envelope"></i> <a href="mailto:info@berber-magic-tours.com">info@berber-magic-tours.com</a></li>
                    </ul>
                    <div class="social-links mt-4">
                        <a href="YOUR_LINK_HERE" target="_blank" title="Facebook"><i class="fab fa-facebook-f"></i></a>
                        <a href="YOUR_LINK_HERE" target="_blank" title="Instagram"><i class="fab fa-instagram"></i></a>
                        <a href="YOUR_LINK_HERE" target="_blank" title="LinkedIn"><i class="fab fa-linkedin-in"></i></a>
                    </div>
                </div>
                
                <!-- Col 2: Menu -->
                <div class="footer-col links-col">
                    <h3 class="footer-title">Menu</h3>
                    <ul class="footer-links">
                        <li><a href="/">Home</a></li>
                        <li><a href="/about-us">About Us</a></li>
                        <li><a href="/faq">FAQ</a></li>
                        <li><a href="/marrakech-day-trips">Marrakech Day Trips</a></li>
                        <li><a href="/trek-and-hike">Trek &amp; Hike</a></li>
                        <li><a href="/sahara-desert-tours">Sahara Desert Tours</a></li>
                        <li><a href="/morocco-tours">Morocco Tours</a></li>
                        <li><a href="/blog" class="active">Blog</a></li>
                        <li><a href="/contact">Contact Us</a></li>
                    </ul>
                </div>
                
                <!-- Col 3: Popular Morocco -->
                <div class="footer-col popular-col">
                    <h3 class="footer-title">Popular Morocco</h3>
                    <ul class="footer-links">
                        <li><a href="/#trek-hike">Exploring Berber villages &amp; valleys</a></li>
                        <li><a href="/#trek-hike">Climbing Mount Toubkal</a></li>
                        <li><a href="/#tours">Day trips from Marrakech</a></li>
                        <li><a href="/#desert-tours">Desert Tours</a></li>
                        <li><a href="/#morocco-tours">Morocco Trips</a></li>
                        <li><a href="/#combine-tours">Combine Atlas mountains &amp; Desert</a></li>
                    </ul>
                </div>
                
                <!-- Col 4: TripAdvisor -->
                <div class="footer-col tripadvisor-col">
                    <h3 class="footer-title">Recommended</h3>
                    <div class="tripadvisor-widget-dark">
                        <div class="tripadvisor-logo-wrapper">
                            <i class="fab fa-tripadvisor"></i>
                            <span>Tripadvisor</span>
                        </div>
                        <div class="tripadvisor-rating">
                            <span class="bubble"></span>
                            <span class="bubble"></span>
                            <span class="bubble"></span>
                            <span class="bubble"></span>
                            <span class="bubble"></span>
                        </div>
                        <p>Recommended by travelers</p>
                        <a href="YOUR_LINK_HERE" class="btn btn-tripadvisor" target="_blank">View Reviews</a>
                    </div>
                </div>
            </div>
            
            <div class="footer-bottom">
                <p>&copy; 2026 Berber Magic Tours. All Rights Reserved.</p>
                <div class="footer-legal-links">
                    <a href="/privacy-policy">Privacy Policy</a> | <a href="/terms-conditions">Terms &amp; Conditions</a>
                </div>
                <p class="footer-signature mt-2" style="font-size: 0.85rem; color: #94A3B8;">Designed with <i class="fas fa-heart" style="color: #D95D39;"></i> by <a href="https://mahdicreations.dev" target="_blank" rel="noopener" style="color: #ffffff; text-decoration: underline;">mahdicreations.dev</a></p>
            </div>
        </div>
    </footer>

    <script src="/assets/js/main.js?v=1.1"></script>
</body>
</html>
"""

# Write root blog.html and blog/index.html
with open(os.path.join(root_dir, "blog.html"), "w", encoding="utf-8") as f:
    f.write(blog_index_html)

with open(os.path.join(blog_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(blog_index_html)

print("Updated generate_full_blog.py with white header and removed author info successfully.")
