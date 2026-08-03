# -*- coding: utf-8 -*-
import os
import re

tours_dir = r"c:\Users\el mahdi\Desktop\mahdicreations\berber-magic-tours\tours"

# Pattern to match the inline form handler script block (the problematic one)
# It matches the script block containing the tourBookingForm submit listener with alert+reset
pattern = re.compile(
    r'\n?\s*// Form handler\s*\n\s*document\.getElementById\([\'"]tourBookingForm[\'"]\)\.addEventListener\([\'"]submit[\'"],\s*function\(e\)\s*\{[^}]*e\.preventDefault\(\);[^}]*(?:alert|reset)[^}]*\}\);\s*\n?',
    re.DOTALL
)

# Also match a simpler version
pattern2 = re.compile(
    r'\n\s*/\/ Form handler\s*\n\s*document\.getElementById\([\'"](tourBookingForm)[\'"\]]\)\.addEventListener\([\'"](submit)[\'"],\s*function\(e\)\s*\{.*?e\.preventDefault\(\);.*?(?:alert\(.*?\)|this\.reset\(\))\s*;?.*?this\.reset\(\)\s*;?\s*\}\);\s*\n',
    re.DOTALL
)

updated = 0
failed = 0

html_files = [f for f in os.listdir(tours_dir) if f.endswith('.html')]
print(f"Processing {len(html_files)} tour HTML files...")

for filename in html_files:
    filepath = os.path.join(tours_dir, filename)
    
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    # Check if the problematic inline script exists
    if "tourBookingForm" not in content or "alert(" not in content:
        continue
    
    original = content
    
    # Find the exact block using line-by-line approach
    lines = content.split('\n')
    new_lines = []
    skip = False
    skip_count = 0
    i = 0
    
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Detect start of the problematic inline form handler
        if (
            '// Form handler' in stripped or 
            ("tourBookingForm" in stripped and "addEventListener" in stripped and "submit" in stripped)
        ):
            # Look ahead to confirm it contains alert or reset (the bad ones)
            block = '\n'.join(lines[i:i+10])
            if ('alert(' in block or 'this.reset()' in block) and 'e.preventDefault()' in block:
                # Skip this block (usually 5-6 lines)
                # Find the closing }); 
                depth = 0
                j = i
                found_open = False
                while j < len(lines):
                    for ch in lines[j]:
                        if ch == '{':
                            depth += 1
                            found_open = True
                        elif ch == '}':
                            depth -= 1
                    if found_open and depth <= 0:
                        # Skip from i to j inclusive + one more for empty line
                        i = j + 1
                        # Skip the comment line before if it was "// Form handler"
                        if i < len(lines) and lines[i].strip() == '':
                            i += 1
                        break
                    j += 1
                print(f"  Removed inline handler from: {filename}")
                continue
        
        new_lines.append(line)
        i += 1
    
    new_content = '\n'.join(new_lines)
    
    if new_content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        updated += 1
        print("  OK Updated: " + filename)
    
print(f"\n=== DONE ===")
print(f"Updated: {updated} files")
print(f"Skipped (no inline handler): {len(html_files) - updated} files")
