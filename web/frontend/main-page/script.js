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



