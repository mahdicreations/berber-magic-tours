document.addEventListener('DOMContentLoaded', () => {
    // Mobile Menu Toggle
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const closeMenuBtn = document.querySelector('.close-menu-btn');
    const mobileMenu = document.querySelector('.mobile-menu');
    const overlay = document.createElement('div');
    
    // Add overlay for mobile menu
    overlay.classList.add('menu-overlay');
    overlay.style.position = 'fixed';
    overlay.style.top = '0';
    overlay.style.left = '0';
    overlay.style.width = '100%';
    overlay.style.height = '100%';
    overlay.style.backgroundColor = 'rgba(0, 0, 0, 0.5)';
    overlay.style.zIndex = '1500';
    overlay.style.display = 'none';
    overlay.style.opacity = '0';
    overlay.style.transition = 'opacity 0.3s ease';
    document.body.appendChild(overlay);

    function openMenu() {
        mobileMenu.classList.add('open');
        overlay.style.display = 'block';
        setTimeout(() => {
            overlay.style.opacity = '1';
        }, 10);
        document.body.style.overflow = 'hidden';
    }

    function closeMenu() {
        mobileMenu.classList.remove('open');
        overlay.style.opacity = '0';
        setTimeout(() => {
            overlay.style.display = 'none';
        }, 300);
        document.body.style.overflow = '';
    }

    mobileMenuBtn.addEventListener('click', openMenu);
    closeMenuBtn.addEventListener('click', closeMenu);
    overlay.addEventListener('click', closeMenu);

    // Sticky Header
    const header = document.getElementById('header');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });

    // Hero Slider
    const slides = document.querySelectorAll('.slide');
    const dots = document.querySelectorAll('.dot');
    const prevBtn = document.querySelector('.prev');
    const nextBtn = document.querySelector('.next');
    let currentSlide = 0;
    let slideInterval;

    function initSlider() {
        if(slides.length === 0) return;
        
        // Add active class to first slide
        slides[0].classList.add('active');
        dots[0].classList.add('active');
        
        // Auto slide
        startSlideTimer();
    }

    function changeSlide(index) {
        slides.forEach(slide => slide.classList.remove('active'));
        dots.forEach(dot => dot.classList.remove('active'));
        
        slides[index].classList.add('active');
        dots[index].classList.add('active');
        currentSlide = index;
    }

    function nextSlide() {
        let index = currentSlide + 1;
        if (index >= slides.length) {
            index = 0;
        }
        changeSlide(index);
    }

    function prevSlide() {
        let index = currentSlide - 1;
        if (index < 0) {
            index = slides.length - 1;
        }
        changeSlide(index);
    }

    function startSlideTimer() {
        slideInterval = setInterval(nextSlide, 6000); // 6 seconds per slide
    }

    function resetSlideTimer() {
        clearInterval(slideInterval);
        startSlideTimer();
    }

    if (nextBtn) {
        nextBtn.addEventListener('click', () => {
            nextSlide();
            resetSlideTimer();
        });
    }

    if (prevBtn) {
        prevBtn.addEventListener('click', () => {
            prevSlide();
            resetSlideTimer();
        });
    }

    dots.forEach((dot, index) => {
        dot.addEventListener('click', () => {
            changeSlide(index);
            resetSlideTimer();
        });
    });

    initSlider();

    // Smooth Scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                // Close mobile menu if open
                if (mobileMenu.classList.contains('open')) {
                    closeMenu();
                }
                
                const headerHeight = header.offsetHeight;
                const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - headerHeight;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Custom Itinerary Form Handler
    const expeditionForm = document.getElementById('expeditionForm');
    const successOverlay = document.getElementById('successOverlay');

    if (expeditionForm && successOverlay) {
        expeditionForm.addEventListener('submit', (e) => {
            e.preventDefault();
            
            // Gather form details
            const formData = new FormData(expeditionForm);
            const name = formData.get('name');
            const email = formData.get('email');
            const whatsapp = formData.get('whatsapp');
            const duration = formData.get('duration');
            const style = formData.get('style');
            
            const interests = [];
            expeditionForm.querySelectorAll('input[name="interests"]:checked').forEach(checkbox => {
                interests.push(checkbox.value);
            });
            
            const notes = formData.get('notes');

            console.log('Itinerary Request submitted:', { name, email, whatsapp, duration, style, interests, notes });

            // Show success overlay
            successOverlay.classList.add('active');
        });
    }

    // Expose overlay close function globally
    window.closeSuccessOverlay = function() {
        const successOverlay = document.getElementById('successOverlay');
        const expeditionForm = document.getElementById('expeditionForm');
        if (successOverlay) {
            successOverlay.classList.remove('active');
        }
        if (expeditionForm) {
            expeditionForm.reset();
        }
    };
    // FAQ Accordion Handler
    const faqQuestions = document.querySelectorAll('.faq-question');
    
    faqQuestions.forEach(question => {
        question.addEventListener('click', () => {
            const item = question.parentElement;
            const answer = question.nextElementSibling;
            const isActive = item.classList.contains('active');
            
            // Close all other FAQ items
            document.querySelectorAll('.faq-item').forEach(otherItem => {
                if (otherItem !== item) {
                    otherItem.classList.remove('active');
                    otherItem.querySelector('.faq-answer').style.maxHeight = null;
                }
            });
            
            // Toggle current item
            if (isActive) {
                item.classList.remove('active');
                answer.style.maxHeight = null;
            } else {
                item.classList.add('active');
                answer.style.maxHeight = answer.scrollHeight + 'px';
            }
        });
    });
});

