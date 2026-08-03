import os

base_dir = r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours"
index_path = os.path.join(base_dir, "index.html")

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

start_marker = "    <!-- Guest Reviews / What Our Travelers Say Section -->"
end_marker = "    </section>\n\n    <!-- Contact CTA -->"

start_idx = content.find(start_marker)
if start_idx == -1:
    print("ERROR: Start marker not found!")
    exit(1)

end_marker_pos = content.find("<!-- Contact CTA -->")
if end_marker_pos == -1:
    print("ERROR: End marker position not found!")
    exit(1)

# The section ends at the </section> before <!-- Contact CTA -->
reviews_block = content[start_idx:end_marker_pos]

# Remove reviews block from original location
content_without_reviews = content[:start_idx] + content[end_marker_pos:]

# Find target location: right after presentation section </section> and before Trek & Hike
target_marker = "    </section>\n\n    <!-- Trek & Hike Section -->"
target_idx = content_without_reviews.find(target_marker)

if target_idx == -1:
    print("ERROR: Target insertion point not found!")
    exit(1)

insertion_point = target_idx + len("    </section>\n\n")

new_content = (
    content_without_reviews[:insertion_point]
    + reviews_block
    + "\n"
    + content_without_reviews[insertion_point:]
)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Guest Reviews section moved successfully!")
