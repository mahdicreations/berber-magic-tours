import os
import datetime

domain = "https://berber-magic-tours.com"
today = datetime.datetime.now().strftime("%Y-%m-%d")

root_files = sorted([f for f in os.listdir('.') if f.endswith('.html')])
tour_files = sorted([os.path.join('tours', f) for f in os.listdir('tours') if f.endswith('.html')])

url_entries = []

# Homepage
url_entries.append(f"""  <url>
    <loc>{domain}/</loc>
    <lastmod>{today}</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>""")

for f in root_files:
    if f == 'index.html':
        continue
    slug = f[:-5]
    if f in ['about-us.html', 'contact.html', 'faq.html', 'privacy-policy.html', 'terms-conditions.html']:
        priority = '0.7'
        changefreq = 'monthly'
    else:
        priority = '0.9'
        changefreq = 'weekly'
    url_entries.append(f"""  <url>
    <loc>{domain}/{slug}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
  </url>""")

for f in tour_files:
    clean_path = f.replace('\\', '/')
    if clean_path.endswith('.html'):
        clean_path = clean_path[:-5]
    url_entries.append(f"""  <url>
    <loc>{domain}/{clean_path}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>""")

blog_files = sorted([os.path.join('blog', f) for f in os.listdir('blog') if f.endswith('.html') and f != 'index.html'])

for f in blog_files:
    clean_path = f.replace('\\', '/')
    if clean_path.endswith('.html'):
        clean_path = clean_path[:-5]
    url_entries.append(f"""  <url>
    <loc>{domain}/{clean_path}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>""")



xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
xml_content += '\n'.join(url_entries)
xml_content += '\n</urlset>\n'

with open('sitemap.xml', 'w', encoding='utf-8') as sf:
    sf.write(xml_content)

print(f"Generated sitemap.xml with {len(url_entries)} URLs successfully.")