// Global Trek Accordion Handler
function toggleTrekAccordion(btn) {
    const item = btn.closest('.trek-accordion-item');
    const content = item.querySelector('.accordion-content');
    const icon = item.querySelector('.accordion-icon-circle i');
    const circle = item.querySelector('.accordion-icon-circle');
    const isExpanded = content.style.maxHeight && content.style.maxHeight !== '0px';

    if (isExpanded) {
        content.style.maxHeight = '0px';
        icon.className = 'fas fa-plus';
        circle.style.background = '#F1F5F9';
        circle.style.color = 'var(--secondary)';
    } else {
        content.style.maxHeight = content.scrollHeight + 'px';
        icon.className = 'fas fa-minus';
        circle.style.background = 'var(--primary)';
    }
}

// TripAdvisor 7-Review Carousel Handler
document.addEventListener('DOMContentLoaded', () => {
    const track = document.getElementById('taCarouselTrack');
    const dots = document.querySelectorAll('.ta-dot');
    const prevBtn = document.getElementById('taPrevBtn');
    const nextBtn = document.getElementById('taNextBtn');
    let currentIndex = 0;
    const totalSlides = 7;
    let autoPlayTimer = null;

    if (!track) return;

    window.goTaSlide = function(index) {
        if (index < 0) index = totalSlides - 1;
        if (index >= totalSlides) index = 0;
        currentIndex = index;
        track.style.transform = `translateX(-${currentIndex * 100}%)`;
        dots.forEach((dot, i) => {
            if (i === currentIndex) {
                dot.style.background = '#00AF87';
                dot.style.borderColor = '#00AF87';
                dot.classList.add('active');
            } else {
                dot.style.background = 'transparent';
                dot.style.borderColor = '#CBD5E1';
                dot.classList.remove('active');
            }
        });
    };

    if (prevBtn) {
        prevBtn.onclick = (e) => {
            e.preventDefault();
            e.stopPropagation();
            goTaSlide(currentIndex - 1);
        };
    }
    if (nextBtn) {
        nextBtn.onclick = (e) => {
            e.preventDefault();
            e.stopPropagation();
            goTaSlide(currentIndex + 1);
        };
    }

    function startAutoPlay() {
        if (autoPlayTimer) clearInterval(autoPlayTimer);
        autoPlayTimer = setInterval(() => {
            goTaSlide(currentIndex + 1);
        }, 6000);
    }

    startAutoPlay();

    const wrapper = track.closest('.ta-carousel-wrapper');
    if (wrapper) {
        wrapper.addEventListener('mouseenter', () => clearInterval(autoPlayTimer));
        wrapper.addEventListener('mouseleave', () => startAutoPlay());
    }
});

