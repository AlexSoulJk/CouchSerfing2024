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
