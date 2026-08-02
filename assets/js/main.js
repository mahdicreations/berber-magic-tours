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

    const carouselArea = document.querySelector('.ta-carousel-wrapper');
    if (carouselArea) {
        carouselArea.addEventListener('mouseenter', () => clearInterval(autoPlayTimer));
        carouselArea.addEventListener('mouseleave', () => startAutoPlay());
    }
});



