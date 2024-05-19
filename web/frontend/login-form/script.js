document.getElementById("login-form").addEventListener("submit", function(event){
    event.preventDefault();
    const username = document.getElementById("username-login").value;
    const password = document.getElementById("password-login").value;

    console.log("Username: " + username + ", Password: " + password);

    document.getElementById("login-container").style.display = "none";
});

//ШАРИКИ
// Получаем элементы полей ввода пароля
const passwordInputLogin = document.getElementById('password-login');

// Добавляем обработчик события для поля ввода пароля
passwordInputLogin.addEventListener('input', function() {
    // Если поле не пустое, добавляем класс
    if (passwordInputLogin.value !== '') {
        passwordInputLogin.classList.add('password-filled');
    } else {
        passwordInputLogin.classList.remove('password-filled');
    }
});