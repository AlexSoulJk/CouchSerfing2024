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
