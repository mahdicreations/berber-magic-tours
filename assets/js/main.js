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
});
