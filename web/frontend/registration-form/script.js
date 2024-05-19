// document.getElementById("custom-slider").addEventListener("input", function (event){
//     let value = event.target.value;
//     document.getElementById("current-value").innerText=value;
//     document.getElementById("current-value").style.left=`${(value / 10.9) *100}%`;
// });
// function handleSelectColorChange(selectElement) {
//     if (selectElement.value === '') {
//         selectElement.style.color = '#999';
//     } else {
//         selectElement.style.color = '#333';
//     }
// }
//
// document.querySelector('.menu-button').addEventListener('click', function() {
//     var dropdownMenu = document.querySelector('.dropdown-menu');
//     if (dropdownMenu.style.display === 'none') {
//         dropdownMenu.style.display = 'block';
//     } else {
//         dropdownMenu.style.display = 'none';
//     }
// });

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


//ШАРИКИ
// Получаем элементы полей ввода пароля
const passwordInput = document.getElementById('password');
const repeatPasswordInput = document.getElementById('repeat-password');

// Добавляем обработчик события для поля ввода пароля
passwordInput.addEventListener('input', function() {
    // Если поле не пустое, добавляем класс
    if (passwordInput.value !== '') {
        passwordInput.classList.add('password-filled');
    } else {
        passwordInput.classList.remove('password-filled');
    }
});

// Добавляем обработчик события для поля повторного ввода пароля
repeatPasswordInput.addEventListener('input', function() {
    // Если поле не пустое, добавляем класс
    if (repeatPasswordInput.value !== '') {
        repeatPasswordInput.classList.add('password-filled');
    } else {
        repeatPasswordInput.classList.remove('password-filled');
    }
});


//IMBA_SLIDER
const rangeThumb = document.getElementById('range-thumb'),
    rangeNumber = document.getElementById('range-number'),
    rangeLine = document.getElementById('range-line'),
    rangeInput = document.getElementById('range-input')

const rangeInputSlider = () =>{

    // Insert the value of the input range
    rangeNumber.textContent = rangeInput.value

    // Calculate the position of the input thumb
    // rangeInput.value = 50, rangeInput.max = 100, (50 / 100 = 0.5)
    // rangeInput.offsetWidth = 248, rangeThumb.offsetWidth = 32, (248 - 32 = 216)
    const thumbPosition = (rangeInput.value / (rangeInput.max - 0.11)),
        space = rangeInput.offsetWidth - rangeThumb.offsetWidth

    // We insert the position of the input thumb
    // thumbPosition = 0.5, space = 216 (0.5 * 216 = 108)
    rangeThumb.style.left = (thumbPosition * space) + 'px'

    // We insert the width to the slider with the value of the input value
    // rangeInput.value = 50, ancho = 50%
    rangeLine.style.width = rangeInput.value + '%'

    // We call the range input
    rangeInput.addEventListener('input', rangeInputSlider)
}

rangeInputSlider()


//МНОГО НАСТРОЕК ДЛЯ ПОЛЯ ВЫБОРА
document.addEventListener('DOMContentLoaded', function() {
    const choiceSelect = document.getElementById('choice');
    const otherInput = document.getElementById('otherInput');

    choiceSelect.addEventListener('change', function() {
        if (choiceSelect.value === 'other') {
            otherInput.style.display = 'block';
            otherInput.focus();
        } else {
            otherInput.style.display = 'none';
        }
    });
});


const selectElement = document.getElementById('choice');

// Добавляем обработчик для проверки состояния развертывания вариантов выбора
selectElement.addEventListener('click', function() {
    // Проверяем, в фокусе ли поле
    if (document.activeElement === this) {
        selectElement.classList.toggle('focused');
    } else {
        selectElement.classList.remove('focused');
    }
});

// Добавляем обработчик события для клика вне поля выбора
document.addEventListener('click', function(event) {
    // Проверяем, был ли клик вне поля выбора
    if (!selectElement.contains(event.target)) {
        // Удаляем класс focused
        selectElement.classList.remove('focused');
    }
});

// Добавляем обработчик события для изменения значения в поле выбора
selectElement.addEventListener('change', function() {
    // Удаляем фокус с поля выбора
    this.blur();
});



//БЭК
document.getElementById('registration-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Отменяем стандартное поведение отправки формы

    const formData = new FormData(this);

    let jsonData = {};

    // Добавляем обязательные поля
    jsonData['is_active'] = true;
    jsonData['is_superuser'] = false;
    jsonData['is_verified'] = false;

    // Перебираем содержимое объекта FormData и добавляем его в объект JSON
    for (const [key, value] of formData.entries()) {
        jsonData[key] = value;
    }

    // Преобразуем объект JSON в строку
    const jsonString = JSON.stringify(jsonData);

    console.log(jsonString);

    fetch('http://127.0.0.1:8000/auth/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: jsonString
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            // Проверяем статус ответа
            if (response.status === 400) {
                // Если статус ответа 400 (Bad Request), выбрасываем ошибку с текстом из тела ответа
                return response.json().then(data => {
                    throw new Error(data.detail);
                });
            }
            return response.json();
        })
        .then(data => {
            console.log('Success:', data);
            window.location.href = '/CouchSerfing2024/web/frontend/main-page/index.html';
        })
        .catch(error => {
            console.error('Error:', error);
            showErrorModal('Пользователь с таким email уже существует.');
        });
});


//ERROR 200
// Найти модальное окно и кнопку для закрытия
const modal = document.getElementById('error-modal');
const span = document.getElementsByClassName('close')[0];

// Когда пользователь нажимает на крестик, закрываем модальное окно
span.onclick = function() {
    modal.style.display = 'none';
};

// Функция для отображения модального окна с сообщением об ошибке
function showErrorModal(message) {
    const errorMessage = document.getElementById('error-message');
    errorMessage.innerText = message;
    modal.style.display = 'block';
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