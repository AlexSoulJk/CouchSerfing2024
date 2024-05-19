document.addEventListener('DOMContentLoaded', function () {
    // Получаем все элементы изображений в нижней галерее и в свайпере
    const galleryImages = document.querySelectorAll('.swiper-slide');

    // Добавляем обработчик клика на изображения в нижней галерее
    galleryImages.forEach((image) => {
        image.addEventListener('click', function () {
            // Получаем индекс изображения из data-index
            const clickedIndex = parseInt(image.getAttribute('data-index'));
            console.log('clickedIndex', clickedIndex);

            // Получаем слайд в swiperBig с совпадающим индексом data-index-big
            const correspondingSlide = Array.from(swiperBig.slides).find(slide => parseInt(slide.getAttribute('data-index-big')) === clickedIndex);
            console.log('correspondingSlide', correspondingSlide);

            if (correspondingSlide) {
                // Получаем индекс слайда в swiperBig
                const correspondingSlideIndex = swiperBig.slides.indexOf(correspondingSlide);

                // Перемещаем swiperBig на соответствующий слайд
                swiperBig.slideTo(correspondingSlideIndex);

                // Перерисовываем swiperBig
                swiperBig.update();
            }
        });
    });
});


document.addEventListener('DOMContentLoaded', function () {

    // Обработчик события для кнопки "вправо" верхнего свайпера
    document.getElementById('nextBut').addEventListener('click', function () {
        swiperBig.slideNext();
        swiperSmall.slideNext();
        console.log('Active Index in swiperBig arrow:', swiperBig.activeIndex);
        console.log('Active Index in swiperSmall arrow:', swiperSmall.activeIndex);
    });

    // Обработчик события для кнопки "влево" верхнего свайпера
    document.getElementById('prevBut').addEventListener('click', function () {
        swiperBig.slidePrev();
        swiperSmall.slidePrev();
        console.log('Active Index in swiperBig arrow:', swiperBig.activeIndex);
        console.log('Active Index in swiperSmall arrow:', swiperSmall.activeIndex);
    });
});


function expandText() {
    const moreText = document.getElementById("expandText");
    const btnText = document.getElementById("expandButton");

    if (moreText.style.display === "none") {
        moreText.style.display = "inline";
        btnText.innerHTML = "Скрыть"; // меняем текст кнопки на "Скрыть"
        document.querySelector('.studio-description').style.maxHeight = 'none'; // убираем ограничение высоты
    } else {
        moreText.style.display = "none";
        btnText.innerHTML = "...ещё";
        document.querySelector('.studio-description').style.maxHeight = '60px'; // возвращаем начальное значение высоты
    }
}


// const ratingValue = 9.6; // значение рейтинга, которое нужно установить
// const ratingBar = document.querySelector('.rating-fill-real');
// const ratingBarWidth = (ratingValue / 10) * 181; // 175px - максимальная ширина
// ratingBar.style.width = ratingBarWidth + 'px';

// Получаем все элементы с классом "price-quality-row"
const priceQualityRows = document.querySelectorAll('.price-quality-row');

// Проходим по каждому элементу
priceQualityRows.forEach(row => {
    // Находим элемент с классом "expectation-value" внутри текущей строки
    const expectationValueElement = row.querySelector('.expectation-value');
    // Находим элемент с классом "rating-fill-real" внутри текущей строки
    const ratingFillElement = row.querySelector('.rating-fill-real');

    // Получаем значение ожидания из текстового содержимого элемента
    const expectationValue = parseFloat(expectationValueElement.textContent.replace(',', '.'));

    // Устанавливаем ширину заполнения в соответствии с ожидаемым значением
    ratingFillElement.style.width = `${(expectationValue / 10) * 100}%`;
});


//БУРГЕР
// Получаем ссылку на изображение профиля
const profileImage = document.getElementById('profile-image');
// Получаем ссылку на меню профиля
const profileMenu = document.getElementById('profile-menu');
// Получаем все элементы с классом cabinet-item
const cabinetItems = document.querySelectorAll('.cabinet-item');

const personalCabinet = document.querySelector('.personal-cabinet');

// Функция для показа и скрытия меню
function toggleProfileMenu() {
    // Показываем или скрываем меню в зависимости от его текущего состояния
    if (profileMenu.style.display === 'none') {
        profileMenu.style.display = 'flex';
        // Позиционируем меню под изображением профиля
        profileMenu.style.position = 'absolute';
        profileMenu.style.top = `${profileImage.offsetTop + profileImage.offsetHeight}px`;
        profileMenu.style.left = `${profileImage.offsetLeft + profileImage.offsetWidth - profileMenu.offsetWidth}px`;
        profileImage.src = "https://cdn.builder.io/api/v1/image/assets/TEMP/fdd13ab66a22a69d05b79b34424d250054630366692b0c6ba878f9f386f85421?apiKey=34d7d013791846f1943a6733fbd2383a&";
    } else {
        profileMenu.style.display = 'none';
        profileImage.src = "https://cdn.builder.io/api/v1/image/assets/TEMP/2bd64e9a6fa98f01ccec64176921fa8fdda4e581d0686a57ca63d853209ef8e5?apiKey=34d7d013791846f1943a6733fbd2383a&";
    }
}

// Обработчик события клика по cabinet-item
cabinetItems.forEach(item => {
    item.addEventListener('click', function() {
        // Вызываем функцию для показа и скрытия меню
        toggleProfileMenu();
    });
});

// Обработчик события клика по изображению профиля
profileImage.addEventListener('click', function() {
    // Вызываем функцию для показа и скрытия меню
    toggleProfileMenu();
});

// Обработчик события mouseleave для personal-cabinet
personalCabinet.addEventListener('mouseleave', function() {
    // Скрываем меню с плавной анимацией
    profileMenu.style.opacity = 0;
    setTimeout(() => {
        profileMenu.style.display = 'none';
        profileMenu.style.opacity = 1; // Возвращаем opacity обратно для последующих показов
    }, 300); // Задержка должна быть такой же, как в CSS transition
    // Изменяем src изображения профиля на первоначальный
    profileImage.src = "https://cdn.builder.io/api/v1/image/assets/TEMP/2bd64e9a6fa98f01ccec64176921fa8fdda4e581d0686a57ca63d853209ef8e5?apiKey=34d7d013791846f1943a6733fbd2383a&";
});