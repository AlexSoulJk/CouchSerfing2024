const searchInput = document.querySelector('.search-container');
const searchButton = document.querySelector('.search-button');

searchButton.addEventListener('click', function() {
    const searchTerm = searchInput.value.trim();

    if (searchTerm !== '') {
        console.log('Вы ищете: ' + searchTerm);
    } else {
        alert('Пожалуйста, введите поисковый запрос.');
    }
});

searchInput.addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        searchButton.click();
    }
});


//Переходер
function redirectToPage(url) {
    window.location.href = url;
}


//Прокруточка
function scrollToSection(sectionId) {
    const section = document.getElementById(sectionId);
    if (section) {
        // Вычисляем вертикальное смещение секции относительно верхнего края документа
        const offsetTop = section.offsetTop + 6;
        // Прокручиваем страницу к этой секции
        window.scrollTo({
            top: offsetTop,
            behavior: "smooth" // Добавляем плавную прокрутку
        });
    }
}


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