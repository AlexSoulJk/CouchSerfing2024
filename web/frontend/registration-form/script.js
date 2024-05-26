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
// document.addEventListener('DOMContentLoaded', function() {
//     const groups = document.querySelectorAll('[data-group]');
//
//     groups.forEach(function(group) {
//         const groupId = group.getAttribute('data-group');
//         const choiceSelect = group.querySelector(`[data-choice="${groupId}"]`);
//         const otherInput = group.querySelector(`[data-other-input="${groupId}"]`);
//
//         choiceSelect.addEventListener('change', function() {
//             // Получаем индекс последнего элемента в списке опций
//             const lastIndex = choiceSelect.options.length - 1;
//             // Проверяем, выбран ли последний элемент или нет
//             const isLastOptionSelected = choiceSelect.selectedIndex === lastIndex;
//
//             if (isLastOptionSelected) {
//                 otherInput.style.display = 'block';
//                 otherInput.focus();
//             } else {
//                 otherInput.style.display = 'none';
//             }
//         });
//     });
// });

const selectElements = document.querySelectorAll('[data-choice]');

// Добавляем обработчик для проверки состояния развертывания вариантов выбора
selectElements.forEach(function(selectElement) {
    selectElement.addEventListener('click', function() {
        // Проверяем, в фокусе ли поле
        if (document.activeElement === this) {
            selectElement.classList.toggle('focused');
        } else {
            selectElement.classList.remove('focused');
        }
    });
});

// Добавляем обработчик события для клика вне поля выбора
document.addEventListener('click', function(event) {
    // Проверяем, был ли клик вне полей выбора
    selectElements.forEach(function(selectElement) {
        if (!selectElement.contains(event.target)) {
            // Удаляем класс focused
            selectElement.classList.remove('focused');
        }
    });
});

// Добавляем обработчик события для изменения значения в поле выбора
selectElements.forEach(function(selectElement) {
    selectElement.addEventListener('change', function() {
        // Удаляем фокус с поля выбора
        this.blur();
    });
});



document.addEventListener('DOMContentLoaded', function() {
    const groups = document.querySelectorAll('[data-group]');

    groups.forEach(function(group) {
        const groupId = group.getAttribute('data-group');
        const choiceSelect = group.querySelector(`[data-choice="${groupId}"]`);
        const otherInput = group.querySelector(`[data-other-input="${groupId}"]`);

        choiceSelect.addEventListener('change', function() {
            if (choiceSelect.value === 'other') {
                otherInput.style.display = 'block';
                otherInput.focus();
            } else {
                otherInput.style.display = 'none';
            }
        });
    });
});


let backendData = null;
// Запрос на ПОЛУЧЕНИЕ ДАННЫХ С СЕРВЕРА
fetch('http://127.0.0.1:8000/main/registration_form/fields', {
    method: 'GET',
    headers: {
        'Content-Type': 'application/json'
    },
})
    .then(response => response.json())
    .then(data => {
        const reversedData = data.reverse();
        console.log(reversedData);
        backendData = data;
        data.forEach((item, index) => { // Используем порядковый номер
            const groupNumber = index + 1; // Порядковый номер
            const questionDescription = item.question.description;
            const answers = item.answers;

            const groupElement = document.querySelector(`.personal-form-group[data-group="${groupNumber}"]`);
            if (groupElement) {
                const labelElement = groupElement.querySelector('label');
                labelElement.textContent = questionDescription;

                const selectElement = groupElement.querySelector('select');

                answers.forEach(answer => {
                    const optionElement = document.createElement('option');
                    optionElement.value = answer.id;
                    optionElement.textContent = answer.description;
                    selectElement.appendChild(optionElement);
                });

                const otherOptionElement = document.createElement('option');
                otherOptionElement.value = 'other';
                otherOptionElement.textContent = 'Другое';
                selectElement.appendChild(otherOptionElement);
            }
        });
    })
    .catch(error => {
        // Обработка ошибок
        console.error('Error:', error);
    });







//БЭК
// document.getElementById('registration-form').addEventListener('submit', function(event) {
//     event.preventDefault(); // Отменяем стандартное поведение отправки формы
//
//     const formData = new FormData(this);
//
//     let jsonData = {};
//
//     // Добавляем обязательные поля
//     jsonData['is_active'] = true;
//     jsonData['is_superuser'] = false;
//     jsonData['is_verified'] = false;
//
//     // Перебираем содержимое объекта FormData и добавляем его в объект JSON
//     for (const [key, value] of formData.entries()) {
//         jsonData[key] = value;
//     }
//
//     // Преобразуем объект JSON в строку
//     const jsonString = JSON.stringify(jsonData);
//
//     console.log(jsonString)
//
//     fetch('http://127.0.0.1:8000/main/auth/register', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: jsonString
//     })
//         .then(response => {
//             if (!response.ok) {
//                 throw new Error('Network response was not ok');
//             }
//             // Проверяем статус ответа
//             if (response.status === 400) {
//                 // Если статус ответа 400 (Bad Request), выбрасываем ошибку с текстом из тела ответа
//                 return response.json().then(data => {
//                     throw new Error(data.detail);
//                 });
//             }
//             return response.json();
//         })
//         .then(data => {
//             console.log('Success:', data);
//             window.location.href = '/CouchSerfing2024/web/frontend/main-page/index.html';
//         })
//         .catch(error => {
//             console.error('Error:', error);
//             showErrorModal('Пользователь с таким email уже существует.');
//         });
// });


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