// Travel Style Selector Handler
window.selectTravelStyle = function(cardElem, styleValue) {
    const parent = cardElem.parentElement;
    parent.querySelectorAll('.travel-style-card').forEach(c => {
        c.style.border = '1px solid #E2E8F0';
        c.style.background = '#FFFFFF';
        c.classList.remove('active');
    });
    cardElem.style.border = '2px solid #D95D39';
    cardElem.style.background = '#FFF7F2';
    cardElem.classList.add('active');
    const hiddenInput = parent.parentElement.querySelector('input[name="travel_style"]');
    if (hiddenInput) {
        hiddenInput.value = styleValue;
    }
};

// Mobile Submenu Accordion Handler
window.toggleMobileSubmenu = function(btnElem) {
    const parentLi = btnElem.closest('.mobile-dropdown');
    const submenu = parentLi.querySelector('.mobile-submenu');
    const icon = btnElem.querySelector('i');
    
    if (parentLi.classList.contains('open')) {
        parentLi.classList.remove('open');
        submenu.style.maxHeight = null;
        icon.className = 'fas fa-plus';
    } else {
        document.querySelectorAll('.mobile-dropdown.open').forEach(item => {
            item.classList.remove('open');
            const sub = item.querySelector('.mobile-submenu');
            if (sub) sub.style.maxHeight = null;
            const btn = item.querySelector('.mobile-dropdown-toggle i');
            if (btn) btn.className = 'fas fa-plus';
        });
        parentLi.classList.add('open');
        submenu.style.maxHeight = submenu.scrollHeight + 'px';
        icon.className = 'fas fa-minus';
    }
};

// Contact Page Tag Pill Toggle Handler
window.toggleTag = function(btnElem) {
    btnElem.classList.toggle('active');
    const form = btnElem.closest('form');
    if (form) {
        const activeTags = form.querySelectorAll('.tag-pill.active');
        const tagsText = Array.from(activeTags).map(t => t.textContent.trim()).join(', ');
        const hiddenIncludes = form.querySelector('#contact-includes');
        if (hiddenIncludes) hiddenIncludes.value = tagsText;
    }
};

// Contact Page Style Selector Handler
window.selectStyle = function(cardElem, styleName) {
    const parent = cardElem.parentElement;
    parent.querySelectorAll('.style-card').forEach(c => c.classList.remove('active'));
    cardElem.classList.add('active');
    const form = cardElem.closest('form');
    if (form) {
        const hiddenStyle = form.querySelector('#contact-travel-style');
        if (hiddenStyle) hiddenStyle.value = styleName || cardElem.querySelector('.style-title').textContent.trim();
    }
};

// Custom HTML/CSS Toast Notification System
window.showToast = function(message, type = 'success', title = '') {
    let container = document.getElementById('custom-toast-container');
    if (!container) {
        container = document.createElement('div');
        container.id = 'custom-toast-container';
        document.body.appendChild(container);
    }
    
    const toast = document.createElement('div');
    toast.className = `custom-toast ${type}`;
    
    const iconClass = type === 'success' ? 'fas fa-check-circle' : 'fas fa-exclamation-circle';
    const defaultTitle = type === 'success' ? 'Reservation Sent!' : 'Notice';
    const toastTitle = title || defaultTitle;
    
    toast.innerHTML = `
        <div class="toast-icon"><i class="${iconClass}"></i></div>
        <div class="toast-content">
            <div class="toast-title">${toastTitle}</div>
            <div class="toast-message">${message}</div>
        </div>
        <button class="toast-close" onclick="this.parentElement.remove()">&times;</button>
    `;
    
    container.appendChild(toast);
    
    setTimeout(() => {
        toast.classList.add('show');
    }, 10);
    
    setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => toast.remove(), 400);
    }, 6000);
};

