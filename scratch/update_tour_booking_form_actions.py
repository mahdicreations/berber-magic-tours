import os
import re

base_dir = r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours"
tours_dir = os.path.join(base_dir, "tours")

print("=== UPDATING TOUR BOOKING FORM ACTIONS AND HIDDEN FIELDS ===")
updated_count = 0

for filename in sorted(os.listdir(tours_dir)):
    if not filename.endswith(".html"):
        continue

    filepath = os.path.join(tours_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Match <form ... class="tour-booking-form" ...>
    if 'class="tour-booking-form"' in content:
        # Replace form tag with action and method
        content = re.sub(
            r'<form\s+class="tour-booking-form"\s+id="tourBookingForm"[^>]*>',
            '<form class="tour-booking-form" id="tourBookingForm" action="../send-mail.php" method="POST">\n                                <input type="hidden" name="form_type" value="Tour Booking Request">',
            content
        )
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        updated_count += 1
        print(f"Updated booking form action in [{filename}]")

print(f"\nDone! Updated booking form actions across {updated_count} tour pages.")
