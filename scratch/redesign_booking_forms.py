import os
import re

base_dir = r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours\tours"

# The new compact, organized booking form HTML template
NEW_FORM_HTML = '''                            <form class="tour-booking-form" id="tourBookingForm" action="../send-mail.php" method="POST">
                                <input type="hidden" name="form_type" value="Tour Booking Request">
                                <input type="hidden" name="tour_name" value="{tour_name}">

                                <!-- Row 1: Name + WhatsApp -->
                                <div class="bk-row">
                                    <div class="bk-field">
                                        <label for="book-name"><i class="fas fa-user"></i> Name</label>
                                        <input type="text" id="book-name" class="form-control" name="name" placeholder="Your name" required>
                                    </div>
                                    <div class="bk-field">
                                        <label for="book-phone"><i class="fab fa-whatsapp"></i> WhatsApp</label>
                                        <input type="tel" id="book-phone" class="form-control" name="phone" placeholder="+1 234 567 890" required>
                                    </div>
                                </div>

                                <!-- Row 2: Email (full width) -->
                                <div class="bk-row">
                                    <div class="bk-field bk-full">
                                        <label for="book-email"><i class="far fa-envelope"></i> Email Address</label>
                                        <input type="email" id="book-email" class="form-control" name="email" placeholder="you@example.com" required>
                                    </div>
                                </div>

                                <!-- Row 3: Date + Travelers -->
                                <div class="bk-row">
                                    <div class="bk-field">
                                        <label for="book-date"><i class="far fa-calendar-alt"></i> Travel Date</label>
                                        <input type="date" id="book-date" class="form-control" name="date" required>
                                    </div>
                                    <div class="bk-field">
                                        <label for="book-travelers"><i class="fas fa-users"></i> Travelers</label>
                                        <input type="number" id="book-travelers" class="form-control" name="travelers" min="1" value="2" required>
                                    </div>
                                </div>

                                <!-- Travel Style -->
                                <div class="bk-style-group">
                                    <label class="bk-style-label"><i class="fas fa-star"></i> Travel Style</label>
                                    <input type="hidden" name="travel_style" id="book-travel-style" value="Standard">
                                    <div class="bk-style-options">
                                        <div class="bk-style-card active" onclick="selectTravelStyle(this, 'Standard')">
                                            <i class="fas fa-wallet"></i>
                                            <span>Standard</span>
                                        </div>
                                        <div class="bk-style-card" onclick="selectTravelStyle(this, 'Comfort')">
                                            <i class="fas fa-hotel"></i>
                                            <span>Comfort</span>
                                        </div>
                                        <div class="bk-style-card" onclick="selectTravelStyle(this, 'Luxury')">
                                            <i class="fas fa-crown"></i>
                                            <span>Luxury</span>
                                        </div>
                                    </div>
                                </div>

                                <!-- Message (optional, compact) -->
                                <div class="bk-row">
                                    <div class="bk-field bk-full">
                                        <label for="book-message"><i class="fas fa-comment-alt"></i> Special Requests <span class="bk-optional">(optional)</span></label>
                                        <textarea id="book-message" class="form-control" name="message" rows="2" placeholder="Dietary requirements, special needs..."></textarea>
                                    </div>
                                </div>

                                <button type="submit" class="btn btn-primary btn-block w-100 submit-btn bk-submit-btn">
                                    <span>Request Booking</span> <i class="fas fa-arrow-right"></i>
                                </button>
                                <p class="form-note mt-2 text-center"><small><i class="fas fa-shield-alt"></i> No payment required now. Secure booking.</small></p>
                            </form>'''

# Regex to match the complete form block (from <form ... id="tourBookingForm" to </form>)
FORM_PATTERN = re.compile(
    r'<form\s+class="tour-booking-form"\s+id="tourBookingForm".*?</form>',
    re.DOTALL
)

# Regex to extract tour_name from hidden input
TOUR_NAME_PATTERN = re.compile(r'name="tour_name"\s+value="([^"]+)"')

files_updated = 0
files_skipped = 0

for filename in sorted(os.listdir(base_dir)):
    if not filename.endswith('.html'):
        continue

    filepath = os.path.join(base_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find existing form block
    form_match = FORM_PATTERN.search(content)
    if not form_match:
        print(f"  SKIP (no form found): {filename}")
        files_skipped += 1
        continue

    existing_form = form_match.group(0)

    # Extract tour_name from the existing form
    name_match = TOUR_NAME_PATTERN.search(existing_form)
    tour_name = name_match.group(1) if name_match else "Tour"

    # Build new form with correct tour_name
    new_form = NEW_FORM_HTML.replace("{tour_name}", tour_name)

    # Replace old form with new compact form
    new_content = content[:form_match.start()] + new_form + content[form_match.end():]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"  UPDATED [{tour_name}]: {filename}")
    files_updated += 1

print(f"\nDone! Updated: {files_updated} | Skipped: {files_skipped}")
