with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
idx = css.find('.tripadvisor-widget-dark')
if idx != -1:
    print("--- TRIPADVISOR WIDGET CSS ---")
    print(css[idx-100:idx+800])

idx_soc = css.find('.social-links')
if idx_soc != -1:
    print("\n--- SOCIAL LINKS CSS ---")
    print(css[idx_soc-50:idx_soc+500])
