with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

idx = css.find('.mobile-menu')
if idx != -1:
    print(css[idx:idx+1000])
else:
    print("mobile-menu not found in style.css")
