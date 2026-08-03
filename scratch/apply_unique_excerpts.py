import os
import re

base_dir = r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours"
root_files = [f for f in os.listdir(base_dir) if f.endswith(".html")]

excerpts_map = {
    "2-days-mount-toubkal.html": "Ascend North Africa's highest peak (4,167m) over 2 days with experienced mountain guides, traditional Berber meals, and spectacular High Atlas mountain views.",
    "2days-atlas-mountains-valleys.html": "Discover the breathtaking scenery of High Atlas valleys, rustic clay villages, and terraced fields on an authentic 2-day guided mountain trek.",
    "2days-azzaden-valley.html": "Hike through the colorful red clay villages of Azzaden Valley, majestic juniper forests, and mountain streams with local Berber hospitality.",
    "3-day-desert-tour-casablanca-marrakech.html": "Journey from Casablanca to Marrakech via the High Atlas Mountains, Ait Benhaddou kasbah, Dades Gorges, and an unforgettable night in a Sahara desert camp.",
    "3-day-hiking-atlas-mountains.html": "Explore the diverse landscapes of Azzaden, Dknt, and Imlil valleys on a scenic 3-day trek through traditional Berber mountain hamlets.",
    "3-days-atlas-mountains-trek-camel-ride.html": "Combine high mountain trekking through Berber villages with a scenic camel ride and sunset views over the High Atlas foothills.",
    "3-days-mount-toubkal.html": "Enjoy an extended 3-day ascent of Mount Toubkal (4,167m) allowing better altitude acclimatization, panoramic ridge views, and comfortable refuge stays.",
    "3days-fes-to-marrakech-desert-tour.html": "Cross the Middle Atlas cedar forests, Ziz Valley, and Merzouga dunes on a spectacular 3-day desert journey from Fes to Marrakech.",
    "3days-in-three-valleys.html": "Immerse yourself in three distinct Atlas valleys — Imlil, Azzaden, and Matat — trekking through walnut orchards and ancient mountain passes.",
    "3days-merzouga-desert.html": "Experience the magic of Merzouga dunes with sunset camel treks, authentic Berber music around campfire, and stargazing in the Erg Chebbi desert.",
    "3days-to-setti-fattma.html": "Follow scenic waterfall trails and green riverbank paths through Ourika Valley up to Setti Fattma's famous cascading mountain streams.",
    "4-day-desert-tour-from-fes-to-marrakech.html": "Travel from imperial Fes through Ziz Valley, Merzouga dunes, Todra Gorges, and Ait Benhaddou to Marrakech on a scenic 4-day desert itinerary.",
    "4-days-biking-in-morocco.html": "Cycle through historic mountain passes, rugged dirt trails, and panoramic Berber valley tracks on an exhilarating 4-day mountain biking adventure.",
    "4-days-sahara-desert-marrakech-to-fes.html": "Connect Marrakech and Fes via High Atlas passes, Ouarzazate, Todra Gorge, Merzouga dunes, and the scenic cedar forests of Ifrane.",
    "4-days-toubkal-peaks.html": "Challenge yourself across multiple High Atlas summits including Toubkal, Ouanoukrim, and Aguelzim peak with expert mountain guides.",
    "4days-berber-villages-toubkal.html": "Combine authentic cultural stays in remote High Atlas Berber villages with the summit climb of Mount Toubkal over 4 rewarding days.",
    "4days-in-four-valleys.html": "Trek through four legendary Atlas valleys — Imlil, Azzaden, Dknt, and Imnane — offering unparalleled views of authentic mountain life.",
    "4days-sahara-desert.html": "Unwind on a relaxed 4-day desert excursion to Merzouga with camel trekking, ancient kasbah visits, and tranquil desert nights under the stars.",
    "5-day-desert-tour-from-fes-to-marrakech.html": "An enriched 5-day desert journey connecting Fes, Middle Atlas forests, Merzouga dunes, Dades Valley, and Marrakech at an easy, enjoyable pace.",
    "5-days-atlas-mountain-trek.html": "Traverse deep High Atlas valleys, high altitude mountain passes, remote Berber settlements, and dramatic mountain ridges over 5 scenic days.",
    "5-days-desert-tour-from-casablanca.html": "Discover Rabat, Fes, Merzouga desert camp, Todra Gorge, Ait Benhaddou, and Marrakech on an all-inclusive 5-day Grand Morocco tour from Casablanca.",
    "5-days-imperial-cities.html": "Explore Morocco's rich history, architectural marvels, vibrant medinas, and UNESCO heritage sites across Casablanca, Rabat, Meknes, Fes, and Marrakech.",
    "5-days-morocco-biking.html": "Tackle thrilling downhill singletracks and scenic mountain dirt roads across the High Atlas valleys on a premier 5-day cycling tour.",
    "5days-berber-villages-toubkal.html": "Combine a multi-valley Berber village trek with the summit of Mount Toubkal, experiencing local homecooked meals and warm mountain hospitality.",
    "5days-berber-villagessahara.html": "Experience the best of Morocco in 5 days — combining High Atlas mountain trekking in Berber villages with a camel safari in Merzouga dunes.",
    "5days-toubkal-sahara.html": "Summit Mount Toubkal (4,167m) and travel directly to the golden dunes of Merzouga on an action-packed 5-day mountain and desert adventure.",
    "6-days-berber-villages-toubkal.html": "A comprehensive 6-day High Atlas expedition featuring deep valley exploration, traditional village guesthouses, and the Toubkal summit trek.",
    "6-days-desert-tour-from-casablanca.html": "An extensive 6-day Morocco road trip from Casablanca covering Fes medina, Sahara desert glamping, Dades Valley, Ait Benhaddou, and Marrakech.",
    "6-days-desert-tour-from-fes-to-marrakech.html": "Immerse yourself in desert culture with 6 unhurried days exploring Fes, Ziz Oasis, Merzouga luxury camp, Dades Valley, and High Atlas passes.",
    "6days-berber-villagessahara-opt-2.html": "Enjoy a balanced 6-day itinerary blending relaxed Berber village hiking in the Atlas with camel riding and luxury camping in Merzouga dunes.",
    "6days-berber-villagessahara.html": "Hike through remote mountain valleys, stay in traditional Berber guesthouses, and ride camels into the Sahara desert over 6 unforgettable days.",
    "6days-imperial-cities-desert.html": "The ultimate 6-day Morocco highlight tour: imperial medinas, ancient monuments, High Atlas mountains, and Sahara desert luxury camping.",
    "6days-toubkal-sahara-opt-2.html": "Summit North Africa's highest peak and unwind with an immersive Sahara desert safari, luxury camp stays, and Berber cultural encounters.",
    "6days-toubkal-sahara.html": "An epic 6-day expedition summiting Mount Toubkal and venturing deep into the Merzouga desert dunes for camel treks and stargazing.",
    "7-days-around-morocco.html": "Experience the full diversity of Morocco — imperial cities, High Atlas mountains, Sahara dunes, and coastal charm on a comprehensive 7-day tour.",
    "7days-berber-villagessahara.html": "A 7-day grand adventure combining deep Atlas mountain trekking through Berber villages with a Sahara desert safari and kasbah tours.",
    "best-of-morocco-holidays.html": "The ultimate 10-day Grand Morocco holiday covering imperial cities, High Atlas mountain treks, Sahara desert camps, and coastal Essaouira.",
    "cooking-class-in-high-atlas.html": "Learn secret Berber culinary traditions, shop for fresh ingredients, and prepare authentic Moroccan tajine and mint tea with a local family.",
    "day-trip-to-ourika-valley.html": "Escape Marrakech for a refreshing day trip to Ourika Valley, walking along mountain streams, waterfalls, and terraced Berber villages.",
    "imlil-valley-day-trip.html": "Discover the scenic gateway to Mount Toubkal with a guided day trek through walnut groves, waterfalls, and traditional Imlil hamlets.",
    "mount-toubkal-3days-trek-acclimatization.html": "Achieve maximum summit success on Mount Toubkal with an acclimatization day hike through Azzaden Valley before ascending the peak.",
    "mountain-bike-day-trip.html": "Experience an exhilarating day of mountain biking along scenic dirt paths and valley tracks in the High Atlas mountains with guide support.",
    "overnight-in-atlas-mountains.html": "Escape to a peaceful mountain guesthouse in Imlil Valley, enjoying guided walks, Berber hospitality, and scenic terrace dining.",
    "toubkal-summit-via-lake-ifni-6-days.html": "A magnificent 6-day trek following wild mountain trails, turquoise Lake Ifni, high passes, and the summit of Mount Toubkal.",
    "toubkal-winter-climb.html": "Experience the thrilling winter ascent of Mount Toubkal equipped with crampons and ice axes under the guidance of certified winter experts."
}

