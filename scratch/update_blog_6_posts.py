import os

blog_html_content = '''<!DOCTYPE html>
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
    <link rel="stylesheet" href="assets/css/style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Style+Script&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/lipis/flag-icons@7.0.0/css/flag-icons.min.css" />
    <style>
        /* Blog Custom CSS Styles */
        .blog-hero {
            background: linear-gradient(135deg, rgba(15, 23, 42, 0.88), rgba(30, 41, 59, 0.82)), url('assets/images/blog-toubkal.jpg') center/cover no-repeat;
            padding: 90px 0 60px 0;
            color: #ffffff;
            text-align: center;
            position: relative;
        }

        .blog-hero h1 {
            font-family: var(--font-heading);
            font-size: 3rem;
            font-weight: 700;
            margin-bottom: 16px;
            color: #ffffff;
        }

        .blog-hero p {
            font-size: 1.12rem;
            color: #CBD5E1;
            max-width: 680px;
            margin: 0 auto 20px auto;
            line-height: 1.6;
        }

        .blog-badge {
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
        }

        .blog-section {
            padding: 70px 0;
            background: #F8FAFC;
        }

        /* 3-Column Article Grid (2 rows of 3 = 6 articles) */
        .blog-grid-3 {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 32px;
        }

        .blog-card {
            background: #ffffff;
            border-radius: 16px;
            overflow: hidden;
            border: 1px solid #E2E8F0;
            box-shadow: 0 6px 20px rgba(0,0,0,0.03);
            display: flex;
            flex-direction: column;
            transition: all 0.3s ease;
        }

        .blog-card:hover {
            transform: translateY(-7px);
            box-shadow: 0 16px 38px rgba(0,0,0,0.08);
            border-color: var(--primary);
        }

        .blog-card-img {
            height: 230px;
            overflow: hidden;
            position: relative;
        }

        .blog-card-img img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.5s ease;
        }

        .blog-card:hover .blog-card-img img {
            transform: scale(1.06);
        }

        .blog-card-tag {
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
        }

        .blog-card-body {
            padding: 26px 24px;
            display: flex;
            flex-direction: column;
            flex-grow: 1;
        }

        .blog-meta {
            display: flex;
            align-items: center;
            gap: 14px;
            font-size: 0.82rem;
            color: #64748B;
            margin-bottom: 12px;
        }

        .blog-meta span {
            display: flex;
            align-items: center;
            gap: 5px;
        }

        .blog-meta i {
            color: var(--primary);
        }

        .blog-card-title {
            font-family: var(--font-heading);
            font-size: 1.25rem;
            font-weight: 700;
            color: var(--secondary);
            line-height: 1.38;
            margin-bottom: 12px;
        }

        .blog-excerpt {
            color: #475569;
            font-size: 0.92rem;
            line-height: 1.65;
            margin-bottom: 20px;
            flex-grow: 1;
        }

        .blog-read-btn {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            color: var(--primary);
            font-weight: 700;
            font-size: 0.92rem;
            cursor: pointer;
            transition: gap 0.2s ease;
            background: none;
            border: none;
            padding: 0;
            margin-top: auto;
        }

        .blog-read-btn:hover {
            gap: 12px;
            color: var(--primary-dark);
        }

        /* Modal styling for article reader */
        .blog-modal-backdrop {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(15, 23, 42, 0.78);
            backdrop-filter: blur(6px);
            z-index: 99999;
            display: none;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }

        .blog-modal-backdrop.active {
            display: flex;
        }

        .blog-modal-container {
            background: #ffffff;
            width: 100%;
            max-width: 820px;
            max-height: 90vh;
            border-radius: 20px;
            overflow-y: auto;
            position: relative;
            box-shadow: 0 25px 60px rgba(0,0,0,0.3);
            animation: modalFadeIn 0.3s ease;
        }

        @keyframes modalFadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .blog-modal-close {
            position: absolute;
            top: 18px;
            right: 22px;
            width: 38px;
            height: 38px;
            border-radius: 50%;
            background: #F1F5F9;
            color: #334155;
            border: none;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            font-size: 1.1rem;
            transition: all 0.2s ease;
            z-index: 10;
        }

        .blog-modal-close:hover {
            background: var(--primary);
            color: #ffffff;
        }

        .blog-modal-header {
            height: 320px;
            position: relative;
            overflow: hidden;
        }

        .blog-modal-header img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .blog-modal-body {
            padding: 40px 45px;
        }

        .blog-modal-body h2 {
            font-family: var(--font-heading);
            font-size: 2rem;
            color: var(--secondary);
            margin-bottom: 16px;
            line-height: 1.3;
        }

        .blog-modal-body p {
            color: #334155;
            font-size: 1.02rem;
            line-height: 1.8;
            margin-bottom: 20px;
            text-align: justify;
        }

        .blog-modal-body h3 {
            font-family: var(--font-heading);
            font-size: 1.35rem;
            color: var(--secondary);
            margin: 28px 0 12px 0;
        }

        .blog-modal-body ul {
            margin-bottom: 24px;
            padding-left: 20px;
        }

        .blog-modal-body li {
            color: #334155;
            font-size: 0.98rem;
            line-height: 1.7;
            margin-bottom: 8px;
        }

        @media (max-width: 992px) {
            .blog-grid-3 {
                grid-template-columns: repeat(2, 1fr);
            }
        }

        @media (max-width: 640px) {
            .blog-grid-3 {
                grid-template-columns: 1fr;
            }
            .blog-hero h1 {
                font-size: 2.1rem;
            }
            .blog-modal-body {
                padding: 25px 20px;
            }
            .blog-modal-header {
                height: 220px;
            }
        }
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
                <a href="/"><img src="assets/images/logo.png" alt="Berber Magic Tours"></a>
            </div>
            
            <nav class="nav">
                <ul class="nav-list">
                    <li><a href="/">Home</a></li>
                    <li><a href="marrakech-day-trips">Marrakech Day Trips</a></li>
                    
                    <li class="dropdown">
                        <a href="trek-and-hike">Trek &amp; Hike <i class="fas fa-chevron-down"></i></a>
                        <ul class="dropdown-menu">
                            <li><a href="climb-mount-toubkal">Climb Mount Toubkal</a></li>
                            <li><a href="berber-village-treks">Berber Village Treks</a></li>
                            <li><a href="combine-toubkal-and-villages">Combine Toubkal &amp; Villages</a></li>
                            <li><a href="biking-in-morocco">Biking in Morocco</a></li>
                        </ul>
                    </li>
                    
                    <li class="dropdown">
                        <a href="combine-atlas-mountains-and-desert">Combine Atlas Mountains &amp; Desert <i class="fas fa-chevron-down"></i></a>
                        <ul class="dropdown-menu">
                            <li><a href="combine-berber-villages-and-sahara">Combine Berber Villages &amp; Sahara</a></li>
                            <li><a href="combine-toubkal-and-sahara">Combine Toubkal &amp; Sahara</a></li>
                        </ul>
                    </li>
                    
                    <li class="dropdown">
                        <a href="#">Other Tours <i class="fas fa-chevron-down"></i></a>
                        <ul class="dropdown-menu">
                            <li class="dropdown-submenu">
                                <a href="sahara-desert-tours">Sahara Desert Tours <i class="fas fa-chevron-right"></i></a>
                                <ul class="dropdown-menu">
                                    <li><a href="tours-from-marrakech">Tours from Marrakech</a></li>
                                    <li><a href="tours-from-casablanca">Tours from Casablanca</a></li>
                                    <li><a href="tours-from-fes">Tours from Fes</a></li>
                                </ul>
                            </li>
                            <li><a href="morocco-tours">Morocco Tours</a></li>
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
                <a href="contact" class="btn btn-primary"><i class="fas fa-envelope"></i> Contact Us</a>
                <button class="mobile-menu-btn"><i class="fas fa-bars"></i></button>
            </div>
        </div>
    </header>

    <!-- Mobile Menu -->
    <div class="mobile-menu">
        <div class="mobile-menu-header">
            <img src="assets/images/logo.png" alt="Berber Magic Tours" class="mobile-logo">
            <button class="mobile-menu-close"><i class="fas fa-times"></i></button>
        </div>
        <ul class="mobile-nav-list">
            <li><a href="/">Home</a></li>
            <li><a href="about-us">About Us</a></li>
            <li><a href="faq">FAQ</a></li>
            <li><a href="marrakech-day-trips">Marrakech Day Trips</a></li>
            <li><a href="trek-and-hike">Trek &amp; Hike</a></li>
            <li><a href="sahara-desert-tours">Sahara Desert Tours</a></li>
            <li><a href="morocco-tours">Morocco Tours</a></li>
            <li><a href="contact">Contact Us</a></li>
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
                
                <!-- Article 1 -->
                <div class="blog-card">
                    <div class="blog-card-img">
                        <img src="assets/images/blog-toubkal.jpg" alt="Trekking Mount Toubkal">
                        <span class="blog-card-tag" style="background: var(--primary);">Trekking Guide</span>
                    </div>
                    <div class="blog-card-body">
                        <div class="blog-meta">
                            <span><i class="far fa-calendar-alt"></i> August 2026</span>
                            <span><i class="far fa-clock"></i> 7 min read</span>
                        </div>
                        <h3 class="blog-card-title">The Ultimate Guide to Trekking Mount Toubkal</h3>
                        <p class="blog-excerpt">Planning to conquer North Africa's highest peak (4,167m)? Discover essential preparation, acclimatization routes, gear, and local Berber guide insights.</p>
                        <button class="blog-read-btn" onclick="openBlogModal('article1')">
                            Read Full Article <i class="fas fa-arrow-right"></i>
                        </button>
                    </div>
                </div>

                <!-- Article 2 -->
                <div class="blog-card">
                    <div class="blog-card-img">
                        <img src="assets/images/blog-sahara.jpg" alt="Sahara Desert Experience">
                        <span class="blog-card-tag">Sahara Desert</span>
                    </div>
                    <div class="blog-card-body">
                        <div class="blog-meta">
                            <span><i class="far fa-calendar-alt"></i> July 2026</span>
                            <span><i class="far fa-clock"></i> 5 min read</span>
                        </div>
                        <h3 class="blog-card-title">Sahara Desert Guide: Erg Chebbi vs Erg Chigaga</h3>
                        <p class="blog-excerpt">Which desert dunes fit your dream tour? Compare dune heights, luxury glamping camps, camel treks, and stargazing between Merzouga and Zagora.</p>
                        <button class="blog-read-btn" onclick="openBlogModal('article2')">
                            Read Full Article <i class="fas fa-arrow-right"></i>
                        </button>
                    </div>
                </div>

                <!-- Article 3 -->
                <div class="blog-card">
                    <div class="blog-card-img">
                        <img src="assets/images/blog-valleys.jpg" alt="Atlas Valleys Berber Villages">
                        <span class="blog-card-tag">Cultural Treks</span>
                    </div>
                    <div class="blog-card-body">
                        <div class="blog-meta">
                            <span><i class="far fa-calendar-alt"></i> July 2026</span>
                            <span><i class="far fa-clock"></i> 6 min read</span>
                        </div>
                        <h3 class="blog-card-title">Exploring Hidden Atlas Valleys: Imlil &amp; Azzaden</h3>
                        <p class="blog-excerpt">Journey beyond Marrakech into tranquil High Atlas river valleys. Experience authentic Berber hospitality, walnut groves, and ancient village paths.</p>
                        <button class="blog-read-btn" onclick="openBlogModal('article3')">
                            Read Full Article <i class="fas fa-arrow-right"></i>
                        </button>
                    </div>
                </div>

                <!-- Article 4 -->
                <div class="blog-card">
                    <div class="blog-card-img">
                        <img src="assets/images/blog-morocco.jpg" alt="Morocco Cultural Travel Tips">
                        <span class="blog-card-tag">Travel Tips</span>
                    </div>
                    <div class="blog-card-body">
                        <div class="blog-meta">
                            <span><i class="far fa-calendar-alt"></i> June 2026</span>
                            <span><i class="far fa-clock"></i> 8 min read</span>
                        </div>
                        <h3 class="blog-card-title">First Time in Morocco? 10 Essential Travel Tips</h3>
                        <p class="blog-excerpt">From souk bargaining secrets and mint tea etiquette to cash usage and respectful dress codes, ensure a seamless cultural trip.</p>
                        <button class="blog-read-btn" onclick="openBlogModal('article4')">
                            Read Full Article <i class="fas fa-arrow-right"></i>
                        </button>
                    </div>
                </div>

                <!-- Article 5 (NEW) -->
                <div class="blog-card">
                    <div class="blog-card-img">
                        <img src="assets/images/blog-winter-toubkal.jpg" alt="Mount Toubkal Winter Ascent">
                        <span class="blog-card-tag" style="background: #0284C7;">Winter Treks</span>
                    </div>
                    <div class="blog-card-body">
                        <div class="blog-meta">
                            <span><i class="far fa-calendar-alt"></i> June 2026</span>
                            <span><i class="far fa-clock"></i> 6 min read</span>
                        </div>
                        <h3 class="blog-card-title">Mount Toubkal Winter Ascent: Preparation &amp; Safety</h3>
                        <p class="blog-excerpt">Climbing Mount Toubkal in snow requires specialized crampon skills, warm layering, and expert mountain guidance for an alpine adventure.</p>
                        <button class="blog-read-btn" onclick="openBlogModal('article5')">
                            Read Full Article <i class="fas fa-arrow-right"></i>
                        </button>
                    </div>
                </div>

                <!-- Article 6 (NEW) -->
                <div class="blog-card">
                    <div class="blog-card-img">
                        <img src="assets/images/blog-moroccan-food.jpg" alt="Moroccan Gastronomy & Culinary Secrets">
                        <span class="blog-card-tag" style="background: #D97706;">Gastronomy</span>
                    </div>
                    <div class="blog-card-body">
                        <div class="blog-meta">
                            <span><i class="far fa-calendar-alt"></i> May 2026</span>
                            <span><i class="far fa-clock"></i> 5 min read</span>
                        </div>
                        <h3 class="blog-card-title">Moroccan Gastronomy: From Tagine to Pastilla</h3>
                        <p class="blog-excerpt">Explore the rich flavors of Moroccan cuisine: aromatic spices, slow-cooked Berber tagines, couscous traditions, and sweet pastillas.</p>
                        <button class="blog-read-btn" onclick="openBlogModal('article6')">
                            Read Full Article <i class="fas fa-arrow-right"></i>
                        </button>
                    </div>
                </div>

            </div>

        </div>
    </section>

    <!-- Modal Article Reader -->
    <div class="blog-modal-backdrop" id="blogModal" onclick="closeBlogModalOnBackdrop(event)">
        <div class="blog-modal-container">
            <button class="blog-modal-close" onclick="closeBlogModal()"><i class="fas fa-times"></i></button>
            <div class="blog-modal-header">
                <img id="modalImg" src="" alt="Article Banner">
            </div>
            <div class="blog-modal-body" id="modalContent">
                <!-- Content injected dynamically via JS -->
            </div>
        </div>
    </div>

    <!-- Footer -->
    <footer class="footer">
        <div class="container footer-container">
            <div class="footer-grid">
                <!-- Col 1: About -->
                <div class="footer-col about-col">
                    <img src="assets/images/logo.png" alt="Berber Magic Tours" class="footer-logo">
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
                        <li><a href="about-us">About Us</a></li>
                        <li><a href="faq">FAQ</a></li>
                        <li><a href="marrakech-day-trips">Marrakech Day Trips</a></li>
                        <li><a href="trek-and-hike">Trek &amp; Hike</a></li>
                        <li><a href="sahara-desert-tours">Sahara Desert Tours</a></li>
                        <li><a href="morocco-tours">Morocco Tours</a></li>
                        <li><a href="blog" class="active">Blog</a></li>
                        <li><a href="contact">Contact Us</a></li>
                    </ul>
                </div>
                
                <!-- Col 3: Popular Morocco -->
                <div class="footer-col popular-col">
                    <h3 class="footer-title">Popular Morocco</h3>
                    <ul class="footer-links">
                        <li><a href="#trek-hike">Exploring Berber villages &amp; valleys</a></li>
                        <li><a href="#trek-hike">Climbing Mount Toubkal</a></li>
                        <li><a href="#tours">Day trips from Marrakech</a></li>
                        <li><a href="#desert-tours">Desert Tours</a></li>
                        <li><a href="#morocco-tours">Morocco Trips</a></li>
                        <li><a href="#combine-tours">Combine Atlas mountains &amp; Desert</a></li>
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
                    <a href="privacy-policy">Privacy Policy</a> | <a href="terms-conditions">Terms &amp; Conditions</a>
                </div>
            </div>
        </div>
    </footer>

    <script src="assets/js/main.js?v=1.1"></script>
    <script>
        // Full Article Content Data for 6 Articles
        const articlesData = {
            article1: {
                title: "The Ultimate Guide to Trekking Mount Toubkal",
                img: "assets/images/blog-toubkal.jpg",
                meta: "August 2026 • 7 min read • By Hassan (Senior Berber Guide)",
                html: `
                    <h2>The Ultimate Guide to Trekking Mount Toubkal</h2>
                    <p>Standing at 4,167 meters (13,671 ft), Mount Toubkal is the highest peak in North Africa and the Arabian World. Located just 60km south of Marrakech in the High Atlas Mountains, it offers one of the most accessible and thrilling alpine trekking experiences in Africa.</p>
                    
                    <h3>1. Choosing the Right Trek Duration</h3>
                    <p>While experienced hikers can summit in 2 days, we strongly recommend a 3-day or 4-day itinerary. Taking extra time allows proper altitude acclimatization, reducing the risk of altitude sickness while enabling you to explore surrounding valleys like Azzaden or Lake Ifni.</p>

                    <h3>2. Best Time to Hike Mount Toubkal</h3>
                    <p>Toubkal can be climbed year-round, but conditions vary significantly:</p>
                    <ul>
                        <li><strong>Spring (April - June):</strong> Ideal weather, blossoming valleys, wild flowers, and lingering snow patches on upper slopes.</li>
                        <li><strong>Autumn (September - November):</strong> Crisp air, pleasant daytime temperatures, and clear blue skies.</li>
                        <li><strong>Winter (December - March):</strong> Requires winter mountaineering gear (crampons, ice axes). Suitable for experienced trekkers or guided winter climbs.</li>
                    </ul>

                    <h3>3. Essential Packing List</h3>
                    <p>Proper footwear is crucial. Sturdy, broken-in ankle-support hiking boots are mandatory. Layered clothing is essential because temperatures at the refuge (3,207m) and summit drop significantly before dawn. Always pack a windproof/waterproof jacket, warm hat, gloves, sun cream, and hydration bladder.</p>

                    <h3>4. Why Hire a Certified Local Berber Guide?</h3>
                    <p>Since 2019, regulations require all trekkers to be accompanied by a licensed mountain guide. Our local Berber guides are born and raised in Imlil valley. They bring invaluable safety expertise, handle refuge bookings, coordinate luggage transport with muleteers, and enrich your journey with authentic Berber stories.</p>
                `
            },
            article2: {
                title: "Sahara Desert Guide: Erg Chebbi vs Erg Chigaga",
                img: "assets/images/blog-sahara.jpg",
                meta: "July 2026 • 5 min read • By Berber Magic Tours Team",
                html: `
                    <h2>Sahara Desert Guide: Erg Chebbi vs Erg Chigaga</h2>
                    <p>No trip to Morocco is complete without experiencing the majestic Sahara Desert. Endless golden dunes, starry night skies, traditional Gnawa music around campfire, and camel treks at sunset create lifelong memories. But which desert region should you choose?</p>

                    <h3>Erg Chebbi (Merzouga) – The Iconic Golden Dunes</h3>
                    <p>Erg Chebbi is famous for its towering sand dunes reaching up to 150 meters in height. The sand has a rich reddish-gold color that changes shades throughout the day.</p>
                    <ul>
                        <li><strong>Pros:</strong> Easy road access right up to the dune edge, wide selection of luxury desert camps with private en-suite bathrooms and hot showers, ideal for 3-day tours from Marrakech or Fes.</li>
                        <li><strong>Activities:</strong> Sunset camel trekking, quad biking, sandboarding, luxury glamping.</li>
                    </ul>

                    <h3>Erg Chigaga (Zagora Region) – Wild & Off-the-Beaten-Path</h3>
                    <p>Erg Chigaga is larger and more remote, stretching across 40km of wild desert landscapes reachable only via 4x4 off-road driving.</p>
                    <ul>
                        <li><strong>Pros:</strong> Deep wilderness feel, fewer tourists, pure silence and untouched dune expanses.</li>
                        <li><strong>Best For:</strong> Adventurers seeking an authentic off-road expedition experience over 4+ days.</li>
                    </ul>

                    <h3>Our Recommendation</h3>
                    <p>If you want high dramatic dunes combined with comfort and luxury camp amenities, <strong>Erg Chebbi in Merzouga</strong> is the premier choice for most travelers.</p>
                `
            },
            article3: {
                title: "Exploring Hidden Atlas Valleys: Imlil & Azzaden",
                img: "assets/images/blog-valleys.jpg",
                meta: "July 2026 • 6 min read • By Berber Magic Tours Team",
                html: `
                    <h2>Exploring Hidden Atlas Valleys: Imlil & Azzaden</h2>
                    <p>While Marrakech captivates travelers with its bustling medina and vibrant souks, just an hour's drive south lies an entirely different realm—the serene High Atlas Mountains, home to ancient Berber villages nestled in lush river valleys.</p>

                    <h3>Imlil Valley – The Gateway to Toubkal</h3>
                    <p>Situated at 1,740m altitude, Imlil is surrounded by walnut trees, apple orchards, and terraced agricultural fields. It serves as the primary base camp for High Atlas trekking. Walking through villages like Aroumd and Targa Imoula offers a glimpse into traditional mountain lifestyle.</p>

                    <h3>Ourika Valley – Refreshing Waterfalls & River Dining</h3>
                    <p>Located closer to Marrakech, Ourika Valley is famous for its cool mountain river and the 7 Setti Fatma waterfalls. It's a favorite day trip spot for cooling off in summer and dining right by the water on traditional carpeted seating.</p>

                    <h3>Azzaden Valley – The Secret Red Clay Valley</h3>
                    <p>Azzaden Valley is widely considered the most beautiful valley in the High Atlas. Lined with red clay Berber houses, terraced fields, and juniper forests, it remains unspoiled by mass tourism. Our 3-day and 4-day valley treks lead you through Tizi n'Test and Tizi Mzik pass into Azzaden for an unforgettable remote experience.</p>
                `
            },
            article4: {
                title: "First Time in Morocco? 10 Essential Travel Tips",
                img: "assets/images/blog-morocco.jpg",
                meta: "June 2026 • 8 min read • By Berber Magic Tours Team",
                html: `
                    <h2>First Time in Morocco? 10 Essential Travel Tips</h2>
                    <p>Morocco is a sensory paradise where ancient traditions meet warm hospitalities. To ensure your first visit is smooth, respectful, and joyful, here are 10 practical travel tips from our local team:</p>

                    <h3>1. Moroccan Mint Tea (The National Drink)</h3>
                    <p>Mint tea—affectionately called "Berber Whiskey"—is a symbol of hospitality. It is served hot and sweet. Accepting a glass when offered by locals or shopkeepers is a sign of friendship and respect.</p>

                    <h3>2. Currency & Cash Usage</h3>
                    <p>The official currency is the Moroccan Dirham (MAD). While major hotels and restaurants accept cards, cash is king in souks, rural villages, mountain guesthouses, and taxis. Always carry small Dirham bills.</p>

                    <h3>3. Respectful Dress Code</h3>
                    <p>Morocco is a welcoming but conservative country. In cities and mountain villages, dressing modestly (covering shoulders and knees) is appreciated and earns great respect from local communities.</p>

                    <h3>4. Haggling in the Souks</h3>
                    <p>Bargaining is an art form and social interaction in Moroccan markets. Always stay friendly, smile, and start with a lighthearted offer around 40-50% of the initial price until you reach a comfortable agreement.</p>

                    <h3>5. Tipping Etiquette (Baksheesh)</h3>
                    <p>Tipping is customary in Morocco. In restaurants, 10% is appreciated. For private drivers and mountain guides who take care of you throughout your tour, tipping reflects your satisfaction with their personal service.</p>
                `
            },
            article5: {
                title: "Mount Toubkal Winter Ascent: Preparation & Safety",
                img: "assets/images/blog-winter-toubkal.jpg",
                meta: "June 2026 • 6 min read • By Brahim (Alpine Berber Guide)",
                html: `
                    <h2>Mount Toubkal Winter Ascent: Preparation & Safety</h2>
                    <p>From December through April, the High Atlas Mountains transform into a winter paradise. Climbing Mount Toubkal in snow conditions is an exhilarating mountaineering experience that requires technical preparation, proper winter gear, and local guide leadership.</p>

                    <h3>1. Winter Weather Conditions</h3>
                    <p>Snow covers the peaks above 2,500m, and temperatures at the Toubkal Refuge (3,207m) frequently drop below freezing (-5°C to -15°C at dawn). Clear blue skies are common, but mountain weather can change rapidly.</p>

                    <h3>2. Technical Gear Required</h3>
                    <p>Unlike summer treks, a winter summit attempt requires specific equipment:</p>
                    <ul>
                        <li><strong>Crampons & Ice Axe:</strong> Essential for ascending the icy snow chutes (South Ikhibi route). Our team provides technical gear and fitting in Imlil before departure.</li>
                        <li><strong>Mountaineering Boots:</strong> Sturdy, stiff-soled boots compatible with crampons.</li>
                        <li><strong>Thermal Layers & Windproof Shell:</strong> Heavy down jacket, thermal base layers, waterproof gloves, and balaclava.</li>
                    </ul>

                    <h3>3. Guided Safety & Acclimatization</h3>
                    <p>Winter conditions demand expert route selection and avalanche safety awareness. Our certified Berber mountain guides inspect trail safety daily to ensure every client reaches the 4,167m summit safely.</p>
                `
            },
            article6: {
                title: "Moroccan Gastronomy: From Tagine to Pastilla",
                img: "assets/images/blog-moroccan-food.jpg",
                meta: "May 2026 • 5 min read • By Berber Magic Tours Culinary Team",
                html: `
                    <h2>Moroccan Gastronomy: From Tagine to Pastilla</h2>
                    <p>Moroccan cuisine is celebrated worldwide for its rich fusion of Berber, Arab, Andalusian, and Mediterranean flavors. Slow cooking in conical clay tagines infuses aromatic spices like cumin, saffron, cinnamon, and ginger into succulent tender meats and fresh vegetables.</p>

                    <h3>1. Traditional Berber Tagine</h3>
                    <p>The iconic tagine is named after the terracotta dish in which it cooks slowly over charcoal embers. Favorite local varieties include Lamb Tagine with Prunes & Almonds, Chicken Tagine with Preserved Lemons & Olives, and Mountain Vegetable Berber Tagines cooked freshly on mountain treks.</p>

                    <h3>2. Royal Moroccan Pastilla</h3>
                    <p>A masterpiece of sweet and savory flavors, Pastilla consists of paper-thin warka pastry stuffed with shredded spiced poultry or seafood, layered with crushed roasted almonds, and dusted with powdered sugar and cinnamon.</p>

                    <h3>3. Traditional Couscous Fridays</h3>
                    <p>In Moroccan homes and villages, Friday is dedicated to gathering after prayer for a massive platter of steamed semolina couscous topped with seven tender vegetables and rich savory broth.</p>

                    <h3>Cooking Classes in the High Atlas</h3>
                    <p>Join our Berber Cooking Class in Imlil to visit local spice markets, learn authentic family recipes, and cook your own traditional meal with a local Berber family!</p>
                `
            }
        };

        function openBlogModal(articleKey) {
            const data = articlesData[articleKey];
            if (!data) return;
            document.getElementById('modalImg').src = data.img;
            document.getElementById('modalContent').innerHTML = `
                <span style="color: var(--primary); font-size: 0.85rem; font-weight: 700;">${data.meta}</span>
                <div style="margin-top: 15px;">${data.html}</div>
            `;
            document.getElementById('blogModal').classList.add('active');
            document.body.style.overflow = 'hidden';
        }

        function closeBlogModal() {
            document.getElementById('blogModal').classList.remove('active');
            document.body.style.overflow = '';
        }

        function closeBlogModalOnBackdrop(e) {
            if (e.target.id === 'blogModal') {
                closeBlogModal();
            }
        }
    </script>
</body>
</html>
'''

with open(r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours\blog.html", "w", encoding="utf-8") as f:
    f.write(blog_html_content)

print("Updated blog.html with 6 posts in 3-column grid successfully.")
