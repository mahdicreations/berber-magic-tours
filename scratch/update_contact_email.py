import os

base_dir = r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours"

old_email = "contact@berber-magic-tours.com"
new_email = "info@berber-magic-tours.com"

updated_files = 0
total_replacements = 0

for root, dirs, files in os.walk(base_dir):
    # Skip .git or scratch folders
    if ".git" in root or "scratch" in root:
        continue

    for filename in files:
        if filename.endswith(".html") or filename.endswith(".js") or filename.endswith(".css") or filename.endswith(".php") or filename.endswith(".md"):
            filepath = os.path.join(root, filename)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()

                if old_email in content:
                    count = content.count(old_email)
                    content = content.replace(old_email, new_email)
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(content)
                    updated_files += 1
                    total_replacements += count
                    print(f"Replaced {count} occurrence(s) in [{os.path.relpath(filepath, base_dir)}]")
            except Exception as e:
                print(f"Error processing {filepath}: {e}")

print(f"\nCompleted! Replaced '{old_email}' with '{new_email}' {total_replacements} times across {updated_files} files.")
