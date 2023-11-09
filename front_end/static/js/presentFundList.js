// progressbar 진행상황
document.addEventListener("DOMContentLoaded", function() {
  for(let i = 1; i<=4; i++) {
    let price = parseInt(document.querySelector(`.totalMoney${i}`).textContent);
    console.log(price);
    let currentMoney = parseInt(document.querySelector(`.currentMoney${i}`).textContent);
    let progress = (currentMoney / price) * 100;
    let currentProgress = document.querySelector(`.bar${i}`);
    currentProgress.style.width = progress + "%";
    currentProgress.setAttribute("aria-valuenow", progress);
    let currentPercent = document.querySelector(`.percent${i}`);
    currentPercent.innerText = Math.round(progress);
  }
});
