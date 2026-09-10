import os

js_path = 'assets/js/main.js'
content = open(js_path, 'r', encoding='utf-8').read()

js_patch = """
    // Mobile Submenu Toggle (A11y)
    const dropdownToggles = document.querySelectorAll('.mobile-dropdown-toggle');
    dropdownToggles.forEach(toggle => {
        toggle.addEventListener('click', function(e) {
            e.preventDefault();
            const li = this.closest('li.mobile-dropdown');
            const icon = this.querySelector('i');
            
            const isExpanded = this.getAttribute('aria-expanded') === 'true';
            this.setAttribute('aria-expanded', !isExpanded);
            
            if (isExpanded) {
                li.classList.remove('open');
                if(icon) { icon.classList.remove('fa-minus'); icon.classList.add('fa-plus'); }
            } else {
                li.classList.add('open');
                if(icon) { icon.classList.remove('fa-plus'); icon.classList.add('fa-minus'); }
            }
        });
    });

    // Slider Dot Click Support
    const sliderDots = document.querySelectorAll('.slider-dots .dot');
    sliderDots.forEach(dot => {
        dot.addEventListener('click', function() {
            const index = parseInt(this.getAttribute('data-index'), 10);
            if(typeof changeSlide === 'function') {
                changeSlide(index);
                // Restart timer if needed, but changeSlide handles the visual change
            }
        });
    });
"""

if '// Mobile Submenu Toggle (A11y)' not in content:
    # Insert before the last DOMContentLoaded closing bracket
    # Find the last '});' which closes DOMContentLoaded
    parts = content.rsplit('});', 1)
    if len(parts) == 2:
        new_content = parts[0] + js_patch + '});\n' + parts[1]
        open(js_path, 'w', encoding='utf-8').write(new_content)
        print("Updated main.js")
    else:
        print("Could not find the end of DOMContentLoaded")
else:
    print("main.js already patched")