//валидация пароля
document.getElementById('registration-form').addEventListener('submit', function(event) {
    event.preventDefault();  // Предотвращаем отправку формы

    const password = document.getElementById('password').value;
    const repeatPassword = document.getElementById('repeat-password').value;
    const errorMessage = document.getElementById('error-message');
    const consentCheckbox = document.getElementById('consent-checkbox');
    let formIsValid = true;

    // Проверка совпадения паролей
    if (password !== repeatPassword) {
        showErrorModal('Пароли не совпали');
        formIsValid = false;

        // Сброс значений полей пароля и установка новых плейсхолдеров
        const passwordField = document.getElementById('password');
        const repeatPasswordField = document.getElementById('repeat-password');

        passwordField.value = '';
        repeatPasswordField.value = '';

        // Установка новых плейсхолдеров
        passwordField.placeholder = 'Попробуйте ещё';
        repeatPasswordField.placeholder = 'И ещё';

        // Перенаправление фокуса на первое поле пароля
        passwordField.focus();

        // Сброс состояния чекбокса
        consentCheckbox.checked = false;
    } else {
        errorMessage.style.display = 'none';
    }

    // Если пароли не совпадают, прекращаем дальнейшую обработку
    if (!formIsValid) {
        return;
    }

    // Если все проверки пройдены, выполняем дальнейшие действия
    processForm();
});

function processForm() {
    const registrationForm = document.getElementById('registration-form');
    const loginForm = document.getElementById('login-form');
    const groups = document.querySelectorAll('[data-group]');

    const formData = new FormData(registrationForm);

    let jsonData = {};

    jsonData['is_active'] = true;
    jsonData['is_superuser'] = false;
    jsonData['is_verified'] = false;

    for (const [key, value] of formData.entries()) {
        jsonData[key] = value;
    }

    const jsonString = JSON.stringify(jsonData);

    console.log(jsonString);

    // Регистрируем пользователя
    fetch('http://127.0.0.1:8000/main/auth/register', {
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
            return response.json();
        })
        .then(data => {
            // После успешной регистрации авторизуем пользователя
            const loginFormData = new FormData();
            loginFormData.append('grant_type', 'password');
            loginFormData.append('username', formData.get('email')); // Используем email в качестве имени пользователя
            loginFormData.append('password', formData.get('password'));

            fetch('http://127.0.0.1:8000/main/auth/login', {
                method: 'POST',
                body: loginFormData
            })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    localStorage.setItem('token', data.access_token); // Сохраняем токен в localStorage
                    console.log(localStorage.getItem('token'));
                    // Отправляем данные на /main/registration_form/${isWithRule}
                    groups.forEach(function(group) {
                        const groupId = group.getAttribute('data-group');
                        const choiceSelect = group.querySelector(`[data-choice="${groupId}"]`);
                        const selectedValue = choiceSelect.value;
                        const groupIndex = parseInt(groupId) - 1; // Преобразуем groupId в индекс массива
                        const dataItem = backendData[groupIndex]; // Получаем объект данных по индексу
                        const isWithRule = dataItem.is_with_rule; // Получаем значение is_with_rule из объекта данных
                        console.log(isWithRule);
                        if (selectedValue && selectedValue !== 'other') {
                            const formData = {
                                answer_id: parseInt(selectedValue)
                            };

                            sendFormData(formData, isWithRule);

                        } else if (selectedValue === 'other') {
                            const otherValue = group.querySelector(`[data-other-input="${groupId}"]`).value;
                            console.log('Other value entered:', otherValue);
                            // Здесь можно сделать отдельный POST запрос для сохранения этого значения, если необходимо
                        }
                    });

                    window.location.href = '/CouchSerfing2024/web/frontend/main-page/index.html'; // Перенаправляем пользователя на главную страницу
                })
                .catch(error => {
                    console.error('Error:', error);
                    // Обработка ошибки авторизации
                });
        })
        .catch(error => {
            console.error('Error:', error);
            alert("А вы ведь уже зарегистрированы!");
        });
}

// Функция для отправки данных на бэкэнд
function sendFormData(formData, isWithRule) {
    console.log(JSON.stringify([formData]));

    fetch(`http://127.0.0.1:8000/main/registration_form/${isWithRule}`, {
        method: 'POST',
        headers: {
            'Authorization': `Bearer ${localStorage.getItem('token')}`,
            'Content-Type': 'application/json',
            'Access-Control-Allow-Credentials': 'true',
            'Access-Control-Allow-Origin': 'http://localhost:63343'
        },
        body: JSON.stringify([formData])
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log(`Response from backend for is_with_rule=${isWithRule}:`, data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
}
