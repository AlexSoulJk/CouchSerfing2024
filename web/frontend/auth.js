// Функция для проверки авторизации пользователя
function checkAuthorization() {
    // Получаем токен из локального хранилища
    const token = localStorage.getItem('token');
    // Если токен есть, значит пользователь авторизован
    if (token) {
        // Показываем ссылку "LOG OUT"
        document.getElementById("logout-link").style.display = "block";
        // Прячем ссылку "LOG IN"
        document.getElementById("login-link").style.display = "none";
    } else {
        // Прячем ссылку "LOG OUT"
        document.getElementById("logout-link").style.display = "none";
        // Показываем ссылку "LOG IN"
        document.getElementById("login-link").style.display = "block";
    }
}

// Вызываем функцию для проверки авторизации при загрузке страницы
checkAuthorization();

// Обработчик события клика на ссылке "LOG OUT"
document.getElementById("logout-link").addEventListener("click", function(event) {
    event.preventDefault();
    // Вызываем функцию для выхода из системы
    logout();
});

// Функция для выхода из системы
function logout() {

    const token = localStorage.getItem('token');
    // Удаляем токен из локального хранилища
    localStorage.removeItem('token');

    // Отправляем запрос на сервер для выхода из системы
    fetch('http://127.0.0.1:8000/main/auth/logout', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}` // Включаем токен в заголовок запроса
        },
        body: JSON.stringify({}) // Может быть какая-то информация о пользователе, если требуется
    })
        .then(response => {
            if (response.ok) {
                // Проверяем авторизацию после удаления токена
                checkAuthorization();
            } else {
                // Обработка ошибки, если не удалось выйти из системы
                console.error('Failed to logout');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}




//АВТОРИЗАЦИЯ
const loginModal = document.getElementById('login-modal');
const submitAction = document.getElementById('submit-login');

// по submit
submitAction.onclick = function() {
    loginModal.style.display = 'none';
};

// опять же нажатие на поле вне окна
window.onclick = function(event) {
    if (event.target === loginModal) {
        loginModal.style.display = 'none';
    }
};

function showLogin() {
    loginModal.style.display = 'block';
}

//AUTH
document.getElementById("login-form").addEventListener("submit", function(event){
    event.preventDefault(); // Prevent form submission

    const formData = new FormData();
    formData.append('grant_type', 'password');
    formData.append('username', document.getElementById("username-login").value);
    formData.append('password', document.getElementById("password-login").value);

    fetch('http://127.0.0.1:8000/main/auth/login', {
        method: 'POST',
        body: formData,
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Save JWT token in localStorage
            localStorage.setItem('token', data.access_token);
            // Redirect to main page
            window.location.href = '/CouchSerfing2024/web/frontend/main-page/index.html';
        })
        .catch(error => {
            console.error('Error:', error);
            // Handle error, e.g., display error message to the user
        });
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


//НЕ ХОЧУ ДОПУСКАТЬ ПЕРЕХОД НА СТРАНИЦУ РЕГИСТРАЦИИ АВТОРИЗОВАННЫМ ПОЛЬЗОВАТЕЛЯМ
// Обработчик клика на кнопку для перехода на страницу регистрации
document.getElementById("registration-button").addEventListener("click", function(event) {
    // Получаем токен из локального хранилища
    const token = localStorage.getItem('token');
    // Если токен есть, значит пользователь авторизован
    if (token) {
        // Предотвращаем переход на страницу регистрации
        event.preventDefault();
        // Выводим сообщение о том, что пользователь уже авторизован
        alert("А вы ведь уже зарегистрированы!");
        // Если нужно, можно выполнить другие действия, например, перенаправить на другую страницу
        // window.location.href = '/another-page.html';
    } else {
        redirectToPage('/CouchSerfing2024/web/frontend/registration-form/index.html');
    }
});