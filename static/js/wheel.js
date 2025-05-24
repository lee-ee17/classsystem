// script.js
document.addEventListener("DOMContentLoaded", function () {
   

document.getElementById('spinBtn').addEventListener('click', function() {
    const wheel = document.getElementById('spinner');
    const randomDegree = Math.floor(Math.random() * 360) + 3600; // 隨機數值，最少轉 10 圈
    wheel.style.transition = 'transform 4s ease-out';
    wheel.style.transform = `rotate(${randomDegree}deg)`;
});
});
