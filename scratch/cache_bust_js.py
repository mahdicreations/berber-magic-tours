import os

base_dir = r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours\tours"

updated = 0
for filename in os.listdir(base_dir):
    if filename.endswith(".html"):
        filepath = os.path.join(base_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Replace main.js with main.js?v=1.1 to bust cache
        if "main.js" in content and "main.js?v=1.1" not in content:
            new_content = content.replace("main.js", "main.js?v=1.1")
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            updated += 1

print(f"Busted JS cache in {updated} tour files.")
