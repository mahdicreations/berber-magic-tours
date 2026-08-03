import os
import re

base_dir = r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours"
tours_dir = os.path.join(base_dir, "tours")

print("=== SETTING DEDICATED TOUR FORM ACTION TO send-mail.php ===")
updated = 0

for filename in sorted(os.listdir(tours_dir)):
    if not filename.endswith(".html"):
        continue

    filepath = os.path.join(tours_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Update form action from ../send-mail.php to send-mail.php
    if 'action="../send-mail.php"' in content:
        content = content.replace('action="../send-mail.php"', 'action="send-mail.php"')
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        updated += 1
        print(f"Updated action in [{filename}] -> action=\"send-mail.php\"")

print(f"\nDone! Updated direct form action across {updated} tour pages.")