print("=== APPLYING UNIQUE TOUR EXCERPTS TO ALL CARD BLOCKS ===")
total_updated = 0

for file_name in sorted(root_files):
    file_path = os.path.join(base_dir, file_name)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    modified = False

    # Match each card block
    for tour_file, excerpt in excerpts_map.items():
        # Search for cards linking to this tour_file
        # Look for <p class="...">...</p> inside cards containing href="tours/tour_file"
        
        # Regex to find card block for tour_file and replace its <p> text
        # Match from card start down to card footer
        pattern = r'(href=["\']tours/' + re.escape(tour_file) + r'["\'][\s\S]*?<p[^>]*class=["\'][^"\'\n]*tour-card-text[^"\'\n]*["\'][^>]*>)([\s\S]*?)(</p>)'
        
        if re.search(pattern, content):
            content, count = re.subn(pattern, r'\g<1>' + excerpt + r'\g<3>', content)
            if count > 0:
                modified = True

        # Reverse pattern (if <p> appears before <a> href)
        pattern_rev = r'(<p[^>]*class=["\'][^"\'\n]*tour-card-text[^"\'\n]*["\'][^>]*>)([\s\S]*?)(</p>[\s\S]*?href=["\']tours/' + re.escape(tour_file) + r'["\'])'
        if re.search(pattern_rev, content):
            content, count = re.subn(pattern_rev, r'\g<1>' + excerpt + r'\g<3>', content)
            if count > 0:
                modified = True

    if modified:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated card excerpts in [{file_name}]")
        total_updated += 1

print(f"\nDone! Updated card excerpts across {total_updated} page(s).")
