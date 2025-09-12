// Staff Engineer's Field Guide - Homepage Interactions
// Parallax scrolling and smooth animations

document.addEventListener('DOMContentLoaded', function() {
    
    // Parallax effect for hero section
    function initParallaxEffect() {
        const heroWallpaper = document.querySelector('.hero-wallpaper');
        if (!heroWallpaper) return;

        let ticking = false;

        function updateParallax() {
            const scrolled = window.pageYOffset;
            const rate = scrolled * -0.5;
            const opacity = Math.max(0, 1 - scrolled / (window.innerHeight * 0.8));
            
            heroWallpaper.style.transform = `translate3d(0, ${rate}px, 0)`;
            heroWallpaper.style.opacity = opacity;
            
            ticking = false;
        }

        function requestTick() {
            if (!ticking) {
                requestAnimationFrame(updateParallax);
                ticking = true;
            }
        }

        window.addEventListener('scroll', requestTick, { passive: true });
    }

    // Smooth scroll for hero scroll indicator
    function initSmoothScroll() {
        const scrollIndicator = document.querySelector('.hero-scroll-indicator');
        if (!scrollIndicator) return;

        scrollIndicator.addEventListener('click', function(e) {
            e.preventDefault();
            const contentSection = document.querySelector('.content-section');
            if (contentSection) {
                contentSection.scrollIntoView({ 
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    }

    // Animate elements on scroll
    function initScrollAnimations() {
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -100px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate-in');
                }
            });
        }, observerOptions);

        // Observe card elements
        const cards = document.querySelectorAll('.grid.cards > *, .admonition, .authority-showcase, .features-highlight');
        cards.forEach(card => {
            card.classList.add('animate-on-scroll');
            observer.observe(card);
        });
    }

    // Stats counter animation
    function initStatsAnimation() {
        const stats = document.querySelectorAll('.stat-item');
        
        const statsObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('stat-animate');
                }
            });
        }, { threshold: 0.5 });

        stats.forEach(stat => statsObserver.observe(stat));
    }

    // Floating animation for hero elements
    function initFloatingAnimation() {
        const heroContent = document.querySelector('.hero-content');
        if (!heroContent) return;

        let mouseX = 0;
        let mouseY = 0;
        let targetX = 0;
        let targetY = 0;

        function updateFloat() {
            targetX += (mouseX - targetX) * 0.02;
            targetY += (mouseY - targetY) * 0.02;
            
            heroContent.style.transform = `translate(${targetX * 0.02}px, ${targetY * 0.02}px)`;
            requestAnimationFrame(updateFloat);
        }

        heroContent.addEventListener('mousemove', (e) => {
            const rect = heroContent.getBoundingClientRect();
            mouseX = (e.clientX - rect.left - rect.width / 2) / rect.width * 100;
            mouseY = (e.clientY - rect.top - rect.height / 2) / rect.height * 100;
        });

        updateFloat();
    }

    // Enhanced button hover effects
    function initButtonEffects() {
        const buttons = document.querySelectorAll('.md-button');
        
        buttons.forEach(button => {
            button.addEventListener('mouseenter', function() {
                this.style.transform = 'translateY(-2px) scale(1.02)';
            });
            
            button.addEventListener('mouseleave', function() {
                this.style.transform = 'translateY(0) scale(1)';
            });
        });
    }

    // Initialize all effects
    initParallaxEffect();
    initSmoothScroll();
    initScrollAnimations();
    initStatsAnimation();
    initFloatingAnimation();
    initButtonEffects();

    // Add a subtle cursor trail effect
    function initCursorTrail() {
        const heroWallpaper = document.querySelector('.hero-wallpaper');
        if (!heroWallpaper) return;

        let trail = [];
        const trailLength = 8;

        function createTrailDot(x, y) {
            const dot = document.createElement('div');
            dot.className = 'cursor-trail-dot';
            dot.style.left = x + 'px';
            dot.style.top = y + 'px';
            heroWallpaper.appendChild(dot);

            setTimeout(() => {
                dot.remove();
            }, 800);
        }

        heroWallpaper.addEventListener('mousemove', (e) => {
            if (Math.random() > 0.8) { // Only create dots occasionally
                createTrailDot(e.clientX - heroWallpaper.offsetLeft, e.clientY - heroWallpaper.offsetTop);
            }
        });
    }

    initCursorTrail();

    // Add typing effect to the hero title
    function initTypingEffect() {
        const title = document.querySelector('.hero-title');
        if (!title) return;

        const text = title.textContent;
        title.textContent = '';
        title.style.borderRight = '2px solid rgba(255,255,255,0.8)';

        let i = 0;
        function typeWriter() {
            if (i < text.length) {
                title.textContent += text.charAt(i);
                i++;
                setTimeout(typeWriter, 100);
            } else {
                // Remove cursor after typing
                setTimeout(() => {
                    title.style.borderRight = 'none';
                }, 1000);
            }
        }

        // Start typing after a short delay
        setTimeout(typeWriter, 500);
    }

    initTypingEffect();
});