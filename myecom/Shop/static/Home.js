document.addEventListener('DOMContentLoaded', function() {
    const slider = document.querySelector('.slide');
    const leftBtn = document.getElementById('left');
    const rightBtn = document.getElementById('right');
    const cards = document.querySelectorAll('.cart');
    slider.innerHTML = '';

    cards.forEach(card => {
        slider.appendChild(card.cloneNode(true));
    });
    cards.forEach(card => {
        slider.appendChild(card.cloneNode(true));
    });
    
    // Add copies to the beginning
    cards.forEach(card => {
        slider.insertBefore(card.cloneNode(true), slider.firstChild);
    });

    const cardWidth = 395;
    const totalOriginalCards = cards.length;
    let isAnimating = false;
    
    // Set initial position to show the original set (skip the prepended clones)
    let currentPosition = -totalOriginalCards * cardWidth;
    slider.style.transform = `translateX(${currentPosition}px)`;

    function updateSliderPosition() {
        slider.style.transform = `translateX(${currentPosition}px)`;
    }

    function slideRight() {
        if (isAnimating) return;
        isAnimating = true;

        currentPosition -= cardWidth;
        slider.style.transition = 'transform 0.5s ease-in-out';
        updateSliderPosition();

        // If we've scrolled past all originals + one set of clones
        if (currentPosition <= -(totalOriginalCards * 2) * cardWidth) {
            setTimeout(() => {
                slider.style.transition = 'none';
                currentPosition = -totalOriginalCards * cardWidth;
                updateSliderPosition();
            }, 500);
        }

        setTimeout(() => {
            isAnimating = false;
        }, 500);
    }

    function slideLeft() {
        if (isAnimating) return;
        isAnimating = true;

        currentPosition += cardWidth;
        slider.style.transition = 'transform 0.5s ease-in-out';
        updateSliderPosition();

        // If we've scrolled back to the clones
        if (currentPosition > -totalOriginalCards * cardWidth) {
            setTimeout(() => {
                slider.style.transition = 'none';
                currentPosition = -(totalOriginalCards * 2) * cardWidth;
                updateSliderPosition();
            }, 500);
        }

        setTimeout(() => {
            isAnimating = false;
        }, 500);
    }

    // Auto slide every 3 seconds
    let autoSlideInterval = setInterval(slideRight, 3000);

    // Reset interval on manual navigation
    function resetInterval() {
        clearInterval(autoSlideInterval);
        autoSlideInterval = setInterval(slideRight, 3000);
    }

    rightBtn.addEventListener('click', () => {
        slideRight();
        resetInterval();
    });

    leftBtn.addEventListener('click', () => {
        slideLeft();
        resetInterval();
    });

    // Pause auto-slide when hovering over the slider
    slider.addEventListener('mouseenter', () => {
        clearInterval(autoSlideInterval);
    });

    slider.addEventListener('mouseleave', () => {
        autoSlideInterval = setInterval(slideRight, 3000);
    });

    // Handle transition end
    slider.addEventListener('transitionend', () => {
        isAnimating = false;
    });

    // Initialize slider position
    updateSliderPosition();
});
