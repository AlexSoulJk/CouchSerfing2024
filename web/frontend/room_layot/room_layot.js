function showOnMap() {
    const coordinates = document.getElementById("coordinates").textContent;
    const [lat, lng] = coordinates.split(",");
    const newCoordinates = `${lng}, ${lat}`;
    const mapLink = `https://yandex.ru/maps/?ll=${newCoordinates}&z=18&l=map&pt=${newCoordinates},pm2rdl` ;
    window.open(mapLink, "_blank");
}
document.querySelector('.menu-button').addEventListener('click', function() {
  var dropdownMenu = document.querySelector('.dropdown-menu');
  if (dropdownMenu.style.display === 'none') {
      dropdownMenu.style.display = 'block';
  } else {
      dropdownMenu.style.display = 'none';
  }
});
$('.slide-show').slick({
  slidesToShow: 1,
  slidesToScroll: 1,
  asNavFor: '.slider-nav',
  prevArrow: "<img src='prev (1).svg' class='prev slick-arrow' style='width:40px' alt='1'>",
  nextArrow: "<img src='prev (2).svg' class='next slick-arrow' style='width:40px' alt='2'>",
});
$('.slider-nav').slick({
  slidesToScroll: 1,
  asNavFor: '.slide-show',
  dots: false,
  centerMode: true,
  focusOnSelect: true,
  responsive: [
    {
      breakpoint: 2000,
      settings: {
        slidesToShow: 5,
        arrows:false,
      }
    },
    {
      breakpoint: 1200,
      settings: {
        slidesToShow: 4,
        arrows:false,
      }
    },
    {
      breakpoint: 998,
      settings: {
        slidesToShow: 3,
        arrows:false,
      }
    },
    {
      breakpoint: 700,
      settings: {
        slidesToShow: 2,
        arrows:false,
      }
    }


  ]
 
});

//Обработка рейтинга отзывов

const cleanProgress = document.getElementById("clean-progress");

const placeProgress = document.getElementById("place-progress");

const expectationProgress = document.getElementById("expectation-progress");

const priceProgress = document.getElementById("price-progress");

function updateProgressBar(progress, percentage) {
  // Обновите ширину полосы
  progress.style.width = `${percentage * 10}%`;

  // Обновите отображаемый процент
  percentage.innerHTML = `${percentage}%`;
}

let cleanDataValue = document.getElementById("clean-value")
let placeDataValue = document.getElementById("place-value")
let progressDataValue = document.getElementById("expectation-value")
let priceDataValue = document.getElementById("price-value")

updateProgressBar(cleanProgress, parseFloat(cleanDataValue.innerText));
updateProgressBar(placeProgress, parseFloat(placeDataValue.innerText));
updateProgressBar(expectationProgress, parseFloat(progressDataValue.innerText));
updateProgressBar(priceProgress, parseFloat(priceDataValue.innerText));


 