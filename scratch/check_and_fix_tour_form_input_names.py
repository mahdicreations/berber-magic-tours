import os
import re

base_dir = r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours"
tours_dir = os.path.join(base_dir, "tours")

print("=== CHECKING AND FIXING ALL TOUR FORM INPUT NAMES ===")

missing_name_files = []
missing_email_files = []

for filename in sorted(os.listdir(tours_dir)):
    if not filename.endswith(".html"):
        continue

    filepath = os.path.join(tours_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the <form ... tour-booking-form ... > ... </form> block
    form_match = re.search(r'<form[^>]*class="[^"]*tour-booking-form[^"]*"[\s\S]*?</form>', content)
    if not form_match:
        print(f"[NO FORM FOUND] {filename}")
        continue

    form_html = form_match.group(0)

    # Check if name attribute exists for name and email
    has_name_attr = re.search(r'name=["\'](name|full_name|book-name|book_name)["\']', form_html, re.I)
    has_email_attr = re.search(r'name=["\'](email|user_email|book-email|book_email)["\']', form_html, re.I)

    if not has_name_attr:
        missing_name_files.append(filename)
    if not has_email_attr:
        missing_email_files.append(filename)

print(f"\nFiles missing name input name attribute: {len(missing_name_files)}")

for f in missing_name_files:
    print(" -", f)

print(f"\nFiles missing email input name attribute: {len(missing_email_files)}")
for f in missing_email_files:
    print(" -", f)
