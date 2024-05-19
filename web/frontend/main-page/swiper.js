const swiper1 = new Swiper('#swiper1', {
    loop: true,
    slidesPerView: 3,
    spaceBetween: 15,
    navigation: {
        nextEl: '#nextBut',
        prevEl: '#prevBut',
    },
    on: {
        slideChange: function () {
            const activeIndex = this.activeIndex;

            this.slides.forEach((slide, index) => {
                if (index === activeIndex) {
                    slide.style.transform = 'scale(0.9)';
                } else if (index === activeIndex - 1 || (activeIndex === 0 && index === this.slides.length - 1)) {
                    slide.style.transform = 'scale(0.9)';
                } else if (index === activeIndex + 1 || (activeIndex === this.slides.length - 1 && index === 0)) {
                    slide.style.transform = 'scale(1)';
                } else {
                    slide.style.transform = 'scale(0.9)';
                }
            });
        },
    },
});

const swiper2 = new Swiper('#swiper2', {
    loop: true,

    // Navigation arrows
    navigation: {
        nextEl: '#nextBut2',
        prevEl: '#prevBut2',
    },
});


