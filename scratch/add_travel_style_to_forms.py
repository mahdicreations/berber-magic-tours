import os
import re

base_dir = r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours"
tours_dir = os.path.join(base_dir, "tours")

travel_style_html = """                                <div class="form-group mb-3">
                                    <label style="font-weight: 700; font-size: 0.95rem; color: #1E293B; margin-bottom: 10px; display: block;">Travel Style</label>
                                    <input type="hidden" name="travel_style" id="book-travel-style" value="Standard">
                                    <div class="travel-style-options" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px;">
                                        <div class="travel-style-card active" onclick="selectTravelStyle(this, 'Standard')" style="border: 2px solid #D95D39; background: #FFF7F2; border-radius: 14px; padding: 12px 6px; text-align: center; cursor: pointer; transition: all 0.25s ease;">
                                            <i class="fas fa-wallet" style="font-size: 1.35rem; color: #D95D39; margin-bottom: 6px; display: block;"></i>
                                            <span style="font-weight: 700; font-size: 0.92rem; color: #1E293B; display: block;">Standard</span>
                                            <small style="font-size: 0.72rem; color: #64748B; display: block; margin-top: 3px; line-height: 1.2;">Authentic &amp; Simple</small>
                                        </div>
                                        <div class="travel-style-card" onclick="selectTravelStyle(this, 'Comfort')" style="border: 1px solid #E2E8F0; background: #FFFFFF; border-radius: 14px; padding: 12px 6px; text-align: center; cursor: pointer; transition: all 0.25s ease;">
                                            <i class="fas fa-hotel" style="font-size: 1.35rem; color: #D95D39; margin-bottom: 6px; display: block;"></i>
                                            <span style="font-weight: 700; font-size: 0.92rem; color: #1E293B; display: block;">Comfort</span>
                                            <small style="font-size: 0.72rem; color: #64748B; display: block; margin-top: 3px; line-height: 1.2;">3-4★ Riads &amp; Camps</small>
                                        </div>
                                        <div class="travel-style-card" onclick="selectTravelStyle(this, 'Luxury')" style="border: 1px solid #E2E8F0; background: #FFFFFF; border-radius: 14px; padding: 12px 6px; text-align: center; cursor: pointer; transition: all 0.25s ease;">
                                            <i class="fas fa-crown" style="font-size: 1.35rem; color: #D95D39; margin-bottom: 6px; display: block;"></i>
                                            <span style="font-weight: 700; font-size: 0.92rem; color: #1E293B; display: block;">Luxury</span>
                                            <small style="font-size: 0.72rem; color: #64748B; display: block; margin-top: 3px; line-height: 1.2;">5★ Riads &amp; Glamping</small>
                                        </div>
                                    </div>
                                </div>\n"""

print("=== ADDING TRAVEL STYLE WIDGET TO ALL TOUR BOOKING FORMS ===")
total_updated = 0

for file_name in sorted(os.listdir(tours_dir)):
    if not file_name.endswith(".html"):
        continue

    file_path = os.path.join(tours_dir, file_name)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Skip if Travel Style is already present
    if "Travel Style" in content:
        continue

    # Insert right before <div class="form-group mb-4"> (which is book-message / Additional Requests)
    target_str = '<div class="form-group mb-4">'
    if target_str in content:
        content = content.replace(target_str, travel_style_html + "                                " + target_str, 1)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        total_updated += 1
        print(f"Updated booking form in [{file_name}]")
    else:
        # Fallback target: before Additional Requests
        target_alt = '<label for="book-message">'
        if target_alt in content:
            pos = content.find(target_alt)
            # Find preceding <div class="form-group
            div_pos = content.rfind('<div class="form-group', 0, pos)
            if div_pos != -1:
                content = content[:div_pos] + travel_style_html + "                                " + content[div_pos:]
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                total_updated += 1
                print(f"Updated booking form in [{file_name}] (fallback target)")

print(f"\nDone! Added Travel Style widget to booking forms across {total_updated} tour pages.")