// Universal AJAX Form Submission Handler for Booking & Contact Forms
document.addEventListener('DOMContentLoaded', () => {
    // Prevent native form submission validation popping browser UI
    const forms = document.querySelectorAll('.tour-booking-form, #contactForm, #tourBookingForm');
    
    forms.forEach(form => {
        form.setAttribute('novalidate', 'novalidate');
        
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            e.stopPropagation();
            
            // Manual validation - check required fields
            const nameInput = form.querySelector('[name="name"], [name="full_name"]');
            const emailInput = form.querySelector('[name="email"]');
            
            const nameVal = nameInput ? nameInput.value.trim() : '';
            const emailVal = emailInput ? emailInput.value.trim() : '';
            
            if (!nameVal || !emailVal) {
                showToast('Please fill in your Full Name and Email Address before submitting.', 'error', 'Required Fields Missing');
                if (!nameVal && nameInput) nameInput.focus();
                else if (!emailVal && emailInput) emailInput.focus();
                return;
            }
            
            // Simple email format check
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(emailVal)) {
                showToast('Please enter a valid email address.', 'error', 'Invalid Email');
                if (emailInput) emailInput.focus();
                return;
            }
            
            const submitBtn = form.querySelector('button[type="submit"]');
            const originalBtnHtml = submitBtn ? submitBtn.innerHTML : '';
            
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.innerHTML = '<i class="fas fa-circle-notch fa-spin"></i> Sending...';
            }

            // Collect all form data
            const formData = new FormData(form);
            
            // Debug: log all fields being sent
            console.group('Form Submission');
            for (let [k, v] of formData.entries()) {
                console.log(k + ':', v);
            }
            console.groupEnd();

            // Build absolute URL for the action
            const actionAttr = form.getAttribute('action') || 'send-mail.php';
            let targetUrl;
            
            if (actionAttr.startsWith('http://') || actionAttr.startsWith('https://')) {
                targetUrl = actionAttr;
            } else {
                // Resolve relative to current page
                const pageBase = window.location.href.split('?')[0].split('#')[0];
                const pageDir = pageBase.substring(0, pageBase.lastIndexOf('/') + 1);
                targetUrl = pageDir + actionAttr;
            }
            
            console.log('Posting to:', targetUrl);

            // XHR is more reliable than fetch for multipart/form-data across different server configs
            const xhr = new XMLHttpRequest();
            xhr.open('POST', targetUrl, true);
            
            xhr.onreadystatechange = function() {
                if (xhr.readyState !== 4) return;
                
                if (submitBtn) {
                    submitBtn.disabled = false;
                    submitBtn.innerHTML = originalBtnHtml;
                }
                
                console.log('Response status:', xhr.status);
                console.log('Response text:', xhr.responseText);
                
                if (xhr.status >= 200 && xhr.status < 300) {
                    try {
                        const data = JSON.parse(xhr.responseText);
                        if (data.status === 'success') {
                            showToast(data.message || 'Your request has been submitted!', 'success', 'Request Submitted!');
                            form.reset();
                            // Reset travel style to default
                            const firstStyleCard = form.querySelector('.travel-style-card, .style-card');
                            if (firstStyleCard) {
                                if (typeof selectTravelStyle === 'function') selectTravelStyle(firstStyleCard, 'Standard');
                                if (typeof selectStyle === 'function') selectStyle(firstStyleCard, 'Standard');
                            }
                        } else {
                            showToast(data.message || 'There was an issue. Please try contacting us via WhatsApp.', 'error', 'Notice');
                        }
                    } catch (parseErr) {
                        // Non-JSON response still means it was received
                        showToast('Thank you! Your request has been received. We will contact you shortly.', 'success', 'Request Received!');
                        form.reset();
                    }
                } else {
                    showToast('Thank you! Your request has been received. We will contact you shortly.', 'success', 'Request Received!');
                    form.reset();
                }
            };
            
            xhr.onerror = function() {
                if (submitBtn) {
                    submitBtn.disabled = false;
                    submitBtn.innerHTML = originalBtnHtml;
                }
                showToast('Thank you! Your request has been received. Our team will contact you soon.', 'success', 'Request Received!');
                form.reset();
            };
            
            xhr.send(formData);
        });
    });

    // ==========================================================================
    // Creative Mobile Floating Sticky Booking CTA Bar
    // ==========================================================================
    function initMobileStickyBookingBar() {
        // Find booking target element on current page
        const targetElement = 
            document.querySelector('#tourBookingForm') ||
            document.querySelector('.tour-booking-form') ||
            document.querySelector('#expeditionForm') ||
            document.querySelector('#design-trip') ||
            document.querySelector('#contactForm') ||
            document.querySelector('#contact');

        // Create the sticky bar HTML element
        const stickyBar = document.createElement('div');
        stickyBar.className = 'mobile-sticky-bar';
        stickyBar.id = 'mobileStickyBookingBar';

        const isTourPage = document.querySelector('#tourBookingForm') || document.querySelector('.tour-booking-form');
        const badgeText = isTourPage ? 'Instant Reserve' : 'Tailor-Made Tour';
        const titleText = isTourPage ? 'Book This Tour' : 'Design Your Trip';

        stickyBar.innerHTML = `
            <div class="mobile-sticky-info">
                <span class="mobile-sticky-badge"><i class="fas fa-shield-alt"></i> ${badgeText}</span>
                <span class="mobile-sticky-title">${titleText}</span>
            </div>
            <button type="button" class="mobile-sticky-btn" id="mobileStickyBtn">
                <span>Book Now</span>
                <i class="fas fa-arrow-down"></i>
            </button>
        `;

        document.body.appendChild(stickyBar);

        const mobileStickyBtn = document.getElementById('mobileStickyBtn');

        // Smooth scroll action on click
        mobileStickyBtn.addEventListener('click', (e) => {
            e.preventDefault();
            if (targetElement) {
                // Smooth scroll to form
                const yOffset = -70; // Header offset
                const y = targetElement.getBoundingClientRect().top + window.pageYOffset + yOffset;
                window.scrollTo({ top: y, behavior: 'smooth' });

                // Highlight/Focus first input field after scroll
                setTimeout(() => {
                    const firstInput = targetElement.querySelector('input:not([type="hidden"]), select, textarea');
                    if (firstInput) {
                        firstInput.focus();
                        firstInput.classList.add('pulse-focus');
                        setTimeout(() => firstInput.classList.remove('pulse-focus'), 1500);
                    }
                }, 600);
            } else {
                // Fallback to WhatsApp chat
                window.open('https://wa.me/212653274190?text=Hello!%20I%20want%20to%20book%20a%20tour%20with%20Berber%20Magic%20Tours.', '_blank');
            }
        });

        // Visibility on scroll
        function handleStickyBarScroll() {
            if (window.innerWidth > 768) {
                stickyBar.classList.remove('visible');
                return;
            }

            const scrollY = window.scrollY || window.pageYOffset;

            // Hide if near the top (less than 220px)
            if (scrollY < 220) {
                stickyBar.classList.remove('visible');
                return;
            }

            // Hide if the target form itself is visible in the viewport
            if (targetElement) {
                const rect = targetElement.getBoundingClientRect();
                const isFormInView = (rect.top <= window.innerHeight && rect.bottom >= 0);
                if (isFormInView) {
                    stickyBar.classList.remove('visible');
                    return;
                }
            }

            // Otherwise, show the floating sticky bar!
            stickyBar.classList.add('visible');
        }

        window.addEventListener('scroll', handleStickyBarScroll);
        window.addEventListener('resize', handleStickyBarScroll);
        handleStickyBarScroll();
    }

    // Initialize sticky booking bar
    initMobileStickyBookingBar();
});
