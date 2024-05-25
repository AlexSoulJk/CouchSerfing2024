const swiperBig = new Swiper('#swiper-big', {
    loop: true,

    // Navigation arrows
    navigation: {
        nextEl: '#nextBut',
        prevEl: '#prevBut',
    },
});

const swiperSmall = new Swiper('#swiper-small', {
    loop: true,
    slidesPerView: 5,
    spaceBetween: 20,
    initialSlide: 1,
});