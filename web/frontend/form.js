document.getElementById("custom-slider").addEventListener("input", function (event){
    let value = event.target.value;
    document.getElementById("current-value").innerText=value;
    document.getElementById("current-value").style.left=`${(value / 10) *100}%`;

});
function handleSelectColorChange(selectElement) {
    if (selectElement.value === '') {
        selectElement.style.color = '#999';
    } else {
        selectElement.style.color = '#333';
    }
}
